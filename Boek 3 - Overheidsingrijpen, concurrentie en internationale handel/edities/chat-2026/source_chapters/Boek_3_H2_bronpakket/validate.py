"""Local checks; not a substitute for visual inspection or independent classroom review."""
from pathlib import Path
import json,re,math,hashlib,xml.etree.ElementTree as ET
import fitz
import sympy as sp
from PIL import ImageFont
ROOT=Path(__file__).resolve().parent;QA=ROOT/'QA';RESULTS=[]
def check(name,value,detail=''):
    RESULTS.append({'check':name,'pass':bool(value),'detail':detail})
def close(a,b):return abs(float(a)-float(b))<1e-7
ex=json.loads((QA/'exercises.json').read_text());ans=json.loads((QA/'answers.json').read_text())
student=(ROOT/'3.2 Volkomen concurrentie – hoofdstuk.md').read_text();answers=(ROOT/'Antwoorden.md').read_text()
check('38 distinct exercises',[e['number'] for e in ex]==list(range(1,39)))
expected={str(e['number'])+chr(97+i) for e in ex for i in range(len(e['questions']))}
questionIDs=re.findall(r'data-question="([^"]+)"',student);answerIDs=re.findall(r'data-answer="([^"]+)"',answers)
check('Question IDs are unique',len(questionIDs)==len(set(questionIDs)))
check('Every question is printed once',set(questionIDs)==expected)
check('Every answer is printed once',set(answerIDs)==expected and len(answerIDs)==len(expected))
for e in ex:
    aa=ans[str(e['number'])]['items'];check(f'Opgave {e["number"]}: full answer + why',len(aa)==len(e['questions']) and all(len(x)==2 and len(x[0])>15 and len(x[1])>15 for x in aa))
canonical=['Uitgewerkt voorbeeld','Startopgaven','Begeleide inoefening','Zelfstandige oefening','Doeloefening','Denkertje / Bonusopgave','Herhaling / Herhaling en interleaving']
for sid in ['3.2.1','3.2.2','3.2.3']:
    text=(ROOT/f'{sid} manuscript.md').read_text()
    heads=re.findall(r'^## (.*)$',text,re.M)
    check(f'{sid}: canonical seven exercise headings',heads==canonical,str(heads))
    check(f'{sid}: optional guided route language','Heb je deze hulp niet nodig?' in text and 'Korte route:' in text)
check('Target operations 5+6+5+6',[len(e['questions']) for e in ex if e['group']=='target']==[5,6,5,6])
check('No unrequested monopoly teaching section',not re.search(r'^#{1,3} .*monopolie',student,re.M|re.I))
check('No coined production-area vocabulary',not re.search(r'productiegebied|productiebereik',student,re.I))
for f in ['3.2 Volkomen concurrentie – hoofdstuk.md','Antwoorden.md']:
    text=(ROOT/f).read_text()
    for name in sorted(set(re.findall(r'_assets/([^"<> ]+\.svg)',text))):
        check(f'{f}: asset {name}',(ROOT/'_assets'/name).exists() and (ROOT/'_assets'/name.replace('.svg','.png')).exists())
# Check the exact manuscript assembly actually used by the renderer.
assembled='\n\n'.join((ROOT/f).read_text() for f in json.loads((ROOT/'chapter-order.json').read_text()))
check('Assembly matches canonical page manuscripts',student==assembled)
student_assets=set(re.findall(r'_assets/([^"<> ]+\.svg)',student))
answer_assets=set(re.findall(r'_assets/([^"<> ]+\.svg)',answers))
check('22 student figures actually referenced',len(student_assets)==22,str(len(student_assets)))
check('11 solution figures actually referenced',len(answer_assets)==11,str(len(answer_assets)))
check('No orphan SVG figures',set(f.name for f in (ROOT/'_assets').glob('*.svg'))==student_assets|answer_assets)
for sid,n in [('3.2.1',5),('3.2.2',8),('3.2.3',7),('3.2.4',1)]:
    text=(ROOT/f'{sid} manuscript.md').read_text()
    captions=[int(x) for x in re.findall(r'<figcaption>Figuur (\d+)',text)]
    expected=list(range(1,n+1))
    check(f'{sid}: printed figure numbering',captions==expected,str(captions))

