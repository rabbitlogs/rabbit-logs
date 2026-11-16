# -*- coding: utf-8 -*-
"""
SAP MM 자격증 C_TS452 Q&A 도식 (brand_v3)

한글판(기본 파일명)과 영문판(_en)을 같은 레이아웃 코드로 만든다.

사용법 (저장소 루트에서):
  python3 scripts/diagrams/sap_mm_c_ts452_faq.py              # 전부, public/images에
  python3 scripts/diagrams/sap_mm_c_ts452_faq.py ko           # 한글판만
  python3 scripts/diagrams/sap_mm_c_ts452_faq.py en <출력폴더>  # 영문판만, 지정 폴더에
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import brand_v3 as B
from PIL import Image, ImageDraw

SLUG = "sap-mm-c-ts452-faq"


class _Canvas(B.Canvas):
    def __init__(self, w, h, bg=B.BG):
        self._w = w
        self.h = h
        self.img = Image.new("RGB", (w * B.SCALE, h * B.SCALE), bg)
        self.d = ImageDraw.Draw(self.img)

    def save(self, path, quality=90):
        self.img.save(path, "JPEG", quality=quality, optimize=True)
        kb = os.path.getsize(path) / 1024
        print(f"캔버스: {self._w*B.SCALE}x{self.h*B.SCALE}px  {os.path.basename(path)}  {kb:.0f}KB")


def _banner_height(c, title, sub):
    y = 26 + 18 + c.text_h(title, B.F("ExtraBold", 27)) + 12
    if sub:
        y += c.text_h(sub, B.F("Medium", 17)) + 10
    return y + 14


def _wrap(c, text, font, width):
    """공백 기준 줄바꿈. 한글도 어절 단위로 끊는다."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if c.text_w(t, font) <= width:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def _down_arrow(c, x, y0, y1, col=B.NEUT_S[3]):
    head = 10
    c.line([x, y0, x, y1 - head * 0.7], fill=col, width=2)
    c.polygon([x, y1, x - head * 0.45, y1 - head, x + head * 0.45, y1 - head], fill=col)


# ---------------------------------------------------------------- 01: 준비 순서
T_01 = {
    "ko": {
        "title": "C_TS452 준비 순서",
        "sub": "기본 흐름을 먼저 손에 익히고, 어려운 세 영역에 시간을 모은다",
        "step_label": "1단계 · 기본 흐름",
        "steps": [("S4500", "구매"), ("S4510", "재고관리"), ("S4515", "송장검증")],
        "focus_label": "2단계 · 가장 많은 시간",
        "focus": [("기본 설정", "S4550 · 조직 단위 만들고 연결"),
                  ("외주가공", "부품 제공 → 입고 → 부품 소비"),
                  ("MRP", "MRP 유형·로트 크기·소스 지정")],
    },
    "en": {
        "title": "C_TS452 study order",
        "sub": "Get the basic flow into your hands, then spend time on three hard areas",
        "step_label": "Step 1 · Basic flow",
        "steps": [("S4500", "Purchasing"), ("S4510", "Inventory"), ("S4515", "Invoices")],
        "focus_label": "Step 2 · Most of your time",
        "focus": [("Basic settings", "S4550 · create and link org units"),
                  ("Subcontracting", "Provide parts → receive → consume"),
                  ("MRP", "MRP type, lot size, source")],
    },
}


def build_01(lang, out):
    t = T_01[lang]
    W = 800
    gap = 46                       # 카드 사이 최소 44px 규칙
    n = len(t["steps"])
    cw = (W - 2 * B.PAD - gap * (n - 1)) / n
    f_lab = B.F("Bold", 17)
    f_code = B.F("ExtraBold", 24)
    f_name = B.F("SemiBold", 19)
    f_ft = B.F("Bold", 19)
    f_fd = B.F("Regular", 16)
    probe = _Canvas(W, 10)

    step_h = 92
    fcw = (W - 2 * B.PAD - 28 - 2 * 16) / 3     # 강조 밴드 안 3칸
    f_lines = [_wrap(probe, d, f_fd, fcw - 28) for _, d in t["focus"]]
    fbox_h = 20 + 26 + max(len(l) for l in f_lines) * 22 + 18
    top = _banner_height(probe, t["title"], t["sub"])
    H = int(top + 28 + step_h + 54 + 28 + fbox_h + 32 + 26)
    c = _Canvas(W, H)
    y = B.banner_B(c, t["title"], t["sub"])

    # 1단계: 순서가 있는 세 과정 (번호 + 화살표)
    c.text((B.PAD, y), t["step_label"], f_lab, fill=B.TEAL_S[1])
    y += 28
    for i, (code, name) in enumerate(t["steps"]):
        x = B.PAD + i * (cw + gap)
        c.rect([x, y, x + cw, y + step_h], fill="#ffffff", outline=B.TEAL_S[4], width=1.5, radius=14)
        c.center_text(x + cw / 2, y + 34, code, f_code, fill=B.TEAL_S[1])
        c.center_text(x + cw / 2, y + 66, name, f_name, fill=B.NEUT_S[1])
        if i < n - 1:
            B.flow_arrow(c, x + cw, x + cw + gap, y + step_h / 2)
    y += step_h

    # 아래로 이어지는 화살표
    _down_arrow(c, W / 2, y + 12, y + 42)
    y += 54

    # 2단계: 순서 없는 세 영역 (번호·화살표 없음, 강조 밴드)
    c.text((B.PAD, y), t["focus_label"], f_lab, fill=B.GOLD_S[0])
    y += 28
    band_h = fbox_h + 32
    c.rect([B.PAD, y, W - B.PAD, y + band_h], fill=B.GOLD_S[5], radius=16)
    for i, ((title, _), lines) in enumerate(zip(t["focus"], f_lines)):
        x = B.PAD + 14 + i * (fcw + 16)
        by = y + 16
        c.rect([x, by, x + fcw, by + fbox_h], fill="#ffffff", radius=12)
        c.text((x + 14, by + 18), title, f_ft, fill=B.GOLD_S[0])
        for j, ln in enumerate(lines):
            c.text((x + 14, by + 48 + j * 22), ln, f_fd, fill=B.NEUT_S[1])
    c.save(out)


