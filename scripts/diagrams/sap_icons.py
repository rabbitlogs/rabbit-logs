# -*- coding: utf-8 -*-
"""SAP 실무 어휘 선 아이콘 세트 v1. 모든 아이콘 24x24 논리단위, cx/cy 중심, s 배율.
   공통: 둥근 선(joint=curve 흉내), 굵기 w 통일."""
import sys, math
sys.path.insert(0,"/sessions/magical-elegant-hopper/mnt/rabbit-logs/scripts/diagrams")
import brand_v3 as B

def _L(c, pts, col, w):
    # 폴리라인 (둥근 느낌 위해 각 점에 작은 원)
    c.d.line([v*B.SCALE for v in pts], fill=col, width=max(1,int(w*B.SCALE)), joint="curve")

def i_gear(c,cx,cy,s=1,col=None,w=2):  # 표준/설정 (컨피그)
    r=6*s
    c.ellipse([cx-r,cy-r,cx+r,cy+r],outline=col,width=w)
    c.ellipse([cx-2*s,cy-2*s,cx+2*s,cy+2*s],outline=col,width=w)
    for k in range(8):
        a=math.radians(k*45); x0=cx+math.cos(a)*r; y0=cy+math.sin(a)*r
        x1=cx+math.cos(a)*(r+2.6*s); y1=cy+math.sin(a)*(r+2.6*s)
        c.line([x0,y0,x1,y1],fill=col,width=w)

def i_code(c,cx,cy,s=1,col=None,w=2):  # 개발/CBO (</>)
    c.line([cx-2*s,cy-7*s,cx-8*s,cy,cx-2*s,cy+7*s],col,w) if False else None
    _L(c,[cx-2.5*s,cy-7*s,cx-8*s,cy,cx-2.5*s,cy+7*s],col,w)
    _L(c,[cx+2.5*s,cy-7*s,cx+8*s,cy,cx+2.5*s,cy+7*s],col,w)

def i_doc(c,cx,cy,s=1,col=None,w=2):  # 문서/명세
    c.rect([cx-6*s,cy-8*s,cx+6*s,cy+8*s],outline=col,width=w,radius=1.5*s)
    for dy in(-4,-1,2,5):
        c.line([cx-3*s,cy+dy*s,cx+3*s,cy+dy*s],fill=col,width=w)

def i_db(c,cx,cy,s=1,col=None,w=2):  # 데이터/DB (원통)
    c.ellipse([cx-6*s,cy-8*s,cx+6*s,cy-4*s],outline=col,width=w)
    c.line([cx-6*s,cy-6*s,cx-6*s,cy+6*s],fill=col,width=w)
    c.line([cx+6*s,cy-6*s,cx+6*s,cy+6*s],fill=col,width=w)
    c.arc([cx-6*s,cy+4*s,cx+6*s,cy+8*s],0,180,fill=col,width=w)
    c.arc([cx-6*s,cy-2*s,cx+6*s,cy+2*s],0,180,fill=col,width=w)

def i_flow(c,cx,cy,s=1,col=None,w=2):  # 프로세스/흐름 (박스→박스 화살표)
    c.rect([cx-8.5*s,cy-4*s,cx-2*s,cy+4*s],outline=col,width=w,radius=1.5*s)
    c.rect([cx+2*s,cy-4*s,cx+8.5*s,cy+4*s],outline=col,width=w,radius=1.5*s)
    # 연결 화살표 (두 박스 사이 짧은 구간)
    c.line([cx-2*s,cy,cx+0.3*s,cy],fill=col,width=w)
    c.polygon([cx+2*s,cy, cx-0.4*s,cy-2.4*s, cx-0.4*s,cy+2.4*s],fill=col)

def i_check(c,cx,cy,s=1,col=None,w=2):  # 검토/승인
    c.ellipse([cx-8*s,cy-8*s,cx+8*s,cy+8*s],outline=col,width=w)
    _L(c,[cx-4*s,cy+0.5*s,cx-1*s,cy+4*s,cx+4.5*s,cy-3.5*s],col,w)

