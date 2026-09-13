"""Deterministic local checks, not a replacement for independent content review.
Expected answers below were fixed separately from the SVG generator. The graph
areas are checked with analytic antiderivatives and independent shoelace area.
Run after build_all.py or directly after all PDFs and exports exist.
"""
from pathlib import Path
import re,json,math,hashlib,xml.etree.ElementTree as ET
import fitz
from PIL import Image
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parent
CHECKS=[]
def check(name,condition,detail=''):
    CHECKS.append({'check':name,'passed':bool(condition),'detail':str(detail)})
def close(name,actual,expected):
    check(name,math.isclose(actual,expected,abs_tol=1e-7,rel_tol=1e-9),f'actual={actual:g}; expected={expected:g}')
def norm(s):return re.sub(r'\s+',' ',s).strip()

# Independently specified numerical scenarios: a-bQ demand, c+dQ supply.
# price/cap=None means free equilibrium. Values are verified against fixed keys.
CASES=[
('theory skate',30,.5,None,None,10,None,{'Q':40,'CS':400}),
('WE escaperoom',20,.25,None,None,10,None,{'Q':40,'CS':200}),
('231.3 klimhal',24,.4,None,None,8,None,{'Q':40,'CS':320}),
('231.4 museum',18,.3,None,None,6,None,{'Q':40,'CS':240}),
('231.6 zwemmen',18,.2,None,None,8,None,{'Q':50,'CS':250}),
('231.7 boeken',16,.1,None,None,6,None,{'Q':100,'CS':500,'TO':600}),
('231.8 target',50,.5,None,None,20,None,{'Q':60,'CS':900}),
('231.9 counterexample',20,.25,None,None,5,None,{'Q':60,'CS':450}),
('theory posters',40,1,10,.5,None,None,{'Q':20,'P':20,'CS':200,'PS':100,'TS':300}),
('WE notitieboeken',24,.5,4,.5,None,None,{'Q':20,'P':14,'CS':100,'PS':100,'TS':200}),
('232.1 ophalen',18,1,6,.5,None,None,{'Q':8,'P':10}),
('232.3 bloemen',30,1,6,.5,None,None,{'Q':16,'P':14,'CS':128,'PS':64,'TS':192}),
('232.4 handdoeken',32,.5,8,.5,None,None,{'Q':24,'P':20,'CS':144,'PS':144,'TS':288}),
('232.6 bekers',36,.5,6,.5,None,None,{'Q':30,'P':21,'CS':225,'PS':225,'TS':450}),
('232.8 target',50,.5,5,.25,None,None,{'Q':60,'P':20,'CS':900,'PS':450,'TS':1350}),
('theory posters cap',40,1,10,.5,22,12,{'Qd':18,'Qs':24,'Q':12,'Dq':28,'Sq':16,'CS':144,'PS':108,'TS':252,'loss':48}),
('WE workshop',30,1,6,1,20,8,{'Qe':12,'Pe':18,'TSfree':144,'Qd':10,'Qs':14,'Q':8,'Dq':22,'Sq':14,'CS':48,'PS':80,'TS':128,'loss':16}),
('233.3 zaal',24,.5,4,.5,14,12,{'Qe':20,'Pe':14,'TSfree':200,'Qd':20,'Qs':20,'Dq':18,'Sq':10,'CS':84,'PS':84,'TS':168,'loss':32}),
('233.4 kajak',30,.5,6,.5,20,16,{'Qe':24,'Pe':18,'TSfree':288,'Qd':20,'Qs':28,'Dq':22,'Sq':14,'CS':96,'PS':160,'TS':256,'loss':32}),
('233.5 schilder',40,1,10,1,26,10,{'Qe':15,'Pe':25,'TSfree':225,'Qd':14,'Qs':16,'Dq':30,'Sq':20,'CS':90,'PS':110,'TS':200,'loss':25}),
('233.6 target',50,.5,5,.25,25,40,{'Qe':60,'Pe':20,'TSfree':1350,'Qd':50,'Qs':80,'Dq':30,'Sq':15,'CS':600,'PS':600,'TS':1200,'loss':150}),
('234.1 surf',60,1,12,1,None,None,{'Q':24,'P':36,'CS':288,'PS':288,'TS':576}),
('234.2 plants',48,1,12,.5,26,16,{'Qe':24,'Pe':24,'TSfree':432,'Qd':22,'Qs':28,'Dq':32,'Sq':20,'CS':224,'PS':160,'TS':384,'loss':48}),
('234.3 target',80,1,20,.5,45,30,{'Qe':40,'Pe':40,'TSfree':1200,'Qd':35,'Qs':50,'Dq':50,'Sq':35,'CS':600,'PS':525,'TS':1125,'loss':75}),
]
for name,a,b,c,d,p,q,expected in CASES:
    values={}
    if c is not None:
        qe=(a-c)/(b+d);pe=a-b*qe
        values.update(Qe=qe,Pe=pe,TSfree=(a-c)*qe-(b+d)*qe*qe/2)
        if p is None:p=pe
    if q is None:q=(a-p)/b
    values.update(Q=q,P=p,Qd=(a-p)/b,Dq=a-b*q,CS=(a-p)*q-b*q*q/2,TO=p*q)
    if c is not None:
        values.update(Qs=(p-c)/d,Sq=c+d*q,PS=(p-c)*q-d*q*q/2)
        values['TS']=values['CS']+values['PS'];values['loss']=values['TSfree']-values['TS']
        close(name+' / cancellation of transfer',values['TS'],(a-c)*q-(b+d)*q*q/2)
        if q<qe-1e-7:
            check(name+' / cap strictly binding',q<values['Qd'] and q<values['Qs'])
            close(name+' / loss triangle',(qe-q)*(values['Dq']-values['Sq'])/2,values['loss'])
    for key,expected_val in expected.items():close(name+' / '+key,values[key],expected_val)

