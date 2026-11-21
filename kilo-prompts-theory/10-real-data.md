# PROMPT 10 — B10: GĐ4 — DỮ LIỆU THẬT (sửa 9 lỗi D1–D9)

> **Đọc trước:** `00-shared-contract.md` · `04_data/feasibility_probe.md` (B1) · `03_model_specification/IFWST_Model_Specification.md` (B9)
> **Bước workflow:** B10 · **Ước lượng:** 2–3 tuần
> **Mục tiêu:** thay dữ liệu **proxy** hiện tại bằng dữ liệu **thật**, và làm mọi biến khớp với định nghĩa trong khung lý thuyết.
> **Cấm:** không đổi định nghĩa biến để hợp với dữ liệu sẵn có. Nếu dữ liệu không đủ → báo, không tự bịa.

---

## 1. Hiện trạng — 9 lỗi đã kiểm chứng

| # | Lỗi | Bằng chứng | Sửa ở |
|---|---|---|---|
| **D1** | Thiếu 3 nguồn then chốt: không có `bis_credit.csv`, `bis_crossborder.csv`, `imf_ifs.csv` | `data/raw/` chỉ có `wb_*.csv` + `crisis_dates*.csv`; `code/01_download_bis.py:52-55` có **fallback về World Bank** ("This is proxy data") | 10.2 |
| **D2** | `credit_gap` **không phải** credit gap BIS. Là lệch so với trung bình 5 năm **không trung tâm**, không phải HP filter λ=400.000 như `tasks/task_data_collection.md` bước 5 yêu cầu | `code/05_derived_final.py:91-93` | 10.3 |
| **D3** | `sandpile_load` = `1 − capital/10` → **hằng số 0.2 suốt giai đoạn ở Brazil** ⇒ biến không biến động. Không phải "tích lũy tổn thất / bộ đệm" | `code/05_derived_final.py:100-102` | 10.4 |
| **D4** | `network_density` = `trade_openness / max(trade_openness)` → mở thương chuẩn hóa, **không phải mật độ mạng tài chính**. H4 (sóng/lan truyền) đang đo sai đại lượng | `code/05_derived_final.py:110-111` | 10.4 |
| **D5** | `regime` = `1{gdp_growth > 0}` → không phải chuyển chế độ boom/bust. H2 (đa thang đo) không kiểm định được | `code/05_derived_final.py:118-119` | 10.4 |
| **D6** | **Tần suất NĂM**, không phải QUÝ như `03_model_specification` §5.1 | `ifwst_panel.csv`: 1990–2023, 714 dòng | 10.6 |
| **D7** | `data_quality_report.md` kết luận "Data is ready for analysis" nhưng chỉ kiểm missing/range/outlier — **không** kiểm validness cấu trúc | `output/data_quality_report.md:50-53` | 10.5 |
| **D8** | **4 script derived trùng nhau**; bản "final" (14 cột) ≠ producer thật của panel (19 cột, `code/06_panel.py`) | `code/05_derived{,_simple,_v2,_final}.py` | 10.6 |
| **D9** | **Thiếu tầng truy vết dữ liệu**: không có `source_registry.csv`, `variable_dictionary.csv`, `formula_registry.csv` | `data/` chỉ có `raw/` + `processed/` | 10.2 |

## 2. Hành động

### 2.1 Tải dữ liệu thật (theo kết quả B1)

Dùng `04_data/feasibility_probe.md` làm danh sách nguồn đã xác minh. **Bắt buộc:** sửa `code/01_download_bis.py` để **bỏ fallback World Bank** — hoặc fallback phải **ghi cảnh báo to** vào log + tên file khác (`*_PROXY.csv`).

Nguyên tắc: **dữ liệu proxy không được trộn vào dữ liệu thật** trong cùng cột mà không ghi nhãn.

### 2.2 Tầng truy vết (D9) — tạo trong `data/`

| File | Nội dung |
|---|---|
| `data/source_registry.csv` | nguồn · URL · tần suất · phạm vi · ngày tải · sha256 · giấy phép · **có phải proxy không** |
| `data/variable_dictionary.csv` | biến · định nghĩa · đơn vị · nguồn · công thức · `global_id` liên quan (từ `theory/`) |
| `data/formula_registry.csv` | biến phái sinh · công thức · tham số · biến đầu vào · dựa trên nguồn nào |
| `data/data_inventory.csv` | inventory file · số dòng · số cột · khoảng thời gian · số quốc gia |

**Cột `global_id`** trong `variable_dictionary.csv` là cầu nối giữa dữ liệu và tầng `theory/` — **bắt buộc có** cho biến trung tâm.

### 2.3 Sửa `credit_gap` (D2)

Định nghĩa đúng (theo `tasks/task_data_collection.md` bước 5): **HP filter với λ = 400.000** trên `credit_to_private_sector / GDP`, lấy **khoảng cách** (gap) giữa thực tế và xu hướng (deviation), **không** phải lệch so với trung bình 5 năm.

- Phải ghi rõ: λ, đoạn xu hướng, xử lý đầu–cuối mẫu, tần suất.
- Kiểm nghiệm độ nhạy với λ (bảng so sánh λ ∈ {10000, 100000, 400000, 1000000}) — **đây là kiểm định độ bền bắt buộc**, vì kết quả phụ thuộc mạnh vào λ.
- Nếu chỉ có World Bank (proxy) → **ghi nhãn `proxy = TRUE`** trong `variable_dictionary.csv` và `source_registry.csv`, và nêu trong báo cáo rằng kết luận về `credit_gap` là **giới hạn**.

