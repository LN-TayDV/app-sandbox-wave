#!/usr/bin/env python3
"""math_render.py — phục hồi LaTeX từ span PDF của sách toán.

Vì sao cần
-----------
Text layer của PyMuPDF làm mất toàn bộ ngữ nghĩa toán học: chỉ số trên/dưới
tách rời, ký hiệu tổng lớn tách khỏi giới hạn, dấu bằng bị mất khi nằm ở
font riêng.  Kết quả là "xiei = 0." thay vì "\\sum_i x_i e_i = 0".

Cách khôi phục
--------------
Sách toán dùng font Computer Modern với quy ước ổn định:

  Cmmi10   biến toán học nghiêng (x, y, beta)
  Cmmib10  biến toán học đậm (vector, ma trận)
  Cmmi8    chỉ số trên/dưới (cỡ nhỏ hơn, lệch baseline)
  Cmex10   ký hiệu lớn: \sum \prod \int (bbox cao hơn nhiều)
  Cmbx10   nội dung trong khung (\boxed)
  Cmr10    chữ thẳng toán học (số, từ khóa)

Chỉ số trên/dưới suy ra từ vị trí baseline: origin_y lớn hơn => chỉ số dưới,
nhỏ hơn => chỉ số trên.  Giới hạn của \sum/\prod nằm ở các span cỡ nhỏ nằm
trên/dưới glyph lớn theo trục x.

Kết quả là chuỗi LaTeX có thể parse bằng SymPy, nhưng vẫn phải qua
render-diff trước khi gắn nhãn VERIFIED.
"""
from __future__ import annotations

import re

#: Font -> ký hiệu toán học cố định
BIG_OPS = {
    "∑": r"\sum", "∏": r"\prod", "∫": r"\int", "∬": r"\iint",
    "∭": r"\iiint", "∮": r"\oint", "∞": r"\infty",
    "⇒": r"\Rightarrow", "⇔": r"\Leftrightarrow",
    "≤": r"\leq", "≥": r"\geq", "≠": r"\neq", "≈": r"\approx",
    "≡": r"\equiv", "∼": r"\sim", "∝": r"\propto", "∈": r"\in",
    "∉": r"\notin", "⊂": r"\subset", "∪": r"\cup", "∩": r"\cap",
    "∀": r"\forall", "∃": r"\exists", "∂": r"\partial", "∇": r"\nabla",
    "√": r"\sqrt", "×": r"\times", "÷": r"\div",
    "±": r"\pm", "∓": r"\mp", "→": r"\to", "↔": r"\leftrightarrow",
    "…": r"\dots", "⋅": r"\cdot", "′": "'", "°": r"^{\circ}",
}

#: Cmex10 — Computer Modern "extension" font dùng cho ký hiệu lớn.
#:
#: PyMuPDF decode sai font này: nó trả ký tự theo WinAnsi của font TrueType con
#: (nên glyph \sum ở code 0x58 bị trả thành 'X'), dù PDF khai báo
#: /Identity-H cho font Type0.  Bảng dưới đây là mapping chuẩn của cmex10
#: (theo Adobe/TeX), lấy từ cmap của bản cmex10 gốc.
#:
#: Toàn bộ mã >= 0x239B là dấu ngoặc lớn (delimiters), trả về cùng một dạng
#: ngoặc thường vì không thể phân biệt kích thước khi dựng LaTeX từ text.
CMEX_MAP = {
    0x50: r"\sum", 0x51: r"\prod", 0x52: r"\int", 0x53: r"\cup",
    0x58: r"\sum", 0x59: r"\prod", 0x5A: r"\int", 0x5B: r"\cup",
    0x5C: r"\cap", 0x5D: r"\cup", 0x5E: r"\cap",
    0x62: "", 0x64: "", 0x65: "", 0x66: "", 0x67: "",
    0x6F: r"\}", 0x71: r"\sqrt", 0x72: r"\sqrt",
    0xAF: r"|", 0xB0: r"\|",
    0x2219: r"[",
    # ngoặc lớn -> ngoặc thường
    0x21: r")", 0x22: r"[", 0x23: r"]", 0x28: r"\{", 0x29: r"\}",
    0x68: r"[", 0x69: r"]", 0x6E: r"\{", 0x6F: r"\}",
    0x70: r"\sqrt", 0xA1: r"(", 0xA2: r")", 0xA3: r"[", 0xA4: r"]",
    0xA9: r"\{", 0xAA: r"\}",
    0xB3: r"(", 0xB4: r")", 0xB5: r"(", 0xB6: r")",
    0xB8: r"]", 0xBD: r"\{", 0xC3: r"(",
}

