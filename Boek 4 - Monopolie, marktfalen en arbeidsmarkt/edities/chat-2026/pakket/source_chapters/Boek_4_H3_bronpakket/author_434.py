from author_common import *
section('4.3.4')
page('Een ondergrens aan het loon',begin('Een hoger uurloon voor iedereen?',
'Je kunt bepalen of een minimumloon bindend is. Je kunt in een gegeven model arbeidsvraag, arbeidsaanbod, werkgelegenheid en loonsom berekenen. Je kunt verschillen tussen groepen werknemers uitleggen.',
'Een minimumloon kan het uurloon verhogen. Maar is de totale hoeveelheid betaald werk dan ook groter? We gebruiken de minimumprijs uit Boek 3 opnieuw, nu met loon en arbeid.')+
box('Definitie · minimumloon','Een ondergrens waaronder het loon niet mag liggen. In dit hoofdstuk gebruiken we fictieve uurlonen om een economisch model te onderzoeken, niet de actuele wettelijke bedragen.','definition')+
table(['Minimumprijs bij een product','Minimumloon in ons model'],[['Vergelijk de ondergrens met de evenwichtsprijs.','Vergelijk de ondergrens met het evenwichtsloon.'],['Bereken vraag en aanbod bij de opgelegde prijs.','Bereken arbeidsvraag en arbeidsaanbod bij het loon.'],['Stel vast hoeveel er werkelijk wordt verkocht.','Stel vast hoeveel arbeid werkelijk wordt betaald.']])+
'''Als het evenwichtsloon € 12 is en het minimum € 10, verandert het evenwicht niet. € 12 is immers toegestaan. Het minimum is dan **niet-bindend**. Het feitelijke loon wordt dus niet automatisch € 10.

'''+fig('floor_nonbinding','Een loonvloer onder het evenwicht raakt de feitelijke loonvorming in dit model niet.')+
'<p class="small">Model: concurrerende werkgevers, vergelijkbare arbeid en naleving van de vloer. Werkgevers passen personeelsaantallen aan; alle gevraagde plaatsen worden gevuld, zonder vacatures of zoekproblemen.</p>')
page('Een bindend minimumloon', '''### Hoger dan het evenwicht
In dezelfde voorbeeldmarkt geldt **Lᵥ = 200 − 10w** en **Lₐ = −40 + 10w**, voor € 4 ≤ w ≤ € 20. L is het aantal personen met ieder 20 uur per week; w is het uurloon in euro. Het vrije evenwicht is **€ 12 en 80 personen**.

Nu komt er een minimumloon van € 14. Dat ligt boven het evenwicht en is **bindend**. In dit model wordt het loon € 14.

Arbeidsvraag: 200 − 10 × 14 = **60 personen**.<br>
Arbeidsaanbod: −40 + 10 × 14 = **100 personen**.

'''+fig('floor_binding','Het minimumloon verandert het loon op de bestaande lijnen. Het aanbodoverschot is een horizontale afstand, geen oppervlakte.')+
'''Werkgelegenheid = **60 personen**: werkgevers vullen alle gevraagde plaatsen. Het aanbodoverschot is 100 − 60 = **40 personen**. Die 40 willen bij dit loon werken, zoeken en zijn beschikbaar, maar krijgen in dit model geen baan.

### Niet alle veertig hebben hun baan verloren
Eerst werkten 80 personen; nu 60. Dat zijn **20 minder werkenden**. Tegelijk groeit het aantal aanbieders van 80 naar 100: **20 extra aanbieders**.

Het nieuwe verschil van 40 bestaat dus uit 20 minder werkenden én 20 extra aanbieders. Je mag niet zeggen dat alle 40 een baan hebben verloren.
'''+box('Wie heeft voordeel?','Wie hetzelfde aantal uren blijft werken, krijgt meer loon per uur. Wie geen werk krijgt, ontvangt dat hogere loon niet. Een uitspraak over “de werknemers” moet daarom aangeven over welke groep zij gaat.','summary'))
page('Loonsom: loon maal betaalde arbeid', '''### Het loon per uur en de totale uitbetaling
De **loonsom** is het totale loon dat werknemers samen ontvangen in een periode. Kijk steeds naar de arbeid die werkelijk wordt betaald, niet naar alle arbeid die mensen graag willen aanbieden.

'''+formula('loonsom per week = uurloon × betaalde uren per week<br>= uurloon × uren per werknemer × werkenden')+
'''Oud: € 12 × 20 uur × 80 personen = **€ 19.200 per week**.<br>
Nieuw: € 14 × 20 uur × 60 personen = **€ 16.800 per week**.

De loonsom daalt hier met (€ 16.800 − € 19.200) / € 19.200 × 100% = **12,5%**. Het hogere uurloon weegt niet op tegen de daling van het aantal betaalde uren.

'''+fig('floor_bill','De rechthoek w × L gebruikt het aantal werkenden. Omdat L hier personen is, vermenigvuldig je nog met 20 uur per persoon per week.')+
'''Bij een andere arbeidsvraag kan de werkgelegenheid minder sterk reageren. Dan kan een hoger uurloon samengaan met een hogere totale loonsom. Reken daarom beide situaties uit; onthoud geen vaste uitkomst voor de loonsom.

### Geen algemene voorspelling over de werkelijkheid
Werkgevers kunnen anders reageren dan in dit eenvoudige model. Ook productiviteit, vacatures, prijzen en marktverhoudingen kunnen veranderen. Een berekende daling in ons model bewijst niet dat iedere echte minimumloonsverhoging precies dit effect heeft.
'''+box('Geen automatische aankoop door de overheid','Een minimumloon betekent niet dat de overheid de niet-geplaatste arbeid “opkoopt”. Daarvoor zou een afzonderlijke regeling in de bron moeten staan.','warning'))
page('Uitgewerkt voorbeeld',heading('Uitgewerkt voorbeeld')+
source('Een loonvloer in de pakketbranche','Lᵥ = 180 − 5w; Lₐ = −20 + 5w, voor € 4 ≤ w ≤ € 36. L is het aantal personen met ieder 20 betaalde uren per week; w is het uurloon in euro. Het minimumloon wordt € 22. Neem concurrerende werkgevers, gelijke arbeid en geen vacatures of zoekproblemen aan. Het brutoloon is in dit model ook de volledige uurkost voor de werkgever.')+
'''### 1 · Bereken het vrije evenwicht en toets de ondergrens
180 − 5w = −20 + 5w → 200 = 10w → **w = € 20**.<br>
L = 180 − 5 × 20 = **80 personen**. € 22 > € 20: de vloer is bindend.

### 2 · Bereken beide hoeveelheden en de werkgelegenheid
Lᵥ = 180 − 5 × 22 = **70 personen**.<br>
Lₐ = −20 + 5 × 22 = **90 personen**.<br>
Er werken **70 personen**. Het aanbodoverschot is 90 − 70 = **20 personen**.

### 3 · Vergelijk de loonsommen
Oud: € 20 × 20 × 80 = **€ 32.000 per week**.<br>
Nieuw: € 22 × 20 × 70 = **€ 30.800 per week**.<br>
Verandering: (30.800 − 32.000) / 32.000 × 100% = **−3,75%**.

### 4 · Leg de verdeling uit
Wie 20 uur blijft werken, krijgt € 440 in plaats van € 400 per week. Er zijn wel 10 minder werkenden. Het aanbod groeit met 10 personen. Samen geeft dat het nieuwe aanbodoverschot van 20 personen.

Het hogere loon geldt dus niet als inkomen voor alle 90 aanbieders. Zonder individuele gegevens weten we ook niet welke personen hun baan behouden.
'''+box('Samenvatting §4.3.4','Eerst het vrije evenwicht, dan de bindendheid. Bereken vraag, aanbod en betaald werk afzonderlijk. Gebruik betaald werk voor de loonsom. Maak onderscheid tussen blijvende werknemers, minder werkenden en extra aanbieders. In §4.3.5 bekijken we loonafspraken en beleid.','summary'))
page('Start en een vloer herkennen',start()+
ex('De minimumprijs terughalen','Op een goederenmarkt is de evenwichtsprijs € 8. Er komt een minimumprijs van € 10. Bij € 10 is de vraag 60 en het aanbod 100 producten per week. De overheid koopt niets op.',[
('Hoeveel producten worden verkocht en hoe groot is het aanbodoverschot?',ans('Er worden <b>60 producten per week</b> verkocht. Aanbodoverschot = 100 − 60 = <b>40 producten per week</b>.','Zonder aankoopregeling zijn er niet automatisch kopers voor alle aangeboden producten.'))])+ 
ex('Personen zijn geen uren','Er werken 50 mensen. Ieder werkt 20 uur per week tegen € 15 bruto per uur.',[
('Bereken de loonsom per week.',ans('€ 15 × 20 × 50 = <b>€ 15.000 per week</b>.','Het uurloon moet met het aantal betaalde uren worden vermenigvuldigd.'))])+guided()+
fig('floor_we','Bij het voorbeeld worden 70 personen gevraagd en bieden 90 personen arbeid aan. Gebruik de gemarkeerde uitkomst.')+ex('Begrijpen vóór rekenen','Gebruik het volledig uitgewerkte voorbeeld op de vorige pagina: oud € 20 en 80 werkenden; nieuw € 22, 70 werkenden en 90 aanbieders.',[
('Hoeveel minder mensen werken er? Hoeveel extra mensen bieden arbeid aan?',ans('Minder werkenden: 80 − 70 = <b>10 personen</b>. Extra aanbieders: 90 − 80 = <b>10 personen</b>.','Samen vormen deze veranderingen het nieuwe verschil van 20 personen.')),
('Waarom reken je voor de nieuwe loonsom niet met alle 90 aanbieders?',ans('Alleen de 70 werkenden ontvangen loon voor de gevraagde arbeid. De overige 20 krijgen in dit model geen baan.','Aanbod is niet hetzelfde als betaalde arbeid.'))]))
page('Van begeleid naar zelfstandig',guided().replace('## Begeleide inoefening','<div class="continuation">Begeleide inoefening · vervolg</div>')+
ex('De vloer stap voor stap','Lᵥ = 180 − 6w en Lₐ = −12 + 6w. L is het aantal personen met 20 uur per week; w is het uurloon in euro. Gebruik € 2 ≤ w ≤ € 30. Het vrije evenwicht is € 16 en 84 personen. Alle gevraagde plaatsen worden gevuld. Een minimum van € 18 wordt ingevoerd.',[
('Toets de bindendheid en bereken Lᵥ en Lₐ bij het minimum.',ans('€ 18 > € 16: <b>bindend</b>. Lᵥ = 180 − 6 × 18 = <b>72</b>. Lₐ = −12 + 6 × 18 = <b>96 personen</b>.','De ondergrens ligt boven het vrije evenwichtsloon.')),
('Bereken de werkgelegenheid, het aanbodoverschot en de nieuwe loonsom.',ans('Werkgelegenheid = <b>72 personen</b>. Overschot = 96 − 72 = <b>24 personen</b>. Loonsom = € 18 × 20 × 72 = <b>€ 25.920 per week</b>.','Je gebruikt de daadwerkelijk gevulde plaatsen voor de loonsom.'))],answer_fig='floor_guide_answer')+heading('Zelfstandige oefening')+
ex('Een andere reactie','In een cateringmarkt geldt Lᵥ = 140 − 2w en Lₐ = 5w, met L in personen en w in euro per uur. Iedereen werkt 20 uur per week. Het vrije evenwicht is € 20 en 100 personen. Alle gevraagde plaatsen worden gevuld. Het minimum wordt € 22.',[
('Bereken werkgelegenheid, aanbodoverschot en loonsom bij de vloer. Vergelijk met de oude loonsom.',ans('Lᵥ = 140 − 2 × 22 = <b>96 personen</b>; Lₐ = 5 × 22 = <b>110 personen</b>. Overschot = <b>14 personen</b>. Nieuw: 22 × 20 × 96 = <b>€ 42.240 per week</b>. Oud: 20 × 20 × 100 = <b>€ 40.000 per week</b>. Stijging: <b>€ 2.240</b>.','Hier daalt betaald werk relatief weinig, zodat de loonsom stijgt.'))])+ 
ex('Een minimum onder de markt','In een aparte markt is het vrije evenwicht € 24 per uur met 60 werkenden. Het minimumloon wordt € 21. Alle overige omstandigheden blijven gelijk.',[
('Welk loon en welke werkgelegenheid verwacht je volgens het model? Licht toe.',ans('<b>€ 24 per uur en 60 werkenden</b>. De vloer is niet-bindend, omdat het vrije loon erboven ligt.','Een minimum is een ondergrens, geen verplichte prijs.'))]))
page('Doeloefening',heading('Doeloefening')+
ex('Een loonvloer in de sorteercentra','Lᵥ = 220 − 10w en Lₐ = −20 + 10w, voor € 2 ≤ w ≤ € 22. L is het aantal personen met ieder 25 betaalde uren per week; w is het brutouurloon in euro. Een fictief minimumloon wordt € 14. Werkgevers concurreren; er zijn geen vacatures of zoekproblemen. Alle gevraagde plaatsen worden gevuld. Alle aanbieders zonder baan zoeken en zijn direct beschikbaar.',[
('Bereken het vrije evenwicht en bepaal of de loonvloer bindend is.',ans('220 − 10w = −20 + 10w → 240 = 20w → <b>w = € 12</b>. L = 220 − 10 × 12 = <b>100 personen</b>. € 14 > € 12: <b>bindend</b>.','De loonvloer sluit het vrije evenwicht uit.')),
('Bereken bij de loonvloer arbeidsvraag, arbeidsaanbod, werkgelegenheid en aanbodoverschot. Geef de loonvloer en beide hoeveelheden aan in de basisgrafiek.',ans('Lᵥ = 220 − 140 = <b>80</b>; Lₐ = −20 + 140 = <b>120 personen</b>. Werkgelegenheid = <b>80</b>; overschot = 120 − 80 = <b>40 personen</b>.','De aangeboden 120 banen aan arbeid worden niet alle door werkgevers gevraagd.')),
('Bereken de loonsom vóór en na de verandering en de procentuele verandering.',ans('Oud = 12 × 25 × 100 = <b>€ 30.000 per week</b>. Nieuw = 14 × 25 × 80 = <b>€ 28.000 per week</b>. (28.000 − 30.000) / 30.000 × 100% ≈ <b>−6,67%</b>.','De stijging van het uurloon compenseert hier de afname van betaalde uren niet.')),
('Leg uit waarom “alle 40 hebben hun baan verloren” en “iedereen verdient meer” geen juiste conclusies zijn.',ans('Er zijn <b>20 minder werkenden</b> en <b>20 extra aanbieders</b>. Samen vormen zij het verschil van 40. Alleen wie werk houdt en dezelfde uren werkt, krijgt het hogere weekloon.','Aanbodoverschot, banenverlies en inkomenswinst zijn verschillende grootheden.'))],points=[2,3,3,2],answer_fig='floor_target_answer')+
fig('floor_target','De vraag- en aanbodlijn zijn gegeven. Vul de loonvloer, vraag en aanbod aan; teken de lijnen niet opnieuw.'))
page('Denkertje en herhaling',heading('Denkertje / Bonusopgave')+
ex('Een hoger loon, minder uren per persoon','Een werknemer krijgt eerst € 16 per uur en werkt 25 uur per week. Later krijgt deze werknemer € 18 per uur maar werkt 20 uur. Deze verandering geldt voor alle werknemers; hun aantal blijft gelijk.',[
('Beoordeel welke uitspraken juist zijn: het uurloon stijgt, het weekloon stijgt, de werkgelegenheid in personen daalt, de arbeidsinzet in uren daalt. Leg uit waarom de eenheid ertoe doet.',
'Het uurloon stijgt. Het weekloon daalt van 16 × 25 = € 400 naar 18 × 20 = € 360. De werkgelegenheid in personen blijft gelijk, maar het aantal gewerkte uren daalt. Een hogere prijs per uur zegt dus niet genoeg over het inkomen per week.<br><b>Beoordelingscriteria:</b> rekent beide weeklonen juist; houdt personen gelijk; onderscheidt uren van personen en uurloon van weekloon.')])+heading('Herhaling / Herhaling en interleaving')+
ex('Productiviteit blijft nodig','Een producent maakt 4.800 producten in 800 arbeidsuren. De volledige uurkosten zijn € 27.',[
('Bereken de arbeidsproductiviteit en loonkosten per product.',ans('Productiviteit = 4.800 / 800 = <b>6 producten per uur</b>. Loonkosten = € 27 / 6 = <b>€ 4,50 per product</b>.','Een uurkost moet je over de productie in dat uur verdelen. Herhaal bij moeite §4.3.1.'))])+
box('Terugblik','Bij een loonmaatregel reken je niet alleen met het uurloon. Je controleert ook betaald werk, aangeboden arbeid, arbeidsduur en de totale loonsom.','summary'))
