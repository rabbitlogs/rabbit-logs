# -*- coding: utf-8 -*-
"""
sap-mes-interface-01/02 — 본문 구조에 맞춘 전용 렌더, 두 이미지로 분리.

본문(sap-mes-interface.md)에는 두 개의 서로 다른 축이 나온다.
1) 연결 방식: RFC(직접 연결) vs PI/PO(중앙 관제) — sap-mes-interface-01
2) 소통 스타일: 동기 vs 비동기 — sap-mes-interface-02

01번은 박스+화살표로 SAP↔MES 연결 구조를 그대로 그려봤으나, 왕복 화살표의
색·굵기 구분이 흐릿하고 PI/PO 쪽은 편도만 그려져 어색했다. §9 대응표로
다시 보면 RFC vs PI/PO는 "대립·트레이드오프" 관계이므로, 박스 다이어그램
대신 이미 검증된 duo(2열 비교 카드 + 큰 키포인트) 템플릿으로 통일한다.
02번(동기/비동기)은 원래도 2카드였으므로 같은 duo 템플릿으로 맞춘다.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from templates import duo


MES_IF_1 = {
    "ko": dict(
        banner="SAP MES 인터페이스", sub="RFC vs PI/PO 연결 방식",
        headline="직접 통화할까, 중앙 관제를 거칠까",
        left=("RFC", "SAP ↔ MES 직접 연결",
              ["중간 단계 없이 바로 통신", "실시간 확인에 적합(동기 방식)",
               "한쪽 장애가 다른 쪽에 그대로 전파"],
              "직통 전화"),
        right=("PI / PO", "중간 시스템이 통신 관리",
               ["다운돼도 메시지 보관 후 재전송(안정성)", "WMS·QMS 등 여러 시스템과 동시 연결(유연성)",
                "통신 이력이 남아 추적 쉬움(모니터링)"],
               "중앙 관제"),
    ),
    "en": dict(
        banner="SAP MES interfaces", sub="RFC vs PI/PO",
        headline="Call directly, or route through a control tower?",
        left=("RFC", "SAP and MES connect directly",
              ["Direct communication, no middle layer", "Suited to real-time checks (synchronous)",
               "A failure on one side spreads to the other"],
              "The direct call"),
        right=("PI / PO", "A middle system manages traffic",
               ["Stores and resends messages if down (stability)",
                "Connects to WMS, QMS and more at once (flexibility)",
                "Full history makes tracing issues easy (monitoring)"],
               "The control tower"),
    ),
}

MES_IF_2 = {
    "ko": dict(
        banner="SAP MES 인터페이스", sub="소통 스타일",
        headline="동기 vs 비동기",
        left=("동기", "Synchronous",
              ["SAP가 요청 후 MES 응답까지 대기", "실시간 재고 확인 등 즉시 확인 필요할 때 적합"],
              "답장 올 때까지 대기"),
        right=("비동기", "Asynchronous",
               ["SAP가 전달 후 응답 기다리지 않고 다음 업무로", "대량 생산 계획 배치 전송에 적합",
                "수신 확인이 즉시 안 됨"],
               "시간 될 때 답장"),
    ),
    "en": dict(
        banner="SAP MES interfaces", sub="Communication style",
        headline="Synchronous vs asynchronous",
        left=("Synchronous", None,
              ["SAP waits for MES's reply before moving on", "Good for instant checks like live stock levels"],
              "Waits for the reply"),
        right=("Asynchronous", None,
               ["SAP hands off and moves on without waiting", "Good for large, stable batch plan transfers",
                "Hard to confirm receipt right away"],
               "Replies when ready"),
    ),
}


def _duo(spec):
    def build(lang, out):
        t = spec[lang]
        duo(out, t["banner"], t["headline"], t["left"], t["right"], sub=t.get("sub"))
    return build


BUILDERS = {
    "sap-mes-interface-01": _duo(MES_IF_1),
    "sap-mes-interface-02": _duo(MES_IF_2),
}
