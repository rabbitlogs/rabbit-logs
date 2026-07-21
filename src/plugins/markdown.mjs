import { visit } from 'unist-util-visit';
import GithubSlugger from 'github-slugger';
import fs from 'node:fs';
import path from 'node:path';

// ==중요== → <mark> 하이라이트로 변환
export function remarkHighlight() {
  return (tree) => {
    visit(tree, 'text', (node, index, parent) => {
      const regex = /==([^=]+)==/g;
      if (!regex.test(node.value)) return;
      const parts = [];
      let last = 0;
      node.value.replace(/==([^=]+)==/g, (match, inner, offset) => {
        if (offset > last) parts.push({ type: 'text', value: node.value.slice(last, offset) });
        parts.push({ type: 'html', value: `<mark class="hl">${inner}</mark>` });
        last = offset + match.length;
        return match;
      });
      if (last < node.value.length) parts.push({ type: 'text', value: node.value.slice(last) });
      parent.children.splice(index, 1, ...parts);
    });
  };
}

// > **3줄 요약**
// > - ...
// > - ...
// > - ...
//
// 형태의 blockquote를 감지해 "3줄 요약" 전용 카드(.tldr-box)로 변환한다.
// 일반 인용구(blockquote)를 재활용하는 대신 완전히 별도 마크업을 그려서,
// 나중에 진짜 인용구를 쓰더라도 스타일이 충돌하지 않게 한다.
// 리스트 항목은 순서 목록(1. 2. 3.)이든 불릿 목록(-)이든 둘 다 인식하되,
// 화면에는 항상 불릿(•)으로 통일해서 그린다.
// mdast 인라인 노드에서 순수 텍스트만 재귀적으로 추출한다(strong/emphasis 등 안의 텍스트 포함).
function plainText(node) {
  if (!node) return '';
  if (node.type === 'text' || node.type === 'inlineCode') return node.value;
  if (node.children) return node.children.map(plainText).join('');
  return '';
}

export function remarkTldrBox() {
  return (tree) => {
    visit(tree, 'blockquote', (node, index, parent) => {
      if (!parent || !node.children || node.children.length < 2) return;

      const firstPara = node.children[0];
      if (firstPara.type !== 'paragraph') return;
      // Rabbit Logs는 "> **3줄 요약**"처럼 strong 노드로 감싸 쓰므로, 순수 텍스트뿐 아니라
      // strong 등 인라인 노드 안의 텍스트까지 재귀적으로 모아야 헤더 문구를 인식할 수 있다.
      const headerText = firstPara.children.map(plainText).join('').trim();
      const isKo = headerText.includes('3줄 요약');
      const isEn = /3-line summary/i.test(headerText);
      if (!isKo && !isEn) return;

      const listNode = node.children.find((c) => c.type === 'list');
      if (!listNode || !listNode.children || listNode.children.length === 0) return;

      const items = listNode.children.map((li) => {
        const inlineHtml = (li.children || [])
          .filter((c) => c.type === 'paragraph')
          .flatMap((p) => p.children)
          .map((c) => inlineToHtml(c))
          .join('');
        return `<li>${inlineHtml}</li>`;
      });

      const badgeLabel = isKo ? '3줄 요약' : '3-line summary';
      const boxHtml =
        '<div class="tldr-box">' +
        '<div class="tldr-header"><span class="tldr-badge">' +
        '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18h6"></path><path d="M10 22h4"></path><path d="M12 2a7 7 0 0 0-4 12.7V17a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1v-2.3A7 7 0 0 0 12 2z"></path></svg>' +
        badgeLabel + '</span></div>' +
        `<ul class="tldr-list">${items.join('')}</ul>` +
        '</div>';

      parent.children.splice(index, 1, { type: 'html', value: boxHtml });
    });
  };
}

// mdast 인라인 노드를 최소 HTML로 직렬화한다(3줄 요약 안의 **굵게** 등 간단한 서식 지원용).
function inlineToHtml(node) {
  if (!node) return '';
  if (node.type === 'text') return node.value;
  if (node.type === 'html') return node.value;
  if (node.type === 'break') return '<br />';
  if (node.type === 'strong') {
    return `<strong>${(node.children || []).map(inlineToHtml).join('')}</strong>`;
  }
  if (node.type === 'emphasis') {
    return `<em>${(node.children || []).map(inlineToHtml).join('')}</em>`;
  }
  if (node.type === 'inlineCode') return `<code>${node.value}</code>`;
  if (node.children) return node.children.map(inlineToHtml).join('');
  return '';
}

// 헤딩에서 순수 텍스트만 추출
function headingText(node) {
  let text = '';
  visit(node, (child) => {
    if (child.type === 'text' || child.type === 'inlineCode') text += child.value;
  });
  return text;
}

