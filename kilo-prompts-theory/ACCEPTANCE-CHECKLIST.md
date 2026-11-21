# ACCEPTANCE CHECKLIST — LUẬN VĂN IFWST / CÁT TRUỒI

> Checklist nghiệm thu tổng hợp. Đối chiếu cuối cùng, sau khi chạy hết bộ prompt.
> Mỗi mục phải có **bằng chứng quan sát được** (lệnh đã chạy + output, hoặc số đo).

---

## A. Khoảng trắng tri thức (B2–B7)

| # | Mục | Đạt khi | Bằng chứng |
|---|---|---|---|
| A1 | 4 cuốn đã ingest | `books.yaml` có 4 cuốn, mỗi cuốn `total_pages` đo bằng script + `sha256` | đọc file |
| A2 | Không trang nào mất | PIN 787/787 · ROM 738/738 · HAN/MAD khớp manifest | `coverage.json` |
| A3 | Mâu thuẫn PIN đã giải thích | `books.yaml` `notes` nêu nguyên nhân 787 vs 761 | đọc file |
| A4 | Chunk có cấu trúc | mọi chunk có `book_code`, `pdf_page`, `kind`, `heading_path` | script kiểm |
| A5 | FTS5 truy vấn được | truy vấn trả kết quả đúng, nối được chunk ↔ registry | output truy vấn |
| A6 | SOP định nghĩa "xong" | 6 điều kiện DONE · 10 loại `kind` · bậc A/B/C · render-diff | đọc `EXTRACTION_SOP.md` |
| A7 | Validator mạnh | 7 kiểm tra · exit ≠ 0 khi lỗi · **≥1 lỗi thật** được bắt | output validator |
| A8 | 4 cuốn trích hết | 100% chương, có `CHAPTER_REPORT_*` cho mọi chương | đếm file |
| A9 | `global_id` duy nhất | 0 trùng toàn hệ thống | validator |
| A10 | Gộp đủ | equation gộp = 4 cuốn + 57 (MICRO) + 29 (MACRO) | đếm dòng |
| A11 | Cross-book index | ≥5 khái niệm dùng chung, có cột đối chiếu cơ chế | đọc file |
| A12 | Coverage audit | % phủ chương 100% hoặc phần thiếu đã giải thích · 7 bất biến đạt | đọc `COVERAGE_REPORT.md` |
| A13 | Trung thực bằng chứng | `FORMULA_UNVERIFIED` được giữ, không nâng vô lý | đối chiếu registry |

## B. Tổng quan tài liệu (B8)

| # | Mục | Đạt khi | Bằng chứng |
|---|---|---|---|
| B1 | Ma trận không rỗng | `literature_matrix.csv` ≥15 dòng, header giữ nguyên | đếm dòng |
| B2 | Nguồn kiểm chứng được | mọi dòng có DOI/URL truy cập được + `access_date` | output kiểm tra |
| B3 | Phủ 7 nhánh A–G | `search_log.csv` ghi đủ truy vấn | đọc file |
| B4 | Đọc đúng mức | `full_text` chỉ khi đọc thật toàn văn | rà từng dòng |
| B5 | Luna & Zanforlin (2025) | đã đọc toàn văn, có đánh giá phản bác | trích dẫn + trang |
| B6 | `critical_review.md` | có phần đánh giá phản bác | đọc file |
| B7 | `research_gap.md` | có 4 mục; phân biệt khoảng trống thật vs chưa đọc | đọc file |

## C. Lý thuyết & mô hình (B9)

| # | Mục | Đạt khi | Bằng chứng |
|---|---|---|---|
| C1 | Khái niệm gắn nguồn | mọi khái niệm có `global_id` **thật** hoặc nhãn `RESEARCH_SYNTHESIS` | script kiểm |
| C2 | Phương trình gắn nguồn | mọi phương trình có `source_global_id` hoặc `ORIGINAL` | rà từng phương trình |
| C3 | Truy được tới registry | mọi `global_id` tồn tại trong `theory/registry/` | script |
| C4 | Không tự xác nhận | không phương trình nào lên `FORMULA_VERIFIED` khi chưa đối chiếu | đối chiếu |
| C5 | Giới hạn mô hình | có 3 phần: không mô tả được gì · chưa kiểm định được gì · điều kiện phản bác | đọc file |
| C6 | Khớp ràng buộc thống kê | đặc tả khớp `feasibility_probe.md` | đối chiếu |

## D. Dữ liệu (B10)

