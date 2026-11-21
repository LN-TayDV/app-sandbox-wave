# PROMPT 00 — EXECUTION CONTRACT (DÙNG CHUNG CHO CẢ HAI REPO)

> **Cách dùng:** Prompt này là **hợp đồng thực thi** áp dụng cho mọi prompt còn lại. Kilo phải đọc và tuân thủ nó trước khi bắt đầu bất kỳ prompt nào khác.
> **Thứ tự:** chạy `00` → `01` → `02` → … theo thứ tự trong `README.md`. Không bỏ qua, không chạy song song hai prompt cùng lúc trên cùng một repo.

---

## 0.0. ĐƯỜNG DẪN TUYỆT ĐỐI (dán nguyên văn, không tự dò)

**Repo `MACRO`** — David Romer, *Advanced Macroeconomics*, 4e:
```
C:\Users\PC\Documents\AI_project\sandbox-financial\research\advanced-macroeconomics-fourth-edition
```

**Repo `MICRO`** — Pindyck & Rubinfeld, *Microeconomics*, Global Edition 2017:
```
C:\Users\PC\Documents\AI_project\sandbox-financial\research\microeconomics-pindyck-rubinfeld
```

**Thư mục chứa prompt:**
```
C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts
```

**File trạng thái (đọc khi bắt đầu phiên mới, cập nhật sau mỗi prompt):**
```
C:\Users\PC\Documents\AI_project\sandbox-financial\research\advanced-macroeconomics-fourth-edition\docs\KILO_STATUS.md
C:\Users\PC\Documents\AI_project\sandbox-financial\research\microeconomics-pindyck-rubinfeld\docs\KILO_STATUS.md
```

**Ma trận thực thi (dependency, phạm vi, baseline, cổng chặn):**
```
C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts\EXECUTION-MATRIX.md
```

---

## 0.1. Bối cảnh

Hai hệ thống học tập tương tác dựa trên sách giáo khoa, nằm trong cùng workspace:

| Mã | Sách | Workspace | Bản dựng web |
|---|---|---|---|
| `MACRO` | David Romer, *Advanced Macroeconomics*, 4e | `C:\Users\PC\Documents\AI_project\sandbox-financial\research\advanced-macroeconomics-fourth-edition` | `web/` → `dist-web/` |
| `MICRO` | Pindyck & Rubinfeld, *Microeconomics*, Global Edition 2017 | `C:\Users\PC\Documents\AI_project\sandbox-financial\research\microeconomics-pindyck-rubinfeld` | `web/` → `dist/` |

**Quy tắc bất di bất dịch:** hai repo độc lập hoàn toàn. Không trộn dữ liệu, nội dung, số liệu, thuật ngữ hay bảng biểu của hai cuốn sách. Không tạo registry chung. Không trích dẫn Romer trong dự án Pindyck hay ngược lại.

Nếu một prompt yêu cầu sửa `MACRO`, **chỉ sửa trong `MACRO`**. Nếu yêu cầu sửa `MICRO`, chỉ sửa trong `MICRO`.

---

## 0.2. Nguyên tắc bằng chứng (áp dụng cho MỌI nội dung học thuật)

Mọi khẳng định học thuật phải mang nhãn trạng thái bằng chứng đã có trong repo. **Không tự chế nhãn mới.** Dùng đúng tập nhãn đang tồn tại trong repo (ví dụ `MICRO`: `VERIFIED` / `TÍNH TAY` / `CHƯA ĐỐI CHIẾU ẢNH` / `SUY RA` / `CHƯA NHẤT QUÁN`; `MACRO`: `BOOK_EVIDENCE_VERIFIED` / `DERIVED_VERIFIED` / `NUMERICALLY_VERIFIED` / `FORMULA_UNVERIFIED` / `UNVERIFIED` / `ILLUSTRATIVE` / `DOMAIN_GAP`).

- **Không** tự tạo nội dung để lấp chỗ trống rồi trình bày như thể tác giả sách đã viết.
- **Không** nâng trạng thái bằng chứng để "cho đẹp". Trạng thái `FORMULA_UNVERIFIED` phải giữ nguyên nếu chưa đối chiếu (xem `MACRO` — `PT-10-01` là ví dụ bắt buộc giữ).
- Khi một giá trị **suy ra** từ phương trình đã xác minh, ghi rõ là suy ra.
- Số liệu ví dụ minh họa phải gắn nhãn `ILLUSTRATIVE` (hoặc tương đương theo quy ước repo), không được trình bày như số liệu trong sách.
- Nội dung UI (nhãn nút, hướng dẫn) là **tiếng Việt, không dấu-có-đúng**. Nội dung học thuật là tiếng Việt đầy đủ.

---

## 0.3. Quy trình bắt buộc cho MỌI prompt

Mỗi prompt trong bộ này có cấu trúc thống nhất. Kilo phải thực hiện theo đúng 5 bước:

**Bước 1 — Xác minh hiện trạng (Verify before edit).**
Trước khi sửa bất kỳ dòng nào, đọc đúng file được nêu trong prompt. Nếu prompt nêu một đường dẫn mà thực tế không tồn tại, **đừng đoán** — hãy tìm đường dẫn đúng bằng `ls`/`grep`, ghi nhận sai lệch vào báo cáo, rồi tiếp tục với đường dẫn đúng tìm được. Nếu không tìm ra, dừng và báo `BLOCKED` cho phần đó.

**Bước 2 — Sửa code.**
Sửa đúng phạm vi prompt nêu. Không refactor tới các file không liên quan. Không xóa file. Không đổi công nghệ.

