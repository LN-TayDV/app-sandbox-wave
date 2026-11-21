# Memory — IFWST / Cát Truồi

> Trạng thái ở đây phải **khớp** `PROJECT_STATUS.md` và `00_project_management/WORKFLOW.md` §0.
> Mọi mục đều kèm đường dẫn bằng chứng.

## Sản phẩm đã có

- [GĐ1] Tổng quan tài liệu — **PROVISIONAL**: `01_literature/Literature_Sources_Compilation.md` (~7 nguồn, 2 full-text PDF). ⚠️ `literature_matrix.csv` **RỖNG**; `critical_review.md` + `research_gap.md` chưa có
- [GĐ2] Khung lý thuyết — `02_conceptual_framework/IFWST_Conceptual_Framework.md` (3 lớp: Wave + Network + Sandpile)
- [GĐ3] Đặc tả mô hình — `03_model_specification/IFWST_Model_Specification.md` (M1/M2/M3, tham số, SVD, Sargan, backtest)
- [GĐ4] Chiến lược dữ liệu — `04_data/IFWST_Data_Collection_Strategy.md`
- [GĐ0] Tài liệu quản lý — `00_project_management/*` (7 file) + `RESEARCH_MANIFEST.md` + `README.md`

## Khoảng trống còn mở (gây chặn)

- `01_literature/literature_matrix.csv` — rỗng → **chặn GĐ1 và mọi tuyên bố về đóng góp**
- `01_literature/research_gap.md` — chưa có
- `data/raw/bis_*.csv`, `data/raw/imf_ifs.csv` — thiếu → **chặn GĐ4/GĐ5**
- `data/processed/ifwst_panel.csv` — biến là proxy + tần suất năm (9 lỗi: xem `PROJECT_STATUS.md` §2)
- `code/08`–`code/16` — chưa có → **chặn GĐ5**
- `09_thesis/` — chưa có → **chặn GĐ6/GĐ7**
- `theory/` — chưa có → tầng trích xuất tri thức 4 cuốn (BƯỚC 2–B7)

## Quyết định kiến trúc (2026-10-22)

- Tầng tri thức dùng chung đặt tại `theory/`; trích xuất **hết** 4 cuốn sách làm nền toán học lý thuyết.
- Thực thi **tuần tự theo pha**; song song chỉ **bên trong** pha trích xuất (4 worker theo cuốn/chương).
- Registry là nguồn duy nhất cho phương trình được trích dẫn: `global_id` + trang in + trang PDF + `verification_status`.
- Không sửa `research/microeconomics-pindyck-rubinfeld/` và `research/advanced-macroeconomics-fourth-edition/` — chỉ đọc.
- Chi tiết: `00_project_management/decision_log.md`.

## Project Progress

**Giai đoạn 0** ✅ — Kiểm kê dự án (2026-10-17)
**Giai đoạn 1** ⚠️ PROVISIONAL — Tổng quan tài liệu (matrix rỗng)
**Giai đoạn 2** ✅ — Khung lý thuyết (2026-10-17)
**Giai đoạn 3** ✅ — Đặc tả mô hình (2026-10-17)
**Giai đoạn 4** ⚠️ PARTIAL — Dữ liệu (chỉ World Bank proxy; thiếu BIS/IMF)
**Giai đoạn 5** ⬜ — Thực nghiệm
**Giai đoạn 6** ⬜ — Viết luận văn
**Giai đoạn 7** ⬜ — Kiểm định cuối

**Bước workflow hiện tại: B0 ✅ → B1 (probe khả thi dữ liệu).**
Xem `00_project_management/WORKFLOW.md`.
- [Kilo prompts theory structure](kilo_prompts_theory_structure.md) — hook
