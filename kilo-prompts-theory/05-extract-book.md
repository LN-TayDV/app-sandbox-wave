# PROMPT 05 — B5: TRÍCH XUẤT MỘT CUỐN SÁCH (dùng chung cho 4 worker)

> **Đọc trước:** `00-shared-contract.md` · `03-sop-validator.md` (SOP + validator) · `04-pilot-hansen.md` (kết quả pilot để lấy ngưỡng)
> **Bước workflow:** B5 · **Ước lượng:** mỗi cuốn 3–10 ngày tùy độ dài (đã đo ở pilot)
> **Mục tiêu:** trích xuất **TOÀN BỘ** cuốn sách — **không phải phần liên quan**.
> **Cấm:** không dừng giữa chừng vì "phần quan trọng đã xong". Không bỏ chương. Không tự bịa.

---

## 1. Nguyên tắc cốt lõi của B5

- **Trích hết.** Mục tiêu là *coverage*, không phải *độ sâu ở vài chỗ*. Đây là tầng **nền lý thuyết dùng chung** cho mọi phân tích sau này — thiếu một chương là thiếu một mảnh.
- **Sai lệch so với "chỉ trích phần liên quan"** là nguyên nhân phổ biến nhất khiến tầng tri thức vô dụng về sau.
- **Bậc toán học trung thực.** Công thức nào không đọc được → `FORMULA_UNVERIFIED` + ghi cách suy. **Không** bịa phương trình.
- **Chương là đơn vị hoàn thành.** Xong một chương thì cập nhật trạng thái; **không** để dở dang 2 chương cùng lúc.

## 2. Tham số

| Tham số | Giá trị |
|---|---|
| `{BOOK_CODE}` | `HAN` · `ROM` · `PIN` · `MAD` |
| `{BOOK_TITLE}` | xem bảng ở `00-shared-contract.md` §0.0 |

**Cấu trúc đầu ra cho mỗi cuốn** (tạo trong `theory/books/{BOOK_CODE}/`):
```
theory/books/{BOOK_CODE}/
  chunks.jsonl          # L1 (từ B2)
  units/{NN}_{slug}.csv # từng chương: equation/assumption/theory/caveat/... 
  units/registry.csv    # gộp các chương của cuốn này
  coverage.json         # % phủ theo chương
  CHAPTER_REPORT_*.md   # báo cáo từng chương
```

## 3. Hành động

### 3.1 Xác định cấu trúc sách (không đoán)

Đọc **mục lục thật** trong PDF (front matter) → ghi vào `theory/registry/books.yaml` (`chapter_count`, `chapters: [{n, title, printed_start, printed_end, pdf_start, pdf_end}]`).

> **Cấm** dùng số chương từ trí nhớ. Lấy từ TOC của PDF. Nếu PDF không có TOC rõ → dựng từ heading chunk L1 và ghi rõ là "suy ra từ heading, không phải từ TOC".

### 3.2 Trích từng chương, theo SOP

Với **mỗi** chương, theo `theory/docs/EXTRACTION_SOP.md`:

1. **L1** — segment (đã có từ B2; kiểm lại coverage chương này)
2. **L3** — trích nội dung theo 10 loại `kind`, sinh `units/{NN}_{slug}.csv`
3. **L4** — verify toán học bậc A/B/C; bậc C **bắt buộc** qua `scientific/registry.py` (bản copy ở `theory/scripts/registry.py`)
4. **L5** — `CHAPTER_REPORT_{BOOK}_{NN}.md` theo mẫu SOP

**Mỗi dòng registry phải có:** `book_code` · `global_id` (`EQ-{BOOK}-0001` / `TH-{BOOK}-0001` / `AS-{BOOK}-0001` / …) · `id` cũ (nếu registry đích có cột này) · `printed_page` · `pdf_page` · `verification_status` · `note`.

### 3.3 Quy tắc nội dung học thuật

