# BỘ PROMPT THỰC THI CHO KILO CODE

> ### ⚠️ Bộ này dành cho app học tập MACRO/MICRO — **đã hoàn thành** (34/34 browser smoke · 75/75 pytest · 21/21 node).
>
> **Bộ prompt cho dự án luận văn IFWST / Cát Truồi nằm ở thư mục khác:**
> → **[`../kilo-prompts-theory/README.md`](../kilo-prompts-theory/README.md)** — 13 prompt, B1–B12 (probe dữ liệu → trích xuất 4 cuốn sách → dữ liệu → ước lượng → luận văn).
>
> Hai bộ **không trộn**: bộ này dựng app web dạy-học; bộ kia phục vụ luận văn học thuật.

Bộ 10 prompt viết lại cho **Kilo Code**, xử lý **hai hệ thống học tập tương tác** độc lập:
Advanced Macroeconomics (Romer 4e) và Microeconomics (Pindyck & Rubinfeld, Global Edition 2017).

---

## 1. Vấn đề gốc mà bộ này giải quyết

Prompt cũ **không hỏng vì thiếu chi tiết** — chúng hỏng vì coi ứng dụng là đã xong khi thực tế tầng dữ liệu dưới cùng **chưa bao giờ chạy được**:

- `MACRO` build **thành công** nhưng mọi trang dữ liệu rỗng, console báo `SyntaxError`, và 5 file view hiển thị mojibake (114 dòng trong `web/src/`).
- `MICRO` trang phương trình rỗng, mọi chương báo *"chưa có bài tập tự kiểm tra"* trong khi quảng bá 163 bài, và **12 file JSON chứa toàn bộ nội dung chương chưa hề được import ở bất kỳ đâu**.

Nguyên nhân: prompt cũ kiểm tra *"file tồn tại"*, *"build không lỗi"*, *"test pass"* — nhưng **không kiểm tra ứng dụng có thực sự tải được dữ liệu và hiển thị nội dung không**.

Bộ prompt này chuyển trọng tâm sang:
1. **Sửa nguyên nhân gốc trước** (prompt 01) — không vá triệu chứng.
2. **Bắt lỗi bằng test runtime** (prompt 08) — không chỉ test cấu trúc dữ liệu.
3. **Trung thực về bằng chứng học thuật** (prompt 04) — nhãn `CHƯA ĐỐI CHIẾU` hợp lệ hơn `VERIFIED` bịa.
4. **Ghi trạng thái vào repo** (prompt 09) — để không mất tiến độ khi bị gián đoạn.

---

## 2. Thứ tự chạy

```
00-shared-contract.md        ← ĐỌC TRƯỚC TẤT CẢ
      │
      ▼
01-root-cause-recovery.md    ← P0. CHẠY ĐẦU TIÊN, MỘT MÌNH
      │
      ├──► 02-data-pipeline.md
      │        └──► 04-academic-content.md
      └──► 03-vue-router-state.md
                  │
                  └─────────────────┐
                                    ▼
              05-latex-tables-charts-labs.md
                                    │
                                    ▼
                 06-ui-ux.md
                                    │
                                    ▼
              07-integration-i18n.md
                                    │
                                    ▼
              08-e2e-regression.md
                                    │
                                    ▼
              09-recovery-guide.md  (cập nhật liên tục)
```

Chi tiết dependency, phạm vi theo repo và lệnh kiểm thử: **[EXECUTION-MATRIX.md](EXECUTION-MATRIX.md)**

---

## 3. Danh sách file

| File | Vai trò |
|---|---|
| **[00-shared-contract.md](00-shared-contract.md)** | Hợp đồng thực thi: nguyên tắc bằng chứng, quy trình 5 bước, mẫu báo cáo, điều kiện DONE/BLOCKED, quy tắc phạm vi |
| **[01-root-cause-recovery.md](01-root-cause-recovery.md)** | **P0** — 9 nguyên nhân gốc đã tái hiện, cách sửa từng cái, 21 acceptance criteria |
| **[02-data-pipeline.md](02-data-pipeline.md)** | Bản đồ generator, tính tái lập (deterministic), bảo toàn registry |
| **[03-vue-router-state.md](03-vue-router-state.md)** | Reactivity theo `route.params`, store singleton, dọn global, router 404 |
| **[04-academic-content.md](04-academic-content.md)** | Nội dung học thuật có nguồn, nhãn bằng chứng, chương chưa phân tích |
| **[05-latex-tables-charts-labs.md](05-latex-tables-charts-labs.md)** | LaTeX, bảng, ma trận, biểu đồ, port lab |
| **[06-ui-ux.md](06-ui-ux.md)** | Mobile, tìm kiếm, empty state, bàn phím, i18n UI |
| **[07-integration-i18n.md](07-integration-i18n.md)** | Lab chết, chương 13–20, thuật ngữ, cô lập hai repo |
| **[08-e2e-regression.md](08-e2e-regression.md)** | 10 test Vitest + 6 test node, chứng minh đỏ-trước/xanh-sau |
| **[09-recovery-guide.md](09-recovery-guide.md)** | `KILO_STATUS.md`, `health_check.sh`, `HANDOVER.md`, giao thức tiếp tục |
| **[EXECUTION-MATRIX.md](EXECUTION-MATRIX.md)** | Ma trận dependency, phạm vi, baseline đã đo, cổng chặn |
| **[ACCEPTANCE-CHECKLIST.md](ACCEPTANCE-CHECKLIST.md)** | Checklist nghiệm thu tổng hợp để đối chiếu cuối |

