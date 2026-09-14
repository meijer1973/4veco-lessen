"""Apply the documented 40 -> 48 page instructional revision to the frozen baseline.
Existing targets and exercise identifiers are retained. New exercises use 22A, 40A, 47A.
Run only to regenerate this revision's authored Markdown; normal rebuild uses build_all.py.
"""
from pathlib import Path
from copy import deepcopy
from html import escape
import re,json
ROOT=Path(__file__).resolve().parent
BASE=ROOT/'revision_base'

def chunks(text):
 a=re.split(r'<!-- PAGE (.*?) -->',text,flags=re.S)
 return [dict(json.loads(a[i]),body=a[i+1].strip()) for i in range(1,len(a),2)]
def dump(pages):
 return '\n\n'.join('<!-- PAGE '+json.dumps({k:v for k,v in p.items() if k!='body'},ensure_ascii=False)+' -->\n\n'+p['body'].strip() for p in pages)+'\n'
def fig(name,cap):
 return '<figure><img src="_assets/'+name+'.svg" alt="'+escape(cap,quote=True)+'"><figcaption>'+cap+'</figcaption></figure>'
def exercise(n,title,ctx,qs,kind='practice'):
 return {'number':n,'title':title,'context':ctx,'questions':qs,'kind':kind}
def exhtml(e):
 return '<div class="exercise" id="opg'+str(e['number'])+'"><p><b>Opgave '+str(e['number'])+' · '+e['title']+'</b></p><p>'+e['context']+'</p>'+''.join('<p><b>'+chr(97+i)+'.</b> '+q+'</p>' for i,q in enumerate(e['questions']))+'</div>'

def addpage(sec,title,body):return {'section':sec,'title':title,'body':body.strip()}

