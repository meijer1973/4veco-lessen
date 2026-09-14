"""Create numerically controlled SVG/PNG teaching figures. No network required.
Fonts are resolved from the host system and are not distributed in this package.
"""
from pathlib import Path
import html,json,math
import cairosvg
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'_assets';OUT.mkdir(exist_ok=True)
INK='#183247';MUTED='#536777';GRID='#dce4e9';BLUE='#17688f';AMBER='#ad601b';GREEN='#227064';LIGHT='#f2f6f8'
DATA=[]
def text(x,y,s,size=18,fill=INK,anchor='start',weight='normal',extra=''):
 return f'<text x="{x:.3f}" y="{y:.3f}" font-family="Lato, DejaVu Sans, sans-serif" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}" {extra}>{html.escape(str(s))}</text>'
def line(x1,y1,x2,y2,c=INK,w=2,dash=None):
 return f'<line x1="{x1:.3f}" y1="{y1:.3f}" x2="{x2:.3f}" y2="{y2:.3f}" stroke="{c}" stroke-width="{w}"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>'
def rect(x,y,w,h,fill=LIGHT,stroke='none',rx=6):return f'<rect x="{x:.3f}" y="{y:.3f}" width="{w:.3f}" height="{h:.3f}" rx="{rx}" fill="{fill}" stroke="{stroke}"/>'
def arrow(x1,y1,x2,y2,c=MUTED,w=2):
 a=math.atan2(y2-y1,x2-x1);z=9
 x3=x2-z*math.cos(a-.45);y3=y2-z*math.sin(a-.45)
 x4=x2-z*math.cos(a+.45);y4=y2-z*math.sin(a+.45)
 return line(x1,y1,x2,y2,c,w)+f'<path d="M{x3:.3f},{y3:.3f} L{x2:.3f},{y2:.3f} L{x4:.3f},{y4:.3f}" fill="none" stroke="{c}" stroke-width="{w}"/>'
def start(h,title):return f'<svg xmlns="http://www.w3.org/2000/svg" width="720" height="{h}" viewBox="0 0 720 {h}" role="img"><title>{html.escape(title)}</title><rect width="720" height="{h}" fill="white"/>'
def save(name,s,meta=None):
 s+='</svg>';(OUT/f'{name}.svg').write_text(s,encoding='utf-8');cairosvg.svg2png(bytestring=s.encode(),write_to=str(OUT/f'{name}.png'),output_width=1800)
 if meta:DATA.append({'asset':name,**meta})

# 2.2.1: a single quantitative axis, common scale for all percentage bars.
h=300;s=start(h,'Dezelfde prijsstijging, verschillende hoeveelheidsreacties')
s+=text(360,23,'Vergelijk procenten, niet alleen aantallen',21,anchor='middle',weight='bold')
X=lambda v:490+v*10
for v in [-20,-10,0,10]:
 s+=line(X(v),48,X(v),258,GRID,1)+text(X(v),282,('+' if v>0 else '')+str(v)+'%',16,anchor='middle')
s+=line(X(0),48,X(0),258,MUTED,1.5)
for y,name,role,v,col in [(72,'RolVast','P',10,BLUE),(115,'','Qv',-5,GREEN),(193,'SpringVrij','P',10,BLUE),(236,'','Qv',-20,GREEN)]:
 if name:s+=text(12,y+5,name,19,weight='bold')
 s+=text(228,y+5,role,18,anchor='end')
 a,b=sorted([X(0),X(v)]);s+=rect(a,y-13,b-a,24,col,rx=2)
 s+=text(X(v)+(10 if v>0 else -10),y+5,('+' if v>0 else '')+str(v)+'%',18,col,anchor='start' if v>0 else 'end',weight='bold')
save('2.2.1_fig_1',s,{'type':'percentage_bars','x_origin':490,'pixels_per_percent':10,'values':[10,-5,10,-20],'contexts':{'RolVast':[10,11,200,190],'SpringVrij':[10,11,200,160]}})

s=start(237,'Van twee veranderingen naar Ev')
for x,title,calc,result,col in [(5,'Prijs: € 10 → € 11','(11 − 10) / 10 × 100%','+10%',BLUE),(380,'Qv: 200 → 190','(190 − 200) / 200 × 100%','−5%',GREEN)]:
 s+=rect(x,8,335,112)+text(x+167.5,36,title,20,anchor='middle',weight='bold')+text(x+167.5,66,calc,18,anchor='middle')+text(x+167.5,101,result,24,col,anchor='middle',weight='bold')
