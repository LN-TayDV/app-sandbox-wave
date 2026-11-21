# PROMPT 03 — B3: SOP TRÍCH XUẤT + VALIDATOR MÁY

> **Đọc trước:** `00-shared-contract.md` · **Điều kiện:** B2 đã qua cổng
> **Bước workflow:** B3 · **Ước lượng:** 1 ngày
> **Mục tiêu:** biến "một chương coi như xong" thành **quy tắc máy kiểm được**, trước khi giao việc cho 4 worker.
> **Cấm:** chưa chạy worker. Chưa trích xuất chương nào.

---

## 1. Vì sao bước này bắt buộc

B5 cần 4 worker chạy song song trên 4 cuốn. Nếu không có định nghĩa *máy kiểm được* về "xong", mỗi worker sẽ tự hiểu một kiểu → registry hỗn loạn → B6 gộp lại nổ → phải làm lại 2–3 tuần.

**Nguyên tắc:** validator phải **bắt được ít nhất 1 lỗi thật** trong registry hiện có. Nếu bắt 0 lỗi → validator chưa đủ mạnh, phải siết lại. Đây là cổng, không phải khuyến nghị.

## 2. Hành động

### 2.1 `theory/docs/EXTRACTION_SOP.md` — hợp đồng hoàn thành 1 chương

**6 điều kiện để một chương là DONE:**
1. **Phủ** — mọi mục trong chương đã vào registry; `coverage` = 100% về mặt *đơn vị nội dung*, không phải về mặt *trang*.
2. **Trích dẫn** — mọi dòng có `book_code`, `printed_page`, `pdf_page`, `global_id`.
3. **Nhãn bằng chứng** — `verification_status` ∈ tập §0.2 của hợp đồng.
4. **Toán học** — mọi phương trình: LaTeX parse được (SymPy) + trạng thái đúng + `formula_ref` trỏ tới định nghĩa.
5. **Validator** — `validate_theory_layer.py` chạy xanh trên registry của chương đó.
6. **Báo cáo chương** — `theory/docs/CHAPTER_REPORT_<BOOK>_<CH>.md` có bảng đối chiếu.

**Bảng `kind` (10 loại + trường bắt buộc):**

| `kind` | Trường bắt buộc |
|---|---|
| `concept` | `definition`, `meaning` (tiếng Việt), `usage` |
| `equation` | `equation_latex`, `symbols` (mỗi ký hiệu: tên, định nghĩa, đơn vị), `verification_status` |
| `assumption` | `statement`, `scope` (điều kiện áp dụng), `role` (giả định/định nghĩa/hẹn) |
| `theorem` | `statement`, `premises`, `conclusion`, `proof_sketch` |
| `caveat` | `statement`, `trigger` (khi nào cảnh báo), `severity` |
| `example` | `setup`, `result`, `numbers` (gắn nhãn `ILLUSTRATIVE` nếu tự tính) |
| `figure` | `caption`, `file` (ảnh crop), `source_page` |
| `table` | `caption`, `data_file`, `source_page` |
| `exercise` | `question`, `answer_available` (CÓ/KHÔNG), `answer` |
| `narrative` | `summary` (diễn giải trung thực, không thêm ý tác giả không nói) |

**Quy trình toán học 3 bậc:**

| Bậc | Nghĩa là | Cách làm | Nhãn kết quả |
|---|---|---|---|
| **A** | Công thức ghi nguyên văn từ sách | copy LaTeX/Unicode từ text layer | `BOOK_EVIDENCE` |
| **B** | Mất vị trí chỉ số hoặc ký hiệu | suy từ text + hình trang | `FORMULA_UNVERIFIED` + ghi chú cách suy |
| **C** | Công thức là ảnh, không đọc được | dùng `scientific/registry.py` render-diff để đối chiếu | `NUMERICALLY_VERIFIED` hoặc `FORMULA_UNVERIFIED` |

**Quy tắc verify bằng render-diff** (tái dùng từ `research/advanced-macroeconomics-fourth-edition/scientific/registry.py`, 374 dòng, 4 lớp source→symbolic→numeric→render):
- Bậc C **bắt buộc** đi qua lớp symbolic → numeric → render, rồi so khớp với ảnh trang.
- Không khớp → `FORMULA_UNVERIFIED`. **Không** tự "sửa cho khớp".

**Mẫu báo cáo chương** — trong file SOP.

### 2.2 `theory/scripts/validate_theory_layer.py` — validator 7 kiểm tra

