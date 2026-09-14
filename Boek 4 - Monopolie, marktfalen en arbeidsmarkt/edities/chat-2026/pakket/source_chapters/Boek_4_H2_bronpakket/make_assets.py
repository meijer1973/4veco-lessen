"""Exact vector diagrams with auditable function/point/area geometry."""
from pathlib import Path
from html import escape
import json, math
import cairosvg
ROOT=Path(__file__).resolve().parent;AS=ROOT/'_assets';AS.mkdir(exist_ok=True)
INK='#183247';BLUE='#146d9b';TEAL='#247d70';AMBER='#ae681c';RED='#ab4943';GRAY='#637986'
LOG=[]
def num(v):return str(int(round(v))) if abs(v-round(v))<1e-7 else ('%.2f'%v).rstrip('0').rstrip('.').replace('.',',')
def polygon_area(coords):return abs(sum(coords[i][0]*coords[(i+1)%len(coords)][1]-coords[(i+1)%len(coords)][0]*coords[i][1] for i in range(len(coords))))/2
class SVG:
 def __init__(self,name,w=900,h=430,title=''):
  self.name=name;self.w=w;self.h=h;self.plots=[];self.labels=[]
  self.bits=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img"><title>{escape(title or name)}</title>',f'<rect width="{w}" height="{h}" rx="8" fill="#f5f8fa"/>', '''<defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10" fill="none" stroke="#637986" stroke-width="1.5"/></marker><pattern id="hatch" width="10" height="10" patternUnits="userSpaceOnUse"><path d="M0 10L10 0" stroke="#183247" stroke-width="1" opacity=".25"/></pattern><pattern id="horizontal" width="10" height="8" patternUnits="userSpaceOnUse"><path d="M0 4H10" stroke="#183247" stroke-width="1" opacity=".22"/></pattern><pattern id="cross" width="10" height="10" patternUnits="userSpaceOnUse"><path d="M0 10L10 0M0 0L10 10" stroke="#183247" stroke-width="1" opacity=".25"/></pattern></defs>''']
 def text(self,x,y,text,size=18,color=INK,anchor='start',weight=400):
  self.bits.append(f'<text x="{x:.4f}" y="{y:.4f}" font-family="Lato,DejaVu Sans,sans-serif" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{color}">{escape(str(text))}</text>')
  self.labels.append({'text':str(text),'x':x,'y':y,'size':size,'anchor':anchor})
 def line(self,x1,y1,x2,y2,color=GRAY,width=1.4,dash='',arrow=False):
  self.bits.append(f'<line x1="{x1:.4f}" y1="{y1:.4f}" x2="{x2:.4f}" y2="{y2:.4f}" stroke="{color}" stroke-width="{width}"'+(f' stroke-dasharray="{dash}"' if dash else '')+(' marker-end="url(#arrow)"' if arrow else '')+'/>')
 def rect(self,x,y,w,h,fill='white',stroke=BLUE):self.bits.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" stroke="{stroke}" stroke-width="1.3"/>')
 def save(self):
  data='\n'.join(self.bits+['</svg>']);(AS/(self.name+'.svg')).write_text(data,encoding='utf-8')
  cairosvg.svg2png(bytestring=data.encode(),write_to=str(AS/(self.name+'.png')),output_width=1800)
  LOG.append({'file':self.name,'width':self.w,'height':self.h,'plots':self.plots,'labels':self.labels})
