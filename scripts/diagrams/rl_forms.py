# -*- coding: utf-8 -*-
"""
Rabbit Logs 도식 렌더 모듈 (레퍼런스 결 반영판)
- 그리드 카드형, 순환형, 넘버링/프로세스형, 계층형, 숫자/차트형, 통합허브형, 대칭 비교형
- 공통: brand_v3(Canvas·색·폰트) + sap_icons(선 아이콘) 사용
- 규칙(image-rules-final.md): 논리폭 800(2배 렌더), Pretendard, 옅은 칸엔 잉크 글자,
  배지=진한 톤+흰 글자, 200KB 이하.
색 매핑: 모듈/성격에 따라 teal/gold/berry 축을 고른다(image-choice-guide.md).
"""
import sys, math
sys.path.insert(0, "/sessions/magical-elegant-hopper/mnt/rabbit-logs/scripts/diagrams")
import brand_v3 as B
import v3_forms as F
import sap_icons as SI

T = B.TEAL_S; N = B.NEUT_S; G = B.GOLD_S; BE = B.BERRY_S
AXIS = {"teal": T, "gold": G, "berry": BE, "neutral": N}

# ── 글자색 (종이톤/흰카드 위에서 모두 대비 6:1 이상) ──
INK    = "#25302b"   # 제목·강조
BODY   = "#3a4340"   # 카드 본문·불릿 (기존 #4a534c보다 진하게)
SUBTLE = "#5f5a4e"   # 부제·캡션 (기존 #7d7768 대체, 대비 6.47)


# ── 폭 가변 캔버스 (v3_forms.WideCanvas 재사용) ──
WideCanvas = F.WideCanvas


def _dark(axis):
    """배지·헤더용 진한 톤. 골드는 대비 위해 0단계."""
    return axis[0] if axis is G else axis[1]


# ─────────────────────────────────────────────────────────────
# 통일 배너 (좌측정렬) — 모든 이미지가 공유하는 단일 기준
# 간격은 글자 높이(text_h)에 의존하지 않고 고정값을 쓴다.
#   컬러룰(44×4) → RULE_GAP → 제목 top → 제목높이 TITLE_BAND
#   → 부제 top → 부제높이 SUB_BAND → BODY_GAP → 본문 시작
# ─────────────────────────────────────────────────────────────
BANNER_RULE_W   = 44
BANNER_RULE_H   = 4
BANNER_RULE_GAP = 16    # 룰 아래 여백
BANNER_TITLE_PT = 28
BANNER_TITLE_BAND = 40  # 제목 top → 부제 top 고정 간격
BANNER_SUB_PT   = 17
BANNER_SUB_BAND = 30    # 부제 top → 본문 시작까지
BANNER_TOP      = 26

def banner(c, title, sub=None):
    """통일 좌측정렬 배너. 고정 간격이라 어떤 글자든 위치가 동일하다."""
    x = B.PAD
    y = BANNER_TOP
    c.rect([x, y, x + BANNER_RULE_W, y + BANNER_RULE_H], fill=T[2], radius=2)
    y += BANNER_RULE_H + BANNER_RULE_GAP
    c.text((x, y), title, B.F("ExtraBold", BANNER_TITLE_PT), fill=T[1])
    if sub:
        y += BANNER_TITLE_BAND
        c.text((x, y), sub, B.F("Medium", BANNER_SUB_PT), fill=SUBTLE)
        y += BANNER_SUB_BAND
    else:
        y += BANNER_TITLE_BAND
    return y

def banner_height(title, sub=None):
    """banner()가 반환할 본문 시작 y를 미리 계산 (렌더 없이)."""
    y = BANNER_TOP + BANNER_RULE_H + BANNER_RULE_GAP + BANNER_TITLE_BAND
    if sub:
        y += BANNER_SUB_BAND
    return y


def _round_corner(c, x_from, y, x_to, col, width, r):
    """수직선 끝(x_from, y-r 지점 이후) → 수평선(x_to 방향)을 잇는 라운드 코너.
    사분원을 짧은 선분들로 근사해 매끄럽게."""
    import math as _m
    sign = 1 if x_to > x_from else -1
    cx = x_from + sign * r   # 원 중심 x
    cy = y - r               # 원 중심 y
    steps = 10
    pts = []
    for i in range(steps + 1):
        # 각도: 아래(수직 접점, 180°/0°)에서 옆(수평 접점, 90°)으로
        if sign > 0:  # 오른쪽으로 꺾임: 180°→90°
            a = _m.radians(180 - (i / steps) * 90)
        else:         # 왼쪽으로 꺾임: 0°→90°
            a = _m.radians((i / steps) * 90)
        pts += [cx + r * _m.cos(a), cy + r * _m.sin(a)]
    c.d.line([v * B.SCALE for v in pts], fill=col,
             width=max(1, int(width * B.SCALE)), joint="curve")