#: Ký tự Unicode -> LaTeX
CHAR_MAP = {
    "−": "-", "×": r"\times", "÷": r"\div", "±": r"\pm", "∓": r"\mp",
    "≤": r"\leq", "≥": r"\geq", "≠": r"\neq", "≈": r"\approx",
    "≡": r"\equiv", "∼": r"\sim", "∝": r"\propto", "∞": r"\infty",
    "∈": r"\in", "∉": r"\notin", "⊂": r"\subset", "∪": r"\cup",
    "∩": r"\cap", "∀": r"\forall", "∃": r"\exists", "∂": r"\partial",
    "∇": r"\nabla", "∑": r"\sum", "∏": r"\prod", "∫": r"\int",
    "√": r"\sqrt", "→": r"\to", "↔": r"\leftrightarrow", "⋯": r"\cdots",
    "…": r"\dots", "⋅": r"\cdot", "′": "'", "°": r"^{\circ}",
    "…": r"\ldots", "≠": r"\neq", "≥": r"\geq", "≤": r"\leq",
}

#: Ký tự LaTeX đặc biệt cần escape
_ESCAPE = {
    "%": r"\%", "&": r"\&", "#": r"\#", "_": r"\_", "$": r"\$",
    "{": r"\{", "}": r"\}",
}

#: Font toán học -> phong cách
ITALIC_FONTS = {"Cmmi10", "Cmmib10", "Cmmi8", "Cmmi7", "Cmmi6", "Cmmi5",
                "Cmmib10", "Cmmi10", "Cmmti10", "Cmti10"}
MATH_FONTS = ITALIC_FONTS | {"Cmr10", "Cmbx10", "Cmex10", "Cmsy10",
                             "Cmsy7", "Cmsy9", "Cmmib10", "Cmmi8"}

RE_EQ_NUMBER = re.compile(r"^\(\s*\d{1,2}\.\d{1,2}\s*\)$")
RE_EQ_NUMBER_INLINE = re.compile(r"^\(\s*\d{1,2}\.\d{1,2}\s*\)\.?$")


def _escape(text: str) -> str:
    out = []
    for ch in text:
        if ch in CHAR_MAP:
            out.append(CHAR_MAP[ch])
        elif ch in _ESCAPE:
            out.append(_ESCAPE[ch])
        else:
            out.append(ch)
    return "".join(out)


def _is_script(span: dict, base_size: float) -> bool:
    """Span nhỏ hơn đáng kể so với cỡ gốc -> là chỉ số trên/dưới."""
    return span["sz"] < base_size * 0.85


def _script_dir(span: dict, ref_y: float) -> str:
    """> 0 -> dưới (subscript), < 0 -> trên (superscript)."""
    return "_" if span["o"][1] > ref_y + 0.4 else "^"


def _cmex_latex(txt: str) -> str:
    """Cmex10 -> LaTeX, dùng CMEX_MAP (xem chú thích ở trên)."""
    out = []
    for ch in txt:
        tex = CMEX_MAP.get(ord(ch))
        if tex:
            out.append(tex)
        elif ch.strip():
            out.append(_escape(ch))
    return "".join(out)


def _span_latex(sp: dict, base_size: float, prev: dict | None) -> str:
    """Một span -> LaTeX fragment."""
    txt = sp["t"]
    font = sp.get("f", "")

    if font.startswith("Cmex"):
        return _cmex_latex(txt)

    if font == "Cmbx10":
        # khung: \boxed{...}
        return r"\boxed{" + _escape(txt.strip()) + "}"

    if font.startswith("Cmsy"):
        # symbol font: ≤ ≥ ≠ ∑ ...
        return _escape(txt)

    if _is_script(sp, base_size) and prev is not None:
        direction = _script_dir(sp, prev["o"][1])
        return direction + "{" + _escape(txt.strip()) + "}"

    if font in ITALIC_FONTS:
        # biến toán học: giữ nguyên ký tự, chỉ escape ký tự đặc biệt
        return _escape(txt)

    # chữ thường: escape
    return _escape(txt)


