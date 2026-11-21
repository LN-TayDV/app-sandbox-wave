# EXECUTION MATRIX — MA TRẬN THỰC THI

Bản đồ thứ tự, dependency, phạm vi và lệnh kiểm thử cho toàn bộ bộ prompt.

> ### Đường dẫn làm việc
> **`MACRO`** → `C:\Users\PC\Documents\AI_project\sandbox-financial\research\advanced-macroeconomics-fourth-edition`
> **`MICRO`** → `C:\Users\PC\Documents\AI_project\sandbox-financial\research\microeconomics-pindyck-rubinfeld`
> **Thư mục prompt** → `C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts`

---

## 1. Ma trận phụ thuộc

```
00 (contract)  ← đọc trước TẤT CẢ
   │
   ├──► 01 (root-cause)  ← PHẢI XONG TRƯỚC, không làm gì khác trước
   │        │
   │        ├──► 02 (data pipeline)
   │        │        │
   │        │        └──► 04 (academic content) ──┐
   │        └──► 03 (vue/router/state) ───────────┤
   │                                               ├──► 05 (latex/tables/charts/labs)
   │                                               │         │
   │                                               │         └──► 06 (ui/ux)
   │                                               │                  │
   │                                               │                  └──► 07 (integration/i18n)
   │                                               │                           │
   │                                               └───────────────────────────┴──► 08 (e2e/regression)
   │                                                                                       │
   └──► 09 (recovery & handover) ◄──────────────────────────────────────────────────────────┘
```

**Quy tắc cứng:**
- `00` đọc trước mọi prompt.
- `01` chạy **trước tiên**, một mình. Hai app đều đang tải sai dữ liệu; mọi prompt sau giả định dữ liệu chạy đúng.
- `02` và `03` có thể chạy song song **trên hai repo khác nhau**, nhưng không song song trên cùng một repo.
- `04` cần `02` (sửa ở generator) và `03` (store).
- `05` cần `04` (nội dung phải có trước khi render).
- `06` cần `05` (component ổn định rồi mới tinh chỉnh layout).
- `07` cần `06`.
- `08` chạy song song với phần cuối `07` nếu đủ người, nhưng test phải viết **sau** khi hiểu hành vi cuối cùng.
- `09` là prompt liên tục — cập nhật file trạng thái sau **mỗi** prompt.

---

## 2. Phạm vi theo từng prompt

| Prompt | `MACRO` (Romer 4e) | `MICRO` (Pindyck & Rubinfeld) |
|---|---|---|
| **00** | Hợp đồng chung | Hợp đồng chung |
| **01** | A.1–A.7: sửa fetch dữ liệu, `dist-web` thiếu `data/`, mojibake (114 dòng), reactivity `route.params` | B.1–B.8: `window.MIC` chết, `exercises` không nối, 12 `chapter-XX.json` chết, lab không render, `undefined`, reactivity |
| **02** | `manifest.json` là hợp đồng; đồng bộ `data/learning/` 12 chương | `scripts/build_*.py` → `web/src/data/`; tính tái lập; bảo toàn 3 registry CSV |
| **03** | `useData` → store singleton; `loadAll()` 1 chỗ; 404; scroll | `window.MIC` → store; `exercises` + `chapterContent` vào store; 404 |
| **04** | Bảo toàn trạng thái bằng chứng; `PT-10-01` giữ `FORMULA_UNVERIFIED`; đối chiếu `data/_source/` | Rà soát §0–§11 × 12 chương; bổ sung phần thiếu từ `03_chapter_analyses/`; chương 13–20 hiện trạng thái trung thực |
| **05** | LaTeX, bảng, ma trận (`data/matrices/`), chart, 2 lab (`lab-solow`, `lab-taylor`) | LaTeX (thêm KaTeX), bảng `verification_rows`, chart `graph.json`, **port ≥7 lab có file thật** + xử lý lab còn thiếu (Kilo tự đếm số lab trong `course.json` vs file JS thực) |
| **06** | 8 tab tràn mobile; tìm kiếm; empty state; `document.title` | Nav 7 mục tràn 375px; tìm kiếm; empty state; nút chương trước/sau |
| **07** | Bảng đồ tri thức; điều hướng chéo 6 loại | **12/19 chương trỏ lab chết** (13 lab không có mã nguồn); **chương 13–20** chưa có nội dung; i18n; cô lập 2 repo |
| **08** | 6 test mới: M1–M6 (M1/M2 bắt trực tiếp lỗi dữ liệu) | 10 test Vitest mới T1–T10; sửa `npm test` đang hỏng (exit 1) |
| **09** | `docs/KILO_STATUS.md`, `docs/HANDOVER.md`, `scripts/health_check.sh` | `docs/KILO_STATUS.md`, `docs/HANDOVER.md`, `scripts/health_check.sh` |

---

## 3. Lệnh kiểm thử bắt buộc theo từng repo

### `MACRO`

```bash
cd "C:\Users\PC\Documents\AI_project\sandbox-financial\research\advanced-macroeconomics-fourth-edition"

npm --prefix web run typecheck     # vue-tsc --noEmit
npm --prefix web run test          # test:models (node) + test:data (python)
npm --prefix web run build         # vue-tsc --noEmit && vite build → dist-web/
python scripts/validate_app_data.py
```

### `MICRO`

