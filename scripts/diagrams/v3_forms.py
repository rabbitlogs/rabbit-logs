# -*- coding: utf-8 -*-
"""
brand_v3 위에 얹는 공용 형태 헬퍼 (레이어 2 공용).

§9 관계→형태 대응표의 형태들을 재사용 가능한 함수로 제공한다.
모든 함수는 폭을 인자로 받는 WideCanvas 위에서 동작한다(폭 역산 지원).

제공 형태:
- numbering_rows : 2K 넘버링 로우 (순차 진행)
- compare_two    : 2G 비교형 (대립·트레이드오프, Before/After)
- hier_center    : 방사/계층 (중심 + 주변)
- mini_table     : 미니 표 직접 그리기 (분류)
공통:
- WideCanvas     : 인스턴스별 폭을 갖는 Canvas
- banner         : banner_B 재노출
- fit_font       : 폭에 맞는 폰트 크기 자동 축소(하한 준수)
"""
import os
import brand_v3 as B
from PIL import Image, ImageDraw


class WideCanvas(B.Canvas):
    """brand_v3.Canvas는 폭 W 전역 고정. 폭 역산을 위해 인스턴스 폭을 갖는 버전."""
    def __init__(self, w, h, bg=B.BG):
        self._w = int(w)
        self.h = int(h)
        self.img = Image.new("RGB", (self._w * B.SCALE, self.h * B.SCALE), bg)
        self.d = ImageDraw.Draw(self.img)

    @property
    def w(self):
        return self._w

    def save(self, path, quality=90):
        self.img.save(path, "JPEG", quality=quality, optimize=True)
        kb = os.path.getsize(path) / 1024
        print(f"저장 {os.path.basename(path)}  {self._w*B.SCALE}x{self.h*B.SCALE}px  {kb:.0f}KB")


def banner_height(title, sub=None):
    c = WideCanvas(10, 10)
    y = 26 + 18
    y += c.text_h(title, B.F("ExtraBold", 27)) + 12
    if sub:
        y += c.text_h(sub, B.F("Medium", 17)) + 10
    return y + 14


def wrap(c, text, font, max_w):
    """공백 기준 줄바꿈. 한 단어가 넘치면 그대로 둔다."""
    words = text.split(" ")
    lines, cur = [], ""
    for wd in words:
        trial = wd if not cur else cur + " " + wd
        if c.text_w(trial, font) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = wd
    if cur:
        lines.append(cur)
    return lines


# ─────────────────────────────────────────────────────────────
# 2K 넘버링 로우
# ─────────────────────────────────────────────────────────────
def numbering_rows(title, sub, steps, out, quality=90,
                   accent="teal", row_h=96, num_col_w=78):
    """steps: [(제목, 설명), ...]  단색 계열 진→옅."""
    axis = {"teal": B.TEAL_S, "gold": B.GOLD_S, "berry": B.BERRY_S}[accent]
    shades = [axis[min(1 + i, 4)] for i in range(len(steps))]

    probe = WideCanvas(10, 10)
    f_desc = B.F("Regular", 18)
    f_step = B.F("ExtraBold", 22)
    f_num = B.F("Black", 46)
    text_x = B.PAD + num_col_w + 24
    longest = max(probe.text_w(d, f_desc) for _, d in steps)
    longest = max(longest, max(probe.text_w(s, f_step) for s, _ in steps))
    W_needed = int(min(B.W, max(560, text_x + longest + B.PAD)))

    H = int(banner_height(title, sub) + row_h * len(steps) + 24)
    c = WideCanvas(W_needed, H)
    y0 = B.banner_B(c, title, sub)

    for i, (step, desc) in enumerate(steps):
        cy = y0 + row_h * i + row_h / 2 - 6
        col = shades[i]
        c.text((B.PAD, cy - 30), f"0{i+1}", f_num, fill=col)
        rule_x = B.PAD + num_col_w + 4
        c.rect([rule_x, cy - 26, rule_x + 3, cy + 28], fill=col, radius=1)
        c.text((text_x, cy - 30), step, f_step, fill=B.TEAL_S[0])
        c.text((text_x, cy + 4), desc, f_desc, fill=B.NEUT_S[1])
        if i < len(steps) - 1:
            ly = y0 + row_h * (i + 1)
            c.line([B.PAD, ly, W_needed - B.PAD, ly], fill=B.NEUT_S[4], width=1)
    c.save(out, quality=quality)


