# PROMPT 09 — RECOVERY (KHÔI PHỤC KHI BỊ GIÁN ĐOẠN) & BÀN GIAO

> **Mã repo:** `MACRO` và `MICRO` — hai phần độc lập.
> **Phụ thuộc:** `00-shared-contract.md` và các prompt 01–08.

> ### Đường dẫn làm việc
> **`MACRO`** → `C:\Users\PC\Documents\AI_project\sandbox-financial\research\advanced-macroeconomics-fourth-edition`
> **`MICRO`** → `C:\Users\PC\Documents\AI_project\sandbox-financial\research\microeconomics-pindyck-rubinfeld`
> **Hợp đồng** → `C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts\00-shared-contract.md`
> **Ma trận thực thi** → `C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts\EXECUTION-MATRIX.md`
> **Mục tiêu:** Kilo bị gián đoạn (hết phiên, hết thời gian, đổi mô hình) thì có thể **tiếp tục chính xác** mà không làm lại hoặc làm hỏng.

---

## 9.0. Nguyên tắc

> **Trạng thái công việc phải nằm trong repo, không nằm trong đầu Kilo.**

Mỗi prompt bắt buộc ghi lại trạng thái vào **file trong repo** (không phải file ngoài repo, không phải chỉ trong chat). Nếu Kilo bị cắt ngang, người tiếp tục chỉ cần đọc file đó là biết chỗ nào đang dở.

---

## 9.1. File trạng thái bắt buộc

Mỗi repo có **một** file trạng thái duy nhất:

- `MACRO`: `C:\Users\PC\Documents\AI_project\sandbox-financial\research\advanced-macroeconomics-fourth-edition\docs\KILO_STATUS.md`
- `MICRO`: `C:\Users\PC\Documents\AI_project\sandbox-financial\research\microeconomics-pindyck-rubinfeld\docs\KILO_STATUS.md`

Nếu `docs/` chưa có thì tạo. Nếu file đã có (do phiên trước tạo) — **cập nhật**, không tạo bản sao.

### 9.1.1 Cấu trúc `KILO_STATUS.md`

```markdown
# Trạng thái triển khai Kilo — <Tên sách>

_Cập nhật lần cuối: <YYYY-MM-DD HH:MM>_

## Tổng quan
- Prompt hiện tại: <đang làm prompt nào>
- Trạng thái: <CHƯA BẮT ĐẦU | ĐANG LÀM | ĐÃ XONG | BLOCKED>
- Lệnh kiểm thử cuối đã chạy: <lệnh> → <PASS/FAIL>
- Commit gần nhất: <hash> — <thông điệp>

## Tiến độ theo prompt
| Prompt | Mục tiêu | Trạng thái | Ghi chú |
|---|---|---|---|
| 01 | Root-cause recovery | DONE | A1–A9, B1–B12 đạt |
| 02 | Data pipeline | CHƯA BẮT ĐẦU | — |
| ... | | | |

## Việc đang dở (DỒN NHIỀU VÀO ĐÂY)
- **File:** <path> — **Dòng:** <số> — **Cần làm:** <một câu>
- **Vì sao dở:** <lý do>
- **Cách tiếp tục:** <hành động cụ thể cho lần sau>

## Quyết định đã chốt (KHÔNG cần hỏi lại)
- <quyết định> — <lý do> — <áp dụng cho prompt nào>

## BLOCKED
- <mục> — <lý do> — <cần gì để mở>

## Kinh nghiệm rút ra
- <bài học từ lỗi đã gặp — ngắn gọn, để prompt sau không lặp lại>
```

### 9.1.2 Quy tắc cập nhật

- Cập nhật file này **ngay sau khi** mỗi bước con quan trọng, không chờ cuối prompt.
- "Việc đang dở" phải đủ cụ thể để người khác đọc là hiểu ngay, không cần đọc lại lịch sử chat.
- "Quyết định đã chốt" là phần **quan trọng nhất** — ghi lại các quyết định kiến trúc (ví dụ: "chọn import tĩnh thay vì `server.fs.allow`") để prompt sau không đề xuất ngược lại.

---

## 9.2. Giao thức tiếp tục sau khi bị gián đoạn

Khi bắt đầu phiên mới, Kilo làm đúng thứ tự này **trước khi sửa bất kỳ dòng nào**:

**Bước 1 — Đọc trạng thái.**
```bash
cat "C:\Users\PC\Documents\AI_project\sandbox-financial\research\advanced-macroeconomics-fourth-edition\docs\KILO_STATUS.md"
cat "C:\Users\PC\Documents\AI_project\sandbox-financial\research\microeconomics-pindyck-rubinfeld\docs\KILO_STATUS.md"
```

**Bước 2 — Xác minh bằng thực tế.** Không tin mô tả trong file — hãy kiểm, cho **từng repo**:
```bash
cd "C:\Users\PC\Documents\AI_project\sandbox-financial\research\advanced-macroeconomics-fourth-edition" && git status && git log --oneline -5
cd "C:\Users\PC\Documents\AI_project\sandbox-financial\research\microeconomics-pindyck-rubinfeld" && git status && git log --oneline -5
```
Chạy lại lệnh kiểm thử ghi trong "Lệnh kiểm thử cuối đã chạy" để xác nhận trạng thái hiện tại.

**Bước 3 — Đối chiếu.** Mô tả trong `KILO_STATUS.md` có khớp với `git status` không?
- Khớp → tiếp tục đúng chỗ đang dở.
- Lệch (có file sửa dở, hoặc có thay đổi lạ) → **dừng**, ghi rõ vào báo cáo, và tiếp tục một cách **bảo thủ**: hoàn tất phần đang dở trước, **không** làm thêm việc mới.

