# -*- coding: utf-8 -*-
"""
SAP MM 자격증 C_TS452 연재 도식 (brand_v3)

마스터 프롬프트 9절대로 한글판(기본 파일명)과 영문판(_en)을 함께 만든다.
영문 글은 remarkEnImages 폴백으로 _en 파일을 자동으로 쓴다.

사용법 (저장소 루트에서):
  python3 scripts/diagrams/gen_mm_c_ts452.py            # 전부 생성
  python3 scripts/diagrams/gen_mm_c_ts452.py 2-01       # 하나만
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import brand_v3 as B
from PIL import Image, ImageDraw

OUT = os.path.join("public", "images")


class _Canvas(B.Canvas):
    """brand_v3.Canvas는 폭이 전역 고정이라, 인스턴스별 폭을 쓰는 래퍼."""
    def __init__(self, w, h, bg=B.BG):
        self._w = w
        self.h = h
        self.img = Image.new("RGB", (w * B.SCALE, h * B.SCALE), bg)
        self.d = ImageDraw.Draw(self.img)

    def save(self, path, quality=90):
        self.img.save(path, "JPEG", quality=quality, optimize=True)
        kb = os.path.getsize(path) / 1024
        print(f"캔버스: {self._w*B.SCALE}x{self.h*B.SCALE}px  {os.path.basename(path)}  {kb:.0f}KB")


def _banner_height(c, title, sub):
    y = 26 + 18
    y += c.text_h(title, B.F("ExtraBold", 27)) + 12
    if sub:
        y += c.text_h(sub, B.F("Medium", 17)) + 10
    return y + 14


def _wrap(c, text, font, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if c.text_w(t, font) <= width:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


# ---------------------------------------------------------------- 2편
T_2_01 = {
    "ko": {
        "title": "1차 이후 바꾼 세 가지",
        "sub": "몰라서가 아니라, 해내는 방식이 문제였다",
        "before": "1차 때", "after": "그 뒤로",
        "rows": [
            ("지침", "한국어(기계번역) 지침으로 읽었다", "영어 원문 지침으로 읽는다"),
            ("시간", "막힌 화면 하나를 오래 붙잡았다", "막힌 화면은 따로 모아 반복 연습한다"),
            ("저장", "Save 후 바로 다음으로 넘어갔다", "저장 전 대조, 저장 후 조회로 확인한다"),
        ],
    },
    "en": {
        "title": "Three things I changed after the first attempt",
        "sub": "Not a knowledge gap, but how I executed",
        "before": "First attempt", "after": "Afterward",
        "rows": [
            ("Instructions", "Read the machine-translated Korean version", "Read the original English instructions"),
            ("Time", "Held on to one stuck screen for too long", "Collect stuck screens and drill them separately"),
            ("Saving", "Pressed Save and moved straight on", "Check before saving, confirm on display after"),
        ],
    },
}


def build_2_01(lang, out):
    """전/후 비교형 — 1차 때 → 그 뒤로, 항목 3개."""
    t = T_2_01[lang]
    W = 800
    lab_w = 120 if lang == "en" else 70
    x_lab = B.PAD
    x_b = B.PAD + lab_w + 10
    arrow_w = 34
    col_w = (W - B.PAD - x_b - arrow_w) / 2
    x_a = x_b + col_w + arrow_w
    f_head = B.F("Bold", 17)
    f_lab = B.F("ExtraBold", 18)
    f_b = B.F("Regular", 17)
    f_a = B.F("SemiBold", 17)
    lh = 25
    probe = _Canvas(W, 10)
    wrapped = [(_wrap(probe, r[1], f_b, col_w - 28), _wrap(probe, r[2], f_a, col_w - 28)) for r in t["rows"]]
    row_hs = [max(len(b), len(a)) * lh + 28 for b, a in wrapped]
    top = _banner_height(probe, t["title"], t["sub"])
    H = int(top + 36 + sum(row_hs) + 12 * len(row_hs) + 20)
    c = _Canvas(W, H)
    y = B.banner_B(c, t["title"], t["sub"])
    c.text((x_b + 14, y), t["before"], f_head, fill=B.BERRY_S[1])
    c.text((x_a + 14, y), t["after"], f_head, fill=B.TEAL_S[1])
    y += 34
    for (lab, _, _), (bl, al), rh in zip(t["rows"], wrapped, row_hs):
        c.text((x_lab, y + 14), lab, f_lab, fill=B.NEUT_S[1])
        c.rect([x_b, y, x_b + col_w, y + rh], fill=B.BERRY_S[5], radius=10)
        c.rect([x_a, y, x_a + col_w, y + rh], fill=B.TEAL_S[5], radius=10)
        for j, line in enumerate(bl):
            c.text((x_b + 14, y + 14 + j * lh), line, f_b, fill=B.BERRY_S[0])
        for j, line in enumerate(al):
            c.text((x_a + 14, y + 14 + j * lh), line, f_a, fill=B.TEAL_S[0])
        ay = y + rh / 2
        ax0, ax1 = x_b + col_w + 7, x_a - 7
        c.line([ax0, ay, ax1 - 6, ay], fill=B.NEUT_S[3], width=2)
        c.polygon([ax1, ay, ax1 - 9, ay - 6, ax1 - 9, ay + 6], fill=B.NEUT_S[3])
        y += rh + 12
    c.save(out)


# ---------------------------------------------------------------- 3편
T_3_01 = {
    "ko": {
        "title": "3시간을 어떻게 썼나",
        "sub": "1차 시험과 3차 시험의 시간 배분 (분, 대략치)",
        "rows": [
            ("1차 시험", [("한 과제", 100, "berry"), ("나머지 과제", 80, "berry2")], "마지막 과제는 손도 못 댐"),
            ("3차 시험", [("과제", 85, "teal"), ("검증", 35, "gold"), ("남은 시간", 60, "rest")], "약 2시간 만에 제출"),
        ],
        "axis": "분",
    },
    "en": {
        "title": "How I spent the 3 hours",
        "sub": "First and third attempts (minutes, approximate)",
        "rows": [
            ("1st attempt", [("One task", 100, "berry"), ("Other tasks", 80, "berry2")], "Never reached the last tasks"),
            ("3rd attempt", [("Tasks", 85, "teal"), ("Check", 35, "gold"), ("Left", 60, "rest")], "Submitted after about 2 hours"),
        ],
        "axis": "min",
    },
}


def build_3_01(lang, out):
    """3시간(180분) 누적 막대 3줄 — 1차/리허설/3차 시간 배분 비교."""
    t = T_3_01[lang]
    pal = {"berry": B.BERRY_S[2], "berry2": B.BERRY_S[4], "teal": B.TEAL_S[2],
           "gold": B.GOLD_S[2], "rest": B.NEUT_S[5]}
    txt = {"berry": "#ffffff", "berry2": B.BERRY_S[0], "teal": "#ffffff",
           "gold": "#ffffff", "rest": B.NEUT_S[2]}
    W = 800
    label_w = 150
    x0 = B.PAD + label_w
    x1 = W - B.PAD
    per_min = (x1 - x0) / 180
    bar_h = 40
    row_h = 104
    f_label = B.F("Bold", 19)
    f_seg = B.F("SemiBold", 16)
    f_note = B.F("Regular", 16)
    f_axis = B.F("Medium", 14)

    probe = _Canvas(W, 10)
    top = _banner_height(probe, t["title"], t["sub"])
    H = int(top + row_h * len(t["rows"]) + 40)
    c = _Canvas(W, H)
    y = B.banner_B(c, t["title"], t["sub"])

    for name, segs, note in t["rows"]:
        by = y + 8
        c.text((B.PAD, by + bar_h / 2 - 12), name, f_label, fill=B.TEAL_S[0])
        x = x0
        for seg, mins, key in segs:
            w = mins * per_min
            c.rect([x, by, x + w - 2, by + bar_h], fill=pal[key], radius=6)
            lab = f"{seg} {mins}"
            if c.text_w(lab, f_seg) > w - 12:
                lab = str(mins)
            c.center_text(x + w / 2, by + bar_h / 2, lab, f_seg, fill=txt[key])
            x += w
        c.text((x0, by + bar_h + 10), note, f_note, fill=B.NEUT_S[1])
        y += row_h

    # 축 눈금 0 / 60 / 120 / 180
    ay = y + 2
    c.line([x0, ay, x1, ay], fill=B.NEUT_S[3], width=1)
    for m in (0, 60, 120, 180):
        ax = x0 + m * per_min
        c.line([ax, ay - 4, ax, ay + 4], fill=B.NEUT_S[3], width=1)
        c.center_text(ax, ay + 16, f"{m}{t['axis'] if m == 180 else ''}", f_axis, fill=B.MUTE)

    c.save(out)


# ---------------------------------------------------------------- 0편(총정리)
T_0_01 = {
    "ko": {
        "title": "세 번의 응시 기록",
        "sub": "SAP MM 자격증 C_TS452",
        "cards": [
            ("1차", "불합격", "", "기계번역 지침, 시간 부족, 저장 전 대조 없음", "berry"),
            ("2차", "시스템 결함", "응시권 재부여", "결함 근거 정리 → Help Center에 케이스 접수", "gold"),
            ("3차", "합격", "", "영어 지침, 저장 전후 확인, 마지막 전수 검증", "teal"),
        ],
    },
    "en": {
        "title": "Three exam attempts",
        "sub": "SAP MM certification C_TS452",
        "cards": [
            ("1st", "Failed", "", "Machine translation, no time, no check before saving", "berry"),
            ("2nd", "Defect", "Attempt reissued", "Evidence collected, case filed with the Help Center", "gold"),
            ("3rd", "Passed", "", "English instructions, checks around saves, final review", "teal"),
        ],
    },
}


def build_0_01(lang, out):
    """세 번의 응시를 카드 3장으로 나란히(타임라인)."""
    t = T_0_01[lang]
    col = {"berry": (B.BERRY_S[2], B.BERRY_S[5]), "gold": (B.GOLD_S[1], B.GOLD_S[5]),
           "teal": (B.TEAL_S[2], B.TEAL_S[5])}
    W = 800
    gap = 18
    cw = (W - 2 * B.PAD - 2 * gap) / 3
    f_lab = B.F("Bold", 18)
    f_score = B.F("Black", 34)
    f_res = B.F("Bold", 18)
    f_note = B.F("Regular", 16)
    probe = _Canvas(W, 10)
    notes = [_wrap(probe, c[3], f_note, cw - 32) for c in t["cards"]]
    card_h = 24 + 24 + 50 + 30 + max(len(n) for n in notes) * 24 + 20
    top = _banner_height(probe, t["title"], t["sub"])
    H = int(top + card_h + 30)
    c = _Canvas(W, H)
    y = B.banner_B(c, t["title"], t["sub"])
    for i, (lab, score, res, _, key) in enumerate(t["cards"]):
        x = B.PAD + i * (cw + gap)
        main, light = col[key]
        c.rect([x, y, x + cw, y + card_h], fill=light, radius=12)
        c.rect([x, y, x + cw, y + 6], fill=main, radius=3)
        c.text((x + 16, y + 22), lab, f_lab, fill=B.NEUT_S[1])
        c.text((x + 16, y + 48), score, f_score, fill=main)
        if res:
            c.text((x + 16, y + 98), res, f_res, fill=main)
        for j, line in enumerate(notes[i]):
            c.text((x + 16, y + 128 + j * 24), line, f_note, fill=B.NEUT_S[1])
    c.save(out)


BUILDERS = {
    "2-01": (build_2_01, "sap-mm-c-ts452-certification-2-01"),
    "3-01": (build_3_01, "sap-mm-c-ts452-certification-3-01"),
    "0-01": (build_0_01, "sap-mm-c-ts452-certification-0-01"),
}

if __name__ == "__main__":
    keys = sys.argv[1:] or list(BUILDERS)
    for k in keys:
        fn, base = BUILDERS[k]
        fn("ko", os.path.join(OUT, base + ".jpg"))
        fn("en", os.path.join(OUT, base + "_en.jpg"))
