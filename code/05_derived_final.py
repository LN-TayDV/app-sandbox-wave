"""
STEP 7: Tính Derived Variables (Final)
- Use correct country names
"""
import os
import pandas as pd
import numpy as np

RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"
os.makedirs(PROCESSED_DIR, exist_ok=True)

print("=" * 60)
print("STEP 7: Tính Derived Variables")
print("=" * 60)

# Country mapping (ISO code to full name)
COUNTRY_MAP = {
    "USA": "United States",
    "GBR": "United Kingdom",
    "DEU": "Germany",
    "FRA": "France",
    "JPN": "Japan",
    "ITA": "Italy",
    "CAN": "Canada",
    "CHE": "Switzerland",
    "CHN": "China",
    "IND": "India",
    "BRA": "Brazil",
    "MEX": "Mexico",
    "RUS": "Russian Federation",
    "TUR": "Turkiye",
    "KOR": "Korea, Rep.",
    "IDN": "Indonesia",
    "POL": "Poland",
    "HUN": "Hungary",
    "CZE": "Czechia",
    "ROU": "Romania",
    "BGR": "Bulgaria",
}

TARGET_COUNTRIES = list(COUNTRY_MAP.values())

# ========================================
# 1. Load variables
# ========================================
print("\n[1] Loading variables...")

key_files = {
    "domestic_credit_gdp": "wb_domestic_credit_gdp.csv",
    "bank_assets_gdp": "wb_bank_assets_gdp.csv",
    "bank_capital_assets": "wb_bank_capital_assets.csv",
    "gdp_growth": "wb_gdp_growth.csv",
    "inflation": "wb_inflation.csv",
    "trade_openness": "wb_trade_openness.csv",
    "market_cap": "wb_market_capitalization.csv",
}

variables = {}
for var_name, filename in key_files.items():
    filepath = f"{RAW_DIR}/{filename}"
    if os.path.exists(filepath):
        df = pd.read_csv(filepath, index_col=[0, 1])
        df = df.reset_index()
        df.columns = ['country', 'date', var_name]
        df["date"] = df["date"].astype(int).astype(str)
        variables[var_name] = df

# ========================================
# 2. Merge
# ========================================
print("\n[2] Merging...")

first_var = list(variables.keys())[0]
merged = variables[first_var].copy()

for var_name in list(variables.keys())[1:]:
    merged = merged.merge(variables[var_name], on=["country", "date"], how="outer")

# Filter to target countries
merged = merged[merged["country"].isin(TARGET_COUNTRIES)]
merged = merged.sort_values(["country", "date"])
print(f"  Shape: {merged.shape}")

# ========================================
# 3. Credit Gap
# ========================================
print("\n[3] Credit Gap...")

if "domestic_credit_gdp" in merged.columns:
    merged["credit_gap"] = merged.groupby("country")["domestic_credit_gdp"].transform(
        lambda x: x - x.rolling(5, min_periods=2, center=True).mean()
    ).fillna(0)

# ========================================
# 4. Sandpile Load
# ========================================
print("\n[4] Sandpile Load...")

if "bank_capital_assets" in merged.columns:
    capital = merged["bank_capital_assets"].fillna(8)
    merged["sandpile_load"] = (1 - capital / 10).clip(0, 1)
    merged["sandpile_cumulative"] = merged.groupby("country")["sandpile_load"].cumsum()

# ========================================
# 5. Network Density
# ========================================
print("\n[5] Network Density...")

if "trade_openness" in merged.columns:
    merged["network_density"] = merged["trade_openness"] / merged["trade_openness"].max()

# ========================================
# 6. Regime
# ========================================
print("\n[6] Regime...")

if "gdp_growth" in merged.columns:
    merged["regime"] = (merged["gdp_growth"] > 0).astype(int)

# ========================================
# 7. Crisis
# ========================================
print("\n[7] Crisis...")

crisis = pd.read_csv(f"{RAW_DIR}/crisis_dates_annual.csv")
crisis["date"] = crisis["year"].astype(str)
# Map country names
crisis["country"] = crisis["country"].replace(COUNTRY_MAP)

merged = merged.merge(crisis[["country", "date", "crisis_sys"]], on=["country", "date"], how="left")
merged["crisis_sys"] = merged["crisis_sys"].fillna(0).astype(int)

# ========================================
# 8. Save
# ========================================
print("\n[8] Saving...")

cols = ["country", "date", "domestic_credit_gdp", "credit_gap", "bank_assets_gdp",
        "bank_capital_assets", "gdp_growth", "inflation", "trade_openness",
        "network_density", "sandpile_load", "sandpile_cumulative", "regime", "crisis_sys"]

existing = [c for c in cols if c in merged.columns]
df_final = merged[existing].copy()

df_final.to_csv(f"{PROCESSED_DIR}/variables_derived.csv", index=False)

# ========================================
# Summary
# ========================================
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"Countries: {df_final['country'].nunique()}")
print(f"Time: {df_final['date'].min()} - {df_final['date'].max()}")
print(f"Obs: {len(df_final)}")
print(f"Vars: {len(df_final.columns)}")

print("\nMissing:")
for c in df_final.columns:
    m = df_final[c].isna().sum()
    print(f"  {c}: {m}")

print("\nSample:")
print(df_final.head(10).to_string())

print("\nSTEP 7 COMPLETE")
