# -*- coding: utf-8 -*-
"""템플릿 기반 도식 묶음 4 — 마지막 그룹."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from templates import steps, duo, matrix

AUTOCOMPLETE = {
    "ko": dict(banner="SAP 자동완성 설정", sub="입력 이력 관리하기",
        headline="이력을 켜둘까, 끌까, 일부만 지울까",
        left=("이력 그대로 사용", None,
              ["예전 값이 계속 노출", "오타 · 옛 데이터도", "자동완성 후보에 남음"]),
        right=("설정 후 정리", None,
               ["옵션에서 이력 삭제 · 끄기", "필요한 항목만", "깔끔하게 유지"])),
    "en": dict(banner="SAP autocomplete settings", sub="managing input history",
        headline="Keep the history, turn it off, or clear just part of it",
        left=("History left as is", None,
              ["Old values keep appearing", "Typos and stale data stay",
               "in the suggestion list"]),
        right=("After cleaning up", None,
               ["Delete or disable history in options", "Keep only what you need",
                "and stay tidy"])),
}

BATCH_JOB = {
    "ko": dict(banner="SAP 배치잡", sub="야간에 혼자 도는 자동 정산",
        headline="예약부터 모니터링까지 두 개의 T-CODE",
        left=("SM36", "배치잡 예약 등록",
              ["언제, 무엇을,", "얼마나 자주", "실행할지 설정"]),
        right=("SM37", "실행 결과 모니터링",
               ["성공 · 실패 여부 확인", "로그를 보고", "문제를 진단"])),
    "en": dict(banner="SAP background jobs", sub="the settlement that runs overnight",
        headline="Two T-codes: one to schedule, one to watch",
        left=("SM36", "Schedule the job",
              ["Set when, what,", "and how often", "it should run"]),
        right=("SM37", "Monitor the results",
               ["Check success or failure", "Read the log", "and diagnose problems"])),
}

EXAM_FORMAT = {
    "ko": dict(banner="SAP 자격증 시험, 두 가지 유형", sub="응시자가 고르는 것이 아니라, 과목이 유형을 정한다",
        headline="시스템 실습 시험과 AI 시나리오 시험",
        left=("시스템 실습 시험", "System Based Exam",
              ["직접 시스템에 들어가 수행", "개발 · 세팅 위주 과목",
               "8개 실습 과제, 최대 3시간", "영어로만 평가 (번역 끄기)",
               "SAP GUI · Fiori · BTP · Eclipse"]),
        right=("AI 시나리오 시험", "AI Scenario Exam",
               ["손님 응대를 롤플레잉", "컨설팅 · 영업 위주 과목",
                "예약 없이 즉시 응시", "한국어 완벽 지원",
                "카메라 켜고 진행"])),
    "en": dict(banner="Two SAP exam formats", sub="the subject decides the format, not the candidate",
        headline="A hands-on system exam and an AI scenario exam",
        left=("System based exam", "Hands-on in the system",
              ["Performed inside a real system", "Development and configuration subjects",
               "Eight tasks, up to three hours", "Assessed in English only",
               "SAP GUI · Fiori · BTP · Eclipse"]),
        right=("AI scenario exam", "Role-play with an AI",
               ["Role-play a client conversation", "Consulting and sales subjects",
                "Sit it immediately, no booking", "Full Korean language support",
                "Taken with the camera on"])),
}

FIELD_NAMES = {
    "ko": dict(banner="AUFK 레시피 카드", sub="필드 이름 읽는 법",
        headline="독일어 원어를 쪼개면, 외우지 않아도 뜻이 보인다",
        cols=[("필드 이름", "생산오더 레시피 카드"), ("독일어 원어 쪼개보기", "앞 세 글자만 봐도 뜻이 짐작된다")],
        rows=["AUFNR", "AUART", "WERKS", "GSTRP", "ERNAM"],
        cells=[["주문서 번호표", "Auftrag(주문) + Nummer(번호)"],
               ["요리 종류", "Auftrag + Art(종류)"],
               ["요리할 주방", "Werk(공장, 작업장)"],
               ["조리 시작 예정", "Geplant(계획된) + Start + Termin(일정)"],
               ["작성한 셰프", "Erfasst(기록된) von(~에 의해) + Name"]],
        foot="필드 이름 = 레시피 재료명 — 원어를 쪼개면 규칙이 보입니다"),
    "en": dict(banner="The AUFK recipe card", sub="how to read SAP field names",
        headline="Split the German root and the meaning appears without memorising",
        cols=[("Field name", "Production order card"), ("German root, split apart", "The first three letters give it away")],
        rows=["AUFNR", "AUART", "WERKS", "GSTRP", "ERNAM"],
        cells=[["Order number tag", "Auftrag (order) + Nummer (number)"],
               ["Type of dish", "Auftrag + Art (type)"],
               ["Which kitchen", "Werk (plant, workshop)"],
               ["Planned start", "Geplant (planned) + Start + Termin (date)"],
               ["Chef who wrote it", "Erfasst (recorded) von (by) + Name"]],
        foot="Field names are ingredient names — split the root and the pattern shows"),
}

PI_OVERVIEW = {
    "ko": dict(banner="SAP PI 전후", sub="레스토랑 운영 흐름 비교",
        headline="같은 SAP, 같은 레스토랑이라도 PI를 거쳤는지가 다른 결과를 만든다",
        left=("끊어진 흐름", "PI 이전",
              ["주문을 손으로 직접 메모", "주방에 메모 전달 — 사람이 직접 들고 이동",
               "재고 파악 안 됨 — 대기 · 재고 실시간 확인 불가",
               "사장이 영수증 집계 — 밤새워 수기로 정산"]),
        right=("이어진 흐름", "PI 이후",
               ["주문이 POS 입력 — 입력 즉시 시스템 반영",
                "주방 모니터 자동 표시 — 전달 과정 없이 즉시 확인",
                "재고 실시간 업데이트 — 기준치 이하 시 발주 신호",
                "마감 버튼 자동 정산 — 수기 집계 과정 사라짐"])),
    "en": dict(banner="Before and after SAP PI", sub="comparing how the restaurant runs",
        headline="Same SAP, same restaurant — going through PI changes the outcome",
        left=("A broken flow", "Before PI",
              ["Orders written down by hand", "Someone physically carries the note to the kitchen",
               "No stock visibility — waits and levels unknown",
               "The owner tallies receipts by hand at night"]),
        right=("A connected flow", "After PI",
               ["Orders entered at the POS — live in the system at once",
                "The kitchen screen shows it — no hand-off step",
                "Stock updates in real time — reorder signals fire automatically",
                "One closing button settles the day — no manual tally"])),
}

UAT = {
    "ko": dict(banner="성공하는 UAT의 4가지 조건", sub="현업이 직접 여는 최종 리허설",
        headline="준비 없는 UAT는 형식적인 사인에 그칩니다",
        cards=[("현실 기반 시나리오", ["단순 기능이 아니라", "주문 접수부터", "세금계산서 발행까지", "실제 업무의 처음과 끝"]),
               ("실제 데이터", ["'테스트'가 아니라", "㈜대한전자 같은", "실제 운영 데이터로", "숨은 오류를 잡는다"]),
               ("사용자 주도", ["주인공은 컨설턴트가", "아니라 현업 사용자", "사소한 불편도", "모두 이야기한다"]),
               ("사전 교육", ["조작법을 먼저 익혀야", "조작 미숙을 결함으로", "오해하지 않고", "테스트가 효율적이다"])]),
    "en": dict(banner="Four conditions for a successful UAT", sub="the final rehearsal, led by the business",
        headline="Without preparation, UAT becomes a formality and a signature",
        cards=[("Realistic scenarios", ["Not isolated features but", "the whole job end to end,",
                                        "from taking an order", "to issuing the invoice"]),
               ("Real data", ["Not \"test test test\" but", "actual operational data",
                              "with real customer names —", "it surfaces hidden errors"]),
               ("User-led", ["The lead role belongs to", "business users, not consultants",
                             "Every small annoyance", "gets raised out loud"]),
               ("Training first", ["Learn the operations first", "so clumsiness is not",
                                   "mistaken for a defect —", "the test stays efficient"])]),
}

WORK_CENTER = {
    "ko": dict(banner="작업장(Work Center)", sub="요리가 실제로 이뤄지는 자리",
        headline="누가, 어디서, 얼마나 걸려 만드는가",
        cards=[("능력(Capacity)", ["하루에 몇 시간", "가동할 수 있는가", "설비 · 인원 기준"]),
               ("표준값(Formula)", ["작업 시간 계산식", "준비 시간 + 가공 시간", "수량에 따라 자동 계산"]),
               ("원가 배부", ["작업장별 시간당 단가", "가동 시간 × 단가", "= 가공비"])]),
    "en": dict(banner="The work center", sub="where the cooking actually happens",
        headline="Who makes it, where, and how long it takes",
        cards=[("Capacity", ["How many hours a day", "it can actually run",
                             "Based on equipment and staff"]),
               ("Standard values", ["The formula for work time", "Setup time plus processing time",
                                    "Calculated from the quantity"]),
               ("Cost allocation", ["An hourly rate per work center", "Run time × rate",
                                    "= the processing cost"])]),
}

ROUTING = {
    "ko": dict(banner="라우팅(Routing)", sub="조리 순서와 동선",
        headline="같은 재료라도 순서가 다르면 다른 요리가 된다",
        cards=[("공정 순서", ["0010, 0020, 0030 …", "번호 순으로 진행", "순서를 건너뛸 수 없다"]),
               ("작업장 지정", ["각 공정을 어느", "작업장에서 할지", "지정한다"]),
               ("표준 시간", ["준비 · 가공 · 대기", "공정별 소요 시간", "일정 계산의 근거"])]),
    "en": dict(banner="Routing", sub="the cooking sequence and path",
        headline="The same ingredients in a different order make a different dish",
        cards=[("Operation sequence", ["0010, 0020, 0030 …", "Carried out in number order",
                                       "Steps cannot be skipped"]),
               ("Work center assignment", ["Which work center", "performs each operation",
                                           "is specified here"]),
               ("Standard times", ["Setup, processing, queue", "Time required per operation",
                                   "The basis for scheduling"])]),
}

CLEAN_CORE = {
    "ko": dict(banner="Joule로 가는 길, 순서가 거꾸로다", sub="쓰고 싶은 것은 맨 위지만, 손대야 할 것은 맨 아래부터",
        headline="",
        cards=[("최종 목표 — SAP Joule", ["자연어로 지시하는", "SAP 전용 AI 비서"]),
               ("전제 조건 — 클린코어", ["표준은 깨끗하게,", "확장은 BTP에 얹어", "붙이는 구조"]),
               ("선결 과제 — Z-코드 정리", ["표준을 직접 고쳐 쌓인", "커스텀 코드부터 진단"])]),
    "en": dict(banner="The road to Joule runs backwards", sub="what you want is at the top; what you must fix is at the bottom",
        headline="",
        cards=[("The goal — SAP Joule", ["An SAP-native AI assistant", "you instruct in plain language"]),
               ("The prerequisite — clean core", ["Keep the standard clean and", "put extensions on BTP",
                                                  "instead of in the core"]),
               ("The first task — Z-code cleanup", ["Start by auditing the custom", "code piled onto the standard"])]),
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


def _matrix(spec):
    def build(lang, out):
        t = spec[lang]
        matrix(out, t["banner"], t["headline"], t["cols"], t["rows"], t["cells"],
               sub=t.get("sub"), foot=t.get("foot"))
    return build


BUILDERS = {
    "sap-autocomplete-01":     _duo(AUTOCOMPLETE),
    "sap-batch-job-01":        _duo(BATCH_JOB),
    "sap-exam-format-02":      _duo(EXAM_FORMAT),
    "sap-pi-overview-01":      _duo(PI_OVERVIEW),
    "sap-field-names-01":      _matrix(FIELD_NAMES),
    "sap-uat-01":              _steps(UAT),
    "study-pp-work-center-01": _steps(WORK_CENTER),
    "study-pp-routing-01":     _steps(ROUTING),
    "clean-core-dependency":   _steps(CLEAN_CORE),
}
