"""Teacher guide, alignment and source boundaries. No classroom-timing or independent-review claim."""
from pathlib import Path
import json,hashlib,shutil
R=Path(__file__).resolve().parent
P=[]
def page(t,b):P.append({'section':'Docent','title':t,'body':b})
def box(t,b):return f'<div class="box"><b>{t}</b><br>{b}</div>'
page('Overzicht','''<div class="kicker">4VECO · BOEK 3 · HOOFDSTUK 3.1</div>
# Docenteninformatie<br>Overheidsingrijpen

**Doelgroep:** 4 vwo. **Leerlingdeel:** 40 pagina’s inclusief opening, uitleg, voorbeelden, alle opgaven en overzicht. **Structuur:** vijf theorieparagrafen en één consolidatieparagraaf. **Opgaven:** 48, met 131 deelvragen; zes nieuwe doeloefeningen. De vijf volledig uitgewerkte voorbeelden zijn geen genummerde opgaven.

### Welke bronnen sturen deze editie?

De door de gebruiker aangeleverde **Book 3 outline proposal v2** bepaalt de inhoud, volgorde, grenzen en doelopgavebriefs. De **Book 4 outline proposal v2** bepaalt de latere toepassingen die hier juist niet worden vooruitgelopen. De gebruiker heeft deze bijlagen voor deze bouwopdracht boven de oudere repositoryoutline geplaatst.

De huidige repositoryrichtlijn **econ-exercise-builder.md** bepaalt de zeven zichtbare oefenkoppen, het terugwaartse ontwerp, de papieren kernroute, het afbouwen van ondersteuning en de antwoordmodellen. De grafiekstandaard bepaalt onder meer assen, eenheden, schaal en overeenstemming van grafiek en getal.

'''+box('Nieuwe targets, geen stilzwijgende registry-overname','De bijlagen bevatten doelopgavebriefs, geen afgewerkte opgaven. De zes doeloefeningen in deze editie zijn daarom nieuw ontworpen uit die briefs. Zij zijn niet gepresenteerd als reeds officieel goedgekeurde registry-targets of als CvTE-opgaven. Er is niets naar GitHub geschreven.')+'''
### Wat blijft op papier compleet?

Alle uitleg, voorbeelden, startwerk, begeleide ondersteuning, zelfstandige oefening en targets staan in het hoofdstuk. Voor grafiekvragen zijn de oorspronkelijke marktcurven meegeleverd. Het noodzakelijke nieuwe tekenen betreft een beleidslijn, prijs/hoeveelheidsmarkeringen of een oppervlakte, niet steeds een nieuw assenstelsel.

### Wat is niet automatisch verplicht?

De korte route is Startopgaven → Zelfstandige oefening → Doeloefening. Begeleide inoefening is een alternatieve ondersteuningsstap naar hetzelfde doel. Bonus is geen vereiste voor de basisroute. Herhaling is geschikt als huiswerk of gespreid startwerk.

<div class="small muted">Alle beleidsbronnen en getallen zijn fictief. Het hoofdstuk geeft geen actuele juridische tarieven, geen empirische effectschatting en geen volledige beleidsbeoordeling buiten de genoemde modelvoorwaarden.</div>
''')

