# -*- coding: utf-8 -*-
"""stats-descriptive-basics-01 — 3열 컬러 카드(중심/퍼짐/위치)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brand import *

T = {
    "ko": dict(
        banner="기술통계 — 데이터를 요약하는 세 가지 질문",
        tags=["[중심]", "[퍼짐]", "[위치]"],
        heads=["평균 · 중앙값", "분산 · 표준편차", "사분위수 Q1 · Q2 · Q3"],
        subs=["데이터가 어디에 몰려 있나?", "데이터가 얼마나 흩어져 있나?", "데이터가 어떻게 나뉘어 있나?"],
        blocks=[
            [("평균", ["모든 값의 합 ÷ 개수", "→ 극단값 하나에 크게 흔들린다"]),
             ("중앙값", ["크기순 나열 시 정가운데 값", "→ 극단값이 있어도 안정적이다"])],
            [("분산", ["각 값과 평균의 거리²의 평균", "→ 단위가 제곱이라 직관이 어렵다"]),
             ("표준편차", ["분산의 제곱근 √분산", "→ 원래 단위로 해석 가능하다"])],
            [("Q1", ["하위 25% 경계값"]),
             ("Q2", ["중앙값 = 정확히 가운데"]),
             ("Q3", ["상위 25% 경계값"])],
        ],
        notes=["평균 ≈ 중앙값이면 분포가 치우치지 않았다는 신호",
               "평균이 같아도 표준편차가 크면 품질 편차가 크다",
               "min · Q1 · Q2 · Q3 · max 다섯 수치로 전체 윤곽 파악"],
        foot="중심(평균·중앙값) · 퍼짐(분산·표준편차) · 위치(사분위수) — 기술통계의 세 축",
    ),
    "en": dict(
        banner="Descriptive statistics — three questions that summarise data",
        tags=["[CENTRE]", "[SPREAD]", "[POSITION]"],
        heads=["Mean · Median", "Variance · Std. dev.", "Quartiles Q1 · Q2 · Q3"],
        subs=["Where does the data cluster?", "How widely is it scattered?", "How is it divided up?"],
        blocks=[
            [("Mean", ["Sum of all values ÷ count", "→ One outlier shifts it sharply"]),
             ("Median", ["Middle value when ordered", "→ Stays stable despite outliers"])],
            [("Variance", ["Mean of squared distances", "→ Squared units are unintuitive"]),
             ("Std. dev.", ["Square root of variance", "→ Readable in original units"])],
            [("Q1", ["Boundary of the bottom 25%"]),
             ("Q2", ["The median — exact middle"]),
             ("Q3", ["Boundary of the top 25%"])],
        ],
        notes=["Mean ≈ median signals a distribution that is not skewed",
               "Equal means with a larger SD means wider quality variation",
               "min · Q1 · Q2 · Q3 · max outline the whole shape"],
        foot="Centre (mean·median) · Spread (variance·SD) · Position (quartiles) — the three axes",
    ),
}

HEAD_BG = [TEAL, MARIGOLD, BERRY]
PALE    = [TEAL_PALE, GOLD_PALE, BERRY_PALE]
ACCENT  = [TEAL, MARIGOLD_D, BERRY]


def build(lang, out):
    t = T[lang]
    f_tag  = font("Bold", 13)
    f_head = font("Bold", 21)
    f_sub  = font("Medium", 15)
    f_name = font("Bold", 17)
    f_body = font("Regular", 15)
    f_note = font("Medium", 14)
    f_foot = font("Medium", 15)

    n = 3
    gap_x = 20
    card_w = (W - MARGIN * 2 - gap_x * (n - 1)) / n
    head_h = 92
    note_h = 64
    top = BANNER_H + 26

    # 본문 높이 역산
    body_h = 0
    for blk in t["blocks"]:
        h = 14
        for name, lines in blk:
            h += 26 + len(lines) * 22 + 16
        body_h = max(body_h, h)
    card_h = head_h + body_h + 14 + note_h + 16
    img_h = int(top + card_h + 20 + 26 + 22)

    img, d = new_canvas(img_h)
    draw_banner(d, t["banner"])

    for i in range(n):
        x0 = MARGIN + i * (card_w + gap_x)
        x1 = x0 + card_w
        cx = (x0 + x1) / 2
        d.rounded_rectangle([x0, top, x1, top + card_h], radius=16,
                            fill=WHITE, outline=LINE, width=2)
        # 헤더
        d.rounded_rectangle([x0, top, x1, top + head_h], radius=16, fill=HEAD_BG[i])
        d.rectangle([x0, top + head_h - 16, x1, top + head_h], fill=HEAD_BG[i])

        center_x_text(d, cx, top + 12, t["tags"][i], f_tag, "#ffffff")
        center_x_text(d, cx, top + 34, t["heads"][i], f_head, WHITE)
        center_x_text(d, cx, top + 66, t["subs"][i], f_sub, "#e6efed")

        y = top + head_h + 16
        for name, lines in t["blocks"][i]:
            d.text((x0 + 20, y), name, font=f_name, fill=ACCENT[i])
            y += 26
            for ln in lines:
                d.text((x0 + 20, y), ln, font=f_body, fill=MUTED)
                y += 22
            y += 16

        # 노트 박스 — 카드 하단 고정
        ny = top + card_h - note_h - 14
        d.rounded_rectangle([x0 + 14, ny, x1 - 14, ny + note_h], radius=10, fill=PALE[i])
        words = t["notes"][i].split()
        lines, cur = [], ""
        for w in words:
            trial = (cur + " " + w).strip()
            if text_w(d, trial, f_note) > card_w - 56 and cur:
                lines.append(cur); cur = w
            else:
                cur = trial
        lines.append(cur)
        ly = ny + (note_h - len(lines) * 20) / 2
        for ln in lines:
            center_x_text(d, cx, ly, ln, f_note, INK)
            ly += 20

    center_x_text(d, W / 2, top + card_h + 22, t["foot"], f_foot, MUTED)
    save(img, out)
