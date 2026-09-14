"""Independent arithmetic, SVG, coverage and PDF preflight checks.

The numeric specifications below are separate from the authoring helpers.
They verify calculations and key displayed answer values, not learning gains
or all possible nuances in prose. Exit nonzero on any failure.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from html import unescape
import json, re, hashlib, math, sys, xml.etree.ElementTree as ET
import fitz
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parent
QADIR=ROOT/'QA'; E=json.loads((QADIR/'exercises.json').read_text())
checks=[]
def check(category,name,ok,detail=''):
    checks.append(dict(category=category,name=name,passed=bool(ok),detail=str(detail)))
def eq(name,result,expected):
    check('numeric',name,abs(float(result)-float(expected))<1e-8,f'{result} ; expected {expected}')
def ratio(a,b):return F(str(a))/F(str(b))
def pct(a,b):return (ratio(b,a)-1)*100

def labor(label,a,b,c,d,w0,L0,ap=None,wnew=None,Lnew=None,floor=None,hours=None):
    w=ratio(c-a,b-d);L=F(a)+F(b)*w
    eq(label+' equilibrium wage',w,w0);eq(label+' equilibrium employment',L,L0)
    if ap is not None:
        w1=ratio(c-ap,b-d);L1=F(ap)+F(b)*w1
        eq(label+' new wage',w1,wnew);eq(label+' new employment',L1,Lnew)
        eq(label+' unchanged wage new demand',F(ap)+F(b)*w0,F(ap)+F(b)*w)
    if floor:
        wf,ld,ls=floor
        eq(label+' floor demand',F(a)+F(b)*wf,ld);eq(label+' floor supply',F(c)+F(d)*wf,ls)
        eq(label+' shortage decomposition',ls-ld,(L0-ld)+(ls-L0))
        if hours:
            h,oldbill,newbill=hours
            eq(label+' old wage bill',F(w0)*h*L0,oldbill);eq(label+' new wage bill',F(wf)*h*ld,newbill)

# Worked examples and numerical explanations.
for name,res,expected in [
('6 people hours',6*20,120),('hours to fte',ratio(120,40),3),
('theory AP',ratio(2400,600),4),('theory unit cost',ratio(24,4),6),
('fixed output new hours',ratio(2400,5),480),('growing output same hours',ratio(3000,5),600),('growing output more hours',ratio(3300,5),660),
('WE431 old AP',ratio(1200,300),4),('WE431 new hours',ratio(1800,5),360),('WE431 hours change',pct(300,360),20),('WE431 old unit cost',ratio(24,4),6),('WE431 new unit cost',ratio(25,5),5),
('theory gross participation',ratio(600+100,1000)*100,70),('theory net participation',ratio(600,1000)*100,60),
('WE432 gross',ratio(1260+140,2000)*100,70),('WE432 net',ratio(1260,2000)*100,63),
('vacancies figure unemployment',ratio(100,900+100)*100,10),('vacancies identity',1000-(900+60),100-60),
('WE433 unemployment',ratio(160,1840+160)*100,8),('WE433 labor demand',1840+90,1930),('WE433 erroneous gap',2000-1930,70),
('floor theory wagebill percentage',pct(19200,16800),F(-25,2)),('WE434 wagebill percentage',pct(32000,30800),F(-15,4)),
('WE435 old cost',ratio(24,4),6),('WE435 new cost',ratio('25.2','4.5'),F(28,5)),
('WE435 wage index',ratio('25.2',24)*100,105),('WE435 AP index',ratio('4.5',4)*100,F(225,2)),('WE435 cost index',ratio(105,'112.5')*100,F(280,3)),
('WE435 training included',ratio('25.2','4.5')+F(1,4),F(117,20))]:eq(name,res,expected)

labor('theory432',180,-10,-20,10,10,80)
labor('WE432',160,-5,-20,5,18,70)
labor('theory433',200,-10,-40,10,12,80,ap=160,wnew=10,Lnew=60)
labor('WE433',200,-8,-24,8,14,88,ap=168,wnew=12,Lnew=72)
labor('theory434',200,-10,-40,10,12,80,floor=(14,60,100),hours=(20,19200,16800))
labor('WE434',180,-5,-20,5,20,80,floor=(22,70,90),hours=(20,32000,30800))

# All exercise cases that involve numerical answers.
for name,res,expected in [
('1a',ratio(2700,900),3),('1b',pct(900,1080),20),('3a',100-80,20),
('4a AP',ratio(1600,400),4),('4a hours',ratio(2400,6),400),('4a cost',ratio(21,6),F(7,2)),
('5a',ratio(1200,200),6),('5b hours',ratio(1500,'7.5'),200),('5b old cost',ratio(30,6),5),('5b new cost',ratio(30,'7.5'),4),
('6a old',160-5*16,80),('6a new',160-5*20,60),
('7a AP',ratio(2400,600),4),('7a hours',ratio(3300,'5.5'),600),('7b old cost',ratio(24,4),6),('7b new cost',ratio('26.4','5.5'),F(24,5)),('7c output growth',pct(2400,3300),F(75,2)),('7c AP growth',pct(4,'5.5'),F(75,2)),
('8a AP person A',ratio(600,10),60),('8a AP person B',ratio(480,8),60),('8a AP hour A',ratio(600,10*30),2),('8a AP hour B',ratio(480,8*20),3),
('9a TK',600+12*100,1800),('9a GTK',ratio(1800,100),18),('10a equilibrium P',ratio(120-20,4+1),20),('10a equilibrium Q',120-4*20,40),('10b',ratio(72,120)*100,60),
('12a BB',480+80,560),('12b gross',ratio(560,800)*100,70),('12b net',ratio(480,800)*100,60),
('14a BB',720+120,840),('14a gross',ratio(840,1200)*100,70),('14a net',ratio(720,1200)*100,60),
('16a BB',3000+500,3500),('16a gross',ratio(3500,5000)*100,70),('16a net',ratio(3000,5000)*100,60),
('17a new gross',ratio(600+150,1000)*100,75),('17a unchanged net',ratio(600,1000)*100,60),('18a wedge',12-9,3),('18a revenue',3*200,600),
('19a BB',2400+400,2800),('19a gross',ratio(2800,4000)*100,70),('20a unemployment',ratio(6,60)*100,10),
('21a unemployment',ratio(50,450+50)*100,10),('21b incorrect percentage',ratio(500-(450+30),500)*100,4),('23a unemployment',ratio(500,4500+500)*100,10),
('25a BB',2700+300,3000),('25a unemployment',ratio(300,3000)*100,10),('25a demand',2700+120,2820),('25a erroneous gap',3000-2820,180),('25c fixedwage demand',144-6*16,48),('25c fixedwage supply',-12+6*16,84),('25c gap',84-48,36),
('26a old',ratio(100,1000)*100,10),('26a new',ratio(50,950)*100,F(100,19)),
('27a TO q10',30*10-F(1,2)*100,250),('27a derivative slope',2*F(-1,2),-1),
('28a trades',min(60,100),60),('28a excess',100-60,40),('29a payroll',50*20*15,15000),
('30a lost employment',80-70,10),('30a extra supply',90-80,10),('34c percentage',pct(30000,28000),F(-20,3)),
('35a old weekly pay',16*25,400),('35a new weekly pay',18*20,360),('36a AP',ratio(4800,800),6),('36a cost',ratio(27,6),F(9,2)),
('37a index',ratio(22,20)*100,110),('37b cost',ratio(22,5),F(22,5)),
('39a old',ratio(30,5),6),('39a new',ratio('31.5',6),F(21,4)),('39b change',pct(6,'5.25'),F(-25,2)),
('40a totalcost',F('11.4')+F('.8'),F('12.2')),('41a index',ratio(108,104)*100,F(1350,13)),('41a percent',ratio(108,104)*100-100,F(50,13)),
('43b old',ratio(30,5),6),('43b new',ratio('31.5','5.5'),F(63,11)),('43b change',pct(6,F(63,11)),F(-50,11)),('43c training included',F(63,11)+F('.2'),F(326,55)),
('45a subsidy',25*40,1000),('46a fte',ratio(160,40),4),('46b unemployment',ratio(40,960+40)*100,4),
('47a old AP',ratio(6000,1000),6),('47a new hours',ratio(7560,'7.2'),1050),('47a hours growth',pct(1000,1050),5),('47b old cost',ratio(24,6),4),('47b new cost',ratio('25.2','7.2'),F(7,2)),
('49a totalpop',12600+1400+6000,20000),('49a BB',12600+1400,14000),('49a gross',ratio(14000,20000)*100,70),('49a unemployment',ratio(1400,14000)*100,10),('49e old cost',ratio(24,8),3),('49e new cost',ratio('25.2','8.8'),F(63,22)),('49e cost change',pct(3,F(63,22)),F(-50,11))]:eq(name,res,expected)
labor('13',140,-5,-20,5,16,60)
labor('15',200,-8,-24,8,14,88)
labor('16',240,-10,-40,10,14,100)
labor('24',180,-5,-20,5,20,80,ap=160,wnew=18,Lnew=70)
labor('25',180,-6,-12,6,16,84,ap=144,wnew=13,Lnew=66)
labor('31 and48',180,-6,-12,6,16,84,floor=(18,72,96),hours=(20,26880,25920))
labor('32',140,-2,0,5,20,100,floor=(22,96,110),hours=(20,40000,42240))
labor('34',220,-10,-20,10,12,100,floor=(14,80,120),hours=(25,30000,28000))
labor('49',240,-10,-40,10,14,100,ap=280,wnew=16,Lnew=120)

# Check key numerical values actually appear in the rendered answer content.
qa={q['id']:q for e in E for q in e['questions']}
expected_tokens={
'1a':['3'], '1b':['20'], '4a':['4','400','3,50'], '5b':['200','5','4'],
'7a':['4','600'],'7b':['6','4,80'],'8a':['60','2','3'],'9a':['1.800','18'],
'10a':['20','40'],'10b':['60'],'12a':['560'],'12b':['70','60'],'13a':['16','60'],
'14a':['840','70','60'],'15a':['14','88'],'16a':['3.500','70','60'],'16b':['14','100'],
'17a':['70','75','60'],'18a':['3','600'],'19a':['2.800','70'],'21a':['500','10'],'21b':['480','30'],
'23a':['5.000','10'],'24a':['18','70'],'24b':['60','80','20'],'25a':['3.000','10','2.820','180'],'25b':['13','66'],'25c':['48','84','36'],
'26a':['10','950','5,26'],'27a':['30','0,5'],'28a':['60','40'],'29a':['15.000'],
'30a':['10'],'31a':['72','96'],'31b':['24','25.920'],'32a':['96','110','14','42.240','40.000','2.240'],
'33a':['24','60'],'34a':['12','100'],'34b':['80','120','40'],'34c':['30.000','28.000','6,67'],
'35a':['400','360'],'36a':['6','4,50'],'37a':['110'],'37b':['4,40'],'39a':['6','5,25'],'39b':['12,5'],
'40a':['12,20','12'],'41a':['103,85','3,85'],'43b':['6','5,73','4,55'],'43c':['5,93'],
'45a':['1.000'],'46a':['4','8'],'46b':['1.000','4'],'47a':['6','1.050','5'],'47b':['4','3,50'],
'48a':['16','84','72','25.920'],'48b':['96','24'],'49a':['20.000','14.000','70','10'],
'49b':['14','100'],'49c':['16','120'],'49e':['3','2,86','4,55']}
for qid,vals in expected_tokens.items():
    text=BeautifulSoup(qa[qid]['answer'],'html.parser').get_text(' ')
    tokens=set(re.findall(r'(?<!\w)\d+(?:\.\d{3})*(?:,\d+)?',text))
    check('displayed-answer',qid,set(vals).issubset(tokens),{'expected':vals,'actual_tokens':sorted(tokens)})

# Actual SVG endpoints (not just generator metadata), sample points and rectangle.
geom=json.loads((QADIR/'figure_geometry.json').read_text()); ns={'s':'http://www.w3.org/2000/svg'}
byfile={}
for g in geom:byfile.setdefault(g['file'],[]).append(g)
for fn,rows in byfile.items():
    svg=ET.parse(ROOT/'_assets'/f'{fn}.svg').getroot();x0,y0,pw,ph=rows[0]['plot'];xm,ym=rows[0]['xmax'],rows[0]['ymax']
    for row in rows:
        el=next(x for x in svg.findall('s:line',ns) if x.get('data-curve')==row['curve'])
        xys=[[float(el.get(k)) for k in ('x1','y1')],[float(el.get(k)) for k in ('x2','y2')]]
        error=0;inbox=True
        for x,y in xys:
            L=(x-x0)/pw*xm;w=(y0-y)/ph*ym
            error=max(error,abs(L-(row['L_intercept']+row['L_slope']*w)))
            inbox=inbox and -0.001<=L<=xm+.001 and -.001<=w<=ym+.001
        check('svg-curve',fn+' / '+row['curve'],error<.005 and inbox,{'equation_error':error,'in_plot':inbox})
    for pt in svg.findall('s:circle',ns):
        L=(float(pt.get('cx'))-x0)/pw*xm;w=(y0-float(pt.get('cy')))/ph*ym
        err=min(abs(L-r['L_intercept']-r['L_slope']*w) for r in rows)
        check('svg-point',fn+' / '+str(pt.get('data-point')),err<.005,err)
    for tx in svg.findall('s:text',ns):
        x,y=float(tx.get('x')),float(tx.get('y'));check('svg-text-anchor',fn+' / '+str(tx.text),0<=x<=720 and 0<=y<=350)
# Geometrically displayed payroll rectangle: actual SVG dimensions convert to 14*60=840.
root=ET.parse(ROOT/'_assets'/'floor_bill.svg').getroot()
r=next((e for e in root.findall('s:rect',ns) if e.get('fill')=='#d7e8e2'),None)
if r is None:check('svg-area','payroll rectangle',False)
else:eq('SVG payroll width times height',float(r.get('width'))/(495/200)*float(r.get('height'))/(218/24),840)

# Coverage, structure, assets, bounds and navigation.
student=BeautifulSoup((ROOT/'output/Boek_4_H3_Arbeidsmarkt.html').read_text(),'html.parser')
answers=BeautifulSoup((ROOT/'output/Boek_4_H3_Antwoorden.html').read_text(),'html.parser')
qids=[p.get('data-question') for p in student.select('[data-question]')]
aids=[p.get('data-answer') for p in answers.select('[data-answer]')]
check('coverage','50 consecutive exercises',[e['number'] for e in E]==list(range(1,51)))
check('coverage','92 unique questions',len(qids)==len(set(qids))==92)
check('coverage','every question has exactly one answer',Counter(qids)==Counter(aids))
check('coverage','six authored targets',len([e for e in E if e['stage']=='Doeloefening'])==6)
check('coverage','24 target subquestions',sum(len(e['questions']) for e in E if e['stage']=='Doeloefening')==24)
for e in E:
    for q in e['questions']:
        check('answer-meaning',q['id'],('Waarom:' in q['answer']) if 'Bonus' not in e['stage'] else ('Beoordelingscriteria:' in q['answer']))
for sec in ['4.3.1','4.3.2','4.3.3','4.3.4','4.3.5']:
    text=(ROOT/f'{sec} manuscript.md').read_text()
    hs=re.findall(r'^## (.+)$',text,re.M)
    expected=['Uitgewerkt voorbeeld','Startopgaven','Begeleide inoefening','Zelfstandige oefening','Doeloefening','Denkertje / Bonusopgave','Herhaling / Herhaling en interleaving']
    check('structure',sec+' headings',hs==expected,hs)
    check('structure',sec+' summary placement',text.find('## Uitgewerkt voorbeeld')<text.find('Samenvatting §')<text.find('## Startopgaven'))
figs=json.loads((QADIR/'instructional-figures.json').read_text())
check('figures','24 student placements',len(figs)==24)
sol=[e['answer_fig'] for e in E if e['answer_fig']]
check('figures','8 solution figure placements',len(sol)==8)
for name in {f['file'] for f in figs}|set(sol):
    check('assets',name,all((ROOT/'_assets'/f'{name}.{ext}').is_file() for ext in ['svg','png']))
counts={}
for stem,expected in [('Boek_4_H3_Arbeidsmarkt',50),('Boek_4_H3_Antwoorden',18),('Boek_4_H3_Docenteninformatie',8)]:
    pdf=fitz.open(ROOT/'output'/f'{stem}.pdf');counts[stem]=len(pdf)
    check('pdf',stem+' page count',len(pdf)==expected,len(pdf))
    for i,p in enumerate(pdf):
        text=p.get_text();check('pdf-page',stem+f' {i+1} searchable',len(text.strip())>40)
        bad=[]
        for b in p.get_text('dict')['blocks']:
            for l in b.get('lines',[]):
                for s in l['spans']:
                    x0,y0,x1,y1=s['bbox']
                    if x0<-.5 or y0<-.5 or x1>p.rect.width+.5 or y1>p.rect.height+.5:bad.append((s['text'],s['bbox']))
        check('pdf-page',stem+f' {i+1} text within page',not bad,bad)
        check('pdf-page',stem+f' {i+1} text encoding','\ufffd' not in text and '\x00' not in text)
        for link in p.get_links():
            if link.get('kind')==fitz.LINK_GOTO:check('navigation',stem+f' page{i+1}',0<=link['page']<len(pdf))
    if 'Arbeidsmarkt' in stem:
        check('navigation','9 student bookmarks',len(pdf.get_toc())==9)
        check('navigation','target49 sources facing questions','Bron A' in pdf[45].get_text() and 'Opgave 49' in pdf[46].get_text())
        pm=json.loads((QADIR/(stem+'_page_map.json')).read_text())
        check('pagination','no student page drift',all(p['designed_pages']==[p['pdf_page']] for p in pm))
    pdf.close()
# Pin and verify supplied outlines, independent of installed source location.
reg=ROOT/'sources'/'source-register.json'
if reg.exists():
    data=json.loads(reg.read_text())
    for src in data['uploaded_outlines']:
        got=hashlib.sha256((ROOT/src['local_path']).read_bytes()).hexdigest()
        check('sources',src['local_path'],got==src['sha256'],got)
else:check('sources','source register exists',False)
report={'status':'PASS' if all(c['passed'] for c in checks) else 'FAIL','pages':counts,'exercises':50,'subquestions':92,'targets':6,'target_subquestions':24,'student_figure_placements':24,'solution_figure_placements':8,'checks':checks,'categories':dict(Counter(c['category'] for c in checks)),'limits':['No claim of independent specialist review, live repository approval or classroom-measured learning gains.','Layout is additionally inspected using rendered pages; text-bound checks alone do not prove visual quality.','Arithmetic tests and selected answer tokens supplement, not replace, editorial reading of the full narrative.']}
(QADIR/'validation_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(report['status'],len(checks),'checks;',dict(Counter(c['category'] for c in checks)))
for c in checks:
    if not c['passed']:print('FAIL:',c['category'],c['name'],c['detail'])
sys.exit(0 if report['status']=='PASS' else 1)
