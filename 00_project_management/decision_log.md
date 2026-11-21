# Decision Log — IFWST

| Ngày | Quyết định | Lý do | Trạng thái |
|------|-----------|-------|-----------|
| 2026-10-17 | Thư mục gốc dự án: `C:\Users\PC\Documents\AI_project\sandbox-financial` | Theo bản mệnh lệnh init-task.md (PHẦN 6, 19) | Đã thực hiện |
| 2026-10-17 | Không tạo thư mục rỗng chưa cần dùng; chỉ tạo thành phần cần thiết cho công việc thực tế | Quy tắc quản lý PHẦN 6 | Đã thực hiện |
| 2026-10-17 | Tạo README.md, PROJECT_STATUS.md, RESEARCH_MANIFEST.md, 00_project_management/* | Đầu ra Giai đoạn 0 theo PHẦN 19 | Đã thực hiện |
| 2026-10-17 | Ngôn ngữ luận văn: Tiếng Việt; tài liệu nguồn: Tiếng Anh và các ngôn ngữ phù hợp khác | Theo init-task.md | Đã thực hiện |
| 2026-10-17 | Trường hợp nghiên cứu trọng tâm đầu tiên: khủng hoảng tài chính toàn cầu 2008 | Theo PHẦN 10 | Đã lập kế hoạch |
| 2026-10-22 | Workflow tổng của dự án gồm 13 bước nằm tại `00_project_management/WORKFLOW.md`; `WORKFLOW.md` ở gốc chỉ áp dụng cho Giai đoạn 5 (mã nguồn `code/01`–`code/07`) | Tránh hai file cùng tên mô tả hai quy trình khác nhau | Đã thực hiện |
| 2026-10-22 | Dựng tầng tri thức dùng chung tại `theory/`: trích xuất **hết** 4 cuốn sách (Hansen Econometrics 2014, Romer Advanced Macroeconomics 4e, Pindyck & Rubinfeld Microeconomics, Madura International Financial Management 11e) làm nền toán học lý thuyết cho mọi phân tích | Kỹ thuật lý thuyết phải tái sử dụng được cho nhiều luận văn và có truy vết nguồn (chương/trang/trạng thái xác minh), không phải trích dẫn theo trí nhớ | Đã thực hiện |
| 2026-10-22 | Thực thi **tuần tự theo pha**: trích xuất tri thức (B1–B7) hoàn tất trước khi làm dữ liệu và viết luận văn; chỉ song song hóa **bên trong** pha trích xuất, theo từng cuốn/chương | Trộn việc đọc sách với viết luận văn và làm dữ liệu khiến mọi phần đều dở dang; ngoài ra phải trích xuất trước khi biết dữ liệu có thật là cam kết 2–3 tuần không có cơ sở | Đã thực hiện |
| 2026-10-22 | Registry là nguồn duy nhất cho mọi phương trình được trích dẫn trong luận văn; mỗi trích dẫn phải có `global_id` + số trang in + số trang PDF + `verification_status` | Tránh sai sót không thể phát hiện khi AI tự nhớ nội dung sách | Đã thực hiện |
| 2026-10-22 | Không sửa `research/microeconomics-pindyck-rubinfeld/` và `research/advanced-macroeconomics-fourth-edition/`; tầng `theory/` chỉ **đọc** từ chúng | Hai repo đã verified (34/34 browser smoke, 75/75 pytest, 21/21 node) — union read-only không gây hồi quy | Đã thực hiện |

2026-10-23T09:46:06.021148 | DECISION | CẦN XỬ LÝ TOÁN HỌC BỔ SUNG — render-diff required before expanding to 4 books (B5 blocked)

2026-10-27 | DECISION | B4 pilot Hansen Ch 7 hoan tat: 87 don vi (da deduplicate tu 94), M1: Level A=20/B=7/C=24 (47.1% Level C can render-diff), M2: ~4.0 gio, M3: 87 don vi, M4: 5/7 kiem tra du lieu PASS. B5 quyet dinh: CAN XU LY TOAN HOC BOI SUNG — khong mo rong sang 4 cuon truoc khi render-diff 24 phuong trinh Level C, rebuild 7 Level B, phan doan trang pdf=182, reconcile validator schema. FILE: theory/PILOT_REPORT.md, theory/docs/CHAPTER_REPORT_HAN_07.md, logs/quality.json