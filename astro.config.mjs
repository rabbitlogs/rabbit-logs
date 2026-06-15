import { defineConfig } from 'astro/config';
import rehypeSlug from 'rehype-slug';
import rehypeAutolinkHeadings from 'rehype-autolink-headings';
import rehypeExternalLinks from 'rehype-external-links';
import { remarkHighlight, remarkStripToc } from './src/plugins/markdown.mjs';

export default defineConfig({
  site: 'https://rabbitlogs.com',
  i18n: {
    defaultLocale: 'ko',
    locales: ['ko', 'en'],
    routing: { prefixDefaultLocale: false },
  },
  markdown: {
    remarkPlugins: [remarkHighlight, remarkStripToc],
    rehypePlugins: [
      rehypeSlug,
      [rehypeAutolinkHeadings, { behavior: 'wrap' }],
      // 외부 링크는 새 탭 + 보안 속성 자동 적용
      [rehypeExternalLinks, { target: '_blank', rel: ['noopener', 'noreferrer'] }],
    ],
  },
});