class Plot:
 def __init__(self,s,x=78,y=76,w=748,h=268,xmax=60,ymax=80,xt=None,yt=None,title='',xlabel='Q (eenheden per periode)',ylabel='P en kosten (€ per eenheid)'):
  self.s=s;self.x=x;self.y=y;self.w=w;self.h=h;self.xmax=xmax;self.ymax=ymax
  self.id='p'+str(len(s.plots));self.log={'id':self.id,'box':[x,y,w,h],'xmax':xmax,'ymax':ymax,'curves':[],'points':[],'areas':[]};s.plots.append(self.log)
  s.text(x+w/2,28,title,21,anchor='middle',weight=700);s.text(x,55,ylabel,17)
  for q in xt if xt is not None else [xmax*i/4 for i in range(5)]:
   s.line(self.X(q),y,self.X(q),y+h,'#dbe4e9',.7);s.text(self.X(q),y+h+25,num(q),17,anchor='middle')
  for p in yt if yt is not None else [ymax*i/4 for i in range(5)]:
   s.line(x,self.Y(p),x+w,self.Y(p),'#dbe4e9',.7);s.text(x-10,self.Y(p)+5,num(p),17,anchor='end')
  s.line(x,y+h,x+w+8,y+h,INK,1.8,arrow=True);s.line(x,y+h,x,y-5,INK,1.8,arrow=True)
  s.text(x+w/2,y+h+53,xlabel,18,anchor='middle')
 def X(self,q):return self.x+q/self.xmax*self.w
 def Y(self,p):return self.y+self.h-p/self.ymax*self.h
 def curve(self,name,a,b,color=BLUE,dash='',labelq=None,dx=0,dy=-11,sz=18,anchor='start'):
  lo,hi=0.,self.xmax
  if b!=0:
   u,v=sorted([(0-a)/b,(self.ymax-a)/b]);lo=max(lo,u);hi=min(hi,v)
  elif not 0<=a<=self.ymax:return
  if hi<lo:return
  pts=[(lo,a+b*lo),(hi,a+b*hi)]
  self.s.bits.append(f'<polyline data-panel="{self.id}" data-curve="{escape(name)}" points="'+ ' '.join(f'{self.X(q):.8f},{self.Y(p):.8f}' for q,p in pts)+f'" fill="none" stroke="{color}" stroke-width="3"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>')
  self.log['curves'].append({'name':name,'a':a,'b':b,'endpoints':pts})
  q=labelq if labelq is not None else lo+.75*(hi-lo)
  self.s.text(self.X(q)+dx,self.Y(a+b*q)+dy,name,sz,color,anchor=anchor,weight=700)
 def point(self,q,p,name='',curve=None,dx=9,dy=-12,guides=True):
  if guides:
   self.s.line(self.x,self.Y(p),self.X(q),self.Y(p),GRAY,1,'5 4');self.s.line(self.X(q),self.y+self.h,self.X(q),self.Y(p),GRAY,1,'5 4')
  self.s.bits.append(f'<circle data-panel="{self.id}" data-point="{escape(name)}" cx="{self.X(q):.4f}" cy="{self.Y(p):.4f}" r="4.2" fill="{INK}"/>')
  if name:self.s.text(self.X(q)+dx,self.Y(p)+dy,name,18,weight=700)
  self.log['points'].append({'q':q,'p':p,'name':name,'curve':curve})
 def area(self,vertices,label='',color=BLUE,pattern='hatch',at=None,callout=None,visible=True):
  pts=' '.join(f'{self.X(q):.8f},{self.Y(p):.8f}' for q,p in vertices)
  key=label or f'gebied{len(self.log["areas"])}'
  self.s.bits.append(f'<polygon data-panel="{self.id}" data-area="{escape(key)}" points="{pts}" fill="{color}" fill-opacity=".15" stroke="none"/>')
  self.s.bits.append(f'<polygon points="{pts}" fill="url(#{pattern})"/>')
  entry={'name':key,'vertices':vertices,'area':polygon_area(vertices)};self.log['areas'].append(entry)
  if label and visible:
   q,p=at or (sum(v[0] for v in vertices)/len(vertices),sum(v[1] for v in vertices)/len(vertices))
   if callout:
    tq,tp=callout;self.s.text(self.X(tq),self.Y(tp),label,18,color,weight=700)
    self.s.line(self.X(tq)-7,self.Y(tp)-5,self.X(q),self.Y(p),color,1.2,arrow=True)
   else:self.s.text(self.X(q),self.Y(p)+6,label,18,color,anchor='middle',weight=700)
 def level(self,p,qend=None):self.s.line(self.x,self.Y(p),self.X(qend or self.xmax),self.Y(p),GRAY,1.2,'5 4')

