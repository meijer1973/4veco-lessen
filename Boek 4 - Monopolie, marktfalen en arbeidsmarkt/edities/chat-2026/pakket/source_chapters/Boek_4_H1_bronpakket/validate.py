"""Reproducible local release checks. No independent-review or classroom claim."""
from pathlib import Path
from fractions import Fraction as F
import json,math,re,hashlib,xml.etree.ElementTree as ET
import fitz
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parent;QA=ROOT/'QA';OUT=ROOT/'output'
checks=[]
def check(name,condition,detail=''):
    checks.append({'name':name,'pass':bool(condition),'detail':detail})
def close(a,b,eps=1e-7):return abs(float(a)-float(b))<=eps

def numerical():
    # Independent rational calculation of the student/answer model values.
    def revenue(a,b,q):a,b,q=map(lambda v:F(str(v)),[a,b,q]);return (a-b*q)*q
    intervals=[('theory412',20,.2,20,30,320,420,10,140,40),('Luma',12,.1,30,40,270,320,5,80,30),('ex13',16,.2,20,30,240,300,6,100,40),('ex14',18,.2,20,30,280,360,8,120,40),('ex15',23,.2,40,50,600,650,5,130,80),('ex16',25,.25,20,40,400,600,10,300,100),('target18',30,.5,20,30,400,450,5,150,100)]
    for name,a,b,q0,q1,t0,t1,avg,gain,loss in intervals:
        a,b,q0,q1=map(lambda v:F(str(v)),[a,b,q0,q1])
        actual0=revenue(a,b,q0);actual1=revenue(a,b,q1)
        check(name+' TO pair',actual0==t0 and actual1==t1)
        check(name+' interval',(actual1-actual0)/(q1-q0)==avg)
        check(name+' gain/loss',(q1-q0)*(a-b*q1)==gain and q0*b*(q1-q0)==loss)
        check(name+' identity',actual1-actual0==gain-loss)
        # Independent finite difference symmetry is only a test, not a student rule.
        eps=F(1,1000);m0=(revenue(a,b,q0+eps)-revenue(a,b,q0-eps))/(2*eps)
        check(name+' derivative',m0==a-2*b*q0)
    demandcases=[('Parkveer40',12,.1,40,8),('Parkveer80',12,.1,80,4),('ex4a',18,.1,40,14),('ex4b',18,.1,80,10),('ex6a',40,.5,20,30),('ex6b',40,.5,40,20),('target8a',24,.1,60,18),('target8b',24,.1,120,12)]
    for name,a,b,q,p in demandcases:check(name,close(a-b*q,p))
    # a,b define demand p=a-bq; alpha,c,f define total cost alpha q²+cq+f.
    models=[('start1',10,0,.1,2,40,60,40,10,120),('core413',30,.2,0,6,200,100,60,18,520),('capacity50',30,.2,0,6,200,50,50,20,500),('loss',30,.2,0,6,900,100,60,18,-180),('Mira',24,.2,.1,6,80,50,30,18,190),('review20',12,0,.1,4,100,60,40,12,60),('Wavo24',28,.2,0,8,100,100,50,18,400),('Wavo25both',32,.2,0,8,180,100,60,20,540),('Helder26',40,.2,.1,4,100,70,60,28,980),('capacity27',22,.2,0,2,50,40,40,14,430),('Nova28',40,.25,.125,10,200,80,40,30,400),('KleurFix35',32,.2,.1,8,120,60,40,24,360),('competitor35',18,0,.1,8,120,60,50,18,130),('capacity37old',20,.1,0,4,100,60,60,14,500),('capacity37new',20,.1,0,4,100,100,80,12,540)]
    out=[]
    for vals in models:
        name,*vv=vals;a,b,aa,c,f,cap,qexpect,pexpect,wexpect=map(lambda x:F(str(x)),vv)
        qtheory=(a-c)/(2*(b+aa));q=max(F(0),min(cap,qtheory));p=a-b*q
        tk=lambda x:aa*x*x+c*x+f
        win=lambda x:revenue(a,b,x)-tk(x)
        check(name+' q',q==qexpect)
        check(name+' P',p==pexpect)
        check(name+' profit',win(q)==wexpect)
        check(name+' feasible',0<=q<=cap and p>=0)
        check(name+' maximum on feasible interval',all(win(q)>=win(cap*i/500) for i in range(501)))
        check(name+' boundary zero',win(q)>=win(F(0)))
        check(name+' profit rectangle',q==0 or (p-tk(q)/q)*q==win(q))
        out.append({'name':name,'q_candidate':float(qtheory),'q_chosen':float(q),'price':float(p),'revenue':float(revenue(a,b,q)),'cost':float(tk(q)),'profit':float(win(q))})
    check('Revenue versus profit example',revenue(30,.2,75)==1125 and revenue(30,.2,75)-(6*75+200)==475)
    check('Wrong P=MK candidate',close(40-.25*60, .25*60+10) and close(40-.5*60,10) and 10<25)
    check('Exercise 33 table', [revenue(28,.2,q)-F('0.1')*q*q-4*q-100 for q in [20,40,60,80]]==[260,380,260,-100])
    check('Exercise 30 finite-percent effect',11*180==1980 and 10*200==2000 and F(1980-2000,2000)==F(-1,100))
    check('Exercise 34 elasticity', F(20,100)/F(-10,100)==-2 and 9*120-10*100==80)
    (QA/'numerical-checks.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))

def geometry():
    logs=json.loads((QA/'figure_geometry.json').read_text());ns={'s':'http://www.w3.org/2000/svg'}
    for f in logs:
        path=ROOT/'_assets'/(f['file']+'.svg');tree=ET.parse(path).getroot()
        check(f['file']+' viewBox',tree.get('viewBox')==f"0 0 {f['width']} {f['height']}")
        check(f['file']+' PNG mirror',(ROOT/'_assets'/(f['file']+'.png')).stat().st_size>1000)
        for pl in f['panels']:
            x,y,w,h=pl['box'];qm=pl['xmax'];lo=pl['ymin'];hi=pl['ymax']
            inv=lambda xx,yy:((xx-x)/w*qm,hi-(yy-y)/h*(hi-lo))
            functions={}
            for c in pl['curves']:
                ps=c['params'];kind=c['kind']
                if kind=='linear':fn=lambda q,ps=ps:ps[0]+ps[1]*q
                elif kind=='total':fn=lambda q,ps=ps:ps[0]*q*q+ps[1]*q+ps[2]
                else:fn=lambda q,ps=ps:ps[0]*q+ps[1]+ps[2]/q
                functions[c['name']]=fn
                nodes=[n for n in tree.findall('s:polyline',ns) if n.get('data-panel')==pl['id'] and n.get('data-curve')==c['name']]
                check(f['file']+' curve exists '+c['name'],len(nodes)==1)
                if nodes:
                    pts=[tuple(map(float,z.split(','))) for z in nodes[0].get('points').split()]
                    err=[]
                    for xx,yy in pts:
                        q,p=inv(xx,yy)
                        if kind=='avg' and q<qm*.002:continue # Coordinate rounding magnifies reciprocal errors near zero.
                        err.append(abs(fn(q)-p))
                    check(f['file']+' geometry '+c['name'],max(err,default=0)<.003,f'max error {max(err,default=0):.6g}')
                    check(f['file']+' curve clipping '+c['name'],nodes[0].get('clip-path')==f"url(#{pl['id']})")
            nodes=[n for n in tree.findall('s:circle',ns) if n.get('data-panel')==pl['id']]
            check(f['file']+' point count '+pl['id'],len(nodes)==len(pl['points']))
            for k,(pt,nd) in enumerate(zip(pl['points'],nodes)):
                q,p=inv(float(nd.get('cx')),float(nd.get('cy')))
                check(f['file']+f' point {k} coordinates',close(q,pt['q'],.0001) and close(p,pt['p'],.0001))
                if pt.get('curve'):check(f['file']+f' point {k} lies on curve',close(functions[pt['curve']](pt['q']),pt['p'],1e-7))
            nodes=[n for n in tree.findall('s:polygon',ns) if n.get('data-area') is not None and n.get('data-panel')==pl['id']]
            check(f['file']+' area count '+pl['id'],len(nodes)==len(pl['areas']))
            for ar,nd in zip(pl['areas'],nodes):
                coords=[inv(*map(float,z.split(','))) for z in nd.get('points').split()]
                check(f['file']+' polygon '+ar['label'],len(coords)==len(ar['vertices']) and all(close(q,xq,.0001) and close(p,xp,.0001) for (q,p),(xq,xp) in zip(coords,ar['vertices'])))

def structure():
    files=json.loads((ROOT/'chapter-order.json').read_text());body='\n'.join((ROOT/f).read_text() for f in files)
    ex=json.loads((QA/'exercises.json').read_text());ans=json.loads((QA/'answers.json').read_text())
    check('38 exercises contiguous',[e['number'] for e in ex]==list(range(1,39)))
    wanted={str(e['number'])+chr(97+i) for e in ex for i,_ in enumerate(e['questions'])}
    got=[str(a['exercise'])+a['label'] for a in ans]
    check('107 subquestions',len(wanted)==107)
    check('Every subquestion answered exactly once',set(got)==wanted and len(got)==len(set(got)))
    soup=BeautifulSoup((OUT/'Boek_4_H1_Monopolie.html').read_text(),'html.parser')
    asoup=BeautifulSoup((OUT/'Boek_4_H1_Antwoorden.html').read_text(),'html.parser')
    check('Final HTML questions match registry',{p.get('data-question') for p in soup.select('[data-question]')}==wanted)
    check('Final HTML answer labels match registry',{p.get('data-answer-question') for p in asoup.select('[data-answer-question]')}==wanted)
    for e in ex:
        el=soup.select_one(f'[data-exercise="{e["number"]}"]')
        check('Exercise '+str(e['number'])+' exists',el is not None)
        if el is not None:
            text=el.get_text(' ',strip=True)
            check('Exercise '+str(e['number'])+' title unchanged',e['title'] in text)
    sequence=['Uitgewerkt voorbeeld','Startopgaven','Begeleide inoefening','Zelfstandige oefening','Doeloefening','Denkertje / Bonusopgave','Herhaling / Herhaling en interleaving']
    for sid in ['4.1.1','4.1.2','4.1.3']:
        text=(ROOT/f'{sid} manuscript.md').read_text();heads=re.findall(r'^## (.+)$',text,re.M)
        check(sid+' canonical section order',heads==sequence,str(heads))
        check(sid+' route note','Korte route:' in text and 'Heb je deze hulp niet nodig?' in text)
        check(sid+' one target',sum(e['section']==sid and e['group']=='target' for e in ex)==1)
    targets=[e for e in ex if e['group']=='target']
    check('4 targets, 22 subquestions',len(targets)==4 and sum(len(e['questions']) for e in targets)==22)
    check('Consolidation has no new-theory template','## Uitgewerkt voorbeeld' not in (ROOT/'4.1.4 manuscript.md').read_text())
    check('No point elasticity formula', 'dQ/dP' not in body and 'P/Q' not in body)
    check('Paper-first',not any(s in body.lower() for s in ['qr-code','ga naar de website','open de app']) and not re.search(r'\bpart\s+[ab]\b', body.lower()))
    for s,prefix in [(soup,'Student'),(asoup,'Answers')]:
        anchors={n.get('id') for n in s.select('[id]')}
        check(prefix+' internal links resolve',all(a.get('href')[1:] in anchors for a in s.select('a[href^="#"]')))
    for fname,expected in [('Boek_4_H1_Monopolie',38),('Boek_4_H1_Antwoorden',20),('Boek_4_H1_Docenteninformatie',7)]:
        d=fitz.open(OUT/(fname+'.pdf'));mapping=json.loads((QA/(fname+'_page_map.json')).read_text())
        check(fname+' page count',len(d)==expected,str(len(d)))
        check(fname+' no page flow drift',all(m['designed_pages']==[m['pdf_page']] for m in mapping))
        check(fname+' searchable pages',all(len(p.get_text().strip())>150 for p in d))
        check(fname+' no replacement glyph',all('\ufffd' not in p.get_text() for p in d))
        check(fname+' A4',all(abs(p.rect.width-595.276)<1 and abs(p.rect.height-841.89)<1 for p in d))
        # All text runs within media bounds; rendering still required for visual fit.
        bad=[]
        for i,p in enumerate(d):
            for b in p.get_text('dict')['blocks']:
                for l in b.get('lines',[]):
                    for sp in l['spans']:
                        x0,y0,x1,y1=sp['bbox']
                        if x0<-.5 or y0<-.5 or x1>p.rect.width+.5 or y1>p.rect.height+.5:bad.append([i+1,sp['text']])
        check(fname+' text within page',not bad,str(bad[:5]))
    d=fitz.open(OUT/'Boek_4_H1_Monopolie.pdf')
    check('Student <=40 pages',len(d)<=40)
    for page,sid in [(2,'4.1.1'),(10,'4.1.2'),(21,'4.1.3'),(32,'4.1.4')]:check('TOC start '+sid,sid in d[page-1].get_text())
    check('Mixed source and questions face each other','Bron A' in d[33].get_text() and 'Opgave 35' in d[34].get_text())
    # The source-level list must match the actual referenced asset files.
    referenced=set(re.findall(r'_assets/([^"\s]+\.svg)',body+(ROOT/'Antwoorden.md').read_text()))
    check('All referenced figures exist',all((ROOT/'_assets'/f).exists() for f in referenced))
    check('31 unique used vector figures',len(referenced)==31,str(len(referenced)))
    for source in json.loads((QA/'source-register.json').read_text())['attached_outlines']:
        check(source['file']+' original hash',hashlib.sha256((ROOT/source['file']).read_bytes()).hexdigest()==source['sha256'])

if __name__=='__main__':
    numerical();geometry();structure()
    fail=[c for c in checks if not c['pass']]
    result={'scope':'Local arithmetic, SVG geometry, coverage, source, and PDF structure checks; not independent review or classroom timing verification','total':len(checks),'passed':len(checks)-len(fail),'failed':len(fail),'checks':checks}
    (QA/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
    print('Checks:',len(checks),'failures:',len(fail))
    for f in fail:print(f)
    if fail:raise SystemExit(1)
