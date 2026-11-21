# CHIẾN LƯỢC THU THẬP DỮ LIỆU — IFWST

## 1. TỔNG QUAN DỮ LIỆU

### 1.1 Nguồn Dữ liệu Chính

| Nguồn | Dữ liệu | Phạm vi | Ưu tiên |
|--------|----------|----------|----------|
| **BIS CBS** | Credit-to-GDP gaps, property gaps, DSR | 1990Q1-2024Q1 | 🔴 Cao nhất |
| **BIS Cross-border** | Cross-border claims, liên kết | 2000Q1-2024Q1 | 🔴 Cao |
| **IMF IFS** | GDP, inflation, policy rates | 1990Q1-2024Q1 | 🟡 Trung bình |
| **Bankscope** | Bank-level balance sheets | 1990-2023 | 🔴 Cao |
| **Laeven-Valencia** | Crisis dates | 1970-2023 | 🔴 Cao nhất |
| **ECB CSFB** | Composite indicators | 1990Q1-2024Q1 | 🟡 Trung bình |

### 1.2 Kiến trúc Dữ liệu

```
┌─────────────────────────────────────────────────────────────────┐
│                    IFWST DATA ARCHITECTURE                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐       │
│  │  MACRO DATA  │   │  BANK DATA   │   │  NETWORK    │       │
│  │              │   │              │   │    DATA     │       │
│  │  - GDP       │   │  - Assets    │   │  - Links    │       │
│  │  - Inflation │   │  - Capital   │   │  - Exposure │       │
│  │  - Rates     │   │  - Loans     │   │  - Flow     │       │
│  └──────┬───────┘   └──────┬───────┘   └──────┬───────┘       │
│          │                  │                  │               │
│          ▼                  ▼                  ▼               │
│  ┌──────────────────────────────────────────────────────┐       │
│  │              DERIVED VARIABLES                        │       │
│  │  - Credit gap    - DSR       - Sandpile load       │       │
│  │  - Property gap  - Network   - Wave intensity       │       │
│  └──────────────────────────────────────────────────────┘       │
│                              │                                 │
│                              ▼                                 │
│  ┌──────────────────────────────────────────────────────┐       │
│  │              ANALYSIS DATASET                         │       │
│  │  Country × Quarter panel                             │       │
│  └──────────────────────────────────────────────────────┘       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. BIẾN SỐ VÀ NGUỒN CHI TIẾT

### 2.1 Biến Phụ thuộc (Dependent Variables)

| Biến | Định nghĩa | Nguồn | Mã |
|-------|-------------|-------|-----|
| `Crisis` | Dummy khủng hoảng hệ thống | Laeven-Valencia | `crisis_sys` |
| `BankCrisis` | Dummy khủng hoảng ngân hàng | Laeven-Valencia | `crisis_bank` |
| `ΔCredit` | Thay đổi tín dụng | BIS CBS | `credit_chng` |
| `ΔGDP` | Thay đổi GDP | IMF IFS | `gdp_chng` |

### 2.2 Early Warning Indicators (EWI)

| Biến | Định nghĩa | Nguồn | Công thức |
|------|-------------|-------|-----------|
| `CreditGap` | Chênh lệch tín dụng/GDP | BIS CBS | `credit_gdp - trend(credit_gdp)` |
| `PropertyGap` | Chênh lệch giá BĐS | BIS CBS | `property_gdp - trend(property_gdp)` |
| `DSR` | Tỷ lệ trả nợ | BIS CBS | `debt_service / income` |
| `HouseholdDSR` | DSR hộ gia đình | BIS CBS | `hh_debt_service / hh_income` |
| `ForeignDebt` | Nợ nước ngoài | BIS CBS | `fcy_debt / gdp` |
| `CrossBorder` | Yêu cầu xuyên biên giới | BIS CBS | `cross_border / gdp` |

### 2.3 Biến Mạng (Network)

| Biến | Định nghĩa | Nguồn | Mã |
|------|-------------|-------|-----|
| `InterbankLink` | Liên kết liên ngân hàng | Bankscope | `ib_link` |
| `ForeignShare` | Tỷ lệ sở hữu nước ngoài | Bankscope | `foreign_share` |
| `CrossBorderClaim` | Yêu cầu xuyên biên giới | BIS | `cb_claim` |
| `Concentration` | Herfindahl index | Bankscope | `concentration` |

### 2.4 Biến Sandpile (Derived)

| Biến | Định nghĩa | Công thức |
|------|-------------|-----------|
| `SandpileLoad` | Tải trọng tích lũy | `Σlosses / (N × Buffer)` |
| `AvalanchePotential` | Khả năng avalanche | `H(Load - Threshold)` |
| `BufferRatio` | Tỷ lệ bộ đệm | `Capital / Risk_Assets` |
| `LossAccumulation` | Tích lũy tổn thất | `Σ(Defaults × Exposure)` |

### 2.5 Biến Điều khiển (Control)

| Biến | Định nghĩa | Nguồn |
|------|-------------|-------|
| `GDPGrowth` | Tăng trưởng GDP | IMF IFS |
| `Inflation` | Lạm phát | IMF IFS |
| `PolicyRate` | Lãi suất chính sách | IMF IFS |
| `TradeOpen` | Mở cửa thương mại | IMF IFS |
| `Regime` | Boom/Bust | Derived |

---

## 3. QUY TRÌNH THU THẬP

### 3.1 Bước 1: Download BIS CBS

```python
# Priority: Credit-to-GDP, Property prices, DSR
URL: https://www.bis.org/statistics/counterparty_credits.htm
File: credit_counterparty.csv
Variables: credit_gdp, property_gdp, dsr
```

### 3.2 Bước 2: Download BIS Cross-border

```python
URL: https://www.bis.org/statistics/cross_border.htm
File: cross_border_claims.csv
Variables: claims_foreign, claims_domestic
```

### 3.3 Bước 3: Download IMF IFS

```python
URL: https://dataservices.imf.org/REST/SDMX_JSON.svc/CompactData/IFS
File: ifs_macroeconomic.csv
Variables: gdp, inflation, policy_rate
```

### 3.4 Bước 4: Download Laeven-Valencia

```python
URL: https://www.imf.org/external/np/seminars/eng/2012/arcrisis/data/lamon.pdf
# Hoặc: https://www.bis.org/publ/work1437.pdf
File: crisis_dates.csv
Variables: crisis_start, crisis_end, crisis_type
```

### 3.5 Bước 5: Download Bankscope (nếu có)

```python
# Cần subscription - có thể cần thay thế bằng:
# - World Bank Global Financial Development
# - IMF Financial Access Survey
URL: https://www.worldbank.org/en/programs/financial-inclusion
File: bank_level.csv
```

---

## 4. CHUẨN HÓA DỮ LIỆU

### 4.1 Xử lý Missing Data

| Tình huống | Phương pháp |
|------------|-------------|
| < 5% missing | Linear interpolation |
| 5-20% missing | Multiple imputation (MICE) |
| > 20% missing | Drop variable hoặc sensitivity |

### 4.2 Tính Credit Gap

```python
# One-sided HP filter (BIS method)
# λ = 400,000 cho quarterly data

