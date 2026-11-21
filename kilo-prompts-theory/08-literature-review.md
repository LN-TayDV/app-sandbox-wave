# PROMPT 08 — B8: GĐẠN 1 — TỔNG QUAN TÀI LIỆU (đóng được)

> **Đọc trước:** `00-shared-contract.md` · `theory/docs/COVERAGE_REPORT.md` (B7) · `theory/docs/CROSS_BOOK_INDEX.md` (B6)
> **Bước workflow:** B8 · **Ước lượng:** 1–2 tuần
> **Mục tiêu:** đóng GĐ1 thật sự — hiện tại `literature_matrix.csv` **rỗng** (309 B = chỉ header), `critical_review.md` và `research_gap.md` **chưa tồn tại**.
> **Cấm:** không bịa trích dẫn. Không tự tạo DOI. Mọi nguồn phải truy cập được và có bằng chứng.

---

## 1. Hiện trạng (đã kiểm chứng)

| Artifact | Trạng thái |
|---|---|
| `01_literature/Literature_Sources_Compilation.md` | 12.049 B · ~7 nguồn · 3 nhóm chính |
| `01_literature/literature_matrix.csv` | **RỖNG** — 309 B, chỉ header |
| `01_literature/search_log.csv` | 3.907 B |
| `01_literature/sources/` | 2 PDF + 2 TXT |
| `01_literature/critical_review.md` | **chưa có** |
| `01_literature/research_gap.md` | **chưa có** |
| `memory/literature-research-complete.md` | ghi "hoàn thành" — **sai**, vì matrix rỗng |

**Chưa phủ 7 nhánh A–G** trong `tasks/search.md` (hiện phủ khoảng 1/3).

## 2. Hành động

### 2.1 Hoàn thiện ma trận tài liệu

Đọc header của `01_literature/literature_matrix.csv` trước → giữ **nguyên tên cột và thứ tự cột**, chỉ điền dữ liệu.

Mỗi dòng phải có nguồn kiểm chứng được:
- `doi` hoặc `url` — **phải truy cập được**, không bịa
- `access_date` — ngày truy cập thật
- `evidence_status` ∈ tập nhãn §0.2 hợp đồng
- trạng thái đọc: `full_text` / `abstract_only` / `metadata_only` — **không đánh dấu full_text nếu chỉ đọc abstract**

### 2.2 Khảo sát đủ 7 nhánh A–G

Đọc `tasks/search.md` để lấy đúng 7 nhánh và từ khóa. Mỗi nhánh: ghi vào `search_log.csv` (truy vấn + ngày + số kết quả + nguồn), rồi chọn nguồn đáng đưa vào ma trận.

**Ưu tiên bổ sung nguồn phản bác mạnh nhất:**
- **Luna & Zanforlin (2025)** — chưa đọc toàn văn. Đây là bằng chứng phản bác mạnh nhất với luận văn. **Phải đọc toàn văn và đối chiếu trực tiếp** với ý tưởng Cát Truồi.
- Các nghiên cứu dùng **sandpile/network contagion** trong tài chính (Brunnermeier, Gai–Kapadia, Caccioli, Diebold–Yilmaz, Acemoglu–Ozdaglar, Battiston) — đây là "hàng xóm" học thuật của IFWST.

### 2.3 `01_literature/critical_review.md`

Mỗi nguồn quan trọng: tóm tắt · phương pháp · dữ liệu · kết quả chính · **hạn chế** · **khoảng trống** · **quan hệ với IFWST** (củng cố / mâu thuẫn / bổ sung).

**Phải có phần đánh giá phản bác:** nguồn nào làm suy yếu luận văn, và vì sao.

### 2.4 `01_literature/research_gap.md`

Chỉ được viết khi ma trận đủ. Cấu trúc:
1. Khoảng trống đã xác định (mỗi khoảng trống → trích dẫn nguồn minh hoạ)
2. Khoảng trống **đóng góp được** của IFWST
3. Khoảng trống **chưa đóng được** → phải nói thẳng
4. Phân biệt: khoảng trống **thực sự** vs khoảng trống do **chưa đọc** (hai loại này khác nhau — đừng trộn)

### 2.5 Dùng tầng `theory/` để định vị

B6–B7 đã cho `theory/docs/CROSS_BOOK_INDEX.md` — khái niệm dùng chung giữa 4 cuốn. Dùng nó để xác định: **những cơ chế mà sách giáo khoa đã mô tả** ⇒ khoảng trống nghiên cứu không nằm ở phát minh cơ chế, mà ở **áp dụng cơ chế đó vào bối cảnh tài chính quốc tế cụ thể** của IFWST.

Đây là lý do B5–B7 phải xong trước B8: nó biến `research_gap.md` từ "chỗ chưa ai làm" (yếu) thành "cơ chế đã biết, chưa ai ghép với bối cảnh này" (mạnh).

## 3. Acceptance criteria

| # | Tiêu chí | Bằng chứng |
|---|---|---|
| A1 | `literature_matrix.csv` **không còn rỗng**; số dòng ≥ số nguồn đã xác minh; giữ nguyên header | đếm dòng + dump header |
| A2 | **≥15 nguồn**, phủ đủ 7 nhánh A–G | ma trận + search_log |
| A3 | Mọi dòng có DOI/URL **truy cập được** (kiểm HTTP status) + `access_date` | output kiểm tra |
| A4 | `evidence_status` hợp lệ; trạng thái đọc trung thực (không đánh dấu full_text khi chỉ đọc abstract) | rà lại từng dòng |
| A5 | **Luna & Zanforlin (2025) đã đọc toàn văn** và có đánh giá trong `critical_review.md` | trích dẫn + trang |
| A6 | `critical_review.md` tồn tại, có phần đánh giá phản bác | đọc file |
| A7 | `research_gap.md` tồn tại, có cả 4 mục §2.4; phân biệt khoảng trống thật vs chưa đọc | đọc file |
| A8 | Có trích dẫn **từ tầng `theory/`** (khái niệm dùng chung) để định vị khoảng trống | mục 2.5 |
| A9 | `memory/literature-research-complete.md` được sửa để phản ánh đúng (không còn ghi "hoàn thành" khi thiếu) | đọc lại |
| A10 | `search_log.csv` ghi đủ truy vấn của phiên này | đọc file |

## 4. Cổng đạt

A1–A10 đạt → tick GĐ1 ✅ trong `PROJECT_STATUS.md` + `MEMORY.md` + `task_backlog.md` → sang B9.

## 5. Cập nhật trạng thái

`theory/docs/KILO_STATUS.md` · `00_project_management/WORKFLOW.md` §0 · `PROJECT_STATUS.md` · `MEMORY.md` · `logs/execution_log.md` · `00_project_management/task_backlog.md`
