# MASTER PROMPT — PRODUCT-FIRST REBUILD

# ADVANCED MACROECONOMICS: ĐỌC HIỂU SÂU, TÁI DỰNG MÔ HÌNH VÀ XÂY DỰNG HỆ THỐNG HỌC TẬP TƯƠNG TÁC

## 0. CHỈ THỊ TỐI CAO — HIỂU ĐÚNG MỤC TIÊU DỰ ÁN

Bạn đang tiếp tục phát triển dự án học tập dựa trên cuốn sách:

**David Romer — Advanced Macroeconomics, Fourth Edition.**

Workspace:

`C:\Users\PC\Documents\AI_project\sandbox-financial\research\advanced-macroeconomics-fourth-edition`

Đây là một dự án xây dựng hệ thống học tập kinh tế vĩ mô nâng cao dựa trên nội dung sách gốc. Không phải dự án chỉ để xây dựng HTML, tạo knowledge graph, trích xuất phương trình, viết registry hoặc bổ sung thư viện tính toán khoa học.

**Nhiệm vụ cốt lõi là đọc hiểu toàn bộ cuốn sách ở cấp độ học thuật, phân tích cấu trúc lập luận của từng chương, tái dựng các mô hình kinh tế, xác minh phương trình, hiểu cơ chế vận hành và biến kết quả nghiên cứu thành một hệ thống học tập có thể tương tác, kiểm tra và truy nguyên nguồn.**

Người học phải có khả năng trả lời được các câu hỏi:

- Chương này đang giải quyết vấn đề kinh tế nào?
- Tại sao cần xây dựng mô hình này?
- Mô hình bắt đầu từ những giả định nào?
- Các phương trình được thiết lập như thế nào?
- Một phương trình được suy ra từ phương trình trước bằng lập luận gì?
- Ý nghĩa kinh tế của từng biến, tham số và điều kiện là gì?
- Nghiệm cân bằng được tìm ra bằng cách nào?
- Tại sao nghiệm đó tồn tại, duy nhất hoặc ổn định trong những điều kiện nhất định?
- Kết quả thay đổi như thế nào khi thay đổi giả định hoặc tham số?
- Mô hình giải thích được điều gì, không giải thích được điều gì?
- Mô hình liên hệ với các chương khác ra sao?
- Kết luận nào được Romer trình bày trực tiếp, kết luận nào do người học hoặc ứng dụng suy ra?

Không được coi việc đã trích xuất PDF, tạo file JSON, ghi nhận phương trình hoặc chạy thành công một solver là đã hiểu mô hình.

Không được coi việc có một biểu đồ hoặc slider là đã xây dựng xong một Economic Lab.

Không được tự tạo nội dung để lấp đầy chương còn thiếu, rồi trình bày nội dung đó như thể được Romer viết trong sách.

Mọi công nghệ, registry, phép tính, giao diện và bài kiểm tra phải phục vụ trực tiếp mục tiêu đọc hiểu và phân tích kinh tế vĩ mô nâng cao.

---

## 1. PHẠM VI NGUỒN VÀ NGUYÊN TẮC BẰNG CHỨNG

### 1.1. Xác minh nguồn sách và cấu trúc chương

Bắt đầu bằng việc xác minh PDF nguồn hiện có trong workspace hoặc các thư mục dữ liệu mà dự án đang tham chiếu.

Không tự đoán đường dẫn PDF. Tìm trong cấu hình, registry, checkpoint và scripts hiện có để xác định chính xác file nguồn đang được sử dụng.

Xác minh:

- Đúng tác giả, tên sách và phiên bản Fourth Edition.
- Mục lục và thứ tự chương.
- Các mục, tiểu mục và phần mở rộng.
- Số trang PDF thực tế và cách ánh xạ sang số trang in của sách.
- Các chunk, OCR, trích xuất văn bản và artifacts nghiên cứu hiện có.
- Các phương trình, bảng, hình và chú thích liên quan.
- Các nguồn dẫn chiếu bên trong sách.

Không sử dụng mục lục của ấn bản khác thay cho mục lục của Fourth Edition nếu chưa đối chiếu.

Nếu PDF có trang quét, công thức hoặc ký hiệu bị lỗi khi trích xuất văn bản, hãy kiểm tra hình ảnh trang gốc tại đúng vị trí cần thiết. Không suy đoán phần bị thiếu dựa trên kiến thức chung.

### 1.2. Phân biệt bằng chứng và mức độ xác minh

Duy trì hoặc ánh xạ về hệ thống trạng thái bằng chứng hiện có. Nếu dự án đã có registry chuẩn, không tạo thêm một registry cạnh tranh.

Tối thiểu phải phân biệt:

- `BOOK_EVIDENCE_VERIFIED`: đối chiếu được với nguồn sách.
- `DERIVED_VERIFIED`: kết quả suy ra từ phương trình đã xác minh và có kiểm tra độc lập.
- `NUMERICALLY_VERIFIED`: kết quả tính số được kiểm thử nhưng chưa tự động chứng minh tính đúng đắn về kinh tế.
- `FINANCIAL_REFERENCE`: kiến thức tham khảo bên ngoài được ghi rõ nguồn.
- `ILLUSTRATIVE`: ví dụ số minh họa, không phải dữ liệu gốc.
- `UNVERIFIED`: chưa đủ bằng chứng để xác nhận.
- `DOMAIN_GAP`: thiếu dữ liệu hoặc đặc tả cần thiết.

Có thể giữ các trạng thái hiện hữu như `FORMULA_UNVERIFIED` nếu chúng đã được dùng trong pipeline.

Không tự nâng trạng thái xác minh chỉ vì:

- Công thức có vẻ hợp lý.
- Solver trả về nghiệm.
- Hai implementation cho kết quả gần nhau.
- Unit tests chạy thành công.
- Nội dung xuất hiện trong một file nghiên cứu nhưng không truy ngược được về nguồn.

**Quy tắc bảo toàn bằng chứng:** mọi kết quả chưa xác minh phải tiếp tục được đánh dấu chưa xác minh cho đến khi có bằng chứng thích hợp.

Đặc biệt:

- Giữ `PT-10-01` ở trạng thái `FORMULA_UNVERIFIED` cho đến khi có đủ bằng chứng nguồn.
- Không đưa `eq-nsc` vào dữ liệu học tập hoặc mô hình đang hoạt động.
- Không tự động sửa các trường hợp provenance mismatch hoặc `no_claim` chỉ để báo cáo sạch hơn.
- Không xóa cảnh báo cũ nếu chưa xác định được nguyên nhân và bằng chứng khắc phục.

### 1.3. Truy nguyên nguồn

Mỗi nội dung học thuật quan trọng phải có thể truy ngược về:

- Chương.
- Mục hoặc tiểu mục.
- Trang in nếu xác định được.
- Trang PDF tương ứng nếu có.
- Chunk hoặc đoạn trích nguồn.
- ID phương trình hoặc mô hình liên quan.
- Trạng thái xác minh.

Không bịa số trang hoặc gán một phương trình cho Romer nếu chưa xác minh.

Phân biệt rõ số trang in và số trang của file PDF.

---

## 2. ĐỌC HIỂU SÂU TỪNG CHƯƠNG — CÔNG VIỆC ƯU TIÊN SỐ MỘT

Không bắt đầu bằng việc thêm hàng loạt biểu đồ hoặc mở rộng giao diện.

Trước hết, phải xây dựng được hiểu biết học thuật có cấu trúc cho từng chương.

Với mỗi chương, thực hiện quy trình sau.

### Bước 1 — Xác định câu hỏi trung tâm

Giải thích:

- Vấn đề kinh tế vĩ mô mà chương muốn giải quyết.
- Vì sao vấn đề đó quan trọng.
- Những hạn chế của cách giải thích hoặc mô hình trước đó.
- Câu hỏi mà mô hình mới trả lời.
- Phạm vi mà mô hình không cố gắng giải quyết.

Không chỉ tóm tắt tiêu đề chương. Phải nêu được vấn đề kinh tế và động cơ xây dựng mô hình.

### Bước 2 — Tái dựng cấu trúc lập luận của tác giả

Phân tích trình tự lập luận thực tế trong chương:

1. Vấn đề hoặc hiện tượng kinh tế.
2. Kiến thức nền được sử dụng.
3. Các giả định ban đầu.
4. Cấu trúc mô hình.
5. Phương trình nền tảng.
6. Các phép biến đổi và kết quả trung gian.
7. Điều kiện cân bằng hoặc nghiệm.
8. Kết quả chính.
9. Phân tích so sánh tĩnh, động học hoặc ổn định nếu có.
10. Diễn giải kinh tế.
11. Giới hạn, phản biện hoặc phần mở rộng.

Không ép mọi chương vào cùng một trình tự nếu cách tổ chức của Romer khác. Phải phản ánh được lập luận thực tế của từng chương.

### Bước 3 — Xây dựng bản đồ phụ thuộc kiến thức

Xác định:

- Khái niệm cần biết trước.
- Mô hình nền tảng.
- Phương trình được sử dụng lại.
- Kết quả được kế thừa từ chương trước.
- Kết quả trở thành đầu vào cho chương sau.
- Các giả định thay đổi giữa những mô hình liên quan.

Ví dụ, chỉ thiết lập quan hệ giữa mô hình tăng trưởng, tích lũy vốn, quyết định tiết kiệm, tiến bộ công nghệ, tối ưu hóa liên thời gian hoặc các mô hình chu kỳ kinh doanh khi nội dung thực tế của sách hỗ trợ quan hệ đó.

Không nối hai mô hình chỉ vì chúng cùng đề cập đến vốn, tiêu dùng, sản lượng hoặc lãi suất.

Mỗi quan hệ phải có ý nghĩa ngữ nghĩa rõ ràng, chẳng hạn:

- `PREREQUISITE_OF`
- `USES_EQUATION`
- `DERIVES_FROM`
- `EXTENDS_MODEL`
- `CONTRASTS_WITH`
- `SPECIAL_CASE_OF`
- `USES_ASSUMPTION`
- `RELAXES_ASSUMPTION`

Chỉ dùng những loại quan hệ thực sự cần thiết; không tạo edge để làm graph trông đầy đủ.

### Bước 4 — Tạo bản giải thích học thuật bằng tiếng Việt

Với mỗi ý tưởng cốt lõi, trình bày theo ba tầng:

**Tầng A — Trực giác**

Giải thích bằng ngôn ngữ tự nhiên, chính xác và dễ hiểu mà không làm sai ý nghĩa kinh tế.

**Tầng B — Cơ chế**

Giải thích quan hệ nhân quả, quyết định của tác nhân, ràng buộc và cơ chế truyền dẫn. Nêu rõ điều gì là giả định, điều gì là hệ quả.

**Tầng C — Toán học**

Trình bày phương trình, cách suy ra, điều kiện cần thiết, nghiệm và ý nghĩa kinh tế của kết quả.

Không thay thế chứng minh bằng trực giác. Không thay thế trực giác bằng một chuỗi phương trình không được giải thích.

Nếu có bước suy luận quan trọng, phải giải thích tại sao bước đó hợp lệ.

