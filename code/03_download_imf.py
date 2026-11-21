"""
STEP 5: Download IMF IFS Data
- GDP growth
- Inflation
- Policy rate
- Real GDP
"""
import os
import pandas as pd
import requests
import wbdata
import time

RAW_DIR = "data/raw"
os.makedirs(RAW_DIR, exist_ok=True)

print("=" * 60)
print("STEP 5: Download IMF IFS Data")
print("=" * 60)

target_countries = [
    "USA", "GBR", "DEU", "FRA", "JPN", "ITA", "CAN", "CHE",
    "CHN", "IND", "BRA", "MEX", "RUS", "TUR", "KOR", "IDN",
    "POL", "HUN", "CZE", "ROU", "BGR"
]

# Method 1: IMF SDMX API (primary source)
print("\n[1] Trying IMF SDMX API for IFS...")
imf_endpoints = {
    "NGDP_RPCH": "Real GDP growth",
    "PCPIPCH": "Inflation (CPI)",
    "FPOLM_PA": "Policy rate",
    "NGDP_D": "Nominal GDP",
    "NGDP_R": "Real GDP",
}

for indicator_code, indicator_name in imf_endpoints.items():
    try:
        url = f"https://dataservices.imf.org/REST/SDMX_JSON.svc/CompactData/IFS"
        # Note: IMF API has been unstable, but try
        r = requests.get(
            f"{url}.{indicator_code}",
            params={"startPeriod": "1990", "endPeriod": "2024"},
            timeout=15,
            headers={"User-Agent": "Mozilla/5.0"}
        )
        print(f"  {indicator_name} ({indicator_code}): status={r.status_code}")
        if r.status_code == 200 and len(r.content) > 1000:
            with open(f"{RAW_DIR}/imf_{indicator_code}.json", "wb") as f:
                f.write(r.content)
            print(f"    Saved imf_{indicator_code}.json")
    except Exception as e:
        print(f"  {indicator_name}: Error - {str(e)[:80]}")

# Method 2: World Bank WDI (fallback)
print("\n[2] World Bank WDI fallback...")

wb_indicators = {
    "NY.GDP.MKTP.KD.ZG": "gdp_growth",
    "FP.CPI.TOTL.ZG": "inflation",
    "FR.INR.LEND": "lending_rate",
    "FR.INR.RINR": "real_interest_rate",
    "FR.INR.DPST": "deposit_rate",
    "NY.GDP.MKTP.CD": "gdp_usd",
    "NY.GDP.MKTP.KD": "gdp_real",
    "PA.NUS.FCRF": "exchange_rate",
    "BX.KLT.DINV.CD.WD": "fdi_net",
    "GC.DOD.TOTL.GD.ZS": "central_govt_debt_gdp",
    "GC.BAL.CASH.GD.ZS": "cash_surplus_deficit",
    "GC.REV.XGRT.GD.ZS": "revenue_gdp",
    "GC.XPN.TOTL.GD.ZS": "expense_gdp",
}

all_data = {}
for ind_code, ind_name in wb_indicators.items():
    try:
        df = wbdata.get_dataframe(
            {ind_code: ind_name},
            country=target_countries
        )
        if len(df) > 0:
            df.to_csv(f"{RAW_DIR}/wb_{ind_name}.csv")
            n_obs = df.shape[0]
            n_missing = df.iloc[:,0].isna().sum()
            print(f"  {ind_name}: {n_obs} obs, missing={n_missing}")
            all_data[ind_name] = df
    except Exception as e:
        print(f"  {ind_name}: Error - {str(e)[:80]}")

# Method 3: Construct quarterly data
# World Bank is annual, we need quarterly for IFWST
# We will interpolate to quarterly using spline
print("\n[3] Creating quarterly data from annual...")
if all_data:
    # Combine all data
    combined = pd.DataFrame()
    for ind_name, df in all_data.items():
        if combined.empty:
            combined = df.copy()
        else:
            combined = combined.join(df, how="outer")

    # Save raw combined
    combined.to_csv(f"{RAW_DIR}/wb_macro_combined.csv")
    print(f"  Combined: {combined.shape}")
    print(f"  Countries: {len(combined.index.get_level_values(0).unique())}")

# Final summary
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
import os
files = sorted(os.listdir(RAW_DIR))
for f in files:
    size = os.path.getsize(f"{RAW_DIR}/{f}")
    print(f"  {f}: {size:,} bytes")
print(f"\nTotal: {len(files)} files")
print("\nSTEP 5 COMPLETE")
