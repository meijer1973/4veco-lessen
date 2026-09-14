"""Authored student manuscript. The uploaded v2 outlines control scope.
Targets and all numerical cases are original teaching designs, not registry copies.
"""
from pathlib import Path
import json, re
ROOT=Path(__file__).resolve().parent
PAGES=[]; EXERCISES=[]; FIGS={}
def box(title,text,cls=''):
    return f'<div class="box {cls}"><b>{title}</b><br>{text}</div>\n\n'
def form(text):return f'<div class="formula">{text}</div>\n\n'
def fig(name,caption):
    sec='.'.join(name.split('_')[0].split('.')[:3])
    FIGS[sec]=FIGS.get(sec,0)+1
    return f'<figure><img src="_assets/{name}.svg" alt="{caption}"><figcaption>Figuur {FIGS[sec]}. {caption}</figcaption></figure>\n\n'
def ex(n,title,ctx,qs,kind='practice'):
    EXERCISES.append({'number':n,'title':title,'context':ctx,'questions':qs,'kind':kind})
    paras=''.join(f'<p><b>{chr(97+i)}.</b> {t}</p>' for i,t in enumerate(qs))
    return f'<div class="exercise {"target" if kind=="target" else ""}" id="opg{n}"><p><b>Opgave {n} · {title}</b></p><p>{ctx}</p>{paras}</div>\n\n'
def pg(sec,title,body):PAGES.append({'section':sec,'title':title,'body':body.strip()})
ROUTE='<div class="route"><b>Korte route:</b> Startopgaven → Zelfstandige oefening → Doeloefening. Extra hulp nodig? Maak eerst Begeleide inoefening.</div>\n\n'
SKIP='<p class="small">Heb je deze hulp niet nodig? Ga dan verder met Zelfstandige oefening.</p>\n\n'

pg('3.1','Overheidsingrijpen','''<div class="kicker">4VECO · ECONOMIE · 4 VWO · BOEK 3</div>
<div class="cover-title">Overheidsingrijpen</div>
<div class="lead">Wie betaalt, wie profiteert en wat verandert er?</div>

Een belasting maakt een product duurder. Een subsidie maakt het goedkoper. Een maximumprijs lijkt aantrekkelijk voor kopers. Maar wie krijgt het product nog? En wie betaalt de rekening?

Je gebruikt de gereedschappen uit Boek 1 en 2 opnieuw: vraag en aanbod, evenwicht, procenten en surplus. Nieuw is **de manier waarop een maatregel de markt verandert**.

<div class="contents">
<a href="#s311"><b>3.1.1 · Belastingen: wig en nieuw evenwicht <span>2</span></b>De koper betaalt iets anders dan de verkoper overhoudt.</a>
<a href="#s312"><b>3.1.2 · Belastingdruk en welvaartsverlies <span>9</span></b>Verdeel de last en onderscheid belastingopbrengst van verlies.</a>
<a href="#s313"><b>3.1.3 · Subsidies <span>16</span></b>Dezelfde methode, met de geldstroom omgekeerd.</a>
<a href="#s314"><b>3.1.4 · Maximumprijs <span>23</span></b>Een lage toegestane prijs is nog geen aankoopgarantie.</a>
<a href="#s315"><b>3.1.5 · Minimumprijs en quota <span>30</span></b>Een prijsgrens en een hoeveelheidsgrens werken anders.</a>
<a href="#s316"><b>3.1.6 · Gemengde opgaven <span>37</span></b>Kies zelf de methode en onderbouw een beleidsconclusie.</a>
<a href="#overzicht"><b>Hoofdstukoverzicht <span>40</span></b>De belangrijkste begrippen en controles bij elkaar.</a>
</div>

'''+box('Werkwijze','Lees de uitleg en het uitgewerkte voorbeeld. De startopgaven halen benodigde voorkennis op. Begeleide inoefening is extra steun, geen extra verplicht einddoel. Zelfstandige oefening bereidt je voor op de doeloefening. Bonus en herhaling kunnen buiten de les.','goals')+'''
<div class="small muted">Werk in je schrift; gebruik de afgedrukte grafieken waar dat wordt gevraagd. Reken tussendoor ongerond; rond eurobedragen en percentages zo nodig af op twee decimalen. Alle markten, beleidsbronnen en bedragen zijn fictieve oefensituaties, geen actuele belastingregels.</div>
''')

# §3.1.1 — pages 2–8
pg('3.1.1','Eén product, twee prijzen','''<a id="s311"></a>
<div class="kicker">3.1.1 · BELASTINGEN: WIG EN NIEUW EVENWICHT</div>
# Eén product, twee prijzen

Op een kleine markt verkopen verschillende kramen fruitbekers. De overheid voert in deze oefensituatie een belasting van € 4 per verkochte beker in. De verkoper moet die € 4 afdragen.

Betekent dit dat de koper precies € 4 meer gaat betalen? Niet noodzakelijk. De marktprijs kan veranderen en de verkoper kan zelf een deel van de last dragen.

'''+box('Lesdoelen','Je kunt het vrije evenwicht berekenen. Je kunt bij een belasting de kopersprijs, verkopersontvangst en nieuwe hoeveelheid berekenen. Je kunt de belastingwig in een marktgrafiek markeren en uitleggen waarom afdragen niet hetzelfde is als de last dragen.','goals')+'''
### Geef de prijzen een eigen naam

**Pc** is de prijs die de consument betaalt. **Pp** is het bedrag dat de producent per verkocht product overhoudt na afdracht van de belasting, maar **vóór aftrek van zijn productiekosten**. **t** is de belasting per product.

'''+fig('3.1.1_fig_1','Van de € 10 die de koper betaalt, houdt de verkoper € 6 over. De overige € 4 gaat naar de overheid.')+form('Belastingwig: Pc − Pp = t<br>Dus: Pc = Pp + t')+'''
<div class="small">De bedragen in de geldstroom zijn de nieuwe marktuitkomst die we hierna berekenen. Pp is dus géén winst per product.</div>
''')

pg('3.1.1','De markt rekent met beide prijzen','''### Wat blijft hetzelfde?

Kopers reageren op **hun betaalde prijs Pc**. Verkopers reageren op **hun ontvangst Pp**. Bij het nieuwe evenwicht wordt nog steeds evenveel gevraagd als aangeboden. Alleen gebruik je niet meer voor iedereen dezelfde prijs.

Voor fruitbekers geldt:

'''+form('Vraag: Pc = 14 − 0,10Q<br>Aanbod: Pp = 2 + 0,10Q')+'''
Q is het aantal fruitbekers per dag. Pc en Pp zijn euro per beker. Zonder belasting is Pc = Pp. Met t = € 4 wordt de aanbodlijn, uitgedrukt in de **kopersprijs**:

'''+form('Pc = Pp + 4 = 6 + 0,10Q')+'''
### Lees de grafiek in drie stappen

Eerst staan V en A er: het vertrouwde vrije evenwicht. Daarna schuift de aanbodlijn in kopersprijzen € 4 omhoog naar **A + t**. Het snijpunt met V geeft de nieuwe hoeveelheid en Pc. Lees bij **dezelfde Q** op de oorspronkelijke A af wat verkopers ontvangen.

'''+fig('3.1.1_fig_2','Zonder belasting: 60 bekers voor € 8. Met belasting: 40 bekers, Pc = € 10 en Pp = € 6. De verticale afstand bij Q = 40 is € 4.')+box('Ons marktmodel','We rekenen met veel kopers en verkopers die de marktprijs als gegeven nemen. Er is één product, er zijn geen andere gelijktijdige veranderingen en alle gevraagde en aangeboden eenheden bij het nieuwe evenwicht worden verhandeld. Kosten of baten voor buitenstaanders blijven in dit hoofdstuk buiten beeld.','small')+'''
''')

pg('3.1.1','Van formule naar belastingwig','''## Uitgewerkt voorbeeld

**Fruitbekers.** Gebruik Pc = 14 − 0,10Q en Pp = 2 + 0,10Q. De verkoper draagt € 4 per verkochte beker af. Bereken de twee marktuitkomsten en leg de wig uit.

### 1 · Begin zonder belasting

Zonder belasting krijgen beide kanten dezelfde prijs. Stel daarom vraag en aanbod aan elkaar gelijk.

'''+form('14 − 0,10Q = 2 + 0,10Q<br>12 = 0,20Q → Q₀ = 60<br>P₀ = 14 − 0,10 × 60 = € 8')+'''
### 2 · Schrijf het aanbod in de kopersprijs

De verkoper wil Pp ontvangen en moet daarnaast € 4 afdragen. De koper betaalt samen dus Pc = 6 + 0,10Q.

### 3 · Bereken het nieuwe evenwicht

'''+form('14 − 0,10Q = 6 + 0,10Q<br>8 = 0,20Q → Qt = 40<br>Pc = 14 − 0,10 × 40 = € 10<br>Pp = 2 + 0,10 × 40 = € 6')+'''
### 4 · Controleer en verklaar

Er worden **40 fruitbekers per dag** verkocht. Controle: € 10 − € 6 = € 4. Markeer in figuur 2 bij Q = 40 beide prijzen; de verticale afstand is de wig.

De koper betaalt € 2 meer dan eerst. De verkoper houdt € 2 minder over. Hoewel de verkoper de volledige belasting afdraagt, wordt de last hier verdeeld. We rekenen nog niet met surplus; dat komt in §3.1.2.

'''+box('Onthouden','Vrij evenwicht: één prijs. Belasting: Pc − Pp = t. Gebruik de vraaglijn voor Pc en de oorspronkelijke aanbodlijn voor Pp, beide bij dezelfde nieuwe hoeveelheid. Controleer altijd de wig.','summary')+'''
## Startopgaven

'''+ROUTE+ex(1,'Evenwicht terughalen','Voor sleutelhangers geldt vraag P = 12 − 0,10Q en aanbod P = 4 + 0,10Q. Q is stuks per dag; P is euro per stuk.',[
'Bereken de evenwichtshoeveelheid en de evenwichtsprijs.',
'Bereken met de aanbodfunctie welk bedrag bij Q = 30 hoort.'
])+ex(2,'Wie draagt af?','Na een belasting betaalt een koper € 9. De verkoper houdt na afdracht € 6 over.',[
'Hoe groot is de belasting per product?',
'Kun je zonder de oude prijs berekenen wie de grootste last draagt? Licht je antwoord toe.'
]))