# Target table points and Pareto witnesses, independently specified.
for label,a,b,c,d,q,p,ewtp,emc,bgain,sgain in [
('poster13',40,1,10,.5,13,22,27,16.5,5,5.5),
('workshop9',30,1,6,1,9,20,21,15,1,5),
('kajak17',30,.5,6,.5,17,20,21.5,14.5,1.5,5.5),
('schilder11',40,1,10,1,11,26,29,21,3,5),
('target41',50,.5,5,.25,41,25,29.5,15.25,4.5,9.75),
('planten17',48,1,12,.5,17,26,31,20.5,5,5.5),
('target31',80,1,20,.5,31,45,49,35.5,4,9.5)]:
    close(label+' / WTP',a-b*q,ewtp);close(label+' / MK',c+d*q,emc)
    close(label+' / buyer gain',a-b*q-p,bgain);close(label+' / seller gain',p-c-d*q,sgain)
    check(label+' / both benefit',bgain>0 and sgain>0)
for label,a,b,c,d,q,expected in [('target Q50',50,.5,5,.25,50,7.5),('target Q70',50,.5,5,.25,70,-7.5),('flowers Q10',30,1,6,.5,10,9),('flowers Q20',30,1,6,.5,20,-6),('cups Q20',36,.5,6,.5,20,10),('cups Q40',36,.5,6,.5,40,-10),('surf Q30',60,1,12,1,30,-12)]:
    close(label+' / marginal difference',a-b*q-c-d*q,expected)
for name,actual,expected in [
('231.1 Q',(16-6)/.2,50),('231.1 area',.5*50*10,250),('231.2 individual',18-12,6),('231.5 prints',.5*30*(17-5),180),
('231.10 percentage',(460-400)/400*100,15),('231.11 TK',200+3*100,500),('231.11 GTK',(200+3*100)/100,5),
('232.2 buyer',12-9,3),('232.2 seller',9-5,4),('232.5 combined change',(16-5)-(14-6),3),('232.7 TS',300+100,400),
('232.9 TS p15',(30-15)+(15-10),20),('232.9 TS p25',(30-25)+(25-10),20),('232.10 MK',(280-240)/(50-40),4),('232.11 Ev',-5/10,-.5),
('233.1 CS',.5*20*(25-15),100),('233.1 PS',.5*20*(15-5),100),('233.2 net positive not Pareto',8-3,5),('233.8 profit',900-760,140),('233.9 area',.5*80*12,480),
('234.4 efficient assignment',30+24-5-11,38),('234.4 costly assignment',30+24-5-20,29),('234.5 Ev',((90-100)/100)/((12-10)/10),-.5),('234.5 old TO',10*100,1000),('234.5 new TO',12*90,1080),('234.6 profit',1000-600-250,150),('234.7 loss B',800-350-430,20)]:
    close(name,actual,expected)

