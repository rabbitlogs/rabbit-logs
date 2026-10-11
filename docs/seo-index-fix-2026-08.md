# GSC 색인 문제 진단 및 조치 기록 (2026-08-20)

## 배경
Google Search Console에서 "크롤링됨 - 현재 색인이 생성되지 않음" 유효성 검사가
반복 실패. 조사 결과 여러 원인이 중첩돼 있었음.

## GSC 색인 미생성 항목 전체 분류 (2026-08-20 기준)

| 사유 | 건수 | 원인 | 조치 |
|---|---|---|---|
| 리디렉션이 포함된 페이지 | 126 | (a) 옛 WP URL 301 — **정상** (b) 슬래시 없는 현재 글 — 문제 | (b)만 수정 |
| 표준 없는 중복 페이지 | 9 | canonical 부재 + ko/en 중복 | canonical/hreflang 추가 |
| 크롤링됨-색인 안 됨 | 33 | hike 서브도메인 15건 + PDF/RSS/cdn-cgi 노이즈 | 속성 삭제, 나머지 방치 |
| NOINDEX 제외 | 4 | WP 시절 카테고리 잔재 | 자연 소멸 |
| 404 | 1 | `/wp-content/plugins/*` — **정상 동작** | 방치 |
| 서버 오류 5xx | 0 | — | 양호 |
| 발견됨-색인 안 됨 | 66 | 크롤링 예산 | 위 수정 후 관찰 |

## 핵심 원인 2가지

### 1. trailingSlash 미설정
`astro.config.mjs`에 `trailingSlash` 설정이 없어 Astro 기본값 `'ignore'` 적용.
내부 링크가 슬래시 없이 생성 → Cloudflare가 301 리디렉션 → 구글이 매 크롤링마다
리디렉션 URL을 재발견. "리디렉션이 포함된 페이지" 126건의 주요 부분.

### 2. canonical / hreflang 전무
`src/` 전체에 canonical도 hreflang도 한 줄도 없었음.
ko 64개 + en 64개가 짝을 이루는데 관계 표시가 없어 구글이 중복으로 판단.
`/en/`은 실제 영어 번역본이므로 각자 self-canonical + 상호 hreflang이 정답
(en의 canonical을 ko로 향하게 하면 영문판이 영구 색인 제외되므로 금지).

## 적용한 수정 (브랜치 seo-fix → main, 커밋 4c54632)

1. **astro.config.mjs** — `trailingSlash: 'always'` 추가
2. **BaseLayout.astro** — frontmatter에 경로 계산 로직 + head에 self-canonical 및
   ko/en/x-default hreflang 삽입. 전 페이지 자동 적용.
3. **내부 링크 24곳 슬래시 통일** — index/en-index, category(4), map(2×2),
   PostLayout 미니맵, JSON-LD pageUrl, BaseLayout 네비(8), about 카드(8), mapHref(2)

## 검증 결과 (로컬 빌드)
- index.html 158개 전부 canonical 보유, 누락 0
- 사이트맵 슬래시 누락 0건
- ko/en 상호 hreflang 정상, en은 self-canonical 유지
- 슬래시 없는 내부 링크 0건
- 실서버 배포 확인: `/blog/sap-cpim/` canonical 정상 출력

## 조치하지 않은 것 (의도적)

- **robots.txt 경고** — 30행 `Content-Signal`은 Cloudflare 자동 주입.
  Googlebot이 인식 못 하는 확장 문법이라 "무시되는 규칙"으로 표시될 뿐 오류 아님.
  바로 다음 줄 `Allow: /`는 정상 적용. AI 크롤러 차단에 유용하므로 유지.
- **옛 WP URL 301** — 리디렉션되는 URL이 색인 안 되는 건 정상. 목적지가 색인됨.
- **PDF / rss.xml / feed** — 원래 색인 대상 아님.
- **`/wp-content/plugins/*` 404** — 없는 경로가 404 주는 게 올바른 동작.

## 이전 조치 (2026-08-10, 사용자 직접)
`_redirects`의 포괄 규칙 `/sap-* → /` 삭제. 소프트 404를 유발하던 것으로,
이 판단이 정확했음 — 현재 404가 1건뿐이고 5xx가 0건인 이유.

## 향후 관찰
- 성공 지표는 **색인 페이지 수 추이** (유효성 검사 통과가 아님).
  PDF·RSS 등이 목록에 남아 있어 검사 완전 통과는 비현실적.
- 반영까지 2~4주 소요 예상.
- 새 글 발행 시 `_redirects` 정밀 연결 영역에 한 줄 추가하는 관례 유지.

## 미결 (우선순위 낮음)
- robots.txt에 `Disallow: /cdn-cgi/` 추가 — 크롤링 예산 영향 미미
- `/en/` 페이지의 한국어 UI 잔여물(내비게이션, 목차 안내) 영문화
  — 목차·광고 라벨은 커밋 8b95acd에서 영문화 완료. 나머지 잔여물은 미확인.
