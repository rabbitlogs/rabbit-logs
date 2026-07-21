# -*- coding: utf-8 -*-
"""템플릿 기반 도식 묶음 3."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from templates import steps, duo, matrix

STATUS_FLOW = {
    "ko": dict(banner="생산오더 상태", sub="요리 한 접시의 순서",
        headline="각 단계가 되어야 다음 작업이 허가된다",
        cards=[("CRTD", ["재료 준비", "오더 생성 · 수정 가능"]),
               ("REL", ["요리 시작", "자재 출고 · 공정 가능"]),
               ("CNF", ["공정 완료", "작업 확인 도장"]),
               ("DLV", ["완성 · 입고", "창고에 입고됨"]),
               ("TECO", ["주방 마감", "더 이상 변경 잠금"])]),
    "en": dict(banner="Production order status", sub="the order of a single dish",
        headline="Each stage unlocks the work that follows",
        cards=[("CRTD", ["Ingredients ready", "Order can still be edited"]),
               ("REL", ["Cooking starts", "Issue materials, run operations"]),
               ("CNF", ["Operation done", "The confirmation stamp"]),
               ("DLV", ["Finished, received", "Stock enters the warehouse"]),
               ("TECO", ["Kitchen closed", "Locked against further change"])]),
}

INTEGRATION_TEST = {
    "ko": dict(banner="통합 테스트", sub="모듈이 맞물려 흐르는가",
        headline="주문에서 수금까지, 모듈을 넘나드는 하나의 흐름",
        cards=[("SD · 판매 오더 등록", ["영업 담당"]),
               ("MM · 제품 출고", ["물류 담당"]),
               ("FI · 세금계산서 발행", ["회계 담당"]),
               ("FI · 수금 처리", ["회계 담당"])]),
    "en": dict(banner="Integration testing", sub="do the modules mesh?",
        headline="Order to cash — one flow crossing every module",
        cards=[("SD · Sales order", ["Sales team"]),
               ("MM · Goods issue", ["Logistics team"]),
               ("FI · Invoice", ["Finance team"]),
               ("FI · Payment received", ["Finance team"])]),
}

PP_MASTER_DATA = {
    "ko": dict(banner="SAP PP 기준정보 핵심 4가지", sub="레시피 하나가 완성되는 데 필요한 정보들",
        headline="무엇을, 무엇으로, 어떻게, 어떤 조합으로",
        cards=[("자재 마스터", ["모든 자재의 기본 정보", "제품 · 반제품 · 원재료", "메뉴판의 각 요리"]),
               ("BOM", ["제품을 만드는 재료 목록", "자재 명세서", "요리의 레시피"]),
               ("라우팅", ["작업 순서와 공정 경로", "조리 순서 · 동선", ""]),
               ("생산버전", ["BOM과 라우팅의 짝", "레시피 + 조리법 세트", ""])]),
    "en": dict(banner="The four PP master data objects", sub="what one recipe needs to exist",
        headline="What, from what, how, and in which combination",
        cards=[("Material master", ["Basic data for every material", "Finished, semi-finished, raw",
                                    "Each dish on the menu"]),
               ("BOM", ["The list of components", "The bill of materials", "The recipe itself"]),
               ("Routing", ["Operation sequence and path", "The cooking order", ""]),
               ("Production version", ["The BOM and routing pair", "Recipe plus method", ""])]),
}

WIP_OVERVIEW = {
    "ko": dict(banner="WIP, 원자재와 완제품 사이", sub="아직 접시에 담기지 않았을 뿐, 이미 가치를 지닌 자산",
        headline="같은 WIP를 세 사람이 다르게 본다",
        cards=[("PP · 생산", ["생산 라인의 정체기", "쌓이면 병목 신호"]),
               ("CO · 원가", ["숨은 자산의 근거", "결산 안 하면 자산 누락"]),
               ("MM · 재고", ["미래 계획의 나침반", "곧 완성될 공급 물량"])]),
    "en": dict(banner="WIP — between raw material and finished goods", sub="not yet plated, but already an asset",
        headline="Three people see the same WIP differently",
        cards=[("PP · Production", ["A stall on the line", "Piling up signals a bottleneck"]),
               ("CO · Costing", ["Evidence of a hidden asset", "Skip it and assets go missing"]),
               ("MM · Inventory", ["A compass for planning", "Supply about to be finished"])]),
}

BEST_PRACTICE = {
    "ko": dict(banner="SAP Best Practice 흐름", sub="표준에서 우리 회사 설정까지",
        headline="글로벌 표준을 우리 회사에 맞게 조정해가는 3단계",
        cards=[("글로벌 표준", ["SAP Best Practice", "수천 개 기업의", "성공 사례를 정제한", "업종별 표준 프로세스"]),
               ("Fit/Gap 분석", ["표준과 현실 비교", "표준에 맞춰보고(Fit)", "꼭 필요한 예외만", "따로 처리(Gap)"]),
               ("우리 회사 설정", ["맞춤 조정 완료", "회사의 강점은 살리고", "표준은 최대한", "그대로 활용"])]),
    "en": dict(banner="The SAP Best Practice flow", sub="from the standard to your own configuration",
        headline="Three steps that shape a global standard to your company",
        cards=[("Global standard", ["SAP Best Practice", "Industry processes distilled",
                                    "from thousands of", "successful companies"]),
               ("Fit/Gap analysis", ["Compare standard to reality", "Fit where you can,",
                                     "handle only the essential", "exceptions as gaps"]),
               ("Your configuration", ["Tailoring complete", "Keep what makes you strong,",
                                       "use the standard", "wherever possible"])]),
}

BUILD_DIFFICULTY = {
    "ko": dict(banner="SAP 구축 프로젝트 5단계", sub="새 매장을 여는 과정처럼",
        headline="단계마다 빠지기 쉬운 함정이 있습니다",
        cards=[("착수", ["자리 잡기", "\"옆 가게처럼 해주세요\"", "업종 같아도 속사정은 다름"]),
               ("블루프린트", ["설계도 그리기", "\"우리 업무는 단순해요\"", "파고들면 수기 예외가 잔뜩"]),
               ("구축 · 개발", ["본격 공사", "\"구두로 합의했잖아요\"", "기록 없는 합의가 가장 위험"]),
               ("테스트", ["오픈 전 점검", "새 요구사항 쏟발 시기", "직접 써봐야 불편함이 보임"]),
               ("안정화", ["가동 · 정착", "오픈은 끝이 아닌 시작", "대응 속도가 성패를 가름"])]),
    "en": dict(banner="Five stages of an SAP project", sub="like opening a new restaurant",
        headline="Every stage has a trap that is easy to fall into",
        cards=[("Kick-off", ["Finding your feet", "\"Just do what they did\"",
                             "Same industry, different reality"]),
               ("Blueprint", ["Drawing the plans", "\"Our work is simple\"",
                              "Dig in and manual exceptions appear"]),
               ("Build", ["Construction proper", "\"But we agreed verbally\"",
                          "Undocumented agreements hurt most"]),
               ("Test", ["Checks before opening", "New requirements pour in",
                         "Problems show only in real use"]),
               ("Stabilise", ["Running and settling", "Go-live is a start, not an end",
                              "Response speed decides success"])]),
}

CPIM = {
    "ko": dict(banner="CPIM", sub="생산·재고관리 국제 자격",
        headline="SAP 자격증과 무엇이 다른가",
        left=("CPIM", "이론 · 개념 중심",
              ["생산 · 재고관리의 원리", "특정 시스템에 종속되지 않음",
               "APICS(ASCM)가 주관", "왜 그렇게 하는지를 배운다"]),
        right=("SAP 자격증", "도구 · 조작 중심",
               ["SAP 시스템 사용법", "SAP 제품에 특화됨",
                "SAP가 직접 주관", "어떻게 하는지를 배운다"])),
    "en": dict(banner="CPIM", sub="an international production and inventory credential",
        headline="How it differs from an SAP certification",
        left=("CPIM", "Concept-led",
              ["The principles behind planning", "Not tied to any one system",
               "Run by APICS (ASCM)", "Teaches why things are done"]),
        right=("SAP certification", "Tool-led",
               ["How to operate SAP", "Specific to SAP products",
                "Run by SAP itself", "Teaches how things are done"])),
}

CUTOVER = {
    "ko": dict(banner="컷오버", sub="이사하는 날",
        headline="기존 시스템에서 새 시스템으로 넘어가는 단 한 번의 순간",
        cards=[("사전 준비", ["런북 작성", "리허설 반복", "역할 · 시간 배분"]),
               ("데이터 이전", ["기준정보 먼저", "잔액 · 재고 순서로", "건수 검증 필수"]),
               ("검증 · 판단", ["체크리스트 확인", "Go 또는 Rollback", "되돌릴 기준 사전 합의"])]),
    "en": dict(banner="Cutover", sub="moving day",
        headline="The single moment you cross from the old system to the new",
        cards=[("Preparation", ["Write the runbook", "Rehearse repeatedly",
                                "Assign roles and timings"]),
               ("Data migration", ["Master data first", "Then balances and stock",
                                   "Always verify record counts"]),
               ("Verify and decide", ["Work the checklist", "Go, or roll back",
                                      "Agree the trigger in advance"])]),
}

CHANGE_MGMT = {
    "ko": dict(banner="변화 저항 곡선", sub="네 단계를 거쳐 새 시스템에 정착",
        headline="누구나 겪는 감정의 흐름, 알면 덜 힘듭니다",
        cards=[("충격 · 부정", ["\"왜 바꾸나요,", "기존이 편한데요\""]),
               ("분노 · 좌절", ["생산성 최저점", "\"왜 이렇게 느려요\""]),
               ("탐색 · 수용", ["작은 성공 경험", "\"한번 써봐야겠다\""]),
               ("통합", ["\"이제 이게 편해요\"", "완전히 자리잡음"])]),
    "en": dict(banner="The change resistance curve", sub="four stages to settling in",
        headline="Everyone goes through it — knowing helps",
        cards=[("Shock · denial", ["\"Why change it?", "The old way was fine\""]),
               ("Anger · frustration", ["Productivity bottoms out", "\"Why is this so slow?\""]),
               ("Exploration", ["Small wins accumulate", "\"Maybe I'll try it properly\""]),
               ("Integration", ["\"This is easier now\"", "Fully settled in"])]),
}

CBO = {
    "ko": dict(banner="표준 T-CODE vs Z코드(CBO)", sub="편의성과 통제, 그 사이의 줄다리기",
        headline="정답은 한쪽이 아니라, 두 장점을 살리고 단점을 줄이는 균형이다",
        left=("표준 T-CODE", "SAP 기본 제공",
              ["강력하고 범용적", "회사 규칙은 자동 반영 안 됨",
               "사용자마다 다르게 쓰면 혼란", "통제 · 관리가 어려움"]),
        right=("Z코드 (CBO)", "Customer Bolt-On",
               ["회사가 직접 추가 개발", "이름은 Z · Y로 시작",
                "회사 규칙이 이미 반영됨", "쌓이면 블랙박스화 위험"])),
    "en": dict(banner="Standard T-codes vs Z-codes (CBO)", sub="convenience against control",
        headline="The answer is balance — keep both strengths, limit both weaknesses",
        left=("Standard T-code", "Shipped by SAP",
              ["Powerful and general-purpose", "Your rules are not built in",
               "Different habits cause confusion", "Harder to control and govern"]),
        right=("Z-code (CBO)", "Customer Bolt-On",
               ["Built by your own company", "Names begin with Z or Y",
                "Company rules already embedded", "Piles up into a black box"])),
}

DATA_TYPES = {
    "ko": dict(banner="SAP 데이터 유형 세 가지", sub="운영 규칙과 기준표가 모여, 매일의 기록을 만든다",
        headline="컨피규레이션 · 마스터 데이터 · 트랜잭션 데이터",
        cards=[("컨피규레이션", ["매장 운영 규칙", "주문번호 부여 방식", "변경 거의 없음 · 초기 세팅"]),
               ("마스터 데이터", ["식자재 기준표", "자재 마스터 · BOM(레시피)", "변경 낮음 · 필요시만"]),
               ("트랜잭션 데이터", ["그날의 주문 · 영수증", "판매오더 → 출고지시 → 매출전표", "변경 매우 높음 · 실시간 발생"])]),
    "en": dict(banner="Three kinds of SAP data", sub="rules and reference tables shape the daily record",
        headline="Configuration · master data · transaction data",
        cards=[("Configuration", ["The rules of the restaurant", "How order numbers are assigned",
                                  "Rarely changes — set up once"]),
               ("Master data", ["The ingredient reference", "Material master, BOM (recipe)",
                                "Changes seldom, only as needed"]),
               ("Transaction data", ["Today's orders and receipts", "Sales order → delivery → invoice",
                                     "Changes constantly, in real time"])]),
}

MES_ROLE = {
    "ko": dict(banner="SAP MES", sub="총괄 셰프(SAP)와 주방 팀(MES)의 역할 분담",
        headline="계획은 위에서, 실행은 현장에서",
        left=("SAP (ERP)", "총괄 셰프 | 계획의 중심",
              ["생산오더 생성 — 무엇을, 얼마나, 언제", "BOM · Routing 관리 — 레시피와 조리 순서",
               "자재 소요량 계획(MRP)", "원가 분석 · 정산 — 계획 vs 실제",
               "시간 단위: 월 / 주 / 일"]),
        right=("MES", "주방 팀 | 실행의 중심",
               ["실시간 생산 실행 · 추적", "설비 상태 모니터링 — 온도 · 라인 상태",
                "품질 · 불량 관리 — 로트 단위 추적", "자재 실사용량 추적",
                "시간 단위: 분 / 초 (실시간)"])),
    "en": dict(banner="SAP and MES", sub="the head chef and the kitchen team",
        headline="Planning happens above; execution happens on the floor",
        left=("SAP (ERP)", "Head chef | the planning centre",
              ["Creates production orders — what, how much, when",
               "Manages BOM and routing", "Material requirements planning (MRP)",
               "Cost analysis — plan versus actual", "Time unit: month / week / day"]),
        right=("MES", "Kitchen team | the execution centre",
               ["Real-time execution and tracking", "Equipment monitoring — temperature, line state",
                "Quality and defects — traced by lot", "Tracks actual material consumption",
                "Time unit: minutes / seconds"])),
}

PLANNED_VS_PRODUCTION = {
    "ko": dict(banner="계획오더 vs 생산오더", sub="준비 초안에서 확정된 실행 지시서로",
        headline="MRP가 만든 '초안'을 확정하면 '실행 지시서'가 된다",
        left=("계획오더", "Planned Order",
              ["MRP가 자동 생성", "수량 · 일정 변경 자유로움",
               "아직 실제 생산 아님", "\"이렇게 만들 예정\""]),
        right=("생산오더", "Production Order",
               ["계획오더를 변환해 생성", "확정 — 함부로 못 바꿈",
                "실제 생산 · 자재출고 진행", "\"지금부터 만든다\""])),
    "en": dict(banner="Planned order vs production order", sub="from draft to firm instruction",
        headline="Convert the MRP draft and it becomes a work order",
        left=("Planned order", "Created by MRP",
              ["Generated automatically by MRP", "Quantity and dates change freely",
               "Not yet real production", "\"This is what we intend to make\""]),
        right=("Production order", "The firm instruction",
               ["Created by converting the plan", "Firm — not changed lightly",
                "Real production and goods issue", "\"We start making it now\""])),
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
    "sap-production-order-status-flow": _steps(STATUS_FLOW),
    "sap-integration-test-flow":        _steps(INTEGRATION_TEST),
    "sap-pp-master-data":               _steps(PP_MASTER_DATA),
    "sap-wip-overview":                 _steps(WIP_OVERVIEW),
    "sap-best-practice-01":             _steps(BEST_PRACTICE),
    "sap-build-project-difficulty-01":  _steps(BUILD_DIFFICULTY),
    "sap-cutover-01":                   _steps(CUTOVER),
    "sap-change-management-01":         _steps(CHANGE_MGMT),
    "sap-data-types-01":                _steps(DATA_TYPES),
    "sap-cpim-01":                      _duo(CPIM),
    "sap-cbo-comparison":               _duo(CBO),
    "sap-mes-role-01":                  _duo(MES_ROLE),
    "sap-planned-vs-production-order":  _duo(PLANNED_VS_PRODUCTION),
}