pg('3.1.1','Oefenen met minder steun','''## Begeleide inoefening

'''+SKIP+ex(3,'Lees de geldstroom','Gebruik de volledig uitgewerkte fruitbekermarkt in figuur 2 op pagina 3.',[
'Lees Q₀, P₀, Qt, Pc en Pp af. Welke twee prijzen horen bij dezelfde hoeveelheid?',
'Leg uit waarom je Pp niet afleest op A + t.',
'Een leerling telt € 4 op bij de oude prijs van € 8 en krijgt Pc = € 12. Wijs met de berekende hoeveelheid aan waarom die aanpak hier niet klopt.'
])+ex(4,'Posters','Vraag Pc = 16 − 0,10Q; aanbod Pp = 4 + 0,10Q. Q is posters per week. De verkoper draagt € 4 per verkochte poster af.',[
'Vul eerst in: Pc = Pp + … = … + 0,10Q.',
'Los 16 − 0,10Q = … + 0,10Q op. Bereken daarna Pc en Pp.',
'Teken in de basisgrafiek A + t. Markeer bij de nieuwe hoeveelheid beide prijzen en verbind ze met een verticale lijn.',
'Controleer de wig en leg in één zin uit waarom er minder posters worden verkocht.'
])+fig('3.1.1_ex_1','Basisgrafiek bij opgave 4. V en A zijn gegeven; de belastinglijn en de nieuwe uitkomst teken je zelf.'))

pg('3.1.1','Zelf de belasting verwerken','''## Zelfstandige oefening

'''+ex(5,'Mokken','Op de markt voor mokken geldt Pc = 18 − 0,20Q en Pp = 6 + 0,10Q. Q is mokken per dag. Verkopers dragen € 3 per verkochte mok af.',[
'Bereken het vrije evenwicht.',
'Stel het aanbod in kopersprijzen na de belasting op. Bereken Qt, Pc en Pp.',
'Teken A + t in de basisgrafiek. Markeer de nieuwe hoeveelheid, beide prijzen en de belastingwig.',
'Leg uit waarom de verkopersontvangst lager kan zijn terwijl de kopersprijs hoger is.'
])+fig('3.1.1_ex_2','Basisgrafiek bij opgave 5. De assen gebruiken aantallen per dag en euro per mok.')+ex(6,'Twee bedragen veranderen','Een marktonderzoek meldt na een belasting: de prijs voor kopers stijgt van € 7 naar € 9. De ontvangst van verkopers daalt van € 7 naar € 6.',[
'Bereken afzonderlijk de prijsverandering voor kopers en voor verkopers. Bereken daarna de belasting per product.',
'Beoordeel: “De belasting is € 2, want dat is wat de koper extra betaalt.”'
]))

pg('3.1.1','Laat zien wat je kunt','''## Doeloefening

'''+ex(7,'Bedrukte tassen','Verschillende aanbieders verkopen dezelfde soort bedrukte tas. Vraag: Pc = 20 − 0,20Q. Aanbod: Pp = 2 + 0,10Q. Q is tassen per dag; prijzen zijn euro per tas. De overheid heft € 3 per verkochte tas. De verkopers dragen de belasting af. De andere marktomstandigheden blijven gelijk.',[
'Bereken de vrije evenwichtsprijs en -hoeveelheid.',
'Stel na invoering van de belasting het aanbod in kopersprijzen op. Bereken de nieuwe hoeveelheid.',
'Bereken de prijs die kopers betalen en het bedrag dat verkopers na afdracht ontvangen.',
'Teken de nieuwe aanbodlijn in de basisgrafiek. Markeer de nieuwe hoeveelheid, beide prijzen en de belastingwig.',
'Een verkoper zegt: “Wij dragen alles af; dus wij dragen ook de hele economische last.” Beoordeel met de oude en nieuwe prijzen.'
],'target')+fig('3.1.1_target','Basisgrafiek bij de doeloefening. Gebruik V voor de kopersprijs en de oorspronkelijke A voor de verkopersontvangst.')+box('Controle vóór je inlevert','Staan beide prijzen bij dezelfde Q? Is hun verschil precies € 3? Heeft de hoeveelheid de juiste eenheid?','small'))

pg('3.1.1','Een andere betalingsroute','''## Denkertje / Bonusopgave

'''+ex(8,'De koper draagt af','Op een markt geldt Pc = 16 − 0,10Q en Pp = 4 + 0,10Q. De belasting is € 4 per verkocht product. Tot nu toe droeg de verkoper die af. Een nieuw voorstel laat de koper € 4 rechtstreeks aan de overheid betalen, boven op het bedrag voor de verkoper. Het product, de belasting per transactie en het gedrag van kopers en verkopers blijven verder gelijk.',[
'Voorspel of de nieuwe hoeveelheid, Pc en Pp veranderen. Onderbouw zonder alleen te zeggen wie het geld overmaakt.',
'Teken een geldstroomschema met koper, verkoper en overheid. Laat zien dat dezelfde wig blijft bestaan.'
],'bonus')+box('Denk aan het onderscheid','Een betalingsroute vertelt wie het geld overmaakt. Een economische last volgt uit de verandering ten opzichte van de situatie zonder belasting.','small')+'''
## Herhaling / Herhaling en interleaving

'''+ex(9,'Prijs en gevraagde hoeveelheid','Een prijs stijgt van € 10 naar € 12. De gevraagde hoeveelheid daalt van 200 naar 180 producten per week. Gebruik de oude waarden als basis.',[
'Bereken de procentuele prijsverandering en de procentuele hoeveelheidsverandering.',
'Bereken Ev en bepaal of de vraag prijsinelastisch of prijselastisch is.'
])+'''
### Maak je antwoord controleerbaar

Een berekening is pas af als duidelijk is **wat** je hebt berekend. Schrijf bijvoorbeeld “Pc = € 10 per tas” in plaats van alleen “10”. Bij een uitleg verbind je een feit aan een gevolg: “De verkoper ontvangt minder per tas en biedt daarom, bij dezelfde aanbodfunctie, minder tassen aan.”

'''+box('Verder in de volgende paragraaf','Je kunt nu de nieuwe marktuitkomst bepalen. In §3.1.2 onderzoek je wie welk deel van de last draagt, hoeveel de overheid ontvangt en welke voordelen van handel verdwijnen.','summary'))

# §3.1.2 — pages 9–15
pg('3.1.2','Waar blijft de belasting?','''<a id="s312"></a>
<div class="kicker">3.1.2 · BELASTINGDRUK EN WELVAARTSVERLIES</div>
# Waar blijft de belasting?

Bij de fruitbekers steeg de kopersprijs van € 8 naar € 10. Verkopers hielden nog € 6 over. Er werden 40 in plaats van 60 bekers verkocht. De overheid ontving € 4 per verkochte beker.

De kopers en verkopers verliezen voordeel. Maar verdwijnt al dat voordeel? Een deel komt bij de overheid terecht. Een ander deel ontstaat helemaal niet meer, doordat transacties wegvallen.

'''+box('Lesdoelen','Je kunt de belastingdruk per product over kopers en verkopers verdelen, ook in procenten. Je kunt belastingopbrengst, CS, PS en welvaartsverlies berekenen en markeren. Je kunt uitleggen waarom de minder prijsgevoelige kant relatief meer last draagt.','goals')+form('Last koper per stuk = Pc − P₀<br>Last verkoper per stuk = P₀ − Pp<br>Aandeel koper = (Pc − P₀) / t × 100%')+'''
Het aandeel van de koper heet ook het **afwentelingspercentage**: welk deel van de belasting komt via een hogere prijs bij kopers terecht? In het fruitbekervoorbeeld is dat € 2 / € 4 × 100% = 50%.

'''+box('Belastingopbrengst O','De overheid ontvangt alleen belasting over werkelijk verkochte producten.<br><b>O = t × Qt</b>. Hier: € 4 per beker × 40 bekers per dag = € 160 per dag.')+'''
### Geen verdwenen geld

De € 160 is een overdracht aan de overheid. Het is geen € 160 aan verdwenen welvaart. Voor onze vergelijking tellen we overheidsontvangsten mee naast het consumenten- en producentensurplus.

'''+box('Onze welvaartsmaat','Zonder belasting: CS + PS. Met belasting: CS + PS + O. We rekenen zonder effecten voor buitenstaanders en zonder uitvoeringskosten. Wat de overheid later met het geld doet, is hier niet gegeven.','warning'))

pg('3.1.2','Rechthoek, driehoek en prijsgevoeligheid','''### De gebieden vertellen elk iets anders

De vraaglijn geeft de betalingsbereidheid. De oorspronkelijke aanbodlijn stelt in dit model de marginale kosten voor. CS ligt boven **Pc**; PS ligt onder **Pp**. De belastingopbrengst ligt tussen die twee prijzen, over de verkochte hoeveelheid.

'''+fig('3.1.2_fig_1','O is de belastingrechthoek: 40 × € 4. W is de driehoek van gemiste transacties tussen Q = 40 en Q = 60.')+'''
De extra transacties tussen 40 en 60 zouden meer opleveren aan betalingsbereidheid dan ze kosten. Door de wig komen ze niet tot stand. Hun gezamenlijke gemiste voordeel heet **welvaartsverlies W**.

'''+form('W = oude welvaartsmaat − nieuwe welvaartsmaat<br>Bij deze rechte lijnen ook: W = ½ × (Q₀ − Qt) × t')+'''
### Wie kan makkelijker reageren?

Als kopers makkelijk overstappen of afzien van aankoop, kunnen verkopers een prijsverhoging minder makkelijk doorberekenen. Zijn kopers juist weinig prijsgevoelig vergeleken met verkopers, dan dragen kopers een groter deel van de last. Dezelfde redenering geldt omgekeerd voor weinig prijsgevoelige verkopers.

'''+box('Niet alleen naar de helling kijken','Vergelijk prijsgevoeligheid niet met lijnen uit grafieken met verschillende schalen. Op pagina 15 staat een gecontroleerde vergelijking: dezelfde beginprijs, beginhoeveelheid, aanbodfunctie en belasting.','small'))

