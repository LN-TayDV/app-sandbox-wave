# ĐẶC TẢ MÔ HÌNH TOÁN HỌC — IFWST

## 1. PHƯƠNG TRÌNH CỐT LÕI

### 1.1 Mô hình Giá trị Hệ thống

```
V(t) = V₀ + ∫₀ᵗ [S(u) - D(u)] du + A(t) + C(t) + ε(t)
```

**Ý nghĩa các thành phần:**

| Thành phần | Định nghĩa | Đơn vị | Nguồn |
|-------------|-------------|---------|--------|
| `V(t)` | Giá trị hệ thống tài chính tại t | % GDP | Model output |
| `V₀` | Giá trị ban đầu (baseline) | % GDP | Calibration |
| `S(u)` | Dòng vào (shocks) | % GDP/quarter | Wave layer |
| `D(u)` | Dòng ra (dissipation/absorption) | % GDP/quarter | Damping |
| `A(t)` | Hiệu ứng avalanche | % GDP | Sandpile layer |
| `C(t)` | Hiệu ứng contagion | % GDP | Network layer |
| `ε(t)` | Nhiễu ngẫu nhiên | % GDP | Stochastic |

### 1.2 Phương trình Sóng (Wave Equation)

```
Sᵢ(t) = α₀ · exp(-γτ) · ∑ⱼ wⱼ · Sⱼ(t - τᵢⱼ) + νᵢ(t)
```

**Tham số:**

| Tham số | Ý nghĩa | Phạm vi ước lượng | Đơn vị |
|---------|---------|-------------------|---------|
| `α₀` | Hệ số truyền dẫn gốc | [0.1, 2.0] | - |
| `γ` | Hệ số suy hao theo thời gian | [0.1, 0.5] | 1/quarter |
| `wⱼ` | Trọng số nguồn j | [0, 1], Σwⱼ=1 | - |
| `τᵢⱼ` | Độ trễ từ nguồn j đến i | [1, 12] | quarters |
| `νᵢ(t)` | Nhiễu | N(0, σ²) | - |

### 1.3 Phương trình Mạng (Network Equation)

```
Cᵢ(t) = ∑ⱼ g̃ᵢⱼ · ΔVⱼ(t-1) · I(ΔVⱼ < 0)
```

**Liên kết mở rộng:**

```
g̃ᵢⱼ = gᵢⱼ × β(L) × γ(dᵢⱼ) × δ(ρᵢⱼ)
```

| Tham số | Ý nghĩa | Phạm vi |
|---------|---------|---------|
| `gᵢⱼ` | Liên kết cơ bản (Eisenberg-Noe) | [0, 1] |
| `β(L)` | Hệ số khuếch đại sandpile | [1, ∞) |
| `γ(dᵢⱼ)` | Hệ số suy hao theo khoảng cách | (0, 1] |
| `δ(ρᵢⱼ)` | Hệ số tương quan | [0, 1] |

### 1.4 Phương trình Đống Cát (Sandpile Equation)

```
A(t) = Σₖ ωₖ · H(L(t) - Tₖ) · f(L(t))
```

**Hàm Avalanche:**

```
f(L) = { L - Tₖ    nếu L > Tₖ
        { 0         nếu L ≤ Tₖ
```

**Hàm Heaviside:**

```
H(x) = { 1  nếu x ≥ 0
       { 0  nếu x < 0
```

| Tham số | Ý nghĩa | Phạm vi |
|---------|---------|---------|
| `L(t)` | Tải trọng tích lũy (load) | [0, ∞) |
| `Tₖ` | Ngưỡng thứ k | [0.5, 1.5] × Buffer |
| `ωₖ` | Cường độ avalanche | [0, 1] |

---

## 2. ĐỊNH NGHĨA BIẾN SỐ

### 2.1 Biến Phụ thuộc (Dependent Variables)

| Biến | Định nghĩa | Nguồn dữ liệu |
|------|-------------|----------------|
| `ΔV_i` | Thay đổi giá trị ngân hàng i | Bankscope |
| `Crisis_i,t` | Dummy = 1 nếu khủng hoảng tại i,t | Borio-Drehmann |
| `Default_i,t` | Dummy = 1 nếu default | Bankscope |

