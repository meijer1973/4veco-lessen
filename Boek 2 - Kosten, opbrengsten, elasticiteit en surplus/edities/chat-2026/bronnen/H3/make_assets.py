"""Reproducible, numerically specified SVG/PNG figures for Chapter 2.3.
Run locally with Python 3 and cairosvg. No network or bundled font files.
"""
from pathlib import Path
import html, json, math
import cairosvg
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'_assets'; OUT.mkdir(exist_ok=True)
INK='#183247'; MUTED='#536777'; GRID='#dce4e9'; BLUE='#17688f'; GREEN='#227064'; AMBER='#ad601b'
DATA=[]
def txt(x,y,s,size=18,col=INK,anchor='start',bold=False,extra=''):
 return f'<text x="{x:.3f}" y="{y:.3f}" font-family="Lato, DejaVu Sans, sans-serif" font-size="{size}" fill="{col}" text-anchor="{anchor}" font-weight="{700 if bold else 400}" {extra}>{html.escape(str(s))}</text>'
def line(x1,y1,x2,y2,col=INK,w=2,dash=None):
 return f'<line x1="{x1:.3f}" y1="{y1:.3f}" x2="{x2:.3f}" y2="{y2:.3f}" stroke="{col}" stroke-width="{w}"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>'
def rect(x,y,w,h,col='#f2f6f8',stroke='none',rx=5): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{col}" stroke="{stroke}"/>'
def arrow(x1,y1,x2,y2,col=MUTED):
 a=math.atan2(y2-y1,x2-x1); z=8
 return line(x1,y1,x2,y2,col,2)+f'<path d="M{x2-z*math.cos(a-.5)},{y2-z*math.sin(a-.5)} L{x2},{y2} L{x2-z*math.cos(a+.5)},{y2-z*math.sin(a+.5)}" stroke="{col}" stroke-width="2" fill="none"/>'
def start(h,title): return f'<svg xmlns="http://www.w3.org/2000/svg" width="720" height="{h}" viewBox="0 0 720 {h}" role="img"><title>{html.escape(title)}</title><rect width="720" height="{h}" fill="white"/>'
def save(name,s,meta):
 s+='</svg>'; (OUT/f'{name}.svg').write_text(s,encoding='utf-8')
 cairosvg.svg2png(bytestring=s.encode(),write_to=str(OUT/f'{name}.png'),output_width=1800)
 DATA.append({'asset':name,**meta})
def n(v): return f'{v:g}'.replace('.',',')
def area(points): return abs(sum(x*y2-y*x2 for (x,y),(x2,y2) in zip(points,points[1:]+points[:1])))/2

