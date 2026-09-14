"""Exact, reproducible SVG teaching diagrams; also exports 2x PNG previews.
No external images or font files. CairoSVG resolves installed fonts.
"""
from pathlib import Path
from html import escape
import json, math
import cairosvg
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'_assets'; OUT.mkdir(exist_ok=True)
INK='#183247'; BLUE='#17688f'; GREEN='#22796b'; GOLD='#af641e'; PURPLE='#76559a'; GRAY='#657986'
RECORDS=[]
def fmt(v):
    return str(int(round(v))) if abs(v-round(v))<1e-8 else f'{v:.2f}'.rstrip('0').replace('.',',')
def save(name,s,record=None):
    (OUT/(name+'.svg')).write_text(s,encoding='utf-8')
    cairosvg.svg2png(bytestring=s.encode(),write_to=str(OUT/(name+'.png')),output_width=1600)
    if record: RECORDS.append(dict(file=name,**record))
def graph(name,c,b,a,d,xmax,ymax,unit,period='',mode='base',amount=0,policy=None,labels=True):
    """Inverse demand c-bQ; inverse competitive supply / MC a+dQ.
    All shaded polygons and markers derive from these functions.
    mode: base / tax / tax_areas / subsidy / subsidy_budget / ceiling / floor /
          quota / surplus / supply_tax / supply_subsidy.
    """
    W,H=800,394; x0,x1,yt,yb=92,706,44,316
    X=lambda q:x0+(x1-x0)*q/xmax
    Y=lambda p:yb-(yb-yt)*p/ymax
    q0=(c-a)/(b+d); p0=c-b*q0
    q=q0; pc=pp=p0
    if mode.startswith('tax') or mode=='supply_tax': q=(c-a-amount)/(b+d);pc=c-b*q;pp=a+d*q
    if mode.startswith('subsidy') or mode=='supply_subsidy': q=(c-a+amount)/(b+d);pc=c-b*q;pp=a+d*q
    qd=qs=None
    if mode in ('ceiling','floor'):
        pc=pp=amount; qd=(c-amount)/b; qs=(amount-a)/d; q=min(qd,qs)
    if mode=='quota': q=min(amount,q0);pc=pp=c-b*q
    s=[f'<svg xmlns="http://www.w3.org/2000/svg" width="800" height="394" viewBox="0 0 800 394"><rect width="800" height="394" fill="#f7fafb" rx="8"/>']
    def text(x,y,t,size=15,col=INK,anchor='start',weight='normal'):
        s.append(f'<text x="{x:.2f}" y="{y:.2f}" font-family="Lato,DejaVu Sans,sans-serif" font-size="{size}" fill="{col}" text-anchor="{anchor}" font-weight="{weight}">{escape(t)}</text>')
    def line(q1,p1,q2,p2,color=GRAY,width=1,dash=None):
        s.append(f'<line x1="{X(q1):.4f}" y1="{Y(p1):.4f}" x2="{X(q2):.4f}" y2="{Y(p2):.4f}" stroke="{color}" stroke-width="{width}"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>')
    shapes=[]; points=[]; curves=[]
    def polygon(pts,color,label=None):
        coords=' '.join(f'{X(x):.4f},{Y(y):.4f}' for x,y in pts)
        s.append(f'<polygon points="{coords}" fill="{color}" fill-opacity="0.19" stroke="{color}" stroke-width="1"/>')
        shapes.append({'points':pts,'label':label})
        if label:
            cx=sum(x for x,y in pts)/len(pts);cy=sum(y for x,y in pts)/len(pts)
            text(X(cx),Y(cy)+5,label,16,color,'middle','bold')
    # Axis scaffolding first, then reference grids, fills, curves and markers.
    text(x0,24,f'P (€ per {unit})',16,weight='bold')
    plural={'fruitbeker':'fruitbekers','poster':'posters','mok':'mokken','tas':'tassen','stickerpakket':'stickerpakketten','workshopplaats':'workshopplaatsen','lesplaats':'lesplaatsen','sportplaats':'sportplaatsen','cursusplaats':'cursusplaatsen','puzzel':'puzzels','schilderpakket':'schilderpakketten','bordspel':'bordspellen','tent':'tenten','festivalbandje':'festivalbandjes'}.get(unit,unit.replace('krat ','kratten '))
    xlabel=f'Q ({plural}{" " + period if period else ""})'
    text((x0+x1)/2,380,xlabel,16,anchor='middle',weight='bold')
    pxstep=20 if xmax>=100 else 10
    pystep=2 if ymax<=20 else 5 if ymax<=40 else 10
    for xx in range(0,int(xmax)+1,pxstep):
        line(xx,0,xx,ymax,'#dde6eb',.65)
        text(X(xx),yb+21,fmt(xx),14,anchor='middle')
    special=[]
    if mode not in ('base','supply_tax','supply_subsidy'):
        special=[(pc,'Pc') ,(pp,'Pp')] if mode.startswith(('tax','subsidy')) else [(pc,'P')]
        if labels and all(abs(Y(p0)-Y(v))>=19 for v,l in special): special.append((p0,'P₀'))
    unique=[]
    for v,l in special:
        if not any(abs(v-u[0])<1e-7 for u in unique):unique.append((v,l))
    for yy in range(0,int(ymax)+1,pystep):
        line(0,yy,xmax,yy,'#dde6eb',.65)
        if not (labels and any(abs(Y(yy)-Y(v))<13 for v,l in unique)):
            text(x0-10,Y(yy)+5,fmt(yy),14,anchor='end')
    line(0,0,0,ymax,INK,1.6);line(0,0,xmax,0,INK,1.6)
    # Shaded welfare surfaces, never used as a solution on a base exercise graph.
    if mode=='tax_areas':
        polygon([(0,pc),(0,c),(q,pc)],BLUE,'CS')
        polygon([(0,a),(0,pp),(q,pp)],GREEN,'PS')
        polygon([(0,pp),(q,pp),(q,pc),(0,pc)],PURPLE,'O')
        polygon([(q,pp),(q,pc),(q0,p0)],GOLD,'W')
    if mode in ('subsidy','subsidy_budget'):
        polygon([(0,pc),(q,pc),(q,pp),(0,pp)],PURPLE,'U')
        if mode=='subsidy_budget':polygon([(q0,p0),(q,pc),(q,pp)],GOLD,'W')
    if mode=='surplus':
        polygon([(0,p0),(0,c),(q0,p0)],BLUE,'CS')
        polygon([(0,a),(0,p0),(q0,p0)],GREEN,'PS')
    if mode=='floor' and policy=='purchase':
        polygon([(qd,0),(qs,0),(qs,pc),(qd,pc)],PURPLE,'U')
    def curve(intercept,slope,label,col,delta=0,dashed=False):
        lo=0.; hi=float(xmax)
        if slope<0: hi=min(hi,intercept/-slope)
        elif slope>0:
            lo=max(lo,-intercept/slope);hi=min(hi,(ymax-intercept)/slope)
        if hi<lo:return
        line(lo,intercept+slope*lo,hi,intercept+slope*hi,col,2.7,'8 4' if dashed else None)
        curves.append({'label':label,'intercept':intercept,'slope':slope,'ends':[[lo,intercept+slope*lo],[hi,intercept+slope*hi]]})
        # Put label right of the endpoint; full right margin is reserved for this.
        ty=Y(intercept+slope*hi)+5+delta
        if ty>yb-7:ty=yb-9
        text(X(hi)+8,ty,label,15,col,weight='bold')
    curve(c,-b,'V',BLUE)
    curve(a,d,'A',GREEN)
    if mode in ('tax','supply_tax'):curve(a+amount,d,'A + t',PURPLE,dashed=True)
    if mode in ('subsidy','supply_subsidy'):curve(a-amount,d,'A − s',PURPLE,dashed=True)
    if mode in ('ceiling','floor'):
        line(0,amount,xmax,amount,GOLD,2.2)
        text(x1+8,Y(amount)+5,'Pmax' if mode=='ceiling' else 'Pmin',14,GOLD,weight='bold')
    if mode=='quota':
        line(amount,0,amount,ymax,PURPLE,2,'7 4')
        text(X(amount)+9,yt+19,'quotum',14,PURPLE)
    def dot(qq,ppp,label=None,kind='demand'):
        s.append(f'<circle cx="{X(qq):.4f}" cy="{Y(ppp):.4f}" r="4.5" fill="{INK}"/>')
        points.append({'q':qq,'p':ppp,'on':kind})
        if label:text(X(qq)+10,Y(ppp)+23,label,14,GRAY)
    if labels and mode not in ('base','supply_tax','supply_subsidy'):
        dot(q0,p0,f'E₀ ({fmt(q0)}; {fmt(p0)})' if not any(l=='P₀' for v,l in unique) else 'E₀','both')
        for val,label in unique:
            line(0,val,min(q,xmax),val,GRAY,1,'5 4')
            text(x0-9,Y(val)+5,f'{label}={fmt(val)}',14,anchor='end')
        if mode.startswith(('tax','subsidy')):
            dot(q,pc,kind='demand');dot(q,pp,kind='supply')
            line(q,pp,q,pc,GOLD,3.6);line(q,0,q,min(pc,pp),GRAY,1.1,'5 4')
            if abs(q/pxstep-round(q/pxstep))>.001: text(X(q),yb+21,fmt(q),14,anchor='middle',weight='bold')
            text(X(q),yb+43,'nieuw',13,GOLD,anchor='middle')
        if mode in ('ceiling','floor'):
            for qq,k in [(qd,'demand'),(qs,'supply')]:
                dot(qq,amount,kind=k);line(qq,0,qq,amount,GRAY,1,'5 4')
                if abs(qq/pxstep-round(qq/pxstep))>.001:text(X(qq),yb+21,fmt(qq),14,anchor='middle')
            text(X(qd),yb+43,'Qv',14,BLUE,anchor='middle',weight='bold')
            text(X(qs),yb+43,'Qa',14,GREEN,anchor='middle',weight='bold')
        if mode=='quota':dot(q,pc,kind='demand');text(X(q),yb+43,'quotum',14,PURPLE,anchor='middle')
    s.append('</svg>')
    save(name,''.join(s),{'c':c,'b':b,'a':a,'d':d,'xmax':xmax,'ymax':ymax,'mode':mode,'amount':amount,'q0':q0,'p0':p0,'q':q,'pc':pc,'pp':pp,'points':points,'curves':curves,'areas':shapes})

