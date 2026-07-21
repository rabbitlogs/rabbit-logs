# -*- coding: utf-8 -*-
"""stats-correlation-vs-causation-01 — 4분할 산점도(상관계수 r).

산점도 점은 고정 시드 난수로 생성해 재현성을 보장한다(국문·영문 동일 배치).
"""
import sys, os, math, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brand import *

T = {
    "ko": dict(
        banner="상관계수 r — 두 변수의 관계 강도",
        titles=["강한 양의 상관", "약한 양의 상관", "무상관", "강한 음의 상관"],
        rs=["r = +0.92", "r = +0.45", "r ≈ 0.00", "r = −0.90"],
        notes=["한쪽이 오르면 다른 쪽도 강하게 오른다",
               "약한 경향은 있지만 예외가 많다",
               "두 변수 사이에 관계가 없다",
               "한쪽이 오르면 다른 쪽은 강하게 내린다"],
        foot="r = +1에 가까울수록 강한 양의 상관 · r = 0은 무상관 · r = −1에 가까울수록 강한 음의 상관",
    ),
    "en": dict(
        banner="Correlation coefficient r — the strength of a relationship",
        titles=["Strong positive", "Weak positive", "No correlation", "Strong negative"],
        rs=["r = +0.92", "r = +0.45", "r ≈ 0.00", "r = −0.90"],
        notes=["As one rises, the other rises sharply",
               "A weak tendency, but many exceptions",
               "No relationship between the variables",
               "As one rises, the other falls sharply"],
        foot="Closer to +1 = strong positive · 0 = none · closer to −1 = strong negative",
    ),
}

COLORS = [TEAL, MARIGOLD_D, "#8a8578", BERRY]
PALES  = [TEAL_PALE, GOLD_PALE, "#eeebe4", BERRY_PALE]
SPECS  = [(0.92, 1), (0.45, 1), (0.0, 0), (-0.90, -1)]


def points(r, n=34, seed=7):
    """목표 상관계수 r에 가까운 표준화 점들을 생성한다."""
    rnd = random.Random(seed)
    xs = [rnd.gauss(0, 1) for _ in range(n)]
    es = [rnd.gauss(0, 1) for _ in range(n)]
    k = math.sqrt(max(0.0, 1 - r * r))
    ys = [r * x + k * e for x, e in zip(xs, es)]

    def norm(v):
        lo, hi = min(v), max(v)
        return [(t - lo) / (hi - lo) for t in v]

    return list(zip(norm(xs), norm(ys)))


def build(lang, out):
    t = T[lang]
    f_title = font("Bold", 17)
    f_r     = font("Bold", 26)
    f_note  = font("Medium", 14)
    f_foot  = font("Regular", 14)

    n = 4
    gap_x = 18
    card_w = (W - MARGIN * 2 - gap_x * (n - 1)) / n
    plot_h = 210
    head_h = 76
    note_h = 44
    card_h = head_h + plot_h + note_h + 18
    top = BANNER_H + 24

    img, d = new_canvas(int(top + card_h + 24 + 22))
    draw_banner(d, t["banner"])

    for i in range(n):
        x0 = MARGIN + i * (card_w + gap_x)
        x1 = x0 + card_w
        cx = (x0 + x1) / 2
        col = COLORS[i]

        d.rounded_rectangle([x0, top, x1, top + card_h], radius=14,
                            fill=PALES[i], outline=LINE, width=1)

        center_x_text(d, cx, top + 14, t["titles"][i], f_title, col)
        center_x_text(d, cx, top + 40, t["rs"][i], f_r, col)

        # 산점도 영역
        px0, py0 = x0 + 22, top + head_h
        px1, py1 = x1 - 22, top + head_h + plot_h - 16
        # 격자
        for g in range(1, 4):
            gx = px0 + (px1 - px0) * g / 4
            gy = py0 + (py1 - py0) * g / 4
            d.line([(gx, py0), (gx, py1)], fill="#ffffff", width=1)
            d.line([(px0, gy), (px1, gy)], fill="#ffffff", width=1)
        d.rectangle([px0, py0, px1, py1], outline="#d5cdbd", width=1)

        r, slope = SPECS[i]
        for ux, uy in points(r, seed=11 + i):
            cxp = px0 + 12 + ux * (px1 - px0 - 24)
            cyp = py1 - 12 - uy * (py1 - py0 - 24)
            d.ellipse([cxp - 4, cyp - 4, cxp + 4, cyp + 4], fill=col)

        # 추세선 (무상관은 생략)
        if slope != 0:
            m = 0.62 * slope
            x_a, x_b = px0 + 14, px1 - 14
            mid_y = (py0 + py1) / 2
            span = (py1 - py0) * 0.34
            y_a = mid_y + span * (1 if slope > 0 else -1)
            y_b = mid_y - span * (1 if slope > 0 else -1)
            d.line([(x_a, y_a), (x_b, y_b)], fill=col, width=3)

        ny = top + card_h - note_h - 8
        d.rounded_rectangle([x0 + 12, ny, x1 - 12, ny + note_h], radius=9, fill=WHITE)
        words = t["notes"][i].split()
        lines, cur = [], ""
        for w in words:
            trial = (cur + " " + w).strip()
            if text_w(d, trial, f_note) > card_w - 46 and cur:
                lines.append(cur); cur = w
            else:
                cur = trial
        lines.append(cur)
        ly = ny + (note_h - len(lines) * 19) / 2
        for ln in lines:
            center_x_text(d, cx, ly, ln, f_note, INK)
            ly += 19

    center_x_text(d, W / 2, top + card_h + 22, t["foot"], f_foot, MUTED)
    save(img, out)