manuscripts={p.name.split()[0]:p.read_text() for p in (ROOT/'manuscript').glob('2.3.[1-4]*')}
answers=(ROOT/'2.3 Surplus en welvaart – antwoorden.md').read_text()
canon=['Uitgewerkt voorbeeld','Startopgaven','Begeleide inoefening','Zelfstandige oefening','Doeloefening','Denkertje / Bonusopgave','Herhaling / Herhaling en interleaving']
all_student_ids=set();all_answer_ids=set()
for pid,text in sorted(manuscripts.items()):
    actual=set(map(int,re.findall(r'\*\*Opgave (\d+)\b',text)))
    expected=set(range(1,{'2.3.1':12,'2.3.2':12,'2.3.3':10,'2.3.4':8}[pid]))
    check(pid+' / student exercise numbers',actual==expected,sorted(actual))
    section=re.search(r'^# '+re.escape(pid)+r' [\s\S]*?(?=^# |\Z)',answers,re.M).group(0)
    ansnums=set(map(int,re.findall(r'^## Opgave (\d+)\b',section,re.M)))
    check(pid+' / all answers present',ansnums==actual,sorted(ansnums))
    all_student_ids|={(pid,i) for i in actual};all_answer_ids|={(pid,i) for i in ansnums}
    if pid!='2.3.4':
        headings=re.findall(r'^## (.+)$',text,re.M)
        check(pid+' / canonical seven sections',headings==canon,headings)
        check(pid+' / summary in correct place',text.index('## Uitgewerkt voorbeeld')<text.index('class="box summary"')<text.index('## Startopgaven'))
        check(pid+' / optional support note','Heb je deze hulp niet nodig? Ga dan verder met Zelfstandige oefening.' in text)
    # Compare literal subquestion labels in student and answer blocks.
    for no in actual:
        matches=list(re.finditer(r'\*\*Opgave '+str(no)+r'\b[^\n]*\*\*',text))
        subtext=''
        for match in matches:
            rest=text[match.end():];stop=re.search(r'\*\*Opgave \d+\b',rest)
            subtext+=rest[:stop.start()] if stop else rest
        student_labels=re.findall(r'^([a-z]|[1-9])\) ',subtext,re.M)
        ansmatch=re.search(r'^## Opgave '+str(no)+r'\b[^\n]*\n([\s\S]*?)(?=^## Opgave |\Z)',section,re.M)
        anslabels=re.findall(r'^([a-z]|[1-9])\) ',ansmatch.group(1),re.M)
        check(f'{pid}.{no} / subanswer labels',student_labels==anslabels,f'{student_labels} / {anslabels}')
check('38 complete exercises',len(all_student_ids)==38 and all_student_ids==all_answer_ids)

T=json.loads((ROOT/'provenance/target-transcription.json').read_text())['targets']
count=0
for pid,t in T.items():
    check(pid+' / source target context',norm(t['context']) in norm(manuscripts[pid]))
    for i,q in enumerate(t['questions'],1):
        check(f'{pid} / source target question {i}',norm(q) in norm(manuscripts[pid]));count+=1
check('22 source target subquestions retained',count==22)
check('No leaked target loss in student chapter',not re.search(r'€\s*75\b',manuscripts['2.3.4']))

all_text='\n'.join(p.read_text() for p in (ROOT/'manuscript').glob('*.md'))
soup=BeautifulSoup(all_text,'html.parser')
refs={img.get('src') for img in soup.find_all('img')}
check('27 instructional student figures',len(refs)==27,len(refs))
for img in soup.find_all('img'):
    check('Student image alt / '+img.get('src',''),bool(img.get('alt','').strip()))
for path in refs|set(re.findall(r'src="([^"]+)"',answers)):
    check('Image reference / '+path,(ROOT/path).is_file())
for phrase in ['Part A','Part B','companion','QR-code','Ga naar de website','productiegebied']:
    check('No internal/distracting wording / '+phrase,phrase not in all_text)

