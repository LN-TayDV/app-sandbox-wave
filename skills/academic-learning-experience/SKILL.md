---
name: academic-learning-experience
description: Thiết kế, tái cấu trúc và triển khai ứng dụng học thuật tương tác cho kinh tế học, tài chính, toán học và khoa học. Chuyên sâu về cấu trúc khung lý thuyết, tổ chức chương nhiều chủ đề bằng tab, ví dụ có biểu đồ tương tác, phòng thí nghiệm nhiều panel, ma trận và bảng dữ liệu gọn gàng, Vue 3/TypeScript, ECharts, backend Python/FastAPI, Playwright, kiểm thử và checkpoint. Ưu tiên triển khai thực tế, bảo toàn bằng chứng học thuật và xác minh chức năng.
---

# ACADEMIC LEARNING EXPERIENCE ENGINEERING

**Academic Theory → Conceptual Explanation → Mathematical Model → Interactive Visualization → Experiment → Evidence-Based Learning**

Vue 3 · TypeScript · Design Systems · ECharts · Mathematical Models · Interactive Labs · Python/FastAPI · Playwright

## 1. MỤC ĐÍCH VÀ PHẠM VI

Skill này quy định quy trình thiết kế, tái cấu trúc, triển khai và kiểm thử ứng dụng học tập tương tác dựa trên sách giáo khoa, tài liệu nghiên cứu và dữ liệu học thuật.

Phạm vi bao gồm:

- Kinh tế vi mô và kinh tế vĩ mô.
- Kinh tế học tài chính và tài chính doanh nghiệp.
- Phân tích đầu tư, danh mục và quản trị rủi ro.
- Toán học, xác suất, thống kê và khoa học định lượng.
- Ứng dụng biến sách, phương trình, bảng dữ liệu và nghiên cứu thành trải nghiệm học tập trực quan.

Sản phẩm có thể bao gồm chương học, khung lý thuyết, khái niệm, công thức, mô hình, ví dụ, biểu đồ, bảng dữ liệu, ma trận, phòng thí nghiệm, bài tập và đồ thị tri thức.

### Nguyên tắc cốt lõi

**Người học phải hiểu được lý thuyết, quan sát được cơ chế và tự kiểm chứng kết quả bằng tương tác.**

Một ứng dụng không được coi là tốt chỉ vì có giao diện đẹp, nhiều component, nhiều biểu đồ hoặc nhiều slider.

Chất lượng phải được đánh giá dựa trên:

1. Cấu trúc kiến thức rõ ràng.
2. Giải thích lý thuyết có chiều sâu.
3. Tính đúng đắn của công thức và mô hình.
4. Ví dụ gắn với biểu đồ phù hợp.
5. Tương tác thực sự làm thay đổi kết quả.
6. Phòng thí nghiệm dễ hiểu, gọn gàng.
7. Bảng và ma trận giúp đọc dữ liệu hiệu quả.
8. Khả năng truy nguyên nguồn học thuật.
9. Kiểm thử có bằng chứng.
10. Khả năng bảo trì và mở rộng.

Mỗi dự án phải giữ độc lập domain, dữ liệu, công thức, registry, provenance, checkpoint và cấu hình riêng. Skill chỉ chia sẻ quy trình kỹ thuật và nguyên tắc trải nghiệm.

---

## 2. NGUYÊN TẮC THỰC THI

Khi người dùng yêu cầu đại tu hoặc triển khai, phải trực tiếp làm việc trong workspace được chỉ định.

Quy trình mặc định:

1. Khảo sát workspace và trạng thái hiện tại.
2. Đọc checkpoint, kiến trúc, dữ liệu và test liên quan.
3. Xác định đúng nguồn kiến thức và cấu trúc chương.
4. Xây dựng bản đồ lý thuyết, mô hình, ví dụ và thí nghiệm.
5. Thiết kế cấu trúc điều hướng và layout.
6. Chọn hoặc tái sử dụng UI framework và thư viện biểu đồ.
7. Triển khai giao diện và logic tính toán.
8. Kết nối dữ liệu học thuật hiện có.
9. Kiểm thử logic, biểu đồ và trình duyệt.
10. Sửa lỗi và chạy lại test.
11. Cập nhật checkpoint hiện có.
12. Báo cáo kết quả thực tế bằng tiếng Việt.

Không dừng ở audit, kế hoạch, mockup hoặc scaffold nếu nhiệm vụ yêu cầu hoàn thiện sản phẩm.

Không tuyên bố đã kiểm thử, xác minh, cài đặt hoặc triển khai thành công khi chưa có bằng chứng.

Nếu một phần bị chặn, tiếp tục thực hiện những phần không phụ thuộc vào trở ngại đó.

---

## 3. KHẢO SÁT VÀ BẢO TOÀN CODEBASE

Trước khi sửa đổi:

- Xác định workspace và phạm vi được phép thay đổi.
- Đọc entry point, routing, component và stylesheet.
- Kiểm tra `package.json`, lockfile, scripts và phiên bản runtime.
- Xác định framework, UI library và thư viện biểu đồ hiện có.
- Kiểm tra cấu trúc dữ liệu, công thức, model registry và provenance.
- Đọc checkpoint, test và các quy ước hiện hành.
- Xác định dữ liệu nguồn của sách và trạng thái xác minh.
- Kiểm tra cách chạy ứng dụng và quy trình build hiện tại.
- Xác định file/thư mục được bảo vệ.
- Ghi nhận những chức năng đang hoạt động trước khi thay đổi.