### 2.2 Biến Độc lập (Independent Variables)

| Biến | Định nghĩa | Nguồn |
|------|-------------|-------|
| `CreditGap_i,t` | Credit-to-GDP gap | BIS |
| `PropertyGap_i,t` | Property price gap | BIS |
| `DSR_i,t` | Debt service ratio | BIS |
| `ForeignExposure_i,t` | Phơi nhiễm nước ngoài | BIS/IMF |
| `InterbankLink_i,t` | Liên kết liên ngân hàng | Bankscope |
| `SandpileLoad_i,t` | Tổn thất tích lũy / Buffer | Computed |

### 2.3 Biến Điều khiển (Control Variables)

| Biến | Ý nghĩa |
|------|---------|
| `GDP_growth_i,t` | Tăng trưởng GDP |
| `Inflation_i,t` | Lạm phát |
| `PolicyRate_i,t` | Lãi suất chính sách |
| `Regime_i,t` | Dummy boom/bust |

---

## 3. ƯỚC LƯỢNG THAM SỐ

### 3.1 Phương pháp Ước lượng

**Phương pháp chính: Maximum Likelihood Estimation (MLE)**

```
θ̂ = arg max θ L(θ; Y, X)
```

**Hàm log-likelihood:**

```
log L = Σᵢ log f(yᵢ | xᵢ, θ)
```

### 3.2 Ước lượng từng lớp

**Lớp 1 — Wave:**

```
Sᵢ(t) = α₀ · exp(-γτ) · w · S_source(t-τ) + ν

→ Ước lượng: OLS / GMM với instruments
```

**Lớp 2 — Network:**

```
C = G × ΔV × β(L)

→ Ước lượng: Network regression (spatial Durbin)
```

**Lớp 3 — Sandpile:**

```
A = ω · H(L - T) · (L - T)

→ Ước lượng: Threshold regression ( Hansen 2000 )
```

### 3.3 Ước lượng Tích hợp

```
IFWST_Model:
  V(t) = f(Wave_params, Network_params, Sandpile_params) + ε
  
  → Phương pháp: Seemingly Unrelated Regression (SUR)
  → Hoặc: Bayesian MCMC cho uncertainty quantification
```

---

## 4. KIỂM TRA KHẢ NĂNG NHẬN DẠNG (IDENTIFICATION)

### 4.1 Kiểm tra xác định (Rank Condition)

Ma trận thông tin Fisher:

```
I(θ) = -E[∂²log L / ∂θ∂θ']
```

Điều kiện: `rank(I(θ)) = k` (đầy đủ)

### 4.2 Kiểm tra Overidentifying Restrictions

```
Sargan statistic: J = n × R²_2SLS ~ χ²(k - m)
```

### 4.3 Instruments cho identification

| Biến nội sinh | Instrument | Lý do |
|---------------|------------|--------|
| `C(t)` (contagion) | Lagged G, shocks abroad | External variation |
| `A(t)` (avalanche) | Pre-crisis buffers | Exogenous to current shock |
| `S(t)` (shock) | US mortgage losses | Source of 2008 crisis |

### 4.4 Sensitivity Analysis

- Thay đổi specification
- Thay đổi instruments
- Subsample stability
- Bayesian sensitivity

---

## 5. ĐIỀU KIỆN ƯỚC LƯỢNG

### 5.1 Dữ liệu Tối thiểu

| Yêu cầu | Chi tiết |
|----------|----------|
| Time span | Tối thiểu 20 năm (1990-2020) |
| Countries | Tối thiểu 20 quốc gia |
| Frequency | Quarterly |
| Missing data | < 20% per variable |

### 5.2 Nguồn Dữ liệu Chính