pg('3.1.2','Reken de welvaartsverandering na','''## Uitgewerkt voorbeeld

**Fruitbekers, vervolg.** Vraag Pc = 14 − 0,10Q; aanbod Pp = 2 + 0,10Q. Zonder belasting: Q₀ = 60 en P₀ = € 8. Bij t = € 4: Qt = 40, Pc = € 10 en Pp = € 6.

**1 · Verdeel de last.** Koper: 10 − 8 = € 2. Verkoper: 8 − 6 = € 2. De koper draagt 2 / 4 × 100% = **50%**.

**2 · Bereken de gebieden.** De basis van elke surplusdriehoek is de verkochte hoeveelheid; de hoogte is een prijsverschil.

| Grootheid | Zonder belasting (€ per dag) | Met belasting (€ per dag) |
|---|---|---|
| CS | ½ × 60 × (14 − 8) = 180 | ½ × 40 × (14 − 10) = 80 |
| PS | ½ × 60 × (8 − 2) = 180 | ½ × 40 × (6 − 2) = 80 |
| O | 0 | 4 × 40 = 160 |
| CS + PS + O | 360 | 320 |

**3 · Bereken en controleer W.** W = 360 − 320 = **€ 40 per dag**. Met de driehoek: ½ × (60 − 40) × 4 = € 40. Beide routes geven hetzelfde.

**4 · Trek een conclusie.** Kopers en verkopers verliezen samen € 200 surplus. Daarvan ontvangt de overheid € 160. Alleen de overige € 40 is in dit model welvaartsverlies. Bij een minder prijsgevoelige vraag en gelijk aanbod zou een groter deel van de belasting bij kopers terechtkomen.

'''+box('Onthouden','Last per stuk ≠ belastingopbrengst ≠ welvaartsverlies. O is een rechthoek over verkochte producten. W is de driehoek van gemiste voordelige transacties. De minder prijsgevoelige kant draagt relatief meer last.','summary')+'''
## Startopgaven

'''+ROUTE+ex(10,'Surplus terughalen','Een markt heeft Q₀ = 40 en P₀ = € 10. De vraaglijn snijdt de prijsas bij € 18; de aanbodlijn bij € 6. Beide lijnen zijn recht.',[
'Bereken CS en PS met basis, hoogte en eenheid.'
])+ex(11,'Geld of gemiste handel?','Een belasting levert de overheid € 120 op. De welvaartsmaat daalt van € 500 naar € 470.',[
'Hoe groot is het welvaartsverlies? Leg uit waarom dit niet € 120 is.'
]))

pg('3.1.2','Alle onderdelen zichtbaar','''## Begeleide inoefening

'''+SKIP+ex(12,'Lees het belastingplaatje','Gebruik de volledig ingekleurde fruitbekermarkt in figuur 1 op pagina 10.',[
'Wijs CS, PS, O en W aan. Welke prijs vormt de ondergrens van CS? Welke prijs vormt de bovengrens van PS?',
'Bereken eerst alleen de oppervlakte O. Gebruik daarna Q₀ − Qt als basis van W.',
'Leg uit waarom de hele oppervlakte tussen Pc en Pp niet hetzelfde is als W.'
])+ex(13,'Kaartensets','Voor kaartensets is het vrije evenwicht Q₀ = 60 en P₀ = € 10. Een belasting van € 4 geeft Qt = 40, Pc = € 12 en Pp = € 8. De rechte vraaglijn begint op de prijsas bij € 16 en de rechte aanbodlijn bij € 4. Q is sets per dag.',[
'Vul eerst de tabel hieronder volledig in. Noteer eenheden en laat voor CS en PS telkens basis en hoogte zien.',
'Bereken O en W. Controleer W met de driehoek.',
'Beoordeel: “Omdat kopers en verkopers elk € 2 per set dragen, ontvangt de overheid maar € 2 per set.”'
])+'''
| Grootheid | Zonder belasting | Met belasting |
|---|---|---|
| CS (€ per dag) | … | … |
| PS (€ per dag) | … | … |
| O (€ per dag) | 0 | … |
| CS + PS + O (€ per dag) | … | … |

'''+box('Laat de hulp los','Schrijf bij de volgende opgaven zelf op welke prijs, hoeveelheid en oppervlakte je nodig hebt. Een uitkomst zonder economische betekenis is nog geen conclusie.','small'))

pg('3.1.2','Last en verlies zelf berekenen','''## Zelfstandige oefening

'''+ex(14,'Stickerpakketten','Vraag Pc = 16 − 0,10Q; aanbod Pp = 4 + 0,10Q. Zonder belasting: Q₀ = 60 en P₀ = € 10. Verkopers dragen € 4 per verkocht pakket af. Na invoering: Qt = 40, Pc = € 12 en Pp = € 8. Q is pakketten per week.',[
'Bereken de last per pakket voor kopers en verkopers en het afwentelingspercentage.',
'Bereken CS en PS voor en na de belasting, O en W.',
'Markeer in de basisgrafiek Pc, Pp en Qt. Arceer O en W verschillend en benoem beide gebieden.'
])+fig('3.1.2_ex_1','Basisgrafiek bij opgave 14. De oorspronkelijke A blijft de marginale-kostenlijn.')+ex(15,'Niet even prijsgevoelig','Twee markten hebben dezelfde beginprijs en beginhoeveelheid, hetzelfde aanbod en dezelfde belasting. In markt X kunnen kopers makkelijk een ander product kiezen; in markt Y veel minder.',[
'In welke markt verwacht je een groter aandeel van de belasting bij de koper? Leg uit via de mogelijkheid om op de prijs te reageren.',
'Waarom is “de verkoper draagt af” geen bewijs voor jouw antwoord?'
]))

pg('3.1.2','De hele belastingrekening','''## Doeloefening

'''+ex(16,'Bedrukte tassen: wie betaalt?','Dit is de markt uit §3.1.1, met alle gegevens opnieuw gegeven. Vraag Pc = 20 − 0,20Q; aanbod Pp = 2 + 0,10Q. Q is tassen per dag. Eerst: Q₀ = 60 en P₀ = € 8. Met t = € 3: Qt = 50, Pc = € 10 en Pp = € 7. De belasting heeft geen effecten voor buitenstaanders en geen uitvoeringskosten.',[
'Bereken de last per tas voor beide kanten en het afwentelingspercentage.',
'Bereken de belastingopbrengst per dag.',
'Bereken CS en PS zonder en met belasting. Bereken daarna de welvaartsmaat met overheid en het welvaartsverlies.',
'Markeer Qt, Pc en Pp in de basisgrafiek. Arceer de belastingopbrengst en het welvaartsverlies verschillend. Noteer basis en hoogte van W.',
'Een koper zegt: “Als de vraag nog minder prijsgevoelig was, zouden wij minder belasting dragen.” Beoordeel, bij gelijk aanbod en dezelfde belasting.'
],'target')+fig('3.1.2_target','Basisgrafiek bij de doeloefening. Gebruik de twee werkelijk ontvangen en betaalde prijzen, niet één middenprijs.'))

pg('3.1.2','Vergelijk eerlijk','''## Denkertje / Bonusopgave

'''+ex(17,'Een gecontroleerd experiment','Beide markten beginnen bij P₀ = € 8 en Q₀ = 60. Het aanbod is steeds Pp = 2 + 0,10Q. De belasting is steeds € 3 per product. In A is de vraag Pc = 14 − 0,10Q; in B is die Pc = 20 − 0,20Q. Na belasting: A heeft Q = 45, Pc = € 9,50 en Pp = € 6,50. B heeft Q = 50, Pc = € 10 en Pp = € 7.',[
'Bij een stijging van Pc van € 8 naar € 9: bereken de gevraagde hoeveelheid in A en B. Welke vraag reageert minder sterk?',
'Verbind dat verschil met de verdeling van de € 3 belasting in de figuur. Waarom is deze vergelijking zorgvuldiger dan twee willekeurige hellingen vergelijken?'
],'bonus')+fig('3.1.2_fig_2','In A dragen koper en verkoper elk € 1,50. In B draagt de koper € 2 en de verkoper € 1. Alle begin- en aanbodvoorwaarden zijn gelijk gehouden.')+'''
## Herhaling / Herhaling en interleaving

'''+ex(18,'Een bedrag per product','Een producent verkoopt 100 producten voor € 9 per stuk. TK = 300 + 4Q, met kosten in euro per dag en Q in producten per dag.',[
'Bereken TO, TK en de winst per dag.',
'Leg uit waarom een ontvangst van € 9 per product geen winst van € 9 per product is.'
])+box('Verder in de volgende paragraaf','Bij een subsidie legt de overheid geld bij. De wig draait om. Maar voor welvaart moet je de overheidsuitgaven juist aftrekken.','summary'))