Không OCR lại toàn bộ sách nếu dữ liệu đã có và có thể tái sử dụng.

Không xóa lockfile, nâng cấp hàng loạt dependency, thay backend hoặc viết lại ứng dụng chỉ vì muốn sử dụng stack mới.

Không thay dữ liệu học thuật bằng nội dung giả để giao diện có vẻ hoàn chỉnh.

---

# 4. KIẾN TRÚC KIẾN THỨC: TỪ LÝ THUYẾT ĐẾN THÍ NGHIỆM

Mọi nội dung phải được tổ chức theo chuỗi:

**Vấn đề → Khung lý thuyết → Cơ chế → Mô hình → Phương trình → Ví dụ → Biểu đồ → Thí nghiệm → Kết luận → Kiểm tra hiểu biết.**

Đây là cấu trúc logic, không phải yêu cầu tất cả nội dung phải nằm trên một trang dài.

Mỗi loại nội dung phải có cách trình bày phù hợp với mục tiêu học tập.

## 4.1. Khung lý thuyết (Theory Framework)

Khung lý thuyết phải là nơi người học xây dựng cách hiểu về một chủ đề, không phải một vùng chứa định nghĩa.

Tùy bản chất của lý thuyết, trình bày các thành phần sau:

1. **Câu hỏi trung tâm:** Lý thuyết muốn giải thích hiện tượng nào?
2. **Bối cảnh:** Vấn đề xuất hiện trong hoàn cảnh nào?
3. **Giả định:** Mô hình giả định điều gì?
4. **Các chủ thể và biến số:** Những đối tượng nào tham gia và chúng có vai trò gì?
5. **Cơ chế:** Các biến tác động lẫn nhau thông qua quá trình nào?
6. **Mệnh đề hoặc kết luận:** Lý thuyết dự đoán điều gì?
7. **Phương trình:** Quan hệ toán học biểu diễn cơ chế.
8. **Biểu đồ hoặc sơ đồ:** Cách quan sát cơ chế bằng hình ảnh.
9. **Bằng chứng hoặc ví dụ:** Nội dung nào minh họa cho lý thuyết?
10. **Giới hạn:** Lý thuyết không giải thích được điều gì, hoặc kết luận phụ thuộc vào giả định nào?
11. **Liên kết:** Lý thuyết này kế thừa hoặc bổ sung kiến thức nào?

Không ép tất cả lý thuyết vào một biểu mẫu giống nhau. Mô hình tối ưu hóa, lý thuyết hành vi, mô hình cân bằng và lý thuyết thực nghiệm có thể cần cấu trúc giải thích khác nhau.

### Trình bày lý thuyết theo nhiều lớp

**Lớp 1 — Trực giác**

Giải thích hiện tượng bằng ngôn ngữ tự nhiên, bắt đầu từ một câu hỏi hoặc tình huống dễ hình dung.

**Lớp 2 — Cơ chế**

Chia cơ chế thành từng bước. Làm rõ nguyên nhân, biến trung gian, kết quả và điều kiện áp dụng.

**Lớp 3 — Mô hình**

Xác định biến số, tham số, giả định và quan hệ giữa chúng.

**Lớp 4 — Toán học**

Trình bày phương trình, giải thích từng ký hiệu và chỉ ra cách suy ra kết quả khi nguồn hỗ trợ.

**Lớp 5 — Quan sát**

Dùng biểu đồ, bảng hoặc sơ đồ để người học kiểm tra kết quả.

**Lớp 6 — Phản biện**

Nêu giới hạn, tình huống ngoại lệ và câu hỏi giúp người học nhận biết khi nào không nên áp dụng máy móc mô hình.

Không bắt buộc một lý thuyết phải có đủ sáu lớp nếu nguồn không hỗ trợ; phải ghi nhận nội dung còn thiếu thay vì tự bịa.

## 4.2. Khung trình bày phương trình

Mỗi phương trình quan trọng phải có:

- Phương trình được trình bày dễ đọc.
- Ý nghĩa kinh tế hoặc khoa học.
- Giải thích các biến và tham số.
- Giả định, miền xác định và điều kiện áp dụng.
- Diễn giải quan hệ giữa các biến.
- Ví dụ tính toán khi phù hợp.
- Liên kết tới biểu đồ hoặc thí nghiệm tương ứng.
- Nguồn hoặc trạng thái xác minh theo quy ước của dự án.

Với phương trình suy ra từ một mô hình, giải thích các bước biến đổi cần thiết. Không chỉ đưa ra công thức cuối cùng rồi yêu cầu người học tự đoán.

Nếu công thức phức tạp, chia thành các bước có thể mở rộng hoặc điều hướng; không dồn toàn bộ chứng minh vào một khối văn bản lớn.

## 4.3. Khung trình bày cơ chế

Khi giải thích một cơ chế, ưu tiên sơ đồ:

`Đầu vào → Quy tắc hoặc quyết định → Tác động trung gian → Kết quả`

Đây chỉ là ví dụ về cách tổ chức. Cấu trúc thực tế phải phù hợp với mô hình.

Phải phân biệt rõ:

- Biến ngoại sinh và biến nội sinh.
- Tham số và biến trạng thái.
- Giả định và kết luận.
- Quan hệ nhân quả được mô hình hóa và quan hệ chỉ mang tính tương quan.
- Cân bằng ban đầu và cân bằng sau thay đổi.
- Dữ liệu quan sát và dữ liệu giả định.

---

# 5. CẤU TRÚC CHƯƠNG NHIỀU CHỦ ĐỀ: BẮT BUỘC CÓ PHÂN CẤP

Không trình bày một chương có nhiều chủ đề như một trang HTML kéo dài liên tục.

## 5.1. Cấu trúc cấp chương

Mỗi chương có thể bao gồm:

- Tổng quan chương.
- Khung lý thuyết.
- Các chủ đề hoặc bài học.
- Phương trình và mô hình.
- Ví dụ minh họa.
- Phòng thí nghiệm liên quan.
- Bài tập và tự kiểm tra.
- Liên kết kiến thức.

Không bắt buộc mọi chương có đủ mọi mục; chỉ hiển thị mục có nội dung thực.

## 5.2. Quy tắc chia tab

Nếu một chương có nhiều chủ đề độc lập hoặc nội dung quá dài, phải chia thành các tab theo **cấu trúc kiến thức**, không chia tùy tiện theo số lượng component.

Ví dụ về bố cục:

- Tổng quan.
- Chủ đề 1.
- Chủ đề 2.
- Chủ đề 3.
- Mô hình và công thức.
- Ví dụ và ứng dụng.
- Tự kiểm tra.

Đây là ví dụ, không phải mẫu cố định cho mọi chương.

Nếu một chủ đề lớn còn chứa nhiều tiểu chủ đề, tiếp tục chia thành tab con hoặc danh mục nội dung cấp hai. Không tạo quá nhiều tầng khiến người dùng không biết mình đang ở đâu.

### Quy tắc chọn giữa tab, panel và accordion

| Tình huống | Cách trình bày ưu tiên |
|---|---|
| Nhiều chủ đề ngang hàng | Tab cấp một |
| Một chủ đề có nhiều phần liên quan | Tab con hoặc danh mục nội bộ |
| Nội dung phụ, ít khi cần xem | Accordion |
| Công thức và giải thích ngắn | Panel |
| Biểu đồ và điều khiển cần quan sát đồng thời | Panel chia cột |
| Bảng dữ liệu lớn | Khu vực dữ liệu có bộ lọc hoặc phân trang phù hợp |
| Chi tiết bổ sung trên màn hình nhỏ | Drawer hoặc panel thu gọn |
| Các bước học tuần tự | Stepper hoặc điều hướng bài học |

Không dùng tab để chia một bài viết thành quá nhiều mảnh nhỏ thiếu ngữ cảnh.

## 5.3. Giữ ngữ cảnh điều hướng

Người học phải luôn biết:

- Đang ở chương nào.
- Đang học chủ đề nào.
- Chủ đề này thuộc phần nào.
- Phần trước và sau là gì.
- Có ví dụ, biểu đồ hoặc thí nghiệm liên quan hay không.

Khi chuyển tab, giữ trạng thái học và tham số Lab nếu phù hợp. Không tự reset mọi thứ khiến người dùng mất tiến trình.

Trên màn hình nhỏ, tab phải cuộn ngang có kiểm soát hoặc chuyển thành menu chọn; không để nhãn bị cắt không thể đọc.

---

# 6. VÍ DỤ MINH HỌA: BIỂU ĐỒ LÀ THÀNH PHẦN HỌC TẬP

**Mọi ví dụ có thể biểu diễn bằng quan hệ định lượng hoặc mô hình phải có biểu đồ phù hợp và tương tác thực sự.**

Không chấp nhận ví dụ định lượng chỉ có đoạn văn và kết quả tính toán nếu quan hệ giữa các biến có thể được trực quan hóa có ý nghĩa.

## 6.1. Cấu trúc một ví dụ hoàn chỉnh

Mỗi ví dụ nên có:

1. **Bối cảnh:** Vấn đề thực tế hoặc tình huống giả định.
2. **Câu hỏi:** Người học cần tìm hiểu điều gì?
3. **Dữ liệu:** Bảng dữ liệu, tham số hoặc các giả định đầu vào.
4. **Mô hình:** Phương trình và điều kiện áp dụng.
5. **Biểu đồ:** Biểu diễn mối quan hệ cốt lõi.
6. **Thao tác:** Thay đổi biến phù hợp với mô hình.
7. **Kết quả:** Các đại lượng được tính toán hoặc quan sát.
8. **Diễn giải:** Vì sao kết quả thay đổi?
9. **Kết luận:** Người học cần rút ra điều gì?
10. **Giới hạn:** Điều gì không thể suy ra từ ví dụ?

Với ví dụ định tính không có mô hình định lượng phù hợp, sử dụng sơ đồ cơ chế, timeline, ma trận so sánh hoặc hình thức trực quan phù hợp khác. Không ép tạo biểu đồ số liệu vô nghĩa chỉ để đáp ứng quy tắc.

## 6.2. Yêu cầu đối với biểu đồ của ví dụ

Biểu đồ phải thể hiện đúng nội dung mà ví dụ đang giải thích:

