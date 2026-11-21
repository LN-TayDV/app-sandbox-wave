# Execution Log — IFWST / Cát Truồi

> Nguyên tắc: ghi **việc đã thực sự làm**, kèm đường dẫn sản phẩm. Không ghi ý định.

| Ngày | Công việc | Sản phẩm / Kết quả | Ghi chú |
|------|-----------|-------------------|---------|
| 2026-10-17 | Đọc bản mệnh lệnh init-task.md | `tasks/init-task.md` (1102 dòng) | Xác nhận mục tiêu, phạm vi, giai đoạn thực thi |
| 2026-10-17 | Kiểm tra thư mục `sandbox-financial` | Chỉ có `tasks/init-task.md` | Thư mục tồn tại, chưa có tài sản khác |
| 2026-10-17 | Tạo tài liệu quản lý Giai đoạn 0 | `README.md`, `PROJECT_STATUS.md`, `RESEARCH_MANIFEST.md`, `00_project_management/*` | Cấu trúc dự án đã được thiết lập |
| 2026-10-17 18:14 | Tạo khung `literature_matrix.csv` | `01_literature/literature_matrix.csv` (309 B) | **Chỉ có header — chưa điền dữ liệu** |
| 2026-10-17 18:20 | Lập nhật ký tìm kiếm | `01_literature/search_log.csv` (3.907 B) | Ghi lại truy vấn + nguồn |
| 2026-10-17 19:13 | Tải tài liệu nguồn | `01_literature/sources/` (2 PDF + 2 TXT) | Full-text có sẵn cho 2 nguồn |
| 2026-10-17 19:17 | Tổng hợp tài liệu | `01_literature/Literature_Sources_Compilation.md` (12.049 B) | ~7 nguồn, 3 nhóm chính |
| 2026-10-17 19:19 | Đóng GĐ1 (ghi nhớ) | `memory/literature-research-complete.md` | Ghi nhận "hoàn thành" — **thực tế là PROVISIONAL** (matrix rỗng) |
| 2026-10-17 19:51 | Xây khung lý thuyết | `02_conceptual_framework/IFWST_Conceptual_Framework.md` (14.020 B) | Kiến trúc 3 lớp Wave + Network + Sandpile |
| 2026-10-17 19:52 | Đóng GĐ2 | `memory/conceptual-framework-complete.md` | — |
| 2026-10-17 19:58 | Đặc tả mô hình | `03_model_specification/IFWST_Model_Specification.md` (8.849 B) | M1/M2/M3, SVD, Sargan, backtest; typo dòng 232 |
| 2026-10-17 20:00 | Đóng GĐ3 | `memory/model-specification-complete.md` | — |
| 2026-10-17 20:06 | Chiến lược dữ liệu | `04_data/IFWST_Data_Collection_Strategy.md` (11.816 B) | 7 nguồn, 6 bước |
| 2026-10-17 20:07 | Đóng GĐ4 | `memory/data-strategy-complete.md` | Ghi nhận "hoàn thành" — **thực tế PARTIAL** (chỉ World Bank) |
| 2026-10-17 20:36 | Viết `code/01_download_bis.py` | 3.352 B | Dòng 52–55: **fallback về World Bank** khi BIS lỗi |
| 2026-10-17 20:37–20:43 | Chạy 4 script tải dữ liệu | `data/raw/` 23 file (`wb_*` + `crisis_dates*`) | **Không có `bis_*.csv` hay `imf_ifs.csv`** → BIS/IMF thất bại |
| 2026-10-17 20:46–20:47 | Ngày khủng hoảng | `data/raw/crisis_dates.csv` (16.933 B), `crisis_dates_annual.csv`, `crisis_severity.csv` | — |
| 2026-10-17 20:57–21:10 | Script derived (4 bản) | `code/05_derived{,_simple,_v2,_final}.py` | **4 bản trùng nhau**, chỉ `_final` được giữ |
| 2026-10-17 21:20 | Ghép panel | `code/06_panel.py` → `data/processed/ifwst_panel.csv` | 714 dòng × 19 cột, 21 nước, 1990–2023, **tần suất năm** |
| 2026-10-17 21:23 | Tóm tắt panel | `output/panel_summary.csv` (2.165 B) | — |
| 2026-10-17 21:30 | Kiểm tra chất lượng | `code/07_quality.py` (6.234 B) | Chỉ missing/range/outlier |
| 2026-10-17 21:32 | Báo cáo chất lượng | `output/data_quality_report.md` (1.289 B) | Kết luận "ready" — **thiếu kiểm validness cấu trúc** |
| 2026-10-22 08:38 | Trích xuất MICRO (Pindyck–Rubinfeld) | `research/microeconomics-pindyck-rubinfeld/` | L0 787/787 trang, 0 failed, 18 short; 34/34 browser smoke, 75/75 pytest, 21/21 node |
| 2026-10-22 08:41 | Trích xuất MACRO (Romer) | `research/advanced-macroeconomics-fourth-edition/` | L0 738/738 trang, 0 failed, 8 short (front matter); có `chapter_ranges` 12 chương |
| 2026-10-22 | Khảo sát repo để thiết kế workflow trích xuất | Đọc `master-idea.md`, `init-task.md`, `PROJECT_STATUS.md`, `WORKFLOW.md`, 2 repo research, `skills/*` | Xác định mâu thuẫn PIN 787 vs 761; schema registry 16/19 cột trùng khớp giữa 2 cuốn |
| 2026-10-22 | Tạo workflow chuẩn 13 bước | `00_project_management/WORKFLOW.md` | B0–B12, cổng đạt, cấm đoán, lịch 6 tuần, mẫu báo cáo phiên |
| 2026-10-22 | Tạo trang điều hướng | `00_project_management/START_HERE.md` (126 dòng) | Bản đồ file → câu hỏi; bảng lỗi sai lệch trong repo |
| 2026-10-22 | Sửa `WORKFLOW.md` gốc | Thêm banner trỏ sang workflow mới | Ghi rõ `code/08`–`code/16` chưa tồn tại |
| 2026-10-22 | Ghi 5 quyết định | `00_project_management/decision_log.md` | Workflow 13 bước · tầng `theory/` · tuần tự theo pha · registry là nguồn duy nhất · repo research chỉ đọc |
| 2026-10-22 | **B0 — Đồng bộ repo** | `PROJECT_STATUS.md`, `MEMORY.md`, `00_project_management/task_backlog.md`, `logs/execution_log.md` | GĐ1 → PROVISIONAL, GĐ4 → PARTIAL; 9 lỗi dữ liệu D1–D9 ghi rõ bằng đường dẫn |
| 2026-10-22 | Probe sơ bộ 12 endpoint dữ liệu | `04_data/feasibility_probe.md` (SƠ BỘ) | ECB 200 · World Bank 200 · BIS `api/v1/dataflow` 200 (SDMX-ML XML) · IMF 200→403 (WAF) · FRED 200 nhưng body HTML · `macrohistory.org` DNS fail · `www.bis.org` 403 |
| 2026-10-22 | Trích cấu trúc DSD BIS credit gap | `feasibility_probe.md` §2.2 | 15 chiều (FREQ.BORROWERS_CTY.TC_BORROWERS.TC_LENDERS.CG_DTYPE + 10) · 4 codelist; key thử đều 404 → cần đủ 15 đoạn |
| 2026-10-22 | **Tạo bộ prompt thực thi cho luận văn** | `kilo-prompts-theory/` — 13 prompt (00–12) + `EXECUTION-MATRIX.md` + `ACCEPTANCE-CHECKLIST.md` + `README.md` | Ánh xạ 1-1 với B1–B12; prompt 01 nhúng sẵn kết quả probe để worker không dò lại từ đầu |
| 2026-10-22 | Gắn bộ prompt mới vào repo | `kilo-prompts/README.md` (banner trỏ), `00_project_management/WORKFLOW.md` (link), `task_backlog.md` (tick) | Tách 2 bộ: `kilo-prompts/` = app MACRO/MICRO (xong) · `kilo-prompts-theory/` = luận văn (đang chạy) |