new22=exercise('22A','Eerst de drie rekeningen',
 'Op een oefenmarkt voor keramieklesplaatsen krijgt de aanbieder € 4 subsidie per verkochte plaats. Er zijn geen baten voor buitenstaanders en geen uitvoeringskosten. De nieuwe hoeveelheid en prijzen zijn al berekend; oefen hier alleen de surplus- en begrotingsrekening. Q is plaatsen per week; prijzen zijn euro per plaats.',[
 'Vul eerst de tabel onder de bron volledig in. Gebruik voor iedere surplusdriehoek de juiste basis en hoogte. De rij zonder subsidie is als voorbeeld ingevuld.',
 'Bereken hoeveel CS en PS ieder toenemen. Vergelijk hun gezamenlijke toename met de subsidie-uitgaven.',
 'Bereken het welvaartsverlies op twee manieren: met de oude en nieuwe welvaartsmaat en met de driehoek van extra transacties.',
 'Een leerling schrijft: “U = 4 × (70 − 60) = € 40.” Leg uit welke gesubsidieerde verkopen in deze berekening ontbreken.'
], 'guided')
new40=exercise('40A','Eerst alleen een quotum',
 'Verschillende aanbieders verkopen paprikakratten. Vraag: P = 26 − 0,20Q. Aanbod: P = 8 + 0,10Q. P is euro per krat; Q is kratten per week. Het vrije evenwicht is Q₀ = 60 en P₀ = € 14. Er komt uitsluitend een productiequotum van 40 kratten. De rechten zijn gratis verdeeld. Alle 40 toegestane kratten worden geproduceerd en verkocht; er is geen overheidsopkoop.',[
 'Vergelijk het quotum met Q₀. Waarom bindt de maatregel? Welke hoeveelheid wordt werkelijk verkocht?',
 'Vul in: P = 26 − 0,20 × … = … . Teken de quotumgrens in de basisgrafiek en markeer de verkoopprijs op de vraaglijn. Bereken ook het bedrag op A bij Q = 40. Waarom is dat niet de verkoopprijs?',
 'Nu vervangt een quotum van 80 kratten de grens van 40. De rest blijft gelijk. Bepaal de werkelijke hoeveelheid, de marktprijs en de overheidsuitgaven. Beoordeel: “Een quotum van 80 betekent dat er 80 worden geproduceerd.”'
], 'guided')
new47=exercise('47A','Drie berekeningen die overtuigend lijken',
 'Lees de drie berichten hieronder als afzonderlijke markten. Alle bedragen hebben betrekking op één week. Er zijn geen kosten of baten voor buitenstaanders en geen uitvoeringskosten. Noem bij ieder antwoord de juiste grootheid, berekening en reden.',[
 'Bericht A. Aanbieders maken € 3 per verkocht product over aan de overheid. De verkoop daalt van 60 naar 45. Een leerling berekent overheidsontvangsten als 3 × (60 − 45) = € 45. Verbeter de berekening en benoem de hoeveelheid waarover de belasting wordt ontvangen.',
 'Bericht B. Aanbieders krijgen € 2 voor elk verkocht product. De verkoop stijgt van 60 naar 70. CS neemt met € 65 toe en PS ook met € 65. Een leerling noemt de toename van € 130 een welvaartswinst. Bereken de overheidsuitgaven en de verandering van de welvaartsmaat. Beoordeel de conclusie.',
 'Bericht C. Bij een bindende minimumprijs van € 12 zijn Qv = 30 en Qa = 70. Er zijn geen andere kopers, voorraden of overheidsaankopen. Een leerling schrijft: “Er worden 70 verkocht; de overheid betaalt 12 × 40 = € 480.” Verbeter beide uitkomsten. Welke extra afspraak zou de berekende € 480 wél rechtvaardigen?'
], 'mixed')
new17=exercise(17,'Kan de schaal de belastingdruk veranderen?',
 'De twee grafieken hieronder tonen precies dezelfde vraagfunctie: P = 14 − 0,10Q. Q is producten per week; P is euro per product. Alleen de schaal van de verticale as verschilt. Het aanbod en de belasting blijven buiten deze twee afbeeldingen.',[
 'Een leerling noemt de vraag in de linker grafiek minder prijsgevoelig omdat de lijn daar steiler lijkt. Bereken in beide grafieken Q bij P = € 8 en bij P = € 9. Beoordeel de uitspraak.',
 'Kun je uit alleen deze twee vraaggrafieken afleiden welk aandeel van een belasting kopers dragen? Leg uit welke aanvullende informatie je nodig hebt. Leg ook uit waarom het aanpassen van de asschaal op zichzelf geen andere economische uitkomst veroorzaakt.'
], 'practice')

order=json.loads((BASE/'chapter-order.json').read_text())
pages=[]
for f in order:
 for p in chunks((BASE/f).read_text()):
  p['old_page']=len(pages)+1;p['source']=f;pages.append(p)
byold={p['old_page']:p for p in pages}

