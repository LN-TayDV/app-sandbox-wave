# PROMPT 01 — ROOT-CAUSE RECOVERY (KHÔI PHỤC KHẢ NĂNG CHẠY)

> **Mã repo:** `MACRO` và `MICRO` — hai phần độc lập trong cùng prompt này.
> **Phụ thuộc:** `00-shared-contract.md` (bắt buộc đọc trước).
> **Đây là prompt P0.** Không làm gì khác cho tới khi prompt này xong. Mọi prompt sau giả định hai ứng dụng thực sự tải được dữ liệu.

> ### Đường dẫn làm việc
> **`MACRO`** → `C:\Users\PC\Documents\AI_project\sandbox-financial\research\advanced-macroeconomics-fourth-edition`
> **`MICRO`** → `C:\Users\PC\Documents\AI_project\sandbox-financial\research\microeconomics-pindyck-rubinfeld`
> **Hợp đồng** → `C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts\00-shared-contract.md`
> **Ma trận thực thi** → `C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts\EXECUTION-MATRIX.md`

---

## 1.0. Vì sao prompt cũ không hiệu quả — nguyên nhân gốc đã xác minh

Trước khi sửa, Kilo phải hiểu rằng các prompt cũ **không hỏng vì thiếu chỉ dẫn chi tiết**, mà hỏng vì chúng coi ứng dụng là "đã xong" khi thực tế tầng dữ liệu dưới cùng **chưa bao giờ chạy được**. Cụ thể, đã tái hiện:

| # | Repo | Triệu chứng đã tái hiện | Nguyên nhân gốc |
|---|---|---|---|
| R1 | `MACRO` | Console: `SyntaxError: Unexpected token '<', "<!DOCTYPE "... is not valid JSON`. Trang `/chapters` hiển thị "12 Chương" nhưng **0** thẻ chương, "Đã xác minh **0**", "Chưa xác minh công thức **0**". | `web/src/composables/useData.ts` và `web/src/views/ChapterView.vue` fetch đường dẫn tương đối `../data/learning/index.json`. Ở route `/chapters`, `../` **chạy lên trên gốc**, nên URL thực tế là `/data/...` — nhưng Vite **không serve** thư mục `../data` (nằm ngoài `root` web/, và `vite.config.ts` **không** có `server.fs.allow`). Vite trả **SPA fallback HTML** với HTTP 200 → `res.ok` là `true` → `res.json()` ném `SyntaxError`. |
| R2 | `MACRO` | Build ra `dist-web/` chỉ có `assets/` + `index.html` — **không có** `data/`. Dù có sửa dev server, bản production vẫn hỏng. | Không có bước copy `data/` vào `dist-web/`, và `base`/`publicDir` chưa cấu hình. |
| R3 | `MACRO` | Toàn bộ 5 file view hiển thị mojibake: `PhÃ²ng ThÃ­ Nghiá»‡m`, `Romer â€” Thá»© SÃ¡t`. Đã xác minh **114 dòng** chứa mắt xích hỏng trong `web/src/` (`HomeView.vue` 28, `LabView.vue` 43, `GraphView.vue` 23, `ExplorerView.vue` 11, `LabsView.vue` 9) — và cùng số mắt xích đó xuất hiện trong bundle `dist-web/assets/index-s8a1rH--.js`. | Nguồn `.vue` đã bị hỏng encoding từ trước (5 file trong `web/src/views/`). |
| R4 | `MICRO` | Trang `/phuong-trinh` (Phương trình) render **rỗng** — chỉ có header bảng, 0 dòng. | `web/src/views/EquationsView.vue:48` và `web/src/components/tabs/EquationsTab.vue:52` đọc `(window as any).MIC?.registry?.equations`. Nhưng `window.MIC` **không hề được định nghĩa** trong ứng dụng Vue (`main.ts` không set, không có file nào gán). `?? []` biến lỗi thành danh sách rỗng, im lặng. |
| R5 | `MICRO` | Tab "Kiểm tra hiểu biết" mọi chương: *"Chương này chưa có bài tập tự kiểm tra đã được đăng ký."* — dù home page quảng bá **163 bài tập có đáp án**. | `web/src/views/ChapterView.vue` lấy `chapterExercises` từ `courseStore.course.exercises`, nhưng `web/src/data/course.json` **không có** key `exercises` (chỉ có `book`, `page_offset`, `evidence_statuses`, `parts`, `chapters`). `web/src/data/exercises.json` tồn tại nhưng **không file nào import nó**. |
| R6 | `MICRO` | Nội dung phong phú của `web/src/data/chapters/chapter-01..12.json` (block, concepts, equation_rows, figure_rows, mechanisms, summary_html, verification_rows) **chưa bao giờ** hiển thị. | `ChapterView.vue` đọc `courseStore.chapterByNumber(...)` → dữ liệu trong `course.json` chỉ là **metadata** (`number, title_en, title_vi, part, status, available, central_question, labs, toc_sections, analysis_sections, sub_sections`). File `chapter-XX.json` (12 file) **không được import ở bất kỳ đâu** — grep `import.meta.glob`/`@/data/chapters` cho 0 kết quả. |
| R7 | `MICRO` | Tab "Phòng thí nghiệm" của Chương 2: **không có** select, không có slider, không có nút tính. | `LabTab.vue` dựa trên `chapter.labs` (mảng id chuỗi) nhưng **không** nạp phần hiển thị lab. 7 lab JS đã verify sẵn nằm ở `html/assets/labs/*.js` (đăng ký vào `root.MICLabs`) và `html/assets/lib/core.js` (đăng ký `root.MICCore`). |
| R8 | `MICRO` | Chapter page hiện chuỗi `undefined` trong tab "Ví dụ & biểu đồ". | Trường dữ liệu thiếu ở nơi render, không có guard `??` / `?? '—'`. |
| R9 | Cả hai | Điều hướng bằng nút "chương trước / chương sau" hoặc link nội bộ giữa hai chương **không cập nhật nội dung**. | Cả hai `ChapterView.vue` đọc `route.params` **một lần** ở setup (`const id = route.params.id` / `const chapterNumber = Number(route.params.number)`), không có `watch(() => route.params...)`. Vue Router tái sử dụng component khi chỉ đổi param. |