- Tên biểu đồ rõ ràng.
- Trục, đơn vị và chú giải.
- Đường cong hoặc dữ liệu tương ứng với mô hình.
- Điểm cân bằng, điểm tối ưu hoặc vùng quan trọng nếu phù hợp.
- Tooltip hoặc hiển thị giá trị khi chọn điểm.
- Trạng thái ban đầu có thể tái lập.
- Giải thích kết quả ngay gần biểu đồ.

Nếu ví dụ có các bước tính toán, cần kết nối kết quả từng bước với các giá trị trên biểu đồ khi có thể.

## 6.3. Tương tác của ví dụ

Tùy nội dung, cho phép:

- Điều chỉnh giá, thu nhập, chi phí hoặc các tham số.
- Thay đổi một giả định.
- Chuyển đổi kịch bản.
- So sánh trước và sau.
- Hiển thị hoặc ẩn chuỗi dữ liệu.
- Chọn một điểm để xem diễn giải.
- Đặt lại về dữ liệu mặc định.

Khi thay đổi đầu vào, phải cập nhật đồng bộ:

1. Giá trị tham số.
2. Kết quả tính toán.
3. Biểu đồ.
4. Bảng dữ liệu.
5. Phần diễn giải phụ thuộc vào kết quả.

Không làm cho biểu đồ chuyển động nếu mô hình và kết quả không được tính lại.

---

# 7. PHÒNG THÍ NGHIỆM TƯƠNG TÁC: GỌN, RÕ, CÓ CẤU TRÚC

Phòng thí nghiệm phải được thiết kế như một workspace để khám phá mô hình, không phải một trang tập hợp tất cả widget theo chiều dọc.

## 7.1. Cấu trúc tổng thể

Phân cấp điều hướng theo:

**Phòng thí nghiệm → Nhóm mô hình → Mô hình → Thí nghiệm hoặc kịch bản.**

Các nhóm mô hình phải được xác định từ domain và nội dung thực tế. Không tạo tab không có mô hình thật.

Nếu một nhóm chứa nhiều mô hình, tiếp tục chia thành tab con, menu chọn hoặc danh mục nội bộ.

Chỉ render nội dung đang hoạt động khi phù hợp, thay vì đặt tất cả mô phỏng nối tiếp nhau trên một trang.

## 7.2. Bố cục workspace

Trên màn hình desktop, ưu tiên:

| Vùng | Trách nhiệm |
|---|---|
| Điều hướng mô hình | Chọn nhóm, mô hình và kịch bản |
| Bảng điều khiển | Thay đổi tham số và giả định |
| Vùng trực quan hóa | Biểu đồ, sơ đồ hoặc ma trận |
| Kết quả | Các chỉ số đầu ra và so sánh |
| Giải thích | Diễn giải cơ chế và kết luận |

Các vùng có thể kết hợp khi mô hình đơn giản. Không bắt buộc chia năm cột riêng biệt.

Bố cục thường phù hợp là:

- Cột trái: mô hình và tham số.
- Vùng trung tâm: biểu đồ hoặc ma trận.
- Cột phải hoặc panel dưới: kết quả và giải thích.

Không để panel điều khiển chiếm diện tích lớn hơn nội dung trực quan hóa nếu không có lý do.

Trên màn hình nhỏ, chuyển điều khiển, kết quả và giải thích thành các tab hoặc drawer phù hợp. Không thu nhỏ mọi cột đến mức khó đọc.

## 7.3. Tab cấp một và tab cấp hai

Tab cấp một phân biệt nhóm thí nghiệm. Tab cấp hai phân biệt mô hình hoặc góc nhìn trong cùng nhóm.

Ví dụ minh họa:

- **Thị trường:** Cân bằng, dịch chuyển đường cong, kiểm soát giá.
- **Co giãn:** Co giãn theo giá, theo thu nhập, theo giá chéo.
- **Chi phí:** Chi phí ngắn hạn, chi phí dài hạn, so sánh quy mô.
- **Cấu trúc thị trường:** So sánh các mô hình cạnh tranh khi có trong chương trình học.

Chỉ sử dụng những nhóm phù hợp với nội dung nguồn và dữ liệu có sẵn.

Không tạo một trang dài gồm nhiều mô hình chỉ khác tham số.

## 7.4. Cấu trúc của một thí nghiệm

Mỗi thí nghiệm phải có:

**A. Câu hỏi**

Người học đang kiểm tra giả thuyết hoặc cơ chế nào?

**B. Mô hình**

Phương trình, giả định và miền giá trị.

**C. Điều khiển**

Slider, input, lựa chọn kịch bản hoặc các điều khiển phù hợp.

**D. Trực quan hóa**

Biểu đồ, bảng, ma trận hoặc sơ đồ.

**E. Kết quả**

Các chỉ số đầu ra, giá trị trước/sau và chênh lệch khi phù hợp.

**F. Giải thích**

Diễn giải cơ chế thay vì chỉ thông báo kết quả.

**G. Thử thách**

Câu hỏi dự đoán, khám phá hoặc so sánh kịch bản.

**H. Reset**

Khôi phục trạng thái mặc định và kết quả tương ứng.

Các thành phần có thể được trình bày theo panel, tab hoặc layout chia cột. Không buộc người dùng cuộn qua tất cả các phần nếu chúng có thể quan sát đồng thời.

## 7.5. Quy tắc giảm chiều dài trang

