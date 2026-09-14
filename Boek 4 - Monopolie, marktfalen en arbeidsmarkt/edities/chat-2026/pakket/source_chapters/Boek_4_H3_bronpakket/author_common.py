"""Content helpers. All cases are authored teaching models, not observed data."""
from pathlib import Path
import json, re
from html import escape
ROOT=Path(__file__).resolve().parent
PAGES=[]; EXERCISES=[]; FIGURES=[]
STAGE=''; SECTION=''
TITLES={'4.3.1':'Arbeidsvraag en arbeidsproductiviteit','4.3.2':'Arbeidsaanbod, participatie en evenwicht','4.3.3':'Werkloosheid en veranderingen op de arbeidsmarkt','4.3.4':'Minimumloon','4.3.5':'Vakbonden, cao en arbeidsmarktbeleid','4.3.6':'Gemengde opgaven: arbeidsmarkt'}
def section(s):
    global SECTION; SECTION=s

def heading(s):
    global STAGE; STAGE=s
    return '\n\n## '+s+'\n\n'

def page(title, body):
    PAGES.append({'section':SECTION,'title':title,'body':body.strip()})

def box(title,body,kind=''):
    return f'<div class="box {kind}"><b>{title}</b><br>{body}</div>\n\n'

def source(title,body):return f'<div class="source"><b>{title}</b><br>{body}</div>\n\n'
def formula(body):return f'<div class="formula">{body}</div>\n\n'
def fig(name,caption):
    n=len(FIGURES)+1; FIGURES.append({'number':n,'file':name,'caption':caption,'section':SECTION})
    cap=f'Figuur {n}. {caption}'
    return f'<figure><img src="_assets/{name}.svg" alt="{escape(cap,quote=True)}"><figcaption>{cap}</figcaption></figure>\n\n'

def ex(title,context,qa,points=None,answer_fig=None,tags=None):
    n=len(EXERCISES)+1
    if points is None:points=[None]*len(qa)
    out=f'<div class="exercise {"target" if STAGE=="Doeloefening" else ""}" id="opg{n}" data-exercise="{n}"><p><b>Opgave {n} · {title}</b></p>'
    if context:out+=f'<p>{context}</p>'
    qs=[]
    for j,((q,a),pts) in enumerate(zip(qa,points)):
        lab=chr(97+j);id=f'{n}{lab}'
        out+=f'<p data-question="{id}"><b>{lab}.</b> '+(f'<span class="muted">({pts}p)</span> ' if pts else '')+q+'</p>'
        qs.append({'id':id,'label':lab,'prompt':q,'answer':a,'points':pts})
    out+='</div>\n\n'
    EXERCISES.append({'number':n,'title':title,'section':SECTION,'stage':STAGE,'context':context,'questions':qs,'answer_fig':answer_fig,'tags':tags or []})
    return out

def begin(title,goals,lead):
    return f'<a id="s{SECTION.replace(".","")}"></a>\n<div class="kicker">{SECTION} · {TITLES[SECTION].upper()}</div>\n\n# {title}\n\n{lead}\n\n'+box('Lesdoelen',goals,'goals')

def start():return heading('Startopgaven')+'<div class="route"><b>Korte route:</b> Startopgaven → Zelfstandige oefening → Doeloefening. Extra hulp nodig? Maak eerst Begeleide inoefening.</div>\n\n'
def guided():return heading('Begeleide inoefening')+'<p class="small">Heb je deze hulp niet nodig? Ga dan verder met Zelfstandige oefening.</p>\n\n'
def finish_sources():
    order=[]
    for s in ['front']+list(TITLES)+['back']:
        pp=[p for p in PAGES if p['section']==s]
        if not pp:continue
        fname={'front':'00 Inleiding.md','back':'07 Overzicht.md'}.get(s,f'{s} manuscript.md')
        (ROOT/fname).write_text('\n\n'.join('<!-- PAGE '+json.dumps({k:v for k,v in p.items() if k!='body'},ensure_ascii=False)+' -->\n\n'+p['body'] for p in pp),encoding='utf-8');order.append(fname)
    (ROOT/'chapter-order.json').write_text(json.dumps(order,ensure_ascii=False,indent=2))
    (ROOT/'QA'/'exercises.json').write_text(json.dumps(EXERCISES,ensure_ascii=False,indent=2))
    (ROOT/'QA'/'instructional-figures.json').write_text(json.dumps(FIGURES,ensure_ascii=False,indent=2))
    print('Authored:',len(PAGES),'pages,',len(EXERCISES),'exercises,',sum(len(e['questions']) for e in EXERCISES),'subquestions,',len(FIGURES),'figures')

def table(headers,rows):
    return '<table><thead><tr>'+''.join('<th>'+str(x)+'</th>' for x in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+str(x)+'</td>' for x in row)+'</tr>' for row in rows)+'</tbody></table>\n\n'
def ans(text,why):return text+'<br><i>Waarom:</i> '+why
