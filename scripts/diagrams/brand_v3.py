# -*- coding: utf-8 -*-
"""
Rabbit Logs 도식 브랜드 레이어 v3
- 논리 캔버스 800px, 2배 렌더(1600px 저장)
- 팔레트 중간톤 확장 (각 색 6단계)
- 레스토랑 어휘 선 아이콘 세트 (PIL 직접 드로잉, 이모지 미사용)
- 배너 A/B안 선택 가능
"""
from PIL import Image, ImageDraw, ImageFont
import os, math

# ================= 팔레트: 각 축 6단계로 확장 =================
# 기존 브랜드 원색은 인덱스 2(메인)에 그대로 보존 — 색 자체는 바꾸지 않았다.
TEAL_S = ["#1b3a35", "#234b45", "#2c5f57", "#4e857b", "#7ba99f", "#b8d0ca"]
GOLD_S = ["#8f5c1d", "#bd7c2c", "#d99441", "#e3b071", "#eecda3", "#f7e6cd"]
BERRY_S= ["#7a3950", "#93465e", "#a8516e", "#c07f95", "#d6aab8", "#ecd5dd"]
NEUT_S = ["#25302b", "#4a534c", "#7d7768", "#a9a396", "#ded8cb", "#f0ece2"]

TEAL, MARIGOLD, BERRY = TEAL_S[2], GOLD_S[2], BERRY_S[2]
INK, MUTE, LINE = NEUT_S[0], NEUT_S[2], NEUT_S[4]
BG = "#faf8f3"

# ================= 캔버스 기준 =================
W = 800
SCALE = 2
PAD = 30
RADIUS = 12
BANNER_H = 46

MIN_TITLE, MIN_SUB, MIN_EMPH, MIN_LABEL, MIN_BODY = 28, 17, 21, 20, 17

FONT_DIR = None
for p in ("./scripts/diagrams/fonts", "./fonts", "/tmp/fonts"):
    if os.path.isdir(p) and os.path.exists(os.path.join(p, "Pretendard-Bold.otf")):
        FONT_DIR = p
        break
if FONT_DIR is None:
    raise RuntimeError("Pretendard 폰트를 찾을 수 없습니다.")

_cache = {}
def F(weight, size):
    key = (weight, size)
    if key not in _cache:
        _cache[key] = ImageFont.truetype(
            os.path.join(FONT_DIR, f"Pretendard-{weight}.otf"), int(size * SCALE))
    return _cache[key]


class Canvas:
    def __init__(self, h, bg=BG):
        self.h = h
        self.img = Image.new("RGB", (W * SCALE, h * SCALE), bg)
        self.d = ImageDraw.Draw(self.img)

    def _s(self, box): return [v * SCALE for v in box]

    def rect(self, box, fill=None, outline=None, width=1, radius=None):
        b = self._s(box)
        if radius is None:
            self.d.rectangle(b, fill=fill, outline=outline, width=max(1, int(width * SCALE)))
        else:
            self.d.rounded_rectangle(b, radius=int(radius * SCALE), fill=fill,
                                     outline=outline, width=max(1, int(width * SCALE)))

    def text(self, xy, s, font, fill=INK):
        self.d.text((xy[0] * SCALE, xy[1] * SCALE), s, font=font, fill=fill)

    def text_w(self, s, font):
        return self.d.textlength(s, font=font) / SCALE

    def text_h(self, s, font):
        bb = self.d.textbbox((0, 0), s, font=font)
        return (bb[3] - bb[1]) / SCALE

    def center_text(self, cx, cy, s, font, fill=INK):
        bb = self.d.textbbox((0, 0), s, font=font)
        self.d.text((cx * SCALE - (bb[0] + bb[2]) / 2,
                     cy * SCALE - (bb[1] + bb[3]) / 2), s, font=font, fill=fill)

    def line(self, pts, fill=LINE, width=1):
        self.d.line([p * SCALE for p in pts], fill=fill, width=max(1, int(width * SCALE)))

    def ellipse(self, box, fill=None, outline=None, width=1):
        self.d.ellipse(self._s(box), fill=fill, outline=outline,
                       width=max(1, int(width * SCALE)))

    def arc(self, box, a0, a1, fill=LINE, width=1):
        self.d.arc(self._s(box), a0, a1, fill=fill, width=max(1, int(width * SCALE)))

    def polygon(self, pts, fill=None, outline=None):
        self.d.polygon([p * SCALE for p in pts], fill=fill, outline=outline)

    def save(self, path, quality=90):
        self.img.save(path, "JPEG", quality=quality, optimize=True)
        kb = os.path.getsize(path) / 1024
        print(f"저장 {os.path.basename(path)}  {W*SCALE}x{self.h*SCALE}px  {kb:.0f}KB")


