# ACCEPTANCE CHECKLIST — NGHIỆM THU CUỐI

Checklist tổng hợp để đối chiếu sau khi Kilo hoàn thành **toàn bộ** prompt 01–09 ở **cả hai** repo.

Cách dùng: in ra, đánh dấu ✅/❌, đính kèm bằng chứng. **Mục nào ❌ thì chưa được bàn giao.**

> ### Đường dẫn làm việc
> **`MACRO`** → `C:\Users\PC\Documents\AI_project\sandbox-financial\research\advanced-macroeconomics-fourth-edition`
> **`MICRO`** → `C:\Users\PC\Documents\AI_project\sandbox-financial\research\microeconomics-pindyck-rubinfeld`
> **Thư mục prompt** → `C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts`

---

## A. CỔNG CHẶN THEO THỨ TỰ

| # | Cổng | Điều kiện qua | ✅ |
|---|---|---|---|
| G1 | 01 | Cả 2 app thực sự hiển thị nội dung (không chỉ "build xanh") | ☐ |
| G2 | 02 | Build deterministic; không mất record registry | ☐ |
| G3 | 03 | 1 request/lần tải; 0 global chết; điều hướng đổi nội dung | ☐ |
| G4 | 04 | Mọi khối nội dung có nguồn + nhãn; chương chưa có nội dung hiện trung thực | ☐ |
| G5 | 05 | 0 lỗi render; 0 `undefined`; mọi lab chạy được; parity xanh | ☐ |
| G6 | 06 | Không tràn ở 375/768/1440; tìm kiếm hoạt động | ☐ |
| G7 | 07 | 0 lab chết; chương 13–20 hiện trạng thái; 0 vi phạm cô lập | ☐ |
| G8 | 08 | Mỗi lỗi R1–R9 có ≥ 1 test, chứng minh đỏ-trước/xanh-sau | ☐ |
| G9 | 09 | `health_check.sh` xanh ở cả 2 repo; handover đủ 7 mục | ☐ |

---

## B. LỖI GỐC — MỖI LỖI PHẢI ĐÃ ĐƯỢC SỬA VÀ CÓ TEST

| Lỗi | Repo | Đã sửa | Test chống tái phát | Test chứng minh đỏ-trước |
|---|---|---|---|---|
| R1 — fetch trả HTML → `SyntaxError` | MACRO | ☐ | `M1`, `M2` → ☐ | ☐ |
| R2 — `dist-web/` thiếu `data/` | MACRO | ☐ | `M4`, `M6` → ☐ | ☐ |
| R3 — mojibake trong 5 file view | MACRO | ☐ | `M3` → ☐ | ☐ |
| R4 — `window.MIC` chết | MICRO | ☐ | `T1` → ☐ | ☐ |
| R5 — `exercises` không nối | MICRO | ☐ | `T2` → ☐ | ☐ |
| R6 — 12 `chapter-XX.json` chết | MICRO | ☐ | `T3`, `T4` → ☐ | ☐ |
| R7 — lab không render | MICRO | ☐ | `T8`, `T9` → ☐ | ☐ |
| R8 — chuỗi `undefined` | MICRO | ☐ | `T6` → ☐ | ☐ |
| R9 — đổi chương không đổi nội dung | Cả hai | ☐ | `T5`, `M2` → ☐ | ☐ |

**Quy tắc:** test phải **thất bại trước** khi sửa. Test luôn xanh mà không chứng minh được đỏ-trước → coi như chưa có test.

---

## C. `MACRO` — NGHIỆM THU CHI TIẾT

### C.1 Chức năng

| # | Tiêu chí | Baseline | Sau | ✅ |
|---|---|---|---|---|
| 1 | Lỗi console khi mở `/chapters` | `SyntaxError` | 0 lỗi | ☐ |
| 2 | Số thẻ chương ở `/chapters` | 0 | 12 | ☐ |
| 3 | Bộ đếm "Đã xác minh" | 0 | > 0 | ☐ |
| 4 | `/chapters/ch1` hiện nội dung thật | rỗng | có nội dung | ☐ |
| 5 | Điều hướng `ch1`→`ch2` đổi nội dung | không đổi | đổi | ☐ |
| 6 | Số request `data/learning/index.json` khi điều hướng 3 trang | nhiều | **1** (hoặc 0) | ☐ |
| 7 | `loadAll()` gọi từ 1 chỗ duy nhất | 5 chỗ | 1 | ☐ |
| 8 | Route 404 có link về trang chủ | không có | có | ☐ |

### C.2 Nội dung & bằng chứng

