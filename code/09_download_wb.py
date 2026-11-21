#!/usr/bin/env python
"""
B2 — Tải lại World Bank cho bộ 21 nước panel MỚI (NL, SE thay BG, RO).

File WB cũ (data/raw/wb_*.csv) được tải cho bộ 21 nước cũ (có BGR, ROU;
thiếu NLD, SWE). Script này tải lại cho bộ chốt cuối, ghi đè.

Chạy:  python code/09_download_wb.py
"""

from __future__ import annotations

import io
import json
import sys
import time
import urllib.request
from pathlib import Path

import pandas as pd

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")

# 21 nước panel cuối cùng — dùng mã ISO-2 mà World Bank API chấp nhận
COUNTRIES = ["BR", "CA", "CH", "CN", "CZ", "DE", "FR", "GB", "HU", "ID", "IN",
             "IT", "JP", "KR", "MX", "NL", "PL", "RU", "SE", "TR", "US"]

# indicator -> tên cột trong data/raw
INDICATORS = {
    "NY.GDP.MKTP.KD.ZG": "gdp_growth",
    "FP.CPI.TOTL.ZG": "inflation",
    "FB.BNK.CAPA.ZS": "bank_capital_assets",
    "FB.AST.NPLO.ZS": "npl_total_loans",
    "FS.LBL.LIQU.GD.ZS": "liquid_liabilities_gdp",
    "CM.MKT.LCAP.GD.ZS": "market_capitalization",
    "FS.AST.DOMS.GD.ZS": "domestic_credit_gdp",
    "GB.XPD.RSDV.GD.ZS": "research_development",
    "NE.EXP.GNFS.ZS": "trade_openness",
    "FB.AST.NPER.ZS": "bank_assets_gdp",
    "FR.INR.LEND": "lending_rate",
    "FR.INR.DPST": "deposit_rate",
    "FR.INR.RINR": "real_interest_rate",
    "PA.NUS.FCRF": "exchange_rate",
    "NY.GDP.MKTP.CD": "gdp_usd",
    "NY.GDP.MKTP.KD": "gdp_real",
    "BX.KLT.DINV.CD.WD": "fdi_net",
    "GC.DOD.TOTL.GD.ZS": "central_govt_debt_gdp",
    "GC.REV.XGRT.GD.ZS": "revenue_gdp",
    "GC.XPN.TOTL.GD.ZS": "expense_gdp",
    "NV.AGR.TOTL.ZS": "agriculture_va",
    "NV.IND.TOTL.ZS": "industry_va",
    "NV.SRV.TOTL.ZS": "services_va",
}

# chỉ số WB đã tải trước đó dưới tên khác — giữ để không mất dữ liệu
LEGACY = {
    "wb_gdp_growth.csv": "gdp_growth",
    "wb_inflation.csv": "inflation",
    "wb_bank_capital_assets.csv": "bank_capital_assets",
    "wb_market_capitalization.csv": "market_capitalization",
    "wb_domestic_credit_gdp.csv": "domestic_credit_gdp",
    "wb_trade_openness.csv": "trade_openness",
    "wb_lending_rate.csv": "lending_rate",
    "wb_deposit_rate.csv": "deposit_rate",
    "wb_real_interest_rate.csv": "real_interest_rate",
    "wb_exchange_rate.csv": "exchange_rate",
    "wb_gdp_usd.csv": "gdp_usd",
    "wb_gdp_real.csv": "gdp_real",
    "wb_fdi_net.csv": "fdi_net",
    "wb_central_govt_debt_gdp.csv": "central_govt_debt_gdp",
    "wb_revenue_gdp.csv": "revenue_gdp",
    "wb_expense_gdp.csv": "expense_gdp",
    "wb_bank_assets_gdp.csv": "bank_assets_gdp",
}


def fetch_indicator(code: str) -> pd.DataFrame | None:
    """Tải 1 indicator cho 21 nước qua World Bank API (JSON), trả DataFrame dạng long."""
    url = (f"https://api.worldbank.org/v2/country/"
           f"{';'.join(COUNTRIES)}/indicator/{code}"
           f"?format=json&per_page=20000&date=1990:2023")
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for attempt in range(1, 4):
        try:
            with urllib.request.urlopen(req, timeout=90) as resp:
                payload = json.loads(resp.read().decode("utf-8", errors="ignore"))
            break
        except Exception as exc:  # noqa: BLE001
            print(f"    attempt {attempt}: {type(exc).__name__}: {exc}")
            payload = None
            time.sleep(2 ** attempt)
    if not payload or len(payload) < 2 or payload[1] is None:
        return None
    rows = []
    for item in payload[1]:
        if item.get("value") is None:
            continue
        rows.append({"country": item["country"]["value"],
                     "date": str(item["date"]),
                     "value": item["value"]})
    if not rows:
        return None
    return pd.DataFrame(rows)


def load_legacy(fname: str) -> pd.DataFrame | None:
    p = RAW / fname
    if not p.exists():
        return None
    try:
        df = pd.read_csv(p)
    except Exception:  # noqa: BLE001
        return None
    if df.shape[1] < 3:
        return None
    df.columns = ["country", "date", "value"]
    df["date"] = df.date.astype(str)
    return df


def main() -> int:
    RAW.mkdir(parents=True, exist_ok=True)
    print(f"=== World Bank — {len(COUNTRIES)} nước, 1990-2023 ===\n")

    for code, col in INDICATORS.items():
        df = fetch_indicator(code)
        if df is None:
            print(f"  {col:26s} FAIL")
            continue
        n_cty = df.country.nunique()
        out = RAW / f"wb_{col}.csv"
        df.to_csv(out, index=False)
        print(f"  {col:26s} {len(df):>5d} obs | {n_cty:>2d} nước | wb_{col}.csv")

    # file cũ tải cho bộ nước cũ — bổ sung nước mới (NL, SE) nếu có
    print("\n=== Bổ sung NL/SE cho file WB cũ (nếu API trong lô trên chưa đủ) ===")
    for fname, col in LEGACY.items():
        p = RAW / fname
        old = load_legacy(fname)
        if old is None:
            continue
        have = set(old.country)
        missing = [c for c in COUNTRIES if c not in have]
        if not missing:
            print(f"  {fname:34s} OK (đủ 21 nước)")
            continue
        df = fetch_indicator(code=code_for(col))
        if df is None:
            print(f"  {fname:34s} thiếu {missing} — API fail")
            continue
        add = df[df.country.isin(missing)]
        if add.empty:
            print(f"  {fname:34s} thiếu {missing} — API không có dữ liệu")
            continue
        merged = pd.concat([old, add], ignore_index=True)
        merged.to_csv(p, index=False)
        print(f"  {fname:34s} +{len(add)} dòng cho {missing}")

    return 0


def code_for(col: str) -> str:
    for c, name in INDICATORS.items():
        if name == col:
            return c
    return ""


if __name__ == "__main__":
    sys.exit(main())