### Bước 5 — Xác định phần chưa hiểu hoặc chưa đủ bằng chứng

Tạo danh sách cụ thể cho từng chương:

- Đoạn nguồn cần đọc lại.
- Phương trình chưa xác minh.
- Ký hiệu mơ hồ.
- Bước suy luận bị thiếu.
- Điều kiện tồn tại hoặc duy nhất của nghiệm chưa rõ.
- Mô hình chưa có implementation.
- Kết quả số chưa có giá trị tham chiếu.
- Quan hệ giữa các chương chưa được chứng minh.

Không che giấu các khoảng trống bằng nội dung tổng quát.

Nếu một phần chưa thể hoàn thành, ghi rõ phần nào bị chặn, cần bằng chứng gì và phần nào vẫn có thể tiếp tục triển khai độc lập.

---

## 3. PHÂN TÍCH MÔ HÌNH VÀ PHƯƠNG TRÌNH

Đây là lớp học thuật trung tâm của dự án.

Không chỉ lưu phương trình dưới dạng chuỗi LaTeX. Phải hiểu được vai trò của nó trong mô hình và lập luận của tác giả.

### 3.1. Hồ sơ chuẩn của mỗi mô hình

Mỗi mô hình phải có các trường phù hợp với nội dung thực tế:

- `model_id`: ID ổn định.
- Tên mô hình.
- Câu hỏi kinh tế.
- Chương và mục nguồn.
- Mục tiêu mô hình.
- Tác nhân kinh tế.
- Biến trạng thái.
- Biến điều khiển.
- Biến nội sinh.
- Biến ngoại sinh.
- Tham số.
- Đơn vị và quy ước thời gian.
- Giả định.
- Ràng buộc.
- Phương trình nền tảng.
- Điều kiện ban đầu hoặc điều kiện biên.
- Điều kiện cân bằng.
- Điều kiện tối ưu nếu có.
- Điều kiện tồn tại và duy nhất nếu có.
- Điều kiện ổn định hoặc hội tụ nếu có.
- Nghiệm hoặc kết quả chính.
- Phương pháp giải.
- Implementation số.
- Test cases.
- Giới hạn và trường hợp ngoại lệ.
- Provenance.
- Liên kết bài học và lab.

Không bắt buộc mọi mô hình phải có tất cả trường. Trường nào không áp dụng thì bỏ qua hoặc ghi rõ không áp dụng; không điền dữ liệu giả để đủ schema.

### 3.2. Hồ sơ của mỗi phương trình

Với từng phương trình quan trọng, phải trả lời:

1. Phương trình được đưa ra ở đâu?
2. Nó mô tả quan hệ kinh tế nào?
3. Từng ký hiệu có ý nghĩa gì?
4. Các biến được đo theo đơn vị nào?
5. Phương trình là định nghĩa, đồng nhất thức kế toán, điều kiện tối ưu, phương trình hành vi, điều kiện cân bằng hay quan hệ chuyển động?
6. Phương trình được giả định hay suy ra?
7. Nếu suy ra, cần những bước biến đổi nào?
8. Các giả định nào cần thiết cho phép biến đổi?
9. Miền xác định của phương trình là gì?
10. Phương trình được sử dụng để suy ra kết quả nào?
11. Kết quả đó có diễn giải kinh tế gì?
12. Có trường hợp biên hoặc ngoại lệ nào không?

Không coi mọi phương trình trong sách là phương trình hành vi. Phải phân biệt rõ bản chất kinh tế và toán học của từng phương trình.

### 3.3. Quy trình xác minh phương trình

Áp dụng quy trình phù hợp cho từng phương trình:

1. Trích xuất phương trình và ngữ cảnh từ nguồn.
2. Kiểm tra ký hiệu, chỉ số, dấu, số mũ và điều kiện.
3. Đối chiếu hình ảnh trang PDF khi văn bản trích xuất không đáng tin cậy.
4. Chuẩn hóa phương trình nhưng giữ nguyên ý nghĩa và quy ước gốc.
5. Ghi lại mọi thay đổi ký hiệu hoặc biến đổi.
6. Kiểm tra tính tương đương đại số khi có chuyển đổi.
7. Kiểm tra miền xác định và các điều kiện cần thiết.
8. Dùng SymPy hoặc công cụ phù hợp để kiểm tra biểu thức nếu hữu ích.
9. Kiểm tra số bằng các trường hợp xác định.
10. So sánh với kết quả hoặc điều kiện tham chiếu trong sách nếu có.
11. Ghi nhận bằng chứng, phương pháp kiểm tra và giới hạn.
12. Chỉ nâng trạng thái khi đã đáp ứng tiêu chuẩn xác minh.

Kiểm tra ký hiệu không thay thế việc hiểu nội dung. Hai biểu thức đại số tương đương vẫn có thể được sử dụng sai nếu giả định hoặc miền áp dụng khác nhau.

### 3.4. Phân biệt phương trình gốc, phương trình suy ra và mô hình mở rộng

Luôn phân biệt:

- Phương trình được trình bày trực tiếp trong sách.
- Phương trình được biến đổi từ phương trình gốc.
- Kết quả suy ra dưới các giả định bổ sung.
- Implementation số được sử dụng để tính toán.
- Biểu thức dùng để hiển thị trên giao diện.
- Mô hình mở rộng do ứng dụng bổ sung.

Không gắn nhãn tất cả các biểu thức là phương trình của Romer.

Nếu một công thức chỉ đúng trong trường hợp đặc biệt, phải ghi rõ điều kiện.

Nếu chưa xác định được liệu một phương trình là của tác giả hay do implementation bổ sung, giữ trạng thái chưa xác minh.

