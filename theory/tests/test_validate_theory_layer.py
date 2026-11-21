import csv, json, subprocess, sys
from pathlib import Path

ROOT = Path(r"C:\Users\PC\Documents\AI_project\sandbox-financial")
SCRIPT = ROOT / "theory" / "scripts" / "validate_theory_layer.py"
BOOKS = ROOT / "theory" / "registry" / "books.yaml"

def run(registry, out):
    r = subprocess.run([sys.executable, str(SCRIPT), "--registry", str(registry), "--books", str(BOOKS), "--out", str(out)],
                       capture_output=True, text=True)
    try:
        data = json.loads(r.stdout)
    except Exception:
        data = None
    return r, data

def write_csv(path, header, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        for r in rows:
            w.writerow(r)

EQ_HEADER = ["equation_id","theory_id","chapter_id","equation_label","equation_latex","variable_definitions","parameter_definitions","assumptions","derivation_summary","economic_interpretation","equilibrium_or_optimality_conditions","printed_page","pdf_page","source_context","verification_status","verification_notes"]
TH_HEADER = ["theory_id","canonical_name","original_name","authors","year","chapter_id","section_title","printed_page","pdf_page","research_question","assumptions","mechanisms","key_results","limitations","empirical_evidence","related_theories","thesis_relevance","evidence_status","verification_notes"]

def test_help():
    r = subprocess.run([sys.executable, str(SCRIPT), "--help"], capture_output=True, text=True)
    assert r.returncode == 0
    assert "registry" in r.stdout

def test_empty_file(tmp_path):
    p = tmp_path/"empty.csv"; p.write_text("", encoding="utf-8")
    r,data = run(p, tmp_path/"out.json")
    assert r.returncode == 0
    assert data["summary"]["total_records"] == 0

def test_header_only(tmp_path):
    p = tmp_path/"h.csv"; p.write_text(",".join(EQ_HEADER)+"\n", encoding="utf-8")
    r,data = run(p, tmp_path/"out.json")
    assert r.returncode == 0

def test_bad_schema(tmp_path):
    p = tmp_path/"bad.csv"; p.write_text("a,b,c\n1,2,3\n", encoding="utf-8")
    r,data = run(p, tmp_path/"out.json")
    assert r.returncode != 0
    assert any(e["check"]=="schema" for e in data["errors"])

def test_duplicate_id(tmp_path):
    rows = [["EQ-PIN-0001","TH-X","Ch1","l","x=1","","","","","","","1","1","","BOOK_EVIDENCE","note"],
            ["EQ-PIN-0001","TH-X","Ch1","l","x=1","","","","","","","1","1","","BOOK_EVIDENCE","note"]]
    p = tmp_path/"dup.csv"; write_csv(p, EQ_HEADER, rows)
    r,data = run(p, tmp_path/"out.json")
    assert r.returncode != 0
    assert any("duplicate" in e["msg"] for e in data["errors"])

def test_page_exceed(tmp_path):
    rows = [["EQ-PIN-0001","TH-X","Ch1","l","x=1","","","","","","","1","9999","","BOOK_EVIDENCE","note"]]
    p = tmp_path/"pg.csv"; write_csv(p, EQ_HEADER, rows)
    r,data = run(p, tmp_path/"out.json")
    assert r.returncode != 0
    assert any("total_pages" in e["msg"] for e in data["errors"])

def test_bad_status(tmp_path):
    rows = [["EQ-PIN-0001","TH-X","Ch1","l","x=1","","","","","","","1","1","","NOPE","note"]]
    p = tmp_path/"st.csv"; write_csv(p, EQ_HEADER, rows)
    r,data = run(p, tmp_path/"out.json")
    assert r.returncode != 0
    assert any(e["check"]=="vocabulary" for e in data["errors"])

def test_bad_latex(tmp_path):
    rows = [["EQ-PIN-0001","TH-X","Ch1","l","x={1","","","","","","","1","1","","BOOK_EVIDENCE","note"]]
    p = tmp_path/"lx.csv"; write_csv(p, EQ_HEADER, rows)
    r,data = run(p, tmp_path/"out.json")
    assert r.returncode != 0
    assert any(e["check"]=="latex" for e in data["errors"])

def test_formula_unverified_note(tmp_path):
    rows = [["EQ-PIN-0001","TH-X","Ch1","l","x=1","","","","","","","1","1","","FORMULA_UNVERIFIED",""]]
    p = tmp_path/"fu.csv"; write_csv(p, EQ_HEADER, rows)
    r,data = run(p, tmp_path/"out.json")
    assert r.returncode != 0
    assert any("FORMULA_UNVERIFIED requires note" in e["msg"] for e in data["errors"])

def test_verified_requires_page(tmp_path):
    rows = [["EQ-PIN-0001","TH-X","Ch1","l","x=1","","","","","","","","","","VERIFIED",""]]
    p = tmp_path/"vr.csv"; write_csv(p, EQ_HEADER, rows)
    r,data = run(p, tmp_path/"out.json")
    assert r.returncode != 0
    assert any("requires printed_page" in e["msg"] for e in data["errors"])

def test_json_valid(tmp_path):
    p = tmp_path/"empty.csv"; p.write_text("", encoding="utf-8")
    out = tmp_path/"out.json"
    run(p, out)
    data = json.loads(out.read_text(encoding="utf-8"))
    assert "timestamp" in data