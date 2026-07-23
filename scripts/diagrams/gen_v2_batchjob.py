# -*- coding: utf-8 -*-
"""
sap-batch-job-01 — SM36→SM37 전용 렌더, 화살표를 얇게 절제.

본문(sap-batch-job.md)은 SM36(예약 등록) 다음 SM37(모니터링)이라는 실제
순차 관계를 설명하므로(등록해야 모니터링할 대상이 생긴다), duo()의 좌우
비교와 달리 이 둘 사이의 화살표 자체는 유지한다. 다만 기존 duo()가 쓰던
굵은 삼각형 화살표는 다른 "비교/대립" 도식들과 톤이 같아 보여, 이 도식만
"가벼운 순서 안내"라는 느낌이 나도록 더 얇고 옅은 화살표로 바꾼다.

카드는 steps() 계열의 알약형 T-CODE 배지 + 점선 구분 스타일을 그대로
쓰되, 카드가 2개뿐이라 steps()를 그대로 쓰면 배지 원형 번호(1/2)가
T-CODE 알약과 중복돼 보이므로 전용 렌더로 분리한다.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brand import *


BATCH_JOB = {
    "ko": dict(banner="SAP 배치잡", sub="야간에 혼자 도는 자동 정산",
        headline="예약부터 모니터링까지 두 개의 T-CODE",
        cards=[
            dict(code="SM36", title="배치잡 예약 등록", col=TEAL,
                 body=["언제, 무엇을,", "얼마나 자주", "실행할지 설정"]),
            dict(code="SM37", title="실행 결과 모니터링", col=MARIGOLD_D,
                 body=["성공 · 실패 여부 확인", "로그를 보고", "문제를 진단"]),
        ],
        foot="예약만 해두면, 사람이 잠든 사이 시스템이 알아서 돌아갑니다",
    ),
    "en": dict(banner="SAP background jobs", sub="the settlement that runs overnight",
        headline="Two T-codes: one to schedule, one to watch",
        cards=[
            dict(code="SM36", title="Schedule the job", col=TEAL,
                 body=["Set when, what,", "and how often", "it should run"]),
            dict(code="SM37", title="Monitor the results", col=MARIGOLD_D,
                 body=["Check success or failure", "Read the log", "and diagnose problems"]),
        ],
        foot="Once it's scheduled, the system runs it while everyone's asleep",
    ),
}


def _wrap(d, text, f, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if text_w(d, t, f) > max_w and cur:
            lines.append(cur); cur = w
        else:
            cur = t
    if cur:
        lines.append(cur)
    return lines


def _thin_arrow(d, x0, y, x1, color=ARROW, width=3, head=10):
    """
    가벼운 순서 안내용 화살표. 기존 브랜드 arrow()보다 선을 가늘게,
    머리를 작게 만들어 "대립/비교"가 아니라 "다음 단계로"라는 절제된
    톤으로 그린다.
    """
    d.line([(x0, y), (x1 - head, y)], fill=color, width=width)
    d.polygon([(x1, y), (x1 - head, y - head * 0.5), (x1 - head, y + head * 0.5)], fill=color)


def _batch_job(lang, out):
    t = BATCH_JOB[lang]
    f_code = font("Bold", 15)
    f_title = font("Bold", 19)
    f_body = font("Regular", 15)
    f_foot = font("Bold", 16)

    n = len(t["cards"])
    gap_x = 60
    card_w = (W - MARGIN * 2 - gap_x * (n - 1)) / n
    card_h = 200
    code_h = 30

    top = BANNER_H + 96
    foot_gap = 24
    foot_h = 48

    img_h = int(top + card_h + foot_gap + foot_h + 40)
    img, d = new_canvas(img_h)
    draw_banner(d, t["banner"], t["sub"])
    draw_headline(d, BANNER_H + 30, t["headline"])

    bounds = []
    for i, c in enumerate(t["cards"]):
        x0 = MARGIN + i * (card_w + gap_x)
        x1 = x0 + card_w
        cx = (x0 + x1) / 2
        bounds.append((x0, x1))
        col = c["col"]

        top_bar_card(d, [x0, top, x1, top + card_h], col, radius=14, bar_h=5)

        cy = top + 30
        cw = text_w(d, c["code"], f_code) + 28
        d.rounded_rectangle([cx - cw / 2, cy - code_h / 2, cx + cw / 2, cy + code_h / 2],
                             radius=code_h / 2, fill=col)
        true_center_text(d, cx, cy, c["code"], f_code, WHITE)

        ty = cy + code_h / 2 + 26
        center_x_text(d, cx, ty, c["title"], f_title, INK)
        ty += 32
        dotted_line(d, x0 + 30, x1 - 30, ty)
        ty += 24
        for ln in c["body"]:
            center_x_text(d, cx, ty, ln, f_body, MUTED)
            ty += 26

    ay = top + card_h / 2
    for i in range(n - 1):
        span = bounds[i + 1][0] - bounds[i][1]
        gap = max(8, span * 0.2)
        _thin_arrow(d, bounds[i][1] + gap, ay, bounds[i + 1][0] - gap, color=ARROW, width=3, head=10)

    fy = top + card_h + foot_gap
    d.rounded_rectangle([MARGIN, fy, W - MARGIN, fy + foot_h], radius=12, fill=TEAL)
    true_center_text(d, W / 2, fy + foot_h / 2, t["foot"], f_foot, WHITE)

    save(img, out)


BUILDERS = {
    "sap-batch-job-01": _batch_job,
}
