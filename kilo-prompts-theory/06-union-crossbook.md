# PROMPT 06 — B6: GỘP 4 CUỐN + CROSS-BOOK INDEX

> **Đọc trước:** `00-shared-contract.md` · `03-sop-validator.md`
> **Bước workflow:** B6 · **Ước lượng:** 3 ngày
> **Điều kiện:** cả 4 cuốn ở B5 đã đạt cổng.
> **Mục tiêu:** gộp 4 registry thành **một** tầng tri thức dùng chung, có tra cứu nhanh.
> **Cấm:** không sửa lại nội dung đã trích (trừ khi phát hiện lỗi schema/lỗi `global_id` — khi đó ghi lại, không âm thầm sửa).

---

## 1. Vì sao cần B6

4 registry rời rạc không phải tầng tri thức. Cần:
- **một** registry chuẩn, truy vấn được
- `global_id` duy nhất toàn hệ thống
- **cross-book index**: khái niệm/cơ chế dùng chung giữa nhiều cuốn — đây là chỗ **giá trị học thuật lớn nhất** sinh ra từ việc gộp (một cơ chế được mô tả ở 3 cuốn khác nhau = 3 bằng chứng độc lập).

## 2. Hành động

### 2.1 Gộp registry

Đầu ra vào `theory/registry/`:
```
theory/registry/
  equation_registry.csv      # gộp 4 cuốn
  theory_registry.csv        # gộp 4 cuốn
  assumption_registry.csv
  theorem_registry.csv
  caveat_registry.csv
  concept_registry.csv
  figure_registry.csv
  table_registry.csv
  exercise_registry.csv
  bibliography.csv
  books.yaml
```

**Quy tắc gộp:**
- **Giữ nguyên ID cũ** ở cột `id` (nếu có) — không phá vỡ tham chiếu từ `research/`.
- Thêm `book_code` (bắt buộc) + `global_id` (bắt buộc, duy nhất) + `source_repo` (`research/...` hoặc `theory/books/...`) để truy vết nguồn gốc.
- `global_id` theo format `<KIND>-<BOOK>-<NNNN>`, ví dụ `EQ-HAN-0001`, `TH-ROM-0007`, `AS-PIN-0003`, `CV-MAD-0012`.
  - `KIND`: `EQ` equation · `TH` theory · `AS` assumption · `TM` theorem · `CV` caveat · `CN` concept · `FG` figure · `TB` table · `EX` exercise.
- **Thứ tự dòng:** theo `book_code` (HAN → ROM → PIN → MAD) rồi `printed_page` rồi `id`.
- **Không sửa nội dung.** Nếu phát hiện dòng lỗi (thiếu trang, `global_id` trùng, LaTeX hỏng) → ghi vào `theory/registry/_merge_issues.csv` với lý do, và sửa **chỉ** lỗi kỹ thuật, không sửa nội dung học thuật.

### 2.2 Kế thừa 2 registry sẵn có

| Registry | Đường dẫn | Dòng | Cột |
|---|---|---|---|
| MICRO equation | `research/microeconomics-pindyck-rubinfeld/05_equation_registry.csv` | 57 | 16 |
| MACRO equation | `research/advanced-macroeconomics-fourth-edition/workflows/05_equation_registry.csv` | 29 | 16 |
| MICRO theory | `research/microeconomics-pindyck-rubinfeld/04_theory_registry.csv` | 32 | 19 |
| MACRO theory | `research/advanced-macroeconomics-fourth-edition/workflows/04_theory_registry.csv` | 16 | 19 |

**Đây là 2 registry đầu tiên phải gộp vào** — chúng đã có `book_code`/`global_id` sẵn thì giữ nguyên; chưa có thì **sinh** theo quy tắc §2.1 và **ghi lại** việc sinh ở `_merge_issues.csv` (không phải lỗi, là *ghi chú chuẩn hóa*).

> **Đừng để sót:** registry đã có 2 cuốn này là nguồn tri thức có giá trị nhất hiện tại. Gộp phải **giữ đủ** số dòng — kiểm bằng đếm.

### 2.3 Cross-book index

`theory/docs/CROSS_BOOK_INDEX.md` — bảng trỏ tới khái niệm/cơ chế xuất hiện ở **≥2 cuốn**:

| Khái niệm | Cơ chế | HAN | ROM | PIN | MAD | Ghi chú đối chiếu |
|---|---|---|---|---|---|---|
| Credit crunch | Nguồn cung tín dụng co | ✓ | ✓ | — | ✓ | ROM: cung–cầu tín dụng; MAD: thanh khoản quốc tế; HAN: hệ số nhân |
| Financial contagion | Lan truyền | — | ✓ | — | ✓ | ... |

**Yêu cầu:** cột "Ghi chú đối chiếu" phải nêu **cơ chế có khác nhau không** — đây mới là giá trị. Nếu 3 cuốn nói cùng một điều → ghi "cùng cơ chế". Nếu khác → ghi khác ở đâu, và ảnh hưởng gì.

### 2.4 Index tra cứu nhanh

- `theory/knowledge.db` (SQLite + FTS5) — nạp **cả** chunks và **cả** registry để tra cứu liên bảng: tìm một khái niệm → xem nó xuất hiện ở đâu, ở chương nào, trang nào, với công thức nào.
- `theory/docs/INDEX.md` — mục lục người đọc: theo chương, theo `kind`, theo chủ đề, theo `global_id`.
- Script: `theory/scripts/build_union.py` (gộp) + `theory/scripts/build_index.py` (index) — **phải chạy lại được**, không sửa tay file sinh ra.

## 3. Acceptance criteria

| # | Tiêu chí | Bằng chứng |
|---|---|---|
| A1 | `theory/registry/equation_registry.csv` có đủ dòng từ 4 cuốn **+** 57 (MICRO) + 29 (MACRO) | đếm dòng, đối chiếu |
| A2 | `theory/registry/theory_registry.csv` có đủ dòng từ 4 cuốn + 32 (MICRO) + 16 (MACRO) | đếm dòng |
| A3 | Mọi dòng có `book_code` + `global_id`; `global_id` **duy nhất** toàn file | validator + đếm trùng |
| A4 | Cột giữ **đúng 16 / 19** như registry gốc (không thêm/bớt cột ngoài ý muốn) | dump header |
| A5 | `theory/docs/CROSS_BOOK_INDEX.md` có ≥5 khái niệm dùng chung, cột đối chiếu nêu rõ khác biệt cơ chế | đọc file |
| A6 | `theory/docs/INDEX.md` tồn tại, tra cứu được theo 4 chiều | đọc + thử tìm |
| A7 | `theory/knowledge.db` truy vấn FTS5 trả kết quả **nối được** chunk ↔ registry (VD: tìm "credit crunch" → ra cuốn, chương, trang, công thức liên quan) | output truy vấn |
| A8 | `_merge_issues.csv` ghi lại mọi chuẩn hóa/lỗi đã xử lý | đọc file |
| A9 | `theory/scripts/build_union.py` + `build_index.py` chạy lại từ đầu cho ra **kết quả giống hệt** (deterministic) | chạy 2 lần, so hash |

## 4. Cổng đạt

A1–A9 đạt → sang B7 (audit coverage).

## 5. Cập nhật trạng thái

`theory/docs/KILO_STATUS.md` · `00_project_management/WORKFLOW.md` §0 · `logs/execution_log.md` · `00_project_management/task_backlog.md`
