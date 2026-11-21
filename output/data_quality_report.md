# IFWST Data Quality Report
Generated: 2026-10-17 21:32:32.968579

## Dataset Overview
- Countries: 21
- Time period: 1990 - 2023
- Observations: 714
- Variables: 19

## Missing Values
- country: 0 (0.0%)
- date: 0 (0.0%)
- domestic_credit_gdp: 0 (0.0%)
- credit_gap: 0 (0.0%)
- bank_assets_gdp: 0 (0.0%)
- bank_capital_assets: 0 (0.0%)
- gdp_growth: 0 (0.0%)
- inflation: 0 (0.0%)
- trade_openness: 0 (0.0%)
- network_density: 0 (0.0%)
- sandpile_load: 0 (0.0%)
- sandpile_cumulative: 0 (0.0%)
- regime: 0 (0.0%)
- crisis_sys: 0 (0.0%)
- crisis_lag1: 0 (0.0%)
- crisis_lead1: 0 (0.0%)
- credit_growth: 0 (0.0%)
- sandpile_network: 0 (0.0%)
- pre_crisis: 0 (0.0%)

## Range Checks
- gdp_growth: [-20, 20] - OK
- inflation: [-5, 100] - OK
- sandpile_load: [0, 1] - OK
- network_density: [0, 1] - OK
- regime: [0, 1] - OK
- crisis_sys: [0, 1] - OK

## Outliers
- gdp_growth: 9 outliers
- inflation: 7 outliers
- sandpile_load: 3 outliers

## Data Quality Summary
- Missing values: 0 total
- Range violations: 1
- Time gaps: 0 countries
- Outliers: 19 total

## Recommendation
Data is ready for analysis with minor caveats:
- Some outliers in inflation (expected for emerging markets)
- Crisis persistence shows some short crisis episodes
