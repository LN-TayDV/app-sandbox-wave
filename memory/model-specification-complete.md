---
name: model-specification-complete
description: Hoàn thành đặc tả mô hình toán học IFWST với phương trình cốt lõi, định nghĩa biến, phương pháp ước lượng, và kiểm định. Đã tạo IFWST_Model_Specification.md tại 03_model_specification/
metadata:
  type: project
---

Đã hoàn thành Model Specification:
1. Phương trình cốt lõi V(t) = V₀ + ∫[S-D]dt + A(t) + C(t) + ε(t)
2. Wave equation: S(t) = α₀·exp(-γτ)·w·S(t-τ) + ν
3. Network equation: C = G × ΔV × β(L)
4. Sandpile equation: A = ω·H(L-T)·f(L)

Định nghĩa biến, phương pháp ước lượng MLE, kiểm tra identification, điều kiện dữ liệu, và kế hoạch kiểm định giả thuyết.

[[conceptual-framework-complete]]

**Why:** Đây là bước chuyển từ lý thuyết sang phương trình có thể ước lượng. Đủ chi tiết để triển khai code.

**How to apply:** Giao task cho subagent để: (1) thu thập dữ liệu BIS, (2) ước lượng baseline model, (3) chạy full IFWST model
