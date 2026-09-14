"""Original vector illustrations for the trade chapter. Values are synthetic model data.
All curves, intersections and polygons are computed from declared equations.
SVG and matching PNG are emitted; fonts are not distributed.
"""
from pathlib import Path
from html import escape
import math,json
import cairosvg
ROOT=Path(__file__).resolve().parent;AS=ROOT/'_assets';AS.mkdir(exist_ok=True)
INK='#183247';BLUE='#146d9b';TEAL='#247d70';AMBER='#ad681f';GRAY='#667c8b';LIGHT='#edf3f6';RED='#a54c39'
LOG=[]
def num(v):
 if abs(v-round(v))<1e-8:return str(int(round(v)))
 return f'{v:.2f}'.rstrip('0').rstrip('.').replace('.',',')
class SVG:
 def __init__(self,name,w=900,h=410,title=''):
  self.name,self.w,self.h=name,w,h;self.panels=[];self.texts=[]
  self.bits=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img"><title>{escape(title or name)}</title>',
   '<defs><marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10" fill="none" stroke="#536777" stroke-width="1.5"/></marker><pattern id="hatch" width="8" height="8" patternUnits="userSpaceOnUse"><path d="M0,8 L8,0" stroke="#183247" stroke-opacity=".25" stroke-width="1"/></pattern></defs>',f'<rect width="{w}" height="{h}" rx="10" fill="#f5f8fa"/>']
 def text(self,x,y,t,size=18,color=INK,anchor='start',weight=400,halo=False):
  base=f'<text x="{x:.8f}" y="{y:.8f}" font-family="Lato,DejaVu Sans,sans-serif" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}"'
  if halo:self.bits.append(base+f' fill="#f5f8fa" stroke="#f5f8fa" stroke-width="4" stroke-linejoin="round">{escape(str(t))}</text>')
  self.bits.append(base+f' fill="{color}">{escape(str(t))}</text>')
  self.texts.append({'x':x,'y':y,'text':str(t),'size':size,'anchor':anchor})
 def line(self,x1,y1,x2,y2,color=GRAY,width=1.5,dash='',arrow=False,both=False):
  self.bits.append(f'<line x1="{x1:.8f}" y1="{y1:.8f}" x2="{x2:.8f}" y2="{y2:.8f}" stroke="{color}" stroke-width="{width}"'+(f' stroke-dasharray="{dash}"' if dash else '')+(' marker-end="url(#arr)"' if arrow or both else '')+(' marker-start="url(#arr)"' if both else '')+'/>')
 def rect(self,x,y,w,h,fill='white',stroke=BLUE):
  self.bits.append(f'<rect x="{x:.8f}" y="{y:.8f}" width="{w:.8f}" height="{h:.8f}" rx="5" fill="{fill}" stroke="{stroke}" stroke-width="1.6"/>')
 def save(self):
  text='\n'.join(self.bits+['</svg>']);(AS/f'{self.name}.svg').write_text(text,encoding='utf8')
  cairosvg.svg2png(bytestring=text.encode(),write_to=str(AS/f'{self.name}.png'),output_width=1800)
  LOG.append({'file':self.name,'width':self.w,'height':self.h,'panels':self.panels,'texts':self.texts})