# §3.1.3 — pages 16–22
pg('3.1.3','De overheid legt geld bij','''<a id="s313"></a>
<div class="kicker">3.1.3 · SUBSIDIES</div>
# De overheid legt geld bij

Een gemeente wil meer workshopbezoek. In deze oefensituatie krijgt de aanbieder € 4 subsidie voor iedere werkelijk verkochte workshopplaats. De koper betaalt aan de aanbieder; de gemeente betaalt het subsidiebedrag erbij.

De aanbieder ontvangt nu meer dan de koper betaalt. Je gebruikt dezelfde twee prijzen als bij belasting, maar **de wig wijst de andere kant op**.

'''+box('Lesdoelen','Je kunt bij een subsidie per verkocht product Pc, Pp en de hoeveelheid berekenen. Je kunt de overheidsuitgaven bepalen en de voordelen voor kopers en verkopers vergelijken. Je kunt een welvaartsclaim beoordelen door de uitgaven mee te rekenen.','goals')+fig('3.1.3_fig_1','De koper betaalt € 10. De gemeente legt € 4 bij. De aanbieder ontvangt samen € 14 per verkochte workshopplaats.')+form('Subsidiewig: Pp − Pc = s<br>Dus: Pp = Pc + s en Pc = Pp − s')+'''
**s** is de subsidie per verkocht product. **Pp** is hier de totale ontvangst van de producent: het bedrag van de koper plus de subsidie. Daar moeten de productiekosten nog af.

'''+box('Vergelijk met belasting','Belasting: Pc is hoger dan Pp. Subsidie: Pp is hoger dan Pc. In beide gevallen lees je Pc op de vraaglijn en Pp op de oorspronkelijke aanbodlijn bij dezelfde nieuwe Q.','summary'))

pg('3.1.3','Meer handel is niet gratis','''### De aanbodlijn in kopersprijzen

Voor workshopplaatsen geldt Pc = 18 − 0,10Q en Pp = 6 + 0,10Q. Q is plaatsen per week; prijzen zijn euro per plaats. Door de subsidie van € 4 hoeft de koper € 4 minder te betalen dan de aanbieder totaal wil ontvangen.

'''+form('Pc = Pp − 4 = 2 + 0,10Q')+fig('3.1.3_fig_2','A − s ligt € 4 onder A. Bij Q = 80 zijn Pc = € 10 en Pp = € 14. U is de uitgavenrechthoek over alle 80 plaatsen.')+'''
### Een rekening voor de overheid

De subsidie geldt hier voor **elke verkochte plaats**, niet alleen voor de extra plaatsen. De overheidsuitgaven zijn dus **U = s × Qs**: de rechthoek U in de figuur. Met Qs bedoelen we hier de hoeveelheid mét subsidie; het aanbod noteren we als Qa.

### Kijk verder dan CS en PS

Kopers betalen minder en aanbieders ontvangen meer. CS en PS kunnen dus allebei stijgen. Maar de overheid betaalt ervoor. De relevante welvaartsmaat is hier **CS + PS − U**.

De extra transacties voorbij het vrije evenwicht kosten in dit model meer dan de kopers ervoor overhebben. Zonder baten voor buitenstaanders kan de subsidie daardoor welvaartsverlies veroorzaken. We veronderstellen ook hier geen uitvoeringskosten.

'''+box('Geen dubbele telling','Tel U niet bij het voordeel van kopers en verkopers op. De subsidie zit al in de grotere gebieden CS en PS. Voor de welvaartsvergelijking trek je de overheidsuitgaven af.','warning'))

pg('3.1.3','Dezelfde stappen, een andere wig','''## Uitgewerkt voorbeeld

**Workshopplaatsen.** Pc = 18 − 0,10Q; Pp = 6 + 0,10Q; s = € 4 per verkochte plaats. Zonder subsidie: Q₀ = 60, P₀ = € 12, CS = € 180 en PS = € 180 per week.

**1 · Pas de kopersprijs van het aanbod aan.** Pc = Pp − 4 = 2 + 0,10Q.

**2 · Bereken de nieuwe hoeveelheid en prijzen.**

'''+form('18 − 0,10Q = 2 + 0,10Q → Qs = 80<br>Pc = 18 − 0,10 × 80 = € 10<br>Pp = 6 + 0,10 × 80 = € 14')+'''
Controle: 14 − 10 = € 4. Kopers betalen € 2 minder; aanbieders ontvangen € 2 meer per plaats. De aanbieder krijgt de subsidie uitbetaald, maar is niet de enige die profiteert.

**3 · Bereken uitgaven en surplus.**

| Grootheid | Berekening na subsidie | Uitkomst per week |
|---|---|---|
| U | 4 × 80 | € 320 |
| CS | ½ × 80 × (18 − 10) | € 320 |
| PS | ½ × 80 × (14 − 6) | € 320 |
| CS + PS − U | 320 + 320 − 320 | € 320 |

**4 · Vergelijk.** Eerst was de welvaartsmaat € 360. Nu is zij € 320: **€ 40 welvaartsverlies**. Controle met rechte lijnen: ½ × (80 − 60) × 4 = € 40.

'''+box('Onthouden','Subsidie: Pp − Pc = s. Bereken U over alle gesubsidieerde verkopen. Vergelijk niet alleen CS en PS, maar CS + PS − U. Zonder externe baten is méér productie niet automatisch beter.','summary')+'''
## Startopgaven

'''+ROUTE+ex(19,'De wig terughalen','Bij een belasting van € 3 betaalt de koper € 11. Bij een andere markt met € 3 subsidie betaalt de koper ook € 11.',[
'Bereken in beide gevallen Pp. Geef aan wanneer je € 3 aftrekt en wanneer je € 3 optelt.'
])+ex(20,'Voor alle verkochte plaatsen','Een subsidie van € 2 vergroot de verkoop van 50 naar 60 plaatsen per week.',[
'Bereken de uitgaven als iedere verkochte plaats recht op subsidie geeft. Waarom gebruik je niet alleen de 10 extra plaatsen?'
]))

pg('3.1.3','Herken de omgekeerde route','''## Begeleide inoefening

'''+SKIP+ex(21,'Lees de subsidie-uitkomst','Gebruik de workshopgrafiek op pagina 17. De vraag- en aanbodlijn zijn niet van betekenis veranderd.',[
'Lees bij Q = 80 beide prijzen af. Welke partij ontvangt samen € 14?',
'Leg uit waarom de aanbodlijn in kopersprijzen naar beneden schuift en niet de vraaglijn.',
'Bereken het voordeel per plaats voor de koper én voor de aanbieder, vergeleken met € 12.'
])+ex(22,'Muzieklesplaatsen','Vraag Pc = 22 − 0,10Q; aanbod Pp = 10 + 0,10Q. Zonder subsidie: Q₀ = 60 en P₀ = € 16. De aanbieder krijgt € 4 per verkochte lesplaats. Q is lesplaatsen per week.',[
'Vul eerst in: Pc = Pp − … = … + 0,10Q. Bereken vervolgens de nieuwe hoeveelheid en beide prijzen.',
'Teken A − s in de basisgrafiek en markeer Pc, Pp en Qs.',
'Bereken U. Bereken daarna CS en PS met de nieuwe hoeveelheid; vergelijk CS + PS − U met de oude € 360.'
])+fig('3.1.3_ex_1','Basisgrafiek bij opgave 22. A beschrijft de totale ontvangst die aanbieders bij elke hoeveelheid nodig hebben.'))

pg('3.1.3','Reken mét de overheidsrekening','''## Zelfstandige oefening

'''+ex(23,'Sportplaatsen','Vraag Pc = 24 − 0,20Q; aanbod Pp = 6 + 0,10Q. Eerst zijn Q₀ = 60 en P₀ = € 12. Aanbieders krijgen € 3 per verkochte sportplaats. Q is plaatsen per week. De oude welvaartsmaat is € 540 per week.',[
'Bereken de nieuwe hoeveelheid, Pc en Pp. Teken A − s en markeer de drie uitkomsten.',
'Bereken de subsidie-uitgaven, CS en PS.',
'Bereken CS + PS − U en het welvaartsverlies. Noem de veronderstelling over baten voor anderen.'
])+fig('3.1.3_ex_2','Basisgrafiek bij opgave 23. Controleer na het rekenen de richting én de grootte van de wig.')+ex(24,'Meer voordeel, toch een rekening','Na een subsidie betalen kopers per product € 2 minder en ontvangen verkopers per product € 1 meer dan voorheen.',[
'Hoe hoog is de subsidie per product?',
'Beoordeel: “Iedereen profiteert, want kopers én verkopers zijn beter af.” Noem welke partij en welk bedrag per transactie in deze uitspraak ontbreken.'
]))

pg('3.1.3','Wie krijgt het subsidievoordeel?','''## Doeloefening

'''+ex(25,'Cursusplaatsen','Vraag Pc = 26 − 0,20Q; aanbod Pp = 8 + 0,10Q. Q is cursusplaatsen per week. Eerst: Q₀ = 60, P₀ = € 14, CS = € 360 en PS = € 180 per week. Aanbieders ontvangen € 3 subsidie per werkelijk verkochte plaats. Er zijn geen baten voor buitenstaanders en geen uitvoeringskosten.',[
'Stel het aanbod in kopersprijzen mét subsidie op. Bereken Qs, Pc en Pp.',
'Bereken de overheidsuitgaven per week.',
'Bereken het voordeel per plaats voor kopers en aanbieders. Leg uit waarom uitbetaling aan aanbieders niet betekent dat zij het hele voordeel krijgen.',
'Bereken CS en PS na subsidie. Bepaal CS + PS − U en het welvaartsverlies ten opzichte van de oude situatie.',
'Markeer Qs, Pc en Pp in de basisgrafiek. Arceer de rechthoek van de overheidsuitgaven. Beoordeel: “De subsidie verhoogt in dit model automatisch de welvaart.”'
],'target')+fig('3.1.3_target','Basisgrafiek bij de doeloefening. De uitgavenrechthoek ligt tussen Pc en Pp, van Q = 0 tot de nieuwe hoeveelheid.'))