def flow(name,kind):
    # Few words, explicit roles; arrows show payment flows rather than fictitious curves.
    svg=['<svg xmlns="http://www.w3.org/2000/svg" width="800" height="220" viewBox="0 0 800 220"><rect width="800" height="220" rx="8" fill="#f2f6f8"/>']
    def txt(x,y,t,size=17,col=INK,weight='normal'):
        svg.append(f'<text x="{x}" y="{y}" text-anchor="middle" fill="{col}" font-family="Lato,DejaVu Sans,sans-serif" font-size="{size}" font-weight="{weight}">{escape(t)}</text>')
    for x,t,col in [(30,'Koper',BLUE),(305,'Verkoper',GREEN),(580,'Overheid',PURPLE)]:
        svg.append(f'<rect x="{x}" y="55" width="185" height="92" rx="6" fill="white" stroke="{col}" stroke-width="2"/>');txt(x+92.5,85,t,20,col,'bold')
    if kind=='tax':
        txt(122,116,'betaalt Pc = € 10');txt(397,116,'houdt Pp = € 6');txt(672,116,'ontvangt t = € 4')
        for x in [220,495]:svg.append(f'<path d="M{x} 99 h76 l-10 -6 m10 6 l-10 6" stroke="{INK}" fill="none" stroke-width="2"/>')
        txt(400,183,'Pc − Pp = t     →     € 10 − € 6 = € 4',21,INK,'bold')
        txt(400,27,'Geldstroom per verkochte fruitbeker',17)
    else:
        txt(122,116,'betaalt Pc = € 10');txt(397,116,'ontvangt Pp = € 14');txt(672,116,'betaalt s = € 4')
        svg.append(f'<path d="M220 99 h76 l-10 -6 m10 6 l-10 6 M575 99 h-76 l10 -6 m-10 6 l10 6" stroke="{INK}" fill="none" stroke-width="2"/>')
        txt(400,183,'Pp − Pc = s     →     € 14 − € 10 = € 4',21,INK,'bold')
        txt(400,27,'Geldstroom per verkochte workshopplaats',17)
    svg.append('</svg>');save(name,''.join(svg),{'type':'flow','kind':kind})

