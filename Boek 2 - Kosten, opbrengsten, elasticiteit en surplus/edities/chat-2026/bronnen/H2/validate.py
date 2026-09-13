"""Reproducible local checks; not the repository's formal integration validators.
Run after build.py and build_answers.py. Numerical fixtures are explicit so they
can be inspected independently of both the prose and the SVG drawing code.
"""
from pathlib import Path
from fractions import Fraction as F
import json,re,math,html,xml.etree.ElementTree as ET,hashlib,os
from bs4 import BeautifulSoup
from PIL import Image,ImageFont
import fitz
from build import ROOT,PAGES,render_markdown
RESULTS=[]
def check(name,condition,detail=''):
 RESULTS.append({'check':name,'passed':bool(condition),'detail':detail})
def eq(name,a,b):check(name,abs(float(a)-float(b))<1e-8,f'{a} == {b}')
def pct(new,old):return (F(str(new))-F(str(old)))/F(str(old))*100
def ratio(n,d):return F(str(n))/F(str(d))
def norm(s):return re.sub(r'\s+',' ',html.unescape(s)).strip()

# 1. Structure and counterpart answers.
counts={'2.2.1':10,'2.2.2':10,'2.2.3':11,'2.2.4':7}
route=['Uitgewerkt voorbeeld','Startopgaven','Begeleide inoefening','Zelfstandige oefening','Doeloefening','Denkertje / Bonusopgave','Herhaling / Herhaling en interleaving']
answers=(ROOT/'2.2 Elasticiteit – antwoorden.md').read_text()
sec_text={sec:'\n'.join(p['body'] for p in PAGES if p['section']==sec) for sec in counts}
for sec,n in counts.items():
 t=sec_text[sec]
 nums=set(map(int,re.findall(r'<b>Opgave (\d+)',t)))
 check(f'{sec} unique exercises',nums==set(range(1,n+1)),str(sorted(nums)))
 a=re.search(r'^# '+re.escape(sec)+r' [\s\S]*?(?=^# 2\.2\.|\Z)',answers,re.M).group()
 anums=list(map(int,re.findall(r'^## Opgave (\d+)',a,re.M)))
 check(f'{sec} complete answers',anums==list(range(1,n+1)),str(anums))
 if sec!='2.2.4':
  heads=re.findall(r'^## (.*)$',t,re.M);check(f'{sec} canonical seven headings',heads==route,str(heads))
  check(f'{sec} summary position',t.index('## Uitgewerkt voorbeeld')<t.index('class="box summary"')<t.index('## Startopgaven'))
  check(f'{sec} optional guided route','Heb je deze hulp niet nodig? Ga dan verder met Zelfstandige oefening.' in t)
  check(f'{sec} short route','Korte route: Startopgaven → Zelfstandige oefening → Doeloefening.' in t)
check('38 numbered exercises',sum(counts.values())==38)
full='\n'.join(p['body'] for p in PAGES)
check('no device dependency',not re.search(r'(scan de|QR-code|ga naar de website|open de companion|Part A|Part B)',full,re.I))
check('no legacy production-range term','productiegebied' not in full.lower())

# 2. Target wording, independent excerpts from the connected authority.
authority=json.loads((ROOT/'provenance/target_questions.json').read_text())
for sec,target in authority['targets'].items():
 printed=norm(BeautifulSoup(render_markdown(sec_text[sec]),'html.parser').get_text(' '))
 check(f'{sec} registry context',norm(target['context']) in printed)
 positions=[]
 for lab,points,prompt in target['questions']:
  clean=norm(prompt);check(f'{sec} target question {lab} verbatim',clean in printed)
  if clean in printed:positions.append(printed.index(clean))
 check(f'{sec} target question order',positions==sorted(positions) and len(positions)==len(target['questions']))
 totals={'2.2.1':9,'2.2.2':11,'2.2.3':16,'2.2.4':14}
 eq(f'{sec} target point total',sum(q[1] for q in target['questions']),totals[sec])

