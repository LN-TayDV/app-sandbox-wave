# BỘ PROMPT THỰC THI — LUẬN VĂN IFWST / CÁT TRUỒI

Bộ **13 prompt** cho **Kilo Code**, dẫn dắt toàn bộ dự án luận văn: từ probe dữ liệu → trích xuất **hết 4 cuốn sách** vào tầng tri thức dùng chung → dữ liệu thật → ước lượng → viết luận văn.

> **Bộ này tách biệt với `kilo-prompts/`** (bộ dựng app học tập MACRO/MICRO — đã xong, 34/34 + 75/75 + 21/21). Không trộn hai bộ.

---

## 1. Bối cảnh — vì sao cần bộ prompt này

`00_project_management/WORKFLOW.md` đã chốt **13 bước B0–B12**. Nhưng workflow chỉ nói *làm gì*, không nói *làm thế nào cho đúng và cho đo được*. Bộ prompt này là phần "cách làm":

1. **Sửa nguyên nhân gốc trước** — `01` đo được dữ liệu thật trước khi cam kết 3 tuần.
2. **Bằng chứng trước khẳng định** — mọi prompt đều có *acceptance criteria* đo được, không có "làm cho xong".
3. **Trung thực về bằng chứng học thuật** — `FORMULA_UNVERIFIED` phải giữ nguyên nếu chưa đối chiếu.
4. **Trạng thái nằm trong repo** — `theory/docs/KILO_STATUS.md`, không nằm trong chat.
5. **Chặn cổng** — không sang prompt kế tiếp khi cổng hiện tại chưa đạt.

---

## 2. Thứ tự chạy

```
00-shared-contract.md          ← ĐỌC TRƯỚC TẤT CẢ
      │
      ▼
01-data-feasibility-probe.md   B1  probe 7 nguồn dữ liệu ──────────┐
      ▼                                                        │
02-theory-pipeline.md          B2  dựng theory/ + L0/L1/L2         │
      ▼                                                        │  1 ngày
03-sop-validator.md            B3  SOP + validator 7 kiểm tra        │
      ▼                                                        │
04-pilot-hansen.md             B4  pilot Hansen Ch.7  (đo 4 số) ───┘
      ▼
05-extract-book.md             B5  trích HẾT 4 cuốn  ★ 4 WORKER SONG SONG ★
      │
      ▼
06-union-crossbook.md          B6  gộp + cross-book index
      ▼
07-coverage-audit.md           B7  audit coverage toàn bộ
      ▼
────────────── HẾT PHA KỸ THUẬT. KHÔNG XEN KẼ ──────────────
      ▼
08-literature-review.md        B8  GĐ1 tổng quan tài liệu
      ▼
09-model-and-theory.md         B9  GĐ2 + GĐ3 (đối chiếu theory/)
      ▼
10-real-data.md                B10 GĐ4 dữ liệu thật (sửa D1–D9)
      ▼
11-estimation.md               B11 GĐ5 thực nghiệm (code/13–16)
      ▼
12-thesis-writing.md           B12 GĐ6 + GĐ7 luận văn + kiểm định
```

Chi tiết dependency, phạm vi, baseline đã đo, cổng chặn: **[EXECUTION-MATRIX.md](EXECUTION-MATRIX.md)**

---

## 3. Danh sách file

| File | Vai trò | Bước |
|---|---|---|
| **[00-shared-contract.md](00-shared-contract.md)** | Hợp đồng thực thi: đường dẫn tuyệt đối, nhãn bằng chứng, quy trình 5 bước, mẫu báo cáo, quy tắc registry | — |
| **[01-data-feasibility-probe.md](01-data-feasibility-probe.md)** | Probe 7 nguồn, chốt lõi dữ liệu, tính công suất thống kê | B1 |
| **[02-theory-pipeline.md](02-theory-pipeline.md)** | Dựng `theory/`, script L0/L1/L2, xử lý mâu thuẫn 787 vs 761 của PIN | B2 |
| **[03-sop-validator.md](03-sop-validator.md)** | SOP 6 điều kiện DONE, 10 loại `kind`, bậc A/B/C, validator 7 kiểm tra | B3 |
| **[04-pilot-hansen.md](04-pilot-hansen.md)** | Pilot 1 chương, đo 4 con số M1–M4, quyết định mở rộng | B4 |
| **[05-extract-book.md](05-extract-book.md)** | Trích 1 cuốn (dùng chung cho 4 worker) | B5 |
| **[06-union-crossbook.md](06-union-crossbook.md)** | Gộp 4 registry + 2 registry sẵn có, cross-book index, FTS5 | B6 |
| **[07-coverage-audit.md](07-coverage-audit.md)** | Đối chiếu chương với TOC, đếm theo `kind`, kiểm 3 mức sót | B7 |
| **[08-literature-review.md](08-literature-review.md)** | Đóng GĐ1: ma trận, critical review, research gap | B8 |
| **[09-model-and-theory.md](09-model-and-theory.md)** | Đóng GĐ2+GĐ3 bằng cách gắn mọi claim vào `global_id` | B9 |
| **[10-real-data.md](10-real-data.md)** | Đóng GĐ4: sửa 9 lỗi D1–D9, tầng truy vết, `code/08`–`12` | B10 |
| **[11-estimation.md](11-estimation.md)** | Đóng GĐ5: `code/13`–`16`, H1–H5, 6 kiểm tra độ bền | B11 |
| **[12-thesis-writing.md](12-thesis-writing.md)** | Đóng GĐ6+GĐ7: 11 file luận văn + 8 kiểm tra cuối | B12 |
| **[EXECUTION-MATRIX.md](EXECUTION-MATRIX.md)** | Dependency · baseline đã đo · cổng chặn · xử lý vướng | — |
| **[ACCEPTANCE-CHECKLIST.md](ACCEPTANCE-CHECKLIST.md)** | Checklist nghiệm thu tổng hợp (8 nhóm) | — |

