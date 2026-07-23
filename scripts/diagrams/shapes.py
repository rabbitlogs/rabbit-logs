# -*- coding: utf-8 -*-
"""
레이어 2 확장 템플릿 — 카드형 외의 형태들.

마스터 프롬프트 §9 "도식 유형 선택"의 관계→형태 대응표를 코드로 구현한 것.
내용의 관계가 순서가 아닐 때(변화·순환·포함·중심·대비·시간) 여기서 고른다.

화살표 간격 규칙(§9): 간격은 카드 수와 무관하게 최소 44px, gap/head는 간격에 비례.
"""
import math
from PIL import Image, ImageDraw
from brand import *


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


def arrow_between(d, x0, x1, y, gap_px, color=MARIGOLD):
    """§9 규칙: gap·head를 간격에 비례시키고, 선이 남는지 검증한다."""
    span = x1 - x0
    gap = max(8, span * 0.28)
    head = max(10, span * 0.32)
    if span - gap * 2 - head < 8:          # 선이 소멸하는 구간 → 머리만 축소
        head = max(9, span - gap * 2 - 8)
    arrow(d, x0 + gap, y, x1 - gap, color=color, width=6, head=int(head))


# ══ 곡선형 — 감정·성과의 오르내림 ═══════════════════════════════════════════
def curve(out, banner, headline, points, sub=None, ylabel=None):
    """points = [(라벨, 인용구, 상대높이 0~1), ...] — U자 곡선 위에 배치."""
    f_lbl = font("Bold", 19)
    f_q   = font("Regular", 15)
    f_y   = font("Medium", 14)

    # 곡선 위/아래에 라벨과 인용구가 붙으므로 상하 여백을 넉넉히 확보한다.
    top = BANNER_H + (92 if headline else 44)
    plot_h = 232
    pad_top, pad_bot = 128, 110
    img_h = int(top + pad_top + plot_h + pad_bot)
    img, d = new_canvas(img_h)
    draw_banner(d, banner, sub)
    if headline:
        draw_headline(d, BANNER_H + 30, headline)

    # 양끝 점의 인용구가 잘리지 않도록 좌우를 들여 그린다.
    x0, x1 = MARGIN + 152, W - MARGIN - 118
    y_top, y_bot = top + pad_top, top + pad_top + plot_h

    # 세로축 안내 — 축은 캔버스 왼쪽 끝에 두고, 라벨은 축 아래쪽에 가로로 쓴다.
    # (글자를 한 자씩 세로로 쌓으면 영문이 'P r o d u c t i v i t y'가 되어 읽기 어렵고,
    #  축 라벨을 위쪽에 두면 첫 번째 점의 라벨과 겹친다.)
    if ylabel:
        ax = MARGIN + 34
        d.line([(ax, y_top), (ax, y_bot)], fill=LINE, width=2)
        d.polygon([(ax, y_top - 9), (ax - 5, y_top + 1), (ax + 5, y_top + 1)], fill=LINE)
        d.text((ax - text_w(d, ylabel, f_y) / 2, y_bot + 10), ylabel, font=f_y, fill=MUTED)

    n = len(points)
    xs = [x0 + (x1 - x0) * i / (n - 1) for i in range(n)]
    ys = [y_bot - (y_bot - y_top) * p[2] for p in points]

    # 부드러운 곡선 — 인접 점 사이를 2차 베지어로 잇는다
    for i in range(n - 1):
        ax, ay, bx, by = xs[i], ys[i], xs[i + 1], ys[i + 1]
        mx = (ax + bx) / 2
        for t in range(41):
            u = t / 40
            cx_ = (1 - u) ** 2 * ax + 2 * (1 - u) * u * mx + u ** 2 * bx
            cy_ = (1 - u) ** 2 * ay + 2 * (1 - u) * u * ((ay + by) / 2) + u ** 2 * by
            d.ellipse([cx_ - 2, cy_ - 2, cx_ + 2, cy_ + 2], fill="#c9b487")

    for i, (lbl, quote, _) in enumerate(points):
        cx_, cy_ = xs[i], ys[i]
        col = [TEAL, BERRY, MARIGOLD, TEAL][i % 4]
        r = 17
        d.ellipse([cx_ - r, cy_ - r, cx_ + r, cy_ + r], fill=col)
        true_center_text(d, cx_, cy_, str(i + 1), font("Bold", 18), WHITE)

        # 라벨은 곡선의 바깥쪽(값이 높으면 위, 낮으면 아래)에 붙여 곡선과 겹치지 않게 한다.
        high = points[i][2] >= 0.5
        # 인용구는 되도록 한 줄로. 이웃 점과의 간격뿐 아니라 캔버스 좌우 여백까지 쓴다
        # (인접 라벨은 곡선 높이가 달라 세로로 어긋나므로 가로로 조금 겹쳐도 읽기에 문제없다).
        neigh = min([abs(xs[i] - xs[j]) for j in range(n) if j != i])
        room_l = (cx_ - 8) * 2
        room_r = (W - cx_ - 8) * 2
        avail = min(max(neigh + 84, 250), room_l, room_r)
        qlines = _wrap(d, quote, f_q, avail)
        if high:
            qy_start = cy_ - r - 30 - len(qlines) * 20
            ly = qy_start - 26
        else:
            ly = cy_ + r + 16
            qy_start = ly + 26
        center_x_text(d, cx_, ly, lbl, f_lbl, col)
        qy = qy_start
        for ln in qlines:
            center_x_text(d, cx_, qy, ln, f_q, MUTED)
            qy += 20

    save(img, out)


