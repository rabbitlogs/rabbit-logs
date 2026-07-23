# -*- coding: utf-8 -*-
"""
sap-fit-gap-ways — 원본 구조 복원.

원본 구조: 상단에 Fit(체크)/Gap(느낌표) 두 카드를 나란히 놓아 "맞는 부분과
고칠 부분을 먼저 가른다"를 보여주고, 그 아래에 "Gap을 푸는 세 가지 길"
헤드라인과 3개의 색카드(개발/프로세스 변경/수용)를 배치해 각 카드 하단에
칩으로 결과 요약을 붙인다. 매트릭스(2x2)로는 이 "먼저 가르고, 그다음
세 갈래로 푼다"는 2단계 흐름이 사라지므로 커스텀 레이아웃으로 되돌린다.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brand import *


FIT_GAP_WAYS = {
    "ko": dict(
        banner="Fit/Gap", sub="표준과 우리 매장 사이",
        top=[
            ("Fit", "check", TEAL, TEAL_PALE, "표준 그대로 쓰면 되는 부분"),
            ("Gap", "exclaim", MARIGOLD_D, GOLD_PALE, "손봐야 하거나 없는 부분"),
        ],
        mid_headline="Gap을 푸는 세 가지 길",
        cards=[
            ("개발", "표준을 우리에게 맞춘다 · Z코드 개발", "비용 · 시간 ↑", MARIGOLD_D),
            ("프로세스 변경", "우리를 표준에 맞춘다 · 업무 방식을 시스템에", "가장 이상적", TEAL),
            ("수용", "표준에 없지만 감수한다 · 불편해도 표준 사용", "현명한 타협", "#8a8578"),
        ],
    ),
    "en": dict(
        banner="Fit/Gap", sub="between the standard and our restaurant",
        top=[
            ("Fit", "check", TEAL, TEAL_PALE, "Parts where the standard works as is"),
            ("Gap", "exclaim", MARIGOLD_D, GOLD_PALE, "Parts that need fixing, or don't exist"),
        ],
        mid_headline="Three ways to close a Gap",
        cards=[
            ("Develop", "Bend the system to us · Z-code development", "Cost & time ↑", MARIGOLD_D),
            ("Change the process", "Bend ourselves to the standard · adapt how we work", "The ideal outcome", TEAL),
            ("Accept", "Not in the standard, but bearable · use it anyway", "A wise compromise", "#8a8578"),
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


def _icon_check(d, cx, cy, r, color):
    """채운 원 배지 안에 흰 체크 — 얇은 외곽선보다 뚜렷하고 깔끔하게 보인다."""
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)
    d.line([(cx - r * 0.45, cy + r * 0.02), (cx - r * 0.08, cy + r * 0.4)], fill=WHITE, width=5)
    d.line([(cx - r * 0.08, cy + r * 0.4), (cx + r * 0.5, cy - r * 0.35)], fill=WHITE, width=5)


def _icon_exclaim(d, cx, cy, r, color):
    """채운 원 배지 안에 흰 느낌표."""
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)
    d.rounded_rectangle([cx - 3.2, cy - r * 0.5, cx + 3.2, cy + r * 0.12], radius=3, fill=WHITE)
    d.ellipse([cx - 3.6, cy + r * 0.32 - 3.6, cx + 3.6, cy + r * 0.32 + 3.6], fill=WHITE)


def _fit_gap(lang, out):
    t = FIT_GAP_WAYS[lang]
    f_head = font("Black", 32)
    f_sub = font("Medium", 15)
    f_mid = font("Bold", 23)
    f_ctitle = font("Bold", 21)
    f_cdesc = font("Regular", 15)
    f_chip = font("Bold", 15)

    top = BANNER_H + 40

    # ── 상단 Fit/Gap 두 카드 ──
    gap_x = 32
    top_card_w = (W - MARGIN * 2 - gap_x) / 2
    top_card_h = 118

    # ── 중간 헤드라인 ──
    mid_y = top + top_card_h + 40

    # ── 하단 3카드 ──
    bot_top = mid_y + 44
    n = len(t["cards"])
    bgap = 38
    bot_card_w = (W - MARGIN * 2 - bgap * (n - 1)) / n
    bot_card_h = 168

    img_h = int(bot_top + bot_card_h + 40)
    img, d = new_canvas(img_h)
    draw_banner(d, t["banner"], t["sub"])

    # 상단 카드
    for i, (label, icon, col, pale, desc) in enumerate(t["top"]):
        x0 = MARGIN + i * (top_card_w + gap_x)
        x1 = x0 + top_card_w
        cy = top + top_card_h / 2
        d.rounded_rectangle([x0, top, x1, top + top_card_h], radius=16,
                            fill=WHITE, outline=col, width=2)

        tx = x0 + 34
        d.text((tx, top + 16), label, font=f_head, fill=col)
        for j, ln in enumerate(_wrap(d, desc, f_sub, top_card_w - 190)):
            d.text((tx, top + 66 + j * 20), ln, font=f_sub, fill=MUTED)

        icx, icy = x1 - 56, cy
        if icon == "check":
            _icon_check(d, icx, icy, 27, col)
        else:
            _icon_exclaim(d, icx, icy, 27, col)

    # 중간 헤드라인
    center_x_text(d, W / 2, mid_y, t["mid_headline"], f_mid, INK)

    # 하단 3카드
    for i, (title, desc, chip, col) in enumerate(t["cards"]):
        x0 = MARGIN + i * (bot_card_w + bgap)
        x1 = x0 + bot_card_w
        cx = (x0 + x1) / 2
        head_h = 52

        d.rounded_rectangle([x0, bot_top, x1, bot_top + bot_card_h], radius=16,
                            fill=WHITE, outline=LINE, width=2)
        d.rounded_rectangle([x0, bot_top, x1, bot_top + head_h], radius=16, fill=col)
        d.rectangle([x0, bot_top + head_h - 16, x1, bot_top + head_h], fill=col)
        true_center_text(d, cx, bot_top + head_h / 2, title, f_ctitle, WHITE)

        dy = bot_top + head_h + 22
        for ln in _wrap(d, desc, f_cdesc, bot_card_w - 40):
            center_x_text(d, cx, dy, ln, f_cdesc, INK)
            dy += 23

        chip_h = 38
        chip_y = bot_top + bot_card_h - chip_h - 16
        pale = {MARIGOLD_D: GOLD_PALE, TEAL: TEAL_PALE}.get(col, "#efece5")
        d.rounded_rectangle([x0 + 20, chip_y, x1 - 20, chip_y + chip_h], radius=10, fill=pale)
        true_center_text(d, cx, chip_y + chip_h / 2, chip, f_chip, col)

    save(img, out)


BUILDERS = {
    "sap-fit-gap-ways": _fit_gap,
}
