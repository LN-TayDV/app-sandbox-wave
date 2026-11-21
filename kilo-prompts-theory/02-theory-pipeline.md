# PROMPT 02 — B2: DỰNG TẦNG `theory/` + PIPELINE L0/L1/L2

> **Đọc trước:** `00-shared-contract.md` · **Điều kiện:** B1 đã qua cổng
> **Bước workflow:** B2 · **Ước lượng:** 2 ngày
> **Mục tiêu:** biến 4 PDF thành **chunk có cấu trúc + chỉ mục tìm kiếm** — chưa động vào tri thức (L3+ là B4/B5).
> **Cấm:** không trích xuất nội dung học thuật ở bước này. Không sửa `research/`. Không sửa `data/book/`.

---

## 1. Bối cảnh

Hai trong 4 cuốn đã có L0 (PDF → text) nhưng **nằm trong repo khác, không dùng lại được trực tiếp** mà không sửa `research/`. Phải **copy script** sang `theory/scripts/`, chạy lại từ PDF gốc trong `data/book/`, và dựng chung một định dạng cho cả 4.

**Đã biết (không cần đo lại):**

| Cuốn | Số trang | Tình trạng L0 hiện có | Vấn đề cần xử lý |
|---|---|---|---|
| `PIN` | **787** | `research/microeconomics-pindyck-rubinfeld/logs/extract_pdf.json` ghi 787 trang, `logs/coverage.json` ghi **761** | ⚠️ **Mâu thuẫn 26 trang.** 14 trang "short" nội địa (90, 170, 180, 210, 284, 368, 370, 454, 544, 574, 610, 646, 676, 784) — nhiều khả năng là **trang hình toàn trang** |
| `ROM` | **738** | `research/advanced-macroeconomics-fourth-edition/logs/extract_pdf.json` — 738/738, 0 failed, 8 short (đều là front matter) | ✅ Có `chapter_ranges` 12 chương — **dùng làm mẫu segmentation** |
| `HAN` | **?** | ❌ Chưa ai trích xuất | Phải tự làm L0 |
| `MAD` | **?** | ❌ Chưa ai trích xuất | Phải tự làm L0 |

## 2. Script có thể tái dùng (đọc trước khi viết mới)

```
C:\Users\PC\Documents\AI_project\sandbox-financial\research\advanced-macroeconomics-fourth-edition\scripts\inspect_source.py
C:\Users\PC\Documents\AI_project\sandbox-financial\research\advanced-macroeconomics-fourth-edition\scripts\extract_pdf.py
```

**Cấu trúc `research/advanced-macroeconomics-fourth-edition/`** (tham khảo layout output mong muốn):
`scientific/` (4 lớp source→symbolic→numeric→render, dùng lại ở B4) · `scripts/` · `workflows/` (chứa `05_equation_registry.csv`) · `logs/` · `docs/`

**Cấu trúc `research/microeconomics-pindyck-rubinfeld/`**: `05_equation_registry.csv` (16 cột / 57 dòng) · `04_theory_registry.csv` (19 cột / 32 dòng) · `logs/` · `web/`

## 3. Hành động

### 3.1 Dựng skeleton `theory/`

```
theory/
  books/{HAN,ROM,PIN,MAD}/     # L0 output: text theo trang, page_map, chunks.jsonl
  registry/                    # books.yaml + các registry CSV gộp
  scripts/                     # ingest_book.py, segment_book.py, index_knowledge.py
  docs/                        # EXTRACTION_SOP.md, KILO_STATUS.md, COVERAGE_REPORT.md
  figures/ tables/ exercises/  # tài nguyên trích từ PDF (ảnh crop)
```

### 3.2 `theory/registry/books.yaml` — manifest 4 cuốn

Mỗi cuốn: `book_code` · `title` · `authors` · `edition` · `year` · `pdf_path` (tương đối so với gốc) · `total_pages` (đo bằng PyMuPDF, **không đoán**) · `sha256` (bằng `Get-FileHash`) · `chapter_count` · `notes` (gồm mâu thuẫn PIN nếu có).

### 3.3 `theory/scripts/ingest_book.py` — L0 (copy + sửa từ `extract_pdf.py`)

