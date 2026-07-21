# -*- coding: utf-8 -*-
"""stats-adsp-01 — 배너 + 메타줄 + 3과목 카드 + 합격 기준 바."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brand import *

T = {
    "ko": dict(
        banner="ADsP 시험 구성 & 합격 기준",
        meta="50문항 · 4지선다 · 시험시간 100분 · 응시료 50,000원 · 영구 유효",
        tag=["과목 Ⅰ", "과목 Ⅱ", "과목 Ⅲ"],
        names=["데이터 이해", "데이터분석 기획", "데이터분석"],
        items=[
            ["데이터의 이해", "데이터의 가치와 미래", "데이터 사이언스 전략"],
            ["분석 기획의 이해", "분석 마스터플랜", "데이터 거버넌스"],
            ["R 기초와 데이터 마트", "통계분석", "정형 데이터 마이닝"],
        ],
        pass_t="합격 기준",
        pass_s="전 과목 평균 60점 이상  |  과목별 최소 40점 이상 (과락 기준)",
    ),
    "en": dict(
        banner="ADsP exam structure & passing criteria",
        meta="50 questions · multiple choice · 100 minutes · KRW 50,000 · no expiry",
        tag=["Part Ⅰ", "Part Ⅱ", "Part Ⅲ"],
        names=["Understanding data", "Analytics planning", "Data analysis"],
        items=[
            ["What data is", "The value and future of data", "Data science strategy"],
            ["Planning fundamentals", "The analytics master plan", "Data governance"],
            ["R basics and data marts", "Statistical analysis", "Structured data mining"],
        ],
        pass_t="Passing criteria",
        pass_s="Average 60+ across all parts  |  Minimum 40 per part (fail threshold)",
    ),
}


def build(lang, out):
    t = T[lang]
    f_meta = font("Regular", 17)
    f_tag  = font("Bold", 15)
    f_name = font("Bold", 25)
    f_item = font("Regular", 17)
    f_pt   = font("Bold", 21)
    f_ps   = font("Medium", 17)

    n = 3
    gap_x = 22
    card_w = (W - MARGIN * 2 - gap_x * (n - 1)) / n
    card_h = 232
    pass_h = 74

    y = BANNER_H + 26
    top = y + 34 + 22
    img_h = int(top + card_h + 18 + pass_h + 26)
    img, d = new_canvas(img_h)

    draw_banner(d, t["banner"])

    center_x_text(d, W / 2, y, t["meta"], f_meta, MUTED)
    _, m0, _, m1 = d.textbbox((0, 0), t["meta"], font=f_meta)
    ly = y + (m1 - m0) + 16
    d.line([(MARGIN + 20, ly), (W - MARGIN - 20, ly)], fill=MARIGOLD, width=2)

    for i in range(n):
        x0 = MARGIN + i * (card_w + gap_x)
        x1 = x0 + card_w
        cx = (x0 + x1) / 2
        d.rounded_rectangle([x0, top, x1, top + card_h], radius=18, fill=TEAL)

        # 과목 태그 — 마리골드 pill
        tw = text_w(d, t["tag"][i], f_tag)
        pw, ph = tw + 30, 30
        d.rounded_rectangle([cx - pw / 2, top + 22, cx + pw / 2, top + 22 + ph],
                            radius=15, fill=MARIGOLD)
        true_center_text(d, cx, top + 22 + ph / 2, t["tag"][i], f_tag, WHITE)

        ty = top + 22 + ph + 20
        center_x_text(d, cx, ty, t["names"][i], f_name, WHITE)
        _, a0, _, a1 = d.textbbox((0, 0), t["names"][i], font=f_name)
        ty += (a1 - a0) + 18

        d.line([(x0 + 26, ty), (x1 - 26, ty)], fill="#4e857b", width=1)
        ty += 18

        for it in t["items"][i]:
            center_x_text(d, cx, ty, it, f_item, "#d8e5e2")
            ty += 29

    py = top + card_h + 18
    d.rounded_rectangle([MARGIN, py, W - MARGIN, py + pass_h], radius=14, fill=MARIGOLD)
    center_x_text(d, W / 2, py + 14, t["pass_t"], f_pt, WHITE)
    center_x_text(d, W / 2, py + 44, t["pass_s"], f_ps, "#fdf3e3")

    save(img, out)
