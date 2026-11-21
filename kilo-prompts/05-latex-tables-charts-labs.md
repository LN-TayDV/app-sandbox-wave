# PROMPT 05 — LATEX / TABLES / MATRICES / CHARTS / LABS

> **Mã repo:** `MACRO` và `MICRO` — hai phần độc lập.
> **Phụ thuộc:** `00-shared-contract.md`, `01`–`04`.

> ### Đường dẫn làm việc
> **`MACRO`** → `C:\Users\PC\Documents\AI_project\sandbox-financial\research\advanced-macroeconomics-fourth-edition`
> **`MICRO`** → `C:\Users\PC\Documents\AI_project\sandbox-financial\research\microeconomics-pindyck-rubinfeld`
> **Hợp đồng** → `C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts\00-shared-contract.md`
> **Ma trận thực thi** → `C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts\EXECUTION-MATRIX.md`
> **Mục tiêu:** công thức, bảng, ma trận, biểu đồ và phòng thí nghiệm hiển thị đúng, đẹp, và **chạy được thật**.

---

## 5.0. Phạm vi

Đây là nhóm khả năng "nặng về kỹ thuật trình bày". Tập trung vào 5 thứ:

1. **LaTeX** — công thức toán hiển thị đúng, không lỗi render.
2. **Bảng** — dữ liệu đúng, đọc được, xuất được.
3. **Ma trận** — `MACRO` có `data/matrices/`, hiển thị đúng công thức toán.
4. **Biểu đồ** — dùng ECharts, đúng số liệu, responsive.
5. **Labs** — mô hình chạy được, tham số đổi được, kết quả đúng.

Nguyên tắc chung: **dữ liệu hiển thị phải khớp dữ liệu nguồn đến từng con số.** Một biểu đồ vẽ đúng nhưng gắn sai nhãn trục là lỗi nặng hơn biểu đồ không vẽ.

---

## 5.1. PHẦN A — `MACRO`

### A.1 LaTeX

Repo đã có `web/src/components/MathRenderer.vue` và KaTeX đã bundle (`dist-web/assets/KaTeX_*.woff2` — không dùng CDN, chạy offline).

Việc cần làm:
1. Rà soát mọi chuỗi LaTeX trong `data/equations/`, `data/learning/`, `data/models/`, `data/matrices/`.
2. Tìm chuỗi **không render được**: lệnh sai, `\text` chứa ký tự Unicode lạ, `\begin{}` không đóng, ký hiệu chưa define.
3. Sửa ở **generator/dữ liệu nguồn**, không vá chuỗi lúc render.
4. Thêm guard trong `MathRenderer.vue`: nếu KaTeX lỗi, hiển thị công thức thô kèm cảnh báo nhỏ — **không** render trang trắng.

Tiêu chí đo: script duyệt toàn bộ chuỗi LaTeX, đếm số chuỗi **render lỗi** = 0.

### A.2 Bảng

`MACRO` có `data/` (bảng dữ liệu), `CalculationTable.vue`, và `tests` đã kiểm tra "Bảng đối chiếu mô hình có dữ liệu" (19 dòng).

Việc cần làm:
- Xác nhận mọi bảng có tiêu đề cột tiếng Việt, đơn vị, và nguồn.
- Bảng dài → cần phân trang hoặc cuộn ngang, không làm vỡ layout.
- Số trong bảng phải là số hữu hạn, định dạng thống nhất (số thập phân, dấu phân cách nghìn).
- Kiểm tra "13 dòng có ô bị cắt" mà test báo INFO — đây là **ô bị cắt trong ma trận nguồn**. Phải giữ nguyên việc đánh dấu ô bị cắt (không tự suy đoán), nhưng **hiển thị** phải rõ ràng cho người học biết ô đó bị cắt, không hiện số sai.

### A.3 Ma trận

`data/matrices/` — kiểm tra:
- Ma trận nào là "ô bị cắt" → render bằng dấu hiệu riêng (ví dụ `…`), kèm chú thích.
- Ma trận nào đã đầy đủ → render dạng lưới đẹp, không cắt chữ.
- Kích thước ma trận lớn → cho phép cuộn, không phá layout mobile.

### A.4 Biểu đồ

`MACRO` có `GraphView.vue`, `data/graph/`, `data/scientific/`.

Việc cần làm:
- Mọi chart phải lấy dữ liệu từ `data/` qua store, không hardcode.
- Trục X/Y có nhãn + đơn vị; chú giải đọc được; số liệu không bị che bởi trục.
- Responsive: resize không vỡ; tooltip không tràn khung.
- **Không** dùng CDN — ECharts phải được bundle (repo đã khai dependency `echarts`).

### A.5 Labs

`MACRO` có `data/labs/index.json` với **2 lab**: `lab-solow`, `lab-taylor`. Test hiện có đã kiểm tra mỗi lab có tham số, đầu ra, biểu đồ, trích dẫn phương trình hợp lệ.

Có `assets/js/models/solow.js` và `assets/js/models/taylor-rule.js` (alias `@models`).

