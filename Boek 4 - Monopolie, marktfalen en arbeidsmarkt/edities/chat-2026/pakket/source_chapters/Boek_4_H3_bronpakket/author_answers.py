"""Produce the answer manuscript from the complete exercise registry."""
from pathlib import Path
import json
from html import escape
ROOT=Path(__file__).resolve().parent
E=json.loads((ROOT/'QA/exercises.json').read_text())
from author_common import TITLES
pages=[]
def add(title,body,section='Antwoorden'):
    pages.append({'section':section,'title':title,'body':body})
def fig(name,cap):return f'<figure><img src="_assets/{name}.svg" alt="{escape(cap)}"><figcaption>{cap}</figcaption></figure>'
intro='''<div class="kicker">BOEK 4 · HOOFDSTUK 3</div>
# Antwoorden · Arbeidsmarkt

Dit antwoordboek hoort bij de 50 opgaven van het hoofdstuk. De volgorde en letters zijn gelijk aan die in het leerlingboek.

<div class="box"><b>Rekenen en afronden</b><br>Schrijf eerst de verhouding of vergelijking, vul de waarden in en vermeld de eenheid. Reken tussentijds met de exacte waarde. Rond geldbedragen en percentages zo nodig af op twee decimalen. Een indexcijfer heeft geen euroteken. Het werkloosheidspercentage gebruikt een andere noemer dan participatie.</div>

<div class="box"><b>Betekenis van de antwoorden</b><br>Bij open vragen zijn ook andere antwoorden goed als zij kloppen met de bron en de opgegeven modelaannames. De bonusvragen geven een mogelijk sterk antwoord met beoordelingscriteria, geen verplichte formulering.</div>

<p class="small">De punten staan bij de doeloefeningen in het leerlingboek. Waardeer een correcte werkwijze en passende eenheden; straf dezelfde doorwerkfout niet telkens opnieuw.</p>

<div class="contents">
'''
for s,t in TITLES.items():
 ns=[e['number'] for e in E if e['section']==s]
 intro+=f'<a href="#a{s.replace(".","")}"><b>{s} {t}</b>Opgaven {min(ns)}–{max(ns)}</a>'
intro+='</div><p class="small">Alle numerieke gevallen zijn lesmodellen. Uit modelwerkloosheid volgt geen gemeten Nederlands werkloosheidscijfer. Minimumlonen zijn fictief.</p>'
add('Inhoud',intro)
for s,t in TITLES.items():
 text=f'<a id="a{s.replace(".","")}"></a>\n# {s} · {t}\n\n'
 prev=None
 for e in [x for x in E if x['section']==s]:
  if e['stage']!=prev:text+=f'<div class="answer-stage">{e["stage"]}</div>';prev=e['stage']
  text+='<div class="answer-block" data-answer-exercise="'+str(e['number'])+'">'
  text+=f'<h3 id="antwoord{e["number"]}">Opgave {e["number"]} · {e["title"]}</h3>'
  for q in e['questions']:
   text+=f'<div class="answer-item" data-answer="{q["id"]}"><p><b>{q["label"]}.</b> {q["answer"]}</p></div>'
  text+='</div>'
  if e['answer_fig']:
   text+=fig(e['answer_fig'],f'Solution bij opgave {e["number"]}. De getallen en eenheden horen bij de bijbehorende bron.'.replace('Solution','Uitwerking'))
 add(t,text,s)
(ROOT/'Antwoorden.md').write_text('\n\n'.join('<!-- PAGE '+json.dumps({k:v for k,v in p.items() if k!='body'},ensure_ascii=False)+' -->\n\n'+p['body'] for p in pages))
print('answer coverage',sum(len(e['questions']) for e in E),'subquestions')
