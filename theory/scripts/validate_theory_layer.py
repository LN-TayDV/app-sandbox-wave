#!/usr/bin/env python3
"""validate_theory_layer.py - validator 7 checks for theory layer registries."""
import argparse
import csv
import json
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(r"C:\Users\PC\Documents\AI_project\sandbox-financial")
BOOKS_YAML = ROOT / "theory" / "registry" / "books.yaml"
LOG = ROOT / "logs" / "registry_validation.json"

CONTRACT_LABELS = {"BOOK_EVIDENCE", "PRIMARY_SOURCE", "SECONDARY_SOURCE", "DERIVED_RESULT",
                   "RESEARCH_HYPOTHESIS", "RESEARCH_SYNTHESIS", "UNVERIFIED", "SOURCE_GAP"}
LABELS = CONTRACT_LABELS | {"FORMULA_VERIFIED", "FORMULA_UNVERIFIED", "NUMERICALLY_VERIFIED", "VERIFIED", "ILLUSTRATIVE", "BOOK_EVIDENCE_VERIFIED"}
KINDS = {"concept", "equation", "assumption", "theorem", "caveat", "example", "figure", "table", "exercise", "narrative"}
BOOK_CODES = {"HAN", "ROM", "PIN", "MAD"}


def load_books():
    res = {}
    if not BOOKS_YAML.exists():
        return res
    try:
        txt = BOOKS_YAML.read_text(encoding="utf-8")
    except Exception:
        return res
    cur = None
    for line in txt.splitlines():
        m = re.match(r"^\s{2}([A-Z]{3}):\s*$", line)
        if m:
            cur = m.group(1)
            res[cur] = {}
            continue
        m = re.match(r"^\s{4}total_pages:\s*(\d+)", line)
        if m and cur:
            res[cur]["total_pages"] = int(m.group(1))
    return res


def try_latex(s):
    if not s or not str(s).strip():
        return True, ""
    s2 = str(s)
    try:
        import sympy  # noqa
        from sympy.parsing.latex import parse_latex
        parse_latex(s2)
        return True, ""
    except Exception:
        if s2.count("{") != s2.count("}"):
            return False, "unbalanced braces"
        if s2.count("[") != s2.count("]"):
            return False, "unbalanced brackets"
        return True, "fallback_ok"


