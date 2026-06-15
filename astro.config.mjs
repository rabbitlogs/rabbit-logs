import { defineConfig } from 'astro/config';

// 사이트 주소와 한국어/영어 다국어(i18n) 설정
export default defineConfig({
  site: 'https://rabbitlogs.com',
  i18n: {
    defaultLocale: 'ko',          // 기본은 한국어 → rabbitlogs.com/...
    locales: ['ko', 'en'],        // 영어는 rabbitlogs.com/en/...
    routing: {
      prefixDefaultLocale: false, // 한국어 글엔 /ko 안 붙임
    },
  },
});