**Bài học cho prompt:** prompt cũ kiểm tra "file tồn tại", "build không lỗi", "test pass" — nhưng **không kiểm tra ứng dụng có thực sự tải được dữ liệu và hiển thị nội dung không**. `npm run build` của `MACRO` **thành công** trong khi ứng dụng hỏng hoàn toàn. Phải có kiểm thử *runtime* mới bắt được R1–R9.

---

## 1.1. PHẦN A — `MACRO`: sửa tầng dữ liệu

### A.1 Chẩn đoán chính xác trước khi sửa

Chạy và dán output:

```bash
cd "C:\Users\PC\Documents\AI_project\sandbox-financial\research\advanced-macroeconomics-fourth-edition\web"
npm run dev
```

Mở trình duyệt, đi tới `http://localhost:5185/chapters`, mở DevTools → Console. Xác nhận `SyntaxError: Unexpected token '<'`. Trong Network tab, xác nhận request `.../data/learning/index.json` trả `Content-Type: text/html` (SPA fallback) chứ không phải `application/json`.

Nếu hiện tượng **không** tái hiện → dừng phần này, báo lại, vì có thể đã có sửa đổi ngoài phạm vi.

### A.2 Sửa đường dẫn tải dữ liệu

**Đừng** sửa bằng cách thêm `server.fs.allow` trong `vite.config.ts` — cách đó chỉ chữa dev server, còn bản production vẫn hỏng (R2), và mở toàn bộ cây thư mục ngoài `root` ra ngoài. Sửa đúng cách:

**Cách ưu tiên — nạp dữ liệu bằng import tĩnh (build-time).**
Repo đã có alias sẵn: `@data` → `../data`, `@models` → `../assets/js/models` (khai trong `web/vite.config.ts`).

Trong `web/src/composables/useData.ts`, thay `loadJson(path)` bằng import tĩnh:

```ts
import chaptersJson from '@data/learning/index.json'
import equationsJson from '@data/equations/index.json'
import modelsJson from '@data/models/index.json'
import labsJson from '@data/labs/index.json'
```

