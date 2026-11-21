# TASK: IFWST PHASE 1 — EVIDENCE-BASED LITERATURE REVIEW & RESEARCH GAP IDENTIFICATION

## 1. VAI TRÒ VÀ MỤC TIÊU

Bạn là Research Architect kiêm Financial Economics Researcher, chịu trách nhiệm triển khai **Giai đoạn 1 — Tổng quan tài liệu khoa học** cho dự án:

**International Financial Wave–Sandpile Theory (IFWST)**

Thư mục dự án:

`C:\Users\PC\Documents\AI_project\sandbox-financial`

Đây là nhiệm vụ thực thi nghiên cứu, không phải yêu cầu lập kế hoạch rồi dừng lại.

Bạn phải tự tìm kiếm tài liệu, đọc nguồn, xây dựng ma trận bằng chứng, phản biện giả thuyết, xác định khoảng trống nghiên cứu, tạo các sản phẩm nghiên cứu thực tế và cập nhật trạng thái dự án.

Không được yêu cầu người dùng tìm tài liệu thay bạn khi bạn có thể tự tìm. Chỉ yêu cầu người dùng cung cấp sách hoặc tài liệu khi chứng minh được tài liệu đó cần thiết và không thể truy cập bằng các phương tiện hiện có.

## 2. BỐI CẢNH LÝ THUYẾT CẦN NGHIÊN CỨU

IFWST là giả thuyết nghiên cứu chưa được xác nhận, không phải một lý thuyết đã được khoa học công nhận.

Ý tưởng ban đầu gồm các thành phần:

### 2.1. Sóng xung kích tài chính quốc tế

Một cú sốc có thể bắt đầu tại một quốc gia rồi lan sang các quốc gia khác với độ trễ, cường độ và cơ chế khác nhau.

Các kênh cần xem xét:

- Thị trường tài chính và giá tài sản.
- Tín dụng xuyên biên giới và mạng lưới ngân hàng.
- Thanh khoản, nguồn vốn USD và rủi ro tái cấp vốn.
- Tỷ giá, dòng vốn và cán cân thanh toán.
- Thương mại, sản xuất và chuỗi cung ứng.
- Kỳ vọng, hành vi nhà đầu tư và hiệu ứng bán tháo.
- Phản ứng chính sách tiền tệ, tài khóa và biện pháp ổn định hệ thống.

Các cú sốc thứ cấp có thể phát sinh tại nước tiếp nhận, lan tiếp sang quốc gia khác hoặc phản hồi về nước khởi phát.

Không được mặc định mọi biến động đều là một “sóng” theo nghĩa vật lý. Phải tìm cách định nghĩa và đo lường từng cơ chế bằng dữ liệu kinh tế - tài chính thực tế.

### 2.2. Financial Sandpile — trạng thái dễ tổn thương tích lũy

Trước khi xảy ra cú sốc, mỗi quốc gia có thể mang những mức độ dễ tổn thương khác nhau, gồm:

- Tổng nợ và tăng trưởng tín dụng.
- Nghĩa vụ trả nợ so với thu nhập.
- Đòn bẩy tài chính.
- Kỳ hạn nợ và nhu cầu tái cấp vốn.
- Nợ ngoại tệ và mức độ phụ thuộc vào nguồn vốn quốc tế.
- Mức độ phụ thuộc vào ngân hàng, thị trường vốn hoặc một nhóm chủ nợ.
- Định giá tài sản và mức độ tập trung rủi ro.
- Bộ đệm thanh khoản, dự trữ ngoại hối và năng lực hấp thụ tổn thất.
- Khả năng thanh toán và khả năng tiếp cận nguồn vốn khi thị trường căng thẳng.
- Mức độ kết nối với các quốc gia và tổ chức tài chính khác.

Không được tự ý gộp các biến thành một chỉ số tổng hợp tùy ý. Mỗi biến phải có định nghĩa, đơn vị, nguồn dữ liệu và cơ sở lý thuyết rõ ràng.

Phải phân biệt:
- Thanh khoản với khả năng thanh toán.
- Tổng nợ với nghĩa vụ trả nợ.
- Tổn thất được chuyển từ chủ thể này sang chủ thể khác với tổn thất mới phát sinh cho toàn hệ thống.
- Cú sốc ngoại sinh với phản ứng nội sinh.
- Cú sốc chung toàn cầu với lây lan thực sự từ một quốc gia sang quốc gia khác.