def flow(name,boxes,title,note='',height=198):
 s=SVG(name,900,height,title);s.text(450,28,title,22,anchor='middle',weight=700)
 w=(840-24*(len(boxes)-1))/len(boxes)
 for i,lines in enumerate(boxes):
  x=30+i*(w+24);s.rect(x,51,w,83,stroke=[BLUE,TEAL,AMBER][i%3])
  for j,t in enumerate(lines):s.text(x+w/2,82+25*j,t,19 if j==0 else 17,anchor='middle',weight=700 if j==0 else 400)
  if i<len(boxes)-1:s.line(x+w+2,92,x+w+20,92,arrow=True)
 if note:s.text(450,173,note,17,anchor='middle')
 s.save()

def actors(name,positive=False):
 s=SVG(name,900,255,'Een derde partij buiten de markt')
 s.text(450,28,'Wie neemt deel? Wie ondervindt het effect?',21,anchor='middle',weight=700)
 for x,title,sub in [(35,'Koper','betaalt de dienst'),(345,'Aanbieder','ontvangt de prijs'),(655,'Derden','geen marktbetaling')]:
  s.rect(x,63,210,85,stroke=BLUE if x<600 else TEAL)
  s.text(x+105,95,title,22,anchor='middle',weight=700);s.text(x+105,123,sub,17,anchor='middle')
 s.line(250,94,338,94,arrow=True);s.text(294,82,'betaling',16,anchor='middle')
 s.line(560,105,648,105,TEAL if positive else RED,1.8,arrow=True)
 s.text(604,89,'effect',16,anchor='middle')
 s.text(450,193,'Voordeel voor buren' if positive else 'Schade bij omwonenden',21,TEAL if positive else RED,anchor='middle',weight=700)
 s.text(450,222,'Niet vergoed in de onderzochte transactie',18,anchor='middle');s.save()

def monopoly(name,a=80,b=1,c=20,d=1,xmax=60,ymax=80,mode='choice',title='',unit='verhuurbeurten per dag',small=False):
 h=315 if small else 430;ph=180 if small else 268
 s=SVG(name,900,h,title);p=Plot(s,h=ph,xmax=xmax,ymax=ymax,xt=list(range(0,int(xmax)+1,10 if xmax<=60 else 20)),yt=sorted(set([0,c]+list(range(0,int(ymax)+1,10)))),title=title or 'Dezelfde vraag en kosten',xlabel=f'Q ({unit})',ylabel='P, MO en MK (€ per eenheid)')
 qm=(a-c)/(2*b+d);qe=(a-c)/(b+d);pm=a-b*qm;pe=a-b*qe;mc=lambda q:c+d*q
 if mode=='transfer':
  p.area([[0,pe],[qm,pe],[qm,pm],[0,pm]],'Overdracht',BLUE,at=(qm*.44,(pe+pm)/2))
  p.area([[qm,pm],[qe,pe],[qm,mc(qm)]],'Verlies',RED,'cross',callout=(qe+8,pe+15))
 if mode=='guided':
  p.area([[0,pe],[qm,pe],[qm,pm],[0,pm]],'A',BLUE)
  p.area([[qm,pm],[qe,pe],[qm,mc(qm)]],'B',RED,'cross')
 if mode=='answer':
  p.area([[0,a],[qm,pm],[0,pm]],'CS',BLUE)
  p.area([[0,c],[qm,mc(qm)],[qm,pm],[0,pm]],'PS',AMBER,'horizontal',at=(qm*.4,(c+pm)*.5))
  p.area([[qm,pm],[qe,pe],[qm,mc(qm)]],'verlies',RED,'cross',callout=(qe+8,pe+18))
 p.curve('Vraag = GO',a,-b,BLUE,labelq=xmax*.73,dy=-13)
 p.curve('MO',a,-2*b,TEAL,'7 5',labelq=min(xmax*.22,a/(2*b)*.5),dy=-13)
 p.curve('MK',c,d,RED,labelq=xmax*.90,dy=-12,anchor='end')
 if mode!='blank':
  p.point(qm,mc(qm),'',curve='MK');p.point(qm,pm,'M',curve='Vraag = GO')
  if mode!='choice':p.point(qe,pe,'E',curve='Vraag = GO',dx=9,dy=-15)
  if not small:s.text(450,422,'M: '+num(qm)+' eenheden tegen € '+num(pm)+('   |   E: '+num(qe)+' tegen € '+num(pe) if mode!='choice' else ''),17,anchor='middle')
 s.save()