class Plot:
 def __init__(self,s,x=72,y=75,w=700,h=220,xmax=120,ymax=60,xticks=None,yticks=None,title='',unit='stuks per week',priceunit='€ per product'):
  self.s=s;self.x=x;self.y=y;self.w=w;self.h=h;self.xmax=xmax;self.ymax=ymax
  self.id=f'p{len(s.panels)}';self.log={'id':self.id,'box':[x,y,w,h],'xmax':xmax,'ymax':ymax,'curves':[],'points':[],'areas':[],'prices':[],'gaps':[]};s.panels.append(self.log)
  s.text(x+w/2,26,title,21,weight=700,anchor='middle');s.text(x,54,f'P ({priceunit})',17)
  s.bits.append(f'<defs><clipPath id="{self.id}"><rect x="{x}" y="{y}" width="{w}" height="{h}"/></clipPath></defs>')
  for q in (xticks if xticks is not None else [xmax*i/6 for i in range(7)]):
   xx=self.X(q);s.line(xx,y,xx,y+h,'#dce5eb',.8);s.text(xx,y+h+23,num(q),16,anchor='middle')
  for p in (yticks if yticks is not None else [ymax*i/6 for i in range(7)]):
   yy=self.Y(p);s.line(x,yy,x+w,yy,'#dce5eb',.8);s.text(x-11,yy+5,num(p),16,anchor='end')
  s.line(x,y+h,x+w+8,y+h,INK,1.7,arrow=True);s.line(x,y+h,x,y-8,INK,1.7,arrow=True)
  s.text(x+w/2,s.h-15,f'Q ({unit})',17,anchor='middle')
 def X(self,q):return self.x+self.w*q/self.xmax
 def Y(self,p):return self.y+self.h*(1-p/self.ymax)
 def curve(self,name,a,b,color):
  qs=[0,self.xmax]
  for p in [0,self.ymax]:
   if b!=0:qs.append((p-a)/b)
  valid=sorted(q for q in qs if -1e-7<=q<=self.xmax+1e-7 and -1e-7<=a+b*q<=self.ymax+1e-7)
  if len(valid)<2:raise ValueError('Invisible curve')
  q0,q1=valid[0],valid[-1];pts=[[q0,a+b*q0],[q1,a+b*q1]]
  coords=' '.join(f'{self.X(q):.8f},{self.Y(p):.8f}' for q,p in pts)
  self.s.bits.append(f'<polyline data-curve="{name}" data-panel="{self.id}" points="{coords}" fill="none" stroke="{color}" stroke-width="3"/>')
  self.log['curves'].append({'name':name,'a':a,'b':b,'points':pts})
  q=q0+(q1-q0)*.78;p=a+b*q
  self.s.text(self.X(q)+6,self.Y(p)+(22 if b<0 else -10),name,19,color,weight=700,halo=True)
 def price(self,p,label,color=GRAY,dash='6 4',dy=-5):
  self.s.line(self.x,self.Y(p),self.x+self.w,self.Y(p),color,1.8,dash)
  self.s.text(self.x+self.w+11,self.Y(p)+dy,label,16,color)
  self.log['prices'].append({'p':p,'label':label})
 def point(self,q,p,label='',dx=0,dy=-10,anchor='middle',guides=True):
  if guides:self.s.line(self.X(q),self.Y(p),self.X(q),self.y+self.h,GRAY,1.2,'4 4')
  self.s.bits.append(f'<circle data-point="{escape(label)}" data-panel="{self.id}" cx="{self.X(q):.8f}" cy="{self.Y(p):.8f}" r="4" fill="{INK}"/>')
  if label:self.s.text(self.X(q)+dx,self.Y(p)+dy,label,17,anchor=anchor,weight=700,halo=True)
  self.log['points'].append({'q':q,'p':p,'label':label})
 def gap(self,q1,q2,label):
  left,right=sorted([q1,q2]);y=self.y+self.h+48
  self.s.line(self.X(left),y-7,self.X(left),y+6);self.s.line(self.X(right),y-7,self.X(right),y+6);self.s.line(self.X(left),y,self.X(right),y,both=True)
  self.s.text((self.X(left)+self.X(right))/2,y+26,label,18,anchor='middle',weight=700)
  self.log['gaps'].append({'from':left,'to':right,'value':right-left,'label':label})
 def polygon(self,label,points,color,showlabel=True):
  coords=' '.join(f'{self.X(q):.8f},{self.Y(p):.8f}' for q,p in points)
  self.s.bits.append(f'<polygon data-area="{label}" data-panel="{self.id}" points="{coords}" fill="{color}" fill-opacity=".19" stroke="{color}" stroke-width="1"/>')
  self.s.bits.append(f'<polygon points="{coords}" fill="url(#hatch)"/>')
  area=abs(sum(points[i][0]*points[(i+1)%len(points)][1]-points[(i+1)%len(points)][0]*points[i][1] for i in range(len(points)))/2)
  self.log['areas'].append({'label':label,'points':points,'value':area})
  if showlabel:
   q=sum(v[0] for v in points)/len(points);p=sum(v[1] for v in points)/len(points)
   self.s.text(self.X(q),self.Y(p)+6,label,18,color,anchor='middle',weight=700)

