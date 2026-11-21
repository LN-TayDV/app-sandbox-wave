# PROMPT 00 — HỢP ĐỒNG THỰC THI (LUẬN VĂN IFWST / CÁT TRUỒI)

> **Cách dùng:** đọc file này **trước mọi prompt khác**. Không bỏ qua bước nào.
> **Thứ tự:** `00` → `01` → `02` → … theo [`README.md`](README.md). Chạy **một prompt mỗi phiên**.
> **Bộ này tách biệt hoàn toàn** với bộ `kilo-prompts/` (dựng app học tập MACRO/MICRO — đã xong).

---

## 0.0. ĐƯỜNG DẪN TUYẤT ĐỐI (dán nguyên văn, đừng tự dò)

**Thư mục gốc dự án:**
```
C:\Users\PC\Documents\AI_project\sandbox-financial
```

**Thư mục chứa prompt (bộ này):**
```
C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts-theory
```

**File trạng thái (đọc khi mở phiên mới, cập nhật sau mỗi prompt):**
```
C:\Users\PC\Documents\AI_project\sandbox-financial\theory\docs\KILO_STATUS.md
```

**Workflow chuẩn (nguồn sự thật về thứ tự và cổng đạt):**
```
C:\Users\PC\Documents\AI_project\sandbox-financial\00_project_management\WORKFLOW.md
```

**Ma trận thực thi (dependency, phạm vi, baseline, cổng chặn):**
```
C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts-theory\EXECUTION-MATRIX.md
```

**PDF nguồn — BẤT BIẾN, KHÔNG ĐƯỢC SỬA / DI CHUYỂN / GHI ĐÈ:**
```
C:\Users\PC\Documents\AI_project\sandbox-financial\data\book\econometrics-bruce-hansen-2014.pdf
C:\Users\PC\Documents\AI_project\sandbox-financial\data\book\b81821bd16a42211f919748c26cd0774.pdf
C:\Users\PC\Documents\AI_project\sandbox-financial\data\book\Robert S Pindyck_ Daniel L Rubinfeld - Microeconomics, Global Edition (2017, Pearson Education Limited) - libgen.li.pdf
C:\Users\PC\Documents\AI_project\sandbox-financial\data\book\international-financial-management-11th-edition-by-jeff-madura.pdf
```

**Hai repo `research/` — CHỈ ĐỌC, KHÔNG SỬA:**
```
C:\Users\PC\Documents\AI_project\sandbox-financial\research\advanced-macroeconomics-fourth-edition
C:\Users\PC\Documents\AI_project\sandbox-financial\research\microeconomics-pindyck-rubinfeld
```
Được phép **copy script** từ đó sang `theory/scripts/` rồi sửa bản copy. **Cấm** ghi bất kỳ thứ gì vào `research/`.

**Bộ 4 sách (mã dùng xuyên suốt):**

| Mã | Sách | Tác giả / ấn bản | PDF |
|---|---|---|---|
| `HAN` | *Econometrics* | Bruce Hansen, 2014 | `econometrics-bruce-hansen-2014.pdf` |
| `ROM` | *Advanced Macroeconomics*, 4e | David Romer, 2012/2019 | `b81821bd16a42211f919748c26cd0774.pdf` (738 trang) |
| `PIN` | *Microeconomics*, Global Edition 2017 | Pindyck & Rubinfeld | `Robert S Pindyck_...libgen.li.pdf` (787 trang) |
| `MAD` | *International Financial Management*, 11e | Jeff Madura | `international-financial-management-11th-edition-by-jeff-madura.pdf` |

---

## 0.1. Bối cảnh và mục tiêu

Đây là dự án **luận văn học thuật**, không phải dự án phần mềm. Mục tiêu:

> **IFWST — International Financial Wave–Sandpile Theory (Cát Truồi).** Dùng 4 cuốn sách làm **nền toán học – lý thuyết dùng chung**, xây dựng mô hình lan truyền sóng + tích lũy tích cát ở hệ thống tài chính quốc tế, ước lượng trên panel quốc gia, và viết luận văn.

**Cấu trúc 13 bước (B0–B12) đã chốt:**

```
B0 ✅ đồng bộ repo
  → B1 probe dữ liệu → B2 dựng theory/ → B3 SOP+validator → B4 pilot Hansen
  → B5 trích xuất HẾT 4 cuốn → B6 union+cross-book → B7 audit coverage
  → B8 GĐ1 tổng quan tài liệu → B9 GĐ2+GĐ3 → B10 GĐ4 dữ liệu thật
  → B11 GĐ5 thực nghiệm → B12 GĐ6+GĐ7 luận văn
```