pg('3.1.3','De vorm van steun doet ertoe','''## Denkertje / Bonusopgave

'''+ex(26,'Per verkoop of een vast bedrag?','Regeling A geeft aanbieders € 3 per verkochte cursusplaats. In de markt van opgave 25 ontstaan dan 70 verkopen. Regeling B vervangt A door samen € 210 vaste steun aan de bestaande aanbieders, ongeacht hoeveel zij verkopen. Volgens de bron veranderen bij B de vraag, de marginale kosten en de marktdeelname niet; het vrije evenwicht blijft dus 60 plaatsen voor € 14.',[
'Vergelijk de uitgaven onder A en B. Welke regeling verandert in deze bron de prikkel om extra plaatsen aan te bieden?',
'Leg uit waarom je bij B niet automatisch A met € 3 omlaag mag verschuiven. Gebruik het verschil tussen een vast bedrag en een bedrag per verkoop.'
],'bonus')+fig('3.1.3_fig_3','Terugblik op de workshopmarkt: U omvat alle 80 gesubsidieerde plaatsen. W markeert de extra transacties waarvan de marginale kosten boven de betalingsbereidheid liggen.')+'''
## Herhaling / Herhaling en interleaving

'''+ex(27,'Totaal en per eenheid','Een zaal heeft € 600 constante kosten per week. De zaal verhuurt eerst 100 en later 150 stoelen per week, binnen dezelfde productiecapaciteit.',[
'Bereken de gemiddelde constante kosten bij beide aantallen.',
'Leg uit waarom de totale constante kosten niet dalen als de gemiddelde constante kosten dalen.'
])+'<p class="small">Volgende stap: een maximumprijs begrenst de prijs, niet het bedrag per verkoop.</p>')

# §3.1.4 — pages 23–29
pg('3.1.4','Goedkoper, maar ook verkrijgbaar?','''<a id="s314"></a>
<div class="kicker">3.1.4 · MAXIMUMPRIJS</div>
# Goedkoper, maar ook verkrijgbaar?

Op een markt voor puzzels is de vrije prijs € 8. Een regeling verbiedt prijzen boven € 6. Dat klinkt gunstig voor kopers. Toch kan niet iedereen die bij € 6 wil kopen een puzzel krijgen.

Een prijsregel verandert niet wat consumenten graag willen of wat productie kost. Hij kan wel verhinderen dat de prijs vraag en aanbod bij elkaar brengt.

'''+box('Lesdoelen','Je kunt bepalen of een maximumprijs bindt. Je kunt bij die prijs vraag, aanbod, werkelijke verkopen en het tekort berekenen. Je kunt de drie hoeveelheden in een grafiek onderscheiden en uitleggen welke kopers geen product krijgen.','goals')+box('Maximumprijs','De hoogste toegestane verkoopprijs. Een maximumprijs <b>onder de vrije evenwichtsprijs</b> is in ons model bindend: hij verandert de marktuitkomst.')+fig('3.1.4_fig_1','Bij Pmax = € 6 willen kopers 80 puzzels, maar verkopers bieden er 40 aan. Er worden 40 verkocht; het tekort is 40.')+'''
Qv is wat kopers **willen kopen**. Qa is wat verkopers **willen verkopen**. Het werkelijke aantal transacties is weer iets anders. Zonder extra aanvoer kunnen niet meer producten worden verkocht dan er worden aangeboden.

'''+box('Geen wig','Hier is geen belasting of subsidie per verkoop. Bij een verkoop betaalt de koper hetzelfde bedrag als de verkoper ontvangt. Het probleem is een verschil tussen hoeveelheden, niet tussen twee prijzen.','small'))

pg('3.1.4','Eerst binding, dan hoeveelheden','''### Een maximum is geen verplicht prijskaartje

Bij een vrije evenwichtsprijs van € 8 laat een maximum van € 10 de marktprijs van € 8 toe. Verkopers hoeven niet € 10 te vragen. De regeling is dan **niet bindend**.

| Maximumprijs | Bindend bij vrij evenwicht € 8? | Marktuitkomst in dit model |
|---|---|---|
| € 6 | Ja | Bereken Qv en Qa bij € 6. |
| € 10 | Nee | P blijft € 8; Q blijft 60. |

### De korte kant bepaalt wat er kan worden verkocht

In de puzzelmarkt zijn 40 producten beschikbaar en willen kopers er 80. Neem aan dat die 40 daadwerkelijk worden verkocht. Dan geldt:

'''+form('Werkelijke verkopen = Qa = 40<br>Tekort = Qv − Qa = 80 − 40 = 40')+'''
Je kunt deze regel niet gebruiken zonder de context te lezen. Een bron kan bijvoorbeeld voorraden of extra aanvoer noemen. In onze oefeningen zijn die er niet, tenzij de tekst dat uitdrukkelijk zegt.

### Wie ontvangt het product?

Voor het totale aantal verkopen is “40 aangeboden” genoeg. Voor de verdeling van het voordeel is ook nodig **welke kopers** de 40 producten krijgen. Een wachtrij, loting en toewijzing op betalingsbereidheid kunnen andere kopers selecteren.

Krijgen de hoogste betalingsbereidheden voorrang, dan blijven andere geïnteresseerde kopers zonder product. Een lagere prijs is dus niet automatisch beter voor iedere koper.

'''+box('Surplus vraagt om een toewijzingsregel','Bij een tekort gebruik je niet zomaar de hele driehoek tot Qv. Alleen werkelijk verkochte producten leveren surplus op. Wie ze ontvangt, bepaalt het CS. In dit onderdeel staan binding, hoeveelheden en de verdeling van toegang centraal; het denkertje laat de toewijzing zien.','warning')+'''
### Zelfde rekenen, andere interpretatie

In Boek 1 vulde je een prijs in om Qv en Qa te bepalen. Die techniek blijft gelijk. Nieuw is dat de opgelegde prijs niet vrij kan stijgen om het tekort op te lossen. Markeer daarom vraag, aanbod **en** werkelijke verkopen afzonderlijk.
''')

pg('3.1.4','Een lage prijs analyseren','''## Uitgewerkt voorbeeld

**Puzzels.** Vraag P = 14 − 0,10Q; aanbod P = 2 + 0,10Q. Q is puzzels per week. Er komen geen voorraden of extra producten bij. Alle aangeboden puzzels worden verkocht aan de kopers met de hoogste betalingsbereidheid.

**1 · Bereken het vrije evenwicht.**

'''+form('14 − 0,10Q = 2 + 0,10Q → Q₀ = 60<br>P₀ = 14 − 0,10 × 60 = € 8')+'''
**2 · Controleer de maximumprijs.** € 6 is lager dan € 8, dus de regeling bindt.

**3 · Bereken beide gewenste hoeveelheden.** Gebruik nu dezelfde prijs van € 6 in beide oorspronkelijke functies.

'''+form('Vraag: 6 = 14 − 0,10Qv → Qv = 80<br>Aanbod: 6 = 2 + 0,10Qa → Qa = 40<br>Verkopen = 40; tekort = 80 − 40 = 40')+'''
**4 · Markeer en verklaar.** Figuur 1 laat bij P = € 6 twee snijpunten zien. Markeer Qa = 40 als werkelijk verkocht. De 40 hoogste betalingsbereidheden krijgen een puzzel. Van de overige kopers die voor € 6 willen kopen, krijgen er 40 geen.

Bij een maximum van € 10 zou de oude prijs van € 8 toegestaan blijven. Dan blijven prijs en hoeveelheid € 8 en 60; je vult dus niet automatisch € 10 in.

'''+box('Onthouden','Vergelijk eerst Pmax met P₀. Alleen bij een bindende maximumprijs bereken je de nieuwe hoeveelheden bij Pmax. Zonder extra aanvoer: verkopen = Qa en tekort = Qv − Qa. Een lage prijs is geen aankoopgarantie.','summary')+'''
## Startopgaven

'''+ROUTE+ex(28,'Hoeveelheid bij een prijs','Vraag P = 18 − 0,20Q; aanbod P = 6 + 0,10Q. Q is producten per dag.',[
'Bereken het vrije evenwicht.',
'Bereken bij P = € 8 afzonderlijk Qv en Qa.'
])+ex(29,'Mag de oude prijs nog?','De vrije marktprijs is € 12. Er komt een maximumprijs van € 15.',[
'Verandert de marktprijs in ons model? Leg uit waarom wel of niet.'
]))

pg('3.1.4','Van aflezen naar invullen','''## Begeleide inoefening

'''+SKIP+ex(30,'Bekijk eerst het tekort','Gebruik de volledig gemarkeerde puzzelmarkt op pagina 23.',[
'Lees Qv en Qa bij de maximumprijs af. Benoem welk aantal werkelijk wordt verkocht.',
'Wijs het tekort aan als een horizontaal verschil tussen hoeveelheden. Waarom is het geen verticale afstand tussen prijzen?',
'Beoordeel: “Alle 80 geïnteresseerde kopers betalen nu minder en zijn dus beter af.”'
])+ex(31,'Schilderpakketten','Vraag P = 16 − 0,10Q; aanbod P = 4 + 0,10Q. Q is pakketten per week. Het vrije evenwicht is Q₀ = 60, P₀ = € 10. De maximumprijs wordt € 8. Er is geen extra aanvoer; alle aangeboden pakketten worden verkocht.',[
'Leg uit waarom het maximum bindt.',
'Vul eerst in: 8 = 16 − 0,10Qv → Qv = …; 8 = 4 + 0,10Qa → Qa = … . Noteer vervolgens verkopen en tekort.',
'Teken Pmax en markeer Qv, Qa en het tekort in de basisgrafiek.',
'Welke uitkomst blijft gelden als het maximum niet € 8 maar € 12 wordt?'
])+fig('3.1.4_ex_1','Basisgrafiek bij opgave 31. De kopers en verkopers reageren op dezelfde toegestane prijs.'))

pg('3.1.4','De regel zelfstandig toepassen','''## Zelfstandige oefening

'''+ex(32,'Bordspellen','Vraag P = 20 − 0,20Q; aanbod P = 2 + 0,10Q. Q is spellen per week. De overheid zet de maximumprijs op € 6. Er zijn geen voorraden of andere aanvoer; alle aangeboden spellen worden verkocht.',[
'Bereken het vrije evenwicht en bepaal of de maximumprijs bindt.',
'Bereken Qv, Qa, de verkopen en het tekort.',
'Teken Pmax in de basisgrafiek. Markeer de hoeveelheden en het tekort.',
'Leg uit waarom je zonder toewijzingsregel niet weet welke geïnteresseerde kopers een spel krijgen.'
])+fig('3.1.4_ex_2','Basisgrafiek bij opgave 32. Noteer bij de hoeveelheden ook wat elk getal betekent.')+ex(33,'De markt verandert','Eerst is de vrije evenwichtsprijs € 8 en geldt een maximum van € 10. Later neemt de vraag toe: zonder prijsregel zou het nieuwe evenwicht € 12 zijn. Tegelijk verlaagt de overheid het maximum tot € 9.',[
'Bepaal eerst alleen het effect van het lagere maximum bij de oude markt. Bindt € 9 dan?',
'Bepaal daarna of € 9 bij de nieuwe markt bindt. Beoordeel: “Of een maximum bindt, hangt alleen van het bedrag in de regeling af.”'
]))