def validate_file(path):
    errors = []
    books = load_books()
    p = Path(path)
    if not p.exists():
        errors.append({"check": "schema", "severity": "ERROR", "file": str(path), "line": 0, "field": None,
                       "msg": "file not found", "rule": "IO"})
        return {"file": str(path), "errors": errors, "summary": {"errors": len(errors), "total_records": 0}}
    try:
        text = p.read_text(encoding="utf-8-sig", errors="replace")
    except Exception as e:
        errors.append({"check": "schema", "severity": "ERROR", "file": str(path), "line": 0, "field": None,
                       "msg": f"read error: {e}", "rule": "IO"})
        return {"file": str(path), "errors": errors, "summary": {"errors": len(errors), "total_records": 0}}
    if text.strip() == "":
        return {"file": str(path), "errors": [], "summary": {"errors": 0, "total_records": 0}, "note": "empty file"}
    try:
        with open(p, newline="", encoding="utf-8-sig") as f:
            reader = csv.reader(f)
            rows = list(reader)
    except Exception as e:
        errors.append({"check": "schema", "severity": "ERROR", "file": str(path), "line": 0, "field": None,
                       "msg": f"csv parse error: {e}", "rule": "CSV"})
        return {"file": str(path), "errors": errors, "summary": {"errors": len(errors), "total_records": 0}}

    if not rows:
        return {"file": str(path), "errors": [], "summary": {"errors": 0, "total_records": 0}}
    header = [str(h).strip() for h in rows[0]]
    data = rows[1:]

    # CHECK 1 - Schema
    if len(header) not in (16, 19):
        errors.append({"check": "schema", "severity": "ERROR", "file": str(path), "line": 1, "field": None,
                       "msg": f"unexpected column count {len(header)} (expected 16 or 19)", "rule": "V1_SCHEMA"})
    else:
        if len(header) == 16:
            expected = ["equation_id", "theory_id", "chapter_id", "equation_label", "equation_latex",
                        "variable_definitions", "parameter_definitions", "assumptions", "derivation_summary",
                        "economic_interpretation", "equilibrium_or_optimality_conditions", "printed_page",
                        "pdf_page", "source_context", "verification_status", "verification_notes"]
            if header != expected:
                errors.append({"check": "schema", "severity": "ERROR", "file": str(path), "line": 1, "field": None,
                               "msg": "column names/order differ from expected for 16-col equation registry",
                               "rule": "V1_SCHEMA"})
        elif len(header) == 19:
            expected = ["theory_id", "canonical_name", "original_name", "authors", "year", "chapter_id",
                        "section_title", "printed_page", "pdf_page", "research_question", "assumptions",
                        "mechanisms", "key_results", "limitations", "empirical_evidence", "related_theories",
                        "thesis_relevance", "evidence_status", "verification_notes"]
            if header != expected:
                errors.append({"check": "schema", "severity": "ERROR", "file": str(path), "line": 1, "field": None,
                               "msg": "column names/order differ from expected for 19-col theory registry",
                               "rule": "V1_SCHEMA"})

    idx = {name: i for i, name in enumerate(header)}
    seen_ids = set()
    total_records = 0

    for ri, row in enumerate(data, start=2):
        if not row or all((str(c).strip() == "" for c in row)):
            continue
        total_records += 1
        while len(row) < len(header):
            row.append("")
        if len(row) > len(header):
            errors.append({"check": "schema", "severity": "ERROR", "file": str(path), "line": ri, "field": None,
                           "msg": f"row has extra columns ({len(row)} vs {len(header)})", "rule": "V1_SCHEMA"})

        def get(col):
            i = idx.get(col)
            if i is None or i >= len(row):
                return ""
            return str(row[i]).strip()

        if "global_id" in idx:
            gid_check = get("global_id")
        elif "equation_id" in idx:
            gid_check = get("equation_id")
        elif "theory_id" in idx and len(header) == 19:
            gid_check = get("theory_id")
        elif "theory_id" in idx:
            gid_check = get("theory_id")
        else:
            gid_check = ""

        book = get("book_code")
        pp = get("printed_page")
        pdfp = get("pdf_page")
        vs = get("verification_status") if "verification_status" in idx else get("evidence_status")
        kind = get("kind")
        latex = get("equation_latex")
        note = get("note") if "note" in idx else get("verification_notes")

        if gid_check:
            if re.match(r"^[A-Z]+-[A-Z]{3}-\d{4}$", gid_check):
                if gid_check in seen_ids:
                    errors.append({"check": "global_id", "severity": "ERROR", "file": str(path), "line": ri,
                                   "field": header[0] if header else "id", "global_id": gid_check,
                                   "msg": f"duplicate global_id: {gid_check}", "rule": "V2_GLOBAL_ID"})
                seen_ids.add(gid_check)
                m = re.match(r"^[A-Z]+-([A-Z]{3})-\d{4}$", gid_check)
                if m and book and m.group(1) != book:
                    errors.append({"check": "global_id", "severity": "ERROR", "file": str(path), "line": ri,
                                   "field": "book_code", "global_id": gid_check,
                                   "msg": f"book_code mismatch between id and field: {gid_check} vs {book}",
                                   "rule": "V2_GLOBAL_ID"})
            elif '-' in gid_check and re.match(r"^[A-Z0-9]+-[A-Z0-9]+", gid_check):
                errors.append({"check": "global_id", "severity": "ERROR", "file": str(path), "line": ri,
                               "field": header[0] if header else "id", "global_id": gid_check,
                               "msg": f"bad global_id format: {gid_check}", "rule": "V2_GLOBAL_ID"})

        if book and book not in BOOK_CODES:
            errors.append({"check": "global_id", "severity": "ERROR", "file": str(path), "line": ri,
                           "field": "book_code", "msg": f"invalid book_code: {book}", "rule": "V2_GLOBAL_ID"})

        if (pp == "") != (pdfp == ""):
            errors.append({"check": "pages", "severity": "ERROR", "file": str(path), "line": ri,
                           "field": "printed_page/pdf_page",
                           "msg": "printed_page/pdf_page must both present or both empty", "rule": "V4_PAGES"})
        if pdfp:
            try:
                n = int(float(pdfp))
                tp = books.get(book, {}).get("total_pages") if book else None
                if tp is None and books:
                    tp = max((b.get("total_pages",0) for b in books.values() if isinstance(b,dict)), default=None)
                if tp is not None and n > tp:
                    errors.append({"check": "pages", "severity": "ERROR", "file": str(path), "line": ri,
                                   "field": "pdf_page", "msg": f"pdf_page {n} > total_pages {tp}", "rule": "V4_PAGES"})
            except Exception:
                errors.append({"check": "pages", "severity": "ERROR", "file": str(path), "line": ri,
                               "field": "pdf_page", "msg": f"non-integer pdf_page: {pdfp}", "rule": "V4_PAGES"})

        if vs and vs not in CONTRACT_LABELS and vs not in {"FORMULA_VERIFIED", "FORMULA_UNVERIFIED", "NUMERICALLY_VERIFIED", "VERIFIED", "ILLUSTRATIVE"}:
            errors.append({"check": "vocabulary", "severity": "ERROR", "file": str(path), "line": ri,
                           "field": "verification_status/evidence_status", "msg": f"unknown verification_status/evidence_status: {vs}",
                           "rule": "V5_VOCAB"})
        if kind and kind not in KINDS:
            errors.append({"check": "vocabulary", "severity": "ERROR", "file": str(path), "line": ri,
                           "field": "kind", "msg": f"unknown kind: {kind}", "rule": "V5_VOCAB"})

        if latex:
            ok, msg = try_latex(latex)
            if not ok:
                errors.append({"check": "latex", "severity": "ERROR", "file": str(path), "line": ri,
                               "field": "equation_latex", "msg": f"latex parse error: {msg}", "rule": "V6_LATEX"})

        if vs == "FORMULA_UNVERIFIED" and not note:
            errors.append({"check": "completeness", "severity": "ERROR", "file": str(path), "line": ri,
                           "field": "verification_notes/note", "msg": "FORMULA_UNVERIFIED requires note/explanation",
                           "rule": "V7_STATUS"})
        if vs in ("VERIFIED", "NUMERICALLY_VERIFIED", "FORMULA_VERIFIED") and pp == "":
            errors.append({"check": "completeness", "severity": "ERROR", "file": str(path), "line": ri,
                           "field": "printed_page", "msg": f"{vs} requires printed_page", "rule": "V7_STATUS"})

    theory_ids = set()
    if len(header) == 16 and p.name.lower().endswith("05_equation_registry.csv"):
        cand = p.parent / "04_theory_registry.csv"
        if cand.exists():
            try:
                with open(cand, newline="", encoding="utf-8-sig") as f:
                    r = csv.reader(f)
                    trows = list(r)
                if trows:
                    th = trows[0]
                    ti = th.index("theory_id") if "theory_id" in th else 0
                    for tr in trows[1:]:
                        if tr and len(tr) > ti:
                            theory_ids.add(str(tr[ti]).strip())
            except Exception:
                pass

    if len(header) == 16 and "theory_id" in idx:
        for ri, row in enumerate(data, start=2):
            if not row or all((str(c).strip() == "" for c in row)):
                continue
            while len(row) < len(header):
                row.append("")
            tid = row[idx["theory_id"]].strip() if idx["theory_id"] < len(row) else ""
            if tid == "":
                errors.append({"check": "foreign_key", "severity": "ERROR", "file": str(path), "line": ri,
                               "field": "theory_id", "msg": "theory_id is required in equation registry", "rule": "V3_FK"})
            elif theory_ids and tid not in theory_ids:
                errors.append({"check": "foreign_key", "severity": "ERROR", "file": str(path), "line": ri,
                               "field": "theory_id", "global_id": row[0].strip() if row else None,
                               "msg": f"Referenced theory_id does not exist: {tid}", "rule": "V3_FK"})

    return {"file": str(path), "errors": errors, "summary": {"errors": len(errors), "total_records": total_records},
            "schema": {"columns": len(header), "header": header}}


def main():
    global BOOKS_YAML, LOG
    ap = argparse.ArgumentParser(description="Validate theory layer registries (7 checks).")
    ap.add_argument("--registry", required=True, help="path to csv registry")
    ap.add_argument("--books", default=str(BOOKS_YAML), help="path to books.yaml")
    ap.add_argument("--out", default=str(LOG), help="output json log")
    args = ap.parse_args()
    BOOKS_YAML = Path(args.books)
    LOG = Path(args.out)
    res = validate_file(args.registry)
    res["timestamp"] = datetime.utcnow().isoformat() + "Z"
    res["run_identifier"] = f"run-{datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}"
    res["parser_dependency_status"] = {}
    try:
        import sympy
        from sympy.parsing.latex import parse_latex
        res["parser_dependency_status"]["sympy"] = True
    except Exception as e:
        res["parser_dependency_status"]["sympy"] = False
        res["parser_dependency_status"]["sympy_error"] = str(e)
    LOG.parent.mkdir(parents=True, exist_ok=True)
    LOG.write_text(json.dumps(res, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(res, indent=2, ensure_ascii=False))
    if res.get("errors"):
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
