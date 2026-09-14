"""Update teacher navigation, first-use planning and traceable revision review."""
from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parent;BASE=ROOT/'revision_base'

def chunks(text):
 a=re.split(r'<!-- PAGE (.*?) -->',text,flags=re.S)
 return [dict(json.loads(a[i]),body=a[i+1].strip()) for i in range(1,len(a),2)]
def page(title,body):return dict(section='Docent',title=title,body=body.strip())
def dump(pages):return '\n\n'.join('<!-- PAGE '+json.dumps({k:v for k,v in p.items() if k!='body'},ensure_ascii=False)+' -->\n\n'+p['body'].strip() for p in pages)+'\n'
m={int(k):v for k,v in json.loads((ROOT/'QA/page_concordance.json').read_text())['old_to_new'].items()}
def refs(text):
 def f(a):return a[1]+' '+str(m.get(int(a[2]),int(a[2])))+('–'+str(m.get(int(a[4]),int(a[4]))) if a[4] else '')
 return re.sub(r'\b(pagina(?:’s|s)?|p\.)\s*(\d+)(?:\s*([–-])\s*(\d+))?',f,text)
pages=chunks((BASE/'Docenteninformatie.md').read_text())
for p in pages:p['body']=refs(p['body'])
pages[0]['body']=pages[0]['body'].replace('40 pagina’s','48 pagina’s').replace('**Opgaven:** 48, met 131 deelvragen','**Opgaven:** 51, met 141 deelvragen')
pages[0]['body']+='''

<div class="box small"><b>Wat deze herziening verandert</b><br>Acht extra leerlingpagina’s versterken de uitleg vóór de targets. Opgaven 22A en 40A bieden extra steun; 47A biedt extra gemengde oefening. Bonus 17 is herschreven. Alle bestaande opgavenummers en de zes targets blijven behouden. Achterin deze handleiding staat de beoordeling van de oorspronkelijke 40-pagina-editie.</div>
'''
lesson1=page('Lestijd · belasting en subsidie', '''
# Meer uitleg, geen verplichte extra stapel

De extra pagina’s vervangen geen leerdoel en voegen geen nieuw beleidsonderwerp toe. Ze maken bestaande stappen kleiner. Dat maakt een rekenzware paragraaf niet vanzelf een les van 55 minuten. Reserveer bij eerste inzet **ongeveer negen lessen**, met ruimte voor één of twee extra feedback-/ondersteuningslessen.

De routes hieronder zijn **ontwerpschattingen**, geen gemeten leerlingtijden. Het startwerk mag vóór de uitleg worden gemaakt. De gedrukte volgorde blijft hetzelfde.

| Les | Concrete route | Minuten |
|---|---|---:|
| 3.1.1 | Start 1–2: 6; motivatie: 3; uitleg inclusief dezelfde-Q-tabel: 12; voorbeeld: 8; zelfstandig 5–6: 10; doel 7: 13; terugblik: 3 | 55 |
| 3.1.2 A | Start 10–11: 6; motivatie: 2; uitleg gebieden en rekeningen: 14; voorbeeld: 8; begeleid 12–13: 18; terugblik: 7 | 55 |
| 3.1.2 B | Ophalen: 3; gecontroleerde prijsgevoeligheidsvergelijking: 10; zelfstandig 14–15: 15; doel 16: 18; feedback: 9 | 55 |
| 3.1.3 A | Start 19–20: 5; motivatie: 2; uitleg omgekeerde wig en welvaart: 12; voorbeeld: 8; begeleid 21–22: 20; terugblik: 8 | 55 |
| 3.1.3 B | Ophalen: 4; 22A of gerichte feedback op 22: 14; zelfstandig 23–24: 14; doel 25: 17; terugblik: 6 | 55 |

### Niet alles is cumulatief verplicht

Begeleide inoefening is een ondersteuningsroute naar dezelfde target. Een leerling die 22c niet kan structureren, kan eerst **22A** maken. Wie de rekening al beheerst, gebruikt die tijd voor eigen fouten of een uitlegvergelijking. Bonus en herhaling komen niet stilzwijgend boven op de 55 minuten.

### Waar de extra uitleg essentieel is

De gecontroleerde vergelijking op leerlingpagina **13** hoort vóór het zelfstandige werk en de doelvraag over prijsgevoeligheid. De subsidiefiguur op leerlingpagina **21** hoort vóór de welvaartsrekening. Deze twee kernonderdelen staan niet meer alleen bij bonuswerk.
''')
lesson2=page('Lestijd · grenzen en consolidatie', '''
# Grenzen, quota en modelkeuze

| Les | Concrete route | Minuten |
|---|---|---:|
| 3.1.4 | Motivatie: 3; uitleg: 8; voorbeeld: 6; overgangen: 2; start 28–29: 6; zelfstandig 32–33: 15; doel 34: 15 | 55 |
| 3.1.5 A | Start 37–38: 5; motivatie: 2; uitleg prijsgrens en opkoop: 12; voorbeeld stappen 1–3: 7; begeleid 39 en 40a–b: 18; vergelijking en feedback: 11 | 55 |
| 3.1.5 B | Uitleg quotum en voorbeeld stap 4: 10; 40A of feedback op 40c: 10; zelfstandig 41–42: 14; doel 43: 16; terugblik: 5 | 55 |
| 3.1.6 | Opening: 2; methodebespreking: 5; overgang: 1; opgave 46: 8; opgave 47: 8; doel 48: 25; terugblik: 6 | 55 |

### Een echte tussenstap bij quota

De leerling kan **40A vóór 40c** gebruiken. Eerst wordt uitsluitend een quotum bekeken: binding → werkelijk verkochte hoeveelheid → prijs op V → controle van de overheidsregel. Daarna volgt de vergelijking met minimumprijs en opkoop. Dezelfde methode staat later in zelfstandige opgave 41 en doelopgave 43.

### Extra gemengde oefening 47A

Gebruik 47A als huiswerk vóór de consolidatieles of als gerichte herhaling na fouten met O, U en werkelijke verkoop. Reserveer circa **10–15 minuten**. De oefening is niet verplicht boven op de bestaande 55-minutenroute. Bij veel verwarring kan zij opgave 46 of 47 tijdens de les vervangen; laat de overgeslagen oefening dan desgewenst later terugkomen.

### Wat bewust niet is uitgebreid

De maximumprijsparagraaf heeft al binding, niet-binding, het onderscheid Qv/Qa/verkopen en een expliciete toewijzingsvoorwaarde. De target vraagt terecht geen nieuwe, volledige welvaartsrekening onder rantsoenering. Daar zijn geen extra pagina’s nodig.

De zes doeloefeningen zijn behouden. De toegevoegde steun maakt hun bewerkingen toegankelijker; ze verhoogt de eindnorm niet en maakt het bonuswerk niet verplicht.
''')
new=pages[:1]+[lesson1,lesson2]+pages[2:]
# Correct the now-outdated alignment account of where the core comparison is taught.
for p in new:
 p['body']=p['body'].replace('p. 11; conclusie bij voorbeeld p. 14 | procenten / Ev uit Boek 2; bonus 17 is extra contrast','p. 13; gecontroleerde vergelijking vóór voorbeeld en target | procenten / Ev uit Boek 2; bonus 17 toetst nu de asschaal')
 p['body']=p['body'].replace('20; 21c; 22c |','20; 21c; 22c; 22A |').replace('| 22c | 23c; 24b |','| 22c; 22A | 23c; 24b |')
 p['body']=p['body'].replace('| 40c | 41c; 42b |','| 40c; 40A | 41c; 42b |')
 p['body']=p['body'].replace('26, 33 en 42','26, 33 en 42')
 p['body']=p['body'].replace('controleert het maximum van 40 leerlingpagina’s','controleert de herziene editie van 48 leerlingpagina’s en het maximum van 50')
 p['body']=p['body'].replace('De leerling-, antwoord- en docent-PDF worden gerenderd','De leerling-, antwoord- en docent-PDF worden gerenderd')
 p['body']=p['body'].replace('een 40-pagina-editie','een 48-pagina-editie')