def _group_script_runs(spans: list[dict]) -> list[tuple[list[dict], str]]:
    """Gom span liên tiếp cùng loại (script / không) thành nhóm.

    Nhiều chỉ số liên tiếp (x_{ij}) phải gộp vào MỘT nhóm để LaTeX đúng.
    """
    if not spans:
        return []
    base_size = max(s["sz"] for s in spans)
    groups: list[tuple[list[dict], str]] = []
    cur: list[dict] = [spans[0]]
    cur_is_script = _is_script(spans[0], base_size)
    for sp in spans[1:]:
        s = _is_script(sp, base_size)
        if s == cur_is_script:
            cur.append(sp)
        else:
            groups.append((cur, "script" if cur_is_script else "base"))
            cur = [sp]
            cur_is_script = s
    groups.append((cur, "script" if cur_is_script else "base"))
    return groups


def _render_line_spans(spans: list[dict]) -> str:
    """LaTeX cho một dòng, gom chỉ số liên tiếp vào cùng nhóm."""
    base_size = max((s["sz"] for s in spans), default=0)
    out: list[str] = []
    prev: dict | None = None
    for grp, kind in _group_script_runs(spans):
        txt = "".join(s["t"] for s in grp).strip()
        if not txt:
            continue
        if kind == "script" and prev is not None:
            direction = _script_dir(grp[0], prev["o"][1])
            out.append(direction + "{" + _escape(txt) + "}")
        else:
            # trong nhóm base, các span toán học xen kẽ với chữ
            sub = []
            p = None
            for sp in grp:
                sub.append(_span_latex(sp, base_size, p))
                p = sp
            out.append("".join(sub))
        # cập nhật prev bằng span cuối không phải script
        last_base = [s for s in grp if not _is_script(s, base_size)]
        if last_base:
            prev = last_base[-1]
        else:
            prev = grp[-1]
    return "".join(out).strip()


def _merge_big_op_limits(lines: list[dict]) -> str:
    """Ghép các dòng PDF của một phương trình thành LaTeX, gắn giới hạn
    của ký hiệu lớn (\\sum, \\prod, \\int) từ span nằm trên/dưới.

    `lines`: list các dòng (mỗi dòng = dict có "spans", "bbox").
    """
    if not lines:
        return ""
    # tìm dòng chứa ký hiệu lớn
    big_idx = None
    for i, ln in enumerate(lines):
        for sp in ln.get("spans", []):
            if sp.get("f", "").startswith("Cmex"):
                big_idx = i
                break
        if big_idx is not None:
            break

    if big_idx is None:
        return " ".join(_render_line_spans(ln.get("spans", []))
                        for ln in lines).strip()

    big = lines[big_idx]
    bspan = next(sp for sp in big["spans"] if sp.get("f", "").startswith("Cmex"))
    bx0, bx1 = bspan["b"][0], bspan["b"][2]
    base_y = bspan["o"][1]

    upper: list[str] = []
    lower: list[str] = []
    for i, ln in enumerate(lines):
        if i == big_idx:
            continue
        for sp in ln.get("spans", []):
            # nằm trong cột của ký hiệu lớn
            if not (bx0 - 4 <= sp["b"][0] <= bx1 + 4):
                continue
            txt = sp["t"].strip()
            if not txt:
                continue
            if sp["o"][1] < base_y:
                upper.append(_escape(txt))
            else:
                lower.append(_escape(txt))

    op = _cmex_latex(bspan["t"]).strip()

    if upper:
        op = op + "^{" + "".join(upper) + "}"
    if lower:
        op = op + "_{" + "".join(lower) + "}"

    # thay span ký hiệu lớn trong dòng đó bằng op
    parts: list[str] = []
    prev: dict | None = None
    base_big = max(s["sz"] for s in big["spans"])
    for sp in big["spans"]:
        if sp.get("f", "").startswith("Cmex"):
            parts.append(op)
            prev = sp
            continue
        parts.append(_span_latex(sp, base_big, prev))
        if not _is_script(sp, base_big):
            prev = sp

    before = " ".join(_render_line_spans(ln.get("spans", []))
                      for ln in lines[:big_idx]).strip()
    after = " ".join(_render_line_spans(ln.get("spans", []))
                     for ln in lines[big_idx + 1:]).strip()
    mid = "".join(parts).strip()
    return " ".join(p for p in (before, mid, after) if p).strip()


def _line_center(ln: dict) -> float:
    b = ln["bbox"]
    return (b[1] + b[3]) / 2


#: Font chữ thường (văn xuôi) trong sách toán.  Số/math khác font này.
TEXT_FONTS = {"Dcr10", "Dcbx10", "Dcbx12", "Dcsl10", "Dcti10", "Dcr12",
              "Dcr17", "Dcrb10", "Dcrbx10", "Dcrbx12", "Dcti12", "Dcr8",
              "Dcr7", "Dcr6", "TimesNewRomanPSMT", "TimesNewRomanPS-BoldMT",
              "TimesNewRomanPS-ItalicMT", "ArialMT", "Arial-BoldMT"}

