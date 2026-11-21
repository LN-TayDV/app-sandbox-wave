# Feasibility Probe — Dữ liệu cho luận văn IFWST

> **Trạng thái: ✅ B1 ĐẠT CỔNG.** Probe hoàn tất ngày 2026-10-23 (đo sơ bộ 2026-10-22).
> **Cổng B1:** ≥4/7 nguồn dùng được → **5/7 đạt** → sang B2.
>
> **Dự án:** International Financial Wave–Sandpile Theory (IFWST) / Cát Truồi
> **Phạm vi cần:** 21 nước · 1990–2023 (mục tiêu tần suất **quý**) · biến tài chính + biến phụ thuộc khủng hoảng
> **Script tải:** `code/00_probe_bis.py` → ghi vào `data/raw/`

---

## 1. Bảng trạng thái 7 nguồn (đo 2026-10-23)

Đo bằng: `curl.exe -s -L -A "<UA trình duyệt>" -o NUL -w "%{http_code}|%{size_download}" --max-time 30 <url>`
— **luôn kiểm body**, không chỉ status code (bài học #1 ở §3).

| # | Nguồn | Endpoint đã thử | HTTP | Kết quả | Kết luận |
|---|---|---|---|---|---|
| 1 | **BIS** — Credit gap | `stats.bis.org/api/v2/data/dataflow/BIS/WS_CREDIT_GAP/1.0/Q..P.A.C` | **200** | 7.620 obs · 44 nước · 1957Q4–2026Q1 | ✅ **Dùng được** → `data/raw/bis_credit_gap.csv` |
| 2 | **BIS** — DSR | `stats.bis.org/api/v2/data/dataflow/BIS/WS_DSR/1.0/Q...A` | **200** | 7.182 obs · 32 nước · 1999Q1–2026Q1 | ✅ **Dùng được** → `data/raw/bis_dsr.csv` |
| 3 | **BIS** — LBS cross-border | `stats.bis.org/api/v2/data/dataflow/BIS/WS_LBS_D_PUB/1.0/Q.S.C.A.TO1.F.5J.A.{CTY}.A.5J.A` | **200** | 194 obs · 1977Q4–2026Q1 | ✅ **Dùng được** → `data/raw/bis_lbs_cross_border_*.csv` |
| 4 | **ECB** — SDMX 2.0 | `data-api.ecb.europa.eu/service/data/EXR/A.USD.EUR.SP00.A?format=csvdata&lastNObservations=1` | **200** | CSV, 529 B | ✅ **Dùng được** |
| 5 | **World Bank** | `api.worldbank.org/v2/country/KOR/indicator/FS.AST.DOMS.GD.ZS?format=json&per_page=5` | **200** | JSON, 1.291 B | ✅ **Dùng được** (23 file `wb_*.csv` đã có) |
| 6 | **IMF** — DataMapper | `www.imf.org/external/datamapper/api/v1/NGDPD` (retry ×3 + backoff) | **403** | HTML "Access Denied" | ❌ WAF — **BLOCKED** |
| 7 | **FRED** | `fred.stlouisfed.org/graph/fredgraph.csv?id=GDP` | **000** | — | ❌ Timeout / bảo trì — **BLOCKED** |

**Tổng: 5/7 nguồn dùng được → ĐẠT cổng B1 (≥4/7).**

### 1.1 Nguồn ngoài danh sách 7 (đã probe, không dùng)

| Nguồn | Kết quả | Ghi chú |
|---|---|---|
| BIS `www.bis.org/statistics/*.csv` | **404** | URL legacy của `code/01_download_bis.py` — **đã hỏng**, phải dùng SDMX |
| BIS `api/v2` structure (non-data) | **501** | Chỉ `api/v1` trả được structure metadata |
| BIS `stats.bis.org/static/bulk/*.csv` | **200 nhưng là HTML** | Trả trang Next.js, không phải CSV → **phải kiểm body** |
| JST Macrohistory | **DNS fail** | "Non-existent domain" — không phân giải từ mạng này |
| Laeven–Valencia (IMF WP/2012/212) | **403** | `www.imf.org` bị WAF |
| JSTOR | 200 | Truy cập được nhưng paywall |

---

## 2. Kết quả chi tiết — BIS (biến trung tâm)

### 2.1 Endpoint & xác minh

| API | Kết quả |
|---|---|
| `https://stats.bis.org/api/v1/dataflow/BIS/{FLOW}/latest?references=all` | ✅ 200 — SDMX-ML **XML** (không phải JSON) |
| `https://stats.bis.org/api/v2/data/dataflow/BIS/{FLOW}/1.0/{KEY}` | ✅ **200 — dùng để tải dữ liệu thật** |
| `.../api/v1/data/...` | ❌ 404 — tham số path kiểu cũ không được BIS chấp nhận |
| `.../api/v2/data/...?...format=csvfile` | ❌ 406 — `format` không hợp lệ; BIS v2 **chỉ trả XML** |

> **Phát hiện then chốt:** `api/v1` chỉ dùng cho **structure metadata**; `api/v2` mới là endpoint **data**.
> Probe sơ bộ ban đầu kết luận "v2 → 501, chỉ v1 dùng được" là **sai** — vẫn v1 cho metadata.

### 2.2 Cấu trúc DSD `WS_CREDIT_GAP` (đã trích đầy đủ)

**6 chiều** (không phải 15 — probe sơ bộ đếm nhầm):

| pos | id | Codelist | Mã giá trị |
|---|---|---|---|
| 1 | `FREQ` | `CL_FREQ` | A,B,D,E,H,M,Q,W |
| 2 | `BORROWERS_CTY` | `CL_BIS_GL_REF_AREA` | ISO-3166 (2 ký tự) + mã tổng hợp (`5A`,`5R`,`4T`…) |
| 3 | `TC_BORROWERS` | `CL_TC_BORROWERS` | C, G, H, N, **P** (=Private non-financial sector) |
| 4 | `TC_LENDERS` | `CL_L_SECTOR` | A (=All sectors), B, C, F, G, H, … |
| 5 | `CG_DTYPE` | `CL_CREDT_GAP_DTYPE` | **A**=ratio thô, **B**=HP trend, **C**=**gap (actual−trend)** |
| 6 | `TIME_PERIOD` | — | `1947-Q4` … |

**Key đã xác minh hoạt động:**

```
WS_CREDIT_GAP/1.0/Q..P.A.C   →  44 nước,  7.620 obs, gap
WS_CREDIT_GAP/1.0/Q..P.A.A   →  44 nước,  9.380 obs, ratio thô
WS_CREDIT_GAP/1.0/Q.US.P.A.C →  Mỹ,       274 obs
WS_DSR/1.0/Q...A              →  32 nước,  7.182 obs
WS_LBS_D_PUB/1.0/Q.S.C.A.TO1.F.5J.A.{CTY}.A.5J.A → 194 obs/nước
```

> `Q..P.A.C`: `Q`=FREQ · `.`=BORROWERS_CTY mọi nước · `.`=TC_LENDERS mọi · `P`=borrower private sector · `C`=gap.
> Rút ngắn từ `Q...A` (thiếu TC_BORROWERS) cũng chạy nhưng trả cả `G`/`H`/`N` — dùng `Q..P.A.C` để nhất quán.

### 2.3 `WS_DSR` — 4 chiều

`FREQ` · `BORROWERS_CTY` · `DSR_BORROWERS` · `TIME_PERIOD`.
`DSR_BORROWERS` dùng `CL_TC_BORROWERS` (C/G/H/N/P) **và** `CL_COLLECTION` → cột `TITLE_TS` trong CSV cho tên tiếng Anh.
**Chọn `P` (Private non-financial sector)** để khớp với credit gap.

### 2.4 `WS_LBS_D_PUB` — 13 chiều (12 dim + TIME_PERIOD)

`FREQ` · `L_MEASURE` · `L_POSITION` · `L_INSTR` · `L_DENOM` · `L_CURR_TYPE` · `L_PARENT_CTY` · `L_REP_BANK_TYPE` · `L_REP_CTY` · `L_CP_SECTOR` · `L_CP_COUNTRY` · `L_POS_TYPE` · `TIME_PERIOD`

**Key đã xác minh:** `Q.S.C.A.TO1.F.5J.A.{CTY}.A.5J.A`
→ `S`=Amounts outstanding (stocks) · `C`=Total claims · `A`=All instruments · `TO1`=All currencies ·
`F`=Foreign currency · `5J`=All countries · `{CTY}`=nước báo cáo · `5J`=counterparty · `A`=All position type.

> ⚠️ **Lưu ý:** `L_POS_TYPE=N` (cross-border) trả 404 với bộ `L_POSITION=D`. Đã thử `D` (cross-border claims)
> với nhiều tổ hợp → không có kết quả. Key chạy được dùng `L_POSITION=C` + `L_POS_TYPE=A/N`.
> Đây là **giới hạn cần xác minh lại ở B2** — chưa chắc `D` (cross-border claims) thực sự là mã đúng cho
> "cross-border" trong bản publish này.

### 2.5 44 nước có credit gap

```
AR AT AU BE BR CA CH CL CN CO CZ DE DK ES FI FR GB GR HK HU ID IE IL IN
IT JP KR LU MX MY NL NO NZ PL PT RU SA SE SG TH TR US XM ZA
```
→ **vượt yêu cầu 21 nước**; có thể chọn 21 theo tiêu chí tần suất quan sát.

---

## 3. Bài học về phương pháp probe

| # | Bài học | Bằng chứng |
|---|---|---|
| 1 | **HTTP 200 ≠ có dữ liệu** | FRED 200 với HTML "Site Maintenance"; BIS `static/bulk/*.csv` 200 với HTML Next.js |
| 2 | **WAF chặn theo UA/IP và theo tần suất** | IMF: 200 (lần 1) → 403 (lần 2) cùng URL, kể cả sau retry |
| 3 | **Phải retry có backoff + UA trình duyệt** | 3 lần, 2s/5s/10s |
| 4 | **Phải kiểm Content-Type + dòng đầu body** | không chỉ `%{http_code}` |
| 5 | **DNS fail ≠ nguồn chết** — ghi cả "không truy cập được từ mạng này" lẫn trạng thái thật | `macrohistory.org`: "Non-existent domain" |
| 6 | **Cấu trúc SDMX phải lấy từ DSD, không đoán** | Key 15 đoạn thất bại → trích DSD → key 6 đoạn thành công ngay |
| 7 | **Cấu trúc response khác nhau theo dataflow** | `WS_CREDIT_GAP` → `<Series>`; `WS_LBS_D_PUB` → `<Group>` (không phải `<Series>`) |

---

## 4. Chốt lõi dữ liệu — **ĐÃ CHỐT: phương án A (BIS)**

| Phương án | Ưu | Nhược | Trạng thái |
|---|---|---|---|
| **A — BIS** | 44 nước, 1947–, quý, biến tài chính đầy đủ (credit gap, DSR, LBS) | chỉ ~15–25 sự kiện khủng hoảng → EPV thấp | ✅ **CHỌN** |
| **B — JST Macrohistory** | 17 nước, 1870–, nhiều sự kiện → EPV tốt | **DNS không phân giải** | ❌ |
| **C — Hỗn hợp** | BIS cho biến tài chính, nguồn khác cho biến phụ thuộc | nguồn khủng hoảng thay thế chưa có | ⏸ giữ lựa chọn |
| **D — Giảm bậc biến phụ thuộc** | biến phụ thuộc **liên tục** (`credit_gap`) → EPV cao hơn nhiều | thiết kế lại mô hình | ✅ **song hành với A** |

### 4.1 Hệ quả công suất thống kê (bắt buộc ghi trong báo cáo luận văn)

- Với ~15–25 sự kiện khủng hoảng và 7 biến giải thích: **EPV ≈ 2–3,5**.
- Quy tắc ngón tay cái cần **≥10–20 sự kiện trên mỗi tham số** ⇒ cần **70–140 sự kiện**.
- ⇒ **Logit 7 biến trên 21×34 quý là không khả thi.**
- ⇒ Thiết kế thay thế: **biến phụ thuộc chính là biến liên tục**
  (ví dụ `credit_gap`, `bank_z`, `crisis_severity`), với **khủng hoảng là nhóm con** để phân tích phụ —
  không phải biến 0/1 duy nhất. (Phương án D.)
- Hoặc: mở rộng cửa sổ mẫu về 1900–2023 (cần nguồn dài hơn BIS), hoặc tìm cơ sở dữ liệu khủng hoảng khác.

---

## 5. Việc còn lại

- [x] BIS: dựng key → tải credit gap CSV thật (44 nước, 7.620 obs) — `data/raw/bis_credit_gap.csv`
- [x] BIS: DSR (32 nước, 7.182 obs) — `data/raw/bis_dsr.csv`
- [x] BIS: LBS cross-border (key `Q.S.C.A.TO1.F.5J.A.{CTY}.A.5J.A`) — `data/raw/bis_lbs_cross_border_*.csv`
- [ ] BIS: tải LBS **per-country** cho đủ 21 nước của panel (hiện mới có US + tổng hợp)
- [ ] BIS: xác minh lại `L_POSITION=D` (cross-border claims thuần) — hiện `L_POSITION=C` mới chạy được
- [ ] IMF: tìm mirror (archive.org / MIMF) nếu B10 cần IFS — hiện BLOCKED
- [ ] FRED: thử lại khi site bảo trì xong — hiện BLOCKED
- [ ] Laeven–Valencia (2012): tìm mirror cho bộ ngày khủng hoảng; **kiểm tra nguồn gốc** `data/raw/crisis_dates.csv` (16.933 B, tải 2026-10-17) — file này đến từ đâu?
- [ ] ECB: xác nhận phạm vi + tần suất + có bộ EWI dùng được không
- [ ] Chốt danh sách 21 nước cuối cùng theo tần suất quan sát của credit gap