| Nguồn | Biến | Khoảng thời gian |
|--------|-------|------------------|
| BIS CBS | Credit gaps, property gaps, DSR | 1990Q1-2023Q4 |
| BIS Cross-border | Liên kết xuyên biên giới | 2000Q1-2023Q4 |
| IMF IFS | GDP, inflation, rates | 1990Q1-2023Q4 |
| Bankscope | Bank-level data | 1990-2023 |
| Laeven-Valencia | Crisis dates | 1970-2023 |

### 5.3 Phần mềm Ước lượng

- **R**: {sandpile, igraph, network, spdep}
- **Python**: {networkx, numpy, scipy, pymc}
- **Stata**: s пространственный

---

## 6. KIỂM ĐỊNH GIẢ THUYẾT

### 6.1 Kiểm định từng phần

| Giả thuyết | Thống kê | Critical value (5%) |
|------------|----------|-------------------|
| H1: α > 0 | t-stat | ±1.96 |
| H2: γ > 0 | t-stat | ±1.96 |
| H3: β(L) > 1 | LR test | χ²(1) |
| H4: ω > 0 | Wald | χ²(1) |

### 6.2 So sánh Mô hình

| Tiêu chí | Công thức |
|-----------|-----------|
| AIC | -2 log L + 2k |
| BIC | -2 log L + k log n |
| RMSE | √(1/n Σ(y-ŷ)²) |
| MAE | (1/n) Σ|y-ŷ| |
| AUC-ROC | Area under ROC curve |

### 6.3 Backtesting

```
Train: 1990Q1 - 2007Q2
Test:   2007Q3 - 2009Q4

Metrics:
- Signal accuracy
- Timing accuracy
- Magnitude accuracy
```

---

## 7. ƯỚC LƯỢNG MÔ HÌNH CƠ SỞ (BASELINE)

### 7.1 Mô hình EWI Cơ bản

```
Logit(Crisis_i,t) = β₀ + β₁·CreditGap_i,t 
                          + β₂·PropertyGap_i,t 
                          + β₃·DSR_i,t 
                          + Controls
```

### 7.2 Mô hình Network

```
Logit(Crisis_i,t) = β₀ + β₁·CreditGap 
                          + β₂·InterbankLink 
                          + β₃·CrossBorder 
                          + Controls
```

### 7.3 Mô hình IFWST (Đầy đủ)

```
Logit(Crisis_i,t) = β₀ + β₁·CreditGap 
                          + β₂·PropertyGap 
                          + β₃·DSR 
                          + β₄·SandpileLoad 
                          + β₅·NetworkContagion 
                          + β₆·WaveCoherence 
                          + Controls
```

---

## 8. KẾT QUẢ KỲ VỌNG

### 8.1 Dấu hiệu Tham số

| Tham số | Kỳ vọng | Lý do |
|---------|----------|--------|
| α₀ | > 0 | Shock truyền dẫn |
| γ | > 0 | Suy hao theo thời gian |
| β(L) | > 1 | Khuếch đại gần ngưỡng |
| ω | > 0 | Avalanche tồn tại |
| T | > 0 | Ngưỡng hữu hạn |

### 8.2 Kiểm định Giả thuyết

- **H1 (Áp lực tích lũy)**: β₄ > 0, significant
- **H2 (Đa thang đo)**: Time-varying params improve fit
- **H3 (Tính dễ tổn thương)**: Regime interaction significant
- **H4 (Sóng thứ cấp)**: β₅ > β₄
- **H5 (Giá trị cảnh báo)**: IFWST AUC > EWI baseline

---

## 9. BƯỚC TIẾP THEO

- [ ] Ước lượng baseline model (EWI only)
- [ ] Ước lượng full IFWST model
- [ ] So sánh performance
- [ ] Sensitivity analysis
- [ ] Backtest 2008 crisis

---

**Tài liệu tham khảo:**
- Hansen, B.E. (2000). Threshold effects in non-dynamic panels. Econometrica
- Jackson, M.O. & Pernoud, A. (2021). Systemic Risk in Financial Networks. Annual Review of Economics
- Luna, F. & Zanforlin, L. (2025). Sandcastles and Financial Systems. IMF WP 2025/041
