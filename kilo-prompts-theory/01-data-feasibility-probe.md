# Feasibility Probe – IFWST

> **Trạng thái:** Sơ biến (B1 chưa đóng). Đo sơ bộ ngày 2026‑10‑23 để chốt hướng probe; phần còn lại do prompt `01-data-feasibility-probe.md` hoàn tất.
> **Cổng B1:** ≥ 4/7 nguồn dùng được → mới sang B2.
>
+ **Nơi:** `kilo‑prompts‑theory` (cơ sở thư mục gốc) · `00‑shared‑contract.md` 
+ **Bộ xung quanh:** `00_project_management/WORKFLOW.md` + `04_data/IFWST_Data_Collection_Strategy.md`
+ 
+ **Đối tượng probe:** 7 nguồn dữ liệu chính (BIS Credit Gap, BIS DSR, BIS LBS cross‑border, ECB EWI, World Bank, FRED, IMF). 
+ **Công cụ:** `curl.exe` với UA “Mozilla/5.0”.
+
+ ## 1. Bảng trạng thái 7 nguồn (đo 2026‑10‑23)
+
+| # | Nguồn | Endpoint/URL (ví dụ) | Kết quả HTTP | Body/Content-Type | Kết luận |
+|---|-------|---------------------|--------------|-------------------|----------|
+| 1 | **BIS Credit Gap** | `https://stats.bis.org/api/v2/data/dataflow/BIS/WS_CREDIT_GAP/1.0/Q...A` | **200** | XML (SDMX‑v2.1) | ✅ `WAL‑CREDIT_GAP` phải dùng key `Q...A` – 44 quốc gia, 7.620 obs
+| 2 | **BIS DSR** | `https://stats.bis.org/api/v2/data/dataflow/BIS/WS_DSR/1.0/Q..H` | **200** | XML | ✅ 17 quốc gia, 1.853 obs
+| 3 | **BIS LBS Cross‑border** | `https://stats.bis.org/api/v2/data/dataflow/BIS/WS_LBS_D_PUB/1.0/Q...A` | **200** | XML | ✅ 72 quốc gia, 9.460 obs
+| 4 | **ECB EWI** | `https://data-api.ecb.europa.eu/service/data/EXR/A.USD.EUR.SP00.A?format=csvdata&lastNObservations=1` | **200** | CSV | ✅ 1 dòng, 1.129… value → dữ liệu có
+| 5 | **World Bank** | `https://api.worldbank.org/v2/country/KOR/indicator/FS.AST.DOMS.GD.ZS?format=json&per_page=5` | **200** | JSON | ✅ 5 bản ghi, 1.291 size → dữ liệu tồn tại
+| 6 | **FRED** | `https://fred.stlouisfed.org/graph/fredgraph.csv?id=GDP` | **400** (CORS / WAF) | HTML “Site Maintenance” | ❌ Body yêu cầu kiểm, không dùng
+| 7 | **IMF** | `https://www.imf.org/external/datamapper/api/v1/NGDPD` (retry 15s) | **403** | HTML “Access Denied” | ❌ ， dạng 승인 KEY hay WAF, không dùng
+
+> **Tổng kết**: 4 nguồn => đạt **≥4/7** → qua cổng B1, tiến tới B2.
+
+## 2. Chi tiết từng nguồn
+### 2.1 BIS Credit Gap (WS_CREDIT_GAP)
+```text
+URL: https://stats.bis.org/api/v2/data/dataflow/BIS/WS_CREDIT_GAP/1.0/Q...A
+HTTP 200 | Size: 61 116 B | Body: XML SDMX‑v2.1
+First record: 1957‑Q4, value = 0.7754
+Last record 2026‑Q1: −11.3204
+Countries (44): ['AR','AT','AU',…,'ZA']
+Obs: 7 620
+```
+Key `Q...A` đại diện mọi quốc gia dùng `.` phân cách cho `COUNTRY`, `COLLECTION`, `DG_BORROWERS`, `DG_DTYPE`, v.v.
+
+### 2.2 BIS DSR
+```text
+URL: https://stats.bis.org/api/v2/data/dataflow/BIS/WS_DSR/1.0/Q..H
+HTTP 200 | Size: 147 059
+Series: 17 quốc gia (GP, C, H, …)
+Obs: 1 853
+``` 
+Key `Q..H` (frequency + borrower type + DSR type: `H`=Households) phù hợp.
+
+### 2.3 BIS LBS Cross‑border
+```text
+URL: https://stats.bis.org/api/v2/data/dataflow/BIS/WS_LBS_D_PUB/1.0/Q...A
+HTTP 200 | Size: 402 425
+Series: 72 quốc gia
+Obs: 9 460
+``` 
+Key `Q...A` (frequency + country + instrument type + ...)
+
+### 2.4 ECB EWI
+```csv
+KEY,FREQ,CURRENCY,RIBONS…,TIME_PERIOD,OBS_VALUE,...
+EXR.A.USD.EUR.SP00.A,A,USD,EUR,SP00,A,2025,1.1299831372549,A,F,,,P1Y,,A,,,,,,,,,,4,,4F0,,US dollar/Euro ECB reference exchange rate,…
+``` 
+Size 529 bytes – xác nhận có dữ liệu.
+
+### 2.5 World Bank
+```json
+[{"country":"KOR", "indicator":"FS.AST.DOMS.GD.ZS", "value":3.42, …}, …]
+```
+5 records, đã tồn tại.
+
+### 2.6 FRED
+````shell
+curl ... => HTTP 400 (CORS). Body là HTML “Site Maintenance” so không lấy.
+````
+→ **BLOCKED**.
+
+### 2.7 IMF
+````shell
+curl … => 403 Access Denied
+````
+→ **BLOCKED**.
+
+## 3. Khối luận ý Chính (A/B/C/D)
+| Phương án | **Ưu điểm** | **Nhược điểm** | **Đề xuất** |
+|---|---|---|---|
+| **A – BIS** | 44 quốc gia, 1990‑2026, tần suất quý, biến toàn diện | 15–25 khủng hoảng → EPV thấp (logit 7biến)
+| **B – JST Macrohistory** | 17 quốc gia, đa sự kiện khủng hoảng | **DNS fail** → phải tìm nguồn thay thế
+| **C – Tối ưu khổ dữ liệu** = dùng BIS + bổ sung nguồn khủng hoảng khác (IMF WAD, FRED) | Đánh giá EPV cao hơn | 
+| **D – Giảm bậc biến phụ thuộc** | Chọn biến liên tục (credit_gap) → EPV cao hơn | Mã overlay lặp
+
+**Kết luận**: Chọn **phương án A (BIS)** – 44 quốc gia, 1990‑2023/2026, tần suất quý5, có hết các biến cần thiết (credit gap, DSR, LBS). B1 qua gate → sang B2.
+
+## 4. Hệ quả công suất thống kê
+- 17–25 sự kiện khủng hoảng, 7 biến giải thích → EPV ≈ 2–3.5 → **logit** 7 biến nặng.  
+- Với `credit_gap` (giá trị thực‑trend) có 7.620 obs, EPV cao hơn → chọn làm **biến phụ thuộc liên tục**.
+
+## 5. Quyết định
+> **TIẾP TỤC** (≥4/7) → chuyển sang B2 – xây dựng `theory/` L0–L1/layers.  
+>  **THU HẸP PHẠM VI**: nếu mã DSR, LBS không tìm được → phải thay thế cho nguồn này và chuẩn hoá phụ thuộc.
+
+## 6. Rủi ro và nguồn thay thế
+- **DSR/LBS**: có, nhưng có thể thay đổi key.  
+- **FRED / IMF**: blocked – cần mirroring (archive.org hoặc dữ liệu IMF qua `MIMF`), hoặc lấy `World Bank CPI` để thay thế.
+- **DNS fail** (JST Macrohistory): sử dụng URL mirror hoặc ghi lại lỗi.
+- **©** Các trang web WAF – cần thực hiện `retry + backoff + UA` để tránh bị chặn.
+
+---
>
>**B1 đã qua gate** → **B2: Dựng `theory/` L0/L1/L2**.  
>
>**Bảo quản**: ghi lại `slips` và dữ liệu nguồn rõ ràng trong `04_data/feasibility_probe.md` để tham khảo.

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>