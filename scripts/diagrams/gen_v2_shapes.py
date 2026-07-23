# -*- coding: utf-8 -*-
"""
v2 — 본문 내용에 맞춰 카드형이 아닌 형태를 배정한 도식들.

배정 근거는 각 도식 위 주석에 적었다(§9 관계→형태 대응표 기준).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brand import *
from shapes import curve, cycle, hierarchy, hub, timeline, quadrant

# ── 변화 저항 곡선 → 곡선형 ────────────────────────────────────────────────
# 본문: "생산성이 가장 떨어지는 시기" = 값의 오르내림이 내용의 핵심. 카드로 펴면 손실.
CHANGE = {
    "ko": dict(banner="변화 저항 곡선", sub="네 단계를 거쳐 새 시스템에 정착",
        headline="누구나 겪는 감정의 흐름, 알면 덜 힘듭니다", ylabel="생산성",
        points=[("충격 · 부정", "\"왜 바꾸나요, 기존이 편한데요\"", 0.72),
                ("분노 · 좌절", "생산성 최저점 — \"왜 이렇게 느려요\"", 0.12),
                ("탐색 · 수용", "작은 성공 경험 — \"한번 써봐야겠다\"", 0.52),
                ("통합", "\"이제 이게 편해요\" 완전히 자리잡음", 0.93)]),
    "en": dict(banner="The change resistance curve", sub="four stages to settling in",
        headline="Everyone goes through it — knowing helps", ylabel="Productivity",
        points=[("Shock · denial", "\"Why change? The old way was fine\"", 0.72),
                ("Anger · frustration", "Productivity bottoms out — \"Why so slow?\"", 0.12),
                ("Exploration", "Small wins — \"Maybe I'll try it properly\"", 0.52),
                ("Integration", "\"This is easier now\" — fully settled", 0.93)]),
}

# ── 순환 BOM → 순환형 ──────────────────────────────────────────────────────
# 본문: "A가 B를 부르고 B가 다시 A를" = 되돌아옴 자체가 주제. 직선 카드로는 표현 불가.
CIRCULAR = {
    "ko": dict(banner="순환 BOM", sub="레시피가 자기를 다시 부르는 구조",
        headline="완성품이 재작업을 거쳐 다시 완성품이 되는 고리",
        loop="다시 완성품으로",
        nodes=[("완성품", ["정상 생산된 제품", "일부가 불량 판정"]),
               ("불량품", ["재작업 공정에", "투입 자재로 들어간다"]),
               ("재작업 공정", ["고쳐서 다시", "완성품을 만든다"])],
        note="'순환 허용' 체크가 없으면 MRP가 무한루프로 판단해 멈춘다"),
    "en": dict(banner="Circular BOMs", sub="when a recipe calls itself",
        headline="The loop where a finished good becomes a finished good again",
        loop="back to finished goods",
        nodes=[("Finished good", ["Produced normally,", "some judged defective"]),
               ("Defective unit", ["Goes in as an input", "to the rework operation"]),
               ("Rework operation", ["Repairs it and produces", "a finished good again"])],
        note="Without 'allow circularity', MRP reads this as an infinite loop and stops"),
}

# ── 조직 구조 → 계층형 ─────────────────────────────────────────────────────
# 본문: "위에서 아래로, 담는 범위가 점점 좁아집니다" = 포함 관계. 나열이 아님.
ORG = {
    "ko": dict(banner="SAP 조직 구조", sub="건물 설계도의 네 단계",
        headline="위에서 아래로, 담는 범위가 점점 좁아집니다",
        levels=[("클라이언트", "Client", "레스토랑 그룹 전체 · 시스템의 최상위 단위"),
                ("회사 코드", "Company Code", "독립적인 회계 장부 단위 · 강남점 법인"),
                ("플랜트", "Plant", "실제 요리가 이뤄지는 매장 · 생산과 재고의 핵심"),
                ("저장 위치", "Storage Location", "냉장 창고 · 상온 창고 · 플랜트 안 보관 장소")],
        note="플랜트는 SAP에서 가장 자주 마주치는 단위 — 먼저 내 플랜트를 파악하세요"),
    "en": dict(banner="SAP organisational structure", sub="four levels of the blueprint",
        headline="Top to bottom, each level narrows what it holds",
        levels=[("Client", "Client", "The whole restaurant group · the top of the system"),
                ("Company code", "Company Code", "An independent set of books · one legal entity"),
                ("Plant", "Plant", "Where cooking happens · the core of output and stock"),
                ("Storage location", "Storage Location", "Chilled or dry store inside the plant")],
        note="Plant is the unit you meet most often in SAP — learn yours first"),
}

# ── WIP 세 관점 → 허브형 ───────────────────────────────────────────────────
# 본문: "같은 WIP를 세 사람이 다르게 본다" = 중심 하나에 여럿이 연결.
WIP = {
    "ko": dict(banner="WIP, 원자재와 완제품 사이", sub="아직 접시에 담기지 않았을 뿐, 이미 가치를 지닌 자산",
        headline="같은 WIP를 세 부서가 다르게 본다",
        center=("WIP", "만들어지는 중"),
        spokes=[("PP · 생산", "생산 라인의 청진기 — 쌓이면 병목 신호"),
                ("CO · 원가", "숨은 자산의 근거 — 결산 안 하면 자산 누락"),
                ("MM · 재고", "미래 계획의 나침반 — 곧 완성될 공급 물량")]),
    "en": dict(banner="WIP — between raw material and finished goods", sub="not yet plated, but already an asset",
        headline="Three departments see the same WIP differently",
        center=("WIP", "work in progress"),
        spokes=[("PP · Production", "A stethoscope on the line — piles signal a bottleneck"),
                ("CO · Costing", "Proof of a hidden asset — skip it and assets vanish"),
                ("MM · Inventory", "A compass for planning — supply about to arrive")]),
}

# ── SAP 모듈 → 허브형 ──────────────────────────────────────────────────────
# 본문: "10개 모듈은 중앙 SAP를 중심으로 하나로 연결된다" = 방사형이 원본 의도.
WHAT_IS_SAP = {
    "ko": dict(banner="SAP, 하나로 연결된 레스토랑", sub="한 번의 입력이 모든 부서로",
        headline="누구도 옆 파트에 전화하지 않는다 — 같은 정보를 실시간으로 본다",
        center=("SAP", "통합 시스템"),
        spokes=[("홀 · 주문 (SD)", "손님 주문을 받아 시스템에 입력"),
                ("주방 · 생산 (PP)", "주문을 받아 요리를 계획하고 만든다"),
                ("창고 · 재고 (MM)", "재료를 관리하고 부족하면 발주"),
                ("계산대 · 회계 (FI/CO)", "매출과 원가를 정리한다")]),
    "en": dict(banner="SAP — one connected restaurant", sub="one entry reaches every department",
        headline="Nobody phones the next station — everyone sees the same data live",
        center=("SAP", "the integrated system"),
        spokes=[("Floor · orders (SD)", "Takes the guest's order into the system"),
                ("Kitchen · production (PP)", "Plans and cooks against that order"),
                ("Store · inventory (MM)", "Manages stock and reorders when low"),
                ("Till · finance (FI/CO)", "Settles revenue and cost")]),
}

# ── 컷오버 타임라인 → 전용 렌더(균등 간격, 원본 구조 복원) ──────────────────
# 본문: "다운타임 선언부터 Go-Live까지" 체크포인트 흐름 — 시간의 경과가 주제.
# 원본 스크린샷 구조: 5개 지점 균등 간격, 원 크기 전부 동일, 번호는 원 아래 작게,
# 시작·끝만 청록, 중간 3개는 마리골드, "시각" 텍스트 줄 없이 라벨만 크게 위/아래 배치.
CUTOVER_MAIN = {
    "ko": dict(banner="SAP 컷오버 타임라인", sub="다운타임 선언부터 Go-Live까지",
        headline="오래된 주방에서 새 주방으로 이사하는 순서",
        stops=[(None, "다운타임\n선언", TEAL),
               ("1", "데이터\n마이그레이션", MARIGOLD),
               ("2", "설정\n최종 점검", MARIGOLD),
               ("3", "계정 · 권한\n활성화", MARIGOLD),
               (None, "Go-Live", TEAL)],
        foot="세 가지 작업이 다운타임 안에 동시에 진행되고, 시간 초과는 곧 비즈니스 중단입니다"),
    "en": dict(banner="SAP cutover timeline", sub="from downtime declared to Go-Live",
        headline="The order of moving from the old kitchen to the new",
        stops=[(None, "Downtime\ndeclared", TEAL),
               ("1", "Data\nmigration", MARIGOLD),
               ("2", "Final config\ncheck", MARIGOLD),
               ("3", "Accounts &\npermissions", MARIGOLD),
               (None, "Go-Live", TEAL)],
        foot="Three tasks run at once inside the downtime window — running over means the business stops"),
}

# ── 컷오버 30시간 → 타임라인형 ─────────────────────────────────────────────
# 본문: "가장 힘든 순간은 새벽 두세 시" = 시간의 경과가 주제. 원본도 타임라인이었다.
CUTOVER_LIVE = {
    "ko": dict(banner="컷오버 현장, 30시간", sub="다운타임부터 롤백 분기까지",
        headline="가장 힘든 순간은 새벽 두세 시입니다",
        stops=[("토요일 오후", "다운타임 시작", "기존 시스템 종료 · 되돌릴 수 없는 출발", False),
               ("저녁~자정", "데이터 이전", "런북대로 순차 진행 · 건수 검증", False),
               ("새벽 2~3시", "가장 힘든 고비", "판단력이 떨어지는데 결정은 몰려온다", True),
               ("일요일 아침", "검증", "기준정보 · 재고 대조 확인", False),
               ("일요일 낮", "Go-Live 또는 롤백", "성공 또는 되돌리고 재시도", False)],
        foot="롤백은 실패가 아니라, 더 큰 사고를 막는 가장 용기 있는 결정입니다"),
    "en": dict(banner="Thirty hours of cutover", sub="from downtime to the rollback call",
        headline="The hardest moment lands at two or three in the morning",
        stops=[("Sat afternoon", "Downtime begins", "The old system stops · no way back", False),
               ("Evening–midnight", "Data migration", "Step by step per the runbook", False),
               ("02:00–03:00", "The hardest stretch", "Judgement fades as decisions pile up", True),
               ("Sunday morning", "Verification", "Master data and stock reconciled", False),
               ("Sunday midday", "Go-live or rollback", "Succeed, or revert and retry", False)],
        foot="A rollback is not a failure — it is the bravest call, made to prevent a worse one"),
}

# ── SAP 역사 → 타임라인형 ──────────────────────────────────────────────────
HISTORY = {
    "ko": dict(banner="SAP 50여 년의 발자취", sub="작은 레스토랑에서 시작된 이야기",
        headline="펀치카드에서 실시간으로, 그리고 인메모리로",
        stops=[("1972", "다섯 사람의 창업", "IBM을 떠나 실시간 처리를 꿈꾸다", False),
               ("1979", "R/2", "메인프레임 기반 통합 업무 처리", False),
               ("1992", "R/3", "클라이언트-서버로 전환\n· 세계 표준이 되다", True),
               ("2010", "HANA", "인메모리 DB로 속도의 판을 바꾸다", False),
               ("2015", "S/4HANA", "HANA 전용으로 다시 쓴 차세대 ERP", False)],
        foot="지금의 SAP는 '실시간으로 처리한다'는 창업 당시의 목표가 쌓여 만들어졌습니다"),
    "en": dict(banner="Fifty years of SAP", sub="a story that began in a small town",
        headline="From punch cards to real time, and then to in-memory",
        stops=[("1972", "Five founders", "They left IBM chasing real-time processing", False),
               ("1979", "R/2", "Integrated business processing on mainframes", False),
               ("1992", "R/3", "Client-server architecture\n· it became the standard", True),
               ("2010", "HANA", "In-memory database changed the speed equation", False),
               ("2015", "S/4HANA", "The next-generation ERP rewritten for HANA", False)],
        foot="Today's SAP is the accumulation of one founding goal — process it in real time"),
}

# ── 생산오더 상태 → 타임라인형 ─────────────────────────────────────────────
# 본문: "각 단계가 되어야 다음 작업이 허가된다" = 관문이 있는 순차 진행.
STATUS = {
    "ko": dict(banner="생산오더 상태", sub="요리 한 접시가 완성되는 순서",
        headline="각 단계가 되어야 다음 작업이 허가됩니다",
        stops=[("CRTD", "재료 준비", "오더 생성 · 아직 수정 가능", False),
               ("REL", "요리 시작", "이 상태부터 자재 출고 가능", True),
               ("CNF", "공정 완료", "작업 확인 도장 · 원가 집계 시작", False),
               ("DLV", "완성 · 입고", "완제품이 창고로 들어감", False),
               ("TECO", "주방 마감", "더 이상 변경할 수 없게 잠김", True)],
        foot="REL이어야 재료를 꺼낼 수 있고, TECO가 되면 더 이상 손댈 수 없습니다"),
    "en": dict(banner="Production order status", sub="the order in which a dish is finished",
        headline="Each stage unlocks the work that follows",
        stops=[("CRTD", "Ingredients ready", "Created · still editable", False),
               ("REL", "Cooking starts", "Only now can materials be issued", True),
               ("CNF", "Operation done", "The confirmation stamp · costs start", False),
               ("DLV", "Delivered", "Finished goods enter the warehouse", False),
               ("TECO", "Kitchen closed", "Locked against any further change", True)],
        foot="You cannot issue materials before REL, and cannot touch the order after TECO"),
}

# ── Fit/Gap → 매트릭스형 ───────────────────────────────────────────────────
# 본문: "맞으면 Fit, 안 맞으면 Gap — Gap은 세 가지 길" = 표준 적합성 × 대응 비용.
FIT_GAP = {
    "ko": dict(banner="Fit/Gap", sub="표준과 우리 매장 사이",
        headline="표준에 맞는가, 그리고 고치는 데 얼마가 드는가",
        x_axis="→ 대응 비용이 커진다", y_axis="표준적합",
        quads=[("Fit — 그대로 쓴다", ["표준 기능이 그대로 맞는다", "추가 개발 없음", "가장 저렴하고 안전"]),
               ("수용 — 받아들인다", ["표준에 없지만 감수한다", "불편해도 표준 사용", "현명한 타협"]),
               ("프로세스 변경", ["우리를 표준에 맞춘다", "업무 방식을 시스템에", "가장 이상적"]),
               ("개발 — 고쳐 쓴다", ["표준을 우리에게 맞춤", "Z코드 개발", "비용 · 시간 ↑"])]),
    "en": dict(banner="Fit/Gap", sub="between the standard and our restaurant",
        headline="Does it fit the standard, and what does closing the gap cost?",
        x_axis="→ cost of response rises", y_axis="Fits std",
        quads=[("Fit — use as is", ["The standard already fits", "No development needed", "Cheapest and safest"]),
               ("Accept — live with it", ["Not in the standard, but bearable", "Use the standard anyway", "A wise compromise"]),
               ("Change the process", ["Bend ourselves to the standard", "Adapt how we work", "The ideal outcome"]),
               ("Develop — modify it", ["Bend the system to us", "Z-code development", "Cost and time rise"])]),
}


def _curve(s):
    def b(lang, out):
        t = s[lang]; curve(out, t["banner"], t["headline"], t["points"],
                           sub=t.get("sub"), ylabel=t.get("ylabel"))
    return b


def _cycle(s):
    def b(lang, out):
        t = s[lang]; cycle(out, t["banner"], t["headline"], t["nodes"],
                           center_note=t.get("note"), sub=t.get("sub"),
                           loop_label=t.get("loop"))
    return b


def _hier(s):
    def b(lang, out):
        t = s[lang]; hierarchy(out, t["banner"], t["headline"], t["levels"],
                               sub=t.get("sub"), note=t.get("note"))
    return b


def _hub(s):
    def b(lang, out):
        t = s[lang]; hub(out, t["banner"], t["headline"], t["center"], t["spokes"],
                         sub=t.get("sub"))
    return b


def _tl(s):
    def b(lang, out):
        t = s[lang]; timeline(out, t["banner"], t["headline"], t["stops"],
                              sub=t.get("sub"), foot=t.get("foot"))
    return b


def _cutover_main(lang, out):
    """
    sap-cutover-01 전용 렌더 — 5개 체크포인트를 균등 간격으로 배치한다.
    공용 timeline()은 '시각' 라벨 줄이 있는 연표(역사·30시간 컷오버)에 맞춰져
    있어 여기 쓰면 양끝이 안쪽으로 몰린다. 이 도식은 시각 없이 라벨만 쓰고
    끝점 2개를 청록으로, 중간 3개를 마리골드로 구분하는 원본 구조를 따른다.
    """
    t = CUTOVER_MAIN[lang]
    f_lbl = font("Bold", 19)
    f_num = font("Black", 18)
    f_end = font("Bold", 19)

    top = BANNER_H + 96
    track_y = top + 96
    img_h = int(track_y + 140 + 64)
    img, d = new_canvas(img_h)
    draw_banner(d, t["banner"], t["sub"])
    draw_headline(d, BANNER_H + 30, t["headline"])

    x0, x1 = MARGIN + 30, W - MARGIN - 30
    d.rounded_rectangle([x0, track_y - 5, x1, track_y + 5], radius=5, fill="#e4ddd0")

    stops = t["stops"]
    n = len(stops)
    xs = [x0 + (x1 - x0) * i / (n - 1) for i in range(n)]
    r = 24  # 숫자를 원 안에 담기 위해 배지 반경을 키운다(기존 15px는 두 자리 숫자에도 좁음)

    for i, (num, lbl, col) in enumerate(stops):
        cx_ = xs[i]
        is_end = num is None
        d.ellipse([cx_ - r - 4, track_y - r - 4, cx_ + r + 4, track_y + r + 4], fill=BG)
        d.ellipse([cx_ - r, track_y - r, cx_ + r, track_y + r], fill=col)
        if not is_end:
            true_center_text(d, cx_, track_y, num, f_num, WHITE)

        lines = lbl.split("\n")
        up = i % 2 == 0
        line_h = 26
        block_h = len(lines) * line_h
        gap = 22
        if up:
            ty = track_y - r - gap - block_h
        else:
            ty = track_y + r + gap

        yy = ty
        f_this = f_end if is_end else f_lbl
        for ln in lines:
            center_x_text(d, cx_, yy, ln, f_this, INK)
            yy += line_h

    d.rounded_rectangle([MARGIN, img_h - 56, W - MARGIN, img_h - 16], radius=11, fill=TEAL_PALE)
    true_center_text(d, W / 2, img_h - 36, t["foot"], font("Medium", 15), TEAL)

    save(img, out)


def _quad(s):
    def b(lang, out):
        t = s[lang]; quadrant(out, t["banner"], t["headline"], t["x_axis"],
                              t["y_axis"], t["quads"], sub=t.get("sub"))
    return b


BUILDERS = {
    "sap-change-management-01":        _curve(CHANGE),
    "sap-circular-bom-01":             _cycle(CIRCULAR),
    "sap-what-is-sap-01":              _hub(WHAT_IS_SAP),
    "sap-cutover-01":                  _cutover_main,
    "sap-cutover-live-01":             _tl(CUTOVER_LIVE),
    "sap-history-timeline":            _tl(HISTORY),
    "sap-production-order-status-flow": _tl(STATUS),
}
