# -*- coding: utf-8 -*-
"""
sap-project-decision-log — 프로젝트 의사결정 기록 글의 도식 1개 (brand_v3 + v3_forms).

§9 관계→형태: "현업이 남겨야 할 네 가지"는 순서 없는 병렬 나열 → 카드 그리드(2x2).
번호/화살표는 순서에만 붙인다는 규칙에 따라, 여기서는 번호 대신 라벨만 쓴다.
v3_forms에 카드 그리드 헬퍼가 없어 WideCanvas 위에 직접 그린다(brand_v3 색·폰트 규칙 준수).

영문 라벨이 한글보다 길어(예: "What conditions apply") 카드 폭을 넘칠 수 있으므로,
렌더 전에 getlength()로 최장 줄을 재서 카드 폭과 비교해 필요시 폭을 넓힌다.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import brand_v3 as B
from v3_forms import WideCanvas, banner_height, wrap

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(REPO, "public", "images")

T = {
    "ko": dict(
        title="결정이 날 때마다 남겨야 할 네 가지",
        sub="가장 자주 빠지고, 가장 자주 필요해지는 건 네 번째다",
        cards=[
            ("무엇으로 정했나", "실제 확정된 내용을 문장으로", B.TEAL_S),
            ("어떤 선택지가 있었나", "검토했지만 안 고른 안도 함께", B.TEAL_S),
            ("왜 이쪽인가", "우리 업무의 어떤 사정 때문인지", B.GOLD_S),
            ("어떤 조건이 붙나", "예외 상황, 나중에 다시 볼 지점", B.BERRY_S),
        ],
    ),
    "en": dict(
        title="Four things to record with every decision",
        sub="The fourth is the one most often skipped, and most often needed",
        cards=[
            ("What was decided", "The actual confirmed outcome, in a sentence", B.TEAL_S),
            ("What the alternatives were", "Including options considered but not chosen", B.TEAL_S),
            ("Why this one", "Which specifics of our operation drove it", B.GOLD_S),
            ("What conditions apply", "Exceptions, points to revisit later", B.BERRY_S),
        ],
    ),
}


def gen_01(lang, out):
    t = T[lang]
    title, sub, cards = t["title"], t["sub"], t["cards"]

    f_label = B.F("ExtraBold", 20)
    f_desc = B.F("Regular", 16)

    probe = WideCanvas(10, 10)
    gap = 20

    # 카드 폭을 라벨 실측 길이 기준으로 역산 — 영문이 한글보다 길어 넘칠 수 있음
    min_cell_w = 320
    longest_label = max(probe.text_w(label, f_label) for label, _, _ in cards)
    cell_w = max(min_cell_w, longest_label + 28 + 20)
    W_ = int(B.PAD * 2 + cell_w * 2 + gap)
    W_ = min(W_, B.W)
    cell_w = (W_ - B.PAD * 2 - gap) / 2

    cell_h = 128
    top = banner_height(title, sub)
    H = int(top + cell_h * 2 + gap + 30)

    c = WideCanvas(W_, H)
    B.banner_B(c, title, sub)

    for i, (label, desc, axis) in enumerate(cards):
        row, col = divmod(i, 2)
        x0 = B.PAD + col * (cell_w + gap)
        y0 = top + row * (cell_h + gap)
        x1 = x0 + cell_w
        y1 = y0 + cell_h

        # 강조 대상(네 번째 카드)만 살짝 진한 배경으로 구분 — 원색은 좁은 요소에만
        is_key = (i == 3)
        c.rect([x0, y0, x1, y1], fill=(axis[5] if is_key else "#ffffff"),
               outline=axis[3], width=2, radius=12)
        c.rect([x0 + 14, y0 + 14, x0 + 14 + 28, y0 + 18], fill=axis[1], radius=2)

        ly = y0 + 30
        for ln in wrap(c, label, f_label, cell_w - 28):
            c.text((x0 + 14, ly), ln, f_label, fill=axis[0])
            ly += c.text_h(ln, f_label) + 6

        ly += 6
        for ln in wrap(c, desc, f_desc, cell_w - 28):
            c.text((x0 + 14, ly), ln, f_desc, fill=B.NEUT_S[1])
            ly += c.text_h(ln, f_desc) + 5

    c.save(out)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    gen_01("ko", os.path.join(OUT, "sap-project-decision-log-01.jpg"))
    gen_01("en", os.path.join(OUT, "sap-project-decision-log-01_en.jpg"))
