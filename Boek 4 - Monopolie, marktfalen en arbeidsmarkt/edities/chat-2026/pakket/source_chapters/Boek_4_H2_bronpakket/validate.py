"""Local, reproducible numerical, SVG, source and PDF checks. Not a learner-outcome test."""
from pathlib import Path
import json,re,math,hashlib,xml.etree.ElementTree as ET
from collections import Counter
from html import unescape
from bs4 import BeautifulSoup
import fitz
R=Path(__file__).resolve().parent
checks=[]
def check(condition,name,detail=None):
 checks.append({'check':name,'pass':bool(condition),**({'detail':detail} if detail is not None else {})})
def close(a,b,name):check(math.isclose(a,b,rel_tol=1e-8,abs_tol=1e-6),name,{'actual':a,'expected':b})
N=[]
def values(name, actual, expected):
 N.append({'case':name,'calculated':actual,'expected':expected})
 for k,v in expected.items():close(actual[k],v,name+' / '+k)

def mono(a,b,c,d=0,F=0,cap=1e9):
 q=(a-c)/(2*b+d);p=a-b*q;e=(a-c)/(b+d);pe=a-b*e
 cs=b*q*q/2;tv=c*q+d*q*q/2;ps=p*q-tv;ts=cs+ps
 ecs=b*e*e/2;eps=d*e*e/2;ets=ecs+eps
 check(0<=q<=cap and 0<=e<=cap,'Monopoly/benchmark feasible',{'q':q,'efficient':e,'capacity':cap})
 # Concavity is the negative slope of MO - MK, not just equality.
 check(-2*b-d<0,'Monopoly marginal difference crosses downward')
 return dict(q=q,p=p,efficient=e,ep=pe,CS=cs,PS=ps,TS=ts,profit=ps-F,efficientTS=ets,loss=ets-ts,transfer=q*(p-pe))
def policy(a,b,c,d,external,rate,positive=False):
 sign=1 if positive else -1
 q0=(a-c)/(b+d);p0=a-b*q0;q=(a-c+sign*rate)/(b+d)
 pc=a-b*q;pp=c+d*q;cs=b*q*q/2;ps=d*q*q/2;budget=rate*q;ex=external*q
 w=cs+ps-sign*budget+sign*ex
 w0=(b+d)*q0*q0/2+sign*external*q0
 qe=(a-c+sign*external)/(b+d)
 # Independent welfare calculation using areas under the marginal lines.
 w_integral=(a-c+sign*external)*q-(b+d)*q*q/2
 close(w,w_integral,'Policy ledger equals benefit-minus-real-cost area')
 close(pp-pc if positive else pc-pp,rate,'Policy wedge at the same quantity')
 return dict(q0=q0,p0=p0,q=q,pc=pc,pp=pp,CS=cs,PS=ps,budget=budget,externalTotal=ex,W0=w0,W=w,gain=w-w0,efficient=qe)
def two(aA,aB,c,F,uniform,cap):
 qa=(aA-c)/2;qb=(aB-c)/2;pa=aA-qa;pb=aB-qb
 qau=max(aA-uniform,0);qbu=max(aB-uniform,0)
 def outcome(qA,qB,pA,pB):
  to=pA*qA+pB*qB;tv=c*(qA+qB);ps=to-tv;cs=(qA*qA+qB*qB)/2
  return dict(Q=qA+qB,TO=to,TK=tv+F,profit=ps-F,CS=cs,PS=ps,TS=ps+cs)
 u=outcome(qau,qbu,uniform,uniform);v=outcome(qa,qb,pa,pb)
 check(qa+qb<=cap,'Joint segment output below common capacity')
 close(aA-2*qa,c,'Segment A marginal equality');close(aB-2*qb,c,'Segment B marginal equality')
 return {'QA':qa,'QB':qb,'PA':pa,'PB':pb,**{'uniform_'+k:z for k,z in u.items()},**{'group_'+k:z for k,z in v.items()}}