- Chia mô hình thành các tab có ý nghĩa.
- Không render tất cả thí nghiệm cùng lúc nếu chúng không cần được so sánh đồng thời.
- Dùng panel chia cột khi người học cần quan sát điều khiển và kết quả cùng lúc.
- Dùng bảng có giới hạn chiều cao và cuộn nội bộ cho dữ liệu dài.
- Dùng accordion cho giải thích phụ, không dùng để giấu toàn bộ chức năng chính.
- Hạn chế khoảng trắng và card trang trí không cần thiết.
- Giữ nhãn, giá trị và đơn vị của điều khiển gần nhau.
- Không để phần giải thích dài đẩy biểu đồ quan trọng xuống quá xa.
- Cung cấp đường dẫn tới lý thuyết liên quan.
- Giữ trạng thái khi chuyển tab nếu phù hợp.

---

# 8. BẢNG, MA TRẬN VÀ DỮ LIỆU: TRÌNH BÀY GỌN GÀNG

Bảng và ma trận là thành phần chính thức của trải nghiệm học tập, đặc biệt với các mô hình định lượng, so sánh kịch bản và phân tích nhiều biến.

## 8.1. Khi nào dùng bảng?

Dùng bảng khi người học cần:

- Đọc giá trị cụ thể.
- So sánh nhiều trường hợp.
- Theo dõi các bước tính.
- Xem dữ liệu đầu vào và đầu ra.
- Đối chiếu giả định hoặc tham số.
- Kiểm tra kết quả của các kịch bản.

Bảng phải có tiêu đề, tên cột rõ ràng, đơn vị, định dạng số và chú thích cần thiết.

Không chuyển mọi nội dung thành bảng. Đoạn giải thích vẫn cần thiết để người học hiểu ý nghĩa dữ liệu.

## 8.2. Khi nào dùng ma trận?

Dùng ma trận khi có quan hệ hai chiều hoặc cấu trúc theo hàng và cột, chẳng hạn:

- Ma trận tương quan hoặc hiệp phương sai.
- Ma trận so sánh các mô hình theo nhiều tiêu chí.
- Ma trận đầu vào/đầu ra.
- Ma trận chuyển trạng thái.
- Ma trận kịch bản.
- Bảng nhạy cảm theo hai tham số.
- Các cấu trúc toán học có ý nghĩa hàng-cột.

Chỉ dùng loại ma trận phù hợp với kiến thức đang học. Không tạo ma trận chỉ vì muốn giao diện trông chuyên nghiệp.

## 8.3. Quy chuẩn trình bày

- Căn phải số liệu và căn trái văn bản khi phù hợp.
- Hiển thị đơn vị và độ chính xác phù hợp.
- Dùng định dạng nhất quán cho phần trăm, tiền tệ và số âm.
- Phân biệt ô nhập liệu, ô tính toán và ô kết quả.
- Dùng nhãn hàng/cột có ý nghĩa.
- Làm nổi bật hàng tổng, giá trị cân bằng hoặc kết quả quan trọng khi cần.
- Tránh đường viền dày và tô màu quá nhiều.
- Không lặp lại đơn vị ở mọi ô nếu có thể đặt ở tiêu đề cột.
- Có trạng thái rỗng, lỗi và loading phù hợp.
- Với bảng lớn, cân nhắc lọc, sắp xếp, phân trang hoặc cuộn nội bộ.
- Trên màn hình nhỏ, cho phép cuộn ngang có kiểm soát hoặc chuyển thành dạng phù hợp; không ép cột co đến mức không thể đọc.

## 8.4. Ma trận và biểu đồ phải đồng bộ

Khi người dùng thay đổi tham số:

- Cập nhật ma trận hoặc bảng kết quả.
- Cập nhật biểu đồ liên quan.
- Cập nhật các chỉ số tóm tắt.
- Giải thích những thay đổi có ý nghĩa.

Nếu dữ liệu là một ma trận đối xứng, cần giữ tính đối xứng theo định nghĩa mô hình. Nếu có ràng buộc như tổng xác suất bằng 1 hoặc tổng trọng số bằng 1, phải kiểm tra ràng buộc tương ứng.

Không giả định mọi ma trận đều phải đối xứng, khả nghịch hoặc xác định dương. Chỉ áp dụng điều kiện toán học khi mô hình yêu cầu.

## 8.5. So sánh kịch bản

Khi người học so sánh các kịch bản, ưu tiên một bảng tổng hợp:

| Biến hoặc chỉ số | Kịch bản A | Kịch bản B | Chênh lệch |
|---|---:|---:|---:|
| Tham số đầu vào | Giá trị thực tính | Giá trị thực tính | B − A |
| Kết quả chính | Giá trị thực tính | Giá trị thực tính | B − A |

Đây là mẫu trình bày, không phải dữ liệu mặc định để hiển thị trong ứng dụng.

Chỉ tạo cột chênh lệch khi ý nghĩa so sánh phù hợp. Không điền số giả để hoàn thiện bảng.

---

# 9. HỆ THỐNG BIỂU ĐỒ VÀ ECHARTS

Ưu tiên đánh giá Apache ECharts cho biểu đồ tương tác; dùng D3.js khi cần khả năng trực quan hóa chuyên biệt mà ECharts không đáp ứng phù hợp.

Tách ba trách nhiệm:

