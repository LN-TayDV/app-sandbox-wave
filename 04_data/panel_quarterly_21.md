# B2 — Panel Quý 21 Nước (IFWST)

**Output:** `data/processed/ifwst_panel_quarterly.csv`
**Script:** `code/08_build_panel.py` (dựng) · `code/00_probe_bis.py` + `code/09_download_wb.py` (tải)
**Cửa sổ:** 1990Q1–2023Q4 · 21 nước × 136 quý = **2.856 dòng** · 39 cột

---

## 1. Danh sách 21 nước — chốt theo độ phủ dữ liệu thật

Tiêu chí (theo thứ tự ưu tiên): (a) có BIS credit-to-GDP gap + DSR, (b) có ≥1 khủng hoảng ngân hàng hệ thống trong Laeven–Valencia 1990–2023, (c) có LBS cross-border.

| # | ISO2 | ISO3 | Quốc gia | Credit gap | DSR | LBS | Sự kiện LV |
|---|---|---|---|---|---|---|---|
| 1 | BR | BRA | Brazil | 72 | 100 | 85 | 2 |
| 2 | CA | CAN | Canada | 136 | 100 | 123 | 0 |
| 3 | CH | CHE | Switzerland | 136 | 100 | 136 | 1 |
| 4 | CN | CHN | China | 113 | 100 | 33 | 1 |
| 5 | CZ | CZE | Czechia | 84 | 100 | — | 1 |
| 6 | DE | DEU | Germany | 136 | 100 | 136 | 1 |
| 7 | FR | FRA | France | 136 | 100 | 65 | 1 |
| 8 | GB | GBR | United Kingdom | 136 | 100 | 136 | 1 |
| 9 | HU | HUN | Hungary | 136 | 100 | — | 2 |
| 10 | ID | IDN | Indonesia | 136 | 100 | 53 | 1 |
| 11 | IN | IND | India | 136 | 100 | 89 | 1 |
| 12 | IT | ITA | Italy | 136 | 100 | 58 | 1 |
| 13 | JP | JPN | Japan | 136 | 100 | 136 | 1 |
| 14 | KR | KOR | Korea, Rep. | 136 | 100 | 76 | 1 |
| 15 | MX | MEX | Mexico | 133 | 100 | 81 | 2 |
| 16 | NL | NLD | Netherlands | 136 | 100 | 136 | 1 |
| 17 | PL | POL | Poland | 88 | 100 | — | 1 |
| 18 | RU | RUS | Russian Federation | 75 | 100 | 25 | 2 |
| 19 | SE | SWE | Sweden | 136 | 100 | 135 | 2 |
| 20 | TR | TUR | Turkiye | 112 | 88 | 93 | 2 |
| 21 | US | USA | United States | 136 | 100 | 136 | 1 |

*(số = số quý có quan sát thật trong 136 quý)*

**Hai nước bị thay:** bản cũ dùng **BGR** và **ROU** — không có trong BIS credit gap / DSR / LBS. Thay bằng **NLD** (136 credit gap, 136 LBS, 1 khủng hoảng 2008) và **SWE** (136 credit gap, 135 LBS, 2 khủng hoảng).

---

## 2. Nguồn dữ liệu

| Nguồn | Biến | Tần suất | API |
|---|---|---|---|
| **BIS** WS_CREDIT_GAP | `credit_gap`, `credit_gdp_ratio` | quý | `stats.bis.org/api/v2/data/dataflow/BIS/WS_CREDIT_GAP/1.0/Q..P.A.C` |
| **BIS** WS_DSR | `dsr` (DSR borrowers = P) | quý | `.../WS_DSR/1.0/Q...A` |
| **BIS** WS_LBS_D_PUB | `xborder_claims_usd_bn` | quý | `.../WS_LBS_D_PUB/1.0/Q.S.C.A.TO1.F.5J.A.{CTY}.A.5J.A` |
| **World Bank** WDI | macro, tài chính ngân hàng | **năm** | `api.worldbank.org/v2/country/{21 nước}/indicator/{code}` |
| **Laeven–Valencia (2020)** | `crisis_sys`, `crisis_severity` | sự kiện → quý | Springer static-content (xlsx) |

### Đường dẫn Laeven–Valencia (quan trọng)

`www.bis.org/publ/work1437.pdf` **404** (WAF chặn). `laevenvalencia.github.io` **404**. `imf.org` 403. Đường dẫn dùng được:

```
https://static-content.springer.com/esm/art%3A10.1057%2Fs41308-020-00107-3/MediaObjects/41308_2020_107_MOESM1_ESM.xlsx
```

Tìm qua repo `chickymonkeys/LaevenValenciaBankingCrises` → `src/BankingCrisisDB.do`. File: 120.754 bytes, 6 sheet. Sheet dùng: **"Crisis Resolution and Outcomes"** (có Start/End + output loss, fiscal cost, peak NPL).

---

## 3. Độ phủ thật (không điền median)