def market(name,a,b,c=None,d=None,p=None,q=None,cs=False,ps=False,dwl=False,eq=False,split=False,
           xmax=None,ymax=None,stepx=10,stepy=10,title='',unit='producten',priceunit='product',axes_only=False,demand_only=False,
           mark_values=True,eq_guides=False):
 """P_d=a-bQ; P_s=c+dQ. All polygons and intersections derive from these functions."""
 if xmax is None:xmax=a/b
 if ymax is None:ymax=max(a, (c+d*xmax) if c is not None else 0)
 H=300 if name == "2.3.1_ex_1" else 360
 L,R,T,B=87.,672.,48.,float(H-88)
 X=lambda x:L+x/xmax*(R-L); Y=lambda y:B-y/ymax*(B-T)
 demand=lambda x:a-b*x
 supply=lambda x:c+d*x
 qe=(a-c)/(b+d) if c is not None else None
 pe=demand(qe) if qe is not None else None
 if q is None and p is not None:q=(a-p)/b
 s=start(H,title); s+=txt(360,24,title,20,anchor='middle',bold=True)
 for x in range(0,int(xmax)+1,stepx):
  s+=line(X(x),T,X(x),B,GRID,1)+txt(X(x),B+24,str(x),17,anchor='middle')
 for y in range(0,int(ymax)+1,stepy):
  s+=line(L,Y(y),R,Y(y),GRID,1)+txt(L-12,Y(y)+6,str(y),17,anchor='end')
 polygons=[]; labels=[]
 def poly(points,fill,label,col,label_at=None):
  nonlocal s
  pp=' '.join(f'{X(x):.3f},{Y(y):.3f}' for x,y in points)
  s+=f'<polygon points="{pp}" fill="{fill}" stroke="{col}" stroke-width="0.6"/>'
  # Centroid of polygon, computed exactly; area recorded independently.
  cross=[x*y2-x2*y for (x,y),(x2,y2) in zip(points,points[1:]+points[:1])]
  denom=3*sum(cross)
  cx=sum((x+x2)*k for ((x,y),(x2,y2)),k in zip(zip(points,points[1:]+points[:1]),cross))/denom
  cy=sum((y+y2)*k for ((x,y),(x2,y2)),k in zip(zip(points,points[1:]+points[:1]),cross))/denom
  if label_at:cx,cy=label_at
  if label:
   if label=='verlies' and (X(qe)-X(q))<95:
    # Narrow loss triangles use an external labelled leader, never an overflowing label.
    lx=min(R-45,X(qe)+100);ly=Y(pe)-70
    s+=txt(lx,ly,label,18,col,anchor='middle',bold=True)
    s+=arrow(lx-20,ly+7,X(cx)+4,Y(cy)-3,col)
   else:
    labels.append(rect(X(cx)-25,Y(cy)-17,50,29,fill,rx=2)+txt(X(cx),Y(cy)+6,label,20,col,anchor='middle',bold=True))
  polygons.append({'label':label,'points':points,'area':area(points),'label_at':[cx,cy]})
 if cs:poly([(0,p),(0,a),(q,demand(q)),(q,p)],'#dcecf4','CS',BLUE)
 if ps:poly([(0,c),(0,p),(q,p),(q,supply(q))],'#dceee4','PS',GREEN)
 if dwl:poly([(q,demand(q)),(qe,pe),(q,supply(q))],'#f4dcc1','verlies',AMBER)
 if not axes_only:
  end=min(xmax,a/b); s+=line(X(0),Y(a),X(end),Y(demand(end)),BLUE,3)
  vl=min(end*.90,xmax*.90)
  s+=txt(X(vl),Y(demand(vl))-12,'V',20,BLUE,anchor='end',bold=True)
  if c is not None and not demand_only:
   end=min(xmax,(ymax-c)/d) if d else xmax
   s+=line(X(0),Y(c),X(end),Y(supply(end)),GREEN,3)
   al=end*.96
   s+=txt(X(al),Y(supply(al))-12,'A = MK',19,GREEN,anchor='end',bold=True)
 if p is not None:
  s+=line(L,Y(p),R,Y(p),INK,1.8,'8 5')
  labels.append(rect(R-86,Y(p)-13,83,25,'white',rx=3)+txt(R-8,Y(p)+6,'P = '+n(p),17,INK,anchor='end',bold=True))
 if q is not None and mark_values:
  top=max(demand(q),p or 0)
  s+=line(X(q),Y(top),X(q),B,MUTED,1.7,'5 4')
  # Q-label on an inset strip below tick labels, avoids tick collisions.
  s+=txt(X(q),B+47,'Q = '+n(q),17,MUTED,anchor='middle',bold=True)
 if split and q is not None:
  s+=line(L,Y(demand(q)),X(q),Y(demand(q)),BLUE,1.5,'4 4')
  s+=line(L,Y(supply(q)),X(q),Y(supply(q)),GREEN,1.5,'4 4')
  for val,col in [(demand(q),BLUE),(supply(q),GREEN)]:
   s+=txt(X(q)+9,Y(val)+(5 if col==BLUE else 17),n(val),17,col,bold=True)
 if eq:
  s+=f'<circle cx="{X(qe)}" cy="{Y(pe)}" r="4" fill="{INK}"/>'
  labels.append(rect(X(qe)-10,Y(pe)-34,20,24,'white',rx=2)+txt(X(qe),Y(pe)-15,'E',18,anchor='middle',bold=True))
  if eq_guides:
   s+=line(X(qe),Y(pe),X(qe),B,MUTED,1,'3 4')+line(L,Y(pe),X(qe),Y(pe),MUTED,1,'3 4')
 s+=''.join(labels)
 s+=line(L,T-2,L,B,INK,2)+line(L,B,R+4,B,INK,2)
 s+=txt(24,(T+B)/2,'P (€ per '+priceunit+')',18,anchor='middle',extra=f'transform="rotate(-90 24 {(T+B)/2})"')
 s+=txt(380,H-9,'Q ('+unit+')',18,anchor='middle')
 save(name,s,{'type':'market','a':a,'b':b,'c':c,'d':d,'price':p,'quantity':q,'qe':qe,'pe':pe,
              'xmax':xmax,'ymax':ymax,'plot':[L,R,T,B],'polygons':polygons,'axes_only':axes_only})