# 3. Price/revenue cases: old P, new P, old Q, new Q, expected %P, %Q, Ev, TO old, TO new.
cases=[
 ('RolVast',10,11,200,190,10,-5,-.5,2000,2090),
 ('SpringVrij',10,11,200,160,10,-20,-2,2000,1760),
 ('KlimStudio',20,22,400,380,10,-5,-.5,8000,8360),
 ('Museum retrieval',8,10,120,108,25,-10,-.4,960,1080),
 ('EscapeLab',20,22,1000,800,10,-20,-2,20000,17600),
 ('BroodBus',2,2.2,200,190,10,-5,-.5,400,418),
 ('StripRuil',10,9,100,120,-10,20,-2,1000,1080),
 ('StickerHub',5,6,400,280,20,-30,-1.5,2000,1680),
 ('RetroGames',12,10.8,200,240,-10,20,-2,2400,2592),
 ('Nova',10,12,500,420,20,-16,-.8,5000,5040),
 ('Pencils',2,2.2,1000,900,10,-10,-1,2000,1980),
 ('MuseumBos/PuzzelClub',10,11,100,95,10,-5,-.5,1000,1045),
 ('Finite counterexample',10,12,100,82,20,-18,-.9,1000,984),
 ('FotoWorkshop',20,22,50,40,10,-20,-2,1000,880),
 ('LeesLounge',10,12,100,95,20,-5,-.25,1000,1140),
 ('SneakerSwap',50,55,100,80,10,-20,-2,5000,4400),
 ('BordspelBar',8,10,500,450,25,-10,-.4,4000,4500),
 ('KaraokeKade',10,11,400,320,10,-20,-2,4000,3520),
 ('PlantenPop',20,19,100,110,-5,10,-2,2000,2090),
 ('StreamNow',20,22,1000,800,10,-20,-2,20000,17600),
 ('Course bonus',40,50,100,80,25,-20,-.8,4000,4000),
 ('Magazine',4,4.4,600,570,10,-5,-.5,2400,2508),
 ('Notebook',5,5.5,400,360,10,-10,-1,2000,1980),
 ('LunchCampus',4,4.4,1000,950,10,-5,-.5,4000,4180),
 ('WorkshopApp',20,22,200,170,10,-15,-1.5,4000,3740),
 ('SkillBox',16,18,250,230,12.5,-8,-.64,4000,4140),
 ('StreamPlus',10,12,50000,43000,20,-14,-.7,500000,516000),
 ('StudioScene',20,22,300,270,10,-10,-1,6000,5940)]
for name,po,pn,qo,qn,pp,qq,e,to,tn in cases:
 eq(name+' %P',pct(pn,po),pp);eq(name+' %Q',pct(qn,qo),qq)
 eq(name+' Ev',pct(qn,qo)/pct(pn,po),e)
 eq(name+' TO old',F(str(po))*F(str(qo)),to);eq(name+' TO new',F(str(pn))*F(str(qn)),tn)
expected_revenue=[('PuzzelClub',1000,1045,4.5),('FotoWorkshop',1000,880,-12),('Kraam',800,900,12.5),('LeesLounge',1000,1140,14),('SneakerSwap',5000,4400,-12),('BordspelBar',4000,4500,12.5),('KaraokeKade',4000,3520,-12),('Nova',5000,5040,.8),('StreamNow',20000,17600,-12),('Large counterexample',1000,984,-1.6),('Unitary finite example',6000,5940,-1)]
for name,old,new,result in expected_revenue:eq(name+' percent revenue',pct(new,old),result)

# 4. Ei/Ek ratio fixtures; deliberately include negative denominator cases.
ratios=[('Ei theory normal',5,10,.5),('Ei theory inferior',-5,10,-.5),('Ei theory luxury',20,10,2),('Train vs bus',6,10,.6),('Ink vs printer',-4,10,-.4),('WE scooter luxury',20,10,2),('WE scooter inferior',-5,10,-.5),('WE bicycle vs train',5,10,.5),('WE reservations vs train',-8,10,-.8),('Merksnacks',2,4,.5),('Budgetsoep',-2,4,-.5),('Hobbysets',8,4,2),('Wheels/skateboard',15,-10,-1.5),('Fruitbar soda',4,10,.4),('Fruitbar cup',-6,20,-.3),('Headphones',10,5,2),('Earphones',2,5,.4),('Players',-5,5,-1),('Portable/consoles',-5,-10,.5),('Controllers/consoles',15,-10,-1.5),('Target meal boxes',8,5,1.6),('Target noodles',-3,5,-.6),('Target tea',4,10,.4),('Target filters',-6,10,-.6),('Consumer group A',-5,10,-.5),('Consumer group B',15,10,1.5),('Drawing luxury',12,8,1.5),('Sketchbooks',4,8,.5),('Paper leftovers',-2,8,-.25),('Memory cards',-6,10,-.6),('SkillBox cross',3,10,.3),('Premium StreamPlus',15,8,1.875),('Budget StreamPlus',-4,8,-.5),('StreamPlus cross',5,12.5,.4),('Scene income',5,10,.5),('Scene cross',-2,5,-.4)]
for name,n,d,expected in ratios:eq(name,ratio(n,d),expected)

