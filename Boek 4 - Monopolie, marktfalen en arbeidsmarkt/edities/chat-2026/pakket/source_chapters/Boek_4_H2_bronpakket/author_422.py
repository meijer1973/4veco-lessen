from author_common import *
def author():
 section('4.2.2')
 page('Dezelfde dienst, een andere prijs',begin('Waarom krijgt de één korting?',
 'Je kunt prijsdiscriminatie herkennen en de voorwaarden uitleggen. Je kunt twee gescheiden groepen vergelijken met één gezamenlijke prijs. Je kunt omzet, kosten, winst en de verdeling van surplus beoordelen.',
 'Twee bezoekers gebruiken dezelfde klimhal, op hetzelfde tijdstip. Een student betaalt minder dan een andere bezoeker. De toegang kost de hal evenveel. Waarom verkoopt de hal niet aan iedereen voor dezelfde prijs?')+box('Prijsdiscriminatie','Een aanbieder vraagt verschillende prijzen voor hetzelfde product of dezelfde dienst, terwijl het prijsverschil niet door een verschil in kosten wordt verklaard.','definition')+'''
### Drie voorwaarden moeten passen
De aanbieder heeft **enige marktmacht**: hij kan zijn prijs beïnvloeden. Hij kan groepen met een verschillende betalingsbereidheid of prijsgevoeligheid **herkennen en apart behandelen**. En kopers kunnen het goed niet gemakkelijk goedkoop kopen en vervolgens doorverkopen aan de duurdere groep.

Een persoonlijk toegangsbewijs kan doorverkoop verhinderen. Twee afzonderlijke prijzen werken niet als iedereen zonder controle het goedkoopste kaartje kan kiezen.
'''+fig('422_conditions','De aanbieder moet de groepen werkelijk kunnen scheiden. Alleen een andere prijslijst is niet genoeg.')+box('Niet elk prijsverschil is prijsdiscriminatie','Een product thuisbezorgen kan duurder zijn doordat bezorging extra kost. Een luxere kamer is niet dezelfde dienst als een eenvoudige kamer. Beschrijf daarom eerst het product en de kosten.','warning'))
 page('De bekende methode, nu tweemaal','''### Elke groep heeft haar eigen vraag
Groep A en groep B reageren ieder op hun eigen prijs. De aanbieder bepaalt binnen elke groep één uniforme prijs. De twee prijzen mogen wel verschillen.

Voor een sporthal geldt in een oefenweek: **P_A = 36 − Q_A** en **P_B = 20 − Q_B**. Prijzen zijn euro per bezoek; hoeveelheden zijn bezoeken per week. Q_A loopt van 0 tot 36 en Q_B van 0 tot 20. Andere vraagfactoren blijven gelijk.

De marginale kosten zijn steeds **€ 4 per extra bezoek**, ook als beide groepen samen meer komen. De capaciteit is ruim genoeg voor 56 bezoeken. Daarom kunnen we de bekende MO/MK-keuze voor elke groep apart uitvoeren.
'''+fig('422_groups','De twee panelen gebruiken dezelfde schaal. Lees de prijs van iedere groep af op haar eigen vraaglijn, niet op MO.')+formula('Per groep: MO = MK → Q → P op de eigen vraaglijn<br>TO totaal = P_A × Q_A + P_B × Q_B<br>TK totaal = TCK + 4 × (Q_A + Q_B)')+box('Constante kosten tel je eenmaal','Het zijn twee klantgroepen van één bedrijf. Dezelfde huur of installatie is niet ineens twee keer nodig. Als MK zou afhangen van de totale productie, kun je beide groepen niet zomaar los optimaliseren. Dat complexere geval gebruiken we hier niet.','warning'))
 page('Een prijsvergelijking uitwerken',heading('Uitgewerkt voorbeeld')+'''
**Avondhal** gebruikt de gegevens van de vorige pagina. De constante kosten zijn € 64 per week. Met één gemeenschappelijke prijs van € 16 verkoopt de hal 20 bezoeken aan A en 4 aan B. De bron geeft deze gemeenschappelijke prijs; we hoeven hem niet opnieuw te bepalen. Er zijn geen externe effecten.

**1 · Herken de voorwaarden.** De groepen gebruiken dezelfde voorziening en kosten per bezoek evenveel. Persoonlijke passen houden de groepen gescheiden. Beide vraagfuncties blijven bij de vergelijking gelijk.

**2 · Bepaal de aparte keuzes.** Voor A: MO_A = 36 − 2Q_A = 4 → Q_A = 16 en P_A = € 20. Voor B: MO_B = 20 − 2Q_B = 4 → Q_B = 8 en P_B = € 12. Bij beide groepen ligt MO vóór deze hoeveelheid boven MK en erna eronder.

**3 · Bereken het bedrijfsresultaat.**

| Per week | Eén prijs | Twee groepsprijzen |
|---|---:|---:|
| Totale afzet | 20 + 4 = 24 | 16 + 8 = 24 |
| TO | 16 × 24 = € 384 | 20 × 16 + 12 × 8 = € 416 |
| TK | 64 + 4 × 24 = € 160 | 64 + 4 × 24 = € 160 |
| Winst | € 224 | € 256 |

**4 · Kijk ook naar kopers.** A betaalt meer en koopt minder; B betaalt minder en koopt meer. CS_A daalt van ½ × 20 × 20 = € 200 naar ½ × 16 × 16 = € 128. CS_B stijgt van € 8 naar € 32. Samen daalt CS van € 208 naar € 160.

**5 · Begrens je conclusie.** PS stijgt van 384 − 96 = € 288 naar 416 − 96 = € 320. TS daalt daardoor van € 496 naar € 480. De aanbieder wint, maar dat is geen bewijs voor meer totale welvaart. Zelfs de gelijke totale afzet garandeert dat niet: de verdeling van de bezoeken verandert.
'''+box('Onthouden','Herken groepen en controleer doorverkoop. Kies per groep Q en lees de bijbehorende P. Tel omzet op, maar tel de gezamenlijke constante kosten slechts eenmaal. Beoordeel daarna de verdeling; winst en welvaart zijn verschillende uitkomsten.','summary'))
 page('Herkennen en narekenen',start()+ex('Twee inkomsten, één bedrijf',
 'Een aanbieder verkoopt in één week 30 bezoeken voor € 12 en 20 bezoeken voor € 8. De variabele kosten zijn € 3 per bezoek; de gezamenlijke constante kosten zijn € 90.',[
 ('Bereken totale omzet, totale kosten en winst.','TO = 30 × 12 + 20 × 8 = € 520. Q = 50. TK = 90 + 3 × 50 = € 240. Winst = 520 − 240 = € 280 per week.'),
 ('Waarom trek je de € 90 niet voor elke groep afzonderlijk af?','Het gaat om één gezamenlijke vaste kostenpost. Die nogmaals aftrekken zou de kosten dubbel tellen en de winst te laag maken.')])+ex('Drie prijskaartjes',
 'A: dezelfde rondleiding is goedkoper met een gecontroleerde studentenpas, zonder kostenverschil. B: een taxi rekent extra voor een langere rit. C: een abonnement met extra opslag kost meer.',[
 ('Welke situatie beschrijft prijsdiscriminatie? Leg uit.','A: dezelfde dienst, maar een andere prijs die niet door andere kosten wordt verklaard. De pas maakt het onderscheid tussen groepen mogelijk.'),
 ('Waarom zijn B en C geen voldoende bewijs?','Bij B verandert de geleverde afstand en daarmee de dienst en de kosten. Bij C wordt meer opslag geleverd. Verschillende producten of kosten kunnen het prijsverschil verklaren.')])+guided()+ex('Een volledig ingevuld paneel',
 'Lees in de figuur de keuzes van Lichtzaal voor twee soorten persoonlijke passen. MK = € 4 per bezoek. Er zijn geen extra kosten om groepen te scheiden.',[
 ('Lees voor A en B de hoeveelheid en de prijs af. Bereken de totale omzet.','A: Q_A = 16 en P_A = € 20. B: Q_B = 8 en P_B = € 12. TO = 16 × 20 + 8 × 12 = € 416 per week.'),
 ('Leg uit waarom het horizontale niveau van € 4 niet de verkoopprijs is.','€ 4 is MK en bij de gekozen hoeveelheden ook MO. De verkoopprijs staat voor elke groep hoger op haar eigen vraaglijn: € 20 respectievelijk € 12.')])+fig('422_guided','Gebruik de gemarkeerde hoeveelheden. Ga daarna naar de vraaglijn voor de prijs.'))
 page('De gezamenlijke kosten bewaken',ex('De rekentabel van de ijsbaan',
 'Dezelfde ijsbaandienst wordt aan twee herkenbare groepen verkocht. De bron geeft de haalbare keuzes in de tabel. Variabele kosten: € 2 per bezoek. Gezamenlijke constante kosten: € 100 per week.',[
 ('Vul eerst de lege cellen TO, TK en winst in voor beide situaties.','Eén prijs: Q = 20 + 10 = 30; TO = 10 × 30 = € 300; TK = 100 + 2 × 30 = € 160; winst = € 140. Twee prijzen: Q = 15 + 20 = 35; TO = 12 × 15 + 7 × 20 = € 320; TK = 100 + 2 × 35 = € 170; winst = € 150.'),
 ('Een leerling rekent bij twee prijzen € 220 winst. Welke kostenpost ontbreekt in zijn berekening 320 − 100?','Hij heeft wel de constante kosten afgetrokken, maar de variabele kosten 2 × 35 = € 70 niet. Omzet minus alleen vaste kosten is niet de winst.')])+'''
| Gegeven | Eén prijs | Twee prijzen |
|---|---:|---:|
| Prijs A / afzet A | € 10 / 20 | € 12 / 15 |
| Prijs B / afzet B | € 10 / 10 | € 7 / 20 |
| TO (€ per week) | … | … |
| TK (€ per week) | … | … |
| Winst (€ per week) | … | … |
'''+heading('Zelfstandige oefening')+ex('Toegang tot een tentoonstelling',
 'Voor groep A geldt P_A = 28 − Q_A; voor B geldt P_B = 20 − Q_B. Prijzen zijn euro per bezoek, hoeveelheden bezoeken per week. MK = € 4 voor beide groepen. TCK = € 40 per week. De capaciteit is 48. De groepen gebruiken dezelfde dienst en kunnen niet doorverkopen.',[
 ('Bereken de winstmaximale afzet en de prijs voor elke groep.','MO_A = 28 − 2Q_A = 4 geeft Q_A = 12 en P_A = € 16. MO_B = 20 − 2Q_B = 4 geeft Q_B = 8 en P_B = € 12. Samen 20, dus haalbaar. MO daalt in beide groepen door MK heen.'),
 ('Bereken de totale winst en geef één reden waarom de twee prijzen uitvoerbaar zijn.','TO = 16 × 12 + 12 × 8 = € 288. TK = 40 + 4 × (12 + 8) = € 120. Winst = € 168 per week. De groepen zijn herkenbaar en doorverkoop is uitgesloten; daardoor kan niet iedereen de lagere prijs kiezen.')]))
 page('Niet alleen het bedrijf beoordelen',ex('Tegengestelde gevolgen',
 'Een ontspanningscentrum vervangt één tarief door groepsprijzen. Deelnemers van A betalen meer; CS_A daalt € 90. B krijgt korting; CS_B stijgt € 30. PS stijgt € 40 per week. Geen andere maatschappelijke posten veranderen.',[
 ('Bekijk eerst alleen de prijsverandering voor A. Wat gebeurt met het surplus van A?','A betaalt meer en verliest € 90 consumentensurplus.'),
 ('Bekijk nu alleen de prijsverandering voor B. Wat gebeurt met het surplus van B?','B krijgt korting en wint € 30 consumentensurplus. Dat staat los van het verlies bij A.'),
 ('Bereken de verandering van het totale CS en van TS.','ΔCS = −90 + 30 = −€ 60. ΔTS = −60 + 40 = −€ 20 per week.'),
 ('Beoordeel: “Er is korting en de aanbieder verdient meer, dus alle partijen winnen.”','Onjuist. De korting geldt alleen voor B. A verliest meer surplus dan B wint; zelfs na de PS-stijging daalt TS met € 20. Een voordeel voor één groep is geen voordeel voor iedereen.')])+'''
### Gebruik prijsgevoeligheid als verklaring, niet als etiket
Een groep met goede alternatieven kan sterker afhaken bij een prijsverhoging. Dat maakt een lager tarief aantrekkelijk voor een aanbieder. Maar “student”, “volwassene” of “zakelijke klant” is op zichzelf geen bewijs voor een bepaalde elasticiteit. Gebruik gegevens over keuzes of reacties uit de bron.

Ook de helling van een getekende lijn is niet genoeg. Bij verschillende prijzen en hoeveelheden kunnen dezelfde absolute veranderingen heel andere procentuele veranderingen zijn. In dit hoofdstuk leiden we hiervoor geen nieuwe elasticiteitsformule af.
'''+box('Een advies in drie zinnen','Beschrijf eerst wat met de winst gebeurt. Noem daarna welke klantgroep voordeel of nadeel ondervindt. Beperk ten slotte je welvaartsconclusie tot de bekende bedragen en aannames.'))
 page('Doel: één prijs en twee prijzen',heading('Doeloefening')+source('Bron A · FilmLab',
 'FilmLab biedt dezelfde toegangsdienst aan A en B. Het heeft marktmacht. De passen zijn persoonlijk; groepen worden gecontroleerd en doorverkoop is onmogelijk. Vraag: P_A = 40 − Q_A en P_B = 24 − Q_B. P is euro per bezoek; Q_A en Q_B zijn bezoeken per week. De hoeveelheden lopen van 0 tot 40 en van 0 tot 24. MK = € 8 voor elk bezoek. TCK = € 80 per week, samen voor beide groepen. Capaciteit: 64 bezoeken.')+source('Bron B · De vergelijking',
 'Bij één gegeven prijs van € 20 koopt A 20 bezoeken en B 4. Het totale CS is dan € 208 per week. Bij de afzonderlijk winstmaximale groepsprijzen is het totale CS € 160. De vraag en kosten veranderen niet; er zijn geen externe effecten.')+ex('FilmLab','Gebruik beide bronnen. Je hoeft de gemeenschappelijke prijs van € 20 niet opnieuw te bepalen.',[
 ('Bereken per groep MO, de winstmaximale hoeveelheid en de groepsprijs.','MO_A = 40 − 2Q_A; 40 − 2Q_A = 8 → Q_A = 16, P_A = € 24. MO_B = 24 − 2Q_B; 24 − 2Q_B = 8 → Q_B = 8, P_B = € 16. Beide marginale lijnen dalen; vóór de keuze is MO groter dan MK en erna kleiner. Samen 24 ≤ 64.'),
 ('Bereken TO en winst bij één prijs en bij de groepsprijzen.','Eén prijs: TO = 20 × (20 + 4) = € 480; TK = 80 + 8 × 24 = € 272; winst = € 208. Groepsprijzen: TO = 24 × 16 + 16 × 8 = € 512; TK = € 272; winst = € 240 per week. De vaste kosten worden één keer afgetrokken.'),
 ('Welke groep betaalt meer en welke minder? Noem één noodzakelijke voorwaarde uit bron A.','A betaalt € 24 in plaats van € 20; B betaalt € 16 in plaats van € 20. Bijvoorbeeld: de persoonlijke gecontroleerde passen voorkomen doorverkoop en houden de groepen gescheiden.'),
 ('Bereken met bron B PS en TS in beide situaties. Is de hogere winst hier ook een hogere totale welvaart?','PS = TO − TVK. Eén prijs: PS = 480 − 192 = € 288; TS = 208 + 288 = € 496. Groepsprijzen: PS = 512 − 192 = € 320; TS = 160 + 320 = € 480. Winst stijgt € 32, maar TS daalt € 16. Dus niet in deze case.'),
 ('Waarom bewijst deze ene case niet dat prijsdiscriminatie altijd welvaart verlaagt?','Dit resultaat hoort bij de gegeven vraag, kosten en afzet. In een andere case kunnen bijvoorbeeld extra kopers worden bereikt die anders niets kopen. Dan kan de verandering van TS anders zijn. Zonder die gegevens is geen algemene richting bewezen.')],points=[3,3,2,3,2],answer_fig='422_answer16')+fig('422_target','De twee groepen zijn gescheiden. Vul de benodigde hoeveelheden en prijzen aan.'))
 page('Een conclusie kan van geval verschillen',heading('Denkertje / Bonusopgave')+ex('Dezelfde naam, een ander gevolg',
 'Een onderzoeker beschrijft twee denkbeeldige prijsdiscriminatiegevallen. Er zijn geen externe effecten. In geval I verandert CS van € 500 naar € 430 en PS van € 300 naar € 350. In geval II verandert CS van € 100 naar € 160 en PS van € 200 naar € 260. De bedragen zijn per maand.',[
 ('Vergelijk de verandering van TS in beide gevallen.','Geval I: TS gaat van 800 naar 780, dus −€ 20. Geval II: TS gaat van 300 naar 420, dus +€ 120 per maand.'),
 ('Geef een mogelijke verklaring voor het verschil, zonder te doen alsof de cijfers die verklaring bewijzen.','In II kan een lagere prijs een nieuwe groep kopers hebben bereikt, waardoor meer voordelige transacties ontstaan. In I kan vooral afzet tussen groepen zijn verschoven. Dit zijn mogelijke mechanismen; de opgegeven totaalcijfers bewijzen de oorzaak niet.'),
 ('Welke extra broninformatie heb je nodig om te beoordelen wie erop vooruitgaat?','Prijzen, afzet en CS per klantgroep, en informatie over wie de ondernemingsopbrengst ontvangt. Een hoger totaal kan nog steeds verlies voor een afzonderlijke groep verbergen.')])+heading('Herhaling / Herhaling en interleaving')+ex('Terug naar één uniforme prijs',
 'Een monopolist gebruikt P = 24 − 0,2Q en MK = € 4. Q is stuks per week; de capaciteit is 100.',[
 ('Bereken Qm en Pm.','MO = 24 − 0,4Q. MO = 4 geeft Qm = 50 stuks per week, binnen de capaciteit. Pm = 24 − 0,2 × 50 = € 14 per stuk.'),
 ('Bereken het consumentensurplus bij monopolie.','CS = ½ × 50 × (24 − 14) = € 250 per week. Het ligt boven P = 14 en onder de vraaglijn, tot Q = 50.')]))