**Hai pha không được xen kẽ:**
- **Pha kỹ thuật (B1–B7):** trích xuất tri thức. Xong trước.
- **Pha học thuật (B8–B12):** nghiên cứu, dữ liệu, ước lượng, viết luận văn.

> **Cấm tuyệt đối:** viết luận văn khi pha kỹ thuật chưa xong; chạy tải dữ liệu toàn bộ khi mới ở B1; trích xuất chương 2+ của bất kỳ cuốn nào trước khi B4 đạt cổng.

---

## 0.2. Quy tắc bằng chứng học thuật

Mọi khẳng định học thuật phải mang nhãn trạng thái bằng chứng. **Không tự chế nhãn mới.** Dùng đúng tập nhãn đã có trong repo:

`BOOK_EVIDENCE` · `PRIMARY_SOURCE` · `SECONDARY_SOURCE` · `DERIVED_RESULT` · `RESEARCH_HYPOTHESIS` · `RESEARCH_SYNTHESIS` · `UNVERIFIED` · `SOURCE_GAP`

Và cho phương trình: `FORMULA_VERIFIED` / `FORMULA_UNVERIFIED` / `NUMERICALLY_VERIFIED` / `ILLUSTRATIVE`.

- **Cấm** tự sáng tác nội dung rồi trình bày như của tác giả sách.
- **Cấm** nâng trạng thái bằng chứng "cho đẹp". `FORMULA_UNVERIFIED` phải giữ nguyên nếu chưa đối chiếu.
- Số liệu minh họa gắn nhãn `ILLUSTRATIVE`.
- **Cấm** đưa phương trình chưa đủ bằng chứng vào `data/` hay registry "chính" (xem `PT-10-01` của MACRO — ví dụ bắt buộc giữ `FORMULA_UNVERIFIED`).
- Phân biệt rõ **trang in** (`printed_page`) và **trang PDF** (`pdf_page`). Không đoán — suy ra từ `page_map`, ghi rõ là suy ra.
- Nguồn thứ cấp (paper, web) ghi `SECONDARY_SOURCE`; sách ghi `BOOK_EVIDENCE`; tài liệu gốc (IMF, BIS, paper gốc) ghi `PRIMARY_SOURCE`.

---

## 0.3. Quy trình bắt buộc cho MỌI prompt

**Bước 1 — Xác minh hiện trạng (verify before edit).**
Đọc đúng file được nêu. Nếu đường dẫn trong prompt không tồn tại: **đừng đoán** — tìm bằng `ls`/`grep`, ghi sai lệch vào báo cáo, rồi dùng đường dẫn đúng tìm được. Không tìm ra → `BLOCKED` cho phần đó.

**Bước 2 — Làm.**
Đúng phạm vi prompt nêu. Không refactor file không liên quan. Không xóa file. Không đổi công nghệ.

**Bước 3 — Chạy lệnh kiểm chứng.**
Chạy **đúng lệnh** prompt nêu. Dán output thật, không tóm tắt suông.

**Bước 4 — Đối chiếu acceptance criteria.**
Từng tiêu chí phải có bằng chứng quan sát được (lệnh đã chạy + output, hoặc con số đo).

**Bước 5 — Báo cáo + cập nhật trạng thái.**
Dùng mẫu §0.5. Cập nhật `theory/docs/KILO_STATUS.md` và bảng trạng thái §0 trong `00_project_management/WORKFLOW.md`.

---

## 0.4. Cấu trúc báo cáo (bắt buộc)

```
## BÁO CÁO — <TÊN PROMPT> (B<bước>)

### ĐÃ LÀM
- <file:line hoặc đường dẫn> — <thay đổi cụ thể> — <bằng chứng: lệnh + output>

### ĐÃ KIỂM CHỨNG
- Acceptance criterion: <tiêu chí> → <PASS/FAIL> — <bằng chứng>

### CHƯA LÀM / BLOCKED
- <mục> — <lý do cụ thể> — <cần gì để mở>

### FILE ĐÃ SỬA / ĐÃ TẠO
<danh sách đường dẫn, mỗi dòng một file>

### RỦI RO CÒN LẠI
- <rủi ro cụ thể>
```

