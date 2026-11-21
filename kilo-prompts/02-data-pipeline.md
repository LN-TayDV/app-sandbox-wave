# PROMPT 02 — DATA PIPELINE (ĐƯỜNG ỐNG DỮ LIỆU & TÍNH TÁI LẬP)

> **Mã repo:** `MACRO` và `MICRO` — hai phần độc lập.
> **Phụ thuộc:** `00-shared-contract.md`, `01-root-cause-recovery.md`.

> ### Đường dẫn làm việc
> **`MACRO`** → `C:\Users\PC\Documents\AI_project\sandbox-financial\research\advanced-macroeconomics-fourth-edition`
> **`MICRO`** → `C:\Users\PC\Documents\AI_project\sandbox-financial\research\microeconomics-pindyck-rubinfeld`
> **Hợp đồng** → `C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts\00-shared-contract.md`
> **Ma trận thực thi** → `C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts\EXECUTION-MATRIX.md`
> **Mục tiêu:** bảo đảm mọi dữ liệu trong app đều **sinh ra từ nguồn kiểm chứng được**, và build lại cho ra **cùng** kết quả.

---

## 2.0. Vấn đề gốc

Sau prompt 01, app đã tải được dữ liệu. Nhưng nếu quy trình sinh dữ liệu không bị ràng buộc, mỗi lần sửa nội dung sẽ tạo ra app **không tái lập được**: dữ liệu JSON trong `web/src/data/` và `data/` bị sửa tay, generator không tái tạo được, và test không bắt được sai lệch.

Nguyên tắc bắt buộc:

> **Không sửa tay file dữ liệu sinh ra. Sửa generator, rebuild, commit kết quả.**

Đây là nguyên tắc dễ vi phạm nhất — Kilo sẽ bị kéo về phía sửa nhanh file JSON. Phải chống lại điều đó ở từng bước.

---

## 2.1. PHẦN A — `MICRO`

### A.1 Lập bản đồ generator (đọc trước, không sửa ngay)

Đọc và ghi lại sơ đồ nguồn→đích cho từng script trong `scripts/`:

| Script | Đọc từ | Ghi ra | Có chạy tự động? |
|---|---|---|---|
| `build_vue_data.py` | ? | `web/src/data/*.json` | ? |
| `build_app_data.py` | ? | `html/data/*.js` | ? |
| `build_app_shells.py` | ? | `html/*.html` | ? |
| `build_chapter_map.py` | ? | ? | ? |
| `build_chunks.py` | PDF | `extracted/chunks/` | ? |
| `extract_pdf.py` | PDF | `extracted/pages/` | ? |
| `validate_html.py` | — | báo cáo | — |

Kết quả bản đồ này là **deliverable bắt buộc** của phần A. Ghi vào `docs/DATA_PIPELINE.md` (tạo mới nếu chưa có) — nếu `docs/` đã có, bổ sung mục, không tạo file trùng lặp.

### A.2 Xác định chuỗi build chuẩn

Từ bản đồ, xác định **thứ tự chạy đúng** của các script để tái tạo `web/src/data/` từ sạch. Viết thành một lệnh duy nhất.

Yêu cầu: tạo `scripts/build_all.py` (hoặc shell script) chạy đúng thứ tự đó, **không** phá vỡ dữ liệu hiện có, và in ra thông báo rõ ràng từng bước.

### A.3 Tính tái lập (reproducibility check)

Chạy thử trên bản sao (không phá bản gốc):

```bash
cd "C:\Users\PC\Documents\AI_project\sandbox-financial\research\microeconomics-pindyck-rubinfeld"
```

1. Sao lưu `web/src/data/` ra thư mục tạm.
2. Chạy chuỗi build.
3. So sánh file-by-file với bản sao.

**Tiêu chí:** build phải **tái tạo giống hệt** file đã có, hoặc chỉ khác ở những thay đổi **có chủ đích** mà bạn vừa thực hiện (nếu không có thay đổi chủ đích thì phải giống 100%).

Nếu có khác biệt do timestamp/random → sửa generator để **deterministic** (sắp xếp key, cố định thứ tự, bỏ timestamp). Đây là điều kiện bắt buộc để test hồi quy chạy ổn định.

### A.4 Bảo toàn registry và nhãn bằng chứng

`04_theory_registry.csv`, `05_equation_registry.csv`, `06_figure_table_registry.csv` là nguồn chuẩn. Đảm bảo generator đọc chúng và phát ra `web/src/data/registry.json` mà **không làm mất** trường nào.

