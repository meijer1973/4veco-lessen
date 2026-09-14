"""Numerically specified vector teaching figures; no external data or fonts bundled."""
from pathlib import Path
from html import escape
import json,math
import cairosvg
ROOT=Path(__file__).resolve().parent; AS=ROOT/'_assets';AS.mkdir(exist_ok=True)
INK='#183247'; BLUE='#146d9b';TEAL='#247d70';AMBER='#ad681f';GRAY='#667c8b';LIGHT='#edf3f6';RED='#a54c39'
LOG=[]
def n(v):
    if abs(v-round(v))<1e-8:return f'{int(round(v)):,}'.replace(',','.')
    return f'{v:.2f}'.rstrip('0').rstrip('.').replace('.',',')
class SVG:
    def __init__(self,name,w=900,h=415,title=''):
        self.name=name;self.w=w;self.h=h;self.panels=[]
        self.bits=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img"><title>{escape(title or name)}</title>',
        '<defs><marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10" fill="none" stroke="#536777" stroke-width="1.6"/></marker><pattern id="hatch" width="9" height="9" patternUnits="userSpaceOnUse"><path d="M-2,2 L2,-2 M0,9 L9,0 M7,11 L11,7" stroke="#183247" stroke-opacity=".22" stroke-width="1"/></pattern></defs>',
        f'<rect width="{w}" height="{h}" rx="10" fill="#f5f8fa"/>']
    def text(self,x,y,t,size=18,color=INK,anchor='start',weight=400):
        self.bits.append(f'<text x="{x:.3f}" y="{y:.3f}" font-family="Lato,DejaVu Sans,sans-serif" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{color}">{escape(str(t))}</text>')
    def line(self,x1,y1,x2,y2,color=GRAY,width=1.6,dash='',arrow=False):
        self.bits.append(f'<line x1="{x1:.4f}" y1="{y1:.4f}" x2="{x2:.4f}" y2="{y2:.4f}" stroke="{color}" stroke-width="{width}"'+(f' stroke-dasharray="{dash}"' if dash else '')+(' marker-end="url(#arr)"' if arrow else '')+'/>')
    def rect(self,x,y,w,h,fill='white',stroke=BLUE):
        self.bits.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{fill}" stroke="{stroke}" stroke-width="1.6"/>')
    def save(self):
        txt='\n'.join(self.bits+['</svg>']);(AS/f'{self.name}.svg').write_text(txt,encoding='utf8')
        cairosvg.svg2png(bytestring=txt.encode(),write_to=str(AS/f'{self.name}.png'),output_width=1800)
        LOG.append({'file':self.name,'width':self.w,'height':self.h,'panels':self.panels})
