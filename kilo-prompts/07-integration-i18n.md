# PROMPT 07 — INTEGRATION / i18n / NỘI DUNG CHƯA CÓ (CHƯƠNG 13–20)

> **Mã repo:** `MACRO` và `MICRO` — hai phần độc lập.
> **Phụ thuộc:** `00-shared-contract.md`, `01`–`06`.

> ### Đường dẫn làm việc
> **`MACRO`** → `C:\Users\PC\Documents\AI_project\sandbox-financial\research\advanced-macroeconomics-fourth-edition`
> **`MICRO`** → `C:\Users\PC\Documents\AI_project\sandbox-financial\research\microeconomics-pindyck-rubinfeld`
> **Hợp đồng** → `C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts\00-shared-contract.md`
> **Ma trận thực thi** → `C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts\EXECUTION-MATRIX.md`
> **Mục tiêu:** khép kín mọi khoảng trống tích hợp; xử lý chương chưa có nội dung; đảm bảo hai app không bao giờ lẫn dữ liệu.

---

## 7.0. Ba việc còn lại

1. **Tích hợp chéo** — mọi dữ liệu, lab, phương trình, bài tập phải nối được với nhau bằng link/traverse; không có nội dung "mồ côi".
2. **i18n** — bảo đảm toàn bộ chuỗi hiển thị là tiếng Việt, đúng encoding, đúng thuật ngữ chuyên ngành.
3. **Khoảng trống nội dung** — `MICRO` có **12/19 chương trỏ tới lab không tồn tại** (20 lab khai, chỉ 7 có file JS thật) và **8 chương (C13–C20)** chưa có phân tích. Xử lý trung thực.

---

## 7.1. PHẦN A — `MICRO`: nhiều chương trỏ lab không tồn tại

### A.1 Hiện trạng đã xác minh

`web/src/data/course.json` khai **19 chương**, tổng cộng **20 id lab**. Trong `html/assets/labs/` chỉ có **7 file JS thật** → **12/19 chương trỏ lab chết**, tức **13 lab không có mã nguồn**.

| # | Lab | Chương | File JS |
|---|---|---|---|
| 1 | `price-index` | Ch1 | ❌ chết |
| 2 | `supply-demand` | Ch2 | ✅ |
| 3 | `elasticity` | Ch2 | ✅ |
| 4 | `consumer-choice` | Ch3 | ✅ |
| 5 | `income-substitution` | Ch4 | ❌ chết |
| 6 | `risk-insurance` | Ch5 | ❌ chết |
| 7 | `production` | Ch6 | ✅ |
| 8 | `cost-curves` | Ch7 | ❌ chết |
| 9 | `profit-max` | Ch8 | ✅ |
| 10 | `welfare` | Ch9 | ✅ |
| 11 | `monopoly` | Ch10 | ✅ |
| 12 | `price-discrimination` | Ch11 | ❌ chết |
| 13 | `oligopoly` | Ch12 | ❌ chết |
| 14 | `game-theory` | Ch13 | ❌ chết |
| 15 | `factor-markets` | Ch14 | ❌ chết |
| 16 | `capital-markets` | Ch15 | ❌ chết |
| 17 | `general-equilibrium` | Ch16 | ❌ chết |
| 18 | `asymmetric-info` | Ch17 | ❌ chết |
| 19 | `externalities-public-goods` | Ch18 | ❌ chết |
| 20 | `behavioral` | Ch19 | ❌ chết |

**7 lab có file thật** (đã verify parity Python↔JS): `supply-demand`, `elasticity`, `consumer-choice`, `production`, `profit-max`, `welfare`, `monopoly`.

**13 lab chết** — trong đó 3 lab (`price-index`, `income-substitution`, `risk-insurance`) là lab kinh điển, nên **có thể** port được từ `scripts/scientific/models.py`. 10 lab còn lại (`cost-curves` → `behavioral`) nằm ở các chương chưa được phân tích → nhiều khả năng **không** có mô hình Python; khi đó hiển thị empty state trung thực.

