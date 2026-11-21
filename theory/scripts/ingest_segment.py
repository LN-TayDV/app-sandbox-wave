#!/usr/bin/env python3
# ingest_segment.py - L0/L1 INFRA_PREP (không trích tri thức)
import json
from pathlib import Path

import fitz

BOOKS = {
    "HAN": {
        "pdf": r"C:\Users\PC\Documents\AI_project\sandbox-financial\data\book\econometrics-bruce-hansen-2014.pdf",
        "out_dir": Path(r"C:\Users\PC\Documents\AI_project\sandbox-financial\theory\books\HAN"),
    },
    "ROM": {
        "pdf": r"C:\Users\PC\Documents\AI_project\sandbox-financial\data\book\b81821bd16a42211f919748c26cd0774.pdf",
        "out_dir": Path(r"C:\Users\PC\Documents\AI_project\sandbox-financial\theory\books\ROM"),
    },
    "PIN": {
        "pdf": r"C:\Users\PC\Documents\AI_project\sandbox-financial\data\book\Robert S Pindyck_ Daniel L Rubinfeld - Microeconomics, Global Edition (2017, Pearson Education Limited) - libgen.li.pdf",
        "out_dir": Path(r"C:\Users\PC\Documents\AI_project\sandbox-financial\theory\books\PIN"),
    },
    "MAD": {
        "pdf": r"C:\Users\PC\Documents\AI_project\sandbox-financial\data\book\international-financial-management-11th-edition-by-jeff-madura.pdf",
        "out_dir": Path(r"C:\Users\PC\Documents\AI_project\sandbox-financial\theory\books\MAD"),
    },
}

def main():
    for code, cfg in BOOKS.items():
        out_dir = cfg["out_dir"]
        out_dir.mkdir(parents=True, exist_ok=True)
        pdf_path = cfg["pdf"]
        doc = fitz.open(pdf_path)
        total = len(doc)
        chunks = []
        for i in range(total):
            try:
                page = doc[i]
                text = page.get_text("text")
                # L0/L1 thô - không phân loại tri thức
                chunk = {
                    "chunk_id": f"{code}-p{i+1:04d}",
                    "book_code": code,
                    "pdf_page": i + 1,
                    "text": text,
                    "kind": None,  # sẽ xác định sau, chưa trích
                    "heading_path": [],
                }
                chunks.append(chunk)
            except Exception as e:
                chunks.append({
                    "chunk_id": f"{code}-p{i+1:04d}",
                    "book_code": code,
                    "pdf_page": i + 1,
                    "text": "",
                    "kind": None,
                    "heading_path": [],
                    "error": str(e),
                })
        doc.close()
        out_file = out_dir / "chunks.jsonl"
        with out_file.open("w", encoding="utf-8") as f:
            for c in chunks:
                f.write(json.dumps(c, ensure_ascii=False) + "\n")
        coverage = {
            "book_code": code,
            "total_pages": total,
            "chunks": len(chunks),
            "pages_with_text": sum(1 for c in chunks if c.get("text","").strip()),
            "pages_empty": sum(1 for c in chunks if not c.get("text","").strip()),
            "infra_prep": True,
            "note": "INFRA_PREP only - no units extracted",
        }
        (out_dir / "coverage.json").write_text(json.dumps(coverage, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"{code}: {total} pages -> {out_file}")

if __name__ == "__main__":
    main()
