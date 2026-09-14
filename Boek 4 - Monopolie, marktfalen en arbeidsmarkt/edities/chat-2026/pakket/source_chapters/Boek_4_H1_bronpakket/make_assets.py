"""Exact numerical SVG figures for the new monopoly chapter; PNG mirrors for editing."""
from pathlib import Path
from html import escape
import math,json
import cairosvg
ROOT=Path(__file__).resolve().parent;AS=ROOT/'_assets';AS.mkdir(exist_ok=True)
INK='#183247';BLUE='#146d9b';TEAL='#247d70';AMBER='#ad681f';RED='#aa4e42';GRAY='#657986'
LOG=[]
def num(v):
    if abs(v-round(v))<1e-8:return str(int(round(v)))
    return ('%.2f'%v).rstrip('0').rstrip('.').replace('.',',')
class SVG:
    def __init__(self,name,w=900,h=425,title=''):
        self.name=name;self.w=w;self.h=h;self.panels=[]
        self.bits=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img"><title>{escape(title or name)}</title>',
        '<defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10" fill="none" stroke="#536777" stroke-width="1.5"/></marker><pattern id="hatch" width="9" height="9" patternUnits="userSpaceOnUse"><path d="M-2,2 L2,-2 M0,9 L9,0 M7,11 L11,7" stroke="#183247" stroke-opacity=".22" stroke-width="1"/></pattern></defs>',f'<rect width="{w}" height="{h}" rx="8" fill="#f5f8fa"/>']
    def text(self,x,y,t,size=18,color=INK,anchor='start',weight=400):
        self.bits.append(f'<text x="{x:.4f}" y="{y:.4f}" font-family="Lato,DejaVu Sans,sans-serif" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{color}">{escape(str(t))}</text>')
    def line(self,x1,y1,x2,y2,color=GRAY,width=1.5,dash='',arrow=False):
        self.bits.append(f'<line x1="{x1:.4f}" y1="{y1:.4f}" x2="{x2:.4f}" y2="{y2:.4f}" stroke="{color}" stroke-width="{width}"'+(f' stroke-dasharray="{dash}"' if dash else '')+(' marker-end="url(#arrow)"' if arrow else '')+'/>')
    def rect(self,x,y,w,h,fill='white',stroke=BLUE):
        self.bits.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>')
    def save(self):
        text='\n'.join(self.bits+['</svg>']);(AS/(self.name+'.svg')).write_text(text)
        cairosvg.svg2png(bytestring=text.encode(),write_to=str(AS/(self.name+'.png')),output_width=1800)
        LOG.append({'file':self.name,'width':self.w,'height':self.h,'panels':self.panels})
