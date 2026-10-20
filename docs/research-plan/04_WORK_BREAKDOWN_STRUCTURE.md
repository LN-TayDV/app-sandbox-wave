# 04 — Cấu trúc phân rã công việc (WBS)

## Work Packages

### WP0 — Khảo sát hiện trạng & tổ chức dự án
- T0.1 Kiểm kê file hiện có. Đầu ra: danh sách file. Nghiệm thu: báo cáo kiểm kê. Phụ thuộc: none. Độ khó: thấp. Ước lượng: 0.5 ngày. Trạng thái: VERIFIED (thư mục rỗng).
- T0.2 Tạo cấu trúc docs/research-plan. Đầu ra: thư mục + file. Nghiệm thu: tồn tại. Phụ thuộc: T0.1. Độ khó: thấp. Ước lượng: 0.5 ngày. Trạng thái: DONE (đang thực hiện).

### WP1 — Xác định vấn đề, phạm vi, mục tiêu
- T1.1 Viết hiến chương. Đầu ra: 00. Nghiệm thu: mục tiêu/phạm vi/out-of-scope rõ. Phụ thuộc: WP0. Độ khó: trung bình. Ước lượng: 2 ngày.
- T1.2 Xác định phạm vi không gian/thời gian. Đầu ra: quyết định. Nghiệm thu: có giá trị cụ thể. Phụ thuộc: T1.1. Độ khó: trung bình. Ước lượng: UNKNOWN (cần dữ liệu). Trạng thái: DECISION_REQUIRED.

### WP2 — Nền tảng kiến thức
- T2.1 Lập bản đồ kiến thức. Đầu ra: 02. Nghiệm thu: mỗi kiến thức gắn WP. Phụ thuộc: WP1. Độ khó: trung bình. Ước lượng: 3 ngày.
- T2.2 Lập kế hoạch học. Đầu ra: lộ trình học. Nghiệm thu: có thứ tự & đầu ra chứng minh. Phụ thuộc: T2.1. Độ khó: trung bình. Ước lượng: 2 ngày.

### WP3 — Tìm kiếm & tổng quan tài liệu
- T3.1 Xây từ khóa & chiến lược tìm kiếm. Đầu ra: protocol. Nghiệm thu: từ khóa VN/EN. Phụ thuộc: WP1. Độ khó: thấp. Ước lượng: 2 ngày.
- T3.2 Tìm & sàng lọc tài liệu. Đầu ra: danh sách nguồn. Nghiệm thu: ≥? (UNKNOWN). Phụ thuộc: T3.1. Độ khó: cao. Ước lượng: UNKNOWN.
- T3.3 Đọc & trích xuất bằng chứng. Đầu ra: Evidence Table. Nghiệm thu: ≥30 nguồn có trích xuất. Phụ thuộc: T3.2. Độ khó: cao. Ước lượng: UNKNOWN.

### WP4 — Hệ thống hóa lý thuyết & bằng chứng
- T4.1 Tổng hợp lý thuyết theo trường phái. Đầu ra: synthesis. Nghiệm thu: có mâu thuẫn được ghi nhận. Phụ thuộc: WP3. Độ khó: cao. Ước lượng: UNKNOWN.
- T4.2 Nhận diện khoảng trống. Đầu ra: danh sách gaps (HYPOTHESIS). Phụ thuộc: T4.1. Độ khó: cao. Ước lượng: UNKNOWN.

### WP5 — Câu hỏi, giả thuyết, khung khái niệm
- T5.1 Chốt câu hỏi nghiên cứu chính (DECISION_REQUIRED). Đầu ra: RQ. Nghiệm thu: câu hỏi có thể kiểm tra. Phụ thuộc: WP3/WP4. Độ khó: cao. Ước lượng: UNKNOWN.
- T5.2 Xác định giả thuyết & cạnh tranh. Đầu ra: hypotheses. Nghiệm thu: falsifiable. Phụ thuộc: T5.1.
- T5.3 Khung khái niệm. Đầu ra: conceptual framework. Nghiệm thu: biến & quan hệ rõ.

### WP6 — Thiết kế mô hình & phương pháp
- T6.1 Chọn phương pháp dựa trên RQ & dữ liệu. Đầu ra: method design. Nghiệm thu: có lý do. Phụ thuộc: WP5/WP7. Độ khó: cao.
- T6.2 Đặc tả mô hình. Đầu ra: model spec. Nghiệm thu: giả định rõ.

### WP7 — Dữ liệu
- T7.1 Xác định nguồn dữ liệu ứng viên (cần xác minh). Đầu ra: data inventory. Nghiệm thu: nguồn + tần suất + bao phủ. Phụ thuộc: WP5. Độ khó: trung bình.
- T7.2 Thu thập & làm sạch. Đầu ra: dataset. Nghiệm thu: code + log. Phụ thuộc: T7.1.
- T7.3 Kiểm tra dữ liệu & EDA. Đầu ra: báo cáo EDA. Nghiệm thu: missing/outlier/document.

### WP8 — Research Lab tối thiểu
- T8.1 Spec Lab (07). Đầu ra: spec. Nghiệm thu: phân biệt 4 loại nội dung. Phụ thuộc: WP6. Độ khó: trung bình.
- T8.2 Xây Lab tối thiểu (chỉ sau khi duyệt). Đầu ra: prototype. Nghiệm thu: minh họa + mô phỏng + trực quan.

### WP9 — Phân tích, ước lượng, kiểm định
- T9.1 Ước lượng mô hình. Đầu ra: results. Nghiệm thu: bảng kết quả + code. Phụ thuộc: WP6/WP7.
- T9.2 Kiểm tra độ bền. Đầu ra: robustness. Nghiệm thu: ≥3 kiểm tra.

### WP10 — Kiểm tra độ bền, phản biện, diễn giải
- T10.1 Phản biện giả thuyết cạnh tranh. Đầu ra: critique. Nghiệm thu: có bằng chứng phản biện.
- T10.2 Diễn giải kết quả & giới hạn. Đầu ra: interpretation.

### WP11 — Viết luận văn
- T11.1 Dàn ý & viết bản thảo. Đầu ra: draft. Nghiệm thu: đầy đủ chương.
- T11.2 Chỉnh sửa & hoàn thiện. Đầu ra: final thesis.

### WP12 — Website nghiên cứu & tái lập
- T12.1 Tài liệu tái lập. Đầu ra: reproducibility package.
- T12.2 Hoàn thiện website (chỉ mức đủ). Đầu ra: site.

Tổng: 13 WP, ~30+ Task. Điều chỉnh theo phát hiện thực tế.