# Make room for a careful causal argument instead of leaving it after the target.
byold[10]['body']=byold[10]['body'].split('### Wie kan makkelijker reageren?')[0].rstrip()+'''

De breedte van O telt **verkochte producten**. De breedte van W telt juist **transacties die wegvallen**. Bekijk op de volgende pagina hoe dit verschil terugkomt in de bedragen.
'''
# Replace the old optional controlled example by a true critique task; its teaching content moves into core theory.
b=byold[15]['body']
b=re.sub(r'<div class="exercise\s*" id="opg17">.*?</div>',exhtml(new17),b,flags=re.S)
b=re.sub(r'<figure>.*?</figure>',fig('3.1.2_rev_scales','Dezelfde vraag, twee asschalen. De punten geven in beide grafieken dezelfde combinaties van prijs en hoeveelheid.'),b,count=1,flags=re.S)
byold[15]['body']=b
# The subsidy welfare visual is needed BEFORE the worked example and target, not in the bonus.
b=byold[22]['body']
b=re.sub(r'<figure>.*?</figure>','',b,count=1,flags=re.S)
b=b.replace('## Herhaling / Herhaling en interleaving', '''### Twee vragen bij iedere subsidieregeling

**Waarvoor wordt betaald?** Een bedrag per verkoop verandert de opbrengst van een extra verkochte eenheid. Een vast bedrag doet dat in de beschreven situatie niet.

**Welke rekening hoort erbij?** Neem de overheidsuitgaven mee voordat je een welvaartsconclusie trekt. Hetzelfde totaalbedrag kan bij verschillende regelingen andere productieprikkels geven.

## Herhaling / Herhaling en interleaving''')
byold[22]['body']=b
# A focused quota theory page now follows the explicit no-purchase/guaranteed-purchase comparison.
b=byold[31]['body']; b=b[b.index('### Een quotum begrenst de hoeveelheid'):]
b += '''

### Waarom lees je de prijs op de vraaglijn?

De productiegrens bepaalt hier dat er 40 kratten worden verkocht. De vraaglijn vertelt welke prijs particuliere kopers voor dat aantal willen betalen. Bij € 10 vragen zij precies 40 kratten.

Op A staat bij Q = 40 juist € 6. Dat is de marginale kost van die hoeveelheid in dit model, niet de verkoopprijs. Het quotum voorkomt dat de productie door kan groeien tot het vrije evenwicht.

<div class="box small"><b>Niet dezelfde regel</b><br>Een minimumprijs verbiedt lage prijzen. Een quotum verbiedt te veel productie. Dat beide in dit voorbeeld tot een prijs van € 10 leiden, maakt de mechanismen niet hetzelfde.</div>
'''
byold[31]['body']=b
byold[37]['body']=byold[37]['body'].replace('De bronnen staan op pagina 38 en de vragen op pagina 39.', 'De bronnen staan op pagina 38 en de vragen op pagina 39. Opgave 47A is extra gemengde oefening voor de keuze van de juiste hoeveelheid en overheidsrekening.')
# Typo already corrected in the assembled book is also corrected in the standalone source.
byold[40]['body']=byold[40]['body'].replace('Qsubub','Qsub')

