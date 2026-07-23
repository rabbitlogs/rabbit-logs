# -*- coding: utf-8 -*-
"""
sap-pp-master-data — 원본 구조 복원.

원본 구조: 2x2 그리드. 각 셀은 왼쪽에 작은 색 태그 필("무엇을"/"무엇으로"/
"어떻게"/"어떤 조합으로"), 같은 줄 오른쪽에 큰 키포인트 제목(자재 마스터/
BOM/라우팅/생산버전), 그 아래 본문 설명, 카드 맨 아래에 옅은 노트 칩
(메뉴판의 각 요리/요리의 레시피/조리 순서·동선/레시피+조리법 세트)을 얹는다.
4카드 한 줄(steps)로는 "짝을 이루는 네 가지 기준정보"라는 2x2 대응 관계가
사라지므로 커스텀 그리드로 되돌린다.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brand import *


PP_MASTER = {
    "ko": dict(
        banner="SAP PP 기준정보 핵심 4가지", sub="레스토랑 메뉴 하나가 완성되는 데 필요한 정보들",
        headline="무엇을, 무엇으로, 어떻게, 어떤 조합으로",
        cells=[
            ("무엇을", "자재 마스터", "모든 자재의 기본 정보 · 제품 · 반제품 · 원재료", "메뉴판의 각 요리", MARIGOLD, GOLD_PALE),
            ("무엇으로", "BOM", "제품을 만드는 재료 목록 · 자재 명세서", "요리의 레시피", TEAL, TEAL_PALE),
            ("어떻게", "라우팅", "작업 순서와 공정 경로 · 조리 순서 · 동선", "조리 순서 · 동선", TEAL, TEAL_PALE),
            ("어떤 조합으로", "생산버전", "BOM과 라우팅의 짝 · 레시피 + 조리법 세트", "레시피 + 조리법 세트", MARIGOLD, GOLD_PALE),
        ],
    ),
    "en": dict(
        banner="The four PP master data objects", sub="what one recipe needs to exist",
        headline="What, from what, how, and in which combination",
        cells=[
            ("What", "Material master", "Basic data for every material · finished, semi, raw", "Each dish on the menu", MARIGOLD, GOLD_PALE),
            ("From what", "BOM", "The list of components · the bill of materials", "The recipe itself", TEAL, TEAL_PALE),
            ("How", "Routing", "Operation sequence and path · the cooking order", "The cooking order & path", TEAL, TEAL_PALE),
            ("Which combination", "Production version", "The BOM and routing pair", "Recipe plus method", MARIGOLD, GOLD_PALE),
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


def _pp_master(lang, out):
    t = PP_MASTER[lang]
    f_tag = font("Bold", 14)
    f_key = font("Black", 27)
    f_desc = font("Regular", 15)
    f_note = font("Bold", 14)

    top = BANNER_H + 96
    gap_x, gap_y = 30, 26
    cell_w = (W - MARGIN * 2 - gap_x) / 2
    cell_h = 158

    img_h = int(top + cell_h * 2 + gap_y + 40)
    img, d = new_canvas(img_h)
    draw_banner(d, t["banner"], t["sub"])
    draw_headline(d, BANNER_H + 30, t["headline"])

    for i, (tag, key, desc, note, col, pale) in enumerate(t["cells"]):
        r, c = divmod(i, 2)
        x0 = MARGIN + c * (cell_w + gap_x)
        x1 = x0 + cell_w
        y0 = top + r * (cell_h + gap_y)
        y1 = y0 + cell_h

        d.rounded_rectangle([x0, y0, x1, y1], radius=16, fill=WHITE, outline=LINE, width=2)

        pad = 26
        # 태그 필 (왼쪽) + 큰 키포인트(오른쪽 정렬), 같은 줄
        tag_w = text_w(d, tag, f_tag) + 24
        tag_h = 28
        d.rounded_rectangle([x0 + pad, y0 + 20, x0 + pad + tag_w, y0 + 20 + tag_h],
                            radius=tag_h / 2, fill=pale)
        true_center_text(d, x0 + pad + tag_w / 2, y0 + 20 + tag_h / 2, tag, f_tag, col)

        key_x = x1 - pad
        kw = text_w(d, key, f_key)
        d.text((key_x - kw, y0 + 14), key, font=f_key, fill=col)

        # 본문 설명
        dy = y0 + 20 + tag_h + 16
        for ln in _wrap(d, desc, f_desc, cell_w - pad * 2):
            d.text((x0 + pad, dy), ln, font=f_desc, fill=MUTED)
            dy += 22

        # 하단 노트 칩
        chip_h = 34
        chip_y = y1 - chip_h - 16
        d.rounded_rectangle([x0 + pad, chip_y, x1 - pad, chip_y + chip_h], radius=9, fill=pale)
        true_center_text(d, (x0 + x1) / 2, chip_y + chip_h / 2, note, f_note, col)

    save(img, out)


BUILDERS = {
    "sap-pp-master-data": _pp_master,
}
