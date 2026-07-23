# -*- coding: utf-8 -*-
"""
sap-mes-role-01 — 원본 디자인 복원.

원본 구조: 좌측 SAP(청록 헤더) / 우측 MES(마리골드 헤더) 두 카드가 나란히
서고, 그 사이 중앙 열에 위쪽 "① 작업 지시"(SAP→MES, 청록 화살표)와
아래쪽 "③ 실적 보고"(MES→SAP, 마리골드 화살표) 두 개의 반대 방향 화살표가
있다. 각 카드 안은 4개 항목이 세로 막대(아이콘 대용) + 굵은 제목 + 설명
한 줄로 나열되고, 항목 사이는 점선으로 구분된다. 카드 맨 아래 "시간 단위"
한 줄과 그 아래 옅은 알약 태그 3개, 전체 맨 아래 한 줄 요약 캡션.

본문(sap-mes-role.md) "협업 4단계"가 실제로는 SAP→MES(작업 지시) 뒤에
MES 내부 두 단계(생산 실행/모니터링), 그리고 MES→SAP(실적 보고) 뒤에
SAP 내부 분석 단계로 이어지는 왕복 흐름이라, duo()의 단순 좌우 비교로는
이 "주고받는 대화" 구조가 사라진다. 전용 렌더로 되돌려 중앙 화살표 두
개로 그 왕복을 표현한다.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
from brand import *


MES_ROLE = {
    "ko": dict(
        banner="SAP MES", sub="총괄 셰프(SAP)와 주방 팀(MES)의 역할 분담",
        left=dict(title="SAP (ERP)", sub="총괄 셰프 | 계획의 중심", col=TEAL, pale=TEAL_PALE,
            items=[
                ("생산오더 생성", "\"무엇을, 얼마나, 언제\" 만들지 공식 지시"),
                ("BOM · Routing 관리", "레시피(BOM)와 조리 순서(Routing) 정의"),
                ("자재 소요량 계획 (MRP)", "필요 식자재 수량 계산, 부족분 구매 지시"),
                ("원가 분석 · 정산", "계획 vs 실제 원가 비교, 재무 반영"),
            ],
            time="시간 단위: 월 / 주 / 일", tags=["계획", "관리", "분석"]),
        right=dict(title="MES", sub="주방 팀 | 실행의 중심", col=MARIGOLD_D, pale=GOLD_PALE,
            items=[
                ("실시간 생산 실행 · 추적", "완료 수량을 초 단위로 카운트, WIP 추적"),
                ("설비 상태 모니터링", "그릴 온도 · 라인 상태 실시간 감시"),
                ("품질 · 불량 관리", "기준 미달 즉시 처리, 로트 단위 추적"),
                ("자재 실사용량 추적", "어느 자재가 어느 제품에 얼마나 투입됐는지"),
            ],
            time="시간 단위: 분 / 초 (실시간)", tags=["실행", "현장", "실시간"]),
        arrow_up="① 작업 지시", arrow_up_sub="생산오더 전달",
        arrow_down="③ 실적 보고", arrow_down_sub="완료 · 불량 · 자재",
        foot="SAP(계획) ↔ MES(실행) — 두 시스템이 유기적으로 맞물릴 때 스마트 팩토리의 기반이 갖춰진다",
    ),
    "en": dict(
        banner="SAP MES", sub="how the head chef (SAP) and kitchen team (MES) split the work",
        left=dict(title="SAP (ERP)", sub="Head chef | the planning centre", col=TEAL, pale=TEAL_PALE,
            items=[
                ("Creates production orders", "Formal instructions for what, how much, when"),
                ("Manages BOM and routing", "Defines the recipe (BOM) and cooking sequence (routing)"),
                ("Material requirements planning (MRP)", "Calculates needed quantities, flags shortfalls to buy"),
                ("Cost analysis and settlement", "Compares plan vs. actual cost, feeds into finance"),
            ],
            time="Time unit: month / week / day", tags=["Plan", "Manage", "Analyze"]),
        right=dict(title="MES", sub="Kitchen team | the execution centre", col=MARIGOLD_D, pale=GOLD_PALE,
            items=[
                ("Real-time execution & tracking", "Counts completed units by the second, tracks WIP"),
                ("Equipment monitoring", "Watches grill temperature and line status live"),
                ("Quality & defect management", "Handles misses immediately, tracks by lot"),
                ("Actual material consumption", "Tracks which material went into which product, how much"),
            ],
            time="Time unit: minute / second (real time)", tags=["Execute", "On the floor", "Real time"]),
        arrow_up="① Work instruction", arrow_up_sub="Production order sent",
        arrow_down="③ Results reported", arrow_down_sub="Completed · defects · material",
        foot="SAP (plan) ↔ MES (execution) — when the two systems mesh, that's the foundation of a smart factory",
    ),
}


def _arrow_left(d, x0, y, x1, color=ARROW, width=5, head=11):
    """오른쪽→왼쪽 수평 화살표. arrow()의 좌우 반전판(brand.arrow는 좌→우 전용)."""
    d.line([(x0, y), (x1 + head, y)], fill=color, width=width)
    d.polygon([(x1, y), (x1 + head, y - head * 0.62), (x1 + head, y + head * 0.62)], fill=color)


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


def _mes_role(lang, out):
    t = MES_ROLE[lang]
    f_htitle = font("Bold", 20)
    f_hsub = font("Medium", 13)
    f_item_t = font("Bold", 15)
    f_item_d = font("Regular", 13)
    f_time = font("Bold", 14)
    f_tag = font("Bold", 13)
    f_arrow = font("Bold", 14)
    f_arrow_sub = font("Regular", 12)
    f_foot = font("Regular", 14)

    gap_x = 34
    mid_w = 140
    card_w = (W - MARGIN * 2 - gap_x * 2 - mid_w) / 2
    head_h = 56
    pad = 22

    # 항목 줄 수(설명 wrap 포함) 미리 측정해 카드 높이를 동적으로 계산
    tmp_img = Image.new("RGB", (10, 10))
    tmp_d = ImageDraw.Draw(tmp_img)

    def items_h(items):
        y = 0
        for title, desc in items:
            y += 22  # 제목
            desc_lines = _wrap(tmp_d, desc, f_item_d, card_w - pad * 2 - 14)
            y += len(desc_lines) * 19
            y += 26  # 항목 간 여백 + 구분선
        return y

    body_h = max(items_h(t["left"]["items"]), items_h(t["right"]["items"]))
    time_block_h = 34 + 40  # 시간 단위 줄 + 태그 알약
    card_h = head_h + pad + body_h + time_block_h

    top = BANNER_H + 44
    foot_h = 40

    img_h = int(top + card_h + foot_h + 30)
    img, d = new_canvas(img_h)

    # §8 공통 규칙: 모든 도식은 draw_banner()의 청록 그라데이션 배너를 쓴다.
    draw_banner(d, t["banner"], t["sub"])

    lx0 = MARGIN
    lx1 = lx0 + card_w
    rx0 = lx1 + gap_x + mid_w + gap_x
    rx1 = rx0 + card_w
    y0 = top
    y1 = top + card_h

    for (x0, x1), spec in [((lx0, lx1), t["left"]), ((rx0, rx1), t["right"])]:
        col, pale = spec["col"], spec["pale"]
        d.rounded_rectangle([x0, y0, x1, y1], radius=14, fill=pale, outline=col, width=2)
        d.rounded_rectangle([x0, y0, x1, y0 + head_h], radius=14, fill=col)
        d.rectangle([x0, y0 + head_h - 14, x1, y0 + head_h], fill=col)
        center_x_text(d, (x0 + x1) / 2, y0 + 12, spec["title"], f_htitle, WHITE)
        center_x_text(d, (x0 + x1) / 2, y0 + 38, spec["sub"], f_hsub, "#eef4f2")

        iy = y0 + head_h + pad
        for i, (title, desc) in enumerate(spec["items"]):
            d.rectangle([x0 + pad, iy + 2, x0 + pad + 4, iy + 16], fill=col)
            d.text((x0 + pad + 14, iy), title, font=f_item_t, fill=INK)
            iy += 22
            for ln in _wrap(d, desc, f_item_d, card_w - pad * 2 - 14):
                d.text((x0 + pad + 14, iy), ln, font=f_item_d, fill=MUTED)
                iy += 19
            iy += 12
            if i < len(spec["items"]) - 1:
                dotted_line(d, x0 + pad, x1 - pad, iy)
            iy += 14

        ty = y1 - time_block_h + 8
        center_x_text(d, (x0 + x1) / 2, ty, spec["time"], f_time, col)
        ty += 26
        tx = x0 + pad
        for tag in spec["tags"]:
            tw = text_w(d, tag, f_tag) + 22
            th = 26
            d.rounded_rectangle([tx, ty, tx + tw, ty + th], radius=th / 2, fill=WHITE, outline=col, width=1)
            true_center_text(d, tx + tw / 2, ty + th / 2, tag, f_tag, col)
            tx += tw + 10

    # 중앙 화살표 2개(왕복) — SAP→MES(작업 지시, 위), MES→SAP(실적 보고, 아래)
    mx0 = lx1 + gap_x
    mx1 = mx0 + mid_w
    mcx = (mx0 + mx1) / 2

    ay1_c = y0 + head_h + pad + 40
    d.rounded_rectangle([mx0, ay1_c - 30, mx1, ay1_c - 8], radius=8, fill="#f4f0e8")
    center_x_text(d, mcx, ay1_c - 27, t["arrow_up"], f_arrow, TEAL)
    arrow(d, mx0 + 6, ay1_c + 16, mx1 - 6, color=TEAL, width=6, head=14)
    center_x_text(d, mcx, ay1_c + 24, t["arrow_up_sub"], f_arrow_sub, MUTED)

    ay2_c = y0 + card_h - time_block_h - 30
    d.rounded_rectangle([mx0, ay2_c - 30, mx1, ay2_c - 8], radius=8, fill="#f4ede0")
    center_x_text(d, mcx, ay2_c - 27, t["arrow_down"], f_arrow, MARIGOLD_D)
    _arrow_left(d, mx1 - 6, ay2_c + 16, mx0 + 6, color=MARIGOLD_D, width=6, head=14)
    center_x_text(d, mcx, ay2_c + 24, t["arrow_down_sub"], f_arrow_sub, MUTED)

    fy = y1 + 22
    center_x_text(d, W / 2, fy, t["foot"], f_foot, MUTED)

    save(img, out)


BUILDERS = {
    "sap-mes-role-01": _mes_role,
}
