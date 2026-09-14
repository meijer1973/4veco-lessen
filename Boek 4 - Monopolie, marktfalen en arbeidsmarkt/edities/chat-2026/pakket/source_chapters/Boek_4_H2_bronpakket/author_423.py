from author_common import *
def author():
 section('4.2.3')
 page('Vier marktvormen herkennen',begin('Veel merken. Ook veel concurrentie?',
 'Je kunt vier marktvormen onderscheiden met brongegevens. Je kunt de rol van productverschillen en toetreding uitleggen. Je kunt de bekende winstprocedure toepassen op een gegeven ondernemingsmodel.',
 'In een winkel staan twintig merken frisdrank. Maar misschien zijn die merken van slechts enkele ondernemingen. Om concurrentie te beoordelen, moet je weten wie aanbiedt, wat kopers als alternatief zien en wie kan toetreden.')+'''
### Gebruik kenmerken, niet alleen een bedrijfsnaam
Een **homogeen product** is in de ogen van kopers gelijkwaardig aan dat van andere aanbieders. Bij **heterogene producten** zien kopers verschillen, bijvoorbeeld in kwaliteit, smaak, plaats of service. Het aantal merken hoeft niet gelijk te zijn aan het aantal zelfstandige aanbieders.

| Marktvorm | Aanbieders | Product | Toetreding in het model |
|---|---|---|---|
| Volkomen concurrentie | Veel kleine | Homogeen | Vrij |
| Monopolistische concurrentie | Veel | Heterogeen | Relatief eenvoudig |
| Oligopolie | Enkele grote | Homogeen of heterogeen | Vaak belemmerd |
| Monopolie | Eén | Geen goed alternatief binnen de afgebakende markt | Sterk belemmerd |

Bij **monopolistische concurrentie** heeft elke onderneming enige ruimte voor een eigen prijs, maar er zijn veel alternatieven. Denk aan de verschillende lunchzaken in een beschreven winkelgebied. Dat is niet hetzelfde als een monopolie.

Bij **oligopolie** hangt een prijskeuze mede af van wat de andere grote ondernemingen doen. Er bestaat daarom niet één vraaglijn die voor elke oligopolist in elke situatie geldt.
'''+box('Marktvorm en uitkomst zijn verschillende vragen','Een marktvorm herkennen bewijst nog niet hoeveel winst een onderneming maakt. Daarvoor zijn prijs, vraag en kosten nodig. Een hoge prijs alleen bewijst evenmin een monopolie.','warning'))
 page('Een bekende berekening in een nieuwe markt',heading('Uitgewerkt voorbeeld')+'''
In het centrum zijn veel onafhankelijke ijszaken. Ze verschillen in smaak en locatie. Nieuwe zaken kunnen relatief eenvoudig beginnen. Voor **IJsatelier** geldt op korte termijn P = 18 − 0,10q. MK = € 6 per portie en TCK = € 120 per dag. q is porties per dag, met een capaciteit van 100. Andere zaken veranderen in deze berekening hun gedrag niet.

**1 · Classificeer met bronbewijs.** Veel aanbieders, productverschillen en relatief eenvoudige toetreding passen bij **monopolistische concurrentie**. De zaak is geen monopolist op de ijsmarkt.

**2 · Gebruik de gegeven vraag voor deze zaak.** TO = 18q − 0,10q² en MO = 18 − 0,20q. De dalende lijn geldt voor één onderneming en voor de beschreven situatie, niet voor alle markten met veel aanbieders.

**3 · Kies q, lees P en bereken winst.** MO = MK geeft 18 − 0,20q = 6 → q = 60. Dat past binnen de capaciteit. Vóór 60 is MO groter dan MK en erna kleiner. P = 18 − 0,10 × 60 = € 12. TO = € 720 en TK = 120 + 6 × 60 = € 480. De winst is **€ 240 per dag**.
'''+fig('423_we','Hetzelfde rekenpad als bij monopolie, maar nu voor één zaak tussen veel aanbieders van verschillende producten.')+'''
**4 · Begrens het resultaat.** Dit is een berekening voor deze vraag en deze korte termijn. De marktvorm alleen levert geen bedrag van € 240 op. Een reactie van concurrenten kan de gegeven vraag veranderen.
'''+box('Onthouden','Classificeer met aantal aanbieders, product en toetreding. Kies daarna het gegeven ondernemingsmodel. De rekenregel kan bekend zijn terwijl de economische situatie anders is. We bouwen hier geen apart strategisch model voor oligopolie.','summary'))
 page('Van bron naar kenmerk',start()+ex('Prijsnemer of prijszetter?',
 'Onderneming A is een kleine prijsnemer en ontvangt € 9 per kg. Voor onderneming B geldt P = 18 − 0,20q. q is kg per week.',[
 ('Geef voor A GO en MO.','Bij de prijsnemer zijn GO = MO = P = € 9 per kg, binnen de haalbare productie.'),
 ('Bepaal TO en MO voor B. Is MO bij positieve q gelijk aan P?','TO = 18q − 0,20q²; MO = 18 − 0,40q. Bij positieve q is MO lager dan P: een extra verkoop tegen een lagere uniforme prijs verlaagt ook de opbrengst op eerdere eenheden.')])+ex('Vier logo’s',
 'Vier populaire merken meel zijn allemaal eigendom van dezelfde producent. Over andere meelproducenten geeft de bron niets.',[
 ('Bewijzen vier merken dat er vier zelfstandige aanbieders zijn?','Nee. De vier merken horen bij één producent. Merken tellen is niet hetzelfde als zelfstandige ondernemingen tellen.'),
 ('Kun je nu zeker zeggen dat de hele meelmarkt een monopolie is?','Nee. Informatie over andere aanbieders en goede alternatieven ontbreekt. De markt moet eerst worden afgebakend.')])+guided()+ex('De kenmerken staan er al',
 'A: veel telers leveren een identieke kwaliteit graan; toetreding is vrij. B: veel onafhankelijke kapsalons bieden verschillende service; beginnen is relatief eenvoudig. C: drie grote fabrikanten domineren een markt met hoge startkosten. D: één leverancier bezit de enige toegestane toegang tot een voorziening.',[
 ('Koppel A tot en met D aan de vier marktvormen.','A: volkomen concurrentie. B: monopolistische concurrentie. C: oligopolie. D: monopolie.'),
 ('Welke informatie onderscheidt B van een monopolie en C van volkomen concurrentie?','B heeft veel zelfstandige aanbieders en relatief eenvoudige toetreding. C heeft slechts drie grote aanbieders en hoge startkosten; dat wijkt af van veel kleine prijsnemers met vrije toetreding.')])+box('Een bronantwoord opbouwen','Noem de marktvorm én twee passende gegevens. “Oligopolie, want drie ondernemingen beheersen de markt en starten kost veel geld” is sterker dan alleen “oligopolie”.','small'))
 page('Het gegeven model toepassen',ex('Een zaak met een eigen vraaglijn',
 'De figuur hoort bij één lunchzaak tussen veel vergelijkbare maar niet identieke lunchzaken. De bron houdt het gedrag van andere zaken gelijk. MK = € 10 per maaltijd; q is maaltijden per dag.',[
 ('Lees de gemarkeerde hoeveelheid en prijs af. Welke twee lijnen gebruik je achtereenvolgens?','q = 20 maaltijden per dag en P = € 20. Eerst bepaalt MO = MK de hoeveelheid; daarna lees je bij die hoeveelheid P op GO/vraag.'),
 ('Waarom mag je dezelfde grafiek niet automatisch voor iedere oligopolist gebruiken?','De figuur is een specifieke vraag- en kostenaanname voor deze lunchzaak. Bij oligopolie kan de vraag naar één onderneming mede afhangen van de reacties van andere grote ondernemingen; daarvoor zijn extra aannames nodig.')])+fig('423_guided','De route is gegeven. Het aantal aanbieders verandert de algebra niet, maar wel de betekenis en voorwaarden van de vraaglijn.')+heading('Zelfstandige oefening')+ex('Twee veranderingen in een winkelstraat',
 'Eerst zijn er veel onafhankelijke gelijksoortige winkels. Daarna kopen twee ketens bijna alle winkels op. Tegelijk gaan de winkels sterk verschillen in assortiment. Er worden geen prijs- of kostencijfers gegeven.',[
 ('Bekijk eerst alleen de overnames. Welk kenmerk verandert?','Het aantal zelfstandige aanbieders neemt af: veel winkels vallen nu onder slechts twee beslissende ondernemingen.'),
 ('Bekijk alleen de verschillende assortimenten. Welk kenmerk verandert?','De productverschillen nemen toe: kopers zien meer heterogeniteit.'),
 ('Combineer de twee veranderingen. Welke marktvorm past nu het best bij de bron?','Enkele grote aanbieders én heterogene producten: oligopolie. De twee kenmerken moeten samen worden gebruikt.'),
 ('Beoordeel: “Door verschillende assortimenten is er nu zeker monopolistische concurrentie.”','Dat volgt niet. Monopolistische concurrentie vereist veel aanbieders. Twee dominerende ketens passen eerder bij oligopolie met heterogene producten. Productverschillen alleen bepalen de marktvorm niet.')]))
 independent_last=ex('Een kleine bakker met een eigen recept',
 'Voor één bakker tussen veel zelfstandige bakkers geldt op korte termijn P = 20 − 0,10q en TK = 80 + 4q. q is producten per dag; de capaciteit is 100. Het gedrag van concurrenten blijft gelijk.',[
 ('Bereken de winstmaximale hoeveelheid, prijs en winst.','TO = 20q − 0,10q², MO = 20 − 0,20q en MK = 4. MO = MK geeft q = 80, binnen de capaciteit; MO daalt door MK. P = € 12. TO = 12 × 80 = € 960; TK = 80 + 4 × 80 = € 400; winst = € 560 per dag.'),
 ('Maakt de gebruikte rekenprocedure deze bakker tot monopolist?','Nee. Ook een onderneming onder monopolistische concurrentie kan een dalende eigen vraag hebben. De bron noemt juist veel aanbieders. De procedure is geen bewijs van een monopolie.')])
 page('Zelf toepassen en doeloefening',independent_last+heading('Doeloefening')+source('Bron A · Vier afgebakende markten',
 'I: veel kleine telers bieden een identieke grondstof aan; kopers kennen de prijzen en toetreding is vrij. II: veel onafhankelijke lunchzaken verschillen in smaak en locatie; toetreding is relatief eenvoudig. III: drie grote aanbieders bedienen vrijwel de hele markt; een nieuw netwerk bouwen kost veel. IV: één aanbieder heeft als enige toegang tot een noodzakelijke voorziening; binnen deze markt zijn geen goede alternatieven.')+source('Bron B · Lunchzaak Puur',
 'Puur hoort bij markt II. Voor één dag geldt P = 30 − 0,25q en TK = 144 + 6q. q is maaltijden per dag; P is euro per maaltijd. De productiecapaciteit is 80 maaltijden. De vaste kosten blijven ook bij q = 0 bestaan. Gedrag van concurrenten, kwaliteit en overige vraagfactoren blijven in deze berekening gelijk.')+ex('Marktvorm is het begin','Gebruik alleen de beschreven markten en de gegeven korte-termijnberekening.',[
 ('Classificeer I tot en met IV. Geef voor elke markt het beslissende bronbewijs.','I: volkomen concurrentie: veel kleine aanbieders, homogeen product en vrije toetreding. II: monopolistische concurrentie: veel aanbieders, heterogene diensten en relatief eenvoudige toetreding. III: oligopolie: drie grote aanbieders en hoge toetredingskosten. IV: monopolie: één aanbieder en een onoverkomelijke toegangsdrempel binnen de afgebakende markt.'),
 ('Bepaal voor Puur TO, MO en MK.','TO = (30 − 0,25q)q = 30q − 0,25q². MO = 30 − 0,50q. MK = 6; de constante € 144 verdwijnt bij de marginale afleiding.'),
 ('Bereken de winstmaximale haalbare q, de verkoopprijs en de winst.','30 − 0,50q = 6 geeft q = 48. Dat is lager dan de capaciteit van 80. MO ligt ervoor boven 6 en erna eronder. P = 30 − 0,25 × 48 = € 18. TO = 18 × 48 = € 864; TK = 144 + 6 × 48 = € 432; winst = € 432 per dag.'),
 ('Verklaar waarom Puur geen horizontale GO-lijn hoeft te hebben, ook al zijn er veel aanbieders.','De producten zijn heterogeen: klanten onderscheiden smaak en locatie. Puur heeft daardoor enige invloed op de prijs. Een kleine prijsnemer bij volkomen concurrentie biedt juist een homogeen goed aan en neemt P als gegeven.'),
 ('Mag je de functie van Puur zonder extra broninformatie gebruiken voor markt III? Leg uit.','Nee. De functie geldt voor Puur onder de gegeven voorwaarden. Bij oligopolie moet onder meer duidelijk zijn hoe concurrenten reageren. De marktvorm III levert geen universele functie P = 30 − 0,25q op.')],points=[4,2,3,2,2],answer_fig='423_answer25')+box('Controle van je antwoord','Verbind de classificatie aan de bron. Houd de hoeveelheid van één zaak (q) apart van de hele markt (Q). Lees de verkoopprijs op de vraaglijn.','small'))
 page('Een markt is een afbakening',heading('Denkertje / Bonusopgave')+ex('De enige winkel op het station',
 'Op één perron staat één broodjeswinkel. Buiten het station liggen meerdere lunchzaken. Reizigers met haast blijven vaak op het perron; reizigers met veel tijd lopen geregeld naar buiten.',[
 ('Waarom kan de conclusie over marktmacht verschillen per klantgroep?','Reizigers met weinig tijd hebben minder bruikbare alternatieven dan reizigers die naar buiten kunnen. De effectieve concurrentie en prijsgevoeligheid kunnen dus verschillen, hoewel hetzelfde bedrijf verkoopt.'),
 ('Welke gegevens zou je verzamelen voordat je de markt definitief afbakent?','Bijvoorbeeld hoeveel reizigers bij een prijsverhoging elders kopen, hoeveel tijd dat kost en welke alternatieven zij als gelijkwaardig zien. Een keuze voor marktgrenzen vraagt gedragsinformatie.'),
 ('Waarom is “één winkel in beeld” onvoldoende bewijs van een monopolie?','Een foto zegt niets over alternatieven buiten beeld of over de relevante marktgrens. Eén locatie kan nog steeds concurrentie ondervinden van andere aanbieders.')])+heading('Herhaling / Herhaling en interleaving')+ex('De vaste kosten nogmaals controleren',
 'Twee klantgroepen leveren samen € 900 omzet. Er zijn in totaal 80 bezoeken. Variabele kosten zijn € 5 per bezoek en gezamenlijke constante kosten € 200.',[
 ('Bereken PS en winst.','TVK = 80 × 5 = € 400. PS = TO − TVK = 900 − 400 = € 500. Winst = PS − TCK = 500 − 200 = € 300.'),
 ('Leg uit welke fout ontstaat als iemand per groep € 200 vaste kosten aftrekt.','Dan telt diegene dezelfde gezamenlijke kosten twee keer. De totale winst wordt daardoor € 200 te laag berekend.')])+box('Vooruitblik','Tot nu toe telden we voordelen binnen de markt. De volgende paragrafen voegen gevolgen toe voor mensen die niet aan de transactie deelnemen.'))