# ================= 배너 =================
def banner_A(c, title):
    """A안: 기존 유지 — 전폭 청록 그라데이션 배너"""
    grad = Image.new("RGB", (W * SCALE, BANNER_H * SCALE))
    gd = ImageDraw.Draw(grad)
    c0, c1 = TEAL_S[1], TEAL_S[3]
    r0, g0, b0 = int(c0[1:3],16), int(c0[3:5],16), int(c0[5:7],16)
    r1, g1, b1 = int(c1[1:3],16), int(c1[3:5],16), int(c1[5:7],16)
    for x in range(W * SCALE):
        t = x / (W * SCALE)
        gd.line([(x,0),(x,BANNER_H*SCALE)],
                fill=(int(r0+(r1-r0)*t), int(g0+(g1-g0)*t), int(b0+(b1-b0)*t)))
    mask = Image.new("L", (W*SCALE, BANNER_H*SCALE), 0)
    ImageDraw.Draw(mask).rounded_rectangle(
        [0,0,W*SCALE-1, BANNER_H*SCALE + RADIUS*SCALE], radius=RADIUS*SCALE, fill=255)
    c.img.paste(grad, (0,0), mask)
    c.center_text(W/2, BANNER_H/2, title, F("Bold", 22), fill="#ffffff")
    return BANNER_H + 18


def banner_B(c, title, sub=None):
    """B안: 좌측 정렬 텍스트 타이틀 + 짧은 컬러 룰 (에디토리얼)"""
    y = 26
    c.rect([PAD, y, PAD + 44, y + 4], fill=TEAL, radius=2)
    y += 18
    f = F("ExtraBold", 27)
    c.text((PAD, y), title, f, fill=TEAL_S[1])
    y += c.text_h(title, f) + 12
    if sub:
        fs = F("Medium", 17)
        c.text((PAD, y), sub, fs, fill=MUTE)
        y += c.text_h(sub, fs) + 10
    return y + 14


# ================= 선 아이콘 세트 (레스토랑 어휘) =================
# 모두 24x24 논리 단위 기준. cx,cy 중심, s = 크기 배율.
def _ic(c, cx, cy, s, col, w):
    return (lambda *p: [cx + p[i] * s if i % 2 == 0 else cy + p[i] * s
                        for i in range(len(p))])

def icon_order(c, cx, cy, s=1.0, col=TEAL, w=2):
    """주문서 (SD) — 문서 + 체크"""
    hw, hh = 7*s, 9*s
    c.rect([cx-hw, cy-hh, cx+hw, cy+hh], outline=col, width=w, radius=2*s)
    for i, dy in enumerate((-4.5, -1.5, 1.5)):
        c.line([cx-4*s, cy+dy*s, cx+(3 if i < 2 else 1)*s, cy+dy*s], fill=col, width=w)
    c.line([cx-3.5*s, cy+5.5*s, cx-1.5*s, cy+7.5*s], fill=col, width=w)
    c.line([cx-1.5*s, cy+7.5*s, cx+4*s, cy+4*s], fill=col, width=w)

def icon_box(c, cx, cy, s=1.0, col=MARIGOLD, w=2):
    """식자재 박스 (MM)"""
    hw = 8*s
    c.polygon([cx-hw, cy-3*s, cx, cy-8*s, cx+hw, cy-3*s, cx, cy+2*s], outline=col)
    c.line([cx-hw, cy-3*s, cx-hw, cy+5*s], fill=col, width=w)
    c.line([cx+hw, cy-3*s, cx+hw, cy+5*s], fill=col, width=w)
    c.line([cx-hw, cy+5*s, cx, cy+9*s], fill=col, width=w)
    c.line([cx+hw, cy+5*s, cx, cy+9*s], fill=col, width=w)
    c.line([cx, cy+2*s, cx, cy+9*s], fill=col, width=w)

def icon_pot(c, cx, cy, s=1.0, col=TEAL, w=2):
    """냄비 (PP·주방)"""
    c.rect([cx-7*s, cy-3*s, cx+7*s, cy+7*s], outline=col, width=w, radius=2*s)
    c.line([cx-10*s, cy-1*s, cx-7*s, cy-1*s], fill=col, width=w)
    c.line([cx+7*s, cy-1*s, cx+10*s, cy-1*s], fill=col, width=w)
    c.line([cx-8*s, cy-3*s, cx+8*s, cy-3*s], fill=col, width=w)
    for dx in (-3.5, 0, 3.5):
        c.arc([cx+dx*s-2*s, cy-9*s, cx+dx*s+2*s, cy-5*s], 200, 340, fill=col, width=w)

