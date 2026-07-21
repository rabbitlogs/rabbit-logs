# -*- coding: utf-8 -*-
"""템플릿 기반 도식 묶음 2."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from templates import steps, duo, matrix

GI_GR_CNF = {
    "ko": dict(banner="GI · GR · CNF", sub="재고의 세 순간",
        headline="나가고, 들어오고, 만들어진다",
        cards=[("출고 (GI)", ["재고가 나가는 것", "창고 → 주방 · 출하", "감소 −"]),
               ("입고 (GR)", ["재고가 들어오는 것", "납품 · 생산품 받기", "증가 +"]),
               ("실적확정 (CNF)", ["만들고 보고하는 것", "완제품 입고 + 원가", "증가 + 정산"])]),
    "en": dict(banner="GI · GR · CNF", sub="three moments in inventory",
        headline="Goods leave, goods arrive, goods get made",
        cards=[("Goods issue (GI)", ["Stock leaving", "Warehouse → kitchen", "Decrease −"]),
               ("Goods receipt (GR)", ["Stock arriving", "Deliveries, finished output", "Increase +"]),
               ("Confirmation (CNF)", ["Making and reporting", "Finished goods plus cost", "Increase + settle"])]),
}

MOVEMENT = {
    "ko": dict(banner="이동유형", sub="재고가 움직이는 흐름",
        headline="들어오면 100번대, 나가면 200번대, 옮기면 300번대",
        cards=[("261 · 자재 출고", ["재료를 꺼내 주방으로"]),
               ("101 · 생산품 입고", ["완성 메뉴, 픽업대로"]),
               ("311 · 저장위치 이동", ["창고 안에서 자리 이동"]),
               ("531 · 부산물 입고", ["육수 우려낸 부산물도 입고"])]),
    "en": dict(banner="Movement types", sub="how stock moves",
        headline="100s come in, 200s go out, 300s move within",
        cards=[("261 · Material issue", ["Ingredients out to the kitchen"]),
               ("101 · Production receipt", ["Finished dish to the pass"]),
               ("311 · Storage transfer", ["Moved within the warehouse"]),
               ("531 · By-product receipt", ["Even stock left from the broth"])]),
}

ORG_STRUCTURE = {
    "ko": dict(banner="SAP 조직 구조", sub="건물 설계도의 네 단계",
        headline="위에서 아래로, 담는 범위가 점점 좁아집니다",
        cards=[("클라이언트", ["레스토랑 그룹 전체", "시스템 전체의", "가장 큰 단위"]),
               ("회사 코드", ["독립적인 회계 장부 단위", "강남점 법인 ·", "홍대점 법인"]),
               ("플랜트", ["실제 요리가 이뤄지는 매장", "생산 · 재고 관리의", "핵심 단위"]),
               ("저장 위치", ["냉장 창고 · 상온 창고", "플랜트 안 물리적", "보관 장소"])]),
    "en": dict(banner="SAP organisational structure", sub="four levels of the blueprint",
        headline="Top to bottom, each level narrows what it holds",
        cards=[("Client", ["The whole restaurant group", "The largest unit in", "the entire system"]),
               ("Company code", ["An independent set of books", "The Gangnam entity,", "the Hongdae entity"]),
               ("Plant", ["Where cooking actually happens", "The core unit for output", "and inventory"]),
               ("Storage location", ["Chilled store, dry store", "A physical place", "inside the plant"])]),
}

USER_PARAMS = {
    "ko": dict(banner="SAP 매개변수 ID", sub="매일 쓰는 기본값 한 번에 저장",
        headline="F1로 찾고, SU3에 등록하면 끝",
        cards=[("F1로 확인", ["자주 입력하는 필드에", "커서를 두고 F1", "매개변수 ID 확인"]),
               ("SU3에 등록", ["매개변수 ID와", "기본값을 입력해", "개인 설정에 저장"]),
               ("자동으로 채워짐", ["다음부터 그 필드는", "기본값이 미리", "입력된 채로 시작"])]),
    "en": dict(banner="SAP parameter IDs", sub="save the values you type every day",
        headline="Find it with F1, register it in SU3, done",
        cards=[("Check with F1", ["Put the cursor in a field", "you fill in often and", "press F1 for the ID"]),
               ("Register in SU3", ["Enter the parameter ID", "and default value in", "your own settings"]),
               ("Filled automatically", ["From then on the field", "starts pre-filled with", "your default"])]),
}

CIRCULAR_BOM = {
    "ko": dict(banner="순환 BOM", sub="레시피가 자기를 다시 부르는 오류",
        headline="A가 B를 부르고, B가 다시 A를 부르면 멈추지 않습니다",
        cards=[("정상 BOM", ["상위 → 하위로만", "한 방향으로 흐른다", "계산이 끝난다"]),
               ("순환 발생", ["하위가 상위를", "다시 자재로 참조", "무한 반복 시작"]),
               ("MRP 중단", ["계산이 끝나지 않아", "오류로 멈춤", "CS15로 역추적"])]),
    "en": dict(banner="Circular BOMs", sub="when a recipe calls itself",
        headline="If A calls B and B calls A again, it never stops",
        cards=[("A healthy BOM", ["Flows one way only,", "parent down to child", "The calculation ends"]),
               ("The loop appears", ["A child references its", "own parent as a component", "Infinite repetition begins"]),
               ("MRP halts", ["The run never finishes", "and stops with an error", "Trace it back with CS15"])]),
}

BATCH_MGMT = {
    "ko": dict(banner="배치에 담기는 정보", sub="다섯 가지 핵심 항목",
        headline="배치 하나로 이력 전체를 추적합니다",
        cards=[("배치 번호", ["자재코드+배치번호로", "재고를 특정"]),
               ("생산일자 · 플랜트", ["언제, 어느 공장에서", "만들었는지"]),
               ("원자재 정보", ["어떤 공급업체의", "원자재를 사용했는지"]),
               ("품질 데이터", ["당도 · 수분 · 순도 등", "측정값(특성값)"]),
               ("유통기한", ["유통기한 또는", "최소 보관 기간"])]),
    "en": dict(banner="What a batch records", sub="five essential fields",
        headline="One batch number traces the entire history",
        cards=[("Batch number", ["Material code plus batch", "pinpoints the stock"]),
               ("Date · plant", ["When and at which", "plant it was made"]),
               ("Raw material", ["Which supplier's", "materials went in"]),
               ("Quality data", ["Measured values such as", "sugar, moisture, purity"]),
               ("Shelf life", ["Expiry date or the", "minimum storage period"])]),
}

FIT_GAP = {
    "ko": dict(banner="Fit/Gap", sub="표준과 우리 매장 사이",
        headline="맞으면 Fit, 안 맞으면 Gap — Gap은 세 가지 길로 푼다",
        left=("Fit", "표준 그대로 쓰면 되는 부분",
              ["표준 기능이 그대로 맞는다", "추가 개발이 필요 없다", "가장 저렴하고 안전하다"]),
        right=("Gap", "손봐야 하거나 없는 부분",
               ["개발 — 표준을 우리에게 맞춤 (비용 · 시간 ↑)",
                "프로세스 변경 — 우리를 표준에 맞춤 (가장 이상적)",
                "수용 — 그냥 받아들임 (현명한 타협)"])),
    "en": dict(banner="Fit/Gap", sub="between the standard and our restaurant",
        headline="A fit needs nothing; a gap has three ways out",
        left=("Fit", "Works as delivered",
              ["The standard function already fits", "No extra development needed",
               "The cheapest and safest option"]),
        right=("Gap", "Missing or needs changing",
               ["Develop — bend the system to us (cost, time ↑)",
                "Change process — bend us to the standard (ideal)",
                "Accept — live with it (a wise compromise)"])),
}

MES_INTERFACE = {
    "ko": dict(banner="SAP MES 인터페이스", sub="RFC vs PI/PO 연결 방식",
        headline="직접 통화할까, 중앙 관제를 거칠까",
        left=("RFC", "직접 전화 방식",
              ["빠른 속도, 중간 단계 없음", "실시간 동기 방식에 적합",
               "동기(Sync) — 답장 올 때까지 대기", "실시간 재고 확인 등 즉시 확인이 필요할 때"]),
        right=("PI / PO", "중앙 관제 방식",
               ["안정성, 메시지 보관 · 재전송", "비동기 방식에 유리",
                "비동기(Async) — 시간 될 때 답장", "대량 생산 계획 배치 전송에 적합"])),
    "en": dict(banner="SAP MES interfaces", sub="RFC vs PI/PO",
        headline="Call directly, or route through the control tower?",
        left=("RFC", "The direct call",
              ["Fast, with no middle layer", "Suited to real-time sync calls",
               "Synchronous — waits for the reply", "For instant checks like live stock"]),
        right=("PI / PO", "The control tower",
               ["Stable, stores and resends messages", "Better suited to async work",
                "Asynchronous — replies when ready", "Good for large batch plan transfers"])),
}

CUTOVER_LIVE = {
    "ko": dict(banner="컷오버 현장, 30시간", sub="다운타임부터 롤백 분기까지",
        headline="가장 힘든 순간은 새벽 두세 시입니다",
        cards=[("토요일 오후", ["기존 시스템 종료"]),
               ("데이터 이전 실행", ["런북대로 순차 진행"]),
               ("새벽 2~3시", ["가장 힘든 고비"]),
               ("검증", ["기준정보 · 재고 확인"]),
               ("Go-Live 또는 롤백", ["성공 또는 재시도"])]),
    "en": dict(banner="Thirty hours of cutover", sub="from downtime to the rollback call",
        headline="The hardest moment lands at two or three in the morning",
        cards=[("Saturday afternoon", ["The old system shuts down"]),
               ("Data migration runs", ["Step by step, per the runbook"]),
               ("02:00–03:00", ["The hardest stretch"]),
               ("Verification", ["Master data and stock checks"]),
               ("Go-live or rollback", ["Succeed, or try again"])]),
}

CARRYOVER = {
    "ko": dict(banner="생산오더 이월 방식", sub="오더 이월 vs WIP 이월",
        headline="만들다 만 음식 30인분, 어떻게 처리할까",
        left=("방식 1: 오더 이월", None,
              ["기존 오더 TECO(마감)", "새 오더 신규 생성", "→ 70개 / 30개로 명확히 구분됨"]),
        right=("방식 2: WIP 이월", None,
               ["오더는 계속 오픈 유지", "원가만 다음 달로 이전", "→ 오더 하나로 전체 이력 유지"])),
    "en": dict(banner="Carrying a production order over", sub="order carry-over vs WIP carry-over",
        headline="Thirty portions half-made — what do you do with them?",
        left=("Option 1: carry the order", None,
              ["TECO the existing order", "Create a brand-new order",
               "→ A clean split of 70 and 30"]),
        right=("Option 2: carry the WIP", None,
               ["The order stays open", "Only the cost moves to next month",
                "→ One order keeps the full history"])),
}

ORDER_NUMBER = {
    "ko": dict(banner="생산오더 번호 구조", sub="클라이언트 단위 고유성",
        headline="AUFK 테이블의 유일한 키는 오더 번호 하나뿐",
        left=("A 공장", "1000만 번대",
              ["10000001, 10000002 …", "번호가 겹치지 않도록", "처음부터 범위 분리"]),
        right=("B 공장", "2000만 번대",
               ["20000001, 20000002 …", "번호가 겹치지 않도록", "처음부터 범위 분리"])),
    "en": dict(banner="Production order numbering", sub="unique across the client",
        headline="AUFK has exactly one key — the order number",
        left=("Plant A", "10-million range",
              ["10000001, 10000002 …", "Ranges are split up front",
               "so numbers never collide"]),
        right=("Plant B", "20-million range",
               ["20000001, 20000002 …", "Ranges are split up front",
                "so numbers never collide"])),
}


def _steps(spec):
    def build(lang, out):
        t = spec[lang]
        steps(out, t["banner"], t["headline"], t["cards"], sub=t.get("sub"))
    return build


def _duo(spec):
    def build(lang, out):
        t = spec[lang]
        duo(out, t["banner"], t["headline"], t["left"], t["right"], sub=t.get("sub"))
    return build


BUILDERS = {
    "sap-gi-gr-cnf-flow":                _steps(GI_GR_CNF),
    "sap-movement-type-flow":            _steps(MOVEMENT),
    "sap-org-structure-master-data-01":  _steps(ORG_STRUCTURE),
    "sap-user-parameters-01":            _steps(USER_PARAMS),
    "sap-circular-bom-01":               _steps(CIRCULAR_BOM),
    "sap-batch-management-01":           _steps(BATCH_MGMT),
    "sap-cutover-live-01":               _steps(CUTOVER_LIVE),
    "sap-fit-gap-ways":                  _duo(FIT_GAP),
    "sap-mes-interface-01":              _duo(MES_INTERFACE),
    "sap-production-order-carryover-01": _duo(CARRYOVER),
    "sap-production-order-number-01":    _duo(ORDER_NUMBER),
}
