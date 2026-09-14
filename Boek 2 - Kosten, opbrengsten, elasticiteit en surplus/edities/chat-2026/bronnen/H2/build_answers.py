"""Render the Markdown answer manuscript to a self-contained HTML file and PDF."""
from pathlib import Path
import re, json
from bs4 import BeautifulSoup
from weasyprint import HTML
from build import ROOT, OUTPUT, render_markdown, embedded_html

TITLES={'2.2.1':'Prijselasticiteit','2.2.2':'Elasticiteit en omzet','2.2.3':'Inkomenselasticiteit en kruislingse elasticiteit','2.2.4':'Gemengde opgaven'}
FRONT='''<p class="kicker">4VECO · ECONOMIE · 4 VWO</p>
<h1>Antwoorden<br>Elasticiteit</h1>
<p class="lead">Boek 2 · Hoofdstuk 2.2</p>
<p>Dit antwoordenboek hoort bij de nieuw geschreven editie met 36 leerlingpagina’s. De opgavenummers beginnen bij elke paragraaf opnieuw.</p>
<div class="box"><b>Zo controleer je je werk</b><br>Vergelijk de gekozen verhouding, de ingevulde waarden, het teken, de eenheid en de economische uitleg. Kijk niet alleen of het laatste getal hetzelfde is. Verbeter een fout met een volledige berekening of redenering.</div>
<p><b>Afronden.</b> Reken tussendoor ongerond. Rond einduitkomsten zo nodig af op twee decimalen. Een exacte breuk of meer decimalen kan ook goed zijn. Elasticiteiten hebben geen eenheid; omzet heeft wél een geldeenheid en periode.</p>
<p><b>Drie inkomenscategorieën.</b> In deze methode geldt: Ei &lt; 0 inferieur goed; 0 &lt; Ei &lt; 1 normaal goed; Ei &gt; 1 luxegoed. Ei = 0 en Ei = 1 blijven grenswaarden.</p>
<p><b>Formuleringen.</b> Andere zinnen met dezelfde economische betekenis kunnen ook goed zijn. Bij denkertjes staan modelantwoorden en beoordelingscriteria. Gebruik bij een mogelijke verklaring geen sterkere zekerheid dan de bron toelaat.</p>
<div class="contents">
<a href="#ant-2.2.1"><b>2.2.1 · Prijselasticiteit</b><span>Opgaven 1–10</span></a>
<a href="#ant-2.2.2"><b>2.2.2 · Elasticiteit en omzet</b><span>Opgaven 1–10</span></a>
<a href="#ant-2.2.3"><b>2.2.3 · Inkomenselasticiteit en kruislingse elasticiteit</b><span>Opgaven 1–11</span></a>
<a href="#ant-2.2.4"><b>2.2.4 · Gemengde opgaven</b><span>Opgaven 1–7</span></a>
</div>
'''

def build_answers(source=None):
    source=Path(source) if source else ROOT/'2.2 Elasticiteit – antwoorden.md'
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
        starts_part=(node.name=='p' and re.match(r'^(?:[a-z]|[1-9])\)',node.get_text().strip())) or node.name=='ol'
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
    # Keep the review tail together at the section end, and start the mixed
    # target answer on a fresh page rather than leaving only answer 1 below it.
    sec = None
    for heading in soup.find_all(['h1', 'h2']):
        if heading.name == 'h1':
            sec = heading.get_text().split()[0]
        else:
            m = re.match(r'Opgave (\d+)\b', heading.get_text())
            if m and (sec, int(m.group(1))) in {('2.2.1', 8), ('2.2.4', 5)}:
                heading['style'] = 'break-before:page'
    html=embedded_html('<section class="answer-front">'+FRONT+'</section><main class="answer">'+str(soup)+'</main>', 'Antwoorden · Boek 2 · Elasticiteit',extra_css='''
@page { @top-left {content:"4veco / Antwoorden";} }
.answer-front{break-after:page;}
h1.answer-section{break-before:page;font-size:22pt;border-bottom:1.5pt solid #17688f;padding-bottom:10pt;}
.answer h2{font-size:14pt;margin:14pt 0 8pt;}
.answer{font-size:11.4pt;line-height:1.33;}
.answer p{margin-bottom:6pt;}
.answer .answer-block{margin-bottom:7pt;}
.answer table{font-size:9.8pt;}
.answer figcaption{font-size:9.2pt;}
''')
    (OUTPUT/'Boek_2_H2_Antwoorden.html').write_text(html)
    d=HTML(string=html,base_url=str(ROOT)).render()
    d.write_pdf(OUTPUT/'Boek_2_H2_Antwoorden.pdf')
    print('Answer PDF:',len(d.pages),'pages; answers:',len(re.findall(r'^## Opgave ', source.read_text(),re.M)))
    return len(d.pages)
if __name__=='__main__':build_answers()
