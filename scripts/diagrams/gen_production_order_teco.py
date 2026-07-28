# -*- coding: utf-8 -*-
"""
sap-production-order-teco — 생산오더 TECO 글의 도식 1개 (brand_v3 + v3_forms).

§9 관계→형태: TECO → 정산 → CLSD는 순차 진행(단계가 명확) → 넘버링 로우(2K).
02번(CO02 메뉴 스크린샷)은 한글 SAP GUI라 영문판 대상이 아니다(§9 이미지 규칙 —
영문판이 필요 없는 이미지: 한글 GUI 캡처).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import brand_v3 as B
from v3_forms import numbering_rows

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(REPO, "public", "images")

T = {
    "ko": dict(
        title="생산오더가 완전히 닫히기까지 세 단계",
        sub="TECO는 생산을 닫을 뿐, 원가까지 닫지는 않는다",
        steps=[
            ("TECO", "생산 종료 — 미결 예약·잔여 능력소요 삭제, 발생 원가는 그대로 남음"),
            ("정산", "원가 종료 — 투입 자재비·노무비를 원가 대상으로 이전, 차이 계산"),
            ("CLSD", "오더 종결 — 정산까지 끝난 오더를 완전히 닫음, 이후 변경 불가"),
        ],
    ),
    "en": dict(
        title="Three steps to fully close a production order",
        sub="TECO closes out production only — not cost",
        steps=[
            ("TECO", "Production ends — open reservations and capacity cleared, cost remains"),
            ("Settlement", "Cost ends — material and labor cost moves to the cost object"),
            ("CLSD", "Order closes fully once settlement is done — no further changes"),
        ],
    ),
}


def gen_01(lang, out):
    t = T[lang]
    numbering_rows(
        title=t["title"], sub=t["sub"], steps=t["steps"],
        out=out, accent="teal",
    )


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    gen_01("ko", os.path.join(OUT, "sap-production-order-teco-01.jpg"))
    gen_01("en", os.path.join(OUT, "sap-production-order-teco-01_en.jpg"))
