from author_common import *
section('4.3.1')
page('Wie vraagt arbeid?',begin('Wie koopt jouw werktijd?',
'Je kunt werkgevers en werknemers op de arbeidsmarkt onderscheiden. Je kunt arbeidsproductiviteit, benodigde arbeidsuren en loonkosten per product berekenen. Je kunt een loonverandering onderscheiden van een verandering in de arbeidsvraag.',
'Een fietsenmaker zoekt een medewerker. Jij zoekt een bijbaan. Wie is hier de vrager? In het dagelijks taalgebruik biedt het bedrijf een baan aan. Economisch koopt het bedrijf jouw arbeid.')+
box('Definitie · arbeidsvraag','De hoeveelheid arbeid die werkgevers bij een bepaald loon willen inzetten. Werkgevers vragen arbeid omdat zij daarmee goederen of diensten kunnen produceren.','definition')+
fig('actor_bridge','Op de goederenmarkt kopen huishoudens producten. Op de arbeidsmarkt leveren zij arbeid en ontvangen zij loon.')+
'''### Dezelfde marktlogica, andere rollen
Een werknemer **biedt arbeid aan**. Een werkgever **vraagt arbeid**. Een vacature is een nog niet vervulde arbeidsplaats: de werkgever zoekt iemand.

De prijs van arbeid heet het **loon**. We gebruiken de letter **w** voor het loon per uur. De hoeveelheid arbeid noemen we **L**. Daarbij vermelden we steeds of het om uren of personen gaat.

Een stijging van de vraag naar fietsen kan dus leiden tot meer vraag naar monteurs. De vraag naar arbeid hangt mede af van wat bedrijven kunnen verkopen.
''')
page('Arbeid meten', '''### Zes mensen zijn niet hetzelfde als zes voltijdbanen
Een bedrijf heeft zes medewerkers. Ieder werkt 20 uur per week. Samen leveren zij 6 × 20 = **120 arbeidsuren per week**. Bij een voltijdweek van 40 uur is dat 120 / 40 = **3 fte**.

'''+fig('units','Fte is een rekeneenheid voor de omvang van werk, niet het aantal verschillende mensen.')+
box('Definitie · fte','Een fulltime-equivalent is de arbeidsduur van één voltijdbaan. Welke arbeidsduur daarbij hoort, staat in de opgave. Twee halve banen tellen samen als één fte.','definition')+
'''### Productiviteit: hoeveel productie levert de arbeid op?
Een werkplaats maakt 2.400 onderdelen in 600 arbeidsuren. Gemiddeld zijn dat **4 onderdelen per arbeidsuur**. Dit noemen we arbeidsproductiviteit.

'''+formula('arbeidsproductiviteit = productie / arbeidsinzet<br>benodigde arbeidsinzet = productie / arbeidsproductiviteit')+
'''In dit hoofdstuk gebruiken we meestal arbeidsuren. Deel dus producten per week door arbeidsuren per week. De uitkomst is producten **per arbeidsuur**.

Productiviteit per medewerker mag ook, maar alleen met een duidelijke periode en arbeidsduur. Twee bedrijven vergelijken op productie per persoon kan misleiden als hun medewerkers niet evenveel uren werken.
'''+box('Eerst de eenheid','Schrijf vóór het rekenen op wat je moet vinden: personen, arbeidsuren, fte of producten per arbeidsuur. Wissel tijdens een berekening niet ongemerkt van eenheid.','warning'))
page('Kosten per product', '''### Een duurder arbeidsuur kan toch een goedkoper product opleveren
De werkplaats maakt 4 onderdelen per arbeidsuur. Een arbeidsuur kost de werkgever € 24. De loonkosten per onderdeel zijn dan € 24 / 4 = **€ 6**.

'''+formula('loonkosten per product = totale loonkosten / productie<br>loonkosten per product = uurkosten / productie per uur')+
'''Uurkosten zijn hier de **volledige loonkosten van de werkgever per arbeidsuur**. Ze kunnen meer omvatten dan het brutoloon. Gebruik de uurkosten die de bron geeft. Voeg niet zelf onbekende kosten toe.

Stijgt de productiviteit naar 5 onderdelen per uur, bij dezelfde uurkosten? Dan dalen de loonkosten naar € 24 / 5 = **€ 4,80 per onderdeel**. De werknemer hoeft daarvoor niet minder loon te ontvangen.

### Meer productie per uur: hoeveel uren zijn nog nodig?
'''+fig('productivity_paths','Vergelijk zowel de productie als de productiviteit. Eén van beide veranderingen bekijken is niet genoeg.')+
'''Bij dezelfde productie zijn minder uren nodig. Bij voldoende extra opdrachten kan de totale arbeidsinzet juist toenemen. Het rekenschema houdt de gevraagde productie per situatie vast; het voorspelt niet automatisch alle veranderingen in een economie.
'''+box('Arbeidskosten zijn niet alle kosten','Een lagere loonkost per product bewijst nog niet dat de totale kostprijs daalt. Machines, energie en grondstoffen kunnen ook veranderen.','warning'))
page('Bewegen of verschuiven?', '''### Het loon zelf verandert
Een arbeidsvraaglijn toont hoeveel arbeid werkgevers bij verschillende lonen willen inzetten, **terwijl andere omstandigheden gelijk blijven**. In ons eenvoudige model daalt de gevraagde hoeveelheid arbeid als het uurloon stijgt. Arbeid wordt duurder ten opzichte van wat zij oplevert.

'''+fig('demand_move','Van A naar B: het loon stijgt van € 16 naar € 20. Langs dezelfde vraaglijn daalt de hoeveelheid van 80 naar 60 arbeidsuren per week.')+
'''### Een andere omstandigheid verandert
Meer exportorders kunnen de arbeidsvraag vergroten: bij hetzelfde loon willen werkgevers dan meer mensen of uren inzetten. De vraaglijn verschuift naar rechts. Minder vraag naar het eindproduct kan de lijn naar links verschuiven.

Ook techniek verandert de behoefte aan arbeid. Een machine kan bepaalde taken vervangen, maar nieuwe taken en extra productie mogelijk maken. Zonder verdere gegevens ligt de totale verandering niet vast.
'''+box('Zo houd je de twee uit elkaar','Alleen het loon verandert → <b>beweging langs</b> een arbeidsvraaglijn.<br>Een andere vraagbepalende factor verandert → <b>verschuiving van</b> de arbeidsvraaglijn.','summary'))
page('Uitgewerkt voorbeeld',heading('Uitgewerkt voorbeeld')+
source('Verpakkingen voor export','Een bedrijf maakt eerst 1.200 dozen per week in 300 arbeidsuren. De volledige uurkosten zijn € 24. Een nieuw werkproces levert 5 dozen per uur op. Het bedrijf ontvangt orders voor 1.800 dozen per week; de uurkosten worden € 25. Alle genoemde veranderingen horen bij dit plan.')+
'''### 1 · Bereken de oorspronkelijke productiviteit
Arbeidsproductiviteit = productie / arbeidsuren = 1.200 / 300 = **4 dozen per arbeidsuur**.

### 2 · Bereken de nieuwe benodigde arbeidsinzet
Arbeidsuren = productie / arbeidsproductiviteit = 1.800 / 5 = **360 uur per week**. Dat is 60 uur meer dan eerst, ofwel 60 / 300 × 100% = **20% meer**.

### 3 · Bereken de loonkosten per doos
Oud: € 24 / 4 = **€ 6 per doos**. Nieuw: € 25 / 5 = **€ 5 per doos**.

De uurkosten stijgen, maar de productie per uur stijgt sterker. Daardoor dalen de loonkosten per doos. Tegelijk stijgt de totale arbeidsinzet, omdat het bedrijf veel meer dozen gaat maken.

### 4 · Leg de arbeidsvraag uit
Kijk nu naar twee **afzonderlijke** veranderingen. Alleen een hoger loon, bij verder gelijke omstandigheden, geeft een beweging langs de vraaglijn naar minder arbeid. Alleen meer orders, bij gelijk loon en dezelfde techniek, verschuift de vraaglijn naar rechts.

In het totale rekenplan zijn zowel productie als productiviteit veranderd. Uit alleen de productiviteitsstijging mag je dus niet concluderen dat het bedrijf minder uren nodig heeft.
'''+box('Samenvatting §4.3.1','Werkgevers vragen arbeid; huishoudens bieden arbeid aan. Bereken productiviteit en arbeidsinzet met dezelfde eenheden. Deel uurkosten door productie per uur voor loonkosten per product. Benoem bij een vraagverandering de oorzaak. In §4.3.2 voegen we arbeidsaanbod en evenwicht toe.','summary'))
page('Start en herkennen',start()+
ex('Een bekende verhouding','Een drukker produceert 900 posters met € 2.700 totale kosten.',[
('Bereken de gemiddelde kosten per poster.',ans('Gemiddelde kosten = totale kosten / productie = € 2.700 / 900 = <b>€ 3 per poster</b>.','Je verdeelt de totale kosten over de geproduceerde posters.')),
('De productie stijgt van 900 naar 1.080 posters. Bereken de procentuele stijging.',ans('(1.080 − 900) / 900 × 100% = <b>20%</b>.','De oude productie is de basis van de vergelijking.'))])+ 
ex('Wie koopt wat?','Een restaurant neemt een kok aan.',[
('Wie is de vrager en wie de aanbieder op deze arbeidsmarkt? Licht beide rollen toe.',ans('Het restaurant vraagt arbeid; de kok biedt arbeid aan. Het restaurant betaalt loon voor de arbeid van de kok.','Een baan aanbieden is niet hetzelfde als arbeid aanbieden.'))])+guided()+
fig('demand_shift','Lees eerst de volledig gemarkeerde verandering: bij € 16 per uur gaat de gevraagde hoeveelheid van A naar C.')+
ex('Een order erbij','Een assemblagebedrijf ontvangt meer orders. De figuur laat alleen die verandering zien; loon en techniek blijven gelijk.',[
('Lees af hoeveel extra arbeidsuren per week het bedrijf bij hetzelfde loon wil inzetten.',ans('100 − 80 = <b>20 extra arbeidsuren per week</b>.','Beide hoeveelheden horen bij hetzelfde uurloon van € 16.')),
('Waarom is dit geen beweging langs de oude vraaglijn?',ans('De orders veranderen, niet het loon. Bij hetzelfde loon vraagt het bedrijf meer arbeid: de vraaglijn verschuift naar rechts.','Een verandering van een andere vraagbepalende factor verandert de hele relatie.'))]))
page('Rekenen met minder steun',guided().replace('## Begeleide inoefening','<div class="continuation">Begeleide inoefening · vervolg</div>')+
ex('Een tabel opbouwen','Een kaarsenmaker vergelijkt twee weken. Neem de tabel over en <b>vul eerst de drie lege cellen in</b>.'+table(['Grootheid','Week 1','Week 2'],[['Productie (kaarsen)','1.600','2.400'],['Arbeidsuren','400','…'],['Productiviteit (kaarsen/uur)','…','6'],['Uurkosten','€ 20','€ 21'],['Loonkosten per kaars','€ 5','…']]),[
('Vul de ontbrekende productiviteit, arbeidsuren en loonkosten per kaars in. Gebruik achtereenvolgens productie / uren, productie / productiviteit en uurkosten / productiviteit.',ans('Week 1: 1.600 / 400 = <b>4 kaarsen per uur</b>. Week 2: 2.400 / 6 = <b>400 arbeidsuren</b>. Week 2: € 21 / 6 = <b>€ 3,50 per kaars</b>.','De productie en productiviteit groeien even sterk. De benodigde uren blijven gelijk.')),
('Leg zonder extra berekening uit waarom een stijgend uurbedrag hier samengaat met lagere loonkosten per kaars.',ans('Per arbeidsuur worden meer kaarsen gemaakt. De productiviteit stijgt sterker dan de uurkosten, zodat elke kaars een kleiner deel van die uurkosten draagt.','Een uurbedrag en een bedrag per product hebben verschillende noemers.'))])+heading('Zelfstandige oefening')+
ex('Bestellingen voor een meubelmaker','Een meubelmaker levert 1.200 plankdelen in 200 arbeidsuren. De uurkosten bedragen € 30. Volgende week zijn 1.500 delen nodig. De productiviteit stijgt naar 7,5 delen per uur; de uurkosten blijven € 30.',[
('Bereken de oorspronkelijke arbeidsproductiviteit.',ans('1.200 / 200 = <b>6 delen per arbeidsuur</b>.','Je deelt productie door de bijbehorende arbeidsuren.')),
('Bereken de benodigde arbeidsuren volgende week en de loonkosten per deel in beide weken.',ans('Uren nieuw = 1.500 / 7,5 = <b>200 uur</b>. Oud: € 30 / 6 = <b>€ 5 per deel</b>. Nieuw: € 30 / 7,5 = <b>€ 4 per deel</b>.','Meer productie en een hogere productiviteit kunnen samengaan met dezelfde arbeidsinzet.'))]))
page('Twee veranderingen tegelijk',heading('Zelfstandige oefening').replace('## Zelfstandige oefening','<div class="continuation">Zelfstandige oefening · vervolg</div>')+
ex('Loon én orders veranderen','Een fietsenonderdelenbedrijf krijgt twee veranderingen: het uurloon stijgt van € 16 naar € 20 en de buitenlandse orders nemen toe. In de basisgrafiek staat alleen de oorspronkelijke arbeidsvraag. De productiviteit blijft gelijk.',[
('Bekijk eerst alleen de loonstijging. Lees de oude en nieuwe hoeveelheid af en benoem de verandering.',ans('Bij € 16: <b>80 uur</b>. Bij € 20: <b>60 uur</b>. Dit is een beweging langs de oorspronkelijke arbeidsvraaglijn naar minder arbeid.','Alle andere factoren worden voor dit deel gelijk gehouden.')),
('Bekijk nu alleen de extra orders bij een gelijk loon. Welke kant verschuift de arbeidsvraaglijn?',ans('Naar rechts: bij hetzelfde loon wil het bedrijf meer arbeid inzetten.','Meer opdrachten vragen bij dezelfde techniek om meer arbeidsinzet.')),
('Kun je zonder de omvang van de verschuiving vaststellen of er uiteindelijk meer of minder arbeidsuren worden gevraagd dan eerst? Leg uit.',ans('Nee. De loonstijging vermindert de gevraagde hoeveelheid, terwijl extra orders de arbeidsvraag vergroten. De grootte van de tweede verandering ontbreekt.','Tegengestelde effecten geven zonder omvang geen vast nettoresultaat.')),
('Een leerling zegt: “Beide veranderingen verschuiven de vraaglijn.” Verbeter die uitspraak.',ans('Alleen de extra orders verschuiven de vraaglijn. De loonstijging geeft een beweging langs de toepasselijke vraaglijn.','De factor die op de verticale as staat, verandert de positie op de lijn; een andere vraagfactor verandert de lijn.'))],answer_fig='demand_move')+
fig('demand_base','Gebruik de bestaande schaal voor vraag a. Voor de orderverandering hoef je geen nieuwe numerieke lijn te verzinnen.')+
box('Een economisch antwoord','Noem de oorzaak, de verandering van de lijn of het punt, en de betekenis voor arbeid. Alleen “meer” of “minder” is niet genoeg.','summary'))
page('Doeloefening',heading('Doeloefening')+
ex('FrameWerk groeit','FrameWerk produceert fietsframes voor export. De tabel beschrijft het volledige productieplan.'+table(['Grootheid','Oude week','Nieuwe week'],[['Productie (frames)','2.400','3.300'],['Arbeidsuren','600','te berekenen'],['Productiviteit (frames/uur)','te berekenen','5,5'],['Volledige uurkosten','€ 24','€ 26,40']])+ 'Los van dit rekenplan beoordeel je bij d twee afzonderlijke veranderingen. Er worden geen huidige wettelijke loonbedragen gebruikt.',[
('Bereken de oorspronkelijke arbeidsproductiviteit en de benodigde arbeidsuren in de nieuwe week.',ans('Oude productiviteit = 2.400 / 600 = <b>4 frames per uur</b>. Nieuwe uren = 3.300 / 5,5 = <b>600 uur per week</b>.','Productie en productiviteit stijgen beide met 37,5%; de benodigde uren blijven gelijk.')),
('Bereken de loonkosten per frame in beide weken.',ans('Oud: € 24 / 4 = <b>€ 6 per frame</b>. Nieuw: € 26,40 / 5,5 = <b>€ 4,80 per frame</b>.','Het hogere uurbedrag wordt over meer frames verdeeld.')),
('De directeur zegt: “Een hogere productiviteit betekent altijd minder arbeidsuren.” Beoordeel dit met de tabel.',ans('Onjuist. In dit plan stijgt de productiviteit, maar blijven <b>600 arbeidsuren</b> nodig doordat de productie eveneens stijgt.','Arbeidsinzet hangt af van productie én productiviteit.')),
('Benoem en verklaar de verandering van de arbeidsvraag bij: (1) alleen een hoger uurloon en (2) alleen extra exportorders bij gelijk loon en gelijke techniek.',ans('(1) Een beweging langs de vraaglijn naar minder arbeid. (2) Een verschuiving naar rechts: bij hetzelfde loon is meer arbeid nodig voor de extra orders.','De twee verklaringen houden verschillende factoren constant.'))],points=[3,2,2,3])+
box('Wat lever je in?','Berekeningen met eenheden en twee afzonderlijke verklaringen voor de arbeidsvraag.','summary'))
page('Denkertje en herhaling',heading('Denkertje / Bonusopgave')+
ex('Wie lijkt het productiefst?','In dezelfde week maakt atelier A 600 tassen met 10 medewerkers. Atelier B maakt 480 tassen met 8 medewerkers. Een verslaggever noemt de ateliers even productief.',[
('Beoordeel het oordeel. Beschrijf welke informatie ontbreekt en bedenk een situatie waarin de vergelijking per medewerker gelijk is, maar per uur verschilt.',
'Een sterk antwoord: beide ateliers maken 60 tassen per medewerker in de genoemde periode, maar de gewerkte uren ontbreken. Bij A kunnen de tien medewerkers ieder 30 uur werken: 600 / 300 = 2 tassen per uur. Bij B kunnen de acht medewerkers ieder 20 uur werken: 480 / 160 = 3 tassen per uur. De vergelijking per uur verschilt dan.<br><b>Beoordelingscriteria:</b> onderscheidt personen en uren; gebruikt dezelfde periode; geeft een consistent tegenvoorbeeld.')])+heading('Herhaling / Herhaling en interleaving')+
ex('Kosten uit Boek 2','Een reparatiewerkplaats heeft TK = 600 + 12q, met TK in euro per week en q in reparaties per week. Er zijn deze week 100 reparaties.',[
('Bereken TK en GTK.',ans('TK = 600 + 12 × 100 = <b>€ 1.800 per week</b>. GTK = 1.800 / 100 = <b>€ 18 per reparatie</b>.','Totale kosten zijn een weekbedrag; gemiddelde kosten zijn een bedrag per reparatie. Herhaal bij moeite §2.1.1.')),
('Leg uit waarom GTK daalt als het aantal reparaties stijgt, zolang dezelfde formule geldt.',ans('De constante kosten van € 600 worden over meer reparaties verdeeld. De variabele kosten blijven € 12 per reparatie.','Een dalend gemiddelde betekent niet dat de totale kosten dalen.'))])+
box('Terugblik','Je kunt nu productie vertalen naar arbeidsinzet. De volgende stap is de andere kant van de markt: hoeveel arbeid willen huishoudens aanbieden?','summary'))
