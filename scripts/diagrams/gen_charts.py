# -*- coding: utf-8 -*-
"""차트형 도식(레이어 2A) — 좌 차트 + 우 해설 카드."""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brand import *

# ══ stats-sap-inventory-variance-01 ════════════════════════════════════════
VAR = {
    "ko": dict(
        banner="재고 편차 — SAP 수량과 실제 수량의 차이",
        chart_title="품목별 재고 편차 (실사 − SAP)",
        labels=["자재 A", "자재 B", "자재 C", "자재 D", "자재 E"],
        values=[-2, -5, 13, 0, -13],
        legend=["실사 > SAP (과소 기록)", "실사 < SAP (과다 기록)"],
        cards=[("평균 편차", "방향 파악", "−1.4개", "→ SAP가 재고를 과다 기록하는 경향"),
               ("표준편차", "흩어짐 파악", "8.5개", "→ 품목마다 편차 규모가 크게 다르다"),
               ("편차 0 品목", "기준점 확인", "자재 D", "→ SAP와 실사 완벽 일치, 벤치마크")],
        foot="재고 실사 편차 5개 품목 예시 | 평균 편차 −1.4개, 표준편차 8.5개",
    ),
    "en": dict(
        banner="Inventory variance — SAP quantity versus physical count",
        chart_title="Variance by item (count − SAP)",
        labels=["Item A", "Item B", "Item C", "Item D", "Item E"],
        values=[-2, -5, 13, 0, -13],
        legend=["Count > SAP (under-recorded)", "Count < SAP (over-recorded)"],
        cards=[("Mean variance", "Overall direction", "−1.4 units", "→ SAP tends to over-record stock"),
               ("Std. deviation", "How scattered", "8.5 units", "→ Variance size differs sharply by item"),
               ("Zero-variance item", "The benchmark", "Item D", "→ SAP and the count match exactly")],
        foot="Five sample items | mean variance −1.4 units, standard deviation 8.5",
    ),
}

# ══ stats-mean-trap-kpi-01 ═════════════════════════════════════════════════
MEAN = {
    "ko": dict(
        banner="평균은 어디에 있는가 — 같은 데이터, 다른 해석",
        chart_title="견적 완료일 분포",
        labels=["1~4일", "5~8일", "9~12일", "13~16일"],
        values=[3, 1, 0, 1],
        bins=[(1, 4), (5, 8), (9, 12), (13, 16)],   # 각 막대의 일수 구간
        median_val=4.0, mean_val=6.0,               # 점선을 찍을 실제 x값(일)
        unit="건수",
        mean_label="평균 6.0일", med_label="중앙값 4.0일",
        head="이 데이터가 말하는 것",
        cards=[("평균  6.0일", "외부조달 1건이 전체를 끌어올렸습니다.", "→ KPI 목표(5일) 미달성 기록"),
               ("중앙값  4.0일", "실제 대부분의 건은 3~5일 안에 완료됩니다.", "→ 외부조달 제외 평균도 4.0일"),
               ("두 값의 차이 = 2.0일", "평균 · 중앙값 차이가 크다", "→ 분포가 치우쳐 있다는 신호")],
        foot="견적 완료일 KPI 5건 | 평균 6.0일 vs 중앙값 4.0일 — 같은 데이터, 다른 해석",
    ),
    "en": dict(
        banner="Where is the mean? — same data, different readings",
        chart_title="Distribution of quotation lead times",
        labels=["1–4 days", "5–8 days", "9–12 days", "13–16 days"],
        values=[3, 1, 0, 1],
        bins=[(1, 4), (5, 8), (9, 12), (13, 16)],
        median_val=4.0, mean_val=6.0,
        unit="Count",
        mean_label="Mean 6.0 days", med_label="Median 4.0 days",
        head="What this data is saying",
        cards=[("Mean  6.0 days", "One externally sourced case pulled the whole average up.",
                "→ Recorded as missing the 5-day KPI"),
               ("Median  4.0 days", "Most cases actually finish within three to five days.",
                "→ Excluding that one case, the mean is also 4.0"),
               ("Gap = 2.0 days", "A wide mean-to-median gap", "→ A signal that the distribution is skewed")],
        foot="Five quotation records | mean 6.0 days vs median 4.0 — same data, different readings",
    ),
}