```bash
cd "C:\Users\PC\Documents\AI_project\sandbox-financial\research\microeconomics-pindyck-rubinfeld"

npm --prefix web run typecheck
npm --prefix web test              # vitest run — HIỆN ĐANG HỎNG (exit 1, không có test file)
python -m pytest tests -q
node --test "tests/*.test.mjs"     # 21/21 baseline
npm --prefix web run build         # → dist/
python scripts/validate_html.py
```

### Cổng chặn chung

```bash
bash scripts/health_check.sh       # tạo ở prompt 09, mỗi repo một bản
```

---

## 4. Baseline đã đo — dùng để so sánh

Các con số này đã được đo **trước** khi sửa. Prompt 01 yêu cầu Kilo đo lại và so sánh.

### `MACRO` — baseline

| Chỉ số | Trước | Mục tiêu |
|---|---|---|
| Lỗi console khi mở `/chapters` | `SyntaxError: Unexpected token '<'` | 0 lỗi |
| Số thẻ chương hiển thị ở `/chapters` | **0** | 12 |
| Bộ đếm "Đã xác minh" | **0** | > 0 |
| `dist-web/` chứa `data/` | **không** | có (hoặc đã bundle) |
| Mắt xích mojibake trong `dist-web/assets/*.js` | có (cùng nguồn với `web/src/`) | 0 |
| Kết quả `npm --prefix web run test` | 52 PASS, 1 WARN, 2 INFO | xanh, WARN xử lý |

### `MICRO` — baseline

| Chỉ số | Trước | Mục tiêu |
|---|---|---|
| Số dòng bảng ở `/phuong-trinh` | **0** (chỉ có header) | 56 |
| Số bài tập ở tab "Kiểm tra hiểu biết" (Ch2) | **0** | > 0 (đúng chương 2) |
| Tab "Tổng quan" Ch2 | placeholder, không phải nội dung thật | nội dung từ `chapter-02.json` |
| Số chương có nội dung thật | **0 / 12** | 12 / 12 |
| Tab "Phòng thí nghiệm" Ch2 | không có select/slider/nút tính | đủ tham số + tính được |
| Chuỗi `undefined` trong tab "Ví dụ & biểu đồ" | **1** | 0 |
| `npm --prefix web test` | **exit 1** (không có test file) | exit 0 |
| `node --test "tests/*.test.mjs"` | 21/21 | ≥ 21/21 |

---

## 5. Nguyên nhân gốc — bản đồ lỗi → prompt

| Lỗi | Repo | Mô tả | Prompt xử lý | Test chống tái phát |
|---|---|---|---|---|
| R1 | MACRO | Fetch trả SPA HTML → `SyntaxError` | 01 (A.2) | M1, M2 |
| R2 | MACRO | `dist-web/` thiếu `data/` | 01 (A.4) | M4, M6 |
| R3 | MACRO | Mojibake trong 5 file view (114 dòng) | 01 (A.5) | M3 |
| R4 | MICRO | `window.MIC` undefined → bảng rỗng | 01 (B.2), 03 (B.2) | T1 |
| R5 | MICRO | `exercises` không nối → 0 bài tập | 01 (B.3) | T2 |
| R6 | MICRO | 12 `chapter-XX.json` chết | 01 (B.4), 04 (A.2) | T3, T4 |
| R7 | MICRO | Lab không render | 01 (B.5), 05 (B.4) | T8, T9 |
| R8 | MICRO | Chuỗi `undefined` | 01 (B.6), 05 (B.3) | T6 |
| R9 | Cả hai | `route.params` đọc 1 lần | 01 (A.6/B.7), 03 | T5, M2 |
| S1 | Cả hai | Global không ai định nghĩa | 03 | T1, T2 |
| S2 | Cả hai | `useData()` tạo state riêng mỗi view | 03 (A.2) | — |
| L1 | MICRO | 12/19 chương trỏ lab chết (13 lab) | 05 (B.4), 07 (A.2) | T9 |
| L2 | MICRO | Chương 13–20 chưa có nội dung | 07 (B.2) | T7 |
| L3 | Cả hai | Moji/bố cục mobile, không tìm kiếm | 06 | — |
| L4 | Cả hai | Test không bắt được lỗi runtime | 08 | Toàn bộ |
| L5 | Cả hai | Trộn dữ liệu giữa 2 sách | 07 (D.1) | — |

---

## 6. Cổng chặn (gates) giữa các prompt

| Cổng | Sau prompt | Điều kiện qua |
|---|---|---|
| G1 | 01 | Cả 2 app thực sự hiển thị nội dung (không chỉ "build xanh") |
| G2 | 02 | Build deterministic; không mất record registry |
| G3 | 03 | 1 request/lần tải; 0 global chết; điều hướng đổi nội dung |
| G4 | 04 | Mọi khối nội dung có nguồn + nhãn; chương chưa có nội dung hiện trung thực |
| G5 | 05 | 0 lỗi render; 0 `undefined`; mọi lab chạy được; parity xanh |
| G6 | 06 | Không tràn ở 375/768/1440; tìm kiếm hoạt động |
| G7 | 07 | 0 lab chết; chương 13–20 hiện trạng thái; 0 vi phạm cô lập |
| G8 | 08 | Mỗi lỗi R1–R9 có ≥ 1 test, chứng minh đỏ-trước/xanh-sau |
| G9 | 09 | `health_check.sh` xanh ở cả 2 repo; handover đủ 7 mục |

**Quy tắc:** không sang cổng kế tiếp khi cổng hiện tại chưa đạt. Nếu không đạt được, ghi `BLOCKED` và **dừng chuỗi phụ thuộc** — đừng làm tiếp trên nền chưa vững.