# ══ 순환형 — 자기 참조·되돌아옴 ════════════════════════════════════════════
def cycle(out, banner, headline, nodes, center_note=None, sub=None, loop_label=None):
    """
    nodes = [(제목, [설명...]), ...] — 가로로 나열하고, 마지막에서 처음으로
    되돌아오는 곡선을 아래로 크게 둘러 그린다.

    원형(방사형) 배치를 쓰지 않는 이유: 노드가 3개면 아래 두 박스의 x 간격이
    박스 폭보다 좁아 서로 맞붙고, 순환 화살표가 박스 뒤로 숨어 "되돌아온다"는
    핵심이 보이지 않는다. 가로 배치 + 하단 회귀 곡선이 순환을 훨씬 분명히 보여준다.
    """
    f_t = font("Bold", 19)
    f_b = font("Regular", 15)
    f_c = font("Bold", 16)

    top = BANNER_H + (86 if headline else 40)
    n = len(nodes)
    gap_x = 62                                   # §9: 화살표가 살 수 있게 최소 44px 이상
    card_w = (W - MARGIN * 2 - gap_x * (n - 1)) / n
    body_n = max(len(b) for _, b in nodes)
    card_h = 34 + 28 + 16 + body_n * 22 + 22
    loop_h = 74                                  # 하단 회귀 곡선이 차지할 높이
    note_h = 46 if center_note else 0
    img_h = int(top + card_h + loop_h + note_h + 30)

    img, d = new_canvas(img_h)
    draw_banner(d, banner, sub)
    if headline:
        draw_headline(d, BANNER_H + 28, headline)

    xs = []
    for i, (title, body) in enumerate(nodes):
        x0 = MARGIN + i * (card_w + gap_x)
        x1 = x0 + card_w
        cx_ = (x0 + x1) / 2
        xs.append((x0, x1, cx_))
        col = [TEAL, MARIGOLD, BERRY][i % 3]
        pale = [TEAL_PALE, GOLD_PALE, BERRY_PALE][i % 3]
        d.rounded_rectangle([x0, top, x1, top + card_h], radius=14,
                            fill=pale, outline=col, width=2)
        center_x_text(d, cx_, top + 20, title, f_t, col)
        by = top + 20 + 30
        dotted_line(d, x0 + 26, x1 - 26, by)
        by += 16
        for ln in body:
            center_x_text(d, cx_, by, ln, f_b, INK)
            by += 22

    # 앞으로 흐르는 화살표 (§9 규칙: gap·head를 간격에 비례)
    ay = top + card_h / 2
    for i in range(n - 1):
        arrow_between(d, xs[i][1], xs[i + 1][0], ay, gap_x)

    # 되돌아오는 곡선 — 마지막 카드 아래 → 첫 카드 아래로 크게 둘러 온다
    ly = top + card_h + loop_h - 24
    sx, ex = xs[-1][2], xs[0][2]
    d.line([(sx, top + card_h + 4), (sx, ly - 14)], fill=MARIGOLD, width=4)
    steps = 60
    pts = []
    for s in range(steps + 1):
        t = s / steps
        # 좌우 끝을 둥글게 잇는 완만한 곡선
        px = sx + (ex - sx) * t
        py = ly - 14 - math.sin(math.pi * t) * 16
        pts.append((px, py))
    for s in range(len(pts) - 1):
        d.line([pts[s], pts[s + 1]], fill=MARIGOLD, width=4)
    # 첫 카드 밑면으로 올라가는 화살표 머리
    d.line([(ex, ly - 14), (ex, top + card_h + 18)], fill=MARIGOLD, width=4)
    d.polygon([(ex, top + card_h + 4), (ex - 9, top + card_h + 20),
               (ex + 9, top + card_h + 20)], fill=MARIGOLD)

    lbl = font("Bold", 15)
    txt = loop_label or ""
    tw = text_w(d, txt, lbl) if txt else 0
    if txt:
        mxp = (sx + ex) / 2
        d.rectangle([mxp - tw / 2 - 10, ly - 32, mxp + tw / 2 + 10, ly - 10], fill=BG)
        true_center_text(d, mxp, ly - 21, txt, lbl, MARIGOLD_D)

    if center_note:
        ny = top + card_h + loop_h + 2
        d.rounded_rectangle([MARGIN, ny, W - MARGIN, ny + 40], radius=11, fill=GOLD_PALE)
        true_center_text(d, W / 2, ny + 20, center_note, f_c, MARIGOLD_D)

    save(img, out)