| # | Mục | Đạt khi | Bằng chứng |
|---|---|---|---|
| D1 | Tầng truy vết | `source_registry.csv`, `variable_dictionary.csv`, `formula_registry.csv`, `data_inventory.csv` | đọc file |
| D2 | Cầu nối `theory/` | `variable_dictionary.csv` có `global_id` tồn tại thật | script |
| D3 | D1 — nguồn thật | có `bis_*`/`imf_ifs` thật **hoặc** bản `_PROXY` ghi nhãn đầy đủ | đọc `data/raw/` |
| D4 | D2 — `credit_gap` | HP filter λ=400.000 + bảng nhạy cảm λ | output script |
| D5 | D3/D4/D5 — 3 biến | `sandpile_load`, `network_density`, `regime` có std>0 và khác nhau giữa các nước | output thống kê |
| D6 | D6 — tần suất | khớp đặc tả (quý) hoặc đã ghi điều chỉnh | đếm |
| D7 | D7 — chất lượng | `data_quality_report.md` có construct validity + độ phủ + cảnh báo biến hằng số | đọc file |
| D8 | D8 — dọn code | còn đúng 1 script derived; deterministic | `ls` + hash |
| D9 | `code/08`–`code/12` | tồn tại, chạy được | output `--help` |
| D10 | Không biến proxy không nhãn | mọi biến proxy có nhãn trong dictionary | rà |

## E. Thực nghiệm (B11)

| # | Mục | Đạt khi | Bằng chứng |
|---|---|---|---|
| E1 | `code/13`–`code/16` | tồn tại, chạy end-to-end không lỗi | output |
| E2 | Deterministic | chạy 2 lần → hash giống | hash |
| E3 | EPV | đã tính; cảnh báo nếu <10 | đọc log |
| E4 | H1–H5 | mỗi giả thuyết có cách kiểm định, p, CI, kết luận trung thực | bảng kết quả |
| E5 | Độ bền | 6 kiểm tra §2.5 của prompt 11 đã chạy | output |
| E6 | Trái kỳ vọng | có mục phân tích riêng | đọc log |
| E7 | Truy vết số liệu | mọi bảng/biểu đồ có nguồn (script + file + tham số) | đọc bảng |
| E8 | Lookahead | đã kiểm không rò rỉ thông tin tương lai | mô tả + kết quả |

## F. Luận văn & kiểm định cuối (B12)

| # | Mục | Đạt khi | Bằng chứng |
|---|---|---|---|
| F1 | Đủ chương | 11 file trong `09_thesis/` | đọc thư mục |
| F2 | Claim → bằng chứng | mọi claim quan trọng có dòng bằng chứng | đọc bảng |
| F3 | Không vượt bằng chứng | 0 claim vượt | rà |
| F4 | Trích dẫn 2 chiều | 0 lệch | output script |
| F5 | Số liệu khớp | 100% | output script |
| F6 | Mã tái lập | hash giống | output |
| F7 | Nhất quán | thuật ngữ, ký hiệu, đánh số bảng/hình | rà |
| F8 | Đối chiếu `theory/` | 100% trích dẫn sách khớp registry | output script |
| F9 | Hạn chế được nêu | proxy / thiếu nguồn / EPV thấp đều nêu rõ | đọc `07_discussion.md` |
| F10 | References | chỉ nguồn đã đọc, URL đã kiểm | output |
| F11 | Thuật ngữ | có bảng thuật ngữ | đọc file |
| F12 | Trạng thái repo | `PROJECT_STATUS.md` + `MEMORY.md` + `task_backlog.md` khớp nhau | đọc cả 3 |

---

## G. Bất biến toàn hệ thống (kiểm ở mọi cổng)

| # | Bất biến | Kiểm bằng |
|---|---|---|
| G1 | `global_id` duy nhất toàn hệ thống | validator |
| G2 | `book_code` ∈ {HAN, ROM, PIN, MAD} | validator |
| G3 | `printed_page` + `pdf_page` cùng có hoặc cùng rỗng | validator |
| G4 | `pdf_page` ≤ `total_pages` của cuốn đó | validator |
| G5 | `verification_status` ∈ tập nhãn hợp đồng | validator |
| G6 | `equation_latex` parse được bằng SymPy | validator |
| G7 | `kind` ∈ 10 loại SOP | validator |
| G8 | Validator exit code = 0 trên registry cuối cùng | chạy validator |
| G9 | Script deterministic (chạy 2 lần → hash giống) | hash |
| G10 | Không sửa `research/`, `data/book/`, `tasks/` | `git status` |

---

## H. Trạng thái tổng kết

| Giai đoạn | Trạng thái | Ngày | Bằng chứng |
|---|---|---|---|
| GĐ0 — Kiểm kê | ✅ | 2026-10-17 | `PROJECT_STATUS.md` |
| GĐ1 — Tổng quan tài liệu | ⬜ | | `01_literature/literature_matrix.csv` |
| GĐ2 — Khung lý thuyết | ⬜ | | `02_conceptual_framework/` |
| GĐ3 — Đặc tả mô hình | ⬜ | | `03_model_specification/` |
| GĐ4 — Dữ liệu | ⬜ | | `data/` |
| GĐ5 — Thực nghiệm | ⬜ | | `output/` |
| GĐ6 — Luận văn | ⬜ | | `09_thesis/` |
| GĐ7 — Kiểm định cuối | ⬜ | | `output/final_audit.md` |
