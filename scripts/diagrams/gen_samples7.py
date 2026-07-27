# -*- coding: utf-8 -*-
"""유형별 대표 이미지 7개 생성 → public/images/new"""
import sys
sys.path.insert(0, "/sessions/magical-elegant-hopper/mnt/rabbit-logs/scripts/diagrams")
import rl_forms as R
import sap_icons as SI

OUT = "/sessions/magical-elegant-hopper/mnt/rabbit-logs/public/images/new"

# 1. 그리드 카드형 — Fit/Gap (Gap 푸는 3길 + Fit)
R.grid_cards(
    "SAP Fit/Gap, 갭을 푸는 길", "표준과 현실이 어긋날 때 택하는 네 갈래",
    [
        ("Fit · 표준 그대로", SI.i_gear, "teal",
         ["SAP 표준이 우리 업무와 맞음", "커스터마이징 없이 사용", "유지보수 부담 최소"]),
        ("개발 · 표준을 맞춤", SI.i_code, "berry",
         ["Z코드로 맞춤 기능 개발", "가장 흔하지만 비용·시간 큼", "확장(BTP)으로 코어 분리"]),
        ("프로세스 변경 · 우리를 맞춤", SI.i_flow, "gold",
         ["업무를 SAP 표준에 맞춤", "가장 이상적이나 저항 존재", "충분한 변화관리가 관건"]),
        ("수용 · 그냥 받아들임", SI.i_check, "neutral",
         ["불편하지만 못 쓸 정도 아님", "현명한 타협이 필요", "모든 걸 개발할 순 없음"]),
    ],
    f"{OUT}/rl-fit-gap-ways.jpg")

# 2. 순환형 — 순환 BOM 재작업
R.cycle_ring(
    "SAP 순환 BOM, 불량을 되돌리는 고리", "완성품이 다시 자기 재료가 되는 재작업 구조",
    [("완성품", "teal"), ("불량 발견", "berry"), ("재작업 투입", "gold"), ("재완성", "teal")],
    f"{OUT}/rl-circular-bom.jpg",
    center_top="재작업", center_bot="LOOP",
    note="BOM 등록 시 ‘순환 허용’ 체크 — 안 하면 저장·MRP 오류")

# 3. 넘버링/프로세스형 — MRP 4단계
R.process_steps(
    "SAP MRP, 자재계획 4단계", "생산 목표에서 계획오더까지 자동으로 계산된다",
    [("총소요량", "BOM을 전개해 필요한 자재 총량을 뽑는다"),
     ("순소요량", "현재 재고를 빼고 실제 부족분만 남긴다"),
     ("발주 시점", "리드타임을 거꾸로 세어 발주일을 정한다"),
     ("계획오더", "무엇을·얼마나·언제 만들지 초안을 만든다")],
    f"{OUT}/rl-mrp-flow.jpg", axis="teal")

# 4. 계층형 — 조직구조 + 기준정보 스트립
R.hierarchy(
    "SAP 조직 구조, 건물의 뼈대", "위가 아래를 품는다 — 한 번 잡으면 바꾸기 어렵다",
    [("클라이언트", "시스템 전체 — 그룹을 담는 최상위"),
     ("회사 코드", "독립 회계 장부를 갖는 법인 단위"),
     ("플랜트", "생산·재고의 핵심 — 요리가 이뤄지는 매장"),
     ("저장 위치", "플랜트 안 물리적 보관 장소")],
    f"{OUT}/rl-org-structure.jpg", axis="teal",
    footer_title="그 위에 올라가는 기준정보 4종",
    footer_items=[("자재 마스터", SI.i_box), ("BOM", SI.i_doc),
                  ("작업장", SI.i_gear), ("Routing", SI.i_flow)])

# 5. 숫자/차트형 — 재고 편차
R.variance_bars(
    "재고 편차, 숫자로 읽기", "실사 − SAP · 청록은 실사 초과, 베리는 실사 부족",
    [("자재 A", -2), ("자재 B", -5), ("자재 C", 13), ("자재 D", 0), ("자재 E", -13)],
    f"{OUT}/rl-inventory-variance.jpg", pos_axis="teal", neg_axis="berry",
    stat_cards=[("평균 −1.4", "전체적으로 실사가 SAP보다 적은 쪽으로 치우침", "teal"),
                ("표준편차 8.5", "품목마다 편차가 제각각 — 상쇄되고 있을 뿐", "berry"),
                ("원인 3종", "입출고 누락·불량 처리 오류·입력 실수", "gold")])

# 6. 통합 허브형 — SAP가 부서를 잇는다
R.hub_spokes(
    "SAP, 흩어진 부서를 하나로", "한 번의 입력이 모든 부서로 이어진다",
    "SAP",
    [("영업 · SD", SI.i_doc, "teal"), ("자재 · MM", SI.i_box, "gold"),
     ("생산 · PP", SI.i_gear, "teal"), ("원가 · CO", SI.i_cost, "berry"),
     ("재무 · FI", SI.i_chart, "teal")],
    f"{OUT}/rl-what-is-sap.jpg",
    note="홀(SD)의 주문이 주방(PP)·창고(MM)로 자동으로 흘러간다")

# 7. 가운데 대칭 비교형 — PI vs 구축
R.compare_center(
    "SAP PI와 구축, 기획자와 시공자",
    "같은 컨설턴트라도 역할이 전혀 다르다",
    ("PI · 설계자", "To-Be 청사진", "berry"),
    ("구축 · 시공자", "현실 시스템화", "teal"),
    [("관점", "이상적 미래", "현실적 제약"),
     ("질문", "어떻게 일해야 하나", "어떻게 지을까"),
     ("전문성", "전략·프로세스", "모듈·ABAP"),
     ("결과물", "꿈의 청사진", "돌아가는 시스템")],
    f"{OUT}/rl-pi-vs-implementation.jpg",
    footer="둘의 균형이 맞을 때 SAP는 진짜 전환의 동력이 된다")

print("== 7개 생성 완료 ==")