additions={}
additions[3]=[addpage('3.1.1','Waarom wordt de aanbodlijn hoger?', '''
### Vergelijk twee prijzen bij dezelfde hoeveelheid

De fruitbekermarkt heeft vraag Pc = 14 − 0,10Q en aanbod Pp = 2 + 0,10Q. Een verkoper draagt **€ 4 per verkochte beker** af. De oorspronkelijke A vertelt nog steeds welk bedrag verkopers willen ontvangen, vóór aftrek van productiekosten.

| Q (bekers per dag) | Bedrag op V: Pc (€ per beker) | Bedrag op A: Pp (€ per beker) | Verschil Pc − Pp (€ per beker) |
|---|---:|---:|---:|
| 20 | 12 | 4 | 8 |
| **40** | **10** | **6** | **4** |
| 60 | 8 | 8 | 0 |

Bij **40 bekers** passen beide kanten én de belasting bij elkaar: kopers betalen € 10, verkopers ontvangen € 6 en de overheid krijgt € 4. Daarom horen beide prijzen bij hetzelfde aantal verkochte bekers.

### Van gewenste ontvangst naar benodigde kopersprijs

Voor 40 bekers geeft A een ontvangst van € 6. De verkoper kan daarvan niet ook nog € 4 afdragen. Hij moet dan € 10 van de koper ontvangen. Deze omzetting geldt bij iedere hoeveelheid:

<div class="formula">Oorspronkelijk aanbod: Pp = 2 + 0,10Q<br>Tel de belasting op: Pc = (2 + 0,10Q) + 4<br>Aanbod in kopersprijzen: Pc = 6 + 0,10Q</div>

De productiekosten veranderen hier niet. A + t geeft dezelfde aanbodbeslissing weer, maar nu in de prijs die kopers moeten betalen. Het snijpunt van **V en A + t** bepaalt de nieuwe hoeveelheid.

<div class="box warning"><b>Niet: oude prijs + hele belasting</b><br>Pc = € 8 + € 4 = € 12 zou Pp = € 8 geven. Bij die twee prijzen worden 20 bekers gevraagd en 60 aangeboden. Dat is geen evenwicht. Laat vraag en aanbod dus eerst samen de nieuwe hoeveelheid bepalen.</div>
''')]
additions[10]=[
addpage('3.1.2','Wat verdwijnt en wat verhuist?', '''
### Houd drie bedragen uit elkaar

In de fruitbekermarkt daalt CS van € 180 naar € 80 per dag. PS daalt evenveel. De overheid krijgt € 160. Het verschil tussen het oude en het nieuwe totaal is € 40.

'''+fig('3.1.2_rev_ledger','Van € 360 aan oud surplus blijft € 320 in de nieuwe welvaartsmaat over. De € 160 belastingopbrengst telt mee; de € 40 verloren voordeel niet.')+'''

De gezamenlijke afname van CS en PS is **€ 200**. Dat bedrag bestaat uit twee delen:

<div class="formula">Verlies van CS en PS: 100 + 100 = € 200<br>Daarvan bij de overheid: € 160<br>Verdwenen voordeel van handel: 200 − 160 = € 40</div>

### Waarom ontstaat dat verloren voordeel?

Bekijk een extra beker rond Q = 50. Op V staat € 9 betalingsbereidheid; op A staat € 7 marginale kosten. Zonder belasting kan die transactie voordeel opleveren. Maar de ruimte van € 2 is niet genoeg om ook de belasting van € 4 te overbruggen. De transactie valt weg.

Alle verdwenen voordelen tussen Qt = 40 en Q₀ = 60 vormen samen driehoek W. Daarom is de basis **20 bekers per dag**, niet 40 verkochte bekers. De hoogte bij Q = 40 is **€ 4 per beker**. De oppervlakte is ½ × 20 × 4 = € 40 per dag.

<div class="box small"><b>Last per verkocht product is niet het hele surplusverlies</b><br>Kopers betalen € 2 extra op 40 verkochte bekers: € 80. Hun CS daalt echter € 100. De overige € 20 is het voordeel op aankopen die wegvallen. Hetzelfde onderscheid geldt voor verkopers.</div>
'''),
addpage('3.1.2','Wie kan makkelijker op de prijs reageren?', '''
### Verander maar één kenmerk

Twee markten beginnen bij **P₀ = € 8 en Q₀ = 60 producten per dag**. Het aanbod is in beide Pp = 2 + 0,10Q. Ook de belasting van € 3 per product is gelijk. Alleen de reactie van de kopers verschilt.

| Vergelijking | Markt A | Markt B |
|---|---:|---:|
| Vraagfunctie | Pc = 14 − 0,10Q | Pc = 20 − 0,20Q |
| Qv bij Pc = € 8 | 60 | 60 |
| Qv bij Pc = € 9 | 50 | 55 |
| Daling door dezelfde prijsstijging | 10 producten | 5 producten |

**B reageert minder sterk.** Kopers blijven bij dezelfde prijsstijging relatief vaker kopen. Verkopers kunnen daardoor een groter deel van de belasting via de prijs doorberekenen. De nieuwe uitkomsten zijn A: Qt = 45, Pc = € 9,50, Pp = € 6,50; B: Qt = 50, Pc = € 10, Pp = € 7.

'''+fig('3.1.2_fig_2','Van dezelfde € 3 belasting draagt de koper in A € 1,50 en in B € 2. De minder prijsgevoelige kopers in B dragen hier het grotere aandeel.')+'''

In A is het kopersaandeel 1,50 / 3 × 100% = **50%**. In B is het 2 / 3 × 100% = **66,67%**. Wie het geld aan de overheid overmaakt, is voor deze vergelijking niet de verklaring.

<div class="box summary"><b>De redenering werkt aan beide kanten</b><br>De kant die minder makkelijk op een prijsverandering kan reageren, draagt relatief meer last. Zijn juist verkopers weinig prijsgevoelig ten opzichte van kopers, dan komt meer last bij verkopers terecht. Vergelijk wel dezelfde uitgangssituatie; een steiler getekende lijn alléén is geen bewijs.</div>
''')]
additions[17]=[addpage('3.1.3','Waarom kan extra handel toch voordeel kosten?', '''
### Volg de drie rekeningen

Bij de workshopplaatsen stijgt Q van 60 naar 80. Kopers betalen € 10 en aanbieders ontvangen in totaal € 14. De overheid legt op **alle 80 plaatsen** € 4 bij: U = € 320 per week.

| Rekening | Zonder subsidie (€ per week) | Met subsidie (€ per week) | Verandering |
|---|---:|---:|---:|
| Consumentensurplus | 180 | 320 | +140 |
| Producentensurplus | 180 | 320 | +140 |
| Overheidsuitgaven | 0 | 320 | +320 uitgaven |
| **CS + PS − U** | **360** | **320** | **−40** |

Kopers en aanbieders krijgen samen **€ 280 meer surplus**. Daar staat een overheidsbetaling van € 320 tegenover. Het verschil van € 40 is in dit model verloren voordeel. De subsidie-uitgaven zélf zijn niet het welvaartsverlies.

'''+fig('3.1.3_fig_3','U betreft alle gesubsidieerde plaatsen. W betreft alleen de extra transacties voorbij Q₀ = 60: basis 20 plaatsen, hoogte € 4 per plaats.')+'''

### Kijk naar één extra plaats

Rond Q = 70 is de betalingsbereidheid 18 − 0,10 × 70 = **€ 11**. De marginale kosten zijn 6 + 0,10 × 70 = **€ 13**. Zo’n extra plaats kost € 2 meer dan het voordeel dat de koper eraan toekent. De subsidie maakt verkoop wel aantrekkelijk voor koper en aanbieder, maar neemt dat verschil niet weg.

<div class="box warning"><b>Wat telt ons model mee?</b><br>We nemen geen extra baten voor buitenstaanders aan. Daarom maakt “meer activiteiten” de uitkomst niet automatisch beter. In Boek 4 onderzoeken we opnieuw subsidies, maar dan mét zulke extra baten.</div>
''')]
additions[19]=[addpage('3.1.3','Oefenen met de welvaartsrekening', '''
### Begeleide inoefening · vervolg

Deze oefening geeft extra steun bij het kiezen van prijzen, hoeveelheden en oppervlakten. Heb je die steun niet nodig? Ga dan door naar Zelfstandige oefening.

'''+exhtml(new22)+'''

<div class="source"><b>Brongegevens</b><br>Vraag: Pc = 30 − 0,20Q. Aanbod: Pp = 6 + 0,20Q.<br>Zonder subsidie: Q₀ = 60; P₀ = € 18.<br>Met subsidie: Qsub = 70; Pc = € 16; Pp = € 20.</div>

| Rekening (€ per week) | Zonder subsidie: voorgedaan | Met subsidie: vul zelf in |
|---|---|---|
| CS | ½ × 60 × (30 − 18) = 360 | ½ × … × (… − …) = … |
| PS | ½ × 60 × (18 − 6) = 360 | ½ × … × (… − …) = … |
| U | 0 | … × … = … |
| CS + PS − U | 360 + 360 − 0 = 720 | … + … − … = … |

<div class="box small"><b>Hulp die je straks weglaat</b><br>CS gebruikt de kopersprijs. PS gebruikt de totale verkopersontvangst. Beide gebruiken de werkelijk verkochte hoeveelheid. Stel bij U apart de vraag: voor welke verkopen betaalt de overheid?</div>
''')]
additions[30]=[addpage('3.1.5','Dezelfde minimumprijs, een andere aankoopregel', '''
### Begin zonder aankoopgarantie

In de appelmarkt is Pmin = € 10. Er worden **40 kratten gevraagd** en **80 aangeboden**. Zonder andere afnemers worden alleen de 40 kratten verkocht die particuliere kopers willen hebben.

'''+fig('3.1.5_rev_nopurchase','Zonder opkoop: Qv = 40 is de werkelijke verkoop; Qa = 80 is het gewenste aanbod bij € 10. Het aanbodoverschot is 40 kratten, geen overheidsaankoop.')+'''

De aanbodlijn vertelt wat telers **willen aanbieden bij een prijs**. Ze bewijst niet dat alle 80 kratten daadwerkelijk worden gemaakt en verkocht. Neem ook niet aan dat de overheid de ontbrekende koper is.

### Voeg nu alleen de opkoopbelofte toe

De overheid belooft elk aangeboden krat dat particulieren niet kopen, tegen € 10 over te nemen. Nu vinden alle aangeboden kratten een afnemer: 40 bij particuliere kopers en 40 bij de overheid.

| Uitkomst per week | Zonder opkoop | Met volledige opkoop |
|---|---:|---:|
| Werkelijke particuliere aankopen | 40 kratten | 40 kratten |
| Overheidsaankopen | 0 kratten | 40 kratten |
| Totale verkopen | 40 kratten | 80 kratten |
| Overheidsuitgaven | € 0 | 40 × € 10 = € 400 |

<div class="box summary"><b>Lees het extra zinnetje in de bron</b><br>De prijs en functies blijven gelijk, maar de overheid wordt een extra koper. De uitgavenrechthoek hoort bij de opkoopbelofte, niet bij elke minimumprijs.</div>
''')]
additions[33]=[addpage('3.1.5','De quotumroute apart oefenen', '''
### Begeleide inoefening · vervolg

Bij opgave 40 vergeleek je twee regelingen. Oefen hier desgewenst eerst de quotumroute afzonderlijk, voordat je de combinatie zelfstandig maakt.

'''+exhtml(new40)+'''

'''+fig('3.1.5_rev_quota_base','Basisgrafiek bij opgave 40A. Teken zelf de productiegrens en zoek daarna de prijs waarbij kopers die hoeveelheid afnemen.')+'''

<div class="box small"><b>Drie controlevragen</b><br>Beperkt het quotum de vrije hoeveelheid? Wordt de toegestane hoeveelheid volgens de bron helemaal verkocht? Welke lijn vertelt wat kopers daarvoor betalen? Een quotum is een maximum, geen productieplicht.</div>
''')]
additions[37]=[addpage('3.1.6','Controleer de aanpak, niet alleen het rekenen', '''
### Extra gemengde oefening

Een berekening kan netjes zijn uitgevoerd en toch de verkeerde economische grootheid gebruiken. Oefen hieronder het kiezen van de juiste hoeveelheid en rekening. Je docent kan deze opgave als extra oefening of als huiswerk gebruiken.

'''+exhtml(new47)+'''

### Zo onderbouw je een correctie

Schrijf niet alleen “fout”. Benoem **welke afspraak uit de bron** bepaalt wat je telt. Maak daarna de berekening en geef aan wat het bedrag betekent. Bij een welvaartsconclusie kijk je naar alle partijen die in de gebruikte welvaartsmaat meetellen.

<div class="box small"><b>Geen nieuwe maatregel</b><br>Je gebruikt uitsluitend bekende belasting-, subsidie- en minimumprijsregels. Daarna pas combineer je in de doeloefening een berekening, grafiek en beleidsconclusie.</div>
''')]

