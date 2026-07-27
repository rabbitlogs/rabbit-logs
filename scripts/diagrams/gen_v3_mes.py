# -*- coding: utf-8 -*-
"""
카테고리 B — SAP 배치/MES/인터페이스 도식 (brand_v3 재설계).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import v3_forms as V

OUT = "/sessions/happy-quirky-mayer/mnt/rabbit-logs/public/images/new"


# ── sap-batch-management-01 : 배치가 담는 정보(병렬) → 넘버링 ──
def batch_management(lang, out):
    D = {
        "ko": ("SAP 배치 관리, 배치에 담기는 것",
               "같은 자재라도 배치로 나눠 이력을 추적한다",
               [("출처", "언제, 어떤 원자재로 만들어졌는지 기록한다"),
                ("품질 데이터", "검사 결과·등급 같은 품질 정보를 담는다"),
                ("유통기한", "언제까지 쓸 수 있는지 관리한다"),
                ("생산 이력", "문제가 생기면 이 배치만 골라 추적한다")]),
        "en": ("SAP Batch Management: What a Batch Holds",
               "Split the same material into batches to trace its history",
               [("Origin", "When and from which raw materials it was made"),
                ("Quality data", "Inspection results and grade information"),
                ("Shelf life", "Manages the usable-by date"),
                ("Production history", "Trace just this batch when a problem hits")]),
    }
    t, s, steps = D[lang]
    V.numbering_rows(t, s, steps, out)


# ── sap-batch-job-01 : SM36→SM37 예약 실행(순차) → 넘버링 ──
def batch_job(lang, out):
    D = {
        "ko": ("SAP 배치잡, 예약부터 모니터링까지",
               "반복 업무를 정해진 시간에 자동 실행한다",
               [("업무 요청", "실무자가 자동화할 작업과 시점을 정의한다"),
                ("조건 설계", "PI가 실행 주기·순서 등 조건을 설계한다"),
                ("SM36 예약", "개발자가 잡을 등록하고 시간을 예약한다"),
                ("SM37 확인", "실행 결과를 모니터링하고 오류를 잡는다")]),
        "en": ("SAP Batch Job: From Scheduling to Monitoring",
               "Run repetitive work automatically at a set time",
               [("Request", "A user defines the task and when to run it"),
                ("Design", "PI designs the timing, order, and conditions"),
                ("Schedule (SM36)", "A developer registers and schedules the job"),
                ("Monitor (SM37)", "Check run results and catch any errors")]),
    }
    t, s, steps = D[lang]
    V.numbering_rows(t, s, steps, out)


# ── sap-mes-role-01 : SAP vs MES 역할 분업 → 비교형 ──
def mes_role(lang, out):
    D = {
        "ko": (("SAP와 MES, 계획과 실행의 분업", "총괄 셰프와 주방 팀은 경쟁하지 않는다"),
               ("SAP (ERP)", "계획의 중심", "teal"), ("MES", "실행의 중심", "gold"),
               ["역할", "관점", "결정", "시간 단위"],
               [("무엇을·얼마나·언제", "지시대로 현장 생산"),
                ("계획을 세운다", "실행을 관리한다"),
                ("생산 목표를 정한다", "현장 변수에 대응한다"),
                ("일·주 단위 계획", "초·분 단위 관리")],
               "경쟁이 아니라 분업 — 계획과 실행이 서로의 빈틈을 채운다"),
        "en": (("SAP & MES: Plan vs Execute", "The head chef and the kitchen team don't compete"),
               ("SAP (ERP)", "planning core", "teal"), ("MES", "execution core", "gold"),
               ["Role", "View", "Decides", "Time unit"],
               [("What, how much, when", "Runs the shop floor"),
                ("Makes the plan", "Manages execution"),
                ("Sets production targets", "Reacts to floor variables"),
                ("Days & weeks", "Seconds & minutes")],
               "Not rivalry but division — plan and execution fill each other's gaps"),
    }
    (t, s), cA, cB, labels, rows, foot = D[lang]
    V.compare_two(t, s, cA, cB, rows, out, footer=foot, rowlabels=labels)


# ── sap-mes-interface-01 : RFC vs PI/PO → 비교형 ──
def mes_interface_01(lang, out):
    D = {
        "ko": (("MES 인터페이스, RFC vs PI/PO", "두 시스템을 잇는 두 가지 연결 방식"),
               ("RFC", "직통 전화", "teal"), ("PI/PO", "중앙 관제", "berry"),
               ["비유", "연결", "중간 관리", "적합"],
               [("직통 전화", "관제탑 경유"),
                ("시스템 간 직접", "허브가 중계"),
                ("없음 — 1:1", "중앙에서 통제"),
                ("단순·소규모 연동", "다수 시스템 연동")],
               "연동 대상이 늘수록 중앙 관제(PI/PO)가 관리에 유리하다"),
        "en": (("MES Interface: RFC vs PI/PO", "Two ways to connect the two systems"),
               ("RFC", "direct line", "teal"), ("PI/PO", "central control", "berry"),
               ["Analogy", "Link", "Middle mgmt", "Fits"],
               [("Direct call", "Via control tower"),
                ("System to system", "A hub relays it"),
                ("None — 1:1", "Controlled centrally"),
                ("Simple, small links", "Many-system links")],
               "The more systems you link, the more central control (PI/PO) helps"),
    }
    (t, s), cA, cB, labels, rows, foot = D[lang]
    V.compare_two(t, s, cA, cB, rows, out, footer=foot, rowlabels=labels)


# ── sap-mes-interface-02 : 동기 vs 비동기 → 비교형 ──
def mes_interface_02(lang, out):
    D = {
        "ko": (("MES 소통 스타일, 동기 vs 비동기", "응답을 기다릴지, 전달하고 넘어갈지"),
               ("동기", "응답 대기", "teal"), ("비동기", "전달 후 진행", "gold"),
               ["방식", "속도감", "안정성", "적합"],
               [("보내고 기다림", "보내고 다음 업무"),
                ("즉시 응답 확인", "나중에 결과 확인"),
                ("응답 지연에 취약", "지연에 강함"),
                ("즉답이 필요할 때", "대량·지연 허용")],
               "업무 특성에 맞춰 동기와 비동기를 섞어 쓴다"),
        "en": (("MES Style: Sync vs Async", "Wait for a reply, or hand off and move on"),
               ("Sync", "waits for reply", "teal"), ("Async", "hands off", "gold"),
               ["Manner", "Feel", "Robustness", "Fits"],
               [("Send and wait", "Send, then move on"),
                ("Reply confirmed now", "Result checked later"),
                ("Weak to reply delay", "Strong against delay"),
                ("When answer needed now", "Bulk / delay-tolerant")],
               "Mix sync and async to match the nature of each task"),
    }
    (t, s), cA, cB, labels, rows, foot = D[lang]
    V.compare_two(t, s, cA, cB, rows, out, footer=foot, rowlabels=labels)


# ── sap-pi-overview-01 : PI 전 vs 후 → 비교형(Before/After) ──
def pi_overview(lang, out):
    D = {
        "ko": (("SAP PI, 매장만 바꾸면 레시피는 그대로", "시스템만 바꾸면 비싼 엑셀 하나 더 사는 셈"),
               ("PI 없이", "시스템만 교체", "berry"), ("PI 후", "프로세스 재설계", "teal"),
               ["흐름", "데이터", "주체", "결과"],
               [("수작업으로 끊김", "통합돼 이어짐"),
                ("부서마다 따로", "한 흐름으로 공유"),
                ("IT 팀이 떠맡음", "현업이 주인공"),
                ("비싼 엑셀", "일하는 방식이 바뀜")],
               "PI는 IT의 일이 아니다 — 현업이 프로세스를 다시 그리는 활동이다"),
        "en": (("SAP PI: A New Storefront Won't Change the Recipe", "Swapping only the system just buys a pricier Excel"),
               ("Without PI", "system only", "berry"), ("With PI", "process redesign", "teal"),
               ["Flow", "Data", "Owner", "Result"],
               [("Broken, manual", "Integrated, continuous"),
                ("Siloed per team", "Shared in one flow"),
                ("Dumped on IT", "Business leads it"),
                ("A pricier Excel", "The way of working changes")],
               "PI isn't IT's job — it's the business redrawing its own processes"),
    }
    (t, s), cA, cB, labels, rows, foot = D[lang]
    V.compare_two(t, s, cA, cB, rows, out, footer=foot, rowlabels=labels)


# ── sap-data-types-01 : config/master/transaction 3층위 → 계층 ──
def data_types(lang, out):
    D = {
        "ko": ("SAP 데이터 3층위, 오류를 어디서 볼까",
               "매장 규칙 · 식자재 기준 · 그날의 주문 기록",
               [("컨피규레이션", "매장 운영 규칙 — 거의 안 바뀌는 설정"),
                ("마스터", "식자재 기준표 — 반복 사용되는 기준 정보"),
                ("트랜잭션", "그날그날의 주문 기록 — 실제 업무 데이터")],
               "오류가 나면 이 세 층위 중 어디를 먼저 볼지 구분하는 눈이 실력"),
        "en": ("SAP's 3 Data Layers: Where to Look",
               "Shop rules · ingredient standards · the day's orders",
               [("Configuration", "Shop operating rules — settings rarely change"),
                ("Master", "Ingredient standards — reused reference data"),
                ("Transaction", "The day's order records — actual work data")],
               "The skill is knowing which of the three layers to check first"),
    }
    t, s, levels, footer = D[lang]
    V.hierarchy(t, s, levels, out, footer=footer)


# ── sap-org-structure-master-data-01 : 조직구조 포함관계 → 계층 ──
def org_structure(lang, out):
    D = {
        "ko": ("SAP 조직 구조, 건물의 뼈대",
               "위가 아래를 품는다 — 한 번 잡으면 바꾸기 어렵다",
               [("클라이언트", "레스토랑 그룹 전체 — 시스템의 가장 큰 단위"),
                ("회사 코드", "강남점 법인 — 독립된 회계 장부 단위"),
                ("플랜트", "실제 요리가 이뤄지는 매장 — 생산·재고 핵심"),
                ("저장 위치", "냉장·상온 창고 — 플랜트 안 물리적 보관 장소")],
               "건물 없이 가구를 놓을 수 없듯, 조직 구조 없이 기준정보는 못 선다"),
        "en": ("SAP Org Structure: The Building's Frame",
               "Each level contains the next — hard to change once set",
               [("Client", "The whole restaurant group — the top unit"),
                ("Company Code", "A legal entity — an independent set of books"),
                ("Plant", "The shop where cooking happens — production & stock"),
                ("Storage Location", "Cold / dry storage — a physical spot in the plant")],
               "As furniture needs a building, master data needs an org structure"),
    }
    t, s, levels, footer = D[lang]
    V.hierarchy(t, s, levels, out, footer=footer)


# ── sap-circular-bom-01 : 재작업 순환 → 순환형 ──
def circular_bom(lang, out):
    D = {
        "ko": ("SAP 순환 BOM, 불량을 되돌리는 고리",
               "완성품이 다시 자기 재료가 되는 재작업 구조",
               [("완성품", "정상 완제품이 생산된다"),
                ("불량 발견", "검사에서 재작업 대상이 나온다"),
                ("재작업 투입", "불량품을 자기 BOM의 재료로 다시 넣는다"),
                ("재완성", "고쳐서 다시 정상 완제품이 된다")],
               "BOM 등록 화면에서 '순환 허용'에 체크해야 저장된다"),
        "en": ("SAP Circular BOM: The Rework Loop",
               "A finished good becomes its own component again",
               [("Finished good", "A normal finished product is made"),
                ("Defect found", "Inspection flags it for rework"),
                ("Rework input", "The defect re-enters its own BOM"),
                ("Re-finished", "Repaired back into a good product")],
               "Tick 'allow recursion' in the BOM screen to save it"),
    }
    t, s, steps, note = D[lang]
    V.cycle(t, s, steps, out, center_label=("재작업" if lang == "ko" else "Rework"))


BUILDERS = {
    "sap-batch-management-01": batch_management,
    "sap-batch-job-01": batch_job,
    "sap-mes-role-01": mes_role,
    "sap-mes-interface-01": mes_interface_01,
    "sap-mes-interface-02": mes_interface_02,
    "sap-pi-overview-01": pi_overview,
    "sap-data-types-01": data_types,
    "sap-org-structure-master-data-01": org_structure,
    "sap-circular-bom-01": circular_bom,
}

# mes-role-01 은 원본이 png. 확장자는 러너가 마크다운 참조를 따르지만
# 단독 실행 시엔 jpg로 저장한다(검수용).
_PNG = {"sap-mes-role-01"}

if __name__ == "__main__":
    for slug, fn in BUILDERS.items():
        ext = ".png" if slug in _PNG else ".jpg"
        fn("ko", os.path.join(OUT, f"{slug}{ext}"))
        fn("en", os.path.join(OUT, f"{slug}_en{ext}"))
