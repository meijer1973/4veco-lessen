"""Retain all baseline target answers; supply solutions for the revised bonus and added practice."""
from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parent;BASE=ROOT/'revision_base'

def chunks(text):
 a=re.split(r'<!-- PAGE (.*?) -->',text,flags=re.S)
 return [dict(json.loads(a[i]),body=a[i+1].strip()) for i in range(1,len(a),2)]
def dump(pages):
 return '\n\n'.join('<!-- PAGE '+json.dumps({k:v for k,v in p.items() if k!='body'},ensure_ascii=False)+' -->\n\n'+p['body'].strip() for p in pages)+'\n'
def fig(name,cap):return '<figure><img src="_assets/'+name+'.svg" alt="'+cap+'"><figcaption>'+cap+'</figcaption></figure>'
def a(s,w):return {'solution':s,'why':w}
ans=json.loads((BASE/'answers.json').read_text())
ans['17']=[
 a('In beide grafieken is Qv bij € 8: (14 − 8) / 0,10 = <b>60 producten per week</b>. Bij € 9: (14 − 9) / 0,10 = <b>50 producten per week</b>. De prijsstijging is steeds 12,5%; de gevraagde hoeveelheid daalt steeds met 16,67%. De vraag is dus niet in één grafiek minder prijsgevoelig.', 'De formule en economische getallen zijn gelijk. Alleen de hoeveelheid papier per euro op de verticale as verandert.'),
 a('Nee. Voor de lastverdeling moet je de reactie van de vraag <b>ten opzichte van het aanbod</b> kennen. Om bedragen uit te rekenen heb je ook de belasting en de oorspronkelijke marktuitkomst nodig. Een andere asschaal verandert de vraagfunctie, het aanbod of de belasting niet.', 'Een visueel steilere lijn door een andere schaal is geen verandering in gedrag. In de gecontroleerde vergelijking in de uitleg waren uitgangswaarden, aanbod en belasting wel gelijk gehouden.')]
ans['22A']=[
 a('CS = ½ × Qsub × (30 − Pc) = ½ × 70 × (30 − 16) = <b>€ 490</b>. PS = ½ × Qsub × (Pp − 6) = ½ × 70 × (20 − 6) = <b>€ 490</b>. U = s × Qsub = 4 × 70 = <b>€ 280</b>. CS + PS − U = 490 + 490 − 280 = <b>€ 700 per week</b>.', 'Beide driehoeken hebben als basis de 70 werkelijk verkochte plaatsen. CS gebruikt Pc, PS de totale ontvangst Pp. De overheid betaalt voor alle 70 plaatsen.'),
 a('CS stijgt met 490 − 360 = <b>€ 130</b>; PS ook met <b>€ 130</b>. Samen is dat € 260. De overheid betaalt € 280, dus <b>€ 20 meer</b> dan de gezamenlijke surpluswinst.', 'De stijging van het particuliere surplus moet worden vergeleken met het bedrag dat daarvoor wordt betaald.'),
 a('Via de welvaartsmaat: W = 720 − 700 = <b>€ 20 per week</b>. Via de driehoek: basis = 70 − 60 = 10 plaatsen per week; hoogte = s = € 4 per plaats. W = ½ × 10 × 4 = <b>€ 20 per week</b>.', 'Bij deze rechte vraag- en aanbodlijnen vormt het nadeel van de extra transacties een driehoek. Beide routes beschrijven hetzelfde verlies.'),
 a('De leerling telt de <b>60 plaatsen die ook zonder subsidie zouden zijn verkocht</b> niet mee. Ook die komen in aanmerking: 60 × 4 = € 240. Samen met 10 × 4 = € 40 is U = <b>€ 280 per week</b>.', 'De bron noemt subsidie per verkochte plaats, niet alleen voor de extra verkopen.')]
ans['40A']=[
 a('Het quotum van 40 ligt onder Q₀ = 60. Het bindt. Volgens de bron worden alle toegestane kratten verkocht: <b>40 kratten per week</b>.', 'Het maximum sluit de vrije evenwichtshoeveelheid uit; de bron legt de werkelijke productie en verkoop vast.'),
 a('P = 26 − 0,20 × <b>40</b> = <b>€ 18 per krat</b>. Teken Q = 40 verticaal en markeer (40; 18) op V. Op A staat 8 + 0,10 × 40 = <b>€ 12 per krat</b>. Dat is het marginale-kostenbedrag bij deze hoeveelheid, niet de prijs waartegen kopers de 40 kratten afnemen.', 'De vraaglijn geeft de prijs bij de beperkt beschikbare verkochte hoeveelheid. Het quotum verhindert uitbreiding tot het vrije evenwicht.'),
 a('80 is meer dan Q₀ = 60; de nieuwe grens bindt niet. Dus <b>Q = 60 kratten per week</b> en <b>P = € 14 per krat</b>. Overheidsuitgaven: <b>€ 0</b>. De uitspraak is onjuist: 80 is toegestaan als maximum, maar productie van 80 is niet verplicht.', 'Een niet-bindend quotum laat het vrije evenwicht toe. De gratis rechten en afwezigheid van opkoop leveren geen overheidsbetaling op.')]