values('4.2.1 theory / exercise 3',mono(80,1,20,1,cap=60),{'q':20,'p':60,'efficient':30,'ep':50,'CS':200,'PS':600,'TS':800,'efficientTS':900,'loss':100,'transfer':200})
values('Studiohuur / exercise 4 / mixed 58A',mono(70,1,10,1,100,50),{'q':20,'p':50,'efficient':30,'ep':40,'CS':200,'PS':600,'profit':500,'TS':800,'efficientTS':900,'loss':100,'transfer':200})
values('Target 7',mono(80,.5,20,.5,200,100),{'q':40,'p':60,'efficient':60,'ep':50,'CS':400,'PS':1200,'profit':1000,'TS':1600,'efficientTS':1800,'loss':200,'transfer':400})
values('Exercise 1',mono(30,.5,10,0,40,40),{'q':20,'p':20,'profit':160})
values('Exercise 6',mono(60,1,0,1,cap=50),{'q':20,'p':40,'efficient':30,'ep':30,'CS':200,'PS':600,'TS':800,'loss':100})
values('Avondhal / exercise 12',two(36,20,4,64,16,56),{'QA':16,'QB':8,'PA':20,'PB':12,'uniform_Q':24,'uniform_TO':384,'uniform_TK':160,'uniform_profit':224,'uniform_CS':208,'uniform_PS':288,'uniform_TS':496,'group_TO':416,'group_TK':160,'group_profit':256,'group_CS':160,'group_PS':320,'group_TS':480})
values('Target 16',two(40,24,8,80,20,64),{'QA':16,'QB':8,'PA':24,'PB':16,'uniform_TO':480,'uniform_profit':208,'uniform_CS':208,'uniform_PS':288,'uniform_TS':496,'group_TO':512,'group_profit':240,'group_CS':160,'group_PS':320,'group_TS':480})
values('Exercise 14',two(28,20,4,40,12,48),{'QA':12,'QB':8,'PA':16,'PB':12,'group_TO':288,'group_TK':120,'group_profit':168})
values('Exercise 18',mono(24,.2,4,cap=100),{'q':50,'p':14,'CS':250})
# Here only firm feasibility is required; no efficient benchmark is taught in 4.2.3.
def firm(a,b,c,F,cap):
 q=(a-c)/(2*b);p=a-b*q;to=p*q;tk=F+c*q
 check(q<=cap,'Firm q within production capacity');check(b>0,'Firm profit concave')
 return dict(q=q,p=p,TO=to,TK=tk,profit=to-tk)