Cho mỗi trang: text thô · số ký tự · ảnh nhúng trong trang (nếu trang là hình toàn trang → đánh dấu `image_page: true`, **không coi là lỗi**) · bbox của khối công thức nếu phát hiện được.

**Bắt buộc:** ghi `page_map` ánh xạ **trang PDF ↔ trang in** (suy ra từ header/footer của sách) — cột `printed_page` trong registry phụ thuộc vào đây. Trang suy ra phải ghi rõ là suy ra.

**Cấm dùng `fitz` ở chế độ làm mất vị trí chỉ số** — đây là lỗi đã từng làm hỏng MACRO. Nếu dùng, phải tắt và ghi lại.

### 3.4 `theory/scripts/segment_book.py` — L1

Cắt chunk theo mục (heading), gán `kind` ∈ {`chapter`, `section`, `subsection`, `paragraph`, `figure`, `table`, `equation`, `exercise`, `example`, `box`, `front_matter`, `back_matter`}, dựng `heading_path` (đường dẫn heading đầy đủ), ghi `coverage.json`.

**Mẫu chuẩn:** `chapter_ranges` của ROM (12 chương). Đọc để biết format mong muốn, rồi làm cho cả 4 cuốn.

**Xử lý 14 trang short của PIN:** nếu trang có `< 200` ký tự và có ảnh → `kind: "image_page"`, **không tính là trang mất**. Nếu không có ảnh → `kind: "unresolved"`, ghi vào `coverage.json` và báo cáo.

### 3.5 `theory/scripts/index_knowledge.py` — L2

SQLite + **FTS5 (stdlib, không thêm dependency)**. Bảng: `books`, `chunks`, `pages`, `fts_chunks`. Phải truy vấn được theo: `book_code`, `heading_path`, `kind`, `printed_page`.

### 3.6 Chạy cho cả 4 cuốn

- `HAN`, `MAD` → chạy L0 từ đầu (chưa có gì)
- `PIN`, `ROM` → chạy L0 + L1 từ PDF gốc trong `data/book/` (không đọc lại output của repo `research/`)

### 3.7 Đối chiếu mâu thuẫn PIN

Ghi vào `books.yaml` `notes` và `coverage.json`: 787 (extract) vs 761 (coverage) — tìm ra nguyên nhân (giả thuyết: coverage chỉ đếm trang có text ≥ ngưỡng, bỏ qua 26 trang hình). **Đo lại và xác định**, đừng chỉ lặp lại con số.

## 4. Acceptance criteria

| # | Tiêu chí | Bằng chứng |
|---|---|---|
| A1 | `theory/registry/books.yaml` có đủ 4 cuốn, mỗi cuốn có `total_pages` **đo bằng script** + `sha256` | đọc file + output script |
| A2 | `theory/scripts/{ingest_book,segment_book,index_knowledge}.py` chạy được từ dòng lệnh, có `--help` | output `--help` |
| A3 | `PIN`: **787/787** trang có chunk, 0 trang mất | `coverage.json` |
| A4 | `ROM`: **738/738** trang có chunk, 0 trang mất | `coverage.json` |
| A5 | `HAN`, `MAD`: có manifest + page_map; số trang khớp `books.yaml` | `coverage.json` |
| A6 | Mâu thuẫn PIN 787 vs 761 **đã giải thích** bằng đo | ghi rõ nguyên nhân trong `books.yaml` + `coverage.json` |
| A7 | Truy vấn FTS5 trả kết quả đúng (ví dụ: tìm "credit crunch" → có chunk thuộc đúng `book_code`) | output truy vấn |
| A8 | Không có file nào bị sửa trong `research/`, `data/book/`, `tasks/` | `git status` |
| A9 | Mọi chunk có `book_code`, `pdf_page`, `printed_page` (hoặc `printed_page` rỗng nhưng `pdf_page` có) | script kiểm |

## 5. Cổng đạt

Đủ A1–A9 **và** truy vấn FTS5 trả kết quả. Không đạt → `BLOCKED` với lý do cụ thể, **không** sang B3.

## 6. Cập nhật trạng thái

`theory/docs/KILO_STATUS.md` · `00_project_management/WORKFLOW.md` §0 (tick B2) · `logs/execution_log.md` · `00_project_management/task_backlog.md`