DATA=json.loads((ROOT/'_assets/geometry-data.json').read_text())
check('38 paired figures',len(DATA)==38 and len(list((ROOT/'_assets').glob('*.svg')))==38)
for g in DATA:
    stem=g['asset'];svg=ROOT/'_assets'/f'{stem}.svg';png=svg.with_suffix('.png')
    tree=ET.parse(svg).getroot();check(stem+' / PNG pair',png.exists())
    with Image.open(png) as im:check(stem+' / raster size',im.width>=1500 and im.height>0,f'{im.width}×{im.height}')
    check(stem+' / title and viewBox',tree.find('{http://www.w3.org/2000/svg}title') is not None and bool(tree.get('viewBox')))
    if g['type']!='market':continue
    a,b,c,d,p,q=[g[k] for k in ['a','b','c','d','price','quantity']]
    if c is not None:
        close(stem+' / equilibrium on demand',a-b*g['qe'],g['pe'])
        close(stem+' / equilibrium on supply',c+d*g['qe'],g['pe'])
    for pol in g['polygons']:
        pts=pol['points'];shoelace=abs(sum(pts[i][0]*pts[(i+1)%len(pts)][1]-pts[(i+1)%len(pts)][0]*pts[i][1] for i in range(len(pts))))/2
        if pol['label']=='CS':expected=(a-p)*q-b*q*q/2
        elif pol['label']=='PS':expected=(p-c)*q-d*q*q/2
        else:expected=(a-c)*g['qe']-(b+d)*g['qe']**2/2-((a-c)*q-(b+d)*q*q/2)
        close(stem+' / '+pol['label']+' polygon area',shoelace,expected)
        check(stem+' / '+pol['label']+' vertices in plot',all(-1e-8<=x<=g['xmax']+1e-8 and -1e-8<=y<=g['ymax']+1e-8 for x,y in pts))
        # Verify the actual serialized SVG pixel vertices against source-space coordinates.
        svgpoly=tree.findall('{http://www.w3.org/2000/svg}polygon')[g['polygons'].index(pol)]
        got=[tuple(map(float,z.split(','))) for z in svgpoly.get('points').split()]
        L,R,T0,B=g['plot'];want=[(L+x/g['xmax']*(R-L),B-y/g['ymax']*(B-T0)) for x,y in pts]
        check(stem+' / '+pol['label']+' serialized geometry',len(got)==len(want) and all(abs(x-x2)<.001 and abs(y-y2)<.001 for (x,y),(x2,y2) in zip(got,want)))

for stem,pages in [('Surplus_en_welvaart',38),('Antwoorden',17),('Docenteninformatie',6)]:
    path=ROOT/'output'/f'Boek_2_H3_{stem}.pdf'
    with fitz.open(path) as doc:
        check(stem+' / page count',len(doc)==pages,len(doc))
        if stem=='Surplus_en_welvaart':check('Student print cap',len(doc)<=40)
        for i,page in enumerate(doc,1):
            text=page.get_text()
            check(f'{stem} p{i} / text and glyphs',len(text.strip())>50 and '\ufffd' not in text)
            spans=[s for b in page.get_text('dict')['blocks'] if 'lines' in b for l in b['lines'] for s in l['spans']]
            outside=[s['text'] for s in spans if s['bbox'][0]<-1 or s['bbox'][1]<-1 or s['bbox'][2]>page.rect.width+1 or s['bbox'][3]>page.rect.height+1]
            check(f'{stem} p{i} / text inside page',not outside,outside)
with fitz.open(ROOT/'output/Boek_2_H3_Antwoorden.pdf') as answer_pdf:
    rendered_answer_text='\n'.join(page.get_text() for page in answer_pdf)
    for label in range(1,7):
        check(f'Mixed target rendered subanswer {label}', bool(re.search(r'^'+str(label)+r'\) ',rendered_answer_text,re.M)))
for file,count in [('page_map.json',38),('teacher_page_map.json',6)]:
    page_map=json.loads((ROOT/'output'/file).read_text())
    check(file+' / no overflow pages',len(page_map)==count and all(row['designed_pages']==[str(row['pdf_page'])] for row in page_map))

if (ROOT/'paragrafen/manifest.json').exists():
    for spec in json.loads((ROOT/'paragrafen/manifest.json').read_text()):
        folder=ROOT/spec['folder'];pid=spec['id']
        kinds=['opgaven','antwoorden']+(['paragraaf'] if spec['theory'] else [])
        for kind in kinds:
            for suffix in ['md','pdf']:
                files=list(folder.glob(f'* – {kind}.{suffix}'))
                check(pid+' / export '+kind+'.'+suffix,len(files)==1 and files[0].stat().st_size>200)
else:check('Paragraph exports present',False)
check('No bundled font files',not any(p.suffix.lower() in {'.ttf','.otf','.woff','.woff2'} for p in ROOT.rglob('*')))
passed=sum(c['passed'] for c in CHECKS);failed=len(CHECKS)-passed
report={'scope':'Local deterministic author checks. Not independent specialist review or platform CI.','passed':passed,'failed':failed,'checks':CHECKS,'outputs':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (ROOT/'output').glob('*.pdf')}}
(ROOT/'QA/validation-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
lines=['# Lokale validatie',f'\n{passed} controles geslaagd; {failed} mislukt.','\nGeen onafhankelijk specialistenoordeel of platform-CI.','\n## Mislukte controles']
lines += [f"- {c['check']}: {c['detail']}" for c in CHECKS if not c['passed']] or ['Geen.']
(ROOT/'QA/VALIDATION.md').write_text('\n'.join(lines)+'\n')
print(f'Local checks: {passed} passed / {failed} failed')
for c in CHECKS:
    if not c['passed']:print('FAIL:',c['check'],c['detail'])
raise SystemExit(1 if failed else 0)
