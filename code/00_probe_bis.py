#!/usr/bin/env python
"""
B2 — Tải dữ liệu BIS (bổ sung LBS per-country) + Laeven–Valencia crisis database.

Nguồn:
  BIS  : SDMX v2  https://stats.bis.org/api/v2/data/dataflow/BIS/{FLOW}/1.0/{KEY}
  LV   : Laeven & Valencia (2020), "Systemic Banking Crises Database"
         https://static-content.springer.com/esm/art%3A10.1057%2Fs41308-020-00107-3/
           MediaObjects/41308_2020_107_MOESM1_ESM.xlsx

Ghi vào `data/raw/`. Chạy:  python code/00_probe_bis.py
"""

from __future__ import annotations

import csv
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

# Console Windows mặc định cp1252 — ép UTF-8 để in được tiếng Việt
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")

BIS = "https://stats.bis.org/api/v2/data/dataflow/BIS"
LV_XLSX = ("https://static-content.springer.com/esm/art%3A10.1057%2Fs41308-020-00107-3/"
           "MediaObjects/41308_2020_107_MOESM1_ESM.xlsx")

# 21 nước của panel cuối cùng (ISO-2 như BIS dùng)
PANEL21 = ["BR", "CA", "CH", "CN", "CZ", "DE", "FR", "GB", "HU", "ID", "IN",
           "IT", "JP", "KR", "MX", "NL", "PL", "RU", "SE", "TR", "US"]

# (dataflow, key, tên file, mô tả)
BIS_TARGETS = [
    ("WS_CREDIT_GAP", "Q..P.A.C", "bis_credit_gap.csv",
     "Credit-to-GDP gaps (actual-trend), 44 ctys, quarterly"),
    ("WS_CREDIT_GAP", "Q..P.A.A", "bis_credit_gdp_ratio.csv",
     "Credit-to-GDP ratios (actual), 44 ctys, quarterly"),
    ("WS_CREDIT_GAP", "Q.US.P.A.C", "bis_credit_gap_us.csv",
     "Credit-to-GDP gap, United States, quarterly"),
    ("WS_DSR", "Q...A", "bis_dsr.csv",
     "Debt service ratios, all borrowers, 32 ctys, quarterly"),
    ("WS_LBS_D_PUB", "Q.S.C.A.TO1.F.5J.A.5A.A.5J.A", "bis_lbs_cross_border_all.csv",
     "LBS cross-border claims, all reporting ctys, quarterly"),
]

# LBS per-country cho 21 nước panel (key đã xác minh cho 16/21)
LBS_SKIP = {"CZ", "HU", "PL", "TH", "NZ"}  # BIS không có series cho các nước này


def fetch(url: str, tries: int = 3, timeout: int = 180) -> tuple[int, bytes, str]:
    """GET có retry + backoff. Trả về (http_code, body, content_type)."""
    last: tuple[int, bytes, str] = (0, b"", "")
    for attempt in range(1, tries + 1):
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.status, resp.read(), resp.headers.get("Content-Type", "")
        except urllib.error.HTTPError as exc:
            last = (exc.code, exc.read(), exc.headers.get("Content-Type", ""))
            print(f"    attempt {attempt}: HTTP {exc.code}")
        except Exception as exc:  # noqa: BLE001 - ghi lại rồi thử lại
            print(f"    attempt {attempt}: {type(exc).__name__}: {exc}")
        if attempt < tries:
            time.sleep(2 ** attempt)
    return last


def parse_sdmx(xml: bytes) -> tuple[list[str], list[dict]]:
    """SDMX-ML: Series/Group chứa Obs lồng nhau. Trả (dim_names, obs_rows)."""
    text = xml.decode("utf-8", errors="ignore")
    dim_names: list[str] = []
    rows: list[dict] = []
    blocks = re.findall(r"<(?:Series|Group) ([^>]*)>(.*?)</(?:Series|Group)>", text, re.S)
    for attrs, body in blocks:
        s = dict(re.findall(r'(\w+)="([^"]*)"', attrs))
        for k in s:
            if k not in dim_names:
                dim_names.append(k)
        for o_attrs in re.findall(r"<Obs ([^>]*?)/?>", body):
            o = dict(re.findall(r'(\w+)="([^"]*)"', o_attrs))
            row = {k: s.get(k, "") for k in dim_names}
            row.update({"TIME_PERIOD": o.get("TIME_PERIOD", ""),
                        "OBS_VALUE": o.get("OBS_VALUE", ""),
                        "OBS_STATUS": o.get("OBS_STATUS", ""),
                        "OBS_CONF": o.get("OBS_CONF", "")})
            rows.append(row)
    return dim_names, rows


