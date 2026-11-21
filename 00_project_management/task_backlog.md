# Task Backlog — IFWST / Cát Truồi

> Nguyên tắc: chỉ tick `[x]` khi **có bằng chứng đường dẫn**. Mục làm dở → `[~]`. Chưa làm → `[ ]`.
> Bổ sung: workflow chuẩn 13 bước ở [`WORKFLOW.md`](WORKFLOW.md).

---

## Giai đoạn 0 — Kiểm kê dự án ✅

- [x] Kiểm tra quyền truy cập và trạng thái thư mục `sandbox-financial` — 2026-10-17
- [x] Bảo toàn các tài sản hiện có (`tasks/init-task.md`, 1102 dòng)
- [x] Thiết lập cấu trúc nghiên cứu phù hợp — `00_project_management/`, `01_literature/` … `09_thesis/`
- [x] Tạo `README.md`, `PROJECT_STATUS.md`, `RESEARCH_MANIFEST.md`
- [x] Tạo `00_project_management/*` (scope_and_boundaries, methodology, research_questions, decision_log, task_backlog, completion_checklist)
- [x] Xác định công cụ và quyền truy cập — Python, PyMuPDF (`fitz`), SymPy, SQLite FTS5, git; kết nối internet OK
- [x] **B0 — Đồng bộ repo**: viết lại `PROJECT_STATUS.md`, `MEMORY.md`, `task_backlog.md`, `logs/execution_log.md` theo bằng chứng — 2026-10-22

## Giai đoạn 1 — Tổng quan tài liệu ⚠️

- [x] Tìm kiếm tài liệu về SOC, sandpile, financial contagion, international banking, network effects, early-warning — `01_literature/search_log.csv` (2026-10-17 18:20)
- [x] Tải 2 full-text + 2 tóm tắt — `01_literature/sources/` (19:13)
- [x] Xác minh nguồn (DOI / trang nhà xuất bản) — `01_literature/Literature_Sources_Compilation.md` (19:17)
- [~] Đọc và phân tích tài liệu — ~7 nguồn, **chưa đọc toàn văn Luna–Zanforlin (2025)** (bằng chứng phản bác mạnh nhất)
- [ ] **Xây dựng `literature_matrix.csv`** — file hiện RỖNG (309 B = chỉ header) → chặn tuyên bố đóng góp
- [ ] Viết `critical_review.md` — chưa có
- [ ] Viết `research_gap.md` — chưa có
- [ ] Khảo sát đủ 7 nhánh A–G trong `tasks/search.md` (hiện phủ khoảng 1/3)

## Giai đoạn 2 — Khung lý thuyết ✅

- [x] Chốt câu hỏi nghiên cứu — `00_project_management/research_questions.md`
- [x] Xác định phạm vi — `00_project_management/scope_and_boundaries.md`
- [x] Định nghĩa biến và thuật ngữ — `02_conceptual_framework/IFWST_Conceptual_Framework.md` (14.020 B, 19:51)
- [x] Xây dựng sơ đồ cơ chế — kiến trúc 3 lớp Wave + Network + Sandpile
- [x] Đề xuất giả thuyết H1–H5 + giải thích cạnh tranh

## Giai đoạn 3 — Đặc tả mô hình ✅

- [x] Xây dựng phương trình — `03_model_specification/IFWST_Model_Specification.md` (8.849 B, 19:58)
- [x] Định nghĩa tham số
- [x] Chọn mô hình tối thiểu — M1/M2/M3
- [x] Xác định điều kiện ước lượng — SVD, Sargan, backtest
- [x] Kiểm tra khả năng nhận dạng
- [ ] Sửa typo dòng 232 (`Stata: s пространственный`) — sửa ở B10 cùng batch

## Giai đoạn 4 — Dữ liệu ⚠️