Việc cần làm:
- Xác nhận 2 lab chạy thật: đổi tham số → kết quả và biểu đồ **đổi theo**.
- Số liệu mặc định phải khớp bảng đối chiếu mô hình (19 dòng) — đây là bằng chứng kiểm chứng sẵn có.
- Kiểm tra trích dẫn phương trình trong lab có tồn tại thật.
- Thêm lab thứ 3 nếu phù hợp nguồn (`data/labs/` có thêm mẫu chưa dùng) — nhưng chỉ khi lab đó có phương trình đã xác minh.

### A.6 Acceptance — `MACRO`

| # | Tiêu chí | Bằng chứng |
|---|---|---|
| A1 | Số chuỗi LaTeX **render lỗi** = 0 | Script đếm + output |
| A2 | LaTeX lỗi không làm trắng trang (guard hoạt động) | Test nhân bản lỗi + screenshot |
| A3 | Mọi bảng: tiêu đề cột tiếng Việt, có nguồn, số hữu hạn | Script quét + mẫu 5 bảng |
| A4 | Ô bị cắt được đánh dấu rõ, **không** hiện số sai | Screenshot ma trận |
| A5 | Mọi chart dùng dữ liệu từ `data/`, không hardcode | Grep + review |
| A6 | Chart responsive, tooltip không tràn | Screenshot 2 kích thước |
| A7 | Không có CDN trong bundle | Grep `http`/`cdn` trong `dist-web/assets/*.js` |
| A8 | `lab-solow` và `lab-taylor` chạy, đổi tham số → kết quả đổi | Screenshot + 2 cặp số |
| A9 | Số mặc định của lab khớp bảng đối chiếu | Script so sánh |
| A10 | `npm --prefix web run test` + `typecheck` + `build` xanh | Output |

---

## 5.2. PHẦN B — `MICRO`

### B.1 LaTeX

`MICRO` có `web/src/components/EquationPanel.vue` và dữ liệu `equation_latex` trong `registry.json` (56 phương trình) + `equation_rows` trong `chapter-XX.json`.

Việc cần làm:
- Rà soát chuỗi LaTeX, tìm chuỗi lỗi, sửa ở dữ liệu nguồn/generator.
- `MICRO` chưa dùng KaTeX (`package.json` không có `katex`). Cân nhắc thêm `katex` + `katex/dist/katex.min.css` làm dependency — **được phép** ở prompt này (khác với prompt 03, nơi cấm thêm thư viện).
- Nếu thêm KaTeX: phải bundle (không CDN), và thêm guard lỗi render.
- Phân quyền ưu tiên: dùng renderer sẵn có nếu đủ; nếu `EquationPanel.vue` hiện render công thức bằng CSS/Unicode thì **giữ** cách đó, chỉ vá lỗi — đừng viết lại toàn bộ nếu không cần.

### B.2 Bảng

`MICRO` có `web/src/components/DataTable.vue`, dữ liệu `figure_rows`, `verification_rows` trong `chapter-XX.json`, và `data/graph.json`.

Việc cần làm:
- Mọi bảng có tiêu đề cột, đơn vị, nguồn.
- `verification_rows` — bảng đối chiếu bằng chứng: phải hiển thị **nhãn trạng thái** cho từng dòng, dùng `EvidenceLabel.vue`.
- Cột số: định dạng thống nhất, số hữu hạn.
- Bảng dài → cuộn ngang, giữ tiêu đề cột.

### B.3 Biểu đồ

`MICRO` có `web/src/components/InteractiveChart.vue` và `web/src/data/graph.json`.

Việc cần làm:
- Xác nhận chart dùng đúng `graph.json` (không hardcode).
- Trục có nhãn + đơn vị; chú giải đọc được.
- Responsive, không tràn.
- Sửa lỗi hiển thị `undefined` trong tab "Ví dụ & biểu đồ" (R8 ở prompt 01) — nếu chưa xử lý, xử lý ở đây: mọi field truyền vào chart phải qua guard.

### B.4 Labs — phần port lớn nhất

Prompt 01 (B.5) đã port 7 lab có file JS thật sang Vue. Prompt này **hoàn thiện chất lượng** các lab đó, và xử lý 3 lab còn thiếu (mô tả bên dưới).

**Nhóm 1 — 7 lab có file JS thật** (đã verify parity Python↔JS, 21/21 test):

| Lab | Chương |
|---|---|
| `supply-demand` | 2 |
| `elasticity` | 2 |
| `consumer-choice` | 3 |
| `production` | 6 |
| `profit-max` | 8 |
| `monopoly` | 10 |
| `welfare` | 12 |

**Nhóm 2 — 13 lab được khai trong `course.json` nhưng không có file JS:**

| Lab | Chương | Có mô hình Python? |
|---|---|---|
| `price-index` | Ch1 | kiểm tra `models.py` |
| `income-substitution` | Ch4 | kiểm tra `models.py` |
| `risk-insurance` | Ch5 | kiểm tra `models.py` |
| `cost-curves` | Ch7 | nhiều khả năng không |
| `price-discrimination` | Ch11 | nhiều khả năng không |
| `oligopoly` | Ch12 | nhiều khả năng không |
| `game-theory` | Ch13 | nhiều khả năng không |
| `factor-markets` | Ch14 | nhiều khả năng không |
| `capital-markets` | Ch15 | nhiều khả năng không |
| `general-equilibrium` | Ch16 | nhiều khả năng không |
| `asymmetric-info` | Ch17 | nhiều khả năng không |
| `externalities-public-goods` | Ch18 | nhiều khả năng không |
| `behavioral` | Ch19 | nhiều khả năng không |

