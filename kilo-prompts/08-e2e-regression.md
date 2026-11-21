# PROMPT 08 — E2E / REGRESSION (KIỂM THỬ HỒI QUY & CHỐNG TÁI PHÁT)

> **Mã repo:** `MACRO` và `MICRO` — hai phần độc lập.
> **Phụ thuộc:** `00-shared-contract.md`, `01`–`07`.

> ### Đường dẫn làm việc
> **`MACRO`** → `C:\Users\PC\Documents\AI_project\sandbox-financial\research\advanced-macroeconomics-fourth-edition`
> **`MICRO`** → `C:\Users\PC\Documents\AI_project\sandbox-financial\research\microeconomics-pindyck-rubinfeld`
> **Hợp đồng** → `C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts\00-shared-contract.md`
> **Ma trận thực thi** → `C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts\EXECUTION-MATRIX.md`
> **Mục tiêu:** viết test bắt được **chính xác** những lỗi đã xảy ra, để chúng không quay lại.

---

## 8.0. Vì sao lỗi R1–R9 (prompt 01) sống sót

Đây là bài học cốt lõi của toàn bộ công việc:

| Lỗi | Tại sao test hiện có không bắt được |
|---|---|
| R1 (`MACRO`): fetch trả HTML → `SyntaxError` | Test kiểm tra **payload tồn tại trên đĩa**, không kiểm tra **app tải được payload đó trong trình duyệt**. `npm run build` xanh hoàn toàn trong khi app hỏng 100%. |
| R4 (`MICRO`): `window.MIC` undefined | `?? []` biến lỗi thành giá trị hợp lệ. Test kiểm tra "component render không crash" — mà nó **không** crash, chỉ rỗng. |
| R5 (`MICRO`): bài tập = 0 | Test kiểm tra shape của `course.json`, không kiểm tra **số bài tập hiển thị**. |
| R6 (`MICRO`): 12 file JSON chết | Không có test nào kiểm tra file dữ liệu nào **được import thật**. File tồn tại → tưởng đã dùng. |
| R7 (`MICRO`): lab không render | Test labs-parity kiểm tra **logic Python↔JS** (đúng), không kiểm tra **lab có render trong app** (sai). |
| R9 (cả hai): đổi chương không đổi nội dung | Test là unit test trên component, không phải test điều hướng thật. |

> **Nguyên tắc:** test phải kiểm tra **thứ người dùng thấy**, không phải thứ file chứa. Một test "app render" chỉ có giá trị nếu nó khẳng định **nội dung cụ thể** xuất hiện.

---

## 8.1. PHẦN A — `MICRO`

### A.1 Bổ sung test Vitest

`web/vite.config.ts` khai `test.include: ['tests/**/*.spec.ts']` nhưng **`web/tests/` không tồn tại** → `npm test` hiện **thoát với code 1** ("No test files found"). Đây là test hỏng âm thầm — CI xanh vì chưa ai để ý.

Việc cần làm:
1. Tạo `web/tests/` với `*.spec.ts`.
2. Đảm bảo `npm test` trong `web/` chạy được và xanh.

Test bắt buộc — mỗi test gắn trực tiếp với một lỗi đã xảy ra:

| # | File test | Khẳng định | Bắt lỗi |
|---|---|---|---|
| T1 | `registry-wiring.spec.ts` | `useCourseStore().registry.equations` có **56** bản ghi, và `EquationsView`/`EquationsTab` **không** đọc `window.MIC` | R4 |
| T2 | `exercises-wiring.spec.ts` | `courseStore.exercises` có > 0 bản ghi; lọc theo chương trả về **> 0** bài cho chương có bài | R5 |
| T3 | `chapter-content.spec.ts` | `chapterContent(n)` trả về nội dung **không rỗng** cho cả 12 chương; mỗi chương có `blocks` hoặc `summary_html` khác rỗng | R6 |
| T4 | `no-dead-data.spec.ts` | **Mọi** file trong `web/src/data/` (trừ `index`/`registry`/`course`) đều được import ở đâu đó trong `src/` — phát hiện dữ liệu chết bằng cách quét import | R6 |
| T5 | `chapter-navigation.spec.ts` | Render `ChapterView` với `route.params.number` = 1, đổi sang 2, `await nextTick()` → nội dung **đã đổi** | R9 |
| T6 | `no-undefined-render.spec.ts` | Render mọi tab của mọi chương; text ra **không** chứa `undefined`, `NaN`, `[object Object]` | R8 |
| T7 | `empty-state.spec.ts` | Chương 13 (chưa có nội dung) render **empty state có chữ**, không phải trang trắng; có link tới registry | Chương 13–20 |
| T8 | `lab-mount.spec.ts` | Mỗi lab được khai cho chương 1–12 **mount được**; có select tham số + nút tính; bấm tính ra kết quả số; tham số vô nghĩa → hiện cảnh báo, không crash | R7 |
| T9 | `lab-registry.spec.ts` | Mọi id lab trong `course.json` đều resolve được tới một module lab thật; id nào không có → phải hiện empty state, không phải link chết | R7 + A2 (prompt 07) |
| T10 | `evidence-label.spec.ts` | Mỗi khối nội dung hiển thị **nhãn trạng thái bằng chứng** hợp lệ từ tập nhãn đã biết | §4 |

