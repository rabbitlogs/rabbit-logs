// 글의 대표 이미지 경로를 결정한다.
// 우선순위: 1) 프론트매터 thumbnail 필드  2) 본문에 처음 등장하는 이미지  3) 없으면 null
//
// 사용처: PostCard.astro, index.astro의 카테고리 카드 등
// null이 반환되면 호출부에서 이미지 없는 레이아웃으로 폴백해야 한다.

const IMAGE_MD_PATTERN = /!\[[^\]]*\]\(([^)]+)\)/;

export function getThumbnail(entry: { data: { thumbnail?: string }; body: string }): string | null {
  if (entry.data.thumbnail) {
    return entry.data.thumbnail;
  }
  const match = entry.body.match(IMAGE_MD_PATTERN);
  return match ? match[1] : null;
}