# Individueel voordeel: proportional money segments, not decorative blocks.
s=start(214,'Je betaalt minder dan je maximaal over hebt')
s+=txt(360,24,'Een kaartje: bereid te betalen € 30, prijs € 20',21,anchor='middle',bold=True)
X=lambda v:80+v*18
s+=rect(80,73,360,45,'#e3e9ed',rx=0)+rect(440,73,180,45,'#dcecf4',rx=0)
s+=txt(260,101,'betaald: € 20',20,anchor='middle',bold=True)+txt(530,101,'CS: € 10',20,BLUE,anchor='middle',bold=True)
for v in [0,20,30]:s+=line(X(v),65,X(v),127,MUTED,1.3)+txt(X(v),150,'€ '+str(v),18,anchor='middle')
s+=txt(360,190,'Voordeel voor de koper = € 30 − € 20 = € 10',21,BLUE,anchor='middle',bold=True)
save('2.3.1_fig_1',s,{'type':'surplus_bar','wtp':30,'price':20,'cs':10,'pixels_per_euro':18})
market('2.3.1_fig_2',30,.5,p=10,cs=True,stepx=10,stepy=5,title='Het voordeel van alle kopers samen',unit='kaartjes',priceunit='kaartje')
market('2.3.1_fig_3',30,.5,p=10,cs=False,stepx=10,stepy=5,title='Van twee snijpunten naar de gevraagde hoeveelheid',unit='kaartjes',priceunit='kaartje')
market('2.3.1_we_1',20,.25,p=10,cs=True,stepx=20,stepy=5,title='Escaperoom: Q = 40 en CS = € 200',unit='tickets',priceunit='ticket')
market('2.3.1_ex_1',24,.4,p=8,cs=True,stepx=10,stepy=4,title='Klimhal: lees eerst het gearceerde gebied',unit='kaartjes',priceunit='kaartje')
market('2.3.1_ex_2',18,.3,axes_only=True,stepx=10,stepy=3,title='Museumavond: voeg lijnen en CS toe',unit='kaartjes',priceunit='kaartje')
# Correct solution graphs are supplied only in the answer book.
market('2.3.1_ans_4',18,.3,p=6,cs=True,stepx=10,stepy=3,title='Museumavond: Q = 40 en CS = € 240',unit='kaartjes',priceunit='kaartje')
market('2.3.1_ans_6',18,.2,p=8,cs=True,xmax=90,stepx=10,stepy=3,title='Zwemkaartjes: Q = 50 en CS = € 250',unit='kaartjes',priceunit='kaartje')
market('2.3.1_ans_8',50,.5,p=20,cs=True,stepx=20,stepy=10,title='Concertkaartjes: Q = 60 en CS = € 900',unit='kaartjes',priceunit='kaartje')

s=start(230,'Eén transactie, twee voordelen')
s+=txt(360,26,'Een drinkfles: betalingsbereidheid € 50, prijs € 35, MK € 20',19,anchor='middle',bold=True)
X=lambda v:60+v*12
for x,w,col,lab in [(60,240,'#e3e9ed','kosten: € 20'),(300,180,'#dceee4','PS: € 15'),(480,180,'#dcecf4','CS: € 15')]:
 s+=rect(x,78,w,46,col,rx=0)+txt(x+w/2,108,lab,20,anchor='middle',bold=True)
