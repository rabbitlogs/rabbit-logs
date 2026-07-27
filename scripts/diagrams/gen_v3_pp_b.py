# -*- coding: utf-8 -*-
"""
카테고리 A — SAP PP/생산 도식 (brand_v3 재설계) 묶음 2.
분류(미니표) + 병렬/순차(넘버링) 형태.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import v3_forms as V

OUT = "/sessions/happy-quirky-mayer/mnt/rabbit-logs/public/images/new"


# ── sap-movement-type-flow : 분류 → 미니표 ──
def movement_type(lang, out):
    D = {
        "ko": ("SAP 이동유형, 3자리 코드로 읽는 재고 이동",
               "왜·어떻게 움직였는지 코드가 말해준다",
               ["코드", "의미", "재고", "회계전표"],
               [["101", "생산품 입고", "증가", "발생"],
                ["261", "오더용 자재 출고", "감소", "발생"],
                ["311", "저장위치 간 이동", "변동 없음", "없음"],
                ["531", "부산물 입고", "증가", "발생"]],
               "100대 입고 · 200대 출고 · 300대 이동 · 500대 특수"),
        "en": ("SAP Movement Types: Stock Moves in 3 Digits",
               "The code tells you why and how stock moved",
               ["Code", "Meaning", "Stock", "FI doc"],
               [["101", "Goods receipt from order", "Up", "Yes"],
                ["261", "Goods issue to order", "Down", "Yes"],
                ["311", "Transfer between storage", "No change", "No"],
                ["531", "By-product receipt", "Up", "Yes"]],
               "100s receipt · 200s issue · 300s transfer · 500s special"),
    }
    t, s, headers, rows, note = D[lang]
    V.mini_table(t, s, headers, rows, out, note=note)


# ── study-pp-work-center-01 : 마스터 구성요소 병렬 → 넘버링 ──
def work_center(lang, out):
    D = {
        "ko": ("SAP 작업장, 공정이 일어나는 스테이션",
               "라우팅이 지정하면 여기서 일정·원가 정보를 읽어온다",
               [("담당자", "이 스테이션을 누가 운영하는지 정한다"),
                ("용량", "하루에 가동 가능한 시간 — 병목 판단의 기준"),
                ("원가센터", "여기서 발생한 가공비가 어디로 집계되는지"),
                ("카테고리", "기계·인력 등 작업장의 성격을 분류한다")]),
        "en": ("SAP Work Center: Where Operations Happen",
               "Routing points here to read scheduling and cost info",
               [("Person in charge", "Who operates this station"),
                ("Capacity", "Available hours a day — basis for bottlenecks"),
                ("Cost center", "Where the processing cost is collected"),
                ("Category", "Classifies the station: machine, labor, etc.")]),
    }
    t, s, steps = D[lang]
    V.numbering_rows(t, s, steps, out)


# ── study-pp-routing-01 : 공정 순서 → 넘버링(순차) ──
def routing(lang, out):
    D = {
        "ko": ("SAP 라우팅, 공정 순서표가 답하는 것",
               "라우팅이 없으면 납기·원가·작업지시를 못 낸다",
               [("공정 순서", "제품을 만드는 작업을 순서대로 나열한다"),
                ("작업장 지정", "각 공정을 어느 스테이션에서 할지 정한다"),
                ("표준시간", "공정마다 보통 걸리는 시간을 등록한다"),
                ("납기·원가 산출", "시간×단가로 가공비와 일정을 계산한다")]),
        "en": ("SAP Routing: What the Process Sheet Answers",
               "Without routing, no due date, cost, or work order",
               [("Operation order", "Lists the steps to make the product in order"),
                ("Work center", "Assigns each operation to a station"),
                ("Standard time", "Registers the usual time per operation"),
                ("Date & cost", "Time × rate gives cost and schedule")]),
    }
    t, s, steps = D[lang]
    V.numbering_rows(t, s, steps, out)


# ── sap-wip-overview : 3관점 병렬 → 넘버링 ──
def wip(lang, out):
    D = {
        "ko": ("SAP WIP, 세 부서가 보는 재공품",
               "만들어지는 중인 가치를 부서마다 다르게 읽는다",
               [("생산 PP", "어디서 막혔는지 알려주는 병목 신호"),
                ("원가 CO", "재무제표에 올라가는 자산 가치의 근거"),
                ("재고 MM", "곧 완성될 공급 물량 — 재고 계획의 기준")]),
        "en": ("SAP WIP: Three Views of Work in Process",
               "Each department reads the in-progress value differently",
               [("Production PP", "A bottleneck signal showing where it stalled"),
                ("Costing CO", "Basis for the asset value on the statements"),
                ("Inventory MM", "Near-finished supply — basis for stock plans")]),
    }
    t, s, steps = D[lang]
    V.numbering_rows(t, s, steps, out)


# ── sap-production-order-number-01 : 개념 3가지 병렬 → 넘버링 ──
def order_number(lang, out):
    D = {
        "ko": ("SAP 생산오더 번호, 알아둘 세 가지",
               "번호는 한 번 쓰면 되돌아오지 않는다",
               [("재사용 불가", "삭제해도 번호는 안 돌아오고 삭제 플래그만 붙는다"),
                ("클라이언트 유일", "회사·공장이 달라도 같은 클라이언트 안엔 중복 없음"),
                ("범위 관리 필요", "소진돼도 자릿수가 안 늘어 사전 관리가 필요하다")]),
        "en": ("SAP Order Numbers: Three Things to Know",
               "Once used, a number never comes back",
               [("Not reusable", "Deleting only sets a flag; the number is gone"),
                ("Unique per client", "No duplicates within a client, any plant"),
                ("Manage the range", "Digits don't auto-grow when exhausted")]),
    }
    t, s, steps = D[lang]
    V.numbering_rows(t, s, steps, out)


BUILDERS = {
    "sap-movement-type-flow": movement_type,
    "study-pp-work-center-01": work_center,
    "study-pp-routing-01": routing,
    "sap-wip-overview": wip,
    "sap-production-order-number-01": order_number,
}

if __name__ == "__main__":
    for slug, fn in BUILDERS.items():
        fn("ko", os.path.join(OUT, f"{slug}.jpg"))
        fn("en", os.path.join(OUT, f"{slug}_en.jpg"))
