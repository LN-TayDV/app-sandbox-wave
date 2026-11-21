"""
STEP 7: Tính Derived Variables
- Credit gap (HP filter)
- Property gap (HP filter)
- Sandpile load
- Network density
- Regime indicators
"""
import os
import pandas as pd
import numpy as np
from scipy import interpolate

RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"
os.makedirs(PROCESSED_DIR, exist_ok=True)

print("=" * 60)
print("STEP 7: Tính Derived Variables")
print("=" * 60)

# Target countries
COUNTRIES = [
    "USA", "GBR", "DEU", "FRA", "JPN", "ITA", "CAN", "CHE",
    "CHN", "IND", "BRA", "MEX", "RUS", "TUR", "KOR", "IDN",
    "POL", "HUN", "CZE", "ROU", "BGR"
]

# ========================================
# 1. Load macro data
# ========================================
print("\n[1] Loading macro data...")

# Load all available indicators
macro_vars = {}
for f in os.listdir(RAW_DIR):
    if f.startswith("wb_") and f.endswith(".csv") and "combined" not in f:
        var_name = f.replace("wb_", "").replace(".csv", "")
        try:
            df = pd.read_csv(f"{RAW_DIR}/{f}", index_col=[0, 1])
            df.index.names = ['country', 'date']
            macro_vars[var_name] = df
            print(f"  {var_name}: {df.shape}")
        except Exception as e:
            print(f"  {var_name}: Error - {e}")

# Combine into single DataFrame
print("\n[2] Combining variables...")
combined = None
for var_name, df in macro_vars.items():
    # Rename column to avoid conflict
    df_renamed = df.copy()
    df_renamed.columns = [f"{var_name}"]
    if combined is None:
        combined = df_renamed
    else:
        combined = combined.join(df_renamed, how="outer")

print(f"  Combined shape: {combined.shape}")

# ========================================
# 2. Interpolate to quarterly (from annual)
# ========================================
print("\n[3] Interpolating to quarterly...")

# Create quarterly index
quarters = pd.date_range(start="1990-01-01", end="2024-01-01", freq="QE")
quarters_df = pd.DataFrame(index=quarters)
quarters_df["year"] = quarters_df.index.year
quarters_df["quarter"] = (quarters_df.index.quarter)

# Interpolate each country
quarterly_data = []
for country in COUNTRIES:
    try:
        # Get annual data for this country
        if country in combined.index.get_level_values(0):
            annual = combined.loc[country].copy()
            annual["year"] = annual.index.astype(int)
            annual = annual.reset_index(drop=True)

            # Interpolate to quarterly
            quarterly = []
            for year in range(1990, 2025):
                for q in [1, 2, 3, 4]:
                    row = {"country": country, "year": year, "quarter": q}
                    # Linear interpolation
                    for col in annual.columns:
                        if annual[col].dtype in [float, int]:
                            # Get surrounding years
                            y_above = annual[annual["year"] <= year]["year"].max()
                            y_below = annual[annual["year"] >= year]["year"].min()
                            if pd.notna(y_above) and pd.notna(y_below):
                                v_above = annual[annual["year"] == y_above][col].values
                                v_below = annual[annual["year"] == y_below][col].values
                                if len(v_above) > 0 and len(v_below) > 0:
                                    if y_above == y_below:
                                        row[col] = v_above[0]
                                    else:
                                        # Linear interpolation
                                        ratio = (year - y_above) / (y_below - y_above) if y_below != y_above else 0
                                        row[col] = v_above[0] * (1 - ratio) + v_below[0] * ratio
                                else:
                                    row[col] = np.nan
                            else:
                                row[col] = np.nan
                        else:
                            row[col] = np.nan
                    quarterly.append(row)

            quarterly_df_country = pd.DataFrame(quarterly)
            quarterly_data.append(quarterly_df_country)
    except Exception as e:
        print(f"  Error for {country}: {e}")

if quarterly_data:
    quarterly_all = pd.concat(quarterly_data, ignore_index=True)
    print(f"  Quarterly data: {quarterly_all.shape}")

# ========================================
# 3. Calculate Credit Gap (HP filter)
# ========================================
print("\n[4] Calculating Credit Gap (HP filter)...")