def i_warn(c,cx,cy,s=1,col=None,w=2):  # 리스크/주의
    _L(c,[cx,cy-8*s,cx-8*s,cy+7*s,cx+8*s,cy+7*s,cx,cy-8*s],col,w)
    c.line([cx,cy-3*s,cx,cy+2*s],fill=col,width=w)
    c.ellipse([cx-0.9*s,cy+4*s,cx+0.9*s,cy+5.8*s],fill=col)

def i_cost(c,cx,cy,s=1,col=None,w=2):  # 비용 (동전 + W)
    c.ellipse([cx-8*s,cy-8*s,cx+8*s,cy+8*s],outline=col,width=w)
    # W 자 (원화 느낌)
    _L(c,[cx-4.5*s,cy-3.5*s,cx-2.5*s,cy+4*s,cx,cy-1.5*s,cx+2.5*s,cy+4*s,cx+4.5*s,cy-3.5*s],col,w)
    c.line([cx-6*s,cy-0.5*s,cx+6*s,cy-0.5*s],fill=col,width=max(1,w-1))
    c.line([cx-6*s,cy+1.5*s,cx+6*s,cy+1.5*s],fill=col,width=max(1,w-1))

def i_time(c,cx,cy,s=1,col=None,w=2):  # 시간/리드타임
    c.ellipse([cx-8*s,cy-8*s,cx+8*s,cy+8*s],outline=col,width=w)
    c.line([cx,cy-4.5*s,cx,cy],fill=col,width=w)
    c.line([cx,cy,cx+4*s,cy+2.5*s],fill=col,width=w)

def i_link(c,cx,cy,s=1,col=None,w=2):  # 통합/인터페이스 (체인)
    c.arc([cx-8*s,cy-4*s,cx-0*s,cy+4*s],40,320,fill=col,width=w)
    c.arc([cx+0*s,cy-4*s,cx+8*s,cy+4*s],220,140,fill=col,width=w)
    c.line([cx-2.5*s,cy,cx+2.5*s,cy],fill=col,width=w)

def i_layers(c,cx,cy,s=1,col=None,w=2):  # 계층/스택
    for k,dy in enumerate((-5,0,5)):
        c.polygon([cx-7*s,cy+dy*s, cx,cy+dy*s-3.5*s, cx+7*s,cy+dy*s, cx,cy+dy*s+3.5*s],outline=col)

def i_org(c,cx,cy,s=1,col=None,w=2):  # 조직구조 (트리)
    c.rect([cx-3*s,cy-8*s,cx+3*s,cy-4*s],outline=col,width=w,radius=1*s)
    for dx in(-6,6):
        c.rect([cx+dx*s-3*s,cy+4*s,cx+dx*s+3*s,cy+8*s],outline=col,width=w,radius=1*s)
    c.line([cx,cy-4*s,cx,cy],fill=col,width=w)
    _L(c,[cx-6*s,cy+4*s,cx-6*s,cy,cx+6*s,cy,cx+6*s,cy+4*s],col,w)

def i_box(c,cx,cy,s=1,col=None,w=2):  # 자재/재고 (3D 박스)
    c.polygon([cx-7*s,cy-3*s,cx,cy-7*s,cx+7*s,cy-3*s,cx,cy+1*s],outline=col)
    _L(c,[cx-7*s,cy-3*s,cx-7*s,cy+5*s,cx,cy+9*s,cx+7*s,cy+5*s,cx+7*s,cy-3*s],col,w)
    c.line([cx,cy+1*s,cx,cy+9*s],fill=col,width=w)

def i_search(c,cx,cy,s=1,col=None,w=2):  # 분석/조회
    c.ellipse([cx-8*s,cy-8*s,cx+3*s,cy+3*s],outline=col,width=w)
    c.line([cx+1.5*s,cy+1.5*s,cx+7*s,cy+7*s],fill=col,width=w+1)

def i_user(c,cx,cy,s=1,col=None,w=2):  # 사용자/역할
    c.ellipse([cx-3.5*s,cy-8*s,cx+3.5*s,cy-1*s],outline=col,width=w)
    c.arc([cx-7*s,cy+0*s,cx+7*s,cy+14*s],180,360,fill=col,width=w)