pg('3.1.4','Een maximum bij tentverhuur','''## Doeloefening

'''+ex(34,'Tenten voor een weekend','Verschillende bedrijven verhuren dezelfde soort tent. Vraag P = 18 − 0,10Q; aanbod P = 6 + 0,10Q. P is de huur in euro per tent voor één weekend; Q is tenten per weekend. Er komt een maximumprijs van € 10. Er is geen extra aanvoer. Alle aangeboden tenten worden verhuurd, aan de vragers met de hoogste betalingsbereidheid.',[
'Bereken de vrije evenwichtsprijs en -hoeveelheid. Leg uit of de maximumprijs bindt.',
'Bereken de gevraagde en aangeboden hoeveelheid, het werkelijke aantal verhuurde tenten en het tekort.',
'Teken de maximumprijs in de basisgrafiek. Markeer Qv, Qa en het werkelijke aantal verhuringen. Geef het tekort aan.',
'Een huurder zegt: “De lagere huur is goed voor iedereen die voor € 10 een tent wil huren.” Beoordeel met de uitkomsten en de toewijzingsregel.',
'Stel dat de maximumprijs € 14 is in plaats van € 10. Geef dan de werkelijke huur en het aantal verhuringen. Licht toe.'
],'target')+fig('3.1.4_target','Basisgrafiek bij de doeloefening. Er is hier geen belasting- of subsidiewig.'))

pg('3.1.4','Dezelfde prijs, andere kopers','''## Denkertje / Bonusopgave

'''+ex(35,'Wie krijgt de twee producten?','Vier kopers willen elk één product kopen. Er zijn twee producten beschikbaar. De maximumprijs én werkelijke verkoopprijs is € 6. In situatie A kopen Noor en Bo. In situatie B krijgen via loting Sam en Imre een product. De onderstaande tabel geeft alle betalingsbereidheden.',[
'Bereken het gezamenlijke consumentensurplus in situatie A en in situatie B.',
'Leg uit waarom prijs en aantal verkopen alleen niet genoeg zijn om CS te bepalen.',
'Betekent het grootste berekende CS automatisch dat die toewijzing het eerlijkst is? Licht toe.'
],'bonus')+'''
| Koper | Betalingsbereidheid per product | Koopt in A? | Koopt in B? |
|---|---:|---|---|
| Noor | € 12 | Ja | Nee |
| Bo | € 10 | Ja | Nee |
| Sam | € 8 | Nee | Ja |
| Imre | € 7 | Nee | Ja |

'''+box('Verwar een norm niet met een berekening','Surplus meet een voordeel volgens betalingsbereidheid. Het zegt niet vanzelf welke verdeling rechtvaardig is. Dat onderscheid ken je uit Boek 2.','small')+'''
## Herhaling / Herhaling en interleaving

'''+ex(36,'Een markt zonder beperking','Vraag P = 30 − 0,50Q; aanbod P = 6 + 0,25Q. Q is kaartjes; P is euro per kaartje.',[
'Bereken de vrije evenwichtsprijs en -hoeveelheid.',
'Bereken CS en PS in het vrije evenwicht.'
])+box('Verder','Een minimumprijs legt juist een ondergrens vast. Dan kunnen aanbieders meer willen verkopen dan kopers willen kopen. De bron moet zeggen wat er met het overschot gebeurt.','summary'))

# §3.1.5 — pages 30–36
pg('3.1.5','Een prijs beschermen','''<a id="s315"></a>
<div class="kicker">3.1.5 · MINIMUMPRIJS EN QUOTA</div>
# Een prijs beschermen

Appeltelers ontvangen in een oefenmarkt € 8 per krat. Een regeling verbiedt verkopen onder € 10. De hogere toegestane opbrengst lokt meer aanbod uit, terwijl kopers juist minder willen kopen.

Wie neemt het overschot af? Dat volgt niet uit het woord “minimumprijs”. De bron moet zeggen of de overheid producten opkoopt.

'''+box('Lesdoelen','Je kunt binding, vraag, aanbod en aanbodoverschot bij een minimumprijs bepalen. Je kunt bij een expliciete aankoopgarantie de overheidsaankopen en uitgaven berekenen. Je kunt deze regeling onderscheiden van een productiequotum.','goals')+box('Minimumprijs','De laagste toegestane verkoopprijs. Een minimumprijs <b>boven de vrije evenwichtsprijs</b> is in ons model bindend. Een lagere minimumprijs laat het vrije evenwicht toe.')+fig('3.1.5_fig_1','Bij Pmin = € 10 zijn Qv = 40 en Qa = 80. In de getekende aankoopregeling koopt de overheid 40 kratten; U = 40 × € 10.')+'''
De oorspronkelijke vraaglijn beschrijft hier de **particuliere kopers**. Hun aankopen zijn dus niet hetzelfde als alle verkopen wanneer de overheid ook koopt.

'''+box('Aanbod is nog geen verkoop','Zonder aankoopgarantie zijn 80 aangeboden kratten niet automatisch 80 verkochte kratten. Met een garantie kan de overheid het verschil tussen Qa en Qv afnemen.','warning'))

pg('3.1.5','Een prijsgrens is geen quotum','''### Lees de aankoopregel

Bij € 10 willen particuliere kopers 40 kratten kopen en bieden telers 80 kratten aan. Het **aanbodoverschot** is 80 − 40 = 40 kratten.

Zonder opkoop verkoopt men in ons model alleen de 40 die particulieren willen kopen. Wordt alle overtollige productie gegarandeerd opgekocht tegen € 10, dan produceren en verkopen telers samen 80 kratten: 40 aan particulieren en 40 aan de overheid.

'''+form('Overheidsaankopen = Qa − Qv  [bij volledige opkoop]<br>U = aankoopprijs × overheidsaankopen')+'''
### Een quotum begrenst de hoeveelheid

Een **productiequotum** is een maximaal toegestane productie. Stel dat de prijsregeling vervalt en telers samen maximaal 40 kratten mogen produceren. Alle 40 worden geproduceerd en verkocht; de productierechten zijn gratis verdeeld. Er zijn geen overheidsaankopen.

'''+fig('3.1.5_fig_2','Het quotum beperkt de productie tot 40. Lees de marktprijs bij deze hoeveelheid op V af: € 10. De overheid koopt hier niets.')+'''
Bij deze hoeveelheid willen kopers € 10 betalen. Dat is hoger dan de oorspronkelijke vrije prijs. Een quotum zet dus niet rechtstreeks een minimumprijs vast, maar beperkt het aanbod. Het kan zo wél de marktprijs verhogen.

'''+box('Controleer ook het quotum','Een quotum van 80 kratten zou hier niet binden: het vrije evenwicht is maar 60. Je produceert dan niet automatisch 80 en leest de prijs dus niet klakkeloos bij 80 af.','small'))

pg('3.1.5','Twee maatregelen vergelijken','''## Uitgewerkt voorbeeld

**Appelkratten.** Vraag P = 14 − 0,10Q; aanbod P = 2 + 0,10Q. Q is kratten per week. Vrij evenwicht: 14 − 0,10Q = 2 + 0,10Q → Q₀ = 60 en P₀ = € 8.

**1 · Minimumprijs controleren.** Pmin = € 10 ligt boven € 8 en bindt.

**2 · Gewenste hoeveelheden berekenen.**

'''+form('10 = 14 − 0,10Qv → Qv = 40<br>10 = 2 + 0,10Qa → Qa = 80<br>Aanbodoverschot = 80 − 40 = 40 kratten')+'''
**3 · De aankoopregel toepassen.** Zonder opkoop zijn er 40 particuliere verkopen. Bij volledige opkoop tegen € 10 koopt de overheid 40 kratten. U = 10 × 40 = **€ 400 per week**. Telers verkopen dan alle 80 kratten.

**4 · Vervang de prijsregeling door een quotum.** Een productiequotum van 40 ligt onder het vrije aantal 60 en bindt. Alle 40 toegestane kratten worden verkocht. De prijs volgt uit de vraag: P = 14 − 0,10 × 40 = **€ 10**. Er is geen aankoopgarantie en U = € 0.

| Uitkomst per week | Minimum + volledige opkoop | Alleen quotum 40 |
|---|---:|---:|
| Particuliere aankopen | 40 kratten | 40 kratten |
| Totale productie en verkoop | 80 kratten | 40 kratten |
| Overheidsaankopen | 40 kratten | 0 kratten |
| Overheidsuitgaven | € 400 | € 0 |

'''+box('Onthouden','Minimumprijs: eerst binding, dan Qv en Qa, dan de aankoopregel. Quotum: eerst binding, dan de toegestane verkochte hoeveelheid en de prijs op V. Veronderstel nooit automatisch opkoop of overheidsinkomsten.','summary')+'''
## Startopgaven

'''+ROUTE+ex(37,'Vraag en aanbod terughalen','Qv = 100 − 5P en Qa = 5P − 20. Q is kratten per week; P is euro per krat.',[
'Bereken het vrije evenwicht en bepaal bij P = € 14 het aanbodoverschot.'
])+ex(38,'Een toegestane prijs','De vrije marktprijs is € 12. De minimumprijs wordt € 9.',[
'Welke marktprijs blijft gelden? Leg uit waarom.'
]))

