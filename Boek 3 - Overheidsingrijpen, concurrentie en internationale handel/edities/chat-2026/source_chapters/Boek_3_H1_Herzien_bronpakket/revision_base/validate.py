"""Local, reproducible checks. Not repository CI or an independent subject review.
Run after python make_assets.py and python build.py. All records are written to
QA/validation.json, including failures; the process exits nonzero on failure.
"""
from pathlib import Path
from fractions import Fraction as F
import json, re, hashlib, math, sys, xml.etree.ElementTree as ET
import fitz
from PIL import Image
from make_assets import fmt

ROOT = Path(__file__).resolve().parent
checks = []
def check(name, ok, detail=None):
    row = {'check': name, 'pass': bool(ok)}
    if detail is not None: row['detail'] = detail
    checks.append(row)
def close(a,b,tol=1e-6): return abs(float(a)-float(b)) <= tol
def frac(v): return F(str(v))
def area(points):
    return abs(sum(x1*y2-x2*y1 for (x1,y1),(x2,y2) in zip(points,points[1:]+points[:1])))/2

def market(c,b,a,d,change=0):
    """Positive change = seller-remitted tax; negative = per-unit seller subsidy."""
    c,b,a,d,t=map(frac,(c,b,a,d,change))
    q0=(c-a)/(b+d);p0=c-b*q0;q=(c-a-t)/(b+d)
    pc=c-b*q;pp=a+d*q
    cs0=q0*(c-p0)/2;ps0=q0*(p0-a)/2
    cs=q*(c-pc)/2;ps=q*(pp-a)/2
    net=cs+ps+t*q;w=cs0+ps0-net
    return dict(q0=q0,p0=p0,q=q,pc=pc,pp=pp,cs0=cs0,ps0=ps0,cs=cs,ps=ps,
                budget=t*q,net=net,w=w,buyer=pc-p0,seller=p0-pp)

order=json.loads((ROOT/'chapter-order.json').read_text())
student='\n'.join((ROOT/f).read_text() for f in order)
answers_md=(ROOT/'Antwoorden.md').read_text(); teacher=(ROOT/'Docenteninformatie.md').read_text()
ex=json.loads((ROOT/'exercises.json').read_text());ans=json.loads((ROOT/'answers.json').read_text())
targets=json.loads((ROOT/'targets-authored.json').read_text())
check('48 unique sequential exercises',[e['number'] for e in ex]==list(range(1,49)))
check('131 subquestions',sum(len(e['questions']) for e in ex)==131)
check('answer keys match exercises',set(ans)=={str(e['number']) for e in ex})
for e in ex:
    n=e['number'];a=ans.get(str(n),[])
    check(f'exercise {n}: answer count',len(a)==len(e['questions']))
    for j,aa in enumerate(a):
        check(f'exercise {n}{chr(97+j)}: solution and reason',bool(aa.get('solution','').strip()) and bool(aa.get('why','').strip()))
    check(f'exercise {n}: printed in student',bool(re.search(r'Opgave\s+'+str(n)+r'\b',student)))
    check(f'exercise {n}: printed in answers',f'id="ans{n}"' in answers_md)
check('six authored targets',[e['number'] for e in targets['exercises']]==[7,16,25,34,43,48])
check('31 target subquestions',sum(len(e['questions']) for e in targets['exercises'])==31)
check('not falsely marked as integrated','not_integrated' in targets['status'])
for target in targets['exercises']:
    check(f'target {target["number"]}: exact exercise record',target==ex[target['number']-1])
headings=['Uitgewerkt voorbeeld','Startopgaven','Begeleide inoefening','Zelfstandige oefening',
          'Doeloefening','Denkertje / Bonusopgave','Herhaling / Herhaling en interleaving']
for i in range(1,6):
    s=(ROOT/f'3.1.{i} manuscript.md').read_text()
    found=re.findall(r'^## (.+)$',s,re.M)
    check(f'3.1.{i}: seven printed sections',found==headings,found)
    check(f'3.1.{i}: non-heading summary between worked example and start',
          'Onthouden' in s[s.index('## Uitgewerkt voorbeeld'):s.index('## Startopgaven')])
    check(f'3.1.{i}: optional guided route','Heb je deze hulp niet nodig?' in s)
    check(f'3.1.{i}: paper short route','Korte route:' in s)
check('consolidation adds no worked-example theory','## Uitgewerkt voorbeeld' not in (ROOT/'3.1.6 manuscript.md').read_text())
check('correct canonical capacity word','productiegebied' not in student.lower())
check('no compulsory digital support',not re.search(r'QR-code|scan de|ga naar de website|Part A|Part B|companion',student,re.I))

