#!/usr/bin/env python
"""
B2 — Dựng panel quarterly 21 nước × 1990Q1-2023Q4 (IFWST).

Nguồn (tất cả trong data/raw/):
  BIS  SDMX v2   : bis_credit_gap.csv (credit-to-GDP gap, quarterly)
                   bis_credit_gdp_ratio.csv (ratio thô)
                   bis_dsr.csv (debt service ratio)
                   bis_lbs_xborder_<cty>.csv (cross-border claims)
  WB   World Bank : wb_macro_combined.csv (macro thường, ANNUAL → nội suy tuyến tính)
  LV   Laeven-Valencia : laeven_valencia_crises.xlsx (khủng hoảng ngân hàng hệ thống)

Quyết định thiết kế:
  * Tần suất QUÝ (BIS có sẵn quý; WB chỉ có năm → nội suy tuyến tính giữa các năm).
  * credit_gap LẤY THẲNG từ BIS (không tự tính như bản cũ).
  * Không điền median — giữ NaN và báo cáo tỉ lệ quan sát thật.
  * Khủng hoảng: biến 0/1 theo QUÝ từ LV start/end year.

Chạy:  python code/08_build_panel.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd

# Console Windows mặc định cp1252 — ép UTF-8 để in được tiếng Việt
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
PROC = ROOT / "data" / "processed"
PROC.mkdir(parents=True, exist_ok=True)

START_Y, END_Y = 1990, 2023

# 21 nước panel (ISO-2 như BIS) — chốt theo độ phủ BIS cg+DSR+LBS và số sự kiện LV
PANEL21 = ["BR", "CA", "CH", "CN", "CZ", "DE", "FR", "GB", "HU", "ID", "IN",
           "IT", "JP", "KR", "MX", "NL", "PL", "RU", "SE", "TR", "US"]

# Tên đầy đủ (ISO-3) để trích dẫn
ISO3 = {"BR": "BRA", "CA": "CAN", "CH": "CHE", "CN": "CHN", "CZ": "CZE",
        "DE": "DEU", "FR": "FRA", "GB": "GBR", "HU": "HUN", "ID": "IDN",
        "IN": "IND", "IT": "ITA", "JP": "JPN", "KR": "KOR", "MX": "MEX",
        "NL": "NLD", "PL": "POL", "RU": "RUS", "SE": "SWE", "TR": "TUR",
        "US": "USA"}

# Tên WB trong file csv (World Bank dùng tên tiếng Anh)
WB_NAME = {"BR": "Brazil", "CA": "Canada", "CH": "Switzerland", "CN": "China",
           "CZ": "Czechia", "DE": "Germany", "FR": "France",
           "GB": "United Kingdom", "HU": "Hungary", "ID": "Indonesia",
           "IN": "India", "IT": "Italy", "JP": "Japan", "KR": "Korea, Rep.",
           "MX": "Mexico", "NL": "Netherlands", "PL": "Poland",
           "RU": "Russian Federation", "SE": "Sweden", "TR": "Turkiye",
           "US": "United States"}

# Nhận diện quốc gia trong file Laeven–Valencia -> ISO-2
LV_NAME = {"Brazil": "BR", "Canada": "CA", "Switzerland": "CH",
           "China, Mainland": "CN", "China, P.R.": "CN", "Czech Republic": "CZ",
           "Germany": "DE", "France": "FR", "United Kingdom": "GB",
           "Hungary": "HU", "Indonesia": "ID", "India": "IN", "Italy": "IT",
           "Japan": "JP", "Korea": "KR", "Mexico": "MX", "Netherlands": "NL",
           "Poland": "PL", "Russia": "RU", "Sweden": "SE", "Turkey": "TR",
           "United States": "US"}


def q_index(period: str) -> int:
    """'1990-Q1' -> 1990*4 + 1 (quý liên tục)."""
    y, q = period.split("-Q")
    return int(y) * 4 + int(q)


def parse_bis(fname: str, value_col: str = "OBS_VALUE") -> pd.DataFrame | None:
    path = RAW / fname
    if not path.exists():
        return None
    df = pd.read_csv(path)
    if "BORROWERS_CTY" in df.columns:
        df = df[df.BORROWERS_CTY.isin(PANEL21)]
        df = df.rename(columns={"BORROWERS_CTY": "cty"})
    elif "L_REP_CTY" in df.columns:
        df = df[df.L_REP_CTY.isin(PANEL21)]
        df = df.rename(columns={"L_REP_CTY": "cty"})
    else:
        return None
    df = df[["cty", "TIME_PERIOD", value_col]].copy()
    df["q"] = df.TIME_PERIOD.map(q_index)
    df[value_col] = pd.to_numeric(df[value_col], errors="coerce")
    df = df.dropna(subset=[value_col])
    # chỉ giữ cửa sổ phân tích + khử trùng (phòng khi dataflow trả nhiều dòng/cty)
    df = df[(df.q >= START_Y * 4 + 1) & (df.q <= END_Y * 4 + 4)]
    df = df.groupby(["cty", "q"], as_index=False)[value_col].mean()
    return df


def load_lv_crises() -> pd.DataFrame:
    """Đọc sheet 'Crisis Resolution and Outcomes' của Laeven–Valencia."""
    path = RAW / "laeven_valencia_crises.xlsx"
    if not path.exists():
        raise FileNotFoundError(f"Thiếu {path} — chạy code/00_probe_bis.py trước")
    d = pd.read_excel(path, sheet_name="Crisis Resolution and Outcomes", header=None)
    d = d.iloc[1:, :11]
    d.columns = ["country", "start", "end", "outloss", "fisc_cost",
                 "fisc_net", "fisc_fs", "peak_liq", "liq_support",
                 "peak_npl", "debt_incr"]
    d = d[d.country.notna()].copy()

    def year_of(x) -> int | None:
        if pd.isna(x):
            return None
        s = re.sub(r"\d+/\s*$", "", str(x)).replace("...", "").strip()
        m = re.match(r"^(\d{4})", s)
        return int(m.group(1)) if m else None

    d["start_y"] = d.start.map(year_of)
    d["end_y"] = d.end.map(year_of)
    d = d.dropna(subset=["start_y"])
    d["cty"] = d.country.str.replace(r"\s+\d+/\s*$", "", regex=True).str.strip()
    d["cty"] = d.cty.map(LV_NAME)
    d = d[d.cty.notna() & d.cty.isin(PANEL21)].copy()
    d = d[d.start_y.between(START_Y, END_Y)]
    for c in ["outloss", "fisc_cost", "peak_npl", "debt_incr"]:
        d[c] = pd.to_numeric(d[c], errors="coerce")
    return d[["cty", "start_y", "end_y", "outloss", "fisc_cost", "peak_npl",
               "debt_incr", "country"]].reset_index(drop=True)


def main() -> int:
    # ---------- 1. lưới quý ----------
    quarters = list(pd.period_range(f"{START_Y}Q1", f"{END_Y}Q4", freq="Q"))
    grid = pd.MultiIndex.from_product(
        [PANEL21, range(len(quarters))], names=["cty", "q"]).to_frame(index=False)
    # quý liên tục: q = year*4 + quarter (khớp q_index của BIS)
    # from_product là cty-major: cty1 x tatca quý, rồi cty2 ...
    grid["q"] = [p.year * 4 + p.quarter for _ in PANEL21 for p in quarters]
    grid["year"] = [p.year for _ in PANEL21 for p in quarters]
    print(f"[1] Lưới: {len(PANEL21)} nước x {len(quarters)} quý = {len(grid):,} dòng")

    # ---------- 2. BIS ----------
    merged = grid.copy()
    for fname, col in [("bis_credit_gap.csv", "credit_gap"),
                       ("bis_credit_gdp_ratio.csv", "credit_gdp_ratio"),
                       ("bis_dsr.csv", "dsr")]:
        d = parse_bis(fname)
        if d is None:
            print(f"    !! thiếu {fname}")
            continue
        if "dsr" in fname:
            # giữ DS_BORROWERS = P (private non-financial sector) cho nhất quán credit gap
            raw = pd.read_csv(RAW / fname)
            raw = raw[(raw.BORROWERS_CTY.isin(PANEL21)) & (raw.DSR_BORROWERS == "P")]
            raw["q"] = raw.TIME_PERIOD.map(q_index)
            raw["OBS_VALUE"] = pd.to_numeric(raw.OBS_VALUE, errors="coerce")
            d = raw[["BORROWERS_CTY", "q", "OBS_VALUE"]].dropna()
            d.columns = ["cty", "q", col]
            d = d[(d.q >= START_Y * 4 + 1) & (d.q <= END_Y * 4 + 4)]
            d = d.groupby(["cty", "q"], as_index=False)[col].mean()
        else:
            d.columns = ["cty", "q", col]
        before = merged[col].notna().sum() if col in merged else 0
        merged = merged.merge(d, on=["cty", "q"], how="left")
        print(f"    {col:20s} {len(d):>5d} quan sát BIS")

    # ---------- 3. LBS per-country ----------
    lbs_files = sorted(RAW.glob("bis_lbs_xborder_*.csv"))
    lbs_parts = []
    for p in lbs_files:
        d = pd.read_csv(p)
        if "L_REP_CTY" not in d.columns:
            continue
        d = d[d.L_REP_CTY.isin(PANEL21)].copy()
        d["q"] = d.TIME_PERIOD.map(q_index)
        d["OBS_VALUE"] = pd.to_numeric(d.OBS_VALUE, errors="coerce")
        lbs_parts.append(d[["L_REP_CTY", "q", "OBS_VALUE"]])
    if lbs_parts:
        lbs = pd.concat(lbs_parts).dropna()
        lbs.columns = ["cty", "q", "xborder_claims_usd_bn"]
        lbs = lbs.groupby(["cty", "q"], as_index=False).mean()
        merged = merged.merge(lbs, on=["cty", "q"], how="left")
        print(f"    xborder_claims_usd_bn {len(lbs):>5d} quan sát "
              f"({lbs.cty.nunique()} nước)")
    else:
        merged["xborder_claims_usd_bn"] = np.nan

    # ---------- 4. World Bank (annual -> quarterly) ----------
    # file wb_*.csv do code/09_download_wb.py tải: cột country, date, value
    WB_VARS = ["gdp_growth", "inflation", "lending_rate", "real_interest_rate",
               "deposit_rate", "gdp_usd", "gdp_real", "exchange_rate", "fdi_net",
               "central_govt_debt_gdp", "revenue_gdp", "expense_gdp",
               "bank_assets_gdp", "bank_capital_assets", "market_capitalization",
               "domestic_credit_gdp", "research_development", "trade_openness",
               "agriculture_va", "industry_va", "services_va"]
    name2iso = {v: k for k, v in WB_NAME.items()}
    wb = None
    for col in WB_VARS:
        f = RAW / f"wb_{col}.csv"
        if not f.exists():
            continue
        e = pd.read_csv(f)
        if "value" not in e.columns:          # file cũ định dạng (country, date, <col>)
            e = e.rename(columns={e.columns[-1]: "value"})
        e = e[["country", "date", "value"]].copy()
        e["cty"] = e.country.map(name2iso)
        e["year"] = e.date.astype(int)
        e = e[e.cty.notna() & e.year.between(START_Y, END_Y)]
        e = e.rename(columns={"value": col})
        e = e.groupby(["cty", "year"], as_index=False)[col].mean()
        wb = e if wb is None else wb.merge(e, on=["cty", "year"], how="outer")
    if wb is None:
        raise FileNotFoundError("Không có file wb_*.csv nào trong data/raw/")
    print(f"    World Bank: {len(wb)} quan sát năm x {wb.cty.nunique()} nuoc")

    # noi suy tuyen tinh CHI giua cac quan sat (limit_area='inside')
    # -> giu NaN o ngoai pham vi du lieu de khong bia gia tri
    for col in WB_VARS:
        if col not in wb.columns:
            continue
        wb[col] = (wb.sort_values(["cty", "year"])
                     .groupby("cty")[col]
                     .transform(lambda x: x.interpolate(method="index", limit_area="inside")))

    merged = merged.merge(
        wb[["cty", "year"] + [c for c in WB_VARS if c in wb.columns]],
        on=["cty", "year"], how="left")

    # ---------- 5. Khủng hoảng từ Laeven–Valencia ----------
    lv = load_lv_crises()
    print(f"[2] LV: {len(lv)} sự kiện khủng hoảng trong {lv.cty.nunique()} nước")

    crisis = np.zeros(len(merged), dtype=int)
    crisis_sev = np.full(len(merged), np.nan)
    q_years = merged.q // 4
    for _, e in lv.iterrows():
        end_y = int(e.end_y) if pd.notna(e.end_y) else int(e.start_y)
        m = ((merged.cty == e.cty) & (q_years >= int(e.start_y)) & (q_years <= end_y))
        crisis[m.to_numpy()] = 1
        sev = e.outloss if pd.notna(e.outloss) else e.peak_npl
        if pd.notna(sev):
            crisis_sev[m.to_numpy()] = float(sev)
    merged["crisis_sys"] = crisis
    merged["crisis_severity"] = crisis_sev

    # ---------- 6. Biến mạng ----------
    # 6a. cơ sở vốn ngân hàng (WB) → sandpile load (thiếu dữ liệu ở nhiều nước)
    if "bank_capital_assets" in merged.columns:
        cap = merged.bank_capital_assets
        merged["sandpile_load"] = (1 - cap / 10).clip(0, 1)
    # 6b. density mạng từ trade openness (WB) — chuẩn hoá trong nước
    if "trade_openness" in merged.columns:
        g = merged.groupby("cty").trade_openness
        lo, hi = g.transform("min"), g.transform("max")
        merged["network_density"] = (merged.trade_openness - lo) / (hi - lo).replace(0, np.nan)
    # 6c. credit growth từ BIS ratio
    if "credit_gdp_ratio" in merged.columns:
        merged = merged.sort_values(["cty", "q"])
        merged["credit_growth"] = (
            merged.groupby("cty").credit_gdp_ratio.pct_change() * 100)
    # 6d. lag/lead khủng hoảng
    merged = merged.sort_values(["cty", "q"])
    merged["crisis_lag1"] = merged.groupby("cty").crisis_sys.shift(1).fillna(0)
    merged["crisis_lead1"] = merged.groupby("cty").crisis_sys.shift(-1).fillna(0)
    merged["pre_crisis"] = ((merged.crisis_lead1 == 1) & (merged.crisis_sys == 0)).astype(int)
    # 6e. tương tác sandpile x network
    if {"sandpile_load", "network_density"} <= set(merged.columns):
        merged["sandpile_network"] = merged.sandpile_load * merged.network_density

    merged = merged.sort_values(["cty", "q"]).reset_index(drop=True)
    merged["iso3"] = merged.cty.map(ISO3)
    merged["country"] = merged.cty.map(WB_NAME)

    # ---------- 7. Lưu ----------
    out = PROC / "ifwst_panel_quarterly.csv"
    merged.to_csv(out, index=False)
    print(f"\n[3] Lưu: {out.relative_to(ROOT)}  shape={merged.shape}")

    # ---------- 8. Báo cáo độ phủ ----------
    print("\n=== ĐỘ PHỦ (tỉ lệ quan sát THẬT, không điền median) ===")
    for c in ["credit_gap", "credit_gdp_ratio", "dsr", "xborder_claims_usd_bn",
              "gdp_growth", "inflation", "bank_capital_assets",
              "bank_assets_gdp", "trade_openness", "domestic_credit_gdp"]:
        if c in merged.columns:
            n = merged[c].notna().sum()
            print(f"  {c:24s} {n:>5d}/{len(merged)}  ({100*n/len(merged):5.1f}%)")

    print("\n=== QUAN SÁT THEO NƯỚC ===")
    cov = (merged.groupby("country")
           .agg(credit_gap=("credit_gap", lambda s: s.notna().sum()),
                dsr=("dsr", "count"),
                lbs=("xborder_claims_usd_bn", "count"),
                gdp_growth=("gdp_growth", "count"),
                crisis_q=("crisis_sys", "sum")))
    cov["n_obs_total"] = merged.groupby("country").size()
    print(cov.to_string())

    print("\n=== KHỦNG HOẢNG (quý) ===")
    per_country = merged.groupby("country").crisis_sys.sum()
    print(per_country[per_country > 0].to_string())
    print(f"\n  Tổng quy khủng hoảng: {merged.crisis_sys.sum()}")
    print(f"  Sự kiện LV (start-year): {len(lv)}")
    print(f"  Nước có khủng hoảng: {(per_country>0).sum()}/{len(PANEL21)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