---

## 4. Hai repo

| | `MACRO` | `MICRO` |
|---|---|---|
| **Sách** | David Romer, *Advanced Macroeconomics*, 4e | Pindyck & Rubinfeld, *Microeconomics*, Global Edition 2017 |
| **Đường dẫn** | `research/advanced-macroeconomics-fourth-edition` | `research/microeconomics-pindyck-rubinfeld` |
| **Web** | `web/` → `dist-web/` | `web/` → `dist/` |
| **Lệnh test** | `npm --prefix web run test` | `npm --prefix web test` · `python -m pytest tests -q` · `node --test "tests/*.test.mjs"` |
| **Ghi chú** | Build xanh nhưng app hỏng hoàn toàn | `npm test` hiện **exit 1** (không có test file) |

> **Cấm tuyệt đối trộn dữ liệu, nội dung hay thuật ngữ của hai cuốn sách.** Prompt 07 (D.1) có kiểm tra tự động cho điều này.

---

## 5. Cách dùng

> **Đường dẫn tuyệt đối.** Các prompt dưới đây dán sẵn đường dẫn đầy đủ — copy nguyên văn, đừng tự dò hay rút gọn.

### 5.0. Bản đồ đường dẫn tuyệt đối

**Thư mục prompt (nơi Kilo đọc prompt):**

```
C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts\
```

| Prompt | Đường dẫn tuyệt đối |
|---|---|
| 00 | `C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts\00-shared-contract.md` |
| 01 | `C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts\01-root-cause-recovery.md` |
| 02 | `C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts\02-data-pipeline.md` |
| 03 | `C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts\03-vue-router-state.md` |
| 04 | `C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts\04-academic-content.md` |
| 05 | `C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts\05-latex-tables-charts-labs.md` |
| 06 | `C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts\06-ui-ux.md` |
| 07 | `C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts\07-integration-i18n.md` |
| 08 | `C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts\08-e2e-regression.md` |
| 09 | `C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts\09-recovery-guide.md` |
| Ma trận | `C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts\EXECUTION-MATRIX.md` |
| Checklist | `C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts\ACCEPTANCE-CHECKLIST.md` |

**Repo `MACRO` (Romer 4e):**

```
C:\Users\PC\Documents\AI_project\sandbox-financial\research\advanced-macroeconomics-fourth-edition\
```

**Repo `MICRO` (Pindyck & Rubinfeld):**

```
C:\Users\PC\Documents\AI_project\sandbox-financial\research\microeconomics-pindyck-rubinfeld\
```

**File trạng thái (prompt 09 tạo ra, dùng để tiếp tục sau khi bị gián đoạn):**

| Repo | Đường dẫn tuyệt đối |
|---|---|
| `MACRO` | `C:\Users\PC\Documents\AI_project\sandbox-financial\research\advanced-macroeconomics-fourth-edition\docs\KILO_STATUS.md` |
| `MICRO` | `C:\Users\PC\Documents\AI_project\sandbox-financial\research\microeconomics-pindyck-rubinfeld\docs\KILO_STATUS.md` |

---

### 5.1. Bắt đầu — prompt 01 (làm đầu tiên, một mình)

```
Bạn là Kilo Code. Đọc trước file hợp đồng:
C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts\00-shared-contract.md

Sau đó làm prompt:
C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts\01-root-cause-recovery.md

Hai repo cần làm (làm tuần tự, không song song):
1. MACRO: C:\Users\PC\Documents\AI_project\sandbox-financial\research\advanced-macroeconomics-fourth-edition
2. MICRO: C:\Users\PC\Documents\AI_project\sandbox-financial\research\microeconomics-pindyck-rubinfeld

Báo cáo riêng cho từng repo, theo mẫu §0.4 của hợp đồng.
```

### 5.2. Bắt đầu — prompt N (N từ 02 đến 08)

