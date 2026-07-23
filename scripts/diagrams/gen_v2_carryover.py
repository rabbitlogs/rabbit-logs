# -*- coding: utf-8 -*-
"""
sap-production-order-carryover-01 — 전용 렌더(얇은 색상바 + 중앙 정렬).

기존 duo()는 헤더 전체를 색으로 채우고 항목을 글머리점 왼쪽 정렬로
나열하는 스타일이라, 사용자가 원하는 참고 디자인(카드 상단에 얇은 색
바만 두르고, 제목·본문 모두 가운데 정렬, 화살표(→)로 결과를 짚어주는
한 줄)과 달랐다. 카드 높이도 duo()는 5행 기준으로 계산돼 이 도식처럼
줄 수가 적을 때 카드 아래 여백이 과하게 남는다.

전용 렌더로 만들어 참고 디자인의 톤을 그대로 따르되, 카드 높이를
실제 줄 수(3줄)에 맞춰 계산해 빈 공간을 없앤다. 상단 바는 top_bar_card()
를 그대로 써서 라운드 모서리 이격 문제를 방지한다.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brand import *


CARRYOVER = {
    "ko": dict(banner="생산오더 이월 방식", sub="오더 이월 vs WIP 이월",
        headline="만들다 만 음식 30인분, 어떻게 처리할까",
        left=dict(title="방식 1: 오더 이월", col=TEAL,
                  body=["기존 오더 TECO(마감)", "새 오더 신규 생성", "→ 70개 / 30개로 명확히 구분됨"]),
        right=dict(title="방식 2: WIP 이월", col=MARIGOLD_D,
                   body=["오더는 계속 오픈 유지", "원가만 다음 달로 이전", "→ 오더 하나로 전체 이력 유지"]),
        foot="오더 수가 늘어도 이력이 명확한 쪽 vs 오더는 하나지만 원가 추적이 필요한 쪽",
    ),
    "en": dict(banner="Carrying a production order over", sub="order carry-over vs WIP carry-over",
        headline="Thirty portions half-made — what do you do with them?",
        left=dict(title="Option 1: carry the order", col=TEAL,
                  body=["TECO the existing order", "Create a brand-new order", "→ A clean split of 70 and 30"]),
        right=dict(title="Option 2: carry the WIP", col=MARIGOLD_D,
                   body=["The order stays open", "Only the cost moves to next month",
                         "→ One order keeps the full history"]),
        foot="More orders but a clear trail, vs. one order but cost tracking to manage",
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


def _carryover(lang, out):
    t = CARRYOVER[lang]
    f_title = font("Bold", 20)
    f_body = font("Regular", 16)
    f_foot = font("Bold", 16)

    gap_x = 40
    card_w = (W - MARGIN * 2 - gap_x) / 2
    pad_top = 30
    title_h = 34

    tmp_lines_l = []
    tmp_lines_r = []

    top = BANNER_H + 96
    foot_gap = 24
    foot_h = 48

    from PIL import Image, ImageDraw
    tmp_img = Image.new("RGB", (10, 10))
    tmp_d = ImageDraw.Draw(tmp_img)

    def body_h_for(spec):
        h = 0
        for ln in spec["body"]:
            wrapped = _wrap(tmp_d, ln, f_body, card_w - 60)
            h += len(wrapped) * 26
        return h

    body_h = max(body_h_for(t["left"]), body_h_for(t["right"]))
    card_h = pad_top + title_h + 20 + body_h + 30

    img_h = int(top + card_h + foot_gap + foot_h + 40)
    img, d = new_canvas(img_h)
    draw_banner(d, t["banner"], t["sub"])
    draw_headline(d, BANNER_H + 30, t["headline"])

    for i, spec in enumerate([t["left"], t["right"]]):
        x0 = MARGIN + i * (card_w + gap_x)
        x1 = x0 + card_w
        cx = (x0 + x1) / 2
        col = spec["col"]

        top_bar_card(d, [x0, top, x1, top + card_h], col, radius=14, bar_h=5)

        ty = top + pad_top
        center_x_text(d, cx, ty, spec["title"], f_title, INK)
        ty += title_h + 14

        for ln in spec["body"]:
            for wln in _wrap(d, ln, f_body, card_w - 60):
                center_x_text(d, cx, ty, wln, f_body, MUTED)
                ty += 26

    fy = top + card_h + foot_gap
    d.rounded_rectangle([MARGIN, fy, W - MARGIN, fy + foot_h], radius=12, fill=TEAL)
    fw = text_w(d, t["foot"], f_foot)
    if fw > W - MARGIN * 2 - 40:
        lines = _wrap(d, t["foot"], f_foot, W - MARGIN * 2 - 40)
        ly = fy + foot_h / 2 - (len(lines) - 1) * 11
        for ln in lines:
            center_x_text(d, W / 2, ly - 10, ln, f_foot, WHITE)
            ly += 22
    else:
        true_center_text(d, W / 2, fy + foot_h / 2, t["foot"], f_foot, WHITE)

    save(img, out)


BUILDERS = {
    "sap-production-order-carryover-01": _carryover,
}
