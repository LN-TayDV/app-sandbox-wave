"""
STEP 4: Download Cross-border Banking Data
- BIS Cross-border claims
- IMF Financial Soundness Indicators
- World Bank additional financial indicators
"""
import os
import pandas as pd
import requests
import wbdata
import datetime

RAW_DIR = "data/raw"
os.makedirs(RAW_DIR, exist_ok=True)

print("=" * 60)
print("STEP 4: Download Cross-border + FSI data")
print("=" * 60)

# Method 1: Try BIS Locational Banking Statistics
# These are publicly available CSV files
print("\n[1] Trying BIS Locational Banking Statistics...")

bis_urls = {
    "bis_lbs": "https://www.bis.org/statistics/full_lbs_d_csv/data.csv",
    "bis_cbs_consolidated": "https://www.bis.org/statistics/full_cbs_c_csv/data.csv",
    "bis_debt_sec": "https://www.bis.org/statistics/full_debt_sec_csv/data.csv",
}

for name, url in bis_urls.items():
    try:
        r = requests.get(url, timeout=30, headers={"User-Agent": "Mozilla/5.0"})
        print(f"  {name}: status={r.status_code}, size={len(r.content)}")
        if r.status_code == 200 and len(r.content) > 1000 and "csv" in r.headers.get("content-type", "").lower():
            with open(f"{RAW_DIR}/{name}.csv", "wb") as f:
                f.write(r.content)
            print(f"    Saved {name}.csv")
    except Exception as e:
        print(f"  {name}: Error {e}")

# Method 2: IMF Financial Soundness Indicators
print("\n[2] Trying IMF Financial Soundness Indicators...")
fsi_indicators = {
    "FSANL_PT": "npl_ratio",  # Non-performing loans
    "FSCBN_DC": "deposits_to_credit",  # Bank deposits / credit
    "FSE_LAR_LAR": "liquid_assets_ratio",  # Liquid assets
    "FS_LAR_LAR": "liquid_assets_total",
    "FCB_LAR_LAR": "bank_liquid_assets",
    "FCB_FEE_FEE": "bank_fees",
    "FCB_DEB_DEB": "bank_deposits",
}

target_countries = [
    "USA", "GBR", "DEU", "FRA", "JPN", "ITA", "CAN", "CHE",
    "CHN", "IND", "BRA", "MEX", "RUS", "TUR", "KOR", "IDN",
    "POL", "HUN", "CZE", "ROU", "BGR"
]

# Try IMF API
print("\n[3] Trying IMF SDMX API for FSI...")
imf_url = "https://dataservices.imf.org/REST/SDMX_JSON.svc/CompactData/FSI"
try:
    r = requests.get(imf_url, params={"startPeriod": "2000", "endPeriod": "2024"},
                     timeout=30, headers={"User-Agent": "Mozilla/5.0"})
    print(f"  IMF FSI: status={r.status_code}, size={len(r.content)}")
    if r.status_code == 200:
        with open(f"{RAW_DIR}/imf_fsi_test.json", "wb") as f:
            f.write(r.content)
        print(f"    Saved imf_fsi_test.json")
except Exception as e:
    print(f"  Error: {e}")

# Method 3: World Bank additional indicators (capital adequacy, bank profitability)
print("\n[4] World Bank additional indicators...")
wb_indicators = {
    "FB.BNK.CAPA.ZS": "bank_capital_assets",
    "FB.AST.NPLO.ZS": "npl_total_loans",
    "FB.BNK.BOTB.ZS": "borrowers_bank",
    "FB.BNK.CBKR.ZS": "central_bank_assets",
    "FS.LBL.LIQU.GD.ZS": "liquid_liabilities_gdp",
    "GB.XPD.RSDV.GD.ZS": "research_development",
    "CM.MKT.LDOM.NO": "listed_domestic_companies",
    "CM.MKT.LCAP.GD.ZS": "market_capitalization",
}

# Filter to only working ones (skip the ones we know are broken)
working_indicators = {
    "FB.BNK.CAPA.ZS": "bank_capital_assets",
    "FB.AST.NPLO.ZS": "npl_total_loans",
    "FS.LBL.LIQU.GD.ZS": "liquid_liabilities_gdp",
    "CM.MKT.LCAP.GD.ZS": "market_capitalization",
}

for ind_code, ind_name in working_indicators.items():
    try:
        df = wbdata.get_dataframe(
            {ind_code: ind_name},
            country=target_countries
        )
        if len(df) > 0:
            df.to_csv(f"{RAW_DIR}/wb_{ind_name}.csv")
            print(f"  {ind_name}: {df.shape[0]} obs, missing={df.iloc[:,0].isna().sum()}")
        else:
            print(f"  {ind_name}: No data")
    except Exception as e:
        print(f"  {ind_name}: Error {str(e)[:80]}")

# Method 4: Build a synthetic cross-border network from BIS data structure
# Even if we cannot download BIS directly, we can construct expected network
print("\n[5] Building network topology from World Bank data...")

# Use a simple cross-border approximation
# Real cross-border requires BIS, but we can use:
# 1. Trade openness as proxy
# 2. Financial development as proxy

try:
    df_trade = wbdata.get_dataframe(
        {"NE.TRD.GNFS.ZS": "trade_openness"},
        country=target_countries
    )
    df_trade.to_csv(f"{RAW_DIR}/wb_trade_openness.csv")
    print(f"  trade_openness: {df_trade.shape[0]} obs")
except Exception as e:
    print(f"  trade_openness: Error {e}")

# Final summary
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
import os
for f in sorted(os.listdir(RAW_DIR)):
    size = os.path.getsize(f"{RAW_DIR}/{f}")
    print(f"  {f}: {size:,} bytes")
print("\nSTEP 4 COMPLETE")