#: Font toán học (ký hiệu, biến, số).
MATH_FONTS = {"Cmmi10", "Cmmib10", "Cmmi8", "Cmmi7", "Cmr10", "Cmr8",
              "Cmsy10", "Cmsy8", "Cmsy7", "Cmex10", "Cmbx10", "Cmti10",
              "Cmmi12", "Cmmib12", "Cmbx12", "Cmmib8", "Cmmi9", "Cmmi6"}


def _math_ratio(ln: dict) -> float:
    """Tỉ lệ ký tự nằm trong font toán học của một dòng.

    Nhờ đây mà phân biệt được dòng công thức với dòng văn xuôi: text layer
    của sách toán KHÔNG giữ khoảng trắng giữa các từ ("Weoftenwrite..."),
    nên phải dựa vào font chứ không dựa vào khoảng trắng hay độ dài.
    """
    tot = 0
    math = 0
    for sp in ln.get("spans", []):
        t = sp.get("t", "")
        n = len(t.strip())
        if not n:
            continue
        tot += n
        f = sp.get("f", "")
        if f in MATH_FONTS or f.startswith("Cm"):
            math += n
    if not tot:
        return 0.0
    return math / tot


def _is_prose_line(ln: dict) -> bool:
    """Dòng văn xuôi (không phải mảnh công thức)."""
    if not ln["text"].strip():
        return False
    if _math_ratio(ln) >= 0.5:
        return False
    return True


def _row_key(y: float) -> int:
    """Gom span cùng hàng (baseline gần nhau) vào một nhóm."""
    return int(round(y / 4.0))


def _collect_rows(lines: list[dict], right_x: float, y0: float,
                  y1: float) -> list[dict]:
    """Các hàng span trong vùng (y0, y1) và bên trái right_x, bỏ văn xuôi."""
    rows: dict[int, list[dict]] = {}
    for ln in lines:
        if _is_prose_line(ln):
            continue
        cy = _line_center(ln)
        if not (y0 <= cy <= y1):
            continue
        for sp in ln.get("spans", []):
            if sp["b"][2] > right_x:
                continue
            k = _row_key(sp["o"][1])
            rows.setdefault(k, []).append(sp)
    out = []
    for k in sorted(rows):
        sps = sorted(rows[k], key=lambda s: s["b"][0])
        out.append({"y": sps[0]["o"][1], "spans": sps})
    return out


def _math_blocks(lines: list[dict], right_x: float) -> list[list[dict]]:
    """Chia trang thành các khối dòng toán liên tiếp.

    Hai dòng toán liên tiếp (không có dòng văn xuôi xen giữa) thuộc cùng
    một khối — đó là phương trình cùng với các giới hạn trên/dưới.  Ranh
    giới khối là nơi có văn xuôi xen vào, nên công thức liền kề không bị
    trộn vào nhau.
    """
    blocks: list[list[dict]] = []
    cur: list[dict] = []
    for ln in lines:
        is_math = not _is_prose_line(ln)
        if is_math:
            sps = [sp for sp in ln.get("spans", []) if sp["b"][2] <= right_x]
            if sps:
                cur.append(ln)
        else:
            if cur:
                blocks.append(cur)
                cur = []
    if cur:
        blocks.append(cur)
    return blocks


