"""
STEP 7: Tính Derived Variables (v2)
- Load all individual CSV files properly
- Calculate derived variables
"""
import os
import pandas as pd
import numpy as np

RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"
os.makedirs(PROCESSED_DIR, exist_ok=True)

print("=" * 60)
print("STEP 7: Tính Derived Variables (v2)")
print("=" * 60)

# Target countries
COUNTRIES = [
    "USA", "GBR", "DEU", "FRA", "JPN", "ITA", "CAN", "CHE",
    "CHN", "IND", "BRA", "MEX", "RUS", "TUR", "KOR", "IDN",
    "POL", "HUN", "CZE", "ROU", "BGR"
]

# ========================================
# 1. Load and merge individual variables
# ========================================
print("\n[1] Loading individual variables...")

variables = {}

# Key variables to load
key_files = {
    "domestic_credit_gdp": "wb_domestic_credit_gdp.csv",
    "bank_assets_gdp": "wb_bank_assets_gdp.csv",
    "bank_capital_assets": "wb_bank_capital_assets.csv",
    "gdp_growth": "wb_gdp_growth.csv",
    "inflation": "wb_inflation.csv",
    "trade_openness": "wb_trade_openness.csv",
    "market_cap": "wb_market_capitalization.csv",
}

for var_name, filename in key_files.items():
    filepath = f"{RAW_DIR}/{filename}"
    if os.path.exists(filepath):
        try:
            df = pd.read_csv(filepath, index_col=[0, 1])
            df = df.reset_index()
            df.columns = ['country', 'date', var_name]
            variables[var_name] = df
            print(f"  {var_name}: {len(df)} obs")
        except Exception as e:
            print(f"  {var_name}: Error - {e}")

# ========================================
# 2. Merge all variables
# ========================================
print("\n[2] Merging variables...")

# Start with first variable
first_var = list(variables.keys())[0]
merged = variables[first_var].copy()
merged["date"] = merged["date"].astype(int).astype(str)

for var_name, df in list(variables.items())[1:]:
    df = df.copy()
    df["date"] = df["date"].astype(int).astype(str)
    merged = merged.merge(df, on=["country", "date"], how="outer")

print(f"  Merged: {merged.shape}")

# Filter to target countries
merged = merged[merged["country"].isin(COUNTRIES)]
print(f"  After filter: {merged.shape}")

# ========================================
# 3. Calculate Credit Gap
# ========================================
print("\n[3] Calculating Credit Gap...")

if "domestic_credit_gdp" in merged.columns:
    merged = merged.sort_values(["country", "date"])
    merged["credit_gap"] = merged.groupby("country")["domestic_credit_gdp"].transform(
        lambda x: x - x.rolling(window=5, min_periods=2, center=True).mean()
    )
    merged["credit_gap"] = merged["credit_gap"].fillna(0)
    print(f"  credit_gap: calculated")

# ========================================
# 4. Calculate Sandpile Load
# ========================================
print("\n[4] Calculating Sandpile Load...")

if "bank_capital_assets" in merged.columns:
    # Capital adequacy proxy (higher = more stable)
    capital = merged["bank_capital_assets"].fillna(8)
    merged["sandpile_load"] = 1 - (capital / 10)  # Normalize
    merged["sandpile_load"] = merged["sandpile_load"].clip(0, 1)

    # Cumulative stress
    merged["sandpile_cumulative"] = merged.groupby("country")["sandpile_load"].cumsum()
    print(f"  sandpile_load: calculated")

# ========================================
# 5. Network Density
# ========================================
print("\n[5] Calculating Network Density...")

if "trade_openness" in merged.columns:
    max_trade = merged["trade_openness"].max()
    merged["network_density"] = merged["trade_openness"] / max_trade
    print(f"  network_density: calculated")

# ========================================
# 6. Regime
# ========================================
print("\n[6] Calculating Regime...")

if "gdp_growth" in merged.columns:
    merged["regime"] = (merged["gdp_growth"] > 0).astype(int)
    print(f"  regime: calculated")

# ========================================
# 7. Add Crisis Indicator
# ========================================
print("\n[7] Adding Crisis Indicator...")

crisis = pd.read_csv(f"{RAW_DIR}/crisis_dates_annual.csv")
crisis["date"] = crisis["year"].astype(str)

merged = merged.merge(
    crisis[["country", "date", "crisis_sys"]],
    on=["country", "date"],
    how="left"
)
merged["crisis_sys"] = merged["crisis_sys"].fillna(0).astype(int)
print(f"  crisis_sys: added")

# ========================================
# 8. Save
# ========================================
print("\n[8] Saving...")

final_cols = [
    "country", "date",
    "domestic_credit_gdp", "credit_gap",
    "bank_assets_gdp", "bank_capital_assets",
    "gdp_growth", "inflation",
    "trade_openness", "network_density",
    "sandpile_load", "sandpile_cumulative",
    "regime", "crisis_sys"
]

existing = [c for c in final_cols if c in merged.columns]
df_final = merged[existing].copy()
df_final = df_final.sort_values(["country", "date"])

df_final.to_csv(f"{PROCESSED_DIR}/variables_derived.csv", index=False)
print(f"  Saved: {PROCESSED_DIR}/variables_derived.csv")

# ========================================
# Summary
# ========================================
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"  Countries: {df_final['country'].nunique()}")
print(f"  Time: {df_final['date'].min()} - {df_final['date'].max()}")
print(f"  Observations: {len(df_final)}")
print(f"  Variables: {len(df_final.columns)}")

print("\n  Missing:")
for col in df_final.columns:
    miss = df_final[col].isna().sum()
    pct = miss / len(df_final) * 100
    print(f"    {col}: {miss} ({pct:.1f}%)")

print("\n  Sample:")
print(df_final.head(10).to_string())

print("\nSTEP 7 COMPLETE")