Với từng lab trong nhóm này, đọc `scripts/scientific/models.py` và tìm hàm `compute_*` tương ứng:
- **Có** mô hình Python → port sang `web/src/lib/labs/<id>.js` theo đúng pattern của 7 lab nhóm 1 (tham chiếu `html/assets/labs/supply-demand.js` — file này ghi rõ nó là bản port trực tiếp từ `scripts/scientific/models.py#compute_supply_demand`). Thêm test parity Python↔JS trong `tests/labs-parity.test.mjs`. Wire vào `course.json` **qua generator** `scripts/build_vue_data.py`.
- **Không** có mô hình Python → hiển thị empty state chuẩn: "Chương N chưa có phòng thí nghiệm đã xác minh" + trỏ `13_task_registry.md`. **Không** tự viết lab mới, **không** xóa lab khỏi khai báo.

Trước khi bắt đầu, lập bảng đối chiếu 2 chiều: id lab trong `course.json` (19 chương, 20 lab) ↔ file lab thật trong `html/assets/labs/` (7 file). Nêu bảng này trong báo cáo — nó là cơ sở để xác nhận không còn lab chết.

**Yêu cầu chất lượng (áp dụng cho mọi lab đã render được):**

1. **Đủ tham số.** Mỗi lab hiện đủ: thanh trượt/select cho **mọi** tham số mà `compute()` đọc (đọc kỹ phần đầu `compute()` của từng file lab — ví dụ `supply-demand.js` đọc `a, b, c, d, f, tax, income, policy, policy_price`).
2. **Hiển thị kết quả đầy đủ:** giá cân bằng, lượng, độ co giãn, hàm lợi ích, so sánh chính sách — đúng những gì `compute()` trả về.
3. **Cảnh báo tham số vô nghĩa.** `compute()` có thể `throw` (ví dụ `b <= 0`). Bắt lỗi, hiển thị thông báo tiếng Việt, **không** sập trang.
4. **Thông báo mô hình ngoài miền.** `supply-demand.js` có cảnh báo "Số lượng cân bằng âm" — phải hiển thị được, đây là bài học học thuật quan trọng.
5. **Parity với Python giữ nguyên.** `tests/labs-parity.test.mjs` đã kiểm tra 21 case. Sau khi port lại lần nữa, test phải vẫn xanh — nếu đỏ, **port sai**, sửa port chứ không sửa test.
6. **Tham số mặc định** phải cho kết quả khớp số liệu sách (đã có sẵn trong lab).
7. **Ghi chú phương pháp:** mỗi lab nên hiển thị công thức và trích dẫn trang sách (nếu lab có sẵn trong file legacy thì giữ; nếu không, ghi "chưa đối chiếu" — không bịa trang).

### B.5 Acceptance — `MICRO`

| # | Tiêu chí | Bằng chứng |
|---|---|---|
| B1 | Số chuỗi LaTeX lỗi = 0 | Script đếm |
| B2 | Bảng `verification_rows` có nhãn trạng thái từng dòng | Screenshot |
| B3 | Chart dùng `graph.json`, không hardcode | Grep + review |
| B4 | **0** chuỗi `undefined`/`NaN` trong mọi chart của mọi chương | Script quét 12 chương |
| B5 | Mọi lab đã render (7 lab nhóm 1, cộng các lab nhóm 2 được port thêm) đủ tham số + nút tính + kết quả; lab không port được phải hiện empty state chuẩn | Screenshot từng lab |
| B6 | Lab có tham số vô nghĩa → hiện cảnh báo, **không** crash | Screenshot 1 lab lỗi |
| B7 | Lab hiện cảnh báo "mô hình ngoài miền" khi applicable | Screenshot `supply-demand` |
| B8 | `node --test "tests/*.test.mjs"` ≥ 21/21 xanh | Output |
| B9 | `python -m pytest tests -q` xanh | Output |
| B10 | `npm --prefix web run typecheck` + `build` xanh | Output |

---

## 5.3. Quy tắc chung

- **Không** dùng CDN cho bất kỳ thư viện nào. Tất cả phải bundle.
- **Không** hardcode số liệu trong component để "cho nhanh" — phải đọc từ data.
- Số hiển thị phải hữu hạn; `NaN`/`Infinity` → hiển thị `—` kèm chú thích.
- Mọi chart phải có nhãn trục và đơn vị. Chart không nhãn trục là lỗi nghiêm trọng trong app học thuật.
- Với `MICRO`, giữ nguyên quy ước làm tròn kiểu Python (`pyRound`) để bảng khớp lớp Python.
- Không sửa logic toán của lab. Port nguyên vẹn — chỉ đổi cơ chế module.