# ─────────────────────────────────────────────────────────────
# 2G 비교형 (두 열 대립)
# ─────────────────────────────────────────────────────────────
def compare_two(title, sub, colA, colB, rows, out, quality=90,
                footer=None, rowlabels=None):
    """
    colA / colB : (헤더, 부제, 축이름 'teal'|'gold'|'berry')
    rows        : [(왼쪽값, 오른쪽값), ...]  rowlabels: 각 행 좌측 라벨(옵션)
    """
    axismap = {"teal": B.TEAL_S, "gold": B.GOLD_S, "berry": B.BERRY_S}
    aA, aB = axismap[colA[2]], axismap[colB[2]]

    probe = WideCanvas(10, 10)
    f_head = B.F("ExtraBold", 22)
    f_hsub = B.F("Medium", 15)
    f_val = B.F("Regular", 18)
    f_lab = B.F("SemiBold", 17)

    label_w = 0
    if rowlabels:
        label_w = max(probe.text_w(l, f_lab) for l in rowlabels) + 28
    # 각 열 폭: 헤더/값 중 최장
    def col_w(header, vals):
        w = probe.text_w(header, f_head)
        for v in vals:
            w = max(w, probe.text_w(v, f_val))
        return w + 40
    cwA = col_w(colA[0], [r[0] for r in rows])
    cwB = col_w(colB[0], [r[1] for r in rows])
    col_w_final = max(cwA, cwB)
    W_needed = int(min(B.W, max(560, B.PAD + label_w + col_w_final * 2 + 16 + B.PAD)))
    col_w_final = (W_needed - B.PAD * 2 - label_w - 16) / 2

    head_h = 62
    row_hh = 52
    foot_h = 56 if footer else 0
    H = int(banner_height(title, sub) + head_h + row_hh * len(rows) + foot_h + 30)
    c = WideCanvas(W_needed, H)
    y0 = B.banner_B(c, title, sub)

    xA = B.PAD + label_w
    xB = xA + col_w_final + 16
    # 헤더(옅은 톤 배경 + 좌측 컬러 바)
    for (x, col, axis) in ((xA, colA, aA), (xB, colB, aB)):
        c.rect([x, y0, x + col_w_final, y0 + head_h], fill=axis[5], radius=10)
        c.rect([x, y0 + 8, x + 5, y0 + head_h - 8], fill=axis[1], radius=2)
        c.center_text(x + col_w_final / 2, y0 + 22, col[0], f_head, fill=axis[0])
        if col[1]:
            c.center_text(x + col_w_final / 2, y0 + 44, col[1], f_hsub, fill=B.NEUT_S[1])

    yv = y0 + head_h + 8
    for i, (va, vb) in enumerate(rows):
        ry = yv + row_hh * i
        if i % 2 == 0:
            c.rect([B.PAD, ry, W_needed - B.PAD, ry + row_hh], fill=B.NEUT_S[5], radius=6)
        if rowlabels:
            c.text((B.PAD + 4, ry + row_hh / 2 - 11), rowlabels[i], f_lab, fill=B.TEAL_S[1])
        c.center_text(xA + col_w_final / 2, ry + row_hh / 2, va, f_val, fill=B.NEUT_S[0])
        c.center_text(xB + col_w_final / 2, ry + row_hh / 2, vb, f_val, fill=B.NEUT_S[0])

    if footer:
        fy = yv + row_hh * len(rows) + 8
        c.rect([B.PAD, fy, W_needed - B.PAD, fy + foot_h - 8], fill=B.TEAL_S[5], radius=8)
        c.rect([B.PAD, fy + 6, B.PAD + 5, fy + foot_h - 14], fill=B.TEAL, radius=2)
        c.center_text(W_needed / 2, fy + (foot_h - 8) / 2, footer, B.F("Medium", 17), fill=B.TEAL_S[0])
    c.save(out, quality=quality)