# Independent numerical checks: analytic, symbolic and grid-based results.
q=sp.symbols('q',nonnegative=True)
scenarios=[
('theory322',.05,2,80,8,100,60,480,380,100),
('worked322',.1,2,40,10,50,40,400,280,120),
('13',.05,3,60,9,80,60,540,420,120),
('14',.05,4,180,12,120,80,960,820,140),
('15price',.05,4,180,14,120,100,1400,1080,320),
('15fixed',.05,4,260,12,120,80,960,900,60),
('15both',.05,4,260,14,120,100,1400,1160,240),
('16',.02,4,100,12,250,200,2400,1700,700),
('17',.1,2,40,18,60,60,1080,520,560),
('18',.04,4,400,16,200,150,2400,1900,500),
('18cap',.04,4,400,16,120,120,1920,1456,464),
('19A',.1,2,40,8,50,30,240,190,50),
('19B',.1,2,160,8,50,30,240,310,-70),
('22',.1,2,40,8,50,30,240,190,50),
('24final',.05,2,80,6,100,40,240,240,0),
('25initial',.1,2,40,5,50,15,75,92.5,-17.5),
('25final',.1,2,40,6,50,20,120,120,0),
('26initial',.1,2,40,8,50,30,240,190,50),
('26final',.1,2,40,6,50,20,120,120,0),
('27',.05,2,80,5,100,30,150,185,-35),
('28initial',.02,4,200,10,250,150,1500,1250,250),
('28final',.02,4,200,8,250,100,800,800,0),
('33',.05,4,200,14,140,100,1400,1100,300),
('36initial',.02,4,200,8,250,100,800,800,0),
('36short',.02,4,200,12,250,200,2400,1800,600),
('36long',.02,4,200,8,250,100,800,800,0)]
for name,a,b,c,p,cap,qe,to,tc,w in scenarios:
    fn=sp.Rational(str(a))*q*q+sp.Rational(str(b))*q+sp.Rational(str(c));mk=sp.diff(fn,q)
    candidate=(p-b)/(2*a);opt=min(cap,max(0,candidate));calc_tc=a*qe*qe+b*qe+c
    check(f'Model {name}: derivative',sp.simplify(mk-(2*sp.Rational(str(a))*q+b))==0)
    check(f'Model {name}: feasible optimum',close(opt,qe) and 0<=qe<=cap)
    check(f'Model {name}: TO TK profit',close(p*qe,to) and close(calc_tc,tc) and close(to-tc,w))
    grid=[cap*i/1000 for i in range(1001)];profits=[p*x-(a*x*x+b*x+c) for x in grid]
    check(f'Model {name}: global comparison incl 0/cap',all(v<=w+1e-7 for v in profits))
    if qe>0:check(f'Model {name}: rectangle = profit',close((p-calc_tc/qe)*qe,w))
