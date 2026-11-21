#!/usr/bin/env python3
# Fix HAN text extraction artifacts (copyright etc) without guessing broadly
import json
from pathlib import Path
import fitz

PDF = r"C:\Users\PC\Documents\AI_project\sandbox-financial\data\book\econometrics-bruce-hansen-2014.pdf"
OUT_DIR = Path(r"C:\Users\PC\Documents\AI_project\sandbox-financial\theory\books\HAN")

def fix_text(t):
    if not t:
        return t
    # common artifacts from cp1252/latin-1 misdecode through pymupdf
    # copyright
    t = t.replace('c\uFFFD', '©')
    t = t.replace('C\uFFFD', '©')
    t = t.replace('\u00a9\uFFFD', '©')
    # fi/fl ligatures sometimes lost
    t = t.replace('\uFB01', 'fi')
    t = t.replace('\uFB02', 'fl')
    # en dash/em dash if replaced oddly
    t = t.replace('\u2013', '–')
    t = t.replace('\u2014', '—')
    return t

def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(PDF)
    total = len(doc)
    chunks = []
    for i in range(total):
        try:
            page = doc[i]
            text = page.get_text("text")
            text = fix_text(text)
            chunk = {
                "chunk_id": f"HAN-p{i+1:04d}",
                "book_code": "HAN",
                "pdf_page": i + 1,
                "text": text,
                "kind": None,
                "heading_path": [],
            }
            chunks.append(chunk)
        except Exception as e:
            chunks.append({
                "chunk_id": f"HAN-p{i+1:04d}",
                "book_code": "HAN",
                "pdf_page": i + 1,
                "text": "",
                "kind": None,
                "heading_path": [],
                "error": str(e),
            })
    doc.close()
    out_file = OUT_DIR / "chunks.jsonl"
    with out_file.open("w", encoding="utf-8") as f:
        for c in chunks:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")
    coverage = {
        "book_code": "HAN",
        "total_pages": total,
        "chunks": len(chunks),
        "pages_with_text": sum(1 for c in chunks if c.get("text","").strip()),
        "pages_empty": sum(1 for c in chunks if not c.get("text","").strip()),
        "infra_prep": True,
        "note": "INFRA_PREP only - no units extracted; HAN text normalized for common ligature/copyright artifacts",
    }
    (OUT_DIR / "coverage.json").write_text(json.dumps(coverage, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"HAN fixed: {total} pages")

if __name__ == "__main__":
    main()