def smooth_down_arrow(c, x0, x1, y_top, y_bot, col, width=5):
    """두 지점(x0,x1)에서 내려와 가운데로 모여 아래로 향하는 화살표.
    라운드 코너 + 또렷한 머리로 깔끔하게."""
    cx = (x0 + x1) / 2
    mid_y = (y_top + y_bot) / 2 + 4
    r = 16
    for sx in (x0, x1):
        sign = 1 if cx > sx else -1
        c.line([sx, y_top, sx, mid_y - r], fill=col, width=width)      # 세로 하강
        _round_corner(c, sx, mid_y, cx, col, width, r)                  # 라운드 코너
        c.line([sx + sign * r, mid_y, cx - sign * r, mid_y], fill=col, width=width)  # 수평 수렴
    c.line([cx, mid_y, cx, y_bot - 2], fill=col, width=width)          # 가운데 하강
    hs = 12
    c.polygon([cx, y_bot + 5, cx - hs, y_bot - hs, cx + hs, y_bot - hs], fill=col)  # 머리


def check_bullet(c, x, y, col):
    r = 7
    c.ellipse([x-r, y-r, x+r, y+r], fill=col)
    c.line([x-3.2, y+0.3, x-0.8, y+3], fill="#ffffff", width=2)
    c.line([x-0.8, y+3, x+3.6, y-2.6], fill="#ffffff", width=2)


def icon_disc(c, cx, cy, r, fillcol, iconfn, s=1.0):
    c.ellipse([cx-r, cy-r, cx+r, cy+r], fill=fillcol)
    iconfn(c, cx, cy, s, "#ffffff", 2)


# =========================================================
# 1. 그리드 카드형 (2×2, 아이콘 헤더 + 체크 불릿)
# =========================================================
def grid_cards(title, sub, cards, out, cols=2):
    """cards: [(라벨, 아이콘fn, 축이름, [항목...]), ...]"""
    W = B.W
    probe = WideCanvas(10, 10)
    f_lab = B.F("ExtraBold", 22); f_item = B.F("Medium", 17)
    pad = B.PAD; gap = 20
    cw = (W - pad*2 - gap*(cols-1)) / cols
    item_maxw = cw - 64

    def card_h(items):
        lines = sum(len(F.wrap(probe, it, f_item, item_maxw)) for it in items)
        return 78 + lines*26 + 24

    rows = (len(cards) + cols - 1) // cols
    row_heights = []
    for r in range(rows):
        rc = cards[r*cols:(r+1)*cols]
        row_heights.append(max(card_h(c[3]) for c in rc))
    H = int(banner_height(title, sub) + sum(row_heights) + gap*(rows-1) + 20)
    c = WideCanvas(W, H)
    y0 = banner(c, title, sub)

    yrow = y0
    for r in range(rows):
        rh = row_heights[r]
        for ci in range(cols):
            idx = r*cols + ci
            if idx >= len(cards):
                break
            lab, icon, axname, items = cards[idx]
            S = AXIS[axname]
            qx = pad + ci*(cw+gap); qy = yrow
            c.rect([qx, qy, qx+cw, qy+rh], fill="#ffffff", outline=N[4], width=1, radius=14)
            barcol = S[2] if S is not N else N[2]
            c.rect([qx, qy, qx+cw, qy+6], fill=barcol, radius=3)
            c.rect([qx, qy+3, qx+cw, qy+6], fill=barcol)
            icx = qx+40; icy = qy+42
            icon_disc(c, icx, icy, 24, _dark(S) if S is not N else N[2], icon, 1.15)
            c.text((qx+76, qy+30), lab, f_lab, fill=T[0])
            c.line([qx+20, qy+72, qx+cw-20, qy+72], fill=N[5], width=1)
            yy = qy+92
            accent = S[2] if S is not N else N[2]
            for it in items:
                check_bullet(c, qx+30, yy+2, accent)
                wl = F.wrap(c, it, f_item, item_maxw)
                for j, ln in enumerate(wl):
                    c.text((qx+48, yy-8+j*24), ln, f_item, fill=BODY)
                yy += len(wl)*24 + 6
        yrow += rh + gap
    c.save(out)