**Kilo vẫn phải lập lại bảng 2 chiều** ở đầu phần này để xác nhận trạng thái hiện tại chưa đổi, và ghi bảng đó vào báo cáo. Nếu số liệu khác bảng trên → repo đã thay đổi, dùng số đo mới làm chuẩn và ghi rõ trong báo cáo.

### A.2 Nguyên tắc xử lý

**Không** tạo lab giả. **Không** trỏ tới file không tồn tại. **Không** xóa lab khỏi khai báo một cách âm thầm.

Với mỗi chương, áp dụng **đúng một** trong bốn cách xử lý sau, theo thứ tự ưu tiên:

| Tình huống | Cách xử lý |
|---|---|
| Lab có file JS thật | **Port** sang Vue (đã làm ở prompt 01/05). Hiển thị đầy đủ. |
| Lab có mô hình trong `scripts/scientific/models.py` nhưng chưa có bản JS | **Port** từ Python sang JS theo đúng quy ước `compute_supply_demand` (xem `html/assets/labs/supply-demand.js` — file này ghi rõ nó là bản port trực tiếp từ `scripts/scientific/models.py#compute_supply_demand`). Yêu cầu parity test. |
| Chưa có cả Python lẫn JS | **Hiển thị empty state**: "Chương N chưa có phòng thí nghiệm đã xác minh" + trỏ về `13_task_registry.md` (dòng task tương ứng). Không hiện link chết, không hiện danh sách rỗng. |
| Lab có mô hình nhưng chưa có đặc tả tham số UI | **Hiển thị lab ở chế độ chỉ đọc**: công thức + kết quả với tham số mặc định, ghi rõ "chưa có bộ tham số tương tác" + trỏ registry. |

### A.3 Bổ sung lab còn thiếu (nếu có nguồn)

Phần port lab đã được xử lý ở **prompt 05 (B.4, Nhóm 2)**. Ở đây chỉ **kiểm chứng lại** kết quả đó:

1. Đọc bảng đối chiếu 2 chiều mà prompt 05 đã nộp.
2. Xác nhận **mọi** id lab trong `course.json` giờ đều resolve được tới module thật **hoặc** được đánh dấu trạng thái rõ ràng.
3. Với lab còn thiếu **có** mô hình Python trong `scripts/scientific/models.py` nhưng chưa được port ở prompt 05 → port bổ sung tại đây, theo đúng 3 bước:
   - Port sang `web/src/lib/labs/<id>.js` theo pattern của 7 lab đã có.
   - Thêm test parity Python↔JS trong `tests/labs-parity.test.mjs`.
   - Wire vào `course.json` **qua generator** `scripts/build_vue_data.py`.

**Chỉ làm khi có mô hình Python thật.** Liệt kê các hàm `compute_*` có sẵn trong `scripts/scientific/models.py` để đối chiếu.

### A.4 Acceptance — `MICRO`

| # | Tiêu chí | Bằng chứng |
|---|---|---|
| A1 | Bảng đối chiếu 2 chiều: `course.json` ↔ file lab thật | Bảng 20 lab (baseline: 7 có file, 13 chết) |
| A2 | **0** lab id trong `course.json` trỏ tới lab không tồn tại mà vẫn hiện link chết | Script kiểm tra mọi route |
| A3 | Mỗi chương trong 19 chương: hoặc có lab chạy được, hoặc có empty state rõ ràng | Screenshot mẫu 4 chương (có lab / không lab) |
| A4 | Mọi lab được port mới có test parity | Output `node --test` |
| A5 | Lab còn thiếu **không** bị xóa khỏi khai báo — được đánh dấu trạng thái | Grep + bảng |

---

## 7.2. PHẦN B — `MICRO`: chương 13–20 chưa có phân tích

### B.1 Hiện trạng

- `web/src/data/chapters/` chỉ có `chapter-01..12.json`.
- `03_chapter_analyses/` có phân tích cho 12 chương.
- `13_task_registry.md` ghi MIC-C13…MIC-C20 là TODO.
- `course.json` khai 19 chương, trong đó chương 13–19 có `status` / `available` phản ánh chưa sẵn sàng.