### 2.3. Câu hỏi nghiên cứu trung tâm

“Liệu có thể xây dựng một mô hình định lượng xác định cú sốc tài chính bắt đầu ở đâu, truyền đến những quốc gia nào, qua các kênh nào và với độ trễ bao lâu, tương tác với mức độ dễ tổn thương ban đầu ra sao, tạo ra các cú sốc thứ cấp như thế nào, và trong điều kiện nào biến động trở thành khủng hoảng hệ thống?”

### 2.4. Khung mô hình sơ bộ

Một biểu diễn khái quát có thể là:

\[
\mathbf{x}_{t+1}=F(\mathbf{x}_t,\mathbf{u}_{t+1},\mathbf{A}_t,\boldsymbol{\tau}_t)
\]

Trong đó:
- \(\mathbf{x}_t\): trạng thái tài chính của các quốc gia.
- \(\mathbf{u}_t\): cú sốc.
- \(\mathbf{A}_t\): cấu trúc và cường độ truyền dẫn theo thời gian.
- \(\boldsymbol{\tau}_t\): độ trễ theo kênh và cặp quốc gia.

Đây chỉ là khung ý tưởng. Không được tuyên bố mô hình đã được xác lập hoặc có khả năng dự báo khi chưa có bằng chứng.

## 3. NGUYÊN TẮC NGHIÊN CỨU BẮT BUỘC

### 3.1. Không xác nhận kết luận trước khi có bằng chứng

Không mặc định IFWST là mới, đúng hoặc vượt trội.

Phải sẵn sàng kết luận một trong ba khả năng:

1. Có đóng góp nghiên cứu rõ ràng và có thể kiểm định.
2. Chỉ có đóng góp nếu thu hẹp đáng kể phạm vi.
3. Chưa có đóng góp đủ rõ; cần sửa đổi hoặc từ bỏ một phần giả thuyết.

Nếu tài liệu trước đó đã giải quyết cùng vấn đề, phải ghi nhận và điều chỉnh định hướng.

### 3.2. Phân biệt ba trạng thái bằng chứng

Mọi kết luận quan trọng phải được gắn một trong các trạng thái:

- **CONFIRMED:** Được nguồn đáng tin cậy hỗ trợ trực tiếp.
- **PROVISIONAL:** Nhận định sơ bộ, cần đọc thêm hoặc xác minh.
- **UNVERIFIED:** Chưa có đủ bằng chứng.

Không dùng từ “khoảng trống nghiên cứu đã được xác nhận” khi mới chỉ tìm kiếm sơ bộ.

### 3.3. Không bịa nguồn

Mỗi tài liệu phải có thông tin kiểm chứng được:

- Tác giả.
- Năm.
- Tiêu đề chính xác.
- Tạp chí, nhà xuất bản hoặc tổ chức phát hành.
- DOI hoặc URL chính thức nếu có.
- Loại tài liệu.
- Trạng thái truy cập: đã đọc toàn văn, chỉ đọc abstract, hoặc chỉ tìm thấy thông tin thư mục.
- Phạm vi kết luận có thể rút ra từ nguồn.

Không được tuyên bố đã đọc toàn văn khi chỉ đọc abstract hoặc trang kết quả tìm kiếm.

Ưu tiên bài báo học thuật có phản biện, working paper của BIS/IMF/Federal Reserve/ECB, sách chuyên khảo học thuật và nguồn dữ liệu chính thức.

Nguồn phổ thông chỉ dùng để bổ trợ bối cảnh, không thay thế bằng chứng học thuật.

## 4. BẮT ĐẦU BẰNG KIỂM TRA DỰ ÁN

Trước khi nghiên cứu:

1. Kiểm tra thư mục dự án thực tế.
2. Đọc `README.md`, `PROJECT_STATUS.md`, `RESEARCH_MANIFEST.md` nếu tồn tại.
3. Đọc toàn bộ tài liệu liên quan trong `00_project_management`.
4. Đọc `tasks/init-task.md` nếu tồn tại. Giữ nguyên file này, không ghi đè hoặc chỉnh sửa nếu chưa được cho phép.
5. Đọc `logs/execution_log.md` nếu tồn tại.
6. Kiểm tra các thư mục và tài liệu Phase 0 đã có.
7. Đối chiếu tuyên bố hoàn thành với nội dung thực tế. Không tin trạng thái DONE chỉ vì báo cáo ghi DONE.
8. Lập danh sách những gì thực sự tồn tại, những gì còn thiếu và những mâu thuẫn cần giải quyết.