# 5. All multi-variable model scenarios and computed income elasticities.
functions=[
 ('DeelFiets',200,[-5,2,.01],[(10,15,20000,380),(10,15,22000,400),(10,20,20000,390)],20/38),
 ('StudioPas',200,[-2,1,.01],[(10,20,20000,400),(10,20,22000,420),(10,24,20000,404)],.5),
 ('ZwemPas',200,[-3,1,.02],[(10,30,10000,400),(10,30,11000,420),(10,36,10000,406)],.5),
 ('CreatiefPas',120,[-2,.5,.01],[(10,20,19000,300),(10,20,20900,319),(10,24,19000,302)],19/30),
 ('Target fitness',100,[-2,.5,.01],[(10,20,30000,390),(10,20,33000,420),(10,24,30000,392)],10/13),
 ('Hobby model',1000,[-20,10,.02],[(20,10,20000,1100),(20,10,22000,1140)],None),
 ('Target StreamPlus region',12000,[-400,300,.1],[(12,10,40000,14200),(12,10,42000,14400)],None),
 ('Scene region',500,[-10,2,.02],[(20,50,20000,800),(20,50,22000,840)],None)]
for name,c,coeff,rows,e in functions:
 for j,(*xs,q) in enumerate(rows):
  eq(name+f' scenario {j}',F(str(c))+sum(F(str(a))*F(str(v)) for a,v in zip(coeff,xs)),q)
  if j==1:check(name+' income scenario holds prices',xs[:2]==list(rows[0][:2]))
  if j==2:check(name+' resets Y and holds own P',xs[0]==rows[0][0] and xs[2]==rows[0][2])
 if e is not None:eq(name+' income elasticity',pct(rows[1][3],rows[0][3])/pct(rows[1][2],rows[0][2]),e)
for name,a,b in [('cost total',200+3*100,500),('cost average',(200+3*100)/100,5),('revenue',8*100,800),('profit',8*100-(200+3*100),300),('profit first',8000-6200,1800),('profit second',8600-7100,1500)]:eq(name,a,b)
eq('club growth',pct(880,800),10);eq('club decrease',pct(800,880),-100/11)

# 6. Every referenced figure exists as a vector/raster pair and matches its declared geometry.
refs=set(re.findall(r'src="(_assets/[^\"]+)"',full+answers))
for ref in sorted(refs):
 path=ROOT/ref;check(ref+' exists',path.exists());check(ref+' SVG pair',path.with_suffix('.svg').exists())
 w,h=Image.open(path).size;check(ref+' print resolution',w>=1500 and h>100,str((w,h)))
check('13 referenced teaching figures',len(refs)==13,str(len(refs)))
svgfiles=list((ROOT/'_assets').glob('*.svg'));check('no unreferenced SVG assets',len(svgfiles)==len(refs))
metrics=[]
fontpath=os.environ.get('FONT_REGULAR','/usr/share/fonts/truetype/lato/Lato-Regular.ttf');boldpath=os.environ.get('FONT_BOLD','/usr/share/fonts/truetype/lato/Lato-Bold.ttf')
if not Path(fontpath).is_file() or not Path(boldpath).is_file():
 raise SystemExit('Install local Lato fonts or set FONT_REGULAR and FONT_BOLD to your installed font files; no font files are distributed.')
for f in svgfiles:
 root=ET.parse(f).getroot();width=float(root.attrib['width']);height=float(root.attrib['height'])
 check(f.stem+' SVG accessible title',root.find('{http://www.w3.org/2000/svg}title') is not None)
 bad=[]
 for el in root.iter('{http://www.w3.org/2000/svg}text'):
  if 'transform' in el.attrib:continue
  sz=float(el.attrib['font-size']);font=ImageFont.truetype(boldpath if el.attrib.get('font-weight')=='bold' else fontpath,round(sz*10))
  tw=font.getlength(''.join(el.itertext()))/10;x=float(el.attrib['x']);y=float(el.attrib['y']);anchor=el.attrib.get('text-anchor','start')
  left=x-(tw if anchor=='end' else tw/2 if anchor=='middle' else 0)
  if left<-1 or left+tw>width+1 or y>height+1 or y-sz<-1:bad.append(''.join(el.itertext()))
 check(f.stem+' text within SVG',not bad,str(bad))
