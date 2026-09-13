from pathlib import Path
import math, html, json
import cairosvg
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'_assets'; OUT.mkdir(exist_ok=True)
INK='#183247'; MUTED='#536777'; GRID='#dce4e9'; BLUE='#17688f'; AMBER='#ad601b'; GREEN='#227064'; LIGHT='#f2f6f8'
checks=[]
def esc(s):return html.escape(str(s))
def text(x,y,s,size=17,fill=INK,anchor='start',weight='normal',extra=''):
 return f'<text x="{x:.2f}" y="{y:.2f}" font-family="Lato, DejaVu Sans, sans-serif" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}" {extra}>{esc(s)}</text>'
def line(x1,y1,x2,y2,color=INK,width=2,dash=None):
 d=f' stroke-dasharray="{dash}"' if dash else ''
 return f'<line x1="{x1:.3f}" y1="{y1:.3f}" x2="{x2:.3f}" y2="{y2:.3f}" stroke="{color}" stroke-width="{width}"{d}/>'
def rect(x,y,w,h,fill=LIGHT,stroke='none',rx=5):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}"/>'
def svg_start(h=380):
 return f'<svg xmlns="http://www.w3.org/2000/svg" width="720" height="{h}" viewBox="0 0 720 {h}" role="img"><rect width="720" height="{h}" fill="white"/>'
def save(name,s):
 s+='</svg>'; (OUT/f'{name}.svg').write_text(s)
 cairosvg.svg2png(bytestring=s.encode(),write_to=str(OUT/f'{name}.png'),output_width=1800)
 return name

def graph(name,title,xmax,ymax,curves,xticks=None,yticks=None,xlabel='Hoeveelheid Q (producten per maand)',ylabel='Bedrag (€ per maand)',points=None,profit=None,be=None,capacity=False,notes=None,h=390):
 # Dedicated label reserve on all four sides. Data coordinates are never nudged.
 l,r,t,b=90,665,54,h-73; pw=r-l;ph=b-t
 X=lambda x:l+x/xmax*pw;Y=lambda y:b-y/ymax*ph
 s=svg_start(h)+text(360,25,title,20,anchor='middle',weight='bold')
 xticks=xticks if xticks is not None else [xmax*i/4 for i in range(5)]
 yticks=yticks if yticks is not None else [ymax*i/4 for i in range(5)]
 def num(v):
  return f'{int(v):,}'.replace(',','.') if abs(v-round(v))<1e-8 else f'{v:g}'.replace('.',',')
 for x in xticks:
  s+=line(X(x),t,X(x),b,GRID,1)+text(X(x),b+25,num(x),16,anchor='middle')
 for y in yticks:
  s+=line(l,Y(y),r,Y(y),GRID,1)+text(l-10,Y(y)+5,num(y),16,anchor='end')
 s+=line(l,t-5,l,b)+line(l,b,r+8,b)
 s+=f'<path d="M {l-4} {t+3} L {l} {t-7} L {l+4} {t+3} Z" fill="{INK}"/>'
 s+=f'<path d="M {r+1} {b-4} L {r+11} {b} L {r+1} {b+4} Z" fill="{INK}"/>'
 s+=text((l+r)/2,h-9,xlabel,17,anchor='middle')
 s+=text(24,(t+b)/2,ylabel,17,anchor='middle',extra=f'transform="rotate(-90 24 {(t+b)/2})"')
 for i,c in enumerate(curves):
  col=c.get('color', [AMBER,BLUE,GREEN][i%3]); dash=c.get('dash')
  vals=c.get('points') or [(c.get('xmin',0)+(c.get('xmax',xmax)-c.get('xmin',0))*j/160,c['f'](c.get('xmin',0)+(c.get('xmax',xmax)-c.get('xmin',0))*j/160)) for j in range(161)]
  vals=[(x,y) for x,y in vals if 0<=x<=xmax and 0<=y<=ymax]
  ds=f' stroke-dasharray="{dash}"' if dash else ''
  s+=f'<polyline points="'+ ' '.join(f'{X(x):.3f},{Y(y):.3f}' for x,y in vals)+f'" fill="none" stroke="{col}" stroke-width="3.2"{ds}/>'
  if c.get('dots'):
   for x,y in vals:s+=f'<circle cx="{X(x)}" cy="{Y(y)}" r="4" fill="{col}"/>'
  xlab,ylab=c.get('label_at',vals[-1]); dx,dy=c.get('label_offset',(-8,-9))
  s+=text(X(xlab)+dx,Y(ylab)+dy,c['label'],18,col,anchor=c.get('anchor','end'),weight='bold')
  checks.append({'asset':name,'curve':c['label'],'points':vals,'xmax':xmax,'ymax':ymax,'mapping':[l,r,t,b]})
 if be:
  x,y=be
  s+=line(X(x),b,X(x),Y(y),MUTED,1.3,'5 4')
  s+=f'<circle cx="{X(x)}" cy="{Y(y)}" r="5" fill="{INK}"/>'
  # label uses white backing and is kept away from intersecting curves
  s+=rect(X(x)-65,Y(y)-44,130,26,'white',rx=3)+text(X(x),Y(y)-25,'break-even',16,anchor='middle',weight='bold')
 if profit:
  x,low,high,lab=profit;xp=X(x);a=Y(high);z=Y(low)
  s+=line(xp,a,xp,z,GREEN,2.7)+line(xp-6,a,xp+6,a,GREEN,2)+line(xp-6,z,xp+6,z,GREEN,2)
  dx=profit[4] if len(profit)>4 else 10
  s+=rect(xp+9,(a+z)/2-14,len(lab)*8.8+5,22,'white',rx=2)+text(xp+12,(a+z)/2+5,lab,16,GREEN)
 if points:
  for p in points:
   x,y,lab=p[:3];dx,dy=(p[3],p[4]) if len(p)>3 else (8,-10)
   s+=f'<circle cx="{X(x)}" cy="{Y(y)}" r="4" fill="{INK}"/>'+text(X(x)+dx,Y(y)+dy,lab,16)
 if notes:
  for n in notes:
   x,y,lab=n[:3];s+=text(X(x),Y(y),lab,16,anchor='middle',fill=MUTED)
 if capacity:s+=text(X(xmax)-3,t+20,'capaciteit',15,MUTED,anchor='end')
 return save(name,s)