def flow(name,boxes,heading='',sub=''):
 h=200 if sub else 164;s=SVG(name,900,h,heading);w=(838-26*(len(boxes)-1))/len(boxes)
 if heading:s.text(450,28,heading,21,anchor='middle',weight=700)
 for i,ls in enumerate(boxes):
  x=31+i*(w+26);y=48;s.rect(x,y,w,88,stroke=[BLUE,TEAL,AMBER][i%3])
  for j,t in enumerate(ls):s.text(x+w/2,y+29+j*24,t,19 if j==0 else 17,anchor='middle',weight=700 if j==0 else 400)
  if i<len(boxes)-1:s.line(x+w+3,y+44,x+w+22,y+44,arrow=True)
 if sub:s.text(450,181,sub,17,anchor='middle')
 s.save()
def tradeflow():
 s=SVG('3.3.1_fig_1',900,220,'Import en export vanuit twee landen')
 for x,t in [(35,'LAND A'),(645,'LAND B')]:s.rect(x,50,220,135);s.text(x+110,85,t,22,anchor='middle',weight=700)
 s.text(145,118,'Verkoper',20,anchor='middle');s.text(145,148,'exporteert fietsen',18,anchor='middle')
 s.text(755,118,'Koper',20,anchor='middle');s.text(755,148,'importeert fietsen',18,anchor='middle')
 s.line(273,116,625,116,BLUE,3,arrow=True);s.text(450,96,'dezelfde levering fietsen',20,anchor='middle',weight=700)
 s.line(450,139,450,188,GRAY,1.5,'4 5');s.text(450,210,'landsgrens',17,anchor='middle');s.save()
def comparative():
 s=SVG('3.3.1_fig_2',900,244,'Absoluut versus comparatief voordeel')
 s.text(450,29,'Linde maakt beide producten met minder middelen',22,anchor='middle',weight=700)
 for x,title,lines in [(35,'MACHINES',['Grote absolute voorsprong','Comparatief voordeel: Linde']),(475,'TASSEN',['Kleine absolute voorsprong','Comparatief voordeel: Maris'])]:
  s.rect(x,50,390,135,stroke=BLUE if x<100 else TEAL);s.text(x+195,85,title,21,anchor='middle',weight=700)
  for i,t in enumerate(lines):s.text(x+195,121+i*31,t,19,anchor='middle')
 s.text(450,216,'Maris geeft voor een extra tas minder machineproductie op.',20,anchor='middle');s.save()
def bridge():
 s=SVG('3.3.2_fig_1',900,226,'Binnenlandse productie, verbruik en handel')
 for x,title,sub in [(28,'Binnenlandse producenten','leveren Qa'),(476,'Binnenlandse kopers','gebruiken Qv')]:
  s.rect(x,45,396,78,stroke=TEAL if x<100 else BLUE);s.text(x+198,76,title,21,anchor='middle',weight=700);s.text(x+198,105,sub,19,anchor='middle')
 s.text(450,163,'Qv groter dan Qa? Het verschil wordt ingevoerd.',20,anchor='middle')
 s.text(450,199,'Qa groter dan Qv? Het verschil wordt uitgevoerd.',20,anchor='middle');s.save()

def market(name,D,S,pw,unit,priceunit,xmax,ymax,xticks=None,yticks=None,mark=False,gap=False,tariff=None,revenue=False,noimport=False,h=410,title='De binnenlandse markt'):
 s=SVG(name,900,h,title);pl=Plot(s,w=695,h=h-190,xmax=xmax,ymax=ymax,xticks=xticks,yticks=yticks,title=title,unit=unit,priceunit=priceunit)
 a,b=D;c,d=S;qe=(c-a)/(b-d);pe=a+b*qe
 p=pe if noimport else pw+(tariff or 0);qv=(p-a)/b;qa=(p-c)/d
 pl.curve('V',a,b,BLUE);pl.curve('A',c,d,TEAL)
 pl.price(pw,'Pw = '+num(pw),GRAY,dy=13 if tariff else -7)
 if tariff is not None:pl.price(pw+tariff,'Pw + t = '+num(pw+tariff),AMBER,dy=-8)
 if noimport:pl.price(pe,'P = '+num(pe),TEAL,dy=-4);pl.point(qe,pe,'E',dy=-15)
 elif mark:
  pl.point(qa,p,'Qa = '+num(qa),dx=-9,dy=-12,anchor='end');pl.point(qv,p,'Qv = '+num(qv),dx=9,dy=-12,anchor='start')
 if gap and not noimport:pl.gap(qa,qv,('import' if qv>qa else 'export')+' = '+num(abs(qv-qa)))
 if revenue and not noimport:
  pl.polygon('overheidsopbrengst',[(qa,pw),(qv,pw),(qv,p),(qa,p)],AMBER,False)
  s.text(450,h-48,'Breedte: import na de heffing · hoogte: heffing per product',17,anchor='middle')
 if noimport:s.text(450,h-48,'Geen import: binnenlandse productie = binnenlands verbruik',18,anchor='middle')
 pl.log['model']={'D':D,'S':S,'pw':pw,'tariff':tariff,'actual_price':p,'qa':qa,'qv':qv,'qe':qe,'pe':pe,'trade':0 if noimport else abs(qv-qa)}
 s.save()
