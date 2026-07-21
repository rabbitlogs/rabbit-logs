# -*- coding: utf-8 -*-
"""
도식 일괄 생성 러너.

사용법:
    python3 scripts/diagrams/_runner.py            # 전체 생성
    python3 scripts/diagrams/_runner.py mrp adsp   # 이름에 해당 문자열이 포함된 것만

출력 규칙(검수용 _new):
    public/images/<슬러그>_new.jpg       ← 신규 국문
    public/images/<슬러그>_en_new.jpg    ← 신규 영문

기존 파일은 절대 덮어쓰지 않는다. 검수 후 _new 를 떼어 정식 파일명으로 교체하면
remarkEnImages 폴백이 자동으로 영문판을 잡는다.
"""
import importlib
import os
import sys
import traceback

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(REPO, "public", "images")

sys.path.insert(0, HERE)


def _ref_ext():
    """영문 글 마크다운이 참조하는 이미지 확장자를 슬러그별로 수집한다."""
    import glob, re
    ext = {}
    for f in glob.glob(os.path.join(REPO, "src", "content", "blog", "en", "*.md")):
        with open(f, encoding="utf-8") as fh:
            for ref in re.findall(r"\(/images/([^)]+)\)", fh.read()):
                stem, e = os.path.splitext(ref)
                ext[stem] = e
    return ext


REF_EXT = _ref_ext()

# (모듈명, 슬러그) — 슬러그는 마크다운이 참조하는 실제 파일명(확장자 제외)
DIAGRAMS = [
    ("gen_activity_cnf", "sap-activity-cnf-01"),
    ("gen_mrp_flow",     "sap-mrp-flow"),
    ("gen_adsp",         "stats-adsp-01"),
    ("gen_stats_descriptive", "stats-descriptive-basics-01"),
    ("gen_stats_correlation", "stats-correlation-vs-causation-01"),
]


# 여러 도식을 BUILDERS 딕셔너리로 묶어 제공하는 모듈들(템플릿 기반)
BATCH_MODULES = ["gen_batch1", "gen_batch2", "gen_batch3", "gen_batch4", "gen_charts"]


def _targets():
    """(슬러그, build함수) 목록을 만든다."""
    out = []
    for mod_name, slug in DIAGRAMS:
        mod = importlib.import_module(mod_name)
        importlib.reload(mod)
        out.append((slug, mod.build))
    for mod_name in BATCH_MODULES:
        try:
            mod = importlib.import_module(mod_name)
        except ModuleNotFoundError:
            continue
        importlib.reload(mod)
        for slug, fn in mod.BUILDERS.items():
            out.append((slug, fn))
    return out


def run(filters=None):
    ok, fail = [], []
    for slug, fn in _targets():
        if filters and not any(f in slug for f in filters):
            continue
        try:
            print(f"[{slug}]")
            # 마크다운이 실제로 참조하는 확장자를 따른다.
            ext = REF_EXT.get(slug, ".jpg")
            fn("ko", os.path.join(OUT, f"{slug}_new{ext}"))
            fn("en", os.path.join(OUT, f"{slug}_en_new{ext}"))
            ok.append(slug)
        except Exception:
            fail.append(slug)
            print(f"  !! {slug} 실패")
            traceback.print_exc()

    print(f"\n완료 {len(ok)}개" + (f" / 실패 {len(fail)}개: {', '.join(fail)}" if fail else ""))
    return fail


if __name__ == "__main__":
    sys.exit(1 if run(sys.argv[1:] or None) else 0)