// [[TOC]] 마커 자리에 목차(소제목 h2/h3 기반)를 그려넣는다.
// 소제목 링크의 id는 rehype-slug와 동일한 github-slugger로 생성해 정확히 일치시킨다.
// h2에는 본문과 동일한 번호(01, 02…)를 붙인다. 단 "Rabbit의 한 끗"은 본문에서 카드로
// 옮겨지며 번호가 빠지므로, 목차에서도 번호를 붙이지 않는다(본문과 항상 일치시킴).
export function remarkInlineToc() {
  return (tree) => {
    const slugger = new GithubSlugger();
    const items = [];
    visit(tree, 'heading', (node) => {
      if (node.depth === 2 || node.depth === 3) {
        const text = headingText(node);
        const slug = slugger.slug(text);
        items.push({ depth: node.depth, text, slug });
      }
    });

    let h2Count = 0;
    const isTakeawayHeading = (text) => {
      // 공백과 아포스트로피(일반 '와 스마트따옴표 U+2019 둘 다)를 제거하고 비교해
      // Astro의 smartypants 변환 여부와 무관하게 항상 정확히 매칭되게 한다.
      const t = text.replace(/[\s'\u2019]/g, '');
      return t.includes('Rabbit의한끗') || t.includes('RabbitsTakeaway');
    };

    visit(tree, 'paragraph', (node, index, parent) => {
      if (
        node.children.length === 1 &&
        node.children[0].type === 'text' &&
        node.children[0].value.trim() === '[[TOC]]'
      ) {
        if (items.length < 2) {
          // 소제목이 2개 미만이면 목차 없이 마커만 제거
          parent.children.splice(index, 1);
          return;
        }
        const lis = items
          .map((it) => {
            if (it.depth === 3) {
              return `<li class="sub"><a href="#${it.slug}">${it.text}</a></li>`;
            }
            if (isTakeawayHeading(it.text)) {
              return `<li><a href="#${it.slug}">${it.text}</a></li>`;
            }
            h2Count += 1;
            const num = String(h2Count).padStart(2, '0');
            return `<li><a href="#${it.slug}"><span class="toc-num">${num}</span>${it.text}</a></li>`;
          })
          .join('');
        const html = `<nav class="toc" aria-label="목차"><p class="toc-title">목차 <span class="toc-hint">— 클릭하면 해당 위치로 이동해요</span></p><ul>${lis}</ul></nav>`;
        parent.children.splice(index, 1, { type: 'html', value: html });
      }
    });
  };
}

// 영문 글(src/content/blog/en/)의 이미지 경로를 자동으로 `_en` 버전으로 바꾼다.
// 규칙(마스터 프롬프트 §8): 이미지는 한글·영문 2개 버전으로 만들고 영문만 `_en` 접미사를 붙인다.
//
// 동작: /images/foo-01.jpg  →  public/images/foo-01_en.jpg 가 실제로 있으면 그 경로로 교체,
//       없으면 원래(한글) 경로를 그대로 둔다. 즉 "en 있으면 en, 없으면 국문" 폴백이다.
// 덕분에 영문 .md는 한글과 동일한 경로를 그대로 써도 되고, 나중에 `_en` 이미지를 만들어
// public/images/에 넣기만 하면 마크다운을 손대지 않아도 자동으로 반영된다.
//
// 빌드 시점에 파일 존재 여부를 확인하므로 런타임 비용은 없다. 같은 경로를 여러 번 조회하는
// 것을 막기 위해 결과를 캐시한다(글 61개 × 이미지 여러 개 → fs 호출 폭증 방지).
const EN_IMAGE_CACHE = new Map();
const PUBLIC_DIR = path.resolve('public');

function resolveEnImage(src) {
  if (EN_IMAGE_CACHE.has(src)) return EN_IMAGE_CACHE.get(src);

  let resolved = src;
  // /images/... 형태의 내부 경로만 처리한다(외부 URL·data URI 제외).
  if (src.startsWith('/images/')) {
    const ext = path.extname(src);
    const base = src.slice(0, -ext.length);
    // 이미 _en이 붙어 있으면 그대로 둔다(중복 부착 방지).
    if (!base.endsWith('_en')) {
      const enSrc = `${base}_en${ext}`;
      if (fs.existsSync(path.join(PUBLIC_DIR, enSrc))) {
        resolved = enSrc;
      }
    }
  }

  EN_IMAGE_CACHE.set(src, resolved);
  return resolved;
}

export function remarkEnImages() {
  return (tree, file) => {
    // 이 글이 영문 글인지 파일 경로로 판별한다. 윈도우 경로(\)도 함께 처리.
    const filePath = (file?.history?.[0] || file?.path || '').replace(/\\/g, '/');
    if (!filePath.includes('/content/blog/en/')) return;

    visit(tree, 'image', (node) => {
      node.url = resolveEnImage(node.url);
    });
  };
}