def groups(name,a=36,bb=20,c=4,marked=False,title='Twee groepen, dezelfde kosten'):
 s=SVG(name,900,426,title)
 for k,(x,A,gn) in enumerate([(65,a,'A'),(514,bb,'B')]):
  p=Plot(s,x=x,y=77,w=329,h=259,xmax=40,ymax=40,xt=[0,10,20,30,40],yt=[0,8,16,24,32,40],title='Groep '+gn,xlabel=f'Q_{gn} (bezoeken per week)',ylabel='P, MO en MK (€ per bezoek)')
  p.curve('Vraag / GO',A,-1,BLUE,labelq=A*.58,dy=-12,sz=17)
  p.curve('MO',A,-2,TEAL,'7 4',labelq=A*.17,dy=-10,sz=17)
  p.curve('MK',c,0,RED,labelq=31,dy=-9,sz=17)
  if marked:
   q=(A-c)/2;pr=A-q;p.point(q,pr,'',curve='Vraag / GO');p.point(q,c,'',curve='MK',guides=False)
   s.text(x+165,418,f'Q_{gn} = {num(q)}; P_{gn} = € {num(pr)}',17,anchor='middle',weight=700)
 s.save()

def firm(name,a,b,c,q=None,title='',unit='maaltijden per dag'):
 s=SVG(name);xmax=60 if a==30 else 100
 p=Plot(s,xmax=xmax,ymax=a,xt=[0,xmax/4,xmax/2,xmax*.75,xmax],yt=[0,c,a/2,a],title=title,xlabel=f'q ({unit})',ylabel='P, MO en MK (€ per eenheid)')
 p.curve('GO = P',a,-b,BLUE,labelq=xmax*.7,dy=-15);p.curve('MO',a,-2*b,TEAL,'7 5',labelq=xmax*.25,dy=-12);p.curve('MK',c,0,RED,labelq=xmax*.83,dy=22)
 if q is not None:p.point(q,c,'1',curve='MK',dx=-21,dy=21);p.point(q,a-b*q,'2',curve='GO = P');s.text(450,421,f'q = {num(q)}   →   P = € {num(a-b*q)}',18,anchor='middle',weight=700)
 s.save()

