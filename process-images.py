#!/usr/bin/env python3
"""
Rabbit Logs 이미지 배경 투명화 스크립트

사용법:
  python process-images.py

동작:
  - public/images/_raw/ 폴더의 이미지(제미나이 원본)를 자동으로 배경 투명화
  - 결과를 public/images/ 에 같은 이름의 .png로 저장
  - 원본은 _raw 폴더에 그대로 남아 있음(필요시 다시 처리 가능)

준비물: pip install pillow numpy
"""
import os
import sys
from pathlib import Path

try:
    from PIL import Image
    import numpy as np
except ImportError:
    print("[준비 필요] 아래 명령을 먼저 한 번 실행하세요:")
    print("    pip install pillow numpy")
    sys.exit(1)

BASE = Path(__file__).parent
RAW = BASE / "public" / "images" / "_raw"
OUT = BASE / "public" / "images"

def make_transparent(img):
    """밝은 크림색 배경을 투명하게. 일러스트 내부 흰색은 보존."""
    img = img.convert("RGB")
    arr = np.array(img).astype(int)
    r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]
    brightness = (r + g + b) / 3

    # 배경 = 아주 밝고(>233) 크림 계열(채널 차이 작음)
    is_bg = (brightness > 233) & (abs(r - g) < 20) & (abs(g - b) < 28) & (r > 235)
    # 가장자리 부드럽게(반투명)
    soft = (brightness > 225) & (brightness <= 233) & (abs(r - g) < 22) & (abs(g - b) < 30)

    h, w = is_bg.shape
    rgba = np.zeros((h, w, 4), dtype=np.uint8)
    rgba[:, :, :3] = np.array(img)
    alpha = np.where(is_bg, 0, 255).astype(np.uint8)
    alpha[soft] = 120
    rgba[:, :, 3] = alpha
    return Image.fromarray(rgba, "RGBA")

def main():
    RAW.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)

    raws = [p for p in RAW.iterdir()
            if p.suffix.lower() in (".jpg", ".jpeg", ".png", ".webp")]
    if not raws:
        print(f"[안내] 처리할 이미지가 없습니다.")
        print(f"       제미나이 이미지를 이 폴더에 넣으세요:")
        print(f"       {RAW}")
        return

    for p in raws:
        out_name = p.stem + ".png"  # 결과는 항상 png(투명)
        out_path = OUT / out_name
        try:
            img = Image.open(p)
            result = make_transparent(img)
            result.save(out_path)
            print(f"[완료] {p.name}  ->  images/{out_name}")
        except Exception as e:
            print(f"[실패] {p.name}: {e}")

    print("\n끝! 이제 git add -A → commit → push 하면 블로그에 반영됩니다.")

if __name__ == "__main__":
    main()