page('Lestijd en differentiatie','''# Lestijd: een planning, geen meting

De onderstaande optelsommen zijn ontwerpschattingen voor leerlingen die de gebruikte Boek 1/2-technieken met korte herhaling kunnen uitvoeren. Een 55-minutenoptelsom is **geen bewijs dat iedere klas het haalt**. Oefen de figuurconventies expliciet wanneer die nog niet vlot gaan.

| § | Motivatie | Uitleg | Voorbeeld | Samenvatting / overgangen | Start | Zelfstandig | Doel | Totaal |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 3.1.1 | 3 | 9 | 6 | 2 | 6 | 14 | 15 | 55 |
| 3.1.2 | 2 | 8 | 6 | 2 | 6 | 15 | 16 | 55 |
| 3.1.3 | 2 | 9 | 7 | 2 | 5 | 14 | 16 | 55 |
| 3.1.4 | 3 | 8 | 6 | 2 | 6 | 15 | 15 | 55 |
| 3.1.5 | 2 | 9 | 7 | 2 | 5 | 14 | 16 | 55 |

Het langere targetbudget dan de algemene richtlijn van 8–12 minuten is bewust: meerdere prijs- of surplusberekeningen én grafiekmarkering vragen hier meer tijd. Het wordt niet verstopt door alleen leerlingwerktijd te tellen.

**Consolidatie 3.1.6:** 2 minuten opening + 5 methodebespreking + 1 overgang + 8 opgave 46 + 8 opgave 47 + 25 opgave 48 + 6 terugblik = **55 minuten**. Geen nieuw-theorievoorbeeld toevoegen.

### Eerste inzet: reserveer ruimte

Plan voor een gemiddelde eerste inzet liever **7–9 lessen voor het hoofdstuk** dan vooraf te eisen dat iedere paragraaf één les is. Vooral 3.1.2 en 3.1.5 kunnen twee lessen vragen; ook 3.1.3 kan extra oefentijd nodig hebben. Dit is extra tijd voor bestaande doelen, geen nieuwe telparagraaf.

Een mogelijke tweelessenroute voor een rekenzware paragraaf:

**Les A:** 2 motivatie + 12 uitleg + 8 voorbeeld + 2 samenvatting + 6 start + 18 begeleide inoefening + 7 terugkijken = 55.

**Les B:** 3 korte herneming + 15 zelfstandige oefening + 16 doeloefening + 10 feedback + 8 herhaling + 3 afronding = 55.

### Differentiatie zonder een lager einddoel

Laat het relevante ophaaldeel van Startopgaven eventueel vóór de instructie maken. Houd de gedrukte volgorde ongewijzigd. Bij de begeleide route leest de leerling eerst een volledig uitgewerkt beeld; daarna volgt een formule-invulling met minder steun. Zelfstandig werk en target behouden de oorspronkelijke curven maar verwijderen de oplossingsmarkeringen. Een vastloper vraagt eerst om het juiste onderscheid, niet om nog meer cijfers.
''')

page('Afstemming: belasting en subsidie','''# Afstemming van doel en oefenroute

De pagina’s verwijzen naar het leerlingdeel. Elke target vraagt alleen bewerkingen die zijn voorgedaan of relevant worden opgehaald. De kolom “zelfstandig” is de voorbereiding zonder geleide oplossingsstappen.

| § / doelbewerking | Uitleg en voorbeeld | Start / begeleid | Zelfstandig | Target |
|---|---|---|---|---|
| 3.1.1 Vrij evenwicht | p. 3–4; vergelijking en invulling | 1a; 4b gebruikt dezelfde vergelijkingstechniek | 5a | 7a |
| Aanbod in Pc, Qt, Pc, Pp | p. 2–4; geldstroom en nieuwe vergelijking | 2; 3; 4a–b | 5b; 6a | 7b–c |
| Nieuwe lijn en wig markeren | p. 3; voorgedane figuur | 3; 4c | 5c | 7d |
| Afdragen versus dragen | p. 2 en 4 | 2b; 3c | 5d; 6b | 7e |
| 3.1.2 Last / afwenteling | p. 9 en 11 | 12; 13c | 14a | 16a |
| O en surplusvergelijking | p. 10–11; volledige gebieden en tabel | 10; 11; 12–13 | 14b–c | 16b–d |
| Relatieve prijsgevoeligheid | p. 10; conclusie bij voorbeeld p. 11 | procenten / Ev uit Boek 2; bonus 17 is extra contrast | 15 | 16e |
| 3.1.3 Omgekeerde wig en prijzen | p. 16–18; oorspronkelijke en verlaagde A | 19; 21–22 | 23a | 25a |
| Budget en verdeling voordeel | p. 17–18; U over alle verkopen | 20; 21c; 22c | 23b; 24 | 25b–c |
| Welvaartsmaat met U | p. 17–18; CS + PS − U | 22c | 23c; 24b | 25d–e |

### Waarom de tassenmarkt terugkeert

Opgave 16 gebruikt bewust de markt van opgave 7. Dat is een doorlopende toepassing, geen onbedoelde contextkopie: 3.1.1 ontwerpt het nieuwe evenwicht; 3.1.2 gebruikt de uitkomst om belastingdruk en welvaart te onderzoeken. Alle benodigde gegevens staan bij opgave 16 opnieuw vermeld, zodat een eerdere rekenfout niet doorwerkt.

### Grafieken ondersteunen de bewerking

Blauw = vraag / consumentensurplus; groen = oorspronkelijk aanbod / producentensurplus; paars = beleidslijn of overheidsbudget; warm accent = wig of welvaartsverlies. Letters en teksten dragen de betekenis ook zonder kleur. O, U en W zijn niet onderling verwisselbaar. De subsidiefiguur op p. 17 toont de budgetrechthoek al vóór zelfstandig werk en target.
''')