Kiểm tra `web/tsconfig.json` có `resolveJsonModule: true` và alias `@data` chưa; bổ sung nếu thiếu.

Lợi ích: dữ liệu được Vite đóng gói vào `dist-web/assets/`, không còn phụ thuộc đường dẫn runtime, không còn SPA fallback, chạy được khi mở bằng `file://` hoặc bất kỳ static server nào.

**Phương án thay thế (chỉ dùng nếu import tĩnh không khả thi)** — giữ `fetch` nhưng dùng đường dẫn tuyệt đối phụ thuộc `import.meta.env.BASE_URL`, và cấu hình Vite để copy `data/` sang `dist-web/`:

- `web/vite.config.ts`: thêm `publicDir` trỏ tới một thư mục chứa `data/`, **hoặc** thêm `build.rollupOptions` copy, **hoặc** thêm `base: './'`.
- Kèm bắt buộc: **kiểm tra `res.ok` VÀ `content-type` chứa `application/json`**, nếu không thì ném lỗi có thông điệp rõ ràng thay vì để `SyntaxError` trôi qua.

**Bắt buộc cho mọi phương án:** mọi `fetch` phải có guard `res.ok` và phải bắt lỗi, hiển thị thông báo lỗi cho người dùng thay vì trang trắng.

### A.3 Sửa `ChapterView.vue` (cùng nguyên nhân, cùng cách sửa)

`web/src/views/ChapterView.vue` cũng fetch `../data/learning/${id}.json`. Sửa theo cùng phương án đã chọn ở A.2.

Với import tĩnh, dùng `import.meta.glob` để nạp hết file chương (12 chương, tổng dung lượng nhỏ):

```ts
const chapterFiles = import.meta.glob('@data/learning/*.json')
```

Hoặc nếu file chương lớn, giữ `fetch` với đường dẫn đã sửa ở A.2.

### A.4 Đồng bộ `dist-web/`

Sau khi sửa, `npm run build` phải tạo `dist-web/` **có** dữ liệu dùng được. Kiểm tra bằng cách serve `dist-web/` bằng static server và tải một trang chương thật. Nếu chọn phương án import tĩnh thì dữ liệu nằm trong bundle JS — không cần copy thủ công.

### A.5 Sửa mojibake (R3)

5 file trong `web/src/views/`: `ExplorerView.vue`, `GraphView.vue`, `HomeView.vue`, `LabsView.vue`, `LabView.vue`.

Cách sửa đúng: **không** dùng regex thay thế đại trà. Mỗi chuỗi hỏng là UTF-8 bị decode bằng Latin-1/Cp1252 rồi encode lại UTF-8. Khôi phục bằng cách decode 2 lần:

```python
s.encode('cp1252', errors='strict').decode('utf-8', errors='strict')
```

Nhưng chuỗi có ký tự ngoài cp1252 sẽ ném lỗi — hãy dùng `latin-1` làm fallback, hoặc xử lý từng chuỗi. Viết **script Python** trong `scripts/` để khôi phục hàng loạt, chạy một lần, rồi **xóa script** hoặc giữ lại thành công cụ tái sử dụng có docstring.

Yêu cầu bắt buộc: sau khi sửa, đếm lại số mắt xích mojibake — phải bằng **0** trong cả `web/src/` lẫn `dist-web/assets/*.js`.

Công cụ phát hiện — dùng lại cho MICRO (đếm **số lần xuất hiện**, không phải số dòng):

```python
import glob, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
MARKS = ['Ã', 'áº', 'á»', 'â€']
def count(p):
    return sum(open(p, encoding='utf-8', errors='replace').read().count(m) for m in MARKS)
total = 0
for f in sorted(glob.glob('web/src/**/*.vue', recursive=True) + glob.glob('web/src/**/*.ts', recursive=True)):
    n = count(f)
    if n:
        print(f, 'x%d' % n); total += n
print('TOTAL mojibake (web/src):', total)
for f in sorted(glob.glob('dist-web/assets/*.js')):
    print('BUNDLE', f, 'x%d' % count(f))
```

**Tiền đề:** xác nhận file nguồn là UTF-8 hợp lệ trước khi sửa. Nếu file **không** decode được dưới UTF-8, đó là tình huống khác — báo lại trước khi sửa.