# =========================================================
# 2. 순환형 (원형 노드 + 호 화살표, 중앙 라벨, 옵션 강조)
# =========================================================
def cycle_ring(title, sub, nodes, out, center_top="", center_bot="", note=None):
    """nodes: [(라벨, 축이름), ...] 3~5개"""
    W = B.W; H = 600 if not note else 660
    c = WideCanvas(W, H); y0 = banner(c, title, sub)
    cx = W/2; cy = y0 + (H - y0)/2 + (0 if not note else -20); R = 130; node = 52
    n = len(nodes); ang0 = -90
    pts = [(cx+R*math.cos(math.radians(ang0+i*360/n)),
            cy+R*math.sin(math.radians(ang0+i*360/n))) for i in range(n)]
    for i in range(n):
        a0 = ang0+i*360/n+16; a1 = ang0+(i+1)*360/n-16
        c.arc([cx-R, cy-R, cx+R, cy+R], a0, a1, fill=N[3], width=5)
        ar = math.radians(a1); hx, hy = cx+R*math.cos(ar), cy+R*math.sin(ar)
        _arrowhead(c, hx, hy, ar+math.radians(90), 13, N[3])
    for (px, py), (lab, axname) in zip(pts, nodes):
        S = AXIS[axname]
        c.ellipse([px-node, py-node, px+node, py+node], fill=_dark(S) if S is not N else N[2])
        for j, ln in enumerate(F.wrap(c, lab, B.F("Bold", 17), node*2-10)):
            c.center_text(px, py-8+j*22, ln, B.F("Bold", 17), fill="#ffffff")
    if center_top:
        c.center_text(cx, cy-11, center_top, B.F("ExtraBold", 22), fill=T[1])
    if center_bot:
        c.center_text(cx, cy+14, center_bot, B.F("Medium", 13), fill=N[2])
    if note:
        ny = cy + R + 44
        c.rect([B.PAD, ny, W-B.PAD, ny+44], fill=G[5], radius=10)
        c.rect([B.PAD, ny+6, B.PAD+5, ny+38], fill=G[0], radius=2)
        c.center_text(W/2, ny+22, note, B.F("SemiBold", 16), fill=G[0])
    c.save(out)


def _arrowhead(c, x, y, ang, size, col):
    c.polygon([x, y,
               x-size*math.cos(ang-0.42), y-size*math.sin(ang-0.42),
               x-size*math.cos(ang+0.42), y-size*math.sin(ang+0.42)], fill=col)


# =========================================================
# 3. 넘버링/프로세스형 (세로 배지 + 연결선 + 옅은 카드)
# =========================================================
def process_steps(title, sub, steps, out, axis="teal", icons=None):
    """steps: [(제목, 설명), ...]  icons: [fn,...] 있으면 배지에 아이콘, 없으면 번호"""
    S = AXIS[axis]
    f_step = B.F("ExtraBold", 22); f_desc = B.F("Regular", 18); f_num = B.F("Black", 30)
    badge = 64; tx = B.PAD + badge + 28
    probe = WideCanvas(10, 10)
    longest = max(probe.text_w(d, f_desc) for _, d in steps)
    W = int(min(B.W, max(560, tx + longest + B.PAD))); row_h = 104
    H = int(banner_height(title, sub) + row_h*len(steps) + 20)
    c = WideCanvas(W, H); y0 = banner(c, title, sub); cx = B.PAD + badge/2
    for i, (s, d) in enumerate(steps):
        top = y0 + row_h*i + 14; cyb = top + badge/2
        if i < len(steps)-1:
            c.line([cx, cyb+badge/2, cx, top+row_h-4], fill=S[4], width=3)
        c.ellipse([cx-badge/2, cyb-badge/2, cx+badge/2, cyb+badge/2], fill=_dark(S))
        if icons:
            icons[i](c, cx, cyb, 1.3, "#ffffff", 2)
        else:
            c.center_text(cx, cyb, f"{i+1}", f_num, fill="#ffffff")
        c.rect([tx-14, top, W-B.PAD, top+badge], fill=S[5], radius=10)
        c.text((tx, cyb-badge/2+8), s, f_step, fill=S[0])
        c.text((tx, cyb-badge/2+40), d, f_desc, fill=N[1])
    c.save(out)


# =========================================================
# 4. 계층형 (계단식 들여쓰기 + 우측 설명 + 하단 기준정보 스트립 옵션)
# =========================================================
def hierarchy(title, sub, levels, out, axis="teal", footer_items=None, footer_title=None):
    """levels: [(단계명, 설명), ...] 위→아래 상위→하위 포함"""
    S = AXIS[axis]
    f_lab = B.F("ExtraBold", 21); f_desc = B.F("Regular", 17)
    W = B.W
    box_w = 240; step = 40; row_h = 74
    H = int(banner_height(title, sub) + row_h*len(levels) + 20
            + (120 if footer_items else 0))
    c = WideCanvas(W, H); y0 = banner(c, title, sub)
    for i, (lab, desc) in enumerate(levels):
        x = B.PAD + step*i
        y = y0 + row_h*i
        shade = S[max(1, 1+i) if 1+i <= 4 else 4]
        # 연결선
        if i > 0:
            c.line([B.PAD+step*(i-1)+18, y-row_h+56, B.PAD+step*(i-1)+18, y+28],
                   fill=S[4], width=3)
            c.line([B.PAD+step*(i-1)+18, y+28, x, y+28], fill=S[4], width=3)
        c.rect([x, y+8, x+box_w, y+56], fill=shade, radius=10)
        # 라벨 (밝은 칸이면 잉크, 진한 칸이면 흰색)
        lab_col = "#ffffff" if i <= 1 else T[0]
        c.center_text(x+box_w/2, y+32, lab, f_lab, fill=lab_col)
        c.text((x+box_w+24, y+22), desc, f_desc, fill=BODY)
    if footer_items:
        fy = y0 + row_h*len(levels) + 12
        c.rect([B.PAD, fy, W-B.PAD, fy+96], fill=N[5], radius=12)
        if footer_title:
            c.text((B.PAD+20, fy+14), footer_title, B.F("Bold", 17), fill=T[0])
        cols = len(footer_items)
        cw = (W-B.PAD*2-40)/cols
        for k, (nm, ic) in enumerate(footer_items):
            fx = B.PAD+20 + cw*k
            icon_disc(c, fx+24, fy+58, 18, T[1], ic, 0.95)
            c.text((fx+50, fy+48), nm, B.F("SemiBold", 16), fill=T[0])
    c.save(out)