2026-10-23T09:46:06.021148 | B4 redo pilot HAN Ch.13 | done | PILOT_REPORT updated, render-diff needed for equations

## B3 PASS - 2026-10-27
- Validator tests: 11 passed.
- Real errors found in 4 registries (see logs/registry_validation.json).

## B4 — Pilot Hansen Ch 7 (Restricted Estimation) - 2026-10-27
- L0: 14/14 trang covered (pdf 178–191, printed 169–182), 1 unresolved (pdf=182/printed=173), 0 image pages
- L1-L2: chunks.jsonl 26 section-level chunks, knowledge.db FTS5 index với 74 matches cho GMM/identification/moment
- L3: deduplicate ch07_units.csv 94→87 đơn vị (loại 7 trùng: theorem 7.5.1×2, 7.5.2×3, 7.6.1×3, exercise 7.5×2)
- L4: Phân loại A/B/C: Level A=20 (39.2%), Level B=7 (13.7%), Level C=24 (47.1%); chạy validate_theory_layer.py — 5/7 kiểm tra dữ liệu PASS, 2 FAIL do schema chênh lệch (không phải lỗi dữ liệu)
- L5: Tạo theory/docs/CHAPTER_REPORT_HAN_07.md, theory/PILOT_REPORT.md, logs/quality.json
- B5 decision: CẦN XỬ LÝ TOÁN HỌC BỞI SUNG (render-diff yêu cầu trước khi mở rộng sang 4 cuốn)
- Sản phẩm: theory/PILOT_REPORT.md · theory/docs/CHAPTER_REPORT_HAN_07.md · theory/books/HAN/units/ch07_units.csv (87 đơn vị) · logs/quality.json · theory/logs/registry_validation_ch07.json