| # | Tiêu chí | ✅ |
|---|---|---|
| 9 | `PT-10-01` vẫn `FORMULA_UNVERIFIED` | ☐ |
| 10 | Không phương trình nào bị nâng trạng thái vô căn cứ | ☐ |
| 11 | Mọi `equation_id`/`model_id`/`lab_id` tham chiếu đều tồn tại | ☐ |
| 12 | ≥ 15 phương trình đã đối chiếu với `data/_source/` | ☐ |
| 13 | Mọi khối nội dung có `printed_page` + `evidence_status` | ☐ |
| 14 | Số liệu minh họa gắn nhãn `ILLUSTRATIVE` | ☐ |
| 15 | Mọi ô bị cắt trong ma trận được đánh dấu rõ, không hiện số sai | ☐ |

### C.3 Trình bày & lab

| # | Tiêu chí | ✅ |
|---|---|---|
| 16 | Số chuỗi LaTeX render lỗi = 0 | ☐ |
| 17 | LaTeX lỗi không làm trắng trang | ☐ |
| 18 | Không có CDN trong bundle | ☐ |
| 19 | Chart dùng dữ liệu từ `data/`, không hardcode | ☐ |
| 20 | `lab-solow` và `lab-taylor` chạy, đổi tham số → kết quả đổi | ☐ |
| 21 | Số mặc định của lab khớp bảng đối chiếu (19 dòng) | ☐ |
| 22 | 0 mắt xích mojibake trong `web/src/` **và** `dist-web/assets/*.js` | ☐ |

### C.4 Lệnh kiểm thử — tất cả phải PASS

| Lệnh | Kết quả | ✅ |
|---|---|---|
| `npm --prefix web run typecheck` | | ☐ |
| `npm --prefix web run test` | | ☐ |
| `npm --prefix web run build` | | ☐ |
| `python scripts/validate_app_data.py` | | ☐ |
| `node --test "tests/*.test.mjs"` (≥ 6 test mới) | | ☐ |

---

## D. `MICRO` — NGHIỆM THU CHI TIẾT

### D.1 Chức năng

| # | Tiêu chí | Baseline | Sau | ✅ |
|---|---|---|---|---|
| 1 | Số dòng bảng ở `/phuong-trinh` | 0 | 56 | ☐ |
| 2 | `EquationsTab` lọc đúng chương | — | đúng | ☐ |
| 3 | Số bài tập ở tab "Kiểm tra hiểu biết" (Ch2) | 0 | > 0, đúng Ch2 | ☐ |
| 4 | Tab "Tổng quan" Ch2 hiện nội dung từ `chapter-02.json` | placeholder | nội dung thật | ☐ |
| 5 | Số chương có nội dung thật | 0/12 | 12/12 | ☐ |
| 6 | Tab "Phòng thí nghiệm" Ch2 có select + nút tính, ra kết quả số | không | có | ☐ |
| 7 | Điều hướng `ch2`→`ch3` đổi nội dung | không đổi | đổi | ☐ |
| 8 | Grep `window.MIC` trong `web/src/` | 2 kết quả | **0** | ☐ |
| 9 | Số lab trong `course.json` trỏ tới lab không tồn tại | 13 | **0** | ☐ |
| 10 | `/chuong/13`…`/chuong/20` mở được, hiện trạng thái trung thực | — | có | ☐ |

### D.2 Nội dung

| # | Tiêu chí | ✅ |
|---|---|---|
| 11 | Bảng độ bao phủ §0–§11 × 12 chương được nộp | ☐ |
| 12 | 0 khối nội dung thiếu `printed_page`/`evidence_status` | ☐ |
| 13 | 0 nội dung nào không có nguồn | ☐ |
| 14 | Bảng `verification_rows` có nhãn trạng thái từng dòng | ☐ |
| 15 | Bảng thuật ngữ chuẩn cho từng repo đã lưu | ☐ |
| 16 | 0 mắt xích mojibake trong `web/src/` và bundle | ☐ |
| 17 | Quy ước số nhất quán trong từng repo | ☐ |

### D.3 UI

| # | Tiêu chí | ✅ |
|---|---|---|
| 18 | Không tràn ngang ở 375 / 768 / 1440 | ☐ |
| 19 | Nút chương trước/sau hoạt động | ☐ |
| 20 | Mọi vùng rỗng có empty state + lý do + hướng dẫn | ☐ |
| 21 | Tìm kiếm hoạt động ("độ co giãn" ra kết quả, bấm điều hướng đúng) | ☐ |
| 22 | `document.title` đổi theo route | ☐ |
| 23 | Tương phản WCAG AA (4.5:1) | ☐ |
| 24 | 0 chuỗi `undefined`/`NaN`/`[object Object]` ở mọi tab mọi chương | ☐ |

