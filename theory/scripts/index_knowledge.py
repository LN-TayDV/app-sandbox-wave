#!/usr/bin/env python3
"""index_knowledge.py - L2: SQLite + FTS5 index over chunks."""
import argparse, json, sqlite3, os
from pathlib import Path

ROOT = Path(r"C:\Users\PC\Documents\AI_project\sandbox-financial")
THEORY = ROOT / "theory"
DB = THEORY / "knowledge.db"
BOOKS = ["HAN", "ROM", "PIN", "MAD"]

SCHEMA = """
CREATE TABLE IF NOT EXISTS books (book_code TEXT PRIMARY KEY, title TEXT, total_pages INTEGER, sha256 TEXT);
CREATE TABLE IF NOT EXISTS pages (book_code TEXT, pdf_page INTEGER, printed_page TEXT, char_count INTEGER, image_page INTEGER, PRIMARY KEY(book_code, pdf_page));
CREATE TABLE IF NOT EXISTS chunks (chunk_id TEXT PRIMARY KEY, book_code TEXT, pdf_page INTEGER, printed_page TEXT, kind TEXT, heading_path TEXT, text TEXT);
CREATE VIRTUAL TABLE IF NOT EXISTS fts_chunks USING fts5(chunk_id, book_code, text, content='chunks', content_rowid='rowid');
"""

def _printed(v):
    if v is None or v == "":
        return None
    return str(v)

def build(db_path):
    db_path = Path(db_path)
    tmp = db_path.with_suffix(".tmp.db")
    if tmp.exists():
        tmp.unlink()
    conn = sqlite3.connect(str(tmp))
    try:
        cur = conn.cursor()
        cur.executescript(SCHEMA)
        for code in BOOKS:
            out_dir = THEORY / "books" / code
            manifest = json.loads((out_dir / "manifest.json").read_text(encoding="utf-8")) if (out_dir / "manifest.json").exists() else {}
            cur.execute("INSERT INTO books(book_code,total_pages,sha256) VALUES (?,?,?)",
                        (code, manifest.get("total_pages"), manifest.get("sha256")))
            # dedupe pages
            seen_pages = set()
            for line in (out_dir / "chunks.jsonl").read_text(encoding="utf-8").splitlines():
                if not line.strip():
                    continue
                c = json.loads(line)
                cur.execute("INSERT INTO chunks(chunk_id,book_code,pdf_page,printed_page,kind,heading_path,text) VALUES (?,?,?,?,?,?,?)",
                    (c["chunk_id"], c["book_code"], c["pdf_page"], _printed(c.get("printed_page")), c.get("kind"),
                     json.dumps(c.get("heading_path", []), ensure_ascii=False), c["text"]))
                key = (c["book_code"], c["pdf_page"])
                if key not in seen_pages:
                    seen_pages.add(key)
                    cur.execute("INSERT INTO pages(book_code,pdf_page,printed_page,char_count,image_page) VALUES (?,?,?,?,?)",
                        (c["book_code"], c["pdf_page"], _printed(c.get("printed_page")), c.get("char_count", len(c["text"])),
                         1 if c.get("image_page") else 0))
        cur.execute("INSERT INTO fts_chunks(rowid,chunk_id,book_code,text) SELECT rowid,chunk_id,book_code,text FROM chunks")
        conn.commit()
    except Exception:
        conn.rollback()
        conn.close()
        if tmp.exists():
            tmp.unlink()
        raise
    conn.close()
    # atomic replace
    if db_path.exists():
        backup = db_path.with_suffix(".bak")
        if backup.exists():
            backup.unlink()
        db_path.rename(backup)
        try:
            tmp.rename(db_path)
        except Exception:
            backup.rename(db_path)
            raise
        backup.unlink()
    else:
        tmp.rename(db_path)
    # test query
    conn = sqlite3.connect(str(db_path))
    cur = conn.cursor()
    cur.execute("SELECT chunk_id,book_code FROM fts_chunks WHERE fts_chunks MATCH 'credit' LIMIT 5")
    print("indexed; sample credit matches:", cur.fetchall())
    conn.close()

def main():
    ap = argparse.ArgumentParser(description="L2: build SQLite+FTS5 knowledge index.")
    ap.add_argument("--db", default=str(DB))
    ap.add_argument("--rebuild", action="store_true", help="rebuild from scratch")
    args = ap.parse_args()
    build(Path(args.db))
    print("done")

if __name__ == "__main__":
    main()
print("written")
