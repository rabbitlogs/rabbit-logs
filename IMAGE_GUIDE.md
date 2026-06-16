# 이미지 추가 방법 (Rabbit Logs)

## 한 번에 가까운 워크플로우

1. **제미나이로 이미지 생성** (마스터 프롬프트 사용 — 배경색은 신경 안 써도 됨)
2. 만든 이미지를 이 폴더에 넣기: `public/images/_raw/`
   - 파일 이름은 글 슬러그에 맞춰서. 예: `sap-mrp-basics-01.jpg`
3. Git Bash에서 블로그 폴더로 이동 후, 아래 한 줄 실행:
   ```
   python process-images.py
   ```
   → `_raw`의 모든 이미지가 자동으로 배경 투명 처리되어 `public/images/`에 `.png`로 저장됨
4. 글(.md)에서 이미지 경로를 `.png`로 적기:
   ```
   ![설명](/images/글슬러그-01.png)
   *그림 1. 캡션*
   ```
5. 올리기:
   ```
   git add -A
   git commit -m "add images"
   git push
   ```

## 처음 한 번만: 라이브러리 설치
```
pip install pillow numpy
```

## 메모
- 배경색을 제미나이가 정확히 못 맞추므로, 투명화는 이 스크립트가 자동 처리한다.
- 원본(_raw)은 지우지 말 것 — 나중에 다시 처리할 수 있음.