Không tạo lại các file Phase 0 đã có. Không tạo thêm bản báo cáo trùng lặp chỉ vì muốn có một cấu trúc khác.

Chỉ tạo `01_literature` khi bắt đầu đưa sản phẩm nghiên cứu thực tế vào đó.

Nếu không thể truy cập thư mục dự án hoặc không có quyền ghi, hãy báo rõ giới hạn, tiếp tục các phần nghiên cứu có thể thực hiện và cung cấp nội dung để người dùng áp dụng. Tuyệt đối không giả vờ đã sửa file trên máy người dùng.

## 5. THỰC HIỆN LITERATURE REVIEW THEO CHỦ ĐỀ

Không giới hạn ở từ khóa “sandpile”. Phải khảo sát những nhánh nghiên cứu có thể đã giải quyết từng thành phần của IFWST.

### Nhánh A — Sandpile, criticality và financial fragility

Tìm kiếm:
- Sandpile models in financial systems.
- Self-organized criticality in economics and finance.
- Cascading failures and systemic risk.
- Threshold effects, nonlinear amplification and tipping points.
- Bank failure cascades and financial network structure.

Mục tiêu:
- Xác định chính xác các mô hình sandpile đã tồn tại.
- Tìm hiểu biến nào tích lũy, quy tắc kích hoạt tổn thất, cách mô hình hóa sụp đổ và kết quả đã được chứng minh.
- Xác định IFWST có thực sự bổ sung cơ chế mới hay chỉ đổi tên mô hình có sẵn.

Đặc biệt kiểm tra nghiên cứu IMF Working Paper 2025/041, “Sandcastles and Financial Systems: A Sandpile Metaphor”. Đọc toàn văn nếu truy cập được. Không được tuyên bố mô hình sandpile trong tài chính là đóng góp mới nếu không có bằng chứng phân biệt rõ ràng.

### Nhánh B — International financial contagion và network effects

Tìm kiếm:
- International financial contagion.
- Cross-border banking exposures.
- Financial network systemic risk.
- Common creditors and common asset holdings.
- Direct and indirect contagion.
- Second-round effects and feedback loops.

Mục tiêu:
- Xác định các kênh truyền dẫn đã được mô hình hóa.
- Xác định khi nào sự đồng biến không đồng nghĩa với contagion.
- Làm rõ vai trò của cấu trúc mạng, mức độ tập trung và các vòng phản hồi.

Phải đọc và đối chiếu các tổng quan học thuật có liên quan, gồm:
- Summer (2013), “Financial Contagion and Network Analysis”.
- Jackson và Pernoud (2021), “Systemic Risk in Financial Networks: A Survey”.
- Các nghiên cứu nền tảng liên quan được trích dẫn trong những bài tổng quan này.

### Nhánh C — Liquidity spirals, leverage, fire sales và funding risk

Tìm kiếm:
- Liquidity spirals.
- Funding liquidity and market liquidity.
- Leverage cycles.
- Fire-sale externalities.
- USD funding stress.
- Rollover risk and maturity mismatch.
- Solvency-liquidity interactions.

Đọc Tirole (2011), “Illiquidity and All Its Friends”, cùng các nghiên cứu phù hợp khác.

Mục tiêu:
- Phân biệt những cơ chế có thể gây ra khủng hoảng.
- Xác định cơ chế nào có thể đo lường ở cấp quốc gia.
- Không gộp các loại rủi ro khác nhau vào một khái niệm “độ mong manh” chung chung.

### Nhánh D — Early warning systems và financial vulnerability

Tìm kiếm:
- Early warning indicators of banking crises.
- Credit-to-GDP gap.
- Debt service ratio.
- Credit booms and asset-price booms.
- Foreign-currency debt.
- Cross-border debt.
- Systemic crisis prediction.
- False alarms and out-of-sample validation.

Phải đọc ít nhất các tài liệu sau nếu truy cập được:
- Drehmann và Juselius, “Evaluating Early Warning Indicators of Banking Crises: Satisfying Policy Requirements”.
- Aldasoro, Borio và Drehmann (2018), “Early Warning Indicators of Banking Crises: Expanding the Family”.
- Drehmann (2013), “Total Credit as an Early Warning Indicator for Systemic Banking Crises”.
- Borio và Drehmann (2009), “Assessing the Risk of Banking Crises – Revisited”.

