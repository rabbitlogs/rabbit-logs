# Rabbit Logs — Claude Code 작업 안내

rabbitlogs.com 블로그 저장소. Astro 4 정적 사이트, Cloudflare Pages로 배포.
운영자(Rabbit)는 코딩을 잘 모르므로 설명은 쉬운 한국어로, Git·Cloudflare 작업은 Claude가 전부 처리한다.

## 배포 절차 (반드시 지킬 것)

`main`에 push되면 Cloudflare Pages가 1~3분 안에 rabbitlogs.com에 자동 배포한다.
그 외 브랜치는 미리보기(`*.pages.dev`)만 만들어진다.

1. 작업 브랜치에서 수정한다. `main`에 직접 push하지 않는다.
2. push 전에 `npm ci`(처음 한 번) 후 `npm run build`로 빌드가 성공하는지 확인한다.
   빌드로 바뀐 `.astro/` 파일은 커밋하지 않는다(`git checkout -- .astro`).
3. 작업 브랜치에 push하고 PR을 만든다.
4. 운영자에게 변경 요약과 미리보기 링크(PR의 Cloudflare 봇 댓글)를 전달한다.
   미리보기 링크가 없으면 PR 링크와 변경 내용을 채팅으로 보여준다.
5. 수정 요청이 오면 같은 PR에 추가 push한다.
6. **운영자가 "올려" 등 게시를 명시적으로 지시했을 때만** PR을 `main`에 merge한다.
   지시 없이는 절대 merge하지 않는다.
7. 문제가 생기면 revert 커밋으로 되돌린다(같은 절차). 급하면 Cloudflare 대시보드의 Rollback을 안내한다.

## 글쓰기·운영 규칙 (작업 전에 해당 문서를 읽는다)

- `docs/rabbit-logs-master-prompt.md` — 글쓰기 규칙(Part 1)과 운영·구현 확정사항(Part 2). **글 작업 시 필수.**
- `docs/image-rules-final.md`, `docs/image-choice-guide.md` — 이미지·도식 규칙
- `docs/site-spec.md` — /map, 헤더, About, 슬러그 변경 시 리다이렉트 규칙
- `docs/rabbit-logs-brunch.md` — 브런치 크로스포스팅(모드 C)
- `docs/seo-index-fix-2026-08.md` — 구글 색인(GSC) 문제 진단·조치 기록. SEO·URL·canonical 작업 전에 읽는다.

규칙이 바뀌면 위 문서를 직접 고친다. 이 파일에는 규칙을 중복해서 적지 않는다.

## 구조

- 글: `src/content/blog/ko/<slug>.md`, `src/content/blog/en/<slug>.md` — 한글·영문은 같은 파일명으로 쌍을 이룬다.
  frontmatter 스키마는 `src/content/config.ts`.
- 이미지: `public/images/` — 영문판은 `_en` 접미사(자세한 건 마스터 프롬프트 9절).
- 도식 생성 스크립트: `scripts/diagrams/` (Python + PIL)
- 디자인: `src/layouts/`, `src/components/`, `src/pages/`
- 마크다운 커스텀 플러그인: `src/plugins/markdown.mjs`
- 리다이렉트: `public/_redirects` (슬러그 변경 시 필수)
- `.obsidian/`은 예전 로컬 Obsidian 설정. 건드리지 않는다.
