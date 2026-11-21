# EXECUTION MATRIX — LUẬN VĂN IFWST / CÁT TRUỒI

> Bảng điều khiển cho bộ prompt `kilo-prompts-theory/`. Đọc trước khi chạy bất kỳ prompt nào.

---

## 1. Ma trận dependency

| Prompt | Bước | Phụ thuộc | Cổng chặn (phải đạt trước khi sang) | Ước lượng |
|---|---|---|---|---|
| `00-shared-contract.md` | — | — | đọc trước mọi prompt | 10 phút |
| `01-data-feasibility-probe.md` | B1 | `00` | — | 1 ngày |
| `02-theory-pipeline.md` | B2 | `00`, **B1 ✅** | B1: ≥4/7 nguồn dùng được | 2 ngày |
| `03-sop-validator.md` | B3 | `00`, **B2 ✅** | B2: PIN 787/787 · ROM 738/738 · FTS5 truy vấn được | 1 ngày |
| `04-pilot-hansen.md` | B4 | `00`, **B3 ✅** | B3: validator bắt ≥1 lỗi thật | 1 ngày |
| `05-extract-book.md` | B5 | `00`, **B4 ✅** | B4: có đủ 4 con số M1–M4 + lệnh cho B5 | 3–10 ngày/cuốn |
| `06-union-crossbook.md` | B6 | **B5 ✅ (cả 4 cuốn)** | B5: 100% chương, validator xanh | 3 ngày |
| `07-coverage-audit.md` | B7 | **B6 ✅** | B6: đủ dòng, `global_id` duy nhất | 2 ngày |
| `08-literature-review.md` | B8 | **B7 ✅** | B7: ĐẠT CỔNG + báo cáo coverage | 1–2 tuần |
| `09-model-and-theory.md` | B9 | **B8 ✅** | B8: matrix không rỗng, `critical_review.md` + `research_gap.md` có | 2 tuần |
| `10-real-data.md` | B10 | **B9 ✅** | B9: mọi phương trình có `global_id` hoặc `ORIGINAL` | 2–3 tuần |
| `11-estimation.md` | B11 | **B10 ✅** | B10: đủ tầng truy vết + 9 lỗi D1–D9 xử lý | 2–3 tuần |
| `12-thesis-writing.md` | B12 | **B11 ✅** | B11: H1–H5 có kết quả + độ bền | 2–3 tuần |

## 2. Song song hóa — chỉ ở đúng chỗ

| Chặng | Được song song | Không được song song |
|---|---|---|
| B1–B4 | ❌ tuần tự tuyệt đối | mọi thứ |
| **B5** | ✅ **4 worker, 1 cuốn mỗi worker** (chia chương) | worker trên **cùng** một cuốn |
| B6–B12 | ❌ tuần tự tuyệt đối | mọi thứ |

> **Không xen kẽ pha kỹ thuật (B1–B7) với pha học thuật (B8–B12).**

## 3. Baseline đã đo (2026-10-22) — không cần đo lại

| Hạng mục | Số đo |
|---|---|
| PIN L0 | **787/787** trang, 0 failed, 18 short — nhưng `coverage.json` ghi **761** ⚠️ mâu thuẫn 26 trang |
| PIN trang short nội địa | 90, 170, 180, 210, 284, 368, 370, 454, 544, 574, 610, 646, 676, 784 |
| ROM L0 | **738/738** trang, 0 failed, 8 short (đều front matter); có `chapter_ranges` 12 chương |
| HAN L0 | ❌ chưa có |
| MAD L0 | ❌ chưa có |
| Registry MICRO | equation 16 cột / 57 dòng · theory 19 cột / 32 dòng |
| Registry MACRO | equation 16 cột / 29 dòng · theory 19 cột / 16 dòng |
| Panel hiện tại | 714 dòng × 19 cột · 21 nước · 1990–2023 · **tần suất năm** |
| `data/raw/` | 23 file (`wb_*` + `crisis_dates*`) — **thiếu** `bis_*.csv`, `imf_ifs.csv` |
| Code | `code/01`–`code/07` (4 bản `05_derived*.py` trùng) — **thiếu** `code/08`–`code/16` |
| Test MACRO | 34/34 browser smoke · 75/75 pytest · 21/21 node |
| Test MICRO | đã verify 2026-10-22 |