# ---------------------------------------------------------------- 02: 실수가 번지는 구조
T_02 = {
    "ko": {
        "title": "이어지는 과제에서 실수가 번지는 구조",
        "sub": "앞 단계의 결과를 뒤 단계가 그대로 쓴다",
        "steps": [
            ("구매오더", "수량 100을 1000으로 입력", "오타 1개"),
            ("입고", "구매오더 수량을 참조해 입고", "함께 오답"),
            ("송장", "입고 수량과 대조해 송장 처리", "함께 오답"),
        ],
        "foot": "실수는 하나, 틀린 과제는 셋",
    },
    "en": {
        "title": "How one mistake spreads across linked tasks",
        "sub": "Each step uses the output of the step before it",
        "steps": [
            ("Purchase order", "Quantity 100 entered as 1000", "One typo"),
            ("Goods receipt", "Received against the PO quantity", "Also wrong"),
            ("Invoice", "Matched against the receipt quantity", "Also wrong"),
        ],
        "foot": "One mistake, three wrong tasks",
    },
}


def build_02(lang, out):
    t = T_02[lang]
    W = 800
    gap = 46
    n = len(t["steps"])
    cw = (W - 2 * B.PAD - gap * (n - 1)) / n
    f_name = B.F("Bold", 20)
    f_desc = B.F("Regular", 16)
    f_tag = B.F("Bold", 16)
    f_foot = B.F("Bold", 19)
    probe = _Canvas(W, 10)
    descs = [_wrap(probe, d, f_desc, cw - 32) for _, d, _ in t["steps"]]
    card_h = 20 + 28 + max(len(d) for d in descs) * 22 + 16 + 30 + 18
    top = _banner_height(probe, t["title"], t["sub"])
    H = int(top + card_h + 24 + 46 + 28)
    c = _Canvas(W, H)
    y = B.banner_B(c, t["title"], t["sub"])

    for i, ((name, _, tag), lines) in enumerate(zip(t["steps"], descs)):
        x = B.PAD + i * (cw + gap)
        first = i == 0
        # 첫 카드(실수 지점)는 진한 베리 테두리, 번진 카드는 옅은 베리 면
        c.rect([x, y, x + cw, y + card_h], fill="#ffffff" if first else B.BERRY_S[5],
               outline=B.BERRY_S[2] if first else B.BERRY_S[4], width=2 if first else 1, radius=14)
        c.text((x + 16, y + 18), name, f_name, fill=B.NEUT_S[0])
        for j, ln in enumerate(lines):
            c.text((x + 16, y + 52 + j * 22), ln, f_desc, fill=B.NEUT_S[1])
        # 상태 뱃지
        bw = c.text_w(tag, f_tag) + 24
        by = y + card_h - 18 - 30
        c.rect([x + 16, by, x + 16 + bw, by + 30], fill=B.BERRY_S[0] if first else B.BERRY_S[3], radius=15)
        c.center_text(x + 16 + bw / 2, by + 15, tag, f_tag, fill="#ffffff")
        if i < n - 1:
            B.flow_arrow(c, x + cw, x + cw + gap, y + card_h / 2, col=B.BERRY_S[3])
    y += card_h + 24
    c.rect([B.PAD, y, W - B.PAD, y + 46], fill=B.NEUT_S[5], radius=12)
    c.center_text(W / 2, y + 23, t["foot"], f_foot, fill=B.BERRY_S[0])
    c.save(out)


BUILDERS = {"01": build_01, "02": build_02}

if __name__ == "__main__":
    langs = ["ko", "en"]
    out_dir = os.path.join("public", "images")
    if len(sys.argv) > 1:
        langs = [sys.argv[1]]
    if len(sys.argv) > 2:
        out_dir = sys.argv[2]
    for lang in langs:
        suffix = "" if lang == "ko" else "_en"
        for k, fn in BUILDERS.items():
            fn(lang, os.path.join(out_dir, f"{SLUG}-{k}{suffix}.jpg"))
