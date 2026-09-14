from author_common import *
def author():
 section('4.2.5')
 page('Voordeel voor mensen buiten de markt',begin('Wie profiteert zonder te betalen?',
 'Je kunt private voordelen onderscheiden van voordelen voor derden. Je kunt een subsidie-uitkomst en overheidsuitgaven berekenen. Je kunt beoordelen hoe externe baten de welvaartsconclusie veranderen.',
 'Een inwoner laat een groene voortuin aanleggen. Hij geniet van de tuin en betaalt de hovenier. Ook buren genieten van het uitzicht, zonder daarvoor te betalen. Bij zijn eigen keuze telt hij hun voordeel niet volledig mee.')+box('Positief extern effect','Voordeel voor een derde partij dat door productie of consumptie ontstaat en niet in een betaling of vergoeding is verwerkt. Het voordeel voor de koper zelf is geen extern voordeel.','definition')+fig('425_actors','De koper krijgt privévoordeel. Het extra voordeel voor buren staat daar los van en wordt niet door hun betaling vergoed.')+'''
### Vrijwillige keuzes kunnen te weinig activiteit opleveren
De koper vergelijkt zijn eigen voordeel met de prijs. Als anderen ook voordeel hebben, kan een extra activiteit gezamenlijk aantrekkelijk zijn terwijl de koper haar niet uit zichzelf koopt.

Ook hier geldt niet: zoveel mogelijk is het beste. Een extra tuin, cursus of andere activiteit gebruikt schaarse middelen. We vergelijken daarom de **baten voor iedereen samen** met de extra productiekosten.
'''+box('Twee verschillende vormen van voordeel','De hovenier ontvangt een betaling voor zijn werk. Dat is onderdeel van de markttransactie, geen extern effect. Het onbetaalde uitzichtvoordeel voor buren is in deze oefencase wél extern.','warning'))
 page('De vraaglijn is nog niet het hele voordeel','''### Voeg voordeel voor anderen toe
Voor tuinaanleg geldt in een oefenperiode **P = 50 − 0,5Q** en aanbod **P = 10 + 0,5Q**. Q is aangelegde tuinen per maand; P is euro per gestandaardiseerde aanlegdienst. De getallen zijn een vereenvoudigd rekenmodel. Andere omstandigheden blijven gelijk.

De vraaglijn geeft de **private betalingsbereidheid per extra dienst**. De bron waardeert het bijkomende voordeel voor buren op € 10 per dienst. De maatschappelijke baten per extra dienst liggen dan € 10 boven de vraaglijn.
'''+formula('Baten voor iedereen per extra dienst<br>= private betalingsbereidheid + extern voordeel<br>Hier: 60 − 0,5Q')+fig('425_social','De hogere lijn toont maatschappelijke baten. Zij is niet ineens de prijs die de koper zelf wil betalen.')+'''
Zonder subsidie komen vraag en aanbod samen bij Q₀ = 40 en P₀ = € 30. De maatschappelijke vergelijking is **60 − 0,5Q = 10 + 0,5Q**. De efficiënte hoeveelheid is dus **Qe = 50**.

Bij Q = 45 is het private voordeel € 27,50 en zijn de kosten € 32,50. Zonder steun koopt deze extra klant niet. Inclusief € 10 voordeel voor buren zijn de maatschappelijke baten € 37,50: meer dan de kosten.
''')
 page('De subsidie en het externe voordeel','''### Hetzelfde rekenmiddel als in Boek 3
De overheid betaalt de **aanbieder € 10 per uitgevoerde dienst**. Kopers betalen Pc. Aanbieders ontvangen Pp: de kopersbetaling plus de subsidie. De hovenier krijgt dus niet alleen het bedrag dat de klant betaalt.
'''+formula('Pp = Pc + s<br>10 + 0,5Q = (50 − 0,5Q) + 10<br>Q = 50; Pc = € 25; Pp = € 35')+fig('425_subsidy','Vraag en aanbod in kopersprijzen bepalen Q en Pc. Lees bij dezelfde Q op het oorspronkelijke aanbod Pp af.')+'''
De subsidie wordt betaald op **alle 50 uitgevoerde diensten**, niet alleen op de tien extra diensten. De overheid geeft dus 10 × 50 = € 500 per maand uit.

Het externe voordeel is volgens de bron eveneens 10 × 50 = € 500. Maar het zijn verschillende posten. De subsidie is een betaling. Het externe voordeel is het echte voordeel voor de buren. De overheid creëert niet automatisch € 1 voordeel door € 1 te betalen.
'''+box('Het bedrag moet bij de bron passen','Bij constante externe baten van € 10 bereikt een subsidie van € 10 hier de efficiënte hoeveelheid. Dat geldt onder deze vraag-, kosten- en uitvoeringsaannames. Een hoger bedrag is niet automatisch beter.','warning'))
 page('De welvaartsrekening verandert','''### Eerst de marktdeelnemers, dan de ontbrekende posten
CS wordt berekend met **de prijs die kopers betalen**. PS wordt berekend met **wat aanbieders ontvangen inclusief subsidie**. De subsidie zit daardoor al in het producentensurplus. Om de samenleving als geheel te bekijken, trekken we de overheidsuitgave af.
'''+formula('Maatschappelijk surplus met subsidie<br>= CS + PS − subsidie-uitgaven + externe baten')+'''
Voor de tuinaanlegcase ontstaat deze vergelijking:

| Post (€ per maand) | Zonder subsidie | Met € 10 subsidie |
|---|---:|---:|
| CS | ½ × 40 × (50 − 30) = 400 | ½ × 50 × (50 − 25) = 625 |
| PS | ½ × 40 × (30 − 10) = 400 | ½ × 50 × (35 − 10) = 625 |
| Subsidie-uitgaven | 0 | 10 × 50 = 500 |
| Externe baten | 10 × 40 = 400 | 10 × 50 = 500 |
| Maatschappelijk surplus | **1.200** | **1.250** |

Er ontstaat **€ 50 meer maatschappelijk surplus**. Dat is niet de hele € 500 subsidie en ook niet de hele € 100 extra baten voor buren. De tien extra diensten hebben daarnaast private baten en productiekosten.

Het oorspronkelijke verlies is de driehoek tussen maatschappelijke baten en kosten van Q = 40 tot Q = 50: ½ × 10 × 10 = **€ 50**. De subsidie haalt hier die onderproductie weg.
'''+box('De vergelijking met Boek 3','Zonder extern voordeel zou dezelfde subsidie het maatschappelijk surplus verlagen van € 800 naar € 750. Met de gegeven baten voor derden stijgt het van € 1.200 naar € 1.250. De rekenmethode is niet tegengesproken: de welvaartsgrens is veranderd.','summary')+box('Aannames','We veronderstellen concurrentie, geen extra maatschappelijke schade, geen uitvoeringskosten en geen extra kosten van financiering. Een echte beleidsbeoordeling heeft hiervoor meer gegevens nodig.','small'))
 page('Uitgewerkt: een cursus voor een buurt',heading('Uitgewerkt voorbeeld')+'''
Voor **Buurtvaardig** geldt vraag Pc = 50 − Q en aanbod Pp = 10 + Q. Q is cursusplaatsen per maand; prijzen zijn euro per plaats. Er zijn veel aanbieders. De bron waardeert het voordeel voor andere buurtbewoners op € 8 per deelnemer, naast het eigen voordeel van de deelnemer. De overheid betaalt aanbieders € 8 per gebruikte cursusplaats. Andere kosten of baten ontbreken.

**1 · Benoem het externe voordeel.** De deelnemer heeft zelf voordeel van de cursus. Dat staat in de vraag. Alleen het bijkomende, onbetaalde voordeel voor andere buurtbewoners telt als externe baat.

**2 · Bereken de oorspronkelijke markt.** 50 − Q = 10 + Q → Q₀ = 20. Zonder subsidie betalen en ontvangen partijen € 30 per plaats.

**3 · Gebruik de omgekeerde wig.** Pp = Pc + 8 geeft 10 + Q = 50 − Q + 8 → Q₁ = 24. Pc = € 26 en Pp = € 34. Controle: 34 − 26 = € 8.

**4 · Bereken overheid en derden.** De subsidie kost 8 × 24 = **€ 192 per maand**. De externe baten nemen toe van 8 × 20 = € 160 naar **€ 192 per maand**. Beide bedragen zijn berekend met alle deelnemers in die situatie.
'''+fig('425_we','Dezelfde subsidieprocedure als voorheen. Nieuw is het afzonderlijke voordeel voor mensen buiten de markt.'))
 page('Uitgewerkt: marktvoordeel en echte baten','''<div class="continuation">Uitgewerkt voorbeeld · vervolg</div>

**5 · Bouw de vergelijking op.**

| Post (€ per maand) | Zonder subsidie | Met subsidie |
|---|---:|---:|
| CS | ½ × 20 × (50 − 30) = 200 | ½ × 24 × (50 − 26) = 288 |
| PS | ½ × 20 × (30 − 10) = 200 | ½ × 24 × (34 − 10) = 288 |
| Subsidie-uitgaven | 0 | 192 |
| Externe baten | 160 | 192 |
| Maatschappelijk surplus | 200 + 200 + 160 = **560** | 288 + 288 − 192 + 192 = **576** |

**6 · Trek een begrensde conclusie.** Het maatschappelijk surplus stijgt met € 16. De extra vier plaatsen leveren € 32 extra externe baten op. Na aftrek van de extra private productiekosten en toevoeging van de private voordelen blijft € 16 netto verbetering over.

De maatschappelijke batenlijn is 58 − Q. Vergelijk met MK = 10 + Q: 58 − Q = 10 + Q → **Qe = 24**. Het oorspronkelijke verlies is ½ × (24 − 20) × 8 = **€ 16 per maand**.
'''+fig('425_we_loss','De driehoek markeert gemiste gezamenlijke voordelen van cursusplaatsen die zonder subsidie niet worden gebruikt.')+box('Onthouden','Derdenvoordeel apart van kopersvoordeel → oorspronkelijke uitkomst → subsidiewig → alle gebruikte plaatsen → CS + PS − uitgaven + externe baten → conclusie onder de gegeven aannames. Een andere subsidiehoogte vereist opnieuw rekenen.','summary'))
 page('Betalingen en baten herkennen',start()+ex('De subsidie uit Boek 3',
 'Vraag: Pc = 20 − Q. Aanbod: Pp = 4 + Q. Producenten ontvangen € 4 subsidie per verkochte eenheid. Q is stuks per dag; prijzen zijn euro per stuk.',[
 ('Bereken Q, Pc en Pp na de subsidie.','Pp = Pc + 4: 4 + Q = 20 − Q + 4 → Q = 10. Pc = € 10 en Pp = € 14 per stuk. Het verschil is de subsidie van € 4.'),
 ('Bereken de overheidsuitgaven.','Uitgaven = 4 × 10 = € 40 per dag. De subsidie geldt voor elke verkochte eenheid, niet alleen de extra eenheden.')])+ex('Wie ontvangt het voordeel?',
 'Een deelnemer betaalt voor een cursus. Zelf leert zij er iets van. De aanbieder ontvangt lesgeld. Volgens de bron helpen de aangeleerde vaardigheden daarnaast andere buurtbewoners, zonder dat zij betalen.',[
 ('Welk voordeel is extern en welk voordeel hoort bij de koper?','Het onbetaalde voordeel voor andere buurtbewoners is extern. Wat de deelnemer zelf leert, vormt haar private voordeel en kan in haar betalingsbereidheid zitten.'),
 ('Is het lesgeld van de aanbieder ook een externe baat?','Nee. Lesgeld is een betaling binnen de markttransactie. Het apart als externe baat toevoegen zou dezelfde marktbetaling dubbel waarderen.')])+guided()+ex('Twee batenlijnen lezen',
 'Gebruik de figuur. Het externe voordeel is € 10 per aanlegdienst.',[
 ('Lees bij Q = 20 de private en maatschappelijke baten per extra dienst af.','Private baten = 50 − 0,5 × 20 = € 40. Maatschappelijke baten = 60 − 0,5 × 20 = € 50 per extra dienst.'),
 ('Welke van die bedragen is de betalingsbereidheid van de koper zelf?','€ 40. De extra € 10 is voordeel voor anderen. De hogere batenlijn is niet automatisch een feitelijke vraaglijn waar kopers € 50 betalen.'),
 ('Markeer Q₀ = 40 en Qe = 50. Arceer de oorspronkelijke gemiste baten tussen die hoeveelheden: gebruik de maatschappelijke-batenlijn en MK.','Het verlies is de driehoek tussen Q = 40 en 50. Bij Q = 40 zijn maatschappelijke baten € 40 en MK € 30. Basis = 10 diensten, hoogte = € 10. Verlies = € 50 per maand.')],answer_fig='425_loss')+fig('425_guided','De verticale afstand is extern voordeel per eenheid; de hele hogere lijn is geen extra betaling.'))
 page('De posten stap voor stap combineren',ex('Een lagere subsidie',
 'Een concurrerende cursusmarkt krijgt € 4 subsidie per deelnemer. Er doen 22 deelnemers per maand mee. CS en PS zijn beide € 242. De bron waardeert het externe voordeel op € 8 per deelnemer. Zonder subsidie was het maatschappelijk surplus € 560.',[
 ('Bereken eerst subsidie-uitgaven en externe baten; vul daarna het maatschappelijk surplus in.','Uitgaven = 4 × 22 = € 88. Externe baten = 8 × 22 = € 176. Maatschappelijk surplus = 242 + 242 − 88 + 176 = € 572 per maand.'),
 ('Vergelijk met de beginsituatie. Waarom mogen uitgaven en externe baten hier niet tegen elkaar worden weggestreept?','Verbetering = 572 − 560 = € 12. Uitgaven zijn € 88 en externe baten € 176: ze zijn verschillende posten met verschillende bedragen. De ene volgt uit de subsidie, de andere uit het opgegeven echte derdenvoordeel.')])+'''
| Post (€ per maand) | Nieuwe situatie |
|---|---:|
| CS + PS | 484 |
| Subsidie-uitgaven | … |
| Externe baten | … |
| Maatschappelijk surplus | … |
'''+heading('Zelfstandige oefening')+ex('Twee voordelen veranderen tegelijk',
 'Bij dezelfde hoeveelheid activiteit neemt het private voordeel van één extra activiteit met € 2 toe. Tegelijk daalt het extra voordeel voor derden met € 5. De productiekosten veranderen niet.',[
 ('Beschrijf de invloed van alleen de stijging van het private voordeel.','De maatschappelijke baten per extra activiteit stijgen daardoor met € 2, zolang het externe voordeel gelijk blijft.'),
 ('Beschrijf de invloed van alleen de daling van het externe voordeel.','De maatschappelijke baten per extra activiteit dalen daardoor met € 5, zolang het private voordeel gelijk blijft.'),
 ('Bereken het gezamenlijke effect op de maatschappelijke baten per extra activiteit.','Samen veranderen de maatschappelijke baten met +2 − 5 = −€ 3 per extra activiteit.'),
 ('Beoordeel: “Als kopers meer voordeel krijgen, stijgen de maatschappelijke baten altijd.”','Onjuist: veranderingen voor derden kunnen groter zijn en de andere kant op werken. Hier dalen de maatschappelijke baten ondanks het hogere private voordeel.')]))
 page('Zelfstandig: van subsidie naar gemiste baten',ex('Een cursus met hulp aan anderen',
 'Vraag Pc = 36 − Q; aanbod Pp = 4 + Q. Q is deelnemers per maand, prijzen zijn euro per deelnemer. Het externe voordeel is € 8 per deelnemer. Aanbieders ontvangen een subsidie van € 8; andere maatschappelijke posten ontbreken.',[
 ('Bereken de oorspronkelijke en de gesubsidieerde uitkomst.','Zonder subsidie: 36 − Q = 4 + Q → Q₀ = 16, P₀ = € 20. Met subsidie: 4 + Q = 36 − Q + 8 → Q₁ = 20, Pc = € 16 en Pp = € 24.'),
 ('Bereken het maatschappelijk surplus vóór en na.','Voor: CS = PS = ½ × 16 × 16 = € 128; externe baten = 8 × 16 = € 128; maatschappelijk surplus = € 384. Na: CS = PS = ½ × 20 × 20 = € 200; uitgaven = € 160; externe baten = € 160; maatschappelijk surplus = € 400. Verbetering: € 16 per maand.'),
 ('Bepaal de efficiënte hoeveelheid. Arceer de oorspronkelijk gemiste baten in de gegeven grafiek en bereken het verlies.','Maatschappelijke baten = 44 − Q. 44 − Q = 4 + Q → Qe = 20. De driehoek tussen maatschappelijke baten en MK loopt van Q = 16 tot 20. Basis = 4 deelnemers, hoogte = € 8. Verlies = ½ × 4 × 8 = € 16 per maand.')],answer_fig='425_answer42')+fig('425_independent','De private vraag, maatschappelijke baten en aanbodlijn zijn gegeven; de uitkomsten en het verliesgebied nog niet.'))
 page('Doel: subsidie en maatschappelijk voordeel',heading('Doeloefening')+source('Bron · Buurtcursus',
 'Een cursus geeft deelnemers eigen voordeel én helpt andere buurtbewoners. De bron waardeert uitsluitend dat bijkomende voordeel op € 10 per deelnemer. Vraag: Pc = 60 − 0,5Q; aanbod: Pp = 20 + 0,5Q. Q is deelnemers per maand van 0 tot 100; prijzen zijn euro per deelnemer. Er zijn veel aanbieders. De overheid betaalt aanbieders € 10 subsidie voor elke gebruikte cursusplaats. Andere omstandigheden blijven gelijk. Er zijn geen andere externe effecten, vaste kosten, financierings- of uitvoeringskosten.')+ex('Eigen voordeel en voordeel voor anderen','Gebruik de bron en de basisgrafiek.',[
 ('Benoem het private en externe voordeel. Bereken de oorspronkelijke hoeveelheid en prijs.','Het eigen voordeel van deelnemers staat in de vraag; het bijkomende onbetaalde voordeel voor andere buurtbewoners is extern. 60 − 0,5Q = 20 + 0,5Q → Q₀ = 40 en P₀ = € 40 per deelnemer.'),
 ('Bereken na de subsidie Q, Pc, Pp en de overheidsuitgaven.','20 + 0,5Q = 60 − 0,5Q + 10 → Q₁ = 50. Pc = 60 − 25 = € 35; Pp = 20 + 25 = € 45. Uitgaven = 10 × 50 = € 500 per maand.'),
 ('Bereken CS, PS en het maatschappelijk surplus vóór en na.','Voor: CS = PS = ½ × 40 × 20 = € 400; externe baten = 10 × 40 = € 400; maatschappelijk surplus = € 1.200. Na: CS = PS = ½ × 50 × 25 = € 625; uitgaven = € 500; externe baten = € 500; maatschappelijk surplus = 625 + 625 − 500 + 500 = € 1.250 per maand.'),
 ('Bepaal de efficiënte hoeveelheid en arceer het oorspronkelijke welvaartsverlies.','Maatschappelijke baten per extra deelnemer = 70 − 0,5Q. Vergelijk met MK = 20 + 0,5Q: Qe = 50. De driehoek tussen maatschappelijke baten en MK van Q = 40 tot Q = 50 heeft basis 10 deelnemers en hoogte € 10; verlies = ½ × 10 × 10 = € 50 per maand.'),
 ('Leg uit waarom dit anders uitpakt dan dezelfde subsidie zonder externe baten.','Zonder externe baten zou het maatschappelijk surplus van 800 naar 625 + 625 − 500 = € 750 dalen. Met het gegeven voordeel voor derden stijgt het juist van 1.200 naar 1.250. Niet de subsidie alleen, maar de volledige maatschappelijke rekening bepaalt de conclusie.')],points=[2,3,4,2,2],answer_fig='425_answer43')+fig('425_target','De private vraag, maatschappelijke baten en oorspronkelijke aanbodlijn zijn gegeven. De subsidie is geen nieuwe externe baat.'))
 page('Meer steun is niet vanzelf beter',heading('Denkertje / Bonusopgave')+ex('Een te ruime regeling?',
 'Een model voor tuinaanleg heeft € 10 extern voordeel per dienst. Er zijn geen andere maatschappelijke posten. De bron geeft drie volledig berekende scenario’s. Alle bedragen zijn euro per maand.',[
 ('Bereken het maatschappelijk surplus in de drie rijen.','Geen subsidie: 800 − 0 + 400 = € 1.200. Subsidie € 10: 1.250 − 500 + 500 = € 1.250. Subsidie € 30: 2.450 − 2.100 + 700 = € 1.050.'),
 ('Waarom is “meer externe baten” niet voldoende om de grootste subsidie te kiezen?','Meer activiteit geeft meer externe baten, maar gebruikt ook extra middelen. De subsidie-uitgaven zitten al bij de marktdeelnemers en moeten worden afgetrokken. Bij € 30 wordt zo veel gestimuleerd dat het netto-surplus lager is, ook al zijn de externe baten hoger.'),
 ('Wat kun je wél en niet concluderen uit deze drie scenario’s?','Van deze drie is € 10 het beste volgens de genoemde surplusmaatstaf. Dat is geen universeel subsidiebedrag en bewijst niet dat alle echte kosten, onzekerheden of verdelingswensen zijn meegenomen.')])+'''
| Subsidie per dienst | Q (per maand) | CS + PS | Subsidie-uitgaven | Externe baten |
|---|---:|---:|---:|---:|
| € 0 | 40 | 800 | 0 | 400 |
| € 10 | 50 | 1.250 | 500 | 500 |
| € 30 | 70 | 2.450 | 2.100 | 700 |
'''+heading('Herhaling / Herhaling en interleaving')+ex('Belasting is niet de schade',
 'Bij 20 verkochte eenheden per dag bedraagt een heffing € 6 per eenheid. De bron schat de resterende externe schade op € 10 per eenheid.',[
 ('Bereken de belastingopbrengst en de totale externe schade.','Opbrengst = 6 × 20 = € 120 per dag. Schade = 10 × 20 = € 200 per dag.'),
 ('Hoe neem je deze twee posten mee naast CS en PS?','Maatschappelijk surplus = CS + PS + 120 − 200. De ontvangst is een overdracht aan de overheid; de schade is een echt nadeel voor derden. Ze zijn niet hetzelfde bedrag.')]))