# ─────────────────────────────────────────────────────────────
# 미니 표 직접 그리기 (분류)
# ─────────────────────────────────────────────────────────────
def mini_table(title, sub, headers, rows, out, quality=90,
               accent="teal", note=None):
    """headers: [열 제목...]  rows: [[셀...], ...]  첫 열은 강조 라벨."""
    axis = {"teal": B.TEAL_S, "gold": B.GOLD_S, "berry": B.BERRY_S}[accent]
    probe = WideCanvas(10, 10)
    f_h = B.F("ExtraBold", 18)
    f_c = B.F("Regular", 18)
    f_c0 = B.F("SemiBold", 19)

    ncol = len(headers)
    colw = []
    for j in range(ncol):
        w = probe.text_w(headers[j], f_h)
        for r in rows:
            f = f_c0 if j == 0 else f_c
            w = max(w, probe.text_w(str(r[j]), f))
        colw.append(w + 32)
    W_needed = int(min(B.W, max(560, B.PAD * 2 + sum(colw))))
    # 남는 폭을 마지막 열에 배분
    extra = W_needed - B.PAD * 2 - sum(colw)
    if extra > 0:
        colw[-1] += extra

    head_h = 50
    row_hh = 48
    note_h = 44 if note else 0
    H = int(banner_height(title, sub) + head_h + row_hh * len(rows) + note_h + 30)
    c = WideCanvas(W_needed, H)
    y0 = B.banner_B(c, title, sub)

    x0 = B.PAD
    # 헤더 행
    c.rect([x0, y0, W_needed - B.PAD, y0 + head_h], fill=axis[1], radius=8)
    cx = x0
    for j in range(ncol):
        c.center_text(cx + colw[j] / 2, y0 + head_h / 2, headers[j], f_h, fill="#ffffff")
        cx += colw[j]
    # 데이터 행
    yv = y0 + head_h
    for i, r in enumerate(rows):
        ry = yv + row_hh * i
        if i % 2 == 1:
            c.rect([x0, ry, W_needed - B.PAD, ry + row_hh], fill=B.NEUT_S[5])
        cx = x0
        for j in range(ncol):
            f = f_c0 if j == 0 else f_c
            col = axis[1] if j == 0 else B.NEUT_S[0]
            c.center_text(cx + colw[j] / 2, ry + row_hh / 2, str(r[j]), f, fill=col)
            cx += colw[j]
    # 테두리
    c.rect([x0, y0, W_needed - B.PAD, yv + row_hh * len(rows)],
           outline=B.NEUT_S[4], width=1, radius=8)
    if note:
        ny = yv + row_hh * len(rows) + 10
        c.text((B.PAD, ny), note, B.F("Medium", 15), fill=B.NEUT_S[2])
    c.save(out, quality=quality)


# ─────────────────────────────────────────────────────────────
# 2F 계층 (상위가 하위를 포함) — 좌측 단 스택 + 우측 설명
# ─────────────────────────────────────────────────────────────
def hierarchy(title, sub, levels, out, quality=90, accent="teal", footer=None):
    """levels: [(단계명, 설명), ...] 위→아래 = 상위→하위 포함. 단색 진→옅."""
    axis = {"teal": B.TEAL_S, "gold": B.GOLD_S, "berry": B.BERRY_S}[accent]
    n = len(levels)
    shades = [axis[min(1 + i, 5)] for i in range(n)]

    probe = WideCanvas(10, 10)
    f_lv = B.F("ExtraBold", 21)
    f_ds = B.F("Regular", 18)
    # 좌측 바 폭: 가장 넓은 단계 라벨 + 들여쓰기 여지
    bar_maxw = max(probe.text_w(lv, f_lv) for lv, _ in levels) + 44
    # 각 단계는 아래로 갈수록 살짝 좁아지는 들여쓰기(포함 느낌)
    indent = 22
    bar_w0 = bar_maxw + indent * (n - 1)
    desc_x = B.PAD + bar_w0 + 28
    longest_d = max(probe.text_w(d, f_ds) for _, d in levels)
    W_needed = int(min(B.W, max(560, desc_x + longest_d + B.PAD)))

    row_h = 74
    foot_h = 54 if footer else 0
    H = int(banner_height(title, sub) + row_h * n + foot_h + 26)
    c = WideCanvas(W_needed, H)
    y0 = B.banner_B(c, title, sub)

    for i, (lv, ds) in enumerate(levels):
        ry = y0 + row_h * i
        x_left = B.PAD + indent * i
        x_right = x_left + bar_maxw
        c.rect([x_left, ry + 8, x_right, ry + row_h - 10], fill=shades[i], radius=8)
        txt_col = "#ffffff" if i <= 3 else B.TEAL_S[0]
        c.center_text((x_left + x_right) / 2, ry + (row_h - 2) / 2, lv, f_lv, fill=txt_col)
        c.text((desc_x, ry + row_h / 2 - 12), ds, f_ds, fill=B.NEUT_S[1])
        # 포함 화살표(아래로) — 마지막 제외
        if i < n - 1:
            ax = x_left + 16
            c.line([ax, ry + row_h - 10, ax, ry + row_h + 8], fill=axis[3], width=2)

    if footer:
        fy = y0 + row_h * n + 6
        c.rect([B.PAD, fy, W_needed - B.PAD, fy + foot_h - 8], fill=axis[5], radius=8)
        c.rect([B.PAD, fy + 6, B.PAD + 5, fy + foot_h - 14], fill=axis[1], radius=2)
        c.center_text(W_needed / 2, fy + (foot_h - 8) / 2, footer, B.F("Medium", 17), fill=axis[0])
    c.save(out, quality=quality)


