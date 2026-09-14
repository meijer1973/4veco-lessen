from author_common import *
def author():
 section('4.2.4')
 page('Een derde partij krijgt de rekening',begin('De koper betaalt. Wie draagt de schade?',
 'Je kunt een negatief extern effect en de getroffen derde partij benoemen. Je kunt private en maatschappelijke kosten onderscheiden. Je kunt een belastinguitkomst berekenen en de welvaartsvergelijking uitbreiden met externe kosten.',
 'Een bedrijf verkoopt leveringen. De klant betaalt de vervoerder, maar omwonenden ondervinden geluidshinder. Zij krijgen daarvoor geen vergoeding. De prijs kan dus lager zijn dan de kosten die de levering voor iedereen samen veroorzaakt.')+box('Negatief extern effect','Nadeel voor een derde partij dat door productie of consumptie ontstaat en niet in de prijs of een vergoeding is verwerkt. De derde partij is geen koper of verkoper in de onderzochte transactie.','definition')+fig('424_actors','De betaling loopt tussen koper en verkoper. De hinder treft omwonenden buiten die transactie.')+'''
### Privé kan de levering aantrekkelijk zijn
De vervoerder vergelijkt zijn ontvangsten met eigen kosten. De klant vergelijkt de prijs met eigen voordeel. Zonder heffing of vergoeding hoeven zij de hinder voor anderen niet mee te wegen.

Dat maakt niet elke levering verkeerd. Sommige leveringen leveren ook na aftrek van de schade voordeel op. De vraag is **hoeveel** activiteit gezamenlijk zinvol is, niet of alle activiteit moet verdwijnen.
'''+box('Verwar drie dingen niet','Een hoge rekening voor de koper is niet op zichzelf een extern effect. Een gewone productiekost van de verkoper is dat evenmin. Zoek een nadeel voor een buitenstaander dat niet wordt vergoed.','warning'))
 page('Een nieuwe lijn, met een nieuwe betekenis','''### Voeg de schade per extra eenheid toe
We gebruiken een concurrerende leveringsmarkt. De vraag is **P = 50 − 0,5Q** en het aanbod is **P = 10 + 0,5Q**. Q is leveringen per dag; P is euro per levering. Andere omstandigheden blijven gelijk. De aanbodlijn geeft hier de **marginale private kosten**: de eigen kosten van een extra levering.

Een onderzoek in deze oefencase waardeert de niet-vergoede schade op **€ 10 per levering**. Dat bedrag blijft bij elke hoeveelheid gelijk. De totale externe kosten zijn dus 10 × Q, niet alleen 10 maal de extra of de “te veel” uitgevoerde leveringen.
'''+formula('MK maatschappelijk = MK privé + externe kosten per extra eenheid<br>Hier: MK maatschappelijk = 20 + 0,5Q')+fig('424_social','Begin met vraag en private kosten. De maatschappelijke-kostenlijn ligt bij dezelfde Q precies € 10 hoger.')+'''
De maatschappelijke-kostenlijn laat **echte kosten voor alle betrokkenen samen** zien. Zij is niet automatisch de lijn waar bedrijven hun ongereguleerde aanbod op baseren. Zonder prikkel verandert hun eigen rekening nog niet.

Zonder ingrijpen: 50 − 0,5Q = 10 + 0,5Q → **Q₀ = 40, P₀ = € 30**. De maatschappelijke vergelijking is anders: 50 − 0,5Q = 20 + 0,5Q → **Qe = 30**.
''')
 page('Waarom is veertig hier te veel?','''### Beoordeel de volgende levering
Bij Q = 35 is de betalingsbereidheid € 32,50. De private marginale kosten zijn € 27,50. Koper en verkoper kunnen dus allebei voordeel zien. Maar inclusief € 10 hinder kost die levering de samenleving € 37,50. Het gezamenlijke nadeel is groter dan het gezamenlijke voordeel.

Tussen Q = 30 en Q = 40 worden leveringen uitgevoerd waarvoor de private vergelijking gunstig lijkt, maar de maatschappelijke vergelijking ongunstig is. Dat verschil veroorzaakt welvaartsverlies.
'''+fig('424_loss','Het verloren surplus ligt tussen vraag en maatschappelijke kosten, van de efficiënte naar de ongereguleerde hoeveelheid.')+'''
### Kijk breder dan CS + PS
Zonder belasting is CS = ½ × 40 × (50 − 30) = € 400. PS = ½ × 40 × (30 − 10) = € 400. Het private totale surplus is dus € 800.

De omwonenden dragen echter 40 × € 10 = € 400 schade. Het **maatschappelijk surplus** in dit model is € 800 − € 400 = **€ 400 per dag**.
'''+formula('Maatschappelijk surplus zonder heffing<br>= CS + PS − totale externe kosten')+box('Een begrensde maatstaf','We tellen in deze oefencase eurobedragen zonder verdelingsgewichten. Andere externe effecten, vaste kosten en uitvoeringskosten ontbreken. Verander je die aannames, dan verandert mogelijk de beoordeling.','small'))
 page('De bekende heffing verandert de eigen rekening','''### Gebruik opnieuw de twee prijzen uit Boek 3
Een heffing van **t = € 10 per levering**, afgedragen door de verkoper, maakt de schade voelbaar in de prijskeuze. Kopers betalen Pc. Producenten ontvangen na afdracht Pp. Voor het evenwicht geldt:
'''+formula('Pc = Pp + t<br>50 − 0,5Q = (10 + 0,5Q) + 10<br>Q = 30; Pc = € 35; Pp = € 25')+fig('424_tax','In deze case valt aanbod in kopersprijzen samen met maatschappelijke kosten, omdat t precies € 10 is. De producent blijft op de oorspronkelijke A aflezen.')+'''
### Overheidsontvangsten blijven een overdracht
De overheid ontvangt 10 × 30 = € 300. Dat geld verdwijnt niet uit de samenleving. Als we CS en PS na belasting berekenen, is de afdracht daar al buiten gehouden. Daarom tellen we de ontvangst van de overheid weer mee.
'''+formula('Maatschappelijk surplus met heffing<br>= CS + PS + belastingopbrengst − externe kosten')+'''
De € 300 belastingopbrengst is geen bewijs dat de omwonenden € 300 schadevergoeding krijgen. Ontvangst van geld en resterende hinder zijn verschillende posten. In deze case zijn de bedragen toevallig gelijk door de gekozen heffing per levering.
'''+box('Niet: elke belasting is precies goed','Bij de gegeven constante schade en zonder andere verstoringen bereikt t = € 10 hier de efficiënte hoeveelheid. Een onbekende schade, een te hoog tarief of uitvoeringskosten kunnen tot een andere conclusie leiden.','warning'))
 page('Uitgewerkt: een kleinere productiemarkt',heading('Uitgewerkt voorbeeld')+'''
**Kleurwater** is een denkbeeldige concurrerende markt voor wasbeurten. Vraag: Pc = 40 − Q. Aanbod: Pp = Q. Q is wasbeurten per dag, van 0 tot 40; beide prijzen zijn euro per beurt. Elke beurt veroorzaakt € 8 niet-vergoede hinder voor omwonenden. De verkopers dragen een heffing van € 8 per beurt af. Er zijn geen uitvoeringskosten of andere externe effecten.

**1 · Benoem de ontbrekende partij.** Omwonenden ondervinden hinder zonder vergoeding. Hun kosten horen niet bij de oorspronkelijke private aanbodlijn.

**2 · Bereken de ongereguleerde uitkomst.** Zonder heffing: 40 − Q = Q → Q₀ = 20. De prijs is € 20 per beurt.

**3 · Gebruik de heffingswig.** Pc = Pp + 8 geeft 40 − Q = Q + 8 → Q₁ = 16. Kopers betalen € 24; verkopers ontvangen € 16. Controle: 24 − 16 = € 8.

**4 · Bereken ontvangsten en schade.** De heffingsopbrengst is 8 × 16 = **€ 128 per dag**. De schade daalt van 8 × 20 = € 160 naar 8 × 16 = **€ 128 per dag**. Er blijft dus schade bestaan.
'''+fig('424_we','De heffing verlaagt het aantal wasbeurten van 20 naar 16. Het verschil tussen beide prijzen is de heffing, niet het verschil tussen beide hoeveelheden.'))
 page('Uitgewerkt: de volledige welvaartscontrole','''<div class="continuation">Uitgewerkt voorbeeld · vervolg</div>

**5 · Bereken alle onderdelen met dezelfde grenzen.**

| Post (€ per dag) | Zonder heffing | Met heffing |
|---|---:|---:|
| CS | ½ × 20 × 20 = 200 | ½ × 16 × 16 = 128 |
| PS | ½ × 20 × 20 = 200 | ½ × 16 × 16 = 128 |
| Overheidsontvangsten | 0 | 8 × 16 = 128 |
| Externe kosten | 8 × 20 = 160 | 8 × 16 = 128 |
| Maatschappelijk surplus | 200 + 200 − 160 = **240** | 128 + 128 + 128 − 128 = **256** |

**6 · Vergelijk en verklaar.** CS + PS daalt van € 400 naar € 256. Toch stijgt het maatschappelijk surplus met **€ 16 per dag**. Ontvangsten verschuiven naar de overheid en de externe schade neemt af. Alle onderdelen samen bepalen de uitkomst.

De efficiënte hoeveelheid volgt uit betalingsbereidheid = maatschappelijke MK: 40 − Q = Q + 8 → Qe = 16. De ongereguleerde markt produceerde vier beurten te veel. De verliesdriehoek had basis 4 en hoogte € 8: ½ × 4 × 8 = **€ 16**.
'''+box('De verdwenen € 144 is niet de hele rekening','CS + PS daalt € 144. Daarvan komt € 128 bij de overheid terecht. Het resterende private verlies is € 16. Tegelijk verdwijnt € 32 echte schade. Netto: € 32 − € 16 = € 16 maatschappelijke verbetering.','summary')+'''
### Waarom verschilt dit van Boek 3?
In Boek 3 begon de welvaartsvergelijking zonder externe effecten. Een heffing liet toen voordelige transacties verdwijnen. Hier veroorzaakten sommige transacties meer maatschappelijke kosten dan baten. Juist die activiteit verminderen kan de uitkomst verbeteren.
'''+box('Onthouden','Derde partij → eigen kosten en maatschappelijke kosten → oorspronkelijke markt → heffingswig → CS, PS, overheidsontvangst en resterende schade → maatschappelijke conclusie. Hetzelfde rekenmiddel krijgt een andere betekenis door de externe schade.','summary'))
 page('De nieuwe kosten herkennen',start()+ex('Een heffing terughalen',
 'Vraag: Pc = 20 − Q. Aanbod: Pp = Q. De verkoper draagt € 4 per eenheid af. Q is stuks per dag.',[
 ('Bereken Q, Pc en Pp na de heffing.','20 − Q = Q + 4 → 16 = 2Q → Q = 8. Pc = 20 − 8 = € 12 en Pp = € 8 per stuk. De wig is € 4.'),
 ('Bereken de heffingsopbrengst.','Opbrengst = t × Q = 4 × 8 = € 32 per dag. Gebruik de verkochte hoeveelheid na heffing.')])+ex('Wie staat buiten de transactie?',
 'A: een klant betaalt veel voor een schaars kaartje. B: geluid van een bedrijf verstoort onbetaald de nachtrust van buren. C: een bakker betaalt zijn meelrekening.',[
 ('Welke situatie beschrijft een negatief extern effect? Benoem de derde partij.','B: de buren zijn geen koper of verkoper in de bedrijfstransactie, maar ondervinden niet-vergoede geluidshinder.'),
 ('Waarom zijn A en C op zichzelf geen externe kosten?','A betreft een betaling van de koper binnen de transactie. C is een eigen productiekost die de bakker betaalt. Er is zonder extra informatie geen niet-vergoed nadeel voor derden aangetoond.')])+guided()+ex('Lees beide kostenlijnen',
 'De figuur toont een markt met € 10 externe schade per levering. Gebruik Q = 20.',[
 ('Lees de private en maatschappelijke marginale kosten af.','Bij Q = 20 zijn MK privé = 10 + 0,5 × 20 = € 20 en MK maatschappelijk = € 30 per levering.'),
 ('Bereken de totale externe schade bij 20 leveringen. Waarom is die niet € 10?','Totale schade = 20 × 10 = € 200 per dag. € 10 is de schade van één levering, niet van alle leveringen samen.'),
 ('Markeer Q₀ = 40 en Qe = 30. Arceer het oorspronkelijke verlies tussen die hoeveelheden: gebruik de vraag en de maatschappelijke-kostenlijn.','De verliesdriehoek loopt van Q = 30 tot 40. Bij Q = 40 is maatschappelijke MK € 40 en betalingsbereidheid € 30: hoogte € 10. Verlies = ½ × 10 × 10 = € 50 per dag.')],answer_fig='424_loss')+fig('424_guided','De verticale afstand geeft schade per levering. Totale schade vereist ook het aantal leveringen.'))
 page('Alle posten meenemen',ex('Een gedeeltelijke correctie',
 'Op een markt veroorzaakt elke eenheid € 8 externe schade. Met een heffing van € 4 worden 18 eenheden per dag verkocht. CS en PS zijn beide € 162 per dag. Zonder heffing was het maatschappelijk surplus € 240.',[
 ('Vul eerst de ontbrekende posten in: overheidsontvangst, externe schade en maatschappelijk surplus.','Overheidsontvangst = 4 × 18 = € 72; externe schade = 8 × 18 = € 144. Maatschappelijk surplus = 162 + 162 + 72 − 144 = € 252 per dag.'),
 ('Vergelijk met € 240. Bewijst verbetering dat alle externe schade verdwenen is?','Verbetering = 252 − 240 = € 12 per dag. Nee: er resteert € 144 schade. Meer maatschappelijk surplus is niet hetzelfde als nul hinder.')])+'''
| Post (€ per dag) | Met heffing |
|---|---:|
| CS + PS | 324 |
| Overheidsontvangst | … |
| Externe schade | … |
| Maatschappelijk surplus | … |
'''+heading('Zelfstandige oefening')+ex('Eigen kosten en schade veranderen tegelijk',
 'Bij dezelfde hoeveelheid productie stijgen de private kosten per extra eenheid met € 3 door duurder materiaal. Tegelijk daalt de externe schade per eenheid met € 5 door minder geluid. Er verandert verder niets.',[
 ('Wat doet alleen het duurdere materiaal met maatschappelijke MK?','De private MK stijgt € 3; bij gelijkblijvende externe schade stijgt maatschappelijke MK daardoor ook € 3 per eenheid.'),
 ('Wat doet alleen de afname van geluid met maatschappelijke MK?','De externe schade daalt € 5. Bij gelijkblijvende private kosten daalt maatschappelijke MK daardoor € 5 per eenheid.'),
 ('Bepaal het gezamenlijke effect op de maatschappelijke kosten per extra eenheid.','Het gezamenlijke effect is +3 − 5 = −€ 2 per extra eenheid.'),
 ('Beoordeel: “Meer eigen kosten betekent hier meer maatschappelijke kosten per extra eenheid.”','Onjuist: private kosten stijgen, maar de maatschappelijke MK daalt door de grotere afname van externe schade.')]))
 page('Zelfstandig: van rekenuitkomst naar verliesgebied',ex('Een nieuwe productiemarkt',
 'Voor behandelingen geldt Pc = 40 − Q en Pp = Q, in euro per behandeling; Q is behandelingen per dag. De schade aan omwonenden is € 8 per behandeling. Een producentenheffing bedraagt € 8. Er zijn geen andere maatschappelijke posten.',[
 ('Bereken de oorspronkelijke en de belaste uitkomst, inclusief beide prijzen.','Zonder heffing: 40 − Q = Q → Q₀ = 20 en P₀ = € 20. Met heffing: 40 − Q = Q + 8 → Q₁ = 16, Pc = € 24 en Pp = € 16.'),
 ('Bereken het maatschappelijk surplus vóór en na.','Voor: CS = PS = ½ × 20 × 20 = € 200; schade = € 160; maatschappelijk surplus = € 240. Na: CS = PS = € 128; ontvangst = € 128; schade = € 128; maatschappelijk surplus = € 256. De verbetering is € 16 per dag.'),
 ('Bepaal de efficiënte hoeveelheid. Arceer het oorspronkelijke welvaartsverlies in de gegeven grafiek en bereken het.','Maatschappelijke MK = Q + 8. 40 − Q = Q + 8 → Qe = 16. De verliesdriehoek ligt tussen de maatschappelijke-kostenlijn en de vraag van Q = 16 tot 20. Basis = 4 behandelingen, hoogte = € 8. Verlies = ½ × 4 × 8 = € 16 per dag.')],answer_fig='424_answer33')+fig('424_independent','Gebruik de bron en de gegeven lijnen. Voeg zelf de hoeveelheden, prijzen en het gevraagde gebied toe.'))
 page('Doel: een belasting inclusief derden',heading('Doeloefening')+source('Bron · Reinigingsdiensten',
 'Veel bedrijven bieden dezelfde reinigingsdienst aan. Vraag: Pc = 60 − Q; aanbod: Pp = Q. Q is diensten per dag van 0 tot 60; prijzen zijn euro per dienst. Elke dienst veroorzaakt € 20 niet-vergoede overlast voor omwonenden. De overheid voert een door producenten afgedragen heffing van € 20 per dienst in. Er zijn geen uitvoeringskosten, vaste kosten of andere externe effecten. Andere vraag- en aanbodfactoren veranderen niet.')+ex('Wie telt mee?','Gebruik de bron en de basisgrafiek.',[
 ('Noem de derde partij. Bereken de oorspronkelijke hoeveelheid en prijs, en de totale externe schade.','De derde partij bestaat uit de omwonenden. Zonder heffing: 60 − Q = Q → Q₀ = 30 diensten; P₀ = € 30 per dienst. Schade = 20 × 30 = € 600 per dag.'),
 ('Bereken met de heffingswig Q, Pc, Pp en de overheidsontvangst.','60 − Q = Q + 20 → Q₁ = 20 diensten per dag. Pc = € 40; Pp = € 20. Controle: 40 − 20 = 20. Ontvangst = 20 × 20 = € 400 per dag.'),
 ('Bereken het maatschappelijk surplus vóór en na ingrijpen. Laat alle vier posten zien.','Voor: CS = ½ × 30 × 30 = € 450; PS = € 450; ontvangst = 0; schade = € 600; maatschappelijk surplus = € 300. Na: CS = ½ × 20 × 20 = € 200; PS = € 200; ontvangst = € 400; schade = € 400; maatschappelijk surplus = € 400 per dag.'),
 ('Markeer de efficiënte hoeveelheid en arceer het oorspronkelijke welvaartsverlies. Benoem basis en hoogte.','MK maatschappelijk = Q + 20. 60 − Q = Q + 20 geeft Qe = 20. Het verlies is de driehoek tussen vraag en maatschappelijke MK van Q = 20 tot Q = 30: basis 10 diensten, hoogte € 20 per dienst. Oppervlakte = ½ × 10 × 20 = € 100 per dag.'),
 ('Beoordeel: “CS en PS dalen door de belasting, dus de maatschappij verliest.”','Onjuist in deze case. De overheidsontvangst en de afgenomen externe schade moeten ook worden meegeteld. Het maatschappelijk surplus stijgt van € 300 naar € 400. Dit bewijst niet dat ieder afzonderlijk persoon wint of dat elke belasting goed is.')],points=[3,3,4,2,2],answer_fig='424_answer34')+fig('424_target','De private en maatschappelijke kosten zijn gegeven. Voeg de uitkomsten en het gevraagde verliesgebied toe.'))
 page('Een bedrag is nog geen zekerheid',heading('Denkertje / Bonusopgave')+ex('Hoe goed kennen we de schade?',
 'Een gemeente leest een schatting: externe schade ligt tussen € 6 en € 14 per levering. De gemiddelde waarde is € 10. Een adviseur zegt daarom dat een heffing van precies € 10 onder alle omstandigheden het beste is.',[
 ('Welk verschil bestaat er tussen de eerdere oefencase en deze bron?','In de oefencase stond constante schade per levering exact vast. Hier is zij onzeker en mogelijk afhankelijk van omstandigheden. Een gemiddelde is niet automatisch de marginale schade in elke situatie.'),
 ('Noem twee gegevens die belangrijk zijn voor een beter advies.','Bijvoorbeeld hoe de schade verandert met tijd en hoeveelheid, wie de schade ondervindt, hoe vraag en aanbod op de heffing reageren, en wat meten en handhaven kost. Twee relevante, uitgelegde gegevens volstaan.'),
 ('Formuleer een voorzichtiger conclusie.','Een heffing van € 10 kan een bruikbaar uitgangspunt zijn bij de gemiddelde schatting, maar het optimale tarief is met deze informatie niet exact bewezen. Het advies moet worden getoetst aan schade, reacties en uitvoeringskosten.')])+heading('Herhaling / Herhaling en interleaving')+ex('Niet de prijs van de MO-lijn',
 'Voor een monopolist geldt P = 40 − Q en MK = 10. Q is stuks per week; de capaciteit is 30.',[
 ('Bereken Qm en Pm.','MO = 40 − 2Q. MO = MK geeft 40 − 2Q = 10 → Qm = 15 stuks per week. Pm = 40 − 15 = € 25. De hoeveelheid past binnen de capaciteit.'),
 ('Leg uit waarom € 10 niet de verkoopprijs is.','€ 10 is bij de gekozen hoeveelheid MO = MK. De verkoopprijs wordt op de vraaglijn afgelezen en is € 25. Dezelfde prijsleesmethode uit hoofdstuk 4.1 blijft gelden.')]))