page('Afstemming: grenzen en consolidatie','''# Afstemming van prijs- en hoeveelheidsgrenzen

| § / doelbewerking | Uitleg en voorbeeld | Start / begeleid | Zelfstandig | Target |
|---|---|---|---|---|
| 3.1.4 Binding beoordelen | p. 23–25; bindend en niet-bindend | 28; 29; 31a,d | 32a; 33 | 34a,e |
| Qv, Qa, verkopen, tekort | p. 23–25; één prijs, meerdere aantallen | 28b; 30; 31b | 32b | 34b |
| Grafiekmarkering | p. 23; volledig voorgedaan | 30b; 31c | 32c | 34c |
| Toegang en toewijzing | p. 24–25 | 30c | 32d | 34d |
| 3.1.5 Minimumprijs en overschot | p. 30–32; eigen bindingstoets | 37; 38; 39; 40a | 41a; 42a | 43a–b |
| Publieke aankopen en U | p. 30–32; rechthoek en aankoopregel | 39; 40b | 41b; 42b | 43c |
| Quotum als alternatief | p. 31–32; aparte figuur, geen stapeling | 40c | 41c; 42b | 43d–e |
| 3.1.6 Modelselectie | geen nieuwe theorie | 46; 47 | dezelfde opgaven vereisen eigen selectie | 48a–b,e |
| Prijs, budget en welvaart verbinden | technieken 3.1.1–3.1.4 | eerdere onafhankelijke opgaven | 46–47 | 48c–d |
| Bronclaim begrenzen | terugkerend in alle theorieparagrafen | uitspraken in 6, 15, 24, 33 en 42 | bronselectie p. 37 | 48f |

### Bewust begrensde belasting van de leerling

De maximumprijs-target vraagt geen volledige surplusboekhouding. De nieuwe kern is binding, feitelijke verkoop en toegang. De toewijzingsvoorwaarde wordt wel expliciet behandeld; bonus 35 gebruikt reeds bekende individuele surplusberekening om het belang ervan zichtbaar te maken.

Bij minimumprijs en quota worden twee regelingen **na elkaar**, niet tegelijk doorgerekend. De extra quota-vergelijking blijft beperkt tot binding, hoeveelheid, prijs en begroting. Er wordt geen model van verhandelbare rechten, quotumrente of veiling geïntroduceerd.

Opgave 48 combineert een belastingcase met een maximumprijscontrast. Er is één verplichte grafiekbewerking. De leerling hoeft niet alle vijf instrumenten in één enorme opgave af te handelen. De rekenroute van plan B vraagt daarom geen tweede grafiek en geen onvoorbereide volledige welvaartsrangschikking.

### Inkomende kennis is niet automatisch beheerst

Vraag, aanbod en evenwicht uit Boek 1 en percentages, surplus en de betekenis van marginale kosten uit Boek 2 zijn **eerder onderwezen, ophalen nodig**. Onzekere grafiek- of rekenvaardigheid krijgt de begeleide route of extra lestijd. De belastingwig, subsidieprikkel en de mechaniek van de prijs-/productiegrenzen zijn nieuw formeel leren, geen stilzwijgend veronderstelde voorkennis.
''')