# ══ 계층형 — 상위가 하위를 포함 ════════════════════════════════════════════
def hierarchy(out, banner, headline, levels, sub=None, note=None):
    """levels = [(제목, 영문, 설명), ...] — 위에서 아래로 폭이 좁아지는 계단."""
    f_t = font("Bold", 21)
    f_e = font("Medium", 13)
    f_d = font("Regular", 15)

    top = BANNER_H + (90 if headline else 42)
    row_h, gap = 64, 15
    n = len(levels)
    img_h = int(top + n * (row_h + gap) + (54 if note else 0) + 40)
    img, d = new_canvas(img_h)
    draw_banner(d, banner, sub)
    if headline:
        draw_headline(d, BANNER_H + 28, headline)

    max_w, min_w = W - MARGIN * 2, W - MARGIN * 2 - 300
    cols = [TEAL, MARIGOLD, BERRY, TEAL_LIGHT]
    for i, (title, eng, desc) in enumerate(levels):
        w = max_w - (max_w - min_w) * i / max(1, n - 1)
        x0 = (W - w) / 2
        y = top + i * (row_h + gap)
        col = cols[i % len(cols)]
        d.rounded_rectangle([x0, y, x0 + w, y + row_h], radius=13, fill=col)
        d.text((x0 + 26, y + 12), title, font=f_t, fill=WHITE)
        if eng:
            d.text((x0 + 26, y + 39), eng, font=f_e, fill="#dce8e5")
        tw = text_w(d, desc, f_d)
        d.text((x0 + w - 26 - tw, y + (row_h - 18) / 2), desc, font=f_d, fill="#eef4f2")
        # 포함 관계를 나타내는 아래 방향 표시
        if i < n - 1:
            mx = W / 2
            d.polygon([(mx - 9, y + row_h + 3), (mx + 9, y + row_h + 3),
                       (mx, y + row_h + gap - 2)], fill="#c9b487")

    if note:
        ny = top + n * (row_h + gap) + 6
        d.rounded_rectangle([MARGIN, ny, W - MARGIN, ny + 42], radius=11, fill=TEAL_PALE)
        true_center_text(d, W / 2, ny + 21, note, font("Medium", 15), TEAL)

    save(img, out)