1. **Domain calculation:** Tính kết quả từ mô hình.
2. **Visualization adapter:** Chuyển dữ liệu thành series, axis, annotation và điểm đánh dấu.
3. **Renderer:** Hiển thị biểu đồ.

Không đặt công thức học thuật cốt lõi trong template hoặc chart options.

## 9.1. Quy tắc biểu đồ

- Có tiêu đề và đơn vị rõ ràng.
- Chọn loại biểu đồ đúng với dữ liệu.
- Trục và miền giá trị có ý nghĩa.
- Có chú giải khi có nhiều series.
- Tooltip hiển thị dữ liệu phù hợp.
- Nhấn mạnh điểm cân bằng, ngưỡng hoặc kết quả chính khi cần.
- Phân biệt dữ liệu thực, dữ liệu giả định và kết quả mô hình.
- Có trạng thái dữ liệu rỗng hoặc lỗi.
- Không tạo series giả khi thiếu dữ liệu.
- Không dùng màu sắc làm phương tiện duy nhất để truyền đạt thông tin.

## 9.2. Vòng đời ECharts trong Vue

- Khởi tạo khi container đã có kích thước phù hợp.
- Cập nhật khi reactive data thay đổi.
- Xử lý resize khi cần.
- Xử lý tab hoặc panel ban đầu bị ẩn.
- Dispose instance khi component bị hủy.
- Kiểm tra NaN, dữ liệu rỗng và miền giá trị không hợp lệ.
- Tránh tạo nhiều chart instance cho cùng một container.

## 9.3. Kiểm thử biểu đồ

Không chỉ kiểm tra biểu đồ có render.

Phải xác minh:

- Dữ liệu được tính đúng.
- Thay đổi tham số làm thay đổi series phù hợp.
- Tooltip và nhãn sử dụng đúng dữ liệu.
- Các điểm quan trọng khớp với kết quả mô hình.
- Reset khôi phục đúng dữ liệu ban đầu.
- Biểu đồ hoạt động khi chuyển tab và thay đổi kích thước màn hình.

---

# 10. KIẾN TRÚC FRONTEND, DOMAIN VÀ BACKEND

## 10.1. Stack mặc định

Ưu tiên:

- Vue 3.
- TypeScript.
- Composition API.
- Vite.
- Vue Router khi cần.
- Một UI framework chính hoặc hệ thống component hiện hữu.
- ECharts cho đồ thị khi phù hợp.

Không tự động chuyển đổi stack nếu dự án hiện tại đang hoạt động tốt.

## 10.2. UI framework

Đánh giá theo nhu cầu và tương thích:

- PrimeVue cho bộ component phong phú.
- shadcn-vue cho component tùy chỉnh sâu.
- Tailwind CSS cho utility và design token.
- CSS variables hoặc CSS modules khi phù hợp với kiến trúc hiện tại.
- Ignite UI for Vue chỉ khi xác minh được package Vue chính thức, tương thích và điều kiện sử dụng.

Không cài nhiều framework chồng chéo chỉ để làm giao diện phong phú.

## 10.3. TypeScript

- Khai báo kiểu cho dữ liệu, props, state, sự kiện và kết quả.
- Bật `strict: true` khi tương thích.
- Không dùng `any` tùy tiện.
- Không dùng `@ts-ignore` để che lỗi.
- Kiểm tra JSON ở runtime khi cần.
- Phân biệt dữ liệu thiếu với giá trị 0.
- Tách logic học thuật khỏi component giao diện.

## 10.4. Backend Python

Chỉ xây dựng backend khi có nhu cầu thực tế như API, tính toán khoa học nặng, xử lý dữ liệu lớn hoặc dùng chung dữ liệu giữa nhiều client.

Ưu tiên FastAPI khi cần Python API, nhưng phải kiểm tra môi trường và dependency hiện có.

Nếu có backend:

- Xác định request/response.
- Kiểm tra input và output.
- Phân biệt lỗi HTTP, lỗi dữ liệu và lỗi mô hình.
- Tách API client khỏi component Vue.
- Tách domain calculation khỏi transport.
- Xác định nguồn tính toán chính.
- Kiểm thử hợp đồng API và các phép tính quan trọng.

Không tạo backend giả chỉ để lấp đầy cấu trúc thư mục.

---

# 11. DATA CONTRACT, PROVENANCE VÀ TÍNH ĐÚNG ĐẮN

Mỗi nội dung học thuật cần giữ quan hệ với nguồn và mô hình của nó.

Khi cấu trúc dữ liệu hỗ trợ, cần phân biệt:

- Nội dung giải thích.
- Định nghĩa và khái niệm.
- Phương trình.
- Tham số và dữ liệu đầu vào.
- Kết quả tính toán.
- Cấu hình biểu đồ.
- Ví dụ.
- Cấu hình thí nghiệm.
- Câu hỏi kiểm tra.
- Nguồn và trạng thái xác minh.

Không bắt buộc tạo schema mới nếu dự án đã có data contract phù hợp.

### Trạng thái bằng chứng

Giữ nguyên quy ước của dự án. Nếu dự án sử dụng các trạng thái như `VERIFIED`, `DERIVED`, `MOCK` hoặc `UNVERIFIED`, không được tự ý thay đổi ý nghĩa.

Phân biệt:

- Đúng về mặt hiển thị.
- Đúng về mặt tính toán.
- Đúng về mặt mô hình.
- Đúng về mặt nguồn học thuật.

Đây là bốn tiêu chí riêng biệt.

Không bịa công thức, dữ liệu, giả định, trích dẫn hoặc số trang. Không đổi trạng thái xác minh chỉ để validator vượt qua.

---

# 12. THIẾT KẾ SYSTEM COMPONENT

Tổ chức component theo trách nhiệm. Các tên dưới đây là gợi ý, không phải danh sách bắt buộc phải tạo đầy đủ.

### Lý thuyết và nội dung

- `TheoryFramework`
- `ConceptExplainer`
- `MechanismDiagram`
- `EquationPanel`
- `AssumptionPanel`
- `LessonNavigator`
- `ChapterWorkspace`

### Ví dụ và biểu đồ

- `WorkedExample`
- `InteractiveChart`
- `ChartAnnotation`
- `ScenarioComparison`
- `CalculationSteps`

### Dữ liệu

- `DataTable`
- `MatrixView`
- `SensitivityTable`
- `ResultSummary`

### Phòng thí nghiệm

- `LabWorkspace`
- `LabTabNavigation`
- `ModelSelector`
- `ParameterPanel`
- `ExperimentChart`
- `ExperimentResults`
- `ExperimentExplanation`
- `ExperimentChallenge`

### Kiểm tra kiến thức

- `KnowledgeCheck`
- `AnswerFeedback`
- `LearningProgress`

Không gom toàn bộ ứng dụng vào một component khổng lồ. Không tạo component dùng chung nếu nó làm tăng độ phức tạp hoặc khiến cấu trúc nội dung bị cứng nhắc.

---

# 13. ACCESSIBILITY, RESPONSIVE VÀ UTF-8

- Đảm bảo tiếng Việt đầy đủ dấu và mã hóa UTF-8.
- Không để lỗi mojibake, ký tự thay thế hoặc nhãn bị cắt.
- Điều hướng tab hỗ trợ bàn phím và có trạng thái focus rõ ràng.
- Nhãn input phải gắn với điều khiển.
- Không dùng màu sắc làm tín hiệu duy nhất.
- Giữ độ tương phản và kích thước chữ dễ đọc.
- Kiểm tra desktop, tablet và màn hình nhỏ.
- Đảm bảo bảng lớn có cách xem phù hợp.
- Đảm bảo biểu đồ không bị cắt hoặc sai kích thước khi tab chuyển trạng thái.
- Không thu nhỏ chữ để nhồi thêm dữ liệu.

Ưu tiên thiết kế nội dung dễ đọc trước, sau đó tối ưu mật độ thông tin.

---

# 14. TESTING VÀ PLAYWRIGHT

Trước khi cài công cụ mới, kiểm tra dependency và test hiện có.

Sử dụng Vitest cho logic và unit test khi phù hợp; Playwright cho luồng trình duyệt khi môi trường hỗ trợ.

### Luồng kiểm thử bắt buộc khi có chức năng tương ứng

1. Mở ứng dụng.
2. Điều hướng tới một chương.
3. Chuyển giữa các chủ đề hoặc tab.
4. Mở khung lý thuyết.
5. Xem phương trình và chú giải.
6. Mở ví dụ và biểu đồ.
7. Thay đổi tham số.
8. Xác minh kết quả tính toán thay đổi đúng.
9. Xác minh bảng và biểu đồ đồng bộ.
10. Mở phòng thí nghiệm.
11. Chuyển nhóm mô hình và tab con.
12. Chạy thí nghiệm và reset.
13. Kiểm tra dữ liệu rỗng hoặc đầu vào không hợp lệ.
14. Kiểm tra viewport hẹp.
15. Kiểm tra console và tài nguyên thất bại.

Không chỉ kiểm tra SVG hoặc canvas tồn tại. Phải xác minh kết quả đầu ra hoặc trạng thái mô hình có thể quan sát.

Phân biệt rõ unit test, integration test, build, type-check, E2E và kiểm tra thủ công. Chỉ đánh dấu PASS cho những phần thực sự được kiểm tra.

Không giảm assertion hoặc thay test thật bằng mock để tạo kết quả PASS giả.

---

# 15. QUY TRÌNH TRIỂN KHAI

## Bước 1 — Inspect

Khảo sát codebase, checkpoint, dữ liệu, mô hình và test.

## Bước 2 — Map Knowledge

Xây dựng bản đồ chương → chủ đề → lý thuyết → mô hình → phương trình → ví dụ → biểu đồ → Lab.

## Bước 3 — Structure

Xác định cấp điều hướng, các tab, panel, bảng, ma trận và các điểm liên kết giữa nội dung.

## Bước 4 — Design

Xây dựng hoặc điều chỉnh design system và layout dựa trên mục tiêu học tập.

## Bước 5 — Implement

Triển khai component, dữ liệu và logic tính toán.

## Bước 6 — Integrate

Kết nối nguồn dữ liệu và mô hình hiện có. Không thay bằng dữ liệu giả.

## Bước 7 — Verify

Chạy build, type-check, unit test, integration test và E2E phù hợp.

## Bước 8 — Fix

Sửa lỗi và chạy lại các kiểm tra bị ảnh hưởng.

## Bước 9 — Checkpoint

Cập nhật checkpoint hiện có với kết quả thực tế.

