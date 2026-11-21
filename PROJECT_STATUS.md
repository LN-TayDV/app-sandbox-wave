# Trạng thái dự án — IFWST / CÁT TRUỒI

**Cập nhật lần cuối:** 2026-10-22
**Nguồn chuẩn:** [`00_project_management/WORKFLOW.md`](00_project_management/WORKFLOW.md) — 13 bước, mỗi bước có cổng đạt
**Trang điều hướng:** [`00_project_management/START_HERE.md`](00_project_management/START_HERE.md)

> **Bước hiện tại: BƯỚC 0 — Đồng bộ repo.**

---

## 1. Giai đoạn thực thi học thuật (theo `00_project_management/methodology.md`)

Trạng thái dùng 4 mức: `✅` đạt · `⚠️` một phần · `⬜` chưa bắt đầu.
**Mọi mục đều kèm bằng chứng đường dẫn — không dựa vào file trạng thái khác.**

| GĐ | Tên | Trạng thái | Bằng chứng | Ghi chú |
|---|-----|-----------|-----------|---------|
| 0 | Kiểm kê dự án | ✅ | `README.md`, `PROJECT_STATUS.md`, `RESEARCH_MANIFEST.md`, `00_project_management/*` (7 file) | Hoàn tất 2026-10-17 |
| 1 | Tổng quan tài liệu | ⚠️ | `01_literature/Literature_Sources_Compilation.md` (12.049 B, ~7 nguồn) · `01_literature/sources/` (2 PDF + 2 TXT) · `01_literature/search_log.csv` | **`literature_matrix.csv` RỖNG (309 B = chỉ header)** · `critical_review.md` chưa có · `research_gap.md` chưa có · 7 nhánh A–G trong `tasks/search.md` chưa khảo sát đầy đủ |
| 2 | Khung lý thuyết | ✅ | `02_conceptual_framework/IFWST_Conceptual_Framework.md` (14.020 B) — kiến trúc 3 lớp Wave + Network + Sandpile | Hoàn tất 2026-10-17 19:51 |
| 3 | Đặc tả mô hình | ✅ | `03_model_specification/IFWST_Model_Specification.md` (8.849 B) — M1/M2/M3, tham số, SVD, Sargan, backtest | Hoàn tất 2026-10-17 19:58 · **lỗi typo dòng 232**: `Stata: s пространственный` |
| 4 | Dữ liệu | ⚠️ | `data/raw/` 23 file · `data/processed/ifwst_panel.csv` (714 dòng) · `output/data_quality_report.md` | **Xem §2 — panel hiện dùng biến proxy, sai tần suất** |
| 5 | Thực nghiệm | ⬜ | — | `code/` chỉ có `01`–`07` (data pipeline). **Cần code ước lượng `08`–`16`** |
| 6 | Viết luận văn | ⬜ | — | `09_thesis/` chưa tồn tại |
| 7 | Kiểm định cuối | ⬜ | — | — |

---

## 2. Vấn đề dữ liệu đang mở (chặn GĐ4 và GĐ5)

