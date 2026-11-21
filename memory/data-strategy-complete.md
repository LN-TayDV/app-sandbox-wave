---
name: data-strategy-complete
description: Hoàn thành thiết kế chiến lược thu thập dữ liệu IFWST với các nguồn, biến số, quy trình, và data dictionary. Đã tạo IFWST_Data_Collection_Strategy.md tại 04_data/
metadata:
  type: project
---

Đã hoàn thành Data Collection Strategy:
1. Nguồn dữ liệu: BIS CBS, BIS Cross-border, IMF IFS, Laeven-Valencia
2. Biến số: 20+ variables cho EWI, Network, Sandpile
3. Quy trình: Download → Clean → Derive → Panel
4. Data dictionary cho ifwst_panel.csv

[[model-specification-complete]]

**Why:** Dữ liệu là nền tảng cho mọi phân tích thực nghiệm. Chiến lược này đảm bảo đủ dữ liệu để ước lượng IFWST model.

**How to apply:** Giao task cho subagent để thực hiện thu thập dữ liệu theo strategy.