# ─────────────────────────────────────────────────────────────
# 2L 순환형 (자기 참조·되돌아옴) — 도넛 조각 + 바깥 방향 호살표
# ─────────────────────────────────────────────────────────────
def cycle(title, sub, steps, out, quality=90, accent="teal", center_label=None):
    """steps: [(제목, 설명), ...] 3~5개. 링 둘레에 배치, 바깥에 방향 화살표 하나."""
    import math
    axis = {"teal": B.TEAL_S, "gold": B.GOLD_S, "berry": B.BERRY_S}[accent]
    n = len(steps)

    probe = WideCanvas(10, 10)
    f_st = B.F("ExtraBold", 20)
    f_ds = B.F("Regular", 16)
    # 우측 설명 목록 폭
    longest = max(probe.text_w(f"{i+1}. {s}", f_st) for i, (s, _) in enumerate(steps))
    longest = max(longest, max(probe.text_w(d, f_ds) for _, d in steps))
    ring_area = 300           # 좌측 링 영역
    desc_x = B.PAD + ring_area + 30
    W_needed = int(min(B.W, max(600, desc_x + longest + B.PAD)))

    list_h = 66 * n
    H = int(banner_height(title, sub) + max(ring_area, list_h) + 30)
    c = WideCanvas(W_needed, H)
    y0 = B.banner_B(c, title, sub)

    # 링
    cx = B.PAD + ring_area / 2
    cy = y0 + max(ring_area, list_h) / 2
    R = 108
    ring_w = 30
    # 도넛: 옅은 링 + 조각 색
    seg = 360 / n
    for i in range(n):
        a0 = -90 + seg * i + 4
        a1 = -90 + seg * (i + 1) - 4
        col = axis[min(1 + i, 4)]
        for rr in range(R - ring_w, R):
            c.arc([cx - rr, cy - rr, cx + rr, cy + rr], a0, a1, fill=col, width=2)
        # 조각 번호
        mid = math.radians((a0 + a1) / 2)
        nx = cx + (R - ring_w / 2) * math.cos(mid)
        ny = cy + (R - ring_w / 2) * math.sin(mid)
        c.center_text(nx, ny, str(i + 1), B.F("Bold", 16), fill="#ffffff")
    # 바깥 방향 호살표 하나 (우상단)
    aa = math.radians(-52)
    hx = cx + (R + 14) * math.cos(aa)
    hy = cy + (R + 14) * math.sin(aa)
    tang = aa + math.pi / 2
    hl = 13
    p1 = (hx, hy)
    p2 = (hx - hl * math.cos(tang - 0.4), hy - hl * math.sin(tang - 0.4))
    p3 = (hx - hl * math.cos(tang + 0.4), hy - hl * math.sin(tang + 0.4))
    c.polygon([p1[0], p1[1], p2[0], p2[1], p3[0], p3[1]], fill=axis[1])
    if center_label:
        c.center_text(cx, cy, center_label, B.F("ExtraBold", 18), fill=axis[0])

    # 우측 설명 목록
    ly0 = cy - list_h / 2
    for i, (st, ds) in enumerate(steps):
        ry = ly0 + 66 * i + 12
        c.text((desc_x, ry), f"{i+1}. {st}", f_st, fill=axis[0])
        c.text((desc_x, ry + 28), ds, f_ds, fill=B.NEUT_S[1])
    c.save(out, quality=quality)