**Yêu cầu viết test:**
- Dùng `@vue/test-utils` (`mount`) + `createPinia()` + `createRouter(createMemoryHistory())`.
- Test phải **fail trước khi sửa** và **pass sau khi sửa** — nếu Kilo viết test sau khi sửa xong, phải xác nhận bằng cách **tạm revert** một thay đổi và thấy test đỏ. Nêu cách xác nhận trong báo cáo.
- Không test "component không crash". Test **nội dung cụ thể**.
- Không snapshot toàn bộ DOM (nhạy cảm, khó bảo trì). Assert theo text/selector cụ thể.

### A.2 Sửa `npm test` đang hỏng

Sau khi tạo `web/tests/`, `npm test` phải xanh. Nếu `package.json` của `web/` có `test: vitest run` — kiểm tra nó trỏ đúng `web/` (cwd), và `vite.config.ts` `test.include` đúng.

### A.3 Bổ sung test Python

`tests/` (ở gốc repo) đã có: `app-smoke.test.mjs`, `data-contract.test.mjs`, `labs-parity.test.mjs`, `test_app_shells.py`, `test_browser_smoke.py`, `test_html_app.py`, `test_scientific.py`.

Bổ sung (chỉ nếu chưa có):
- `test_vue_data_contract.py`: `course.json` phải có `exercises` (hoặc file tương đương) khớp `exercises.json`; 12 `chapter-XX.json` phải parse được và có `prev_chapter`/`next_chapter` đúng dãy.
- Test khẳng định **không có id lab chết** trong `course.json`.

### A.4 Acceptance — `MICRO`

| # | Tiêu chí | Bằng chứng |
|---|---|---|
| A1 | `npm --prefix web test` **thoát code 0** (trước đây code 1) | Output |
| A2 | Có **≥ 10** file `.spec.ts` trong `web/tests/` | Liệt kê |
| A3 | Mỗi test T1–T10 có file tương ứng | Bảng ánh xạ T→file |
| A4 | Chứng minh mỗi test **thất bại trước khi sửa** | Output đỏ trước, xanh sau |
| A5 | `python -m pytest tests -q` xanh | Output |
| A6 | `node --test "tests/*.test.mjs"` xanh | Output |
| A7 | `npm --prefix web run typecheck` + `build` xanh | Output |

---

## 8.2. PHẦN B — `MACRO`

### B.1 Test runtime cho `MACRO`

`MACRO` có `tests/models.test.mjs` (node) + `scripts/validate_app_data.py` (python). Cả hai kiểm tra **dữ liệu**, không kiểm tra **runtime**.

Bổ sung test runtime bắt được R1/R3/R9:

