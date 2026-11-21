# WORKFLOW THỰC THI IFWST — Từng Bước

> ⚠️ **PHẠM VI FILE NÀY:** Đây là workflow **riêng cho Giai đoạn 5 (mã nguồn thực nghiệm)** — các STEP tải dữ liệu → derived variables → panel → quality check.
> **Workflow tổng của cả dự án** (13 bước, từ đồng bộ repo đến luận văn) nằm ở: [`00_project_management/WORKFLOW.md`](00_project_management/WORKFLOW.md).
> **Trang điều hướng:** [`00_project_management/START_HERE.md`](00_project_management/START_HERE.md).
>
> ⚠️ Lưu ý: `code/08_summary.py` → `code/16_report.py` **chưa tồn tại**. Các STEP 10–18 dưới đây là kế hoạch, chưa được hiện thực. Chúng được viết ở BƯỚC 11 của workflow tổng.

> **Quy tắc:** Mỗi step tôi sẽ dừng lại. Bạn đọc kết quả, ra lệnh chạy step tiếp theo.

---

## STEP 1: Tạo Cấu trúc Thư mục

**Mục tiêu:** Tạo thư mục cho dữ liệu, code, output

**Lệnh chạy:**
```bash
mkdir -p data/raw data/processed code output logs
```

**Kỳ vọng:** Tạo thành công các thư mục con

---

## STEP 2: Cài đặt Python Packages

**Mục tiêu:** Cài các thư viện cần thiết

**Lệnh chạy:**
```bash
pip install pandas numpy statsmodels scipy scikit-learn matplotlib seaborn requests wbdata
```

**Kỳ vọng:** Tất cả packages cài thành công

---

## STEP 3: Download Dữ liệu BIS Credit Statistics

**Mục tiêu:** Lấy Credit-to-GDP gaps, DSR, LBS cross-border claims

**File code:** `code/00_probe_bis.py` ✅ *(đã chạy thành công — B1)*
> `code/01_download_bis.py` dùng URL `www.bis.org/statistics/...` — **404**, `www.bis.org` bị WAF chặn.
> Nguồn dùng được: **SDMX v2** `https://stats.bis.org/api/v2/data/dataflow/BIS/{FLOW}/1.0/{KEY}`.

**Lệnh chạy:**
```bash
python code/00_probe_bis.py
```

**Kỳ vọng:** các file sau trong `data/raw/` được tạo/cập nhật

| File | Nội dung | Dòng | Kỳ |
|---|---|---|---|
| `bis_credit_gap.csv` | Credit-to-GDP gap (actual−trend), 44 nước, quý | 7.620 | 1957-Q4 → 2026-Q1 |
| `bis_credit_gdp_ratio.csv` | Credit-to-GDP ratio (thô), 44 nước, quý | 9.380 | 1947-Q4 → 2026-Q1 |
| `bis_credit_gap_us.csv` | Gap riêng Mỹ | 274 | 1957-Q4 → 2026-Q1 |
| `bis_dsr.csv` | Debt service ratios, 32 nước, quý | 7.182 | 1999-Q1 → 2026-Q1 |
| `bis_lbs_cross_border_us.csv` | LBS cross-border claims, Mỹ | 194 | 1977-Q4 → 2026-Q1 |
| `bis_lbs_cross_border_all.csv` | LBS cross-border claims, tổng hợp | 194 | 1977-Q4 → 2026-Q1 |

**SDMX key đã xác minh** (dùng lại được):
`WS_CREDIT_GAP` → `Q..P.A.C` (gap) · `Q..P.A.A` (ratio) · `Q.US.P.A.C` (Mỹ) ·
`WS_DSR` → `Q...A` · `WS_LBS_D_PUB` → `Q.S.C.A.TO1.F.5J.A.{CTY}.A.5J.A`

---

## STEP 4: Download Cross-border Banking Data

**Mục tiêu:** Lấy liên kết xuyên biên giới

**File code:** `code/02_download_crossborder.py`

**Lệnh chạy:**
```bash
python code/02_download_crossborder.py
```

**Kỳ vọng:** File `data/raw/bis_crossborder.csv` được tạo

---

## STEP 5: Download IMF IFS Data

**Mục tiêu:** Lấy macro data (GDP, inflation, rates)

**File code:** `code/03_download_imf.py`

**Lệnh chạy:**
```bash
python code/03_download_imf.py
```