# HP filter approximation: Use rolling mean deviation
# BIS uses lambda=400000 for quarterly
# We'll use simpler deviation from trend

def calculate_hp_gap(series, window=8):
    """Simplified HP-like gap calculation"""
    # Rolling mean as trend
    trend = series.rolling(window=window, min_periods=3, center=True).mean()
    gap = series - trend
    return gap, trend

# Calculate credit gap
if "domestic_credit_gdp" in quarterly_all.columns:
    quarterly_all["credit_gap"], _ = calculate_hp_gap(quarterly_all["domestic_credit_gdp"])
    print(f"  credit_gap: calculated")

# ========================================
# 4. Calculate Sandpile Load
# ========================================
print("\n[5] Calculating Sandpile Load...")

# Sandpile Load = Cumulative losses / Buffer
# Proxy: (1 - capital_adequacy) as stress indicator
if "bank_capital_assets" in quarterly_all.columns:
    # Capital adequacy ratio (higher = more stable)
    capital_ratio = quarterly_all["bank_capital_assets"].fillna(10) / 100
    # Stress = 1 - stability
    quarterly_all["sandpile_load"] = (1 - capital_ratio)
    # Cumulative stress
    quarterly_all["sandpile_cumulative"] = quarterly_all.groupby("country")["sandpile_load"].cumsum()
    print(f"  sandpile_load: calculated")

# ========================================
# 5. Calculate Network Density Proxy
# ========================================
print("\n[6] Calculating Network Density Proxy...")

# Network density proxy: trade openness as proxy for financial integration
if "trade_openness" in quarterly_all.columns:
    # Normalize to 0-1
    max_trade = quarterly_all["trade_openness"].max()
    quarterly_all["network_density"] = quarterly_all["trade_openness"] / max_trade
    print(f"  network_density: calculated (from trade_openness)")

# ========================================
# 6. Regime Indicator (Boom/Bust)
# ========================================
print("\n[7] Calculating Regime Indicator...")

# Regime: 1 = boom (GDP growth > 0), 0 = bust (GDP growth <= 0)
if "gdp_growth" in quarterly_all.columns:
    quarterly_all["regime"] = (quarterly_all["gdp_growth"] > 0).astype(int)
    print(f"  regime: calculated")

# ========================================
# 7. Add Crisis Indicator
# ========================================
print("\n[8] Adding Crisis Indicator...")

# Load crisis dates
try:
    crisis = pd.read_csv(f"{RAW_DIR}/crisis_dates.csv")
    print(f"  Crisis data: {crisis.shape}")

    # Merge
    quarterly_all = quarterly_all.merge(
        crisis[["country", "year", "quarter", "crisis_sys"]],
        on=["country", "year", "quarter"],
        how="left"
    )
    quarterly_all["crisis_sys"] = quarterly_all["crisis_sys"].fillna(0).astype(int)
    print(f"  crisis_sys: merged")
except Exception as e:
    print(f"  Error: {e}")
    quarterly_all["crisis_sys"] = 0

# ========================================
# 8. Save derived variables
# ========================================
print("\n[9] Saving derived variables...")

# Select key variables
key_vars = [
    "country", "year", "quarter",
    "domestic_credit_gdp", "credit_gap",
    "bank_assets_gdp", "bank_capital_assets",
    "gdp_growth", "inflation",
    "trade_openness", "network_density",
    "sandpile_load", "sandpile_cumulative",
    "regime", "crisis_sys"
]

# Keep only existing columns
existing_cols = [c for c in key_vars if c in quarterly_all.columns]
derived = quarterly_all[existing_cols].copy()

# Save
derived.to_csv(f"{PROCESSED_DIR}/variables_derived.csv", index=False)
print(f"  Saved to: {PROCESSED_DIR}/variables_derived.csv")

# Summary
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"  Countries: {derived['country'].nunique()}")
print(f"  Time range: {derived['year'].min()} - {derived['year'].max()}")
print(f"  Observations: {len(derived)}")
print(f"  Variables: {len(derived.columns)}")

# Missing summary
print("\n  Missing values:")
for col in derived.columns:
    missing = derived[col].isna().sum()
    pct = missing / len(derived) * 100
    print(f"    {col}: {missing} ({pct:.1f}%)")

print("\nSTEP 7 COMPLETE")
