# -*- coding: utf-8 -*-
"""
공정 카드 흐름 + 데이터 표 하이브리드.

첨부된 원본(study-pp-routing-01)의 구조를 §9 규칙에 맞게 되살린 것.
- 원본은 하단에 청록 캡션 바가 있었으나 §8 위반이므로 제거하고 높이를 역산했다.
- 위: 공정 단계를 헤더 색 카드 + 화살표로 흐르게 보여준다(구체적 예시 데이터 유지).
- 아래: 같은 데이터를 4열 표로 정리한다(공정·작업명·작업장·표준시간).

추상적 3단계 개념 카드로 바꾸면 원본이 담았던 실제 라우팅 데이터가 사라진다 —
본문이 "공정 10부터 40까지"를 그림으로 가리키므로 예시 데이터를 반드시 유지한다.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brand import *

ROUTING = {
    "ko": dict(
        banner="SAP 라우팅 — 주방 공정 순서표",
        steps=[("공정 10", "재료 손질", "전처리 스테이션", "10분"),
               ("공정 20", "조리 · 가열", "화구 스테이션", "25분"),
               ("공정 30", "소스 · 마무리", "소스 스테이션", "10분"),
               ("공정 40", "플레이팅", "플레이팅 스테이션", "5분")],
        cols=["공정", "작업명", "작업장(스테이션)", "표준시간"],
    ),
    "en": dict(
        banner="SAP routing — the kitchen operation sheet",
        steps=[("Op 10", "Prep", "Prep station", "10 min"),
               ("Op 20", "Cook · heat", "Range station", "25 min"),
               ("Op 30", "Sauce · finish", "Sauce station", "10 min"),
               ("Op 40", "Plating", "Plating station", "5 min")],
        cols=["Op", "Task", "Work center (station)", "Std. time"],
    ),
}


def _routing(lang, out):
    t = ROUTING[lang]
    f_hd   = font("Bold", 15)      # 카드 헤더(공정 N)
    f_task = font("Bold", 18)      # 작업명
    f_sta  = font("Regular", 14)   # 스테이션
    f_time = font("Bold", 17)      # 표준시간
    f_ch   = font("Bold", 15)      # 표 헤더
    f_cell = font("Regular", 16)   # 표 셀

    n = len(t["steps"])
    gap_x = 46
    card_w = (W - MARGIN * 2 - gap_x * (n - 1)) / n
    card_h = 96
    top = BANNER_H + 30

    head_colors = [TEAL, MARIGOLD, MARIGOLD, BERRY]
    pale_colors = [TEAL_PALE, GOLD_PALE, GOLD_PALE, BERRY_PALE]

    # 표 크기
    row_h = 46
    table_head_h = 44
    table_top = top + card_h + 30
    table_h = table_head_h + n * row_h

    img_h = int(table_top + table_h + 34)
    img, d = new_canvas(img_h)
    draw_banner(d, t["banner"])

    # ── 공정 카드 흐름 ──
    bounds = []
    for i, (opn, task, sta, tm) in enumerate(t["steps"]):
        x0 = MARGIN + i * (card_w + gap_x)
        x1 = x0 + card_w
        cx = (x0 + x1) / 2
        bounds.append((x0, x1))
        col, pale = head_colors[i], pale_colors[i]

        d.rounded_rectangle([x0, top, x1, top + card_h], radius=12, fill=pale,
                            outline=col, width=1)
        # 헤더 바
        d.rounded_rectangle([x0, top, x1, top + 30], radius=12, fill=col)
        d.rectangle([x0, top + 18, x1, top + 30], fill=col)
        true_center_text(d, cx, top + 15, opn, f_hd, WHITE)

        center_x_text(d, cx, top + 40, task, f_task, INK)
        center_x_text(d, cx, top + 64, sta, f_sta, MUTED)
        center_x_text(d, cx, top + 82, tm, f_time, col)

    # 화살표 (§9: gap·head를 간격에 비례, 선이 남는지 보장)
    ay = top + card_h / 2
    for i in range(n - 1):
        x0a, x1a = bounds[i][1], bounds[i + 1][0]
        span = x1a - x0a
        gap = span * 0.28
        arrow(d, x0a + gap, ay, x1a - gap, color=TEAL, width=5,
              head=max(10, int(span * 0.32)))

    # ── 데이터 표 ──
    col_frac = [0.10, 0.34, 0.36, 0.20]
    xcuts = [MARGIN]
    for f in col_frac:
        xcuts.append(xcuts[-1] + (W - MARGIN * 2) * f)

    # 헤더
    d.rounded_rectangle([MARGIN, table_top, W - MARGIN, table_top + table_head_h],
                        radius=8, fill=TEAL)
    for c, name in enumerate(t["cols"]):
        true_center_text(d, (xcuts[c] + xcuts[c + 1]) / 2,
                         table_top + table_head_h / 2, name, f_ch, WHITE)

    # 행
    for r in range(n):
        y = table_top + table_head_h + r * row_h
        if r % 2 == 1:
            d.rectangle([MARGIN, y, W - MARGIN, y + row_h], fill="#f2ede4")
        opn, task, sta, tm = t["steps"][r]
        vals = [opn.split()[-1] if lang == "ko" else opn.split()[-1], task, sta, tm]
        # 공정 번호만 표기(10,20,…)
        vals[0] = ["10", "20", "30", "40"][r]
        weights = [f_cell, f_cell, f_cell, f_cell]
        for c, v in enumerate(vals):
            colr = TEAL if c == 0 else INK
            fnt = font("Bold", 16) if c == 0 else f_cell
            true_center_text(d, (xcuts[c] + xcuts[c + 1]) / 2, y + row_h / 2, v, fnt, colr)
        d.line([(MARGIN, y + row_h), (W - MARGIN, y + row_h)], fill=LINE, width=1)

    save(img, out)


BUILDERS = {
    "study-pp-routing-01": _routing,
}
