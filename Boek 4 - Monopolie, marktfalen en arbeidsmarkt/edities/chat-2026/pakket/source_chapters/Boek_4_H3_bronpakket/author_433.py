from author_common import *
section('4.3.3')
page('Werkloos: kies de juiste noemer',begin('Vacatures én werklozen. Hoe kan dat?',
'Je kunt het werkloosheidspercentage berekenen. Je kunt oorzaken van werkloosheid onderscheiden. Je kunt een verschuiving van arbeidsvraag verwerken en uitleggen waarom een model niet alle waargenomen werkloosheid beschrijft.',
'Een regio telt honderd werklozen, terwijl werkgevers zestig mensen zoeken. Is de werkloosheid dan eigenlijk maar veertig? Nee. Een openstaande baan is nog niet door een werkloze vervuld.')+
formula('werklozen = beroepsbevolking − werkenden<br>werkloosheidspercentage = werklozen / beroepsbevolking × 100%')+
'''Bij 900 werkenden en 100 werklozen is de beroepsbevolking 1.000 personen. Het werkloosheidspercentage is 100 / 1.000 × 100% = **10%**. De noemer is nu niet de hele bevolking.

'''+fig('vacancy_overlap','Een fictieve bron telt één baan per werkende en één persoon per vacature. De 900 werkenden komen in beide tellingen voor.')+
'''In deze bron is arbeidsvraag = werkgelegenheid + vacatures = 900 + 60 = 960 arbeidsplaatsen. Arbeidsaanbod = beroepsbevolking = 1.000 personen.

Maar aanbod − vraag = 1.000 − 960 = 40 is **niet** het aantal werklozen. Je hebt dan vacatures van werklozen afgetrokken. Er zijn nog steeds 100 mensen zonder werk die zoeken en beschikbaar zijn.
'''+box('Gelijke eenheden zijn nodig','In werkelijke bronnen kunnen banen en personen verschillen: één persoon kan meer banen hebben. Onze rekenvoorbeelden melden daarom expliciet wanneer één persoon bij één baan hoort.','warning'))
page('Verschillende oorzaken', '''### Minder bestedingen, andere productie of zoektijd?
Bij **conjuncturele werkloosheid** is er minder vraag naar goederen en diensten. Huishoudens of bedrijven besteden minder. Bedrijven krijgen minder opdrachten en hebben daardoor minder personeel nodig. Het probleem is hier niet dat iedereen plotseling de verkeerde opleiding heeft.

Bij **structurele werkloosheid** past de beschikbare arbeid niet goed bij het werk dat gevraagd wordt. Techniek kan beroepen veranderen. Een regio kan veel werkzoekenden hebben, terwijl passende banen ergens anders liggen. Scholing en verhuizing kosten tijd en geld.

**Frictiewerkloosheid** ontstaat doordat het tijd kost om een passende baan en werknemer te vinden. Iemand kan tussen twee banen zitten, zonder dat er te weinig banen voor zijn beroep zijn. We rekenen deze zoektijd hier tot structurele werkloosheid.

'''+fig('unemployment_causes','De bron moet de oorzaak ondersteunen. “Lang werkloos” of “weinig vacatures” is op zichzelf nog geen volledige verklaring.')+
'''### Waarom vallen vacatures en werklozen niet direct samen?
Een installateur zoekt een ervaren elektricien. Een werkloze kandidaat heeft ervaring als winkelmedewerker. Er is een vacature én iemand zoekt werk, maar er is nog geen passende match. Ook reistijd, werktijden en informatie kunnen een match in de weg staan.

Een hoog totaal aantal vacatures bewijst daarom niet dat iedere werkzoekende direct kan beginnen. Evenmin betekent ieder langdurig werkloosheidsgeval automatisch dat het conjunctureel is.
'''+box('Benoem een mechanisme','Schrijf bijvoorbeeld: “Minder consumentenbestedingen → minder winkelverkopen → minder vraag naar winkelpersoneel.” Het woord conjunctureel alleen verklaart nog niets.','summary'))
page('Een verschuiving bij flexibel loon', '''### Minder opdrachten verschuiven de arbeidsvraag
We gebruiken opnieuw het bekende marktmodel. De lijnen tonen verbanden bij verder gelijke omstandigheden. De aanbodlijn blijft nu gelijk; door minder bestedingen daalt de arbeidsvraag bij ieder loon.

Oud: **Lᵥ = 200 − 10w**. Nieuw: **Lᵥ = 160 − 10w**.<br>
Aanbod: **Lₐ = −40 + 10w**. L is het aantal personen met ieder 20 uur per week; w is het uurloon in euro. We gebruiken € 4 ≤ w ≤ € 16. Het loon kan vrij aanpassen, zonder vacatures of zoekproblemen.

'''+fig('shift_flex','E₀ is het oude evenwicht: € 12 en 80 personen. Na de daling van de arbeidsvraag ligt E₁ bij € 10 en 60 personen.')+
'''Nieuwe vergelijking: 160 − 10w = −40 + 10w → 200 = 20w → **w = € 10**.<br>
Invullen: L = 160 − 10 × 10 = **60 personen**.

De nieuwe evenwichtswerkgelegenheid is lager. Toch is er in dit eenvoudige model geen aanbodoverschot bij het nieuwe loon. Bij € 10 willen minder personen arbeid aanbieden dan bij € 12. Gevraagde en aangeboden hoeveelheid zijn nu beide 60.

Dat betekent niet dat iedereen in de echte regio onmiddellijk werk vindt. Het model laat zoekproblemen, verschillen in vaardigheden en vaste afspraken weg.
'''+box('Geen dubbele verschuiving','De arbeidsvraaglijn verschuift naar links. Het dalende loon veroorzaakt een <b>beweging langs de gelijk gebleven aanbodlijn</b>. Een nieuwe evenwichtsprijs is niet automatisch een verschuiving van beide lijnen.','warning'))
page('Hetzelfde verlies aan vraag, maar vast loon', '''### Het loon daalt niet meteen
Veronderstel nu dat in precies dezelfde sector het uurloon voorlopig **€ 12 blijft**. Dat kan bijvoorbeeld door bestaande loonafspraken. We gebruiken dezelfde nieuwe arbeidsvraag en dezelfde aanbodlijn als op de vorige pagina.

Vraag bij € 12: 160 − 10 × 12 = **40 personen**.<br>
Aanbod bij € 12: −40 + 10 × 12 = **80 personen**.

'''+fig('shift_fixed','Bij het vastgehouden loon ligt de nieuwe vraag bij 40 en het aanbod bij 80 personen. Het horizontale verschil is 40 personen.')+
'''Er zijn in dit model geen vacatures, geen zoekproblemen en geen tweede baan per persoon. Alle 40 gevraagde plaatsen worden gevuld. De overige 40 aanbieders willen werken, zoeken werk en zijn beschikbaar, maar vinden hier geen baan.

Vergelijk de twee situaties. Bij een flexibel loon ontstaat € 10 met 60 werkenden. Bij een loon dat € 12 blijft, zijn er 40 werkenden en 40 niet-geplaatste aanbieders. Hetzelfde verschil in opdrachten krijgt dus een andere uitkomst door de **loonaanpassing**.

### Wat mag je concluderen?
Je kunt de uitkomst onder beide aannames berekenen. Je kunt uit deze berekening niet bewijzen dat werkelijke lonen direct dalen of dat alle echte werkloosheid door vaste lonen ontstaat.
'''+box('Telling of model?','In een waarneming tel je werklozen rechtstreeks of als beroepsbevolking min werkenden. Alleen onder de expliciete modelvoorwaarden zonder vacatures of mismatch mag je het arbeidsaanbodoverschot als modelwerkloosheid lezen.','summary'))
page('Uitgewerkt voorbeeld',heading('Uitgewerkt voorbeeld')+
source('Minder evenementen','Een regio telt 1.840 werkenden en 160 werklozen. Er zijn 90 vacatures; elke werkende heeft precies één baan. In een aparte evenementenmarkt daalt de arbeidsvraag van Lᵥ = 200 − 8w naar Lᵥ = 168 − 8w. Het aanbod blijft Lₐ = −24 + 8w. L is het aantal personen, w het uurloon in euro; € 3 ≤ w ≤ € 21. Het oude evenwicht is w = € 14 en L = 88. Consumenten besparen op evenementen.')+
'''### 1 · Bereken de waargenomen werkloosheid
Beroepsbevolking = 1.840 + 160 = **2.000 personen**.<br>
Werkloosheidspercentage = 160 / 2.000 × 100% = **8%**.

Arbeidsvraag = 1.840 + 90 = **1.930 arbeidsplaatsen**. Het verschil van 70 is werklozen min vacatures, niet de werkloosheid.

### 2 · Noem de oorzaak en de verschuiving
Minder bestedingen → minder evenementen → minder arbeidsvraag. Dit is **conjunctureel**. Vraag verschuift naar links; aanbod blijft gelijk.

### 3 · Bereken het nieuwe evenwicht bij flexibel loon
168 − 8w = −24 + 8w → 192 = 16w → **w = € 12**.<br>
L = 168 − 8 × 12 = **72 personen**.

### 4 · Vergelijk met voorlopig vast loon
Bij € 14: Lᵥ = 168 − 8 × 14 = **56** en Lₐ = −24 + 8 × 14 = **88 personen**. Zonder vacatures of zoekproblemen worden 56 plaatsen gevuld en is het aanbodoverschot **32 personen**.

De sectorgrafiek vervangt niet de aparte regiotelling.
'''+box('Samenvatting §4.3.3','Werkloosheid gebruikt de beroepsbevolking als noemer. Trek vacatures niet af. Benoem oorzaak en loonaanpassing. Houd model en waarneming gescheiden. In §4.3.4 voegen we een minimumloon toe.','summary'))
page('Start en een oorzaak herkennen',start()+
ex('Terug naar de groepen','Een gemeente telt 4.000 inwoners van 15 tot 75 jaar. Er zijn 2.400 werkenden en 400 werklozen.',[
('Bereken de beroepsbevolking en de bruto-participatie.',ans('Beroepsbevolking = 2.400 + 400 = <b>2.800 personen</b>. Bruto = 2.800 / 4.000 × 100% = <b>70%</b>.','Bruto-participatie gebruikt alle inwoners in de opgegeven leeftijdsgroep als noemer.'))])+ 
ex('Een andere noemer','In een andere regio is 6% van de bevolking werkloos. De bruto-participatie is 60%.',[
('Is het werkloosheidspercentage automatisch 6%? Leg uit zonder het precieze percentage te hoeven berekenen.',ans('Nee. Het werkloosheidspercentage deelt werklozen door de beroepsbevolking, niet door alle inwoners.','Dezelfde teller kan met een andere noemer een ander percentage geven.')),
('Een andere werkzoekende is tussen twee banen drie weken op zoek. De vaardigheden sluiten aan bij openstaande vacatures. Welk type werkloosheid past hierbij?',ans('Frictiewerkloosheid: het kost tijd om een passende werkgever en werknemer bij elkaar te brengen.','De bron wijst op zoektijd, niet op te weinig bestedingen of verdwenen vaardigheden.'))])+guided()+
ex('Een vervulde baan ontbreekt nog','Een klein gebied telt 450 werkenden, 50 werklozen en 30 vacatures. Iedereen heeft hoogstens één baan. Een vacature past niet bij iedere werkzoekende.',[
('Bereken eerst de beroepsbevolking en daarna het werkloosheidspercentage.',ans('Beroepsbevolking = 450 + 50 = <b>500 personen</b>. Werkloosheid = 50 / 500 × 100% = <b>10%</b>.','De 30 vacatures zijn nog niet vervuld en veranderen de telling van 50 werklozen niet.')),
('Een leerling rekent (500 − 480) / 500 × 100% = 4%. Wat trekt die leerling ten onrechte af?',ans('De leerling trekt via de arbeidsvraag van 480 ook de <b>30 vacatures</b> van de 50 werklozen af.','Arbeidsvraag = 450 werkenden + 30 vacatures; het verschil is niet de werkloosheid.'))]))
page('Van oorzaak naar uitkomst',guided().replace('## Begeleide inoefening','<div class="continuation">Begeleide inoefening · vervolg</div>')+
ex('Wat verandert er?', 'Een reisbureau krijgt minder boekingen doordat huishoudens minder besteden. In zijn arbeidsmarkt blijft het loon eerst gelijk.',[
('Noem de oorzaak van werkloosheid die bij de bron past en maak de keten af: minder bestedingen → … → minder vraag naar arbeid.',ans('Een conjuncturele oorzaak. Minder bestedingen → minder reisboekingen → minder werk voor het reisbureau → minder vraag naar arbeid.','De bron beschrijft een daling van de vraag naar eindproducten.')),
('Welke lijn verschuift en welke druk op loon en werkgelegenheid ontstaat als het loon later wel kan dalen?',ans('De arbeidsvraag verschuift naar links. In het eenvoudige model ontstaat neerwaartse loondruk en een lagere evenwichtswerkgelegenheid.','Bij een lager loon beweeg je langs de onveranderde aanbodlijn.'))])+heading('Zelfstandige oefening')+
ex('Werk en techniek','Een provincie heeft 4.500 werkenden en 500 werklozen. Een deel van de werklozen deed invoerwerk dat nu door software wordt uitgevoerd. Nieuwe vacatures vragen andere vaardigheden.',[
('Bereken het werkloosheidspercentage en benoem de best passende oorzaak voor de beschreven groep.',ans('Beroepsbevolking = 4.500 + 500 = <b>5.000 personen</b>. Werkloosheid = 500 / 5.000 × 100% = <b>10%</b>. De beschreven groep heeft een <b>structurele</b> oorzaak: ander werk vraagt andere vaardigheden.','De bron wijst op een verandering in techniek en aansluiting van vaardigheden, niet op lagere totale bestedingen.'))])+ 
ex('Minder schoonmaakopdrachten','Oud: Lᵥ = 180 − 5w. Nieuw: Lᵥ = 160 − 5w. Aanbod blijft Lₐ = −20 + 5w. L is het aantal personen; w is het uurloon in euro. Gebruik € 4 ≤ w ≤ € 32. Oud evenwicht: € 20 en 80 personen. Loon is vrij aanpasbaar; er zijn geen vacatures of zoekproblemen.',[
('Bereken het nieuwe evenwicht. Benoem één verschuiving en één beweging langs een lijn.',ans('160 − 5w = −20 + 5w → 180 = 10w → <b>w = € 18</b>. L = 160 − 5 × 18 = <b>70 personen</b>. Vraag verschuift naar links; het lagere loon geeft een beweging langs aanbod naar minder aanbod.','De aanbodfunctie blijft gelijk.')),
('Bereken het aanbodoverschot als het loon toch € 20 blijft.',ans('Lᵥ = 160 − 100 = <b>60 personen</b>. Lₐ = −20 + 100 = <b>80 personen</b>. Overschot = 80 − 60 = <b>20 personen</b>.','Bij het vastgehouden loon wordt de nieuwe vraag niet door loonaanpassing in evenwicht gebracht.'))],answer_fig='shift_ind_answer'))
page('Doeloefening',heading('Doeloefening')+
ex('Rivierenregio: cijfers en een sector','Bron A: de regio telt 2.700 werkenden, 300 werklozen en 120 vacatures. Iedere werkende heeft één baan.<br>Bron B: in een afzonderlijke sector nemen de opdrachten af doordat huishoudens minder besteden. Lᵥ daalt van 180 − 6w naar 144 − 6w; Lₐ blijft −12 + 6w. L is het aantal personen; w is het uurloon in euro; € 2 ≤ w ≤ € 24. Het oude evenwicht is € 16 en 84 personen. Er zijn in dit sector-model geen vacatures of zoekproblemen.',[
('Bereken met bron A het werkloosheidspercentage. Leg uit waarom arbeidsaanbod min arbeidsvraag hier niet de werkloosheid geeft.',ans('Beroepsbevolking = 2.700 + 300 = <b>3.000 personen</b>. Werkloosheid = 300 / 3.000 × 100% = <b>10%</b>. Arbeidsvraag = 2.700 + 120 = 2.820; het verschil 180 is 300 − 120, niet de 300 werklozen.','Vacatures zijn nog niet ingevuld.')),
('Benoem met bron B de oorzaak en bereken het nieuwe evenwicht als het loon vrij aanpast.',ans('Conjuncturele oorzaak: minder bestedingen verlagen opdrachten en arbeidsvraag. 144 − 6w = −12 + 6w → 156 = 12w → <b>w = € 13</b>. L = 144 − 6 × 13 = <b>66 personen</b>.','De oude evenwichtswerkgelegenheid van 84 daalt; dit is geen berekening van alle werklozen in de regio.')),
('Markeer het oude en nieuwe evenwicht in de basisgrafiek. Bereken daarna het aanbodoverschot bij een loon dat € 16 blijft.',ans('E₀ = (84;16), E₁ = (66;13). Bij € 16: Lᵥ = 144 − 96 = <b>48</b>, Lₐ = −12 + 96 = <b>84 personen</b>. Overschot = <b>36 personen</b>.','Een gelijkblijvend loon en een flexibel loon leveren niet dezelfde sectoruitkomst op.'))],points=[3,3,3],answer_fig='shift_target_answer')+
fig('shift_target','De oude en nieuwe vraaglijn en de aanbodlijn zijn gegeven. Voeg alleen E₀ en E₁ toe.'))
page('Denkertje en herhaling',heading('Denkertje / Bonusopgave')+
ex('Een dalend percentage zonder extra banen','Een dorp telt eerst 900 werkenden en 100 werklozen. Later stoppen 50 werklozen met zoeken. Zij hebben geen betaald werk en horen nu bij de niet-beroepsbevolking. Er komt geen baan bij.',[
('Beoordeel: “De lagere werkloosheid bewijst dat meer mensen werk hebben.” Gebruik zowel aantallen als percentages.',
'Eerst is de beroepsbevolking 1.000 en het werkloosheidspercentage 100 / 1.000 × 100% = 10%. Later zijn er 900 werkenden en 50 werklozen: beroepsbevolking 950; werkloosheidspercentage 50 / 950 × 100% ≈ 5,26%. Het aantal werkenden blijft 900. De daling komt door uitstroom uit de beroepsbevolking, niet door extra banen.<br><b>Beoordelingscriteria:</b> verandert zowel teller als noemer; houdt werkenden op 900; onderscheidt stoppen met zoeken van een baan vinden.')])+heading('Herhaling / Herhaling en interleaving')+
ex('Marginale opbrengst uit hoofdstuk 4.1','Een onderneming heeft P = 30 − 0,5q en TK = 6q + 100. P is euro per product, q producten per week. De gevraagde hoeveelheid is niet negatief.',[
('Bepaal TO en MO.',ans('TO = P × q = (30 − 0,5q)q = <b>30q − 0,5q²</b>, in euro per week. MO = <b>30 − q</b>, in euro per extra product.','Bij een uniforme lagere prijs verandert ook de opbrengst op eerdere eenheden. Herhaal bij moeite §4.1.2.'))])+
box('Terugblik','Een cijfer wordt pas betekenisvol met de juiste teller, noemer en definitie. Een modeluitkomst vraagt bovendien een expliciete aanname over loonaanpassing.','summary'))