Kiểm tra tương thích trường: `registry.json` hiện có `theories` (87), `equations` (56), `figures` (65). Mỗi record giữ `chapter_id` dạng `"Ch2"`, `printed_page`, `pdf_page`. Không được đổi tên trường mà không cập nhật toàn bộ nơi đọc.

Nếu có record trong CSV mà `registry.json` **không** có → đó là dữ liệu mất. Phải phục hồi, không phải "chấp nhận thiếu".

### A.5 Acceptance — `MICRO`

| # | Tiêu chí |
|---|---|
| A1 | `docs/DATA_PIPELINE.md` mô tả đủ chuỗi build, đúng thứ tự |
| A2 | `scripts/build_all.py` chạy từ đầu không lỗi |
| A3 | Build lại cho ra file **giống hệt** bản đang có (hoặc chỉ khác ở thay đổi chủ đích, đã liệt kê) |
| A4 | Số record `registry.json` **không giảm**: theories ≥ 87, equations ≥ 56, figures ≥ 65 |
| A5 | Không mất trường nào so với CSV nguồn |
| A6 | Build **deterministic**: chạy 2 lần cho kết quả giống nhau |
| A7 | `python -m pytest tests -q` xanh |

---

## 2.2. PHẦN B — `MACRO`

### B.1 Lập bản đồ generator

`MACRO` có pipeline khác hình dạng: dữ liệu nằm ở `data/` (12 chương, `data/learning/`, `data/equations/`, `data/models/`, `data/labs/`, `data/graph/`, `data/matrices/`, `data/scientific/`, `data/audit/`, `data/dictionaries/`, `data/chapters/`, `data/_source/`).

Có script `scripts/validate_app_data.py` (chạy bằng `npm run test:data`).

Đọc `data/manifest.json` và `scripts/validate_app_data.py` — manifest có vẻ là **hợp đồng** giữa pipeline và app (test hiện có kiểm tra "Mọi payload mà manifest khai báo đều tồn tại").

Xác định: manifest được sinh ra bởi script nào, hay viết tay? App đọc manifest ở đâu?

Ghi bản đồ vào `docs/DATA_PIPELINE.md` của `MACRO` (tạo mới nếu chưa có).

### B.2 Bảo toàn `manifest.json` làm hợp đồng

`manifest.json` khai 8 tab theo thứ tự `['overview','explorer','graph','equations','chapters','models','tables','experiments']` — phải khớp router. Test hiện có đã kiểm tra điều này.

Sau khi sửa bất kỳ thứ gì liên quan tab/data, **phải giữ** manifest và router đồng bộ. Nếu prompt nào sau đổi số tab, phải cập nhật manifest **và** test.

### B.3 Kiểm tra chéo dữ liệu chương

`data/learning/` có 12 file `ch1..ch12.json` + `index.json`. `data/chapters/` là lớp nghiên cứu gốc.

Viết kiểm tra: mỗi chương trong `index.json` phải có file `data/learning/<id>.json` tương ứng, và mỗi chương phải có **câu hỏi trung tâm, chủ đề, bài học, câu hỏi tự kiểm tra, thuật ngữ, điểm kết** — như test hiện có đã kiểm tra.

Nếu chạy lại test thấy thiếu, **sửa dữ liệu**, không sửa test để cho qua.

### B.4 Acceptance — `MACRO`

| # | Tiêu chí |
|---|---|
| B1 | `docs/DATA_PIPELINE.md` mô tả chuỗi build của `MACRO` |
| B2 | `scripts/validate_app_data.py` xanh |
| B3 | 12 chương: `index.json` ↔ `data/learning/*.json` khớp 1-1 |
| B4 | Mỗi chương có đủ 6 thành phần nội dung bắt buộc |
| B5 | Mọi `chapter_id` trong `data/equations/`, `data/models/`, `data/labs/` trỏ tới chương có thật |
| B6 | `manifest.json` khớp router, 8 tab, đúng thứ tự |
| B7 | `npm --prefix web run test` xanh |

---

## 2.3. Quy tắc chung cho cả hai phần

- **Cấm** sửa tay file JSON sinh ra. Mọi thay đổi dữ liệu phải qua generator.
- **Cấm** xóa dòng registry để làm test xanh.
- **Cấm** thêm `timestamp`/random vào output.
- Nếu generator hiện tại chỉ hỗ trợ 12 chương của `MICRO` (C13–C20 chưa có) — đó là **giới hạn đã biết**, ghi vào báo cáo và xử lý ở prompt 07, **không** tự tạo dữ liệu cho các chương đó.
- Nếu phát hiện generator và file sinh ra **không khớp** (data cũ hơn generator) → báo cáo, rebuild, và so sánh diff. Không âm thầm chọn một bên.