# =========================================================
# 5. 숫자/차트형 (수평 편차 바 + 통계 해설 카드)
# =========================================================
def variance_bars(title, sub, rows, out, pos_axis="teal", neg_axis="berry",
                  stat_cards=None):
    """rows: [(라벨, 값(부호포함)), ...]  stat_cards: [(제목, 설명, 축), ...]"""
    W = B.W
    f_lab = B.F("SemiBold", 18); f_val = B.F("ExtraBold", 19)
    labw = 90; padx = B.PAD
    zero_x = padx + labw + 130   # 0 기준선 위치
    maxabs = max(abs(v) for _, v in rows)
    scale = (W - zero_x - padx - 60) / maxabs   # 양수 방향 최대폭
    left_room = (zero_x - padx - labw - 20)
    scale = min(scale, left_room / maxabs)
    row_h = 46
    chart_h = row_h*len(rows) + 20
    card_h = 120 if stat_cards else 0
    H = int(banner_height(title, sub) + chart_h + card_h + 24)
    c = WideCanvas(W, H); y0 = banner(c, title, sub)
    # 0 기준선
    c.line([zero_x, y0, zero_x, y0+chart_h-20], fill=N[4], width=2)
    for i, (lab, v) in enumerate(rows):
        cy = y0 + row_h*i + row_h/2
        c.text((padx, cy-11), lab, f_lab, fill=N[1])
        S = AXIS[pos_axis] if v >= 0 else AXIS[neg_axis]
        bw = abs(v)*scale
        if v >= 0:
            c.rect([zero_x, cy-13, zero_x+bw, cy+13], fill=_dark(S), radius=5)
            c.text((zero_x+bw+10, cy-11), f"+{v}", f_val, fill=S[1] if S is not G else G[0])
        else:
            c.rect([zero_x-bw, cy-13, zero_x, cy+13], fill=_dark(S), radius=5)
            c.text((zero_x-bw-46, cy-11), f"{v}", f_val, fill=S[1])
    if stat_cards:
        fy = y0 + chart_h + 8
        cols = len(stat_cards); cw = (W-B.PAD*2-20*(cols-1))/cols
        for k, (t, d, ax) in enumerate(stat_cards):
            S = AXIS[ax]; fx = B.PAD + (cw+20)*k
            c.rect([fx, fy, fx+cw, fy+card_h-10], fill=S[5], radius=12)
            c.rect([fx, fy, fx+6, fy+card_h-10], fill=_dark(S), radius=3)
            c.text((fx+22, fy+16), t, B.F("ExtraBold", 20), fill=T[0])
            for j, ln in enumerate(F.wrap(c, d, B.F("Regular", 16), cw-44)):
                c.text((fx+22, fy+50+j*23), ln, B.F("Regular", 16), fill=N[1])
    c.save(out)


# =========================================================
# 6. 통합 허브형 (중앙 노드 + 방사형 위성 + 연결선)
# =========================================================
def hub_spokes(title, sub, center, satellites, out, note=None):
    """center: (라벨,) / satellites: [(라벨, 아이콘fn, 축), ...] 4~6개"""
    W = B.W; H = 620 if not note else 680
    c = WideCanvas(W, H); y0 = banner(c, title, sub)
    cx = W/2; cy = y0 + (H-y0)/2 + (0 if not note else -20)
    Rsat = 175; sat_r = 54; hub_r = 66
    nnum = len(satellites)
    pts = []
    for i in range(nnum):
        a = math.radians(-90 + i*360/nnum)
        pts.append((cx+Rsat*math.cos(a), cy+Rsat*math.sin(a)))
    # 연결선 먼저
    for (px, py) in pts:
        c.line([cx, cy, px, py], fill=T[4], width=3)
    # 중앙 허브
    c.ellipse([cx-hub_r, cy-hub_r, cx+hub_r, cy+hub_r], fill=T[1])
    for j, ln in enumerate(F.wrap(c, center, B.F("ExtraBold", 22), hub_r*2-16)):
        c.center_text(cx, cy-10+j*26, ln, B.F("ExtraBold", 22), fill="#ffffff")
    # 위성
    for (px, py), (lab, icon, axname) in zip(pts, satellites):
        S = AXIS[axname]
        c.ellipse([px-sat_r, py-sat_r, px+sat_r, py+sat_r], fill="#ffffff",
                  outline=_dark(S), width=3)
        icon(c, px, py-14, 1.25, _dark(S), 2)
        c.center_text(px, py+26, lab, B.F("Bold", 17), fill=T[0])
    if note:
        ny = cy + Rsat + sat_r + 20
        c.center_text(W/2, ny, note, B.F("Medium", 17), fill=N[1])
    c.save(out)


