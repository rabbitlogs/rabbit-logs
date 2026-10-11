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
        "title": "1차 시험이 31%에 그친 이유",
        "sub": "몰라서가 아니라, 해내지 못해서",
        "head": ("원인", "무슨 일이 있었나", "그 뒤로 바꾼 것"),
        "rows": [
            ("기계번역 지침", "번역된 숫자와 구성이 원문과 다르게 읽혔다", "지침은 영어로 읽는다"),
            ("한 과제에 쏠린 시간", "낯선 설정 화면에서 헤매며 한 과제에 약 100분", "3분 룰: 한 화면에서 3분 막히면 넘어간다"),
            ("저장 전 대조 없음", "0 하나 더, 필수 필드 누락, 습관대로 한 단계 추가", "Save 전에 지침과 필드를 1:1로 대조한다"),
        ],
    },
    "en": {
        "title": "Why my first attempt scored 31%",
        "sub": "Not a knowledge gap, but an execution gap",
        "head": ("Cause", "What happened", "What I changed"),
        "rows": [
            ("Machine-translated instructions",
             "Numbers and structure read differently from the original",
             "Read the instructions in English"),
            ("Time sink",
             "About 100 minutes lost in unfamiliar configuration screens",
             "3-minute rule: stuck on a screen, move on"),
            ("No check before Save",
             "An extra zero, a missing field, one step added out of habit",
             "Compare every field with the instructions before saving"),
        ],
    },
}


def build_2_01(lang, out):
    """1차 31% — 원인 3가지를 '원인 / 무슨 일이 있었나 / 바꾼 것' 미니 표로."""
    t = T_2_01[lang]
    title, sub, head, rows = t["title"], t["sub"], t["head"], t["rows"]
    W = 800
    cols = [B.PAD, 250, 520]           # 열 시작 x
    widths = [cols[1] - cols[0] - 20, cols[2] - cols[1] - 20, W - B.PAD - cols[2]]
    f_head = B.F("Bold", 17)
    f_cause = B.F("ExtraBold", 19)
    f_body = B.F("Regular", 17)
    lh = 25

    probe = _Canvas(W, 10)
    wrapped = []
    for r in rows:
        cells = [_wrap(probe, r[0], f_cause, widths[0]),
                 _wrap(probe, r[1], f_body, widths[1]),
                 _wrap(probe, r[2], B.F("SemiBold", 17), widths[2])]
        wrapped.append(cells)
    row_hs = [max(len(x) for x in cells) * lh + 30 for cells in wrapped]

    top = _banner_height(probe, title, sub)
    head_h = 40
    H = int(top + head_h + sum(row_hs) + 26)
    c = _Canvas(W, H)
    y = B.banner_B(c, title, sub)

    # 헤더
    for i, h in enumerate(head):
        col = B.BERRY_S[1] if i == 0 else (B.NEUT_S[1] if i == 1 else B.TEAL_S[1])
        c.text((cols[i], y + 8), h.upper() if lang == "en" else h, f_head, fill=col)
    y += head_h
    c.line([B.PAD, y, W - B.PAD, y], fill=B.NEUT_S[2], width=1.5)

    for (cells, rh) in zip(wrapped, row_hs):
        ty = y + 15
        for j, line in enumerate(cells[0]):
            c.text((cols[0], ty + j * lh), line, f_cause, fill=B.BERRY_S[1])
        for j, line in enumerate(cells[1]):
            c.text((cols[1], ty + j * lh), line, f_body, fill=B.NEUT_S[1])
        for j, line in enumerate(cells[2]):
            c.text((cols[2], ty + j * lh), line, B.F("SemiBold", 17), fill=B.TEAL_S[1])
        y += rh
        c.line([B.PAD, y, W - B.PAD, y], fill=B.NEUT_S[4], width=1)

    c.save(out)


# ---------------------------------------------------------------- 3편
T_3_01 = {
    "ko": {
        "title": "3시간을 어떻게 썼나",
        "sub": "1차 시험, 연습 리허설, 3차 시험의 시간 배분",
        "rows": [
            ("1차 시험", [("한 과제", 100, "berry"), ("나머지 과제", 80, "berry2")], "마지막 과제는 손도 못 댐"),
            ("R3 리허설", [("과제", 100, "teal"), ("검증", 80, "gold")], "남은 시간은 전부 검증"),
            ("3차 시험", [("과제", 85, "teal"), ("검증", 35, "gold"), ("남은 시간", 60, "rest")], "약 2시간 만에 제출"),
        ],
        "axis": "분",
    },
    "en": {
        "title": "How I spent the 3 hours",
        "sub": "First attempt, practice rehearsal, and third attempt",
        "rows": [
            ("1st attempt", [("One task", 100, "berry"), ("Other tasks", 80, "berry2")], "Never reached the last tasks"),
            ("R3 rehearsal", [("Tasks", 100, "teal"), ("Check", 80, "gold")], "All spare time went to checking"),
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


BUILDERS = {
    "2-01": (build_2_01, "sap-mm-c-ts452-certification-2-01"),
    "3-01": (build_3_01, "sap-mm-c-ts452-certification-3-01"),
}

if __name__ == "__main__":
    keys = sys.argv[1:] or list(BUILDERS)
    for k in keys:
        fn, base = BUILDERS[k]
        fn("ko", os.path.join(OUT, base + ".jpg"))
        fn("en", os.path.join(OUT, base + "_en.jpg"))
