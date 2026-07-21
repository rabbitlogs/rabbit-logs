# -*- coding: utf-8 -*-
"""sap-mrp-flow — 4단계 카드형. 상단 타이틀(배너 아님) + 예시 칩."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brand import *

T = {
    "ko": dict(
        title="MRP가 계획을 세우는 4단계",
        sub="목표와 재고로 '무엇을, 얼마나, 언제' 주문할지 역산한다",
        cards=[
            ("총 소요량", "목표 × 레시피(BOM)",   "김치 10통 → 배추 10포기"),
            ("순 소요량", "총 소요량 − 현재 재고", "배추 10 − 2 = 8포기"),
            ("발주 시점", "리드타임 역산",         "2일 걸리면 목요일 주문"),
            ("계획 오더", "최종 쇼핑 리스트",      "\"목요일: 배추 8포기\""),
        ],
    ),
    "en": dict(
        title="The four steps MRP takes to build a plan",
        sub="From target and stock, it works back to what, how much, and when to order",
        cards=[
            ("Gross requirement", "Target × recipe (BOM)",      "10 tubs → 10 cabbages"),
            ("Net requirement",   "Gross − stock on hand",      "10 − 2 = 8 cabbages"),
            ("Order date",        "Back-scheduled lead time",   "2-day lead → order Thursday"),
            ("Planned order",     "The final shopping list",    "\"Thu: 8 cabbages\""),
        ],
    ),
}

BADGE_BG = [GOLD_PALE, TEAL_PALE, GOLD_PALE, TEAL_PALE]
BADGE_FG = [MARIGOLD_D, TEAL, MARIGOLD_D, TEAL]
BORDER   = [MARIGOLD, TEAL, MARIGOLD, TEAL]


def build(lang, out):
    t = T[lang]
    f_title = font("Bold", 32)
    f_sub   = font("Medium", 18)
    f_name  = font("Bold", 21)
    f_desc  = font("Regular", 16)
    f_chip  = font("Medium", 15)

    n = 4
    gap_x = 30
    card_w = (W - MARGIN * 2 - gap_x * (n - 1)) / n
    card_h = 300

    y = 34
    img_h = int(y + 40 + 34 + 30 + card_h + 46)
    img, d = new_canvas(img_h)

    center_x_text(d, W / 2, y, t["title"], f_title, TEAL)
    _, y0, _, y1 = d.textbbox((0, 0), t["title"], font=f_title)
    y += (y1 - y0) + 20
    center_x_text(d, W / 2, y, t["sub"], f_sub, MUTED)
    _, y0, _, y1 = d.textbbox((0, 0), t["sub"], font=f_sub)
    top = y + (y1 - y0) + 34

    centers = []
    for i, (name, desc, chip) in enumerate(t["cards"]):
        x0 = MARGIN + i * (card_w + gap_x)
        x1 = x0 + card_w
        cx = (x0 + x1) / 2
        centers.append((x0, x1))

        rounded_card(d, [x0, top, x1, top + card_h], fill=WHITE,
                     outline=BORDER[i], radius=18, width=2)

        r = 30
        by = top + 58
        d.ellipse([cx - r, by - r, cx + r, by + r], fill=BADGE_BG[i])
        true_center_text(d, cx, by, str(i + 1), font("Bold", 30), BADGE_FG[i])

        ty = by + r + 26
        center_x_text(d, cx, ty, name, f_name, INK)
        _, a0, _, a1 = d.textbbox((0, 0), name, font=f_name)
        ty += (a1 - a0) + 18

        center_x_text(d, cx, ty, desc, f_desc, MUTED)
        _, b0, _, b1 = d.textbbox((0, 0), desc, font=f_desc)
        ty += (b1 - b0) + 30

        # 예시 칩 — 카드 하단 고정
        chip_h = 46
        chip_y = top + card_h - chip_h - 22
        d.rounded_rectangle([x0 + 18, chip_y, x1 - 18, chip_y + chip_h],
                            radius=10, fill="#f2ece1")
        true_center_text(d, cx, chip_y + chip_h / 2, chip, f_chip, INK)

    gap = 12
    ay = top + card_h / 2
    for i in range(n - 1):
        col = MARIGOLD if i % 2 == 0 else TEAL
        arrow(d, centers[i][1] + gap, ay, centers[i + 1][0] - gap,
              color=col, width=6, head=14)

    save(img, out)
