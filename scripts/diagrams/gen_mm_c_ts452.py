# -*- coding: utf-8 -*-
"""
SAP MM 자격증 C_TS452 연재 도식 (brand_v3)

운영자 결정: 이 연재의 도식은 영문 라벨 1종만 만들어 한글판·영문판 글에 함께 쓴다.
(_en 파일을 따로 두지 않는다.)

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
def build_2_01(out):
    """1차 31% — 원인 3가지를 '원인 / 무슨 일이 있었나 / 바꾼 것' 미니 표로."""
    title = "Why my first attempt scored 31%"
    sub = "Not a knowledge gap, but an execution gap"
    head = ("Cause", "What happened", "What I changed")
    rows = [
        ("Machine-translated instructions",
         "Quantities and dates were swapped in the Korean version",
         "Read the instructions in English"),
        ("Time sink",
         "About 100 minutes went into one configuration-heavy task",
         "3-minute rule: stuck on a screen, move on"),
        ("No check before Save",
         "An extra zero, a missing field, one step added out of habit",
         "Compare every field with the instructions before saving"),
    ]
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
        c.text((cols[i], y + 8), h.upper(), f_head, fill=col)
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


BUILDERS = {
    "2-01": (build_2_01, "sap-mm-c-ts452-certification-2-01.jpg"),
}

if __name__ == "__main__":
    keys = sys.argv[1:] or list(BUILDERS)
    for k in keys:
        fn, name = BUILDERS[k]
        fn(os.path.join(OUT, name))