class Plot:
    def __init__(self,s,x,y,w,h,xmax,ymax,xticks,yticks,title='',xlabel='q (kg per week)',ylabel='Bedrag (€ per kg)',ymin=0):
        self.s=s;self.x=x;self.y=y;self.w=w;self.h=h;self.xmax=xmax;self.ymax=ymax;self.ymin=ymin
        self.id='p'+str(len(s.panels));self.log={'id':self.id,'box':[x,y,w,h],'xmax':xmax,'ymin':ymin,'ymax':ymax,'curves':[],'points':[],'areas':[]};s.panels.append(self.log)
        s.text(x+w/2,27,title,21,anchor='middle',weight=700);s.text(x,54,ylabel,17)
        s.bits.append(f'<defs><clipPath id="{self.id}"><rect x="{x}" y="{y}" width="{w}" height="{h}"/></clipPath></defs>')
        for v in xticks:
            s.line(self.X(v),y,self.X(v),y+h,'#dbe4e9',.7);s.text(self.X(v),y+h+25,num(v),17,anchor='middle')
        for v in yticks:
            s.line(x,self.Y(v),x+w,self.Y(v),'#dbe4e9',.7);s.text(x-11,self.Y(v)+5,num(v),17,anchor='end')
        s.line(x,self.Y(0),x+w+7,self.Y(0),INK,1.7,arrow=True);s.line(x,y+h,x,y-5,INK,1.7,arrow=True)
        s.text(x+w/2,y+h+52,xlabel,18,anchor='middle')
    def X(self,q):return self.x+self.w*q/self.xmax
    def Y(self,p):return self.y+self.h*(self.ymax-p)/(self.ymax-self.ymin)
    def curve(self,name,kind,params,color=BLUE,dash='',labelq=None,dx=0,dy=-12,label=True):
        def fn(q):
            if kind=='linear':return params[0]+params[1]*q
            if kind=='total':return params[0]*q*q+params[1]*q+params[2]
            if kind=='avg':return params[0]*q+params[1]+params[2]/q
        lo=self.xmax/1500 if kind=='avg' else 0
        points=[[lo+(self.xmax-lo)*i/600,fn(lo+(self.xmax-lo)*i/600)] for i in range(601)]
        pts=' '.join(f'{self.X(q):.8f},{self.Y(p):.8f}' for q,p in points)
        self.s.bits.append(f'<polyline data-panel="{self.id}" data-curve="{escape(name)}" points="{pts}" fill="none" stroke="{color}" stroke-width="3" clip-path="url(#{self.id})"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>')
        self.log['curves'].append({'name':name,'kind':kind,'params':params})
        if label:
            q=labelq if labelq is not None else self.xmax*.75;p=fn(q)
            if self.ymin<=p<=self.ymax:self.s.text(self.X(q)+dx,self.Y(p)+dy,name,18,color,weight=700)
        return fn
    def point(self,q,p,name='',curve=None,dx=8,dy=-12,guides=True):
        if guides:
            self.s.line(self.x,self.Y(p),self.X(q),self.Y(p),GRAY,1.1,'5 4');self.s.line(self.X(q),self.Y(0),self.X(q),self.Y(p),GRAY,1.1,'5 4')
        self.s.bits.append(f'<circle data-point="{escape(name)}" data-panel="{self.id}" cx="{self.X(q):.4f}" cy="{self.Y(p):.4f}" r="4.2" fill="{INK}"/>')
        if name:self.s.text(self.X(q)+dx,self.Y(p)+dy,name,18,weight=700)
        self.log['points'].append({'q':q,'p':p,'name':name,'curve':curve})
    def area(self,coords,label='',color=TEAL):
        pts=' '.join(f'{self.X(q):.4f},{self.Y(p):.4f}' for q,p in coords)
        self.s.bits.append(f'<polygon data-area="{escape(label)}" data-panel="{self.id}" points="{pts}" fill="{color}" fill-opacity=".12" stroke="none"/>')
        self.s.bits.append(f'<polygon points="{pts}" fill="url(#hatch)"/>')
        self.log['areas'].append({'label':label,'vertices':coords})
    def vertical(self,q,label='',color=GRAY):
        self.s.line(self.X(q),self.y,self.X(q),self.y+self.h,color,1.5,'4 4')
        if label:self.s.text(self.X(q)-7,self.y+23,label,17,color,anchor='end')

def flow(name,boxes,title='',note=''):
    s=SVG(name,900,195,title);s.text(450,28,title,21,anchor='middle',weight=700)
    w=(840-22*(len(boxes)-1))/len(boxes)
    for i,ls in enumerate(boxes):
        x=30+i*(w+22);s.rect(x,50,w,82,stroke=[BLUE,TEAL,AMBER][i%3])
        for j,t in enumerate(ls):s.text(x+w/2,80+24*j,t,19 if j==0 else 17,anchor='middle',weight=700 if j==0 else 400)
        if i<len(boxes)-1:s.line(x+w+2,91,x+w+19,91,arrow=True)
    if note:s.text(450,168,note,18,anchor='middle')
    s.save()

def demand(name,a,b,xmax=None,points=None,caption='',xlabel='q (kaartjes per dag)',price=0):
    xmax=xmax or a/b;s=SVG(name,title=caption)
    pl=Plot(s,78,78,738,265,xmax,a,[xmax*i/4 for i in range(5)],[a*i/4 for i in range(5)],caption or 'Eén monopolist',xlabel,'P (€ per kaartje)')
    pl.curve('Vraag = GO','linear',[a,-b],labelq=xmax*.83,dy=-16)
    for q,label in (points or []):pl.point(q,a-b*q,label,curve='Vraag = GO')
    s.save()