**Bước 3 — Chạy test.**
Chạy đúng lệnh test mà prompt nêu. Ghi lại output thật (không tóm tắt suông).

**Bước 4 — Kiểm tra acceptance criteria.**
Đối chiếu từng tiêu chí của prompt. Mỗi tiêu chí phải có bằng chứng quan sát được (lệnh đã chạy + output, hoặc số đo).

**Bước 5 — Báo cáo.**
Dùng đúng mẫu ở §0.6.

---

## 0.4. Cấu trúc báo cáo (bắt buộc cho mọi prompt)

Kilo trả về **đúng** khối Markdown sau, không thêm bài luận:

```
## BÁO CÁO — <TÊN PROMPT> (<MÃ REPO>)

### ĐÃ LÀM
- <file:line> — <thay đổi cụ thể> — <bằng chứng: lệnh + output>

### ĐÃ KIỂM CHỨNG
- Acceptance criterion: <tiêu chí> → <PASS/FAIL> — <bằng chứng>

### CHƯA LÀM / BLOCKED
- <mục> — <lý do cụ thể> — <cần gì để mở>

### FILE ĐÃ SỬA
<danh sách đường dẫn, mỗi dòng một file>

### RỦI RO CÒN LẠI
- <rủi ro cụ thể, không suông>
```

**Cấm** báo cáo `PASS` khi chưa chạy lệnh kiểm chứng. **Cấm** ghi "đã hoàn thành" khi có mục BLOCKED mà không nêu rõ.

---

## 0.5. Điều kiện DONE / BLOCKED

**DONE** — chỉ khi đồng thời thỏa:
1. Tất cả acceptance criteria của prompt đạt.
2. Lệnh test nêu trong prompt chạy thành công, output được dán vào báo cáo.
3. Không còn mục nào trong "CHƯA LÀM / BLOCKED" **trừ khi** mục đó đã được prompt dự định trước là ngoài phạm vi.
4. Không phá vỡ test đang xanh (nếu có test xanh trước khi sửa, nó phải xanh sau khi sửa).

**BLOCKED** — khi gặp một trong các trường hợp sau. Kilo phải **dừng phần đó**, ghi lý do cụ thể, đề xuất cách gỡ, và **tiếp tục các phần còn lại** của prompt nếu độc lập:
- Dữ liệu nguồn (PDF/chunk/registry) không tồn tại hoặc mâu thuẫn với nhau.
- Cần quyết định học thuật mà prompt không đủ thông tin để quyết.
- Cần sửa ở repo khác (vi phạm §0.1).
- Test gốc đã đỏ trước khi sửa vì lý do không liên quan — phải ghi lại baseline đỏ này.

**Không bao giờ** tự bỏ một acceptance criterion mà không nói. Criterion không đạt = chưa DONE.

---

## 0.6. Quy tắc phạm vi sửa

- Sửa **đúng** file trong phạm vi prompt. Nếu phát hiện lỗi ngoài phạm vi: **ghi vào "RỦI RO CÒN LẠI"**, không sửa ngầm.
- Không xóa dữ liệu nghiên cứu (`data/`, `extracted/`, `04_catalogs/`, `registry` CSV, `03_chapter_analyses/`).
- Không tạo registry thứ hai cạnh tranh với registry hiện có.
- Không sửa file sinh tự động mà không sửa generator tương ứng. Nếu prompt yêu cầu sửa dữ liệu sinh ra, phải sửa `scripts/build_*.py` để lần build sau tái tạo đúng.
- Ưu tiên sửa generator + rebuild hơn là vá file sinh ra bằng tay.
- Comment tiếng Việt, giữ đúng phong cách code hiện có của file (thụt lề, tên biến, ngôn ngữ).

---

## 0.7. Quy ước mã nguồn chung

- Tiếng Anh cho identifier (biến, hàm, component, file). Tiếng Việt cho nội dung hiển thị và comment.
- Không để lộ `console.log` debug trong code bàn giao.
- Mọi giá trị số hiển thị cho người học phải là **số hữu hạn**. Dùng `Number.isFinite()` trước khi render; nếu không hữu hạn hiển thị `—` (không phải chuỗi `undefined`).
- Mọi fetch dữ liệu phải kiểm tra `res.ok` **trước** khi `res.json()`, và phải bắt lỗi để hiển thị thông báo cho người dùng thay vì trang trắng.
- Encoding: file nguồn phải là **UTF-8 không BOM**. Nếu phát hiện mojibake (`Ã¡`, `á»`, `â€`, `Ä`...), sửa tại nguồn và xác minh bằng cách đọc lại file sau khi ghi.

---

## 0.8. Chốt chặn cuối (áp dụng khi kết thúc toàn bộ bộ prompt)

Trước khi báo cáo tổng kết, Kilo phải chạy lại toàn bộ lệnh kiểm thử của **cả hai repo** và dán output thật:

```bash
# MACRO
cd "C:\Users\PC\Documents\AI_project\sandbox-financial\research\advanced-macroeconomics-fourth-edition"
npm --prefix web run typecheck
npm --prefix web run test
npm --prefix web run build
python scripts/validate_app_data.py

# MICRO
cd "C:\Users\PC\Documents\AI_project\sandbox-financial\research\microeconomics-pindyck-rubinfeld"
npm --prefix web run typecheck
python -m pytest tests -q
node --test "tests/*.test.mjs"
npm --prefix web run build
python scripts/validate_html.py
```

Bất kỳ lệnh nào thất bại → không được báo cáo DONE ở cấp tổng thể. Liệt kê lệnh đỏ, output, và trạng thái.
