"""Local artifact validation; deliberately not a replacement for repository gates."""
from pathlib import Path
from fractions import Fraction
from collections import Counter
import json, re, math, hashlib, xml.etree.ElementTree as ET
import fitz
from build import ROOT,PAGES
checks=[]
def require(name, condition, details=None):
    checks.append({'check':name,'passed':bool(condition),'details':details})
    if not condition:print('FAIL:',name,details)
def near(a,b,tol=1e-7):return abs(float(a)-float(b))<=tol
chapter=fitz.open(ROOT/'output/Boek_2_H1_Kosten_en_opbrengsten.pdf')
answers=fitz.open(ROOT/'output/Boek_2_H1_Antwoorden.pdf')
teacher=fitz.open(ROOT/'output/Boek_2_H1_Docenteninformatie.pdf')
require('Printed explanation plus every exercise <= 40 pages',len(chapter)<=40,{'pages':len(chapter),'answers_excluded':len(answers)})
mp=json.loads((ROOT/'output/page_map.json').read_text())
require('One physical page per designed page; no overflow leaves',len(mp)==len(PAGES) and all(x['designed_pages']==[str(x['pdf_page'])] for x in mp),mp)
expected_headings=['Uitgewerkt voorbeeld','Startopgaven','Begeleide inoefening','Zelfstandige oefening','Doeloefening','Denkertje / Bonusopgave','Herhaling / Herhaling en interleaving']
ansmd=(ROOT/'2.1 Kosten en opbrengsten – antwoorden.md').read_text()
for sec,n in [('2.1.1',10),('2.1.2',11),('2.1.3',10),('2.1.4',7)]:
    text='\n'.join(p['body'] for p in PAGES if p['section']==sec)
    found=sorted(set(map(int,re.findall(r'Opgave (\d+)',text))))
    require(f'{sec} sequential exercise numbers',found==list(range(1,n+1)),found)
    part=re.search(r'^# '+re.escape(sec)+r' [\s\S]*?(?=^# 2\.1\.|\Z)',ansmd,re.M).group()
    a_nums=list(map(int,re.findall(r'^## Opgave (\d+)',part,re.M)))
    require(f'{sec} all exercises answered exactly once',a_nums==list(range(1,n+1)),a_nums)
    if sec!='2.1.4':
        headings=re.findall(r'^## (.+)$',text,re.M)
        require(f'{sec} seven exact headings in canonical order',headings==expected_headings,headings)
        start=text.index('## Uitgewerkt voorbeeld');end=text.index('## Startopgaven')
        require(f'{sec} compact summary after worked example before Startopgaven','summary' in text[start:end])
whole='\n'.join(p['body'] for p in PAGES)+'\n'+ansmd
refs=set(re.findall(r'src="(_assets/[^\"]+)"',whole))
require('Every figure reference exists',all((ROOT/x).is_file() for x in refs),sorted(refs))
require('Every instructional figure has explicit alternate text',all('alt=' in tag for tag in re.findall(r'<img\b[^>]*>',whole)))
svg=list((ROOT/'_assets').glob('*.svg'));png=list((ROOT/'_assets').glob('*.png'))
require('Every SVG has a matching PNG',set(x.stem for x in svg)==set(x.stem for x in png),{'svg':len(svg),'png':len(png)})
require('No unused instructional root figures',set(x.stem for x in svg)==set(Path(x).stem for x in refs))
# Check the actual written SVG coordinates against the data used for their plots.
geometry=json.loads((ROOT/'_assets/geometry-data.json').read_text())
per={}
for g in geometry:per.setdefault(g['asset'],[]).append(g)
geoerrors=[]
for name,items in per.items():
    tree=ET.parse(ROOT/'_assets'/f'{name}.svg')
    polys=tree.findall('.//{http://www.w3.org/2000/svg}polyline')
    if len(polys)!=len(items):geoerrors.append([name,'curve count']);continue
    for poly,g in zip(polys,items):
        coords=[list(map(float,p.split(','))) for p in poly.attrib['points'].split()]
        l,r,t,b=g['mapping'];expected=[(l+x/g['xmax']*(r-l),b-y/g['ymax']*(b-t)) for x,y in g['points']]
        if len(coords)!=len(expected) or any(not near(x,u,0.001) or not near(y,v,0.001) for (x,y),(u,v) in zip(coords,expected)):
            geoerrors.append([name,g['curve']])