page('Precisie en bekende valkuilen','''# Didactische en economische precisie

| Veelgemaakte fout | Herstelvraag of correctie |
|---|---|
| Pp is winst per product. | Welke productiekosten moeten nog van de ontvangst af? |
| Pc = P₀ + belasting. | Voldoen vraag en aanbod dan bij dezelfde nieuwe hoeveelheid? |
| Wie afdraagt, draagt alles. | Vergelijk Pc en Pp afzonderlijk met P₀. |
| Belastingopbrengst is W. | Teken de budgetrechthoek en de gemiste transacties apart. |
| Subsidie over alleen extra verkoop. | Welke verkopen zijn volgens de bron subsidiabel? |
| CS + PS stijgt, dus welvaart stijgt. | Wie betaalt de subsidie? Trek U af. |
| Een maximum/minimum wordt altijd de marktprijs. | Is het vrije evenwicht nog toegestaan? |
| Qa betekent altijd feitelijke productie/verkoop. | Welke aankoop- en voorraadregel staat in de bron? |
| Een quotum is een minimumprijs. | Wat wordt direct begrensd: hoeveelheid of prijs? |
| De hele opkooprekening is verlies. | Wat weten we over gebruikswaarde en reële bijkomende kosten? |

### Specifieke modelvoorwaarden

De markten zijn lineaire, competitieve oefenmodellen zonder gelijktijdige veranderingen in andere factoren. De oorspronkelijke aanbodlijn krijgt waar nodig de marginale-kosteninterpretatie uit Boek 2. Alle gebruikte belastingen en subsidies laten een positieve verhandelde hoeveelheid toe; er wordt geen algemene formule voor elke denkbare grenssituatie geclaimd.

Bij maximumprijzen is geen extra aanvoer, tenzij vermeld. De targets geven de toewijzing expliciet. Er wordt niet beweerd dat de hoogste betalingsbereidheid gelijkstaat aan de grootste behoefte of de eerlijkste verdeling.

Bij volledige publieke opkoop is het aanbodoverschot daadwerkelijk afzetbaar. Zonder opkoop worden de niet-gekochte aangeboden hoeveelheden niet stilzwijgend als gerealiseerde productie behandeld. De waarde van publiek aangeschafte goederen is niet gegeven; daarom volgt geen ongevraagde numerieke welvaartsrekening voor opkoop.

### Taal en formulering

De teksten gebruiken korte Nederlandse zinnen en de terminologie uit de bijlagen. Tabellen met lege vakken bevatten eerst een invulopdracht. In grafieken staan variabele, eenheid en schaal. Qsub is gekozen in plaats van Qs om verwarring met de Engelse notatie voor aanbod te voorkomen. De leerling gebruikt Qa voor aanbod.
''')

page('Doorlopende leerlijn','''# Doorwerking naar de rest van Boek 3 en 4

| Nu onderwezen methode | Later gebruik volgens de bijlagen | Nieuwe betekenis die dan nog moet worden geleerd |
|---|---|---|
| Belastingwig en O | 3.3.3 invoerheffing | Belasting alleen over ingevoerde eenheden, niet alle binnenlandse verkopen. |
| Quotum en feitelijke transacties | 3.3.3 importquotum | Verschil tussen een productiegrens en een grens aan import. |
| Marktmodel en prijs | 3.2 volkomen concurrentie | Marktprijs verbinden aan het individuele bedrijf; formele outputkeuze. |
| Belasting en surplus | 4.2.4 negatieve externe effecten | Schade aan buitenstaanders verandert de relevante welvaartsmaat. |
| Subsidie en U | 4.2.5 positieve externe effecten | Baten voor buitenstaanders kunnen de welvaartsconclusie veranderen. |
| Minimumprijs | 4.3.4 minimumloon | Prijs wordt loon; werknemers bieden arbeid aan; arbeidseenheid en modelgrenzen. |

### Niet alvast meenemen

Dit hoofdstuk gebruikt geen monopolie, MO = MK-optimalisatie, afgeleiden, arbeidsproductiviteit, loonevenwicht of internationale-handelsberekeningen. De handels- en arbeidsmarktcontexten zijn geen vereiste voorkennis. Reactiefuncties, strategische spellen en actuele wettelijke tarieven worden evenmin ingevoerd.

### Eerst een eenvoudig model, later een andere aanname

De negatieve welvaartsuitkomst van belasting of subsidie in de voorbeeldmarkt is geen universeel politiek oordeel. Er zijn hier geen kosten of baten voor buitenstaanders. In Boek 4 worden belasting en subsidie juist opnieuw toegepast wanneer die veronderstelling verandert. De nieuwe externe-effectbetekenis moet dan expliciet worden uitgelegd; alleen de techniek mag als herhaling terugkomen.

### Formatieve terugblik

Vraag leerlingen na de target kort: welke prijs gebruikte je, welke transacties telde je en welke bronvoorwaarde bepaalde je antwoord? Noteer foutsoorten in plaats van alleen het eindcijfer. Vergelijk een verkeerd bedrag bij een correct model niet met een perfect uitgerekend verkeerd model.

De drie hoofdfouten die over paragrafen heen terugkomen zijn: verkeerde economische grootheid, verkeerde daadwerkelijk verhandelde hoeveelheid en een te sterke conclusie. De antwoordmodellen bevatten daarom bij iedere deelvraag een toelichting op het waarom.
''')