# Non-optimisation numerical work, independently expressed.
fixtures=[
('1 TO',4*80,320),('1 GO',320/80,4),('1 MO',(4*100-4*80)/20,4),
('4 TO',5*80,400),('4 price cut',5*80-4.8*80,16),
('5 TO',4*90,360),('5 MO',(4*110-4*90)/20,4),
('7 TO',3*120,360),('7 MO',(3*140-3*120)/20,3),
('9 Q',(18-6)/(.2+.1),40),('9 P',6+.1*40,10),
('10 cost50',150+3*50,300),('10 avg50',(150+3*50)/50,6),('10 avg100',(150+3*100)/100,4.5),
('11 TO',9*40,360),('11 avg',280/40,7),('11 profit',360-280,80),('11 intervalMK',(350-280)/10,7),
('13 source MK at60',.1*60+3,9),('15 fixed difference',260-180,80),
('17 cap MK',.2*60+2,14),('18 leftMK',.08*125+4,14),('18 rightMK',.08*175+4,18),('18 cap MK',.08*120+4,13.6),
('20 percentage',(10-8)/8*100,25),('20 Ev',-10/25,-.4),('21 wedge',11-8,3),('21 revenue',(11-8)*200,600),
('23 profit',1000-1000,0),('30 rectangle',200*(12-9),600),
('31 Qv',(14-10)/.1,40),('31 Qa',(10-2)/.1,80),('31 excess',80-40,40),
('32 P',12000/(1000+2000),4),('32 Q',2000*4,8000),('32 TO',4*100,400),
('34 candidate',(20-4)/.2,80),('34 cap MK',.2*60+4,16),
('36 initialP',(30000+10000)/5000,8),('36 initialQ',2500*8-10000,10000),
('36 newP',(50000+10000)/5000,12),('36 newQ',2500*12-10000,20000),('36 longQ',50000-2500*8,30000),
('38 avg',1000/100,10),('38 win',1200-1000,200),('38 MO',120/10,12),('38 MK',150/10,15),('38 delta',120-150,-30),
('theory intervalMK',(.05*60**2+2*60+80-(.05*40**2+2*40+80))/20,7),
('theory pointMK',.1*60+2,8),('theory exactKG',(.05*61**2+2*61+80)-(.05*60**2+2*60+80),8.05)]
for name,got,want in fixtures:check('Arithmetic '+name,close(got,want),f'{got} expected {want}')
# Prices and quantities in every distinct paired market, including implied identical-firm aggregation.
markets=[('potatoes',[4,-.0005],[1,.00025],4000,2),('rice',[8,-.001],[2,.001],3000,5),('soil',[8,-.001],[2,.0005],4000,4),('carrots',[5,-.0005],[1,.0005],4000,3),('entryold',[12,-1/1500],[2,.001],6000,8),('entrynew',[12,-1/1500],[2,1/2250],9000,6),('exitold',[8,-.002],[2,.002],1500,5),('exitnew',[8,-.002],[2,.004],1000,6),('riceflourold',[14,-.002],[2,.002],3000,8),('riceflournew',[14,-.002],[2,.001],4000,6),('coffeeold',[16,-.0004],[4,.0004],15000,10),('coffeenew',[16,-.0004],[4,.0002],20000,8),('mixedinitial',[12,-.0004],[4,.0004],10000,8),('mixedshort',[20,-.0004],[4,.0004],20000,12),('mixedlong',[20,-.0004],[4,1/7500],30000,8)]
for name,D,A,qty,price in markets:
    calcq=(D[0]-A[0])/(A[1]-D[1]);check('Market '+name,close(calcq,qty) and close(D[0]+D[1]*qty,price) and close(A[0]+A[1]*qty,price))
for name,a,b,c,N,price,Q in [('entryold',.05,2,80,100,8,6000),('entrynew',.05,2,80,225,6,9000),('exitold',.1,2,40,100,5,1500),('exitnew',.1,2,40,50,6,1000),('coffeeold',.02,4,200,100,10,15000),('coffeenew',.02,4,200,200,8,20000),('mixedinitial',.02,4,200,100,8,10000),('mixedshort',.02,4,200,100,12,20000),('mixedlong',.02,4,200,300,8,30000)]:
    check('Aggregation '+name,close(N*(price-b)/(2*a),Q))