---

## 4. PHÂN TÍCH CƠ CHẾ KINH TẾ, NGHIỆM VÀ ĐỘNG HỌC

Mỗi mô hình phải được phân tích theo bản chất của nó. Không ép mọi mô hình vào một bộ chỉ tiêu chung.

### 4.1. Với mô hình tĩnh

Khi phù hợp, phân tích:

- Cân bằng.
- Điều kiện tối ưu.
- Tồn tại và duy nhất của nghiệm.
- So sánh tĩnh.
- Tác động của tham số.
- Điều kiện biên.
- Trường hợp không có nghiệm hoặc có nhiều nghiệm.

### 4.2. Với mô hình động

Khi phù hợp, phân tích:

- Biến trạng thái và biến điều khiển.
- Quy luật chuyển động.
- Điều kiện ban đầu.
- Điều kiện biên.
- Trạng thái dừng.
- Điểm cố định.
- Tính ổn định cục bộ hoặc toàn cục.
- Hội tụ hoặc phân kỳ.
- Đường chuyển tiếp.
- Đường đi cân bằng.
- Điều kiện hội tụ và điều kiện chuyển tiếp.
- Tính khả thi của quỹ đạo.

Không sử dụng khái niệm trạng thái dừng thay cho cân bằng trong mọi trường hợp. Không đồng nhất nghiệm số với trạng thái cân bằng kinh tế.

### 4.3. Với mô hình tối ưu hóa

Khi mô hình thực sự yêu cầu, phân tích:

- Hàm mục tiêu.
- Ràng buộc.
- Điều kiện bậc nhất.
- Điều kiện bậc hai nếu cần.
- Điều kiện Kuhn–Tucker khi thích hợp.
- Điều kiện nội điểm hoặc nghiệm góc.
- Tính khả thi.
- Tính tối ưu.
- Ý nghĩa kinh tế của nhân tử Lagrange.
- Phân biệt điều kiện cần và điều kiện đủ.

Không kết luận nghiệm là tối ưu chỉ vì điều kiện bậc nhất bằng không.

### 4.4. Với mô hình cân bằng và hệ phương trình

Khi phù hợp, phân tích:

- Các điều kiện cân bằng.
- Số phương trình và số ẩn.
- Điều kiện tương thích.
- Tính xác định của hệ.
- Điều kiện tồn tại và duy nhất.
- Các điều kiện thị trường hoặc ràng buộc kinh tế.
- Nghiệm ngoài miền kinh tế.
- Tính nhạy cảm với tham số.

### 4.5. Với phương pháp số

Nếu sử dụng solver, phải ghi nhận:

- Phương pháp giải.
- Giá trị đầu vào.
- Giá trị khởi tạo nếu có.
- Dung sai.
- Trạng thái hội tụ.
- Residual hoặc sai số thích hợp.
- Cảnh báo số học.
- Điều kiện có thể dẫn đến nghiệm sai hoặc không hội tụ.
- Cách kiểm tra độc lập.

Không coi solver thành công là bằng chứng đủ để xác nhận mô hình đúng.

---

## 5. PHÂN TÍCH TỪNG CHƯƠNG THEO NỘI DUNG THỰC TẾ CỦA ROMER

Không xây dựng sẵn một danh sách mô hình rồi ép vào các chương.

Hãy đọc mục lục Fourth Edition và các artifacts hiện có để xác định chính xác nội dung của từng chương. Từ đó, lập bản đồ mô hình theo nguồn.

Các nhóm như tăng trưởng tân cổ điển, Ramsey–Cass–Koopmans, mô hình thế hệ chồng lấn, tăng trưởng nội sinh, quyết định tiêu dùng liên thời gian, mô hình chu kỳ kinh doanh, chính sách tiền tệ hoặc các mô hình vĩ mô khác chỉ được đưa vào chương tương ứng khi đã đối chiếu với nội dung sách thực tế.

Đối với mỗi chương:

### A. Chân dung chương

- Câu hỏi trung tâm.
- Đóng góp của chương.
- Mô hình nền tảng.
- Kiến thức tiên quyết.
- Kết quả quan trọng.
- Quan hệ với các chương khác.

### B. Bản đồ lập luận

- Chuỗi các bước tác giả sử dụng để đi từ giả định đến kết luận.
- Các phương trình then chốt.
- Các kết quả trung gian.
- Những bước suy luận dễ bị hiểu nhầm.
- Những điều kiện mà kết luận phụ thuộc vào.

### C. Hồ sơ mô hình

- Các tác nhân.
- Các biến và tham số.
- Ràng buộc.
- Phương trình.
- Điều kiện cân bằng hoặc tối ưu.
- Kết quả.
- Giới hạn.

### D. Phân tích toán học

- Các phép biến đổi.
- Đạo hàm hoặc điều kiện tối ưu khi phù hợp.
- Tuyến tính hóa khi có cơ sở.
- Jacobian hoặc ma trận chuyển tiếp khi cần.
- Giá trị riêng và ổn định khi mô hình yêu cầu.
- Phân tích trạng thái dừng.
- Kiểm tra điều kiện biên và trường hợp đặc biệt.

### E. Diễn giải kinh tế

- Ý nghĩa của từng kết quả.
- Cơ chế truyền dẫn.
- Điều gì thay đổi khi giả định thay đổi.
- Phân biệt tương quan, cơ chế mô hình và quan hệ nhân quả.
- Những điều mô hình không thể kết luận.

### F. Chuyển hóa thành bài học

