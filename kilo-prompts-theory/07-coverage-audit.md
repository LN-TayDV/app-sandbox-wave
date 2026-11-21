# PROMPT 07 — B7: AUDIT COVERAGE TOÀN BỘ

> **Đọc trước:** `00-shared-contract.md` · `03-sop-validator.md`
> **Bước workflow:** B7 · **Ước lượng:** 2 ngày
> **Điều kiện:** B6 đã qua cổng.
> **Mục tiêu:** **chứng minh** rằng 4 cuốn đã được trích xuất đủ — bằng số đo, không bằng cảm nhận.
> **Cấm:** không nâng trạng thái để "cho xanh". Nếu thiếu thì ghi thiếu.

---

## 1. Vì sao cần B7

Sau B5–B6, nguy cơ lớn nhất là **tưởng đã xong thật**. B7 là bước đối chiếu độc lập: lấy danh sách chương từ **bìa/toc của sách** (nguồn độc lập với registry), rồi đối chiếu với những gì đã trích. Lệch ở đâu → nêu ra đó.

## 2. Hành động

### 2.1 Đối chiếu chương

Với mỗi cuốn:
1. Lấy danh sách chương **từ bìa/TOC trong PDF** (nguồn độc lập) → `theory/registry/books.yaml` (trường `toc_chapters`)
2. So với `toc_chapters` với danh sách chương đã có `units/` → bảng lệch
3. Mỗi chương lệch → ghi lý do: `image_only` · `no_text` · `skipped` · `partial` · `missing`

### 2.2 Đếm theo `kind`

Bảng đếm **theo cuốn × theo kind** (10 loại). Nêu rõ:
- Số phương trình theo bậc A / B / C
- Số `FORMULA_UNVERIFIED` và **lý do** từng nhóm
- Số dòng `SOURCE_GAP` / `UNVERIFIED`

### 2.3 Kiểm tra "còn sót"

Đối với mỗi chương, kiểm 3 mức:
- **Mức 1 — sót mục:** heading trong chunk không có dòng registry nào trỏ tới → báo cáo
- **Mức 2 — sót trang:** `printed_page` nào trong khoảng chương không xuất hiện trong registry → báo cáo
- **Mức 3 — sót con số:** công thức nào trong chunk không có dòng equation tương ứng → báo cáo

### 2.4 Kiểm tra bất biến hệ thống

| Kiểm tra | Kỳ vọng |
|---|---|
| `global_id` duy nhất toàn hệ thống | 0 trùng |
| `book_code` hợp lệ | 100% ∈ {HAN,ROM,PIN,MAD} |
| `printed_page`/`pdf_page` cùng có hoặc cùng rỗng | 100% |
| `pdf_page` ≤ `total_pages` | 100% |
| Validator exit code | 0 |
| `knowledge.db` truy vấn được | có kết quả |
| `build_union.py` deterministic | 2 lần chạy → hash giống |

### 2.5 Viết `theory/docs/COVERAGE_REPORT.md`

```markdown
# Coverage Report — 4 cuốn sách
Ngày: <YYYY-MM-DD> · Bước: B7

## 1. Tổng quan (bảng 4 cuốn: chương / trang / dòng registry / % phủ)
## 2. Đối chiếu chương so với TOC (bảng lệch + lý do)
## 3. Đếm theo kind (4 cuốn × 10 loại)
## 4. Bậc toán học A/B/C + danh sách FORMULA_UNVERIFIED
## 5. Kiểm tra sót mục / sót trang / sót con số
## 6. Kiểm tra bất biến hệ thống
## 7. Danh sách SOURCE_GAP — cái gì chưa có và cần gì để có
## 8. Kết luận: ĐẠT CỔNG B7 | CHƯA ĐẠT (còn N việc)
```

## 3. Acceptance criteria

| # | Tiêu chí | Bằng chứng |
|---|---|---|
| A1 | Mỗi cuốn có bảng đối chiếu chương (TOC vs registry) | §2 |
| A2 | Bảng đếm theo `kind` cho cả 4 cuốn | §3 |
| A3 | Tỉ lệ bậc A/B/C **đo bằng script** (không ước lượng) | output script |
| A4 | 3 mức kiểm sót đã chạy, kèm số lệch | §5 |
| A5 | 7 kiểm tra bất biến đã chạy, kèm kết quả từng cái | §6 |
| A6 | `theory/docs/COVERAGE_REPORT.md` đủ 8 mục | đọc file |
| A7 | Mọi `FORMULA_UNVERIFIED` được liệt kê kèm lý do — **không** nâng lên VERIFIED | §4 |
| A8 | Có kết luận rõ: ĐẠT CỔNG hay CHƯA ĐẠT + danh sách việc còn lại | §8 |
| A9 | Không sửa nội dung registry trong bước audit (chỉ báo cáo) | `git status` |

## 4. Cổng đạt

**ĐẠT CỔNG B7** khi:
- % phủ chương = 100% (hoặc phần thiếu đã được **giải thích** và nằm trong `SOURCE_GAP` được thừa nhận)
- Validator exit 0
- 7 bất biến đạt
- Có kết luận dạng danh sách, không phải kết luận miệng

**Nếu CHƯA ĐẠT** → ghi danh sách việc còn lại vào `theory/GAP_REQUESTS.md`, **không** tự nhảy sang B8.

## 5. Cập nhật trạng thái

`theory/docs/KILO_STATUS.md` · `00_project_management/WORKFLOW.md` §0 · `logs/execution_log.md` · `00_project_management/task_backlog.md`