# =========================================================
# 7. 가운데 대칭 비교형 (좌 vs 우, 가운데 라벨 축 + vs 배지)
# =========================================================
def compare_center(title, sub, colA, colB, rows, out, footer=None):
    """colA/colB: (헤더, 부제, 축)  rows: [(라벨, 좌값, 우값), ...]"""
    SA = AXIS[colA[2]]; SB = AXIS[colB[2]]
    W = B.W
    probe = WideCanvas(10, 10)
    f_head = B.F("ExtraBold", 21); f_hsub = B.F("Medium", 14)
    f_val = B.F("SemiBold", 18); f_lab = B.F("Bold", 18)
    lab_w = max(max(probe.text_w(r[0], f_lab) for r in rows) + 44, 130)
    side_gap = 26
    col_w = (W - B.PAD*2 - lab_w - side_gap*2) / 2
    head_h = 66; row_hh = 60; foot_h = 60 if footer else 0
    H = int(banner_height(title, sub) + head_h + row_hh*len(rows) + foot_h + 34)
    c = WideCanvas(W, H); y0 = banner(c, title, sub)
    xA = B.PAD; xMid = B.PAD + col_w + side_gap; xB = xMid + lab_w + side_gap
    for (x, col, S) in ((xA, colA, SA), (xB, colB, SB)):
        c.rect([x, y0, x+col_w, y0+head_h], fill=_dark(S), radius=12)
        c.center_text(x+col_w/2, y0+24, col[0], f_head, fill="#ffffff")
        if col[1]:
            c.center_text(x+col_w/2, y0+47, col[1], f_hsub, fill=S[5])
    vs_y = y0 + head_h/2
    c.ellipse([xMid+lab_w/2-22, vs_y-22, xMid+lab_w/2+22, vs_y+22], fill=N[0])
    c.center_text(xMid+lab_w/2, vs_y, "vs", B.F("ExtraBold", 17), fill="#ffffff")
    yv = y0 + head_h + 12
    for i, (lab, va, vb) in enumerate(rows):
        ry = yv + row_hh*i; cyc = ry + row_hh/2
        c.rect([xA, ry+5, xA+col_w, ry+row_hh-5], fill=SA[5], radius=9)
        c.ellipse([xA+col_w-26, cyc-4, xA+col_w-18, cyc+4], fill=SA[2])
        for j, ln in enumerate(F.wrap(c, va, f_val, col_w-46)):
            c.center_text(xA+col_w/2-10, cyc-8+j*22 if len(F.wrap(c,va,f_val,col_w-46))>1 else cyc, ln, f_val, fill=N[0])
        c.center_text(xMid+lab_w/2, cyc, lab, f_lab, fill=N[1])
        c.rect([xB, ry+5, xB+col_w, ry+row_hh-5], fill=SB[5], radius=9)
        c.ellipse([xB+18, cyc-4, xB+26, cyc+4], fill=SB[2])
        for j, ln in enumerate(F.wrap(c, vb, f_val, col_w-46)):
            c.center_text(xB+col_w/2+10, cyc-8+j*22 if len(F.wrap(c,vb,f_val,col_w-46))>1 else cyc, ln, f_val, fill=N[0])
    if footer:
        fy = yv + row_hh*len(rows) + 10
        c.rect([B.PAD, fy, W-B.PAD, fy+foot_h-8], fill=T[0], radius=10)
        c.center_text(W/2, fy+(foot_h-8)/2, footer, B.F("SemiBold", 16), fill="#ffffff")
    c.save(out)


