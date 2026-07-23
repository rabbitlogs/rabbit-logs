# -*- coding: utf-8 -*-
"""
sap-pp-tcode-01 — sap-pp-tcode.md 글의 대표 이미지.

본문 구조: 주문(VA01·VA03) → 생산(MD04·CO03) → 자재(MMBE·MIGO) → 출하(VL01N)
네 단계를 업무 흐름 순으로 보여주고, 각 단계의 대표 T-CODE를 카드 하단에
코드체로 표기한다. steps() 템플릿과 같은 원형 순번 배지 골격을 쓰되, 카드
맨 아래 T-CODE 줄만 얹은 확장판이라 새 전용 렌더로 만든다(steps()에 CO드
줄을 넣는 옵션이 없어 필드 구조가 다름).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brand import *


PP_TCODE = {
    "ko": dict(
        banner="PP 실무의 업무 흐름", sub="주문에서 출하까지, T-CODE도 흐름 단위로 익힌다",
        cards=[
            dict(title="주문", desc="고객 주문 접수", codes="VA01 · VA03"),
            dict(title="생산", desc="계획 · 오더 처리", codes="MD04 · CO03"),
            dict(title="자재", desc="재고 · 구매 확인", codes="MMBE · MIGO"),
            dict(title="출하", desc="납품 · 배송", codes="VL01N"),
        ],
        foot="자주 이어지는 묶음을 즐겨찾기에 등록하면 작업 속도가 빨라진다",
    ),
    "en": dict(
        banner="The PP workflow in practice", sub="from order to shipment, learn T-codes by the flow",
        cards=[
            dict(title="Order", desc="Customer order intake", codes="VA01 · VA03"),
            dict(title="Production", desc="Planning · order handling", codes="MD04 · CO03"),
            dict(title="Material", desc="Stock · purchasing checks", codes="MMBE · MIGO"),
            dict(title="Shipment", desc="Delivery · dispatch", codes="VL01N"),
        ],
        foot="Bookmark T-codes that often chain together and work moves faster",
    ),
}


def _wrap(d, text, f, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if text_w(d, t, f) > max_w and cur:
            lines.append(cur); cur = w
        else:
            cur = t
    if cur:
        lines.append(cur)
    return lines


COLORS = [TEAL, MARIGOLD_D, TEAL, MARIGOLD_D]
PALES = [TEAL_PALE, GOLD_PALE, TEAL_PALE, GOLD_PALE]


def _pp_tcode(lang, out):
    t = PP_TCODE[lang]
    f_title = font("Bold", 21)
    f_desc = font("Regular", 15)
    f_code = font("Bold", 15)
    f_foot = font("Medium", 15)

    n = len(t["cards"])
    gap_x = 30
    card_w = (W - MARGIN * 2 - gap_x * (n - 1)) / n
    r = 27
    head_h = 34 + r * 2 + 20   # 상단 여백 + 배지 지름 + 배지 아래 여백
    code_h = 40
    card_h = head_h + 26 + 22 + code_h + 20  # 타이틀 + 설명 + 코드칩 + 하단 여백

    top = BANNER_H + 44
    foot_h = 48
    foot_gap = 22

    img_h = int(top + card_h + foot_gap + foot_h + 40)
    img, d = new_canvas(img_h)
    draw_banner(d, t["banner"], t["sub"])

    bounds = []
    for i, c in enumerate(t["cards"]):
        x0 = MARGIN + i * (card_w + gap_x)
        x1 = x0 + card_w
        cx = (x0 + x1) / 2
        bounds.append((x0, x1))
        col, pale = COLORS[i], PALES[i]

        d.rounded_rectangle([x0, top, x1, top + card_h], radius=16, fill=WHITE, outline=LINE, width=2)

        by = top + 34
        d.ellipse([cx - r, by - r, cx + r, by + r], fill=pale)
        true_center_text(d, cx, by, str(i + 1), font("Bold", 24), col)

        ty = by + r + 30
        center_x_text(d, cx, ty, c["title"], f_title, INK)
        ty += 32
        center_x_text(d, cx, ty, c["desc"], f_desc, MUTED)

        chip_w = text_w(d, c["codes"], f_code) + 28
        chip_y = top + card_h - code_h - 14
        d.rounded_rectangle([cx - chip_w / 2, chip_y, cx + chip_w / 2, chip_y + 28], radius=9, fill=pale)
        true_center_text(d, cx, chip_y + 14, c["codes"], f_code, col)

    ay = top + head_h - 6
    for i in range(n - 1):
        flow_arrow(d, bounds[i][1], bounds[i + 1][0], ay)

    fy = top + card_h + foot_gap
    d.rounded_rectangle([MARGIN, fy, W - MARGIN, fy + foot_h], radius=12, fill="#e9e6df")
    center_x_text(d, W / 2, fy + 15, t["foot"], f_foot, INK)

    save(img, out)


BUILDERS = {
    "sap-pp-tcode-01": _pp_tcode,
}
