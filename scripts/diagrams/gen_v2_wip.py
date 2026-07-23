# -*- coding: utf-8 -*-
"""
sap-wip-overview — 원본 디자인 복원.

원본 구조: 상단 3카드가 원자재→WIP→완제품 흐름을 화살표로 연결(WIP 카드만
마리골드 테두리로 강조, 나머지 둘은 무채색 테두리). 중간에 "같은 WIP를 세
부서가 다르게 본다" 헤드라인. 하단 3카드는 상단 컬러 바 + 제목(PP 생산/
CO 원가/MM 재고) + 본문 두 줄(제목/설명) 구조.

기존 hub() 방사형 템플릿은 "위→중→아래로 흐르는 공정"이라는 원본의 시간
축과 "세 부서가 같은 대상을 바라본다"는 병렬 비교 구조 둘 다를 표현하지
못해 전용 렌더로 되돌린다.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brand import *


WIP = {
    "ko": dict(
        banner="WIP, 원자재와 완제품 사이", sub="아직 접시에 담기지 않았을 뿐, 이미 가치를 지닌 자산",
        flow=[
            ("원자재", "창고의 개별 재료", "양파 · 고기 · 양념", False),
            ("WIP", "만들어지는 중", "끓고 있는 찌개", True),
            ("완제품", "접시에 담긴 요리", "손님에게 낼 준비 완료", False),
        ],
        headline="같은 WIP를 세 부서가 다르게 본다",
        views=[
            ("PP 생산", "생산 라인의 청진기", "쌓이면 병목 신호", MARIGOLD),
            ("CO 원가", "숨은 자산의 근거", "결산 안 하면 자산 누락", TEAL),
            ("MM 재고", "미래 계획의 나침반", "곧 완성될 공급 물량", MARIGOLD),
        ],
    ),
    "en": dict(
        banner="WIP — between raw material and finished goods", sub="not yet plated, but already an asset",
        flow=[
            ("Raw material", "Individual items in stock", "Onion · meat · seasoning", False),
            ("WIP", "Being made", "A stew still on the stove", True),
            ("Finished goods", "Plated and ready", "Ready to serve the guest", False),
        ],
        headline="Three departments see the same WIP differently",
        views=[
            ("PP Production", "A stethoscope on the line", "Piles signal a bottleneck", MARIGOLD),
            ("CO Costing", "Proof of a hidden asset", "Skip it and assets vanish", TEAL),
            ("MM Inventory", "A compass for planning", "Supply about to arrive", MARIGOLD),
        ],
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


def _wip(lang, out):
    t = WIP[lang]
    f_title = font("Black", 24)
    f_desc = font("Medium", 16)
    f_sub = font("Regular", 14)
    f_headline = font("Bold", 22)
    f_vtitle = font("Bold", 19)
    f_vdesc = font("Regular", 15)

    top = BANNER_H + 44
    n = len(t["flow"])
    gap_x = 40
    card_w = (W - MARGIN * 2 - gap_x * (n - 1)) / n
    flow_h = 130

    headline_gap_top = 40
    headline_h = 34
    headline_gap_bottom = 30

    view_h = 130
    view_gap = 26

    img_h = int(top + flow_h + headline_gap_top + headline_h + headline_gap_bottom
                + view_h + 40)
    img, d = new_canvas(img_h)
    draw_banner(d, t["banner"], t["sub"])

    bounds = []
    for i, (title, desc, sub, hi) in enumerate(t["flow"]):
        x0 = MARGIN + i * (card_w + gap_x)
        x1 = x0 + card_w
        cx = (x0 + x1) / 2
        bounds.append((x0, x1))

        if hi:
            d.rounded_rectangle([x0, top, x1, top + flow_h], radius=16, fill=WHITE,
                                 outline=MARIGOLD, width=3)
            title_col = MARIGOLD_D
        else:
            d.rounded_rectangle([x0, top, x1, top + flow_h], radius=16, fill=WHITE,
                                 outline=LINE, width=2)
            title_col = MUTED

        ty = top + 26
        center_x_text(d, cx, ty, title, f_title, title_col)
        ty += 40
        center_x_text(d, cx, ty, desc, f_desc, INK)
        ty += 28
        center_x_text(d, cx, ty, sub, f_sub, MUTED)

    ay = top + flow_h / 2
    for i in range(n - 1):
        flow_arrow(d, bounds[i][1], bounds[i + 1][0], ay)

    hy = top + flow_h + headline_gap_top
    center_x_text(d, W / 2, hy, t["headline"], f_headline, INK)

    vy = hy + headline_h + headline_gap_bottom
    vn = len(t["views"])
    vgap_x = 30
    vcard_w = (W - MARGIN * 2 - vgap_x * (vn - 1)) / vn
    for i, (title, desc, sub, col) in enumerate(t["views"]):
        x0 = MARGIN + i * (vcard_w + vgap_x)
        x1 = x0 + vcard_w
        cx = (x0 + x1) / 2

        top_bar_card(d, [x0, vy, x1, vy + view_h], col)

        ty = vy + 14 + 14
        center_x_text(d, cx, ty, title, f_vtitle, INK)
        ty += 40
        for ln in _wrap(d, desc, f_vdesc, vcard_w - 40):
            center_x_text(d, cx, ty, ln, f_vdesc, INK)
            ty += 24
        ty += 4
        for ln in _wrap(d, sub, f_vdesc, vcard_w - 40):
            center_x_text(d, cx, ty, ln, f_vdesc, MUTED)
            ty += 22

    save(img, out)


BUILDERS = {
    "sap-wip-overview": _wip,
}
