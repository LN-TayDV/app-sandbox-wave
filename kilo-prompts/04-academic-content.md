# PROMPT 04 — ACADEMIC CONTENT (NỘI DUNG HỌC THUẬT & BẰNG CHỨNG)

> **Mã repo:** `MACRO` và `MICRO` — hai phần độc lập.
> **Phụ thuộc:** `00-shared-contract.md`, `01`–`03`.

> ### Đường dẫn làm việc
> **`MACRO`** → `C:\Users\PC\Documents\AI_project\sandbox-financial\research\advanced-macroeconomics-fourth-edition`
> **`MICRO`** → `C:\Users\PC\Documents\AI_project\sandbox-financial\research\microeconomics-pindyck-rubinfeld`
> **Hợp đồng** → `C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts\00-shared-contract.md`
> **Ma trận thực thi** → `C:\Users\PC\Documents\AI_project\sandbox-financial\kilo-prompts\EXECUTION-MATRIX.md`
> **Mục tiêu:** mọi câu chữ, phương trình, hình bảng và bài tập hiển thị trong app đều truy nguyên được về nguồn sách, và trạng thái bằng chứng được hiển thị trung thực.

---

## 4.0. Nguyên tắc bất di bất dịch

> **Không có nội dung nào vào app mà không có nguồn truy nguyên.**

Cụ thể, mỗi khối nội dung học thuật phải thoả cả 4 điều kiện:

1. **Có nguồn** — trỏ về trang in hoặc trang PDF cụ thể.
2. **Có nhãn trạng thái bằng chứng** — dùng đúng tập nhãn có sẵn trong repo.
3. **Có nội dung khớp với nguồn** — đối chiếu được, không suy diễn trình bày như sự thật.
4. **Có trạng thái "chưa xác minh" hiển thị trung thực** khi chưa đối chiếu.

**Cấm tuyệt đối:**
- Tự bịa số liệu ví dụ rồi trình bày như trong sách.
- Nâng trạng thái bằng chứng để trang trông hoàn thiện.
- Tạo nội dung cho chương **chưa có phân tích** rồi gắn nhãn như thật.
- Viết nội dung học thuật bằng tiếng Anh trong khi app là tiếng Việt.

---

## 4.1. Tập nhãn bằng chứng — dùng đúng, không tự chế

### `MICRO`

Nhãn đang dùng (đọc từ `web/src/data/course.json` → key `evidence_statuses`, và `04_catalogs/`). Tập nhãn quan sát được trong dữ liệu: `VERIFIED`, `TÍNH TAY`, `CHƯA ĐỐI CHIẾU ẢNH`, `SUY RA`, `CHƯA NHẤT QUÁN`.

Component hiển thị nhãn: `web/src/components/EvidenceLabel.vue` — dùng component này, đừng tự render badge.

### `MACRO`

Nhãn đang dùng: `BOOK_EVIDENCE_VERIFIED`, `DERIVED_VERIFIED`, `NUMERICALLY_VERIFIED`, `FORMULA_UNVERIFIED`, `UNVERIFIED`, `ILLUSTRATIVE`, `DOMAIN_GAP`.

**Trường hợp cụ thể đã xác minh — phải giữ nguyên:** `PT-10-01` giữ trạng thái `FORMULA_UNVERIFIED` theo quy tắc kiểm chứng. Trang chủ hiện đang hiển thị đúng thông báo này. **Không** sửa nó thành `VERIFIED` trừ khi thực sự đối chiếu được với sách.

---

## 4.2. PHẦN A — `MICRO`: nối nội dung chương vào app

### A.1 Bối cảnh

`MICRO` có `03_chapter_analyses/chapter_*.md` cho **12 chương** (C01–C12) — theo `13_task_registry.md`, MIC-C13…MIC-C20 (chương 13–20) vẫn **TODO**.

`web/src/data/chapters/chapter-01..12.json` đã chứa nội dung đã cấu trúc hoá. Prompt 01 (B.4) đã nối file này vào UI.

### A.2 Việc cần làm

**A2.1 — Rà soát độ bao phủ.** Với mỗi chương 1–12, đối chiếu:
- `03_chapter_analyses/chapter_NN_*.md` (nguồn phân tích)
- `web/src/data/chapters/chapter-NN.json` (dữ liệu đã cấu trúc)

Xác định phần nào **đã** vào app và phần nào **chưa**. Lập bảng: chương × §0–§11, đánh dấu có/không.

**A2.2 — Bổ sung phần còn thiếu.** Với mỗi § còn thiếu, trích từ file phân tích `.md` (đã có sẵn, đã kiểm chứng) sang JSON, **không viết lại nội dung mới**.

Yêu cầu kỹ thuật: sửa `scripts/build_vue_data.py` (generator) để sinh ra phần mới, **không** vá tay file JSON.

**A2.3 — Bảo toàn metadata.** Mỗi khối nội dung phải mang:
- `printed_page`, `pdf_page`
- `evidence_status`
- `source_note` (trích dẫn cụ thể)

**A2.4 — Ưu tiên.** Nếu khối lượng lớn, ưu tiên theo thứ tự giá trị học thuật:
1. §0–§2 (nguồn, câu hỏi trung tâm, cấu trúc lập luận) — 12 chương
2. §3–§4 (khái niệm nền tảng, mô hình & phương trình) — 12 chương
3. §6 (cơ chế kinh tế) — 12 chương
4. §7 (ý nghĩa kinh tế, ứng dụng, giới hạn) — 12 chương
5. §9 (bài tập + lời giải) — 12 chương
6. §5, §8, §10–§11