def incidence(name):
    s=['<svg xmlns="http://www.w3.org/2000/svg" width="800" height="300" viewBox="0 0 800 300"><rect width="800" height="300" rx="8" fill="#f7fafb"/>']
    def t(x,y,v,size=16,col=INK):s.append(f'<text x="{x}" y="{y}" font-family="Lato,DejaVu Sans,sans-serif" font-size="{size}" fill="{col}">{escape(v)}</text>')
    t(25,28,'Zelfde beginsituatie: P₀ = € 8; Q₀ = 60. Zelfde aanbod en belasting t = € 3.',17)
    for yy,label,buyer,seller in [(90,'Markt A',1.5,1.5),(182,'Markt B',2,1)]:
        t(28,yy+20,label,19)
        x=185;scale=170
        s.append(f'<rect x="{x}" y="{yy}" width="{buyer*scale}" height="45" fill="{BLUE}"/><rect x="{x+buyer*scale}" y="{yy}" width="{seller*scale}" height="45" fill="{GREEN}"/>')
        t(x+15,yy+28,'koper € '+fmt(buyer),17,'white');t(x+buyer*scale+12,yy+28,'verkoper € '+fmt(seller),17,'white')
    t(28,264,'De vraag reageert in B minder sterk. Kopers dragen daar een groter deel.',17)
    s.append('</svg>');save(name,''.join(s),{'type':'incidence','tax':3,'buyerA':1.5,'sellerA':1.5,'buyerB':2,'sellerB':1})