| Biến | Nguồn | Quan sát thật | % |
|---|---|---|---|
| `credit_gdp_ratio` | BIS | 2.791 | 97.7% |
| `gdp_growth` | WB | 2.848 | 99.7% |
| `inflation` | WB | 2.836 | 99.3% |
| `trade_openness` | WB | 2.832 | 99.2% |
| `credit_gap` | BIS | 2.581 | 90.4% |
| `dsr` | BIS | 2.088 | 73.1% |
| `xborder_claims_usd_bn` | BIS LBS | 1.732 | 60.6% |
| `bank_assets_gdp` | WB | 1.336 | 46.8% |
| `bank_capital_assets` | WB | 1.312 | 45.9% |
| `domestic_credit_gdp` | WB | 952 | 33.3% |

**Quyết định quan trọng:** bản panel cũ (`ifwst_panel.csv`, annual) điền **median** cho ô NaN → `bank_capital_assets` và `bank_assets_gdp` chỉ **46–47% là dữ liệu thật**, phần còn lại là số bịa. Bản mới **giữ NaN** và báo cáo tỉ lệ thật.

WB chỉ có tần suất năm → nội suy tuyến tính **chỉ giữa các quan sát** (`interpolate(limit_area="inside")`), không `bfill` — nếu bfill, 100% "phủ" là giả (ví dụ `bank_capital_assets` Đức chỉ có 2 năm 2022–2023 nhưng bfill sẽ phủ đều 1990–2023).

---

## 4. Khủng hoảng

- **24 sự kiện** khủng hoảng ngân hàng hệ thống trong 20/21 nước (1990–2023), theo Laeven–Valencia.
- Mở rộng theo **quý**: `crisis_sys = 1` từ Q1 năm bắt đầu đến Q4 năm kết thúc.
- **303 quy** khủng hoảng trong panel (20/21 nước; Canada không có khủng hoảng hệ thống nào trong LV).
- `crisis_severity` = output loss (% GDP), fallback peak NPL.

### Đối chiếu bản cũ

| | Bản cũ (`crisis_dates.csv`) | Bản mới (LV thật) |
|---|---|---|
| Nguồn | **hardcode trong `code/04_crisis_dates.py`** | file xlsx Laeven–Valencia 2020 |
| Nước | 20 (ISO-3, sai tên: "China" không có crisis nhưng vẫn có crisis) | 21 ISO-2 chuẩn |
| Sự kiện | ~30 (nhiều mốc bịa, vd. USA 2007–2013 28 quý) | 24 (có start/end/output loss thật) |
| Vấn đề | Ghi chú trong code gọi đây là "Laeven-Valencia" nhưng **không tải file nào** | file thật, có thể trích dẫn |

**Sai lệch lớn nhất:** bản cũ gán JPN khủng hoảng 1990–2005 (64 quý, "Lost decade"). Laeven–Valencia ghi **1997–2001** cho Nhật. Bản cũ gán TUR tới 2020 (36 quý); LV ghi 2000–2001.

---

## 5. Biến dựng thêm

| Biến | Công thức |
|---|---|
| `sandpile_load` | `clip(1 - bank_capital_assets/10, 0, 1)` — mức nạp sandpile từ thiếu vốn |
| `network_density` | trade openness chuẩn hoá **trong nước** (min-max theo cty) |
| `credit_growth` | `% change` của `credit_gdp_ratio` theo quý (BIS) |
| `crisis_lag1` / `crisis_lead1` | shift ±1 quý |
| `pre_crisis` | `crisis_lead1==1 & crisis_sys==0` |
| `sandpile_network` | `sandpile_load × network_density` |

---

## 6. Cảnh báo cho bước phân tích

1. **24 sự kiện khủng hoảng là con số rất nhỏ** cho hồi quy EPV/diD. Tỉ lệ nổ khủng hoảng mục tiêu (treated) là 303/2856 ≈ 10.6% quan sát. Cần cân nhắc: (a) gộp thêm biến "crisis episode" dài hơn, (b) dùng `crisis_severity` như biến liên tục, (c) mô hình hóa `credit_gap` → `crisis` thay vì `crisis` → outcome.
2. **3 nước thiếu LBS** (CZ, HU, PL) — không có series trong BIS LBS publish.
3. **`bank_capital_assets` chỉ 46% phủ** và phân bố rất lệch (Đức 2/34 năm, Thụy Điển 8/34, Trung Quốc 8/34). `sandpile_load` dựa trên biến này sẽ có nhiều NaN → cần cân nhắc thay bằng DSR hoặc credit gap (đã có 90% phủ).
4. **`domestic_credit_gdp` chỉ 7/21 nước** (33%) — đã có `credit_gdp_ratio` từ BIS với 97.7% phủ, nên dùng bản BIS.
5. **Hai biến WB có thể rò rỉ tương lai**: `central_govt_debt_gdp` (17 nước) và `market_capitalization` — kiểm tra tần suất cập nhật trước khi dùng.

---

## 7. Tái lập

```bash
python code/00_probe_bis.py     # BIS SDMX + LBS 21 nước + Laeven–Valencia xlsx
python code/09_download_wb.py    # World Bank 21 nước, 1990-2023
python code/08_build_panel.py    # dựng panel → data/processed/ifwst_panel_quarterly.csv
```