Mục tiêu:
- Xác định các chỉ báo hiện hành đã giải thích được phần nào của Financial Sandpile.
- Đánh giá IFWST có cần một chỉ số mới không, hay nên dùng các biến riêng biệt.
- Thiết lập các mô hình nền để sau này kiểm tra giá trị gia tăng.

### Nhánh E — Financial cycles, macro-financial linkages và nonlinear dynamics

Tìm kiếm:
- Financial cycle and credit cycle.
- Macro-financial feedback.
- Nonlinear time-series models.
- Regime switching and threshold models.
- Time-varying networks.
- Distributed-lag and local-projection approaches.
- Multiscale analysis and wavelet methods.

Mục tiêu:
- Xác định thuật ngữ “wave” nào có cơ sở đo lường.
- Phân biệt chu kỳ, độ trễ, phản ứng động và lan truyền nhân quả.
- Không xem wavelet coherence, tương quan hoặc lead-lag đơn thuần là bằng chứng nhân quả.
- Kiểm tra xem các kỹ thuật này đã được kết hợp trong nghiên cứu quốc tế tương tự hay chưa.

### Nhánh F — Lịch sử khủng hoảng và trường hợp năm 2008

Nghiên cứu cuộc khủng hoảng tài chính toàn cầu 2007–2009.

Phải phân tích:
- Các cú sốc ban đầu tại Mỹ.
- Mức độ dễ tổn thương tích lũy trước khủng hoảng.
- Liên kết giữa các ngân hàng và thị trường tài chính xuyên biên giới.
- Vai trò của chứng khoán hóa, nguồn vốn ngắn hạn, USD funding và thanh khoản.
- Những cơ chế khiến tổn thất lan sang châu Âu và các khu vực khác.
- Những trường hợp chịu cùng cú sốc nhưng kết quả khác nhau.
- Những yếu tố giải thích được bằng lý thuyết hiện có.

Không được đơn giản hóa thành “Mỹ là nguồn phát, châu Âu là nơi khuếch đại” nếu không có bằng chứng theo từng kênh. Quốc gia khởi phát cú sốc không nhất thiết là quốc gia mong manh nhất hoặc khuếch đại mạnh nhất.

### Nhánh G — Các lý thuyết thay thế và nghiên cứu có thể trùng lặp

Tìm kiếm nghiên cứu kết hợp đồng thời:
- Country-level financial vulnerability.
- Cross-border transmission.
- Channel-specific lags.
- Dynamic financial networks.
- Secondary shocks and feedback.
- Threshold-dependent crisis amplification.
- Early-warning performance.

Mục tiêu là tìm các công trình gần IFWST nhất, kể cả các công trình không sử dụng từ “sandpile” hoặc “wave”.

Đây là nhánh quan trọng nhất để đánh giá đóng góp thực sự. Không được kết luận có research gap chỉ vì các bài báo sử dụng thuật ngữ khác nhau.

## 6. PHƯƠNG PHÁP TÌM KIẾM VÀ ĐỌC NGUỒN

Thực hiện theo vòng lặp:

1. Tìm kiếm rộng để lập bản đồ chủ đề.
2. Chọn bài tổng quan và công trình nền tảng.
3. Đọc danh mục tài liệu tham khảo để truy ngược các công trình quan trọng.
4. Tìm nghiên cứu mới hơn trích dẫn các công trình nền tảng.
5. Tìm kiếm theo những giả thuyết và cơ chế cụ thể của IFWST.
6. Đối chiếu các nghiên cứu gần nhất để tìm phần trùng lặp.
7. Đọc toàn văn các nguồn cốt lõi khi có thể.
8. Ghi lại truy vấn, ngày tìm kiếm, nguồn tìm kiếm và kết quả.

Nếu có khả năng truy cập internet, hãy tự tìm nguồn. Nếu không có khả năng truy cập toàn văn:
- Ghi rõ trạng thái.
- Tìm working paper hoặc bản tác giả hợp pháp.
- Không giả vờ đã đọc tài liệu bị khóa.
- Chỉ yêu cầu người dùng tải lên tài liệu khi đó là nguồn cốt lõi và các phương án hợp pháp khác không khả dụng.

