#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sync-relations.py — Rabbit Logs "더 읽어보기" 자동화 스크립트

목적:
  1. src/content/blog/ko/*.md 의 <!-- 관련글: ... --> 주석을 유일한 소스로 삼아
     "더 읽어보기" 텍스트 링크 목록을 md 파일에 자동으로 다시 써준다.
     (대상 글의 "현재" title을 매번 다시 읽어오므로 앵커 텍스트 불일치가 안 생김)
  2. 그 결과로 src/data/book-index.yaml 을 자동 생성한다.
     (map.astro, PostLayout.astro 미니맵이 그대로 읽을 수 있는 동일 포맷 유지)

사람이 직접 손대는 곳은 각 md 파일의 <!-- 관련글: ... --> 주석 한 줄뿐이다.
book-index.yaml은 이제 사람이 관리하는 파일이 아니라 이 스크립트의 산출물이다.

사용법:
  cd ~/Documents/Obsidian/rabbit-logs
  python3 scripts/sync-relations.py            # 실제로 적용
  python3 scripts/sync-relations.py --check    # 미리보기만 (파일 안 건드림)
"""

import re
import sys
import glob
import os
import yaml
from datetime import date

REPO_ROOT = os.getcwd()
KO_DIR = os.path.join(REPO_ROOT, "src", "content", "blog", "ko")
BOOK_INDEX_PATH = os.path.join(REPO_ROOT, "src", "data", "book-index.yaml")

REL_COMMENT_RE = re.compile(
    r"<!--\s*관련글\s*:\s*(.*?)\s*-->", re.DOTALL
)
FRONTMATTER_RE = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)
FURTHER_READING_HEADER = "**더 읽어보기**"

# 카테고리 -> 필수 태그 (book-index.yaml 자동 생성 시 참고용, 이미 tags에 있으면 중복 추가 안 함)
CATEGORY_REQUIRED_TAG = {
    "project": "SAP프로젝트",
    "operations": "SAP실무운영",
    "study": "SAP학습자료",
    "stats": "통계·데이터",
}


def parse_relation_comment(text):
    """<!-- 관련글: prerequisite=a,b; related=c; deepens=d --> 파싱"""
    m = REL_COMMENT_RE.search(text)
    if not m:
        return None, {"prerequisite": [], "related": [], "deepens": []}
    body = m.group(1)
    rel = {"prerequisite": [], "related": [], "deepens": []}
    for part in body.split(";"):
        part = part.strip()
        if not part or "=" not in part:
            continue
        key, val = part.split("=", 1)
        key = key.strip()
        if key not in rel:
            continue
        slugs = [s.strip() for s in val.split(",") if s.strip()]
        rel[key] = slugs
    return m, rel


def parse_frontmatter(text):
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    fm_raw = m.group(1)
    try:
        fm = yaml.safe_load(fm_raw) or {}
    except yaml.YAMLError as e:
        print(f"  [경고] frontmatter YAML 파싱 실패: {e}")
        fm = {}
    return fm, text[m.end():]


def load_all_posts():
    """ko/*.md 전부 읽어서 slug -> {fm, rel, raw_text, path} 딕셔너리로 반환"""
    posts = {}
    for path_ in sorted(glob.glob(os.path.join(KO_DIR, "*.md"))):
        slug = os.path.splitext(os.path.basename(path_))[0]
        with open(path_, "r", encoding="utf-8") as f:
            raw = f.read()
        fm, _ = parse_frontmatter(raw)
        _, rel = parse_relation_comment(raw)
        posts[slug] = {
            "path": path_,
            "raw": raw,
            "fm": fm,
            "rel": rel,
        }
    return posts


def build_display_list(slug, posts):
    """
    한 글의 "더 읽어보기"에 표시할 슬러그 리스트를 우선순위대로 최대 3개 뽑는다.
    우선순위: prerequisite -> deepens -> related (마스터 프롬프트 7번 규칙)
    """
    rel = posts[slug]["rel"]
    ordered = []
    for key in ("prerequisite", "deepens", "related"):
        for s in rel.get(key, []):
            if s == slug:
                continue
            if s not in posts:
                print(f"  [경고] {slug}: 관련글 슬러그 '{s}' 가 실제로 존재하지 않음 (건너뜀)")
                continue
            if s not in ordered:
                ordered.append(s)
    return ordered[:3]


def render_further_reading_block(slug, posts):
    display_slugs = build_display_list(slug, posts)
    if not display_slugs:
        return None, None

    lines = [FURTHER_READING_HEADER, ""]
    for s in display_slugs:
        title = posts[s]["fm"].get("title", s)
        lines.append(f"- [{title}](/blog/{s})")

    rel = posts[slug]["rel"]

    def fmt(key):
        vals = [v for v in rel.get(key, []) if v in posts]
        return ",".join(vals)

    comment_parts = []
    for key in ("prerequisite", "related", "deepens"):
        comment_parts.append(f"{key}={fmt(key)}")
    comment = "<!-- 관련글: " + "; ".join(comment_parts) + " -->"

    return "\n".join(lines), comment


def replace_further_reading(raw, new_block_text, new_comment):
    """
    기존 '**더 읽어보기**' 섹션(있다면, 뒤따르는 관련글 주석까지)을 새 내용으로 교체.
    없으면 관련글 주석 위치(또는 파일 끝)에 새로 삽입.
    """
    # 기존 further-reading 블록 + 뒤따르는 관련글 주석을 통째로 찾아 교체
    pattern = re.compile(
        r"\*\*더 읽어보기\*\*\s*\n(?:- .*\n?)*\s*(?:<!--\s*관련글\s*:.*?-->)?",
        re.DOTALL,
    )
    replacement = new_block_text + "\n\n" + new_comment + "\n"

    if pattern.search(raw):
        new_raw = pattern.sub(replacement.rstrip("\n") + "\n", raw, count=1)
        return new_raw

    # further-reading 섹션 자체가 없는 경우: 기존 관련글 주석만 있으면 그 자리를 교체
    if REL_COMMENT_RE.search(raw):
        new_raw = REL_COMMENT_RE.sub(replacement.rstrip("\n"), raw, count=1)
        return new_raw

    # 둘 다 없으면 파일 끝에 추가
    sep = "" if raw.endswith("\n") else "\n"
    return raw + sep + "\n" + replacement


def sync_further_reading(posts, check_only):
    changed = []
    for slug, post in posts.items():
        block, comment = render_further_reading_block(slug, posts)
        if block is None:
            print(f"  [건너뜀] {slug}: 관련글 관계가 비어 있음 (주석은 있는지 확인 필요)")
            continue

        new_raw = replace_further_reading(post["raw"], block, comment)
        if new_raw != post["raw"]:
            changed.append(slug)
            if not check_only:
                with open(post["path"], "w", encoding="utf-8") as f:
                    f.write(new_raw)
    return changed


def build_book_index(posts):
    """
    각 md의 frontmatter + 관계 주석으로부터 book-index.yaml 데이터를 재구성.
    map.astro / PostLayout.astro 가 기대하는 필드 그대로 유지.
    """
    def sort_key(kv):
        pub = kv[1]["fm"].get("pubDate")
        if hasattr(pub, "isoformat"):
            return pub.isoformat()
        return str(pub) if pub else "0000-00-00"

    entries = []
    for slug, post in sorted(posts.items(), key=sort_key):
        fm = post["fm"]
        rel = post["rel"]
        pub = fm.get("pubDate")
        pub_str = pub.isoformat() if hasattr(pub, "isoformat") else str(pub)

        entries.append({
            "slug": slug,
            "mapTitle": fm.get("mapTitle") or fm.get("title", slug),
            "title": fm.get("title", slug),
            "category": fm.get("category", ""),
            "status": "rebuilt",
            "pubDate": pub_str,
            "level": fm.get("level", "beginner"),
            "tags": fm.get("tags", []) or [],
            "relations": {
                "prerequisite": [s for s in rel.get("prerequisite", []) if s in posts],
                "related": [s for s in rel.get("related", []) if s in posts],
                "deepens": [s for s in rel.get("deepens", []) if s in posts],
            },
        })
    return entries


class QuotedStr(str):
    pass


def quoted_str_representer(dumper, data):
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style='"')


yaml.add_representer(QuotedStr, quoted_str_representer)


def write_book_index(entries, check_only):
    lines = [
        "# Rabbit Logs 마스터 인덱스 (자동 생성 — 직접 수정하지 마세요)",
        "# 이 파일은 scripts/sync-relations.py 가 src/content/blog/ko/*.md 를 스캔해 매번 새로 만듭니다.",
        "# 관계를 바꾸려면 각 md 파일의 <!-- 관련글: ... --> 주석을 고친 뒤 스크립트를 다시 실행하세요.",
        f"# 생성 시각: {date.today().isoformat()}, 총 {len(entries)}개",
        "",
    ]
    for e in entries:
        tags_data = [QuotedStr(t) for t in e["tags"]]
        block = {
            "slug": e["slug"],
            "mapTitle": QuotedStr(e["mapTitle"]),
            "title": QuotedStr(e["title"]),
            "category": e["category"],
            "status": e["status"],
            "pubDate": QuotedStr(e["pubDate"]),
            "level": e["level"],
            "tags": tags_data,
            "relations": e["relations"],
        }
        entry_yaml = yaml.dump(
            [block], allow_unicode=True, sort_keys=False, default_flow_style=None
        )
        lines.append(entry_yaml.rstrip("\n"))
        lines.append("")

    content = "\n".join(lines).rstrip("\n") + "\n"

    old = None
    if os.path.exists(BOOK_INDEX_PATH):
        with open(BOOK_INDEX_PATH, "r", encoding="utf-8") as f:
            old = f.read()

    if old == content:
        return False

    if check_only:
        return True

    with open(BOOK_INDEX_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    return True


def validate(posts):
    """발행 전 자가검증: 깨진 링크, 자기참조 등"""
    problems = []
    for slug, post in posts.items():
        rel = post["rel"]
        for key in ("prerequisite", "related", "deepens"):
            for s in rel.get(key, []):
                if s == slug:
                    problems.append(f"{slug}: {key}에 자기 자신을 참조함")
                elif s not in posts:
                    problems.append(f"{slug}: {key}='{s}' 슬러그가 존재하지 않음")
    return problems


def main():
    check_only = "--check" in sys.argv

    if not os.path.isdir(KO_DIR):
        print(f"[오류] {KO_DIR} 를 찾을 수 없음. 저장소 루트에서 실행했는지 확인하세요.")
        sys.exit(1)

    print(f"글 스캔 중: {KO_DIR}")
    posts = load_all_posts()
    print(f"  총 {len(posts)}개 글 로드")

    problems = validate(posts)
    if problems:
        print("\n[검증 경고]")
        for p in problems:
            print(f"  - {p}")
        print()

    print("\n더 읽어보기 섹션 동기화 중...")
    changed = sync_further_reading(posts, check_only)
    if changed:
        verb = "변경 예정" if check_only else "변경됨"
        print(f"  {verb}: {len(changed)}개 글")
        for s in changed:
            print(f"    - {s}")
    else:
        print("  변경 없음 (이미 최신 상태)")

    if not check_only:
        # 파일을 다시 썼으니, 최신 raw로 다시 로드해서 book-index를 만든다
        posts = load_all_posts()

    print("\nbook-index.yaml 재생성 중...")
    entries = build_book_index(posts)
    index_changed = write_book_index(entries, check_only)
    if index_changed:
        verb = "갱신 예정" if check_only else "갱신됨"
        print(f"  {verb}: {BOOK_INDEX_PATH}")
    else:
        print("  변경 없음 (이미 최신 상태)")

    print("\n완료.")
    if check_only:
        print("(--check 모드라 실제 파일은 건드리지 않았습니다. 적용하려면 --check 없이 다시 실행하세요.)")


if __name__ == "__main__":
    main()