def external(name,a=50,b=.5,c=10,d=.5,e=10,positive=False,mode='social',title='',unit='leveringen per dag',small=False):
 # mode social, loss, policy, guided, blank, answer; policy adds only the familiar shifted supply.
 xmax=100 if b==.5 else 40 if a<=50 else 60
 ymax=max(a+e if positive else a,c+d*xmax+e if not positive else c+d*xmax)
 ymax=math.ceil(ymax/10)*10
 sh=310 if small else 432;ph=176 if small else 268
 s=SVG(name,900,sh,title)
 ylabel='P, kosten en baten (€ per eenheid)' if positive else 'P en kosten (€ per eenheid)'
 p=Plot(s,xmax=xmax,ymax=ymax,h=ph,xt=list(range(0,int(xmax)+1,10 if xmax<=60 else 20)),yt=list(range(0,int(ymax)+1,10)),title=title or ('Privévoordeel en voordeel voor derden' if positive else 'Private en maatschappelijke kosten'),xlabel=f'Q ({unit})',ylabel=ylabel)
 q0=(a-c)/(b+d);q1=(a-c+(e if positive else -e))/(b+d);pc=a-b*q1;pp=c+d*q1
 socialname='Baten maatschappelijk' if positive else 'MK maatschappelijk'
 if mode in ['loss','answer']:
  verts=[[q0,a-b*q0],[q0,a+e-b*q0],[q1,c+d*q1]] if positive else [[q1,a-b*q1],[q0,c+d*q0+e],[q0,a-b*q0]]
  p.area(verts,'verlies',RED,'cross',callout=(xmax*.63 if positive else xmax*.68,ymax*.87 if positive else ymax*.4))
 if mode=='answer':
  p.area([[0,a],[q1,pc],[0,pc]],'CS',BLUE)
  p.area([[0,c],[q1,pp],[0,pp]],'PS',AMBER,'horizontal',at=(q1*.32,c+(pp-c)*.48))
 # Lines: in the policy view the economic interpretation was taught on separate social graph.
 p.curve('Vraag',a,-b,BLUE,labelq=xmax*.7 if a-b*xmax*.7>=0 else .65*a/b,dy=-12)
 p.curve('A = MK privé',c,d,RED,labelq=xmax*.94 if positive else xmax*.78,dy=-13 if positive else 25,anchor='end' if positive else 'start')
 if mode=='policy':
  p.curve('A − s' if positive else 'A + t',c-e if positive else c+e,d,TEAL,'8 5',labelq=xmax*.90,dy=-12,anchor='end')
 else:
  p.curve(socialname,a+e if positive else c+e,-b if positive else d,TEAL,'8 5',labelq=(xmax*.75 if mode=='guided' else xmax*.15) if positive else xmax*.94,dy=-14,anchor='start' if positive else 'end')
 if mode in ['social','loss']:
  p.point(q0,a-b*q0,'0',curve='Vraag',dx=-19,dy=21)
  p.point(q1,c+d*q1 if positive else a-b*q1,'E',curve=socialname,dx=9,dy=-15)
 if mode=='guided':
  q=20;p.point(q,a-b*q if positive else c+d*q,'privé',curve='Vraag' if positive else 'A = MK privé',dx=-55 if positive else 12,dy=25)
  p.point(q,a+e-b*q if positive else c+e+d*q,'maatschappelijk',curve=socialname,dx=12 if positive else -135,dy=-12)
 if mode in ['policy','answer']:
  p.point(q1,pc,'Pc = '+num(pc),curve='Vraag',dx=9,dy=-15 if not positive else 36)
  p.point(q1,pp,'Pp = '+num(pp),curve='A = MK privé',dx=9 if not positive else -92,dy=24 if not positive else -13)
  if not small:s.text(450,423,f'Q = {num(q1)}   |   '+('subsidie' if positive else 'heffing')+f' = € {num(e)} per eenheid',17,anchor='middle')
 s.save()