Không đặt ra số lượng bài báo tối thiểu một cách máy móc. Ưu tiên độ bao phủ, độ liên quan và khả năng phân biệt các hướng nghiên cứu. Tuy nhiên, không được tuyên bố literature review đã đủ nếu các nhánh chính còn chưa được khảo sát.

## 7. TẠO CÁC SẢN PHẨM NGHIÊN CỨU

Tạo hoặc cập nhật các file sau trong `01_literature`:

### 7.1. `literature_matrix.csv`

Mỗi hàng là một tài liệu đã xác minh. Tối thiểu có các cột:

- source_id
- authors
- year
- title
- publication
- document_type
- DOI
- official_url
- research_question
- theory_or_mechanism
- country_or_unit_of_analysis
- data_and_period
- method_or_model
- main_findings
- limitations
- relevance_to_IFWST
- overlap_with_IFWST
- potential_contribution
- full_text_status
- evidence_status
- verification_notes

Không điền dữ liệu không có bằng chứng. Dùng `UNKNOWN` hoặc `NOT_ACCESSIBLE` khi phù hợp.

### 7.2. `critical_review.md`

Viết tổng quan phản biện bằng tiếng Việt, sử dụng thuật ngữ tiếng Anh trong ngoặc khi cần thiết.

Phải:
- Tổng hợp theo cơ chế và trường phái nghiên cứu, không chỉ tóm tắt từng bài.
- Chỉ ra điểm thống nhất, mâu thuẫn và giới hạn phương pháp.
- Phân biệt kết quả được xác nhận với diễn giải của tác giả.
- Giải thích các lý thuyết hiện có đã giải quyết được phần nào của IFWST.
- Phân tích những vấn đề vẫn chưa được giải quyết hoặc chưa có bằng chứng đủ mạnh.
- Dẫn nguồn ngay tại các kết luận quan trọng.
- Phân biệt rõ nguồn đã đọc toàn văn và nguồn mới chỉ đọc abstract.

### 7.3. `research_gap.md`

Đây là tài liệu quyết định hướng đi của dự án.

Phải trả lời:

1. Những thành phần nào của IFWST đã có trong nghiên cứu trước?
2. Những thành phần nào chỉ được kết hợp một phần?
3. Công trình nào gần IFWST nhất?
4. Khoảng trống tiềm năng nằm ở đâu?
5. Khoảng trống đó đã được xác nhận đến mức nào?
6. Điều gì sẽ bác bỏ tuyên bố về đóng góp?
7. IFWST cần thay đổi hoặc thu hẹp như thế nào?
8. Nên tiếp tục, thu hẹp, tái cấu trúc hay tạm dừng lý thuyết?

Đánh giá từng tuyên bố đóng góp theo các trạng thái:
- CONFIRMED GAP
- PROVISIONAL GAP
- ALREADY ADDRESSED
- NOT TESTABLE WITH AVAILABLE DATA
- REQUIRES FURTHER SEARCH

Không gắn `CONFIRMED GAP` khi chưa kiểm tra đủ các nghiên cứu gần nhất.

### 7.4. `search_log.csv`

Ghi:
- Ngày tìm kiếm.
- Cơ sở dữ liệu hoặc công cụ.
- Truy vấn.
- Nhánh nghiên cứu.
- Số kết quả nếu biết.
- Các nguồn đã chọn.
- Lý do loại nguồn.
- Những vấn đề cần tìm tiếp.

### 7.5. `bibliography.bib`

Tạo danh mục BibTeX từ những tài liệu đã xác minh. Không tự tạo DOI, số trang, tên tạp chí hoặc dữ liệu thư mục.

### 7.6. `model_comparison.md`

Đối chiếu các mô hình cạnh tranh để kiểm tra IFWST:

- **B0 — Baseline vulnerability:** các chỉ báo dễ tổn thương hiện hành.
- **B1 — Network contagion:** B0 cộng các liên kết tài chính xuyên biên giới.
- **B2 — Dynamic transmission:** B1 cộng độ trễ và tương tác theo kênh nếu dữ liệu cho phép.
- **B3 — IFWST candidate:** thêm trạng thái dễ tổn thương động, cú sốc thứ cấp và cơ chế ngưỡng có định nghĩa rõ.

