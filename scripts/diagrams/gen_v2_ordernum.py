# -*- coding: utf-8 -*-
"""
sap-production-order-number-01 — 전면 재설계(번호선 형태).

이전 두 시도(좌우 카드 비교, 포함 박스)를 모두 버리고, "번호는 하나의
연속된 줄 위에서 절대 겹치지 않는 구간을 나눠 쓴다"는 사실 자체를
숫자 눈금자(number line) 하나로 표현한다. 헤드라인/부제는 AUFK·AUFNR·
BUKRS·WERKS 같은 테이블/필드명을 노출하지 않고 "번호 하나로 구분한다",
"회사·공장은 참고용일 뿐"처럼 초보자 눈높이 문장으로 푼다(이 글은
level: beginner이고 본문이 은행 대기표·레스토랑 예약 번호 비유로 쉽게
설명하므로, 이미지만 DB 용어로 딱딱해지면 톤이 어긋난다). 가운데 굵은
가로 막대에 A 공장 구간(마리골드)과 B 공장 구간(베리)을 나란히 칠해
겹치지 않는 두 범위를 보여준다. 각 구간 위/아래에 시작 번호와 공장명을
배치하고, 맨 아래 요약 문장.

카드+테두리 방식은 이미 다른 도식(sap-pp-master-data, sap-wip-overview
등)에서 여러 번 쓰였으므로, 이 도식만큼은 "번호 구간"이라는 소재에 맞는
눈금자 은유로 차별화한다.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brand import *


def _factory_icon(d, cx, top_y, size, col):
    """
    간단한 공장 실루엣 — 톱니 지붕 건물 + 굴뚝 + 연기 두 점.
    사진이 아닌 브랜드 색 단색 아이콘으로, 라벨 위에 작게 얹어 "공장"이라는
    맥락을 시각적으로 보태되 도식 전체의 절제된 톤을 벗어나지 않게 한다.
    """
    w = size
    h = size * 0.62
    x0 = cx - w / 2
    y1 = top_y + h
    y0 = top_y

    # 몸체
    d.rectangle([x0, y0 + h * 0.35, x0 + w, y1], fill=col)
    # 톱니 지붕(삼각 파형 3개)
    teeth = 3
    tw = w / teeth
    for i in range(teeth):
        tx0 = x0 + i * tw
        d.polygon([
            (tx0, y0 + h * 0.35),
            (tx0 + tw / 2, y0),
            (tx0 + tw, y0 + h * 0.35),
        ], fill=col)
    # 굴뚝
    chim_w = w * 0.12
    chim_x = x0 + w * 0.72
    d.rectangle([chim_x, y0 - h * 0.28, chim_x + chim_w, y0 + h * 0.15], fill=col)
    # 연기(작은 점 두 개)
    r = chim_w * 0.42
    d.ellipse([chim_x + chim_w / 2 - r, y0 - h * 0.5 - r,
               chim_x + chim_w / 2 + r, y0 - h * 0.5 + r], fill=col)
    d.ellipse([chim_x + chim_w / 2 - r * 0.8 + 3, y0 - h * 0.7 - r * 0.8,
               chim_x + chim_w / 2 + r * 0.8 + 3, y0 - h * 0.7 + r * 0.8], fill=col)
    return h + h * 0.5  # 아이콘이 차지하는 세로 높이(연기 포함) 근사치


ORDER_NUMBER = {
    "ko": dict(
        banner="생산오더 번호 구조", sub="클라이언트 단위 고유성",
        headline="오더를 구분하는 건 오직 '번호' 하나뿐",
        key_note="어느 회사·어느 공장인지는 참고용일 뿐, 번호가 겹치면 안 된다",
        ranges=[
            dict(label="A 공장", start="10000001, 10000002 …", col=MARIGOLD_D, pale=GOLD_PALE),
            dict(label="B 공장", start="20000001, 20000002 …", col=BERRY, pale=BERRY_PALE),
        ],
        range_note="번호가 겹치지 않도록, 공장마다 처음부터 다른 번호대를 쓴다",
        foot="같은 시스템 안에서는 회사·공장이 달라도 오더 번호가 절대 겹치지 않습니다",
    ),
    "en": dict(
        banner="Production order numbering", sub="unique across the client",
        headline="Just one thing tells orders apart: the number",
        key_note="Which company or plant it's from is just a label — the number itself must never repeat",
        ranges=[
            dict(label="Plant A", start="10000001, 10000002 …", col=MARIGOLD_D, pale=GOLD_PALE),
            dict(label="Plant B", start="20000001, 20000002 …", col=BERRY, pale=BERRY_PALE),
        ],
        range_note="Each plant starts from a different range from day one, so numbers never overlap",
        foot="Within the same system, order numbers never collide — even across companies or plants",
    ),
}


def _order_number(lang, out):
    t = ORDER_NUMBER[lang]
    f_key_note = font("Medium", 15)
    f_label = font("Bold", 19)
    f_start = font("Bold", 15)
    f_range_note = font("Regular", 14)
    f_foot = font("Bold", 16)

    top = BANNER_H + 44
    headline_h = 34
    key_note_gap = 14
    key_note_h = 22
    ruler_gap = 96   # key_note 아래 ~ 막대 사이. 이 구간 안에 아이콘+라벨이 들어간다

    bar_h = 56
    icon_size = 34
    icon_gap = 8
    bar_y_gap_label = 34 + icon_size + icon_gap   # 막대 위: 아이콘 + 라벨 공간
    bar_y_gap_num = 32     # 막대 아래 보충 설명 공간

    foot_gap = 26
    foot_h = 48

    ruler_top = top + headline_h + key_note_gap + key_note_h + ruler_gap
    bar_y0 = ruler_top
    bar_y1 = bar_y0 + bar_h

    img_h = int(bar_y1 + bar_y_gap_num + foot_gap + foot_h + 30)
    img, d = new_canvas(img_h)
    draw_banner(d, t["banner"], t["sub"])
    draw_headline(d, BANNER_H + 30, t["headline"])

    ky = BANNER_H + 30 + headline_h + key_note_gap
    center_x_text(d, W / 2, ky, t["key_note"], f_key_note, MUTED)

    # 번호선(눈금자) — 연속된 하나의 막대를 구간별로 색칠
    n = len(t["ranges"])
    seg_w = (W - MARGIN * 2) / n

    d.rounded_rectangle([MARGIN, bar_y0, W - MARGIN, bar_y1], radius=10, fill="#efe9dc")

    for i, r in enumerate(t["ranges"]):
        x0 = MARGIN + i * seg_w
        x1 = x0 + seg_w
        cx = (x0 + x1) / 2

        # 구간 채우기(첫/끝 구간만 바깥쪽 모서리를 둥글게)
        if i == 0:
            d.rounded_rectangle([x0, bar_y0, x1, bar_y1], radius=10, fill=r["col"])
            d.rectangle([x1 - 10, bar_y0, x1, bar_y1], fill=r["col"])
        elif i == n - 1:
            d.rounded_rectangle([x0, bar_y0, x1, bar_y1], radius=10, fill=r["col"])
            d.rectangle([x0, bar_y0, x0 + 10, bar_y1], fill=r["col"])
        else:
            d.rectangle([x0, bar_y0, x1, bar_y1], fill=r["col"])

        # 공장 아이콘 + 라벨(막대 위)
        icon_top = bar_y0 - bar_y_gap_label
        _factory_icon(d, cx, icon_top, icon_size, r["col"])
        ly = bar_y0 - 34
        center_x_text(d, cx, ly, r["label"], f_label, r["col"])

        # 번호 예시(막대 안)
        true_center_text(d, cx, (bar_y0 + bar_y1) / 2, r["start"], f_start, WHITE)

        # 경계 마커(다음 공장 시작 지점) — 첫 구간이 아닐 때만
        if i > 0:
            d.line([(x0, bar_y0 - 8), (x0, bar_y1 + 8)], fill=BG, width=3)

    ny = bar_y1 + 18
    center_x_text(d, W / 2, ny, t["range_note"], f_range_note, MUTED)

    fy = bar_y1 + bar_y_gap_num + foot_gap
    d.rounded_rectangle([MARGIN, fy, W - MARGIN, fy + foot_h], radius=12, fill=TEAL)
    true_center_text(d, W / 2, fy + foot_h / 2, t["foot"], f_foot, WHITE)

    save(img, out)


BUILDERS = {
    "sap-production-order-number-01": _order_number,
}