## Bước 10 — Report

Báo cáo ngắn gọn bằng tiếng Việt, có bằng chứng và nêu rõ phần chưa hoàn thành.

Không dừng ở việc tạo bản đồ nội dung hoặc prototype nếu yêu cầu là triển khai sản phẩm.

---

# 16. CHECKPOINT VÀ QUẢN LÝ PHẠM VI

Ưu tiên cập nhật checkpoint hiện có; không tạo nhiều báo cáo trùng lặp.

Ghi lại:

- Workspace và phạm vi thay đổi.
- Kiến trúc sau chỉnh sửa.
- Component và chức năng đã triển khai.
- Dependency được thêm hoặc thay đổi.
- Chủ đề và chương đã xử lý.
- Biểu đồ và Lab đã kiểm thử.
- Bảng hoặc ma trận đã tích hợp.
- Lệnh kiểm tra, exit code và kết quả test.
- Lỗi còn tồn tại.
- Trạng thái xác minh học thuật.
- Phần chưa được kiểm tra.
- Trạng thái browser verification.

Không ghi kết quả cũ thành kết quả hiện tại. Không commit nếu chưa được yêu cầu. Không sửa ngoài phạm vi cho phép.

---

# 17. TIÊU CHÍ NGHIỆM THU

## A. Khung lý thuyết

- [ ] Câu hỏi trung tâm và cơ chế được giải thích rõ.
- [ ] Giả định, biến số và điều kiện áp dụng được trình bày phù hợp.
- [ ] Phương trình có giải thích ký hiệu và ý nghĩa.
- [ ] Nội dung phân biệt trực giác, cơ chế, mô hình và giới hạn.
- [ ] Không thay lý thuyết bằng danh sách định nghĩa.

## B. Tổ chức chương

- [ ] Chủ đề được chia theo cấu trúc kiến thức.
- [ ] Chương dài được phân cấp bằng tab hoặc panel phù hợp.
- [ ] Không có trang kéo dài chỉ vì mọi nội dung được nối liên tục.
- [ ] Người học biết mình đang ở đâu và cách quay lại.
- [ ] Các liên kết giữa lý thuyết, ví dụ và Lab hoạt động.

## C. Ví dụ và biểu đồ

- [ ] Ví dụ định lượng có biểu đồ phù hợp khi có ý nghĩa.
- [ ] Biểu đồ phản ánh mô hình thực, không phải hình trang trí.
- [ ] Thay đổi tham số làm cập nhật kết quả.
- [ ] Bảng, biểu đồ và phần giải thích đồng bộ.
- [ ] Dữ liệu giả định được ghi nhãn rõ.
- [ ] Có trạng thái reset và xử lý đầu vào không hợp lệ khi cần.

## D. Phòng thí nghiệm

- [ ] Có phân cấp nhóm mô hình, mô hình và kịch bản.
- [ ] Các nhóm nhiều chủ đề được chia tab hợp lý.
- [ ] Điều khiển, biểu đồ, kết quả và giải thích dễ hiểu.
- [ ] Không render tất cả mô hình nối tiếp thành trang quá dài.
- [ ] Mỗi điều khiển có tác động thực tới mô hình.
- [ ] Có bảng hoặc ma trận khi đó là cách biểu diễn phù hợp.
- [ ] Các trạng thái mô hình và reset được kiểm thử.

## E. Bảng và ma trận

- [ ] Đơn vị và tiêu đề cột rõ ràng.
- [ ] Định dạng số nhất quán.
- [ ] Giá trị nhập, giá trị tính và kết quả được phân biệt.
- [ ] Bảng lớn có cách xem phù hợp.
- [ ] Ràng buộc toán học được kiểm tra khi mô hình yêu cầu.

## F. Kỹ thuật và kiểm thử

- [ ] Codebase và dữ liệu hiện có được bảo toàn.
- [ ] Type-check và build đã chạy khi có cấu hình tương ứng.
- [ ] Các test liên quan đã chạy.
- [ ] E2E chỉ được đánh dấu PASS khi trình duyệt thực sự chạy.
- [ ] Tiếng Việt UTF-8 hiển thị chính xác.
- [ ] Checkpoint được cập nhật.
- [ ] Lỗi và phần chưa xác minh được ghi rõ.

**Không được đánh dấu hoàn thành chỉ vì giao diện đã render. Phải xác minh cả trải nghiệm học tập, tính đúng của mô hình và hành vi tương tác.**

---

# 18. ĐỊNH DẠNG BÁO CÁO CUỐI

Báo cáo ngắn gọn bằng tiếng Việt:

1. Các khu vực đã thay đổi.
2. Cách tổ chức khung lý thuyết và chủ đề.
3. Các tab/panel đã triển khai.
4. Ví dụ, biểu đồ, bảng và ma trận đã hoàn thiện.
5. Các thí nghiệm đã kiểm thử.
6. Lệnh kiểm tra và kết quả thực tế.
7. Các lỗi còn tồn tại và phần chưa xác minh.

Không báo cáo PASS khi chưa có bằng chứng. Không thay báo cáo triển khai bằng một kế hoạch dài.

**Mục tiêu cuối cùng: biến kiến thức thành trải nghiệm học tập có cấu trúc — đọc hiểu được, nhìn thấy được, thao tác được và kiểm chứng được.**
