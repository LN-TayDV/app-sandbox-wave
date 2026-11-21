# PROMPT 11 — B11: GĐ5 — THỰC NGHIỆM

> **Đọc trước:** `00-shared-contract.md` · `03_model_specification/IFWST_Model_Specification.md` (B9) · `04_data/IFWST_Data_Collection_Strategy.md` · `data/variable_dictionary.csv` (B10)
> **Bước workflow:** B11 · **Ước lượng:** 2–3 tuần
> **Mục tiêu:** ước lượng mô hình, kiểm định H1–H5, và **báo cáo trung thực cả kết quả trái kỳ vọng**.
> **Cấm:** không chỉnh mô hình đến khi kết quả "đẹp". Không bỏ biến không đáng ký mà không nói.

---

## 1. Hiện trạng

- `code/` có `01`–`07` (pipeline dữ liệu) + `08`–`12` (sẽ có sau B10). **Chưa có script ước lượng.**
- `WORKFLOW.md` (gốc) mô tả `code/` tới `code/16` → cần viết `13`–`16`.
- `03_model_specification/IFWST_Model_Specification.md` đã có: M1/M2/M3, định nghĩa tham số, SVD, kiểm định Sargan, backtest.
- `04_data/IFWST_Data_Collection_Strategy.md` có chiến lược dữ liệu.

## 2. Hành động

### 2.1 Viết `code/13`–`code/16`

| Script | Vai trò |
|---|---|
| `code/13_estimate_base.py` | M1 (mô hình cơ sở) — ước lượng, SE phù hợp (cluster theo nước), xuất bảng kết quả |
| `code/14_estimate_extended.py` | M2/M3 (mô hình mở rộng) + kiểm định H1–H5 |
| `code/15_robustness.py` | Độ bền: thay đổi λ của HP filter · thay biến phụ thuộc (liên tục ↔ nhóm con) · thay mẫu · bỏ dị bất lợn · trùng lặp chéo (Hausman) |
| `code/16_backtest_report.py` | Backtest ngoài mẫu + dự báo sớm + bảng tổng hợp kết quả |

**Yêu cầu kỹ thuật bắt buộc:**
- **Deterministic**: chạy 2 lần → output giống hệt (fix `random_state`).
- Mỗi script có `--help`, `--input`, `--output`, `--seed`.
- **Log đầy đủ**: ghi số quan sát, số nước, số kỳ, phương pháp ước lượng, cảnh báo (dropped obs, collinearity, non-convergence) vào `logs/estimation/{script}_{timestamp}.log` **hoặc** `logs/estimation/latest.log` (ghi đè, kèm timestamp trong nội dung).
- Không nuốt lỗi (`try/except` phải `raise` sau khi ghi log).
- Ghi kết quả ra `output/tables/*.csv` + `output/figures/*.png` + `output/estimation_log.md`.

### 2.2 Công suất thống kê — kiểm tra **trước** khi ước lượng

B1 đã đo số sự kiện khủng hoảng. **Trước khi chạy M1/M2**, ghi ra:
- Số sự kiện × số tham số → **EPV** (events per variable)
- Nếu EPV < 10 → **cảnh báo rõ** và cân nhắc mô hình thay thế (biến phụ thuộc liên tục, hoặc giảm tham số, hoặc penalized likelihood).
- Ghi cảnh báo vào `output/estimation_log.md` — **không** bỏ qua.

### 2.3 Kiểm định H1–H5

Mỗi giả thuyết: cách kiểm định · kết quả · giá trị p · khoảng tin cậy · **kết luận** (chấp nhận / bác bỏ / không đủ bằng chứng).

**Cấm** viết "H2 được chứng minh" khi p = 0.08 — viết "không bác bỏ ở mức 5%, bằng chứng yếu ở mức 10%".

### 2.4 Phân tích kết quả trái kỳ vọng

Bắt buộc có mục riêng cho **kết quả trái kỳ vọng**: giả thuyết nào bị bác bỏ, tại sao, và điều đó có làm suy yếu luận văn không. Nếu không có kết quả trái kỳ vọng nào → kiểm tra lại xem có phải vì chưa kiểm định nghiêm không.

### 2.5 Kiểm tra độ bền bắt buộc

| Kiểm tra | Lý do |
|---|---|
| λ của HP filter | kết quả `credit_gap` phụ thuộc mạnh vào λ |
| Biến phụ thuộc: liên tục ↔ nhóm con khủng hoảng | công suất thống kê thấp |
| Thay đổi mẫu (bỏ nước có tỷ lệ missing cao) | chọn mẫu có thể tự lựa chọn |
| Hausman FE vs RE | ảnh hưởng kết luận H1–H5 |
| Với/without dị bất lợn | có thể thay đổi kết luận |
| Cluster SE theo nước vs theo nước×năm | suy ra sai khi tương quan theo thời gian |

## 3. Acceptance criteria

| # | Tiêu chí | Bằng chứng |
|---|---|---|
| A1 | `code/13`–`code/16` tồn tại, chạy được, có `--help` | output |
| A2 | Chạy end-to-end từ `data/processed/ifwst_panel.csv` → bảng + biểu đồ + log, **không lỗi** | output thật |
| A3 | Deterministic: chạy 2 lần → hash output giống hệt | hash |
| A4 | `output/estimation_log.md` có số quan sát, số nước, số kỳ, phương pháp ước lượng, cảnh báo | đọc file |
| A5 | **EPV được tính và ghi cảnh báo** nếu < 10 | đọc log |
| A6 | H1–H5: mỗi giả thuyết có cách kiểm định + p + CI + kết luận trung thực | bảng kết quả |
| A7 | Có mục phân tích kết quả trái kỳ vọng | `output/estimation_log.md` |
| A8 | 6 kiểm tra độ bền §2.5 đã chạy, có bảng | output |
| A9 | Mọi bảng/biểu đồ có **nguồn số liệu** truy vết được (script + file + tham số) | đọc bảng |
| A10 | Có kiểm tra rò rỉ dữ liệu: biến trong mô hình không chứa thông tin tương lai (lookahead) | mô tả kiểm tra + kết quả |

## 4. Cổng đạt

A1–A10 đạt → tick B11 ✅ → sang B12.

**Lưu ý:** kết quả **trái kỳ vọng không phải** lý do để BLOCKED. BLOCKED chỉ khi không thể ước lượng được.

## 5. Cập nhật trạng thái

`theory/docs/KILO_STATUS.md` · `00_project_management/WORKFLOW.md` §0 · `PROJECT_STATUS.md` · `MEMORY.md` · `logs/execution_log.md` · `00_project_management/task_backlog.md`
