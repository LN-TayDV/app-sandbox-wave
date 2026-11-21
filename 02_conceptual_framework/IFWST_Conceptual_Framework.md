# KHUNG KHÁI NIỆM — International Financial Wave–Sandpile Theory (IFWST)

## 1. TỔNG QUAN KIẾN TRÚC

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        IFWST CONCEPTUAL ARCHITECTURE                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐                   │
│  │   LỚP 1    │    │   LỚP 2    │    │   LỚP 3    │                   │
│  │   SÓNG     │───▶│   MẠNG     │───▶│   CẢNH    │                   │
│  │  (WAVE)    │    │  (NETWORK) │    │  (SANDPILE)│                   │
│  └─────────────┘    └─────────────┘    └─────────────┘                   │
│         │                 │                 │                               │
│         ▼                 ▼                 ▼                               │
│  ┌─────────────────────────────────────────────────────┐                   │
│  │              LỚP TÍCH HỢP (INTEGRATION LAYER)       │                   │
│  │    Wave Propagation × Network Contagion × Avalanche  │                   │
│  └─────────────────────────────────────────────────────┘                   │
│                              │                                            │
│                              ▼                                            │
│  ┌─────────────────────────────────────────────────────┐                   │
│  │              LỚP DỰ BÁO (FORECASTING LAYER)         │                   │
│  │    EWI Enhancement × Crisis Timing × Vulnerability   │                   │
│  └─────────────────────────────────────────────────────┘                   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. NỀN TẢNG LÝ THUYẾT

### 2.1 Lớp Sóng Tài Chính (Financial Wave Layer)

**Nguồn lý thuyết:**
- Brunnermeier (2009): Cơ chế truyền dẫn từ thị trường mortgage → hệ thống tài chính
- Cetorelli & Goldberg (2011): 3 kênh truyền dẫn xuyên biên giới
- Popov & Udell (2010): Bằng chứng thực nghiệm từ CEE 2007-2008

**Định nghĩa:**

Một **sóng tài chính** (financial wave) là sự lan truyền của cú sốc tài chính qua:
1. **Kênh trực tiếp** — cho vay xuyên biên giới, tài sản chung
2. **Kênh gián tiếp** — suy luận từ quan hệ, fire sales
3. **Kênh phản hồi** — run ngân hàng, đóng băng tín dụng

**Mô hình toán học:**

```
W(t) = Σᵢ αᵢ · Sᵢ(t-τᵢ) · Φᵢ(t)
```

Trong đó:
- `W(t)` = cường độ sóng tại thời điểm t
- `Sᵢ(t-τᵢ)` = cú sốc nguồn i tại thời điểm t-τᵢ
- `τᵢ` = độ trễ truyền dẫn
- `αᵢ` = hệ số truyền dẫn
- `Φᵢ(t)` = hàm suy hao theo thời gian

### 2.2 Lớp Mạng (Network Layer)

**Nguồn lý thuyết:**
- Jackson & Pernoud (2021): Khung tổng quan hệ mạng và rủi ro hệ thống
- Allen & Gale (2000): Mạng hoàn thiện vs không hoàn thiện
- Eisenberg & Noe (2001): Thuật toán thanh toán bù trừ

**Định nghĩa:**

Mạng tài chính được biểu diễn bởi:
- **Nút (nodes)**: Các tổ chức tài chính (ngân hàng, quỹ, quốc gia)
- **Liên kết (edges)**: Quan hệ tài chính (cho vay, sở hữu chéo, tài sản chung)

**Ma trận liên kết:**

```
G = [gᵢⱼ]  với gᵢⱼ = giá trị phơi nhiễm từ i → j
```

**Hai loại rủi ro hệ thống (Jackson-Pernoud):**

| Loại | Cơ chế | Ví dụ |
|------|--------|-------|
| **Type I** - Contagion | Thay đổi giá trị cơ bản lan truyền qua mạng | Default cascade, fire sales |
| **Type II** - Feedback | Đa cân bằng, thay đổi kỳ vọng tự hoàn thành | Bank run, credit freeze |

### 2.3 Lớp Đống Cát (Sandpile Layer) — ĐIỂM ĐỘC ĐÁO

**Nguồn lý thuyết — CRITICAL:**
- Luna & Zanforlin (2025) IMF WP/25/041: **Áp dụng mô hình đống cát vào hệ thống tài chính**

