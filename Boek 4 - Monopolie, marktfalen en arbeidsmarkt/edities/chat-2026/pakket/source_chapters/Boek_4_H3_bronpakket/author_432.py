from author_common import *
section('4.3.2')
page('Wie doet mee?',begin('Geen baan. Ook werkloos?',
'Je kunt werkenden, werklozen en niet-deelnemers onderscheiden. Je kunt bruto- en netto-arbeidsparticipatie berekenen. Je kunt met een bekend marktmodel het evenwichtsloon en de werkgelegenheid vinden.',
'Noor heeft een betaalde bijbaan. Amir heeft geen werk, zoekt actief en kan direct beginnen. Tess heeft geen baan en zoekt er ook geen. Alle drie zijn 17. Toch tellen ze niet op dezelfde manier mee.')+
box('Definitie · beroepsbevolking','De mensen die betaald werk hebben, plus de mensen zonder betaald werk die recent werk hebben gezocht en direct beschikbaar zijn. De eerste groep is de werkzame beroepsbevolking; de tweede de werkloze beroepsbevolking.','definition')+
fig('population','Een fictieve bevolking van 1.000 personen: 700 behoren tot de beroepsbevolking. De 100 werklozen zitten al in die 700.')+
'''De **niet-beroepsbevolking** bestaat uit mensen zonder betaald werk die niet recent hebben gezocht of niet direct beschikbaar zijn. Geen baan hebben is dus niet voldoende om als werkloos te tellen.

Noor telt als werkzaam, ook met weinig betaalde uren. Amir telt als werkloos. Tess behoort tot de niet-beroepsbevolking. Een leerling of student kan dus in elk van deze groepen vallen.

We gebruiken in de bevolkingsbronnen steeds **15 tot 75 jaar**: 15-jarigen wel, 75-jarigen niet. De definitie van de groepen en de gekozen leeftijdsgrens sluiten aan bij de CBS-begrippen. De cijfers zijn voor dit boek bedacht.
''')
page('Participatie: kies de juiste teller', '''### Hoe groot is het aandeel dat meedoet?
**Arbeidsparticipatie** gaat over deelname aan de arbeidsmarkt. Bij bruto-participatie tel je werkenden én werklozen. Bij netto-participatie tel je alleen mensen met betaald werk. Voor beide gebruik je dezelfde bevolking als noemer.

'''+formula('bruto-participatie = beroepsbevolking / bevolking × 100%<br>netto-participatie = werkenden / bevolking × 100%')+
'''In de figuur op de vorige pagina is de bevolking 1.000 personen. De beroepsbevolking is 600 + 100 = 700 personen.

Bruto-participatie = 700 / 1.000 × 100% = **70%**.<br>
Netto-participatie = 600 / 1.000 × 100% = **60%**.

Het verschil van 10 procentpunt is hier het aandeel werklozen **in de hele bevolking**. Het is niet het werkloosheidspercentage. Dat percentage krijgt in §4.3.3 een andere noemer.

### Een waarneming is geen aanbodlijn
De telling zegt hoeveel mensen in een regio op dit moment meedoen. Een **arbeidsaanbodlijn** toont hoeveel arbeid huishoudens bij verschillende lonen willen aanbieden, terwijl de andere omstandigheden gelijk blijven.

In ons model loopt de aanbodlijn op. Een hoger loon kan meer mensen aantrekken of mensen meer uren laten aanbieden. Hoe mensen reageren hangt ook af van beschikbare tijd, zorgtaken, opleiding en voorkeuren. We gebruiken de stijgende lijn als vereenvoudiging voor de onderzochte markt.

Meer beschikbare gekwalificeerde werknemers kunnen de aanbodlijn naar rechts verschuiven. Een verandering van alleen het loon is juist een beweging langs die lijn.
'''+box('Tel geen groepen dubbel','Beroepsbevolking = werkenden + werklozen. Voeg de werklozen niet nogmaals toe aan een al gegeven beroepsbevolking. Houd bevolkingscijfers en een aparte sectorberekening uit elkaar.','warning'))
page('Evenwicht: nieuwe namen, bekende methode', '''### Van productprijs naar uurloon
Bij een gewone markt stelde je gevraagde en aangeboden hoeveelheid aan elkaar gelijk. Hier doe je hetzelfde. Alleen de economische betekenis en eenheden veranderen.

'''+table(['Bekende markt','Arbeidsmarkt'],[['Prijs P','Uurloon w'],['Gevraagde hoeveelheid Qᵥ','Arbeidsvraag Lᵥ door werkgevers'],['Aangeboden hoeveelheid Qₐ','Arbeidsaanbod Lₐ door huishoudens'],['Qᵥ = Qₐ','Lᵥ = Lₐ']])+
'''In een kleine voorbeeldsector geldt **Lᵥ = 180 − 10w** en **Lₐ = −20 + 10w**. L is het aantal personen; iedereen biedt één baan met 20 uur per week aan. w is het loon in euro per uur. We gebruiken deze functies voor € 2 ≤ w ≤ € 18.

Gelijkstellen: 180 − 10w = −20 + 10w → 200 = 20w → **w = € 10 per uur**.

Invullen: L = 180 − 10 × 10 = **80 personen**. Controle: −20 + 10 × 10 = 80 personen.

'''+fig('eq_intro','Het snijpunt E geeft het evenwichtsloon en de werkgelegenheid. Loon staat verticaal; de hoeveelheid arbeid staat horizontaal.')+
box('De modelafspraak','Er zijn veel werkgevers en werknemers, vergelijkbare arbeid en geen loonvloer. Het loon kan zich aanpassen. Iedereen vindt direct een passende werkgever of werknemer. Daardoor worden in het evenwicht alle aangeboden arbeidsplaatsen gevuld. Dit is niet een beschrijving van elke werkelijke arbeidsmarkt.','summary'))
page('Uitgewerkt voorbeeld',heading('Uitgewerkt voorbeeld')+
source('Regio en voorbeeldsector','Een fictieve regio heeft 2.000 inwoners van 15 tot 75 jaar: 1.260 werken, 140 zijn werkloos en 600 behoren niet tot de beroepsbevolking. Een <b>aparte</b> sector heeft Lᵥ = 160 − 5w en Lₐ = −20 + 5w. L is het aantal personen met elk 20 uur per week; w is het uurloon in euro. Het model geldt voor € 4 ≤ w ≤ € 32 en kent vrije loonaanpassing zonder zoekproblemen.')+
'''### 1 · Stel de groepen vast
Beroepsbevolking = werkenden + werklozen = 1.260 + 140 = **1.400 personen**. Controle: 1.400 + 600 = 2.000 personen.

### 2 · Bereken de deelname
Bruto: 1.400 / 2.000 × 100% = **70%**.<br>
Netto: 1.260 / 2.000 × 100% = **63%**.

### 3 · Stel in de sector vraag en aanbod gelijk
160 − 5w = −20 + 5w → 180 = 10w → **w = € 18 per uur**.<br>
L = 160 − 5 × 18 = **70 personen**. Controle: −20 + 5 × 18 = 70.

De werkgevers vragen bij dit loon arbeid van 70 personen. Huishoudens bieden bij dit loon arbeid van 70 personen aan. De werkgelegenheid in dit model is dus 70 personen, niet de 1.400 uit de regiotelling.

'''+fig('eq_we','Gebruik het loon uit het snijpunt. De horizontale hoeveelheid blijft een aantal personen, niet een geldbedrag.')+
box('Samenvatting §4.3.2','Kies eerst groep en leeftijdsbereik. Bruto telt werkenden én werklozen; netto alleen werkenden. Deel door de aangegeven bevolking. Vind het model-evenwicht met Lᵥ = Lₐ en controleer door invullen. In §4.3.3 kijken we naar werkloosheid en veranderingen.','summary'))
page('Start en groepen herkennen',start()+
ex('Een bekende markt','Voor een product geldt Qᵥ = 120 − 4P en Qₐ = 20 + P. P is euro per product en Q is producten per week.',[
('Bereken de evenwichtsprijs en -hoeveelheid.',ans('120 − 4P = 20 + P → 100 = 5P → <b>P = € 20</b>. Q = 120 − 4 × 20 = <b>40 producten per week</b>.','Het evenwicht ligt waar gevraagde en aangeboden hoeveelheid gelijk zijn.')),
('Bereken hoeveel procent 72 is van 120.',ans('72 / 120 × 100% = <b>60%</b>.','Het gevraagde aandeel bepaalt de teller; het totaal is de noemer.'))])+
ex('Zoeken én beschikbaar zijn','Lina heeft betaald werk. Mo heeft geen betaald werk, zoekt en kan direct beginnen. Bo heeft geen werk en is niet beschikbaar.',[
('Deel de drie personen in: werkzaam, werkloos of niet-beroepsbevolking.',ans('Lina: <b>werkzaam</b>. Mo: <b>werkloos</b>. Bo: <b>niet-beroepsbevolking</b>.','Voor werkloos tellen zijn zowel recent zoeken als directe beschikbaarheid nodig, naast geen betaald werk.'))])+guided()+
ex('Dezelfde bevolking, twee percentages','Een wijk telt 800 inwoners van 15 tot 75 jaar. Er zijn 480 werkenden, 80 werklozen en 240 niet-deelnemers.',[
('Bereken eerst de beroepsbevolking. Welke twee groepen tel je op?',ans('480 werkenden + 80 werklozen = <b>560 personen</b>.','Beide groepen nemen deel aan de arbeidsmarkt.')),
('Bereken bruto- en netto-participatie. Gebruik voor beide de 800 inwoners als noemer.',ans('Bruto = 560 / 800 × 100% = <b>70%</b>. Netto = 480 / 800 × 100% = <b>60%</b>.','Bruto en netto verschillen in de teller, niet in de noemer.'))])+ex('Vul de evenwichtsroute aan','Een arbeidsmarkt heeft Lᵥ = 140 − 5w en Lₐ = −20 + 5w. L is het aantal personen; w is het uurloon in euro. Gebruik € 4 ≤ w ≤ € 28 en vrije loonaanpassing.',[
('Vul eerst de ontbrekende waarden in: 140 − 5w = −20 + 5w → … = 10w → w = … → L = … .',ans('160 = 10w → <b>w = € 16 per uur</b>. L = 140 − 5 × 16 = <b>60 personen</b>. Controle aanbod: −20 + 5 × 16 = 60.','Dezelfde vergelijking als op de goederenmarkt krijgt een loon- en arbeidsinterpretatie.')),
('Wie vragen deze 60 eenheden arbeid en wie bieden ze aan?',ans('Werkgevers vragen de arbeid van 60 personen. Huishoudens bieden die arbeid aan.','De werkgever koopt arbeid, niet de werknemer.'))]))
page('Van steun naar zelfstandig',heading('Zelfstandige oefening')+
ex('Participatie in een dorp','Een dorp heeft 1.200 inwoners van 15 tot 75 jaar. 720 hebben betaald werk; 120 hebben geen werk, hebben recent gezocht en zijn direct beschikbaar. De rest werkt niet en zoekt niet.',[
('Bereken de beroepsbevolking en beide participatiepercentages.',ans('Beroepsbevolking = 720 + 120 = <b>840 personen</b>. Bruto = 840 / 1.200 × 100% = <b>70%</b>. Netto = 720 / 1.200 × 100% = <b>60%</b>.','Werklozen tellen wel mee in bruto-participatie, maar niet in netto-participatie.'))])+ 
ex('De markt voor magazijnmedewerkers','Lᵥ = 200 − 8w en Lₐ = −24 + 8w. L is het aantal personen met ieder 20 uur per week; w is het uurloon in euro. De functies gelden voor € 3 ≤ w ≤ € 25. Loon past vrij aan en alle matches komen direct tot stand.',[
('Bereken het evenwichtsloon en de werkgelegenheid. Markeer het punt E in de basisgrafiek hieronder.',ans('200 − 8w = −24 + 8w → 224 = 16w → <b>w = € 14 per uur</b>. L = 200 − 8 × 14 = <b>88 personen</b>. E ligt bij (L = 88; w = 14).','Beide lijnen geven bij dit loon dezelfde hoeveelheid; het model veronderstelt dat de banen worden gevuld.'))],answer_fig='eq_ind_answer')+fig('eq_base','Basisgrafiek bij opgave 15. Voeg E en de bijbehorende hulplijnen toe.'))
# The two supplied bases and target must remain readable on separate designed pages.
page('Doeloefening',heading('Doeloefening')+
ex('Waterstad en de bezorgsector','Bron A: Waterstad telt 5.000 inwoners van 15 tot 75 jaar. Er zijn 3.000 werkenden, 500 werklozen en 1.500 niet-deelnemers.<br>Bron B: een afzonderlijk model voor bezorgers geeft Lᵥ = 240 − 10w en Lₐ = −40 + 10w. L is het aantal personen met 20 uur per week; w is het uurloon in euro. Het model geldt voor € 4 ≤ w ≤ € 24. Het loon is flexibel; er zijn geen zoekproblemen of loonafspraken.',[
('Bereken met bron A de beroepsbevolking en de bruto- en netto-participatie.',ans('Beroepsbevolking = 3.000 + 500 = <b>3.500 personen</b>. Bruto = 3.500 / 5.000 × 100% = <b>70%</b>. Netto = 3.000 / 5.000 × 100% = <b>60%</b>.','De 5.000 inwoners zijn voor beide percentages de noemer.')),
('Bereken met bron B het evenwichtsloon en de werkgelegenheid. Markeer E in de basisgrafiek hieronder.',ans('240 − 10w = −40 + 10w → 280 = 20w → <b>w = € 14 per uur</b>. L = 240 − 140 = <b>100 personen</b>. Controle: −40 + 140 = 100.','Werkgevers en aanbieders stemmen in het model bij dit loon overeen over dezelfde hoeveelheid.')),
('Leg uit wie bij dit loon arbeid vragen en aanbieden. Waarom vervangt de modeluitkomst de regiotelling niet?',ans('Werkgevers vragen arbeid; huishoudens bieden die aan. De 100 personen horen bij een aparte sector en een vereenvoudigd model, niet bij alle inwoners van Waterstad.','Een sectorfunctie en een waargenomen bevolkingsbron beschrijven verschillende objecten.'))],points=[3,3,2],answer_fig='eq_target_answer')+fig('eq_target','Basisgrafiek bij opgave 16. Benoem het berekende evenwicht met loon en hoeveelheid.'))
page('Denkertje en herhaling',heading('Denkertje / Bonusopgave')+
ex('Meer deelname, evenveel werk','In een gebied met 1.000 inwoners van 15 tot 75 jaar werken eerst 600 mensen en zoeken 100 anderen zonder baan actief werk. Later gaan 50 niet-deelnemers ook zoeken en zijn direct beschikbaar. Niemand vindt of verliest werk.',[
('Leg uit wat met bruto- en netto-participatie gebeurt. Beoordeel de uitspraak: “Hogere deelname betekent altijd meer werkenden.”',
'Bruto-participatie stijgt van (600 + 100) / 1.000 × 100% = 70% naar (600 + 150) / 1.000 × 100% = 75%. Netto blijft 600 / 1.000 × 100% = 60%. De uitspraak is onjuist: deelname kan stijgen doordat meer mensen zonder baan gaan zoeken.<br><b>Beoordelingscriteria:</b> houdt de bevolking gelijk; telt zoekenden in bruto; stelt vast dat werkenden en netto-participatie gelijk blijven.')])+heading('Herhaling / Herhaling en interleaving')+
ex('De belastingwig terughalen','Bij een belasting op een product betaalt de koper € 12 en ontvangt de verkoper na afdracht € 9. Er worden 200 producten per week verkocht.',[
('Bereken de belasting per product en de overheidsontvangsten.',ans('Belasting = € 12 − € 9 = <b>€ 3 per product</b>. Ontvangsten = € 3 × 200 = <b>€ 600 per week</b>.','De overheid ontvangt het bedrag over de werkelijk verkochte producten. Herhaal bij moeite §3.1.1.'))])+
box('De volgende stap','Een evenwichtsgrafiek laat een vereenvoudigd mechanisme zien. Werkloosheidscijfers zijn waarnemingen. In §4.3.3 leer je die twee gebruiken zonder ze met elkaar te verwarren.','summary'))
