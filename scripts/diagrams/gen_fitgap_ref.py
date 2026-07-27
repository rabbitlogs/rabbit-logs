# -*- coding: utf-8 -*-
"""Fit/Gap 레퍼런스 레이아웃 재현 — 전폭 그라데이션 배너 + Fit/Gap 대비 카드 + 3-way 카드
규격: 논리폭 800(2배 렌더 1600), 브랜드 3색, 표준 최소폰트 이상."""
import sys
sys.path.insert(0,"/sessions/magical-elegant-hopper/mnt/rabbit-logs/scripts/diagrams")
import brand_v3 as B, v3_forms as F, sap_icons as SI

OUT="/sessions/magical-elegant-hopper/mnt/rabbit-logs/public/images/new"
T=B.TEAL_S; N=B.NEUT_S; G=B.GOLD_S; BE=B.BERRY_S

def lerp(c1,c2,t):
    a=tuple(int(c1[i:i+2],16) for i in (1,3,5)); b=tuple(int(c2[i:i+2],16) for i in (1,3,5))
    return tuple(int(a[i]+(b[i]-a[i])*t) for i in range(3))

def check_disc(c,cx,cy,r,fill):
    c.ellipse([cx-r,cy-r,cx+r,cy+r],fill=fill)
    c.line([cx-r*0.42,cy+r*0.02, cx-r*0.1,cy+r*0.34],fill="#ffffff",width=3)
    c.line([cx-r*0.1,cy+r*0.34, cx+r*0.46,cy-r*0.30],fill="#ffffff",width=3)

def excl_disc(c,cx,cy,r,fill):
    c.ellipse([cx-r,cy-r,cx+r,cy+r],fill=fill)
    c.line([cx,cy-r*0.42,cx,cy+r*0.12],fill="#ffffff",width=3)
    c.ellipse([cx-2.2,cy+r*0.30,cx+2.2,cy+r*0.30+4.4],fill="#ffffff")

def build():
    W=B.W  # 800
    PAD=B.PAD
    banner_h=64
    # 높이 산정: 배너 + 대비카드행 + "세 가지 길" 제목 + 3way카드
    cmp_h=112
    ways_gap=54
    way_h=190
    H=int(banner_h+34+cmp_h+ways_gap+way_h+30)
    c=F.WideCanvas(W,H)

    # ── 전폭 그라데이션 배너 ──
    for x in range(W):
        c.d.line([(x*B.SCALE,0),(x*B.SCALE,banner_h*B.SCALE)],
                 fill=lerp(T[0],T[3],x/W), width=B.SCALE)
    fbt=B.F("ExtraBold",26); fbs=B.F("Medium",18)
    t1="SAP Fit/Gap"; t2="표준과 우리 매장 사이의 간격 재기"
    gap=16
    tw=c.text_w(t1,fbt)+gap+c.text_w(t2,fbs)
    bx=(W-tw)/2
    c.text((bx,banner_h/2-16),t1,fbt,fill="#ffffff")
    c.text((bx+c.text_w(t1,fbt)+gap,banner_h/2-12),t2,fbs,fill="#dbe7e4")

    # ── Fit / Gap 대비 카드 2개 ──
    y=banner_h+30
    cw=(W-PAD*2-24)/2
    fF=B.F("ExtraBold",34); fD=B.F("Regular",17)
    # Fit (청록)
    xF=PAD
    c.rect([xF,y,xF+cw,y+cmp_h],fill="#ffffff",outline=T[2],width=2,radius=14)
    c.text((xF+26,y+22),"Fit",fF,fill=T[1])
    c.text((xF+28,y+66),"표준을 그대로 써도 되는 부분",fD,fill=N[1])
    check_disc(c,xF+cw-46,y+cmp_h/2,26,T[1])
    # Gap (골드)
    xG=PAD+cw+24
    c.rect([xG,y,xG+cw,y+cmp_h],fill="#ffffff",outline=G[1],width=2,radius=14)
    c.text((xG+26,y+22),"Gap",fF,fill=G[0])
    c.text((xG+28,y+66),"손봐야 하거나 없는 부분",fD,fill=N[1])
    excl_disc(c,xG+cw-46,y+cmp_h/2,26,G[0])

    # ── 세 가지 길 제목 ──
    yt=y+cmp_h+ways_gap
    ftt=B.F("ExtraBold",24)
    c.center_text(W/2,yt-18,"Gap을 푸는 세 가지 길",ftt,fill=T[0])

    # ── 3-way 컬러 헤더 카드 ──
    yw=yt+16
    ways=[("개발","시스템을 우리에게 맞춤 · Z코드 개발","비용·시간 ↑",G),
          ("프로세스 변경","우리를 표준에 맞춤 · 일하는 방식 조정","가장 이상적",T),
          ("수용","표준에 없지만 감수 · 그대로 사용","현명한 타협",BE)]
    wgap=20; wcw=(W-PAD*2-wgap*2)/3
    head_h=52
    fWh=B.F("ExtraBold",21); fWd=B.F("Regular",16); fWt=B.F("SemiBold",16)
    for i,(lab,desc,tag,S) in enumerate(ways):
        x=PAD+(wcw+wgap)*i
        dark=S[0] if S is G else S[1]
        # 카드 바탕
        c.rect([x,yw,x+wcw,yw+way_h],fill="#ffffff",outline=N[4],width=1,radius=14)
        # 헤더
        c.rect([x,yw,x+wcw,yw+head_h],fill=dark,radius=14)
        c.rect([x,yw+head_h-14,x+wcw,yw+head_h],fill=dark)
        c.center_text(x+wcw/2,yw+head_h/2,lab,fWh,fill="#ffffff")
        # 설명 (줄바꿈)
        dy=yw+head_h+22
        for ln in F.wrap(c,desc,fWd,wcw-36):
            c.center_text(x+wcw/2,dy,ln,fWd,fill=N[1]); dy+=24
        # 태그 pill
        pill_y=yw+way_h-46
        c.rect([x+18,pill_y,x+wcw-18,pill_y+34],fill=S[5],radius=17)
        c.center_text(x+wcw/2,pill_y+17,tag,fWt,fill=dark)
    c.save(f"{OUT}/rl-fit-gap-ways.jpg")

build()
print("done")