# =========================================================
# 8. 가로 타임라인 (트랙 + 노드 + 위/아래 지그재그)
# =========================================================
def timeline_h(title, sub, headline, stops, out, foot=None):
    """stops: [(top라벨, 메인라벨, 설명, 강조, 축), ...]. top라벨=연도/시각/번호."""
    W = B.W; PAD = B.PAD
    f_head = B.F("ExtraBold", 22)
    f_top = B.F("ExtraBold", 20); f_lab = B.F("ExtraBold", 20); f_desc = B.F("Medium", 16)
    y0 = banner_height(title, sub)
    headline_h = 40 if headline else 0
    block_h = 150          # 라벨 블록 높이(위/아래 각각)
    track_y = y0 + headline_h + block_h + 20
    H = int(track_y + block_h + (60 if foot else 0) + 20)
    c = WideCanvas(W, H)
    banner(c, title, sub)
    if headline:
        c.center_text(W/2, y0+14, headline, f_head, fill=INK)
    n = len(stops); inset = 96
    x0, x1 = PAD+inset, W-PAD-inset
    c.rect([PAD+16, track_y-4, W-PAD-16, track_y+4], fill=N[4], radius=4)
    xs = [x0+(x1-x0)*i/(n-1) for i in range(n)]
    node = 26
    for i, (top, lab, desc, emph, axname) in enumerate(stops):
        S = AXIS[axname]; dark = _dark(S); x = xs[i]
        r = node  # 크기 통일(강조는 색으로만)
        c.ellipse([x-r, track_y-r, x+r, track_y+r], fill=dark)
        if top is not None and str(top).isdigit() and len(str(top))<=2:
            c.center_text(x, track_y, str(top), B.F("Black", 22), fill="#ffffff")
        above = (i % 2 == 0)
        col_top = dark
        if above:
            yy = track_y - r - 20
            # 아래에서 위로 쌓기: 설명 → 라벨 → top
            if desc:
                dl = str(desc).split("\n")
                for ln in reversed(dl):
                    c.center_text(x, yy, ln, f_desc, fill=BODY); yy -= 24
            for ln in reversed(str(lab).split("\n")):
                c.center_text(x, yy, ln, f_lab, fill=T[0]); yy -= 26
            if top is not None and not (str(top).isdigit() and len(str(top))<=2):
                c.center_text(x, yy, str(top), f_top, fill=col_top); yy -= 26
        else:
            yy = track_y + r + 22
            if top is not None and not (str(top).isdigit() and len(str(top))<=2):
                c.center_text(x, yy, str(top), f_top, fill=col_top); yy += 28
            for ln in str(lab).split("\n"):
                c.center_text(x, yy, ln, f_lab, fill=T[0]); yy += 26
            if desc:
                for ln in str(desc).split("\n"):
                    c.center_text(x, yy, ln, f_desc, fill=BODY); yy += 24
    if foot:
        fy = H - 60
        c.rect([PAD, fy, W-PAD, fy+44], fill=T[5], radius=10)
        c.center_text(W/2, fy+22, foot, B.F("SemiBold", 16), fill=T[0])
    c.save(out)


# =========================================================
# 9. 감정 곡선 (점선 꺾은선 + 노드 + 라벨/인용구)
# =========================================================
def curve_line(title, sub, headline, points, out, ylabel=None):
    """points: [(라벨, 인용구, 상대높이 0~1), ...]. 축색 자동(청록/베리/골드/청록)."""
    W = B.W; PAD = B.PAD
    f_head = B.F("ExtraBold", 22)
    f_lab = B.F("ExtraBold", 20); f_q = B.F("Medium", 16); f_num = B.F("Black", 22)
    axis_cycle = [T, BE, G, T, BE]
    y0 = banner_height(title, sub)
    headline_h = 40 if headline else 0
    plot_top = y0 + headline_h + 120
    plot_h = 300
    H = int(plot_top + plot_h + 120)
    c = WideCanvas(W, H)
    banner(c, title, sub)
    if headline:
        c.center_text(W/2, y0+14, headline, f_head, fill=INK)
    n = len(points)
    gx0, gx1 = PAD+90, W-PAD-100
    xs = [gx0+(gx1-gx0)*i/(n-1) for i in range(n)]
    ys = [plot_top + plot_h*(1-h) for (_,_,h) in points]
    # (y축·ylabel 없음 — 곡선의 오르내림 자체가 생산성 변화를 나타냄)
    # 점선 연결
    for i in range(n-1):
        x_a,y_a=xs[i],ys[i]; x_b,y_b=xs[i+1],ys[i+1]
        steps=int(((x_b-x_a)**2+(y_b-y_a)**2)**0.5/14)
        for s in range(steps+1):
            t=s/steps; px=x_a+(x_b-x_a)*t; py=y_a+(y_b-y_a)*t
            c.ellipse([px-2.5,py-2.5,px+2.5,py+2.5], fill=G[3])
    # 노드 + 라벨
    for i,((lab,quote,h),x,y) in enumerate(zip(points,xs,ys)):
        S=axis_cycle[i]; dark=_dark(S)
        r=26
        c.ellipse([x-r,y-r,x+r,y+r], fill=dark)
        c.center_text(x,y,str(i+1),f_num,fill="#ffffff")
        # 라벨: 노드가 위쪽(높이 큰)이면 라벨을 위, 아래면 아래
        up = h >= 0.5
        if up:
            c.center_text(x, y-r-46, lab, f_lab, fill=T[0])
            c.center_text(x, y-r-22, quote, f_q, fill=BODY)
        else:
            c.center_text(x, y+r+24, lab, f_lab, fill=T[0])
            c.center_text(x, y+r+48, quote, f_q, fill=BODY)
    c.save(out)