def write_csv(path: Path, dim_names: list[str], rows: list[dict]) -> None:
    cols = dim_names + ["TIME_PERIOD", "OBS_VALUE", "OBS_STATUS", "OBS_CONF"]
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def probe_bis() -> None:
    for dataflow, key, fname, desc in BIS_TARGETS:
        url = f"{BIS}/{dataflow}/1.0/{key}"
        print(f"[{fname}] {dataflow} :: {key}")
        status, body, _ = fetch(url)
        if status != 200:
            print(f"    -> FAIL HTTP {status}")
            continue
        dims, rows = parse_sdmx(body)
        if not rows:
            print("    -> OK HTTP 200 nhưng KHÔNG có obs (key sai)")
            continue
        write_csv(RAW / fname, dims, rows)
        cty_col = "BORROWERS_CTY" if "BORROWERS_CTY" in dims else (
            "L_REP_CTY" if "L_REP_CTY" in dims else None)
        countries = sorted({r[cty_col] for r in rows}) if cty_col else []
        periods = sorted(r["TIME_PERIOD"] for r in rows if r["TIME_PERIOD"])
        print(f"    -> OK {len(rows)} obs | {len(countries)} ctys | "
              f"{periods[0]}..{periods[-1]} | {fname}  ({desc})")


def probe_lbs_per_country() -> None:
    """Tải LBS cross-border claims cho từng nước trong panel 21."""
    print("\n=== LBS per-country (21 nước panel) ===")
    ok, miss = [], []
    for cty in PANEL21:
        if cty in LBS_SKIP:
            print(f"[{cty}] SKIP - BIS không có series")
            miss.append(cty)
            continue
        key = f"Q.S.C.A.TO1.F.5J.A.{cty}.A.5J.A"
        url = f"{BIS}/WS_LBS_D_PUB/1.0/{key}"
        status, body, _ = fetch(url, tries=2, timeout=90)
        if status != 200:
            print(f"[{cty}] -> HTTP {status}")
            miss.append(cty)
            continue
        dims, rows = parse_sdmx(body)
        if not rows:
            print(f"[{cty}] -> không có obs")
            miss.append(cty)
            continue
        fname = f"bis_lbs_xborder_{cty.lower()}.csv"
        write_csv(RAW / fname, dims, rows)
        periods = sorted(r["TIME_PERIOD"] for r in rows if r["TIME_PERIOD"])
        print(f"[{cty}] -> OK {len(rows)} obs | {periods[0]}..{periods[-1]} | {fname}")
        ok.append(cty)
    print(f"\n  Có dữ liệu: {len(ok)}/21 -> {','.join(ok)}")
    print(f"  Thiếu      : {len(miss)}/21 -> {','.join(miss) if miss else '(không)'}")


def probe_laeven_valencia() -> None:
    """Tải file Excel Laeven–Valencia (không qua WAF IMF)."""
    out = RAW / "laeven_valencia_crises.xlsx"
    print(f"\n=== Laeven–Valencia ===\nGET {LV_XLSX}")
    status, body, _ = fetch(LV_XLSX, tries=3, timeout=180)
    if status != 200:
        print(f"    -> FAIL HTTP {status}")
        return
    if not body.startswith(b"PK"):
        print("    -> KHÔNG phải xlsx (bị chặn/HTML)")
        return
    out.write_bytes(body)
    print(f"    -> OK {len(body):,} bytes | {out.name}")


def main() -> int:
    RAW.mkdir(parents=True, exist_ok=True)
    print("=== BIS (SDMX v2) ===")
    probe_bis()
    probe_lbs_per_country()
    probe_laeven_valencia()
    print(f"\n=== data/raw ({len(list(RAW.glob('*.csv')))} csv) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
