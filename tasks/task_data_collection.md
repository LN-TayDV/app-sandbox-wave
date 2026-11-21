# TASK: Thu thập và chuẩn hóa dữ liệu IFWST

## Mục tiêu

Thu thập dữ liệu để ước lượng IFWST model theo chiến lược đã thiết kế.

## Chi tiết công việc

### Bước 1: Download BIS Credit-by-Counterparty Data

- **URL:** https://www.bis.org/statistics/counterparty_credits.htm
- **File output:** `data/raw/bis_credit_gap.csv`
- **Variables cần:** credit_to_gdp, property_prices_to_gdp, dsr
- **Period:** 1990Q1 - 2024Q1
- **Frequency:** Quarterly

### Bước 2: Download BIS Cross-border Data

- **URL:** https://www.bis.org/statistics/cross_border.htm
- **File output:** `data/raw/bis_cross_border.csv`
- **Variables cần:** cross_border_claims_to_gdp
- **Period:** 2000Q1 - 2024Q1

### Bước 3: Download IMF IFS Data

- **URL:** https://dataservices.imf.org/REST/SDMX_JSON.svc/CompactData/IFS
- **File output:** `data/raw/imf_ifs.csv`
- **Variables cần:** gdp_growth, inflation, policy_rate
- **Period:** 1990Q1 - 2024Q1

### Bước 4: Crisis Dates

- **Nguồn:** Laeven-Valencia BIS Working Paper 1437
- **URL:** https://www.bis.org/publ/work1437.pdf
- **File output:** `data/raw/crisis_dates.csv`
- **Variables cần:** country, crisis_start, crisis_end, crisis_type

### Bước 5: Tính Derived Variables

- **CreditGap:** Sử dụng HP filter (λ=400,000)
- **PropertyGap:** Tương tự
- **SandpileLoad:** Σlosses / (N × Buffer)

### Bước 6: Tạo Panel Dataset

- **File output:** `data/processed/ifwst_panel.csv`
- **Format:** Country × Quarter panel
- **Countries:** 20+ quốc gia (US, UK, DE, FR, JP, IT, CA, CH, CN, IN, BR, MX, RU, TR, KR, ID, PL, HU, CZ, RO)

## Tiêu chí hoàn thành

- [ ] Tất cả raw data files trong `data/raw/`
- [ ] Panel dataset trong `data/processed/`
- [ ] Data quality report
- [ ] Summary statistics

## Thời hạn

Ước tính: 2-3 giờ

## Lưu ý

- Nếu BIS/IMF API không accessible, tìm alternative sources hoặc báo cáo
- Document any data issues
- Sử dụng Python hoặc R scripts có thể tái lập