for v in [0,20,35,50]:s+=line(X(v),68,X(v),133,MUTED,1)+txt(X(v),158,'€ '+str(v),18,anchor='middle')
s+=txt(360,203,'Totaal voordeel = € 50 − € 20 = € 30',22,anchor='middle',bold=True)
save('2.3.2_fig_1',s,{'type':'split_benefit','wtp':50,'price':35,'mc':20,'cs':15,'ps':15,'total':30,'pixels_per_euro':12})
market('2.3.2_fig_2',40,1,10,.5,p=20,q=20,ps=True,eq=True,stepx=10,stepy=10,title='Posters: PS ligt boven de aanbodlijn',unit='posters',priceunit='poster')
market('2.3.2_fig_3',40,1,10,.5,p=20,q=20,cs=True,ps=True,eq=True,stepx=10,stepy=10,title='Hetzelfde evenwicht: CS + PS = TS',unit='posters',priceunit='poster')
market('2.3.2_we_1',24,.5,4,.5,p=14,q=20,cs=True,ps=True,eq=True,xmax=40,ymax=24,stepx=10,stepy=4,title='Notitieboeken: evenwicht bij Q = 20',unit='notitieboeken',priceunit='notitieboek')
market('2.3.2_ex_1',30,1,6,.5,p=14,q=16,cs=True,ps=True,eq=True,stepx=5,stepy=5,title='Bloemenbossen: lees de twee surplusgebieden',unit='bossen',priceunit='bos')
market('2.3.2_ex_2',32,.5,8,.5,stepx=8,stepy=8,title='Sporthanddoeken: markeer zelf het evenwicht',unit='handdoeken',priceunit='handdoek')
market('2.3.2_ex_3',36,.5,6,.5,stepx=12,stepy=6,title='Koffiebekers: gebruik de geleverde lijnen',unit='bekers',priceunit='beker')
market('2.3.2_ex_4',50,.5,5,.25,stepx=20,stepy=10,title='Concertkaartjes: basisgrafiek bij de doeloefening',unit='kaartjes',priceunit='kaartje')
market('2.3.2_ans_4',32,.5,8,.5,p=20,q=24,cs=True,ps=True,eq=True,stepx=8,stepy=8,title='Sporthanddoeken: CS = PS = € 144',unit='handdoeken',priceunit='handdoek')
market('2.3.2_ans_6',36,.5,6,.5,p=21,q=30,cs=True,ps=True,eq=True,stepx=12,stepy=6,title='Koffiebekers: CS = PS = € 225',unit='bekers',priceunit='beker')
market('2.3.2_ans_8',50,.5,5,.25,p=20,q=60,cs=True,ps=True,eq=True,stepx=20,stepy=10,title='Concertkaartjes: CS = € 900; PS = € 450',unit='kaartjes',priceunit='kaartje')

market('2.3.3_fig_1',40,1,10,.5,p=22,q=12,eq=True,stepx=10,stepy=10,title='Posters: een boekingsgrens van 12',unit='posters',priceunit='poster')
market('2.3.3_fig_2',40,1,10,.5,p=22,q=12,cs=True,ps=True,split=True,eq=True,stepx=10,stepy=10,title='Rechthoeken en driehoeken: stop bij Q = 12',unit='posters',priceunit='poster')
market('2.3.3_fig_3',40,1,10,.5,p=22,q=12,dwl=True,eq=True,stepx=10,stepy=10,title='Gemiste voordelen: het welvaartsverlies',unit='posters',priceunit='poster')
s=start(233,'Een extra transactie zonder nadeel voor anderen')
s+=txt(360,25,'De 13e poster kan nog worden verhandeld',21,anchor='middle',bold=True)
for x,title,calc,col in [(8,'Nieuwe koper','€ 27 − € 22 = € 5',BLUE),(380,'Nieuwe verkoper','€ 22 − € 16,50 = € 5,50',GREEN)]:
 s+=rect(x,48,332,96)+txt(x+166,77,title,20,col,anchor='middle',bold=True)+txt(x+166,116,calc,20,anchor='middle',bold=True)
