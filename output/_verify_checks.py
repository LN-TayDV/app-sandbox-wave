"""Kiem chung D1-D9 + registry schema. Doc va do, khong sua file."""
import csv
import os
import re

import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print("=" * 70)
print("A. PANEL - D2..D6")
print("=" * 70)
p = pd.read_csv(os.path.join(ROOT, "data/processed/ifwst_panel.csv"))
print("shape", p.shape, "| countries", p["country"].nunique(), "| years", p["date"].min(), "-", p["date"].max())
print("cols:", list(p.columns))

print("\n-- D3 sandpile_load --")
print("nunique =", p["sandpile_load"].nunique())
print(p["sandpile_load"].value_counts().head(3).to_string())
print("rows load == 0.2 :", int((p["sandpile_load"] == 0.2).sum()), "/", len(p))
nun = p.groupby("country")["sandpile_load"].nunique()
print("per-country distinct load values ->", nun.value_counts().to_dict())

print("\n-- D4 network_density --")
mx = p["trade_openness"].max()
print("max |nd - trade/max| =", (p["network_density"] - p["trade_openness"] / mx).abs().max())
print("nd range:", p["network_density"].min(), "->", p["network_density"].max())

print("\n-- D5 regime --")
print("regime == 1{gdp_growth>0} for all rows:", bool((p["regime"] == (p["gdp_growth"] > 0)).all()))
print("regime values:", sorted(p["regime"].unique()))

print("\n-- D2 credit_gap --")
print("nonzero share = %.4f | std = %.4f" % ((p["credit_gap"] != 0).mean(), p["credit_gap"].std()))
print("min/max = %.3f / %.3f" % (p["credit_gap"].min(), p["credit_gap"].max()))

print("\n-- D6 frequency --")
print("distinct 'date' values =", p["date"].nunique(), "-> ANNUAL" if p["date"].nunique() < 60 else "-> not annual")
print("rows per country =", len(p) // p["country"].nunique())

print("\n-- crisis_sys (DV) --")
print("sum =", int(p["crisis_sys"].sum()), "| countries with crisis =", p[p.crisis_sys == 1]["country"].nunique())
print("crisis years:", sorted(p.loc[p["crisis_sys"] == 1, "date"].unique().tolist()))

print("\n-- D8 --")
code = os.path.join(ROOT, "code")
derived = sorted(f for f in os.listdir(code) if f.startswith("05_derived"))
print("05_derived* scripts:", derived)
print("code/08..16 present:", sorted(f for f in os.listdir(code) if re.match(r"^(0[89]|1[0-6])_", f)))

print("\n-- D1 raw data --")
raw = os.path.join(ROOT, "data/raw")
files = sorted(os.listdir(raw))
print("bis_* :", [f for f in files if f.startswith("bis")])
print("imf_* :", [f for f in files if f.startswith("imf")])
print("wb_* count:", len([f for f in files if f.startswith("wb")]))

print("\n-- D9 trace layers --")
for f in ["source_registry.csv", "variable_dictionary.csv", "formula_registry.csv", "model_registry.csv"]:
    print(" ", f, "->", os.path.exists(os.path.join(ROOT, "data", f)))

print("\n" + "=" * 70)
print("B. REGISTRY SCHEMA")
print("=" * 70)
REG = {
    "MICRO_EQ": "research/microeconomics-pindyck-rubinfeld/05_equation_registry.csv",
    "MICRO_TH": "research/microeconomics-pindyck-rubinfeld/04_theory_registry.csv",
    "MACRO_EQ": "research/advanced-macroeconomics-fourth-edition/workflows/05_equation_registry.csv",
    "MACRO_TH": "research/advanced-macroeconomics-fourth-edition/workflows/04_theory_registry.csv",
}
tabs = {}
for k, rel in REG.items():
    rows = list(csv.reader(open(os.path.join(ROOT, rel), encoding="utf-8")))
    tabs[k] = rows
    print("%-10s cols=%d  data_rows=%d  header_hash=%s" % (
        k, len(rows[0]), len(rows) - 1, hash(tuple(rows[0]))))
print("EQ header MICRO == MACRO :", tabs["MICRO_EQ"][0] == tabs["MACRO_EQ"][0])
print("TH header MICRO == MACRO :", tabs["MICRO_TH"][0] == tabs["MACRO_TH"][0])

print("\n-- duplicate ids --")
for k in REG:
    ids = [r[0] for r in tabs[k][1:]]
    print("%-10s dup_ids=%d" % (k, len(ids) - len(set(ids))))

print("\n-- FK: equation.theory_id -> theory registry --")
for eqk, thk in [("MICRO_EQ", "MICRO_TH"), ("MACRO_EQ", "MACRO_TH")]:
    ths = {r[0] for r in tabs[thk][1:]}
    bad = [r[0] for r in tabs[eqk][1:] if r[1] not in ths]
    print("%-10s dangling = %d %s" % (eqk, len(bad), bad[:5]))

print("\n-- G3: printed_page + pdf_page cung co hoac cung rong --")
for k in REG:
    i_pp, i_pf = tabs[k][0].index("printed_page"), tabs[k][0].index("pdf_page")
    half = [r[0] for r in tabs[k][1:] if (r[i_pp].strip() == "") != (r[i_pf].strip() == "")]
    print("%-10s half-filled = %d" % (k, len(half)))

print("\n-- G5: verification_status vocabulary --")
VOCAB = {"BOOK_EVIDENCE", "PRIMARY_SOURCE", "SECONDARY_SOURCE", "DERIVED_RESULT",
         "RESEARCH_HYPOTHESIS", "RESEARCH_SYNTHESIS", "UNVERIFIED", "SOURCE_GAP",
         "FORMULA_VERIFIED", "FORMULA_UNVERIFIED", "NUMERICALLY_VERIFIED", "ILLUSTRATIVE"}
for k in REG:
    i = tabs[k][0].index("verification_status")
    vals = sorted({r[i] for r in tabs[k][1:]})
    bad = [v for v in vals if v not in VOCAB]
    print("%-10s distinct=%s" % (k, vals))
    print("%-10s OFF-VOCAB=%d" % ("", len(bad)), bad)

print("\n-- G2/G1: book_code + global_id presence --")
for k in REG:
    hdr = tabs[k][0]
    has_bc = "book_code" in hdr
    has_gid = "global_id" in hdr
    print("%-10s book_code_col=%s global_id_col=%s" % (k, has_bc, has_gid))

print("\n" + "=" * 70)
print("C. LITERATURE MATRIX")
print("=" * 70)
lm = os.path.join(ROOT, "01_literature/literature_matrix.csv")
if os.path.exists(lm):
    rows = list(csv.reader(open(lm, encoding="utf-8")))
    print("cols=%d data_rows=%d size=%d B" % (len(rows[0]), len(rows) - 1, os.path.getsize(lm)))
    print("header:", rows[0])
else:
    print("MISSING", lm)
for f in ["critical_review.md", "research_gap.md"]:
    print(" ", f, "->", os.path.exists(os.path.join(ROOT, "01_literature", f)))
sl = os.path.join(ROOT, "01_literature/search_log.csv")
if os.path.exists(sl):
    rows = list(csv.reader(open(sl, encoding="utf-8")))
    print("search_log rows:", len(rows) - 1, "| size", os.path.getsize(sl), "B")
    print("header:", rows[0])
