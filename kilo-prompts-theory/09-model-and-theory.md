# PROMPT 09 — B9: GĐ2 + GĐ3 — RÀ LẠI KHUNG LÝ THUYẾT & ĐẶC TẢ MÔ HÌNH (có tầng `theory/`)

> **Đọc trước:** `00-shared-contract.md` · `theory/docs/COVERAGE_REPORT.md` (B7) · `theory/docs/CROSS_BOOK_INDEX.md` (B6)
> **Bước workflow:** B9 · **Ước lượng:** 2 tuần
> **Mục tiêu:** nâng GĐ2/GĐ3 từ "bản nháp tốt" lên "đã đối chiếu được với nguồn gốc" — **dựa trên tầng `theory/` đã xác minh**.
> **Cấm:** không bịa. Không tự xác nhận phương trình chưa có bằng chứng.

---

## 1. Hiện trạng (đã kiểm chứng)

| Artifact | Trạng thái | Hạn chế còn lại |
|---|---|---|
| `02_conceptual_framework/IFWST_Conceptual_Framework.md` | 14.020 B · kiến trúc 3 lớp Wave + Network + Sandpile | Chưa đối chiếu nguồn; chưa gắn `global_id` |
| `03_model_specification/IFWST_Model_Specification.md` | 8.849 B · M1/M2/M3, tham số, SVD, Sargan, backtest | Chưa đối chiếu nguồn; **typo dòng 232** (`Stata: s пространный`) |

**Trước B9, GĐ2/GĐ3 được đánh dấu ✅ vì "có file" — không phải vì "đã xác minh".** B9 là bước đóng bằng chứng cho 2 giai đoạn đó.

## 2. Hành động

### 2.1 Gắn mọi khái niệm vào `global_id`

Lập bảng ánh xạ trong `02_conceptual_framework/`:

| Khái niệm trong framework | Nguồn (`book_code` + `global_id` + trang) | Nhãn bằng chứng | Ghi chú khác biệt |
|---|---|---|---|
| Sóng tài chính (financial wave) | `TH-ROM-00xx` (tr. N) | `BOOK_EVIDENCE` | Romer mô tả ở góc khác — xem `CROSS_BOOK_INDEX.md` |

**Mục tiêu:** **mọi** khái niệm trong framework phải có ít nhất một dòng trích dẫn `global_id`, hoặc được ghi rõ là **suy ra** (`RESEARCH_SYNTHESIS`) nếu là đóng góp riêng của luận văn.

Đây là điểm mấu chốt: tác giả luận văn **không** phải xác nhận điều sách chưa nói.

### 2.3 Rà đặc tả mô hình

Với **mỗi** phương trình trong `03_model_specification/IFWST_Model_Specification.md`:

| Cột | Nội dung |
|---|---|
| `equation_id` | mã nội bộ của luận văn |
| `source_global_id` | `global_id` trong `theory/registry/equation_registry.csv` — hoặc `ORIGINAL` nếu là phương trình do luận văn đề xuất |
| `evidence` | `BOOK_EVIDENCE` / `DERIVED_RESULT` / `RESEARCH_HYPOTHESIS` |
| `printed_page` | trang in trong sách |
| `verified` | `FORMULA_VERIFIED` / `FORMULA_UNVERIFIED` / `NUMERICALLY_VERIFIED` |

**Bắt buộc:** mọi phương trình **có nguồn** phải truy được tới một dòng trong `theory/registry/equation_registry.csv`. Phương trình **không có nguồn** → ghi `ORIGINAL` + lý do + trạng thái `FORMULA_UNVERIFIED` (đừng tự xác nhận).

**Sửa typo dòng 232** trong lúc rà.

### 2.4 Thêm phần "Giới hạn của mô hình"

Viết rõ 3 điều:
1. Mô hình **không** mô tả được cái gì
2. Những giả định nào **chưa kiểm định được** với dữ liệu hiện có
3. Điều gì sẽ khiến mô hình **sai** (điều kiện phản bác)

### 2.5 Khớp với ràng buộc thống kê từ B1

`04_data/feasibility_probe.md` (B1) đã chốt số sự kiện khủng hoảng khả dụng. **Đặc tả mô hình phải khớp với đó:**
- Nếu số sự kiện quá ít cho logit 7 biến → đặc tả phải chuyển sang **biến phụ thuộc liên tục** + khủng hoảng là nhóm con.
- Nếu tần suất là **quý** → mô hình phải dùng cấu trúc panel quý, có thời gian trong mô hình.
- Ghi rõ mô hình **dự kiến** và mô hình **thay thế** nếu ràng buộc dữ liệu khác.

## 3. Acceptance criteria

| # | Tiêu chí | Bằng chứng |
|---|---|---|
| A1 | Mọi khái niệm trong `02_conceptual_framework/` có dòng trích dẫn `global_id` **hoặc** nhãn `RESEARCH_SYNTHESIS` | bảng ánh xạ |
| A2 | Bảng ánh xạ dùng `global_id` **có thật** trong `theory/registry/` — không bịa mã | script kiểm: mọi `global_id` trong bảng tồn tại |
| A3 | Mọi phương trình trong `03_model_specification/` có `source_global_id` **hoặc** `ORIGINAL` | rà từng phương trình |
| A4 | Mọi phương trình có nguồn → truy được tới dòng trong `equation_registry.csv` | script kiểm |
| A5 | Không phương trình nào bị nâng lên `FORMULA_VERIFIED` khi chưa đối chiếu | đối chiếu registry |
| A6 | Typo dòng 232 đã sửa | đọc lại dòng |
| A7 | Có mục "Giới hạn của mô hình" với 3 phần §2.4 | đọc file |
| A8 | Đặc tả **khớp** ràng buộc thống kê từ `04_data/feasibility_probe.md` | đối chiếu, nêu rõ |
| A9 | `PROJECT_STATUS.md` + `MEMORY.md` + `task_backlog.md` được cập nhật: GĐ2/GĐ3 ghi rõ **đã đối chiếu với `theory/`** | đọc lại |
| A10 | Không sửa file trong `theory/registry/` (chỉ trích dẫn) | `git status` |

## 4. Cổng đạt

A1–A10 đạt → tick B9 ✅ → sang B10 (dữ liệu thật).

## 5. Cập nhật trạng thái

`theory/docs/KILO_STATUS.md` · `00_project_management/WORKFLOW.md` §0 · `PROJECT_STATUS.md` · `MEMORY.md` · `logs/execution_log.md` · `00_project_management/task_backlog.md`
