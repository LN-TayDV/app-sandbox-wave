#!/usr/bin/env python3
"""extract_units.py — L1.5: trích đơn vị tri thức từ chunks -> units CSV.

Sinh CSV theo schema 16 cột mà validate_theory_layer.py chấp nhận:
  global_id,book_code,chapter,kind,label,printed_page,pdf_page,
  definition,meaning,usage,equation_latex,symbols,verification_status,
  theory_id,note,source_ref

Nguyên tắc bằng chứng:
  * UNIT có neo đánh số (equation (13.1), Theorem 13.2.1, Figure 1.1, ...)
    -> trích từ text layer, verification_status = BOOK_EVIDENCE
  * UNIT toán học (equation) -> FORMULA_UNVERIFIED + note bắt buộc, vì text
    layer làm mất chỉ số trên/dưới và ký hiệu. Chưa qua render-diff.
  * UNIT suy luận (concept/assumption/caveat/narrative) -> chỉ sinh khi có
    điều kiện nhận dạng chặt; không bịa.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"C:\Users\PC\Documents\AI_project\sandbox-financial")
THEORY = ROOT / "theory"
BOOKS = ["HAN", "ROM", "PIN", "MAD"]

KIND_ORDER = ["equation", "theorem", "concept", "assumption", "caveat",
              "example", "figure", "table", "exercise", "narrative"]

COLUMNS = ["global_id", "book_code", "chapter", "kind", "label", "printed_page",
           "pdf_page", "definition", "meaning", "usage", "equation_latex",
           "symbols", "verification_status", "theory_id", "note", "source_ref"]

# ---------------------------------------------------------------- patterns
# Neo đánh số. Mỗi cuốn dùng hệ thống đánh số riêng:
#   HAN: (13.1), Theorem 13.2.1, Exercise 13.1, Figure 10.1, Table 2.1
#   ROM: (1.1), Figure 1.1, Table 5.1, Exercise 1.9
#   PIN: (1.1), Figure 1.1, Table 1.1
#   MAD: Exhibit 1.1, Exhibit 1.2  (không dùng Figure/Table)
RE_EQ = re.compile(r"\((\d{1,2}\.\d{1,2})\)")
RE_THEOREM = re.compile(
    r"\b(Theorem|Proposition|Lemma|Corollary)\s+(\d{1,2}\.\d{1,2}(?:\.\d{1,2})?)", re.I)
RE_EXERCISE = re.compile(r"\b(Exercise|Problem)\s+(\d{1,2}\.\d{1,2})", re.I)
RE_FIGURE = re.compile(r"\b(Figure|Fig\.|FIGURE|Exhibit)\s+(\d{1,2}\.\d{1,2})", re.I)
RE_TABLE = re.compile(r"\b(Table|TABLE)\s+(\d{1,2}\.\d{1,2})")
RE_EXAMPLE = re.compile(r"\b(Example)\s+(\d{1,2}\.\d{1,2})", re.I)

# Điều kiện nhận dạng cho unit suy luận (chặt, không bịa)
RE_DEFINITION = re.compile(
    r"\b(?P<term>[A-Z][A-Za-z\- ]{2,40}?)\s+(?:is|are)\s+(?:defined|defined as|"
    r"called|known as|referred to as)\b", re.U)
RE_ASSUME = re.compile(
    r"\b(?:we|let\s+us|the\s+model|the\s+theory)\s+(?:assume|suppose|take)\b"
    r"(?P<body>[^.]{10,300})", re.I)
RE_CAVEAT = re.compile(
    r"\b(it\s+is\s+(?:important\s+to\s+)?(?:note|worth\s+noting|essential\s+to\s+note)"
    r"|note\s+that|be\s+careful|caveat|caution|one\s+should\s+be\s+careful"
    r"|do\s+not\s+confuse|this\s+should\s+not\s+be\s+confused)"
    r"(?P<body>[^.]{10,300})", re.I)
RE_IMPORTANT = re.compile(
    r"\b(importantly|in\s+particular|it\s+is\s+worth\s+noting|recall\s+that)\b"
    r"(?P<body>[^.]{15,300})", re.I)

# Số trang in dạng "p.278" / "page 278" dùng làm mẫu số equation
RE_INLINE_PAGE = re.compile(r"\b(?:p\.|pp\.|page)\s*(\d{1,3})\b", re.I)

# Ký tự toán học -> ký hiệu nhận dạng
RE_SYMBOL = re.compile(r"\b([A-Za-z][A-Za-z0-9_]{0,3})\b")

SKIP_CHARS = set("()[]{}.,;:'\"!?")


def _chapter_of(chunk: dict, chapters: list[dict]) -> tuple[str, int]:
    """(chapter_key, chapter_number) cho chunk, dựa trên trang PDF."""
    p = chunk["pdf_page"]
    cur = None
    for ch in chapters:
        if ch["pdf_start"] <= p:
            cur = ch
        else:
            break
    if cur is None:
        return "front", 0
    return cur["key"], cur["n"]


def _chapter_n(chapters: list[dict], pdf_page: int) -> int:
    """Số chương của một trang (dùng khi ghi narrative)."""
    return _chapter_of({"pdf_page": pdf_page}, chapters)[1]


def _page_chapter_map(chunks: list[dict]) -> dict[int, int]:
    """pdf_page -> số chương, lấy trực tiếp từ heading_path của chunk.

    Chunk trong cùng chương có thể mang tiêu đề in-page khác nhau, nên phải
    ánh xạ theo chính chunk chứ không theo danh sách chương (vốn gộp theo
    trang bắt đầu).
    """
    m: dict[int, int] = {}
    for c in chunks:
        hp = c.get("heading_path") or []
        if not hp:
            continue
        _, n = _chapter_of_path(hp)
        if n > 0:
            m.setdefault(c["pdf_page"], n)
    return m


def _chapter_of_path(hp: list[str]) -> tuple[str, int]:
    """Suy ra (key, số chương) từ heading_path.

    heading_path khác nhau theo từng sách:
      HAN  : ["Chapter 13 Generalized Method of Moments", "13.1 ..."] -> 13
      ROM  : ["Chapter 1 THE SOLOW GROWTH MODEL", "1.1 ..."]           -> 1
      PIN  : ["Part One ...", "1 Preliminaries", "1.1 ..."]           -> 1
      MAD  : ["PART 1: ...", "1: MULTINATIONAL ...", "Managing ..."]  -> 1
    Quy tắc: quét path từ đầu, lấy phần tử ĐẦU TIÊN có dạng số chương.
    "PART n" bị bỏ qua (Part khác Chapter).
    """
    for el in hp:
        # "Chapter 13 ...", "13. ..." -> 13
        m = re.match(r"^Chapter\s+(\d{1,2})\b", el, re.I)
        if m:
            return el, int(m.group(1))
        # "1: MULTINATIONAL ..." hoặc "1 Preliminaries" -> 1
        m = re.match(r"^(\d{1,2})\s*[:.]?\s+\S", el)
        if m:
            return el, int(m.group(1))
        # "Appendix A ..." -> 1..26
        m = re.match(r"^Appendix\s+([A-Z])\b", el, re.I)
        if m:
            return el, ord(m.group(1)) - 64
    if hp:
        return hp[0], 0
    return "front", 0


def _chapter_list(code: str, chunks: list[dict]) -> list[dict]:
    """Danh sách chương (key, n, pdf_start) suy ra từ heading_path của chunks.

    Gộp theo SỐ chương (n), không theo chuỗi tiêu đề: cùng một chương có
    nhiều tiêu đề in-page khác nhau ("Managing the MNC", "CHAPTER OBJECTIVES"...)
    nhưng đều thuộc cùng chương. n=0 = front/back matter, không tạo entry.
    """
    out: list[dict] = []
    seen: dict[int, dict] = {}
    for c in chunks:
        hp = c.get("heading_path") or []
        if not hp:
            continue
        key, n = _chapter_of_path(hp)
        if n <= 0:
            continue
        if n not in seen:
            seen[n] = {"key": key, "n": n, "pdf_start": c["pdf_page"], "title": key}
            out.append(seen[n])
    out.sort(key=lambda x: x["pdf_start"])
    return out


def _lines(text: str) -> list[str]:
    return [ln.strip() for ln in text.split("\n")]


def _is_prose(line: str) -> bool:
    """Dòng văn xuôi (không phải mảnh công thức)."""
    s = line.strip()
    if len(s) < 35:
        return False
    if not re.match(r"^[A-Z(]", s):
        return False
    # văn xuôi: có từ dài, kết thúc bằng dấu câu
    words = re.findall(r"[A-Za-z]{3,}", s)
    if len(words) >= 6:
        return True
    return False


def _is_mathy(line: str) -> bool:
    """Dòng có vẻ là mảnh công thức."""
    s = line.strip()
    if not s:
        return True          # dòng trống: có thể nằm giữa công thức
    if _is_prose(s):
        return False
    return bool(re.search(r"[=+\-*/^_∑∏√]|\\\\|[<>]|\d", s))


def _find_equation_context(lines: list[str], num: str) -> tuple[str, str]:
    """Trả về (biểu thức, context) cho phương trình đánh số (num).

    Số nằm ở CUỐI dòng (kiểu sách toán): dòng chứa (num) là dòng số công thức,
    biểu thức nằm ở một hoặc nhiều dòng ngay trước. Đi lùi từ dòng số, gom
    các dòng toán liên tiếp cho tới khi gặp dòng văn xuôi (hoặc đầu trang).
    """
    for i, ln in enumerate(lines):
        if not re.search(r"\(\s*" + re.escape(num) + r"\)\s*$", ln):
            continue
        j = i - 1
        frag: list[str] = []
        while j >= 0:
            s = lines[j].strip()
            if _is_prose(s):
                break
            if not _is_mathy(s):
                break
            frag.append(s)
            j -= 1
        frag.reverse()
        expr = " ".join(f for f in frag if f).strip()
        ctx_start = max(0, j + 1)
        ctx = " ".join(lines[ctx_start:i + 1]).strip()
        return expr, ctx
    return "", ""


def _sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?])\s+", text.replace("\n", " "))
    return [p.strip() for p in parts if p.strip()]


def _short(s: str, n: int = 300) -> str:
    s = re.sub(r"\s+", " ", s).strip()
    return s[:n]


def extract(code: str) -> dict:
    out_dir = THEORY / "books" / code
    chunks = [json.loads(l) for l in
              (out_dir / "chunks.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    chapters = _chapter_list(code, chunks)
    page_ch = _page_chapter_map(chunks)

    # Chỉ trích từ chunk NỘI DUNG. Front/back matter (mục lục, bìa, lời giới
    # thiệu) chứa các chuỗi "Chapter N" trông giống tiêu đề chương nhưng là
    # danh sách mục lục -> trích từ đó sinh ra equation/figure giả.
    CONTENT_KINDS = {"chapter", "section", "subsection"}
    body_chunks = [c for c in chunks if c.get("kind") in CONTENT_KINDS]
    if not body_chunks:
        body_chunks = chunks

    # pdf_page -> printed_page cho các trang mà chunk không ghi (front matter).
    # Offset (pdf - printed) là hằng số trong mỗi cuốn, nên suy từ chunk lân cận.
    pdf2pp: dict[int, int] = {}
    for c in chunks:
        pp = c.get("printed_page")
        if pp not in ("", None):
            pdf2pp[c["pdf_page"]] = int(pp)
    if pdf2pp:
        offs = {p - v for p, v in pdf2pp.items()}
        off = max(offs, key=lambda o: sum(1 for p, v in pdf2pp.items()
                                          if p - v == o))
        for c in chunks:
            if c["pdf_page"] not in pdf2pp:
                cand = c["pdf_page"] - off
                # trang trước trang in đầu tiên không có số trang in
                if cand >= 1:
                    pdf2pp[c["pdf_page"]] = cand

    rows: list[dict] = []
    counters: dict[str, int] = {}

    def new_id(kind: str) -> str:
        counters[kind] = counters.get(kind, 0) + 1
        return f"{kind.upper()}-{code}-{counters[kind]:04d}"

    def base(chunk: dict, kind: str, label: str) -> dict:
        pdfp = chunk.get("pdf_page")
        pp = chunk.get("printed_page")
        if pp in ("", None):
            pp = pdf2pp.get(pdfp)
        chn = page_ch.get(pdfp, 0)
        src = f"{code} p.{pp} pdf {pdfp}" if pp is not None \
            else f"{code} pdf {pdfp}"
        return {
            "global_id": new_id(kind),
            "book_code": code,
            "chapter": chn if chn else 0,
            "kind": kind,
            "label": label,
            "printed_page": "" if pp is None else pp,
            "pdf_page": pdfp,
            "definition": "", "meaning": "", "usage": "",
            "equation_latex": "", "symbols": "",
            "verification_status": "BOOK_EVIDENCE",
            "theory_id": "", "note": "", "source_ref": src,
        }

    for ck in body_chunks:
        text = ck["text"]
        if not text.strip():
            continue
        lines = _lines(text)

        # ---- equation: (N.M) ở cuối dòng ----
        for num in sorted(set(RE_EQ.findall(text)), key=lambda s: [int(x) for x in s.split(".")]):
            expr, ctx = _find_equation_context(lines, num)
            if not ctx:
                continue
            r = base(ck, "equation", f"({num})")
            r["equation_latex"] = expr
            r["meaning"] = _short(ctx, 200)
            syms = [w for w in RE_SYMBOL.findall(expr)
                    if len(w) <= 2 and w not in SKIP_CHARS]
            r["symbols"] = ",".join(dict.fromkeys(syms))[:120]
            r["verification_status"] = "FORMULA_UNVERIFIED"
            r["note"] = ("text-layer extraction; superscripts/subscripts and "
                         "operators may be lossy; needs render-diff")
            rows.append(r)

        # ---- theorem / proposition ----
        for kw, num in RE_THEOREM.findall(text):
            r = base(ck, "theorem", f"{kw.title()} {num}")
            i = text.find(num)
            if i < 0:
                continue
            stmt = _short(text[max(0, i - 200): i + 320])
            r["definition"] = stmt
            r["verification_status"] = "FORMULA_UNVERIFIED" \
                if any(ch in stmt for ch in "=→∀∃√∑") else "BOOK_EVIDENCE"
            r["note"] = "text layer" if r["verification_status"] == "BOOK_EVIDENCE" \
                else "text-layer; symbolic form may be lossy"
            rows.append(r)

        # ---- exercise ----
        for kw, num in RE_EXERCISE.findall(text):
            r = base(ck, "exercise", f"{kw.title()} {num}")
            i = text.find(num)
            if i < 0:
                continue
            r["definition"] = _short(text[i: i + 300])
            rows.append(r)

        # ---- figure ----
        for kw, num in RE_FIGURE.findall(text):
            r = base(ck, "figure", f"{kw.title()} {num}")
            i = text.find(num)
            if i < 0:
                continue
            r["definition"] = _short(text[i: i + 250])
            r["usage"] = "figure caption"
            rows.append(r)

        # ---- table ----
        for _kw, num in set(RE_TABLE.findall(text)):
            r = base(ck, "table", f"Table {num}")
            i = text.find(num)
            if i < 0:
                continue
            r["definition"] = _short(text[i: i + 250])
            r["usage"] = "table caption"
            rows.append(r)

        # ---- example ----
        for kw, num in RE_EXAMPLE.findall(text):
            r = base(ck, "example", f"Example {num}")
            i = text.find(num)
            if i < 0:
                continue
            r["definition"] = _short(text[i: i + 300])
            rows.append(r)

        # ---- concept (định nghĩa có neo) ----
        for m in RE_DEFINITION.finditer(text):
            term = m.group("term").strip()
            if len(term) < 3 or term.lower() in ("this", "that", "it", "there"):
                continue
            if not re.search(r"\b(defin|denot|call|refer|known)\b",
                             text[m.start(): m.start() + 80], re.I):
                continue
            r = base(ck, "concept", term)
            r["definition"] = _short(text[m.start(): m.start() + 260])
            r["meaning"] = _short(m.group(0), 120)
            rows.append(r)

        # ---- assumption ----
        for m in RE_ASSUME.finditer(text):
            body = _short(m.group(0), 300)
            if len(body) < 25:
                continue
            r = base(ck, "assumption", _short(body, 80))
            r["definition"] = body
            r["scope"] = "model assumption stated in text"
            r["meaning"] = "assumption"
            rows.append(r)

        # ---- caveat ----
        for m in RE_CAVEAT.finditer(text):
            body = _short(m.group(0), 300)
            r = base(ck, "caveat", _short(body, 80))
            r["definition"] = body
            r["trigger"] = "stated in text"
            r["severity"] = "note"
            rows.append(r)

    # ---- narrative: tóm tắt mỗi chương ----
    for ch in chapters:
        sub = [c for c in body_chunks
               if page_ch.get(c["pdf_page"]) == ch["n"] and c["text"].strip()]
        if not sub:
            continue
        body = " ".join(c["text"] for c in sub[:6])
        r = base(sub[0], "narrative", f"Chapter {ch['n']} summary")
        r["definition"] = _short(body, 400)
        r["meaning"] = "chapter overview extracted from text layer"
        r["usage"] = "navigate"
        r["pdf_page"] = sub[0]["pdf_page"]
        r["printed_page"] = ("" if sub[0].get("printed_page") in ("", None)
                             else sub[0]["printed_page"])
        r["source_ref"] = f"{code} ch{ch['n']} (pdf {sub[0]['pdf_page']}+)"
        rows.append(r)

    # ghi CSV
    units_dir = out_dir / "units"
    units_dir.mkdir(parents=True, exist_ok=True)
    by_chapter: dict[int, list[dict]] = {}
    for r in rows:
        n = r["chapter"]
        key = n if isinstance(n, int) else 0
        by_chapter.setdefault(key, []).append(r)

    files = []
    for key, rs in sorted(by_chapter.items()):
        fname = (f"ch{key:02d}_units.csv" if isinstance(key, int) and key > 0
                 else "ch00_front_units.csv")
        path = units_dir / fname
        rs_sorted = sorted(rs, key=lambda r: KIND_ORDER.index(r["kind"])
                           if r["kind"] in KIND_ORDER else 99)
        with path.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=COLUMNS, extrasaction="ignore")
            w.writeheader()
            for r in rs_sorted:
                w.writerow(r)
        files.append((fname, len(rs)))

    total = len(rows)
    kinds: dict[str, int] = {}
    for r in rows:
        kinds[r["kind"]] = kinds.get(r["kind"], 0) + 1
    summary = {"book": code, "units": total, "kinds": kinds,
               "chapters": len(chapters), "files": len(files)}
    (out_dir / "units_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False))
    return summary


def main() -> int:
    ap = argparse.ArgumentParser(
        description="L1.5: trích đơn vị tri thức từ chunks -> units CSV.")
    ap.add_argument("--book", choices=BOOKS)
    ap.add_argument("--all", action="store_true")
    args = ap.parse_args()
    targets = BOOKS if args.all else ([args.book] if args.book else [])
    if not targets:
        ap.print_help()
        return 0
    for c in targets:
        extract(c)
    return 0


if __name__ == "__main__":
    sys.exit(main())