class Plot:
    def __init__(self,s,x,y,w,h,xmax,ymax,xticks,yticks,title,xlabel,ylabel='P (€ per kg)',scale=1):
        self.s=s;self.x=x;self.y=y;self.w=w;self.h=h;self.xmax=xmax;self.ymax=ymax
        self.id=f'p{len(s.panels)}';self.log={'id':self.id,'box':[x,y,w,h],'xmax':xmax,'ymax':ymax,'curves':[],'points':[],'areas':[]};s.panels.append(self.log)
        s.text(x+w/2,24,title,21,anchor='middle',weight=700)
        s.text(x,53,ylabel,17)
        s.bits.append(f'<defs><clipPath id="{self.id}"><rect x="{x}" y="{y}" width="{w}" height="{h}"/></clipPath></defs>')
        for v in xticks:
            xx=self.X(v);s.line(xx,y,xx,y+h,'#dce5eb',.7);s.text(xx,y+h+25,n(v/scale),16,anchor='middle')
        for v in yticks:
            yy=self.Y(v);s.line(x,yy,x+w,yy,'#dce5eb',.7);s.text(x-10,yy+5,n(v),16,anchor='end')
        s.line(x,y+h,x+w+6,y+h,INK,1.8,arrow=True);s.line(x,y+h,x,y-6,INK,1.8,arrow=True)
        for i,t in enumerate(xlabel.split('\n')):s.text(x+w/2,y+h+51+i*20,t,17,anchor='middle')
    def X(self,q):return self.x+self.w*q/self.xmax
    def Y(self,p):return self.y+self.h*(1-p/self.ymax)
    def curve(self,name,kind,params,color=BLUE,dash='',label_at=None,dy=-10,dx=0,label=True):
        def f(q):
            if kind=='linear':return params[0]+params[1]*q
            if kind=='avg':return params[0]*q+params[1]+params[2]/q
            if kind=='total':return params[0]*q*q+params[1]*q+params[2]
        lo=self.xmax/1000 if kind=='avg' else 0
        points=[]
        # Dense samples; crop to numerical plot boundaries without drawing through undefined regions.
        for k in range(401):
            q=lo+(self.xmax-lo)*k/400;p=f(q)
            points.append([q,p])
        pts=' '.join(f'{self.X(q):.4f},{self.Y(p):.4f}' for q,p in points)
        self.s.bits.append(f'<polyline data-curve="{escape(name)}" data-panel="{self.id}" points="{pts}" fill="none" stroke="{color}" stroke-width="3" clip-path="url(#{self.id})"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>')
        self.log['curves'].append({'name':name,'kind':kind,'params':params,'points':points})
        if label:
            q=self.xmax*(label_at if label_at is not None else .82);p=f(q)
            if not 0<=p<=self.ymax:
                visible=[v for v in points if 0<=v[1]<=self.ymax]
                if visible:q,p=visible[int(.74*(len(visible)-1))]
            if 0<=p<=self.ymax:self.s.text(self.X(q)+dx,self.Y(p)+dy,name,18,color,weight=700)
        return f
    def point(self,q,p,name='',dx=8,dy=-12,color=INK,guides=True):
        if guides:
            self.s.line(self.x,self.Y(p),self.X(q),self.Y(p),GRAY,1.1,'5 4');self.s.line(self.X(q),self.y+self.h,self.X(q),self.Y(p),GRAY,1.1,'5 4')
        self.s.bits.append(f'<circle data-point="{escape(name)}" data-panel="{self.id}" cx="{self.X(q):.4f}" cy="{self.Y(p):.4f}" r="4" fill="{color}"/>')
        if name:self.s.text(self.X(q)+dx,self.Y(p)+dy,name,17,color,weight=700)
        self.log['points'].append({'q':q,'p':p,'name':name})
    def price(self,p,label='P = GO = MO',color=BLUE,dash='',label_at=.12,dy=-9):
        self.curve(label,'linear',[p,0],color,dash,label_at,dy)
    def area(self,q,p,avg,label='winst'):
        low,high=sorted([p,avg]);x=self.X(0);y=self.Y(high);ww=self.X(q)-x;hh=self.Y(low)-y
        self.s.bits.append(f'<rect data-area="{label}" data-panel="{self.id}" x="{x:.4f}" y="{y:.4f}" width="{ww:.4f}" height="{hh:.4f}" fill="{BLUE if p>=avg else RED}" fill-opacity=".13" stroke="none"/>')
        self.s.bits.append(f'<rect x="{x:.4f}" y="{y:.4f}" width="{ww:.4f}" height="{hh:.4f}" fill="url(#hatch)"/>')
        if hh>=28:self.s.text(x+ww/2,y+hh/2+6,label,17,anchor='middle',weight=700)
        self.log['areas'].append({'q':q,'p':p,'avg':avg,'value':q*(p-avg),'rect':[x,y,ww,hh],'label':label})
    def cap(self,q):
        if q<self.xmax:self.s.line(self.X(q),self.y,self.X(q),self.y+self.h,GRAY,1.2,'3 5')

