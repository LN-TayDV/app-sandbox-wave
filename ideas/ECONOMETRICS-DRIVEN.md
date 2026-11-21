# KILO CODE — ECONOMETRICS-DRIVEN MATHEMATICAL MODELING & RESEARCH LAB

## 1. NHIỆM VỤ

Đọc và khai thác cuốn *Econometrics* của Bruce E. Hansen làm nguồn phương pháp luận để xây dựng một hệ thống nghiên cứu, thiết kế, ước lượng, kiểm định và so sánh mô hình toán học.

Mục tiêu nghiên cứu là phát triển giả thuyết “cát truồi” trong hệ thống tài chính: tích lũy nghĩa vụ nợ, biến đổi sức chống chịu, mất ổn định, lan truyền cú sốc và khả năng xảy ra khủng hoảng.

Đây là dự án nghiên cứu định lượng, không phải website giới thiệu công thức, không phải ứng dụng hiển thị nội dung sách và không phải công cụ sinh phương trình tùy ý.

Phải tạo được một Research Lab có khả năng:
- Truy xuất phương pháp từ sách và tài liệu nghiên cứu.
- Xây dựng mô hình lý thuyết với biến số và cơ chế rõ ràng.
- Ánh xạ mô hình vào dữ liệu thực.
- Ước lượng tham số bằng phương pháp phù hợp.
- Chẩn đoán, kiểm định và bác bỏ mô hình khi bằng chứng không ủng hộ.
- Chạy mô phỏng, phân tích độ nhạy và so sánh mô hình.
- Lưu lại kết quả để tái lập nghiên cứu.

## 2. NGUYÊN TẮC BẮT BUỘC

### 2.1. Nghiên cứu trước khi lập trình

Trước khi xây dựng mô hình:
1. Kiểm tra tài liệu Econometrics thực sự có trong workspace hoặc nguồn được cung cấp.
2. Xác định đúng ấn bản, mục lục, phạm vi trang có thể truy cập và tình trạng trích xuất.
3. Lập danh mục phương pháp có thể sử dụng, điều kiện áp dụng, giả định và giới hạn.
4. Xác định các phương pháp cần bổ sung từ tài liệu học thuật khác.
5. Lập bản đồ từ câu hỏi nghiên cứu đến mô hình, biến quan sát, dữ liệu, phép ước lượng và tiêu chí kiểm định.

Không được tuyên bố đã đọc toàn bộ sách khi chưa xử lý và đối chiếu đầy đủ nguồn.

Nếu không truy cập được nội dung sách, phải ghi nhận rõ và tiếp tục những công việc độc lập có thể xác minh. Không giả vờ trích dẫn nội dung sách.

### 2.2. Không biến giả thuyết thành sự thật

Lý thuyết cát truồi là giả thuyết nghiên cứu cần kiểm định.

Phải phân biệt:
- Kiến thức đã được tài liệu nguồn hỗ trợ.
- Mô hình lý thuyết do dự án đề xuất.
- Giả thuyết chưa kiểm định.
- Kết quả suy ra từ dữ liệu.
- Kết quả mô phỏng.
- Kết quả thực nghiệm đã được kiểm định.
- Kết quả chưa xác minh hoặc chưa đủ dữ liệu.

Không được khẳng định thị trường tài chính tuân theo cơ chế tự tổ chức tới hạn, định luật lũy thừa hoặc cơ chế giống sóng vật lý chỉ vì biểu đồ trông tương tự.

## 3. XÂY DỰNG KHO TRI THỨC MÔ HÌNH TOÁN

Tạo cấu trúc dữ liệu có khả năng truy xuất quan hệ giữa:

Book → Chapter → Concept → Assumption → Equation → Model → Estimator → Dataset → Test → Result.

Mỗi mô hình cần tối thiểu:
- Model ID và phiên bản.
- Câu hỏi nghiên cứu.
- Cơ chế kinh tế được giả định.
- Biến phụ thuộc, biến giải thích, tham số và biến trạng thái.
- Định nghĩa, đơn vị, tần suất và nguồn dữ liệu của từng biến.
- Hệ phương trình và giải thích từng phương trình.
- Giả định nhận dạng và điều kiện áp dụng.
- Phương pháp ước lượng.
- Các kiểm định chẩn đoán.
- Giả thuyết có thể bị bác bỏ.
- Dữ liệu dùng để ước lượng và kiểm định.
- Kết quả, giới hạn và lịch sử phiên bản.
- Tài liệu tham khảo, trang nguồn và bằng chứng hỗ trợ.

Công thức phải lưu dưới dạng có cấu trúc, hỗ trợ LaTeX, hiển thị ma trận và tính toán có thể tái lập.

Không chỉ lưu chuỗi công thức. Phải xác định ý nghĩa của các thành phần và quan hệ phụ thuộc giữa chúng.