- Giải thích trực giác.
- Giải thích cơ chế.
- Giải thích toán học.
- Ví dụ xác định.
- Đồ thị hoặc bảng phù hợp.
- Câu hỏi tự kiểm tra.
- Bài tập suy luận.
- Lab tương tác nếu có cơ sở.
- Nguồn và trạng thái xác minh.

### G. Kiểm định chất lượng

- Nội dung đã đối chiếu nguồn.
- Phương trình đã xác minh.
- Kết quả đã kiểm tra.
- Phần còn chưa xác minh.
- Các lỗi hoặc khoảng trống còn lại.

Không đánh dấu chương hoàn thành chỉ vì có đủ các đề mục trên. Chất lượng nội dung mới là tiêu chí quyết định.

---

## 6. ECONOMIC LAB — CHỈ XÂY DỰNG SAU KHI HIỂU MÔ HÌNH

Mỗi lab phải được xây dựng từ một mô hình đã có cơ sở học thuật.

Không phát triển slider trước rồi tìm công thức để làm cho slider có vẻ hoạt động.

### 6.1. Cấu trúc của một lab

Mỗi lab phải có các thành phần phù hợp:

1. Câu hỏi kinh tế.
2. Bài học nền tảng.
3. Mô hình được sử dụng.
4. Phương trình và nguồn.
5. Giả định.
6. Điều khiển tham số hợp lệ.
7. Phương pháp tính.
8. Kết quả số.
9. Đồ thị hoặc hình thức biểu diễn thích hợp.
10. Bảng kết quả.
11. Diễn giải phụ thuộc vào kết quả hiện tại.
12. Giới hạn và cảnh báo.
13. Khôi phục tham số.
14. So sánh kịch bản.
15. Liên kết tới nguồn và bài học.

Không phải mô hình nào cũng cần slider. Có mô hình phù hợp hơn với bảng kịch bản, sơ đồ dòng, biểu đồ pha, đường chuyển tiếp, ma trận, hoặc bài tập suy luận từng bước.

### 6.2. Một nguồn kết quả duy nhất

Một lần tính toán phải tạo ra một kết quả có cấu trúc dùng chung.

Từ kết quả đó, cập nhật:

- Giá trị số.
- Bảng.
- Đồ thị.
- Các chỉ báo.
- Phần diễn giải phụ thuộc vào kết quả.

Không tạo riêng một công thức cho bảng, một bộ số cho chart và một đoạn văn cố định cho giải thích.

Không cho phép giao diện hiển thị kết quả cũ khi phép tính mới thất bại.

Không âm thầm thay giá trị lỗi bằng 0 hoặc một giá trị mặc định khiến người học hiểu nhầm.

Khi mô hình không có nghiệm, có nhiều nghiệm hoặc solver không hội tụ, hãy hiển thị đúng trạng thái và giải thích giới hạn.

### 6.3. Ví dụ số và mô phỏng

Phân biệt rõ:

- Ví dụ số trong sách.
- Ví dụ số do ứng dụng tạo.
- Kết quả suy ra từ công thức.
- Kết quả do solver tính.
- Mô phỏng ngẫu nhiên.
- Dữ liệu thực nghiệm nếu có nguồn xác minh.

Không gán số liệu minh họa cho Romer.

Nếu dùng mô phỏng ngẫu nhiên, lưu seed và phương pháp tạo dữ liệu để tái lập.

Không thêm dữ liệu vĩ mô thực tế từ bên ngoài chỉ để làm giao diện có vẻ chân thực. Nếu cần dữ liệu ngoài sách, ghi rõ nguồn, thời gian, đơn vị, phạm vi và vai trò của dữ liệu đó.

---

## 7. THIẾT KẾ HỆ THỐNG HỌC TẬP HTML

Sản phẩm cuối cùng là một hệ thống học tập, không phải kho registry.

Tận dụng `knowledge_map.html`, các module JavaScript, dữ liệu và tests hiện có nếu kiến trúc hiện tại phù hợp.

Không viết lại toàn bộ ứng dụng chỉ vì muốn có cấu trúc mới.

### 7.1. Trải nghiệm học tập

Giao diện cần hỗ trợ các hoạt động:

- Khám phá cấu trúc toàn khóa học.
- Học từng chương và từng mục.
- Đọc giải thích học thuật bằng tiếng Việt.
- Mở phương trình và xem định nghĩa biến.
- Theo dõi các bước suy luận.
- Xem giả định và điều kiện áp dụng.
- Mở mô hình từ bài học.
- Thực hiện thí nghiệm hoặc so sánh kịch bản.
- Xem đồ thị, bảng và kết quả.
- Truy nguyên nguồn.
- Khám phá mối liên hệ giữa các mô hình.

Có thể tổ chức trong các tab, panel hoặc modal nếu cách đó giúp học tập liền mạch. Không tạo quá nhiều màn hình độc lập mà không có lý do.

### 7.2. Ngôn ngữ

Mặc định sử dụng tiếng Việt tự nhiên, chuẩn xác về kinh tế vĩ mô và toán học.

Khi cần, ghi kèm thuật ngữ tiếng Anh để người học đối chiếu với sách. Không để thuật ngữ tiếng Anh xuất hiện mà không được giải thích nếu nó là khái niệm quan trọng.

Không dịch máy móc các đoạn văn dài thành nội dung học tập.

Không làm mất các phân biệt học thuật quan trọng khi diễn giải.

### 7.3. Hiển thị phương trình

Mỗi phương trình quan trọng cần có:

- Biểu thức.
- Định nghĩa ký hiệu.
- Vai trò của phương trình.
- Giả định.
- Cách suy ra nếu cần.
- Ý nghĩa kinh tế.
- Nguồn.
- Trạng thái xác minh.

