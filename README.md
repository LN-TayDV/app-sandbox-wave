# Dự án nghiên cứu: International Financial Wave–Sandpile Theory (IFWST)

**Tên tiếng Việt:** Khung lý thuyết sóng tài chính quốc tế kết hợp mô hình đống cát tài chính.

**Thư mục gốc:** `C:\Users\PC\Documents\AI_project\sandbox-financial`

**Ngôn ngữ nghiên cứu và luận văn:** Tiếng Việt.

**Sản phẩm cuối cùng:** Một luận văn nghiên cứu ngắn có cơ sở lý thuyết, mô hình định lượng, bằng chứng có thể kiểm tra, kết luận trung thực và tài liệu tái lập nghiên cứu.

## Cấu trúc thư mục (mục tiêu)

```text
sandbox-financial/
├── README.md
├── PROJECT_STATUS.md
├── RESEARCH_MANIFEST.md
│
├── 00_project_management/
│   ├── research_charter.md
│   ├── research_questions.md
│   ├── scope_and_boundaries.md
│   ├── methodology.md
│   ├── decision_log.md
│   ├── task_backlog.md
│   └── completion_checklist.md
│
├── 01_literature/
├── 02_theory/
├── 03_model/
├── 04_data/
├── 05_code/
├── 06_experiments/
├── 07_case_studies/
├── 08_results/
├── 09_thesis/
├── 10_quality_assurance/
└── logs/
```

Thư mục chỉ được tạo khi có công việc thực tế cần lưu vào đó (theo PHẦN 6). Không tạo thư mục rỗng.

## Quy tắc quản lý (PHẦN 6)

1. Tách biệt tài liệu gốc, dữ liệu gốc, dữ liệu đã xử lý, mã nguồn và kết quả.
2. Ghi nguồn, ngày truy cập và phương pháp xử lý dữ liệu.
3. Lưu cấu hình môi trường và tham số của từng lần chạy.
4. Không ghi đè kết quả thực nghiệm cũ mà không giữ lịch sử.
5. Sử dụng đường dẫn tương đối trong mã khi có thể.
6. Không lưu thông tin xác thực hoặc API key trong kho mã.
7. Hạn chế tạo tài liệu trùng lặp.
8. Duy trì nhật ký quyết định và trạng thái dự án.
9. Nếu có Git, sử dụng để theo dõi thay đổi mà không phá hủy lịch sử có sẵn.
10. Mọi kết quả được sử dụng trong luận văn phải truy xuất ngược được tới nguồn, mã hoặc phép tính đã tạo ra nó.

## Giai đoạn thực thi (PHẦN 14)

- Giai đoạn 0 — Kiểm kê dự án (đang thực hiện)
- Giai đoạn 1 — Tổng quan tài liệu
- Giai đoạn 2 — Khung lý thuyết
- Giai đoạn 3 — Đặc tả mô hình
- Giai đoạn 4 — Dữ liệu
- Giai đoạn 5 — Thực nghiệm
- Giai đoạn 6 — Viết luận văn
- Giai đoạn 7 — Kiểm định cuối

## Tài liệu tham khảo trong dự án

- `tasks/init-task.md` — Mệnh lệnh nghiên cứu tổng thể (bản gốc, không được sửa).
