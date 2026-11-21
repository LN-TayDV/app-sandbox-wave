#!/usr/bin/env python3
"""segment_book.py — L1: cắt chunk theo muc (heading), gan kind, dung heading_path.

Nguyen tac:
  * Dua vao xuat cua L0 (theory/books/<CODE>/pages.jsonl + page_map.json), KHONG
    doc cua research/.
  * Cau truc dau muc tu PDF bookmarks (level 1-4) neu co; HAN khong co bookmarks
    nen phat hien bang kich thuoc font (body 9.2-11.0pt, dau muc >= 11.5pt).
  * Kind in {chapter, section, subsection, paragraph, figure, table, equation,
    exercise, example, box, front_matter, back_matter, image_page, blank_page,
    unresolved}. image_page va unresolved la loai bo sung (special coverage).
  * Moi chunk co book_code, pdf_page, printed_page (co the null), heading_path,
    text. ID deterministic (khong them chunk khi chay lai).
  * Buoc nay CHI xac dinh cau truc, KHONG trich dinh nghia, tom tat, suy luan cong thuc.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

import pymupdf  # PyMuPDF

ROOT = Path(r"C:\Users\PC\Documents\AI_project\sandbox-financial")
DATA_BOOK = ROOT / "data" / "book"
THEORY = ROOT / "theory"
LOG_DIR = THEORY / "logs"
BOOKS = ["HAN", "ROM", "PIN", "MAD"]
PDF_FILES = {
    "HAN": "econometrics-bruce-hansen-2014.pdf",
    "ROM": "b81821bd16a42211f919748c26cd0774.pdf",
    "PIN": ("Robert S Pindyck_ Daniel L Rubinfeld - Microeconomics, Global "
            "Edition (2017, Pearson Education Limited) - libgen.li.pdf"),
    "MAD": "international-financial-management-11th-edition-by-jeff-madura.pdf",
}

MAX_CHARS = 12_000  # gioi han kich thuoc chunk; qua lon se tach -a/-b

BLANK_RE = re.compile(r"this page intentionally left blank", re.I)
CHAPTER_RE = re.compile(r"^\s*(chapter\s+\d+|appendix\s+[A-Z0-9]+)\s*$", re.I)
SECTION_NUM_RE = re.compile(r"^\s*\d+(?:\.\d+)+\s*$")
FIG_RE = re.compile(r"\b(figure|fig\.)\s*\d", re.I)
TAB_RE = re.compile(r"\btable\s*\d", re.I)
EQ_RE = re.compile(r"\(\d+\.\d+\)\s*$")
EX_RE = re.compile(r"\b(exercise|problem)\b", re.I)
BOX_RE = re.compile(r"\b(box|sidebar|worked example|case study)\b", re.I)


def _utf8_stdout() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="strict")
        except Exception:
            pass


def load_toc(code: str) -> list[dict]:
    """Bookmarks PDF: level, title, page (1-based). Tra [] neu khong co."""
    path = DATA_BOOK / PDF_FILES[code]
    doc = pymupdf.open(str(path))
    toc = doc.get_toc()
    doc.close()
    out = []
    for lvl, title, page in toc:
        title = re.sub(r"[\x00-\x1f]+", " ", title).strip()
        title = re.sub(r"\s+", " ", title)
        out.append({"level": int(lvl), "title": title, "page": int(page)})
    return out


def build_toc_tree(toc: list[dict]) -> list[dict]:
    """Moi node bookmark co heading_path (duong dan tu goc den node)."""
    stack: list[tuple[int, str]] = []
    entries = []
    for e in toc:
        lvl = e["level"]
        while stack and stack[-1][0] >= lvl:
            stack.pop()
        path = [t for _, t in stack] + [e["title"]]
        stack.append((lvl, e["title"]))
        entries.append({
            "page": e["page"],
            "level": lvl,
            "title": e["title"],
            "path": list(path),
        })
    entries.sort(key=lambda x: (x["page"], x["level"]))
    return entries


def headings_from_font(pages: list[dict], code: str) -> list[dict]:
    """Phat hien dau muc bang kich thuoc font cho sach khong co bookmarks (HAN)."""
    if code != "HAN":
        return []
    entries = []
    pending = None
    for p in pages:
        for l in p["lines"]:
            if l["in_header"] or l["in_footer"]:
                continue
            txt = l["text"].strip()
            if not txt:
                continue
            sz = l["size"]
            if sz >= 24.0:
                if pending is not None and pending["page"] == p["pdf_page"]:
                    pending["title"] = (pending["title"] + " " + txt).strip()
                continue
            m = re.match(r"^(Chapter|Appendix)\s+([A-Z0-9]+)$", txt, re.I)
            if sz >= 20.0 and m:
                label = "Chapter" if m.group(1).lower() == "chapter" else "Appendix"
                pending = {"page": p["pdf_page"], "level": 1,
                           "title": f"{label} {m.group(2)}", "path": []}
                entries.append(pending)
                continue
            if sz >= 14.0:
                m2 = re.match(r"^(\d+\.\d+(?:\.\d+)?)$", txt)
                if m2:
                    entries.append({"page": p["pdf_page"], "level": 2,
                                    "title": m2.group(1), "path": []})
    stack: list[tuple[int, str]] = []
    for e in entries:
        while stack and stack[-1][0] >= e["level"]:
            stack.pop()
        e["path"] = [t for _, t in stack] + [e["title"]]
        stack.append((e["level"], e["title"]))
    return entries


def classify_kind(text, lines, pdf_page, printed, first_content, last_content,
                  heading) -> str:
    """Gan kind cho chunk."""
    t = text.strip()
    if not t:
        return "blank_page"
    if BLANK_RE.search(t[:200]):
        return "blank_page"

    # Trang anh toan trang -> image_page (duoc biet tu L0, o day kiem tra text it)
    if any(l.get("image_page") for l in lines):
        return "image_page"

    if pdf_page < first_content:
        return "front_matter"
    if pdf_page > last_content:
        return "back_matter"

    if heading:
        lvl = heading["level"]
        if lvl <= 1:
            return "chapter"
        if lvl == 2:
            return "section"
        return "subsection"

    head = "\n".join(l["text"] for l in lines[:3])
    if FIG_RE.search(head):
        return "figure"
    if TAB_RE.search(head):
        return "table"
    if BOX_RE.search(head):
        return "box"
    if EX_RE.search(head):
        return "exercise"
    if EQ_RE.search(t[-200:]):
        return "equation"
    return "paragraph"


def segment(code: str) -> dict:
    out_dir = THEORY / "books" / code
    pages_path = out_dir / "pages.jsonl"
    pmap_path = out_dir / "page_map.json"
    if not pages_path.exists():
        raise FileNotFoundError(f"L0 chua chay cho {code}: {pages_path} thieu")
    pages = [json.loads(l) for l in pages_path.read_text(encoding="utf-8").splitlines() if l.strip()]
    pmap = json.loads(pmap_path.read_text(encoding="utf-8")) if pmap_path.exists() else {}
    pmap_pages = pmap.get("pages", {})

    toc = load_toc(code)
    if toc:
        entries = build_toc_tree(toc)
    else:
        entries = headings_from_font(pages, code)

    # Khoang trang noi dung: tu chuong dau den trang cuoi cung co chuong
    chap_pages = [e["page"] for e in entries if CHAPTER_RE.match(e["title"])]
    first_content = min(chap_pages) if chap_pages else 1
    last_content = max(chap_pages) if chap_pages else len(pages)

    # current toc heading moi trang
    toc_by_page: dict[int, dict] = {}
    cur = None
    ei = 0
    for p in pages:
        pid = p["pdf_page"]
        while ei < len(entries) and entries[ei]["page"] <= pid:
            cur = entries[ei]
            ei += 1
        toc_by_page[pid] = cur

    # Tach tung trang thanh cac piece, moi piece gom 1 heading
    pieces = []
    for p in pages:
        pid = p["pdf_page"]
        printed = p.get("printed_page")
        body = [l for l in p["lines"] if not l["in_header"] and not l["in_footer"]]
        cur_heading = toc_by_page.get(pid)

        # dau muc trong trang (font-size lon, khong phai header/footer)
        cuts = [i for i, l in enumerate(body)
                if l["is_heading"] and l["size"] >= 12.0]

        if not cuts:
            text = "\n".join(l["text"] for l in body)
            pieces.append({
                "pdf_page": pid, "printed_page": printed,
                "heading": cur_heading, "text": text, "lead_heading": None,
            })
            continue

        if cuts[0] > 0:
            text = "\n".join(l["text"] for l in body[:cuts[0]])
            pieces.append({
                "pdf_page": pid, "printed_page": printed,
                "heading": cur_heading, "text": text, "lead_heading": None,
            })
        for ci, start in enumerate(cuts):
            end = cuts[ci + 1] if ci + 1 < len(cuts) else len(body)
            seg_lines = body[start:end]
            head_txt = " ".join(l["text"] for l in seg_lines[:2]).strip()
            heading = _make_heading(head_txt, cur_heading)
            pieces.append({
                "pdf_page": pid, "printed_page": printed,
                "heading": heading, "text": "\n".join(l["text"] for l in seg_lines),
                "lead_heading": head_txt,
            })

    # Gop cac piece lien cung heading_path thanh chunk, tach neu qua MAX_CHARS
    chunks = []
    part_counter: dict[tuple, int] = {}
    for pc in pieces:
        pid = pc["pdf_page"]
        src_page = next((x for x in pages if x["pdf_page"] == pid), None)
        printed_source = src_page.get("printed_page_source", "none") if src_page else "none"
        hp = tuple(pc["heading"]["path"]) if pc["heading"] else ()
        text_piece = pc["text"]
        if chunks:
            prev = chunks[-1]
            same = tuple(prev["heading_path"]) == hp
            fits = len(prev["text"]) + len(text_piece) + 1 <= MAX_CHARS
            if same and fits:
                prev["text"] = (prev["text"] + "\n" + text_piece).strip() \
                    if text_piece.strip() else prev["text"]
                prev["pdf_page_end"] = pc["pdf_page"]
                if pc["printed_page"] is not None:
                    prev["printed_page_end"] = pc["printed_page"]
                continue
            if same and not fits:
                part_counter[hp] = part_counter.get(hp, 0) + 1
        else:
            part_counter[hp] = 0
        suffix = "" if part_counter.get(hp, 0) == 0 else f"-{chr(96 + part_counter[hp])}"
        heading = pc["heading"]
        chunks.append({
            "chunk_id": f"{code}-c{len(chunks) + 1:05d}{suffix}",
            "global_id": f"{code}-c{len(chunks) + 1:05d}{suffix}",
            "book_code": code,
            "kind": None,
            "pdf_page": pc["pdf_page"],
            "pdf_page_end": pc["pdf_page"],
            "printed_page": pc["printed_page"] if pc["printed_page"] is not None else None,
            "printed_page_end": pc["printed_page"] if pc["printed_page"] is not None else None,
            "printed_page_source": printed_source,
            "text": text_piece,
            "char_count": len(text_piece),
            "kind_raw": None,
            "heading_path": list(hp),
            "heading_level": heading["level"] if heading else 0,
            "heading_title": heading["title"] if heading else "",
        })

    # Gan kind + attributes tu trang L0
    page_by_idx = {p["pdf_page"]: p for p in pages}
    for c in chunks:
        pg = page_by_idx[c["pdf_page"]]
        c["kind"] = classify_kind(
            c["text"], pg["lines"], c["pdf_page"], c["printed_page"],
            first_content, last_content,
            {"level": c["heading_level"], "title": c["heading_title"]}
            if c["heading_level"] else None)
        c["image_count"] = pg.get("image_count", 0)
        c["image_page"] = pg.get("image_page", False)
        c["equation_bboxes"] = pg.get("equation_bboxes", [])
        c["char_count"] = len(c["text"])
        c.pop("kind_raw", None)

    (out_dir / "chunks.jsonl").write_text(
        "".join(json.dumps(c, ensure_ascii=False) + "\n" for c in chunks),
        encoding="utf-8")

    # coverage.json
    coverage = _build_coverage(code, pages, chunks, entries, first_content, last_content)
    (out_dir / "coverage.json").write_text(
        json.dumps(coverage, ensure_ascii=False, indent=2), encoding="utf-8")

    LOG_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    (LOG_DIR / f"segment_{code}_{stamp}.log").write_text(
        json.dumps({"book": code, "coverage": coverage, "utc": stamp},
                   ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps({"book": code, "status": "segmented",
                      "total_pages": coverage["total_pages"],
                       "chunks": coverage["chunks_total"],
                      "image_pages": coverage["image_pages"],
                      "unresolved_pages": coverage["unresolved_pages"],
                      "pages_without_coverage": coverage["pages_without_coverage"]},
                     ensure_ascii=False))
    return coverage


def _make_heading(text: str, fallback: dict | None) -> dict:
    t = re.sub(r"\s+", " ", text).strip()
    if not t:
        return fallback or {"level": 2, "title": "", "path": []}
    if fallback:
        path = list(fallback["path"])
        if path and path[-1].lower().startswith(t[:6].lower()):
            path[-1] = t
            return {"level": fallback["level"], "title": t, "path": path}
        return {"level": fallback["level"], "title": t, "path": path + [t]}
    return {"level": 2, "title": t, "path": [t]}


def _build_coverage(code, pages, chunks, entries, first_content, last_content):
    total_pages = len(pages)
    pages_with_text = sum(1 for p in pages if p["char_count"] > 0)
    pages_empty = sum(1 for p in pages if p["char_count"] == 0)
    image_pages = [p["pdf_page"] for p in pages if p.get("image_page")]
    # cac trang duoc bieu dien trong chunks
    chunk_pages = set()
    for c in chunks:
        chunk_pages.add(c["pdf_page"])
        if c.get("pdf_page_end") and c["pdf_page_end"] != c["pdf_page"]:
            for pp in range(c["pdf_page"], c["pdf_page_end"] + 1):
                chunk_pages.add(pp)
    pages_in_chunks = len(chunk_pages)
    pages_with_text_chunks = sum(1 for pp in chunk_pages
                                 if next((p for p in pages if p["pdf_page"] == pp), None)
                                 and next(p for p in pages if p["pdf_page"] == pp)["char_count"] > 0)
    unresolved_pages = [c["pdf_page"] for c in chunks if c["kind"] == "unresolved"]
    blank_pages = [c["pdf_page"] for c in chunks if c["kind"] == "blank_page"]

    # per-page classification
    per_page = []
    for p in pages:
        pid = p["pdf_page"]
        kinds_here = [c["kind"] for c in chunks if c["pdf_page"] == pid]
        if p.get("image_page"):
            classification = "image_page"
        elif pid not in chunk_pages:
            classification = "unresolved"
        elif not kinds_here:
            classification = "unresolved"
        else:
            classification = "resolved"
        per_page.append({
            "pdf_page": pid,
            "printed_page": p.get("printed_page"),
            "printed_page_status": p.get("printed_page_status", "UNKNOWN"),
            "char_count": p["char_count"],
            "image_page": p.get("image_page", False),
            "classification": classification,
            "kinds": sorted(set(k for k in kinds_here if k)),
            "warnings": p.get("warnings", []),
        })

    chapters = sum(1 for c in chunks if c["kind"] == "chapter")
    sections = sum(1 for c in chunks if c["kind"] == "section")
    subsections = sum(1 for c in chunks if c["kind"] == "subsection")

    kinds_counter = Counter(c["kind"] for c in chunks)

    pages_without_coverage = sorted(
        p["pdf_page"] for p in pages
        if p["pdf_page"] not in chunk_pages and not p.get("image_page")
    )

    coverage = {
        "book_code": code,
        "total_pages": total_pages,
        "page_records": total_pages,
        "pages_in_chunks": pages_in_chunks,
        "pages_with_text_chunks": pages_with_text_chunks,
        "image_pages": len(image_pages),
        "image_page_list": image_pages,
        "blank_pages": len(blank_pages),
        "blank_page_list": blank_pages,
        "unresolved_pages": len(unresolved_pages),
        "unresolved_page_list": unresolved_pages,
        "pages_without_coverage": len(pages_without_coverage),
        "pages_without_coverage_list": pages_without_coverage,
        "coverage_percent": {
            "denominator": "total_pdf_pages",
            "denominator_value": total_pages,
            "resolved_pct": round(100.0 * len([pp for pp in chunk_pages
                                               if next((p for p in pages if p["pdf_page"] == pp), None)
                                               and next(p for p in pages if p["pdf_page"] == pp)["char_count"] > 0
                                               and pp not in image_pages]) / total_pages, 4),
            "image_page_pct": round(100.0 * len(image_pages) / total_pages, 4),
            "unresolved_pct": round(100.0 * len(unresolved_pages) / total_pages, 4),
            "uncovered_pct": round(100.0 * len(pages_without_coverage) / total_pages, 4),
        },
        "kinds": dict(kinds_counter),
        "chapters": chapters,
        "sections": sections,
        "subsections": subsections,
        "heading_index_size": len(entries),
        "first_content_page": first_content,
        "last_content_page": last_content,
        "chunks_total": len(chunks),
        "pages_with_text": pages_with_text,
        "pages_empty": pages_empty,
        "per_page": per_page,
        "mismatch": {
            "page_records_vs_pdf": total_pages - len(pages),
            "chunks_pages_vs_pdf": pages_in_chunks - total_pages,
            "unaccounted_pages": pages_without_coverage,
        },
    }
    return coverage


def main() -> int:
    _utf8_stdout()
    ap = argparse.ArgumentParser(
        description="L1 segmentation: cat chunk theo heading, gan kind, viet coverage.json.")
    ap.add_argument("--book-code", dest="book_code", help="ma sach: HAN | ROM | PIN | MAD")
    ap.add_argument("--book", dest="book_code_alias", help=argparse.SUPPRESS)
    ap.add_argument("--all", action="store_true", help="segment tat ca 4 sach")
    args = ap.parse_args()

    codes = []
    if args.all:
        codes = BOOKS
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
            segment(code)
        except Exception as exc:
            print(json.dumps({"book": code, "status": "FATAL", "error": str(exc)},
                             ensure_ascii=False))
            rc = 1
    return rc


if __name__ == "__main__":
    sys.exit(main())