Công thức hiển thị phải nhất quán với công thức được sử dụng trong phép tính.

Nếu công thức hiển thị được biến đổi so với nguồn, phải ghi nhận quan hệ biến đổi và xác minh tương đương.

### 7.4. Knowledge graph

Knowledge graph chỉ là công cụ điều hướng và khám phá.

Người học có thể đi từ chương đến mô hình, từ mô hình đến phương trình, từ phương trình đến giả định và nguồn.

Không để graph thay thế phần giải thích học thuật.

Không tạo quan hệ giả để tăng số lượng node hoặc edge.

Mọi quan hệ quan trọng phải có ý nghĩa rõ ràng và có thể truy nguyên.

---

## 8. KIẾN TRÚC TÍNH TOÁN KHOA HỌC

Tận dụng hệ thống hiện có. Không biến việc thêm thư viện thành mục tiêu.

Trước khi thêm dependency, kiểm tra môi trường Python, package đã cài, scripts, test suite và cách ứng dụng đang chạy offline.

Chỉ sử dụng công cụ khi giải quyết được một bài toán mô hình cụ thể:

- **NumPy:** phép tính số, vector và ma trận.
- **pandas:** bảng kịch bản và dữ liệu có cấu trúc.
- **SciPy:** giải hệ phương trình, tối ưu hóa và phương pháp số.
- **SymPy:** biến đổi đại số, đạo hàm và kiểm tra tương đương ký hiệu.
- **Matplotlib/Seaborn:** phân tích, chẩn đoán và tạo hình tĩnh phía Python.
- **JavaScript:** tương tác trực tiếp, trạng thái giao diện và cập nhật biểu đồ trong trình duyệt.
- **MathML hoặc giải pháp công thức tương thích offline:** trình bày phương trình.

Không mặc định phải dùng tất cả thư viện.

Không chuyển phép tính đơn giản sang backend chỉ vì có thể làm như vậy.

Không dùng Matplotlib để thay thế một chart tương tác nếu người học cần thay đổi tham số ngay trong trình duyệt.

Giữ khả năng hoạt động offline theo kiến trúc hiện tại, trừ khi có lý do kỹ thuật cụ thể và được kiểm thử.

### 8.1. Tách biệt các lớp mô hình

Duy trì sự phân biệt giữa:

1. Bằng chứng nguồn sách.
2. Đặc tả kinh tế của mô hình.
3. Phương trình ký hiệu.
4. Implementation tính toán.
5. Kết quả tính toán.
6. Kết quả kiểm thử.
7. Phương trình hiển thị.
8. Bài học và diễn giải.

Các lớp phải liên kết với nhau bằng ID ổn định và provenance.

Không để implementation số trở thành nguồn chân lý duy nhất về mô hình.

Không coi kết quả của một script là bằng chứng rằng phương trình nguồn đúng.

---

## 9. KIỂM THỬ HỌC THUẬT VÀ TÍNH ĐÚNG ĐẮN

Không chỉ kiểm tra ứng dụng có chạy hay không. Phải kiểm tra cả kiến thức, phương trình, mô hình và trải nghiệm học tập.

### 9.1. Kiểm thử nguồn và provenance

Kiểm tra:

- Mỗi phương trình quan trọng có nguồn hoặc trạng thái chưa xác minh.
- ID nguồn tồn tại.
- Chương và mục được liên kết chính xác.
- Không có trang nguồn tự bịa.
- Không có phương trình chưa xác minh được trình bày như đã xác minh.
- Không có dữ liệu minh họa bị gắn nhãn dữ liệu gốc.
- Không có quan hệ tri thức thiếu cơ sở.

### 9.2. Kiểm thử phương trình

Khi phù hợp:

- So sánh biểu thức ký hiệu.
- Kiểm tra các bước biến đổi.
- Kiểm tra điều kiện và miền xác định.
- Kiểm tra trường hợp đặc biệt.
- Kiểm tra giá trị biên.
- Kiểm tra các điều kiện cần và đủ.
- So sánh các implementation độc lập.
- Đối chiếu với kết quả trong sách nếu có.

Không dựa duy nhất vào một phép kiểm tra số tại một điểm.

### 9.3. Kiểm thử mô hình

Khi phù hợp:

- Điều kiện cân bằng.
- Điều kiện tối ưu.
- Điều kiện chuyển động.
- Tính khả thi của nghiệm.
- Tính ổn định.
- Residual.
- Trường hợp không có nghiệm.
- Trường hợp có nhiều nghiệm.
- Độ nhạy theo tham số.
- Các trường hợp biên.

Không yêu cầu mọi mô hình phải có cùng một bộ test. Bộ test phải phản ánh bản chất toán học của mô hình đó.

### 9.4. Kiểm thử giao diện và Economic Lab

Kiểm tra:

- Thay đổi tham số thực sự gọi hàm tính toán.
- Kết quả số cập nhật.
- Chart và bảng dùng cùng kết quả.
- Diễn giải cập nhật theo kết quả.
- Reset khôi phục đúng giá trị ban đầu.
- So sánh kịch bản hoạt động.
- Lỗi solver không để lại kết quả cũ như thể là kết quả mới.
- Điều khiển có nhãn, đơn vị và miền giá trị.
- Nội dung tiếng Việt hiển thị đúng.
- Offline loading hoạt động.
- Không có nút giả hoặc panel rỗng.

Nếu dùng browser automation, hãy kiểm tra luồng thao tác thật. Unit tests đơn lẻ không đủ để xác nhận lab hoạt động trong trình duyệt.

### 9.5. Không báo cáo PASS thiếu bằng chứng

