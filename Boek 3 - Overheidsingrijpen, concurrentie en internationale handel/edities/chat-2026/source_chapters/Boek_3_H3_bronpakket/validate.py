"""Local reproducible checks for text coverage, arithmetic, SVG geometry and PDFs.
This is a self-check of this print edition, not independent pedagogical review
or an official examination/repository approval. All cases use fictitious data.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import re, json, math, hashlib, sys
import xml.etree.ElementTree as ET
import fitz
from PIL import Image
from bs4 import BeautifulSoup
from build import page_chunks, render_md
ROOT=Path(__file__).resolve().parent
CHECKS=[]
def ck(label, condition, detail='', category='structure'):
    CHECKS.append({'check':label,'passed':bool(condition),'category':category,'detail':str(detail)})
def near(a,b,tol=1e-4):return abs(float(a)-float(b))<=tol

def area(points):
    return abs(sum(points[i][0]*points[(i+1)%len(points)][1]-points[(i+1)%len(points)][0]*points[i][1] for i in range(len(points)))/2)
def nums(points):return [[float(v) for v in pair.split(',')] for pair in points.split()]
def plain(s):return BeautifulSoup(s,'html.parser').get_text(' ',strip=True)
def normalize(s):return re.sub(r'\s+','',plain(s)).replace('−','-').replace('.', '').replace(',','.')

def run():
    ex=json.loads((ROOT/'QA/exercises.json').read_text())
    an=json.loads((ROOT/'QA/answers.json').read_text())
    ck('Exercises numbered 1–38',[e['number'] for e in ex]==list(range(1,39)))
    ck('Answer records cover all 38 exercises',sorted(e['number'] for e in an)==list(range(1,39)))
    qids=[q['id'] for e in ex for q in e['subquestions']]
    aids=[q['id'] for e in an for q in e['subquestions']]
    ck('108 unique subquestions',len(qids)==108 and len(set(qids))==108)
    ck('Every subquestion has exactly one answer',Counter(qids)==Counter(aids))
    targets=[e for e in ex if e['target']]
    ck('Four newly authored target exercises',[e['number'] for e in targets]==[7,17,27,35])
    ck('Targets have 21 subquestions',sum(len(t['subquestions']) for t in targets)==21)
    ck('Target points are 11 / 10 / 11 / 16',[sum(q['points'] for q in t['subquestions']) for t in targets]==[11,10,11,16])
    for e in an:
        for q in e['subquestions']:
            ck('Substantive answer '+q['id'],len(plain(q['answer']))>=15)
            ck('Meaning/why explanation '+q['id'],len(plain(q['why']))>=10)
    order=json.loads((ROOT/'chapter-order.json').read_text())
    pages=[p for f in order for p in page_chunks(ROOT/f)]
    student='\n\n'.join(p['body'] for p in pages)
    answer=(ROOT/'Antwoorden.md').read_text()
    ss=BeautifulSoup(render_md(student),'html.parser'); aa=BeautifulSoup(render_md(answer),'html.parser')
    actualq=[el['data-question'] for el in ss.select('[data-question]')]
    actuala=[el['data-answer-question'] for el in aa.select('[data-answer-question]')]
    ck('Actual student manuscript contains all question IDs',actualq==qids)
    ck('Actual answers are in exercise order',[int(el['data-answer']) for el in aa.select('[data-answer]')]==list(range(1,39)))
    ck('Actual answers cover all manuscript questions',Counter(actualq)==Counter(actuala))
    answer_by_id={q['id']:q for e in an for q in e['subquestions']}
    for e in ex:
        for q in e['subquestions']:
            el=ss.select_one(f'[data-question="{q["id"]}"]')
            ck('Source question '+q['id']+' matches QA',q['prompt'] in str(el))
            el=aa.select_one(f'[data-answer-question="{q["id"]}"]')
            ck('Source answer '+q['id']+' matches QA',plain(answer_by_id[q['id']]['answer']) in plain(str(el)))
    heads=['Uitgewerkt voorbeeld','Startopgaven','Begeleide inoefening','Zelfstandige oefening','Doeloefening','Denkertje / Bonusopgave','Herhaling / Herhaling en interleaving']
    for code in ['3.3.1','3.3.2','3.3.3']:
        t=(ROOT/f'{code} manuscript.md').read_text()
        ck(code+' seven exact exercise headings',re.findall(r'^## (.+)$',t,re.M)==heads)
        ck(code+' compact summary between example and start',t.index('## Uitgewerkt voorbeeld')<t.index('box summary')<t.index('## Startopgaven'))
        ck(code+' short paper route', 'Startopgaven → Zelfstandige oefening → Doeloefening' in t)
        ck(code+' neutral guided opt-out','Heb je deze hulp niet nodig? Ga dan verder met Zelfstandige oefening.' in t)
    ck('Mixed section is consolidation, not a new theory template','## Uitgewerkt voorbeeld' not in (ROOT/'3.3.4 manuscript.md').read_text())
    for token in ['companion','Part A','Part B','lane','QR-code','scan de','online uitleg','Fading','productiegebied']:
        ck('Student copy excludes '+token,token.lower() not in plain(student).lower())
    t331=(ROOT/'3.3.1 manuscript.md').read_text()
    ck('Verbal comparative advantage: no numerical production table',not re.search(r'\|.*\d.*\|',t331))
    ck('Comparative advantage and alternative cost explicitly taught','Comparatief voordeel' in t331 and 'lagere alternatieve kosten' in t331)
    ck('No mandatory full graph construction',not re.search(r'teken (?:zelf |een |de )(?:volledig|vraag- en aanbod|assenstelsel)',student,re.I))
    ck('Explicit fill-table instruction before blank table',student.index('Vul alle lege cellen in de tabel')<student.index('| Begin | € 10 | € 2 | … |'))
    ck('Four prerequisite retrieval starts are supplied',all(n in qids for n in ['1a','11a','21a','31a']))
    ck('No-import case in both teaching and practice','Geen invoer meer' in student and '3.3.3_fig_4' in student)
    ck('Fictitious-source boundary is stated','fictie' in (ROOT/'00 Inleiding.md').read_text().lower())

    # Compute independently from the stated case values, rather than trust graph log totals.
    def calc(label,result,expected,answer_id=None,shown=None):
        ck(label,near(result,expected),f'{result} vs {expected}','arithmetic')
        if answer_id and shown:
            ck(label+' is reported in answer '+answer_id,normalize(shown) in normalize(answer_by_id[answer_id]['answer']),shown,'arithmetic')
    calc('9a original-base percentage',(F(25)-20)/20*100,25,'9a','25%')
    calc('9b reverse percentage',(F(20)-25)/25*100,-20,'9b','-20%')
    calc('10a individual CS',35-25,10,'10a','10')
    calc('10b retailer revenue',25*40,1000,'10b','1.000')
    calc('11a domestic demand',100-2*20,60,'11a','60')
    calc('11a domestic supply',2*20-20,20,'11a','20')
    calc('12a imports',70-30,40,'12a','40')
    calc('15a import gap',90-30,60,'15a','60')
    calc('16a export gap',90-50,40,'16a','40')
    calc('17a import gap',100-60,40,'17a','40')
    calc('20a total revenue',5*80,400,'20a','400')
    calc('20a average revenue',F(400,80),5,'20a','5')
    calc('20b added revenue',5*10,50,'20b','50')
    calc('20b marginal revenue',F(50,10),5,'20b','5')
    calc('21a tax receipts',3*40,120,'21a','120')
    calc('22a taxable imports',90-60,30,'22a','30')
    calc('23c tariff rectangle',(70-50)*(25-20),100,'23c','100')
    for label,wp,t,expected in [('initial',10,2,12),('world price only',8,2,10),('tariff only',10,4,14),('combined',8,4,12)]:
        calc('24a '+label,wp+t,expected,'24a',str(expected))
    calc('25a remaining imports',70-30,40,'25a','40')
    calc('25a tariff receipts',(70-30)*2,80,'25a','80')
    calc('26a no-import domestic price',min(12+9,18),18,'26a','18')
    calc('26b zero receipts',0*9,0,'26b','0')
    calc('27a imports',100-60,40,'27a','40')
    calc('27a revenue',10*(100-60),400,'27a','400')
    calc('29a general-tax revenue',2*100,200,'29a','200')
    calc('29a tariff revenue',2*30,60,'29a','60')
    calc('30a price change',F(12-10,10)*100,20,'30a','20%')
    calc('30a demand change',F(90-100,100)*100,-10,'30a','-10%')
    calc('30a elasticity',F(-10,20),-.5,'30a','-0,5')
    calc('32a export gap',100-60,40,'32a','40')
    calc('34a imports',90-70,20,'34a','20')
    calc('34a tariff revenue',3*(90-70),60,'34a','60')
    calc('35b imports',100-60,40,'35b','40')
    calc('35b receipts',(100-60)*5,200,'35b','200')
    calc('37a tax wedge',12-9,3,'37a','3')
    calc('37a tax revenue',(12-9)*40,120,'37a','120')
    calc('38a revenue',8*100,800,'38a','800')
    calc('38a profit',8*100-650,150,'38a','150')

    # PNG/SVG pairs, actual vector geometry, clipping, labels and area accounting.
    refs=set(re.findall(r'_assets/([^"\s)]+)',student+answer))
    assets=list((ROOT/'_assets').glob('*.svg'))
    ck('27 SVG originals',len(assets)==27)
    ck('22 student figure originals',len(set(re.findall(r'_assets/([^"\s)]+)',student)))==22)
    ck('Five distinct answer figures',len([p for p in assets if '_ans_' in p.name])==5)
    ck('No unreferenced vector assets',{p.name for p in assets}==refs)
    log=json.loads((ROOT/'QA/figure_geometry.json').read_text())
    ck('Geometry record covers every vector',{e['file']+'.svg' for e in log}=={p.name for p in assets})
    ns={'s':'http://www.w3.org/2000/svg'}
    for figure in log:
        name=figure['file'];svg=ROOT/'_assets'/f'{name}.svg';png=svg.with_suffix('.png')
        tree=ET.fromstring(svg.read_text())
        ck(name+' valid accessible SVG',tree.find('s:title',ns) is not None,'','geometry')
        ck(name+' PNG pair exists',png.exists(),'','assets')
        with Image.open(png) as im:ck(name+' raster dimensions',im.width==1800 and abs(im.height-1800*figure['height']/figure['width'])<2,'','assets')
        for panel in figure['panels']:
            x,y,w,h=panel['box'];xm,ym=panel['xmax'],panel['ymax'];pid=panel['id']
            def project(points):return [[x+w*q/xm,y+h*(1-p/ym)] for q,p in points]
            for curve in panel['curves']:
                elems=[e for e in tree.findall('s:polyline',ns) if e.get('data-curve')==curve['name'] and e.get('data-panel')==pid]
                ck(name+' '+pid+curve['name']+' SVG curve present',len(elems)==1,'','geometry')
                if not elems:continue
                drawn=nums(elems[0].get('points'));expect=project(curve['points'])
                ck(name+' '+pid+curve['name']+' exact projected endpoints',all(near(a,b) for p1,p2 in zip(drawn,expect) for a,b in zip(p1,p2)),'','geometry')
                ck(name+' '+pid+curve['name']+' endpoints on economic equation',all(near(p,curve['a']+curve['b']*q) for q,p in curve['points']),'','geometry')
                ck(name+' '+pid+curve['name']+' algebraically clipped',all(-1e-6<=q<=xm+1e-6 and -1e-6<=p<=ym+1e-6 for q,p in curve['points']),'','geometry')
            circles=[e for e in tree.findall('s:circle',ns) if e.get('data-panel')==pid]
            ck(name+' '+pid+' number of points',len(circles)==len(panel['points']),'','geometry')
            for j,(point,el) in enumerate(zip(panel['points'],circles)):
                X,Y=project([[point['q'],point['p']]])[0]
                ck(name+' '+pid+f' point {j} exact',near(el.get('cx'),X) and near(el.get('cy'),Y),'','geometry')
                ck(name+' '+pid+f' point {j} on a represented line',any(near(point['p'],c['a']+c['b']*point['q']) for c in panel['curves']),'','geometry')
            for a in panel['areas']:
                elem=next(e for e in tree.findall('s:polygon',ns) if e.get('data-area')==a['label'] and e.get('data-panel')==pid)
                drawn=nums(elem.get('points'));expected=project(a['points'])
                ck(name+' '+pid+' '+a['label']+' polygon coordinates',len(drawn)==len(expected) and all(near(v,z) for u,t in zip(drawn,expected) for v,z in zip(u,t)),'','geometry')
                ck(name+' '+pid+' '+a['label']+' polygon area',near(area(drawn)/(w/xm*h/ym),a['value']),'','geometry')
            for gap in panel['gaps']:
                ck(name+' gap magnitude',near(gap['to']-gap['from'],gap['value']),'','geometry')
            if 'model' in panel:
                m=panel['model'];a,b=m['D'];c,d=m['S'];qe=(c-a)/(b-d);pe=a+b*qe
                tariff=m['tariff'] or 0
                p=(min(m['pw']+tariff,pe) if m['tariff'] is not None else m['pw'])
                qv=(p-a)/b;qa=(p-c)/d;trade=abs(qv-qa)
                for field,expected in [('qe',qe),('pe',pe),('actual_price',p),('qa',qa),('qv',qv),('trade',trade)]:
                    ck(name+' model '+field,near(m[field],expected),f'{m[field]} vs {expected}','arithmetic')
                for ar in panel['areas']:
                    if ar['label']=='overheidsopbrengst':ck(name+' rectangle equals tariff times remaining imports',near(ar['value'],tariff*max(qv-qa,0)),'','arithmetic')
        for t in figure['texts']:
            ck(name+' label anchor inside canvas: '+t['text'],0<=t['x']<=figure['width'] and 0<t['y']<=figure['height'],'','geometry')
    surplus=next(e for e in log if e['file']=='3.3.2_fig_4')
    ck('Surplus panels use identical axis units and limits',surplus['panels'][0]['xmax']==surplus['panels'][1]['xmax'] and surplus['panels'][0]['ymax']==surplus['panels'][1]['ymax'],'','geometry')
    for j,expect in [(0,[900,900]),(1,[1600,400])]:
        ck('Surplus visual '+str(j)+' matches independent triangle areas',[a['value'] for a in surplus['panels'][j]['areas']]==expect,'','arithmetic')

    # Rendered PDF structure: tests deliberately do not call page boxes 'visual QA'.
    for stem,count in [('Boek_3_H3_Internationale_handel',38),('Boek_3_H3_Antwoorden',17),('Boek_3_H3_Docenteninformatie',7)]:
        pdf=ROOT/'output'/f'{stem}.pdf';doc=fitz.open(pdf)
        ck(stem+' exact page count',len(doc)==count,'','pdf')
        ck(stem+' selectable text',all(len(p.get_text().strip())>50 for p in doc),'','pdf')
        maps=json.loads((ROOT/'QA'/f'{stem}_page_map.json').read_text())
        ck(stem+' no page overflow/drift',all(m['designed_pages']==[m['pdf_page']] for m in maps) and len(maps)==count,'','pdf')
        for n,p in enumerate(doc,1):
            ck(stem+f' p{n} A4',near(p.rect.width,595.276,.1) and near(p.rect.height,841.89,.1),'','pdf')
            text=p.get_text()
            ck(stem+f' p{n} no raw markup/missing-glyph marker',all(v not in text for v in ['###','**','�','□']),'','pdf')
            blocks=p.get_text('blocks')
            ck(stem+f' p{n} text boxes inside page',all(b[0]>=-1 and b[1]>=-1 and b[2]<=p.rect.width+1 and b[3]<=p.rect.height+1 for b in blocks),'','pdf')
            for link in p.get_links():
                if 'page' in link and link['page']>=0:ck(stem+f' p{n} internal destination',0<=link['page']<len(doc),'','pdf')
        if 'Internationale_handel' in stem:
            ck('Student chapter meets maximum 40 pages',len(doc)<=40,'','pdf')
            ck('Mixed target sources and questions form 34–35 spread','Bron A' in doc[33].get_text() and 'Opgave 35' in doc[34].get_text(),'','pdf')
            ck('Contents destinations start at 2/11/21/31/38',set(l['page']+1 for l in doc[0].get_links() if 'page' in l and l['page']>=0)=={2,11,21,31,38},'','pdf')
    # Source copies and paragraph files.
    register=json.loads((ROOT/'bronnen/source-register.json').read_text())
    for att in register['attachments']:
        ck(att['file']+' source hash unchanged',hashlib.sha256((ROOT/att['file']).read_bytes()).hexdigest()==att['sha256'],'','sources')
    exports=json.loads((ROOT/'QA/paragraph-exports.json').read_text())
    ck('Four paragraph export bundles',len(exports)==4,'','exports')
    for e in exports:
        folder=ROOT/e['folder']
        for p in folder.glob('*.md'):
            for path in set(re.findall(r'_assets/([^"\s)]+)',p.read_text())):
                ck(e['paragraph']+' resolves '+path,(folder/'_assets'/path).exists(),'','exports')
        pdfs=list(folder.glob('*.pdf'));ck(e['paragraph']+' PDF variants',len(pdfs)==(2 if e['paragraph']=='3.3.4' else 3),'','exports')
        for p in pdfs:
            with fitz.open(p) as d:ck(e['paragraph']+' readable '+p.stem,len(d)>0 and len(d[0].get_text())>40,'','exports')
    ck('No distributable font binaries',not any(p.suffix.lower() in ['.ttf','.otf','.woff','.woff2'] for p in ROOT.rglob('*')),'','package')
    report={'scope':'Local self-check: coverage, explicit model arithmetic, actual SVG geometry, PDF structure and reproducible exports.',
       'checks':CHECKS,'passed':sum(c['passed'] for c in CHECKS),'failed':sum(not c['passed'] for c in CHECKS),
       'limitations':['Automated tests do not prove classroom learning or 55-minute feasibility.','Rendered pages were also self-reviewed, not independently reviewed.','This edition does not update official targets, live repositories or exam requirements.'],
       'counts':{'student_pages':38,'answer_pages':17,'teacher_pages':7,'exercises':38,'subquestions':108,'target_exercises':4,'target_subquestions':21,'student_figures':22,'answer_specific_figures':5,'worked_examples':3}}
    (ROOT/'QA/validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    rows=Counter(c['category'] for c in CHECKS)
    summary='# Lokale controle — internationale handel\n\n'+f"{report['passed']} controles geslaagd; {report['failed']} niet geslaagd.\n\n"+'\n'.join(f'- {k}: {v} controles' for k,v in sorted(rows.items()))+'\n\n'+ '\n'.join('- '+l for l in report['limitations'])+'\n'
    (ROOT/'QA/validation-summary.md').write_text(summary,encoding='utf-8')
    print(f"Local validation: {report['passed']} passed, {report['failed']} failed")
    for c in CHECKS:
        if not c['passed']:print('FAIL:',c['check'],c['detail'])
    return report['failed']
if __name__=='__main__':sys.exit(1 if run() else 0)
