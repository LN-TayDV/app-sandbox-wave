# PROMPT 12 — B12: GĐ6 + GĐ7 — VIẾT LUẬN VĂN + KIỂM ĐỊNH CUỐI

> **Đọc trước:** `00-shared-contract.md` · **toàn bộ** `output/` từ B11 · `theory/registry/` · `01_literature/` (B8) · `09_thesis/` (nếu đã có)
> **Bước workflow:** B12 · **Ước lượng:** 2–3 tuần
> **Mục tiêu:** viết luận văn **chỉ dựa trên bằng chứng đã có**, rồi kiểm định mọi thứ trước khi nộp.
> **Cấm:** không viết kết luận trước khi có kết quả. Không bịa số liệu. Không trích dẫn nguồn chưa đọc.

---

## 1. Cấu trúc đề xuất

Đặt trong `09_thesis/`:

```
09_thesis/
  00_front-matter.md        # bìa, tóm tắt, mục lục, danh mục bảng/hình
  01_introduction.md        # vấn đề · câu hỏi · đóng góp · cấu trúc luận văn
  02_literature-review.md   # dựa trên 01_literature/ (B8)
  03_conceptual-framework.md
  04_model.md
  05_data.md
  06_empirical-results.md
  07_discussion.md          # gồm cả kết quả trái kỳ vọng + giới hạn
  08_conclusion.md
  09_appendices.md
  10_references.md
```

## 2. Nguyên tắc viết

| Nguyên tắc | Cụ thể |
|---|---|
| **Bằng chứng trước khẳng định** | Mỗi câu khẳng định học thuật phải có nhãn trạng thái (§0.2 hợp đồng) hoặc trích dẫn cụ thể (trang, `global_id`) |
| **Mọi con số phải truy được** | mỗi số trong luận văn → `output/` hoặc `data/processed/` + tên script sinh ra nó |
| **Không diễn giải quá mức** | kết quả p=0.08 ≠ "chứng minh" |
| **Khoảng trống được thừa nhận** | viết rõ giới hạn của dữ liệu (proxy vs thật), của mô hình, của thiết kế |
| **Thuật ngữ thống nhất** | một khái niệm = một thuật ngữ; dùng bảng thuật ngữ ở `00_front-matter.md` |
| **Tiếng Việt** cho diễn giải; **giữ nguyên tiếng Anh** cho thuật ngữ chuyên ngành, ký hiệu, tên mô hình, công thức |

## 3. Quy trình viết (theo thứ tự, không viết chương 6 khi chưa có kết quả)

1. **Đọc lại toàn bộ bằng chứng**: `output/estimation_log.md`, `output/tables/`, `theory/registry/`, `01_literature/research_gap.md`, `03_model_specification/`.
2. **Lập bảng "claim → bằng chứng"** trước khi viết. Mỗi tuyên bố quan trọng → dòng bằng chứng cụ thể. Claim nào không có bằng chứng → **bỏ hoặc hạ thành giả thuyết**.
3. Viết `01_introduction.md` → `02_literature-review.md` → `03` → `04` → `05` → `06` → `07` → `08`.
4. `09_appendices.md`: đầy đủ phương pháp, định nghĩa biến, bảng phụ, mã nguồn.
5. `10_references.md`: **chỉ** những nguồn đã đọc, có DOI/URL đã kiểm tra.

## 4. GĐ7 — Kiểm định cuối

Chạy **tất cả** các kiểm tra sau trước khi kết luận:

| # | Kiểm tra | Công cụ / cách làm | Đạt khi |
|---|---|---|---|
| 1 | **Trích dẫn** | mọi trích dẫn trong luận văn có trong `10_references.md`; ngược lại mọi mục trong references đều được trích dẫn | 0 lệch 2 chiều |
| 2 | **Số liệu** | mọi con số trong luận văn khớp với `output/tables/` | 100% khớp |
| 3 | **Mã** | `code/13`–`code/16` chạy lại từ đầu → kết quả y hệt | hash giống |
| 4 | **Tính nhất quán** | thuật ngữ, ký hiệu, số chương, mã giả thuyết, số bảng/hình khớp giữa các chương | 0 mâu thuẫn |
| 5 | **Tuyên bố khoa học** | không tuyên bố nào vượt quá bằng chứng | rà từng claim theo bảng claim→bằng chứng |
| 6 | **Bảng/hình** | mọi bảng, hình trong luận văn có nguồn, có caption, đánh số liên tục, được trích dẫn trong nội dung | 100% |
| 7 | **Phụ lục** | đủ để người đọc **tái lập** kết quả chính | đọc thử và làm theo |
| 8 | **Đối chiếu `theory/`** | mọi trích dẫn sách trong luận văn khớp với `theory/registry/` (`global_id` + trang) | 100% |

**Đặc biệt:** kiểm tra 8 là kiểm tra **chống bịa trích dẫn**. Mỗi trích dẫn sách phải khớp một dòng trong `theory/registry/`.

## 5. Acceptance criteria

| # | Tiêu chí | Bằng chứng |
|---|---|---|
| A1 | Đủ 11 file trong `09_thesis/` theo §1 | đọc lại thư mục |
| A2 | Bảng "claim → bằng chứng" tồn tại, **mọi** claim quan trọng có dòng bằng chứng | đọc file |
| A3 | **Không** có tuyên bố nào vượt bằng chứng (rà từng claim) | kết quả rà |
| A4 | 8 kiểm tra GĐ7 đã chạy, kết quả ghi vào `09_thesis/09_appendices.md` hoặc `output/final_audit.md` | đọc file |
| A5 | Kiểm tra 1 (trích dẫn 2 chiều) = 0 lệch | output script |
| A6 | Kiểm tra 2 (số liệu) = 100% khớp | output script |
| A7 | Kiểm tra 3 (mã deterministic) = hash giống | output hash |
| A8 | Kiểm tra 8 (đối chiếu `theory/`) = 100% khớp | output script |
| A9 | Mọi hạn chế đã biết (proxy, thiếu nguồn, EPV thấp) được nêu rõ trong `07_discussion.md` | đọc file |
| A10 | `10_references.md` chỉ chứa nguồn **đã đọc**, DOI/URL đã kiểm tra | output kiểm tra URL |
| A11 | Bảng thuật ngữ thống nhất có trong `00_front-matter.md` | đọc file |
| A12 | `PROJECT_STATUS.md` + `MEMORY.md` + `task_backlog.md` cập nhật: GĐ6/GĐ7 ✅ | đọc lại |

## 6. Cổng đạt

A1–A12 đạt → bộ prompt kết thúc. Tick B12 ✅ trong `00_project_management/WORKFLOW.md` §0.

## 7. Cập nhật trạng thái

`theory/docs/KILO_STATUS.md` · `00_project_management/WORKFLOW.md` §0 · `PROJECT_STATUS.md` · `MEMORY.md` · `logs/execution_log.md` · `00_project_management/task_backlog.md` · `00_project_management/decision_log.md`
