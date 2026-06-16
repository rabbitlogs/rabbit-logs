import { defineCollection, z } from 'astro:content';

const blog = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    category: z.enum(['project', 'operations', 'study']),
    series: z.string().optional(),
    tags: z.array(z.string()).optional(),
    level: z.enum(['beginner', 'intermediate']).optional(),
    thumbnail: z.string().optional(),
  }),
});

export const collections = { blog };