**Bước 4 — Tiếp tục.** Làm đúng phần đang dở, cập nhật `KILO_STATUS.md` sau khi xong.

### 9.3 Điều kiện dừng an toàn

Kilo **phải dừng** (không cắt ngang giữa chừng) nếu gặp:

| Tình huống | Hành động |
|---|---|
| Sắp hết thời gian / phiên | Hoàn tất bước con hiện tại → cập nhật `KILO_STATUS.md` → báo cáo |
| Test đỏ do lý do **không liên quan** tới prompt đang làm | Ghi baseline đỏ vào `KILO_STATUS.md` → tiếp tục phần còn lại → nêu trong báo cáo |
| Gặp BLOCKED | Ghi vào mục BLOCKED → **bỏ qua phần đó** → tiếp tục phần khác → báo cáo |
| Không chắc chắn về quyết định học thuật | Ghi vào mục BLOCKED kèm 2–3 lựa chọn và khuyến nghị → tiếp tục phần khác |
| Phát hiện lỗi ngoài phạm vi prompt | Ghi vào "Kinh nghiệm rút ra" hoặc "Rủi ro còn lại" → **không sửa** |

**Không bao giờ** dừng giữa một sửa đổi chưa hoàn tất mà không ghi lại trạng thái file cụ thể.

---

## 9.4. Kiểm tra sức khỏe (chạy trước khi bắt đầu, và trước khi bàn giao)

Tạo một script tự kiểm tra ở **gốc mỗi repo** (không đặt trong `kilo-prompts/`):

- `MACRO`: `C:\Users\PC\Documents\AI_project\sandbox-financial\research\advanced-macroeconomics-fourth-edition\scripts\health_check.sh`
- `MICRO`: `C:\Users\PC\Documents\AI_project\sandbox-financial\research\microeconomics-pindyck-rubinfeld\scripts\health_check.sh`

Script chạy tuần tự các lệnh §0.8 tương ứng, in `PASS`/`FAIL` cho từng lệnh, và **thoại với code ≠ 0 nếu bất kỳ lệnh nào đỏ**.

Dùng cho:
- Kiểm tra trạng thái khi phiên mới bắt đầu.
- Chứng minh trước/sau khi sửa.
- Làm cổng chặn trong CI.

Chạy được bằng 1 lệnh:
```bash
bash scripts/health_check.sh
```

---

## 9.5. Bàn giao cuối cùng

Khi hoàn thành **toàn bộ** prompt 01–08 ở **cả hai** repo, Kilo viết cho mỗi repo một file:

- `MACRO`: `C:\Users\PC\Documents\AI_project\sandbox-financial\research\advanced-macroeconomics-fourth-edition\docs\HANDOVER.md`
- `MICRO`: `C:\Users\PC\Documents\AI_project\sandbox-financial\research\microeconomics-pindyck-rubinfeld\docs\HANDOVER.md`

Nội dung bắt buộc:

```markdown
# Bàn giao — <Tên sách>

## 1. Trạng thái cuối
- Các prompt 01–08: <đã xong / còn tồn đọng>
- Lệnh kiểm thử cuối: <lệnh> → <PASS/FAIL>
- Số lượng bài tập / phương trình / lab đang hiển thị: <con số thật>

## 2. Đã sửa gì (theo nhóm)
| Nhóm | Mô tả | File chính |
|---|---|---|

## 3. Khoảng trống còn lại
| Mục | Lý do chưa làm | Cần gì để làm |
|---|---|---|

## 4. Bản đồ dữ liệu
- Dữ liệu ở đâu, sinh bằng gì, kiểm tra bằng lệnh nào

## 5. Bảng lỗi → test
| Lỗi | Test | File |
|---|---|---|

## 6. Cách chạy app
```bash
# dev
npm --prefix web run dev
# build
npm --prefix web run build
# kiểm thử
bash scripts/health_check.sh
```

## 7. Cảnh báo
- <những gì người sau **phải** biết trước khi sửa>
```

---

## 9.6. Acceptance — PROMPT 09

| # | Tiêu chí | Bằng chứng |
|---|---|---|
| 1 | `docs/KILO_STATUS.md` tồn tại ở **cả hai** repo, đầy đủ mục | Đọc file |
| 2 | `scripts/health_check.sh` tồn tại ở cả hai repo, chạy được, exit ≠ 0 khi đỏ | Chạy + output |
| 3 | File trạng thái ghi đủ "Việc đang dở" với đường dẫn + dòng | Đọc file |
| 4 | "Quyết định đã chốt" ghi lại các quyết định kiến trúc | Đọc file |
| 5 | `docs/HANDOVER.md` tồn tại ở cả hai repo, đủ 7 mục | Đọc file |
| 6 | Mô tả trong `KILO_STATUS.md` khớp `git status` | Đối chiếu |
| 7 | Toàn bộ lệnh §0.8 xanh ở cả hai repo | Output đầy đủ |

---

## 9.7. Nguyên tắc cuối cùng

1. **Sự thật quan trọng hơn sự tốt đẹp.** Một báo cáo trung thực nói "chưa làm X" tốt hơn một báo cáo bịa.
2. **Bằng chứng quan trọng hơn khẳng định.** Không có output lệnh → không được kết luận.
3. **Trạng thái trong repo, không trong chat.** Chat sẽ mất; file thì không.
4. **Sửa một lần, sửa đúng.** Ưu tiên sửa gốc cơ chế (generator, store, path) thay vì vá triệu chứng.
5. **Trung thực về bằng chứng học thuật.** Một nhãn `CHƯA ĐỐI CHIẾU ẢNH` trung thực tốt hơn một `VERIFIED` bịa. Trạng thái hư trống là trạng thái hợp lệ.