## 4. THIẾT KẾ PIPELINE XÂY DỰNG MÔ HÌNH

Triển khai pipeline:

Research Question
→ Literature & Method Review
→ Theoretical Mechanism
→ Mathematical Specification
→ Observable Variables
→ Data Validation
→ Estimation
→ Diagnostics
→ Hypothesis Testing
→ Robustness & Sensitivity
→ Out-of-Sample Evaluation
→ Research Report.

Mỗi giai đoạn phải có đầu vào, đầu ra, điều kiện hoàn thành và bằng chứng kiểm tra được.

Không cho phép chuyển một mô hình sang trạng thái đã xác thực nếu chưa đạt các điều kiện kiểm định tương ứng.

## 5. MÔ HÌNH NGHIÊN CỨU CÁT TRUỒI

Bắt đầu với bài toán tích lũy nợ và rủi ro khủng hoảng hệ thống tại Hoa Kỳ.

### Lớp A — Tích lũy nghĩa vụ tài chính

Nghiên cứu các biến có thể quan sát:
- Tỷ lệ nợ trên thu nhập hoặc GDP.
- Nghĩa vụ trả nợ và khả năng thanh toán.
- Đòn bẩy tài chính.
- Tăng trưởng tín dụng.
- Thanh khoản và chênh lệch kỳ hạn.
- Giá tài sản và điều kiện tài chính.
- Khả năng hấp thụ thua lỗ.

Không mặc định mọi biến đều có sẵn hoặc phù hợp. Phải kiểm tra định nghĩa, tần suất, phạm vi lịch sử và chất lượng dữ liệu.

### Lớp B — Trạng thái hệ thống và sức chống chịu

Xây dựng giả thuyết về mối quan hệ giữa tích lũy nghĩa vụ, thanh khoản, đòn bẩy và sức chống chịu.

Phân biệt biến quan sát trực tiếp với trạng thái tiềm ẩn phải ước lượng.

Nếu đưa vào ngưỡng tới hạn, phải định nghĩa cách ước lượng hoặc kiểm định ngưỡng; không tự đặt một giá trị rồi xem đó là ngưỡng thực tế.

### Lớp C — Cú sốc và lan truyền

Nghiên cứu các phương pháp thích hợp cho:
- Cú sốc ngoại sinh và nội sinh.
- Phản hồi phi tuyến.
- Lan truyền qua liên kết tài chính.
- Thay đổi chế độ.
- Sự kiện cực đoan và rủi ro đuôi.
- Động lực trước, trong và sau khủng hoảng.

Chỉ xây dựng mô hình mạng lưới nếu có dữ liệu hoặc giả định cấu trúc được công bố rõ.

### Lớp D — Xác suất và cảnh báo sớm

Định nghĩa rõ sự kiện cần dự báo, chẳng hạn một cuộc khủng hoảng ngân hàng theo tiêu chí có nguồn.

Ước lượng xác suất xảy ra sự kiện trong một khoảng thời gian xác định.

Đánh giá:
- Khả năng phân biệt giữa giai đoạn bình thường và giai đoạn rủi ro.
- Độ hiệu chỉnh xác suất.
- Tỷ lệ cảnh báo sai và bỏ sót.
- Khả năng cảnh báo trước sự kiện.
- Hiệu quả ngoài mẫu so với mô hình cơ sở.

Không diễn giải điểm rủi ro thành xác suất khủng hoảng nếu chưa có phương pháp hiệu chỉnh phù hợp.

## 6. THIẾT KẾ SO SÁNH MÔ HÌNH

Không chỉ xây dựng một mô hình cát truồi rồi chứng minh nó đúng.

Thiết lập ít nhất các nhóm đối chứng phù hợp với dữ liệu:
1. Mô hình cơ sở dựa trên các chỉ báo tài chính thông thường.
2. Mô hình hồi quy hoặc xác suất phù hợp với biến kết quả.
3. Mô hình động hoặc chuỗi thời gian.
4. Mô hình phi tuyến hoặc thay đổi chế độ nếu có bằng chứng hỗ trợ.
5. Mô hình cát truồi đề xuất.

Không bắt buộc dùng mọi phương pháp nếu chúng không phù hợp. Phải giải thích vì sao chọn hoặc loại bỏ từng phương pháp.

So sánh trên cùng tập dữ liệu, cùng thời điểm dự báo và cùng tiêu chí đánh giá. Báo cáo bất định của tham số và sai số dự báo.

## 7. CHẤT LƯỢNG DỮ LIỆU VÀ TÍNH TÁI LẬP

Mỗi chuỗi dữ liệu phải có:
- Nhà cung cấp và URL hoặc định danh nguồn.
- Tên biến gốc và định nghĩa.
- Đơn vị, tần suất và khoảng thời gian.
- Phương pháp biến đổi và tổng hợp.
- Xử lý dữ liệu thiếu và ngoại lệ.
- Thời điểm dữ liệu thực sự có thể được biết.
- Phiên bản dữ liệu và lịch sử cập nhật.