# =========================================================
# 10. Before/After 2단 플로우 (위=점선 끊김, 아래=실선 연결)
# =========================================================
def flow_before_after(title, sub, before_label, before, after_label, after, foot, out):
    """before/after: [(라벨, 설명), ...] 각 4개. 위는 점선+빈 노드, 아래는 실선+채운 노드."""
    W = B.W; PAD = B.PAD
    f_seclab = B.F("ExtraBold", 19)
    f_lab = B.F("ExtraBold", 19); f_desc = B.F("Medium", 16)
    y0 = banner_height(title, sub)
    sec_gap = 40
    band_h = 150
    foot_h = 56
    H = int(y0 + 10 + band_h + sec_gap + band_h + 30 + foot_h + 20)
    c = WideCanvas(W, H)
    banner(c, title, sub)

    n = len(before)
    inset = 40
    x0, x1 = PAD+inset+30, W-PAD-inset-30
    xs = [x0+(x1-x0)*i/(n-1) for i in range(n)]
    node = 18

    def draw_band(top, label, items, connected, axis):
        S = AXIS[axis]; dark = _dark(S)
        # 섹션 라벨
        c.rect([PAD, top, PAD+5, top+24], fill=dark, radius=2)
        c.text((PAD+16, top), label, f_seclab, fill=dark)
        track_y = top + 92
        # 라벨/설명은 노드 위
        for i, (lab, desc) in enumerate(items):
            x = xs[i]
            c.center_text(x, track_y-52, lab, f_lab, fill=T[0] if connected else B.NEUT_S[1])
            c.center_text(x, track_y-28, desc, f_desc, fill=BODY if connected else SUBTLE)
        # 연결선 + 화살표
        for i in range(n-1):
            xa, xb = xs[i], xs[i+1]
            if connected:
                c.line([xa+node+4, track_y, xb-node-14, track_y], fill=dark, width=4)
                c.polygon([xb-node-4, track_y, xb-node-16, track_y-7, xb-node-16, track_y+7], fill=dark)
            else:
                # 점선
                seg = xb-node-6-(xa+node+6)
                steps = int(seg/14)
                for s in range(steps):
                    px = xa+node+6 + seg*s/steps
                    c.line([px, track_y, px+6, track_y], fill=B.NEUT_S[3], width=3)
                c.polygon([xb-node-2, track_y, xb-node-12, track_y-6, xb-node-12, track_y+6], fill=B.NEUT_S[3])
        # 노드
        for i, x in enumerate(xs):
            if connected:
                c.ellipse([x-node, track_y-node, x+node, track_y+node], fill=dark)
            else:
                c.ellipse([x-node, track_y-node, x+node, track_y+node], fill="#ffffff", outline=BE[2], width=3)

    top1 = y0 + 10
    draw_band(top1, before_label, before, False, "berry")
    # (중간 구분선 없음 — 여백으로만 구분)
    top2 = top1 + band_h + sec_gap
    draw_band(top2, after_label, after, True, "teal")
    # 하단 결론
    fy = H - foot_h - 10
    c.rect([PAD, fy, W-PAD, fy+foot_h-8], fill=T[0], radius=10)
    c.center_text(W/2, fy+(foot_h-8)/2, foot, B.F("SemiBold", 16), fill="#ffffff")
    c.save(out)


# =========================================================
# 11. 3열 카드 + 메타줄 + 하단 강조 바 (ADsP 등)
# =========================================================
def three_col_cards(title, meta, tags, names, items_list, foot_title, foot_sub, out):
    W = B.W; PAD = B.PAD
    y0 = banner_height(title, None)   # 부제 없음, meta로 대체
    # 메타줄
    f_meta = B.F("Medium", 17)
    meta_h = 40
    card_top = y0 + meta_h + 24
    gap = 20
    cw = (W - PAD*2 - gap*2) / 3
    f_tag = B.F("Bold", 15); f_name = B.F("ExtraBold", 24); f_item = B.F("Medium", 17)
    maxitems = max(len(x) for x in items_list)
    card_h = 60 + 44 + 24 + maxitems*30 + 20
    foot_h = 78
    H = int(card_top + card_h + 24 + foot_h + 20)
    c = WideCanvas(W, H)
    banner(c, title, None)
    c.center_text(W/2, y0+meta_h/2-4, meta, f_meta, fill=SUBTLE)
    for i in range(3):
        x = PAD + i*(cw+gap)
        dark = T[1]
        c.rect([x, card_top, x+cw, card_top+card_h], fill=T[1], radius=14)
        # 태그 pill (골드)
        pw = c.text_w(tags[i], f_tag)
        c.rect([x+cw/2-(pw/2+18), card_top+18, x+cw/2+(pw/2+18), card_top+18+30], fill=G[1], radius=15)
        c.center_text(x+cw/2, card_top+18+15, tags[i], f_tag, fill="#ffffff")
        # 과목명
        c.center_text(x+cw/2, card_top+74, names[i], f_name, fill="#ffffff")
        c.line([x+30, card_top+104, x+cw-30, card_top+104], fill=T[3], width=1)
        yy = card_top+128
        for it in items_list[i]:
            c.center_text(x+cw/2, yy, it, f_item, fill="#e8f0ef")
            yy += 30
    # 하단 바
    fy = card_top + card_h + 24
    c.rect([PAD, fy, W-PAD, fy+foot_h], fill=G[1], radius=14)
    c.center_text(W/2, fy+26, foot_title, B.F("ExtraBold", 21), fill="#ffffff")
    c.center_text(W/2, fy+54, foot_sub, B.F("Medium", 17), fill="#fdf3e3")
    c.save(out)