values('IJsatelier worked example',firm(18,.1,6,120,100),{'q':60,'p':12,'TO':720,'TK':480,'profit':240})
values('Guided 22',firm(30,.5,10,0,60),{'q':20,'p':20})
values('Independent 24',firm(20,.1,4,80,100),{'q':80,'p':12,'TO':960,'TK':400,'profit':560})
values('Target 25',firm(30,.25,6,144,80),{'q':48,'p':18,'TO':864,'TK':432,'profit':432})
values('Negative-effect theory / target 52 H',policy(50,.5,10,.5,10,10),{'q0':40,'p0':30,'q':30,'pc':35,'pp':25,'CS':225,'PS':225,'budget':300,'externalTotal':300,'W0':400,'W':450,'gain':50,'efficient':30})
values('Kleurwater / independent 33 / policy example',policy(40,1,0,1,8,8),{'q0':20,'p0':20,'q':16,'pc':24,'pp':16,'CS':128,'PS':128,'budget':128,'externalTotal':128,'W0':240,'W':256,'gain':16,'efficient':16})
values('Guided 31 partial correction',policy(40,1,0,1,8,4),{'q':18,'CS':162,'PS':162,'budget':72,'externalTotal':144,'W':252,'gain':12})
values('Target 34 / mixed 58B',policy(60,1,0,1,20,20),{'q0':30,'p0':30,'q':20,'pc':40,'pp':20,'CS':200,'PS':200,'budget':400,'externalTotal':400,'W0':300,'W':400,'gain':100,'efficient':20})
values('Retrieval 28',policy(20,1,0,1,0,4),{'q':8,'pc':12,'pp':8,'budget':32})
values('Retrieval 36',firm(40,1,10,0,30),{'q':15,'p':25})
values('Positive-effect theory',policy(50,.5,10,.5,10,10,True),{'q0':40,'p0':30,'q':50,'pc':25,'pp':35,'CS':625,'PS':625,'budget':500,'externalTotal':500,'W0':1200,'W':1250,'gain':50,'efficient':50})
values('Buurtvaardig worked example',policy(50,1,10,1,8,8,True),{'q0':20,'p0':30,'q':24,'pc':26,'pp':34,'CS':288,'PS':288,'budget':192,'externalTotal':192,'W0':560,'W':576,'gain':16,'efficient':24})
values('Guided 40 partial support',policy(50,1,10,1,8,4,True),{'q':22,'CS':242,'PS':242,'budget':88,'externalTotal':176,'W':572,'gain':12})
values('Independent 42',policy(36,1,4,1,8,8,True),{'q0':16,'p0':20,'q':20,'pc':16,'pp':24,'CS':200,'PS':200,'budget':160,'externalTotal':160,'W0':384,'W':400,'gain':16,'efficient':20})
values('Target 43',policy(60,.5,20,.5,10,10,True),{'q0':40,'p0':40,'q':50,'pc':35,'pp':45,'CS':625,'PS':625,'budget':500,'externalTotal':500,'W0':1200,'W':1250,'gain':50,'efficient':50})
values('Retrieval 37',policy(20,1,4,1,0,4,True),{'q':10,'pc':10,'pp':14,'budget':40})
values('Bonus 44 oversized subsidy',policy(50,.5,10,.5,10,30,True),{'q':70,'CS':1225,'PS':1225,'budget':2100,'externalTotal':700,'W':1050,'gain':-150})
values('Mixed 57',policy(40,1,0,1,8,8,True),{'q0':20,'p0':20,'q':24,'pc':16,'pp':24,'CS':288,'PS':288,'budget':192,'externalTotal':192,'W0':560,'W':576,'gain':16})
# Small arithmetic and source-table checks, independent of the authored answer strings.
calc_cases=[('2 transfer balance',-120+80,-40),('5 CS',-300-60,-360),('5 PS',300-40,260),('5 TS',-360+260,-100),('9 tax',(15-10)*80,400),('10 TO',30*12+20*8,520),('10 profit',520-(90+3*50),280),('13 uniform profit',10*30-(100+2*30),140),('13 groups profit',12*15+7*20-(100+2*35),150),('15 CS',-90+30,-60),('15 TS',-90+30+40,-20),('17 I',430+350-(500+300),-20),('17 II',160+260-(100+200),120),('27 PS',900-5*80,500),('27 profit',900-5*80-200,300),('30 damage',20*10,200),('32 costs',3-5,-2),('39 private benefit',50-.5*20,40),('39 social benefit',60-.5*20,50),('41 benefits',2-5,-3),('45 tax',6*20,120),('45 damage',10*20,200),('46 welfare',300+200+100-150-20,430),('49 A',420-10,410),('49 B',450-60,390),('50 gain',650+850-40-(400+1000),60),('51 shortage',50-20,30),('51 damage',20*10,200),('52 H',225+225+300-300-20,430),('52 G',225+525-300-40,410),('53 best',100-20,80),('53 worst',100-140,-40),('54 A',(18-14)*50,200),('54 B',(17-12)*60,300),('56 uniform profit',10*40-2*40-60,260),('56 group profit',12*25+8*15-2*40-60,280),('56 uniform TS',200+400-80,520),('56 group TS',170+420-80,510),('57 net welfare',576-10,566),('57 net gain',576-10-560,6),('60 tax',(18-14)*50,200)]
for name,a,b in calc_cases:close(a,b,name)
(R/'QA/numerical-models.json').write_text(json.dumps({'models':N,'arithmetic':calc_cases},ensure_ascii=False,indent=2))

# Structural coverage and source identity.
E=json.loads((R/'QA/exercises.json').read_text());expected_ids=[q['id'] for e in E for q in e['questions']]
check(len(E)==60,'60 exercises');check(len(expected_ids)==169,'169 subquestions');check(len(set(expected_ids))==169,'All subquestion IDs unique')
student_html=(R/'output/Boek_4_H2_Marktvormen_en_marktfalen.html').read_text();answers_html=(R/'output/Boek_4_H2_Antwoorden.html').read_text()
ss=BeautifulSoup(student_html,'html.parser');aa=BeautifulSoup(answers_html,'html.parser')
check(Counter(x['data-question'] for x in ss.select('[data-question]'))==Counter(expected_ids),'Printed student coverage equals exercise registry')
check(Counter(x['data-answer'] for x in aa.select('[data-answer]'))==Counter(expected_ids),'Every subquestion has one printed answer')
check(len(ss.select('[data-exercise]'))==60,'60 printed exercise blocks')
heads=['Uitgewerkt voorbeeld','Startopgaven','Begeleide inoefening','Zelfstandige oefening','Doeloefening','Denkertje / Bonusopgave','Herhaling / Herhaling en interleaving']
for i in range(1,7):
 text=(R/f'4.2.{i} manuscript.md').read_text();found=re.findall(r'^## (.*)$',text,re.M)
 check(found==heads,f'4.2.{i} canonical section order',found)
 check('Korte route:' in text and 'Heb je deze hulp niet nodig?' in text,f'4.2.{i} paper core/support route')