```
Bạn là Kilo Code. Đọc lại hợp đồng:
C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts\00-shared-contract.md

Làm prompt N:
C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts\<TÊN-FILE-Prompt-N>.md

Hai repo cần làm (làm tuần tự, không song song):
1. MACRO: C:\Users\PC\Documents\AI_project\sandbox-financial\research\advanced-macroeconomics-fourth-edition
2. MICRO: C:\Users\PC\Documents\AI_project\sandbox-financial\research\microeconomics-pindyck-rubinfeld

Báo cáo riêng cho từng repo, theo mẫu §0.4 của hợp đồng.
```

Bảng tra tên file theo N:

| N | Tên file |
|---|---|
| 02 | `02-data-pipeline.md` |
| 03 | `03-vue-router-state.md` |
| 04 | `04-academic-content.md` |
| 05 | `05-latex-tables-charts-labs.md` |
| 06 | `06-ui-ux.md` |
| 07 | `07-integration-i18n.md` |
| 08 | `08-e2e-regression.md` |

### 5.3. Tiếp tục sau khi bị gián đoạn

```
Bạn là Kilo Code. Bị gián đoạn giữa chừng — hãy khôi phục công việc.

Đọc file trạng thái:
C:\Users\PC\Documents\AI_project\sandbox-financial\research\advanced-macroeconomics-fourth-edition\docs\KILO_STATUS.md
C:\Users\PC\Documents\AI_project\sandbox-financial\research\microeconomics-pindyck-rubinfeld\docs\KILO_STATUS.md

Đối chiếu với `git status` và `git log --oneline -5` trong từng repo, chạy lại
lệnh kiểm thử ghi trong "Lệnh kiểm thử cuối đã chạy" để xác nhận thực tế.

Rồi tiếp tục đúng phần đang dở, theo giao thức §9.2 của:
C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts\09-recovery-guide.md
```

*(Chi tiết ở prompt 09, §9.2.)*

### 5.4. Chỉ làm một repo

```
Bạn là Kilo Code. Chỉ làm prompt N cho repo MACRO:
C:\Users\PC\Documents\AI_project\sandbox-financial\research\advanced-macroeconomics-fourth-edition

Prompt:
C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts\<TÊN-FILE-Prompt-N>.md
```

### 5.5. Chạy app để tự kiểm

```
MACRO (dev server, cổng 5185):
cd C:\Users\PC\Documents\AI_project\sandbox-financial\research\advanced-macroeconomics-fourth-edition
npm --prefix web run dev

MICRO (dev server, cổng 5186):
cd C:\Users\PC\Documents\AI_project\sandbox-financial\research\microeconomics-pindyck-rubinfeld
npm --prefix web run dev
```

### 5.6. Cổng chặn — kiểm tra trước khi làm prompt kế tiếp

```
Bạn là Kilo Code. Trước khi làm prompt N, hãy kiểm tra cổng chặn G(N-1) theo:
C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts\EXECUTION-MATRIX.md

Cũng đọc trạng thái hiện tại ở docs\KILO_STATUS.md của cả hai repo.
Nếu cổng trước chưa đạt, báo lại và sửa nốt cổng trước — đừng làm tiếp trên nền chưa vững.
```

*(Chi tiết ở [EXECUTION-MATRIX.md](EXECUTION-MATRIX.md), §6.)*

### 5.7. Nghiệm thu cuối

```
Bạn là Kilo Code. Đối chiếu toàn bộ công việc với checklist nghiệm thu:
C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts\ACCEPTANCE-CHECKLIST.md

Đánh dấu từng mục, đính kèm bằng chứng, và nêu rõ mục nào chưa đạt.
```

---

## 6. Quy tắc vàng

1. **Sửa gốc, không vá triệu chứng.** Generator/store/path trước; sửa tay file sinh ra là cách cuối cùng.
2. **Bằng chứng trước khẳng định.** Không có output lệnh → không được kết luận.
3. **Trung thực về bằng chứng học thuật.** Hạ trạng thái bằng chứng còn đúng hơn nâng để đẹp.
4. **Trạng thái nằm trong repo.** `docs/KILO_STATUS.md` — không nằm trong chat.
5. **Chặn cổng.** Không sang prompt kế tiếp khi cổng hiện tại chưa đạt.
6. **Báo cáo trung thực.** Mục `BLOCKED` nêu rõ hơn là làm vờ cho xong.

---

## 7. Phạm vi ngoài bộ prompt này

Bộ này **không** bao gồm: triển khai lên hosting, thiết kế lại từ đầu, thêm chương mới cho `MICRO` (C13–C20), hoặc nâng cấp thư viện.

Nếu Kilo phát hiện ngoài phạm vi → ghi vào **"RỦI RO CÒN LẠI"** trong báo cáo, **không** sửa ngầm.