# ══ stats-excel-powerquery-pivot-01 ════════════════════════════════════════
PQ = {
    "ko": dict(
        banner="SAP 데이터 분석 흐름 — 파워쿼리 정제 → 피벗테이블 분석",
        cols=[("① SAP 데이터 출력",
               ["숫자가 텍스트로 저장됨", "헤더가 두 줄", "소계 · 합계 행 혼입", "빈 셀에 값 없음"],
               "⚠ 바로 피벗 돌리면 엉망"),
              ("② 파워쿼리로 정제",
               ["열 형식 변환(텍스트→숫자)", "불필요한 행 제거", "빈 셀 채우기", "헤더 정리"],
               "✓ 한 번 만들면 새로 고침만"),
              ("③ 피벗테이블 분석",
               ["월별 납기 편차 집계", "품목별 재고 편차 요약", "작업장별 생산량 비교", "KPI 대시보드 구성"],
               "✓ 원하는 그림이 나온다")],
        foot="파워쿼리: SAP 출력물 전처리 자동화 · 피벗테이블: 정제된 데이터로 집계 · 분석",
    ),
    "en": dict(
        banner="The SAP analysis flow — Power Query cleanup → pivot table analysis",
        cols=[("① Export from SAP",
               ["Numbers stored as text", "Headers split over two rows",
                "Subtotal rows mixed in", "Empty cells left blank"],
               "⚠ Pivot it now and it breaks"),
              ("② Clean in Power Query",
               ["Change type (text → number)", "Remove unwanted rows",
                "Fill blank cells down", "Tidy the headers"],
               "✓ Build once, then just refresh"),
              ("③ Analyse in a pivot",
               ["Monthly delivery variance", "Stock variance by item",
                "Output by work center", "Build a KPI dashboard"],
               "✓ The picture you wanted")],
        foot="Power Query automates the cleanup · pivot tables aggregate and analyse the clean data",
    ),
}


