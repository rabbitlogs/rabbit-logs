# -*- coding: utf-8 -*-
"""
sap-mrp-no-planned-order — MRP 계획오더 미생성 글의 도식 3개 (brand_v3 + v3_forms).
한글·영문 버전을 같은 스크립트의 언어 딕셔너리에서 생성해 레이아웃을 공유한다.

§9 관계→형태 대응표 적용:
01: 조달유형(E/F/X) — 분류(축이 하나) → mini_table
02: MRP 유형 ND — 선택 목록에서 한 값을 고르는 것 → mini_table(강조 행)
03: MRP 유형 X0 — 상위가 제외돼도 하위로 이어지는 포함 관계 → hierarchy

brand_v3 규격: 논리 폭 최대 800(내용 기준 역산), SCALE=2로 실제 1600px 저장.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import brand_v3 as B
from v3_forms import mini_table, hierarchy

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(REPO, "public", "images")

T = {
    "ko": dict(
        t01="자재마스터 MRP 뷰 — 조달유형",
        s01="직접 만들지, 사 올지를 정하는 값",
        h01=["코드", "의미", "MRP 결과"],
        r01=[
            ["E", "사내생산", "계획오더 생성"],
            ["F", "외부조달", "구매의뢰 생성"],
            ["X", "둘 다 가능", "특수조달유형이 결정"],
        ],
        n01="회사마다 커스텀 조달유형을 추가해 쓰는 경우가 있어 실제 값과 대조가 필요합니다.",
        t02="자재마스터 MRP 뷰 — MRP 유형",
        s02="이 자재를 계획 대상으로 볼 것인가",
        h02=["코드", "MRP 내역", "계획오더"],
        r02=[
            ["PD", "MRP", "생성됨"],
            ["VB", "수동 재주문점", "생성됨"],
            ["ND", "계획없음", "생성 안 됨"],
        ],
        n02="ND는 계획하지 않겠다는 설정 — 소요가 있어도 계획오더가 생기지 않습니다.",
        t03="MRP 유형 X0 — 제외되지만 이어지는 하위 소요",
        s03="이 자재는 계획에서 빠지지만, BOM 하위 자재에는 소요가 그대로 내려간다",
        lv03=[
            ("반제품 (X0)", "MRP 제외 — 계획오더 생성 안 됨"),
            ("원자재 A", "BOM 하위 — 소요 계산됨"),
            ("원자재 B", "BOM 하위 — 소요 계산됨"),
        ],
        f03="하위는 다 나오는데 이것만 안 나온다면 X0을 의심해 볼 만합니다.",
    ),
    "en": dict(
        t01="Material master MRP view — procurement type",
        s01="The value that decides whether to make it or buy it",
        h01=["Code", "Meaning", "MRP result"],
        r01=[
            ["E", "In-house production", "Planned order created"],
            ["F", "External procurement", "Purchase requisition created"],
            ["X", "Either", "Special procurement type decides"],
        ],
        n01="Companies often add custom procurement types — check against your actual values.",
        t02="Material master MRP view — MRP type",
        s02="Is this material a planning target at all?",
        h02=["Code", "MRP description", "Planned order"],
        r02=[
            ["PD", "MRP", "Created"],
            ["VB", "Manual reorder point", "Created"],
            ["ND", "No planning", "Not created"],
        ],
        n02="ND means don't plan this material — no planned order, no matter the requirement.",
        t03="MRP type X0 — excluded, still flows down",
        s03="Excluded from planning itself, but requirements still flow to its BOM components",
        lv03=[
            ("Semi-finished (X0)", "Excluded from MRP — no planned order"),
            ("Raw material A", "BOM component — requirement calculated"),
            ("Raw material B", "BOM component — requirement calculated"),
        ],
        f03="If everything downstream shows up except this one, suspect X0.",
    ),
}


def gen_01(lang, out):
    t = T[lang]
    mini_table(
        title=t["t01"], sub=t["s01"], headers=t["h01"], rows=t["r01"],
        out=out, accent="teal", note=t["n01"],
    )


def gen_02(lang, out):
    t = T[lang]
    mini_table(
        title=t["t02"], sub=t["s02"], headers=t["h02"], rows=t["r02"],
        out=out, accent="berry", note=t["n02"],
    )


def gen_03(lang, out):
    t = T[lang]
    hierarchy(
        title=t["t03"], sub=t["s03"], levels=t["lv03"],
        out=out, accent="berry", footer=t["f03"],
    )


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    gen_01("ko", os.path.join(OUT, "sap-mrp-no-planned-order-01.jpg"))
    gen_02("ko", os.path.join(OUT, "sap-mrp-no-planned-order-02.jpg"))
    gen_03("ko", os.path.join(OUT, "sap-mrp-no-planned-order-03.jpg"))
    gen_01("en", os.path.join(OUT, "sap-mrp-no-planned-order-01_en.jpg"))
    gen_02("en", os.path.join(OUT, "sap-mrp-no-planned-order-02_en.jpg"))
    gen_03("en", os.path.join(OUT, "sap-mrp-no-planned-order-03_en.jpg"))
