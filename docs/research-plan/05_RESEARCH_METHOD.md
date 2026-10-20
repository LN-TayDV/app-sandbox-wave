# 05 — Kiến trúc phương pháp nghiên cứu

## Nguyên tắc lựa chọn phương pháp

Chọn theo câu hỏi nghiên cứu, cấu trúc dữ liệu và điều kiện nhận diện — không chọn vì phức tạp.

## Phương pháp ứng viên (không áp đặt toàn bộ)

| Phương pháp | Trả lời câu hỏi | Dữ liệu cần | Giả định/Hạn chế | Nghiệm thu |
|---|---|---|---|---|
| Tổng quan lý thuyết | Cơ chế? | Tài liệu | Bias lựa chọn | Protocol rõ |
| Phân tích mô tả | Mức độ? | Dữ liệu | Không nhân quả | EDA report |
| Chuỗi thời gian (ADF, cointegration) | Tính dừng/quan hệ dài hạn? | TS | Giả định tuyến tính | Test results |
| VAR/VECM | Động lực? | TS đa biến | Errore nhận diện | IRF + robust |
| Nhân quả Granger | Dự báo? | TS | Không phải nhân quả cấu trúc | Test + caveat |
| Chuyển đổi chế độ (MS) | Phi tuyến theo chế độ? | TS đủ dài | Số chế độ giả định | Model fit + robust |
| Phân tích chu kỳ (filter, spectral) | Tần suất/biên độ? | TS | Filter-dependent | Sensitivity |
| Phân tích độ nhạy/độ bền | Ổn định? | Kết quả | Multiple testing | Report |
| Mô phỏng | Minh họa cơ chế? | Tham số giả định | Không phải dữ liệu thực | Label rõ |

## Quy trình lựa chọn

1. Xác định RQ (WP5).
2. Xác định dữ liệu khả dụng (WP7).
3. Đánh giá điều kiện nhận diện.
4. Chọn phương pháp đơn giản nhất đủ trả lời RQ.
5. Ghi lý do & lựa chọn thay thế vào Decision Log.

Không áp đặt mô hình phức tạp nếu dữ liệu không hỗ trợ.
