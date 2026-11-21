# PROMPT 03 — VUE / ROUTER / STATE (KIẾN TRÚC ỨNG DỤNG)

> **Mã repo:** `MACRO` và `MICRO` — hai phần độc lập.
> **Phụ thuộc:** `00-shared-contract.md`, `01-root-cause-recovery.md`, `02-data-pipeline.md`.

> ### Đường dẫn làm việc
> **`MACRO`** → `C:\Users\PC\Documents\AI_project\sandbox-financial\research\advanced-macroeconomics-fourth-edition`
> **`MICRO`** → `C:\Users\PC\Documents\AI_project\sandbox-financial\research\microeconomics-pindyck-rubinfeld`
> **Hợp đồng** → `C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts\00-shared-contract.md`
> **Ma trận thực thi** → `C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts\EXECUTION-MATRIX.md`
> **Mục tiêu:** mọi lần điều hướng phải hiển thị đúng nội dung; state dùng chung nhất quán; không còn global window tùy tiện.

---

## 3.0. Vì sao đây là prompt riêng

Prompt 01 đã sửa lỗi tải dữ liệu và lỗi reactivity. Prompt này xử lý **tầng kiến trúc** còn lại — chỗ mà các lỗi tương lai sẽ sinh ra. Ba vấn đề đã xác minh:

| # | Repo | Vấn đề đã xác minh | Hệ quả |
|---|---|---|---|
| S1 | Cả hai | `ChapterView.vue` đọc `route.params` **một lần** trong `setup()`: `const id = route.params.id as string` (`MACRO`) và `const chapterNumber = Number(route.params.number ?? '1')` (`MICRO`). Không có `watch`. | Vue Router tái sử dụng cùng component instance khi chỉ đổi param → nội dung **không đổi**. Người học bấm "chương trước/sau" thì vẫn thấy chương cũ. |
| S2 | `MICRO` | `window.MIC` là global không ai định nghĩa, nhưng `EquationsView.vue` và `EquationsTab.vue` đọc nó. Lỗi bị `?? []` nuốt thành "rỗng" — không báo lỗi. | Kiểu lỗi âm thầm nguy hiểm nhất: giao diện trông "chạy" nhưng không có dữ liệu. |
| S3 | `MACRO` | `useData()` tạo **một `ref` riêng** mỗi lần được gọi. `ChaptersView`, `EquationsView`, `ExplorerView`, `GraphView`, `HomeView`, `LabView`, `ModelsView` đều gọi `useData()` riêng → mỗi view có state riêng, `loadAll()` bị gọi lặp lại ở mỗi view. | Tải trùng, state không đồng bộ giữa các trang, tốn băng thông. |

---

## 3.1. PHẦN A — `MACRO`

### A.1 Sửa S1 — reactivity theo param

`web/src/views/ChapterView.vue`:

```ts
const id = computed(() => route.params.id as string)
```

`loadChapter()` phải được gọi lại khi `id` đổi. Dùng `watch(id, ..., { immediate: true })` và bỏ `onMounted` cũ. Khi đổi chương: reset `activeTopicId` về `null` (để `loadChapter` chọn topic đầu) và **xoá trạng thái tab cũ**.

Quét **toàn bộ** `web/src/views/*.vue` xem còn view nào đọc `route.params`/`route.query` một lần trong setup không — sửa hết. Ghi danh sách file đã sửa vào báo cáo.

### A.2 Sửa S3 — `useData` thành singleton

`web/src/composables/useData.ts` hiện dùng `ref` ở cấp module → mỗi lần gọi tạo state mới. Kiểm tra lại: nếu `ref` nằm **trong** hàm `useData()` thì mỗi lần gọi là một instance mới (vấn đề S3). Nếu nằm ở cấp module thì đã là singleton — hãy **xác minh** và sửa cho đúng, đừng đoán.

Cách sửa chuẩn: chuyển sang **Pinia store** (repo đã dùng Pinia ở `MICRO`; kiểm tra `MACRO` có `stores/ui.ts` — có). Tạo `web/src/stores/data.ts` giữ `chapters`, `equations`, `models`, `labs`, `loading`, `error`, và `loadAll()` **idempotent** (nếu đang tải thì không tải lại; nếu đã tải thì trả về cache).

Rồi cập nhật 7 view để dùng store thay vì `useData()` cục bộ.

**Điều kiện:** `loadAll()` chỉ phát **một** request mỗi tài nguyên, bất kể điều hướng bao nhiêu lần.

### A.3 Sửa S3b — `loadAll()` chỉ được gọi một chỗ

Hiện 5 view tự gọi `data.loadAll().then(...)`. Sau khi có store, chuyển việc gọi `loadAll()` về **một** điểm khởi động duy nhất — ví dụ `App.vue` `onMounted` hoặc router `beforeEach` — và các view chỉ **đọc** state.

Đo lường: mở app, điều hướng qua 3 trang, đếm số request tới `data/learning/index.json` trong Network tab. Phải bằng **1** (hoặc 0 nếu dùng import tĩnh).

### A.4 Chuẩn hóa trạng thái tải và lỗi

Mọi view hiện có `loading`/`error` phải hiển thị:
- Đang tải → skeleton/spinner (không trắng).
- Lỗi → thông báo **cụ thể** kèm đường dẫn payload và gợi ý, **không** phải trang trắng.

