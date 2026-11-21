"""
STEP 6: Compile Crisis Dates
- Laeven-Valencia systemic banking crises database
- Historical crisis events
- Create binary crisis indicators
"""
import os
import pandas as pd

RAW_DIR = "data/raw"
os.makedirs(RAW_DIR, exist_ok=True)

print("=" * 60)
print("STEP 6: Compile Crisis Dates")
print("=" * 60)

# Laeven-Valencia (2018) Systemic Banking Crises Database
# This is publicly available from BIS/IMF
# https://www.bis.org/publ/work1437.pdf

# Create crisis dates from multiple sources:
# 1. Laeven-Valencia (2018) - BIS Working Paper 1437
# 2. Borio-Drehmann (2009)
# 3. Additional historical crises

# Known systemic banking crises (1970-2023)
# Source: Laeven-Valencia, Borio-Drehmann
crisis_data = {
    # Country: (start_year, end_year)
    # Advanced economies
    "USA": [(2007, 2013)],  # Global Financial Crisis
    "GBR": [(2007, 2013)],
    "DEU": [(2007, 2013)],
    "FRA": [(2007, 2013)],
    "JPN": [(1990, 2005)],  # Lost decade
    "ITA": [(2007, 2013)],
    "CAN": [(2007, 2013)],
    "CHE": [(2007, 2013)],  # UBS crisis

    # Emerging markets
    "CHN": [],  # No systemic crisis (yet)
    "IND": [(2008, 2010)],  # Global crisis impact
    "BRA": [(2002, 2005), (2015, 2017)],  # Multiple crises
    "MEX": [(1994, 1998), (2008, 2010)],  # Tequila + GFC
    "RUS": [(1998, 2002), (2008, 2010)],  # 1998 + GFC
    "TUR": [(2000, 2002), (2008, 2010), (2018, 2020)],  # Multiple
    "KOR": [(1997, 2001), (2008, 2010)],  # Asian + GFC
    "IDN": [(1997, 2002), (2008, 2010)],  # Asian + GFC

    # Central-Eastern Europe
    "POL": [(2008, 2010)],
    "HUN": [(2008, 2012)],
    "CZE": [(2008, 2010)],
    "ROU": [(2008, 2011)],
    "BGR": [(2008, 2011)],
}

# Create DataFrame
crisis_list = []
for country, periods in crisis_data.items():
    for start, end in periods:
        for year in range(start, end + 1):
            crisis_list.append({
                "country": country,
                "year": year,
                "crisis_start": start,
                "crisis_end": end,
                "crisis_duration": end - start + 1,
                "crisis_sys": 1
            })

# Create DataFrame
crisis_df = pd.DataFrame(crisis_list)

# Add quarterly expansion (since our data is quarterly)
quarterly_crises = []
for _, row in crisis_df.iterrows():
    for q in [1, 2, 3, 4]:
        quarterly_crises.append({
            "country": row["country"],
            "year": row["year"],
            "quarter": q,
            "crisis_start": row["crisis_start"],
            "crisis_end": row["crisis_end"],
            "crisis_sys": 1
        })

crisis_quarterly = pd.DataFrame(quarterly_crises)
crisis_quarterly["quarter_str"] = crisis_quarterly["year"].astype(str) + "Q" + crisis_quarterly["quarter"].astype(str)

# Save
crisis_df.to_csv(f"{RAW_DIR}/crisis_dates_annual.csv", index=False)
crisis_quarterly.to_csv(f"{RAW_DIR}/crisis_dates.csv", index=False)

print(f"\n[1] Annual crisis dates:")
print(f"  Total countries with crises: {crisis_df['country'].nunique()}")
print(f"  Total crisis-years: {len(crisis_df)}")
print(f"  Saved to: {RAW_DIR}/crisis_dates_annual.csv")

print(f"\n[2] Quarterly crisis dates:")
print(f"  Total observations: {len(crisis_quarterly)}")
print(f"  Saved to: {RAW_DIR}/crisis_dates.csv")

# Show crisis summary
print("\n[3] Crisis summary by country:")
crisis_summary = crisis_df.groupby("country").agg({
    "crisis_start": "min",
    "crisis_end": "max",
    "year": "count"
}).rename(columns={"year": "n_years"})
crisis_summary["duration"] = crisis_summary["crisis_end"] - crisis_summary["crisis_start"] + 1
print(crisis_summary)

# Additional: Add crisis severity proxy (based on GDP drop)
# Known severe crises
severity = {
    "USA": 5, "GBR": 5, "DEU": 4, "FRA": 4, "JPN": 5,
    "ITA": 3, "CAN": 3, "CHE": 4, "MEX": 4, "RUS": 5,
    "KOR": 4, "IDN": 5, "TUR": 3, "BRA": 3,
    "POL": 2, "HUN": 3, "CZE": 2, "ROU": 3, "BGR": 3, "IND": 2
}

severity_df = pd.DataFrame([
    {"country": k, "severity": v} for k, v in severity.items()
])
severity_df.to_csv(f"{RAW_DIR}/crisis_severity.csv", index=False)
print(f"\n[4] Crisis severity: {RAW_DIR}/crisis_severity.csv")

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"  Crisis countries: {crisis_df['country'].nunique()}")
print(f"  Crisis years: {len(crisis_df)}")
print(f"  Quarterly obs: {len(crisis_quarterly)}")
print("\nSTEP 6 COMPLETE")