# Two-page traceable review, without claiming causation or empirical learning gains.
review=[page('Beoordeling van de oorspronkelijke editie','''
<div class="kicker">REDACTIONELE HERBEOORDELING · UITGANGSPUNT: 40 PAGINA’S</div>
# Was het hoofdstuk te compact?

**Ja, op enkele belangrijke overgangen. Niet doordat hele leerdoelen ontbreken of het lettertype te klein is.** De oorspronkelijke editie bevat alle zes paragrafen en de gevraagde targetbewerkingen. De meeste pagina’s hebben voldoende witruimte. De zwakte zit vooral in het tempo van uitleg naar een samengestelde opgave.

Dit oordeel is gebaseerd op vergelijking van de **werkelijk geleverde tekst, figuren, opgaven en antwoorden** met de aangeleverde outline. Het is een didactische beoordeling, geen meting van leerlingenresultaten. Uit de bestanden blijkt niet welke afzonderlijke passage destijds letterlijk wegens paginagebrek is geschrapt.

| Onderdeel | Concrete waarneming in de oude editie | Gevolg voor deze herziening |
|---|---|---|
| Belastingwig | p. 3–4: formule, verschoven lijn en oplossing volgen snel op elkaar. | Extra tussenstap: vergelijk bij dezelfde Q de twee prijzen en leid A + t uit de ontvangst af. |
| Last en welvaart | p. 10–11: budgetrechthoek, verloren handel, meerdere rekeningen en prijsgevoeligheid worden kort achter elkaar uitgelegd. | Scheid de rekening van de gedragsverklaring; voeg een bedragenbeeld en transactievoorbeeld toe. |
| Relatieve prijsgevoeligheid | De gecontroleerde cijfervergelijking staat pas op p. 15 bij bonus 17, ná doelopgave 16e. | Breng die vergelijking vóór het zelfstandige werk en de target. Bonus 17 wordt een echte schaalcritiek. |
| Subsidiewelvaart | p. 17–18: U, CS/PS en verlies moeten snel gecombineerd worden. De verliesfiguur staat pas op p. 22 bij bonus. | Verplaats de figuur vóór het voorbeeld, leg de overheidsrekening apart uit en bied extra invulsteun. |
| Minimumprijs en quota | p. 30–34: minimumprijs, volledige opkoop en quotum staan dicht op elkaar; de eerste begeleide opgave combineert ze al. | Toon zonder/met opkoop afzonderlijk en laat de quotumroute eerst los oefenen. |

**Maximumprijs behouden.** Op p. 23–29 zijn de kernverschillen al behoorlijk uitgewerkt. Extra volledige surplusberekeningen zouden de scope vergroten in plaats van een aantoonbare leemte oplossen.

<div class="small">Paginanummers in deze beoordeling zijn die van het oorspronkelijke losse hoofdstuk. In het oorspronkelijke complete Boek 3 tel je er 4 bij op.</div>
'''),page('Waar de acht extra pagina’s voor dienen','''
# Acht pagina’s met een gerichte functie

| Nieuwe pagina | Functie | Concrete winst in de oefenroute |
|---|---|---|
| 4 | Eén hoeveelheid, twee prijzen | De belastingvergelijking krijgt een economische verklaring; niet alleen een algebraïsche handeling. |
| 12 | Verplaatst en verloren voordeel | Onderscheid verlies van CS/PS, overheidsontvangsten en W. Ook last per product versus totaal surplusverlies wordt uitgelegd. |
| 13 | Gecontroleerde prijsgevoeligheid | De vergelijking uit het oude bonuswerk staat nu in de kernuitleg, met dezelfde uitgangssituatie en numerieke reactie. |
| 21 | Subsidie: drie rekeningen en extra transacties | Het grotere CS/PS wordt verbonden met U en de verliesdriehoek vóór de leerling moet rekenen. |
| 24 | Extra begeleide oefening 22A | Een deels voorgedane tabel oefent prijskeuze, oppervlakte, begroting en controle van de uitkomst. |
| 36 | Minimumprijs zonder/met opkoop | Gewenst aanbod, particuliere verkopen, publieke aankopen en budget worden los van elkaar zichtbaar. |
| 40 | Extra begeleide oefening 40A | Een bindend en niet-bindend quotum, inclusief de prijslezing op V, vóór de zelfstandige vergelijking. |
| 45 | Extra gemengde oefening 47A | Corrigeer een verkeerde belastingbasis, vergeten subsidie-uitgaven en onterechte overheidsopkoop. |

### Omvang, herkenbaarheid en navolgbaarheid

**40 → 48 leerlingpagina’s: +8, binnen de toegestane +10.** De zes paragrafen en zes doeloefeningen blijven bestaan. De oorspronkelijke nummering blijft herkenbaar: alleen 22A, 40A en 47A komen erbij. Het totaal wordt **51 opgaven met 141 deelvragen**. Bonus 17 is inhoudelijk herschreven; de overige wijzigingen in bestaande opgaven zijn paginaverwijzingen.

Er komen geen extra beleidsmodellen, actuele belastingregels, externe-effectberekeningen of onvoorbereide quota-opbrengsten bij. De typfout Qsubub in de oude losse overzichtspagina is hersteld naar Qsub, zoals al in het complete boek was gebeurd.

### Navigatie en controle

De paragrafen beginnen op **2, 10, 19, 28, 35 en 44**; het hoofdstukoverzicht staat op **48**. De bronnen en vragen van doelopgave 48 blijven tegenover elkaar staan: **46–47**. Alle paginaverwijzingen, antwoorden en bronindexen zijn aangepast.

De lokale controle rekent de marktgevallen en nieuwe bedragen na, vergelijkt de targetteksten en -antwoorden met de oude versie, controleert de grafiekgeometrie en controleert de PDF-pagina’s. Zij vervangt geen onafhankelijke vakreview of klasproef. Extra gedrukte steun is niet automatisch extra verplicht werk in dezelfde les.
''')]
new+=review
(ROOT/'Docenteninformatie.md').write_text(dump(new))
(ROOT/'Beoordeling_en_wijzigingen.md').write_text(dump(review))
(ROOT/'QA/revision_summary.json').write_text(json.dumps({'student_pages_old':40,'student_pages_new':48,'added_pages':8,'exercise_count':51,'subquestion_count':141,'added_exercises':['22A','40A','47A'],'rewritten_exercise':17,'unchanged_target_ids':[7,16,25,34,43,48],'teacher_designed_pages':len(new),'review_designed_pages':len(review)},indent=2))
print('Teacher',len(new),'pages; review',len(review),'pages')