- [x] Kiểm tra khả năng truy cập nguồn — **chỉ World Bank truy cập được** (23 file `wb_*.csv` + `crisis_dates*.csv`, 2026-10-17 20:37–20:47)
- [x] Thu thập dữ liệu (partial) — `code/01`–`code/04` chạy; **BIS/IMF thất bại** (`code/01_download_bis.py:52-55` fallback về World Bank)
- [~] Làm sạch và chuẩn hóa — `code/05_derived*.py` (**4 bản trùng**), `code/06_panel.py`, `code/07_quality.py`; panel 714 dòng, 19 cột
- [~] Kiểm tra chất lượng — `output/data_quality_report.md` chỉ kiểm missing/range/outlier, **bỏ qua construct validity** (dòng 50-53)
- [ ] **Ghi nhận nguồn gốc**: `data_inventory.csv`, `data_dictionary.csv`, `source_registry.csv` — chưa có
- [ ] Bổ sung `bis_credit.csv`, `bis_crossborder.csv`, `imf_ifs.csv` (chặn GĐ4/5)
- [ ] Sửa 9 lỗi dữ liệu D1–D9 (xem `PROJECT_STATUS.md` §2)

## Giai đoạn 5 — Thực nghiệm ⬜

- [ ] Chạy mô hình cơ sở — **cần `code/08`–`code/16`**
- [ ] Chạy mô hình mở rộng
- [ ] Kiểm định giả thuyết H1–H5
- [ ] Kiểm tra độ bền
- [ ] Phân tích kết quả âm tính hoặc trái kỳ vọng

## Giai đoạn 6 — Viết luận văn ⬜

- [ ] Viết từng chương dựa trên bằng chứng — `09_thesis/` chưa tồn tại
- [ ] Đồng bộ thuật ngữ và ký hiệu
- [ ] Kiểm tra nguồn và các con số
- [ ] Hoàn thiện hình, bảng và phụ lục

## Giai đoạn 7 — Kiểm định cuối ⬜

- [ ] Kiểm tra trích dẫn
- [ ] Kiểm tra dữ liệu
- [ ] Kiểm tra mã
- [ ] Kiểm tra tính nhất quán
- [ ] Kiểm tra các tuyên bố khoa học
- [ ] Hoàn thiện bản cuối

---

# Phần B — Trích xuất tri thức 4 cuốn sách (B1–B7)

## B1 — Probe khả thi dữ liệu 🔄 (đang làm)

- [x] Probe sơ bộ 7 nguồn (2026-10-22) → `04_data/feasibility_probe.md` — **SƠ BỘ**: 3/7 chắc chắn dùng (ECB, World Bank, BIS catalog), 2/7 cần cứu, 2/7 cần nguồn thay thế
- [ ] BIS: dựng đúng key SDMX 15 đoạn → tải credit gap CSV thật (biến trung tâm)
- [ ] BIS: LBS cross-border (key đúng) + DSR (bypass `www.bis.org` 403)
- [ ] IMF: retry DataMapper có backoff + UA → xác nhận IFS
- [ ] FRED: thử lại, kiểm body (lần trước trả HTML "Site Maintenance")
- [ ] JST Macrohistory: xác nhận không truy cập được (DNS "Non-existent domain")
- [ ] Laeven–Valencia: tìm mirror + **kiểm nguồn gốc** của `data/raw/crisis_dates.csv` hiện có
- [ ] Chốt lõi dữ liệu + hệ quả công suất thống kê (EPV) + quyết định TIẾP TỤC / THU HẸP PHẠM VI
- [ ] Bộ prompt thực thi: `kilo-prompts-theory/` — **✅ đã tạo 2026-10-22** (13 prompt + EXECUTION-MATRIX + ACCEPTANCE-CHECKLIST + README)

## B2 — Dựng tầng `theory/` + pipeline L0/L1/L2 ⬜

- [ ] `theory/` skeleton: `theories/`, `equations/`, `assumptions/`, `caveats/`, `concepts/`, `figures/`, `tables/`, `exercises/`, `bibliography/`, `docs/`
- [ ] Copy + adapt `inspect_source.py`, `extract_pdf.py` từ `research/advanced-macroeconomics-fourth-edition/scripts/`
- [ ] Chạy L0 (PDF → text + metadata) cho **cả 4 cuốn**, kể cả `HAN` và `MAD` (chưa ai làm)
- [ ] Giải quyết mâu thuẫn trang PIN: `extract_pdf.json`=787 vs `coverage.json`=761; 14 trang "short" nội địa (90, 170, 180, 210, 284, 368, 370, 454, 544, 574, 610, 646, 676, 784) → xử lý bằng ảnh
- [ ] L1: chapter segmentation (dùng `chapter_ranges` của ROM làm mẫu) + FTS5 index
- [ ] L2: trích equation / assumption / caveat / concept / figure / table / exercise → registry CSV