def all_assets():
    flow('3.1.1_fig_1','tax');flow('3.1.3_fig_1','subsidy');incidence('3.1.2_fig_2')
    configs={
      '3.1.1_fig_2':(14,.1,2,.1,140,16,'fruitbeker','per dag','tax',4),
      '3.1.1_ex_1':(16,.1,4,.1,160,18,'poster','per week','base',0),
      '3.1.1_ex_2':(18,.2,6,.1,90,20,'mok','per dag','base',0),
      '3.1.1_target':(20,.2,2,.1,100,22,'tas','per dag','base',0),
      '3.1.1_ans_1':(16,.1,4,.1,160,18,'poster','per week','tax',4),
      '3.1.1_ans_2':(18,.2,6,.1,90,20,'mok','per dag','tax',3),
      '3.1.1_ans_3':(20,.2,2,.1,100,22,'tas','per dag','tax',3),
      '3.1.2_fig_1':(14,.1,2,.1,140,16,'fruitbeker','per dag','tax_areas',4),
      '3.1.2_ex_1':(16,.1,4,.1,160,18,'stickerpakket','per week','base',0),
      '3.1.2_target':(20,.2,2,.1,100,22,'tas','per dag','base',0),
      '3.1.2_ans_1':(16,.1,4,.1,160,18,'stickerpakket','per week','tax_areas',4),
      '3.1.2_ans_2':(20,.2,2,.1,100,22,'tas','per dag','tax_areas',3),
      '3.1.3_fig_2':(18,.1,6,.1,160,24,'workshopplaats','per week','subsidy',4),
      '3.1.3_fig_3':(18,.1,6,.1,160,24,'workshopplaats','per week','subsidy_budget',4),
      '3.1.3_ex_1':(22,.1,10,.1,160,28,'lesplaats','per week','base',0),
      '3.1.3_ex_2':(24,.2,6,.1,120,26,'sportplaats','per week','base',0),
      '3.1.3_target':(26,.2,8,.1,130,28,'cursusplaats','per week','base',0),
      '3.1.3_ans_1':(22,.1,10,.1,160,28,'lesplaats','per week','subsidy',4),
      '3.1.3_ans_2':(24,.2,6,.1,120,26,'sportplaats','per week','subsidy',3),
      '3.1.3_ans_3':(26,.2,8,.1,130,28,'cursusplaats','per week','subsidy_budget',3),
      '3.1.4_fig_1':(14,.1,2,.1,140,16,'puzzel','per week','ceiling',6),
      '3.1.4_ex_1':(16,.1,4,.1,160,18,'schilderpakket','per week','base',0),
      '3.1.4_ex_2':(20,.2,2,.1,100,22,'bordspel','per week','base',0),
      '3.1.4_target':(18,.1,6,.1,160,24,'tent','per weekend','base',0),
      '3.1.4_ans_1':(16,.1,4,.1,160,18,'schilderpakket','per week','ceiling',8),
      '3.1.4_ans_2':(20,.2,2,.1,100,22,'bordspel','per week','ceiling',6),
      '3.1.4_ans_3':(18,.1,6,.1,160,24,'tent','per weekend','ceiling',10),
      '3.1.5_fig_1':(14,.1,2,.1,140,16,'krat appels','per week','floor',10),
      '3.1.5_fig_2':(14,.1,2,.1,140,16,'krat appels','per week','quota',40),
      '3.1.5_ex_1':(18,.1,6,.1,160,24,'krat peren','per week','base',0),
      '3.1.5_ex_2':(22,.1,10,.1,160,28,'krat pruimen','per week','base',0),
      '3.1.5_target':(20,.1,8,.1,160,26,'krat paddenstoelen','per week','base',0),
      '3.1.5_ans_1':(18,.1,6,.1,160,24,'krat peren','per week','floor',14),
      '3.1.5_ans_2':(22,.1,10,.1,160,28,'krat pruimen','per week','floor',18),
      '3.1.5_ans_3':(20,.1,8,.1,160,26,'krat paddenstoelen','per week','floor',16),
      '3.1.5_ans_4':(20,.1,8,.1,160,26,'krat paddenstoelen','per week','quota',40),
      '3.1.6_target':(24,.2,6,.1,120,26,'festivalbandje','per dag','base',0),
      '3.1.6_ans_1':(24,.2,6,.1,120,26,'festivalbandje','per dag','tax_areas',3),
      '3.1.6_ans_2':(24,.2,6,.1,120,26,'festivalbandje','per dag','ceiling',10),
    }
    for name,v in configs.items():graph(name,*v,policy='purchase' if '3.1.5' in name and v[-2]=='floor' else None)
    (ROOT/'QA/figure_geometry.json').write_text(json.dumps(RECORDS,ensure_ascii=False,indent=2))
    print('Figures:',len(RECORDS))
if __name__=='__main__':all_assets()
