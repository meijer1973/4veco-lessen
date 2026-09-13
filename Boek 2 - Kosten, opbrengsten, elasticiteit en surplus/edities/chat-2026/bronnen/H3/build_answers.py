"""Build the complete solution book, retaining each subanswer and its explanation."""
from pathlib import Path
import re
from bs4 import BeautifulSoup
from weasyprint import HTML
from build import ROOT, OUTPUT, embedded_html, render_markdown
FRONT='''<p class="kicker">4VECO · ECONOMIE · 4 VWO · BOEK 2</p>
<h1>Antwoorden<br>Surplus en welvaart</h1>
<p class="lead">Hoofdstuk 2.3</p>
<p>Dit antwoordenboek hoort bij de nieuw geschreven editie met 38 leerlingpagina’s. Opgavenummers beginnen bij iedere paragraaf opnieuw.</p>
<div class="box"><b>Zo controleer je je werk</b><br>Vergelijk de gekozen hoeveelheid, het gemarkeerde gebied, basis en hoogte, de berekening, de eenheid en de economische conclusie. Verbeter de eerste fout in je redenering, niet alleen het laatste getal.</div>
<p><b>Afronden.</b> Reken tussendoor ongerond. Rond geldbedragen zo nodig af op twee decimalen. Q heeft een hoeveelheidseenheid; P en MK zijn in euro per product; de surplusbedragen zijn in euro.</p>
<p><b>Grafieken.</b> Andere passende assenschalen zijn goed. De snijpunten, lijnen, gemarkeerde hoeveelheden en gebieden moeten overeenkomen. Een label, arcering of duidelijke kleur is goed zolang het gebied herkenbaar is.</p>
<p><b>Uitleg.</b> Andere woorden met dezelfde economische betekenis kunnen ook goed zijn. Bij denkertjes staan modelantwoorden en criteria; er kan meer dan één goede uitwerking bestaan.</p>
<div class="contents"><a href="#ant-2.3.1"><b><em class="toc-page">2</em>2.3.1 · Consumentensurplus</b><span>Opgaven 1–11</span></a><a href="#ant-2.3.2"><b><em class="toc-page">6</em>2.3.2 · Producentensurplus en totaal surplus</b><span>Opgaven 1–11</span></a><a href="#ant-2.3.3"><b><em class="toc-page">10</em>2.3.3 · Pareto-efficiëntie en welvaartsverlies</b><span>Opgaven 1–9</span></a><a href="#ant-2.3.4"><b><em class="toc-page">14</em>2.3.4 · Gemengde opgaven</b><span>Opgaven 1–7</span></a></div>
<div class="box warning"><b>Model en losse transactie</b><br>Surplusoppervlakken worden berekend met doorlopende rechte lijnen. Bij de Pareto-uitleg gebruik je de gegeven waarden van één mogelijke extra transactie om te laten zien dat zij voordelig en haalbaar is. Die puntvergelijking is geen afzonderlijke integraalberekening over een heel interval.</div>'''

def build_answers():
 text=(ROOT/'2.3 Surplus en welvaart – antwoorden.md').read_text()
 # Literal numbered subanswers avoid renderer resets on interrupted HTML lists.
 text=re.sub(r'^([1-9])\) ',r'\1\\) ',text,flags=re.M)
 soup=BeautifulSoup(render_markdown(text),'html.parser'); grouped=BeautifulSoup('','html.parser');current=None
 for node in list(soup.contents):
  if not getattr(node,'name',None):continue
  boundary=node.name in ('h1','h2')
  part=(node.name=='p' and re.match(r'^(?:[a-z]|[1-9])\)',node.get_text().strip())) or node.name=='ol'
  if boundary:
   grouped.append(node);current=None
  else:
   if part or current is None:
    current=grouped.new_tag('div',attrs={'class':'answer-block'});grouped.append(current)
   current.append(node)
 for h in grouped.find_all('h1'):
  h['id']='ant-'+h.get_text().split()[0];h['class']='answer-section'
 out=embedded_html('<section class="answer-front">'+FRONT+'</section><main class="answer">'+str(grouped)+'</main>','Antwoorden · Boek 2 · Surplus en welvaart',extra_css='''
@page { @top-left {content:"4veco / Antwoorden";} }
.answer-front{break-after:page;}
h1.answer-section{break-before:auto;break-after:avoid;font-size:22pt;border-bottom:1.5pt solid #17688f;padding-bottom:9pt;margin-top:20pt;}
.answer h2{font-size:14pt;margin:11pt 0 6pt;}
.answer{font-size:11.1pt;line-height:1.31;}
.answer p{margin-bottom:5pt;}
.answer .answer-block{margin-bottom:6pt;break-inside:avoid;}
.answer table{font-size:10pt;}
.answer figure{margin:8pt 0 9pt;}
''')
 (OUTPUT/'Boek_2_H3_Antwoorden.html').write_text(out)
 d=HTML(string=out,base_url=str(ROOT)).render();d.write_pdf(OUTPUT/'Boek_2_H3_Antwoorden.pdf')
 print('Answer PDF:',len(d.pages),'pages;',len(re.findall(r'^## Opgave ',text,re.M)),'exercises')
 return len(d.pages)
if __name__=='__main__':build_answers()