for n in [5,15,23,32,41]:check(len(E[n-1]['questions'])==4,f'Exercise {n}: two changes / combine / misconception')
for n in [7,16,25,34,43,52,58]:check(E[n-1]['stage']=='Doeloefening',f'Target {n} labelled and present')
for n in [30,33,39,42]:check(len(E[n-1]['questions'])>=3,f'Exercise {n}: graphical practice before target')
student_assets=[x['file'] for x in json.loads((R/'QA/instructional-figures.json').read_text())]
answer_assets=[]
for e in E:
 f=e['answer_fig'];answer_assets+=f if isinstance(f,list) else [f] if f else []
check(len(student_assets)==32,'32 instructional figures');check(len(answer_assets)==12,'12 solution figure uses')
for name in set(student_assets+answer_assets):check((R/'_assets'/f'{name}.svg').exists() and (R/'_assets'/f'{name}.png').exists(),'Figure available: '+name)
check(not re.search(r'(QR[- ]?code|ga naar de website|bekijk online)',ss.get_text(),re.I),'No device-dependent student instruction')
for title in ['book-3-outline-v2(5).md','book-4-outline-v2(5).md']:
 original=Path('/mnt/data')/title;bundled=R/'sources'/title
 if original.exists():check(original.read_bytes()==bundled.read_bytes(),'Unchanged attached outline: '+title)

# Check the packaged source identity even outside the original chat container.
source_register=json.loads((R/'sources/source-register.json').read_text())
for source in source_register['sources']:
 if source['kind']=='user_attachment':
  close_path=R/source['path']
  check(close_path.exists(),'Bundled source present: '+source['path'])
  check(hashlib.sha256(close_path.read_bytes()).hexdigest()==source['sha256'],'Bundled source hash: '+source['path'])

# Read actual SVG geometry, not only plotting parameters.
ns={'s':'http://www.w3.org/2000/svg'}
def polygon_area(v):return abs(sum(v[i][0]*v[(i+1)%len(v)][1]-v[(i+1)%len(v)][0]*v[i][1] for i in range(len(v))))/2
def pts(st):return [tuple(map(float,x.split(','))) for x in st.split()]
G=json.loads((R/'QA/figure_geometry.json').read_text())
for g in G:
 root=ET.parse(R/'_assets'/(g['file']+'.svg')).getroot()
 for p in g['plots']:
  x,y,w,h=p['box'];xmax,ymax=p['xmax'],p['ymax']
  def X(q):return x+q*w/xmax
  def Y(z):return y+h-z*h/ymax
  for c in p['curves']:
   el=next(z for z in root.findall('.//s:polyline',ns) if z.get('data-curve')==c['name'] and z.get('data-panel')==p['id'])
   actual=pts(el.get('points'));expected=[(X(q),Y(z)) for q,z in c['endpoints']]
   check(all(abs(a-b)<1e-5 for pair,epair in zip(actual,expected) for a,b in zip(pair,epair)),g['file']+' actual curve coordinates / '+c['name'])
   check(all(abs(z-c['a']-c['b']*q)<1e-7 and -1e-6<=q<=xmax+1e-6 and -1e-6<=z<=ymax+1e-6 for q,z in c['endpoints']),g['file']+' endpoints on function and plot / '+c['name'])
  circles=[z for z in root.findall('.//s:circle',ns) if z.get('data-panel')==p['id']]
  check(len(circles)==len(p['points']),g['file']+' actual point count')
  for point,el in zip(p['points'],circles):
   check(abs(float(el.get('cx'))-X(point['q']))<1e-3 and abs(float(el.get('cy'))-Y(point['p']))<1e-3,g['file']+' actual point coordinates / '+point['name'])
   if point['curve']:
    c=next(z for z in p['curves'] if z['name']==point['curve']);close(point['p'],c['a']+c['b']*point['q'],g['file']+' point lies on '+c['name'])
  polygons=[z for z in root.findall('.//s:polygon',ns) if z.get('data-panel')==p['id']]
  for area,el in zip(p['areas'],polygons):
   av=pts(el.get('points'));expected=[(X(q),Y(z)) for q,z in area['vertices']]
   check(all(abs(a-b)<1e-4 for pair,epair in zip(av,expected) for a,b in zip(pair,epair)),g['file']+' actual area vertices / '+area['name'])
   close(polygon_area(av)/(w/xmax*h/ymax),area['area'],g['file']+' plotted economic area / '+area['name'])
 for lab in g['labels']:
  check(0<=lab['x']<=g['width'] and 0<lab['y']<=g['height'],g['file']+' label baseline in canvas / '+lab['text'])