---

## 4. Bốn cuốn sách

| Mã | Sách | PDF (bất biến) | Trạng thái L0 |
|---|---|---|---|
| `HAN` | Hansen, *Econometrics* (2014) | `data/book/econometrics-bruce-hansen-2014.pdf` | ❌ chưa trích xuất |
| `ROM` | Romer, *Advanced Macroeconomics* 4e | `data/book/b81821bd16a42211f919748c26cd0774.pdf` | ✅ 738/738 trang |
| `PIN` | Pindyck & Rubinfeld, *Microeconomics* Global Ed. 2017 | `data/book/Robert S Pindyck_ Daniel L Rubinfeld - Microeconomics, Global Edition (2017, Pearson Education Limited) - libgen.li.pdf` | ✅ 787/787 trang ⚠️ `coverage.json` ghi 761 |
| `MAD` | Madura, *International Financial Management* 11e | `data/book/international-financial-management-11th-edition-by-jeff-madura.pdf` | ❌ chưa trích xuất |

---

## 5. CÁCH CHẠY (hướng dẫn từng bước)

> **Đường dẫn tuyệt đối.** Các prompt dưới đây dán sẵn đường dẫn đầy đủ — copy nguyên văn, đừng tự dò hay rút gọn.

### 5.0. Chuẩn bị (một lần)

1. Mở Kilo Code tại workspace: `C:\Users\PC\Documents\AI_project\sandbox-financial`
2. Bảo đảm `python` chạy được trong terminal của Kilo (cần `pymupdf`, `sympy`; SQLite FTS5 là stdlib):

```powershell
python -c "import fitz, sympy; print(fitz.__doc__); print(sympy.__version__)"
```

3. Kiểm tra quyền ghi:
```powershell
Test-Path "C:\Users\PC\Documents\AI_project\sandbox-financial\theory"
```
→ `False` là đúng (sẽ tạo ở B2).

### 5.1. Prompt đầu tiên — B1 (probe dữ liệu)

```
Bạn là Kilo Code. Đọc trước file hợp đồng:
C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts-theory\00-shared-contract.md

Sau đó làm prompt:
C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts-theory\01-data-feasibility-probe.md

Đọc thêm để biết bối cảnh (không sửa):
C:\Users\PC\Documents\AI_project\sandbox-financial\00_project_management\WORKFLOW.md
C:\Users\PC\Documents\AI_project\sandbox-financial\04_data\IFWST_Data_Collection_Strategy.md

Báo cáo theo mẫu §0.4 của hợp đồng.
```

### 5.2. Prompt thứ N (N = 02 … 12) — làm tuần tự

```
Bạn là Kilo Code. Đọc lại hợp đồng:
C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts-theory\00-shared-contract.md

Làm prompt N:
C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts-theory\<TÊN-FILE-Prompt-N>.md

Báo cáo theo mẫu §0.4 của hợp đồng.
```

Bảng tra tên file theo N:

| N | Tên file |
|---|---|
| 02 | `02-theory-pipeline.md` |
| 03 | `03-sop-validator.md` |
| 04 | `04-pilot-hansen.md` |
| 05 | `05-extract-book.md` |
| 06 | `06-union-crossbook.md` |
| 07 | `07-coverage-audit.md` |
| 08 | `08-literature-review.md` |
| 09 | `09-model-and-theory.md` |
| 10 | `10-real-data.md` |
| 11 | `11-estimation.md` |
| 12 | `12-thesis-writing.md` |

