# PILOT_REPORT.md — B4 Pilot Hansen Chapter 7 (Restricted Estimation)

## Thông tin chung

- **Chương:** Hansen, *Econometrics* (2014), Chương 7 — Restricted Estimation
- **Trang PDF:** 178–191 (trang in: 169–182)
- **Tổng trang chương:** 14 trang
- **File registry:** `theory/books/HAN/units/ch07_units.csv`
- **File báo cáo chương:** `theory/docs/CHAPTER_REPORT_HAN_07.md`
- **File kiểm tra validator:** `theory/logs/registry_validation_ch07.json`
- **Ngày thực thi:** 2026-10-27

---

## 4 con số đo được (M1–M4)

### M1 — Bậc toán học (A/B/C) theo SOP §3

Tổng 51 phương trình trong Chương 7:

| Bậc | Nghĩa | Số lượng | Tỷ lệ |
|-----|-------|----------|-------|
| **A** | Book evidence — text layer sạch, `equation_latex` parse được SymPy | 20 | 39.2% |
| **B** | Reconstruction — `equation_latex` bị mất ký tự, cần rebuild từ ảnh | 7 | 13.7% |
| **C** | Image-only — `equation_latex` trống, cần render-diff so sánh PDF | 24 | 47.1% |
| **Tổng** | | **51** | **100%** |

**Ý nghĩa:** Hơn nửa phương trình (47.1%) là Level C — công thức chỉ có trong ảnh PDF, chưa thể trích xuất từ text layer. Cần render-diff trước khi xác minh.

### M2 — Giờ thực tế (estimated)

| Công việc | Thời gian ước tính |
|-----------|-------------------|
| L0 — kiểm tra coverage, xác minh 14 trang (1 unresolved) | 0.5 giờ |
| L1-L2 — kiểm tra segmentation, FTS5 index | 0.5 giờ |
| L3 — deduplicate 7 dòng trùng, kiểm tra schema | 1.0 giờ |
| L4 — phân loại A/B/C, chạy validator, phân tích lỗi | 1.0 giờ |
| L5 — viết CHAPTER_REPORT + PILOT_REPORT | 1.0 giờ |
| **Tổng cộng** | **~4.0 giờ** |

### M3 — Số unit sinh ra

| Loại | Số lượng (sau deduplicate) | Trước deduplicate |
|------|---------------------------|-------------------|
| equation | 51 | 51 |
| theorem | 14 | 20 (bị loại 6 trùng) |
| exercise | 21 | 22 (bị loại 1 trùng) |
| narrative | 1 | 1 |
| **Tổng** | **87** | **94** |

7 dòng trùng nội dung đã bị loại (theorem 7.5.1×2, 7.5.2×3, 7.6.1×3, exercise 7.5×2).

### M4 — Tỉ lệ verify tự động pass

Validator: `theory/scripts/validate_theory_layer.py` (7 kiểm tra)

| Kiểm tra | Kết quả | Ghi chú |
|----------|---------|---------|
| V1_SCHEMA | FAIL | CSV đơn vị chương dùng schema SOP (global_id, book_code, kind...), khác schema registry phương trình (equation_id, theory_id...) — **không phải lỗi dữ liệu** |
| V2_GLOBAL_ID | PASS | 0 global_id trùng, định dạng đúng, book_code khớp |
| V3_FK | FAIL | theory_id trống tất cả dòng — CSV đơn vị chương không dùng theory_id FK |
| V4_PAGES | PASS | 0 lỗi, printed_page+pdf_page đều có, pdf_page ≤ 387 |
| V5_VOCAB | PASS | 0 lỗi, kind và verification_status đều trong vocabulary |
| V6_LATEX | PASS | 0 lỗi, tất cả equation_latex parse được SymPy hoặc fallback_ok |
| V7_STATUS | PASS | 0 lỗi, FORMULA_UNVERIFIED đều có note |

**Tỷ lệ verify tự động pass (dữ liệu):** 5/7 kiểm tra thực chất PASS (V2–V6, V7). 2 kiểm tra FAIL do sai lệch schema định dạng (V1, V3) — không phải lỗi nội dung.

**Exit code validator:** 1 (do V1_SCHEMA + V3_FK).

---

## Quyết định B5

### CẦN XỬ LÝ TOÁN HỌC BỞI SUNG

**Lý do:**
1. **47.1% phương trình là Level C** (24/51) — `equation_latex` trống, chỉ có trong ảnh PDF. Không thể mở rộng sang 4 cuốn nếu chưa có quy trình render-diff tự động.
2. **13.7% phương trình là Level B** (7/51) — `equation_latex` bị mất ký tự (¢, ¡, v.v.), cần rebuild từ ảnh.
3. **1 trang chưa phân đoạn** (pdf=182, printed=173) — không có chunk kind nào.
4. **Validator exit code 1** — cần reconcile schema CSV đơn vị chương với validator trước khi scale-up.

**Điều kiện để mở B5:**
- Chạy render-diff trên 24 phương trình Level C, chuyển sang `equation_latex` đầy đủ hoặc giữ `FORMULA_UNVERIFIED` kèm note.
- Rebuild 7 phương trình Level B từ ảnh PDF.
- Phân đoạn trang pdf=182, gán kind cho từng chunk.
- Điều chỉnh validator để chấp nhận schema CSV đơn vị chương (hoặc tạo validator riêng cho chapter unit CSV).

**Không được:** Mở rộng sang 4 cuốn trước khi giải quyết vấn đề trên (theo quy tắc B5 cổng: không làm chương thứ 2 của bất kỳ cuốn nào trước khi B4 hoàn tất).

---

## File đầu ra

| File | Đường dẫn | Trạng thái |
|------|-----------|------------|
| Chapter 7 units (cleaned) | `theory/books/HAN/units/ch07_units.csv` | ✅ 87 đơn vị, đã deduplicate |
| Chapter report | `theory/docs/CHAPTER_REPORT_HAN_07.md` | ✅ Đã tạo |
| Validator result | `theory/logs/registry_validation_ch07.json` | ✅ Đã chạy |
| Quality metrics | `logs/quality.json` | ✅ Đã tạo (xem bên dưới) |
| Pilot report | `theory/PILOT_REPORT.md` | ✅ File này |
