import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';

// RSS 피드: https://rabbitlogs.com/rss.xml
// 한국어 글 전체를 최신순으로 제공한다.
// 새 글이 빌드에 포함되면 자동으로 피드에도 반영된다(별도 관리 불필요).
export async function GET(context) {
  const posts = (await getCollection('blog'))
    .filter((p) => p.id.startsWith('ko/'))
    .sort((a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf());

  return rss({
    title: 'Rabbit Logs',
    description:
      '코드는 몰라도, 프로세스는 잘 아는 사람. 생산 PI·SAP PP 구축과 안정화, 현업의 SAP 실무 기록.',
    site: context.site,
    items: posts.map((post) => ({
      title: post.data.title,
      description: post.data.description,
      pubDate: post.data.pubDate,
      link: `/blog/${post.id.replace('ko/', '').replace('.md', '')}/`,
    })),
    customData: '<language>ko-kr</language>',
  });
}
