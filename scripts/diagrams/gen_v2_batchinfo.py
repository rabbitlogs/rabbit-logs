# -*- coding: utf-8 -*-
"""
sap-batch-management-01 — 순번/화살표 제거, 3x2 그리드로 전환.

본문(sap-batch-management.md) "배치에 담기는 정보" 섹션은 배치 하나에
담기는 6가지 정보(배치번호·생산일자/플랜트·원자재정보·품질데이터·
유통기한·상태)를 글머리 기호로 병렬 나열할 뿐, 어떤 순서로 진행되는
절차가 아니다. 그런데 steps() 템플릿은 원형 번호 배지(1→2→3→4→5→6)와
카드 사이 화살표를 강제로 그려, "이 순서대로 처리한다"는 잘못된 인상을
준다("숫자가 맞을까? 화살표도 맞을까?"라는 지적이 정확히 이 지점을
짚었다).

그래서 번호도, 화살표도 없는 3x2 카드 그리드로 바꾼다. 각 카드는 색
상단 바 + 제목 + 설명만 담아 "여섯 개를 나란히 놓고 보는 목록"이라는
본문의 실제 구조를 그대로 반영한다.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brand import *


BATCH_MGMT = {
    "ko": dict(banner="배치에 담기는 정보", sub="여섯 가지 핵심 항목",
        headline="배치 하나로 이력 전체를 추적합니다",
        cards=[
            ("배치 번호", ["자재코드+배치번호로", "재고를 특정"]),
            ("생산일자 · 플랜트", ["언제, 어느 공장에서", "만들었는지"]),
            ("원자재 정보", ["어떤 공급업체의", "원자재를 사용했는지"]),
            ("품질 데이터", ["당도 · 수분 · 순도 등", "측정값(특성값)"]),
            ("유통기한", ["유통기한 또는", "최소 보관 기간"]),
            ("상태", ["사용가능 · 검사중 ·", "잠금 여부"]),
        ]),
    "en": dict(banner="What a batch records", sub="six essential fields",
        headline="One batch number traces the entire history",
        cards=[
            ("Batch number", ["Material code plus batch", "pinpoints the stock"]),
            ("Date · plant", ["When and at which", "plant it was made"]),
            ("Raw material", ["Which supplier's", "materials went in"]),
            ("Quality data", ["Measured values such as", "sugar, moisture, purity"]),
            ("Shelf life", ["Expiry date or the", "minimum storage period"]),
            ("Status", ["Unrestricted, inspection,", "or blocked"]),
        ]),
}

COLORS = [TEAL, MARIGOLD_D, BERRY, TEAL, MARIGOLD_D, BERRY]


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


def _batch_info(lang, out):
    t = BATCH_MGMT[lang]
    f_title = font("Bold", 19)
    f_body = font("Regular", 15)

    cols, rows = 3, 2
    gap_x, gap_y = 26, 24
    card_w = (W - MARGIN * 2 - gap_x * (cols - 1)) / cols
    card_h = 128
    bar_h = 6

    top = BANNER_H + 96
    grid_h = rows * card_h + (rows - 1) * gap_y

    img_h = int(top + grid_h + 40)
    img, d = new_canvas(img_h)
    draw_banner(d, t["banner"], t["sub"])
    draw_headline(d, BANNER_H + 30, t["headline"])

    for i, (title, body) in enumerate(t["cards"]):
        r, c = divmod(i, cols)
        x0 = MARGIN + c * (card_w + gap_x)
        x1 = x0 + card_w
        y0 = top + r * (card_h + gap_y)
        y1 = y0 + card_h
        cx = (x0 + x1) / 2
        col = COLORS[i % len(COLORS)]

        top_bar_card(d, [x0, y0, x1, y1], col, radius=14, bar_h=bar_h)

        ty = y0 + 24
        for ln in _wrap(d, title, f_title, card_w - 32):
            center_x_text(d, cx, ty, ln, f_title, INK)
            ty += 26
        ty += 10
        for ln in body:
            center_x_text(d, cx, ty, ln, f_body, MUTED)
            ty += 22

    save(img, out)


BUILDERS = {
    "sap-batch-management-01": _batch_info,
}