def i_lock(c,cx,cy,s=1,col=None,w=2):  # 권한/보안
    c.rect([cx-6*s,cy-2*s,cx+6*s,cy+8*s],outline=col,width=w,radius=1.5*s)
    c.arc([cx-4*s,cy-8*s,cx+4*s,cy+2*s],180,360,fill=col,width=w)
    c.ellipse([cx-1*s,cy+2*s,cx+1*s,cy+4*s],fill=col)

def i_chart(c,cx,cy,s=1,col=None,w=2):  # 차트/KPI
    c.line([cx-8*s,cy+7*s,cx+8*s,cy+7*s],fill=col,width=w)
    c.line([cx-8*s,cy+7*s,cx-8*s,cy-7*s],fill=col,width=w)
    for dx,h in((-4,3),(0,7),(4,5)):
        c.rect([cx+dx*s-1.6*s,cy+7*s-h*1.6*s,cx+dx*s+1.6*s,cy+7*s],outline=col,width=w)

def i_target(c,cx,cy,s=1,col=None,w=2):  # 목표/전략
    for rr in(8,5,2):
        c.ellipse([cx-rr*s,cy-rr*s,cx+rr*s,cy+rr*s],outline=col,width=w)

def i_refresh(c,cx,cy,s=1,col=None,w=2):  # 순환/재작업
    c.arc([cx-7*s,cy-7*s,cx+7*s,cy+7*s],30,300,fill=col,width=w)
    a=math.radians(30); hx=cx+7*s*math.cos(a); hy=cy+7*s*math.sin(a)
    c.polygon([hx,hy, hx-4*s,hy-1*s, hx-1*s,hy+4*s],fill=col)

def i_bulb(c,cx,cy,s=1,col=None,w=2):  # 개선/아이디어
    c.ellipse([cx-6*s,cy-8*s,cx+6*s,cy+4*s],outline=col,width=w)
    c.line([cx-3*s,cy+5*s,cx+3*s,cy+5*s],fill=col,width=w)
    c.line([cx-2.5*s,cy+7.5*s,cx+2.5*s,cy+7.5*s],fill=col,width=w)

ICONS = [
 ("표준·설정",i_gear),("개발·CBO",i_code),("문서·명세",i_doc),("데이터·DB",i_db),
 ("프로세스",i_flow),("검토·승인",i_check),("리스크",i_warn),("비용",i_cost),
 ("시간·리드타임",i_time),("통합·IF",i_link),("계층·스택",i_layers),("조직구조",i_org),
 ("자재·재고",i_box),("분석·조회",i_search),("사용자·역할",i_user),("권한·보안",i_lock),
 ("차트·KPI",i_chart),("목표·전략",i_target),("순환·재작업",i_refresh),("개선·아이디어",i_bulb),
]

if __name__=="__main__":
    import v3_forms as F
    T=B.TEAL_S; N=B.NEUT_S
    cols=5; rows=(len(ICONS)+cols-1)//cols
    W=B.W; cell_w=(W-B.PAD*2)/cols; cell_h=118
    H=int(70+rows*cell_h+30)
    c=F.WideCanvas(W,H)
    c.rect([B.PAD,26,B.PAD+44,30],fill=T[2],radius=2)
    c.text((B.PAD,44),"SAP 어휘 선 아이콘 세트 v1",B.F("ExtraBold",26),fill=T[1])
    y0=96
    for idx,(name,fn) in enumerate(ICONS):
        r=idx//cols; cc=idx%cols
        cx=B.PAD+cell_w*cc+cell_w/2; cy=y0+cell_h*r+34
        c.ellipse([cx-32,cy-32,cx+32,cy+32],fill="#ffffff",outline=N[4],width=2)
        fn(c,cx,cy,1.5,T[1],3)
        c.center_text(cx,cy+52,name,B.F("SemiBold",15),fill=N[1])
    c.save(f"{OUT_DIR}/sap_icons_sheet.jpg" if False else "/sessions/magical-elegant-hopper/mnt/outputs/sap_icons_sheet.jpg")
    print("sheet done")