# Verify actual plotted objects, not only the generator's numerical metadata.
geom=json.loads((ROOT/'QA/figure_geometry.json').read_text())
svgs={p.stem for p in (ROOT/'_assets').glob('*.svg')}; pngs={p.stem for p in (ROOT/'_assets').glob('*.png')}
check('42 SVG/PNG pairs',len(svgs)==42 and svgs==pngs)
check('figure records cover SVG files',{g['file'] for g in geom}==svgs)
allrefs=re.findall(r'(?:src="|!\[[^\]]*\]\()(_assets/[^"\)]+)',student+answers_md+teacher)
for ref in sorted(set(allrefs)):check('asset exists: '+ref,(ROOT/ref).is_file())
ns={'s':'http://www.w3.org/2000/svg'}
for g in geom:
    name=g['file'];root=ET.parse(ROOT/'_assets'/f'{name}.svg').getroot()
    texts=[''.join(el.itertext()) for el in root.findall('.//s:text',ns)]
    with Image.open(ROOT/'_assets'/f'{name}.png') as im:
        check(f'{name}: nonempty raster',im.width==1600 and im.height>100)
    if 'c' not in g:
        if g.get('type')=='incidence':
            check(name+': buyer/seller sum equals tax',g['buyerA']+g['sellerA']==g['tax'] and g['buyerB']+g['sellerB']==g['tax'])
        continue
    c,b,a,d=map(frac,(g['c'],g['b'],g['a'],g['d']));mode=g['mode'];amount=frac(g['amount'])
    m=market(c,b,a,d,amount if mode.startswith('tax') else -amount if mode.startswith('subsidy') else 0)
    check(name+': original equilibrium',close(g['q0'],m['q0']) and close(g['p0'],m['p0']))
    if mode.startswith(('tax','subsidy')):
        check(name+': new equilibrium and prices',all(close(g[k],m[k]) for k in ('q','pc','pp')))
        check(name+': wedge identity',close(g['pc']-g['pp'],amount if mode.startswith('tax') else -amount))
        check(name+': welfare identity',m['w']==abs(amount*(m['q0']-m['q'])/2))
    if mode in ('ceiling','floor'):
        qv=(c-amount)/b;qa=(amount-a)/d
        check(name+': amount of private transactions',close(g['q'],min(qv,qa)))
        check(name+': binding status',amount<m['p0'] if mode=='ceiling' else amount>m['p0'])
    if mode=='quota':
        check(name+': bounded quota price',close(g['q'],min(amount,m['q0'])) and close(g['pc'],c-b*min(amount,m['q0'])))
    check(name+': labelled axes and original curves',any(t.startswith('P (€ per ') for t in texts) and any(t.startswith('Q (') for t in texts) and 'V' in texts and 'A' in texts)
    X=lambda q:92+614*float(q)/g['xmax'];Y=lambda p:316-272*float(p)/g['ymax']
    lines=root.findall('.//s:line',ns)
    for j,curve in enumerate(g['curves']):
        ends=curve['ends'];ii=curve['intercept'];slope=curve['slope']
        check(f'{name}: curve {j} endpoints obey function',all(close(p,ii+slope*q) for q,p in ends))
        check(f'{name}: curve {j} in viewport',all(-1e-6<=q<=g['xmax']+1e-6 and -1e-6<=p<=g['ymax']+1e-6 for q,p in ends))
        coords=[X(ends[0][0]),Y(ends[0][1]),X(ends[1][0]),Y(ends[1][1])]
        matching=any(all(close(float(el.get(k)),v,0.0002) for k,v in zip(('x1','y1','x2','y2'),coords)) and float(el.get('stroke-width','0'))>2 for el in lines)
        check(f'{name}: curve {j} actual SVG line matches',matching)
    dots=root.findall('.//s:circle',ns)
    check(name+': all recorded dots rendered',len(dots)==len(g['points']))
    for j,(point,dot) in enumerate(zip(g['points'],dots)):
        q,p=point['q'],point['p'];on=point['on'];expected=[]
        if on in ('demand','both'):expected.append(float(c-b*frac(q)))
        if on in ('supply','both'):expected.append(float(a+d*frac(q)))
        check(f'{name}: point {j} on designated curve',all(close(p,v) for v in expected))
        check(f'{name}: point {j} actual SVG position',close(float(dot.get('cx')),X(q),.0002) and close(float(dot.get('cy')),Y(p),.0002))
    polys=root.findall('.//s:polygon',ns)
    check(name+': shaded areas complete',len(polys)==len(g['areas']))
    for j,(poly,shape) in enumerate(zip(polys,g['areas'])):
        pix=[tuple(map(float,p.split(','))) for p in poly.get('points').split()]
        pts=shape['points'];label=shape['label']
        check(f'{name}: area {label} actual SVG vertices',len(pix)==len(pts) and all(close(px,X(q),.0002) and close(py,Y(p),.0002) for (px,py),(q,p) in zip(pix,pts)))
        expected=None
        if label in ('CS','PS'):expected=m[label.lower()]
        elif label in ('O','U'):
            expected=amount*((amount-a)/d-(c-amount)/b) if mode=='floor' else abs(m['budget'])
        elif label=='W':expected=m['w']
        if expected is not None:check(f'{name}: area {label} independently calculated',close(area(pts),expected))
    if mode=='base':check(name+': exercise retains no solution areas',len(g['areas'])==0 and len(g['points'])==0)

