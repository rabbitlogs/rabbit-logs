import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';

// RSS 피드: https://rabbitlogs.com/en/rss.xml
// 영어 글 전체를 최신순으로 제공한다.
// 새 글이 빌드에 포함되면 자동으로 피드에도 반영된다(별도 관리 불필요).
export async function GET(context) {
  const posts = (await getCollection('blog'))
    .filter((p) => p.id.startsWith('en/'))
    .sort((a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf());

  return rss({
    title: 'Rabbit Logs',
    description:
      'Not a coder — the view of someone who runs the system. Field notes on building and operating SAP PP and PI.',
    site: context.site,
    items: posts.map((post) => ({
      title: post.data.title,
      description: post.data.description,
      pubDate: post.data.pubDate,
      link: `/en/blog/${post.id.replace('en/', '').replace('.md', '')}/`,
    })),
    customData: '<language>en-us</language>',
  });
}
