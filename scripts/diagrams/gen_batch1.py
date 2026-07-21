# -*- coding: utf-8 -*-
"""템플릿 기반 도식 묶음 1 — 단계형/2열형/표형."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from templates import steps, duo, matrix

# ── sap-test-flow ───────────────────────────────────────────────────────────
TEST_FLOW = {
    "ko": dict(
        banner="SAP 테스트 5단계", sub="매장을 여는 검증",
        headline="건너뛰거나 순서를 바꿀 수 없는 하나의 여정",
        cards=[("Fit/Gap", ["콘셉트가 맞는가", "표준과 우리 매장 비교"]),
               ("프로토타입", ["시범 매장 보기", "시제품 미리 체험"]),
               ("단위 테스트", ["재료 품질 검사", "부품 하나씩 검증"]),
               ("통합 테스트", ["주방·홀 연동", "전체 흐름 점검"]),
               ("UAT", ["사장 최종 점검", "실사용자 승인"])],
    ),
    "en": dict(
        banner="The five SAP test stages", sub="the checks that open the restaurant",
        headline="One journey — no skipping steps, no changing the order",
        cards=[("Fit/Gap", ["Does the concept fit?", "Standard vs our restaurant"]),
               ("Prototype", ["See the pilot store", "Try the sample early"]),
               ("Unit test", ["Ingredient quality check", "Verify parts one by one"]),
               ("Integration", ["Kitchen-to-floor linkage", "Check the whole flow"]),
               ("UAT", ["The owner's final check", "Real-user sign-off"])],
    ),
}

# ── sap-pp-overview-01 ──────────────────────────────────────────────────────
PP_OVERVIEW = {
    "ko": dict(
        banner="SAP PP 흐름", sub="생산 계획이 완성되는 과정",
        headline="기준정보에서 다른 모듈 연결까지 네 단계",
        cards=[("기준정보", ["BOM · Routing", "레시피와", "조리 순서"]),
               ("계획", ["MRP가", "장보기 목록을", "자동 계산"]),
               ("실행", ["생산오더 발행", "실적을 CNF로", "확정"]),
               ("연결", ["MM · QM · CO 등", "다른 모듈과", "데이터 연동"])],
    ),
    "en": dict(
        banner="The SAP PP flow", sub="how a production plan comes together",
        headline="Four steps from master data to module integration",
        cards=[("Master data", ["BOM · Routing", "the recipe and", "the cooking order"]),
               ("Planning", ["MRP calculates", "the shopping list", "automatically"]),
               ("Execution", ["Release the order,", "confirm results", "via CNF"]),
               ("Integration", ["Data flows to MM,", "QM, CO and other", "modules"])],
    ),
}

# ── sap-prototype-test-01 ───────────────────────────────────────────────────
PROTOTYPE = {
    "ko": dict(
        banner="프로토타입 테스트 흐름", sub="짓기 전에 보는 시범 매장",
        headline="도면으로 볼 때와 직접 만질 때는 완전히 다릅니다",
        cards=[("시범 매장 오픈", ["종이 설계도 대신", "실제로 만져보는", "최소한의 시제품"]),
               ("현업이 직접 확인", ["\"이건 우리 일과 달라요\"", "머리로 상상할 때 놓친", "진짜 요구사항 발견"]),
               ("설계 확정 · 수정", ["오픈 전에 고치면 싸고", "오픈 후에 고치면 비싸다", "큰 방향을 먼저 잡는다"])],
    ),
    "en": dict(
        banner="The prototype test flow", sub="a pilot store before you build",
        headline="Seeing a blueprint and touching the real thing are worlds apart",
        cards=[("Open the pilot", ["A minimal working build", "you can actually touch,", "not a paper design"]),
               ("Users try it", ["\"This isn't how we work\"", "Surfaces real requirements", "imagination would miss"]),
               ("Lock the design", ["Cheap to fix before launch,", "expensive after —", "settle direction first"])],
    ),
}

# ── sap-unit-test-01 (비교표) ───────────────────────────────────────────────
UNIT_TEST = {
    "ko": dict(
        banner="단위 테스트 vs 통합 테스트", sub="재료 검사와 요리 검사",
        headline="작은 부품부터 검사하고, 그다음 전체를 맞춰봅니다",
        cols=[("단위 테스트", "Unit Test"), ("통합 테스트", "Integration Test")],
        rows=["비유", "대상", "목적", "시점", "참여자"],
        cells=[["재료 하나의 품질 검사", "재료들을 합쳐 요리가 되는지"],
               ["작은 부품 하나 (프로그램 · 함수)", "여러 모듈이 연결된 업무 흐름 전체"],
               ["개별 기능의 논리 오류 발견", "모듈 간 연동 오류 발견"],
               ["개발 완료 직후", "단위 테스트 완료 후"],
               ["개발자 · 모듈 컨설턴트", "여러 컨설턴트 · 핵심 사용자"]],
        foot="재료 검사를 건너뛰면, 완성된 요리에서 원인을 찾느라 몇 배로 고생합니다",
    ),
    "en": dict(
        banner="Unit test vs integration test", sub="checking ingredients, then the dish",
        headline="Inspect the smallest parts first, then see how they fit together",
        cols=[("Unit test", "Unit Test"), ("Integration test", "Integration Test")],
        rows=["Analogy", "Scope", "Purpose", "Timing", "Who"],
        cells=[["Quality of one ingredient", "Whether the parts make a dish"],
               ["One small part (program, function)", "A whole flow across linked modules"],
               ["Logic errors in a single feature", "Errors in module-to-module linkage"],
               ["Right after development", "After unit tests pass"],
               ["Developers, module consultants", "Several consultants, key users"]],
        foot="Skip the ingredient check and you pay many times over hunting the cause later",
    ),
}

# ── sap-production-strategy-01 (비교표) ─────────────────────────────────────
STRATEGY = {
    "ko": dict(
        banner="MTS vs MTO", sub="뷔페와 스테이크 하우스",
        headline="재고를 먼저 쌓을까, 주문부터 받을까",
        cols=[("MTS", "재고 생산"), ("MTO", "주문 생산")],
        rows=["비유", "생산 시점", "재고", "납기", "적합 제품"],
        cells=[["뷔페 — 미리 차려둔 음식", "스테이크 하우스 — 주문 후 굽기 시작"],
               ["주문 전 미리 생산", "주문 접수 후 생산"],
               ["완제품 재고 보유", "원자재만 보유"],
               ["즉시 제공 가능", "생산 시간만큼 대기"],
               ["수요 예측 쉬운 제품", "맞춤 · 고가 제품"]],
        foot="정답은 하나가 아니라, 반제품까지만 미리 만드는 절충안도 있습니다",
    ),
    "en": dict(
        banner="MTS vs MTO", sub="the buffet and the steakhouse",
        headline="Build stock first, or wait for the order?",
        cols=[("MTS", "Make to stock"), ("MTO", "Make to order")],
        rows=["Analogy", "When", "Inventory", "Lead time", "Best for"],
        cells=[["Buffet — food laid out in advance", "Steakhouse — cooked once ordered"],
               ["Produced before the order", "Produced after the order"],
               ["Finished goods held", "Only raw materials held"],
               ["Available immediately", "Wait the production time"],
               ["Predictable demand", "Custom or high-value goods"]],
        foot="There is no single answer — many firms stop at semi-finished goods as a middle path",
    ),
}

# ── sap-pi-vs-implementation-01 (2열) ───────────────────────────────────────
PI_VS = {
    "ko": dict(
        banner="PI와 구축", sub="설계자와 시공자의 차이",
        headline="이상을 그리는 사람과, 현실로 만드는 사람",
        left=("PI", "Process Innovation",
              ["비즈니스 컨설턴트 중심", "As-Is 분석 → To-Be 설계",
               "예산 · 기술 제약보다 이상 우선", "\"어떻게 일해야 최적인가?\""]),
        right=("구축", "Implementation",
               ["모듈 · 기술 컨설턴트 중심", "To-Be → 실제 SAP 구현",
                "예산 · 인프라 · 표준 기능 고려", "\"현실에서 잘 돌아가게 하려면?\""]),
    ),
    "en": dict(
        banner="PI and implementation", sub="the architect and the builder",
        headline="One draws the ideal; the other makes it real",
        left=("PI", "Process Innovation",
              ["Led by business consultants", "As-Is analysis → To-Be design",
               "Ideal first, before budget and tech limits", "\"What is the best way to work?\""]),
        right=("Implementation", "Build",
               ["Led by module and tech consultants", "To-Be → actual SAP build",
                "Budget, infrastructure, standard features", "\"How do we make it run in practice?\""]),
    ),
}

# ── sap-password-asterisk-01 (2열) ──────────────────────────────────────────
ASTERISK = {
    "ko": dict(
        banner="SAP 비밀번호 별표", sub="자리표시자 문자 표시 옵션",
        headline="체크 여부가 계정 잠김을 좌우합니다",
        left=("옵션 켜짐(기본)", None,
              ["입력 칸에 별표 잔상", "이전 비밀번호 길이가 시각적으로 남음", "오타로 인한 잠김 위험"]),
        right=("옵션 끔(권장)", None,
               ["입력할 때만 별표 표시", "엔터 후 완전히 비워짐", "오타로 인한 잠김 방지"]),
    ),
    "en": dict(
        banner="SAP password asterisks", sub="the placeholder character option",
        headline="One checkbox decides whether your account locks",
        left=("Option on (default)", None,
              ["Asterisks linger in the field", "The old password length stays visible",
               "Risk of lockout from a typo"]),
        right=("Option off (recommended)", None,
               ["Asterisks show only while typing", "The field clears fully after Enter",
                "Prevents lockouts caused by typos"]),
    ),
}

# ── sap-dropdown-01 (2열) ───────────────────────────────────────────────────
DROPDOWN = {
    "ko": dict(
        banner="SAP 드롭다운 키 표시", sub="이름표에 코드 추가하기",
        headline="텍스트만 vs 코드+텍스트",
        left=("기본 상태", None, ["텍스트만 표시", "\"홍길동\" 처럼", "코드 없이 이름만"]),
        right=("설정 후", None, ["코드 + 텍스트 표시", "\"70012345 홍길동\"", "동명이인도 구분 가능"]),
    ),
    "en": dict(
        banner="SAP dropdown key display", sub="adding codes to the name tag",
        headline="Text only vs code plus text",
        left=("Default", None, ["Text only", "Just \"Jane Doe\"", "No code shown"]),
        right=("After the setting", None, ["Code plus text", "\"70012345 Jane Doe\"",
                                           "Tells duplicate names apart"]),
    ),
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
    "sap-test-flow":                 _steps(TEST_FLOW),
    "sap-pp-overview-01":            _steps(PP_OVERVIEW),
    "sap-prototype-test-01":         _steps(PROTOTYPE),
    "sap-unit-test-01":              _matrix(UNIT_TEST),
    "sap-production-strategy-01":    _matrix(STRATEGY),
    "sap-pi-vs-implementation-01":   _duo(PI_VS),
    "sap-password-asterisk-01":      _duo(ASTERISK),
    "sap-dropdown-01":               _duo(DROPDOWN),
}