# Costs in everyday language: production capacity does not create an artificial minimum output.
s=svg_start(270)+text(360,25,'Eén maand, dezelfde werkplaats',21,anchor='middle',weight='bold')
s+=rect(10,55,325,135)+rect(385,55,325,135)
s+=text(30,87,'Huur: € 300 per maand',20,BLUE,weight='bold')+text(30,119,'0, 200 of 400 drinkflessen?',18)+text(30,151,'Het totale huurbedrag blijft € 300.',17)
s+=text(405,87,'Materiaal: € 2 per fles',20,AMBER,weight='bold')+text(405,119,'200 flessen → € 400 materiaal',17)+text(405,151,'400 flessen → € 800 materiaal',17)
s+=text(173,218,'CONSTANTE KOSTEN',18,BLUE,anchor='middle',weight='bold')+text(548,218,'VARIABELE KOSTEN',18,AMBER,anchor='middle',weight='bold')
s+=text(360,253,'Productiecapaciteit: maximaal 600 flessen per maand.',17,anchor='middle')
save('2.1.1_fig_1',s)
graph('2.1.1_fig_2','Meer produceren: twee verschillende reacties',600,1600,[{'label':'TK','f':lambda q:300+2*q,'color':AMBER,'label_offset':(-7,-12)},{'label':'TVK','f':lambda q:2*q,'color':GREEN,'dash':'8 5','label_offset':(-7,-12)},{'label':'TCK','f':lambda q:300,'color':BLUE,'dash':'3 5','label_offset':(-7,-12)}],xticks=[0,200,400,600],yticks=[0,400,800,1200,1600],xlabel='Hoeveelheid Q (flessen per maand)',ylabel='Kosten (€ per maand)',capacity=False,h=330)
graph('2.1.1_fig_3','Dezelfde vaste kosten over meer flessen',600,6,[{'label':'GTK','f':lambda q:300/q+2,'xmin':75,'color':AMBER,'label_offset':(-7,-12)},{'label':'GVK','f':lambda q:2,'xmin':75,'color':GREEN,'dash':'8 5','label_offset':(-7,-12)},{'label':'GCK','f':lambda q:300/q,'xmin':75,'color':BLUE,'dash':'3 5','label_offset':(-7,-12)}],xticks=[0,200,400,600],yticks=[0,1,2,3,4,5,6],xlabel='Hoeveelheid Q (flessen per maand)',ylabel='Gemiddelde kosten (€ per fles)')
# Revenue/profit flow as a precise nondecorative schematic.
s=svg_start(250)
s+=rect(10,18,270,75,'#eaf3f7')+text(145,47,'TO: wat klanten betalen',19,BLUE,anchor='middle',weight='bold')+text(145,76,'prijs × aantal verkochte producten',16,anchor='middle')
s+=text(320,65,'−',34,anchor='middle')+rect(360,18,350,75,'#fbf1e7')+text(535,47,'TK: alle kosten bij elkaar',19,AMBER,anchor='middle',weight='bold')+text(535,76,'constante + variabele kosten',16,anchor='middle')
s+=line(360,103,360,135,MUTED,2)+text(360,133,'↓',22,anchor='middle')
s+=rect(175,151,370,70)+text(360,180,'Winst = TO − TK',24,GREEN,anchor='middle',weight='bold')+text(360,207,'Een negatieve uitkomst betekent verlies.',16,anchor='middle')
save('2.1.2_fig_1',s)
graph('2.1.2_fig_2','Break-even is het snijpunt, winst is een afstand',150,800,[{'label':'TO = 5Q','f':lambda q:5*q,'color':BLUE},{'label':'TK = 250 + 2Q','f':lambda q:250+2*q,'color':AMBER,'dash':'8 5','label_offset':(-7,43)}],xticks=[0,50,100,150],yticks=[0,200,400,600,800],xlabel='Hoeveelheid Q (wafels per dag)',ylabel='TO en TK (€ per dag)',be=(250/3,1250/3),profit=(100,450,500,'€ 50'),notes=[(28,620,'TO < TK: verlies'),(120,120,'TO > TK: winst')])
graph('2.1.2_ex_1','SokkenShop: lees eerst de getekende lijnen',120,800,[{'label':'TO','f':lambda q:6*q,'color':BLUE},{'label':'TK','f':lambda q:180+3*q,'color':AMBER,'dash':'8 5','label_offset':(-7,23)}],xticks=[0,30,60,90,120],yticks=[0,200,400,600,800],xlabel='Hoeveelheid Q (paar sokken per week)',ylabel='TO en TK (€ per week)',be=(60,360),profit=(90,450,540,'€ 90'),h=330)
graph('2.1.2_ex_2','Vul zelf de ontbrekende opbrengstenlijn aan',120,600,[{'label':'TK','f':lambda q:120+q,'color':AMBER,'dash':'8 5'}],xticks=[0,30,60,90,120],yticks=[0,200,400,600],xlabel='Hoeveelheid Q (kaarten per week)',ylabel='TO en TK (€ per week)',h=330)
graph('2.1.2_ex_3','KaartKunst: de aangevulde grafiek',120,600,[{'label':'TO','f':lambda q:4*q,'color':BLUE},{'label':'TK','f':lambda q:120+q,'color':AMBER,'dash':'8 5'}],xticks=[0,30,60,90,120],yticks=[0,200,400,600],xlabel='Hoeveelheid Q (kaarten per week)',ylabel='TO en TK (€ per week)',be=(40,160),profit=(90,210,360,'€ 150'),notes=[(17,500,'verlies'),(88,70,'winst')])
graph('2.1.2_ex_4','PetPret: winst en verlies bij naamplaatjes',100,1000,[{'label':'TO','f':lambda q:10*q,'color':BLUE},{'label':'TK','f':lambda q:250+4*q,'color':AMBER,'dash':'8 5'}],xticks=[0,20,40,60,80,100],yticks=[0,200,400,600,800,1000],xlabel='Hoeveelheid Q (naamplaatjes per maand)',ylabel='TO en TK (€ per maand)',be=(250/6,2500/6),profit=(60,490,600,'€ 110'),notes=[(18,770,'verlies'),(76,130,'winst')])
graph('2.1.2_ex_5','De Korenaar: het volledige grafiekantwoord',1100,1800,[{'label':'TO','f':lambda q:1.5*q,'xmax':1000,'color':BLUE,'label_at':(930,1395),'label_offset':(-10,-12)},{'label':'TK','f':lambda q:500+.8*q,'xmax':1000,'color':AMBER,'dash':'8 5','label_at':(970,1276),'label_offset':(-5,30)}],xticks=[0,250,500,750,1000],yticks=[0,500,1000,1500],xlabel='Hoeveelheid Q (broden per maand)',ylabel='TO en TK (€ per maand)',be=(500/.7,750/.7),profit=(1000,1300,1500,'€ 200'),notes=[(200,1550,'verlies'),(890,300,'winst')])
# Marginal values: table interval, not derivative at the right endpoint.
s=svg_start(250)+text(360,25,'Marginaal gaat over de extra producten',21,anchor='middle',weight='bold')
for x,head,body in [(10,'Eerst','Q = 40; TK = € 260'),(420,'Daarna','Q = 50; TK = € 300')]:
 s+=rect(x,55,290,83)+text(x+145,85,head,18,anchor='middle',weight='bold')+text(x+145,115,body,19,anchor='middle')
