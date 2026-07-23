# -*- coding: utf-8 -*-
"""
sap-gi-gr-cnf-flow — 원본 디자인 복원.

원본 구조: 헤더 전체를 색으로 채운 3카드(GI/GR/CNF + 영문 부제), 카드 안에
큰 키워드(출고/입고/생산실적확정)를 색상으로 강조, 본문 2줄, 하단에 옅은
색 note 칩(감소 −/증가 +/증가 + 정산). 카드 사이는 화살표로 잇고, 맨 아래
진한 배경의 요약 바로 마무리한다.

기존 steps() 템플릿(원형 순번 배지 + 얇은 상단 컬러바)으로는 이 "헤더색칠+
큰 키워드" 인상이 사라지므로, 이미 fit-gap-ways/mes-interface에서 쓰던
헤더색칠 카드 스타일을 그대로 가져와 전용 렌더로 만든다. 화살표는 §9 규칙
(gap·head를 간격에 비례, 최소 44px 확보)에 맞춰 공용 flow_arrow()를 쓴다.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brand import *


GI_GR_CNF = {
    "ko": dict(
        banner="GI · GR · CNF", sub="재고의 세 순간",
        headline="나가고, 들어오고, 만들어진다",
        cards=[
            dict(tag="GI", tsub="Goods Issue", col=MARIGOLD_D, pale=GOLD_PALE,
                 key="출고", body=["재고가 나가는 것", "창고 → 주방 · 출하"], note="감소 −"),
            dict(tag="GR", tsub="Goods Receipt", col=TEAL, pale=TEAL_PALE,
                 key="입고", body=["재고가 들어오는 것", "납품 · 생산품 받기"], note="증가 +"),
            dict(tag="CNF", tsub="Confirmation", col=MARIGOLD_D, pale=GOLD_PALE,
                 key="생산실적확정", body=["만들고 보고하는 것", "완제품 입고 + 원가"], note="증가 + 정산"),
        ],
        foot_key="GI와 GR은 보통 짝으로",
        foot_note="한쪽에서 나가면 다른 쪽에서 받는다",
    ),
    "en": dict(
        banner="GI · GR · CNF", sub="three moments in inventory",
        headline="Goods leave, goods arrive, goods get made",
        cards=[
            dict(tag="GI", tsub="Goods Issue", col=MARIGOLD_D, pale=GOLD_PALE,
                 key="Issue", body=["Stock leaving", "Warehouse → kitchen"], note="Decrease −"),
            dict(tag="GR", tsub="Goods Receipt", col=TEAL, pale=TEAL_PALE,
                 key="Receipt", body=["Stock arriving", "Deliveries, finished output"], note="Increase +"),
            dict(tag="CNF", tsub="Confirmation", col=MARIGOLD_D, pale=GOLD_PALE,
                 key="Confirmed", body=["Making and reporting", "Finished goods plus cost"], note="Increase + settle"),
        ],
        foot_key="GI and GR usually pair up",
        foot_note="what leaves one side arrives on the other",
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


def _card_body_lines(d, spec, f_body, card_w):
    n = 0
    for ln in spec["body"]:
        n += len(_wrap(d, ln, f_body, card_w - 40))
    return n


def _card(d, box, spec, f_tag, f_tsub, f_key, f_body, f_note, head_h):
    x0, y0, x1, y1 = box
    col, pale = spec["col"], spec["pale"]
    cx = (x0 + x1) / 2

    d.rounded_rectangle(box, radius=16, fill=WHITE, outline=LINE, width=2)
    d.rounded_rectangle([x0, y0, x1, y0 + head_h], radius=16, fill=col)
    d.rectangle([x0, y0 + head_h - 16, x1, y0 + head_h], fill=col)
    if spec.get("tsub"):
        center_x_text(d, cx, y0 + 9, spec["tag"], f_tag, WHITE)
        center_x_text(d, cx, y0 + 34, spec["tsub"], f_tsub, "#f5e9d6" if col == MARIGOLD_D else "#dceae6")
    else:
        true_center_text(d, cx, y0 + head_h / 2, spec["tag"], f_tag, WHITE)

    ky = y0 + head_h + 24
    for ln in _wrap(d, spec["key"], f_key, (x1 - x0) - 32):
        center_x_text(d, cx, ky, ln, f_key, col)
        ky += 34
    by = ky + 12

    for ln in spec["body"]:
        for wln in _wrap(d, ln, f_body, (x1 - x0) - 40):
            center_x_text(d, cx, by, wln, f_body, MUTED)
            by += 22

    note_h = 36
    note_y = y1 - note_h - 18
    d.rounded_rectangle([x0 + 22, note_y, x1 - 22, note_y + note_h], radius=9, fill=pale)
    true_center_text(d, cx, note_y + note_h / 2, spec["note"], font("Bold", 15), col)


def _gi_gr_cnf(lang, out):
    t = GI_GR_CNF[lang]
    f_tag = font("Bold", 21)
    f_tsub = font("Medium", 12)
    f_key = font("Black", 26)
    f_body = font("Regular", 15)
    f_note = font("Bold", 15)
    f_foot_key = font("Bold", 17)
    f_foot_note = font("Medium", 14)

    top = BANNER_H + 96
    n = len(t["cards"])
    gap_x = 46
    card_w = (W - MARGIN * 2 - gap_x * (n - 1)) / n
    head_h = 58

    tmp_img_h = 10
    from PIL import Image, ImageDraw
    tmp_img = Image.new("RGB", (10, tmp_img_h))
    tmp_d = ImageDraw.Draw(tmp_img)

    def _card_h(spec):
        key_lines = len(_wrap(tmp_d, spec["key"], f_key, card_w - 32))
        key_h = key_lines * 34
        body_lines = _card_body_lines(tmp_d, spec, f_body, card_w)
        body_h = body_lines * 22
        return head_h + 24 + key_h + 12 + body_h + 18 + 36 + 18

    card_h = max(_card_h(c) for c in t["cards"])

    foot_h = 52
    foot_gap = 22

    img_h = int(top + card_h + foot_gap + foot_h + 40)
    img, d = new_canvas(img_h)
    draw_banner(d, t["banner"], t["sub"])
    draw_headline(d, BANNER_H + 30, t["headline"])

    bounds = []
    for i, spec in enumerate(t["cards"]):
        x0 = MARGIN + i * (card_w + gap_x)
        x1 = x0 + card_w
        bounds.append((x0, x1))
        _card(d, (x0, top, x1, top + card_h), spec, f_tag, f_tsub, f_key, f_body, f_note, head_h)

    ay = top + head_h + 40
    for i in range(n - 1):
        flow_arrow(d, bounds[i][1], bounds[i + 1][0], ay)

    fy = top + card_h + foot_gap
    d.rounded_rectangle([MARGIN, fy, W - MARGIN, fy + foot_h], radius=12, fill=TEAL)
    key = t["foot_key"]
    note = t["foot_note"]
    kw = text_w(d, key, f_foot_key)
    sep = 12
    nw = text_w(d, note, f_foot_note)
    total = kw + sep + nw
    sx = (W - total) / 2
    d.text((sx, fy + 12), key, font=f_foot_key, fill=WHITE)
    d.text((sx + kw + sep, fy + 13), note, font=f_foot_note, fill="#dceae6")

    save(img, out)


BUILDERS = {
    "sap-gi-gr-cnf-flow": _gi_gr_cnf,
}