# Make the optional detours usable before the most demanding guided subquestions.
byold[19]['body']=byold[19]['body'].replace('<div class="exercise " id="opg22">', '<p class="small">Extra steun voor de surplusrekening bij 22c vind je in opgave 22A. Die kun je zo nodig eerst maken.</p>\n<div class="exercise " id="opg22">')
byold[33]['body']=byold[33]['body'].replace('<div class="exercise " id="opg40">', '<p class="small">Extra steun voor de quotumvraag 40c vind je in opgave 40A. Die kun je zo nodig eerst maken.</p>\n<div class="exercise " id="opg40">')

# Combine with original page identity, then translate old page references atomically.
newpages=[]
for p in pages:
 newpages.append(p)
 for extra in additions.get(p['old_page'],[]):
  extra['source']=p['source'];extra['added']=True;newpages.append(extra)
assert len(newpages)==48
pmap={p['old_page']:n for n,p in enumerate(newpages,1) if 'old_page' in p}

def pagerefs(text):
 pat=r'\b(pagina(?:’s|\'s|s)?|p\.)\s*(\d+)(?:\s*([–−-])\s*(\d+))?'
 def sub(m):
  a=pmap.get(int(m[2]),int(m[2]));tail=''
  if m[4]:tail='–'+str(pmap.get(int(m[4]),int(m[4])))
  return m[1]+' '+str(a)+tail
 return re.sub(pat,sub,text)