### B.2 Xử lý

**Không** tạo nội dung học thuật cho chương 13–20. Không có nguồn đã xác minh thì không được viết.

Yêu cầu cho mỗi chương 13–20:
1. Trang chương vẫn **mở được** (không 404, không trắng).
2. Hiển thị trạng thái trung thực: "Chương N chưa có nội dung đã xác minh" kèm:
   - Câu hỏi trung tâm (nếu `course.json` có) — đây là metadata, dùng được.
   - Phạm vi trang in/PDF (nếu có).
   - Trỏ tới `13_task_registry.md`.
3. Các tab không có dữ liệu → empty state chuẩn (không trắng, không `undefined`).
4. Lab của các chương này → xử lý theo A.2.
5. Điều hướng chương trước/sau vẫn hoạt động xuyên qua vùng này (chương 12 → 13 → 14).

Nếu `13_task_registry.md` có nội dung mô tả phạm vi chương 13–20 đủ để hiển thị "chương này sẽ phân tích gì" — được hiển thị **kèm nhãn** rõ ràng là kế hoạch, **không phải** nội dung đã xác minh.

### B.3 Acceptance — `MICRO`

| # | Tiêu chí | Bằng chứng |
|---|---|---|
| B1 | `/chuong/13`…`/chuong/20` mở được, hiện trạng thái trung thực | Screenshot 2 chương |
| B2 | Mỗi tab của chương 13–20 có empty state, không trắng | Screenshot 1 chương × 7 tab |
| B3 | 0 chuỗi `undefined`/`NaN` ở chương 13–20 | Script quét |
| B4 | Có liên kết tới `13_task_registry.md` | Kiểm tra trong DOM |
| B5 | Điều hướng ch12 → ch13 → ch14 hoạt động | Click + dump |

---

## 7.3. PHẦN C — i18n & thuật ngữ (cả hai repo)

### C.1 Bảng thuật ngữ chuẩn

Hai cuốn sách dùng thuật ngữ **khác nhau cho cùng một khái niệm** — phải giữ đúng thuật ngữ của từng sách, không hợp nhất:

| Khái niệm | `MICRO` (Pindyck & Rubinfeld) | `MACRO` (Romer 4e) |
|---|---|---|
| Cung | cung (supply) | supply / cung |
| Cầu | cầu (demand) | demand / cầu |
| Độ co giãn | độ co giãn (elasticity) | elasticity / độ co giãn |
| Hàm sản xuất | hàm sản xuất | production function |
| Lợi ích biên | lợi ích biên | marginal benefit |
| Chi phí biên | chi phí biên | marginal cost |
| Cạnh tranh hoàn hảo | cạnh tranh hoàn hảo | perfect competition |
| Độc quyền | độc quyền | monopoly |
| Công bằng hiệu quả | hiệu quả | efficiency |
| Chu kỳ kinh doanh | chu kỳ | business cycle |
| Hàm sản xuất Cobb-Douglas | — | Cobb-Douglas |
| Tăng trưởng nội sinh | — | endogenous growth |

**Cấm** dùng chung một bảng thuật ngữ cho hai repo.

### C.2 Việc cần làm

1. **Thuật ngữ chuyên ngành:** rà soát chuỗi hiển thị có thuật ngữ sai hoặc dịch vụ — sửa theo bảng trên và bảng thuật ngữ có sẵn trong repo (`MICRO`: `04_catalogs/`; `MACRO`: `data/dictionaries/`).
2. **Số phân biệt:** chuẩn hoá dấu phân cách nghìn (`,` hay `.`) và dấu thập phân — chọn **một** và dùng nhất quán trong từng repo.
3. **Đơn vị:** tiền tệ, %, lượng, thời gian — luôn kèm đơn vị.
4. **Encoding:** toàn bộ file nguồn UTF-8 không BOM. Rà soát lại sau mọi lần sửa (dùng script đếm mojibake ở prompt 01 A.5).
5. **Dấu nháy và ký hiệu:** nhất quán — dùng dấu nháy kép tiếng Việt, không trộn dấu `"` với `«»` vô tội vạ.
6. **Thuật ngữ trong `title`/`aria-label`/`alt`:** cũng phải tiếng Việt.