Mỗi tuyên bố PASS phải có bằng chứng kiểm thử hoặc xác minh tương ứng.

Phân biệt rõ:

- Đã triển khai.
- Đã chạy test.
- Đã xác minh bằng nguồn.
- Đã kiểm thử trên trình duyệt.
- Đã hoàn thành nội dung học thuật.
- Còn chưa xác minh.
- Bị chặn.

Không sử dụng số lượng file hoặc số lượng test làm đại diện duy nhất cho chất lượng học thuật.

---

## 10. WORKFLOW TRIỂN KHAI — KIỂM TRA, LÀM THỰC, RỒI MỞ RỘNG

Không dừng ở audit. Sau khi xác định trạng thái hiện tại, phải tiếp tục triển khai ngay trong phạm vi hợp lý.

### Phase A — Khôi phục trạng thái thực tế

1. Kiểm tra git status và các thay đổi chưa commit.
2. Kiểm tra cấu trúc workspace.
3. Đọc checkpoint, architecture và các báo cáo nghiên cứu hiện có.
4. Kiểm tra mục lục và artifacts theo chương.
5. Kiểm tra model registry, equation registry và provenance.
6. Kiểm tra `learning_content/`, `data/scientific/`, `assets/js/` và các đường dẫn thực tế hiện có.
7. Kiểm tra scripts build, validator và test.
8. Chạy các kiểm tra hiện có để xác định baseline.
9. Xác định các khoảng trống học thuật quan trọng nhất.

Không giả định các đường dẫn được nêu trong prompt đều tồn tại. Khám phá cấu trúc thực tế trước khi thao tác.

Không xóa artifacts có giá trị hoặc ghi đè thay đổi chưa commit.

### Phase B — Hoàn thiện một chương theo chiều sâu

Chọn chương có nền tảng nghiên cứu và bằng chứng tốt nhất trong workspace.

Không chọn chương chỉ vì dễ tạo giao diện.

Hoàn thiện một lát cắt đầu-cuối:

Nguồn sách → đọc hiểu → bản đồ lập luận → phương trình đã xác minh → đặc tả mô hình → implementation → kiểm thử → bài học tiếng Việt → biểu đồ/bảng hoặc lab → truy nguyên nguồn.

Mục tiêu của phase này là chứng minh pipeline tạo được một bài học thực sự có chiều sâu học thuật, không chỉ là một trang có dữ liệu.

Ưu tiên tận dụng các artifacts Solow, RCK, OLG, AK hoặc các mô hình hiện có **chỉ khi** chúng đã được xác định đúng chương và có bằng chứng nguồn phù hợp.

Không lấy ví dụ này làm chỉ thị phải thêm tất cả mô hình.

### Phase C — Kiểm định lát cắt đầu-cuối

Chứng minh rằng:

- Người học hiểu câu hỏi trung tâm của chương.
- Phương trình có thể truy nguyên nguồn.
- Các bước suy luận được giải thích.
- Mô hình có đặc tả kinh tế rõ ràng.
- Implementation số được kiểm tra.
- Kết quả được diễn giải đúng.
- Giao diện phản ánh kết quả thực tế.
- Nội dung chưa xác minh vẫn được đánh dấu đúng.

Sửa các lỗi tìm được trước khi nhân rộng pipeline.

### Phase D — Hoàn thiện các chương còn lại

Lập bảng tiến độ toàn bộ chương dựa trên mục lục đã xác minh.

Với mỗi chương, xác định:

- Trạng thái đọc nguồn.
- Trạng thái bản đồ lập luận.
- Trạng thái phương trình.
- Trạng thái mô hình.
- Trạng thái kiểm thử.
- Trạng thái bài học.
- Trạng thái lab nếu phù hợp.
- Các khoảng trống còn lại.

Tiếp tục xử lý theo độ ưu tiên dựa trên phụ thuộc kiến thức và chất lượng bằng chứng.

Không sao chép cùng một nội dung chung sang các chương.

Không tạo hàng loạt file khung rồi báo cáo đã hoàn thành toàn bộ sách.

### Phase E — Kết nối tri thức toàn sách

Sau khi các chương có nội dung thực chất:

- Kết nối các khái niệm tiên quyết.
- Liên kết phương trình dùng chung.
- Liên kết mô hình nền tảng và mô hình mở rộng.
- Phân biệt các giả định giữa mô hình.
- Ghi lại kết quả nào được kế thừa từ chương trước.
- Kiểm tra quan hệ ngược và quan hệ phụ thuộc.
- Bổ sung điều hướng từ bài học tới mô hình, phương trình và nguồn.

### Phase F — Hoàn thiện ứng dụng và kiểm tra thực tế

1. Build lại ứng dụng từ dữ liệu nguồn chuẩn.
2. Chạy validator và test suite.
3. Mở ứng dụng trong trình duyệt.
4. Kiểm tra một số chương đại diện cho các loại mô hình khác nhau.
5. Kiểm tra các lab thực sự có tương tác.
6. Kiểm tra hiển thị công thức, bảng và đồ thị.
7. Kiểm tra khả năng truy nguyên nguồn.
8. Kiểm tra offline.
9. Kiểm tra lỗi JavaScript và dữ liệu.
10. Cập nhật checkpoint với trạng thái đã xác minh.

Không báo cáo một phase hoàn thành chỉ vì đã tạo xong script hoặc file dữ liệu.

---

## 11. NGUYÊN TẮC BẢO TOÀN WORKSPACE