### D.4 Lệnh kiểm thử — tất cả phải PASS

| Lệnh | Baseline | Kết quả | ✅ |
|---|---|---|---|
| `npm --prefix web test` | **exit 1** | exit 0 | ☐ |
| `npm --prefix web run typecheck` | — | | ☐ |
| `npm --prefix web run build` | — | | ☐ |
| `python -m pytest tests -q` | — | | ☐ |
| `node --test "tests/*.test.mjs"` | 21/21 | ≥ 21/21 | ☐ |
| `python scripts/validate_html.py` | — | | ☐ |
| Số file `.spec.ts` trong `web/tests/` | 0 | ≥ 10 | ☐ |

---

## E. CÔ LẬP HAI REPO

| # | Tiêu chí | ✅ |
|---|---|---|
| 1 | Grep `pindyck\|rubinfeld` trong `MACRO` → 0 (trừ ngoại lệ đã nêu) | ☐ |
| 2 | Grep `romer\|macroeconomics` trong `MICRO` → 0 (trừ ngoại lệ đã nêu) | ☐ |
| 3 | Ngoại lệ đã được liệt kê trong báo cáo | ☐ |
| 4 | Không có registry chung, không có file dữ liệu dùng chung | ☐ |
| 5 | Bảng thuật ngữ riêng cho từng sách | ☐ |
| 6 | Không đường dẫn nội bộ / cờ toàn vẹn / mã pipeline lọt vào nội dung học thuật | ☐ |

---

## F. TRẠNG THÁI & BÀN GIAO

| # | Tiêu chí | ✅ |
|---|---|---|
| 1 | `docs/KILO_STATUS.md` tồn tại ở cả 2 repo, đủ mục | ☐ |
| 2 | `docs/HANDOVER.md` tồn tại ở cả 2 repo, đủ 7 mục | ☐ |
| 3 | `scripts/health_check.sh` chạy được ở cả 2 repo, exit ≠ 0 khi đỏ | ☐ |
| 4 | Bảng lỗi → test đầy đủ trong handover | ☐ |
| 5 | "Quyết định đã chốt" ghi lại quyết định kiến trúc | ☐ |
| 6 | Không còn mục nào trong "CHƯA LÀM" mà không nêu lý do | ☐ |
| 7 | Không còn `console.log` debug trong mã bàn giao | ☐ |
| 8 | Không có `test.skip` / `xit` để làm xanh | ☐ |
| 9 | Không nới lỏng threshold của test để qua (nếu có, lý do đã ghi) | ☐ |

---

## G. BẰNG CHỨNG BẮT BUỘC KÈM THEO

| # | Bằng chứng | ✅ |
|---|---|---|
| 1 | Output **đầy đủ** của mọi lệnh test ở §C.4 và §D.4 | ☐ |
| 2 | Screenshot ở 375 / 768 / 1440 cho cả 2 app | ☐ |
| 3 | Screenshot 1 app mỗi lab (mọi lab `MICRO` đã render, 2 lab `MACRO`) | ☐ |
| 4 | Bảng đối chiếu baseline ↔ sau (số liệu thật, không mô tả) | ☐ |
| 5 | Bảng lỗi → test → trạng thái đỏ-trước/xanh-sau | ☐ |
| 6 | Bảng độ bao phủ §0–§11 × 12 chương (`MICRO`) | ☐ |
| 7 | Bảng đếm trạng thái bằng chứng trước/sau (`MACRO`) | ☐ |
| 8 | Bảng 2 chiều `course.json` ↔ file lab thật (19 chương) | ☐ |
| 9 | Output script đếm mojibake = 0 (cả `web/src/` và bundle) | ☐ |
| 10 | Bảng kết quả bấm thật cho mọi đường dẫn tích hợp | ☐ |

---

## H. CHỐT

| Điều kiện | ✅ |
|---|---|
| Tất cả mục A–G đạt | ☐ |
| Tất cả lệnh §0.8 xanh ở **cả hai** repo | ☐ |
| Báo cáo cuối có mục "CHƯA LÀM / BLOCKED" trung thực (có thể rỗng) | ☐ |
| `docs/HANDOVER.md` đủ 7 mục ở cả 2 repo | ☐ |

**Còn mục nào ❌ → chưa bàn giao. Ghi rõ mục đó vào `docs/KILO_STATUS.md` và báo cáo.**