# Regression tests for labels at floating-point integer boundaries.
for v,wanted in [(49.99999999999999,'50'),(59.99999999999999,'60'),(69.99999999999999,'70'),(12.000000000000002,'12'),(1.5,'1,5')]:
    check(f'rounding regression {v}',fmt(v)==wanted)
check('target tax graph labels 50, not 49','>50</text>' in (ROOT/'_assets/3.1.2_ans_2.svg').read_text() and '>49</text>' not in (ROOT/'_assets/3.1.2_ans_2.svg').read_text())

# Independent rational-arithmetic oracles for worked examples, practice and targets.
cases=[
 ('tax fruit',(14,.1,2,.1,4),{'q0':60,'p0':8,'q':40,'pc':10,'pp':6,'cs0':180,'ps0':180,'cs':80,'ps':80,'budget':160,'net':320,'w':40}),
 ('posters/cards/stickers',(16,.1,4,.1,4),{'q0':60,'p0':10,'q':40,'pc':12,'pp':8,'cs':80,'ps':80,'budget':160,'w':40}),
 ('mugs',(18,.2,6,.1,3),{'q0':40,'p0':10,'q':30,'pc':12,'pp':9,'buyer':2,'seller':1}),
 ('target bags 7/16',(20,.2,2,.1,3),{'q0':60,'p0':8,'q':50,'pc':10,'pp':7,'cs0':360,'ps0':180,'cs':250,'ps':125,'budget':150,'net':525,'w':15,'buyer':2,'seller':1}),
 ('controlled market A',(14,.1,2,.1,3),{'q0':60,'p0':8,'q':45,'pc':9.5,'pp':6.5,'buyer':1.5,'seller':1.5}),
 ('workshop subsidy',(18,.1,6,.1,-4),{'q0':60,'p0':12,'q':80,'pc':10,'pp':14,'cs':320,'ps':320,'budget':-320,'net':320,'w':40}),
 ('music subsidy',(22,.1,10,.1,-4),{'q0':60,'p0':16,'q':80,'pc':14,'pp':18,'cs':320,'ps':320,'budget':-320,'net':320,'w':40}),
 ('sport subsidy',(24,.2,6,.1,-3),{'q0':60,'p0':12,'q':70,'pc':10,'pp':13,'cs':490,'ps':245,'budget':-210,'net':525,'w':15}),
 ('target courses 25',(26,.2,8,.1,-3),{'q0':60,'p0':14,'q':70,'pc':12,'pp':15,'cs':490,'ps':245,'budget':-210,'net':525,'w':15}),
 ('target mixed 48',(24,.2,6,.1,3),{'q0':60,'p0':12,'q':50,'pc':14,'pp':11,'cs':250,'ps':125,'budget':150,'net':525,'w':15}),
 ('retrieval surplus 36',(30,.5,6,.25,0),{'q0':32,'p0':14,'cs0':256,'ps0':128})]
for name,params,expect in cases:
    m=market(*params)
    for key,val in expect.items():check(name+': '+key,m[key]==frac(val),str(m[key]))
for name,c,b,a,d,p,expect in [
 ('puzzles',14,.1,2,.1,6,(80,40,40)),('painting',16,.1,4,.1,8,(80,40,40)),
 ('boardgames',20,.2,2,.1,6,(70,40,30)),('target tent 34',18,.1,6,.1,10,(80,40,40)),
 ('mixed ceiling 48',24,.2,6,.1,10,(70,40,30)),
 ('apples floor',14,.1,2,.1,10,(40,80,40)),('pears floor',18,.1,6,.1,14,(40,80,40)),
 ('plums floor',22,.1,10,.1,18,(40,80,40)),('target mushrooms 43',20,.1,8,.1,16,(40,80,40))]:
    c,b,a,d,p=map(frac,(c,b,a,d,p));qv=(c-p)/b;qa=(p-a)/d
    check(name+': quantities and gap',(qv,qa,abs(qv-qa))==tuple(map(frac,expect)))
    if 'floor' in name or 'mushroom' in name:
        check(name+': quota40 price matches stated floor',c-b*40==p)
        check(name+': public purchase costs',p*(qa-qv)==p*40)