def surplus():
 s=SVG('3.3.2_fig_4',900,377,'Surplus zonder handel en met import')
 for x,p,title in [(61,30,'Zonder handel'),(517,20,'Met import')]:
  pl=Plot(s,x=x,y=76,w=302,h=206,xmax=120,ymax=60,xticks=[0,40,60,80,120],yticks=[0,20,30,40,60],title=title,unit='tassen per week',priceunit='€ per tas')
  qv=120-2*p;qa=2*p
  pl.polygon('CS',[(0,p),(qv,p),(0,60)],BLUE)
  pl.polygon('PS',[(0,0),(qa,p),(0,p)],TEAL)
  pl.curve('V',60,-.5,BLUE);pl.curve('A',0,.5,TEAL);pl.price(p,'P = '+str(p),GRAY,dy=3)
  pl.point(qv,p,guides=True);pl.point(qa,p,guides=True)
  s.text(x+151,336,'CS bij Qv; PS bij Qa',17,anchor='middle')
 s.save()
def stakeholder():
 s=SVG('3.3.4_fig_2',900,235,'Verschillende gevolgen van een invoerheffing')
 for i,(title,lines,col) in enumerate([('Kopers',['hogere prijs','minder verbruik'],BLUE),('Producenten',['hogere prijs','meer productie'],TEAL),('Overheid',['ontvangsten over','resterende import'],AMBER)]):
  x=25+i*295;s.rect(x,37,265,137,stroke=col);s.text(x+132.5,72,title,21,anchor='middle',weight=700)
  for j,t in enumerate(lines):s.text(x+132.5,108+27*j,t,20,anchor='middle')
 s.text(450,211,'Een voordeel voor één groep bewijst geen voordeel voor iedereen.',19,anchor='middle');s.save()