# ══ 허브형 — 중심 하나에 여럿이 연결 ═══════════════════════════════════════
def hub(out, banner, headline, center, spokes, sub=None):
    """center = (제목, 부제), spokes = [(제목, 설명), ...]"""
    f_c  = font("Bold", 22)
    f_cs = font("Medium", 14)
    f_t  = font("Bold", 17)
    f_b  = font("Regular", 14)

    top = BANNER_H + (86 if headline else 40)
    n = len(spokes)
    R = 152
    bw = 268
    # 박스 높이는 실제 본문 줄 수에서 역산한다. 고정값(78)이면 2줄 본문의 아랫줄이
    # 박스 경계를 넘어 삐져나온다(영문에서 특히). 헤더 26 + 줄 수 × 20 + 상하 여백.
    line_h = 20
    tmp_img = Image.new("RGB", (10, 10))
    tmp_d = ImageDraw.Draw(tmp_img)
    body_lines = [_wrap(tmp_d, b, f_b, bw - 28) for _, b in spokes]
    max_lines = max(len(bl) for bl in body_lines)
    bh = 26 + 12 + max_lines * line_h + 14
    # 노드가 3개면 삼각 배치가 좌우로 벌어지지 않아 여백이 남는다 → 가로 확산을 키운다.
    spread = 2.05 if n <= 3 else 1.72

    # 세로 반경(0.90R)과 박스 높이를 합해 실제로 필요한 영역을 잡고 캔버스를 만든다.
    size = int(R * 0.90 * 2 + bh + 40)
    img_h = int(top + size + 46)
    img, d = new_canvas(img_h)
    draw_banner(d, banner, sub)
    if headline:
        draw_headline(d, BANNER_H + 28, headline)
    cx, cy = W / 2, top + size / 2

    for i in range(n):
        a = math.radians(-90 + 360 * i / n)
        nx, ny = cx + R * math.cos(a) * spread, cy + R * math.sin(a) * 0.90
        # 중심에서 노드 경계까지, 양쪽에 gap을 두고 연결선
        dx, dy = nx - cx, ny - cy
        dist = math.hypot(dx, dy)
        ux, uy = dx / dist, dy / dist
        d.line([(cx + ux * 76, cy + uy * 46), (nx - ux * 92, ny - uy * 34)],
               fill="#d5cdbd", width=3)

    for i, (title, body) in enumerate(spokes):
        a = math.radians(-90 + 360 * i / n)
        nx, ny = cx + R * math.cos(a) * spread, cy + R * math.sin(a) * 0.90
        col = [TEAL, MARIGOLD, BERRY][i % 3]
        pale = [TEAL_PALE, GOLD_PALE, BERRY_PALE][i % 3]
        d.rounded_rectangle([nx - bw / 2, ny - bh / 2, nx + bw / 2, ny + bh / 2],
                            radius=12, fill=pale, outline=col, width=2)
        center_x_text(d, nx, ny - bh / 2 + 11, title, f_t, col)
        yy = ny - bh / 2 + 26 + 12
        for ln in body_lines[i]:
            center_x_text(d, nx, yy, ln, f_b, INK)
            yy += line_h

    # 중심 노드 — 타원 + 그라데이션 느낌
    ew, eh = 152, 92
    d.ellipse([cx - ew / 2, cy - eh / 2, cx + ew / 2, cy + eh / 2], fill=TEAL)
    center_x_text(d, cx, cy - 18, center[0], f_c, WHITE)
    if center[1]:
        center_x_text(d, cx, cy + 10, center[1], f_cs, "#cfe0dc")

    save(img, out)