for name,got,expected in [
 ('retrieval 1 quantity',(F(12)-4)/(F('0.1')+F('0.1')),40),
 ('retrieval 1 substitution',4+F('.1')*30,7),
 ('retrieval 10 CS',F(1,2)*40*(18-10),160),('retrieval 10 PS',F(1,2)*40*(10-6),80),
 ('retrieval 18 profit',9*100-(300+4*100),200),
 ('bonus 35 allocation A',(12-6)+(10-6),10),('bonus 35 allocation B',(8-6)+(7-6),3),
 ('review 9 Ev',(F(180-200,200))/(F(12-10,10)),F(-1,2)),
 ('review 45 Ev',(F(70-80,80))/(F(10-8,8)),F(-1,2)),
 ('review 45 revenue rise',10*70-8*80,60),('mixed 47 purchase',12*(70-30),480),
 ('subsidy start20 budget',2*60,120),('cost review27 old',F(600,100),6),('cost review27 new',F(600,150),4)]:check(name,got==expected,str(got))

# Confirm model outputs that carry the target answers actually appear in answer copy.
for n,terms in {7:['60 tassen','50 tassen','€ 10','€ 7'],16:['€ 250','€ 125','€ 150','€ 525','€ 15'],
 25:['70','€ 12','€ 15','€ 210','€ 490','€ 245','€ 525'],34:['60 tenten','80','40','€ 12'],
 43:['60 kratten','€ 14','80 kratten','€ 640','40 kratten','€ 16'],48:['60 bandjes','€ 12','50','€ 14','€ 11','€ 150','€ 15','70','40','30 bandjes']}.items():
    body=' '.join(a['solution'] for a in ans[str(n)])
    for t in terms:check(f'answer {n}: expected value {t}',t in body)

# Actual PDF preflight: pages, output bounds, text, TOC and navigation.
lengths={'Boek_3_H1_Overheidsingrijpen':40,'Boek_3_H1_Antwoorden':28,'Boek_3_H1_Docenteninformatie':7}
for name,n in lengths.items():
    doc=fitz.open(ROOT/'output'/f'{name}.pdf'); check(name+': page count',len(doc)==n)
    mapping=json.loads((ROOT/'QA'/f'{name}_page_map.json').read_text())
    check(name+': no overflow/reflow pages',all(p['designed_pages']==[p['pdf_page']] for p in mapping))
    for j,p in enumerate(doc,1):
        txt=p.get_text();check(f'{name} p{j}: searchable, nonblank',len(txt.strip())>100)
        check(f'{name} p{j}: no missing Unicode',not any(c in txt for c in ['\ufffd','\u25a0']))
        bad=[]
        for b in p.get_text('dict')['blocks']:
            if b['type']!=0:continue
            for ln in b['lines']:
                for span in ln['spans']:
                    x0,y0,x1,y1=span['bbox']
                    if min(x0,y0)<-0.1 or x1>p.rect.width+.1 or y1>p.rect.height+.1:bad.append(span['text'])
        check(f'{name} p{j}: text within page',not bad,bad)
    check(name+': PDF bookmarks',len(doc.get_toc())>=5)
    doc.close()
sdoc=fitz.open(ROOT/'output/Boek_3_H1_Overheidsingrijpen.pdf')
for page,token in [(2,'3.1.1'),(9,'3.1.2'),(16,'3.1.3'),(23,'3.1.4'),(30,'3.1.5'),(37,'3.1.6')]:
    check(f'TOC section starts p{page}',token in sdoc[page-1].get_text())
check('mixed target sources face questions', 'Bron 1' in sdoc[37].get_text() and 'Opgave 48' in sdoc[38].get_text())
check('chapter ceiling includes overview','Overzicht' in sdoc[39].get_text() and len(sdoc)==40)
sdoc.close()
manifest=json.loads((ROOT/'bronnen/source_manifest.json').read_text())
for name,sha in manifest['sha256'].items():
    check('uploaded outline preserved: '+name,hashlib.sha256((ROOT/'bronnen'/name).read_bytes()).hexdigest()==sha)
check('no font binaries shared',not any(p.suffix.lower() in {'.ttf','.otf','.woff','.woff2'} for p in ROOT.rglob('*')))
report={'scope':'local reproducible checks; not repository CI, classroom testing or independent specialist review',
        'student_pages':40,'answer_pages':28,'teacher_pages':7,'exercises':48,'subquestions':131,'targets':6,
        'figure_pairs':42,'checks':checks,'passed':sum(c['pass'] for c in checks),'failed':sum(not c['pass'] for c in checks)}
(ROOT/'QA/validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print('Local validation:',report['passed'],'passed;',report['failed'],'failed')
for c in checks:
    if not c['pass']:print('FAIL:',c)
sys.exit(1 if report['failed'] else 0)
