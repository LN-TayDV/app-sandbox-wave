"""
STEP 3: Download BIS Credit Statistics
- Credit-to-GDP gaps
- Property price gaps
- Debt Service Ratios
"""
import os
import sys
import pandas as pd
import requests
import time

RAW_DIR = "data/raw"
os.makedirs(RAW_DIR, exist_ok=True)

# BIS has public data for credit-to-GDP gaps (only one-sided HP filter)
# We will attempt to fetch the data
print("=" * 60)
print("STEP 3: Download BIS Credit Statistics")
print("=" * 60)

# BIS provides several Excel files publicly
# Method: Try direct CSV/Excel download
urls = {
    "credit_gdp": "https://www.bis.org/statistics/full_credit_gap_csv/data.csv",
    "dsr": "https://www.bis.org/statistics/full_dsr_csv/data.csv",
    "property": "https://www.bis.org/statistics/full_property_prices_csv/data.csv",
}

# Alternative: Use BIS SDMX REST API
# Note: BIS often requires registration, but some public data is available

results = {}
for name, url in urls.items():
    print(f"\n[*] Trying {name}: {url}")
    try:
        r = requests.get(url, timeout=30, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        })
        print(f"    Status: {r.status_code}")
        print(f"    Size: {len(r.content)} bytes")
        if r.status_code == 200 and len(r.content) > 100:
            results[name] = r.content
    except Exception as e:
        print(f"    Error: {e}")

# If direct URLs fail, we will construct data from alternative sources
# Using World Bank API which is more accessible
print("\n" + "=" * 60)
print("FALLBACK: Using World Bank API")
print("=" * 60)

# World Bank API for credit-to-GDP
# Note: This is proxy data - actual BIS data requires registration
# We'll create a dataset from WB financial development indicators

import wbdata
import datetime

indicators = {
    "FB.AST.NPER.ZS": "bank_assets_gdp",
    "FS.AST.DOMS.GD.ZS": "domestic_credit_gdp",
    "FB.CBK.BRWR.PR.ZS": "borrowers",
    "FS.LBL.LIQU.GD.ZS": "liquid_liabilities",
}

# Test
print("\n[*] Testing World Bank API...")
try:
    # Get data for a single country
    data = wbdata.get_dataframe(
        {"FS.AST.DOMS.GD.ZS": "domestic_credit_gdp"},
        country=["USA", "GBR", "DEU"]
    )
    print(f"    Sample data:\n{data.head()}")
    print(f"    Shape: {data.shape}")

    # Save sample
    data.to_csv(f"{RAW_DIR}/wb_test_credit.csv")
    print(f"    Saved to {RAW_DIR}/wb_test_credit.csv")
except Exception as e:
    print(f"    Error: {e}")

# Download for all IFWST target countries
target_countries = [
    "USA", "GBR", "DEU", "FRA", "JPN", "ITA", "CAN", "CHE",
    "CHN", "IND", "BRA", "MEX", "RUS", "TUR", "KOR", "IDN",
    "POL", "HUN", "CZE", "ROU", "BGR"
]

print("\n[*] Downloading for all target countries...")
all_data = {}
for ind_code, ind_name in indicators.items():
    try:
        df = wbdata.get_dataframe(
            {ind_code: ind_name},
            country=target_countries
        )
        all_data[ind_name] = df
        df.to_csv(f"{RAW_DIR}/wb_{ind_name}.csv")
        print(f"    {ind_name}: {df.shape[0]} obs")
    except Exception as e:
        print(f"    {ind_name}: Error {e}")

# Print summary
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
for name, df in all_data.items():
    print(f"{name}: {df.shape}, missing={df.iloc[:,0].isna().sum()}")
print(f"\nFiles saved in: {RAW_DIR}/")
print("STEP 3 COMPLETE")