Với mỗi mô hình, nêu:
- Giả định.
- Biến đầu vào.
- Dữ liệu cần có.
- Cơ chế được giải thích.
- Cách nhận diện.
- Khó khăn về nhân quả.
- Phương pháp kiểm định.
- Rủi ro overfitting.
- Điều kiện để mô hình phức tạp hơn bị bác bỏ.

Không tuyên bố B3 vượt trội trước khi kiểm định ngoài mẫu.

### 7.7. `data_feasibility.md`

Đánh giá sơ bộ khả năng kiểm định IFWST bằng dữ liệu thực.

Khảo sát các nguồn như BIS, IMF, FRED/Federal Reserve, ECB, World Bank và nguồn chính thức liên quan.

Với từng nhóm dữ liệu, ghi:
- Tên chuỗi hoặc tập dữ liệu cụ thể nếu xác minh được.
- Định nghĩa biến.
- Đơn vị và tần suất.
- Phạm vi quốc gia và thời gian.
- Độ trễ công bố và revision nếu biết.
- Khả năng tải dữ liệu.
- Chi phí hoặc hạn chế truy cập.
- Những biến chưa có hoặc khó đo.
- Hệ quả đối với thiết kế thực nghiệm.

Không mặc định mọi dữ liệu đều miễn phí hoặc có sẵn theo tần suất mong muốn.

### 7.8. `phase1_summary.md`

Tóm tắt dành cho người ra quyết định:
- Những gì đã xác minh.
- Những gì vẫn chưa rõ.
- Các công trình quan trọng nhất.
- Mức độ trùng lặp với IFWST.
- Khoảng trống tiềm năng.
- Rủi ro lớn nhất của đề tài.
- Hướng nghiên cứu được khuyến nghị.
- Những quyết định cần người dùng phê duyệt.

## 8. GIẢ THUYẾT CẦN PHẢN BIỆN

Kiểm tra các giả thuyết ban đầu sau:

- H1: Áp lực tài chính tích lũy cung cấp thông tin bổ sung ngoài tổng nợ.
- H2: Sự kết hợp giữa các động lực ở nhiều thang thời gian giúp nhận diện trạng thái dễ tổn thương.
- H3: Cùng một cú sốc tạo ra tác động khác nhau tùy trạng thái tài chính ban đầu.
- H4: Liên kết quốc tế, cú sốc thứ cấp và vòng phản hồi có thể khuếch đại tổn thất.
- H5: Mô hình tích hợp cải thiện dự báo ngoài mẫu so với các mô hình nền hiện có.

Với mỗi giả thuyết, ghi:
- Cơ chế kinh tế dự kiến.
- Bằng chứng ủng hộ.
- Bằng chứng phản bác.
- Công trình gần nhất.
- Biến đo lường có thể dùng.
- Thiết kế kiểm định khả thi.
- Các yếu tố gây nhiễu.
- Tiêu chí bác bỏ giả thuyết.

Không xem H1–H5 là đúng chỉ vì chúng xuất phát từ ý tưởng của người dùng.

## 9. ĐÁNH GIÁ ĐÓNG GÓP VÀ TÍNH MỚI

Phải phân biệt:

1. Tính mới về thuật ngữ.
2. Tính mới về cách kết hợp các cơ chế.
3. Tính mới về phương pháp mô hình hóa.
4. Tính mới về nhận diện nhân quả.
5. Tính mới về dữ liệu hoặc phép đo.
6. Giá trị giải thích bổ sung.
7. Giá trị dự báo bổ sung.
8. Giá trị sử dụng cho chính sách.

Đổi tên một mô hình cũ không phải là đóng góp khoa học.

Ghép nhiều cơ chế đã biết cũng không tự động trở thành đóng góp. Phải giải thích được vì sao sự kết hợp tạo ra dự đoán mới, phép đo mới hoặc giá trị kiểm định tăng thêm.

Không khẳng định “chưa có nghiên cứu nào” nếu phạm vi tìm kiếm chưa đủ rộng để hỗ trợ kết luận đó.

## 10. ĐIỀU KIỆN TIẾP TỤC HOẶC THU HẸP ĐỀ TÀI

Khuyến nghị tiếp tục chỉ khi có thể xác định được ít nhất một đóng góp tiềm năng cụ thể, có khả năng đo lường và phân biệt với mô hình hiện có.

