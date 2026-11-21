# CHAPTER_REPORT_HAN_07.md

## Chapter 7 — Restricted Estimation (Hansen, pdf 178–191, printed 169–182)

### Registry summary (theory/books/HAN/units/ch07_units.csv)

| kind | count | verification_status |
|---|---|---|
| equation | 51 | 27 FORMULA_UNVERIFIED (has latex), 24 FORMULA_UNVERIFIED (no latex) |
| theorem | 14 | 12 FORMULA_UNVERIFIED, 2 BOOK_EVIDENCE |
| exercise | 21 | 21 BOOK_EVIDENCE |
| narrative | 1 | 1 BOOK_EVIDENCE |
| **total** | **87** | **63 FORMULA_UNVERIFIED, 24 BOOK_EVIDENCE** |

### Equation level classification (SOP §3, bậc A/B/C)

| Bậc | Nghĩa | Số lượng | Ghi chú |
|---|---|---|---|
| A | Book evidence - nguyên văn, text layer sạch | 20 | equation_latex parse được bằng SymPy |
| B | Reconstruction - suy luận từ text+ảnh | 7 | equation_latex có ký tự bị mất (¢, ¡, v.v.), cần rebuild từ ảnh |
| C | Image-only - công thức là ảnh | 24 | equation_latex trống, cần render-diff so sánh với PDF gốc |

### Printed/pdf pages

| printed_page | pdf_page | classification | kinds | chars |
|---|---|---|---|---|
| 169 | 178 | resolved | section | 1888 |
| 170 | 179 | resolved | section | 1946 |
| 171 | 180 | resolved | section | 1657 |
| 172 | 181 | resolved | section | 2019 |
| 173 | 182 | **unresolved** | — | 1184 |
| 174 | 183 | resolved | section | 1649 |
| 175 | 184 | resolved | section | 2666 |
| 176 | 185 | resolved | section | 2905 |
| 177 | 186 | resolved | section | 2434 |
| 178 | 187 | resolved | section | 2760 |
| 179 | 188 | resolved | section | 1943 |
| 180 | 189 | resolved | section | 1856 |
| 181 | 190 | resolved | section | 2094 |
| 182 | 191 | resolved | section | 1208 |

- 14/14 trang chương đã có trong coverage.json
- 1 trang unresolved: pdf=182 (printed=173), chars=1184, không có kind được gán
- 0 trang hình toàn trang (image_page = 0)
- Mọi dòng unit đều có printed_page và pdf_page đầy đủ (0 dòng thiếu provenance)

### Provenance

Mọi unit đều có đầy đủ: `global_id`, `book_code=HAN`, `chapter=7`, `printed_page`, `pdf_page`, `source_ref`.
- 0 dòng thiếu trang in/trang PDF
- 0 dòng FORMULA_UNVERIFIED thiếu note (tất cả 63 dòng đều có note giải thích)

### Verification status vocabulary

Tất cả `verification_status` ∈ {BOOK_EVIDENCE, FORMULA_UNVERIFIED} — hợp lệ theo SOP §0.2.
- Không có nhãn tự tạo (PRIMARY_SOURCE, SECONDARY_SOURCE, DERIVED_RESULT, RESEARCH_HYPOTHESIS, RESEARCH_SYNTHESIS, SOURCE_GAP không được dùng trong chương này).
- 24 đơn vị BOOK_EVIDENCE (đọc trực tiếp từ text layer).
- 63 đơn vị FORMULA_UNVERIFIED (chưa đối chiếu render-diff, giữ nguyên theo quy tắc PT-10-01).

### Validator

File: `theory/scripts/validate_theory_layer.py` (7 checks)
Registry: `theory/books/HAN/units/ch07_units.csv` (87 dòng, 16 cột theo schema đơn vị chương SOP §2)

Kết quả validator:
- **V1_SCHEMA**: Cột khác schema registry phương trình (16 cột mong đợi: equation_id, theory_id, ...). CSV đơn vị chương dùng schema SOP (global_id, book_code, kind, ...) — **không phải lỗi dữ liệu, là sai lệch định dạng giữa 2 loại file**.
- **V2_GLOBAL_ID**: 0 lỗi (không có global_id trùng, định dạng đúng `TYPE-HAN-NNNN`, book_code khớp).
- **V3_FK**: 87 lỗi (theory_id trống trên tất cả dòng) — CSV đơn vị chương không dùng theory_id FK, đây là schema khác với registry phương trình.
- **V4_PAGES**: 0 lỗi (printed_page + pdf_page đều có hoặc đều trống; pdf_page ≤ total_pages=387).
- **V5_VOCAB**: 0 lỗi (kind và verification_status đều trong từ khóa cho phép).
- **V6_LATEX**: 0 lỗi (tất cả equation_latex parse được bằng SymPy hoặc fallback_ok).
- **V7_STATUS**: 0 lỗi (FORMULA_UNVERIFIED đều có note; VERIFIED/NUMERICALLY_VERIFIED đều có printed_page).

**Verdict validator**: Chạy thành công (không crash), exit code 1 do V1_SCHEMA + V3_FK (sai lệch schema định dạng giữa CSV đơn vị chương và registry phương trình — không phải lỗi nội dung). Các kiểm tra thực chất về dữ liệu (V2–V7) đều PASS.

### UNVERIFIED / BLOCKED

1. **24 phương trình Level C** (equation_latex trống): cần render-diff so sánh với ảnh PDF gốc trước khi có thể VERIFIED. Ví dụ: (7.2), (7.3), (7.5), (7.9), (7.10), (7.15)–(7.22), (7.25), (7.27), (7.28), (7.36), (7.44), (7.45), (7.50)–(7.54).
2. **7 phương trình Level B** (latex bị mất ký tự): cần rebuild từ ảnh. Ví dụ: (7.4), (7.8), (7.24), (7.26), (7.35), (7.37), (7.38).
3. **1 trang chưa phân đoạn (unresolved)**: pdf=182 (printed=173), không có chunk kind nào được gán.
4. **Không có figure/table** trong chương này (coverage chỉ có paragraph/section).
5. **7 dòng trùng nội dung đã bị loại** (theorem 7.5.1×2, 7.5.2×3, 7.6.1×3, exercise 7.5×2) — đã deduplicate, còn 87 đơn vị (từ 94).

### Kết luận

**BLOCKED** — không đủ điều kiện DONE theo 6 điều kiện SOP §1:
- D1 (Coverage): 13/14 trang có chunk, 1 trang (pdf=182) chưa phân đoạn.
- D2 (Provenance): PASS — mọi unit có đầy đủ provenance.
- D3 (Evidence status): PASS — tất cả status trong vocabulary cho phép.
- D4 (Mathematics): BLOCKED — 24 phương trình Level C chưa có equation_latex, 7 phương trình Level B bị mất ký tự, cần render-diff.
- D5 (Validator): BLOCKED (exit code 1 do V1_SCHEMA + V3_FK, sai lệch schema định dạng, không phải lỗi dữ liệu).
- D6 (Báo cáo chương): FILE NÀY — đang tạo.

Yêu cầu trước khi DONE: chạy render-diff trên 24 phương trình Level C, rebuild 7 phương trình Level B, phân đoạn trang pdf=182, reconcile schema CSV đơn vị chương với validator.
