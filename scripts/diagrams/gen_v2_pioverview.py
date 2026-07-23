# -*- coding: utf-8 -*-
"""
sap-pi-overview-01 — 전면 재설계.

이전 시도(좌우 4단계 세로 카드 + 중앙 화살표)는 duo()의 변형에 가까워
다른 도식들과 인상이 겹쳤다. 이번엔 완전히 다른 구조: 위/아래 두 개의
"가로 타임라인"으로 같은 하루 흐름(주문→전달→재고→마감)을 PI 전/후로
겹쳐 비교한다.

- 위 타임라인(PI 전): 점 4개를 흐릿한 점선으로 연결 — 정보가 끊기는 느낌.
  점 색은 베리, 배경은 거의 무채색에 가까운 옅은 회갈색.
- 아래 타임라인(PI 후): 점 4개를 굵은 실선 화살표로 연결 — 자동으로
  이어지는 느낌. 점 색은 청록.
- 두 타임라인 사이 왼쪽에 큰 "PI" 세로 배지를 두어, "같은 하루가 PI를
  기점으로 다른 흐름이 된다"는 구조를 한눈에 보여준다.
- 맨 아래 요약 문장.

가로 타임라인 형식은 §9 대응표의 "시간 경과 → timeline" 규칙에 맞고,
steps()/duo() 카드형과는 인상이 완전히 다르다.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
from brand import *


PI_OVERVIEW = {
    "ko": dict(
        banner="SAP PI 전후", sub="같은 하루, 다른 흐름",
        before_label="PI 이전 — 끊어진 흐름",
        before=[
            ("주문 메모", "손으로 기록"),
            ("주방 전달", "사람이 이동"),
            ("재고 불명", "실시간 확인 불가"),
            ("수기 정산", "밤마다 집계"),
        ],
        after_label="PI 이후 — 이어진 흐름",
        after=[
            ("POS 입력", "즉시 시스템 반영"),
            ("모니터 표시", "전달 과정 없이 확인"),
            ("재고 갱신", "기준치 이하 자동 발주"),
            ("자동 정산", "버튼 하나로 마감"),
        ],
        foot="같은 SAP, 같은 레스토랑이라도 PI를 거쳤는지가 다른 결과를 만든다",
    ),
    "en": dict(
        banner="Before and after SAP PI", sub="the same day, a different flow",
        before_label="Before PI — a broken chain",
        before=[
            ("Order noted", "Written by hand"),
            ("Sent to kitchen", "Someone walks it over"),
            ("Stock unclear", "No live visibility"),
            ("Manual close", "Tallied every night"),
        ],
        after_label="After PI — a connected chain",
        after=[
            ("POS entry", "Reflected instantly"),
            ("Monitor updates", "Seen with no hand-off"),
            ("Stock refreshes", "Auto-reorders below threshold"),
            ("Auto close-out", "One button ends the day"),
        ],
        foot="Same SAP, same restaurant — going through PI changes the outcome",
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


def _timeline_row(d, x0, x1, cy, points, dot_col, dot_fill, line_style, f_title, f_sub, title_above=True):
    n = len(points)
    step = (x1 - x0) / (n - 1)
    r = 12

    xs = [x0 + i * step for i in range(n)]

    if line_style == "broken":
        for i in range(n - 1):
            seg_x0, seg_x1 = xs[i] + r + 10, xs[i + 1] - r - 12
            x = seg_x0
            while x < seg_x1:
                d.line([(x, cy), (min(x + 6, seg_x1), cy)], fill=LINE, width=3)
                x += 12
            head = 9
            hx = xs[i + 1] - r - 2
            d.polygon([(hx, cy), (hx - head, cy - head * 0.62), (hx - head, cy + head * 0.62)], fill=LINE)
    else:
        for i in range(n - 1):
            arrow(d, xs[i] + r + 8, cy, xs[i + 1] - r - 8, color=dot_col, width=4, head=10)

    label_max_w = 170
    right_edge = W - MARGIN

    for i, (title, sub) in enumerate(points):
        cx = xs[i]
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=dot_fill, outline=dot_col, width=3)

        if title_above:
            ty = cy - r - 46
        else:
            ty = cy + r + 16

        def _place_x(text_width):
            lo = MARGIN
            hi = right_edge - text_width
            return min(max(cx - text_width / 2, lo), hi)

        tw = text_w(d, title, f_title)
        d.text((_place_x(tw), ty), title, font=f_title, fill=INK)
        sub_lines = _wrap(d, sub, f_sub, label_max_w)
        sy = ty + 24 if title_above else ty + 22
        for ln in sub_lines:
            sw = text_w(d, ln, f_sub)
            d.text((_place_x(sw), sy), ln, font=f_sub, fill=MUTED)
            sy += 17


def _pi_overview(lang, out):
    t = PI_OVERVIEW[lang]
    f_row_label = font("Bold", 17)
    f_title = font("Bold", 16)
    f_sub = font("Regular", 13)
    f_foot = font("Bold", 16)

    top = BANNER_H + 54
    foot_gap = 34
    foot_h = 50

    tl_x0 = MARGIN + 10
    tl_x1 = W - MARGIN - 10

    # 두 타임라인을 같은 왼쪽 기준선에서 시작해 좌우 밸런스를 맞춘다.
    # 위: 라벨 → 텍스트 2줄 → 점.  아래: 점 → 텍스트 2줄.  가운데는 넉넉한
    # 여백만 두어 "같은 하루가 갈라진다"는 대비를 보여준다(별도 배지 없이).
    before_label_y = top
    before_cy = before_label_y + 26 + 44 + 20
    after_cy = before_cy + 130
    after_label_y = after_cy - 26 - 20

    img_h = int(after_cy + 70 + foot_gap + foot_h + 30)
    img, d = new_canvas(img_h)
    draw_banner(d, t["banner"], t["sub"])

    # 위 타임라인 — PI 이전(끊어짐)
    d.text((tl_x0, before_label_y), t["before_label"], font=f_row_label, fill=BERRY)
    _timeline_row(d, tl_x0 + 20, tl_x1, before_cy, t["before"], BERRY, WHITE, "broken",
                  f_title, f_sub, title_above=True)

    # 중앙 구분선 — 두 흐름을 가르는 얇은 선 + 화살표 라벨
    mid_y = (before_cy + after_cy) / 2 + 6
    d.line([(MARGIN, mid_y), (W - MARGIN, mid_y)], fill=LINE, width=1)

    # 아래 타임라인 — PI 이후(이어짐)
    d.text((tl_x0, after_label_y), t["after_label"], font=f_row_label, fill=TEAL)
    _timeline_row(d, tl_x0 + 20, tl_x1, after_cy, t["after"], TEAL, TEAL, "solid",
                  f_title, f_sub, title_above=False)

    fy = after_cy + 60 + foot_gap
    d.rounded_rectangle([MARGIN, fy, W - MARGIN, fy + foot_h], radius=12, fill=TEAL)
    true_center_text(d, W / 2, fy + foot_h / 2, t["foot"], f_foot, WHITE)

    save(img, out)


BUILDERS = {
    "sap-pi-overview-01": _pi_overview,
}