### 5.3. B5 — chạy 4 worker SONG SONG (điểm khác biệt lớn nhất)

Ở B5, mở **4 phiên Kilo riêng biệt** (4 tab / 4 worktree), mỗi phiên một cuốn. **Không** cho 2 worker cùng một cuốn.

Phiên A — `HAN`:
```
Bạn là Kilo Code. Đọc hợp đồng:
C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts-theory\00-shared-contract.md
Đọc SOP + validator:
C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts-theory\03-sop-validator.md
Đọc kết quả pilot:
C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts-theory\04-pilot-hansen.md

Làm prompt 05 với:
BOOK_CODE = HAN
BOOK_TITLE = Bruce Hansen, Econometrics, 2014

Báo cáo theo mẫu §0.4 của hợp đồng.
```

Phiên B — `ROM` (thay `HAN` → `ROM`, tiêu đề → `David Romer, Advanced Macroeconomics, 4th edition`)
Phiên C — `PIN` (thay `HAN` → `PIN`, tiêu đề → `Pindyck & Rubinfeld, Microeconomics, Global Edition 2017`)
Phiên D — `MAD` (thay `HAN` → `MAD`, tiêu đề → `Jeff Madura, International Financial Management, 11th edition`)

**Gộp ý tưởng cho 4 phiên:** dùng **Agent Manager → worktree mode** của Kilo, mỗi task một worktree riêng để không đụng file của nhau. Nếu không, chạy 4 phiên tuần tự vẫn được — chậm hơn nhưng an toàn hơn.

### 5.4. Tiếp tục sau khi bị gián đoạn

```
Bạn là Kilo Code. Bị gián đoạn giữa chừng — hãy khôi phục công việc.

Đọc file trạng thái:
C:\Users\PC\Documents\AI_project\sandbox-financial\theory\docs\KILO_STATUS.md

Đối chiếu với bảng trạng thái §0 của:
C:\Users\PC\Documents\AI_project\sandbox-financial\00_project_management\WORKFLOW.md

Chạy lại lệnh kiểm chứng ghi trong KILO_STATUS.md để xác nhận thực tế,
rồi tiếp tục đúng phần đang dở. Không làm lại phần đã xong.
```

### 5.5. Kiểm tra cổng chặn trước khi làm prompt kế tiếp

```
Bạn là Kilo Code. Trước khi làm prompt N, hãy kiểm tra cổng chặn G(N-1) theo:
C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts-theory\EXECUTION-MATRIX.md

Cũng đọc trạng thái hiện tại ở theory\docs\KILO_STATUS.md.
Nếu cổng trước chưa đạt, báo lại và sửa nốt cổng trước — đừng làm tiếp trên nền chưa vững.
```

### 5.6. Nghiệm thu cuối

```
Bạn là Kilo Code. Đối chiếu toàn bộ công việc với checklist nghiệm thu:
C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts-theory\ACCEPTANCE-CHECKLIST.md

Đánh dấu từng mục, đính kèm bằng chứng, và nêu rõ mục nào chưa đạt.
```

---

## 6. Quy tắc vàng

1. **Sửa gốc, không vá triệu chứng.** Sửa generator + rebuild > sửa tay file sinh ra.
2. **Bằng chứng trước khẳng định.** Không có output lệnh → không được kết luận.
3. **Trung thực về bằng chứng học thuật.** Hạ trạng thái bằng chứng còn đúng hơn nâng cho đẹp.
4. **Trạng thái nằm trong repo.** `theory/docs/KILO_STATUS.md` — không nằm trong chat.
5. **Chặn cổng.** Không sang prompt kế tiếp khi cổng hiện tại chưa đạt.
6. **Báo cáo trung thực.** Mục `BLOCKED` nêu rõ hơn là làm vờ cho xong.
7. **Đo, đừng ước lượng.** Trang, dòng, tỉ lệ — phải chạy lệnh đếm.

---

## 7. Những gì bộ này **không** làm

- ❌ Không sửa `research/microeconomics-pindyck-rubinfeld/` hay `research/advanced-macroeconomics-fourth-edition/` (chỉ đọc, tái dùng script)
- ❌ Không sửa / move / ghi đè `data/book/` hay `tasks/init-task.md`
- ❌ Không dựng lại app học tập MACRO/MICRO (đã xong, nằm ở bộ `kilo-prompts/`)
- ❌ Không triển khai hệ thống, database, API — đây là dự án **luận văn học thuật**
- ❌ Không trộn dữ liệu/thuật ngữ giữa 4 cuốn sách — mỗi cuốn giữ `book_code` riêng

Nếu Kilo phát hiện ngoài phạm vi → ghi vào **"RỦI RO CÒN LẠI"** trong báo cáo, **không** sửa ngầm.