geo=json.loads((ROOT/'_assets/geometry-data.json').read_text())
for g in geo:
 if g['type']=='revenue_rectangles':
  for j,p in enumerate(g['panels']):
   l,r,t,b=p['plot'];x,y,w,h=p['rectangle'];eq(f'rectangle {j} area',w*h/((r-l)/p['xmax']*((b-t)/p['ymax'])),p['p']*p['q'])
 if g['type']=='income_response_bars':
  for j,(d,e) in enumerate(zip(g['demand_percentages'],g['ei'])):eq(f'income visual {j}',d/g['income_percentage'],e)
 if g['type']=='separate_scenarios':
  for j,row in enumerate([g['base']]+g['scenarios']):eq('visual scenario '+str(j),200-5*row['Px']+2*row['Pz']+.01*row['Y'],row['Qx'])

# 7. Rendered PDF page budget, headings, units, printable bounds, no orphan planned pages.
student=fitz.open(ROOT/'output/Boek_2_H2_Elasticiteit.pdf');ans=fitz.open(ROOT/'output/Boek_2_H2_Antwoorden.pdf')
check('student <=40 pages',len(student)<=40,str(len(student)))
check('student exactly36 designed pages',len(student)==len(PAGES)==36)
page_map=json.loads((ROOT/'output/page_map.json').read_text());check('no designed-page overflow',all(p['designed_pages']==[str(p['pdf_page'])] for p in page_map))
check('facing target source page32','Bron A' in student[31].get_text() and 'StreamPlus' in student[31].get_text())
check('facing target question page33','Selecteer uit bron A' in student[32].get_text())
teacher=fitz.open(ROOT/'output/Boek_2_H2_Docenteninformatie.pdf')
check('teacher six pages',len(teacher)==6)
for label,doc in [('student',student),('answers',ans),('teacher',teacher)]:
 bad=[];empty=[]
 for i,page in enumerate(doc,1):
  if len(page.get_text().strip())<50:empty.append(i)
  for b in page.get_text('dict')['blocks']:
   for line in b.get('lines',[]):
    for span in line['spans']:
     x0,y0,x1,y1=span['bbox'];tx=span['text']
     if x0<12 or x1>page.rect.width-10 or y0<10 or y1>page.rect.height-10 or '\ufffd' in tx:bad.append((i,tx))
 check(label+' printable text bounds and glyphs',not bad,str(bad[:10]));check(label+' no empty pages',not empty,str(empty))
 check(label+' A4',all(abs(p.rect.width-595.276)<1 and abs(p.rect.height-841.89)<1 for p in doc))

# Additional print-label and local export checks.
answer_text='\n'.join(p.get_text() for p in ans)
start=answer_text.index('Opgave 5 · Doeloefening: StreamPlus')
end=answer_text.index('Opgave 6 · Denkertje: DataLab',start)
labels=re.findall(r'(?m)^([1-6])\)',answer_text[start:end])
check('mixed-target answer labels 1 through 6',labels==list('123456'),str(labels))
check('no font files distributed',not any(p.suffix.lower() in ['.ttf','.otf','.woff','.woff2'] for p in ROOT.rglob('*')))
exports=json.loads((ROOT/'paragraph-exports.json').read_text())
for sec,info in exports.items():
 check(sec+' export exercise count',info['exercise_count']==counts[sec])
 folder=next((ROOT/'paragrafen').glob(sec+' *'))
 for kind in ['opgaven','antwoorden']+(['paragraaf'] if sec!='2.2.4' else []):
  pdf=next(folder.glob('* – '+kind+'.pdf'))
  check(sec+' '+kind+' PDF nonempty',len(fitz.open(pdf))>0)
report={'scope':'Local structural, arithmetic, target-wording and PDF preflight checks; not an independent pedagogical review or official repository gate.', 'student_pages':len(student),'answer_pages':len(ans),'teacher_pages':len(teacher),'exercises':38,'figures':13,'passed':sum(r['passed'] for r in RESULTS),'failed':sum(not r['passed'] for r in RESULTS),'checks':RESULTS}
(ROOT/'validation-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(f"Local validation: {report['passed']} passed, {report['failed']} failed; student {len(student)} pages, answers {len(ans)} pages")
for r in RESULTS:
 if not r['passed']:print('FAIL',r['check'],r['detail'])
raise SystemExit(1 if report['failed'] else 0)