| # | Test | Khẳng định | Bắt lỗi |
|---|---|---|---|
| M1 | `tests/data-fetch.test.mjs` | Mọi URL payload app fetch (`../data/learning/index.json`, `../data/equations/index.json`, `../data/models/index.json`, `../data/labs/index.json`) trả **Content-Type chứa `application/json`** và **parse được** — dùng chính đường dẫn tương đối mà app dùng, không dùng đường dẫn tuyệt đối | R1 |
| M2 | `tests/chapter-routes.test.mjs` | Với mỗi route chương, payload tương ứng tồn tại **và parse được** dưới đường dẫn tương đối từ route đó | R1 |
| M3 | `tests/encoding.test.mjs` | Mọi file trong `web/src/` **không chứa** mắt xích mojibake (`Ã`, `áº`, `á»`, `â€`, `Ä`...) | R3 |
| M4 | `tests/manifest-contract.test.mjs` | `manifest.json` khai 8 tab, khớp router, và mọi payload khai trong manifest đều tồn tại | R2 |
| M5 | `tests/no-dead-data.test.mjs` | Mọi file trong `data/` mà app **không** đọc → được phải là file nghiên cứu gốc (`data/_source/`, `data/audit/`). Bất kỳ file trong `data/learning|equations|models|labs|graph` nào không được đọc → **fail** | R2, R6 |
| M6 | `tests/build-output.test.mjs` | Sau `vite build`, `dist-web/` **chứa** dữ liệu app cần (dạng import tĩnh trong bundle, hoặc file `data/` được copy) và **không chứa** mojibake | R2, R3 |

**M1/M2 là quan trọng nhất** — chúng bắt trực tiếp lỗi đã làm hỏng toàn bộ app.

Cách viết M1 đúng: **dùng đúng chuỗi URL tương đối mà app dùng**, và `new URL(path, base)` với base là route hiện tại, rồi kiểm tra response. Đừng kiểm tra file trên đĩa — đó chính là lỗ hổng đã để R1 lọt qua.

### B.2 Test hồi quy dữ liệu

`scripts/validate_app_data.py` đã kiểm tra nhiều bất biến (52 PASS). Bổ sung:
- Snapshot trạng thái bằng chứng của mọi phương trình vào `data/audit/evidence-snapshot.json`.
- Test so sánh snapshot với dữ liệu hiện tại: được phép **hạ** trạng thái, **không được nâng** mà không có lý do ghi trong file.

### B.3 Acceptance — `MACRO`

| # | Tiêu chí | Bằng chứng |
|---|---|---|
| B1 | Có **≥ 6** file test mới, bao phủ M1–M6 | Liệt kê |
| B2 | M1/M2 **fail** trên bản code cũ (chứng minh bắt được R1) | Output đỏ |
| B3 | M3 **fail** trên bản code cũ (chứng minh bắt được R3) | Output đỏ |
| B4 | Tất cả test mới xanh trên bản code sau sửa | Output |
| B5 | `npm --prefix web run test` xanh | Output |
| B6 | `python scripts/validate_app_data.py` xanh | Output |
| B7 | `npm --prefix web run typecheck` + `build` xanh | Output |

---

## 8.3. Chống tái phát — quy tắc bàn giao

Để lỗi đã sửa không quay lại:

1. **Mọi lỗi R1–R9 phải có ít nhất một test.** Bảng ánh xạ trong báo cáo:
   `lỗi → file test → tên test → xanh/đỏ`.
2. **Test phải đỏ trước khi sửa.** Nếu không chứng minh được, test có thể vô nghĩa.
3. **CI gate:** tạo file `.github/workflows/` (nếu repo đã có CI) hoặc `scripts/ci.sh` chạy **toàn bộ** lệnh §0.8, exit code khác 0 khi bất kỳ lệnh nào đỏ.
4. **Cấm `test.skip` / `xit` / bỏ assert** để làm xanh. Nếu một test không áp dụng, xóa hẳn khỏi file và ghi lý do.
5. **Cấm nới lỏng threshold** của test để qua (ví dụ đổi `toBe(56)` thành `toBeGreaterThan(0)`) nếu không có lý do học thuật — lý do phải ghi trong báo cáo.

---

## 8.4. Acceptance chung (cả hai repo)

| # | Tiêu chí | Bằng chứng |
|---|---|---|
| G1 | Mỗi lỗi R1–R9 có ≥ 1 test | Bảng ánh xạ |
| G2 | Mỗi test mới chứng minh đỏ-trước/xanh-sau | Output |
| G3 | `npm test` của **mỗi** repo thoát code 0 | Output cả hai |
| G4 | Toàn bộ lệnh §0.8 xanh ở cả hai repo | Output đầy đủ |
| G5 | CI gate chạy toàn bộ lệnh, exit ≠ 0 khi đỏ | Script + output chứng minh |