s+=text(360,107,'→',35,anchor='middle')+text(360,174,'10 extra producten kosten samen € 40 extra.',20,anchor='middle')+rect(125,191,470,43)+text(360,220,'MK = € 40 ÷ 10 = € 4 per extra product',21,GREEN,anchor='middle',weight='bold')
save('2.1.3_fig_1',s)
graph('2.1.3_fig_2','De totale kosten stijgen steeds sneller',12,240,[{'label':'TK','f':lambda q:80+q*q,'color':AMBER,'label_offset':(-9,-10)}],xticks=[0,4,8,12],yticks=[0,80,160,240],xlabel='Hoeveelheid Q (schalen per week)',ylabel='TK (€ per week)',points=[(4,96,'(4; 96)',-95,-10),(8,144,'(8; 144)',-105,-13),(12,224,'',0,0)],h=350)
# Mixed practice supplied graph.
graph('2.1.4_ex_1','FotoFun: kosten en opbrengsten per feest',120,720,[{'label':'TO','f':lambda q:6*q,'color':BLUE},{'label':'TK','f':lambda q:240+2*q,'color':AMBER,'dash':'8 5'}],xticks=[0,30,60,90,120],yticks=[0,180,360,540,720],xlabel='Hoeveelheid Q (foto’s per feest)',ylabel='TO en TK (€ per feest)')
# One capacity, two menus on different days: no production-range exceptions.
def mixed_graph(name,solved=False):
 curves=[{'label':'TO (beide dagen)','f':lambda q:5*q,'color':BLUE,'label_at':(960,4800),'label_offset':(-10,-11)}, {'label':'TK vrijdag','f':lambda q:1200+2*q,'color':AMBER,'dash':'8 5','label_at':(1000,3200),'label_offset':(-12,25)}, {'label':'TK zaterdag','points':[(700,2600),(800,2900),(900,3250),(1000,3650)],'color':GREEN,'dash':'3 5','label_at':(990,3610),'label_offset':(-5,-14),'dots':True}]
 return graph(name,'SmoothBox: twee festivaldagen, twee menu’s',1000,5500,curves,xticks=[0,200,400,600,800,1000],yticks=[0,1000,2000,3000,4000,5000],xlabel='Hoeveelheid Q (lunchboxen per dag)',ylabel='TO en TK (€ per dag)',be=(400,2000) if solved else None,notes=([(210,3900,'TK zaterdag: alleen de'),(210,3550,'gegeven tabelpunten'),(680,950,'vrijdag: positieve winst bij Q > 400'),(680,580,'groei: € 3 per extra lunchbox')] if solved else [(210,3900,'TK zaterdag: alleen de'),(210,3550,'gegeven tabelpunten')]),h=395)