b3=R/'bronnen/book-3-outline-v2(1).md';b4=R/'bronnen/book-4-outline-v2(1).md'
for source in [b3,b4]:
    if not source.is_file():
        raise FileNotFoundError(f'Vereiste bron ontbreekt: {source}')
hashes={source.name:hashlib.sha256(source.read_bytes()).hexdigest() for source in [b3,b4]}
page('Bronnen en controlegrenzen','''# Bronnen, uitvoering en controlegrenzen

**Inhoudelijke basis:** de twee geüploade outlines v2, gedateerd 6 september 2026. Hun hoofdstuk- en paragraafstructuur is aangehouden. De oorspronkelijke bestanden zijn ongewijzigd opgenomen in de map `bronnen` van het bronpakket.

**Geraadpleegde repositoryrichtlijnen:**

- `4veco-platform/RESEARCH_AGENT_MAP.md` en `4veco-lessen/RESEARCH_AGENT_MAP.md`: navigatie en bron-/outputgrens.
- `4veco-platform/skills/econ-exercise-builder.md`: terugwaarts ontwerp, zeven oefenkoppen, tijd en antwoordmodellen.
- `4veco-platform/skills/economic-graph.md`: assen, eenheden, plotgeometrie, leesbaarheid en afbouw van ondersteuning.

De platformreferentie bij deze controle was `96416b6b5bd57094576e9aba0a42d682584ec479`. De maps waren via de GitHub-connector bereikbaar. De huidige oudere Book 3 registry-targets zijn niet gebruikt als inhoudelijke vervanging voor de bijlagen.

### Wat de lokale controle wel doet

`validate.py` controleert het maximum van 40 leerlingpagina’s, de pagina-indeling, opgave-/deelvraagdekking in de antwoorden, de zes targets, de vijf reeksen oefenkoppen, de benodigde assets, formule-uitkomsten en de uit functies berekende grafiekpunten en -oppervlakten. De resultaten staan in `QA/validation.json` en `QA/LOCAL_REVIEW.md`.

De leerling-, antwoord- en docent-PDF worden gerenderd om te controleren op afbreking, onleesbare overlap, ontbrekende figuren en tekst buiten de pagina. De bronbestanden en bouwscripts worden samen geleverd; de hoofdstukken uit Boek 2 zijn niet gewijzigd.

### Wat deze controle niet bewijst

Er heeft geen onafhankelijke specialistbeoordeling, klasproef of nieuwe audit van het examenprogramma plaatsgevonden. Het bronpakket claimt geen uitgevoerde repository-CI, formele targetintegratie of goedgekeurde uitrol. De afgewerkte documenten zijn afzonderlijke leveringen voor de gebruiker. Voor integratie moeten de nieuwe targets en hun afstemming via de normale platformroute worden beoordeeld.

### Bestandsidentiteit van de bijlagen

<div class="small">Book 3 SHA-256:<br>'''+hashes[b3.name]+'''<br><br>Book 4 SHA-256:<br>'''+hashes[b4.name]+'''</div>
''')

if __name__=='__main__':
    (R/'Docenteninformatie.md').write_text('\n\n'.join('<!-- PAGE '+json.dumps({k:v for k,v in p.items() if k!='body'},ensure_ascii=False)+' -->\n\n'+p['body'] for p in P))
    (R/'bronnen/source_manifest.json').write_text(json.dumps({'outline_priority':'uploaded_v2','sha256':hashes,'platform_main':'96416b6b5bd57094576e9aba0a42d682584ec479','guideline_blobs':{'econ-exercise-builder.md':'5504c8e8a325864978c76867b15b857c118df19d','economic-graph.md':'938d5e61c46de0d60b8bdeaf0aced2572715c2d0'}},indent=2))
    print('Teacher designed pages:',len(P))