s+=arrow(175,125,303,157)+arrow(546,125,417,157)
s+=rect(115,164,490,56,'#eaf3f7')+text(360,199,'Ev = −5% / +10% = −0,5',25,BLUE,anchor='middle',weight='bold')
save('2.2.1_fig_2',s,{'type':'ratio_flow','old_price':10,'new_price':11,'old_quantity':200,'new_quantity':190,'ev':-.5})

s=start(200,'De indeling gebruikt de absolute waarde')
s+=text(360,25,'Kijk voor de indeling naar |Ev|',21,anchor='middle',weight='bold')
X=lambda v:65+v*200
s+=rect(X(0),65,200,42,'#eaf3f7',rx=0)+rect(X(1),65,400,42,'#eef5f0',rx=0)
s+=line(65,107,675,107,INK,2)
for v in [0,1,2,3]:s+=line(X(v),101,X(v),115,INK,2)+text(X(v),139,str(v),18,anchor='middle')
s+=line(X(1),55,X(1),116,AMBER,2)+text(X(1),50,'grens 1',17,AMBER,anchor='middle',weight='bold')
s+=text(165,92,'inelastisch',18,BLUE,anchor='middle',weight='bold')+text(465,92,'elastisch',18,GREEN,anchor='middle',weight='bold')
s+=text(165,171,'Ev = −0,5 → |Ev| = 0,5',17,anchor='middle')+text(475,171,'Ev = −2 → |Ev| = 2',17,anchor='middle')
save('2.2.1_fig_3',s,{'type':'absolute_value_scale','range':[0,3],'threshold':1,'origin':65,'pixels_per_unit':200,'examples':[-.5,-2]})

# 2.2.2: identical axis scales; rectangle areas exactly equal P times Q.
s=start(300,'Omzet is P maal Q in een prijs-hoeveelheidsdiagram')
meta=[]
for offset,p,q,label in [(0,10,100,'Vóór: P = € 10; Q = 100'),(365,11,95,'Na: P = € 11; Q = 95')]:
 l=offset+53;r=offset+338;t=49;b=224
 X=lambda v:l+v/110*(r-l);Y=lambda v:b-v/12*(b-t)
 s+=text(offset+180,24,label,18,anchor='middle',weight='bold')
 for v in [0,50,100]:s+=line(X(v),t,X(v),b,GRID,1)+text(X(v),b+22,str(v),15,anchor='middle')
 for v in [0,5,10]:s+=line(l,Y(v),r,Y(v),GRID,1)+text(l-9,Y(v)+5,str(v),15,anchor='end')
 s+=rect(l,Y(p),X(q)-l,b-Y(p),'#d8eaf2',BLUE,rx=0)
 # Grid remains subtly visible, labels inside the real rectangle.
 s+=line(l,t,l,b,INK,2)+line(l,b,r,b,INK,2)
 s+=text((l+X(q))/2,(b+Y(p))/2-2,'TO',20,BLUE,anchor='middle',weight='bold')
 s+=text((l+X(q))/2,(b+Y(p))/2+27,'€ '+f'{p*q:,.0f}'.replace(',','.'),24,BLUE,anchor='middle',weight='bold')
 s+=text(offset+185,282,'Q (kaartjes per dag)',16,anchor='middle')
 s+=text(offset+16,138,'P (€ per kaartje)',16,anchor='middle',extra=f'transform="rotate(-90 {offset+16} 138)"')
 meta.append({'p':p,'q':q,'revenue':p*q,'plot':[l,r,t,b],'rectangle':[l,Y(p),X(q)-l,b-Y(p)],'xmax':110,'ymax':12})
save('2.2.2_fig_1',s,{'type':'revenue_rectangles','panels':meta})

s=start(231,'Twee krachten bij een kleine prijsstijging')
s+=text(360,22,'Bij een kleine prijsstijging',21,anchor='middle',weight='bold')
for x,lab,qtxt,end,col in [(6,'Prijsinelastische vraag','Q daalt relatief weinig','TO stijgt',BLUE),(376,'Prijselastische vraag','Q daalt relatief veel','TO daalt',AMBER)]:
 s+=rect(x,42,337,175,LIGHT)+text(x+168.5,70,lab,19,col,anchor='middle',weight='bold')
 s+=text(x+168.5,104,'Prijs per product stijgt',18,anchor='middle')+text(x+168.5,133,qtxt,18,anchor='middle')
 s+=arrow(x+168.5,143,x+168.5,164,col)
 s+=text(x+168.5,195,end,24,col,anchor='middle',weight='bold')