# Additional independently specified important polygon areas.
area_expectations={'421_transfer':[200,100],'421_we':[200,100],'421_answer7':[400,1200,200],'424_loss':[50],'424_answer34':[100,200,200],'425_we_loss':[16],'425_answer43':[50,625,625],'424_answer33':[16,128,128],'425_answer42':[16,200,200]}
for name,expected in area_expectations.items():
 actual=[a['area'] for p in next(g for g in G if g['file']==name)['plots'] for a in p['areas']]
 check(len(actual)==len(expected),'Area count '+name)
 for i,(a,b) in enumerate(zip(actual,expected)):close(a,b,'Independent area expectation '+name+':'+str(i))

# PDF text bounds, page plan and navigation.
files={'student':('Boek_4_H2_Marktvormen_en_marktfalen',60),'answers':('Boek_4_H2_Antwoorden',24),'teacher':('Boek_4_H2_Docenteninformatie',9)}
pdf_summary={}
for kind,(stem,n) in files.items():
 d=fitz.open(R/'output'/(stem+'.pdf'));pdf_summary[kind]=len(d)
 check(len(d)==n,kind+' page count',len(d))
 if kind=='student':check(len(d)<=60,'Student <= 60-page cap')
 for i,p in enumerate(d):
  check(len(p.get_text().strip())>150,f'{kind} p{i+1} not empty')
  spans=[s for b in p.get_text('dict')['blocks'] if b['type']==0 for l in b['lines'] for s in l['spans']]
  bad=[s['text'] for s in spans if s['bbox'][0]<-0.5 or s['bbox'][1]<-0.5 or s['bbox'][2]>p.rect.width+.5 or s['bbox'][3]>p.rect.height+.5]
  check(not bad,f'{kind} p{i+1} all text within page',bad or None)
  check('\ufffd' not in p.get_text(),f'{kind} p{i+1} no replacement glyph')
  for link in p.get_links():
   if link['kind']==fitz.LINK_GOTO:check(0<=link['page']<len(d),f'{kind} p{i+1} internal link valid')
 check(all(1<=e[2]<=len(d) for e in d.get_toc()),kind+' PDF bookmarks resolve')
 if kind=='student':
  for pg,term in [(3,'welvaart'),(11,'korting'),(19,'merken'),(25,'schade'),(36,'profiteert'),(47,'instrument'),(53,'rekening'),(56,'Studio Solo'),(57,'Opgave 58'),(59,'Kies eerst'),(60,'Begrippenlijst')]:
   check(term.casefold() in d[pg-1].get_text().casefold(),f'Student navigation p{pg}: {term}')
  mp=json.loads((R/'QA'/(stem+'_page_map.json')).read_text());check(all(z['designed_pages']==[z['pdf_page']] for z in mp),'Every planned student page exactly one physical page')
 d.close()
report={'scope':'Local deterministic checks; not independent external review or classroom testing','pdf_pages':pdf_summary,'exercise_count':len(E),'subquestion_count':len(expected_ids),'instructional_figures':len(student_assets),'solution_figure_uses':len(answer_assets),'svg_files':len(G),'passed':sum(z['pass'] for z in checks),'failed':sum(not z['pass'] for z in checks),'checks':checks}
(R/'QA/validation_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print({k:v for k,v in report.items() if k!='checks'})
for z in checks:
 if not z['pass']:print('FAIL',z)
if report['failed']:raise SystemExit(1)