mixed_graph('2.1.4_ex_2');mixed_graph('2.1.4_ex_3',True)
# A small chapter learning map / formula relationship, no new mathematical operation.
s=svg_start(225)
for x,t1,t2 in [(10,'Totaal','alle producten samen'),(250,'Gemiddeld','per product'),(490,'Marginaal','per extra product')]:
 s+=rect(x,38,220,130)+text(x+110,73,t1,23,anchor='middle',weight='bold')+text(x+110,105,t2,16,anchor='middle')
 vals={'Totaal':'TK en TO','Gemiddeld':'TK / Q en TO / Q','Marginaal':'ΔTK / ΔQ en ΔTO / ΔQ'}
 s+=text(x+110,143,vals[t1],16,anchor='middle',fill=BLUE)
s+=text(360,209,'Vraag eerst: gaat het om alles, per product, of om de extra producten?',17,anchor='middle')
save('2.1.4_fig_1',s)
(OUT/'geometry-data.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2))
print('Assets:',len(list(OUT.glob('*.svg'))),'SVG/PNG pairs')

graph('2.1.4_ex_4','FotoFun: het volledige grafiekantwoord',120,720,[{'label':'TO','f':lambda q:6*q,'color':BLUE},{'label':'TK','f':lambda q:240+2*q,'color':AMBER,'dash':'8 5'}],xticks=[0,30,60,90,120],yticks=[0,180,360,540,720],xlabel='Hoeveelheid Q (foto’s per feest)',ylabel='TO en TK (€ per feest)',be=(60,360),profit=(90,420,540,'€ 120'),notes=[(24,620,'verlies'),(86,95,'winst')])
(OUT/'geometry-data.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2))