**A2.5 — Chương 13–20: xử lý trung thực.** Không có phân tích → app **phải** hiển thị trạng thái "chưa có nội dung đã xác minh" kèm:
- Trỏ về `13_task_registry.md` (dòng MIC-C13…MIC-C20).
- Không hiện link tới lab chưa có.
- Không hiện danh sách rỗng.

Đây là hành vi **đúng**, không phải lỗi. Nhãn nhãn bằng chứng: `CHƯA ĐỐI CHIẾU ẢNH` hoặc tương đương theo quy ước repo.

### A.3 Acceptance — `MICRO`

| # | Tiêu chí | Bằng chứng |
|---|---|---|
| A1 | Bảng độ bao phủ §0–§11 × 12 chương được nộp trong báo cáo | Bảng Markdown |
| A2 | Mỗi khối nội dung có `printed_page` + `evidence_status` | Script kiểm tra JSON, đếm số block thiếu = 0 |
| A3 | Không có nội dung nào không có nguồn | Rà soát mẫu ≥ 20 block |
| A4 | Chương 13–20 hiển thị "chưa có nội dung" + trỏ registry | Screenshot 2 chương |
| A5 | Số nhãn bằng chứng theo từng giá trị, so sánh trước/sau | Bảng đếm |
| A6 | `python -m pytest tests -q` xanh | Output |
| A7 | `node --test "tests/*.test.mjs"` xanh | Output |

---

## 4.3. PHẦN B — `MACRO`: bảo toàn và kiểm chứng nội dung học thuật

### B.1 Bối cảnh

`MACRO` có `data/learning/ch1..ch12.json` (lớp nội dung học, đã dựng) và `data/chapters/` (lớp nghiên cứu gốc). `scripts/validate_app_data.py` đã kiểm tra nhiều bất biến (52 PASS, 2 INFO, 1 WARN).

Test hiện có kiểm tra: mỗi chương có câu hỏi trung tâm, chủ đề, bài học, câu hỏi tự kiểm tra, thuật ngữ, điểm kết; mọi liên kết tới phương trình trong câu hỏi đều tồn tại; không chứa đường dẫn nội bộ/cờ toàn vẹn/mã pipeline.

### B.2 Việc cần làm

**B2.1 — Trạng thái bằng chứng.** Với mỗi phương trình trong `data/equations/`, kiểm tra trạng thái có nhất quán với bằng chứng trong `data/chapters/` và `data/audit/` không. Lập bảng đếm theo trạng thái.

**B2.2 — Bảo toàn `FORMULA_UNVERIFIED`.** Xác nhận `PT-10-01` vẫn `FORMULA_UNVERIFIED`. Nếu có phương trình khác bị nâng trạng thái vô căn cứ, **hạ lại** và ghi vào báo cáo.

**B2.3 — Trường `ILLUSTRATIVE`.** Mọi số liệu minh họa phải mang nhãn `ILLUSTRATIVE`. Trong UI, số minh họa không được trình bày như số trong sách.

**B2.4 — Kiểm tra liên kết chéo.** Mọi `equation_id` / `model_id` / `lab_id` mà bài học tham chiếu phải tồn tại. Test hiện có kiểm tra một phần — hãy kiểm tra **toàn bộ** các trường tham chiếu, không chỉ trường trong câu hỏi.

**B2.5 — Đối chiếu `data/_source/`.** Thư mục này có thể chứa bản trích nguồn. Với mẫu ≥ 15 phương trình, đối chiếu trực tiếp với nguồn và đính chính nếu sai. **Nếu không đủ bằng chứng để đối chiếu, hạ trạng thái xuống mức trung thực** thay vì giữ mức cao.

### B.3 Acceptance — `MACRO`

| # | Tiêu chí | Bằng chứng |
|---|---|---|
| B1 | Bảng đếm trạng thái bằng chứng trước/sau | Bảng |
| B2 | `PT-10-01` vẫn `FORMULA_UNVERIFIED` | Grep + output test |
| B3 | Mọi `equation_id`/`model_id`/`lab_id` tham chiếu đều tồn tại | Script đếm broken = 0 |
| B4 | ≥ 15 phương trình đã đối chiếu với `data/_source/`, kết quả ghi lại | Bảng đối chiếu |
| B5 | Không có phương trình nào bị nâng trạng thái vô căn cứ | Đối chiếu diff trạng thái |
| B6 | `npm --prefix web run test` xanh | Output |

---

## 4.4. Quy tắc chung

- **Ưu tiên hạ trạng thái bằng chứng còn đúng** hơn là nâng để đẹp. Một `FORMULA_UNVERIFIED` trung thực tốt hơn một `VERIFIED` bịa.
- Khi hạ trạng thái, **ghi lại lý do** trong báo cáo và trong trường `verification_note` của record.
- Không tạo nội dung mới cho chương chưa có phân tích — chỉ hiển thị trạng thái và trỏ registry.
- Nội dung học thuật: tiếng Việt đầy đủ, có dấu. Identifier: tiếng Anh.
- Mọi con số hiển thị phải là số hữu hạn, làm tròn nhất quán (repo `MICRO` có `pyRound` trong `html/assets/lib/core.js` — tham chiếu quy ước làm tròn này).