> "Treats bank losses as analogous to grains accumulating on a sandpile until a slide occurs — when system-wide capital is insufficient to absorb a failing bank, welfare losses result."

**Mô hình Abelian (Sandpile):**

```
Grains accumulate until threshold → avalanche → redistribution
```

Áp dụng cho tài chính:

| Sandpile | Hệ thống Tài chính |
|----------|---------------------|
| Hạt (grain) | Tổn thất tích lũy (loss accumulation) |
| Ngưỡng (threshold) | Vốn tự kiểm soát (capital buffer) |
| Avalanche | Khủng hoảng hệ thống (systemic crisis) |
| Redistribution | Tổn thất lan truyền (contagion) |

**Định nghĩa hệ thống:**

Một hệ thống tài chính ở trạng thái **cận ngưỡng** khi:

```
Σ(losses) > Buffer × N × ρ
```

Trong đó:
- `Σ(losses)` = tổng tổn thất tích lũy
- `Buffer` = bộ đệm vốn trung bình
- `N` = số lượng tổ chức
- `ρ` = hệ số tương quan hệ thống

---

## 3. CƠ CHẾ TÍCH HỢP

### 3.1 Sơ đồ Truyền dẫn Tích hợp

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     INTEGRATED TRANSMISSION MECHANISM                    │
└─────────────────────────────────────────────────────────────────────────┘

    CÚ SỐC
       │
       ▼
┌──────────────────┐
│   WAVE LAYER     │  ← Xác định nguồn, cường độ, độ trễ
│  (Origin + τ)    │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  NETWORK LAYER   │  ← Xác định đường truyền, tương tác
│   (Paths + G)    │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  SANDPILE LAYER  │  ← Xác định ngưỡng, avalanche, tổn thất
│  (Threshold + ∆) │
└────────┬─────────┘
         │
         ▼
   TỔN THẤT
   HỆ THỐNG
