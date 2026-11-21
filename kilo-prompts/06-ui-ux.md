# PROMPT 06 — UI / UX (GIAO DIỆN & TRẢI NGHIỆM HỌC)

> **Mã repo:** `MACRO` và `MICRO` — hai phần độc lập.
> **Phụ thuộc:** `00-shared-contract.md`, `01`–`05`.

> ### Đường dẫn làm việc
> **`MACRO`** → `C:\Users\PC\Documents\AI_project\sandbox-financial\research\advanced-macroeconomics-fourth-edition`
> **`MICRO`** → `C:\Users\PC\Documents\AI_project\sandbox-financial\research\microeconomics-pindyck-rubinfeld`
> **Hợp đồng** → `C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts\00-shared-contract.md`
> **Ma trận thực thi** → `C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts\EXECUTION-MATRIX.md`
> **Mục tiêu:** ứng dụng dùng được, đọc được, điều hướng được — trên cả desktop lẫn mobile, và bằng bàn phím.

---

## 6.0. Nguyên tắc

Một app học thuật chỉ tốt bằng khả năng **đọc và tìm**. Ưu tiên theo thứ tự:

1. **Tìm được** — điều hướng rõ, breadcrumb, tìm kiếm.
2. **Đọc được** — chữ đủ to, tương phản đủ, khoảng cách thoáng, công thức không tràn.
3. **Dùng được** — bàn phím, màn hình nhỏ, không trắng.
4. **Đẹp** — sau cùng, không phải trước.

Không làm lại thiết kế. Cả hai app đã có hệ màu và typography ổn định. **Giữ nguyên design system**, chỉ sửa chỗ hỏng.

---

## 6.1. PHẦN A — `MICRO`

### A.1 Hiện trạng

Layout: header cố định + nav 7 mục (Trang chủ, Các chương, Mô hình, Phương trình, Bản đồ tri thức, Bài tập, Nguồn học thuật). Trang chương: header chương + 7 tab.

Có `web/src/components/` với `EvidenceLabel.vue`, `EquationPanel.vue`, `DataTable.vue`, `InteractiveChart.vue`, `tabs/*.vue`.

### A.2 Việc cần làm

**A2.1 — Điều hướng trên mobile.** Nav 7 mục chắc chắn tràn ở 375px. Kiểm tra ở 375×812: nếu tràn, gộp thành menu hamburger, hoặc cho nav cuộn ngang. Đo bằng screenshot.

**A2.2 — Điều hướng chương.** Kiểm tra nút "chương trước / chương sau" đã tồn tại chưa — `ChapterView.vue` có `prevChapter`/`nextChapter` computed từ `chapter.prev_chapter`/`next_chapter` (chúng **có** trong `chapter-XX.json`, nhưng `course.json` **không** có — xem R6 ở prompt 01). Sau khi nối dữ liệu, phải hiện nút điều hướng chương **hoạt động**.

**A2.3 — Breadcrumb.** Trang chương hiện có "← Các chương /". Giữ, và làm rõ mức: `Trang chủ › Các chương › Chương 2 › §4 Cơ chế`.

**A2.4 — Trạng thái rỗng.** Mọi vùng có thể rỗng (chương chưa có nội dung, chương chưa có bài tập, chương chưa có lab) phải có **empty state có ý nghĩa**:
- Nói rõ **tại sao** rỗng ("chưa có nội dung đã xác minh" ≠ "chưa có dữ liệu").
- Chỉ ra **điều gì sẽ tới** hoặc **trỏ tới registry**.
- Không để trống trơn.

Hiện tại app hiện câu *"Chương này chưa có bài tập tự kiểm tra đã được đăng ký."* — hướng này đúng, nhưng phải **thống nhất** với mọi vùng rỗng khác, và có liên kết điều hướng.

**A2.5 — Tìm kiếm.** App chưa có tìm kiếm (repo có `02_conceptual_framework/` và `data/graph.json` — dữ liệu đủ để tìm). Thêm ô tìm kiếm toàn cục:
- Tìm theo: tên chương, khái niệm, phương trình, mô hình.
- Kết quả nhóm theo loại, bấm → điều hướng tới đúng chương/tab/anchor.
- Gõ xong hiện kết quả tức thì (debounce ~200ms).
- Không tìm thấy → hiện "không có kết quả" gợi ý thay đổi từ khóa.

**A2.6 — Bảng đồ tri thức.** `KnowledgeMapView.vue` — xem nó có thực sự vẽ đồ thị hay chỉ là bảng. Nếu chỉ là bảng, cân nhắc nâng lên đồ thị tương tác dùng `data/graph.json`. Ưu tiên: đảm bảo nó **dùng dữ liệu thật** và điều hướng được tới chương.

**A2.7 — Tiếng Anh ở nơi không nên có.** Trang chủ hiện hiển thị `Advanced Macroeconomics`-style label cho micro? Không — nhưng rà soát toàn bộ: **mọi chuỗi UI** phải tiếng Việt, kể cả nhãn tab, placeholder, tiêu đề bảng, thông báo lỗi. Rà soát `print`/`page` tiếng Anh sót lại.

**A2.8 — Chiều cao & hiển thị tab.** 7 tab có thể tràn ngang ở 375px. Cho tab cuộn ngang hoặc gập thành select.