**Kỳ vọng:** File `data/raw/imf_ifs.csv` được tạo

---

## STEP 6: Compile Crisis Dates

**Mục tiêu:** Tạo danh sách các khủng hoảng ngân hàng

**File code:** `code/04_crisis_dates.py`

**Lệnh chạy:**
```bash
python code/04_crisis_dates.py
```

**Kỳ vọng:** File `data/raw/crisis_dates.csv` được tạo

---

## STEP 7: Tính Derived Variables

**Mục tiêu:** Tính Credit gap, Sandpile load, Network density

**File code:** `code/05_derived.py`

**Lệnh chạy:**
```bash
python code/05_derived.py
```

**Kỳ vọng:** File `data/processed/variables_derived.csv` được tạo

---

## STEP 8: Tạo Panel Dataset

**Mục tiêu:** Gộp tất cả thành Country × Quarter panel

**File code:** `code/06_panel.py`

**Lệnh chạy:**
```bash
python code/06_panel.py
```

**Kỳ vọng:** File `data/processed/ifwst_panel.csv` được tạo

---

## STEP 9: Data Quality Check

**Mục tiêu:** Kiểm tra chất lượng dữ liệu

**File code:** `code/07_quality.py`

**Lệnh chạy:**
```bash
python code/07_quality.py
```

**Kỳ vọng:** Báo cáo `output/data_quality_report.md`

---

## STEP 10: Summary Statistics

**Mục tiêu:** Tạo bảng thống kê mô tả

**File code:** `code/08_summary.py`

**Lệnh chạy:**
```bash
python code/08_summary.py
```

**Kỳ vọng:** File `output/summary_statistics.csv` và biểu đồ

---

## STEP 11: Estimate Baseline EWI Model

**Mục tiêu:** Ước lượng mô hình EWI cơ sở

**File code:** `code/09_baseline.py`

**Lệnh chạy:**
```bash
python code/09_baseline.py
```

**Kỳ vọng:** File `output/baseline_results.csv`

---

## STEP 12: Estimate Network Model

**Mục tiêu:** Ước lượng mô hình có Network

**File code:** `code/10_network.py`

**Lệnh chạy:**
```bash
python code/10_network.py
```

**Kỳ vọng:** File `output/network_results.csv`

---

## STEP 13: Estimate Full IFWST Model

**Mục tiêu:** Ước lượng mô hình đầy đủ IFWST

**File code:** `code/11_ifwst.py`

**Lệnh chạy:**
```bash
python code/11_ifwst.py
```

**Kỳ vọng:** File `output/ifwst_results.csv`

---

## STEP 14: Compare Models

**Mục tiêu:** So sánh baseline, network, IFWST

**File code:** `code/12_compare.py`

**Lệnh chạy:**
```bash
python code/12_compare.py
```

**Kỳ vọng:** File `output/comparison.csv` và biểu đồ

---

## STEP 15: Backtest 2008 Crisis

**Mục tiêu:** Kiểm tra mô hình trên khủng hoảng 2008

**File code:** `code/13_backtest.py`

**Lệnh chạy:**
```bash
python code/13_backtest.py
```

**Kỳ vọng:** File `output/backtest_2008.md`

---

## STEP 16: Sensitivity Analysis

**Mục tiêu:** Kiểm tra độ bền của mô hình

**File code:** `code/14_sensitivity.py`

**Lệnh chạy:**
```bash
python code/14_sensitivity.py
```

**Kỳ vọng:** File `output/sensitivity.md`

---

## STEP 17: Tạo Visualization

**Mục tiêu:** Vẽ biểu đồ kết quả

**File code:** `code/15_viz.py`

**Lệnh chạy:**
```bash
python code/15_viz.py
```

**Kỳ vọng:** File trong `output/figures/`

---

## STEP 18: Viết Báo cáo

**Mục tiêu:** Tổng hợp kết quả thành báo cáo

**File code:** `code/16_report.py`

**Lệnh chạy:**
```bash
python code/16_report.py
```

**Kỳ vọng:** File `output/IFWST_Final_Report.md`

---

## CÁCH SỬ DỤNG

1. Tôi sẽ tạo code cho **STEP hiện tại**
2. Bạn chạy lệnh
3. Tôi dừng lại, bạn xem kết quả
4. Nếu OK → "tiếp" hoặc "next"
5. Nếu lỗi → báo lỗi để tôi fix

---

**SẴN SÀNG CHẠY STEP 1?**