| # | Kiểm tra | Quy tắc |
|---|---|---|
| 1 | **Schema** | đúng tên cột và đúng thứ tự; `05_equation_registry.csv` = 16 cột, `04_theory_registry.csv` = 19 cột |
| 2 | **`global_id` trùng** | không được trùng trong toàn hệ thống; đúng format `<KIND>-<BOOK>-<NNNN>`; `book_code` ∈ {HAN,ROM,PIN,MAD} |
| 3 | **FK `theory_id`** | mọi `theory_id` trong equation registry phải tồn tại trong theory registry |
| 4 | **Trang** | `printed_page` và `pdf_page` **cùng có hoặc cùng rỗng**; `pdf_page` ≤ `total_pages` của cuốn đó |
| 5 | **Vocabulary** | `verification_status` ∈ tập nhãn §0.2 hợp đồng; `kind` ∈ 10 loại bảng SOP |
| 6 | **LaTeX** | `equation_latex` parse được bằng SymPy (`sympy.parsing.latex` nếu có, nếu không thì parser LaTeX tối giản tự viết) — phải báo dòng lỗi, không crash |
| 7 | **Trạng thái vs độ đầy đủ** | `FORMULA_UNVERIFIED` bắt buộc có `note` giải thích; dòng `VERIFIED` mà thiếu `printed_page` → lỗi |

**Yêu cầu cứng:**
- Chạy được: `python theory/scripts/validate_theory_layer.py --registry <file> --books theory/registry/books.yaml`
- **Exit code ≠ 0 khi có lỗi** (để dùng được làm cổng chặn).
- Xuất JSON kết quả: `logs/registry_validation.json`.
- Không crash với file rỗng, file thiếu cột, LaTeX hỏng.

### 2.3 Nâng validator cũ

```
C:\Users\PC\Documents\AI_project\sandbox-financial\research\advanced-macroeconomics-fourth-edition\scripts\validate_registries.py
```
Hiện **chỉ đếm dòng** → phải trở thành validator 7 kiểm tra ở §2.2 (hoặc gọi chung `theory/scripts/validate_theory_layer.py`).

> **Lưu ý phạm vi:** `research/` là **chỉ đọc**. Nếu chính sách của SOP cấm sửa `research/`, thì **copy** validator về `theory/scripts/` và nâng ở đó; ghi chú trong báo cáo rằng bản gốc trong `research/` không được sửa. Nếu `00-shared-contract.md` cho phép sửa thì sửa bản gốc **và** bản copy — nhưng ưu tiên bản copy.

### 2.4 Chạy validator lên 2 registry hiện có

| File | Số dòng (đã đo) |
|---|---|
| `research/microeconomics-pindyck-rubinfeld/05_equation_registry.csv` | 57 |
| `research/advanced-macroeconomics-fourth-edition/workflows/05_equation_registry.csv` | 29 |
| `research/microeconomics-pindyck-rubinfeld/04_theory_registry.csv` | 32 |
| `research/advanced-macroeconomics-fourth-edition/workflows/04_theory_registry.csv` | 16 |

Ghi kết quả vào `logs/registry_validation.json`.

**Kỳ vọng:** phải phát hiện **≥1 lỗi thật** — ví dụ ID trùng, `printed_page` thiếu, `theory_id` không tồn tại, trang vượt quá `total_pages`, hay LaTeX không parse được. Nếu 0 lỗi → **validator chưa đủ mạnh**, phải siết lại trước khi đi tiếp (đây là điều kiện cổng).

## 3. Acceptance criteria

| # | Tiêu chí | Bằng chứng |
|---|---|---|
| A1 | `theory/docs/EXTRACTION_SOP.md` tồn tại, có đủ: 6 điều kiện DONE · bảng 10 `kind` · quy trình toán học A/B/C · quy tắc render-diff · mẫu báo cáo chương | đọc lại file, đếm mục |
| A2 | `theory/scripts/validate_theory_layer.py` chạy được, có `--help`, exit code ≠ 0 khi lỗi | chạy thử với file lỗi → exit ≠ 0 |
| A3 | Validator chạy trên **cả 4** registry hiện có mà không crash | output |
| A4 | `logs/registry_validation.json` tồn tại | đọc file |
| A5 | **≥1 lỗi thật** được phát hiện, nêu rõ lỗi gì + ở dòng nào | output validator |
| A6 | Validator **không crash** khi: file rỗng · thiếu cột · LaTeX hỏng | 3 lần chạy |
| A7 | Đối chiếu schema: cột của 2 repo khớp nhau, kèm bằng chứng (dump header 2 file) | output lệnh |
| A8 | Không sửa file trong `research/` (trừ khi hợp đồng cho phép, khi đó phải nói rõ) | `git status` |

## 4. Cổng đạt

A1–A8 đạt **và** A5 có ≥1 lỗi thật. Không đạt → BLOCKED, **không** giao việc cho worker.

## 5. Cập nhật trạng thái

`theory/docs/KILO_STATUS.md` · `00_project_management/WORKFLOW.md` §0 · `logs/execution_log.md` · `00_project_management/task_backlog.md`
