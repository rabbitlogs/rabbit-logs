# -*- coding: utf-8 -*-
"""
clean-core-dependency — 피라미드(삼각형 실루엣) 은유.

이 글의 핵심: "정상(Joule)에 닿으려면 맨 아래 기반(Z-코드 정리)부터 다져야
한다." sap-org-structure-master-data-01(gen_v2_orgstructure.py)에서 쓴 것과
동일한 삼각형 실루엣(사다리꼴 스택, 좌우 변이 안쪽으로 기울어짐) 방식을 쓰되,
방향이 반대다: 조직구조는 위(포함하는 쪽)가 넓었지만, 여기는 아래(기반이
되는 Z-코드 정리)가 가장 넓고 위(최종 목표 Joule)로 갈수록 좁아지는 정석
피라미드다 — "기반이 넓어야 정상이 안정적으로 선다"는 은유와도 맞아떨어진다.
제목(①②③ + 이름)은 도형 안에, 태그·설명은 도형 오른쪽 바깥에 배치한다.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brand import *
from PIL import Image, ImageDraw

CLEAN_CORE = {
    "ko": dict(
        banner="Joule로 가는 길, 순서가 거꾸로다",
        sub="쓰고 싶은 것은 정상이지만, 발은 맨 아래 계단부터",
        foot="화려한 기능보다, 내 시스템에 쌓인 Z-코드 점검이 먼저다",
        # 아래 계단 → 위 계단 순서 (밟는 순서 = ①②③)
        steps=[
            ("①", "Z-코드 정리", "선결 과제",
             ["표준을 직접 고쳐 쌓인", "커스텀 코드부터 진단·정리"], "teal"),
            ("②", "클린코어", "전제 조건",
             ["핵심은 표준 그대로,", "확장은 BTP에 앱처럼 붙인다"], "gold"),
            ("③", "SAP Joule", "최종 목표",
             ["자연어로 지시하는", "SAP 전용 AI 비서"], "berry"),
        ],
        top_flag="정상",
    ),
    "en": dict(
        banner="The road to Joule runs backwards",
        sub="the summit is the goal, but your feet start on the bottom step",
        foot="Before the shiny features, audit the Z-code piled onto your system",
        steps=[
            ("①", "Z-code cleanup", "First task",
             ["Audit and clear the custom", "code piled onto the standard"], "teal"),
            ("②", "Clean Core", "Prerequisite",
             ["Keep the core standard;", "add extensions on BTP"], "gold"),
            ("③", "SAP Joule", "The goal",
             ["An SAP-native assistant", "you instruct in plain language"], "berry"),
        ],
        top_flag="Summit",
    ),
}

CMAP = {"teal": (TEAL, TEAL_DARK, TEAL_PALE),
        "gold": (MARIGOLD, MARIGOLD_D, GOLD_PALE),
        "berry": (BERRY, "#8f3f5c", BERRY_PALE)}


def _wrap(d, text, f, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        tt = (cur + " " + w).strip()
        if text_w(d, tt, f) > max_w and cur:
            lines.append(cur); cur = w
        else:
            cur = tt
    if cur:
        lines.append(cur)
    return lines


def _clean_core(lang, out):
    t = CLEAN_CORE[lang]
    f_title = font("Bold", 21)
    f_tag = font("Bold", 15)
    f_desc = font("Regular", 14)
    f_flag = font("Bold", 15)
    f_foot = font("Bold", 16)

    n = len(t["steps"])                 # 3, steps[0]=맨 아래(기반) ... steps[-1]=맨 위(정상)
    top = BANNER_H + 46
    row_h, row_gap = 78, 12
    pyr_h = n * (row_h + row_gap) - row_gap
    flag_h = 40                          # 정상 깃발 공간
    start_h = 26                         # "여기서 시작" 라벨 공간
    foot_h = 44
    foot_gap = 18

    img_h = int(top + flag_h + pyr_h + start_h + foot_gap + foot_h + 30)
    img, d = new_canvas(img_h)
    draw_banner(d, t["banner"], t["sub"])

    pyr_top = top + flag_h

    # 도형 폭 — 글자를 덮을 만큼만. 캔버스를 꽉 채우지 않고, 맨 아래(기반) 단
    # 라벨(가장 긴 텍스트) 폭 + 여유 패딩만큼만 base_w로 잡는다. 맨 위(정상)는
    # base_w의 일정 비율로 좁혀 삼각형 기울기가 뚜렷이 보이게 하되, 그 단
    # 라벨이 들어갈 최소 폭은 보장한다.
    tmp_img = Image.new("RGB", (10, 10))
    tmp_d = ImageDraw.Draw(tmp_img)
    pad_in = 56                           # 라벨 좌우 여유
    label_ws = [text_w(tmp_d, f"{num} {title}", f_title) + pad_in
                for num, title, *_ in t["steps"]]
    top_ratio = 0.45                      # 맨 위 폭 / 맨 아래 폭 — 삼각형 기울기
    # base_w는 두 조건을 모두 만족해야 한다: ①맨 아래 라벨이 들어갈 폭,
    # ②맨 위 라벨이 top_ratio로 좁아진 폭 안에 들어갈 폭(역산). 큰 쪽을 쓴다.
    base_w = max(label_ws[0], label_ws[-1] / top_ratio)
    top_w = base_w * top_ratio
    # 중간 단이 그 위치의 보간 폭보다 라벨이 길면 그만큼 base_w를 늘린다.
    for k in range(1, n - 1):
        frac = k / n
        interp = base_w - (base_w - top_w) * frac
        if label_ws[k] > interp:
            base_w += (label_ws[k] - interp)
            top_w = base_w * top_ratio

    text_gap = 32
    # 피라미드 도형 자체를 캔버스 좌우 정중앙에 둔다(태그 칼럼은 그 오른쪽에
    # 이어 붙인다 — 칼럼까지 포함해 중앙 정렬하면 도형이 왼쪽으로 치우쳐 보인다).
    cx = W / 2

    for i in range(n):                   # i=0: 맨 아래(기반) ... i=n-1: 맨 위(정상)
        num, title, tag, desc, ckey = t["steps"][i]
        col, dark, pale = CMAP[ckey]

        # 아래에서 위로 갈수록(row index가 클수록) 좁아지도록 폭 보간.
        # row 0(가장 아래)의 아래쪽 변 = base_w, row(n-1)의 위쪽 변 = top_w.
        frac_bot = i / n                 # 이 단의 아래쪽 변 위치(0=기반 바닥)
        frac_top = (i + 1) / n           # 이 단의 위쪽 변 위치
        w_bot = base_w - (base_w - top_w) * frac_bot
        w_top = base_w - (base_w - top_w) * frac_top

        y1 = pyr_top + pyr_h - i * (row_h + row_gap)        # 이 단의 아래쪽 y
        y0 = y1 - row_h                                      # 이 단의 위쪽 y

        d.polygon([
            (cx - w_top / 2, y0), (cx + w_top / 2, y0),
            (cx + w_bot / 2, y1), (cx - w_bot / 2, y1),
        ], fill=col)

        # 제목 — 도형 안, 가운데 정렬(번호 + 이름을 한 줄로)
        label = f"{num} {title}"
        ty = (y0 + y1) / 2
        true_center_text(d, cx, ty, label, f_title, WHITE)

        # 태그/설명 — 도형 오른쪽 바깥 여백에 배치(모든 단 동일한 x, 맨 아래
        # 기준 폭으로 고정해야 caption 칼럼이 세로로 정렬된다).
        key_x = cx + base_w / 2 + text_gap
        d.text((key_x, ty - 26), tag, font=f_tag, fill=col)
        dy = ty - 2
        for ln in desc:
            d.text((key_x, dy), ln, font=f_desc, fill=MUTED)
            dy += 19

        if i > 0:
            d.line([(cx, y1 + 2), (cx, y1 + row_gap - 2)], fill=LINE, width=2)

    # 정상 깃발 — 맨 위 단 위쪽. 텍스트는 폴대 왼쪽에 붙여 깃발 천과 겹치지 않게 한다.
    top_y = pyr_top
    fx = cx
    d.line([(fx, top_y - 6), (fx, top_y - 34)], fill=INK, width=3)
    d.polygon([(fx, top_y - 34), (fx + 34, top_y - 28), (fx, top_y - 22)], fill=BERRY)
    flag_w = text_w(d, t["top_flag"], f_flag)
    d.text((fx - flag_w - 10, top_y - 30), t["top_flag"], font=f_flag, fill=BERRY)

    # 맨 아래 밑에 "여기서 시작"
    start_lbl = "여기서 시작 ▲" if lang == "ko" else "start here ▲"
    sy = pyr_top + pyr_h + 6
    slw = text_w(d, start_lbl, f_tag)
    d.text((cx - slw / 2, sy), start_lbl, font=f_tag, fill=TEAL)

    # 하단 마무리
    fy = pyr_top + pyr_h + start_h + foot_gap
    center_x_text(d, W / 2, fy, t["foot"], f_foot, TEAL)

    save(img, out)


BUILDERS = {
    "clean-core-dependency": _clean_core,
}