def icon_plate(c, cx, cy, s=1.0, col=TEAL, w=2):
    """완성 접시 (출하·완제품)"""
    c.ellipse([cx-9*s, cy-6*s, cx+9*s, cy+6*s], outline=col, width=w)
    c.ellipse([cx-4.5*s, cy-3*s, cx+4.5*s, cy+3*s], outline=col, width=w)
    c.arc([cx-11*s, cy+2*s, cx+11*s, cy+10*s], 15, 165, fill=col, width=w)

def icon_receipt(c, cx, cy, s=1.0, col=BERRY, w=2):
    """영수증 (CO·원가)"""
    top, bot = cy-9*s, cy+7*s
    c.line([cx-6*s, top, cx+6*s, top], fill=col, width=w)
    c.line([cx-6*s, top, cx-6*s, bot], fill=col, width=w)
    c.line([cx+6*s, top, cx+6*s, bot], fill=col, width=w)
    zz = []
    for i in range(5):
        zz += [cx-6*s + i*3*s, bot + (2*s if i % 2 else 0)]
    c.d.line([v*SCALE for v in zz], fill=col, width=max(1,int(w*SCALE)))
    for dy in (-5.5, -2.5, 0.5):
        c.line([cx-3.5*s, cy+dy*s, cx+3.5*s, cy+dy*s], fill=col, width=w)

def icon_scale(c, cx, cy, s=1.0, col=NEUT_S[1], w=2):
    """저울 (QM·품질/균형)"""
    c.line([cx, cy-8*s, cx, cy+7*s], fill=col, width=w)
    c.line([cx-8*s, cy-6*s, cx+8*s, cy-6*s], fill=col, width=w)
    c.line([cx-4*s, cy+7*s, cx+4*s, cy+7*s], fill=col, width=w)
    for sx in (-8, 8):
        c.arc([cx+sx*s-4*s, cy-6*s, cx+sx*s+4*s, cy+2*s], 0, 180, fill=col, width=w)

def icon_clock(c, cx, cy, s=1.0, col=NEUT_S[1], w=2):
    """시계 (일정·리드타임)"""
    c.ellipse([cx-8*s, cy-8*s, cx+8*s, cy+8*s], outline=col, width=w)
    c.line([cx, cy-4.5*s, cx, cy], fill=col, width=w)
    c.line([cx, cy, cx+4*s, cy+2.5*s], fill=col, width=w)

def icon_ledger(c, cx, cy, s=1.0, col=TEAL_S[1], w=2):
    """장부 (FI·재무)"""
    c.rect([cx-8*s, cy-8*s, cx+8*s, cy+8*s], outline=col, width=w, radius=2*s)
    c.line([cx-8*s, cy-8*s, cx-8*s, cy+8*s], fill=col, width=w+1)
    c.line([cx-3.5*s, cy-8*s, cx-3.5*s, cy+8*s], fill=col, width=w)
    for dy in (-4, -1, 2, 5):
        c.line([cx-1*s, cy+dy*s, cx+5.5*s, cy+dy*s], fill=col, width=w)

ICONS = {
    "order": ("주문서 · SD", icon_order),
    "box":   ("식자재 · MM", icon_box),
    "pot":   ("조리 · PP",   icon_pot),
    "plate": ("서빙 · LE",   icon_plate),
    "receipt":("원가 · CO",  icon_receipt),
    "scale": ("품질 · QM",   icon_scale),
    "clock": ("리드타임",    icon_clock),
    "ledger":("장부 · FI",   icon_ledger),
}


# ================= 공용 요소 =================
def icon_badge(c, cx, cy, fn, r=19, ring=TEAL_S[4], fill="#ffffff", col=TEAL, s=1.0):
    """아이콘을 원형 뱃지 안에 배치"""
    c.ellipse([cx-r, cy-r, cx+r, cy+r], fill=fill, outline=ring, width=2)
    fn(c, cx, cy, s, col, 2)


def flow_arrow(c, x0, x1, y, col=NEUT_S[3]):
    """간격 비례 gap/head. 좁으면 head 축소해 선이 사라지지 않게."""
    span = x1 - x0
    gap = span * 0.26
    head = max(7, span * 0.30)
    sx, ex = x0 + gap, x1 - gap
    if ex - sx < head + 3:
        head = max(6, (ex - sx) - 3)
    c.line([sx, y, ex - head * 0.7, y], fill=col, width=2)
    c.polygon([ex, y, ex - head, y - head * 0.42, ex - head, y + head * 0.42], fill=col)
