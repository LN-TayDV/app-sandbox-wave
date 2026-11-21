# PROMPT 04 — B4: PILOT HANSEN CHƯƠNG 7 (GMM)

> **Đọc trước:** `00-shared-contract.md` · **Điều kiện:** B3 đã qua cổng
> **Bước workflow:** B4 · **Ước lượng:** 1 ngày
> **Mục tiêu:** **đo chi phí thật** trước khi cam kết 2–3 tuần cho B5.
> **Cấm:** không làm chương thứ 2 của bất kỳ cuốn nào. Không chỉnh số đo dự đoán trước.

---

## 1. Vì sao chọn Hansen Ch.7

Chương 7 của Hansen (*Econometrics*, 2014) — **Identification / GMM** — là chương phương pháp quan trọng nhất với luận văn:
- GMM là phương pháp ước lượng mà `03_model_specification/IFWST_Model_Specification.md` dự kiến dùng (có kiểm định Sargan / Hansen J, kiểm định Hansen J, moment conditions).
- Đồng thời là **bài toán toán học nặng nhất** trong 4 cuốn (nhiều định nghĩa, điều kiện nhận dạng, định lý, giới hạn).

→ Pilot ở chỗ khó nhất = giá trị đo tối đa. Nếu chương dễ mà vẫn ổn, còn gì phải lo.

## 2. Hành động

### 2.1 Chạy trọn pipeline L0 → L5 trên Hansen Ch.7

L0 (text) đã có từ B2. Từ L1 trở đi, làm **đầy đủ theo SOP** (`theory/docs/EXTRACTION_SOP.md`):
- L1 · segment → chunks
- L2 · index FTS5
- L3 · trích **nội dung** theo 10 loại `kind` → registry CSV
- L4 · verify toán học 3 bậc A/B/C
- L5 · báo cáo chương

### 2.2 Đo đúng 4 con số (không dự đoán trước)

| # | Con số | Cách đo | Cần để làm gì |
|---|---|---|---|
| **M1** | **Bậc toán học** | phân bổ các phương trình theo bậc A (text layer sạch) / B (mất vị trí chỉ số) / C (công thức là ảnh) | quyết định có cần OCR/vision cho 4 cuốn |
| **M2** | **Giờ thực tế** | đo bằng đồng hồ: thời gian ingest + segment + index + trích + verify cho 1 chương | định lịch B5 (4 worker × số chương) |
| **M3** | **Số unit sinh ra** | đếm dòng mỗi registry sinh ra | ước lượng tổng khối lượng 4 cuốn |
| **M4** | **Tỉ lệ verify tự động pass** | số phương trình `FORMULA_VERIFIED`+`NUMERICALLY_VERIFIED` / tổng số phương trình | quyết định mức độ cần người kiểm tay |

Ghi **cả 4** vào `theory/PILOT_REPORT.md`, kèm phương pháp đo (lệnh + output).

### 2.3 Dùng `scientific/registry.py` để verify

```
C:\Users\PC\Documents\AI_project\sandbox-financial\research\advanced-macroeconomics-fourth-edition\scientific\registry.py
```
374 dòng, 4 lớp: **source → symbolic → numeric → render**. Dùng để đối chiếu phương trình bậc C (công thức là ảnh).

**Copy** sang `theory/scripts/registry.py` và sửa bản copy (không sửa bản gốc trong `research/`).

### 2.4 Quyết định mở rộng

`theory/PILOT_REPORT.md` phải kết luận **một** trong:
- **MỞ RỘNG** cả 4 cuốn với định dạng hiện tại → kèm lịch dự kiến (tính từ M2 × số chương × số worker)
- **THU HẸỊ ĐỊNH DẠNG UNIT** (ví dụ: chỉ trích `equation` + `assumption` + `theorem`, bỏ `exercise`) → kèm lý do và cái giá bị mất
- **CẦN XỬ LÝ TOÁN HỌC BỔ SUNG** (ví dụ: tỉ lệ bậc C quá cao → cần thêm quy trình render-diff) → kèm kế hoạch

Không chọn "mở rộng" một cách mơ hồ. Số phải ra từ đo.

## 3. Acceptance criteria

| # | Tiêu chí | Bằng chứng |
|---|---|---|
| A1 | Chương 7 của HAN có chunk trong `theory/books/HAN/` | `coverage.json` |
| A2 | Có registry riêng cho chương: `theory/books/HAN/units/*.csv` | đọc file, đếm dòng |
| A3 | `theory/PILOT_REPORT.md` có đủ **4 con số** M1–M4, mỗi con số kèm lệnh đo + output | đọc file |
| A4 | `logs/quality.json` tồn tại, có số đo bằng chứng | đọc file |
| A5 | Validator chạy xanh trên registry của chương 7 (hoặc nêu rõ lỗi còn lại) | output validator |
| A6 | Có `theory/docs/CHAPTER_REPORT_HAN_07.md` theo mẫu SOP | đọc file |
| A7 | `theory/PILOT_REPORT.md` có quyết định rõ ràng (MỞ RỘNG / THU HẸỊ / BỔ SUNG) kèm lịch dự kiến | đọc file |
| A8 | **Không** có chương nào khác của bất kỳ cuốn nào bị trích xuất | `git status` + đếm file trong `theory/books/*/units/` |

## 4. Cổng đạt

A1–A8 đạt → **đây là lệnh cho B5**. Ghi rõ trong báo cáo: "ĐÃ RA LỆNH B5" hoặc "CHƯA ĐỦ ĐIỀU KIỆN — cần làm lại pilot với định dạng đã thu hẹp".

## 5. Cập nhật trạng thái

`theory/docs/KILO_STATUS.md` · `00_project_management/WORKFLOW.md` §0 · `logs/execution_log.md` · `00_project_management/task_backlog.md` · `00_project_management/decision_log.md` (nếu có quyết định thu hẹp phạm vi)