save('2.2.2_fig_2',s,{'type':'conceptual_local_rule','small_price_increase':{'inelastic':'revenue_up','elastic':'revenue_down'}})

s=start(186,'Omzetverandering ten opzichte van de oude omzet')
for x,lab,amount in [(5,'Oud','€ 1.000'),(460,'Nieuw','€ 1.045')]:
 s+=rect(x,12,255,83)+text(x+127.5,39,lab,18,anchor='middle',weight='bold')+text(x+127.5,76,amount,28,BLUE,anchor='middle',weight='bold')
s+=arrow(275,56,443,56,BLUE,2.5)+text(359,42,'+ € 45',20,BLUE,anchor='middle',weight='bold')
s+=rect(106,117,508,53,'#eef5f0')+text(360,151,'€ 45 / € 1.000 × 100% = +4,5%',23,GREEN,anchor='middle',weight='bold')
save('2.2.2_we_1',s,{'type':'revenue_change','old':1000,'new':1045,'delta':45,'percentage':4.5})

# 2.2.3: meanings and separate ceteris-paribus scenarios.
s=start(226,'Drie oorzaken, drie elasticiteiten')
s+=text(360,24,'Wat verandert er?',21,anchor='middle',weight='bold')
for x,head,var,sym,col in [(5,'Eigen prijs','P','Ev',BLUE),(250,'Inkomen','Y','Ei',GREEN),(495,'Prijs ander goed','Pz','Ek',AMBER)]:
 s+=rect(x,44,220,110,LIGHT)+text(x+110,74,head,18,anchor='middle',weight='bold')+text(x+110,103,var,21,col,anchor='middle')+text(x+110,136,sym,28,col,anchor='middle',weight='bold')
 s+=arrow(x+110,158,x+110,179,col)
s+=rect(103,186,514,31,'#eaf3f7')+text(360,208,'Steeds: de procentuele reactie van Qv in de teller',17,BLUE,anchor='middle')
save('2.2.3_fig_1',s,{'type':'elasticity_family','denominators':{'Ev':'own_price','Ei':'income','Ek':'other_price'}})

s=start(282,'Dezelfde inkomensstijging, drie vraagreacties')
s+=text(360,24,'Het inkomen stijgt in alle drie gevallen met 10%',21,anchor='middle',weight='bold')
X=lambda v:350+v*12
for v in [-5,0,5,10,15,20]:s+=line(X(v),46,X(v),228,GRID,1)+text(X(v),255,('+' if v>0 else '')+str(v)+'%',15,anchor='middle')
s+=line(X(0),46,X(0),228,MUTED,1.5)
for y,lab,ev,val,col in [(76,'Inferieur goed','Ei = −0,5',-5,AMBER),(142,'Normaal goed','Ei = +0,5',5,BLUE),(208,'Luxegoed','Ei = +2',20,GREEN)]:
 s+=text(12,y,lab,19,weight='bold')+text(12,y+23,ev,17,col)
 a,b=sorted([X(0),X(val)]);s+=rect(a,y-14,b-a,27,col,rx=2)
 s+=text(X(val)+(10 if val>0 else -10),y+6,('+' if val>0 else '')+str(val)+'%',18,col,anchor='start' if val>0 else 'end',weight='bold')
save('2.2.3_fig_2',s,{'type':'income_response_bars','income_percentage':10,'demand_percentages':[-5,5,20],'ei':[-.5,.5,2],'origin':350,'pixels_per_percent':12})

s=start(268,'Kruislingse elasticiteit benoemt twee goederen')
for y,price,demand,eq,col in [(9,'Busprijs +10%','Treinvraag +6%','Ek = +0,6  ·  substituten',BLUE),(144,'Printerprijs +10%','Inktvraag −4%','Ek = −0,4  ·  complementen',AMBER)]:
 s+=rect(6,y,273,65,LIGHT)+text(142.5,y+39,price,20,anchor='middle',weight='bold')
 s+=rect(439,y,275,65,LIGHT)+text(576.5,y+39,demand,20,anchor='middle',weight='bold')
 s+=arrow(287,y+32,429,y+32,col,2.5)
 s+=text(360,y+96,eq,22,col,anchor='middle',weight='bold')
save('2.2.3_fig_3',s,{'type':'cross_elasticity','cases':[{'denominator_good':'bus','price_percentage':10,'numerator_good':'train','demand_percentage':6,'ek':.6},{'denominator_good':'printer','price_percentage':10,'numerator_good':'ink','demand_percentage':-4,'ek':-.4}]})

