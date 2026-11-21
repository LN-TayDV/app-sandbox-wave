#!/usr/bin/env python3
"""ingest_book.py — L0: PDF goc -> ban ghi cap trang (text, trang in, anh, bbox).

Nguyen tac bat buoc:
  * Tat ca file doc/ghi dung encoding="utf-8". KHONG su dung errors="ignore"
    hoac errors="replace" de che het ma ky tu loi.
  * Raw text lay tu page.get_text("text") va bo nguyen nguyen (nguon thuc te).
  * Toan luu vi tri/co ban dich so dung page.get_text("dict") (span co bbox,
    font, origin). Che do "rawdict"/"blocks" loai vi tri -> KHONG dung (toi hoac
    voi cong thuc toan hoc: chi so tren/duoi o span rieng, baseline lech).
  * printed_page xac minh tu header/footer. Trang khong co by chung trang in
    duoc danh UNKNOWN (null), KHONG bao gio lap so trang ao.
  * Trang chi anh (image_page) duoc luu ban ghi, khong coi la mat trang.
  * Chay lai cung nguon PDF -> xuat ra cung ket qua (deterministic), ghi de,
    khong them/trung ban ghi.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import pymupdf  # PyMuPDF

ROOT = Path(r"C:\Users\PC\Documents\AI_project\sandbox-financial")
DATA_BOOK = ROOT / "data" / "book"
THEORY = ROOT / "theory"
LOG_DIR = THEORY / "logs"
REGISTRY = THEORY / "registry" / "books.yaml"

HEADER_BAND = 0.10   # ty le chieu cao trang o dau
FOOTER_BAND = 0.90   # ty le chieu cao trang o cuoi
IMAGE_CHAR_THRESHOLD = 150      # ky tu thoi gian duong toi co the xet trang anh
IMAGE_AREA_RATIO = 0.70         # anh bao >70% dien tich trang -> nghia la trang anh toan trang
HEADING_SIZE_THRESHOLD = 11.5   # tham chuan kich thuoc chu de L1 phat hien dau muc

KY_TU_TOAN_HOC = set(
    "∫∑∏=≠≤≥≈∂√±×÷∞∘→←↔⊂⊆∈∀∃αβγδεθλμνπρσφψωΔΓΛΣΦΨΩ"
)

# Fallback neu books.yaml chua co (chi duoc su dung khi manifest chua tao).
FALLBACK_PDFS = {
    "HAN": "econometrics-bruce-hansen-2014.pdf",
    "ROM": "b81821bd16a42211f919748c26cd0774.pdf",
    "PIN": ("Robert S Pindyck_ Daniel L Rubinfeld - Microeconomics, Global "
            "Edition (2017, Pearson Education Limited) - libgen.li.pdf"),
    "MAD": "international-financial-management-11th-edition-by-jeff-madura.pdf",
}


def _utf8_stdout() -> None:
    """Ep stdout ve UTF-8 strict neu console ho tro. Neu khong ho tro, bo mac
    dinh va de cac ham in an toan xu ly loi (khong su dung errors="replace")."""
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="strict")
        except Exception:
            pass


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def load_book_pdf(code: str) -> tuple[str, str]:
    """Tra ve (ten_file, duong_dan_relative). Lay tu books.yaml neu co, nguoc
    lai dung FALLBACK_PDFS va canh bao."""
    if REGISTRY.exists():
        import yaml
        with open(REGISTRY, encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        entry = (data.get("books") or {}).get(code)
        if entry and entry.get("pdf_path"):
            return entry["pdf_path"], entry.get("file", Path(entry["pdf_path"]).name)
    if code in FALLBACK_PDFS:
        return FALLBACK_PDFS[code], FALLBACK_PDFS[code]
    raise KeyError(f"Khong tim thong tin PDF cho ma sach '{code}' trong {REGISTRY}")


def _iter_text_lines(page):
    """Danh sach (line_bbox, [span]) theo thu doc cua PyMuPDF; chi lay block
    van ban (type 0), bo dong chi co khoang trang."""
    out = []
    for block in page.get_text("dict")["blocks"]:
        if block.get("type") != 0:
            continue
        for line in block["lines"]:
            spans = line["spans"]
            if not any(s["text"].strip() for s in spans):
                continue
            out.append((line["bbox"], spans))
    return out


def page_candidates(page) -> list[dict]:
    """Cac so nguyen o vung header/footer kha bieu dien so trang in, kèm vi tri."""
    h = page.rect.height
    w = page.rect.width
    cands = []
    for bbox, spans in _iter_text_lines(page):
        y0, y1 = bbox[1], bbox[3]
        in_header = y0 < h * HEADER_BAND
        in_footer = y1 > h * FOOTER_BAND
        if not (in_header or in_footer):
            continue
        for s in spans:
            txt = s["text"].strip()
            if not re.fullmatch(r"\d{1,4}", txt):
                continue
            sx0, _, sx1, _ = s["bbox"]
            cands.append({
                "value": int(txt),
                "source": "header_span" if in_header else "footer_span",
                "right_gap": round(w - sx1, 1),
                "left_gap": round(sx0, 1),
                "size": round(s["size"], 1),
            })
    return cands


def resolve_printed_pages(all_cands: list[list[dict]], n_pages: int):
    """Chon so trang in dung bang rang chuoi 1:1 giua trang PDF va trang in.

    Ket qua: danh sach (printed_page:int|None, status:str, source:str)
    co status trong {VERIFIED, INFERRED, UNKNOWN}.
    """
    n = n_pages
    # dp[(p,i)] = (do_dai_chuai, so_khop_1toi, khoa_truoc)
    dp = {}
    for p in range(n):
        for i, c in enumerate(all_cands[p]):
            best_len, best_match, best_prev = 1, 0, None
            for q in range(max(0, p - 60), p):
                for j, cq in enumerate(all_cands[q]):
                    d_v = c["value"] - cq["value"]
                    d_p = p - q
                    if d_v <= 0 or d_v > d_p:
                        continue
                    ln, mt, _ = dp[(q, j)]
                    cand_len, cand_match = ln + 1, mt + (1 if d_v == d_p else 0)
                    if (cand_len, cand_match) > (best_len, best_match):
                        best_len, best_match, best_prev = cand_len, cand_match, (q, j)
            dp[(p, i)] = (best_len, best_match, best_prev)

    out = [(None, "UNKNOWN", "none")] * n
    if not dp:
        return out

    best_key = max(dp, key=lambda k: (dp[k][0], dp[k][1]))
    path = []
    k = best_key
    while k is not None:
        path.append(k)
        k = dp[k][2]
    path.reverse()

    chain = {p: all_cands[p][i]["value"] for p, i in path}
    chain_src = {}
    for p, i in path:
        c = all_cands[p][i]
        side = "right" if c["right_gap"] < c["left_gap"] else "left"
        chain_src[p] = f"{c['source']}_{side}"

    for p, v in chain.items():
        out[p] = (v, "VERIFIED", chain_src[p])

    # Trang ngoai chuoi: nghich qua offset hang so cua chuoi (INFERRED) neu co the.
    seq = [(p, v) for p, v in chain.items()]
    if seq:
        from collections import Counter
        offs = Counter((p + 1) - v for p, v in seq)
        dom_off, dom_n = offs.most_common(1)[0]
        if dom_n / len(seq) > 0.85:
            for p in range(n):
                if out[p][0] is not None:
                    continue
                cand = (p + 1) - dom_off
                if cand >= 1:
                    out[p] = (cand, "INFERRED", f"offset_inferred+{dom_off}")
    return out


def extract_lines(page):
    """Dong van ban co cau truc (text, size, bbox, is_heading, ...)."""
    h = page.rect.height
    out = []
    for bbox, spans in _iter_text_lines(page):
        txt = "".join(s["text"] for s in spans).strip()
        if not txt:
            continue
        size = round(max(s["size"] for s in spans), 1)
        out.append({
            "text": txt,
            "size": size,
            "bbox": [round(v, 1) for v in bbox],
            "is_heading": size >= HEADING_SIZE_THRESHOLD,
            "in_header": bbox[3] <= h * HEADER_BAND,
            "in_footer": bbox[1] >= h * FOOTER_BAND,
            "spans": [{
                "t": s["text"],
                "sz": round(s["size"], 1),
                "f": s["font"],
                "o": [round(v, 1) for v in s["origin"]],
                "b": [round(v, 1) for v in s["bbox"]],
            } for s in spans if s["text"].strip()],
        })
    return out


def extract_equation_bboxes(page):
    """BBOX cac dong chua ky tu toan hoc (heuristic, chi de dinh vi cong thuc)."""
    h = page.rect.height
    out = []
    for bbox, spans in _iter_text_lines(page):
        txt = "".join(s["text"] for s in spans)
        if not txt:
            continue
        if bbox[3] < h * HEADER_BAND or bbox[1] > h * FOOTER_BAND:
            continue
        if any(ch in KY_TU_TOAN_HOC for ch in txt):
            out.append([round(v, 1) for v in bbox])
    return out


def image_metadata(page):
    """Metadata anh nhung trang (xref, chieu rong/cao, bbox, mau, ...)."""
    infos = []
    try:
        for info in page.get_image_info():
            bbox = info["bbox"]
            area = (bbox[2] - bbox[0]) * (bbox[3] - bbox[1])
            page_area = page.rect.width * page.rect.height
            infos.append({
                "xref": info.get("xref"),
                "width": info.get("width"),
                "height": info.get("height"),
                "bbox": [round(v, 1) for v in bbox],
                "area_ratio": round(area / page_area, 4) if page_area else 0.0,
                "colorspace": info.get("colorspace"),
                "bits": info.get("bits"),
            })
    except Exception:
        pass
    return infos


def ingest(code: str) -> dict:
    rel_pdf, fname = load_book_pdf(code)
    pdf = ROOT / rel_pdf  # books.yaml luu duong dan 상대 so voi ROOT
    if not pdf.exists():
        raise FileNotFoundError(f"PDF khong ton tai: {pdf}")
    out_dir = THEORY / "books" / code
    out_dir.mkdir(parents=True, exist_ok=True)
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    doc = pymupdf.open(str(pdf))
    total = len(doc)

    # Pass 1: thu text, candidate trang in, anh, cong thuc, dong cau truc
    raw_texts, cands, imgs_meta, eq_boxes, lines_all = [], [], [], [], []
    for i in range(total):
        page = doc[i]
        raw_texts.append(page.get_text("text"))
        cands.append(page_candidates(page))
        imgs_meta.append(image_metadata(page))
        eq_boxes.append(extract_equation_bboxes(page))
        lines_all.append(extract_lines(page))

    # Pass 2: xac minh so trang in
    resolved = resolve_printed_pages(cands, total)

    # Xac dinh trang anh toan trang (du nguyen ly)
    image_flags = []
    for i in range(total):
        char_count = len(raw_texts[i])
        images = imgs_meta[i]
        max_area = max((im["area_ratio"] for im in images), default=0.0)
        full_page_image = bool(images) and max_area >= IMAGE_AREA_RATIO
        is_image = (char_count < IMAGE_CHAR_THRESHOLD) and full_page_image
        evidence = []
        if char_count < IMAGE_CHAR_THRESHOLD:
            evidence.append(f"text_ngan({char_count}ky_tu)")
        if images:
            evidence.append(f"anh({len(images)},toan_trang={full_page_image})")
        if full_page_image:
            evidence.append("anh_bao_nhieu_trang")
        image_flags.append({
            "image_page": is_image,
            "evidence": "; ".join(evidence) if evidence else "khong_co_by_chung_anh",
        })

    pages = []
    page_map = {}
    chunks = []
    warnings_log = []
    for i in range(total):
        text = raw_texts[i]
        images = imgs_meta[i]
        printed, status, source = resolved[i]
        img_flag = image_flags[i]
        char_count = len(text)
        page_eq_boxes = eq_boxes[i]
        page_warn = []

        if char_count == 0 and not images:
            page_warn.append("trang_trong_khong_co_text_khong_co_anh")
        if char_count < IMAGE_CHAR_THRESHOLD and not img_flag["image_page"]:
            page_warn.append(f"trang_it_text({char_count}ky_tu)")

        rec = {
            "book_code": code,
            "pdf_page": i + 1,
            "printed_page": printed,
            "printed_page_status": status,
            "printed_page_source": source,
            "text": text,
            "char_count": char_count,
            "lines": lines_all[i],
            "image_count": len(images),
            "images": images,
            "image_page": img_flag["image_page"],
            "image_page_evidence": img_flag["evidence"],
            "extraction_method": "pymupdf_get_text_text_plus_dict",
            "equation_bboxes": page_eq_boxes,
            "status": "OK",
            "warnings": page_warn,
        }
        pages.append(rec)
        page_map[str(i + 1)] = {
            "pdf_page": i + 1,
            "printed_page": printed,
            "printed_page_status": status,
            "source": source,
        }
        chunks.append({
            "chunk_id": f"{code}-p{i + 1:04d}",
            "global_id": f"{code}-p{i + 1:04d}",
            "book_code": code,
            "kind": None,              # L1 gan
            "pdf_page": i + 1,
            "pdf_page_end": i + 1,
            "printed_page": printed if printed is not None else "",
            "printed_page_end": printed if printed is not None else "",
            "printed_page_source": source,
            "heading_path": [],        # L1 xay dung
            "heading_level": 0,
            "heading_title": "",
            "text": text,
            "char_count": char_count,
            "image_count": len(images),
            "image_page": img_flag["image_page"],
            "equation_bboxes": page_eq_boxes,
        })
        if page_warn:
            warnings_log.append({"pdf_page": i + 1, "warnings": page_warn})

    doc.close()

    # Luu outputs (ghi de, deterministic, khong co thoi gian trong du lieu)
    (out_dir / "pages.jsonl").write_text(
        "".join(json.dumps(p, ensure_ascii=False) + "\n" for p in pages), encoding="utf-8")
    (out_dir / "page_map.json").write_text(
        json.dumps({"book_code": code, "total_pages": total, "pages": page_map},
                   ensure_ascii=False, indent=2), encoding="utf-8")
    (out_dir / "chunks.jsonl").write_text(
        "".join(json.dumps(c, ensure_ascii=False) + "\n" for c in chunks),
        encoding="utf-8")

    manifest = {
        "book_code": code,
        "pdf_path": rel_pdf,
        "pdf_abs_path": str(pdf),
        "sha256": sha256_file(pdf),
        "total_pages": total,
        "pages_with_text": sum(1 for p in pages if p["char_count"] > 0),
        "pages_empty": sum(1 for p in pages if p["char_count"] == 0),
        "image_pages": sum(1 for p in pages if p["image_page"]),
        "printed_pages_verified": sum(1 for p in pages if p["printed_page_status"] == "VERIFIED"),
        "printed_pages_inferred": sum(1 for p in pages if p["printed_page_status"] == "INFERRED"),
        "printed_pages_unknown": sum(1 for p in pages if p["printed_page_status"] == "UNKNOWN"),
        "pages_with_warnings": len(warnings_log),
        "extraction_method": "pymupdf_get_text_text_plus_dict",
    }
    (out_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    # Log chay (co thoi gian - phep phep cho log, khong anh huong du lieu)
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    log_path = LOG_DIR / f"ingest_{code}_{stamp}.log"
    log = {
        "book_code": code, "pdf": str(pdf), "sha256": manifest["sha256"],
        "total_pages": total, "utc": stamp, "manifest": manifest,
        "page_warnings": warnings_log[:50],
    }
    log_path.write_text(json.dumps(log, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps({"book": code, "status": "ingested", **manifest}, ensure_ascii=False))
    return manifest


def main() -> int:
    _utf8_stdout()
    ap = argparse.ArgumentParser(
        description="L0 ingest: PDF goc -> ban ghi cap trang + page_map + chunks (trang).")
    ap.add_argument("--book-code", dest="book_code",
                    help="ma sach: HAN | ROM | PIN | MAD")
    ap.add_argument("--book", dest="book_code_alias", help=argparse.SUPPRESS)
    ap.add_argument("--all", action="store_true", help="ingest tat ca 4 sach")
    args = ap.parse_args()

    codes = []
    if args.all:
        codes = ["HAN", "ROM", "PIN", "MAD"]
    elif args.book_code:
        codes = [args.book_code]
    elif args.book_code_alias:
        codes = [args.book_code_alias]
    else:
        ap.print_help()
        return 2

    rc = 0
    for code in codes:
        try:
            ingest(code)
        except Exception as exc:  # fatal -> ma thoat khac 0, khong crash traceback bo loi
            print(json.dumps({"book": code, "status": "FATAL", "error": str(exc)},
                             ensure_ascii=False))
            rc = 1
    return rc


if __name__ == "__main__":
    sys.exit(main())
