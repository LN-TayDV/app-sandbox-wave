"""
STEP 8: Create Panel Dataset
- Merge all variables into final panel
- Handle missing data
- Create analysis-ready dataset
"""
import os
import pandas as pd
import numpy as np

PROCESSED_DIR = "data/processed"
OUTPUT_DIR = "output"

print("=" * 60)
print("STEP 8: Create Panel Dataset")
print("=" * 60)

# ========================================
# 1. Load derived variables
# ========================================
print("\n[1] Loading derived variables...")

df = pd.read_csv(f"{PROCESSED_DIR}/variables_derived.csv")
print(f"  Shape: {df.shape}")
print(f"  Countries: {df['country'].nunique()}")

# ========================================
# 2. Filter to relevant period
# ========================================
print("\n[2] Filtering to analysis period...")

# Focus on 1990-2023 (more data availability)
df["date"] = df["date"].astype(int)
df = df[(df["date"] >= 1990) & (df["date"] <= 2023)]
print(f"  After filter: {df.shape}")

# ========================================
# 3. Handle Missing Data
# ========================================
print("\n[3] Handling missing data...")

# Forward fill within each country for financial variables
financial_vars = ["domestic_credit_gdp", "bank_assets_gdp", "bank_capital_assets",
                 "trade_openness", "network_density"]

for var in financial_vars:
    if var in df.columns:
        df[var] = df.groupby("country")[var].transform(lambda x: x.ffill().bfill())

# Fill remaining with median
for col in df.columns:
    if df[col].dtype in [float, int] and col not in ["country", "date", "regime", "crisis_sys"]:
        median_val = df[col].median()
        df[col] = df[col].fillna(median_val)

print("  Missing after handling:")
for col in df.columns:
    m = df[col].isna().sum()
    if m > 0:
        print(f"    {col}: {m}")

# ========================================
# 4. Create additional variables
# ========================================
print("\n[4] Creating additional variables...")

# Crisis lag (lead/lag of crisis)
df["crisis_lag1"] = df.groupby("country")["crisis_sys"].shift(1).fillna(0)
df["crisis_lead1"] = df.groupby("country")["crisis_sys"].shift(-1).fillna(0)

# Credit growth
df["credit_growth"] = df.groupby("country")["domestic_credit_gdp"].pct_change().fillna(0)

# Interaction: sandpile × network
df["sandpile_network"] = df["sandpile_load"] * df["network_density"]

# Pre-crisis indicator (2 years before crisis)
df["pre_crisis"] = ((df["crisis_lead1"] == 1) & (df["crisis_sys"] == 0)).astype(int)

# ========================================
# 5. Summary Statistics
# ========================================
print("\n[5] Summary statistics...")

print("\n  By variable:")
for col in ["domestic_credit_gdp", "gdp_growth", "inflation", "sandpile_load", "network_density", "crisis_sys"]:
    if col in df.columns:
        mean = df[col].mean()
        std = df[col].std()
        min_v = df[col].min()
        max_v = df[col].max()
        print(f"    {col}: mean={mean:.2f}, std={std:.2f}, min={min_v:.2f}, max={max_v:.2f}")

# ========================================
# 6. Crisis distribution
# ========================================
print("\n[6] Crisis distribution:")
crisis_by_year = df.groupby("date")["crisis_sys"].sum()
print(f"  Total crisis-years: {crisis_by_year.sum()}")
print(f"  Crisis years: {crisis_by_year[crisis_by_year > 0].index.tolist()}")

# ========================================
# 7. Save final panel
# ========================================
print("\n[7] Saving panel...")

# Sort
df = df.sort_values(["country", "date"])

# Save
df.to_csv(f"{PROCESSED_DIR}/ifwst_panel.csv", index=False)
print(f"  Saved: {PROCESSED_DIR}/ifwst_panel.csv")

# Also save summary
summary = df.describe()
summary.to_csv(f"{OUTPUT_DIR}/panel_summary.csv")
print(f"  Summary: {OUTPUT_DIR}/panel_summary.csv")

# ========================================
# Summary
# ========================================
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"Countries: {df['country'].nunique()}")
print(f"Years: {df['date'].min()} - {df['date'].max()}")
print(f"Observations: {len(df)}")
print(f"Variables: {len(df.columns)}")

print("\n  Columns:")
for col in df.columns:
    print(f"    - {col}")

print("\n  Sample (last 5):")
print(df.tail().to_string())

print("\nSTEP 8 COMPLETE")
