# -*- coding: utf-8 -*-
"""
카테고리 A — SAP PP/생산 도식 (brand_v3 재설계) 묶음 1.
넘버링 로우(순차·병렬 항목) + 비교형(대립) 형태.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import v3_forms as V

OUT = "/sessions/happy-quirky-mayer/mnt/rabbit-logs/public/images/new"


# ── sap-pp-master-data : 병렬 4항목 → 넘버링 로우 ──
def pp_master_data(lang, out):
    D = {
        "ko": ("SAP PP 기준정보, 핵심 4가지",
               "정확한 이 데이터 위에서 MRP·생산오더·원가가 굴러간다",
               [("자재 마스터", "무엇을 — 만들 품목과 재료의 기본 정보"),
                ("BOM", "무엇으로 — 완성품에 필요한 자재와 수량"),
                ("라우팅", "어떻게 — 공정 순서·작업장·표준시간"),
                ("생산 버전", "어떤 조합으로 — BOM과 라우팅을 묶은 실행안")]),
        "en": ("SAP PP Master Data: The 4 Essentials",
               "MRP, orders, and costing all rely on this data being right",
               [("Material Master", "What — basic info of the item and materials"),
                ("BOM", "Made of what — components and quantities"),
                ("Routing", "How — operations, work centers, standard times"),
                ("Production Version", "Which combo — a BOM + routing pairing")]),
    }
    t, s, steps = D[lang]
    V.numbering_rows(t, s, steps, out)


# ── sap-mrp-flow : 4단계 순차 → 넘버링 로우 ──
def mrp_flow(lang, out):
    D = {
        "ko": ("SAP MRP, 자재계획 4단계",
               "생산 목표에서 계획오더까지 자동으로 계산된다",
               [("총소요량", "BOM을 전개해 필요한 자재 총량을 뽑는다"),
                ("순소요량", "현재 재고를 빼고 실제 부족분만 남긴다"),
                ("발주 시점", "리드타임을 거꾸로 세어 발주일을 정한다"),
                ("계획오더", "무엇을·얼마나·언제 만들지 초안을 만든다")]),
        "en": ("SAP MRP: Planning in 4 Steps",
               "From a production target to planned orders, computed for you",
               [("Gross Requirement", "Explode the BOM to get total material need"),
                ("Net Requirement", "Subtract stock to leave the real shortfall"),
                ("Order Point", "Count back by lead time to set the order date"),
                ("Planned Order", "Draft of what, how much, and when to make")]),
    }
    t, s, steps = D[lang]
    V.numbering_rows(t, s, steps, out)


# ── sap-production-order-status-flow : 5단계 순차 → 넘버링 로우 ──
def order_status(lang, out):
    D = {
        "ko": ("생산오더 상태, 완성까지 5단계",
               "각 상태가 되어야 다음 작업이 열린다",
               [("CRTD 준비", "오더가 생성됐지만 아직 실행 전이다"),
                ("REL 시작", "릴리스되어 자재 출고가 가능해진다"),
                ("CNF 확정", "공정이 끝나 실적이 확정된다"),
                ("DLV 입고", "완성품이 창고로 입고된다"),
                ("TECO 마감", "기술적으로 종료되어 정산으로 넘어간다")]),
        "en": ("Production Order Status: 5 Steps",
               "Each status unlocks the next action",
               [("CRTD Created", "Order exists but is not yet executable"),
                ("REL Released", "Released, so goods issue becomes possible"),
                ("CNF Confirmed", "Operations done, actuals confirmed"),
                ("DLV Delivered", "Finished goods received into stock"),
                ("TECO Closed", "Technically complete, moves to settlement")]),
    }
    t, s, steps = D[lang]
    V.numbering_rows(t, s, steps, out, row_h=88)


# ── sap-activity-cnf-01 : 3단계 순차 → 넘버링 로우 ──
def activity_cnf(lang, out):
    D = {
        "ko": ("Activity와 CNF, 보고까지 3단계",
               "작업이 확정돼야 재고·원가·후속 계획이 맞는다",
               [("Activity 정의", "생산오더 안에 개별 작업 단계가 담긴다"),
                ("작업 수행", "조리팀이 배분된 각 작업을 실제로 처리한다"),
                ("CNF 확정", "'다 됐다'는 보고로 실적이 시스템에 올라간다")]),
        "en": ("Activity & CNF: 3 Steps to Report",
               "Only confirmed work keeps stock, cost, and plans accurate",
               [("Define Activity", "Individual operations sit inside the order"),
                ("Perform Work", "The team executes each assigned operation"),
                ("Confirm (CNF)", "A 'done' report posts the actuals to SAP")]),
    }
    t, s, steps = D[lang]
    V.numbering_rows(t, s, steps, out)


# ── sap-gi-gr-cnf-flow : 3개 병렬 개념 → 넘버링 로우 ──
def gi_gr_cnf(lang, out):
    D = {
        "ko": ("GI·GR·CNF, 재고가 움직이는 세 순간",
               "출고·입고·생산확정 — 원가 계산의 세 기둥",
               [("GI 출고", "재고가 나간다 — 생산에 재료를 투입한다"),
                ("GR 입고", "재고가 들어온다 — 완성품이 창고로 들어간다"),
                ("CNF 확정", "몇 개를 얼마 들여 만들었는지 실적을 보고한다")]),
        "en": ("GI·GR·CNF: Three Moments of Stock",
               "Issue, receipt, confirmation — three pillars of costing",
               [("GI Issue", "Stock goes out — materials fed into production"),
                ("GR Receipt", "Stock comes in — finished goods enter the warehouse"),
                ("CNF Confirm", "Report how many were made and at what effort")]),
    }
    t, s, steps = D[lang]
    V.numbering_rows(t, s, steps, out)


# ── sap-production-strategy-01 : MTS vs MTO → 비교형 ──
def production_strategy(lang, out):
    D = {
        "ko": (("SAP 생산 전략, MTS vs MTO", "재고를 먼저 쌓을까, 주문부터 받을까"),
               ("MTS", "재고 생산", "teal"), ("MTO", "주문 생산", "gold"),
               ["비유", "생산 시점", "재고", "납기"],
               [("뷔페 — 미리 차림", "스테이크 — 주문 후 조리"),
                ("주문 전 미리 생산", "주문 접수 후 생산"),
                ("완제품 재고 보유", "원자재만 보유"),
                ("즉시 제공 가능", "생산 시간만큼 대기")],
               "정답은 하나가 아니다 — 반제품까지만 미리 만드는 절충안도 있다"),
        "en": (("Strategy: MTS vs MTO", "Stock up first, or wait for the order?"),
               ("MTS", "Make-to-Stock", "teal"), ("MTO", "Make-to-Order", "gold"),
               ["Analogy", "When made", "Inventory", "Lead time"],
               [("Buffet — made ahead", "Steakhouse — cooked on order"),
                ("Produced before orders", "Produced after the order"),
                ("Holds finished goods", "Holds only raw materials"),
                ("Available instantly", "Waits the production time")],
               "There is a middle path — pre-build only to the semi-finished stage"),
    }
    (t, s), cA, cB, labels, rows, foot = D[lang]
    V.compare_two(t, s, cA, cB, rows, out, footer=foot, rowlabels=labels)


# ── sap-planned-vs-production-order : 비교형 ──
def planned_vs_production(lang, out):
    D = {
        "ko": (("계획오더 vs 생산오더", "식단표와 실제 조리 지시서의 차이"),
               ("계획오더", "가계획", "teal"), ("생산오더", "실행 지시", "berry"),
               ["성격", "생성 주체", "자재·설비", "변경"],
               [("유연한 제안서", "확정된 지시서"),
                ("MRP가 자동 생성", "담당자가 확정"),
                ("예약하지 않음", "자재·설비를 예약"),
                ("자유롭게 조정", "통제된 변경")],
               "계획은 제안으로 유연하게, 실행은 명령으로 확실하게"),
        "en": (("Planned vs Production Order", "A menu plan versus a real cooking order"),
               ("Planned Order", "tentative", "teal"), ("Production Order", "executable", "berry"),
               ["Nature", "Created by", "Materials", "Changes"],
               [("Flexible proposal", "Firm instruction"),
                ("Auto-made by MRP", "Confirmed by a planner"),
                ("Reserves nothing", "Reserves material & capacity"),
                ("Freely adjustable", "Controlled changes")],
               "Plan stays flexible as a proposal; execution is firm as a command"),
    }
    (t, s), cA, cB, labels, rows, foot = D[lang]
    V.compare_two(t, s, cA, cB, rows, out, footer=foot, rowlabels=labels)


# ── sap-production-order-carryover-01 : 비교형 ──
def order_carryover(lang, out):
    D = {
        "ko": (("생산오더 이월, 두 가지 방식", "월말에 만들다 만 오더를 처리하는 법"),
               ("오더 이월", "새 오더로", "teal"), ("WIP 이월", "회계로만", "berry"),
               ["기존 오더", "잔량 처리", "회계", "쓰는 때"],
               [("TECO로 마감", "오픈 상태 유지"),
                ("신규 오더로 생성", "그대로 이어서 생산"),
                ("정산 완료", "미완료 원가를 WIP 계정으로"),
                ("잔량을 분리 관리", "원가만 이월하면 될 때")],
               "실물 흐름을 끊을지, 회계만 처리할지가 갈림길이다"),
        "en": (("Order Carryover: Two Ways", "Handling an unfinished order at month-end"),
               ("Order Carryover", "new order", "teal"), ("WIP Carryover", "accounting", "berry"),
               ["Existing order", "Remainder", "Accounting", "When to use"],
               [("Closed with TECO", "Kept open"),
                ("Created as a new order", "Continues as-is"),
                ("Settled", "Unfinished cost to WIP account"),
                ("Split & track leftover", "When only cost carries over")],
               "The fork: break the physical flow, or handle it in accounting only"),
    }
    (t, s), cA, cB, labels, rows, foot = D[lang]
    V.compare_two(t, s, cA, cB, rows, out, footer=foot, rowlabels=labels)


BUILDERS = {
    "sap-pp-master-data": pp_master_data,
    "sap-mrp-flow": mrp_flow,
    "sap-production-order-status-flow": order_status,
    "sap-activity-cnf-01": activity_cnf,
    "sap-gi-gr-cnf-flow": gi_gr_cnf,
    "sap-production-strategy-01": production_strategy,
    "sap-planned-vs-production-order": planned_vs_production,
    "sap-production-order-carryover-01": order_carryover,
}

if __name__ == "__main__":
    for slug, fn in BUILDERS.items():
        fn("ko", os.path.join(OUT, f"{slug}.jpg"))
        fn("en", os.path.join(OUT, f"{slug}_en.jpg"))