- **Tiếng Việt** cho `meaning`, `summary`, `usage`, `caveat`, `note`. **Giữ nguyên tiếng Anh** cho thuật ngữ chuyên ngành, ký hiệu, và công thức.
- **Công thức:** giữ LaTeX gốc nếu có; nếu sách in bằng ký tự Unicode → chuyển sang LaTeX và ghi chú `note` là *chuyển đổi từ ký tự Unicode*.
- **Ví dụ số:** số trong sách = `BOOK_EVIDENCE`. Số **tự tính** = `ILLUSTRATIVE` + nêu công thức dùng.
- **Số trang:** `printed_page` là trang **in trên giấy**; `pdf_page` là trang trong file. Nếu suy ra → ghi rõ trong `note`.
- **Không chép lại nguyên văn đoạn dài** — diễn giải trung thực, trích dẫn ngắn kèm trang.
- **Không thêm ý tác giả không nói.** Nếu là diễn giải của bạn → `RESEARCH_SYNTHESIS`.

### 3.4 Xử lý chỗ không đọc được

| Tình huống | Hành động |
|---|---|
| Trang là **hình toàn trang** (chữ rất ít, có ảnh) | `kind: "image_page"`, trích phần chữ có, ghi rõ "nội dung chính là hình" |
| **Công thức là ảnh** | bậc C: render-diff → `NUMERICALLY_VERIFIED` hoặc `FORMULA_UNVERIFIED` |
| **Chữ bị lỗi font / ký tự vỡ** | ghi `note` cụ thể (mẫu ký tự hỏng), `verification_status: UNVERIFIED` |
| **Bảng số** | `kind: "table"`, tách thành CSV ở `theory/tables/{BOOK}_{NN}_{slug}.csv`, **không** nhúng vào CSV registry |
| **Hình** | `kind: "figure"`, crop ảnh vào `theory/figures/{BOOK}_{NN}_{slug}.png`, ghi `file` |
| **Bài tập** | `kind: "exercise"`, `answer_available` = CÓ/KHÔNG; **không tự giải** bài chưa có lời giải trong sách |

### 3.5 Cập nhật tiến độ sau **mỗi** chương

Không đợi hết cuốn mới ghi. Sau mỗi chương:
- `theory/docs/KILO_STATUS.md`: chương vừa xong, số dòng registry, số phương trình theo bậc
- `theory/books/{BOOK}/coverage.json`: % phủ
- `logs/execution_log.md`: 1 dòng

→ để bị gián đoạn thì nhảy đúng chỗ, không phải làm lại.

## 4. Acceptance criteria

| # | Tiêu chí | Bằng chứng |
|---|---|---|
| A1 | `theory/registry/books.yaml` có cấu trúc chương **lấy từ TOC thật** của PDF | đọc file + trích TOC |
| A2 | **≥90% chương** đã trích xuất (không bỏ chương bắt buộc; cho phép ≤10% chương PARTIAL có lý do) | đối chiếu `chapters[]` với `units/` |
| A3 | `units/registry.csv` của cuốn: mọi dòng có `book_code` + `global_id` duy nhất + trang hợp lệ | chạy validator |
| A4 | Validator chạy xanh trên registry của cuốn này | output validator |
| A5 | Tỉ lệ `FORMULA_UNVERIFIED` **được báo cáo** kèm lý do từng chương | trong CHAPTER_REPORT |
| A6 | Có `CHAPTER_REPORT_{BOOK}_*.md` cho **mọi** chương | đếm file |
| A7 | `coverage.json` phản ánh đúng số chương đã xong | đọc file |
| A8 | Không trích xuất chương nào của cuốn khác trong phiên này | `git status` |
| A9 | `theory/docs/KILO_STATUS.md` cập nhật sau **mỗi** chương (thời gian sửa file tăng dần) | đọc lịch sử sửa |

## 5. Cổng đạt

A1–A9 đạt cho **cuốn đang làm** với ngưỡng phủ ≥90% chương (A2). Một cuốn xong → cuốn đó được tick ✅. Sau cuốn thứ 4 → sang B6.

> **Ghi rõ trong báo cáo nếu phải dừng giữa chừng** (hết phiên, hết giờ): nêu chương đang dở và trạng thái `PARTIAL` — **không** ghi "xong" khi còn chương chưa trích.

## 6. Cập nhật trạng thái

`theory/docs/KILO_STATUS.md` · `00_project_management/WORKFLOW.md` §0 · `logs/execution_log.md` · `00_project_management/task_backlog.md`