pg('3.1.5','Lees wat de overheid belooft','''## Begeleide inoefening

'''+SKIP+ex(39,'Het overschot afnemen','Gebruik de appelgrafiek op pagina 30. De overheid garandeert daar volledige opkoop van het aanbodoverschot.',[
'Lees het aantal particuliere aankopen, de aangeboden hoeveelheid en het aantal overheidsaankopen af.',
'Bereken de oppervlakte U. Waarom is de basis niet de totale hoeveelheid 80?',
'Welke hoeveelheid blijft zeker niet automatisch verkocht als de opkoopgarantie vervalt?'
])+ex(40,'Perenkratten','Vraag P = 18 − 0,10Q; aanbod P = 6 + 0,10Q. Het vrije evenwicht is Q₀ = 60, P₀ = € 12. De minimumprijs is € 14. De overheid koopt elk aangeboden krat dat particulieren niet afnemen, tegen € 14. Q is kratten per week.',[
'Vul eerst in: 14 = 18 − 0,10Qv → …; 14 = 6 + 0,10Qa → … . Bepaal het aanbodoverschot.',
'Teken Pmin en markeer Qv en Qa. Arceer de uitgavenrechthoek en bereken U.',
'Vervang de hele regeling door alleen een quotum van 40. Alle 40 kratten worden verkocht en er is geen opkoop. Bepaal prijs, particuliere verkopen en U.'
])+fig('3.1.5_ex_1','Basisgrafiek bij opgave 40. Particuliere vraag en overheidsaankopen zijn verschillende dingen.'))

pg('3.1.5','Aankopen en quota uit elkaar houden','''## Zelfstandige oefening

'''+ex(41,'Pruimenkratten','Vraag P = 22 − 0,10Q; aanbod P = 10 + 0,10Q. Q is kratten per week. De minimumprijs is € 18. De overheid koopt het volledige aanbodoverschot tegen deze prijs.',[
'Bereken het vrije evenwicht. Bereken bij de minimumprijs Qv, Qa en het aanbodoverschot.',
'Bereken de totale verkoop door telers, de overheidsaankopen en U. Teken de uitgavenrechthoek in de basisgrafiek.',
'Vervang de minimumprijs én opkoop door alleen een bindend quotum van 40. Alle 40 kratten worden verkocht. Bereken de marktprijs en vergelijk de productie met de opkoopregeling.'
])+fig('3.1.5_ex_2','Basisgrafiek bij opgave 41. Begin voor de quotumvergelijking opnieuw, zonder de minimumprijsregeling.')+ex(42,'Geen opkoop afgesproken','Een bron noemt een minimumprijs waarbij Qv = 30 en Qa = 70. Een tweede bron noemt gratis verdeelde productiequota. Geen van beide bronnen noemt betalingen door of aan de overheid.',[
'Hoeveel producten worden in de eerste bron zonder opkoop of andere afnemers verkocht? Hoe groot is het aanbodoverschot?',
'Waarom mag je bij geen van beide bronnen automatisch een bedrag aan overheidsuitgaven of inkomsten berekenen?'
]))

pg('3.1.5','Een garantie voor paddenstoelentelers','''## Doeloefening

'''+ex(43,'Paddenstoelen in kratten','Vraag P = 20 − 0,10Q; aanbod P = 8 + 0,10Q. Q is kratten per week; P is euro per krat. Regeling A voert een minimumprijs van € 16 in. De overheid koopt elk aangeboden krat dat particulieren niet kopen, tegen € 16. De telers leveren samen de aangeboden hoeveelheid.',[
'Bereken het vrije evenwicht en leg uit of de minimumprijs bindt.',
'Bereken bij € 16 de particuliere vraag, het aanbod, het aanbodoverschot en de totale verkoop door telers.',
'Bereken de overheidsaankopen en de overheidsuitgaven per week. Markeer in de grafiek Pmin, Qv, Qa en de uitgavenrechthoek.',
'Regeling B vervangt A volledig: een productiequotum van 40 kratten. Alle 40 worden verkocht; de rechten zijn gratis verdeeld en de overheid koopt niets. Bereken de marktprijs, totale productie en overheidsuitgaven.',
'Een teler zegt: “Omdat beide regelingen dezelfde prijs geven, zijn ze economisch hetzelfde.” Beoordeel met twee berekende verschillen.'
],'target')+fig('3.1.5_target','Basisgrafiek bij de doeloefening. Scheid de berekeningen van regeling A en regeling B.'))

pg('3.1.5','Een begrotingsbedrag is nog geen oordeel','''## Denkertje / Bonusopgave

'''+ex(44,'Is de hele rekening verlies?','Bij opgave 43 koopt de overheid 40 kratten voor € 16 per krat. Een bestuurder zegt: “Dat kost € 640; dus het welvaartsverlies is precies € 640.” Er staat niets over het gebruik van de kratten, de waarde daarvan voor ontvangers of eventuele opslagkosten.',[
'Leg uit waarom een overheidsuitgave niet zonder verdere informatie hetzelfde is als welvaartsverlies.',
'Noem twee soorten informatie die je nodig hebt voor een zorgvuldig welvaartsoordeel over deze aankopen. Je hoeft geen nieuwe welvaartsformule te gebruiken.'
],'bonus')+box('Bronnen begrenzen je conclusie','Je kunt de betaling van € 640 precies berekenen. Je kunt zonder extra gegevens niet precies bepalen wat er met de goederen gebeurt en wat de maatschappelijke waarde daarvan is. Houd die twee uitspraken uit elkaar.','small')+'''
## Herhaling / Herhaling en interleaving

'''+ex(45,'Een prijsreactie meten','De prijs van een product stijgt van € 8 naar € 10. De gevraagde hoeveelheid daalt van 80 naar 70 per week. Andere vraagfactoren blijven gelijk.',[
'Bereken Ev met de oude waarden als basis. Classificeer de vraag.',
'Bereken de omzet vóór en na de prijsstijging. Leg uit waarom een omzetstijging geen bewijs van een hogere winst is.'
])+'''
### Kies het juiste onderscheid

Bij een **prijsgrens** vergelijk je eerst met de vrije prijs. Bij een **quotum** vergelijk je eerst met de vrije hoeveelheid. Daarna pas onderzoek je de feitelijke transacties en de geldstromen.

'''+box('Klaar voor combineren','Je kent nu belasting, subsidie, maximumprijs, minimumprijs en quotum. In de gemengde opgaven staat niet bij elke berekening welk model je moet gebruiken. Lees daarom eerst wat de maatregel werkelijk doet.','summary'))

# §3.1.6 — pages 37–39, and recap page 40
pg('3.1.6','Kies eerst de methode','''<a id="s316"></a>
<div class="kicker">3.1.6 · GEMENGDE OPGAVEN: OVERHEIDSINGRIJPEN</div>
# Kies eerst de methode

Hier komt geen nieuwe theorie bij. Gebruik de vraag- en aanbodtechnieken uit Boek 1, de surplus- en elasticiteitskennis uit Boek 2 en de maatregelen uit dit hoofdstuk.

'''+box('Doel van deze paragraaf','Je kiest op basis van de bron de juiste maatregel en rekentechniek. Je verbindt een berekening met een gelabelde grafiek en trekt een conclusie die niet verder gaat dan de gegevens.','goals')+ex(46,'Vier korte berichten','Lees elk bericht afzonderlijk. De vrije marktuitkomst is telkens gegeven of verandert niet door iets anders.',[
'Aanbieders maken per verkocht product € 2 over aan de overheid. Welke maatregel is dit? Welke prijs is dan hoger: Pc of Pp?',
'Aanbieders krijgen € 3 voor elke werkelijk verkochte plaats. Welke maatregel is dit? Over welke hoeveelheid bereken je U?',
'De vrije prijs is € 9, maar verkopen boven € 7 worden verboden. Benoem de maatregel, geef de bindingscontrole en noem welke hoeveelheden je moet berekenen.',
'Producenten mogen samen niet meer dan 50 producten maken; de vrije hoeveelheid zou 70 zijn. Noem de maatregel en waar je de prijs van de 50 verkochte producten afleest.'
])+ex(47,'De ontbrekende aankoopbelofte','Een minimumprijs van € 12 ligt boven de vrije evenwichtsprijs van € 9. Bij € 12 zijn Qv = 30 en Qa = 70. Er is geen overheidsopkoop, geen voorraadverkoop en geen andere afnemer.',[
'Bepaal de werkelijke verkoop, het aanbodoverschot en de overheidsuitgaven.',
'Een voorstel voegt volledige opkoop van het overschot tegen € 12 toe. Bereken de extra overheidsaankopen en U.',
'Waarom veranderen de antwoorden terwijl de minimumprijs zelf gelijk blijft?'
])+box('Aanpak van de doeloefening','Werk de twee plannen afzonderlijk uit. De bronnen staan op pagina 38 en de vragen op pagina 39. Gebruik voor het tekenen de geleverde marktgrafiek.','small'))

pg('3.1.6','Bronnen bij de doeloefening','''## Doeloefening

<div class="target-source"><b>Opgave 48 · Twee plannen voor festivalbandjes</b><br>
Een gemeente onderzoekt de markt voor eenvoudige festivalbandjes. Verschillende aanbieders verkopen hetzelfde product. Alle bedragen en voorstellen zijn fictief.</div>

### Bron 1 · De markt zonder maatregel

Vraag: **Pc = 24 − 0,20Q**. Aanbod: **Pp = 6 + 0,10Q**. Q is bandjes per dag; Pc en Pp zijn euro per bandje. Zonder maatregel is Pc = Pp. Het CS in het vrije evenwicht is € 360 per dag; het PS is € 180 per dag.

### Bron 2 · Twee alternatieven, niet tegelijk

**Plan A.** De aanbieder draagt € 3 af per verkocht bandje. Er zijn geen andere geldstromen of effecten voor buitenstaanders. Ook uitvoeringskosten blijven buiten beschouwing.

**Plan B.** Een verkoopprijs boven € 10 is verboden. Er is geen extra aanvoer. Alle aangeboden bandjes worden verkocht aan de vragers met de hoogste betalingsbereidheid. Er is geen belasting, subsidie of overheidsopkoop.

### Bron 3 · De beleidsclaim

“Plan B maakt een bandje bereikbaar voor iedereen die er bij € 10 een wil. Plan A levert de overheid geld op; dat geld is volledig verdwenen welvaart.”

'''+fig('3.1.6_target','Basisgrafiek bij opgave 48. Gebruik deze voor plan A. De plannen zijn alternatieven: pas ze niet tegelijk toe.')+'''
<div class="small muted">De vragen staan op de tegenoverliggende pagina. Voor plan B volstaan berekeningen en een conclusie; je hoeft geen tweede grafiek te tekenen.</div>
''')