def mono(name,a,b,cost=None,xmax=None,ymax=None,curves=('go','mr','mc'),qmark=None,showprice=False,profit=False,capacity=None,note='',ymin=0,units='kg per week',title='Eén monopolist'):
    xmax=xmax or a/b;ymax=ymax or a
    s=SVG(name,900,440,title)
    xs=20 if xmax>=100 else 10
    xt=list(range(0,int(xmax)+1,xs))
    ys=10 if ymax-ymin>=40 else 5
    yt=list(range(math.ceil(ymin/ys)*ys,int(ymax)+1,ys))
    if qmark is not None:
        xt=sorted(set([v for v in xt if abs(v-qmark)>=xmax*.07]+[qmark]))
        vals=[a-2*b*qmark] if 'mr' in curves else []
        if showprice: vals += [a-b*qmark]
        for z in vals:
            yt=[v for v in yt if abs(v-z)>=(ymax-ymin)*.065]+[z]
        yt=sorted(set(v for v in yt if ymin<=v<=ymax))
    pl=Plot(s,78,78,738,275,xmax,ymax,xt,yt,title,f'q ({units})','Bedrag (€ per kg)',ymin)
    if 'go' in curves:pl.curve('GO = P','linear',[a,-b],BLUE,labelq=xmax*.72,dy=-13)
    if 'mr' in curves:pl.curve('MO','linear',[a,-2*b],TEAL,'8 5',labelq=min(xmax*.33,a/(2*b)*.64),dy=23)
    if cost:
        aa,c,F=cost
        if 'mc' in curves:pl.curve('MK','linear',[c,2*aa],RED,labelq=xmax*.78,dy=24)
        if 'gtk' in curves:pl.curve('GTK','avg',[aa,c,F],AMBER,labelq=xmax*.75,dy=26)
    if qmark is not None:
        mr=a-2*b*qmark;p=a-b*qmark
        if profit and cost:
            gtk=aa*qmark+c+F/qmark;pl.area([[0,gtk],[qmark,gtk],[qmark,p],[0,p]],'winst' if p>=gtk else 'verlies',BLUE if p>=gtk else RED)
            pl.point(qmark,gtk,'',curve='GTK',guides=False)
            pl.s.line(78,pl.Y(gtk),pl.X(qmark),pl.Y(gtk),GRAY,1,'5 4')
            pl.s.text(pl.X(qmark)/2+39,pl.Y((p+gtk)/2)+6,'winst' if p>=gtk else 'verlies',18,anchor='middle',weight=700)
        if 'mr' in curves:pl.point(qmark,mr,'1',curve='MO',dx=-20,dy=22)
        if showprice:pl.point(qmark,p,'2',curve='GO = P',dx=8,dy=-12)
    if capacity is not None:pl.vertical(capacity,'capaciteit')
    if note:s.text(450,426,note,17,anchor='middle')
    s.save()

def revenues(name,a,b,q0,q1,note=''):
    xmax=max(q1*1.35,q1+5);ymax=a
    s=SVG(name,900,450,'Twee effecten op de omzet')
    pl=Plot(s,80,74,540,275,xmax,ymax,[0,q0,q1],[0,a-b*q1,a-b*q0,a],'Twee effecten op de omzet','q (kg per week)','P (€ per kg)')
    p0=a-b*q0;p1=a-b*q1
    pl.area([[0,0],[q0,0],[q0,p1],[0,p1]],'blijvende omzet',BLUE)
    pl.area([[0,p1],[q0,p1],[q0,p0],[0,p0]],'minder per eerdere kg',RED)
    pl.area([[q0,0],[q1,0],[q1,p1],[q0,p1]],'extra kg',TEAL)
    s.line(pl.X(0),pl.Y(p0),pl.X(q0),pl.Y(p0),BLUE,2.5)
    s.line(pl.X(q1),pl.Y(0),pl.X(q1),pl.Y(p1),TEAL,2.5)
    s.text(646,118,'Extra verkochte kg',18,TEAL,weight=700)
    s.text(646,144,f'{num(q1-q0)} × € {num(p1)}',18)
    s.text(646,171,f'+ € {num((q1-q0)*p1)}',23,TEAL,weight=700)
    s.text(646,228,'Lagere prijs op',18,RED,weight=700);s.text(646,251,'de eerdere kg',18,RED,weight=700)
    s.text(646,277,f'{num(q0)} × € {num(p0-p1)}',18)
    s.text(646,304,f'− € {num(q0*(p0-p1))}',23,RED,weight=700)
    s.text(450,428,note or f'ΔTO = {num((q1-q0)*p1)} − {num(q0*(p0-p1))} = € {num(q1*p1-q0*p0)} per week',20,anchor='middle',weight=700)
    s.save()