require('Drawn curve geometry matches recorded numerical data',not geoerrors,{'curves':len(geometry),'errors':geoerrors})
# Independently re-evaluate the functions behind all numerical curve samples.
def expected_y(asset,label,q):
    if asset=='2.1.1_fig_2':return {'TK':300+2*q,'TVK':2*q,'TCK':300}[label]
    if asset=='2.1.1_fig_3':return {'GTK':300/q+2,'GVK':2,'GCK':300/q}[label]
    specs={'2.1.2_fig_2':(250,2,5),'2.1.2_ex_1':(180,3,6),'2.1.2_ex_2':(120,1,4),'2.1.2_ex_3':(120,1,4),'2.1.2_ex_4':(250,4,10),'2.1.2_ex_5':(500,.8,1.5),'2.1.4_ex_1':(240,2,6),'2.1.4_ex_4':(240,2,6)}
    if asset in specs:
        f,v,p=specs[asset];return p*q if label.startswith('TO') else f+v*q
    if asset=='2.1.3_fig_2':return 80+q*q
    if asset in ('2.1.4_ex_2','2.1.4_ex_3'):
        if label.startswith('TO'):return 5*q
        if label=='TK vrijdag':return 1200+2*q
        return {700:2600,800:2900,900:3250,1000:3650}[int(q)]
    raise ValueError((asset,label,q))
formula_errors=[]
for g in geometry:
    for q,y in g['points']:
        if not near(expected_y(g['asset'],g['curve'],q),y):formula_errors.append([g['asset'],g['curve'],q,y])
require('All graph samples match independently evaluated economics functions',not formula_errors,{'samples':sum(len(g['points']) for g in geometry),'errors':formula_errors})
# Fixed/variable and average cost worked examples, practice and targets.
costcases=[('Fles & Co',300,2,[200,400],[700,1100]),('PlakLab',300,1,[150,300],[450,600]),('TasDruk',120,.5,[200,400],[220,320]),('SleutelStudio',120,1.5,[100,200],[270,420]),('FietsGlans',300,1,[200,400],[500,700]),('De Korenaar',500,.8,[500,1000],[900,1300]),('Boekenbinder',400,6,[100],[1000]),('ShirtSprint',600,5,[150],[1350]),('SmoothBox vrijdag',1200,2,[700],[2600])]
calculations=[]
for name,f,v,qs,tcs in costcases:
    results=[]
    for q,expected in zip(qs,tcs):
        total=f+v*q;require(f'{name} TK at Q={q}',near(total,expected))
        require(f'{name} average identity at Q={q}',near(f/q+v,total/q))
        results.append({'Q':q,'TCK':f,'TVK':v*q,'TK':total,'GCK':f/q,'GVK':v,'GTK':total/q})
    calculations.append({'name':name,'rows':results})
# Interval normalization, including unequal steps and all nonlinear targets.
intervals=[('Hoofduitleg',[0,10,30],[100,130,190],[0,80,240],[3,3],[8,8]),('Linoprint',[0,5,10,15],[120,130,140,150],[0,30,60,90],[2,2,2],[6,6,6]),('Atelier Boog',[0,2,4,6],[40,44,56,76],[0,24,48,72],[2,6,10],[12,12,12]),('HoesHandig',[0,10,20,30],[100,130,160,190],[0,80,160,240],[3,3,3],[8,8,8]),('PotAtelier',[0,2,4,6],[50,54,66,86],[0,40,80,120],[2,6,10],[20,20,20]),('SportLint',[0,10,30],[80,120,200],[0,90,270],[4,4],[9,9]),('StikSnel',[0,5,10,15],[90,100,110,120],[0,35,70,105],[2,2,2],[7,7,7]),('Keramiek Nova',[0,3,6,9],[60,69,96,141],[0,72,144,216],[3,9,15],[24,24,24]),('Linea',[0,10,20,30],[200,230,260,290],[0,80,160,240],[3,3,3],[8,8,8]),('Curva',[0,5,10,15],[100,125,200,325],[0,150,300,450],[5,15,25],[30,30,30]),('SkateService',[10,20,30],[260,320,410],[400,800,1200],[6,9],[40,40]),('SmoothBox zaterdag',[700,800,900,1000],[2600,2900,3250,3650],[3500,4000,4500,5000],[3,3.5,4],[5,5,5])]
for name,qs,tcs,tos,mks,mos in intervals:
    mk=[(b-a)/(v-u) for a,b,u,v in zip(tcs,tcs[1:],qs,qs[1:])]
    mo=[(b-a)/(v-u) for a,b,u,v in zip(tos,tos[1:],qs,qs[1:])]
    require(f'{name} interval MK and MO',all(near(a,b) for a,b in zip(mk,mks)) and all(near(a,b) for a,b in zip(mo,mos)),{'MK':mk,'MO':mo,'profit':[a-b for a,b in zip(tos,tcs)]})
