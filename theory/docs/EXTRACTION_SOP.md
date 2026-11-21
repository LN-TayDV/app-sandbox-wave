# EXTRACTION_SOP.md

## Mục đích
Biến "một chương coi như xong" thành quy tắc máy kiểm được, trước khi giao việc cho 4 worker trích xuất đồng thời 4 cuốn sách.

## 1. Sáu điều kiện DONE của một chương

| # | Điều kiện | Định nghĩa | Bằng chứng |
|---|---|---|---|
| D1 | Phủ (Coverage) | Mọi đơn vị nội dung thuộc phạm vi chương đã được đối chiếu với registry. Coverage được tính theo đơn vị nội dung, không phải theo số trang. Mọi mục bị bỏ qua phải ghi rõ lý do. | CHAPTER_REPORT_<BOOK>_<CH>.md (bảng đối chiếu + coverage %) |
| D2 | Trích dẫn (Provenance) | Mỗi dòng cần trích dẫn phải có book_code, printed_page, pdf_page, global_id. Phân biệt trang in và trang PDF; không điền số trang giả. | Mỗi unit có đầy đủ provenance |
| D3 | Nhãn bằng chứng (Evidence status) | verification_status ∈ tập nhãn §0.2: BOOK_EVIDENCE, PRIMARY_SOURCE, SECONDARY_SOURCE, DERIVED_RESULT, RESEARCH_HYPOTHESIS, RESEARCH_SYNTHESIS, UNVERIFIED, SOURCE_GAP. Với phương trình: FORMULA_VERIFIED, FORMULA_UNVERIFIED, NUMERICALLY_VERIFIED, ILLUSTRATIVE. Không tạo nhãn mới. | Mỗi unit có verification_status hợp lệ |
| D4 | Toán học (Mathematical verification) | Mọi phương trình phải có equation_latex parse được bằng parser phù hợp (SymPy). Trạng thái xác minh phải phản ánh đúng bằng chứng. formula_ref phải trỏ tới định nghĩa/đối tượng được tham chiếu hợp lệ. Parse thành công không đồng nghĩa công thức đúng. | equations.csv + validation LaTeX |
| D5 | Validator | theory/scripts/validate_theory_layer.py chạy thành công (exit code 0) trên registry của chương đó, không crash. | Kết quả validator |
| D6 | Báo cáo chương (Chapter report) | Có theory/docs/CHAPTER_REPORT_<BOOK>_<CH>.md theo mẫu. | File báo cáo tồn tại |

## 2. Bảng 10 loại kind + trường bắt buộc

| kind | Trường bắt buộc | Quy tắc | Provenance | Kiểm tra |
|---|---|---|---|---|
| concept | definition, meaning, usage | meaning bằng tiếng Việt | book_code, printed_page, pdf_page, global_id | Định nghĩa rõ ràng, trung thực |
| equation | equation_latex, symbols, verification_status | symbols có tên/định nghĩa/đơn vị | đầy đủ provenance | Parse LaTeX được; formula_ref hợp lệ nếu có |
| assumption | statement, scope, role | scope rõ điều kiện áp dụng | đầy đủ provenance | Rõ ràng |
| theorem | statement, premises, conclusion, proof_sketch | Tất cả bắt buộc hoặc ghi rõ | đầy đủ provenance | Phân biệt phát biểu vs chứng minh |
| caveat | statement, trigger, severity | Cụ thể | đầy đủ provenance | Có thể hành động |
| example | setup, result, numbers | Số tự tính gắn nhãn ILLUSTRATIVE | đầy đủ provenance | Ghi chú rõ |
| figure | caption, file, source_page | file là ảnh crop | đầy đủ provenance | Có ảnh đã xác minh |
| table | caption, data_file, source_page | Có data_file | đầy đủ provenance | Có dữ liệu |
| exercise | question, answer_available, answer | answer bắt buộc nếu CÓ | đầy đủ provenance | Trung thực |
| narrative | summary | Trung thực, không thêm ý tác giả | đầy đủ provenance | Trung thực |

## 3. Quy trình toán học ba bậc A/B/C

| Bậc | Nghĩa | Cách làm | Nhãn |
|---|---|---|---|
| A | Book evidence - nguyên văn | Copy từ text layer | BOOK_EVIDENCE / FORMULA_VERIFIED |
| B | Reconstruction - suy luận | Suy từ text+ảnh, ghi note rõ | FORMULA_UNVERIFIED + note |
| C | Image-only | symbolic → numeric → render → so sánh ảnh trang gốc (scientific/registry.py) | NUMERICALLY_VERIFIED hoặc FORMULA_UNVERIFIED |

Quy tắc: Bậc C bắt buộc đi qua đủ bước. Không khớp → FORMULA_UNVERIFIED. Không tự sửa công thức chỉ để khớp.

## 4. Mẫu Chapter Report
Tạo theory/docs/CHAPTER_REPORT_<BOOK>_<CH>.md với: thông tin chung, phạm vi, đơn vị nội dung, coverage, phương trình/toán học, kết quả validator, lỗi/ngoại lệ, chưa xác minh, kết luận (DONE/BLOCKED).