from statsmodels.tsa.filters.hp_filter import hpfilter
credit_trend, credit_cycle = hpfilter(credit_gdp, lamb=400000)
CreditGap = credit_cycle  # Deviation from trend
```

### 4.3 Tính Property Gap

```python
# Tương tự với property prices
property_trend, property_cycle = hpfilter(property_gdp, lamb=400000)
PropertyGap = property_cycle
```

### 4.4 Tính Sandpile Load

```python
# L(t) = Σ losses / (N × Buffer)
SandpileLoad = cumulative_losses / (n_banks × avg_capital_ratio)
```

### 4.5 Tạo Panel

```
Country | Quarter | Crisis | CreditGap | PropertyGap | DSR | SandpileLoad | Network | Controls
--------|---------|--------|-----------|------------|-----|--------------|--------|---------
USA     | 2007Q1  | 0      | 12.3      | 8.5        | 35  | 0.45         | 0.32   | ...
USA     | 2007Q2  | 0      | 13.1      | 9.2        | 36  | 0.52         | 0.34   | ...
USA     | 2007Q3  | 0      | 14.0      | 10.1       | 38  | 0.61         | 0.36   | ...
USA     | 2007Q4  | 0      | 14.8      | 11.3       | 41  | 0.73         | 0.38   | ...
USA     | 2008Q1  | 1      | 15.5      | 12.8       | 45  | 0.89         | 0.41   | ...
...
```

---

## 5. KIỂM TRA CHẤT LƯỢNG

### 5.1 Data Quality Checks

| Check | Tiêu chí |
|-------|----------|
| Range check | Giá trị trong phạm vi hợp lý |
| Time consistency | Không có jump đột ngột > 3σ |
| Cross-source | Nhất quán giữa các nguồn |
| Missing rate | < 20% per variable |

### 5.2 Summary Statistics

```python
# Output cần có:
- n (observations)
- mean, std, min, max
- Missing %
- Correlation matrix
```

### 5.3 Visualization

```python
# Time series plots cho mỗi variable
# Distribution plots
# Correlation heatmap
```

---

## 6. DỮ LIỆU MẪU (Sample Countries)

### 6.1 Advanced Economies

| Country | ISO | BIS | IMF |
|---------|-----|-----|-----|
| United States | USA | ✓ | ✓ |
| United Kingdom | GBR | ✓ | ✓ |
| Germany | DEU | ✓ | ✓ |
| France | FRA | ✓ | ✓ |
| Japan | JPN | ✓ | ✓ |
| Italy | ITA | ✓ | ✓ |
| Canada | CAN | ✓ | ✓ |
| Switzerland | CHE | ✓ | ✓ |

### 6.2 Emerging Markets

| Country | ISO | BIS | IMF |
|---------|-----|-----|-----|
| China | CHN | ✓ | ✓ |
| India | IND | ✓ | ✓ |
| Brazil | BRA | ✓ | ✓ |
| Mexico | MEX | ✓ | ✓ |
| Russia | RUS | ✓ | ✓ |
| Turkey | TUR | ✓ | ✓ |
| South Korea | KOR | ✓ | ✓ |
| Indonesia | IDN | ✓ | ✓ |

### 6.3 Central-Eastern Europe

| Country | ISO | BIS | IMF |
|---------|-----|-----|-----|
| Poland | POL | ✓ | ✓ |
| Hungary | HUN | ✓ | ✓ |
| Czech Republic | CZE | ✓ | ✓ |
| Romania | ROU | ✓ | ✓ |
| Bulgaria | BGR | ✓ | ✓ |

---

## 7. OUTPUT: DATA DICTIONARY

### 7.1 File: `ifwst_panel.csv`

```
├── country (str)      : ISO country code
├── quarter (str)     : YYYYQQ format
├── year (int)        : 1990-2024
├── qtr (int)         : 1-4
├── crisis_sys (int)  : 0/1 systemic crisis
├── crisis_bank (int) : 0/1 bank crisis
├── credit_gdp (float): Credit to GDP ratio (%)
├── credit_gap (float): Credit gap (%)
├── property_gdp (float): Property price to GDP
├── property_gap (float): Property gap (%)
├── dsr (float)       : Debt service ratio (%)
├── hh_dsr (float)   : Household DSR (%)
├── fcy_debt_gdp (float): Foreign currency debt (%)
├── cb_claims_gdp (float): Cross-border claims (%)
├── interbank_link (float): Interbank exposure
├── foreign_share (float): Foreign ownership (%)
├── sandpile_load (float): Cumulative load / buffer
├── buffer_ratio (float): Capital / risk assets (%)
├── gdp_growth (float): Real GDP growth (%)
├── inflation (float) : CPI inflation (%)
├── policy_rate (float): Policy rate (%)
├── trade_open (float): Trade openness (%)
└── regime (int)     : 1=boom, 0=bust
```

---

## 8. BƯỚC TIẾP THEO

- [ ] Download BIS CBS data
- [ ] Download BIS cross-border data  
- [ ] Download IMF IFS data
- [ ] Compile crisis dates
- [ ] Calculate derived variables
- [ ] Create panel dataset
- [ ] Quality checks
- [ ] Summary statistics

---

**Task cho subagent:** Thu thập và chuẩn hóa dữ liệu theo chiến lược trên.
