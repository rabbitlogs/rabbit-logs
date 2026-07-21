# -*- coding: utf-8 -*-
"""sap-activity-cnf-01 — 3단계 카드형(레이어 2B). 국문/영문 동일 소스에서 생성."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brand import *

T = {
    "ko": dict(
        banner_t="SAP Activity와 CNF", banner_s="생산오더 실적이 확정되는 순간",
        headline="주방일지가 주방장에게 보고되기까지 세 단계",
        cards=[
            ("생산오더 발행", ["오더 안에 여러", "Activity(작업 단계)", "가 자동으로 생성"]),
            ("Activity 수행",  ["현장에서 실제 작업", "MES가 실적을", "실시간으로 수집"]),
            ("CNF로 확정",     ["실적이 SAP에 반영", "Activity 상태가", "확정(CNF)으로 전환"]),
        ],
    ),
    "en": dict(
        banner_t="SAP Activity and CNF", banner_s="the moment order results are confirmed",
        headline="Three steps from the kitchen log to the head chef",
        cards=[
            ("Order released",   ["Activities (work steps)", "are generated", "inside the order"]),
            ("Activity performed",["Work happens on site;", "MES collects results", "in real time"]),
            ("Confirmed (CNF)",  ["Results post to SAP and", "the activity status", "switches to CNF"]),
        ],
    ),
}

BAR = [TEAL, MARIGOLD, BERRY]
BADGE = [TEAL, MARIGOLD, BERRY]


def build(lang, out):
    t = T[lang]
    f_title = font("Bold", 22)
    f_body  = font("Regular", 17)

    n = 3
    gap_x = 46
    card_w = (W - MARGIN * 2 - gap_x * (n - 1)) / n
    # 카드 높이를 내용 기준으로 역산한다(고정값 금지, §8 레이어 2B).
    body_lines = max(len(b) for _, b in t["cards"])
    card_h = 62 + 27 + 24 + 30 + 22 + 26 + body_lines * 30 + 34
    top = BANNER_H + 96

    img, d = new_canvas(int(top + card_h + 44))
    draw_banner(d, t["banner_t"], t["banner_s"])
    draw_headline(d, BANNER_H + 30, t["headline"])

    centers = []
    for i, (title, body) in enumerate(t["cards"]):
        x0 = MARGIN + i * (card_w + gap_x)
        x1 = x0 + card_w
        cx = (x0 + x1) / 2
        centers.append((x0, x1, cx))

        top_bar_card(d, [x0, top, x1, top + card_h], BAR[i])

        # 원형 뱃지 — 번호
        r = 27
        by = top + 62
        d.ellipse([cx - r, by - r, cx + r, by + r], fill=BADGE[i])
        true_center_text(d, cx, by, str(i + 1), font("Bold", 27), WHITE)

        # 카드 타이틀
        ty = by + r + 24
        center_x_text(d, cx, ty, title, f_title, INK)
        _, y0, _, y1 = d.textbbox((0, 0), title, font=f_title)
        ty += (y1 - y0) + 22

        # 점선 구분
        dotted_line(d, x0 + 30, x1 - 30, ty)
        ty += 26

        for line in body:
            center_x_text(d, cx, ty, line, f_body, MUTED)
            ty += 30

    # 화살표 — 카드 경계에서 gap 만큼 띄운다
    gap = 13
    ay = top + card_h / 2
    for i in range(n - 1):
        arrow(d, centers[i][1] + gap, ay, centers[i + 1][0] - gap,
              color=MARIGOLD, width=6, head=15)

    save(img, out)