s=start(264,'Elk gegeven gaat naar zijn eigen term')
s+=text(360,24,'Qx = 200 − 5Px + 2Pz + 0,01Y',23,anchor='middle',weight='bold')
for x,head,cal,col in [(5,'Px = 10','−5 × 10 = −50',BLUE),(250,'Pz = 15','+2 × 15 = +30',AMBER),(495,'Y = 20.000','+0,01 × 20.000 = +200',GREEN)]:
 s+=rect(x,53,220,97,LIGHT)+text(x+110,84,head,21,col,anchor='middle',weight='bold')+text(x+110,121,cal,17,anchor='middle')
 s+=arrow(x+110,156,360,188,col,1.8)
s+=rect(92,193,536,57,'#eaf3f7')+text(360,228,'200 − 50 + 30 + 200 = 380',24,BLUE,anchor='middle',weight='bold')
save('2.2.3_fig_4',s,{'type':'function_substitution','intercept':200,'coefficients':[-5,2,.01],'inputs':[10,15,20000],'contributions':[-50,30,200],'output':380})

s=start(266,'Twee aparte scenario’s vanaf dezelfde basis')
s+=rect(210,7,300,70,'#eaf3f7')+text(360,34,'Beginsituatie',20,BLUE,anchor='middle',weight='bold')+text(360,62,'Qx = 380',24,BLUE,anchor='middle',weight='bold')
s+=arrow(265,81,172,116,GREEN)+arrow(455,81,548,116,AMBER)
s+=rect(4,123,335,133,LIGHT)+rect(381,123,335,133,LIGHT)
s+=text(171.5,153,'Alleen Y → 22.000',21,GREEN,anchor='middle',weight='bold')+text(171.5,182,'Px = 10; Pz = 15',18,anchor='middle')+text(171.5,220,'Qx = 400',26,GREEN,anchor='middle',weight='bold')
s+=text(548.5,153,'Alleen Pz → 20',21,AMBER,anchor='middle',weight='bold')+text(548.5,182,'Px = 10; Y = 20.000',18,anchor='middle')+text(548.5,220,'Qx = 390',26,AMBER,anchor='middle',weight='bold')
save('2.2.3_fig_5',s,{'type':'separate_scenarios','function':'200-5*Px+2*Pz+.01*Y','base':{'Px':10,'Pz':15,'Y':20000,'Qx':380},'scenarios':[{'Px':10,'Pz':15,'Y':22000,'Qx':400},{'Px':10,'Pz':20,'Y':20000,'Qx':390}]})

# 2.2.4: display simultaneous observations, without asserting causal arrows.
s=start(236,'Vier waarnemingen in dezelfde maand')
s+=text(360,24,'Vier waarnemingen in dezelfde maand',21,anchor='middle',weight='bold')
for x,y,title,value,col in [(5,48,'Prijs','+10%',BLUE),(375,48,'Gevraagde hoeveelheid','+20%',GREEN),(5,141,'Inkomen','stijgt',AMBER),(375,141,'Reclame','grote campagne',MUTED)]:
 s+=rect(x,y,340,78,LIGHT)+text(x+170,y+29,title,18,anchor='middle',weight='bold')+text(x+170,y+61,value,24,col,anchor='middle',weight='bold')
save('2.2.4_fig_1',s,{'type':'simultaneous_observations','price_percentage':10,'quantity_percentage':20,'income':'increases','advertising':'campaign','causal_attribution':None})

s=start(252,'Kies de noemer, behoud de betekenis')
s+=rect(125,7,470,48,'#eaf3f7')+text(360,37,'Teller: %Δ van de gevraagde hoeveelheid',21,BLUE,anchor='middle',weight='bold')
for x,txt,eq,meaning,col in [(5,'Eigen prijs','Ev = %ΔQv / %ΔP','Sterkte: kijk naar |Ev|',BLUE),(250,'Inkomen','Ei = %ΔQv / %ΔY','Teken én grootte',GREEN),(495,'Prijs ander goed','Ek = %ΔQv X / %ΔP Z','Teken; noem X en Z',AMBER)]:
 s+=arrow(360,61,x+110,96,col,1.8)+rect(x,104,220,139,LIGHT)
 s+=text(x+110,132,txt,19,col,anchor='middle',weight='bold')+text(x+110,167,eq,16,anchor='middle',weight='bold')+text(x+110,209,meaning,16,anchor='middle')
save('2.2.4_fig_2',s,{'type':'chapter_summary','families':['Ev','Ei','Ek']})
(OUT/'geometry-data.json').write_text(json.dumps(DATA,ensure_ascii=False,indent=2),encoding='utf-8')
print(f'Created {len(DATA)} SVG/PNG pairs.')