# Exact fractions distinguish continuous intersections and first whole-unit no-loss.
for name,f,v,p,first in [('WafelWagen',250,2,5,84),('SokkenShop',180,3,6,60),('KaartKunst',120,1,4,40),('TheeTuin',180,1,4,60),('PetPret',250,4,10,42),('De Korenaar',500,'0.80','1.50',715),('Theater',500,2,8,84),('Puzzelverkoper',150,2,5,50),('ShirtSprint',600,5,11,100),('SmoothBox',1200,2,5,400)]:
    v=Fraction(str(v));p=Fraction(str(p));q=Fraction(f)/(p-v)
    require(name+' continuous and whole-unit break-even',math.ceil(q)==first and p*q==f+v*q and (p-v)*first-f>=0 and (p-v)*(first-1)-f<0,{'continuous_Q':str(q),'first_whole':first})
require('SmoothBox incremental profits',[(5-x)*100 for x in [3,3.5,4]]==[200,150,100])
require('Unsold muffins do not generate revenue',2*70-(60+.8*100)==0 and near(2*70-(60+.8*70),24))
student_text='\n'.join(p.get_text() for p in chapter)
require('No internal production-lane or production-range jargon in student PDF',not any(x.lower() in student_text.lower() for x in ['productiegebied','productiebereik','productierange','Part A','Part B','companion','QR-code','website','laptop']))
for label,doc in [('chapter',chapter),('answers',answers),('teacher',teacher)]:
    bad=[];tiny=[];artefacts=[]
    for i,p in enumerate(doc):
        words=p.get_text('words')
        if len(words)<90:tiny.append([i+1,len(words)])
        for x0,y0,x1,y1,txt,*_ in words:
            if x0<0 or y0<0 or x1>p.rect.width+0.1 or y1>p.rect.height+0.1:bad.append([i+1,txt,[x0,y0,x1,y1]])
        text=p.get_text()
        if '\ufffd' in text or '**' in text or '\x00' in text:artefacts.append(i+1)
    require(label+' no out-of-page text',not bad,bad)
    require(label+' no nearly empty continuation pages',not tiny,tiny)
    require(label+' no replacement glyphs or unrendered bold Markdown',not artefacts,artefacts)
require('Target source and questions are a facing-page spread',PAGES[31]['section']=='2.1.4' and 'Bron A' in PAGES[31]['body'] and 'Opgave 5' in PAGES[32]['body'])
require('Canonical manuscripts, not Python drafting files, drive chapter build',all((ROOT/x).exists() for x in json.loads((ROOT/'chapter-order.json').read_text())))
files={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (ROOT/'output').glob('*.pdf')}
report={'status':'LOCAL_CHECKS_PASSED' if all(x['passed'] for x in checks) else 'LOCAL_CHECKS_FAILED','scope':'artifact technical checks and independently recomputed numerical model checks; not repository governance, independent specialist review or classroom validation','checks':checks,'passed':sum(x['passed'] for x in checks),'failed':sum(not x['passed'] for x in checks),'counts':{'student_pages':len(chapter),'answer_pages':len(answers),'teacher_pages':len(teacher),'numbered_exercises':38,'worked_examples':3,'svg_png_pairs':len(svg)},'cost_calculation_records':calculations,'pdf_sha256':files}
(ROOT/'validation-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(report['status'],report['passed'],'passed;',report['failed'],'failed')
if report['failed']:raise SystemExit(1)
