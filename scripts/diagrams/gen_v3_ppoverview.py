# -*- coding: utf-8 -*-
"""
sap-pp-overview-01 — brand_v3 재설계 (넘버링 로우 2K)

기존: 4색 상단 띠 카드형 + 전폭 청록 배너 + 카드당 3줄.
문제(§9): 순차 흐름을 카드로 폈고(형태 불일치), 요소마다 다른 원색(§9.4 단색 위배),
         카드당 텍스트 과다(§9.2), 전폭 배너(§9.4 배너 B 위배).
개정: 순차 진행 → 넘버링 로우(2K). 큰 숫자 01~04 + 옆 텍스트, 얇은 구분선.
     청록 단색 계열(진→옅)로 단계 진행을 표현. 카드/테두리 없음(에디토리얼).
     카드당 제목 1줄 + 설명 1줄 상한 준수. 배너 B.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import brand_v3 as B

T = {
    "ko": {
        "title": "SAP PP, 생산이 완성되는 4단계",
        "sub": "기준정보에서 생산오더 완료까지 한 줄기로 이어진다",
        "steps": [
            ("기준정보", "BOM·Routing — 레시피와 조리 순서를 등록한다"),
            ("계획",     "MRP가 소요량을 계산해 계획오더를 만든다"),
            ("실행",     "계획오더를 생산오더로 전환해 생산을 지시한다"),
            ("완료",     "작업이 끝나면 CNF로 실적을 확정한다"),
        ],
    },
    "en": {
        "title": "SAP PP: Production in 4 Steps",
        "sub": "One continuous line from master data to a finished order",
        "steps": [
            ("Master Data", "Register BOM & Routing — the recipe and process order"),
            ("Planning",    "MRP computes demand and creates planned orders"),
            ("Execution",   "Convert planned orders into production orders"),
            ("Completion",  "Confirm the actuals with CNF when work is done"),
        ],
    },
}


def build(lang, out):
    t = T[lang]
    # 4단계 청록 진→옅 (단계가 진행될수록 옅어지는 것이 아니라, 진할수록 확정에 가깝게:
    # 여기서는 시각 리듬만 담당하므로 index 1~4를 순차 배정)
    shades = [B.TEAL_S[1], B.TEAL_S[2], B.TEAL_S[3], B.TEAL_S[4]]

    # 폭 역산: 가장 긴 설명 줄 기준
    c_probe = B.Canvas(10)
    f_desc = B.F("Regular", 18)
    f_step = B.F("ExtraBold", 22)
    f_num = B.F("Black", 46)
    num_col_w = 78          # 큰 숫자 칼럼
    text_x = B.PAD + num_col_w + 24
    longest = max(c_probe.text_w(d, f_desc) for _, d in t["steps"])
    longest = max(longest, max(c_probe.text_w(s, f_step) for s, _ in t["steps"]))
    right_edge = text_x + longest + B.PAD
    W_needed = int(min(B.W, max(560, right_edge)))

    # 행 높이
    row_h = 96
    top = 0  # banner가 잡음
    # 캔버스 높이: 배너 + 행들 + 하단 여백
    # 배너 높이를 먼저 재기 위해 임시 캔버스
    tmp = B.Canvas(10)
    banner_end = _banner_height(tmp, t)
    H = int(banner_end + row_h * len(t["steps"]) + 24)

    # 실제 캔버스
    global _WSAVE
    c = _Canvas(W_needed, H)
    y0 = B.banner_B(c, t["title"], t["sub"])

    for i, (step, desc) in enumerate(t["steps"]):
        cy = y0 + row_h * i + row_h / 2 - 6
        col = shades[i]
        # 큰 숫자
        num = f"0{i+1}"
        c.text((B.PAD, cy - 30), num, f_num, fill=col)
        # 세로 얇은 컬러 룰 (숫자와 텍스트 사이)
        rule_x = B.PAD + num_col_w + 4
        c.rect([rule_x, cy - 26, rule_x + 3, cy + 28], fill=col, radius=1)
        # 스텝명
        c.text((text_x, cy - 30), step, f_step, fill=B.TEAL_S[0])
        # 설명
        c.text((text_x, cy + 4), desc, f_desc, fill=B.NEUT_S[1])
        # 행 구분선 (마지막 행 제외)
        if i < len(t["steps"]) - 1:
            ly = y0 + row_h * (i + 1)
            c.line([B.PAD, ly, W_needed - B.PAD, ly], fill=B.NEUT_S[4], width=1)

    c.save(out, quality=90)


# brand_v3.Canvas는 폭 W가 모듈 전역 고정이라, 폭 역산을 위해 인스턴스별 폭을 쓰는 래퍼.
class _Canvas(B.Canvas):
    def __init__(self, w, h, bg=B.BG):
        self._w = w
        self.h = h
        from PIL import Image, ImageDraw
        self.img = Image.new("RGB", (w * B.SCALE, h * B.SCALE), bg)
        self.d = ImageDraw.Draw(self.img)

    def save(self, path, quality=90):
        self.img.save(path, "JPEG", quality=quality, optimize=True)
        kb = os.path.getsize(path) / 1024
        print(f"저장 {os.path.basename(path)}  {self._w*B.SCALE}x{self.h*B.SCALE}px  {kb:.0f}KB")


def _banner_height(c, t):
    # banner_B 로직을 렌더 없이 높이만 계산 (brand_v3.banner_B와 동일 상수)
    y = 26
    y += 18
    y += c.text_h(t["title"], B.F("ExtraBold", 27)) + 12
    if t["sub"]:
        y += c.text_h(t["sub"], B.F("Medium", 17)) + 10
    return y + 14


BUILDERS = {"sap-pp-overview-01": build}

if __name__ == "__main__":
    OUT = "/sessions/happy-quirky-mayer/mnt/rabbit-logs/public/images/new"
    build("ko", os.path.join(OUT, "sap-pp-overview-01.jpg"))
    build("en", os.path.join(OUT, "sap-pp-overview-01_en.jpg"))
