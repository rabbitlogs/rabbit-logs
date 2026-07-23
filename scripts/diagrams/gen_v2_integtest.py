# -*- coding: utf-8 -*-
"""
sap-integration-test-flow — 원본 디자인 복원.

원본 구조: 각 카드 상단에 모듈 코드(SD/MM/FI) 알약 배지, 그 아래 업무명과
담당 부서. 카드 사이 화살표는 "모듈이 바뀌는 결합 부위"를 강조하기 위해
빨간색으로 통일(본문이 실제로 "이 지점에서 오류가 가장 많이 난다"고 설명하는
의도적 강조이므로 §9 색 사용 원칙의 "포인트에는 원색" 예외로 유지). 화살표
아래 그 의미를 짚어주는 캡션 한 줄, 맨 아래 통합 테스트 체크리스트 박스.

기존 steps() 템플릿(원형 순번 배지)에서는 "모듈 코드가 곧 카드의 정체성"
이라는 원본의 핵심 정보와 빨간 화살표의 의미가 사라지므로 전용 렌더로 되돌린다.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
from brand import *


INTEGRATION_TEST = {
    "ko": dict(
        banner="통합 테스트", sub="모듈이 맞물려 흐르는가",
        headline="주문에서 청구까지, 네 모듈을 넘나드는 하나의 흐름",
        cards=[
            dict(mod="SD", col=MARIGOLD_D, pale=GOLD_PALE, title="판매 오더 등록", dept="영업 담당"),
            dict(mod="PP", col=TEAL, pale=TEAL_PALE, title="생산 오더 처리", dept="생산 담당"),
            dict(mod="MM", col=MARIGOLD_D, pale=GOLD_PALE, title="제품 출고", dept="물류 담당"),
            dict(mod="FI", col=TEAL, pale=TEAL_PALE, title="세금계산서 발행", dept="회계 담당"),
        ],
        arrow_note="빨간 화살표 = 모듈이 바뀌는 '결합 부위' — 오류가 가장 많이 나는 곳",
        note_title="통합 테스트가 보는 세 가지",
        note_items=["모듈 간 연결이 견고한가", "전체 흐름이 끊김 없이 이어지는가", "외부 시스템(WMS·MES)과도 잘 붙는가"],
    ),
    "en": dict(
        banner="Integration testing", sub="do the modules mesh?",
        headline="Order to invoice — one flow crossing four modules",
        cards=[
            dict(mod="SD", col=MARIGOLD_D, pale=GOLD_PALE, title="Sales order", dept="Sales team"),
            dict(mod="PP", col=TEAL, pale=TEAL_PALE, title="Production order", dept="Production team"),
            dict(mod="MM", col=MARIGOLD_D, pale=GOLD_PALE, title="Goods issue", dept="Logistics team"),
            dict(mod="FI", col=TEAL, pale=TEAL_PALE, title="Invoice", dept="Finance team"),
        ],
        arrow_note="Red arrows mark the seams between modules — where errors happen most",
        note_title="What integration testing checks",
        note_items=["Are module connections solid", "Does the flow run without gaps", "Does it mesh with WMS, MES and other systems"],
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


def _integ_test(lang, out):
    t = INTEGRATION_TEST[lang]
    f_mod = font("Bold", 16)
    f_title = font("Bold", 18)
    f_dept = font("Regular", 15)
    f_arrow_note = font("Bold", 15)
    f_note_t = font("Bold", 16)
    f_note_i = font("Medium", 14)

    top = BANNER_H + 96
    n = len(t["cards"])
    gap_x = 34
    card_w = (W - MARGIN * 2 - gap_x * (n - 1)) / n
    card_h = 168
    pill_h = 34

    arrow_note_h = 30
    note_gap = 24

    numerals = ["①", "②", "③"]
    note_line = "   ".join(f"{numerals[i]} {it}" for i, it in enumerate(t["note_items"]))
    tmp_img = Image.new("RGB", (10, 10))
    tmp_d = ImageDraw.Draw(tmp_img)
    note_lines_n = len(_wrap(tmp_d, note_line, f_note_i, W - MARGIN * 2 - 40))
    note_h = 36 + note_lines_n * 22 + 12

    img_h = int(top + card_h + arrow_note_h + note_gap + note_h + 40)
    img, d = new_canvas(img_h)
    draw_banner(d, t["banner"], t["sub"])
    draw_headline(d, BANNER_H + 30, t["headline"])

    bounds = []
    for i, c in enumerate(t["cards"]):
        x0 = MARGIN + i * (card_w + gap_x)
        x1 = x0 + card_w
        cx = (x0 + x1) / 2
        bounds.append((x0, x1))

        d.rounded_rectangle([x0, top, x1, top + card_h], radius=16, fill=WHITE, outline=LINE, width=2)

        pill_w = text_w(d, c["mod"], f_mod) + 30
        py = top + 20
        d.rounded_rectangle([cx - pill_w / 2, py, cx + pill_w / 2, py + pill_h], radius=pill_h / 2, fill=c["col"])
        true_center_text(d, cx, py + pill_h / 2, c["mod"], f_mod, WHITE)

        ty = py + pill_h + 24
        for ln in _wrap(d, c["title"], f_title, card_w - 28):
            center_x_text(d, cx, ty, ln, f_title, INK)
            ty += 24
        ty += 8
        center_x_text(d, cx, ty, c["dept"], f_dept, MUTED)

    # 카드 사이 빨간 화살표 — "모듈이 바뀌는 결합 부위"를 의도적으로 강조
    ay = top + card_h / 2
    for i in range(n - 1):
        span = bounds[i + 1][0] - bounds[i][1]
        gap = max(8, span * 0.22)
        head = max(11, span * 0.34)
        if span - gap * 2 - head < 8:
            head = max(10, span - gap * 2 - 8)
        arrow(d, bounds[i][1] + gap, ay, bounds[i + 1][0] - gap, color=BERRY, width=6, head=int(head))

    arrow_note_y = top + card_h + 14
    center_x_text(d, W / 2, arrow_note_y, "↑ " + t["arrow_note"], f_arrow_note, BERRY)

    ny = arrow_note_y + arrow_note_h + note_gap - 20
    d.rounded_rectangle([MARGIN, ny, W - MARGIN, ny + note_h], radius=14, fill="#e9e6df")
    center_x_text(d, W / 2, ny + 18, t["note_title"], f_note_t, INK)
    lines = _wrap(d, note_line, f_note_i, W - MARGIN * 2 - 40)
    yy = ny + 48
    for ln in lines:
        center_x_text(d, W / 2, yy, ln, f_note_i, MUTED)
        yy += 22

    save(img, out)


BUILDERS = {
    "sap-integration-test-flow": _integ_test,
}