### 2.4 Sửa 3 biến sai định nghĩa (D3, D4, D5)

| Biến | Định nghĩa đúng theo khung lý thuyết | Gợi ý nguồn |
|---|---|---|
| `sandpile_load` | Tích lũy tổn thất so với bộ đệm vốn có (tỷ lệ bị hấp thụ) — **phải biến động theo thời gian và khác nhau giữa các nước** | tổn thất tín dụng (NPL) / vốn, hoặc mô phỏng từ `network` |
| `network_density` | Mật độ mạng tài chính (bằng chứng liên kết bảng cân đối) | BIS LBS cross-border + liên kết ngân hàng |
| `regime` | Chuyển chế độ boom/bust (vd: theo dấu chu kỳ nghiệp vụ, hoặc phân loại 2 nhóm tăng trưởng/giảm) | GDP growth + bộ lọc Kalman/Hodrick-Prescott trên cycle |

**Bắt buộc:** mỗi biến sau khi sửa phải có **thống kê mô tả** chứng minh nó biến động (std > 0, phân bố khác nhau giữa các nước). Nếu vẫn là hằng số → biến vẫn sai.

### 2.5 Kiểm tra chất lượng thật (D7)

`output/data_quality_report.md` mới phải kiểm:
- missing theo từng biến × từng nước × từng năm
- **tần suất** (đồng nhất không)
- **construct validity**: mỗi biến có khớp định nghĩa trong `variable_dictionary.csv` không — kiểm bằng tiêu chí kiểm định cụ thể, không nói chung
- **độ phủ** từng nguồn (BIS/IMF có phủ đủ 21 nước × 34 năm không)
- so sánh **tương quan** với World Bank để phát hiện sai khớp nguồn
- **tỷ lệ trùng**, giá trị bất thường, và **cảnh báo khi một biến hằng số**

### 2.6 Dọn code (D8) và tần suất (D6)

- Gộp 4 script `05_derived*.py` thành **một** `code/05_derived.py` (giữ `05_derived_final.py` làm gốc, bỏ 3 bản trùng — **ghi lại trong báo cáo**, đừng xóa im lặng).
- Chuyển tần suất sang **quý** nếu nguồn cho phép (BIS/ECB/IMF đều có quý). Nếu không → ghi rõ và **điều chỉnh đặc tả mô hình** ở B9 tương ứng, ghi vào `theory/GAP_REQUESTS.md`.
- Script phải **deterministic**: chạy 2 lần cho output giống hệt.

### 2.7 Thiếu `code/08`–`code/16`

`00_project_management/WORKFLOW.md` (gốc) mô tả pipeline `code/01`–`code/16` nhưng **chỉ có `01`–`07`**. Viết các script còn thiếu cho phần **chuẩn bị dữ liệu** (phần ước lượng thuộc B11):
`08` · panel construction cuối cùng · `09` · tạo biến phái sinh từ định nghĩa đã sửa · `10` · tầng truy vết dữ liệu · `11` · kiểm tra chất lượng mở rộng · `12` · dữ liệu phụ trợ (Ảnh hưởng).

> **Ghi rõ ranh giới:** script ước lượng (`13`–`16`) thuộc **B11**, **không** làm ở bước này.

## 3. Acceptance criteria

| # | Tiêu chí | Bằng chứng |
|---|---|---|
| A1 | `data/source_registry.csv`, `variable_dictionary.csv`, `formula_registry.csv`, `data_inventory.csv` tồn tại, đủ cột | đọc file |
| A2 | `variable_dictionary.csv` có cột `global_id`; các `global_id` **tồn tại thật** trong `theory/registry/` | script kiểm |
| A3 | D1: có file BIS/IMF thật **hoặc** bản `_PROXY` được ghi nhãn đầy đủ | đọc `data/raw/` + registry |
| A4 | D2: `credit_gap` dùng HP λ=400.000; **có bảng nhạy cảm λ** | output script + bảng |
| A5 | D3/D4/D5: 3 biến có **thống kê mô tả chứng minh biến động** (std>0, khác nhau giữa nước) | output thống kê |
| A6 | D6: tần suất khớp đặc tả (quý) — hoặc có ghi nhận điều chỉnh ở `theory/GAP_REQUESTS.md` | đọc + đếm |
| A7 | D7: `data_quality_report.md` mới có phần **construct validity** + độ phủ theo nguồn + cảnh báo biến hằng số | đọc file |
| A8 | D8: còn **đúng 1** script derived; chạy 2 lần → output giống hệt | `ls` + hash |
| A9 | `code/08`–`code/12` tồn tại, chạy được (`--help`) | output |
| A10 | `ifwst_panel.csv` mới: số dòng × số cột × số nước được ghi lại; **không** còn biến proxy không nhãn | đọc + thống kê |
| A11 | Không sửa file trong `theory/`, `research/`, `data/book/`, `tasks/` | `git status` |

## 4. Cổng đạt

A1–A11 đạt → tick B10 ✅ → sang B11.

**Nếu dữ liệu thật không lấy được** (D1 chưa giải quyết được) → ghi `BLOCKED` **kèm hệ quả**: kết luận nào của luận văn bị giới hạn. Đây là thông tin quan trọng, phải nói rõ chứ không giấu.

## 5. Cập nhật trạng thái

`theory/docs/KILO_STATUS.md` · `00_project_management/WORKFLOW.md` §0 · `PROJECT_STATUS.md` · `MEMORY.md` · `logs/execution_log.md` · `00_project_management/task_backlog.md` · `theory/GAP_REQUESTS.md`
