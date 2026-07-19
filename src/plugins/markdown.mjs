import { visit } from 'unist-util-visit';
import GithubSlugger from 'github-slugger';

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
