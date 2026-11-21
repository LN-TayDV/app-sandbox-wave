# START HERE — IFWST / CÁT TRUỒI

> **Mở file này khi bắt đầu mỗi phiên làm việc.**
> Ở đây bạn biết: đang ở bước nào, đọc gì tiếp theo, làm gì trong phiên này.

- **Dự án:** International Financial Wave–Sandpile Theory (IFWST) / Cát Truồi
- **Thư mục gốc:** `C:\Users\PC\Documents\AI_project\sandbox-financial`
- **Workflow chuẩn:** [`WORKFLOW.md`](WORKFLOW.md) — 13 bước, mỗi bước có cổng đạt
- **Ngôn ngữ:** Tiếng Việt
- **Cập nhật:** 2026-10-22

---

## 1. Bạn đang ở đâu?

Xem bảng trạng thái trong [`WORKFLOW.md` §0](WORKFLOW.md#0-bảng-trạng-thái).

**Bước hiện tại: BƯỚC 0 — Đồng bộ repo.**
Việc cần làm hôm nay: xem [`WORKFLOW.md` → BƯỚC 0](WORKFLOW.md#bước-0--đồng-bộ-repo) (45 phút).

---

## 2. Bản đồ: file nào trả lời câu hỏi nào

Tất cả đường dẫn tương đối so với `C:\Users\PC\Documents\AI_project\sandbox-financial\`.

### Tài liệu gốc & quản lý

| Câu hỏi | Mở file | Tình trạng |
|---|---|---|
| Mệnh lệnh gốc của dự án? | `tasks/init-task.md` | ✅ 1102 dòng — **mọi cụm "PHẦN 6/14/19" trong các file đều trỏ về đây** |
| Ý tưởng gốc Cát Truồi? | `ideas/master-idea.md` | ✅ 269 dòng — 12 phần, 3 mô hình, H1–H5, sản phẩm A–J |
| Ý tưởng econometrics (mới)? | `ideas/ECONOMETRICS-DRIVEN.md` | ⬜ **rỗng — cần viết** |
| Quy trình thực thi tổng thể? | `00_project_management/WORKFLOW.md` | ✅ **file này** |
| Dự án đang ở đâu? | `PROJECT_STATUS.md` | ⚠️ cần sửa ở B0 |
| Câu hỏi nghiên cứu + giả thuyết? | `RESEARCH_MANIFEST.md` | ✅ |
| Câu hỏi con (10 câu)? | `00_project_management/research_questions.md` | ✅ |
| Phạm vi / ngoài phạm vi? | `00_project_management/scope_and_boundaries.md` | ✅ — luận văn 6.000–10.000 từ |
| Quy trình 8 giai đoạn học thuật? | `00_project_management/methodology.md` | ✅ |
| Đã quyết định gì? | `00_project_management/decision_log.md` | ⚠️ mới 5 dòng — cần cập nhật ở B0 |
| Còn việc gì? | `00_project_management/task_backlog.md` | ⚠️ **mọi checkbox đều trống** — sửa ở B0 |
| Xong chưa (16 tiêu chí)? | `00_project_management/completion_checklist.md` | ✅ |
| Đã chạy gì? | `logs/execution_log.md` | ⚠️ dừng ở 2026-10-17, 4 dòng — sửa ở B0 |

### Nội dung học thuật đã có

| Câu hỏi | Mở file | Tình trạng |
|---|---|---|
| Cơ chế Cát Truồi? | `02_conceptual_framework/IFWST_Conceptual_Framework.md` | ✅ kiến trúc 3 lớp: Wave + Network + Sandpile |
| Mô hình, tham số, cách ước lượng? | `03_model_specification/IFWST_Model_Specification.md` | ✅ — có lỗi typo dòng 232 (`Stata: s пространственный`) |
| Kế hoạch dữ liệu? | `04_data/IFWST_Data_Collection_Strategy.md` | ✅ |
| Tài liệu nào đã đọc? | `01_literature/Literature_Sources_Compilation.md` | ✅ 193 dòng, ~7 nguồn |
| Ma trận tài liệu? | `01_literature/literature_matrix.csv` | ⬜ **RỖNG** — dựng lại ở B8 |
| Khoảng trống nghiên cứu? | `01_literature/research_gap.md` | ⬜ **CHƯA CÓ** — tạo ở B8 |
| Nhật ký tìm kiếm? | `01_literature/search_log.csv` | ⚠️ |

### Dữ liệu & mã

| Câu hỏi | Mở file | Tình trạng |
|---|---|---|
| Dữ liệu thô hiện có? | `data/raw/` | ⚠️ **chỉ có World Bank** — thiếu `bis_*.csv`, `imf_ifs.csv` |
| Panel hiện tại? | `data/processed/ifwst_panel.csv` | ⚠️ 714 dòng, **tần suất năm**, biến là proxy (xem B10) |
| Chất lượng dữ liệu? | `output/data_quality_report.md` | ⚠️ nói "ready" nhưng không kiểm validness |
| Mã đã chạy? | `code/01`–`code/07` | ✅ 7 script; `code/08`–`code/16` **chưa tồn tại** |
| Pipeline mã GĐ5? | `WORKFLOW.md` (gốc) | ⚠️ liệt kê 18 bước nhưng chỉ 01–07 tồn tại |
| Biểu đồ kết quả? | `output/panel_summary.csv` | ✅ |

### Trích xuất sách & công cụ

| Câu hỏi | Mở file | Tình trạng |
|---|---|---|
| Quy trình trích xuất sách? | `skills/academic-book-research-and-learning-engineering/SKILL.md` | ✅ 257 dòng — dùng cho cả 4 cuốn |
| Skill khác? | `skills/academic-book-research/SKILL.md`, `skills/macro-to-web/SKILL.md`, `skills/academic-learning-experience/SKILL.md` | ✅ |
| Mẫu prompt chạy session? | `kilo-prompts/00-shared-contract.md` → `09-recovery-guide.md` | ✅ 10 prompt — **hard-code MACRO/MICRO**, cần bản riêng cho tầng `theory/` |
| Script trích xuất PDF có sẵn? | `research/advanced-macroeconomics-fourth-edition/scripts/{inspect_source,extract_pdf}.py` | ✅ tái dùng được |
| Lớp khoa học 4 lớp (SymPy)? | `research/advanced-macroeconomics-fourth-edition/scientific/registry.py` | ✅ 374 dòng — dùng lại, **không viết mới** |
| Validator registry? | `research/advanced-macroeconomics-fourth-edition/scripts/validate_registries.py` | ⚠️ chỉ đếm dòng — nâng ở B3 |
| 4 PDF nguồn? | `data/book/` | ✅ `b81821bd…pdf` = Romer · `econometrics-bruce-hansen-2014.pdf` = Hansen · `Robert S Pindyck…pdf` = Pindyck · `international-financial-management-11th-edition-by-jeff-madura.pdf` = Madura (**chưa ai đụng**) |

---

## 3. Những điều đang sai trong repo (biết để không tin nhầm)

| Vấn đề | Chi tiết |
|---|---|
| Trạng thái tự mâu thuẫn | `PROJECT_STATUS.md` = "GĐ0" · `MEMORY.md` = "GĐ1 ✅" · `task_backlog.md` = mọi checkbox trống · `execution_log.md` = 4 dòng |
| `literature_matrix.csv` rỗng | dù `MEMORY.md` ghi "literature phase complete" |
| Cấu trúc thư mục lệch | `README.md` khai `02_theory/ 03_model/ 05_code/ 06_experiments/ 07_case_studies/ 08_results/ 09_thesis/ 10_quality_assurance/` — thực tế là `02_conceptual_framework/ 03_model_specification/ 04_data/ code/ data/ output/ logs/` |
| `WORKFLOW.md` (gốc) vượt quá thực tế | liệt kê 18 bước, `code/` chỉ có `01`–`07` |
| Mâu thuẫn số trang PIN | `extract_pdf.json` = 787 trang, `coverage.json` = 761 trang → đối chiếu ở B2 |
| 14 trang "short" ở PIN | trang 90, 170, 180, 210, 284, 368, 370, 454, 544, 574, 610, 646, 676, 784 — nhiều khả năng là **trang hình toàn trang**, cần xử lý bằng ảnh |

---

## 4. Quy tắc bất di bất dịch (rút gọn)

1. Khẳng định trạng thái **kèm đường dẫn file**; không "đã xong" mà không có bằng chứng.
2. **Không nâng trạng thái để đẹp** — `PROVISIONAL` / `FORMULA_UNVERIFIED` hơn `DONE` bịa.
3. **Cổng là số đo.** Không có output lệnh → không đạt cổng.
4. **Trong B1–B7: không tải dữ liệu thật, không viết luận văn.** Nhu cầu phát sinh → `theory/GAP_REQUESTS.md`.
5. **Registry là nguồn duy nhất** cho mọi phương trình trích dẫn.
6. **Không sửa PDF gốc**; **không sửa `research/micro*` hay `research/advanced*`** — chỉ đọc.
7. **Sửa generator, không vá file sinh ra.**
8. **Không xoá lịch sử nghiên cứu.** Muốn bỏ bản cũ → `code/_superseded/` kèm lý do.
9. **Mỗi phiên:** dán mẫu báo cáo + tick bảng §0 của `WORKFLOW.md`.
10. **Bị gián đoạn:** đọc file này → bảng §0 → tiếp tục đúng chỗ.

---

## 5. Sẽ tạo ở các bước sau (để không tưởng là thiếu sót)

| Bước | Tạo gì |
|---|---|
| B0 | `00_project_management/START_HERE.md` (file này) |
| B1 | `04_data/feasibility_probe.md` |
| B2 | `theory/registry/books.yaml` · `theory/scripts/{ingest_book,segment_book,index_knowledge}.py` · `theory/books/<MÃ>/` · `theory/index/knowledge.db` |
| B3 | `theory/EXTRACTION_SOP.md` · `theory/scripts/validate_theory_layer.py` |
| B4 | `theory/PILOT_REPORT.md` · `theory/books/HAN/units/` |
| B5 | `theory/books/<MÃ>/units/*.csv` · `theory/books/<MÃ>/figures/` · `theory/docs/KILO_STATUS.md` |
| B6 | `theory/registry/*.csv` · `theory/relations.csv` · `theory/notation.csv` |
| B7 | `theory/AUDIT.md` |
| B8 | `01_literature/literature_matrix.csv` · `critical_review.md` · `research_gap.md` |
| B9 | cập nhật `02_conceptual_framework/` · `03_model_specification/` |
| B10 | `data/{validated,interim}/` · `data/{source_registry,variable_dictionary,formula_registry,model_registry}.csv` |
| B11 | `code/08`–`code/16` · `output/IFWST_Final_Report.md` |
| B12 | `09_thesis/chapters/` · `09_thesis/build.py` · `09_thesis/claim_evidence_matrix.csv` |