def _render_rows(rows: list[dict]) -> str:
    """Dựng LaTeX từ các hàng span, gắn giới hạn cho ký hiệu lớn.

    Chiến lược: với mỗi ký hiệu lớn (\\sum, \\prod, \\int), tìm các span nằm
    TRÊN và DƯỚI nó trong cùng cột x -> gắn thành ^{...} và _{...}, rồi loại
    chúng khỏi dòng chính.  Các hàng còn lại nối lại theo thứ tự đọc.
    """
    if not rows:
        return ""

    # --- 1. tìm ký hiệu lớn và gán giới hạn ---
    consumed: set[int] = set()          # id span đã dùng làm giới hạn
    op_repl: dict[int, str] = {}        # id span ký hiệu lớn -> LaTeX thay thế
    span_id: dict[int, int] = {}
    _next = [0]

    def sid(sp: dict) -> int:
        if id(sp) not in span_id:
            span_id[id(sp)] = _next[0]
            _next[0] += 1
        return span_id[id(sp)]

    for ri, row in enumerate(rows):
        for sp in row["spans"]:
            if not sp.get("f", "").startswith("Cmex"):
                continue
            op = _cmex_latex(sp["t"]).strip()
            if not op:
                continue
            bx0, bx1 = sp["b"][0], sp["b"][2]
            by = sp["o"][1]
            # ký hiệu lớn có bbox rất cao: dùng TÂM theo trục x, và mốc
            # dọc là ĐÁY bbox (glyph \sum kéo dài xuống dưới baseline)
            cx = (bx0 + bx1) / 2
            up: list[str] = []
            lo: list[str] = []
            for rj, r2 in enumerate(rows):
                if rj == ri:
                    continue
                for s2 in r2["spans"]:
                    sx = (s2["b"][0] + s2["b"][2]) / 2
                    if not (cx - 8 <= sx <= cx + 8):
                        continue
                    dy = s2["o"][1] - by
                    if -24 <= dy < -0.5:
                        up.append(_escape(s2["t"].strip()))
                        consumed.add(sid(s2))
                    elif 0.5 < dy <= 24:
                        lo.append(_escape(s2["t"].strip()))
                        consumed.add(sid(s2))
            frag = op
            if up:
                frag += "^{" + "".join(up) + "}"
            if lo:
                frag += "_{" + "".join(lo) + "}"
            op_repl[sid(sp)] = frag

    # --- 2. dựng từng hàng, bỏ span đã là giới hạn ---
    parts: list[str] = []
    for row in rows:
        sps = [s for s in row["spans"] if sid(s) not in consumed]
        if not sps:
            continue
        base_size = max(s["sz"] for s in sps)
        # tách script / base
        segs = _group_script_runs(sps)
        seg_txt: list[str] = []
        prev: dict | None = None
        for grp, kind in segs:
            if kind == "script" and prev is not None:
                d = _script_dir(grp[0], prev["o"][1])
                seg_txt.append(d + "{" + _escape("".join(s["t"]
                                                           for s in grp).strip()) + "}")
            else:
                sub = []
                p = None
                for s in grp:
                    if sid(s) in op_repl:
                        sub.append(op_repl[sid(s)])
                    else:
                        sub.append(_span_latex(s, base_size, p))
                    if not _is_script(s, base_size):
                        p = s
                seg_txt.append("".join(sub))
            lb = [s for s in grp if not _is_script(s, base_size)]
            prev = lb[-1] if lb else grp[-1]
        line = "".join(seg_txt).strip()
        if line:
            parts.append(line)
    return " ".join(parts).strip()


def extract_equations_from_page(lines: list[dict], page_width: float) -> list[dict]:
    """Tìm các phương trình đánh số trên trang và trả về LaTeX.

    Quy ước sách toán: số phương trình nằm ở mép phải, cách xa, trên một
    dòng riêng.  Nội dung phương trình nằm ở các dòng bên trái, cùng vùng
    chiều cao.

    `lines`: các dòng đã lọc bỏ header/footer, mỗi dòng có "spans" và "bbox".
    """
    out: list[dict] = []
    right_x = page_width * 0.72
    blocks = _math_blocks(lines, right_x)

    for ln in lines:
        txt = ln["text"].strip()
        if not RE_EQ_NUMBER.match(txt):
            continue
        if ln["bbox"][0] < right_x:
            continue
        num = txt.strip("()").strip()
        y = _line_center(ln)

        # khối toán gần dòng số nhất (dòng số nằm ngoài khối: nó là chữ thường)
        best = None
        best_d = 1e9
        for blk in blocks:
            ys = [_line_center(b) for b in blk]
            d = min(abs(v - y) for v in ys)
            if d < best_d:
                best_d = d
                best = blk
        if best is None or best_d > 40:
            continue
        block = best

        rows: dict[int, list[dict]] = {}
        for bl in block:
            # chỉ giữ dòng trong lân cận trên/dưới dòng số: một khối toán
            # có thể chứa nhiều công thức liền nhau
            if abs(_line_center(bl) - y) > 30:
                continue
            for sp in bl.get("spans", []):
                if sp["b"][2] > right_x:
                    continue
                rows.setdefault(_row_key(sp["o"][1]), []).append(sp)
        ordered = []
        for k in sorted(rows):
            sps = sorted(rows[k], key=lambda s: s["b"][0])
            ordered.append({"y": sps[0]["o"][1], "spans": sps})
        if not ordered:
            continue
        latex = _render_rows(ordered)
        if not latex or len(latex) < 3:
            continue
        out.append({
            "number": num,
            "latex": latex,
            "bbox": [round(v, 1) for v in ln["bbox"]],
            "y": y,
            "n_rows": len(ordered),
        })
    return out
