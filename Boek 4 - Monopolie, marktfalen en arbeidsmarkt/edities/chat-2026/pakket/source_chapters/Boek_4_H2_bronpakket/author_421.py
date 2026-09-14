from author_common import *
def author():
 section('4.2.1')
 page('Van winst naar welvaart',begin('Meer winst. Ook meer welvaart?',
 'Je kunt de monopolie-uitkomst vergelijken met een efficiënte uitkomst. Je kunt CS, PS en totaal surplus berekenen en arceren. Je kunt een overdracht onderscheiden van welvaartsverlies en PS onderscheiden van winst.',
 'Een verhuurbedrijf verhoogt de prijs en verhuurt minder apparaten. De winst stijgt. Klanten betalen meer of haken af. Is er alleen geld verschoven, of gaat er ook gezamenlijk voordeel verloren?')+'''
### Dezelfde markt, twee verschillende vragen
In hoofdstuk 4.1 zochten we de grootste winst voor één onderneming. Nu kijken we naar het voordeel van **kopers én verkopers samen**. We houden de vraag, productiekosten en kwaliteit gelijk. Er zijn hier geen externe effecten: buitenstaanders hebben geen kosten of baten van de transacties.

**Consumentensurplus (CS)** is het verschil tussen de betalingsbereidheid en de betaalde prijs, opgeteld over de verkochte eenheden. **Producentensurplus (PS)** is de opbrengst boven de variabele kosten. Het ligt tussen de verkoopprijs en de marginale-kostenlijn, tot aan de verkochte hoeveelheid.
'''+formula('TS = CS + PS<br>winst = PS − TCK')+'''
We noemen TS het **totale surplus**. TCK zijn de totale constante kosten. Bij de vergelijking blijven die kosten gelijk. Daarom geven veranderingen van TS hier ook de verandering van het gezamenlijke voordeel na aftrek van TCK.
'''+box('Welke hoeveelheid?','In hoofdstuk 4.1 stond q voor één onderneming. Hier gebruiken we Q voor de hele markt. Bij één monopolist zijn q en Q hetzelfde aantal. Bij de vergelijking gebruiken we steeds de kosten van de héle onderzochte productie.','small')+'''
### Welvaart is niet hetzelfde als een eerlijke verdeling
Meer totaal surplus zegt nog niet wie het krijgt. De surplusberekening gebruikt betalingsbereidheid in euro en geeft geen volledig oordeel over alle aspecten van welzijn of rechtvaardigheid.
''')
 page('Twee uitkomsten in dezelfde grafiek','''### Eerst de keuze van de monopolist
Voor de verhuur van apparaten geldt **P = 80 − Q** en **MK = 20 + Q**. P en MK zijn euro per verhuur; Q is verhuurbeurten per dag. De capaciteit is 60. Alle klanten betalen in één situatie dezelfde prijs. Andere omstandigheden blijven gelijk.

De bekende route geeft TO = 80Q − Q² en MO = 80 − 2Q. Uit MO = MK volgt **Qm = 20**. Op de vraaglijn hoort daarbij **Pm = € 60**.
'''+fig('421_choice','Punt M ligt op de vraaglijn. Het snijpunt van MO en MK bepaalt alleen de hoeveelheid.')+'''
### Dan de efficiënte hoeveelheid
Een extra verhuur verhoogt het gezamenlijke voordeel zolang de betalingsbereidheid groter is dan MK. Voor het laatste zinvolle beetje productie geldt daarom **P = MK**: 80 − Q = 20 + Q. Dat geeft **Qe = 30** en **Pe = € 50**.
'''+box('Een vergelijkingsmaatstaf','De efficiënte uitkomst gebruikt dezelfde vraag en dezelfde kosten als de monopolie-uitkomst. We veranderen niet tegelijk de techniek of kwaliteit. Dit is geen bewering dat elke echte concurrerende markt exact zo werkt.','small'))
 page('De gebieden uit elkaar houden','''### Wat gebeurt er met het voordeel van kopers?
Bij de efficiënte uitkomst is CS = ½ × 30 × (80 − 50) = **€ 450 per dag**. Bij monopolie is CS = ½ × 20 × (80 − 60) = **€ 200 per dag**.

Kopers verliezen € 250. Maar dat bedrag verdwijnt niet helemaal. De twintig blijvende verhuurbeurten worden € 10 duurder: **€ 200 gaat van kopers naar de aanbieder**. Bij de tien weggevallen verhuurbeurten verdwijnt voordeel voor beide kanten.
'''+fig('421_transfer','De rechthoek is een overdracht. Alleen de driehoek tussen Q = 20 en Q = 30 is verloren surplus.')+'''
### Wat krijgt de aanbieder?
Bij monopolie is MK bij Q = 20 gelijk aan € 40. PS is een rechthoek van 20 × (60 − 40), plus een driehoek van ½ × 20 × (40 − 20): samen **€ 600**. Bij Qe = 30 is PS = ½ × 30 × (50 − 20) = **€ 450**.

PS stijgt met € 150, niet met € 200: de aanbieder krijgt de overdracht, maar verliest ook € 50 surplus door de lagere afzet. TS daalt van € 900 naar € 800. Het **welvaartsverlies is € 100**.
'''+box('Verloren transacties','De driehoek heeft basis 30 − 20 = 10 verhuurbeurten en hoogte 60 − 40 = € 20 per beurt. Welvaartsverlies = ½ × 10 × 20 = € 100 per dag. Het is geen rekening die iemand ontvangt.','summary'))
 page('Eén volledige vergelijking',heading('Uitgewerkt voorbeeld')+'''
**Studiohuur** is de enige aanbieder in deze oefencase. Vraag: P = 70 − Q. Totale kosten: TK = 100 + 10Q + 0,5Q². Q is sessies per week; P is euro per sessie. De capaciteit is 50 sessies. De € 100 constante kosten zijn in deze week onvermijdelijk. Er zijn geen externe effecten.

**1 · Vind beide hoeveelheden.** MO = 70 − 2Q en MK = 10 + Q. Monopolie: 70 − 2Q = 10 + Q → Qm = 20. Lees Pm = 70 − 20 = € 50. Efficiënt: 70 − Q = 10 + Q → Qe = 30 en Pe = € 40. Beide hoeveelheden zijn haalbaar.

**2 · Selecteer en bereken de gebieden.**

| Per week | Monopolie: Q = 20 | Efficiënt: Q = 30 |
|---|---:|---:|
| CS | ½ × 20 × (70 − 50) = € 200 | ½ × 30 × (70 − 40) = € 450 |
| PS | 20 × (50 − 30) + ½ × 20 × (30 − 10) = € 600 | ½ × 30 × (40 − 10) = € 450 |
| TS | € 800 | € 900 |
| Winst = PS − 100 | € 500 | € 350 |

**3 · Controleer het verlies.** TS daalt € 100. De driehoek geeft hetzelfde: ½ × (30 − 20) × (50 − 30) = € 100.

**4 · Leg de verdeling uit.** De overdracht is 20 × (50 − 40) = € 200. De daling van CS is groter, omdat ook kopersvoordeel van weggevallen sessies verdwijnt. Meer PS is hier dus niet meer TS.
'''+fig('421_we','Bij Studiohuur is de driehoek van het verlies los te zien van de rechthoek van de overdracht.')+box('Onthouden','Bereken Qm met MO = MK en Qe met P = MK. Lees beide prijzen op de vraaglijn. Bereken CS en PS bij de werkelijk verkochte hoeveelheid. Welvaartsverlies = verschil in TS. Trek constante kosten nog van PS af voor winst. In §4.2.2 onderzoeken we verschillende prijzen per groep.','summary'))
 page('Opfrissen en aflezen',start()+ex('De bekende monopolieprocedure',
 'Voor een aanbieder geldt P = 30 − 0,5Q en TK = 40 + 10Q. Q is bezoeken per dag; P is euro per bezoek. De capaciteit is 40 bezoeken.',[
 ('Bepaal MO en MK. Bereken Qm en Pm.','TO = 30Q − 0,5Q², dus MO = 30 − Q. MK = 10. Uit 30 − Q = 10 volgt Qm = 20 bezoeken per dag, binnen de capaciteit. Pm = 30 − 0,5 × 20 = € 20 per bezoek.'),
 ('Bereken de winst bij die hoeveelheid.','TO = 20 × 20 = € 400; TK = 40 + 10 × 20 = € 240. Winst = 400 − 240 = € 160 per dag.')])+ex('Niet elk verlies is verdwenen',
 'Na een prijsverandering daalt CS met € 120 per week. PS stijgt met € 80. Andere onderdelen van de welvaartsvergelijking veranderen niet.',[
 ('Bereken de verandering van TS.','ΔTS = −120 + 80 = −€ 40 per week. Het gezamenlijke surplus daalt dus met € 40.'),
 ('Een leerling noemt de hele € 120 welvaartsverlies. Wat vergeet hij?','Hij vergeet de € 80 die bij producenten terechtkomt. Dat deel is een overdracht binnen de onderzochte groep. Alleen het saldo van € 40 verdwijnt uit TS.')])+guided()+ex('Herken de twee gebieden',
 'Gebruik de volledig gemarkeerde figuur op deze pagina. Dezelfde vraag en kosten gelden in beide uitkomsten.',[
 ('Lees Qm, Pm, Qe en Pe af. Benoem de economische functie van gebied A en gebied B.','Qm = 20, Pm = € 60, Qe = 30 en Pe = € 50. A is de overdracht op de blijvende verkopen; B is het welvaartsverlies door minder verkopen.'),
 ('Bereken de oppervlakte van A en B.','A = 20 × (60 − 50) = € 200 per dag. B = ½ × (30 − 20) × (60 − 40) = € 100 per dag.')])+fig('421_guided','A wordt door andere marktdeelnemers ontvangen; B niet. Beide bedragen zijn euro per dag.'))
 page('Van gebieden naar een conclusie',ex('Een tabel aanvullen',
 'Een aanbieder verhuurt opslagvakken. Bij monopolie zijn Q = 20 en P = € 50; de efficiënte uitkomst is Q = 30 en P = € 40. De vraag begint bij € 70; MK = 10 + Q. Alle bedragen hieronder zijn per week. Er zijn geen externe effecten.',[
 ('Vul de lege cellen van de tabel in. Gebruik voor PS bij monopolie eerst een rechthoek en daarna een driehoek.','Monopolie: CS = ½ × 20 × 20 = € 200; PS = 20 × 20 + ½ × 20 × 20 = € 600; TS = € 800. Efficiënt: CS = € 450; PS = € 450; TS = € 900.'),
 ('Bereken de overdracht en het welvaartsverlies.','Overdracht = 20 × (50 − 40) = € 200. Welvaartsverlies = 900 − 800 = € 100 per week.')])+'''
| Situatie | CS (€ per week) | PS (€ per week) | TS (€ per week) |
|---|---:|---:|---:|
| Monopolie | … | … | … |
| Efficiënt | 450 | 450 | … |
'''+heading('Zelfstandige oefening')+ex('Twee effecten tegelijk',
 'Door één prijs- en afzetverandering bij een verhuurder ontstaat een overdracht van € 300 van kopers naar verkopers. Daarnaast vervalt € 60 koperssurplus en € 40 producentensurplus door niet meer gesloten transacties. Er verandert verder niets.',[
 ('Bekijk alleen de overdracht. Wat doet die met CS, PS en TS?','CS daalt € 300 en PS stijgt € 300. TS verandert door deze overdracht niet.'),
 ('Bekijk alleen de weggevallen transacties. Hoe verandert TS?','TS daalt met 60 + 40 = € 100.'),
 ('Bereken de totale verandering van CS, PS en TS.','ΔCS = −300 − 60 = −€ 360; ΔPS = +300 − 40 = +€ 260; ΔTS = −€ 100.'),
 ('Beoordeel: “PS stijgt, dus er is geen marktfalen.”','Onjuist. Het extra PS voor de verkoper is kleiner dan het verlies voor kopers. TS daalt met € 100 door gemiste wederzijds voordelige transacties.')])+ex('De markt voor prints',
 'P = 60 − Q en MK = Q. Q is prints per week en P euro per print, met 0 ≤ Q ≤ 50. Er zijn geen externe effecten.',[
 ('Bepaal de monopolie-uitkomst en de efficiënte uitkomst.','MO = 60 − 2Q. MO = MK geeft Qm = 20 en Pm = € 40. P = MK geeft Qe = 30 en Pe = € 30.'),
 ('Bereken CS, PS en TS bij monopolie en bepaal het welvaartsverlies.','CSm = ½ × 20 × 20 = € 200. PSm = 20 × (40 − 20) + ½ × 20 × 20 = € 600. TSm = € 800. Efficiënt: CSe = PSe = ½ × 30 × 30 = € 450, dus TSe = € 900. Welvaartsverlies = € 100 per week.')]))
 page('Doel: verdeling en verlies',heading('Doeloefening')+source('Bron · De enige VR-studio',
 'Eén studio bedient de hele beschreven markt. Vraag: P = 80 − 0,5Q. Kosten: TK = 200 + 20Q + 0,25Q²; dus MK = 20 + 0,5Q. Q is sessies per week, P is euro per sessie. De capaciteit is 100 sessies. De € 200 constante kosten blijven deze week in beide situaties gelijk. Vergelijk met dezelfde vraag en kosten bij de efficiënte hoeveelheid. Geen externe effecten of andere veranderingen.')+ex('De VR-studio','Gebruik de bron en de basisgrafiek. De lijnen zijn al gegeven.',[
 ('Bereken Qm en Pm, en daarna Qe en Pe.','MO = 80 − Q. Monopolie: 80 − Q = 20 + 0,5Q → 60 = 1,5Q → Qm = 40 sessies, Pm = € 60. Efficiënt: 80 − 0,5Q = 20 + 0,5Q → Qe = 60, Pe = € 50. Beide passen binnen 100.'),
 ('Markeer beide uitkomsten en arceer CS en PS bij monopolie. Bereken die bedragen en de winst.','CSm = ½ × 40 × (80 − 60) = € 400. MK(40) = € 40. PSm = 40 × (60 − 40) + ½ × 40 × (40 − 20) = 800 + 400 = € 1.200. Winst = PS − TCK = 1.200 − 200 = € 1.000 per week. Gebieden: CS tussen vraag en P = 60; PS tussen P = 60 en MK, tot Q = 40.'),
 ('Bereken TS in beide situaties en het welvaartsverlies. Benoem basis en hoogte van de verliesdriehoek.','TSm = 400 + 1.200 = € 1.600. Efficiënt: CSe = ½ × 60 × 30 = € 900 en PSe = ½ × 60 × 30 = € 900; TSe = € 1.800. Verlies = € 200 per week. Basis = 60 − 40 = 20 sessies; hoogte = 60 − 40 = € 20 per sessie; ½ × 20 × 20 = € 200.'),
 ('Bereken de overdracht op de blijvende sessies. Leg uit waarom die niet zelf het welvaartsverlies is.','Overdracht = 40 × (60 − 50) = € 400 per week. Die € 400 verplaatst zich van kopers naar de aanbieder en blijft binnen CS + PS. Het verlies van € 200 betreft niet meer uitgevoerde, gezamenlijk voordelige sessies.'),
 ('Beoordeel: “Meer producentensurplus betekent dat deze uitkomst voor de samenleving beter én eerlijker is.”','Onjuist. PS stijgt van € 900 naar € 1.200, maar TS daalt van € 1.800 naar € 1.600. Wie het voordeel krijgt en wat eerlijk is, vragen bovendien een afzonderlijk verdelingsoordeel. De berekening bevat geen norm voor eerlijkheid.')],points=[3,3,3,2,2],answer_fig='421_answer7')+fig('421_target','Gegeven lijnen voor de VR-studio. Voeg alleen de gevraagde markeringen en arceringen toe.'))
 page('Een vergelijking zorgvuldig gebruiken',heading('Denkertje / Bonusopgave')+ex('Een betere techniek',
 'Een ontwerper zegt: “Mijn nieuwe techniek heeft lagere kosten. Daarom mag je mijn monopolie niet vergelijken met een concurrerende markt met de oude, dure techniek.” Er zijn nog geen cijfers over de nieuwe kosten of toekomstige uitvindingen.',[
 ('Waarom kan een vergelijking met verschillende technieken de oorzaak van een welvaartsverschil vertroebelen?','Dan veranderen marktvorm én kosten tegelijk. Een verschil in TS kan door de prijskeuze komen, door lagere productiekosten of door beide. De afzonderlijke invloed van marktmacht is zo niet af te leiden.'),
 ('Stel twee eerlijke vergelijkingen voor die samen meer inzicht geven.','Vergelijk eerst monopolie en de efficiënte hoeveelheid bij dezelfde nieuwe techniek. Dat isoleert de beperking van afzet. Vergelijk daarnaast de oude en nieuwe techniek onder dezelfde prijs- of marktaannames. Daarvoor zijn kostengegevens nodig.'),
 ('Bewijst het bestaan van een patent al dat de totale maatschappelijke uitkomst beter is?','Nee. Het patent kan in de bron een prikkel of barrière vormen, maar het netto-effect vereist informatie over innovatievoordeel, prijs, productie, looptijd en alternatieven. Die informatie ontbreekt hier.')])+heading('Herhaling / Herhaling en interleaving')+ex('De belasting blijft een wig',
 'Op een concurrerende markt is de oorspronkelijke prijs € 12. Na een belasting betalen kopers € 15 en ontvangen producenten € 10. Er worden 80 stuks per week verkocht.',[
 ('Bereken de belasting per stuk en de overheidsopbrengst.','t = Pc − Pp = 15 − 10 = € 5 per stuk. Opbrengst = 5 × 80 = € 400 per week.'),
 ('Bereken het kopers- en verkopersdeel van de belasting per verkocht stuk.','Kopersdeel = 15 − 12 = € 3; verkopersdeel = 12 − 10 = € 2. Samen € 5. Wie de belasting afdraagt, is hiermee nog niet vastgesteld.')])+box('Terug naar de hoofdvraag','Dezelfde prijsverandering kan tegelijk een overdracht én verloren surplus veroorzaken. Houd die twee effecten in je berekening apart.'))