def _wrap(d, text, f, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if text_w(d, trial, f) > max_w and cur:
            lines.append(cur); cur = w
        else:
            cur = trial
    if cur:
        lines.append(cur)
    return lines


def build_variance(lang, out):
    t = VAR[lang]
    f_ct = font("Bold", 17); f_ax = font("Regular", 13)
    f_kt = font("Bold", 12); f_ks = font("Bold", 20); f_kd = font("Regular", 13)
    f_lg = font("Regular", 13); f_ft = font("Regular", 13)

    card_w, card_gap = 300, 12
    top = BANNER_H + 24
    card_h = 92
    chart_x0 = MARGIN
    chart_x1 = W - MARGIN - card_w - 20
    chart_h = card_h * 3 + card_gap * 2
    img_h = int(top + chart_h + 74)

    img, d = new_canvas(img_h)
    draw_banner(d, t["banner"])
    center_x_text(d, (chart_x0 + chart_x1) / 2, top, t["chart_title"], f_ct, INK)

    py0 = top + 30
    py1 = top + chart_h - 34
    vals = t["values"]
    lim = math.ceil(max(abs(v) for v in vals) / 5) * 5 + 5
    zero_y = py0 + (py1 - py0) * (lim / (2 * lim))

    for g in range(-lim, lim + 1, 5):
        gy = zero_y - (g / lim) * (py1 - py0) / 2
        d.line([(chart_x0 + 42, gy), (chart_x1, gy)], fill="#e8e2d6", width=1)
        d.text((chart_x0 + 8, gy - 8), str(g), font=f_ax, fill=MUTED)
    d.line([(chart_x0 + 42, zero_y), (chart_x1, zero_y)], fill="#b9b0a0", width=2)

    n = len(vals)
    inner = chart_x1 - (chart_x0 + 42)
    bar_w = inner / (n + (n + 1) / 2.0)
    space = bar_w / 2
    for i, v in enumerate(vals):
        bx = chart_x0 + 42 + space + i * (bar_w + space)
        by = zero_y - (v / lim) * (py1 - py0) / 2
        col = TEAL if v > 0 else (BERRY if v < 0 else "#b9b0a0")
        if v != 0:
            d.rectangle([bx, min(by, zero_y), bx + bar_w, max(by, zero_y)], fill=col)
        lbl = f"+{v}" if v > 0 else str(v)
        ly = by - 20 if v >= 0 else by + 5
        center_x_text(d, bx + bar_w / 2, ly, lbl, font("Bold", 14), col if v else MUTED)
        center_x_text(d, bx + bar_w / 2, py1 + 8, t["labels"][i], f_ax, INK)

    lgy = py1 + 32
    for i, (lg, col) in enumerate(zip(t["legend"], [TEAL, BERRY])):
        lx = chart_x0 + 42 + i * 240
        d.rectangle([lx, lgy + 3, lx + 12, lgy + 13], fill=col)
        d.text((lx + 18, lgy), lg, font=f_lg, fill=MUTED)

    cx0 = W - MARGIN - card_w
    for i, (title, sub, big, desc) in enumerate(t["cards"]):
        cy = top + i * (card_h + card_gap)
        col = [TEAL, BERRY, MARIGOLD][i]
        pale = [TEAL_PALE, BERRY_PALE, GOLD_PALE][i]
        d.rounded_rectangle([cx0, cy, cx0 + card_w, cy + card_h], radius=12, fill=pale)
        d.rounded_rectangle([cx0, cy, cx0 + 6, cy + card_h], radius=3, fill=col)
        d.text((cx0 + 18, cy + 9), title, font=f_kt, fill=col)
        d.text((cx0 + 18 + text_w(d, title, f_kt) + 8, cy + 9), sub, font=f_kt, fill=MUTED)
        d.text((cx0 + 18, cy + 28), big, font=f_ks, fill=INK)
        for j, ln in enumerate(_wrap(d, desc, f_kd, card_w - 36)):
            d.text((cx0 + 18, cy + 56 + j * 17), ln, font=f_kd, fill=MUTED)

    center_x_text(d, W / 2, img_h - 30, t["foot"], f_ft, MUTED)
    save(img, out)


def build_mean(lang, out):
    t = MEAN[lang]
    f_ct = font("Bold", 17); f_ax = font("Regular", 13)
    f_hd = font("Bold", 19); f_kt = font("Bold", 17)
    f_kd = font("Regular", 14); f_ft = font("Regular", 13)

    card_w = 470
    top = BANNER_H + 26
    chart_x0, chart_x1 = MARGIN, W - MARGIN - card_w - 24
    chart_h = 326          # 뱃지 2단 공간 확보를 위해 플롯을 내린 만큼 높이도 키운다
    img_h = int(top + chart_h + 72)

    img, d = new_canvas(img_h)
    draw_banner(d, t["banner"])
    center_x_text(d, (chart_x0 + chart_x1) / 2, top, t["chart_title"], f_ct, INK)

    # 평균·중앙값 뱃지(가까우면 위/아래 2단)가 차트 제목을 가리지 않도록 플롯을 충분히 내린다.
    py0, py1 = top + 88, top + chart_h - 30
    vals = t["values"]
    vmax = max(vals)
    for g in range(vmax + 1):
        gy = py1 - (g / vmax) * (py1 - py0)
        d.line([(chart_x0 + 40, gy), (chart_x1, gy)], fill="#e8e2d6", width=1)
        d.text((chart_x0 + 20, gy - 8), str(g), font=f_ax, fill=MUTED)
    d.text((chart_x0, (py0 + py1) / 2 - 10), t["unit"], font=f_ax, fill=MUTED)

    n = len(vals)
    inner = chart_x1 - (chart_x0 + 40)
    bar_w = inner / (n + (n + 1) / 2.0)
    space = bar_w / 2
    bar_cx = []                     # 각 막대의 중심 x
    for i, v in enumerate(vals):
        bx = chart_x0 + 40 + space + i * (bar_w + space)
        bar_cx.append(bx + bar_w / 2)
        bh = (v / vmax) * (py1 - py0)
        if v:
            d.rectangle([bx, py1 - bh, bx + bar_w, py1], fill=TEAL)
            center_x_text(d, bx + bar_w / 2, py1 - bh - 22, f"{v}", font("Bold", 15), TEAL)
        center_x_text(d, bx + bar_w / 2, py1 + 8, t["labels"][i], f_ax, INK)

    # 일수 값 → x좌표 매핑. 각 막대는 구간 중앙(예: 1~4일 → 2.5일)에 위치한다.
    # 두 막대의 (일수중앙, 중심x)를 지나는 직선으로 임의의 일수를 x로 선형 변환한다.
    bins = t["bins"]
    day_centers = [(a + b) / 2 for a, b in bins]          # [2.5, 6.5, 10.5, 14.5]
    step_x = (bar_cx[-1] - bar_cx[0]) / (day_centers[-1] - day_centers[0])

    def day_to_x(day):
        return bar_cx[0] + (day - day_centers[0]) * step_x

    # 중앙값·평균 세로 점선 — 실제 값 위치에 찍는다.
    marks = [(t["median_val"], t["med_label"], MARIGOLD_D),
             (t["mean_val"],   t["mean_label"], BERRY)]
    # 라벨 뱃지가 겹치지 않도록, 두 점선이 가까우면 뱃지를 위/아래 두 단으로 나눈다.
    xs_marks = [day_to_x(m[0]) for m in marks]
    close = abs(xs_marks[1] - xs_marks[0]) < 150
    for k, (val, lbl, col) in enumerate(marks):
        vx = xs_marks[k]
        for yy in range(int(py0), int(py1), 8):
            d.line([(vx, yy), (vx, yy + 4)], fill=col, width=2)
        tw = text_w(d, lbl, font("Bold", 13))
        by = py0 - 26 if (not close or k == 0) else py0 - 52
        d.rounded_rectangle([vx - tw / 2 - 8, by, vx + tw / 2 + 8, by + 22],
                            radius=8, fill=col)
        true_center_text(d, vx, by + 11, lbl, font("Bold", 13), WHITE)

    cx0 = W - MARGIN - card_w
    d.text((cx0, top), t["head"], font=f_hd, fill=INK)
    cy = top + 34
    for i, (title, body, note) in enumerate(t["cards"]):
        col = [BERRY, TEAL, MARIGOLD][i]
        pale = [BERRY_PALE, TEAL_PALE, GOLD_PALE][i]
        lines = _wrap(d, body, f_kd, card_w - 40)
        h = 34 + len(lines) * 20 + 24
        d.rounded_rectangle([cx0, cy, cx0 + card_w, cy + h], radius=12, fill=pale)
        d.rounded_rectangle([cx0, cy, cx0 + 6, cy + h], radius=3, fill=col)
        d.text((cx0 + 18, cy + 10), title, font=f_kt, fill=col)
        yy = cy + 36
        for ln in lines:
            d.text((cx0 + 18, yy), ln, font=f_kd, fill=INK); yy += 20
        d.text((cx0 + 18, yy + 2), note, font=f_kd, fill=col)
        cy += h + 10

    center_x_text(d, W / 2, img_h - 28, t["foot"], f_ft, MUTED)
    save(img, out)


def build_pq(lang, out):
    t = PQ[lang]
    f_h = font("Bold", 18); f_i = font("Regular", 15); f_n = font("Bold", 14)
    f_ft = font("Regular", 13)

    n = 3
    gap_x = 34
    card_w = (W - MARGIN * 2 - gap_x * (n - 1)) / n
    head_h = 50
    rows = max(len(c[1]) for c in t["cols"])
    card_h = head_h + 18 + rows * 28 + 56
    top = BANNER_H + 30
    img_h = int(top + card_h + 62)

    img, d = new_canvas(img_h)
    draw_banner(d, t["banner"])

    bounds = []
    for i, (head, items, note) in enumerate(t["cols"]):
        x0 = MARGIN + i * (card_w + gap_x)
        x1 = x0 + card_w
        cx = (x0 + x1) / 2
        bounds.append((x0, x1))
        col = [BERRY, MARIGOLD, TEAL][i]
        pale = [BERRY_PALE, GOLD_PALE, TEAL_PALE][i]

        d.rounded_rectangle([x0, top, x1, top + card_h], radius=14,
                            fill=WHITE, outline=col, width=2)
        d.rounded_rectangle([x0, top, x1, top + head_h], radius=14, fill=col)
        d.rectangle([x0, top + head_h - 14, x1, top + head_h], fill=col)
        true_center_text(d, cx, top + head_h / 2, head, f_h, WHITE)

        y = top + head_h + 18
        for it in items:
            d.ellipse([x0 + 20, y + 6, x0 + 26, y + 12], fill=col)
            d.text((x0 + 34, y), it, font=f_i, fill=INK)
            y += 28

        ny = top + card_h - 46
        d.rounded_rectangle([x0 + 14, ny, x1 - 14, ny + 34], radius=9, fill=pale)
        true_center_text(d, cx, ny + 17, note, f_n, col)

    ay = top + card_h / 2
    for i in range(n - 1):
        arrow(d, bounds[i][1] + 8, ay, bounds[i + 1][0] - 8,
              color="#b9b0a0", width=5, head=13)

    center_x_text(d, W / 2, img_h - 30, t["foot"], f_ft, MUTED)
    save(img, out)


BUILDERS = {
    "stats-sap-inventory-variance-01": build_variance,
    "stats-mean-trap-kpi-01":          build_mean,
    "stats-excel-powerquery-pivot-01": build_pq,
}