def pair(name,D,A,pr,marketmax,firmmax,ymax,xtm,xtf,yt,firm_line=True,eq=False,unit='kg per dag',note='',cost=None,oldP=None,newA=None,shade=False,firmq=None,markfirm=True):
    s=SVG(name,title='Markt en één onderneming');lm=Plot(s,67,78,330,232,marketmax,ymax,xtm,yt,'De hele markt',f'Q (× 1.000 {unit})',scale=1000)
    lm.curve('V','linear',D,BLUE,label_at=.79,dy=21)
    lm.curve('A₀' if newA else 'A','linear',A,TEAL,label_at=.42,dy=-10,dash='7 4' if newA else '')
    if newA:lm.curve('A₁','linear',newA,TEAL,label_at=.77,dy=-9)
    if eq:
        qe=(D[0]-A[0])/(A[1]-D[1]);lm.point(qe,D[0]+D[1]*qe,'E₀' if newA else 'E',dx=-27,dy=-12)
        if newA:
            qe2=(D[0]-newA[0])/(newA[1]-D[1]);lm.point(qe2,D[0]+D[1]*qe2,'E₁',dx=9,dy=24)
    rf=Plot(s,541,78,330,232,firmmax,ymax,xtf,yt,'Eén onderneming',f'q ({unit})',ylabel='P, MK en GTK (€ per kg)' if cost else 'P (€ per kg)')
    if cost:
        a,b,c=cost
        rf.curve('MK','linear',[b,2*a],TEAL,label_at=.76,dy=-10)
        rf.curve('GTK','avg',[a,b,c],AMBER,label_at=.86,dy=21)
    if oldP is not None:rf.price(oldP,'P₀ = GO₀ = MO₀',GRAY,'7 4',.05,-9)
    if firm_line:
        rf.price(pr,'P₁ = GO₁ = MO₁' if oldP is not None else 'P = GO = MO',BLUE,label_at=.06,dy=-9)
        if cost and markfirm:
            q=firmq if firmq is not None else min(firmmax,max(0,(pr-b)/(2*a)))
            if shade:rf.area(q,pr,a*q+b+c/q)
            rf.point(q,pr,'',guides=True)
            if oldP is not None:
                oq=(oldP-b)/(2*a);rf.point(oq,oldP,'',color=GRAY)
        if not newA and pr is not None:
            s.line(413,lm.Y(pr),520,rf.Y(pr),GRAY,1.5,arrow=True)
            s.text(466,lm.Y(pr)-13,'zelfde P',15,anchor='middle')
    if note:s.text(450,395,note,17,anchor='middle')
    s.save()

def firm(name,cost,P,cap,ymax=24,xt=None,yt=None,mark=False,shade=False,oldP=None,othercap=None,note='',qmark=None):
    s=SVG(name,900,465,title='Kosten en opbrengsten van één onderneming')
    a,b,c=cost
    pl=Plot(s,79,77,742,282,cap,ymax,xt or [cap*i/4 for i in range(5)],yt or [ymax*i/4 for i in range(5)],'Eén onderneming', 'q (kg per week)','Kosten en opbrengsten (€ per kg)')
    pl.curve('MK','linear',[b,2*a],TEAL,label_at=.85,dy=-13)
    pl.curve('GTK','avg',[a,b,c],AMBER,label_at=.88,dy=25)
    if oldP is not None:pl.price(oldP,'oude P = GO = MO',GRAY,'7 4',.04,-10)
    if P is not None:pl.price(P,'P = GO = MO',BLUE,label_at=.04,dy=-10)
    if mark and P is not None:
        q=qmark if qmark is not None else min(cap,max(0,(P-b)/(2*a)));avg=a*q+b+c/q
        if shade:pl.area(q,P,avg,'winst' if P>avg else 'verlies')
        pl.point(q,P,'',guides=True);pl.point(q,avg,'',color=AMBER,guides=False)
        s.text(450,438,note or f'q = {n(q)}; GTK = € {n(avg)}; winst = € {n(q*(P-avg))} per week',18,anchor='middle')
    elif note:s.text(450,438,note,18,anchor='middle')
    if othercap:pl.cap(othercap)
    s.save()

def flow(name,boxes,sub='',heading=''):
    h=210 if sub else 165;s=SVG(name,900,h,title=heading or 'Stappen in de redenering');w=(840-(len(boxes)-1)*24)/len(boxes)
    if heading:s.text(450,28,heading,20,anchor='middle',weight=700)
    y=55 if heading else 24
    for i,lines in enumerate(boxes):
        x=30+i*(w+24);s.rect(x,y,w,80,stroke=[BLUE,TEAL,AMBER,BLUE,TEAL][i%5])
        for j,t in enumerate(lines):s.text(x+w/2,y+28+j*24,t,19 if j==0 else 16,anchor='middle',weight=700 if j==0 else 400)
        if i<len(boxes)-1:s.line(x+w+2,y+40,x+w+20,y+40,arrow=True)
    if sub:s.text(450,h-22,sub,18,anchor='middle')
    s.save()