ans['47A']=[
 a('O = t × Qt = 3 × 45 = <b>€ 135 per week</b>. Gebruik de 45 verkochte producten, niet de 15 verdwenen verkopen.', 'Over een product dat niet meer wordt verkocht, ontvangt de overheid deze belasting niet.'),
 a('U = s × Qsub = 2 × 70 = <b>€ 140 per week</b>. Verandering welvaartsmaat = toename CS + toename PS − U = 65 + 65 − 140 = <b>−€ 10 per week</b>. Er is dus € 10 welvaartsverlies, geen € 130 welvaartswinst.', 'De overheidsuitgaven ontbreken in de redenering van de leerling. In deze bron zijn geen extra baten voor buitenstaanders die dat veranderen.'),
 a('Zonder extra kopers worden <b>30 producten per week</b> verkocht. Het aanbodoverschot is 70 − 30 = <b>40 producten</b>, maar U = <b>€ 0</b>. Bij een expliciete garantie dat de overheid alle 40 overtollige aangeboden producten tegen € 12 koopt, zou U = 12 × 40 = <b>€ 480 per week</b> gelden.', 'Een minimumprijs op zichzelf is geen aankoopgarantie. Gewenst aanbod is niet automatisch gerealiseerde afzet.')]
ex=json.loads((ROOT/'exercises.json').read_text());titles={str(e['number']):e['title'] for e in ex}
def block(n):
 return '<div class="answer-block" id="ans'+n+'"><h3>Opgave '+n+' · '+titles[n]+'</h3>'+''.join('<p><b>'+chr(97+i)+'.</b> '+a['solution']+'</p><p class="why"><b>Waarom:</b> '+a['why']+'</p>' for i,a in enumerate(ans[n]))+'</div>'
pages=chunks((BASE/'Antwoorden.md').read_text())
# Replace only the changed bonus, leaving every target solution intact.
for p in pages:
 if 'id="ans17"' in p['body']:
  p['body']=re.sub(r'<div class="answer-block" id="ans17">.*?</div>',block('17'),p['body'],flags=re.S)
  p['body']=p['body'].replace('Het antwoord vergelijkt de vraagreactie vanaf dezelfde uitgangswaarden, verbindt dat met de aandelen in de belasting en benoemt de constant gehouden omstandigheden.', 'Het antwoord herkent identieke economische getallen bij andere asschalen, gebruikt procenten of aantallen consistent en benoemt de ontbrekende aanbodinformatie voor de lastverdeling.')
# The first page's summary is updated without changing any exercise numbering.
pages[0]['body']=pages[0]['body'].replace('48 opgaven','51 opgaven').replace('131 deelvragen','141 deelvragen').replace('40 pagina’s','48 pagina’s')
pages[0]['body']+='\n\n<div class="small">Herziene editie. Toegevoegde opgaven: 22A, 40A en 47A. Bonus 17 is herschreven. De zes doeloefeningen en hun antwoorden zijn ongewijzigd.</div>'
new=[]; amap={}
for i,p in enumerate(pages,1):
 amap[i]=len(new)+1;new.append(p)
 if i==12:
  new.append(dict(section='3.1.3',title='Extra steun bij de subsidieboekhouding',body=block('22A')))
 if i==22:
  new.append(dict(section='3.1.5',title='De quotumroute afzonderlijk',body=block('40A')+'\n\n'+fig('3.1.5_rev_quota_answer','Opgave 40A: het bindende quotum geeft 40 kratten voor € 18. Bij het niet-bindende quotum van 80 blijft het vrije evenwicht 60 kratten voor € 14.')))
 if i==26:
  new.append(dict(section='3.1.6',title='Een overtuigende berekening controleren',body=block('47A')))
new[0]['body']=re.sub(r'^(\| 3\.1\.\d.*?\|)(\s*)(\d+)(\s*\|)$', lambda m:m[1]+m[2]+str(amap[int(m[3])])+m[4],new[0]['body'],flags=re.M)
new[0]['body']=new[0]['body'].replace('| 19–27 |','| 19–27, incl. 22A |').replace('| 37–45 |','| 37–45, incl. 40A |').replace('| 46–48 |','| 46–48, incl. 47A |')
(ROOT/'Antwoorden.md').write_text(dump(new))
(ROOT/'3.1 Overheidsingrijpen – antwoorden.md').write_text(dump(new))
(ROOT/'answers.json').write_text(json.dumps(ans,ensure_ascii=False,indent=2))
(ROOT/'QA/answer_page_concordance.json').write_text(json.dumps(amap,indent=2))
print('Answers:',len(new),'designed pages')