for n,p in enumerate(newpages,1):
 # The inserted descriptions themselves use no old page-number references.
 if 'old_page' in p:p['body']=pagerefs(p['body'])
 if n==1:
  p['body']=re.sub(r'<span>(\d+)</span>',lambda m:'<span>'+str(pmap[int(m[1])])+'</span>',p['body'])
  p['body']+='<div class="small muted">Herziene editie: extra uitleg en oefensteun bij belasting, subsidie en quota. Opgaven 22A, 40A en 47A zijn toegevoegd; de bestaande opgavenummers blijven behouden.</div>'
# Number instructional captions within each paragraph by their actual order.
counts={}
for p in newpages:
 sec=p['section']
 def renum(m):
  counts[sec]=counts.get(sec,0)+1
  cap=re.sub(r'^Figuur \d+\.\s*','',m[1])
  return '<figcaption>Figuur '+str(counts[sec])+'. '+cap+'</figcaption>'
 p['body']=re.sub(r'<figcaption>(.*?)</figcaption>',renum,p['body'],flags=re.S)
for fn in order:
 out=[{k:v for k,v in p.items() if k in ['section','title','body']} for p in newpages if p['source']==fn]
 (ROOT/fn).write_text(dump(out))
(ROOT/'chapter-order.json').write_text(json.dumps(order,ensure_ascii=False,indent=2))
(ROOT/'3.1 Overheidsingrijpen – hoofdstuk.md').write_text('\n\n'.join((ROOT/f).read_text() for f in order))
(ROOT/'QA/page_concordance.json').write_text(json.dumps({'old_to_new':pmap,'added_pages':[n for n,p in enumerate(newpages,1) if p.get('added')],'section_starts':{p['section']:n for n,p in enumerate(newpages,1) if 'id="s31' in p['body']}},ensure_ascii=False,indent=2))

# Readable index stays in reading order, with stable baseline target IDs.
ex=json.loads((BASE/'exercises.json').read_text());out=[]
for e in ex:
 if e['number']==17:e=deepcopy(new17)
 else:e=deepcopy(e);e['context']=pagerefs(e['context']);e['questions']=[pagerefs(q) for q in e['questions']]
 out.append(e)
 if e['number']==22:out.append(new22)
 if e['number']==40:out.append(new40)
 if e['number']==47:out.append(new47)
(ROOT/'exercises.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
(ROOT/'targets-authored.json').write_text((BASE/'targets-authored.json').read_text())
print('Revised student:',len(newpages),'pages;',len(out),'exercises;',sum(len(e['questions']) for e in out),'subquestions')
print('Added pages:',[n for n,p in enumerate(newpages,1) if p.get('added')])