- Không xóa dữ liệu nghiên cứu hiện có chỉ để tạo cấu trúc sạch hơn.
- Không ghi đè artifacts chưa được kiểm tra.
- Không chạy lại OCR hoặc trích xuất toàn bộ PDF nếu không có nhu cầu thực tế.
- Không tạo registry trùng lặp.
- Không tạo nhiều báo cáo giống nhau.
- Không thêm thư viện không cần thiết.
- Không đổi kiến trúc offline nếu chưa có bằng chứng về lợi ích.
- Không tự tạo nội dung học thuật để lấp chỗ trống.
- Không tự sửa trạng thái chưa xác minh để đạt PASS.
- Không tự động commit.
- Không sửa hoặc xóa các thay đổi không liên quan của người dùng.

Ưu tiên chỉnh sửa trực tiếp các file nguồn đang được ứng dụng sử dụng và giữ artifacts nghiên cứu có thể truy nguyên.

Các checkpoint, logs và báo cáo cập nhật phải nằm trong vị trí hiện hữu phù hợp với cấu trúc dự án; tránh tạo thêm các thư mục và báo cáo không cần thiết.

---

## 12. ĐIỀU KIỆN HOÀN THÀNH SẢN PHẨM

Không sử dụng một tỷ lệ hoàn thành chung để che giấu các khoảng trống học thuật.

Một chương chỉ được xem là **hoàn thành học thuật** khi có bằng chứng cho thấy:

1. Câu hỏi trung tâm được xác định chính xác.
2. Nội dung được đối chiếu với nguồn.
3. Cấu trúc lập luận được tái dựng.
4. Các phương trình trọng yếu được giải thích.
5. Các bước suy luận quan trọng được trình bày.
6. Các giả định và điều kiện được ghi rõ.
7. Kết quả có diễn giải kinh tế.
8. Giới hạn được nêu.
9. Quan hệ với các chương khác có cơ sở.
10. Những phần chưa xác minh được đánh dấu trung thực.

Một mô hình chỉ được xem là **đã xác minh** khi có bằng chứng phù hợp cho đặc tả kinh tế, phương trình, điều kiện áp dụng và implementation liên quan.

Một lab chỉ được xem là **hoạt động thực sự** khi các tham số đầu vào tác động đến phép tính, kết quả số, bảng/đồ thị và phần diễn giải tương ứng; các trường hợp lỗi được xử lý đúng.

Toàn bộ sách chỉ được xem là **đã hoàn thành hệ thống học tập** khi tất cả chương trong mục lục đã xác minh đều được xử lý ở mức chất lượng tương xứng với nội dung thực tế. Không được tuyên bố hoàn thành toàn bộ sách khi còn chương chỉ có scaffold, danh sách khái niệm hoặc nội dung chưa được nghiên cứu.

---

## 13. YÊU CẦU THỰC HIỆN NGAY

Bắt đầu bằng việc kiểm tra workspace và trạng thái hiện tại.

Sau đó, không chỉ trả về một báo cáo audit. Hãy tiếp tục triển khai phần có thể làm ngay dựa trên bằng chứng và artifacts hiện có.

Thứ tự ưu tiên:

1. Xác minh nguồn sách và mục lục.
2. Kiểm tra chất lượng nghiên cứu theo chương.
3. Kiểm tra phương trình, mô hình và provenance.
4. Xác định chương phù hợp nhất để hoàn thiện đầu-cuối.
5. Hoàn thiện bản đọc hiểu và phân tích mô hình của chương đó.
6. Kết nối mô hình với implementation và bài học HTML.
7. Viết hoặc cập nhật tests để chứng minh tính đúng đắn.
8. Tiếp tục mở rộng sang các chương khác theo phụ thuộc kiến thức.
9. Cập nhật checkpoint bằng bằng chứng thực tế.

Nếu có một vấn đề kỹ thuật nhỏ có thể tự giải quyết, hãy tự giải quyết và tiếp tục. Chỉ dừng khi có trở ngại thực sự cần quyết định từ người dùng hoặc khi thiếu nguồn không thể khắc phục bằng các artifacts hiện có.

## 14. BÁO CÁO KẾT QUẢ — NGẮN, CỤ THỂ, CÓ BẰNG CHỨNG

Sau khi triển khai, báo cáo bằng tiếng Việt:

1. **Đã đọc và xác minh:** chương, mục, phương trình hoặc nguồn nào.
2. **Đã phân tích học thuật:** mô hình, lập luận, giả định và kết quả nào.
3. **Đã triển khai:** file nguồn và thành phần nào được sửa.
4. **Đã kiểm thử:** lệnh thực tế, kết quả và phạm vi kiểm thử.
5. **Đã xác minh trên giao diện:** luồng thao tác và lab nào đã thử.
6. **Còn chưa xác minh:** công thức, chương, dữ liệu hoặc quan hệ nào.
7. **Còn bị chặn:** nguyên nhân cụ thể và bằng chứng cần bổ sung.
8. **Bước tiếp theo:** công việc học thuật quan trọng nhất.

Mỗi tuyên bố hoàn thành phải dựa trên bằng chứng. Không ghi PASS nếu chỉ mới tạo file. Không dùng số lượng file làm thước đo chiều sâu nghiên cứu. Không báo cáo một mô hình là đã kiểm chứng nếu mới chỉ kiểm tra rằng solver chạy.

**Tiêu chuẩn cuối cùng: xây dựng một hệ thống giúp người học hiểu được Romer đã lập luận như thế nào, mô hình kinh tế được xây dựng ra sao, phương trình dẫn đến kết quả gì, kết quả phụ thuộc vào giả định nào và có thể kiểm chứng những kết luận đó bằng cách nào.**

Bắt đầu kiểm tra workspace và triển khai ngay theo các nguyên tắc trên.