```

### 3.2 Phương trình Tích hợp

**Mô hình cốt lõi IFWST:**

```
V(t) = V₀ + ∫₀ᵗ [S(u) - D(u)] du + A(t) + C(t) + ε(t)
```

Trong đó:

| Ký hiệu | Ý nghĩa | Nguồn |
|----------|----------|--------|
| `V(t)` | Giá trị hệ thống tại t | Network layer |
| `V₀` | Giá trị ban đầu | Baseline |
| `S(u)` | Dòng vào (shocks) | Wave layer |
| `D(u)` | Dòng ra (dissipation) | Damping |
| `A(t)` | Hiệu ứng avalanche | Sandpile layer |
| `C(t)` | Hiệu ứng contagion | Network layer |
| `ε(t)` | Nhiễu | Stochastic |

**Avalanche function:**

```
A(t) = Σᵢ ωᵢ · H(Σlosses - thresholdᵢ) · f(Σlosses)
```

Trong đó:
- `H()` = hàm Heaviside (0 nếu dưới ngưỡng, 1 nếu vượt ngưỡng)
- `ωᵢ` = cường độ avalanche thứ i
- `f()` = hàm phân phối tổn thất

### 3.3 Ma trận Truyền dẫn Mở rộng

Mở rộng từ Jackson-Pornoud để tích hợp sandpile:

```
┌────────────────────────────────────────────────────────────┐
│              EXTENDED TRANSMISSION MATRIX                   │
├────────────────────────────────────────────────────────────┤
│                                                             │
│  g̃ᵢⱼ = gᵢⱼ × β(Σlosses) × γ(distance) × δ(correlation) │
│                                                             │
│  Trong đó:                                                 │
│  - gᵢⱼ     : liên kết cơ bản (Eisenberg-Noe)            │
│  - β()     : hệ số khuếch đại sandpile                   │
│  - γ()     : hệ số suy hao theo khoảng cách              │
│  - δ()     : hệ số tương quan                             │
│                                                             │
└────────────────────────────────────────────────────────────┘
```

---

## 4. KHUNG DỰ BÁO

### 4.1 Early Warning Indicators (EWI) Mở rộng

**Từ BIS (Aldasoro-Borio-Drehmann 2018):**

| Chỉ báo | Định nghĩa | Ngưỡng |
|---------|-------------|--------|
| Credit-to-GDP gap | Chênh lệch tín dụng/GDP so với xu hướng | > 10% |
| Property price gap | Chênh lệch giá BĐS so với xu hướng | > 15% |
| Aggregate DSR | Tỷ lệ trả nợ tổng | > 40% |

**Bổ sung từ IFWST:**

| Chỉ báo | Định nghĩa | Ngưỡng |
|---------|-------------|--------|
| Sandpile load | Tổng tổn thất tích lũy / Buffer | > 0.8 |
| Network density | Mật độ liên kết mạng | Biến thiên |
| Cascade potential | Khả năng cascade (eigenvector) | > threshold |
| Wave coherence | Độ đồng pha sóng xuyên biên giới | > 0.5 |

### 4.2 Chỉ số Rủi ro Hệ thống Tích hợp

```
IFWST_Risk_Index = w₁·EWI_basic + w₂·Sandpile_Load + w₃·Network_Contagion + w₄·Wave_Coherence
```

Trong đó các trọng số `wᵢ` được ước lượng từ dữ liệu lịch sử.

### 4.3 Dự báo Thời điểm Khủng hoảng

**Mô hình thời gian:**

```
P(crisis | t+τ) = f(IFWST_Risk_Index, τ, regime)
```

- `τ` = horizon dự báo (1-12 quarters)
- `regime` = trạng thái (boom/bust, integrated/fragmented)

---

## 5. KIỂM ĐỊNH GIẢ THUYẾT

### 5.1 Giả thuyết từ Literature

**Từ RESEARCH_MANIFEST:**

| Giả thuyết | Dự đoán | Kiểm định |
|------------|---------|------------|
| H1 - Áp lực tích lũy | Biến tích lũy bổ sung thông tin | So sánh AUC EWI cơ bản vs mở rộng |
| H2 - Đa thang đo | Đặc trưng động cải thiện nhận dạng | Time-varying ROC |
| H3 - Tính dễ tổn thương | Cùng cú sốc → hậu quả khác nhau | Phân tích regime |
| H4 - Sóng thứ cấp | Tổn thất vượt tác động trực tiếp | Decomposition analysis |
| H5 - Giá trị cảnh báo | Mô hình tích hợp tốt hơn | Backtesting 2008 |

### 5.2 Trường hợp Nghiên cứu

**Khủng hoảng 2008:**

- Nguồn sóng: US subprime mortgage
- Đường truyền: Cross-border banking (Cetorelli-Goldberg)
- Ngưỡng sandpile: Tổn thất tích lũy > buffer
- Kết quả: Systemic avalanche

---

## 6. SO SÁNH VỚI CÁC MÔ HÌNH HIỆN CÓ

| Khía cạnh | EWI truyền thống | Network models | IFWST |
|-----------|------------------|----------------|-------|
| Temporal dynamics | Gap indicators | Static/moment | Wave propagation |
| Cross-border |很少 | Partial | Full integration |
| Non-linear | Limited | Limited | Avalanche mechanism |
| Threshold behavior | Ad-hoc | Sometimes | Theoretical (sandpile) |
| Crisis timing | Signal only | Propagation | Timing + magnitude |

---

## 7. KẾT LUẬN KIẾN TRÚC

**Điểm độc đáo của IFWST:**

1. **Tích hợp ba lớp** — Wave + Network + Sandpile
2. **Nền tảng lý thuyết vững chắc** — Luna & Zanforlin (2025) IMF validation
3. **Ngưỡng lý thuyết** — từ mô hình Abelian
4. **Dự báo thời gian** — không chỉ signal mà cả timing

**Hạn chế cần kiểm định:**

- Giả định về ngưỡng cố định
- Chưa có dữ liệu đa quốc gia đầy đủ
- Chưa kiểm tra cho các khủng hoảng khác

---

## 8. BƯỚC TIẾP THEO

- [ ] Xác minh phương trình cơ bản với dữ liệu
- [ ] Ước lượng tham số từ dữ liệu BIS
- [ ] Backtest với khủng hoảng 2008
- [ ] So sánh với EWI cơ sở

---

**Tài liệu tham khảo chính:**
- Jackson & Pernoud (2021) — Financial networks survey
- Luna & Zanforlin (2025) IMF WP/25/041 — Sandpile metaphor
- Aldasoro, Borio, Drehmann (2018) — EWI
- Cetorelli & Goldberg (2011) — Global banks
- Popov & Udell (2010) — Cross-border transmission
- Brunnermeier (2009) — Liquidity crunch