| # | Vấn đề | Bằng chứng | Xử lý ở |
|---|--------|-----------|---------|
| D1 | **Thiếu 3 nguồn dữ liệu then chốt**: không có `bis_credit.csv`, `bis_crossborder.csv`, `imf_ifs.csv` | `data/raw/` chỉ có `wb_*.csv` + `crisis_dates*.csv` · `code/01_download_bis.py` dòng 52–55 có **fallback về World Bank** ("This is proxy data") | BƯỚC 1 + BƯỚC 10 |
| D2 | **`credit_gap` không phải credit gap BIS.** Là lệch so với trung bình 5 năm **không trung tâm**, không phải HP filter λ=400.000 như `tasks/task_data_collection.md` bước 5 yêu cầu | `code/05_derived_final.py:91-93` | BƯỚC 10 (10.3) |
| D3 | **`sandpile_load` là `1 − capital/10`** — hằng số 0.2 suốt giai đoạn ở Brazil ⇒ biến không có biến động. Không phải "tích lũy tổn thất / bộ đệm" | `code/05_derived_final.py:100-102` · `ifwst_panel.csv` dòng 2–4 | BƯỚC 10 (10.4) |
| D4 | **`network_density` = `trade_openness / max(trade_openness)`** — mở thương chuẩn hóa, **không phải mật độ mạng tài chính**. H4 (sóng/lan truyền) hiện đang đo sai đại lượng | `code/05_derived_final.py:110-111` | BƯỚC 10 (10.4) |
| D5 | **`regime` = `1{gdp_growth > 0}`** — không phải chuyển chế độ boom/bust. H2 (đa thang đo) không kiểm định được | `code/05_derived_final.py:118-119` | BƯỚC 10 (10.4) |
| D6 | **Tần suất NĂM, không phải QUÝ** như `03_model_specification` §5.1 yêu cầu | `ifwst_panel.csv`: 1990–2023, 714 dòng | BƯỚC 10 |
| D7 | **`data_quality_report.md` kết luận "Data is ready for analysis"** nhưng chỉ kiểm missing/range/outlier — **không** kiểm validness cấu trúc, tần suất, hay độ phủ biến then chốt | `output/data_quality_report.md:50-53` | BƯỚC 10 (10.5) |
| D8 | **4 script derived trùng nhau**; bản "final" (14 cột) ≠ producer thật của panel (19 cột, `code/06_panel.py`) | `code/05_derived{,_simple,_v2,_final}.py` | BƯỚC 10 (10.6) |
| D9 | **Thiếu tầng truy vết dữ liệu**: không có `source_registry.csv`, `variable_dictionary.csv`, `formula_registry.csv`, `model_registry.csv` | `data/` chỉ có `raw/` + `processed/` | BƯỚC 10 (10.2) |

---

## 3. Bước trích xuất tri thức (B0–B7) — đường đi mới

Quyết định 2026-10-22 (`00_project_management/decision_log.md`): 4 cuốn sách là **nền toán học lý thuyết dùng chung**, trích xuất **hết** trước khi làm dữ liệu và viết luận văn.

| Bước | Nội dung | Trạng thái |
|------|----------|-----------|
| B0 | Đồng bộ repo | ✅ (phiên này) |
| B1 | Probe khả thi dữ liệu | ⬜ |
| B2 | Dựng `theory/` + pipeline L0/L1/L2 | ⬜ |
| B3 | SOP + Validator | ⬜ |
| B4 | Pilot Hansen Ch 7 | ✅ | theory/PILOT_REPORT.md · theory/docs/CHAPTER_REPORT_HAN_07.md · 87 đơn vị (đã deduplicate) | 2026-10-27 |
| B5 | Trích xuất hết 4 cuốn (4 worker song song) | ⛔ BLOCKED | CẦN XỬ LÝ TOÁN HỌC BỞI SUNG — render-diff 24 phương trình Level C, rebuild 7 Level B, phân đoạn trang pdf=182, reconcile validator schema | |
| B6 | Union + cross-book + index | ⬜ |
| B7 | Audit coverage toàn bộ | ⬜ |

**Sẵn có để tái dùng:** `research/advanced-macroeconomics-fourth-edition/scripts/{inspect_source,extract_pdf}.py` · `research/advanced-macroeconomics-fourth-edition/scientific/registry.py` (4 lớp source/symbolic/numeric/render) · `research/microeconomics-pindyck-rubinfeld/05_equation_registry.csv` (16 cột) và `.../04_theory_registry.csv` (19 cột) — **schema trùng khớp với registry MACRO**, nên union được ngay.

---

## 4. Vấn đề hiện tại (theo thứ tự ưu tiên)

1. **Dữ liệu chưa dùng được cho GĐ5** → 9 vấn đề ở §2. Chặn GĐ4/GĐ5.
2. **Tổng quan tài liệu chưa đủ** → `literature_matrix.csv` rỗng, thiếu `research_gap.md`. Chặn GĐ1 và mọi tuyên bố về đóng góp.
3. **Chưa có bằng chứng nào về tính mới** → chưa đọc toàn văn Luna–Zanforlin (2025), là bằng chứng phản bác mạnh nhất.
4. **Chưa có tầng tri thức dùng chung** → chưa trích xuất 4 cuốn. Bắt đầu ở B1.
5. **File trạng thái mâu thuẫn nhau** → đã xử lý ở B0 (file này).

---

## 5. Bước tiếp theo

**BƯỚC 1 — Probe khả thi dữ liệu (1 ngày).** Tải thử 1 file từ 7 nguồn, ghi `04_data/feasibility_probe.md`. Nếu ≥4/7 dùng được → sang B2. Nếu <3 → thu hẹp phạm vi **trước khi** cam kết 2–3 tuần trích xuất sách.
