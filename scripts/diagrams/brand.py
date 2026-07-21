# -*- coding: utf-8 -*-
"""
Rabbit Logs 도식 공통 모듈 — 레이어 1 (브랜드 고정값)

마스터 프롬프트 §8 "도식 생성 규칙 — Python + PIL (레이어 1/2 구조)" 구현.
색·폰트·배너는 여기서만 정의하고, 개별 도식 스크립트(레이어 2)는 이 모듈을 import 해서 쓴다.

중요 규칙 두 가지:
1) draw_caption()은 제공하지 않는다 — 캡션은 항상 마크다운 텍스트로 처리한다.
   (기존 국문 도식 하단의 청록 캡션 바는 §8 위반이므로 재생성 시 제거한다.)
2) 중앙 정렬은 anchor="mm"이 아니라 textbbox() 기반 true_center_text()를 쓴다.
"""
from PIL import Image, ImageDraw, ImageFont
import os

# ── 브랜드 색 (절대 변경 금지) ──────────────────────────────────────────────
BG          = "#faf8f3"   # 배경 — 순백 아닌 종이톤
TEAL        = "#2c5f57"   # 청록(메인)
TEAL_DARK   = "#234b45"   # 청록 진한 톤(그라데이션용)
TEAL_LIGHT  = "#4e857b"   # 청록 밝은 톤(그라데이션용)
MARIGOLD    = "#d99441"
MARIGOLD_D  = "#bd7c2c"
BERRY       = "#a8516e"
TEAL_PALE   = "#e8f0ef"   # 연청록
GOLD_PALE   = "#fdf3e3"   # 연금
BERRY_PALE  = "#f7eaed"   # 연베리
INK         = "#25302b"   # 본문 텍스트
MUTED       = "#7d7768"   # 보조 텍스트
WHITE       = "#ffffff"
ARROW       = "#c9b487"   # 화살표 — 원색 아닌 저채도 톤
LINE        = "#ded7c9"   # 옅은 구분선

# ── 레이아웃 고정값 ─────────────────────────────────────────────────────────
W           = 1200        # 폭 고정 (높이는 내용 기준 역산)
MARGIN      = 44          # 좌우 여백
BANNER_H    = 54          # 상단 배너 높이
BANNER_FS   = 25          # 배너 폰트
RADIUS      = 16          # 카드 반경 (14~18)

FONT_DIR = "/tmp/fonts"

def font(weight="Regular", size=20):
    """Pretendard 로드. 실패하면 조용히 대체하지 않고 예외를 던진다(§8 규칙)."""
    path = os.path.join(FONT_DIR, f"Pretendard-{weight}.otf")
    if not os.path.exists(path):
        raise RuntimeError(
            f"Pretendard 폰트를 찾을 수 없습니다: {path}\n"
            "npm pack pretendard 로 받아 /tmp/fonts 에 배치하세요. "
            "다른 폰트로 임의 대체하지 않습니다(블로그 본문과 통일감이 깨짐)."
        )
    return ImageFont.truetype(path, size)


def true_center_text(d, cx, cy, text, f, fill):
    """textbbox 기반 정중앙 정렬. anchor='mm'은 em box 기준이라 잉크 중심과 어긋난다."""
    x0, y0, x1, y1 = d.textbbox((0, 0), text, font=f)
    d.text((cx - (x1 + x0) / 2, cy - (y1 + y0) / 2), text, font=f, fill=fill)


def center_x_text(d, cx, y, text, f, fill):
    """가로만 중앙 정렬(세로 baseline은 호출부가 관리)."""
    x0, _, x1, _ = d.textbbox((0, 0), text, font=f)
    d.text((cx - (x1 + x0) / 2, y), text, font=f, fill=fill)


def text_w(d, text, f):
    x0, _, x1, _ = d.textbbox((0, 0), text, font=f)
    return x1 - x0


def new_canvas(h):
    img = Image.new("RGB", (W, h), BG)
    return img, ImageDraw.Draw(img)


def _lerp(c1, c2, t):
    a = tuple(int(c1[i:i+2], 16) for i in (1, 3, 5))
    b = tuple(int(c2[i:i+2], 16) for i in (1, 3, 5))
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def draw_banner(d, title, subtitle=None):
    """상단 배너 — 청록 가로 그라데이션. 모든 도식이 공통으로 사용한다."""
    for x in range(W):
        d.line([(x, 0), (x, BANNER_H)], fill=_lerp(TEAL_DARK, TEAL_LIGHT, x / W))

    ft = font("Bold", BANNER_FS)
    if subtitle:
        fs = font("Medium", 17)
        gap = 14
        tw = text_w(d, title, ft) + gap + text_w(d, subtitle, fs)
        x = (W - tw) / 2
        _, y0, _, y1 = d.textbbox((0, 0), title, font=ft)
        d.text((x, BANNER_H / 2 - (y1 + y0) / 2), title, font=ft, fill=WHITE)
        x += text_w(d, title, ft) + gap
        _, y0s, _, y1s = d.textbbox((0, 0), subtitle, font=fs)
        d.text((x, BANNER_H / 2 - (y1s + y0s) / 2), subtitle, font=fs, fill="#d8e5e2")
    else:
        true_center_text(d, W / 2, BANNER_H / 2, title, ft, WHITE)


def draw_headline(d, y, text, size=27):
    """배너 아래 한 줄 헤드라인. 반환값은 텍스트 하단 y."""
    f = font("Bold", size)
    center_x_text(d, W / 2, y, text, f, INK)
    _, y0, _, y1 = d.textbbox((0, 0), text, font=f)
    return y + (y1 - y0) + 8


def rounded_card(d, box, fill=WHITE, outline=None, radius=RADIUS, width=2):
    d.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def top_bar_card(d, box, bar_color, radius=RADIUS, bar_h=7, fill=WHITE):
    """상단에 컬러 바를 얹은 카드(원본 도식에서 쓰인 형태)."""
    x0, y0, x1, y1 = box
    d.rounded_rectangle(box, radius=radius, fill=fill, outline=LINE, width=2)
    # 상단 바를 카드 곡률 안쪽에 맞춰 그린다
    d.rounded_rectangle([x0, y0, x1, y0 + bar_h * 2], radius=radius, fill=bar_color)
    d.rectangle([x0, y0 + bar_h, x1, y0 + bar_h * 2], fill=bar_color)
    d.rectangle([x0, y0 + bar_h * 2 - 1, x1, y0 + bar_h * 2], fill=fill)


def arrow(d, x0, y, x1, color=ARROW, width=5, head=11):
    """수평 화살표. 호출부에서 도형 경계 + gap 을 계산해 좌표를 넘긴다(§8 화살표 규칙)."""
    d.line([(x0, y), (x1 - head, y)], fill=color, width=width)
    d.polygon([(x1, y), (x1 - head, y - head * 0.62), (x1 - head, y + head * 0.62)], fill=color)


def dotted_line(d, x0, x1, y, color=LINE, step=7, seg=3):
    for x in range(int(x0), int(x1), step):
        d.line([(x, y), (x + seg, y)], fill=color, width=2)


def save(img, path, quality=90):
    """JPG 저장 + 규격 검증 출력(§8: 생성 후 반드시 크기 검증)."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if path.lower().endswith(".png"):
        img.save(path, optimize=True)
    else:
        img.save(path, quality=quality, optimize=True, subsampling=0)
    kb = os.path.getsize(path) / 1024
    flag = "OK" if kb <= 200 else "!! 200KB 초과"
    print(f"  {os.path.basename(path):<42} 캔버스: {img.width}x{img.height}px  {kb:6.1f}KB  {flag}")
    return path