# ══ 타임라인형 — 시간의 경과 ═══════════════════════════════════════════════
def timeline(out, banner, headline, stops, sub=None, foot=None):
    """stops = [(시각, 라벨, 설명, 강조여부), ...] — 가로 트랙 위 지그재그 배치."""
    f_time = font("Bold", 17)
    f_lbl  = font("Bold", 18)
    f_desc = font("Regular", 14)

    top = BANNER_H + (88 if headline else 42)
    track_y = top + 132
    img_h = int(track_y + 170 + (40 if foot else 0))
    img, d = new_canvas(img_h)
    draw_banner(d, banner, sub)
    if headline:
        draw_headline(d, BANNER_H + 28, headline)

    # 양끝 항목의 라벨이 캔버스 밖으로 잘리지 않도록, 트랙은 안쪽으로 충분히 들여 그린다.
    inset = 118
    x0, x1 = MARGIN + inset, W - MARGIN - inset
    d.rounded_rectangle([MARGIN + 24, track_y - 5, W - MARGIN - 24, track_y + 5],
                        radius=5, fill="#e4ddd0")

    n = len(stops)
    xs = [x0 + (x1 - x0) * i / (n - 1) for i in range(n)]
    for i, (tm, lbl, desc, hot) in enumerate(stops):
        cx_ = xs[i]
        col = BERRY if hot else (TEAL if i % 2 == 0 else MARIGOLD)
        r = 15 if hot else 12
        d.ellipse([cx_ - r - 4, track_y - r - 4, cx_ + r + 4, track_y + r + 4], fill=BG)
        d.ellipse([cx_ - r, track_y - r, cx_ + r, track_y + r], fill=col)

        # 위쪽 항목은 설명이 트랙에 닿지 않도록 블록 전체 높이를 재서 위로 쌓아 올린다.
        # desc에 명시적 줄바꿈(\n)이 있으면 그 지점에서 끊고, 없으면 폭 기준 자동 줄바꿈.
        if "\n" in desc:
            dlines = desc.split("\n")[:2]
        else:
            dlines = _wrap(d, desc, f_desc, 208)[:2]
        block_h = 24 + 26 + len(dlines) * 19
        up = i % 2 == 0
        if up:
            ty = track_y - r - 16 - block_h
        else:
            ty = track_y + r + 16
        center_x_text(d, cx_, ty, tm, f_time, col)
        center_x_text(d, cx_, ty + 24, lbl, f_lbl, INK)
        yy = ty + 50
        for ln in dlines:
            center_x_text(d, cx_, yy, ln, f_desc, MUTED)
            yy += 19

    if foot:
        d.rounded_rectangle([MARGIN, img_h - 56, W - MARGIN, img_h - 16],
                            radius=11, fill=TEAL_PALE)
        true_center_text(d, W / 2, img_h - 36, foot, font("Medium", 15), TEAL)

    save(img, out)


# ══ 매트릭스형 — 두 축으로 분류 ════════════════════════════════════════════
def quadrant(out, banner, headline, x_axis, y_axis, quads, sub=None):
    """quads = [(사분면명, [항목...]), ...] 순서: 좌상, 우상, 좌하, 우하"""
    f_q  = font("Bold", 18)
    f_i  = font("Regular", 15)
    f_ax = font("Bold", 14)

    top = BANNER_H + (88 if headline else 42)
    side = 330
    img_h = int(top + side + 74)
    img, d = new_canvas(img_h)
    draw_banner(d, banner, sub)
    if headline:
        draw_headline(d, BANNER_H + 28, headline)

    gx0, gx1 = MARGIN + 96, W - MARGIN - 40
    gy0, gy1 = top, top + side
    mx, my = (gx0 + gx1) / 2, (gy0 + gy1) / 2

    pales = [TEAL_PALE, GOLD_PALE, "#efece5", BERRY_PALE]
    cols  = [TEAL, MARIGOLD_D, "#8a8578", BERRY]
    boxes = [(gx0, gy0, mx, my), (mx, gy0, gx1, my),
             (gx0, my, mx, gy1), (mx, my, gx1, gy1)]

    for i, ((qname, items), bx) in enumerate(zip(quads, boxes)):
        a, b, c, e = bx
        d.rectangle([a + 3, b + 3, c - 3, e - 3], fill=pales[i])
        d.text((a + 18, b + 14), qname, font=f_q, fill=cols[i])
        yy = b + 44
        for it in items[:4]:
            d.ellipse([a + 20, yy + 6, a + 26, yy + 12], fill=cols[i])
            for j, ln in enumerate(_wrap(d, it, f_i, (c - a) - 60)[:2]):
                d.text((a + 34, yy), ln, font=f_i, fill=INK)
                yy += 21
            yy += 4

    d.line([(mx, gy0), (mx, gy1)], fill="#b9b0a0", width=2)
    d.line([(gx0, my), (gx1, my)], fill="#b9b0a0", width=2)

    # 축 라벨은 항상 가로로 쓴다. 세로로 한 글자씩 쌓으면 영문이 'F i t s' 처럼 깨진다.
    center_x_text(d, (gx0 + gx1) / 2, gy1 + 14, x_axis, f_ax, MUTED)
    d.text((MARGIN, gy0 - 26), y_axis, font=f_ax, fill=MUTED)
    d.line([(MARGIN + 6, gy0), (MARGIN + 6, gy1)], fill=LINE, width=2)
    d.polygon([(MARGIN + 6, gy0 - 9), (MARGIN + 1, gy0 + 1), (MARGIN + 11, gy0 + 1)], fill=LINE)

    save(img, out)