Không trộn dữ liệu mô phỏng với dữ liệu thực mà không gắn nhãn.

Ngăn chặn rò rỉ dữ liệu tương lai, đặc biệt khi dự báo khủng hoảng. Sử dụng kiểm định theo thời gian, rolling-window hoặc expanding-window khi phù hợp.

Không tuyên bố mô hình dự báo tốt nếu chưa có đánh giá ngoài mẫu.

## 8. RESEARCH LAB VÀ GIAO DIỆN

Giao diện phải hỗ trợ công việc nghiên cứu, không chỉ trình bày văn bản.

Mỗi mô hình cần có các khu vực:

A. Model Specification
- Hệ phương trình.
- Bảng biến và tham số.
- Giả định và điều kiện áp dụng.
- Sơ đồ quan hệ nhân quả được giả thuyết.

B. Data & Evidence
- Bảng dữ liệu gốc.
- Ma trận biến.
- Nguồn và chất lượng dữ liệu.
- Phạm vi thời gian và các biến đổi.

C. Estimation & Diagnostics
- Bảng hệ số ước lượng và sai số chuẩn.
- Khoảng tin cậy, kiểm định và chẩn đoán.
- Bảng phần dư và kết quả đánh giá độ phù hợp.

D. Simulation & Sensitivity
- Điều chỉnh tham số trong giới hạn hợp lệ.
- Mô phỏng các kịch bản.
- So sánh quỹ đạo trạng thái và phân phối kết quả.
- Phân tích độ nhạy, bất định và giới hạn.

E. Validation & Comparison
- Kết quả ngoài mẫu.
- So sánh mô hình cơ sở và mô hình đề xuất.
- Các trường hợp thất bại.
- Kết luận có điều kiện và mức độ bằng chứng.

Mọi nút điều khiển phải có chức năng thực. Không dùng dữ liệu giả để tạo cảm giác mô hình đã chạy. Mọi dữ liệu minh họa phải gắn nhãn MOCK hoặc SIMULATED.

## 9. KIỂM THỬ VÀ NGHIỆM THU

Phải có:
- Kiểm thử công thức bằng các ví dụ có đáp án tham chiếu.
- Kiểm thử tính đúng đắn của phép tính và ma trận.
- Kiểm thử xử lý dữ liệu thiếu, dữ liệu bất thường và mẫu nhỏ.
- Kiểm thử tính ổn định khi thay đổi tham số.
- Kiểm thử khả năng tái lập cùng một kết quả từ cùng dữ liệu và cấu hình.
- Kiểm thử giao diện từ nhập dữ liệu đến xuất kết quả.
- Kiểm tra không có kết quả ước lượng hoặc kiểm định được tạo giả.

Nếu chưa có dữ liệu đủ tin cậy, chỉ nghiệm thu phần kiến trúc và thử nghiệm mô phỏng; không được tuyên bố đã xác thực giả thuyết thực nghiệm.

## 10. QUY TẮC TRIỂN KHAI TRONG REPOSITORY

Trước khi sửa code:
1. Kiểm tra repository, kiến trúc hiện có, công nghệ, test và các module nghiên cứu đã tồn tại.
2. Xác định các phần có thể tái sử dụng.
3. Lập kế hoạch thay đổi và xác định chính xác file sẽ sửa.
4. Bảo toàn tài liệu nguồn và dữ liệu gốc.
5. Không tạo một hệ thống mới trùng chức năng với hệ thống hiện hữu.
6. Không tự ý thay đổi phạm vi repository hoặc xóa dữ liệu.

Thực hiện theo từng giai đoạn nhỏ, chạy kiểm thử sau mỗi giai đoạn và lưu checkpoint.

## 11. BÁO CÁO KẾT QUẢ

Báo cáo bằng tiếng Việt, ngắn gọn nhưng có bằng chứng:
- Nội dung sách đã thực sự khai thác.
- Các phương pháp đã ánh xạ vào hệ thống.
- Các mô hình đã triển khai và trạng thái bằng chứng.
- Nguồn dữ liệu đã kết nối và khoảng thời gian.
- Kiểm thử đã chạy, kết quả và lỗi còn tồn tại.
- Các giả thuyết chưa thể kiểm định.
- Các bước tiếp theo theo mức độ ưu tiên.

Không báo cáo PASS nếu không có kết quả kiểm thử tương ứng.

Bắt đầu bằng việc kiểm tra repository và nguồn sách, sau đó thực hiện theo pipeline. Không dừng ở việc viết kế hoạch hoặc tạo tài liệu mô tả; hãy triển khai phần có thể hoàn thành và kiểm chứng được.