def comparative():
    s=SVG('4.1.1_fig_1',900,435,'De vraag voor één onderneming')
    p=Plot(s,66,78,337,262,100,20,[0,25,50,75,100],[0,5,10,15,20],'Eén kleine prijsnemer','q (kg per dag)','P (€ per kg)')
    p.curve('P = GO = MO','linear',[8,0],BLUE,labelq=5,dy=-13)
    p2=Plot(s,528,78,337,262,400,20,[0,100,200,300,400],[0,5,10,15,20],'Eén monopolist','q (kg per dag)','P (€ per kg)')
    p2.curve('Vraag = GO','linear',[20,-.05],BLUE,labelq=180,dy=-14)
    s.text(450,423,'Links: één klein deel van de markt. Rechts: de aanbieder bedient de hele markt.',17,anchor='middle')
    s.save()

def all_assets():
    flow('4.1_opener',[['Kenmerken','Wie bepaalt de prijs?'],['Opbrengst','Wat levert extra afzet op?'],['Winst','Welke q en welke P?']],title='De route door dit hoofdstuk')
    comparative()
    demand('4.1.1_fig_2',12,.1,120,[(40,'A'),(80,'B')],caption='Dezelfde vraaglijn: twee mogelijke keuzes')
    demand('4.1.1_ex_3',20,.1,200,[(80,'A: (80, 12)'),(120,'B: (120, 8)')],caption='Uitlezen: de prijs en afzet horen bij elkaar')
    demand('4.1.1_target',24,.1,240,[(60,'A'),(120,'B')],caption='Bron B · De vraag naar de veerverbinding')
    revenues('4.1.2_fig_1',20,.2,20,30)
    flow('4.1.2_fig_2',[['P = 20 − 0,2q','prijs per kg'],['TO = 20q − 0,2q²','euro per week'],['MO = 20 − 0,4q','euro per extra kg']],title='Vermenigvuldigen en daarna differentiëren')
    mono('4.1.2_fig_3',20,.2,xmax=100,curves=('go',),units='kg per week',title='Eerst: de vraaglijn is de GO-lijn')
    mono('4.1.2_fig_4',20,.2,xmax=100,curves=('go','mr'),ymin=-20,units='kg per week',title='Voeg MO toe: dezelfde q, een ander bedrag')
    revenues('4.1.2_we',12,.1,30,40)
    revenues('4.1.2_ex_13',16,.2,20,30)
    mono('4.1.2_ex_17',24,.2,xmax=100,curves=('go','mr'),ymin=-16,title='Lees P en MO bij dezelfde afzet')
    mono('4.1.3_fig_1',30,.2,(0,6,200),xmax=100,curves=('mr','mc'),qmark=60,capacity=100,title='Stap 1 · Zoek q met MO en MK',note='Vóór 60 kg is MO > MK. Na 60 kg is MO < MK.')
    mono('4.1.3_fig_2',30,.2,(0,6,200),xmax=100,curves=('go','mr','mc'),qmark=60,showprice=True,title='Stap 2 · Ga bij die q omhoog naar GO',note='q = 60 kg per week; P = € 18 per kg. Het bedrag € 6 is MO = MK.')
    mono('4.1.3_fig_3',30,.2,(0,6,200),xmax=100,curves=('go','gtk'),qmark=60,showprice=True,profit=True,title='Stap 3 · Bereken de winst',note='Winst = (P − GTK) × q = (18 − 9,333…) × 60 = € 520 per week.')
    mono('4.1.3_fig_4',30,.2,(0,6,200),xmax=100,curves=('go','mr','mc'),qmark=50,showprice=True,capacity=50,title='De capaciteit kan eerder een grens stellen',note='Bij een capaciteit van 50 kg blijft MO > MK tot de grens. Kies dan q = 50.')
    mono('4.1.3_we',24,.2,(.1,6,80),xmax=50,curves=('go','mr','mc'),qmark=30,showprice=True,title='Uitgewerkt voorbeeld · Coating Mira',note='MO = MK = € 12; de verkoopprijs is P = € 18 per kg.')
    mono('4.1.3_ex_23',20,.1,(0,4,100),xmax=120,curves=('go','mr','mc'),qmark=80,showprice=True,title='De route is al getekend',note='Punt 1 bepaalt q = 80. Punt 2 geeft P = € 12.')
    mono('4.1.3_ex_24',28,.2,(0,8,100),xmax=100,curves=('go','mr','mc'),title='Vul zelf q en P aan')
    mono('4.1.3_ex_26',40,.2,(.1,4,100),xmax=100,curves=('go','mr','mc'),title='Nieuwe gegevens, dezelfde route')
    mono('4.1.3_target',40,.25,(.125,10,200),xmax=80,curves=('go','mr','mc'),title='Doeloefening · Korrels Nova')
    mono('4.1.4_target',32,.2,(.1,8,120),xmax=80,curves=('go','mr','mc'),title='Bron B · KleurFix')
    flow('4.1_overview',[['MO = MK','kandidaat-q'],['Controle','verloop en capaciteit'],['Vraag / GO','verkoopprijs P'],['TO − TK','totale winst']],title='Eén vaste rekenroute',note='De hoogte van het snijpunt van MO en MK is niet de verkoopprijs.')
    # Answer figures mirror the supplied exercise diagrams, now with the required route.
    demand('4.1.1_ans_8',24,.1,240,[(60,'A: (60, 18)'),(120,'B: (120, 12)')],caption='Doeloefening 8 · Prijs en hoeveelheid')
    mono('4.1.2_ans_18',30,.5,xmax=60,curves=('go','mr'),ymin=-30,title='Doeloefening 18 · GO en MO',note='Bij q = 20: P = € 20 en MO = € 10. Tabelstap 20 → 30: gemiddeld € 5 per kg.')
    mono('4.1.3_ans_24',28,.2,(0,8,100),xmax=100,curves=('go','mr','mc'),qmark=50,showprice=True,title='Opgave 24 · q = 50 en P = 18')
    mono('4.1.3_ans_26',40,.2,(.1,4,100),xmax=100,curves=('go','mr','mc'),qmark=60,showprice=True,title='Opgave 26 · q = 60 en P = 28')
    mono('4.1.3_ans_27',22,.2,(0,2,50),xmax=60,curves=('go','mr','mc'),qmark=40,showprice=True,capacity=40,title='Opgave 27 · De capaciteit bindt')
    mono('4.1.3_ans_28',40,.25,(.125,10,200),xmax=80,curves=('go','mr','mc'),qmark=40,showprice=True,title='Doeloefening 28 · Hoeveelheid en prijs',note='q = 40 kg per week; P = € 30 per kg; winst = € 400 per week.')
    mono('4.1.3_ans_28_profit',40,.25,(.125,10,200),xmax=80,curves=('go','gtk'),qmark=40,showprice=True,profit=True,title='Doeloefening 28 · Winstcontrole',note='GTK = € 20 per kg. De rechthoek is 40 × (30 − 20) = € 400 per week.')
    mono('4.1.4_ans_35',32,.2,(.1,8,120),xmax=80,curves=('go','mr','mc'),qmark=40,showprice=True,title='Doeloefening 35 · KleurFix',note='q = 40 kg per week; P = € 24 per kg; MO = MK = € 16 per kg.')
    (ROOT/'QA'/'figure_geometry.json').write_text(json.dumps(LOG,ensure_ascii=False,indent=2))
if __name__=='__main__':all_assets()