## B3 — SOP + Validator ⬜

- [ ] `theory/docs/EXTRACTION_SOP.md` — quy tắc trích xuất + vocabulary bằng chứng (mượn `skills/academic-book-research-and-learning-engineering/SKILL.md`)
- [ ] Nâng `validate_registries.py` (hiện chỉ đếm dòng) thành 7 kiểm tra: schema · duplicate ID · FK `theory_id` · `printed_page`/`pdf_page` hợp lệ · status vocabulary · LaTeX parse được bằng SymPy · `book_code`+`global_id` unique
- [ ] Xác nhận 16 cột của `05_equation_registry.csv` và 19 cột của `04_theory_registry.csv` khớp giữa MACRO và MICRO

## B4 — Pilot Hansen Ch.7 ✅

- [x] Trích 1 chương thật (Hansen Ch.7 — Restricted Estimation) end-to-end — 87 đơn vị, đã deduplicate
- [x] Chạy `validate_theory_layer.py` verify — 5/7 kiểm tra dữ liệu PASS, 2 FAIL do schema chênh lệch (không phải lỗi dữ liệu)
- [x] Ước lượng thời gian 1 chương → ~4.0 giờ → định lịch B5 bị BLOCKED
- [x] Tạo `theory/PILOT_REPORT.md` + `theory/docs/CHAPTER_REPORT_HAN_07.md` + `logs/quality.json`

## B5 — Trích xuất hết 4 cuốn ⛔ BLOCKED

- [ ] CẦN XỬ LÝ TOÁN HỌC BỞI SUNG — render-diff 24 phương trình Level C, rebuild 7 Level B, phân đoạn trang pdf=182, reconcile validator schema
- [ ] `HAN` — Hansen, *Econometrics* (2014)
- [ ] `ROM` — Romer, *Advanced Macroeconomics* 4e (738 trang)
- [ ] `PIN` — Pindyck & Rubinfeld, *Microeconomics* Global Ed. (787 trang)
- [ ] `MAD` — Madura, *International Financial Management* 11e
- [ ] Mỗi worker: 1 cuốn / chia chương; registry `book_code` + `global_id` (`EQ-HAN-0001`)

## B6 — Union + cross-book + index ⬜

- [ ] Gộp 4 registry vào `theory/registry/` — giữ ID cũ, thêm `book_code`, `global_id`
- [ ] Cross-book index: khái niệm/cơ chế dùng chung (ví dụ "credit crunch" ở HAN + ROM + MAD)
- [ ] Tra cứu nhanh: SQLite FTS5 + `theory/docs/INDEX.md`

## B7 — Audit coverage toàn bộ ⬜

- [ ] Đối chiếu 4 bảng bìa của từng cuốn: mọi chương có mặt trong registry?
- [ ] Đếm equation/assumption/caveat/figure/table/exercise theo từng cuốn
- [ ] Đánh dấu `UNVERIFIED` / `SOURCE_GAP` — không tự xác nhận phương trình thiếu bằng chứng (giữ `PT-10-01 = FORMULA_UNVERIFIED`)
- [ ] `theory/docs/COVERAGE_REPORT.md` — bằng chứng cho cổng B7

---

## Hàng đợi B2–B7 cần đáp ứng

- [ ] `kilo-prompts-theory/` — bộ prompt riêng (bộ `kilo-prompts/` hiện hard-code MACRO/MICRO)
- [ ] `theory/docs/KILO_STATUS.md` — trạng thái resumable cho phiên sau
- [ ] `theory/GAP_REQUESTS.md` — nhu cầu phát sinh giữa pha
- [x] B4 redo pilot HAN Ch.13 (GMM) — 2026-10-23