**A2.9 — Tiêu đề tab trình duyệt.** `document.title` phải đổi theo route (hiện luôn là "Phòng học Kinh tế học vi mô — Pindyck & Rubinfeld"). Dùng `router.afterEach` + `meta.title` (đã thêm ở prompt 03).

### A.3 Acceptance — `MICRO`

| # | Tiêu chí | Bằng chứng |
|---|---|---|
| A1 | Không tràn ngang ở 375×812 (nav, tab, bảng) | Screenshot 375px |
| A2 | Không tràn ở 768px và 1440px | Screenshot 2 size |
| A3 | Nút chương trước/sau hoạt động, dẫn tới đúng chương | Click + dump text |
| A4 | Mọi vùng rỗng có empty state + lý do + hướng dẫn | Screenshot 3 vùng rỗng |
| A5 | Tìm kiếm hoạt động, tìm "độ co giãn" ra kết quả, bấm điều hướng đúng | Screenshot + đường dẫn |
| A6 | Tìm không có kết quả → hiện thông báo phù hợp | Screenshot |
| A7 | `document.title` đổi theo route | Đọc title sau 3 lần điều hướng |
| A8 | Tương phản chữ đạt WCAG AA (4.5:1 cho text thường) | Số đo bằng script |
| A9 | Điều hướng bằng bàn phím: Tab, Enter, Esc hoạt động | Mô tả thao tác + kết quả |
| A10 | 0 chuỗi UI tiếng Anh sót (báo cáo danh sách đã sửa) | Grep + review |
| A11 | `npm --prefix web run typecheck` + `build` xanh | Output |

---

## 6.2. PHẦN B — `MACRO`

### B.1 Hiện trạng

8 tab: `overview`, `explorer`, `graph`, `equations`, `chapters`, `models`, `tables`, `experiments`. Có `stores/ui.ts` (quản lý tab), `views/OverviewView.vue`… `LabView.vue`.

Trang chủ hiện hiển thị mojibake (đã sửa ở prompt 01 A.5) và đếm số liệu sai (`Đã xác minh 0`) do lỗi dữ liệu (đã sửa ở prompt 01).

### B.2 Việc cần làm

**B2.1 — Điều hướng 8 tab.** 8 tab chắc chắn tràn ở mobile. Kiểm tra 375px, sửa bằng cuộn ngang có snap hoặc menu.

**B2.2 — Trạng thái tab phải khớp route.** `stores/ui.ts` giữ tab; router có 8 route. Kiểm tra: click tab → URL đổi → reload giữ đúng tab. Nếu reload mất trạng thái, sửa.

**B2.3 — Vùng rỗng.** Áp dụng cùng chuẩn A2.4: nói rõ lý do, chỉ ra điều gì tới, trỏ registry.

**B2.4 — Trang chủ hiện "PT-10-01 giữ nguyên trạng thái FORMULA_UNVERIFIED theo quy tắc kiểm chứng."** — đây là **hành vi đúng** (minh bạch bằng chứng). Giữ nguyên, nhưng làm rõ bằng nhãn trạng thái chuẩn thay vì text thô, và dẫn tới trang phương trình.

**B2.5 — Tìm kiếm.** `MACRO` có 12 chương + registry phương trình/mô hình/lab — rất phù hợp tìm kiếm. Thêm tìm kiếm toàn cục giống A2.5: tìm chương, phương trình, mô hình, thuật ngữ.

**B2.6 — Bảng dữ liệu & đồ thị tri thức.** `GraphView.vue`, `TablesView.vue` — kiểm tra dùng dữ liệu thật, không trống, điều hướng được.

**B2.7 — Tiêu đề tab trình duyệt.** Đặt theo route, tiếng Việt.

### B.3 Acceptance — `MACRO`

| # | Tiêu chí | Bằng chứng |
|---|---|---|
| B1 | Không tràn ngang ở 375×812 | Screenshot |
| B2 | Click tab → URL đổi; reload → giữ tab | Ảnh chụp trước/sau reload |
| B3 | Mọi vùng rỗng có empty state chuẩn | Screenshot 2 vùng |
| B4 | Tìm kiếm hoạt động (tìm "Solow" ra kết quả) | Screenshot |
| B5 | `document.title` đổi theo route | Đọc 3 lần |
| B6 | Tương phản WCAG AA | Số đo |
| B7 | Điều hướng bàn phím hoạt động | Mô tả + kết quả |
| B8 | 0 chuỗi UI tiếng Anh sót | Grep + review |
| B9 | `npm --prefix web run typecheck` + `test` + `build` xanh | Output |

---

## 6.3. Quy tắc chung

- **Không** đổi bảng màu, font chữ, hay ngôn ngữ thiết kế hiện có. Sửa lỗi hiển thị, không thiết kế lại.
- **Không** thêm animation nặng, không thêm thư viện UI mới.
- Mọi ảnh/chart phải có `alt` hoặc mô tả thay thế tiếng Việt.
- Form nhập (nếu có): có `<label>`, thông báo lỗi gắn với field, không chỉ màu đỏ.
- Ưu tiên sửa ở `web/src/assets/style.css` và component dùng chung, tránh sửa lặp ở từng view.
- Sau khi sửa, kiểm tra ở **3 kích thước**: 375, 768, 1440. Đính kèm screenshot cho mỗi size.