mixedqs=[
'Benoem de maatregelen van plan A en B. Bereken met bron 1 het vrije evenwicht.',
'Bereken voor plan A het nieuwe aanbod in kopersprijzen, de verkochte hoeveelheid, Pc en Pp. Noteer de economische last per bandje voor kopers en verkopers.',
'Bereken bij plan A de overheidsontvangsten, CS, PS en het welvaartsverlies. Gebruik de oorspronkelijke vraag- en aanbodlijn voor de surplusgebieden.',
'Markeer in de basisgrafiek de twee prijzen en de nieuwe hoeveelheid van plan A. Arceer de overheidsontvangsten en het welvaartsverlies verschillend. Benoem beide gebieden.',
'Bereken voor plan B Qv, Qa, werkelijke verkopen en tekort. Controleer eerst of de prijsregel bindt.',
'Beoordeel beide delen van de beleidsclaim uit bron 3. Gebruik minstens één berekening per deel. Geef daarna één verschil tussen de plannen dat voor kopers van belang is; trek geen niet-berekende algemene welvaartsconclusie over plan B.'
]
# Register the complete target once, even though its sources occupy the facing page.
EXERCISES.append({'number':48,'title':'Twee plannen voor festivalbandjes','context':'Bronnen 1–3 op pagina 38; vraag Pc = 24 − 0,20Q en aanbod Pp = 6 + 0,10Q; plan A t=3; plan B Pmax=10.','questions':mixedqs,'kind':'target'})
pg('3.1.6','Vragen bij de doeloefening','''<div class="exercise target" id="opg48">
<p><b>Opgave 48 · Vragen</b></p><p>Gebruik de bronnen en de grafiek op pagina 38. Noteer berekening, eenheid en conclusie.</p>
'''+''.join(f'<p><b>{chr(97+i)}.</b> {q}</p>' for i,q in enumerate(mixedqs))+'''</div>

### Kijk na je berekeningen terug

| Controle | Wat je in je antwoord moet kunnen aanwijzen |
|---|---|
| Modelkeuze | Plan A heeft twee prijzen; plan B één begrensde prijs. |
| Transacties | Geen berekening van budget of surplus over onverkochte bandjes. |
| Geldstroom | Overheidsontvangsten zijn niet volledig welvaartsverlies. |
| Bronconclusie | Een tekort beperkt toegang; een lage prijs garandeert geen aankoop. |

'''+box('Een onderbouwde conclusie','Een bruikbaar antwoord combineert een brongegeven, een berekening en een gevolg. Bijvoorbeeld: “Omdat er maar … bandjes worden aangeboden, kunnen niet alle … vragers kopen.” Vul de getallen zelf in.','small'))

pg('3.1','Hoofdstukoverzicht','''<a id="overzicht"></a>
# Overzicht: één markt, vijf instrumenten

| Instrument | Controle en prijsrelatie | Hoeveelheid en overheid |
|---|---|---|
| Belasting per product | Pc − Pp = t | Nieuw evenwicht; O = t × Qt |
| Subsidie per product | Pp − Pc = s | Nieuw evenwicht; U = s × Qsub |
| Maximumprijs | Bindt als Pmax lager is dan P₀ | Zonder extra aanvoer: verkopen = Qa; tekort = Qv − Qa |
| Minimumprijs | Bindt als Pmin hoger is dan P₀ | Zonder opkoop: verkopen = Qv; overschot = Qa − Qv |
| Productiequotum | Bindt als toegestane Q lager is dan Q₀ | Bij volledige verkoop: prijs op V; budget alleen volgens de bron |

### Vijf begrippenparen die je uit elkaar houdt

**Afdragen en dragen.** Wie belasting overmaakt, draagt niet automatisch de hele last. Gebruik Pc − P₀ en P₀ − Pp.

**Gewenst en werkelijk.** Qv en Qa zijn gewenste hoeveelheden bij een prijs. Lees welke producten daadwerkelijk worden verhandeld.

**Rechthoek en driehoek.** Een bedrag per verkocht product maal de verkochte hoeveelheid geeft een budgetrechthoek. Gemiste voordelen van handel vormen in onze lineaire belastingvoorbeelden een driehoek.

**Geldstroom en welvaartsverlies.** Vergelijk zonder maatregel CS + PS, bij belasting CS + PS + O en bij subsidie CS + PS − U. Dezelfde euro niet dubbel tellen.

**Efficiëntie en verdeling.** Een grotere welvaartsmaat betekent niet dat iedere groep erop vooruitgaat. Een lagere prijs betekent niet dat iedere koper toegang heeft.

'''+form('Vrije markt: stel vraag = aanbod<br>Belasting: aanbod in Pc = oorspronkelijk aanbod + t<br>Subsidie: aanbod in Pc = oorspronkelijk aanbod − s')+box('Voor je antwoord af is','Heb je het juiste plan gekozen? Staan er eenheden bij alle aantallen en bedragen? Klopt de wig? Is de prijs- of hoeveelheidsgrens echt bindend? Is de aankoop- of toewijzingsregel gebruikt? Volgt je conclusie uit de bron?','summary')+'''
<div class="small muted">Grenzen van dit hoofdstuk: geen internationale handel of arbeidsmarktmodel; geen effecten voor buitenstaanders. Belastingen en subsidies worden in Boek 4 opnieuw gebruikt met andere welvaartsveronderstellingen. Een quotum is een regel; productiecapaciteit is wat technisch mogelijk is.</div>
''')

# Streamline the worked-example page without dropping the modelling or retrieval operations.
PAGES[3]['body']='''## Uitgewerkt voorbeeld

**Fruitbekers.** Pc = 14 − 0,10Q en Pp = 2 + 0,10Q. Verkopers dragen € 4 per beker af. Q is bekers per dag.

**1 · Vrij evenwicht.** Zonder belasting zijn beide prijzen gelijk.

'''+form('14 − 0,10Q = 2 + 0,10Q → Q₀ = 60<br>P₀ = 14 − 0,10 × 60 = € 8')+'''
**2 · Nieuw aanbod in kopersprijzen.** De koper betaalt de gewenste ontvangst plus de belasting: Pc = Pp + 4 = 6 + 0,10Q.

**3 · Nieuwe hoeveelheid en beide prijzen.**

'''+form('14 − 0,10Q = 6 + 0,10Q → Qt = 40<br>Pc = 14 − 0,10 × 40 = € 10<br>Pp = 2 + 0,10 × 40 = € 6')+'''
**4 · Controle en uitleg.** 10 − 6 = € 4: de wig klopt. Markeer bij Q = 40 beide prijzen in figuur 2. Kopers betalen € 2 meer dan eerst; verkopers houden € 2 minder over. Afdragen en de last dragen zijn dus verschillend.

'''+box('Onthouden','Gebruik V voor Pc en de oorspronkelijke A voor Pp, beide bij dezelfde nieuwe hoeveelheid. Controleer Pc − Pp = t.','summary')+'''## Startopgaven

'''+ROUTE+''.join(
 f'<div class="exercise" id="opg{n}"><p><b>Opgave {n} · {EXERCISES[n-1]["title"]}</b></p><p>{EXERCISES[n-1]["context"]}</p>'+''.join(f'<p><b>{chr(97+i)}.</b> {q}</p>' for i,q in enumerate(EXERCISES[n-1]['questions']))+'</div>\n\n' for n in [1,2])

# Use a distinct symbol for subsidised quantity to avoid the English Qs / supply ambiguity.
for p in PAGES:
    p['body']=p['body'].replace('Qs','Qsub').replace('Met Qsub bedoelen we hier de hoeveelheid mét subsidie; het aanbod noteren we als Qa.','Qsub is het aantal verkochte plaatsen mét subsidie; Qa blijft de aangeboden hoeveelheid.')
for e in EXERCISES:
    e['context']=e['context'].replace('Qs','Qsub');e['questions']=[q.replace('Qs','Qsub') for q in e['questions']]

def export():
    files=[]
    for sec in ['3.1','3.1.1','3.1.2','3.1.3','3.1.4','3.1.5','3.1.6','overview']:
        selected=([PAGES[0]] if sec=='3.1' else [PAGES[-1]] if sec=='overview' else [p for p in PAGES if p['section']==sec])
        name={'3.1':'00 Inleiding.md','overview':'07 Overzicht.md'}.get(sec,sec+' manuscript.md')
        text='\n\n'.join('<!-- PAGE '+json.dumps({k:v for k,v in p.items() if k!='body'},ensure_ascii=False)+' -->\n\n'+p['body'] for p in selected)
        (ROOT/name).write_text(text,encoding='utf-8');files.append(name)
    (ROOT/'chapter-order.json').write_text(json.dumps(files,ensure_ascii=False,indent=2))
    (ROOT/'exercises.json').write_text(json.dumps(EXERCISES,ensure_ascii=False,indent=2))
    (ROOT/'targets-authored.json').write_text(json.dumps({'status':'authored_for_user_v2_outline_not_integrated_in_repository','exercises':[e for e in EXERCISES if e['kind']=='target']},ensure_ascii=False,indent=2))
    (ROOT/'3.1 Overheidsingrijpen – hoofdstuk.md').write_text('\n\n<div class="page-break"></div>\n\n'.join(p['body'] for p in PAGES))
    print('Designed student pages:',len(PAGES),'exercises:',len(EXERCISES),'targets:',sum(e['kind']=='target' for e in EXERCISES))
if __name__=='__main__':export()