def build_all():
    flow('3.2.1_fig_1',[['Veel kleine','aanbieders'],['Gelijk product','en goede informatie'],['Prijsnemer','markt bepaalt P']], 'De onderneming kiest haar productie; zij kan de marktprijs niet naar haar hand zetten.')
    pair('3.2.1_fig_2',[4,-.0005],[1,.00025],2,8000,150,5,[0,2000,4000,6000,8000],[0,50,100,150],[0,1,2,3,4,5],eq=True,note='Q = 4.000 kg voor de markt; q is de afzet van één teler.')
    pair('3.2.1_ex_1',[8,-.001],[2,.001],5,6000,120,10,[0,2000,4000,6000],[0,40,80,120],[0,2,4,6,8,10],firm_line=False)
    pair('3.2.1_ex_2',[8,-.001],[2,.0005],4,8000,120,10,[0,2000,4000,6000,8000],[0,40,80,120],[0,2,4,6,8,10],firm_line=False)
    pair('3.2.1_target',[5,-.0005],[1,.0005],3,10000,160,6,[0,2000,4000,6000,8000,10000],[0,40,80,120,160],[0,1,2,3,4,5,6],firm_line=False)
    for name,D,A,pr,mm,fm,ym,xtm,xtf,yt in [
        ('3.2.1_ans_1',[8,-.001],[2,.001],5,6000,120,10,[0,2000,4000,6000],[0,40,80,120],[0,2,4,6,8,10]),
        ('3.2.1_ans_2',[8,-.001],[2,.0005],4,8000,120,10,[0,2000,4000,6000,8000],[0,40,80,120],[0,2,4,6,8,10]),
        ('3.2.1_ans_3',[5,-.0005],[1,.0005],3,10000,160,6,[0,2000,4000,6000,8000,10000],[0,40,80,120,160],[0,1,2,3,4,5,6])]:pair(name,D,A,pr,mm,fm,ym,xtm,xtf,yt,eq=True)
    flow('3.2.2_fig_1',[['MO > MK','iets meer produceren'],['MO = MK','controleer het maximum'],['MO < MK','iets minder produceren']], 'Controleer ook: past de berekende hoeveelheid binnen de productiecapaciteit?')
    flow('3.2.2_fig_2',[['a × q²','wordt 2a × q'],['b × q','wordt b'],['c','wordt 0']], 'TK = a × q² + b × q + c    →    MK = 2a × q + b', 'Differentiëren: bekijk elke term apart')
    firm('3.2.2_fig_3',[.05,2,80],8,100,12,[0,20,40,60,80,100],[0,2,4,6,8,10,12],mark=True,note='Links van q = 60: MO > MK. Rechts ervan: MO < MK.')
    firm('3.2.2_fig_4',[.05,2,80],8,100,12,[0,20,40,60,80,100],[0,2,4,6,8,10,12],mark=True,shade=True)
    firm('3.2.2_we_1',[.1,2,40],10,50,16,[0,10,20,30,40,50],[0,4,8,12,16],mark=True,shade=True)
    firm('3.2.2_ex_1',[.05,4,180],12,120,20,[0,20,40,60,80,100,120],[0,4,8,12,16,20])
    firm('3.2.2_ex_2',[.02,4,100],12,250,20,[0,50,100,150,200,250],[0,4,8,12,16,20])
    firm('3.2.2_target',[.04,4,400],16,200,24,[0,50,100,150,200],[0,4,8,12,16,20,24])
    firm('3.2.2_ans_1',[.05,4,180],12,120,20,[0,20,40,60,80,100,120],[0,4,8,12,16,20],mark=True,shade=True)
    firm('3.2.2_ans_2',[.02,4,100],12,250,20,[0,50,100,150,200,250],[0,4,8,12,16,20],mark=True,shade=True)
    firm('3.2.2_ans_3',[.04,4,400],16,200,24,[0,50,100,150,200],[0,4,8,12,16,20,24],mark=True,shade=True)
    flow('3.2.3_fig_1',[['Winst','boven normale beloning'],['Toetreding','marktaanbod neemt toe'],['Prijs daalt','winst per bedrijf daalt']], 'Zolang toetreding aantrekkelijk blijft, gaat de aanpassing verder.')
    pair('3.2.3_fig_2',[12,-1/1500],[2,.001],6,18000,100,14,[0,3000,6000,9000,12000,15000,18000],[0,20,40,60,80,100],[0,2,4,6,8,10,12,14],eq=True,unit='kg per week',cost=[.05,2,80],oldP=8,newA=[2,1/2250],note='De markt groeit van 6.000 naar 9.000 kg; één onderneming gaat van 60 naar 40 kg.')
    pair('3.2.3_fig_3',[8,-.002],[2,.002],6,4000,50,10,[0,1000,2000,3000,4000],[0,10,20,30,40,50],[0,2,4,6,8,10],eq=True,unit='kg per week',cost=[.1,2,40],oldP=5,newA=[2,.004],note='Na uittreding stijgt P van € 5 naar € 6; de overblijvende onderneming produceert meer.')
    firm('3.2.3_we_1',[.1,2,40],6,50,12,[0,10,20,30,40,50],[0,2,4,6,8,10,12],oldP=8,mark=True,note='Langetermijnuitkomst: q = 20, P = MK = GTK = € 6; winst = € 0.')
    pair('3.2.3_ex_1',[8,-.002],[2,.002],5,4000,50,10,[0,1000,2000,3000,4000],[0,10,20,30,40,50],[0,2,4,6,8,10],eq=True,unit='kg per week',cost=[.1,2,40],markfirm=False)
    pair('3.2.3_ex_2',[14,-.002],[2,.002],8,7000,50,16,[0,1000,2000,3000,4000,5000,6000,7000],[0,10,20,30,40,50],[0,4,8,12,16],unit='kg per week',cost=[.1,2,40],markfirm=False)
    pair('3.2.3_target',[16,-.0004],[4,.0004],10,40000,250,20,[0,10000,20000,30000,40000],[0,50,100,150,200,250],[0,4,8,12,16,20],unit='kg per week',cost=[.02,4,200],markfirm=False)
    pair('3.2.3_ans_1',[14,-.002],[2,.002],6,7000,50,16,[0,1000,2000,3000,4000,5000,6000,7000],[0,10,20,30,40,50],[0,4,8,12,16],eq=True,unit='kg per week',cost=[.1,2,40],oldP=8,newA=[2,.001])
    pair('3.2.3_ans_2',[16,-.0004],[4,.0004],8,40000,250,20,[0,10000,20000,30000,40000],[0,50,100,150,200,250],[0,4,8,12,16,20],eq=True,unit='kg per week',cost=[.02,4,200],oldP=10,newA=[4,.0002])
    # Mixed target: supplied market has both demand curves, fixed short-run market supply.
    for suffix,stage in [('target','base'),('ans_1','short'),('ans_2','long')]:
        s=SVG('3.2.4_'+suffix,title='Marktverandering en onderneming')
        lm=Plot(s,67,78,330,232,50000,24,[0,10000,20000,30000,40000,50000],[0,4,8,12,16,20,24],'De hele markt','Q (× 1.000 kg per week)',scale=1000)
        lm.curve('V₀','linear',[12,-.0004],BLUE,'7 4',.27,22)
        lm.curve('V₁','linear',[20,-.0004],BLUE,label_at=.72,dy=-10)
        lm.curve('A₀','linear',[4,.0004],TEAL,label_at=.66,dy=-12,dash='7 4' if stage=='long' else '')
        if stage!='base':lm.point(10000,8,'E₀',dx=-29,dy=22);lm.point(20000,12,'E₁',dx=-25,dy=-13)
        if stage=='long':lm.curve('A₂','linear',[4,1/7500],TEAL,label_at=.82,dy=23);lm.point(30000,8,'E₂',dx=7,dy=24)
        rf=Plot(s,541,78,330,232,250,24,[0,50,100,150,200,250],[0,4,8,12,16,20,24],'Eén onderneming','q (kg per week)',ylabel='P, MK en GTK (€ per kg)')
        rf.curve('MK','linear',[4,.04],TEAL,label_at=.8,dy=-12)
        rf.curve('GTK','avg',[.02,4,200],AMBER,label_at=.83,dy=23)
        if stage=='short':
            rf.price(12,'P₁ = GO₁ = MO₁',label_at=.05);rf.area(200,12,9);rf.point(200,12,'',guides=True);rf.point(200,9,'',color=AMBER,guides=False)
        if stage=='long':
            rf.price(12,'P₁',GRAY,'7 4',.05);rf.price(8,'P₂ = GO₂ = MO₂',label_at=.05);rf.point(100,8,'',guides=True)
        note={'base':'Links: Q in duizenden kg. Rechts: q in kg. Vul de gevraagde markeringen aan.', 'short':'Na de vraagstijging, vóór toetreding: P = € 12, q = 200 en winst = € 600 per week.', 'long':'Na toetreding: P = € 8, markt Q = 30.000, onderneming q = 100 en winst = € 0.'}[stage]
        s.text(450,395,note,16,anchor='middle');s.save()
    flow('3.2.4_fig_1',[['Markt','vind P'],['Onderneming','vergelijk MO en MK'],['Winst','TO − TK'],['Lange termijn','toetreding of uittreding']], 'Controleer telkens de grootheid, de eenheid en het tijdstip.')
    (ROOT/'QA'/'figure_geometry.json').write_text(json.dumps(LOG,ensure_ascii=False,indent=2))
if __name__=='__main__':build_all();print('SVG/PNG figure pairs:',len(LOG))
