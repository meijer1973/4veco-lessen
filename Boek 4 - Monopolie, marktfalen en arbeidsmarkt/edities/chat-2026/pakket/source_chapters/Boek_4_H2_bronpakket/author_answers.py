"""The answer model is stored with each exercise, so no subquestion is lost."""
from pathlib import Path
import json
from html import escape
ROOT=Path(__file__).resolve().parent
from author_common import TITLES
E=json.loads((ROOT/'QA/exercises.json').read_text())
pages=[]
def page(sec,title,body):pages.append({'section':sec,'title':title,'body':body})
page('Antwoorden','Inhoud','''<div class="kicker">BOEK 4 · HOOFDSTUK 2 · ANTWOORDBOEK</div>
# Marktvormen en marktfalen

Dit antwoordboek hoort bij de leerlingtekst van hoofdstuk 4.2. De nummers van de opgaven en deelvragen zijn gelijk. Alle rekenuitkomsten horen bij de vereenvoudigde brongegevens, niet bij gemeten werkelijke markten.

| Paragraaf | Opgaven |
|---|---|
| 4.2.1 Welvaartseffecten van monopolie | 1–9 |
| 4.2.2 Prijsdiscriminatie | 10–18 |
| 4.2.3 Marktvormen vergelijken | 19–27 |
| 4.2.4 Negatieve externe effecten | 28–36 |
| 4.2.5 Positieve externe effecten | 37–45 |
| 4.2.6 Overheidsingrijpen bij marktfalen | 46–54 |
| 4.2.7 Gemengde opgaven | 55–60 |

### Gebruik het antwoord als controle
Vergelijk niet alleen de einduitkomst. Controleer de hoeveelheid, de juiste prijs, alle maatschappelijke posten en de eenheid. Een antwoord dat een belastingoverdracht als echte schade behandelt, is niet goed doordat er toevallig hetzelfde eindbedrag uitkomt.

### Bij uitlegvragen
De gegeven formulering is een voorbeeldantwoord. Accepteer een andere duidelijke formulering wanneer de economische redenering klopt en de conclusie door de bron wordt gedragen. Voor het denkertje is vooral de kwaliteit van het argument belangrijk.

### Tekening en rekenwerk
De oplossingsfiguren laten gevraagde gebieden en punten zien. Een andere leesbare schaal of arcering is mogelijk, mits assen, prijzen, hoeveelheden en gebieden correct zijn. In de leerlingenversie zijn basisgrafieken geleverd; leerlingen hoeven de lijnen niet onnodig opnieuw te tekenen.

<div class="box warning"><b>Drie vaste controles</b><br>PS is niet hetzelfde als winst. MO is niet hetzelfde als de verkoopprijs of maatschappelijke baten. Een overheidsbetaling is niet hetzelfde als een echt extern effect.</div>
''')
for sec,title in TITLES.items():
 body=f'<a id="ant{sec.replace(".","")}"></a>\n\n# {sec} · {title}\n\n'
 current=''
 for e in [e for e in E if e['section']==sec]:
  if current!=e['stage']:
   current=e['stage'];body+=f'<div class="answer-stage"'+(' style="break-before:page"' if e['number']==58 else '')+f'>{current}</div>\n\n'
  body+='<div class="'+('answer-long' if e['number']==58 else 'answer-block')+'">\n'
  body+=f'<h3 id="antwoord{e["number"]}">Opgave {e["number"]} · {e["title"]}</h3>\n'
  for q in e['questions']:
   body+=f'<p class="answer-item" data-answer="{q["id"]}"><b>{q["label"]}.</b> {q["answer"]}</p>\n'
  if e['answer_fig']:
   fs=e['answer_fig'] if isinstance(e['answer_fig'],list) else [e['answer_fig']]
   for f in fs:body+=f'<figure><img src="_assets/{f}.svg" alt="Oplossingsfiguur bij opgave {e["number"]}"><figcaption>Oplossingsfiguur bij opgave {e["number"]}. De rekenuitkomsten en de gevraagde markeringen horen bij dezelfde brongegevens.</figcaption></figure>\n'
  if 'Bonus' in e['stage']:
   body+='<p class="assessment-note"><b>Beoordeling:</b> een eigen antwoord is passend als de genoemde aannames, ontbrekende informatie en conclusie logisch verbonden zijn. Alleen een losse mening is onvoldoende.</p>\n'
  body+='</div>\n\n'
 page(sec,'Antwoorden',body)
(ROOT/'Antwoorden.md').write_text('\n\n'.join('<!-- PAGE '+json.dumps({k:v for k,v in p.items() if k!='body'},ensure_ascii=False)+' -->\n\n'+p['body'] for p in pages),encoding='utf-8')
