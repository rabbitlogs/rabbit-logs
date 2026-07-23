# -*- coding: utf-8 -*-
"""
sap-org-structure-master-data-01 — 전용 렌더(건물 + 가구 합성형).

본문(sap-org-structure.md)을 다시 읽어보면 이 이미지의 alt 텍스트 자체가
"클라이언트·회사코드·플랜트로 이어지는 구조와 그 위에 올라가는 기준정보
4종 레이아웃"이라고 명시한다. 즉 이 도식은 조직 구조 계층 하나만 보여주면
안 되고, 본문의 핵심 비유인 "## 둘의 관계: 건물과 가구"를 그대로 살려
    - 위: 조직 구조 = 건물(계층형, 위로 갈수록 넓게 담는 4단)
    - 아래: 기준정보 = 가구(자재마스터 → BOM, 작업장 → Routing, 생성 순서가
      있는 2개 트랙)
을 한 화면에 함께 보여줘야 한다.

기존 hierarchy() 템플릿은 다른 도식과 공유하므로 건드리지 않고, 이 슬러그
전용으로 완전히 새 레이아웃을 짠다(사용자 승인: "다른 양식 사용해도 됨").
상단 건물 블록은 hierarchy()와 유사한 계층 느낌을 유지하되 2단 텍스트
(굵은 키워드 + 작은 설명)를 쓰고, 하단 가구 블록은 top_bar_card() 기반
카드 4장 + 생성순서 화살표로 표현한다. 중간에는 "그 위에 놓인다"는 관계를
화살표 겸 캡션으로 명시한다.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brand import *

ORG_STRUCTURE = {
    "ko": dict(
        banner="SAP 조직 구조와 기준정보", sub="건물과 그 위에 놓이는 가구",
        headline="건물(조직 구조)이 있어야, 가구(기준정보)를 놓을 수 있습니다",
        building_label="조직 구조 — 레스토랑의 건물 설계도",
        levels=[
            ("클라이언트", "Client", "레스토랑 그룹 전체", "시스템 전체의 가장 큰 단위"),
            ("회사 코드", "Company Code", "강남점 법인", "독립적인 회계 장부 단위"),
            ("플랜트", "Plant", "실제 요리가 이뤄지는 매장", "생산과 재고 관리의 핵심 단위"),
            ("저장 위치", "Storage Location", "냉장 · 상온 창고", "플랜트 안 물리적 보관 장소"),
        ],
        connector="그 위에 놓인다",
        furniture_label="기준정보 — 레스토랑의 레시피와 식재료 목록",
        furniture=[
            dict(title="자재 마스터", eng="Material Master", col=TEAL,
                 desc="식재료 하나하나의 정보 카드"),
            dict(title="BOM", eng="Bill of Materials", col=TEAL,
                 desc="완성품 1개에 들어가는 재료 목록"),
            dict(title="작업장", eng="Work Center", col=MARIGOLD_D,
                 desc="조리가 실제로 이뤄지는 장소"),
            dict(title="Routing", eng="Routing", col=MARIGOLD_D,
                 desc="조리 순서와 소요 시간"),
        ],
        order_note="자재 마스터가 있어야 BOM을, 작업장이 있어야 Routing을 만들 수 있습니다",
        foot="건물 없이 가구를 놓을 수 없듯, 조직 구조 없이 기준정보는 자리 잡지 못합니다",
    ),
    "en": dict(
        banner="SAP organisational structure & master data", sub="the building and the furniture on top",
        headline="You need the building (org structure) before you can add furniture (master data)",
        building_label="Organisational structure — the restaurant's blueprint",
        levels=[
            ("Client", "Client", "The whole restaurant group", "The largest unit in the system"),
            ("Company code", "Company Code", "Gangnam branch entity", "An independent set of books"),
            ("Plant", "Plant", "Where cooking happens", "The core unit for output and stock"),
            ("Storage location", "Storage Location", "Chilled · dry storage", "Physical storage inside the plant"),
        ],
        connector="sits on top of",
        furniture_label="Master data — the restaurant's recipes and ingredient list",
        furniture=[
            dict(title="Material Master", eng="Material Master", col=TEAL,
                 desc="An ID card for each ingredient"),
            dict(title="BOM", eng="Bill of Materials", col=TEAL,
                 desc="The ingredient list for one finished dish"),
            dict(title="Work Center", eng="Work Center", col=MARIGOLD_D,
                 desc="Where the cooking actually happens"),
            dict(title="Routing", eng="Routing", col=MARIGOLD_D,
                 desc="The cooking sequence and timing"),
        ],
        order_note="Material master must exist before BOM; work center must exist before routing",
        foot="No furniture without a building — no master data without an organisational structure",
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


def _org_structure(lang, out):
    t = ORG_STRUCTURE[lang]
    f_section = font("Bold", 16)
    f_title = font("Bold", 20)
    f_eng = font("Medium", 12)
    f_key = font("Bold", 15)
    f_sub = font("Regular", 13)
    f_conn = font("Bold", 15)
    f_ftitle = font("Bold", 17)
    f_feng = font("Medium", 12)
    f_fdesc = font("Regular", 14)
    f_note = font("Medium", 14)
    f_foot = font("Bold", 16)

    top = BANNER_H + 96

    # ── 상단: 건물(조직 구조) — 위로 갈수록 넓은 계층(피라미드를 뒤집은 형태:
    # 클라이언트가 가장 넓게 전체를 담고, 아래로 갈수록 좁아진다) ──
    section_h = 22
    row_h, row_gap = 58, 10
    n_levels = len(t["levels"])
    building_h = section_h + n_levels * (row_h + row_gap) - row_gap

    connector_h = 46

    # ── 하단: 가구(기준정보) 4장, 2트랙(자재마스터→BOM, 작업장→Routing) ──
    furn_section_h = 22
    furn_gap_y = 14
    furn_card_w = (W - MARGIN * 2 - 40 - 20) / 4
    furn_card_h = 108
    furn_h = furn_section_h + furn_gap_y + furn_card_h

    order_note_h = 40
    foot_h = 48
    foot_gap = 20

    img_h = int(top + building_h + connector_h + furn_h + order_note_h + foot_gap + foot_h + 30)
    img, d = new_canvas(img_h)
    draw_banner(d, t["banner"], t["sub"])
    draw_headline(d, BANNER_H + 30, t["headline"])

    # 건물 섹션 라벨
    by = top
    d.text((MARGIN, by), t["building_label"], font=f_section, fill=MUTED)
    by += section_h

    # 삼각형 실루엣(사다리꼴 스택, 좌우 변이 안쪽으로 기울어짐), 캔버스 중앙 배치.
    # title/eng(클라이언트/Client 등)만 도형 안에 넣고, key/sub(설명)는
    # 도형 오른쪽 바깥 여백에 그대로 둔다. 폭은 "글자를 덮을 만큼만" —
    # 맨 위(클라이언트) 라벨 폭 기준으로 pyr_w를 정하고, 맨 아래(저장위치)는
    # 그 비율(bottom_ratio)로 좁히되 라벨이 삐져나오지 않을 최소 폭도 보장한다.
    text_gap = 36                    # 피라미드 오른쪽 설명 텍스트와의 여백
    tmp_img = Image.new("RGB", (10, 10))
    tmp_d = ImageDraw.Draw(tmp_img)
    pad_in = 40
    title_ws = [text_w(tmp_d, lvl[0], f_title) + pad_in for lvl in t["levels"]]
    bottom_ratio = 0.45
    pyr_w = max(title_ws[0], title_ws[-1] / bottom_ratio)
    bottom_w = pyr_w * bottom_ratio
    # 중간 단이 그 위치의 보간 폭보다 라벨이 길면 그만큼 pyr_w를 늘린다.
    for k in range(1, n_levels - 1):
        frac = k / n_levels
        interp = pyr_w - (pyr_w - bottom_w) * frac
        if title_ws[k] > interp:
            pyr_w += (title_ws[k] - interp)
            bottom_w = pyr_w * bottom_ratio
    cx = W / 2
    cols = [TEAL, TEAL_LIGHT, MARIGOLD_D, BERRY]
    level_bottom = by
    for i, (title, eng, key, sub) in enumerate(t["levels"]):
        w_top = pyr_w - (pyr_w - bottom_w) * i / n_levels
        w_bot = pyr_w - (pyr_w - bottom_w) * (i + 1) / n_levels
        y0 = by + i * (row_h + row_gap)
        y1 = y0 + row_h
        col = cols[i % len(cols)]

        d.polygon([
            (cx - w_top / 2, y0), (cx + w_top / 2, y0),
            (cx + w_bot / 2, y1), (cx - w_bot / 2, y1),
        ], fill=col)

        # title — 도형 안, 가운데 정렬(세로 중앙)
        ty = (y0 + y1) / 2
        true_center_text(d, cx, ty, title, f_title, WHITE)

        # key/sub — 도형 오른쪽 바깥 여백에 배치(기존 위치 유지)
        key_x = cx + pyr_w / 2 + text_gap
        d.text((key_x, ty - 24), key, font=f_key, fill=col)
        d.text((key_x, ty - 2), sub, font=f_sub, fill=MUTED)

        if i < n_levels - 1:
            d.line([(cx, y1 + 2), (cx, y1 + row_gap - 2)], fill=LINE, width=2)
        level_bottom = y1

    # ── 연결부: "그 위에 놓인다" — 건물 맨 아래에서 가구 섹션으로 향하는
    # 짧은 수직 화살표 + 캡션. 색은 두 섹션과 구분되도록 MARIGOLD 계열. ──
    cy_conn = level_bottom + connector_h / 2
    conn_x = W / 2
    arrow_top = level_bottom + 8
    arrow_bot = level_bottom + connector_h - 14
    d.line([(conn_x, arrow_top), (conn_x, arrow_bot - 10)], fill=MARIGOLD_D, width=4)
    d.polygon([(conn_x - 8, arrow_bot - 10), (conn_x + 8, arrow_bot - 10), (conn_x, arrow_bot + 4)],
              fill=MARIGOLD_D)
    conn_w = text_w(d, t["connector"], f_conn)
    d.rectangle([conn_x + 16, cy_conn - 11, conn_x + 16 + conn_w + 16, cy_conn + 11], fill=BG)
    d.text((conn_x + 24, cy_conn - 9), t["connector"], font=f_conn, fill=MARIGOLD_D)

    # ── 가구(기준정보) 섹션 ──
    fy = level_bottom + connector_h
    d.text((MARGIN, fy), t["furniture_label"], font=f_section, fill=MUTED)
    fy += furn_section_h + furn_gap_y

    gap_x = 20
    for i, item in enumerate(t["furniture"]):
        x0 = MARGIN + i * (furn_card_w + gap_x)
        x1 = x0 + furn_card_w
        cx = (x0 + x1) / 2
        col = item["col"]
        top_bar_card(d, [x0, fy, x1, fy + furn_card_h], col, radius=13, bar_h=5)

        # title==eng(영문판에서 자재명이 이미 영문)면 중복 줄을 생략한다.
        show_eng = item["title"] != item["eng"]
        ty = fy + (28 if not show_eng else 18)
        for ln in _wrap(d, item["title"], f_ftitle, furn_card_w - 24):
            center_x_text(d, cx, ty, ln, f_ftitle, INK)
            ty += 22
        if show_eng:
            ty += 2
            center_x_text(d, cx, ty, item["eng"], f_feng, col)
            ty += 20
        else:
            ty += 10
        dotted_line(d, x0 + 16, x1 - 16, ty)
        ty += 12
        for ln in _wrap(d, item["desc"], f_fdesc, furn_card_w - 24):
            center_x_text(d, cx, ty, ln, f_fdesc, MUTED)
            ty += 19

    # 트랙 화살표: 자재마스터→BOM(카드0→1), 작업장→Routing(카드2→3).
    # 카드 간격(gap_x=20px)이 좁아 flow_arrow()의 비례 gap/head 계산(26%/30%)이
    # 선을 거의 없애고 화살촉만 남긴다 — 짧은 간격 전용으로 arrow()를 직접
    # 작은 width/head로 호출한다(§8: flow_arrow가 깨지는 짧은 구간의 표준 대응).
    ay = fy + furn_card_h / 2
    x_gap0 = MARGIN + furn_card_w
    x_gap1 = MARGIN + furn_card_w + gap_x
    arrow(d, x_gap0 + 2, ay, x_gap1 - 2, color=MARIGOLD, width=3, head=7)
    x_gap2 = MARGIN + 3 * furn_card_w + 2 * gap_x
    x_gap3 = MARGIN + 3 * furn_card_w + 3 * gap_x
    arrow(d, x_gap2 + 2, ay, x_gap3 - 2, color=MARIGOLD, width=3, head=7)

    # 생성 순서 노트
    ny = fy + furn_card_h + 16
    d.rounded_rectangle([MARGIN, ny, W - MARGIN, ny + order_note_h], radius=11, fill=GOLD_PALE)
    true_center_text(d, W / 2, ny + order_note_h / 2, t["order_note"], f_note, MARIGOLD_D)

    # 하단 요약
    foy = ny + order_note_h + foot_gap
    d.rounded_rectangle([MARGIN, foy, W - MARGIN, foy + foot_h], radius=12, fill=TEAL)
    fw = text_w(d, t["foot"], f_foot)
    if fw > W - MARGIN * 2 - 40:
        lines = _wrap(d, t["foot"], f_foot, W - MARGIN * 2 - 40)
        ly = foy + foot_h / 2 - (len(lines) - 1) * 11
        for ln in lines:
            center_x_text(d, W / 2, ly - 10, ln, f_foot, WHITE)
            ly += 22
    else:
        true_center_text(d, W / 2, foy + foot_h / 2, t["foot"], f_foot, WHITE)

    save(img, out)


BUILDERS = {
    "sap-org-structure-master-data-01": _org_structure,
}
