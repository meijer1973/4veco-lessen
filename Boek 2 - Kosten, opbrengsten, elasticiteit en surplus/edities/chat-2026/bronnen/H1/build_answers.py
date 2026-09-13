"""Render the Markdown answer manuscript to a self-contained HTML file and PDF."""
from pathlib import Path
import re, json
from bs4 import BeautifulSoup
from weasyprint import HTML
from build import ROOT, OUTPUT, render_markdown, embedded_html

TITLES={'2.1.1':'Kostenstructuren','2.1.2':'Opbrengsten, winst en break-even','2.1.3':'Marginale kosten en marginale opbrengsten','2.1.4':'Gemengde opgaven'}
FRONT='''<p class="kicker">4VECO · ECONOMIE · 4 VWO</p>
<h1>Antwoorden<br>Kosten en opbrengsten</h1>
<p class="lead">Boek 2 · Hoofdstuk 2.1</p>
<p>Dit antwoordenboek hoort bij de nieuw opgebouwde editie van het hoofdstuk. De opgavenummers beginnen bij elke paragraaf opnieuw.</p>
<div class="box"><b>Zo controleer je je werk</b><br>Vergelijk niet alleen het eindantwoord. Controleer ook de gekozen formule, de ingevulde getallen, de eenheid en de uitleg. Verbeter een fout met een volledige berekening.</div>
<p><b>Afronden.</b> Reken tussendoor met ongeronde getallen. Rond geldbedragen en niet-gehele uitkomsten aan het einde af op twee decimalen, tenzij anders aangegeven. Voor het eerste gehele productaantal zonder verlies rond je een niet-gehele break-even-uitkomst naar boven af.</p>
<p><b>Marginale bedragen.</b> MK en MO horen hier bij een tabelstap. Bij een stap van meer dan één product zijn het gemiddelde extra bedragen per extra product in die stap. Een streepje in de eerste rij betekent: er is geen voorafgaande rij om mee te vergelijken.</p>
<p><b>Andere antwoorden.</b> Een andere duidelijke formulering met dezelfde economische betekenis kan ook goed zijn. Bij denkertjes staan modelantwoorden en beoordelingscriteria; er kunnen meerdere goede oplossingen zijn.</p>
<div class="contents">
<a href="#ant-2.1.1"><b>2.1.1 · Kostenstructuren</b><span>Opgaven 1–10</span></a>
<a href="#ant-2.1.2"><b>2.1.2 · Opbrengsten, winst en break-even</b><span>Opgaven 1–11</span></a>
<a href="#ant-2.1.3"><b>2.1.3 · Marginale kosten en marginale opbrengsten</b><span>Opgaven 1–10</span></a>
<a href="#ant-2.1.4"><b>2.1.4 · Gemengde opgaven</b><span>Opgaven 1–7</span></a>
</div>
'''

def build_answers(source=None):
    source=Path(source) if source else ROOT/'2.1 Kosten en opbrengsten – antwoorden.md'
    if not source.exists():raise FileNotFoundError(source)
    body=render_markdown(source.read_text())
    soup=BeautifulSoup(body,'html.parser')
    # Keep each sub-answer with its table, explanation, and any solution figure.
    grouped=BeautifulSoup('', 'html.parser')
    current=None
    for node in list(soup.contents):
        if not getattr(node,'name',None):
            continue
        boundary=node.name in ('h1','h2')
        starts_part=node.name=='p' and re.match(r'^[a-z]\)',node.get_text().strip())
        if boundary:
            grouped.append(node)
            current=None
        else:
            if starts_part or current is None:
                current=grouped.new_tag('div',attrs={'class':'answer-block'})
                grouped.append(current)
            current.append(node)
    soup=grouped
    for h in soup.find_all('h1'):
        sec=h.get_text().split()[0];h['id']='ant-'+sec;h['class']='answer-section'
    html=embedded_html('<section class="answer-front">'+FRONT+'</section><main class="answer">'+str(soup)+'</main>', 'Antwoorden · Boek 2 · Kosten en opbrengsten',extra_css='''
@page { @top-left {content:"4veco / Antwoorden";} }
.answer-front{break-after:page;}
h1.answer-section{break-before:page;font-size:22pt;border-bottom:1.5pt solid #17688f;padding-bottom:10pt;}
.answer h2{font-size:14pt;margin:14pt 0 8pt;}
.answer p{margin-bottom:7pt;}
.answer table{font-size:9.8pt;}
.answer figcaption{font-size:9.2pt;}
''')
    (OUTPUT/'Boek_2_H1_Antwoorden.html').write_text(html)
    d=HTML(string=html,base_url=str(ROOT)).render()
    d.write_pdf(OUTPUT/'Boek_2_H1_Antwoorden.pdf')
    print('Answer PDF:',len(d.pages),'pages; answers:',len(re.findall(r'^## Opgave ', source.read_text(),re.M)))
    return len(d.pages)
if __name__=='__main__':build_answers()