## 4. Cổng chặn chi tiết (điều kiện đo được)

| Cổng | Điều kiện | Lệnh kiểm chứng |
|---|---|---|
| G(B1) | `04_data/feasibility_probe.md` có 7 nguồn, mỗi dòng có status + Content-Type + kết luận | đọc file |
| G(B2) | `coverage.json` PIN = 787, ROM = 738; `knowledge.db` truy vấn được | đếm + truy vấn |
| G(B3) | validator exit ≠ 0 trên file lỗi; ≥1 lỗi thật trong registry hiện có | chạy validator |
| G(B4) | `PILOT_REPORT.md` có M1–M4 đo bằng lệnh | đọc file |
| G(B5) | mỗi cuốn: 100% chương + validator xanh + `CHAPTER_REPORT_*` | đếm + validator |
| G(B6) | đủ dòng (4 cuốn + 57 + 29) · `global_id` duy nhất · FTS nối chunk↔registry | đếm + truy vấn |
| G(B7) | % phủ chương 100% (hoặc phần thiếu đã giải thích) · 7 bất biến đạt | đọc `COVERAGE_REPORT.md` |
| G(B8) | `literature_matrix.csv` ≥15 dòng, header giữ nguyên; `critical_review.md` + `research_gap.md` có | đếm dòng |
| G(B9) | mọi `global_id` trong bảng ánh xạ tồn tại thật trong registry | script |
| G(B10) | 4 file truy vết có; 9 lỗi D1–D9 xử lý; `code/08`–`code/12` chạy được | đọc + chạy |
| G(B11) | `code/13`–`code/16` chạy end-to-end; H1–H5 có kết quả; 6 kiểm tra độ bền | output |
| G(B12) | 8 kiểm tra GĐ7 đạt; claim→bằng chứng không lệch | đọc `09_thesis/` |

## 5. Quy tắc ứng xử khi gặp vướng

| Tình huống | Hành động |
|---|---|
| Cổng trước chưa đạt | **DỪNG**, báo lại cổng, sửa nốt cổng trước. Đừng làm tiếp trên nền chưa vững. |
| Nguồn dữ liệu 403 / DNS fail | Ghi `BLOCKED` + **kiểm lại bằng retry có backoff và UA** (đã thấy IMF 200→403, FRED 200→000) |
| HTTP 200 nhưng body sai | Kiểm **Content-Type + dòng đầu body** (đã thấy FRED trả HTML "Site Maintenance") |
| Registry lệch schema | Dừng, sửa `theory/scripts/validate_theory_layer.py` trước — không vá tay dữ liệu |
| Không tìm thấy đường dẫn trong prompt | Tìm bằng `ls`/`grep`, ghi sai lệch vào báo cáo, dùng đường dẫn đúng tìm được |
| Cần sửa `research/` | `research/` chỉ đọc → copy sang `theory/` và sửa bản copy, ghi chú trong báo cáo |
| Hết giờ giữa chừng | Ghi trạng thái `PARTIAL` + chương đang dở. **Không** ghi "xong". |
| Cần quyết định học thuật ngoài phạm vi prompt | Ghi vào `theory/GAP_REQUESTS.md`, báo lại, **không** tự quyết |

## 6. Những thứ đã biết là **KHÔNG** làm lại

- ❌ Không chạy lại L0 cho PIN/ROM từ repo `research/` → copy script, chạy lại từ `data/book/`
- ❌ Không sửa file trong `research/`, `data/book/`, `tasks/init-task.md`
- ❌ Không sửa nội dung registry trong bước audit (B7) — chỉ báo cáo
- ❌ Không tạo registry thứ hai cạnh tranh với registry hiện có
- ❌ Không chạy lại OCR/extraction trên artifact đã verify (trừ khi có lý do cụ thể ghi trong báo cáo)
- ❌ Không chạy lại `npm test` / `pytest` của MACRO/MICRO — đã xanh, ngoài phạm vi