# =========================================================
# 12. 좌우 2분할 대비 (오더 번호대 등)
# =========================================================
def split_two(title, sub, headline, key_note, ranges, range_note, foot, out, icon=None):
    """ranges: [(라벨, 값문자열, 축), ...] 2개"""
    W = B.W; PAD = B.PAD
    y0 = banner_height(title, sub)
    f_head = B.F("ExtraBold", 24); f_note = B.F("Medium", 16)
    f_rlab = B.F("ExtraBold", 21); f_rval = B.F("ExtraBold", 20)
    c_y = y0 + 20
    H = int(y0 + 20 + 40 + 30 + (70 if icon else 0) + 76 + 30 + 40 + 60 + 30)
    c = WideCanvas(W, H)
    banner(c, title, sub)
    yy = y0 + 20
    c.center_text(W/2, yy+16, headline, f_head, fill=INK); yy += 46
    c.center_text(W/2, yy+12, key_note, f_note, fill=SUBTLE); yy += 44
    # 아이콘(공장) + 라벨
    bar_y = yy + (60 if icon else 20)
    half = (W - PAD*2) / 2
    for i, (lab, val, axname) in enumerate(ranges):
        S = AXIS[axname]; dark = _dark(S)
        cx = PAD + half*i + half/2
        if icon:
            icon(c, cx, yy+22, 1.6, dark, 2)
        c.center_text(cx, bar_y-16, lab, f_rlab, fill=dark)
    # 좌우 바
    bar_h = 60
    c.rect([PAD, bar_y, PAD+half, bar_y+bar_h], fill=_dark(AXIS[ranges[0][2]]),
           radius=0)
    c.rect([PAD+half, bar_y, W-PAD, bar_y+bar_h], fill=_dark(AXIS[ranges[1][2]]),
           radius=0)
    for i, (lab, val, axname) in enumerate(ranges):
        cx = PAD + half*i + half/2
        c.center_text(cx, bar_y+bar_h/2, val, f_rval, fill="#ffffff")
    ry = bar_y + bar_h + 24
    c.center_text(W/2, ry+10, range_note, f_note, fill=SUBTLE); ry += 44
    # 하단 결론
    c.rect([PAD, ry, W-PAD, ry+52], fill=T[0], radius=10)
    c.center_text(W/2, ry+26, foot, B.F("SemiBold", 16), fill="#ffffff")
    c.save(out)


# =========================================================
# 13. 미니 비교표 (행 라벨 + 2열)
# =========================================================
def mini_compare_table(title, sub, headline, colA, colB, rows, cells, foot, out):
    """colA/colB=(제목,부제,축), rows=[행라벨...], cells=[[좌,우],...]"""
    W = B.W; PAD = B.PAD
    SA = AXIS[colA[2]]; SB = AXIS[colB[2]]
    y0 = banner_height(title, sub)
    f_head = B.F("ExtraBold", 22); f_h = B.F("ExtraBold", 20); f_hs = B.F("Medium", 15)
    f_rlab = B.F("Bold", 17); f_val = B.F("Medium", 17)
    head_line = y0 + 10
    lab_w = 130
    tbl_top = head_line + 44
    head_h = 66; row_h = 58
    H = int(tbl_top + head_h + row_h*len(rows) + 20 + 56 + 20)
    c = WideCanvas(W, H)
    banner(c, title, sub)
    c.center_text(W/2, head_line+14, headline, f_head, fill=INK)
    cw = (W - PAD*2 - lab_w) / 2
    xA = PAD + lab_w; xB = xA + cw
    # 헤더
    c.rect([xA, tbl_top, xA+cw, tbl_top+head_h], fill=_dark(SA), radius=10)
    c.center_text(xA+cw/2, tbl_top+24, colA[0], f_h, fill="#ffffff")
    c.center_text(xA+cw/2, tbl_top+46, colA[1], f_hs, fill=SA[5])
    c.rect([xB, tbl_top, xB+cw, tbl_top+head_h], fill=_dark(SB), radius=10)
    c.center_text(xB+cw/2, tbl_top+24, colB[0], f_h, fill="#ffffff")
    c.center_text(xB+cw/2, tbl_top+46, colB[1], f_hs, fill=SB[5])
    # 행
    yv = tbl_top + head_h
    for i, rlab in enumerate(rows):
        ry = yv + row_h*i
        if i % 2 == 0:
            c.rect([PAD, ry, W-PAD, ry+row_h], fill=N[5], radius=6)
        c.center_text(PAD+lab_w/2, ry+row_h/2, rlab, f_rlab, fill=T[0])
        c.center_text(xA+cw/2, ry+row_h/2, cells[i][0], f_val, fill=BODY)
        c.center_text(xB+cw/2, ry+row_h/2, cells[i][1], f_val, fill=BODY)
    fy = yv + row_h*len(rows) + 16
    c.rect([PAD, fy, W-PAD, fy+52], fill=T[5], radius=10)
    c.center_text(W/2, fy+26, foot, B.F("SemiBold", 16), fill=T[0])
    c.save(out)