**Lưu ý khi đọc số liệu:** `grep -c` trả về **số dòng** chứa mắt xích, không phải số lần xuất hiện. Bundle build là file tối giản hoá nên có thể gom hàng trăm mắt xích vào một dòng. Luôn dùng script Python ở trên để có con số chuẩn, và dán con số đó vào báo cáo.

### A.6 Sửa reactivity (R9)

`web/src/views/ChapterView.vue`: thay việc đọc `route.params.id` một lần bằng `computed` hoặc `watch`:

```ts
const id = computed(() => route.params.id as string)
```

và `watch(id, () => { activeTopicId.value = null; void loadChapter() }, { immediate: true })`.

Kiểm tra file `web/src/views/LabView.vue` và các view khác có `route.params` tương tự — áp dụng cùng cách.

### A.7 PHẦN A — Acceptance criteria

| # | Tiêu chí | Bằng chứng bắt buộc |
|---|---|---|
| A1 | Console **không** còn `SyntaxError` khi mở `/chapters` | Dán output console sạch |
| A2 | `/chapters` hiển thị **12** thẻ chương click được, số đếm "Đã xác minh" **> 0** | Screenshot hoặc dump text |
| A3 | Mở `/chapters/ch1` hiện nội dung chương thật (không rỗng, không lỗi) | Dump text đã render |
| A4 | Mở `/chapters/ch1` rồi điều hướng sang `ch2` → nội dung **đổi** | Dump text 2 lần, khác nhau |
| A5 | `npm run build` xong, `dist-web/` serve được và hiển thị dữ liệu | Lệnh serve + curl/dump |
| A6 | Số mắt xích mojibake trong `web/src/` **= 0** | Output script đếm |
| A7 | Số mắt xích mojibake trong `dist-web/assets/*.js` **= 0** | Output script đếm |
| A8 | `npm --prefix web run typecheck` pass | Output |
| A9 | `npm --prefix web run test` pass | Output |

---

## 1.2. PHẦN B — `MICRO`: sửa tầng dữ liệu

### B.1 Chẩn đoán chính xác trước khi sửa

Chạy:

```bash
cd "C:\Users\PC\Documents\AI_project\sandbox-financial\research\microeconomics-pindyck-rubinfeld\web"
npm run build
npx vite preview --port 5190
```

Mở `http://localhost:5190/phuong-trinh` → xác nhận bảng rỗng (chỉ header).
Mở `http://localhost:5190/chuong/2` → tab "Kiểm tra hiểu biết" → xác nhận "chưa có bài tập tự kiểm tra".
Mở Console → xác nhận không có lỗi (vì `?? []` đã nuốt lỗi).

Ghi lại **số dòng bảng** và **số câu hỏi** trước khi sửa. Đây là baseline để so sánh.

### B.2 Sửa R4 — registry bị nuốt

`web/src/views/EquationsView.vue:48` và `web/src/components/tabs/EquationsTab.vue:52` đọc `window.MIC`.

Repo đã có store sẵn: `web/src/stores/course.ts` expose `registry` (đã import `data/registry.json`). `registry.json` có `theories` (87), `equations` (56), `figures` (65) — mỗi record có `chapter_id` dạng `"Ch2"`, cùng `printed_page` và `pdf_page`.

Sửa: thay `(window as any).MIC?.registry?.equations ?? []` bằng nguồn đơn nhất đã import tĩnh:

```ts
const registry = computed(() => useCourseStore().registry.equations)
```

Giữ filter `chapter_id === 'Ch' + chapterNumber` như hiện tại. Kiểm tra cả `web/src/views/EquationsView.vue` — nó có thể cần nhiều hơn `equations` (xem `registry.theories`, `registry.figures`).

**Không** được tạo lại global `window.MIC` chỉ để né sửa import — đó là giữ lại kiến trúc lỗi.

### B.3 Sửa R5 — bài tập không tới nơi

`web/src/data/exercises.json` tồn tại (163 bài) nhưng không ai import.

