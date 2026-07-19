#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sap-wip-overview 도식 생성 스크립트 (최종본 — 카드+원 조합)

적용된 규칙 (rabbit-logs-master-prompt.md 8번 섹션 기준):
- 폰트: Pretendard (블로그 본문과 통일). 로컬에 없으면 자동 다운로드.
- 화살표: 도형 경계에서 여백(gap)을 두고 완만한 곡선으로 연결 (end-to-end 금지)
- 사이즈: 폭 1200px 고정, 높이는 콘텐츠 기준으로 자동 역산 (16:9 강제 안 함)
- 캡션은 이미지에 포함하지 않음 — 발행 시 마크다운으로 별도 작성:
    *그림 1. 원자재에서 WIP를 거쳐 완제품으로 가는 흐름과 PP·CO·MM 세 관점*
- 색 사용: 원색은 라벨·테두리·포인트에만, 넓은 면은 그라데이션+저채도

사용법:
    python3 wip_overview_final.py
    → sap-wip-overview.png 생성 (실행 디렉토리 기준)
"""
import os
import urllib.request
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math

W = 1200
FONT_DIR = "./fonts/"

# ── 폰트 준비: 로컬에 없으면 자동 다운로드 ──
_FONT_WEIGHTS = ["Regular", "Medium", "SemiBold", "Bold", "ExtraBold", "Black"]
def ensure_fonts():
    os.makedirs(FONT_DIR, exist_ok=True)
    base_url = "https://raw.githubusercontent.com/orioncactus/pretendard/main/packages/pretendard/dist/public/static/Pretendard-{}.otf"
    for w in _FONT_WEIGHTS:
        path = FONT_DIR + f"Pretendard-{w}.otf"
        if not os.path.exists(path):
            try:
                urllib.request.urlretrieve(base_url.format(w), path)
            except Exception as e:
                raise RuntimeError(
                    f"Pretendard-{w}.otf 다운로드 실패: {e}\n"
                    f"네트워크 문제일 수 있음 — 임의로 다른 폰트로 대체하지 말고 먼저 알릴 것."
                )

ensure_fonts()

BG = (250, 248, 243)
TEAL = (44, 95, 87); TEAL_DEEP = (35, 75, 69); TEAL_LIGHT = (78, 133, 123)
MARIGOLD = (217, 148, 65); MARIGOLD_DEEP = (189, 124, 44)
BERRY = (168, 81, 110)
INK = (37, 48, 43); MUTED = (125, 119, 104); LINE = (221, 213, 196)

def font(weight, size):
    return ImageFont.truetype(FONT_DIR + f"Pretendard-{weight}.otf", size)

def true_center_text(draw, xc, yc, txt, fnt, fill):
    bbox = draw.textbbox((0, 0), txt, font=fnt)
    w, h = bbox[2]-bbox[0], bbox[3]-bbox[1]
    draw.text((xc-w/2-bbox[0], yc-h/2-bbox[1]), txt, font=fnt, fill=fill)

def lerp(c1, c2, t): return tuple(int(c1[i]+(c2[i]-c1[i])*t) for i in range(3))

def radial_patch(size, center_color, edge_color):
    w, h = size
    disc = Image.new("RGB", (w, h), edge_color)
    dd = ImageDraw.Draw(disc)
    cx, cy = w*0.4, h*0.32
    maxr = max(w, h)*0.8
    for i in range(40, 0, -1):
        t = i/40; r = maxr*t
        dd.ellipse([cx-r, cy-r, cx+r, cy+r], fill=lerp(center_color, edge_color, 1-(1-t)**1.4))
    mask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mask).ellipse([0,0,w-1,h-1], fill=255)
    return disc, mask

def paste_shadow(base, box, blur=13, opacity=70, ellipse=True, radius=14):
    x0,y0,x1,y1 = box; pad = blur*2
    sw, sh = int(x1-x0+pad*2), int(y1-y0+pad*2)
    sh_img = Image.new("RGBA", (sw, sh), (0,0,0,0))
    sd = ImageDraw.Draw(sh_img)
    if ellipse: sd.ellipse([pad,pad,sw-pad,sh-pad], fill=(58,50,40,opacity))
    else: sd.rounded_rectangle([pad,pad,sw-pad,sh-pad], radius=radius, fill=(58,50,40,opacity))
    sh_img = sh_img.filter(ImageFilter.GaussianBlur(blur))
    base.paste(sh_img, (int(x0-pad), int(y0-pad)+5), sh_img)

def gapped_arrow(draw, x1, y1, x2, y2, style="solid", width=3.5, color=(201,180,135), curve=0):
    """
    도형 경계에서 이미 여백을 둔 좌표(x1,y1)~(x2,y2)를 받아 화살표를 그린다.
    style: 'solid'(직선굵게) | 'curve'(곡선) | 'dashed'(점선)
    curve: 곡선일 때 휘는 정도(양수=아래로 볼록)
    """
    if style == "curve":
        # 2차 베지어 근사: 중간점을 curve만큼 offset
        mx, my = (x1+x2)/2, (y1+y2)/2 + curve
        steps = 24
        pts = []
        for i in range(steps+1):
            t = i/steps
            bx = (1-t)**2*x1 + 2*(1-t)*t*mx + t**2*x2
            by = (1-t)**2*y1 + 2*(1-t)*t*my + t**2*y2
            pts.append((bx,by))
        draw.line(pts, fill=color, width=int(width), joint="curve")
        # 화살촉: 마지막 두 점으로 각도 계산
        ex, ey = pts[-1]; px, py = pts[-3]
        ang = math.atan2(ey-py, ex-px)
    elif style == "dashed":
        dist = math.hypot(x2-x1, y2-y1)
        n_dash = max(int(dist/14), 3)
        for i in range(n_dash):
            t0 = i/n_dash; t1 = t0 + (0.55/n_dash)
            dx0,dy0 = x1+(x2-x1)*t0, y1+(y2-y1)*t0
            dx1,dy1 = x1+(x2-x1)*t1, y1+(y2-y1)*t1
            draw.line([dx0,dy0,dx1,dy1], fill=color, width=int(width))
        ang = math.atan2(y2-y1, x2-x1)
    else:  # solid
        draw.line([x1,y1,x2,y2], fill=color, width=int(width))
        ang = math.atan2(y2-y1, x2-x1)

    # 화살촉 (끝점에서 안쪽으로)
    ah = 11
    ax, ay = x2, y2
    a1 = ang + math.radians(150)
    a2 = ang - math.radians(150)
    p1 = (ax + ah*math.cos(a1), ay + ah*math.sin(a1))
    p2 = (ax + ah*math.cos(a2), ay + ah*math.sin(a2))
    draw.polygon([(ax,ay), p1, p2], fill=color)


# ═══════════ 콘텐츠 높이 역산 ═══════════
BANNER_H = 54
title_gap = 44
sub_gap = 38
row1_top = 0  # 계산 후 채움
disc_r = [76, 86, 76]
disc_label_gap = 42
disc_sub_gap = 26
row1_bottom_pad = 30

msg_gap = 46
card_h = 150
card_top_pad = 34
bottom_pad = 40

row1_h = max(disc_r)*2 + disc_label_gap + disc_sub_gap + row1_bottom_pad
msg_h = 40
H = BANNER_H + title_gap + sub_gap + 24 + row1_h + msg_gap + msg_h + card_top_pad + card_h + bottom_pad

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# 배너
banner_grad = Image.new("RGB", (W, BANNER_H))
bgd = ImageDraw.Draw(banner_grad)
for x in range(W):
    bgd.line([(x,0),(x,BANNER_H)], fill=lerp(TEAL_LIGHT, TEAL_DEEP, x/W))
img.paste(banner_grad, (0,0))
true_center_text(d, W/2, BANNER_H/2, "SAP WIP", font("Bold",25), (255,255,255))

title_y = BANNER_H + title_gap
true_center_text(d, W/2, title_y, "WIP, 원자재와 완제품 사이", font("Black",36), INK)
sub_y = title_y + sub_gap
true_center_text(d, W/2, sub_y, "아직 접시에 담기지 않았을 뿐, 이미 가치를 지닌 자산", font("Regular",18), MUTED)

row1_cy = sub_y + 24 + max(disc_r)
positions = [220, 600, 980]
radii = disc_r

# 원자재
cx, R = positions[0], radii[0]
paste_shadow(img, [cx-R,row1_cy-R,cx+R,row1_cy+R])
disc, mask = radial_patch((R*2,R*2), (255,255,255), (235,228,210))
img.paste(disc, (cx-R,row1_cy-R), mask)
d.ellipse([cx-R,row1_cy-R,cx+R,row1_cy+R], outline=(213,204,184), width=2)
d.ellipse([cx-54,row1_cy+12,cx+54,row1_cy+40], fill=(231,221,197))
d.ellipse([cx-54,row1_cy+8,cx+54,row1_cy+36], fill=(242,235,216))
d.ellipse([cx-40,row1_cy-4,cx-8,row1_cy+28], fill=(228,201,166))
d.line([cx-24,row1_cy-15,cx-24,row1_cy-4], fill=(168,133,85), width=3)
d.ellipse([cx-8,row1_cy-2,cx+36,row1_cy+30], fill=(224,164,155))
d.line([cx+30,row1_cy+2,cx+37,row1_cy-11], fill=(111,154,84), width=3)
true_center_text(d, cx, row1_cy+R+disc_label_gap, "원자재", font("Bold",22), INK)
true_center_text(d, cx, row1_cy+R+disc_label_gap+disc_sub_gap, "창고의 개별 재료", font("Regular",16), MUTED)

# WIP
cx, R = positions[1], radii[1]
paste_shadow(img, [cx-R,row1_cy-R,cx+R,row1_cy+R], opacity=85)
disc, mask = radial_patch((R*2,R*2), (253,246,234), (246,227,194))
img.paste(disc, (cx-R,row1_cy-R), mask)
d.ellipse([cx-R,row1_cy-R,cx+R,row1_cy+R], outline=MARIGOLD, width=3)
for dx in (-16,3,21):
    d.line([cx+dx,row1_cy-26,cx+dx-8,row1_cy-48], fill=(201,154,94), width=3, joint="curve")
    d.line([cx+dx-8,row1_cy-48,cx+dx,row1_cy-68], fill=(201,154,94), width=3, joint="curve")
pot_w,pot_h = 92,56
pot_grad = Image.new("RGB",(pot_w,pot_h))
pgd = ImageDraw.Draw(pot_grad)
for y in range(pot_h): pgd.line([(0,y),(pot_w,y)], fill=lerp((61,113,104),(32,72,64), y/pot_h))
pot_mask = Image.new("L",(pot_w,pot_h),0)
ImageDraw.Draw(pot_mask).polygon([(4,0),(pot_w-4,0),(pot_w-10,pot_h-4),(10,pot_h-4)], fill=255)
img.paste(pot_grad, (cx-pot_w//2, row1_cy-10), pot_mask)
d.polygon([(cx-44,row1_cy-10),(cx+44,row1_cy-10),(cx+37,row1_cy+44),(cx-37,row1_cy+44)], outline=TEAL_DEEP, width=2)
d.ellipse([cx-44,row1_cy-22,cx+44,row1_cy+2], fill=(78,133,123))
d.ellipse([cx-35,row1_cy-18,cx+35,row1_cy-2], fill=(230,145,84))
d.ellipse([cx-20,row1_cy-16,cx-4,row1_cy-9], fill=(240,172,120))
for bx,by,br in [(-12,-13,4),(7,-15,3),(18,-11,2.5)]:
    d.ellipse([cx+bx-br,row1_cy+by-br,cx+bx+br,row1_cy+by+br], fill=(240,168,98))
d.line([cx-44,row1_cy-4,cx-58,row1_cy-4], fill=TEAL_DEEP, width=5)
d.line([cx+44,row1_cy-4,cx+58,row1_cy-4], fill=TEAL_DEEP, width=5)
true_center_text(d, cx, row1_cy+R+disc_label_gap, "WIP · 만들어지는 중", font("Black",23), INK)
true_center_text(d, cx, row1_cy+R+disc_label_gap+disc_sub_gap, "끓고 있는 찌개", font("Bold",16), MARIGOLD_DEEP)

# 완제품
cx, R = positions[2], radii[2]
paste_shadow(img, [cx-R,row1_cy-R,cx+R,row1_cy+R])
disc, mask = radial_patch((R*2,R*2), (255,255,255), (219,231,227))
img.paste(disc, (cx-R,row1_cy-R), mask)
d.ellipse([cx-R,row1_cy-R,cx+R,row1_cy+R], outline=(195,212,207), width=2)
d.ellipse([cx-54,row1_cy+26,cx+54,row1_cy+50], fill=(214,207,190))
d.ellipse([cx-54,row1_cy+22,cx+54,row1_cy+46], fill=(239,234,221))
cloche_w,cloche_h = 84,66
cl_grad = Image.new("RGB",(cloche_w,cloche_h))
cgd = ImageDraw.Draw(cl_grad)
for y in range(cloche_h): cgd.line([(0,y),(cloche_w,y)], fill=lerp((78,133,123),(40,86,78), y/cloche_h))
cl_mask = Image.new("L",(cloche_w,cloche_h),0)
ImageDraw.Draw(cl_mask).pieslice([0,0,cloche_w,cloche_h*2],180,360,fill=255)
img.paste(cl_grad, (cx-cloche_w//2, row1_cy-22), cl_mask)
d.arc([cx-42,row1_cy-22,cx+42,row1_cy+44],180,360, fill=TEAL_DEEP, width=2)
d.ellipse([cx-5,row1_cy-30,cx+5,row1_cy-20], fill=MARIGOLD, outline=TEAL_DEEP, width=2)
true_center_text(d, cx, row1_cy+R+disc_label_gap, "완제품", font("Bold",22), INK)
true_center_text(d, cx, row1_cy+R+disc_label_gap+disc_sub_gap, "접시에 담긴 요리", font("Regular",16), MUTED)

# ── 화살표: 여백을 두고, 완만한 곡선으로 ──
gap = 16
x1 = positions[0] + radii[0] + gap
x2 = positions[1] - radii[1] - gap
gapped_arrow(d, x1, row1_cy, x2, row1_cy, style="curve", width=4, curve=-14)
x1 = positions[1] + radii[1] + gap
x2 = positions[2] - radii[2] - gap
gapped_arrow(d, x1, row1_cy, x2, row1_cy, style="curve", width=4, curve=-14)

# 구분 메시지
msg_y = row1_cy + max(radii) + row1_bottom_pad + msg_gap
line_w = 480
d.line([W/2-line_w/2, msg_y-14, W/2+line_w/2, msg_y-14], fill=LINE, width=1)
true_center_text(d, W/2, msg_y, "같은 WIP, 세 사람의 시선", font("Bold",21), TEAL)

# 하단 3카드
card_top = msg_y + card_top_pad
gap_x = 45
card_w = 322
start_x = (W - (card_w*3+gap_x*2))/2
cards = [
    (MARIGOLD,"PP · 생산","생산 라인의 청진기","쌓이면 병목 신호",(251,237,213)),
    (TEAL,"CO · 원가","숨은 자산의 근거","결산 안 하면 자산 누락",(228,239,236)),
    (BERRY,"MM · 재고","미래 계획의 나침반","곧 완성될 공급 물량",(243,226,231)),
]
for i,(accent,label,main_t,sub_t,badge_bg) in enumerate(cards):
    cx0 = start_x + i*(card_w+gap_x)
    box = [cx0, card_top, cx0+card_w, card_top+card_h]
    paste_shadow(img, box, blur=13, opacity=55, ellipse=False, radius=18)
    d.rounded_rectangle(box, radius=18, fill=(255,255,255))
    d.rounded_rectangle([box[0],box[1],box[0]+22,box[3]], radius=10, fill=accent)
    d.rectangle([box[0]+10,box[1],box[0]+22,box[3]], fill=accent)
    bcx,bcy,br = box[0]+58, box[1]+52, 28
    d.ellipse([bcx-br,bcy-br,bcx+br,bcy+br], fill=badge_bg)
    d.ellipse([bcx-13,bcy-13,bcx+13,bcy+13], outline=accent, width=3)
    tx = box[0]+100
    d.text((tx,box[1]+34), label, font=font("Bold",15), fill=accent)
    d.text((tx,box[1]+58), main_t, font=font("Bold",20), fill=INK)
    d.text((tx,box[1]+92), sub_t, font=font("Regular",15), fill=MUTED)

img.save("sap-wip-overview.png","PNG")
print(f"캔버스: {W}x{H}px")