**Cấm** báo `PASS` khi chưa chạy lệnh kiểm chứng. **Cấm** ghi "đã hoàn thành" khi còn mục BLOCKED mà không nêu rõ.

---

## 0.5. Điều kiện DONE / BLOCKED

**DONE** — đồng thời thỏa:
1. Tất cả acceptance criteria của prompt đạt.
2. Lệnh kiểm chứng nêu trong prompt chạy thành công, output được dán vào báo cáo.
3. Không còn mục nào trong "CHƯA LÀM / BLOCKED" trừ khi prompt đã dự định là ngoài phạm vi.
4. Không phá vỡ thứ đang xanh.

**BLOCKED** — dừng phần đó, ghi lý do cụ thể, đề xuất cách gỡ, **tiếp tục các phần độc lập**:
- Nguồn dữ liệu / PDF / chunk / registry không tồn tại hoặc mâu thuẫn.
- Cần quyết định học thuật mà prompt không đủ thông tin.
- Cần ghi vào `research/` (vi phạm §0.0) → chuyển sang `theory/` và ghi chú.
- Lệnh kiểm chứng đỏ trước khi sửa vì lý do không liên quan → ghi lại baseline đỏ.

**Không bao giờ** tự bỏ một acceptance criterion mà không nói. Criterion không đạt = chưa DONE.

---

## 0.6. Quy tắc phạm vi sửa

- Sửa **đúng** phạm vi prompt nêu. Lỗi ngoài phạm vi → ghi vào "RỦI RO CÒN LẪI", **không sửa ngầm**.
- **Cấm** sửa/move/xóa file trong `data/book/`, `tasks/init-task.md`, `research/`.
- **Cấm** tạo registry thứ hai cạnh tranh với registry hiện có. Registry là **nguồn duy nhất** cho phương trình được trích dẫn.
- **Cấm** sửa file sinh tự động mà không sửa generator. Sửa generator + rebuild > vá tay file sinh ra.
- **Cấm** chạy lại OCR/extraction trên artifact đã verify, trừ khi có lý do cụ thể ghi trong báo cáo.
- Identifier (biến, hàm, file) tiếng Anh; nội dung hiển thị và comment tiếng Việt.
- File UTF-8 **không BOM**. Ghi xong phải đọc lại để xác nhận không mojibake.
- Comment tiếng Việt, giữ phong cách code hiện có.

---

## 0.7. Quy ước registry bắt buộc

Mọi registry dùng **cùng bộ cột** đã có trong repo (đã kiểm chứng 2 cuốn trùng khớp):

- `05_equation_registry.csv` — **16 cột**
- `04_theory_registry.csv` — **19 cột** (có sẵn `thesis_relevance`)

Mỗi dòng registry mới **phải** có:
- `book_code` ∈ {`HAN`, `ROM`, `PIN`, `MAD`}
- `global_id` — định dạng `EQ-HAN-0001` / `TH-HAN-0001` / `AS-HAN-0001` … (`<KIND>-<BOOK>-<NNNN>`), **duy nhất toàn hệ thống**
- ID cũ (nếu có) giữ nguyên ở cột `id` — không phá vỡ tham chiếu cũ
- `printed_page` **và** `pdf_page`: cùng có, hoặc cùng rỗng (không một có một không)
- `verification_status` ∈ tập nhãn §0.2

Số liệu đo được trước khi bắt đầu:
- MACRO: `05_equation_registry.csv` 16 cột / 29 dòng · `04_theory_registry.csv` 19 cột / 16 dòng
- MICRO: `05_equation_registry.csv` 16 cột / 57 dòng · `04_theory_registry.csv` 19 cột / 32 dòng

---

## 0.8. Nguyên tắc "bằng chứng trước khẳng định"

- Không có output lệnh → không được kết luận.
- Số trang, số dòng, tỉ lệ — phải chạy lệnh đếm, không ước lượng rồi ghi như số thật.
- Nếu chưa đo được thì ghi `CHƯA ĐO`, không ghi con số.
- Cổng = điều kiện đo được. Qua cổng = có số.

---

## 0.9. Chốt chặn cuối (khi kết thúc toàn bộ bộ)

Chạy lại toàn bộ lệnh kiểm chứng của mọi prompt đã chạy, dán output thật, đối chiếu
`ACCEPTANCE-CHECKLIST.md`. Bất kỳ lệnh nào đỏ → không được báo DONE ở cấp tổng thể.
