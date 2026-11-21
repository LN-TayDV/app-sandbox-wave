"""
STEP 7: Tính Derived Variables (Simplified)
- Credit gap
- Sandpile load
- Network density
- Regime indicators
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

# Load macro combined data
print("\n[1] Loading macro data...")
df = pd.read_csv(f"{RAW_DIR}/wb_macro_combined.csv")
print(f"  Shape: {df.shape}")
print(f"  Columns: {df.columns.tolist()}")

# Get country list
countries = df.index.get_level_values(0).unique().tolist()
print(f"  Countries: {len(countries)}")

# ========================================
# 1. Calculate Credit Gap (rolling deviation)
# ========================================
print("\n[2] Calculating Credit Gap...")

if "domestic_credit_gdp" in df.columns:
    # Use rolling mean deviation as proxy for HP filter gap
    df = df.reset_index()
    df["credit_gap"] = df.groupby("country")["domestic_credit_gdp"].transform(
        lambda x: x - x.rolling(window=5, min_periods=3, center=True).mean()
    )
    print(f"  credit_gap: calculated")

# ========================================
# 2. Calculate Sandpile Load
# ========================================
print("\n[3] Calculating Sandpile Load...")

if "bank_capital_assets" in df.columns:
    # Stress = (1 - capital_ratio), proxy for sandpile load
    df["sandpile_load"] = 1 - (df["bank_capital_assets"].fillna(5) / 10)
    # Cumulative stress
    df["sandpile_cumulative"] = df.groupby("country")["sandpile_load"].cumsum()
    print(f"  sandpile_load: calculated")

# ========================================
# 3. Network Density Proxy
# ========================================
print("\n[4] Calculating Network Density...")

if "trade_openness" in df.columns:
    # Normalize trade openness as proxy for financial integration
    max_trade = df["trade_openness"].max()
    df["network_density"] = df["trade_openness"] / max_trade
    print(f"  network_density: calculated")

# ========================================
# 4. Regime Indicator
# ========================================
print("\n[5] Calculating Regime...")

if "gdp_growth" in df.columns:
    df["regime"] = (df["gdp_growth"] > 0).astype(int)
    print(f"  regime: calculated")

# ========================================
# 5. Add Crisis Indicator
# ========================================
print("\n[6] Adding Crisis Indicator...")

crisis = pd.read_csv(f"{RAW_DIR}/crisis_dates_annual.csv")
crisis = crisis.rename(columns={"year": "date"})

# Convert date to string format matching
crisis["date"] = crisis["date"].astype(str)
df["date"] = df["date"].astype(str)

# Merge
df = df.merge(
    crisis[["country", "date", "crisis_sys"]],
    on=["country", "date"],
    how="left"
)
df["crisis_sys"] = df["crisis_sys"].fillna(0).astype(int)
print(f"  crisis_sys: merged")

# ========================================
# 6. Save
# ========================================
print("\n[7] Saving...")

# Select key variables
key_cols = [
    "country", "date",
    "domestic_credit_gdp", "credit_gap",
    "bank_assets_gdp", "bank_capital_assets",
    "gdp_growth", "inflation",
    "trade_openness", "network_density",
    "sandpile_load", "sandpile_cumulative",
    "regime", "crisis_sys"
]

existing_cols = [c for c in key_cols if c in df.columns]
df_final = df[existing_cols].copy()

df_final.to_csv(f"{PROCESSED_DIR}/variables_derived.csv", index=False)
print(f"  Saved to: {PROCESSED_DIR}/variables_derived.csv")

# Summary
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"  Countries: {df_final['country'].nunique()}")
print(f"  Time range: {df_final['date'].min()} - {df_final['date'].max()}")
print(f"  Observations: {len(df_final)}")
print(f"  Variables: {len(df_final.columns)}")

print("\n  Missing values:")
for col in df_final.columns:
    missing = df_final[col].isna().sum()
    pct = missing / len(df_final) * 100
    print(f"    {col}: {missing} ({pct:.1f}%)")

print("\nSTEP 7 COMPLETE")