s+=arrow(174,150,286,177)+arrow(546,150,434,177)
s+=rect(65,180,590,41,'#eef5f0')+txt(360,207,'Bestaande transacties blijven ongewijzigd',21,GREEN,anchor='middle',bold=True)
save('2.3.3_fig_4',s,{'type':'pareto_trade','q':13,'wtp':27,'price':22,'mc':16.5,'buyer_gain':5,'seller_gain':5.5,'existing_unchanged':True})
market('2.3.3_we_1',30,1,6,1,p=20,q=8,cs=True,ps=True,split=True,eq=True,xmax=24,ymax=30,stepx=4,stepy=5,title='Workshop: 8 boekingen in plaats van 12',unit='plaatsen',priceunit='plaats')
market('2.3.3_we_2',30,1,6,1,p=20,q=8,dwl=True,eq=True,xmax=24,ymax=30,stepx=4,stepy=5,title='Workshop: welvaartsverlies van € 16',unit='plaatsen',priceunit='plaats')
market('2.3.3_ex_1',24,.5,4,.5,p=14,q=12,cs=True,ps=True,split=True,eq=True,xmax=40,ymax=24,stepx=10,stepy=4,title='Zaalplaatsen: steun bij het opsplitsen',unit='plaatsen',priceunit='plaats')
market('2.3.3_ex_2',30,.5,6,.5,p=20,q=16,eq=True,xmax=48,ymax=30,stepx=8,stepy=5,title='Kajaks: markeer zelf het gemiste surplus',unit='verhuurbeurten',priceunit='verhuurbeurt')
market('2.3.3_ex_3',40,1,10,1,p=26,q=10,eq=True,xmax=30,ymax=40,stepx=5,stepy=5,title='Schilderworkshop: onafhankelijke oefening',unit='plaatsen',priceunit='plaats')
market('2.3.3_ex_4',50,.5,5,.25,p=25,q=40,eq=True,stepx=20,stepy=10,title='Concertkaartjes: basisgrafiek bij de doeloefening',unit='kaartjes',priceunit='kaartje')
market('2.3.3_ans_4',30,.5,6,.5,p=20,q=16,cs=True,ps=True,dwl=True,split=True,eq=True,xmax=48,ymax=30,stepx=8,stepy=5,title='Kajaks: TS = € 256; verlies = € 32',unit='verhuurbeurten',priceunit='verhuurbeurt')
market('2.3.3_ans_5',40,1,10,1,p=26,q=10,cs=True,ps=True,dwl=True,split=True,eq=True,xmax=30,ymax=40,stepx=5,stepy=5,title='Schilderworkshop: TS = € 200; verlies = € 25',unit='plaatsen',priceunit='plaats')
market('2.3.3_ans_6',50,.5,5,.25,p=25,q=40,cs=True,ps=True,dwl=True,split=True,eq=True,stepx=20,stepy=10,title='Concertkaartjes: CS = PS = € 600; verlies = € 150',unit='kaartjes',priceunit='kaartje')

market('2.3.4_ex_1',48,1,12,.5,p=26,q=16,eq=False,stepx=8,stepy=8,title='Plantenmarkt: twee situaties vergelijken',unit='planten',priceunit='plant')
market('2.3.4_ex_2',80,1,20,.5,stepx=10,stepy=10,title='Huurfietsen: basisgrafiek bij de doeloefening',unit='huurfietsen',priceunit='huurfiets')
market('2.3.4_ans_2',48,1,12,.5,p=26,q=16,cs=True,ps=True,dwl=True,split=True,eq=True,stepx=8,stepy=8,title='Plantenmarkt: TS = € 384; verlies = € 48',unit='planten',priceunit='plant')
market('2.3.4_ans_3',80,1,20,.5,p=45,q=30,cs=True,ps=True,dwl=True,split=True,eq=True,stepx=10,stepy=10,title='Huurfietsen: TS = € 1.125; verlies = € 75',unit='huurfietsen',priceunit='huurfiets')
s=start(227,'De hele route in vier stappen')
for i,(head,body,col) in enumerate([('1 · Hoeveelheid','Wie handelt er echt?',MUTED),('2 · Gebieden','CS boven P; PS onder P',BLUE),('3 · Berekenen','Bereken delen; tel daarna op',GREEN),('4 · Beoordelen','Efficiënt?; Ook eerlijk?',AMBER)]):
 x=4+i*181
 s+=rect(x,45,169,125)+txt(x+84.5,77,head,19,col,anchor='middle',bold=True)
 for j,word in enumerate(body.split('; ')):
  s+=txt(x+84.5,112+j*25,word,16,anchor='middle')
s+=txt(360,211,'Welvaartsverlies = maximaal TS − werkelijk TS',22,anchor='middle',bold=True)
save('2.3.4_fig_1',s,{'type':'chapter_route','stages':['actual_quantity','areas','calculation','interpretation']})
(OUT/'geometry-data.json').write_text(json.dumps(DATA,ensure_ascii=False,indent=2),encoding='utf-8')
print('Created',len(DATA),'SVG/PNG pairs.')