Cách sửa: thêm `exercises` vào store `web/src/stores/course.ts` (import tĩnh `data/exercises.json`), rồi sửa `ChapterView.vue` để lấy `courseStore.exercises` thay vì `courseStore.course.exercises`.

**Quan trọng:** sửa tại **generator** `scripts/build_vue_data.py` để `course.json` **hoặc** một file riêng export được `exercises`, thay vì vá tay file sinh ra. Kiểm tra `scripts/build_vue_data.py` xem nó đã ghi `exercises.json` chưa; nếu ghi rồi thì chỉ cần import đúng file. Nếu chưa ghi, sửa generator để ghi, rồi rebuild.

Sau khi sửa: tab "Kiểm tra hiểu biết" của Chương 2 phải hiện **số bài tập của Chương 2** (không phải 163 của cả sách), kèm lời giải.

### B.4 Sửa R6 — nội dung chương chưa bao giờ hiển thị (quan trọng nhất)

Đây là lỗi nặng nhất: **12 file `web/src/data/chapters/chapter-01..12.json`** chứa toàn bộ nội dung học thuật (block, concepts, equation_rows, figure_rows, mechanisms, summary_html, verification_rows, exercises, sub_nav) nhưng **không được import ở bất kỳ đâu**.

Phân tích trước khi sửa:
1. Đọc `scripts/build_vue_data.py` — xác định file này sinh ra `course.json` và `chapters/chapter-XX.json` từ nguồn nào (`03_chapter_analyses/`, `html/data/`, hay gì khác).
2. Đọc `web/src/views/ChapterView.vue` và 7 file `web/src/components/tabs/*.vue` — xác định tab nào đang cần dữ liệu nào.
3. Đọc `web/src/data/chapters/chapter-02.json` — xác định **shape thật** của nội dung chương.

Sau đó, nối dữ liệu thật vào UI. Yêu cầu:

- Dùng `import.meta.glob('@/data/chapters/*.json', { eager: true })` để nạp 12 file.
- `ChapterView.vue` phải nhận **cả** hai nguồn: metadata từ `course.json` (dùng cho breadcrumb, điều hướng, trạng thái) và nội dung từ `chapter-XX.json` (dùng cho các tab).
- Mỗi tab (`OverviewTab`, `TheoryTab`, `MechanismTab`, `EquationsTab`, `ExamplesTab`, `LabTab`, `CheckTab`) phải **render nội dung thật** từ `chapter-XX.json` thay vì placeholder hiện tại ("Mô hình dựa trên các giả định từ sách.", "Các biến tương tác lẫn nhau để tạo ra kết quả cân bằng.").

**Đây là khối lượng công việc lớn nhất của toàn bộ bộ prompt.** Nếu không thể hoàn thành cả 7 tab, ưu tiên theo thứ tự: `Overview` → `Theory` → `Mechanism` → `Equations` → `Examples` → `Check` → `Lab` (lab xử lý ở prompt 07).

- **Cấm** tự chế nội dung học thuật mới. Chỉ render cái đã có trong `chapter-XX.json` và registry, với nhãn bằng chứng đúng.
- Nếu `chapter-XX.json` cho chương N **không tồn tại** (chương 13–20 chưa phân tích) — xử lý ở prompt 07, không tự bịa.

### B.5 Sửa R7 — tab Phòng thí nghiệm

`LabTab.vue` chỉ hiện danh sách id lab. Cần render lab thật.

**Nguồn có sẵn, đã verify:** 7 file lab đã qua kiểm thử parity Python↔JS (21/21 test node) ở `html/assets/labs/`:
`consumer-choice.js`, `elasticity.js`, `monopoly.js`, `production.js`, `profit-max.js`, `supply-demand.js`, `welfare.js`.

Chúng là IIFE gắn vào global: `root.MICLabs["supply-demand"] = { ... }` (xem `html/assets/labs/supply-demand.js:221-222`) và phụ thuộc `root.MICCore` từ `html/assets/lib/core.js` (`linspace`, `pyRound`, …).

Hai lựa chọn — **chọn A, trừ khi gặp trở ngại kỹ thuật**:

- **Phương án A (ưu tiên):** chuyển 7 file lab + `core.js` sang `web/src/lib/labs/` dưới dạng **ES module** (export `compute`, `params`, `render` thay vì gắn global), import vào `LabTab.vue`. Giữ nguyên logic toán học **tuyệt đối** — chỉ đổi cơ chế xuất/nhập module. Test parity (`tests/labs-parity.test.mjs`) phải vẫn xanh sau khi chuyển.
- **Phương án B:** nạp các file legacy bằng `<script>` tag vào `index.html` (chạy trước app), đọc `window.MICLabs`. Nhanh hơn nhưng để lại global — chỉ chấp nhận nếu A bị chặn, và phải nêu lý do.

Ràng buộc:
- **Không** viết lại công thức lab. Port nguyên vẹn.
- Lab phải **chạy được**: có điều khiển tham số, nút tính, hiển thị kết quả, cảnh báo khi tham số vô nghĩa (ví dụ `b <= 0`).
- Tham số mặc định phải cho kết quả **khớp số liệu sách** (đã có sẵn trong lab).
- Xử lý lỗi: `compute` có thể `throw` — phải bắt và hiển thị thông báo, không làm sập trang.

### B.6 Sửa R8 — chuỗi `undefined`

Trong tab "Ví dụ & biểu đồ", chuỗi `undefined` hiện ra giữa tiêu đề và phần mô tả. Tìm chỗ render thiếu guard, sửa bằng `?? '—'` hoặc bằng điều kiện hiển thị.

Sau khi sửa: **không** còn chuỗi `undefined` hay `NaN` hay `[object Object]` trong text render của bất kỳ tab nào của bất kỳ chương nào.

### B.7 Sửa R9 — reactivity

`web/src/views/ChapterView.vue:72`: `const chapterNumber = Number(route.params.number ?? '1')` — đọc một lần.

Sửa thành `computed` + `watch` để đổi chương thì nội dung đổi theo, và reset `activeTab`/tab con nếu cần.

### B.8 PHẦN B — Acceptance criteria

| # | Tiêu chí | Bằng chứng bắt buộc |
|---|---|---|
| B1 | `/phuong-trinh` hiện **> 0** dòng phương trình (mục tiêu: 56 theo `registry.json`) | Số dòng đếm được |
| B2 | `EquationsTab` trong từng chương hiện phương trình của **đúng chương đó** | Số dòng + vài `equation_id` |
| B3 | Tab "Kiểm tra hiểu biết" của Chương 2 hiện bài tập của Chương 2 (không phải 0, không phải 163) | Số câu + vài nội dung |
| B4 | Tab "Tổng quan" của Chương 2 hiện nội dung **từ `chapter-02.json`** (không còn placeholder "Mô hình dựa trên các giả định từ sách.") | Dump text 2 bản: trước/sau |
| B5 | 12 chương đều render nội dung; không chương nào rỗng | Script quét 12 route, dump độ dài text |
| B6 | **Không** còn chuỗi `undefined` / `NaN` / `[object Object]` trong text render | Script quét 12 route |
| B7 | Điều hướng `ch2` → `ch3` đổi nội dung | Dump text 2 lần |
| B8 | Tab "Phòng thí nghiệm" của Chương 2 có **select tham số + nút tính**, bấm ra kết quả số | Screenshot + giá trị số |
| B9 | `node --test "tests/*.test.mjs"` vẫn xanh (≥ 21/21) | Output |
| B10 | `python -m pytest tests -q` vẫn xanh | Output |
| B11 | `npm --prefix web run typecheck` pass | Output |
| B12 | `npm --prefix web run build` pass, `dist/` serve được | Output |

---

## 1.3. Điều kiện DONE cho PROMPT 01

- Tất cả A1–A9 và B1–B12 đạt.
- Cả hai ứng dụng **thực sự hiển thị nội dung**, không chỉ "build không lỗi".
- Không còn dữ liệu nào chết (file JSON nào có trong `data/`/`web/src/data/` mà không ai import → phải nêu trong báo cáo, đã nối hoặc đã giải thích).
- Báo cáo đúng mẫu §0.4.

**Bằng chứng bắt buộc trong báo cáo:** baseline trước khi sửa (số dòng bảng, số câu hỏi, số thẻ chương) và số sau khi sửa, để chứng minh có cải thiện thật.
