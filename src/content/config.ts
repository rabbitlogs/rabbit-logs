import { defineCollection, z } from 'astro:content';

// 글 하나가 가져야 할 정보(제목, 설명, 날짜, 카테고리)를 정의합니다.
// 워드프레스에서 '제목 칸', '카테고리 칸' 채우던 걸 여기서 규칙으로 정해두는 셈이에요.
const blog = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    // 카테고리는 기존 블로그 3개 그대로
    category: z.enum(['project', 'operations', 'study']),
    thumbnail: z.string().optional(),
  }),
});

export const collections = { blog };