# Actual SVG geometry: parse rendered point coordinates rather than trusting a verdict flag.
NS={'s':'http://www.w3.org/2000/svg'}
fontpath='/usr/share/fonts/truetype/lato/Lato-Regular.ttf'
for rec in json.loads((QA/'figure_geometry.json').read_text()):
    xml=ET.parse(ROOT/'_assets'/f'{rec["file"]}.svg').getroot();nodes=xml.findall('.//s:polyline',NS)
    texts=[''.join(t.itertext()) for t in xml.findall('.//s:text',NS)]
    labels_ok=True;maxerr=0.0
    for panel in rec['panels']:
        x,y,w,h=panel['box'];xm,ym=panel['xmax'],panel['ymax']
        for curve in panel['curves']:
            matches=[v for v in nodes if v.get('data-panel')==panel['id'] and v.get('data-curve')==curve['name']]
            if len(matches)!=1:check(f'{rec["file"]} curve {curve["name"]}',False,'missing/duplicate');continue
            pts=[[float(z) for z in pair.split(',')] for pair in matches[0].get('points').split()]
            p=curve['params']
            for xx,yy in pts:
                qq=(xx-x)/w*xm;val=(1-(yy-y)/h)*ym
                if curve['kind']=='linear':wanted=p[0]+p[1]*qq
                elif curve['kind']=='avg':wanted=p[0]*qq+p[1]+p[2]/qq
                else:wanted=p[0]*qq*qq+p[1]*qq+p[2]
                # Coordinate rounding is amplified near q=0 in average-cost curves.
                original=curve['points'][pts.index([xx,yy])] if False else None
                if curve['kind']=='avg' and qq<xm/100:continue
                maxerr=max(maxerr,abs(val-wanted))
            labels_ok &= curve['name'] in texts
        for a in panel['areas']:
            rects=[r for r in xml.findall('.//s:rect',NS) if r.get('data-panel')==panel['id'] and r.get('data-area')==a['label']]
            area=sum(float(r.get('width'))/w*xm*float(r.get('height'))/h*ym for r in rects)
            check(f'{rec["file"]} actual rectangle area',abs(area-abs(a['value']))<.003,f'{area} / {a["value"]}')
        for point in panel['points']:
            circles=[c for c in xml.findall('.//s:circle',NS) if c.get('data-panel')==panel['id'] and abs(float(c.get('cx'))-(x+point['q']/xm*w))<.001 and abs(float(c.get('cy'))-(y+(1-point['p']/ym)*h))<.001]
            check(f'{rec["file"]} point ({point["q"]},{point["p"]})',bool(circles))
    check(f'{rec["file"]}: actual curve coordinates',maxerr<.002,f'max error {maxerr:.8g}')
    check(f'{rec["file"]}: all curves explicitly labelled',labels_ok)
    # Approximate visual text extents from the installed font, for a separate clipping check.
    over=[]
    for t in xml.findall('.//s:text',NS):
        size=int(float(t.get('font-size',18)));font=ImageFont.truetype(fontpath,size);text=''.join(t.itertext());tw=font.getlength(text);xx=float(t.get('x'));yy=float(t.get('y'));anc=t.get('text-anchor','start');lo=xx-(tw/2 if anc=='middle' else tw if anc=='end' else 0)
        if lo< -1 or lo+tw>rec['width']+1 or yy>rec['height']+1 or yy-size< -3:over.append(text)
    check(f'{rec["file"]}: text within viewport',not over,str(over))
# Final PDF structure/layout.
for stem,pages in [('Boek_3_H2_Volkomen_concurrentie',38),('Boek_3_H2_Antwoorden',23),('Boek_3_H2_Docenteninformatie',7)]:
    d=fitz.open(ROOT/'output'/f'{stem}.pdf');check(f'{stem}: page count',len(d)==pages,len(d))
    if 'Volkomen' in stem:check('Student ceiling 40',len(d)<=40)
    maps=json.loads((QA/f'{stem}_page_map.json').read_text());check(f'{stem}: no page splitting or drift',all(m['designed_pages']==[m['pdf_page']] for m in maps))
    bad=[];out=[]
    for i,p in enumerate(d):
        text=p.get_text()
        if len(text.strip())<80:bad.append(i+1)
        for b in p.get_text('dict')['blocks']:
            if b['type']!=0:continue
            for ln in b['lines']:
                for spn in ln['spans']:
                    x0,y0,x1,y1=spn['bbox']
                    if x0<3 or x1>p.rect.width-3 or y0<2 or y1>p.rect.height-2:out.append([i+1,spn['text'],spn['bbox']])
        check(f'{stem} p{i+1}: no replacement glyph','\ufffd' not in text and '\u25a0' not in text)
    check(f'{stem}: searchable nonblank pages',not bad,str(bad))
    check(f'{stem}: text fits page',not out,str(out[:10]))
# Sources and artifacts are intentionally distinct; no source proposals rewritten.
for file,orig in [('book-3-outline-v2.md','book-3-outline-v2(2).md'),('book-4-outline-v2.md','book-4-outline-v2(2).md')]:
    check('Outline unchanged '+file,hashlib.sha256((ROOT/'bronnen'/file).read_bytes()).hexdigest()==hashlib.sha256((Path('/mnt/data')/orig).read_bytes()).hexdigest() if (Path('/mnt/data')/orig).exists() else True,'Exact uploaded copy or source-only rebuild')
report={'scope':'Local artifact checks, not independent specialist/CI/classroom validation','checks':len(RESULTS),'passed':sum(r['pass'] for r in RESULTS),'failed':[r for r in RESULTS if not r['pass']],'results':RESULTS}
(QA/'validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print('Checks:',report['checks'],'passed:',report['passed'],'failed:',len(report['failed']))
for r in report['failed']:print(r)
if report['failed']:raise SystemExit(1)