def all_assets():
 flow('chapter_route',[['Marktgedrag','Wie kiest prijs en afzet?'],['Welvaart','Welke partijen tellen mee?'],['Beleid','Wat verandert de oorzaak?']],'De route door het hoofdstuk')
 monopoly('421_choice',mode='choice',title='Eerst de winstkeuze van de monopolist')
 monopoly('421_transfer',mode='transfer',title='Een overdracht is geen verloren surplus')
 monopoly('421_we',a=70,c=10,xmax=50,mode='transfer',title='Studiohuur · Monopolie en efficiëntie',unit='sessies per week')
 monopoly('421_guided',mode='guided',title='Lees de twee gebieden A en B')
 monopoly('421_target',a=80,b=.5,c=20,d=.5,xmax=100,ymax=80,mode='blank',title='De VR-studio · Basisgrafiek',unit='sessies per week')
 monopoly('421_answer7',a=80,b=.5,c=20,d=.5,xmax=100,ymax=80,mode='answer',title='Doeloefening 7 · Surplus en verlies',unit='sessies per week')
 flow('422_conditions',[['Marktmacht','eigen prijsruimte'],['Groepen herkennen','verschillende reacties'],['Gescheiden houden','doorverkoop voorkomen']],'Wanneer werken verschillende prijzen?')
 groups('422_groups');groups('422_guided',marked=True)
 groups('422_target',a=40,bb=24,c=8);groups('422_answer16',a=40,bb=24,c=8,marked=True)
 firm('423_we',18,.1,6,60,'IJsatelier · Een korte-termijnkeuze','porties per dag')
 firm('423_guided',30,.5,10,20,'Eén lunchzaak, niet de hele markt')
 firm('423_answer25',30,.25,6,48,'Doeloefening 25 · Puur','maaltijden per dag')
 actors('424_actors');external('424_social',mode='social',title='De schade komt boven op de private kosten')
 external('424_loss',mode='loss',title='Tussen Qe en Q₀ zijn de maatschappelijke kosten te hoog')
 external('424_tax',mode='policy',title='De bekende heffingswig: twee prijzen bij één Q')
 external('424_we',a=40,b=1,c=0,d=1,e=8,mode='policy',title='Kleurwater · De heffing verwerken',unit='wasbeurten per dag')
 external('424_guided',mode='guided',title='Lees kosten per extra levering')
 external('424_target',a=60,b=1,c=0,d=1,e=20,mode='blank',title='Reinigingsdiensten · Basisgrafiek',unit='diensten per dag')
 external('424_answer34',a=60,b=1,c=0,d=1,e=20,mode='answer',title='Doeloefening 34 · Alle relevante partijen',unit='diensten per dag')
 actors('425_actors',True)
 external('425_social',positive=True,mode='social',title='De hogere lijn bevat ook voordeel voor derden',unit='aanlegdiensten per maand')
 external('425_subsidy',positive=True,mode='policy',title='Subsidie aan aanbieders: Pp is hoger dan Pc',unit='aanlegdiensten per maand')
 external('425_we',a=50,b=1,c=10,d=1,e=8,positive=True,mode='policy',title='Buurtvaardig · Dezelfde subsidieprocedure',unit='cursusplaatsen per maand')
 external('425_we_loss',a=50,b=1,c=10,d=1,e=8,positive=True,mode='loss',title='Buurtvaardig · De gemiste maatschappelijke baten',unit='cursusplaatsen per maand')
 external('425_guided',positive=True,mode='guided',small=True,title='Lees private en maatschappelijke baten',unit='aanlegdiensten per maand')
 external('425_target',a=60,b=.5,c=20,d=.5,e=10,positive=True,mode='blank',title='Buurtcursus · Basisgrafiek',unit='deelnemers per maand')
 external('425_answer43',a=60,b=.5,c=20,d=.5,e=10,positive=True,mode='answer',title='Doeloefening 43 · Welvaart inclusief derden',unit='deelnemers per maand')
 flow('426_route',[['Probleem','wie ondervindt nadeel?'],['Mechanisme','waarom ontstaat het?'],['Instrument','wat verandert de keuze?'],['Oordeel','criterium + beperking']],'Beleid: vier stappen',height=198)
 external('425_mixed',a=40,b=1,c=0,d=1,e=8,positive=True,mode='blank',title='Gemengde oefening · De gezamenlijke cursus',unit='deelnemers per maand')
 external('425_mixed57',a=40,b=1,c=0,d=1,e=8,positive=True,mode='answer',title='Opgave 57 · Cursusplaatsen',unit='deelnemers per maand')
 monopoly('427_A',a=70,c=10,xmax=50,mode='blank',title='A · Studio Solo',unit='sessies per week',small=True)
 external('427_B',a=60,b=1,c=0,d=1,e=20,mode='blank',title='B · Reiniging bij woningen',unit='diensten per dag',small=True)
 monopoly('427_answerA',a=70,c=10,xmax=50,mode='answer',title='Doeloefening 58 · Studio Solo',unit='sessies per week')
 external('427_answerB',a=60,b=1,c=0,d=1,e=20,mode='answer',title='Doeloefening 58 · Reiniging bij woningen',unit='diensten per dag')
 external('424_independent',a=40,b=1,c=0,d=1,e=8,mode='blank',title='Behandelingen · Zelfstandig het verlies bepalen',unit='behandelingen per dag')
 external('424_answer33',a=40,b=1,c=0,d=1,e=8,mode='answer',title='Opgave 33 · Het oorspronkelijke verlies',unit='behandelingen per dag')
 external('425_loss',positive=True,mode='loss',title='Opgave 39 · Gemiste maatschappelijke baten',unit='aanlegdiensten per maand')
 external('425_independent',a=36,b=1,c=4,d=1,e=8,positive=True,mode='blank',title='Een cursus · Zelfstandig de gemiste baten bepalen',unit='deelnemers per maand')
 external('425_answer42',a=36,b=1,c=4,d=1,e=8,positive=True,mode='answer',title='Opgave 42 · Het oorspronkelijke verlies',unit='deelnemers per maand')
 (ROOT/'QA'/'figure_geometry.json').write_text(json.dumps(LOG,ensure_ascii=False,indent=2))
 print('Created',len(LOG),'SVG/PNG figure pairs')
if __name__=='__main__':all_assets()
