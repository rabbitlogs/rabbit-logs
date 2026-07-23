# -*- coding: utf-8 -*-
"""
sap-data-types-01 — 원본 구조 복원(2카드 합류 → 1카드) + 빅 키포인트 스타일 통일.

원본 구조: 상단에 컨피규레이션/마스터 데이터 2카드를 나란히 놓고, 두 대각선
화살표가 아래 트랜잭션 데이터 카드로 모인다("두 종류의 기준이 모여 매일의
기록을 만든다"는 합류 관계). steps()의 좌우 화살표로는 이 합류 구조를
표현할 수 없어 커스텀 렌더가 필요하다. 카드 내부는 fit-gap-ways/mes-interface
에서 통일한 빅 키포인트 스타일(헤더 태그 + 큰 제목 + 본문 + 하단 note 칩)로 맞춘다.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
from brand import *


DATA_TYPES = {
    "ko": dict(
        banner="SAP 데이터 유형 세 가지", sub="운영 규칙과 기준표가 모여, 매일의 기록을 만든다",
        headline="컨피규레이션 · 마스터 데이터 · 트랜잭션 데이터",
        top=[
            dict(tag="컨피규레이션", col=MARIGOLD_D, pale=GOLD_PALE,
                 key="매장 운영 규칙",
                 body=["주문번호 부여 방식 · 재고 전략", "MTO / MTS 생산 방식"],
                 note="변경 거의 없음 · 초기 세팅"),
            dict(tag="마스터 데이터", col=TEAL, pale=TEAL_PALE,
                 key="식자재 기준표",
                 body=["자재 마스터 · BOM(레시피)", "고객 · 공급처 정보"],
                 note="변경 낮음 · 필요시만"),
        ],
        bottom=dict(tag="트랜잭션 데이터", col=INK, pale="#e9e6df",
                     key="그날의 주문 · 영수증",
                     body=["판매오더 → 출고지시 → 출고전표 → 매출전표"],
                     note="변경 매우 높음 · 실시간 발생"),
    ),
    "en": dict(
        banner="Three kinds of SAP data", sub="rules and reference tables shape the daily record",
        headline="Configuration · master data · transaction data",
        top=[
            dict(tag="Configuration", col=MARIGOLD_D, pale=GOLD_PALE,
                 key="Restaurant rules",
                 body=["How order numbers are assigned · stock strategy", "MTO / MTS production style"],
                 note="Rarely changes — set up once"),
            dict(tag="Master data", col=TEAL, pale=TEAL_PALE,
                 key="Ingredient reference",
                 body=["Material master · BOM (recipe)", "Customer and supplier info"],
                 note="Changes seldom, only as needed"),
        ],
        bottom=dict(tag="Transaction data", col=INK, pale="#e9e6df",
                     key="Today's orders and receipts",
                     body=["Sales order → delivery → goods issue → invoice"],
                     note="Changes constantly, in real time"),
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
    """실제 줄바꿈 후 총 줄 수 — 카드 높이를 여기서 역산해야 영문처럼 줄이 늘어도 note와 안 겹친다."""
    n = 0
    for ln in spec["body"]:
        n += len(_wrap(d, ln, f_body, card_w - 48))
    return n


def _card(d, box, spec, f_tag, f_key, f_body, f_note, head_h):
    x0, y0, x1, y1 = box
    col, pale = spec["col"], spec["pale"]

    d.rounded_rectangle(box, radius=16, fill=WHITE, outline=LINE, width=2)
    d.rounded_rectangle([x0, y0, x1, y0 + head_h], radius=16, fill=col)
    d.rectangle([x0, y0 + head_h - 16, x1, y0 + head_h], fill=col)
    cx = (x0 + x1) / 2
    true_center_text(d, cx, y0 + head_h / 2, spec["tag"], f_tag, WHITE)

    ky = y0 + head_h + 22
    center_x_text(d, cx, ky, spec["key"], f_key, col)
    _, k0, _, k1 = d.textbbox((0, 0), spec["key"], font=f_key)
    by = ky + (k1 - k0) + 16

    for ln in spec["body"]:
        for wln in _wrap(d, ln, f_body, (x1 - x0) - 48):
            center_x_text(d, cx, by, wln, f_body, MUTED)
            by += 22

    note_h = 34
    note_y = y1 - note_h - 16
    d.rounded_rectangle([x0 + 24, note_y, x1 - 24, note_y + note_h], radius=9, fill=pale)
    true_center_text(d, cx, note_y + note_h / 2, spec["note"], font("Bold", 14), col)


def _elbow_arrow(d, x0, y0, x1, y1, color=ARROW, width=3):
    """
    꺾인(ㄴ자) 합류 커넥터 — 상단 카드 하단 중앙에서 수직으로 내려오다가,
    중간 높이에서 꺾여 하단 카드 목표 x로 이동한 뒤 다시 수직으로 내려와
    화살표 머리로 마무리한다. 대각선보다 "합류 경로"라는 관계가 분명해진다.
    """
    gap = 10
    mid_y = y0 + (y1 - y0) * 0.55   # 꺾이는 지점 — 시작 쪽에 가깝게 둬 세로 구간을 짧게
    head = 11

    # 1) 시작점(카드 하단)에서 살짝 gap을 두고 수직으로 내려온다
    sy = y0 + gap
    d.line([(x0, sy), (x0, mid_y)], fill=color, width=width)
    # 2) 수평으로 꺾여 목표 x까지 이동한다
    d.line([(x0, mid_y), (x1, mid_y)], fill=color, width=width)
    # 3) 목표 x에서 수직으로 내려와 화살표 머리 직전까지
    ey = y1 - gap - head
    d.line([(x1, mid_y), (x1, ey)], fill=color, width=width)
    # 화살표 머리(아래 방향)
    d.polygon([(x1, ey + head), (x1 - head * 0.62, ey), (x1 + head * 0.62, ey)], fill=color)


def _data_types(lang, out):
    t = DATA_TYPES[lang]
    f_tag = font("Bold", 19)
    f_key = font("Black", 27)
    f_body = font("Regular", 15)
    f_note = font("Bold", 14)

    top = BANNER_H + 96
    gap_x = 40
    card_w = (W - MARGIN * 2 - gap_x) / 2
    head_h = 52
    gap_y = 78  # 꺾인 커넥터(수직·수평·수직)가 지나갈 공간
    bottom_w = card_w * 1.35

    # 카드 높이는 실제 콘텐츠(태그행 + 큰 키포인트 + 본문 줄 수 + note)로 역산한다.
    # 고정값을 쓰면 영문처럼 줄바꿈이 늘어난 언어에서 본문이 note 칩과 겹친다.
    tmp_img = Image.new("RGB", (10, 10))
    tmp_d = ImageDraw.Draw(tmp_img)

    def _card_h(spec, width):
        key_h = 27 + 8   # Black 27px 키포인트 대략 높이 + 여유
        body_lines = _card_body_lines(tmp_d, spec, f_body, width)
        body_h = body_lines * 22
        return head_h + 22 + key_h + 16 + body_h + 16 + 34 + 16 + 14  # 태그+간격+키+간격+본문+간격+note+하단여백

    top_card_h = max(_card_h(spec, card_w) for spec in t["top"])
    bottom_h = _card_h(t["bottom"], bottom_w)

    top_y = top
    bottom_y = top_y + top_card_h + gap_y

    img_h = int(bottom_y + bottom_h + 40)
    img, d = new_canvas(img_h)
    draw_banner(d, t["banner"], t["sub"])
    draw_headline(d, BANNER_H + 30, t["headline"])

    boxes = []
    for i, spec in enumerate(t["top"]):
        x0 = MARGIN + i * (card_w + gap_x)
        x1 = x0 + card_w
        boxes.append((x0, top_y, x1, top_y + top_card_h))
        _card(d, (x0, top_y, x1, top_y + top_card_h), spec, f_tag, f_key, f_body, f_note, head_h)

    bx0 = (W - bottom_w) / 2
    bx1 = bx0 + bottom_w
    _card(d, (bx0, bottom_y, bx1, bottom_y + bottom_h), t["bottom"], f_tag, f_key, f_body, f_note, head_h)

    # 꺾인 합류 커넥터 — 각 상단 카드 하단 중앙 → 수직·수평·수직으로 꺾여 하단 카드 상단, 좌우로 벌려 도착
    bcx = (bx0 + bx1) / 2
    for i, (x0, y0, x1, y1) in enumerate(boxes):
        cx = (x0 + x1) / 2
        target_x = bcx + (-1 if i == 0 else 1) * (bottom_w * 0.18)
        _elbow_arrow(d, cx, y1, target_x, bottom_y)

    save(img, out)


BUILDERS = {
    "sap-data-types-01": _data_types,
}