### C.3 Acceptance — i18n

| # | Tiêu chí | Bằng chứng |
|---|---|---|
| C1 | Bảng thuật ngữ chuẩn cho từng repo, lưu trong repo | File `docs/GLOSSARY.md` hoặc tương đương |
| C2 | 0 mắt xích mojibake trong `web/src/` của cả hai repo | Script đếm, output |
| C3 | 0 mắt xích mojibake trong bundle build của cả hai repo | Script đếm, output |
| C4 | Quy ước số nhất quán trong từng repo | Grep + mẫu 20 số |
| C5 | Mọi thuật ngữ trong bảng khớp đúng sách của repo | Review |

---

## 7.4. PHẦN D — tích hợp chéo & cô lập hai repo

### D.1 Yêu cầu cô lập (kiểm tra nghiêm)

Chạy script kiểm tra trên **cả hai** repo:

```bash
# Trong MACRO: không được có "Pindyck" / "Rubinfeld" / "vi mô" của repo kia
grep -rniE "pindyck|rubinfeld" --include=*.vue --include=*.ts --include=*.json --include=*.md . | grep -v node_modules
# Trong MICRO: không được có "Romer" / "macroeconomics" của repo kia
grep -rniE "romer|macroeconomics" --include=*.vue --include=*.ts --include=*.json --include=*.md . | grep -v node_modules
```

**Ngoại lệ được phép:** chỉ trong file bảo trì/kiểm thử chứng minh sự cô lập (ví d. test tự kiểm tra không trộn). Ghi rõ trong báo cáo.

Kết quả mong đợi: **0** kết quả ngoài ngoại lệ. Nếu có → dọn.

### D.2 Tích hợp chéo trong từng app

Kiểm tra các đường dẫn điều hướng nội bộ sau có **hoạt động** (không phải chỉ tồn tại trong dữ liệu):

| Loại | `MICRO` | `MACRO` |
|---|---|---|
| Chương → lab | Từ tab "Phòng thí nghiệm" tới `/phong-thi-nghiem/:labId` | Từ chương tới `/experiments` |
| Phương trình → chương | Từ `/phuong-trinh` tới chương chứa nó | Từ `/equations` tới chương |
| Mô hình → chương | Từ `/mo-hinh` | Từ `/models` |
| Bài tập → chương | Từ `/bai-tap` | — |
| Nguồn → trang sách | Từ `/nguon` | — |
| Bản đồ tri thức → chương | Từ `/ban-do-tri-thuc` | Từ `/graph` |

Với mỗi đường dẫn: bấm thật trong trình duyệt, xác nhận đến đúng nơi, nội dung khớp. Ghi kết quả vào bảng.

### D.3 Acceptance — tích hợp

| # | Tiêu chí | Bằng chứng |
|---|---|---|
| D1 | 0 vi phạm cô lập giữa hai repo | Output grep cả hai |
| D2 | Mọi đường dẫn tích hợp trong bảng D.2 hoạt động | Bảng kết quả bấm thật |
| D3 | Không có liên kết 404 trong app | Script quét tất cả `href`/`router-link` trên mọi route |
| D4 | Mọi nút điều hướng có phản hồi (không im lặng) | Review |

---

## 7.5. Quy tắc chung

- Không tạo nội dung học thuật cho chương chưa có nguồn — **chỉ** empty state + trỏ registry.
- Không xóa khai báo lab/phương trình để làm app "sạch"; đánh dấu trạng thái thay thế.
- Mọi sửa đổi phải đi qua generator nếu đụng dữ liệu sinh ra.
- Sau phần này, chạy lại **toàn bộ** lệnh test của cả hai repo (§0.8) và dán output.