Bổ sung một `<ErrorState>` dùng chung nếu chưa có.

### A.5 Router — kiểm tra guard và 404

`web/src/router/index.ts` có 10 route, `scrollBehavior` trả `{top: 0}`.

Bổ sung:
- Route `/:pathMatch(.*)*` → trang 404 tiếng Việt có nút về trang chủ.
- `scrollBehavior` nên **giữ vị trí scroll** khi quay lại từ trang chi tiết (dùng `savedPosition`).
- Kiểm tra mọi route có `meta` mô tả tiếng Việt để dùng cho tiêu đề tab.

### A.6 Acceptance — `MACRO`

| # | Tiêu chí | Bằng chứng |
|---|---|---|
| A1 | Điều hướng `ch1`→`ch2`→`ch3` đổi nội dung mỗi lần | Dump text 3 lần, khác nhau |
| A2 | Không còn `route.params` đọc một lần trong setup ở bất kỳ view nào | Grep + review |
| A3 | Số request `data/learning/index.json` khi điều hướng 3 trang = **1** (hoặc 0 nếu import tĩnh) | Network tab |
| A4 | `loadAll()` được gọi từ **một** chỗ duy nhất | Grep: ≤ 1 call site |
| A5 | Trang lỗi hiện thông báo cụ thể, không trắng | Screenshot |
| A6 | Route 404 hoạt động, có link về trang chủ | Screenshot |
| A7 | `npm --prefix web run typecheck` + `test` + `build` xanh | Output |

---

## 3.2. PHẦN B — `MICRO`

### B.1 Sửa S1 — reactivity theo param

`web/src/views/ChapterView.vue:72`. Sửa thành `computed` + `watch`:

```ts
const chapterNumber = computed(() => Number(route.params.number ?? '1'))
watch(chapterNumber, () => { activeTab.value = 'overview' })
```

Kiểm tra `web/src/views/LabView.vue` — dùng `route.params.labId`, có cùng vấn đề không.

Quét toàn bộ `web/src/views/*.vue`.

### B.2 Sửa S2 — dọn global `window.MIC`

Đã xử lý trong prompt 01 (B.2). Ở prompt này, **xác nhận lại** và dọn dẹp:

- Grep toàn repo `window.MIC`, `(window as any).MIC` → phải còn **0** kết quả trong `web/src/`.
- `html/assets/app.js` (bản legacy) vẫn dùng `window.MIC` — đó là **bản legacy tách biệt**, để nguyên, nhưng ghi rõ trong báo cáo là hai thế giới khác nhau.
- Nếu `MICRO` còn global nào khác không có nguồn (kiểm tra `window.` trong `web/src/`), xử lý cùng cách.

### B.3 Store — bổ sung `exercises` và `chapters` đầy đủ

`web/src/stores/course.ts` hiện có `course` (course.json), `registry` (registry.json), các computed `chapters`, `parts`, `availableChapters`, `pendingChapters`.

Bổ sung:
- `exercises` từ `data/exercises.json` (đã làm ở prompt 01 B.3).
- `chapterContent(n)` → lấy nội dung đầy đủ từ `data/chapters/chapter-NN.json` (đã làm ở prompt 01 B.4).

Đảm bảo `chapterByNumber` vẫn trả metadata (dùng cho điều hướng), và thêm hàm riêng cho nội dung. **Đừng** trộn hai nguồn vào một object mà mất phân biệt.

### B.4 Router — bổ sung 404 và giữ scroll

`web/src/router/index.ts` có 9 route, path tiếng Việt (`/chuong`, `/phong-thi-nghiem/:labId`, `/ban-do-tri-thuc`, `/mo-hinh`, `/phuong-trinh`, `/nguon`).

Bổ sung:
- Route 404 tiếng Việt.
- `scrollBehavior` hiện xử lý `to.hash` — kiểm tra hash anchor có thật sự hoạt động (view có `id` tương ứng không).
- Mỗi route nên có `meta.title` tiếng Việt.

### B.5 Acceptance — `MICRO`

| # | Tiêu chí | Bằng chứng |
|---|---|---|
| B1 | Điều hướng `ch2`→`ch3` đổi nội dung | Dump text 2 lần |
| B2 | Grep `window.MIC` trong `web/src/` → **0** kết quả | Output grep |
| B3 | Mọi global `window.X` trong `web/src/` đều có nguồn định nghĩa | Grep + đối chiếu |
| B4 | Route 404 hoạt động | Screenshot |
| B5 | `npm --prefix web run typecheck` pass | Output |
| B6 | `npm --prefix web run build` pass | Output |
| B7 | `node --test "tests/*.test.mjs"` xanh (≥ 21/21) | Output |
| B8 | `python -m pytest tests -q` xanh | Output |

---

## 3.3. Quy tắc chung

- **Không** thêm global mới. Dữ liệu đi qua store/composable có kiểu rõ ràng.
- **Không** phá vỡ `MICRO`'s `html/` bản legacy — nó là app độc lập, có test riêng (`tests/test_html_app.py`). Nếu một sửa đổi chạm tới nó, phải chạy cả test legacy.
- **Không** thêm thư viện mới. Cả hai repo đã có đủ (`vue-router`, `pinia`, `echarts`).
- Mọi `computed` phải **pure** — không được side-effect trong getter.
- Sửa xong phải chạy lại **toàn bộ** lệnh test của repo, không chỉ lệnh liên quan.
