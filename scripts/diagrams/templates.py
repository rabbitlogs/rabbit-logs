# -*- coding: utf-8 -*-
"""
레이어 2 공통 템플릿.

같은 골격이 반복되는 도식(단계 카드, 2열 비교, 비교표)을 함수 하나로 처리한다.
개별 스크립트는 텍스트 데이터만 넘기면 되므로, 도식이 늘어나도 코드가 늘지 않는다.
"""
from brand import *

STEP_COLORS = [TEAL, MARIGOLD, BERRY, TEAL, MARIGOLD]
STEP_PALES  = [TEAL_PALE, GOLD_PALE, BERRY_PALE, TEAL_PALE, GOLD_PALE]


def _wrap(d, text, f, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if text_w(d, trial, f) > max_w and cur:
            lines.append(cur); cur = w
        else:
            cur = trial
    if cur:
        lines.append(cur)
    return lines


def steps(out, banner, headline, cards, badge=True, sub=None):
    """N단계 카드 + 화살표. cards = [(제목, [본문줄...]), ...]"""
    f_title = font("Bold", 21)
    f_body  = font("Regular", 16)

    n = len(cards)
    gap_x = 46 if n <= 3 else 30
    card_w = (W - MARGIN * 2 - gap_x * (n - 1)) / n
    body_lines = max(len(b) for _, b in cards)
    card_h = (62 + 27 + 24 if badge else 34) + 30 + 22 + 26 + body_lines * 29 + 30
    top = BANNER_H + (96 if headline else 46)

    img, d = new_canvas(int(top + card_h + 44))
    draw_banner(d, banner, sub)
    if headline:
        draw_headline(d, BANNER_H + 30, headline)

    bounds = []
    for i, (title, body) in enumerate(cards):
        x0 = MARGIN + i * (card_w + gap_x)
        x1 = x0 + card_w
        cx = (x0 + x1) / 2
        bounds.append((x0, x1))
        col = STEP_COLORS[i % len(STEP_COLORS)]
        top_bar_card(d, [x0, top, x1, top + card_h], col)

        if badge:
            r = 27
            by = top + 62
            d.ellipse([cx - r, by - r, cx + r, by + r], fill=col)
            true_center_text(d, cx, by, str(i + 1), font("Bold", 27), WHITE)
            ty = by + r + 24
        else:
            ty = top + 34

        for ln in _wrap(d, title, f_title, card_w - 28):
            center_x_text(d, cx, ty, ln, f_title, INK)
            ty += 28
        ty += 16
        dotted_line(d, x0 + 30, x1 - 30, ty)
        ty += 24
        for line in body:
            center_x_text(d, cx, ty, line, f_body, MUTED)
            ty += 29

    gap = 13
    ay = top + card_h / 2
    for i in range(n - 1):
        arrow(d, bounds[i][1] + gap, ay, bounds[i + 1][0] - gap,
              color=MARIGOLD, width=6, head=15)

    save(img, out)


def duo(out, banner, headline, left, right, sub=None):
    """2열 비교 카드. left/right = (헤더, 부제 or None, [항목...])"""
    f_head = font("Bold", 22)
    f_hsub = font("Medium", 14)
    f_item = font("Regular", 17)

    gap_x = 40
    card_w = (W - MARGIN * 2 - gap_x) / 2
    head_h = 62
    rows = max(len(left[2]), len(right[2]))
    card_h = head_h + 26 + rows * 32 + 24
    top = BANNER_H + (96 if headline else 44)

    img, d = new_canvas(int(top + card_h + 42))
    draw_banner(d, banner, sub)
    if headline:
        draw_headline(d, BANNER_H + 30, headline)

    for i, (head, hsub, items) in enumerate([left, right]):
        x0 = MARGIN + i * (card_w + gap_x)
        x1 = x0 + card_w
        cx = (x0 + x1) / 2
        col = TEAL if i == 0 else MARIGOLD
        pale = TEAL_PALE if i == 0 else GOLD_PALE

        d.rounded_rectangle([x0, top, x1, top + card_h], radius=16,
                            fill=WHITE, outline=LINE, width=2)
        d.rounded_rectangle([x0, top, x1, top + head_h], radius=16, fill=col)
        d.rectangle([x0, top + head_h - 16, x1, top + head_h], fill=col)

        if hsub:
            center_x_text(d, cx, top + 10, head, f_head, WHITE)
            center_x_text(d, cx, top + 39, hsub, f_hsub, "#eef4f2")
        else:
            true_center_text(d, cx, top + head_h / 2, head, f_head, WHITE)

        y = top + head_h + 22
        for it in items:
            d.ellipse([x0 + 24, y + 7, x0 + 31, y + 14], fill=col)
            for j, ln in enumerate(_wrap(d, it, f_item, card_w - 66)):
                d.text((x0 + 42, y), ln, font=f_item, fill=INK if j == 0 else MUTED)
                y += 25
            y += 7

    save(img, out)


def matrix(out, banner, headline, col_heads, row_labels, cells, sub=None, foot=None):
    """비교표. col_heads=[(제목,부제)], row_labels=[...], cells=[[행1...],[행2...]]"""
    f_ch  = font("Bold", 19)
    f_cs  = font("Medium", 13)
    f_rl  = font("Bold", 16)
    f_cell= font("Regular", 16)
    f_foot= font("Medium", 15)

    label_w = 132
    ncol = len(col_heads)
    grid_x = MARGIN + label_w
    col_w = (W - MARGIN - grid_x) / ncol
    head_h = 62
    row_h = 52
    top = BANNER_H + (92 if headline else 40)
    table_h = head_h + row_h * len(row_labels)

    img, d = new_canvas(int(top + table_h + (54 if foot else 0) + 40))
    draw_banner(d, banner, sub)
    if headline:
        draw_headline(d, BANNER_H + 28, headline)

    for c, (ch, cs) in enumerate(col_heads):
        x0 = grid_x + c * col_w
        col = TEAL if c == 0 else MARIGOLD
        d.rounded_rectangle([x0 + 3, top, x0 + col_w - 3, top + head_h], radius=12, fill=col)
        if cs:
            center_x_text(d, x0 + col_w / 2, top + 11, ch, f_ch, WHITE)
            center_x_text(d, x0 + col_w / 2, top + 37, cs, f_cs, "#eef4f2")
        else:
            true_center_text(d, x0 + col_w / 2, top + head_h / 2, ch, f_ch, WHITE)

    for r, label in enumerate(row_labels):
        y = top + head_h + r * row_h
        if r % 2 == 0:
            d.rectangle([MARGIN, y, W - MARGIN, y + row_h], fill="#f4f0e8")
        true_center_text(d, MARGIN + label_w / 2, y + row_h / 2, label, f_rl, TEAL)
        for c in range(ncol):
            x0 = grid_x + c * col_w
            true_center_text(d, x0 + col_w / 2, y + row_h / 2, cells[r][c], f_cell, INK)
        d.line([(MARGIN, y + row_h), (W - MARGIN, y + row_h)], fill=LINE, width=1)

    if foot:
        fy = top + table_h + 16
        d.rounded_rectangle([MARGIN, fy, W - MARGIN, fy + 44], radius=12, fill=TEAL)
        true_center_text(d, W / 2, fy + 22, foot, f_foot, WHITE)

    save(img, out)