def build_all():
 flow('3.3_overzicht',[['Waarom handelen?','relatieve voordelen'],['Wat verandert?','prijs en hoeveelheden'],['Wie merkt dat?','kopers en producenten']],'Handel bekijken vanuit drie vragen')
 tradeflow();comparative()
 flow('3.3.1_fig_3',[['Minder opofferen','relatief voordeel'],['Meer specialiseren','passende activiteiten'],['Ruilen','mogelijk voordeel']],'Waarom handel iets kan opleveren','Beide partijen moeten de ruil aantrekkelijk vinden.')
 flow('3.3.1_fig_4',[['Bronfeit','wat staat er?'],['Verband','waardoor volgt dat?'],['Conclusie','hoe ver mag je gaan?']],'Van bron naar onderbouwd antwoord')
 bridge()
 market('3.3.2_fig_2',[60,-.5],[0,.5],20,'tassen per week','€ per tas',120,60,mark=True,gap=True,title='Lage wereldprijs: import')
 market('3.3.2_fig_3',[60,-.5],[0,.5],40,'tassen per week','€ per tas',120,60,mark=True,gap=True,title='Hoge wereldprijs: export')
 surplus()
 market('3.3.2_we_1',[70,-.5],[10,.5],30,'helmen per week','€ per helm',140,70,xticks=[0,20,40,60,80,100,120,140],yticks=[0,10,20,30,40,50,60,70],mark=True,gap=True,h=380,title='Sporthelmen in Elva')
 market('3.3.2_ex_1',[30,-.25],[0,.25],10,'paren per week','€ per paar',120,30,yticks=[0,5,10,15,20,25,30],title='Handschoenen in Ista')
 market('3.3.2_target',[80,-.5],[0,.5],30,'matten per week','€ per mat',160,80,xticks=list(range(0,161,20)),yticks=list(range(0,81,10)),h=375,title='Kampeermatten in Noro')
 flow('3.3.3_fig_1',[['Doel','wat wil de overheid?'],['Instrument','hoe verandert handel?'],['Gevolgen','voor welke groepen?']],'Beoordeel doel en effecten apart')
 market('3.3.3_fig_2',[60,-.5],[0,.5],20,'flessen per week','€ per fles',120,60,xticks=list(range(0,121,10)),yticks=list(range(0,61,10)),tariff=5,mark=True,gap=True,title='Drinkflessen: een invoerheffing van € 5')
 market('3.3.3_fig_3',[60,-.5],[0,.5],20,'flessen per week','€ per fles',120,60,xticks=list(range(0,121,10)),yticks=list(range(0,61,10)),tariff=5,mark=True,revenue=True,title='De juiste opbrengstrechthoek')
 market('3.3.3_fig_4',[60,-.5],[0,.5],20,'flessen per week','€ per fles',120,60,xticks=list(range(0,121,20)),yticks=[0,10,20,30,40,50,60],tariff=15,noimport=True,h=355,title='De heffing maakt import te duur')
 market('3.3.3_ex_1',[26,-.2],[6,.2],10,'paraplu’s per week','€ per paraplu',130,26,xticks=list(range(0,131,10)),yticks=[0,5,10,15,20,25],tariff=2,h=350,title='Paraplu’s in Luma')
 market('3.3.3_target',[80,-.5],[0,.5],20,'rugzakken per week','€ per rugzak',160,80,xticks=list(range(0,161,20)),yticks=list(range(0,81,10)),tariff=10,h=380,title='Schoolrugzakken in Daro')
 flow('3.3.4_fig_1',[['Bron','selecteer het gegeven'],['Methode','reken of verklaar'],['Oordeel','benoem de grens']],'De bekende werkwijze combineren')
 stakeholder()
 market('3.3.4_target',[40,-.25],[0,.25],10,'jassen per week','€ per jas',160,40,xticks=list(range(0,161,20)),yticks=list(range(0,41,5)),tariff=5,h=390,title='Regenjassen in Nerin')
 flow('3.3_slot',[['Specialisatie','relatief minder opgeven'],['Wereldprijs','productie ≠ verbruik'],['Bescherming','doel ≠ ieders voordeel']],'De kern van internationale handel')
 # Exact solution figures for every required student marking task.
 market('3.3.2_ans_14',[30,-.25],[0,.25],10,'paren per week','€ per paar',120,30,yticks=[0,5,10,15,20,25,30],mark=True,gap=True,h=350,title='Opgave 14: 40 paren import')
 market('3.3.2_ans_17',[80,-.5],[0,.5],30,'matten per week','€ per mat',160,80,xticks=list(range(0,161,20)),yticks=list(range(0,81,10)),mark=True,gap=True,h=350,title='Opgave 17: productie 60, verbruik 100')
 market('3.3.3_ans_25',[26,-.2],[6,.2],10,'paraplu’s per week','€ per paraplu',130,26,xticks=list(range(0,131,10)),yticks=[0,5,10,15,20,25],tariff=2,mark=True,revenue=True,h=350,title='Opgave 25: 40 × € 2 = € 80')
 market('3.3.3_ans_27',[80,-.5],[0,.5],20,'rugzakken per week','€ per rugzak',160,80,xticks=list(range(0,161,20)),yticks=list(range(0,81,10)),tariff=10,mark=True,revenue=True,h=350,title='Opgave 27: 40 × € 10 = € 400')
 market('3.3.4_ans_35',[40,-.25],[0,.25],10,'jassen per week','€ per jas',160,40,xticks=list(range(0,161,20)),yticks=list(range(0,41,5)),tariff=5,mark=True,revenue=True,h=350,title='Opgave 35: 40 × € 5 = € 200')
 (ROOT/'QA'/'figure_geometry.json').write_text(json.dumps(LOG,ensure_ascii=False,indent=2))
 print('Figure pairs',len(LOG))
if __name__=='__main__':build_all()