Khuyến nghị thu hẹp nếu:
- Chỉ một hoặc hai kênh truyền dẫn có dữ liệu tốt.
- Không thể nhận diện độ trễ của nhiều kênh.
- Không thể tách cú sốc chung toàn cầu khỏi contagion.
- Không thể xây dựng thước đo dễ tổn thương có ý nghĩa kinh tế.
- Mô hình tích hợp quá phức tạp so với dữ liệu.

Khuyến nghị dừng hoặc đổi hướng nếu bằng chứng cho thấy các đóng góp dự kiến đã được nghiên cứu trước giải quyết đầy đủ hoặc không thể kiểm định có ý nghĩa.

## 11. QUẢN LÝ DỰ ÁN VÀ BẢO VỆ FILE

- Giữ nguyên `tasks/init-task.md`.
- Không xóa tài liệu Phase 0.
- Không tạo nhiều bản sao của cùng một báo cáo.
- Không tự ý tái cấu trúc toàn bộ dự án.
- Không tạo thư mục rỗng hàng loạt.
- Không đưa file nghiên cứu vào sai thư mục.
- Không sửa code ứng dụng hoặc các dự án khác.
- Tạo artifact đúng vị trí, cập nhật artifact hiện có khi phù hợp.
- Cập nhật `PROJECT_STATUS.md`, `00_project_management/task_backlog.md`, `00_project_management/decision_log.md` và `logs/execution_log.md` nếu các file này tồn tại và cần cập nhật.
- Ghi rõ đường dẫn file, nội dung đã tạo và bằng chứng kiểm tra.
- Không tuyên bố PASS nếu chưa kiểm tra sản phẩm thực tế.

## 12. TIÊU CHÍ NGHIỆM THU

Chỉ đánh dấu Phase 1 hoàn thành khi:

1. Đã xác minh trạng thái thật của Phase 0.
2. Các nhánh nghiên cứu chính đều có kết quả tìm kiếm và ghi nhận phạm vi khảo sát.
3. Có ma trận tài liệu với nguồn và trạng thái đọc rõ ràng.
4. Có tổng quan phản biện theo cơ chế.
5. Có phân tích research gap, nêu cả bằng chứng phản bác.
6. Có so sánh IFWST với mô hình nền và các hướng thay thế.
7. Có đánh giá khả thi về dữ liệu.
8. Các giả thuyết H1–H5 có tiêu chí kiểm định và bác bỏ.
9. Tài liệu tham khảo được xác minh, không có nguồn bịa.
10. Trạng thái CONFIRMED/PROVISIONAL/UNVERIFIED được dùng nhất quán.
11. Các file đầu ra được đọc lại hoặc kiểm tra bằng công cụ phù hợp.
12. Trạng thái dự án và nhật ký thực thi phản ánh đúng những gì đã làm.

Nếu chưa đạt một tiêu chí, phải ghi rõ phần chưa đạt, tiếp tục thực hiện phần khả thi và không đánh dấu hoàn thành giả tạo.

## 13. CÁCH THỰC THI

Bắt đầu ngay bằng việc kiểm tra dự án và đọc các tài liệu Phase 0.

Sau đó thực hiện tuần tự:
1. Xác minh trạng thái dự án.
2. Lập chiến lược tìm kiếm.
3. Tìm và xác minh nguồn.
4. Đọc các nguồn cốt lõi.
5. Lập ma trận tài liệu.
6. Viết tổng quan phản biện.
7. Đánh giá khoảng trống và giả thuyết.
8. Đánh giá khả thi dữ liệu.
9. Tạo các sản phẩm nghiên cứu.
10. Kiểm tra lại toàn bộ sản phẩm.
11. Cập nhật trạng thái và nhật ký.
12. Đưa ra quyết định khuyến nghị cho Phase 2.

Không dừng lại sau khi viết kế hoạch. Không hỏi người dùng xác nhận từng bước nhỏ. Tự đưa ra quyết định nghiên cứu trong phạm vi được giao và ghi lại những quyết định quan trọng.

Chỉ hỏi người dùng khi có một quyết định không thể tự giải quyết bằng bằng chứng, quyền truy cập hoặc phạm vi hiện có.

**Đầu ra cuối cùng phải là một Phase 1 có bằng chứng, có thể kiểm tra và có khả năng định hướng nghiên cứu tiếp theo — không phải một bài luận quảng bá IFWST.**