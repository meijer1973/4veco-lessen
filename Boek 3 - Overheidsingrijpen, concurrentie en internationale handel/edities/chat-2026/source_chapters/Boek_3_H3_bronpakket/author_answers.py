"""Complete authored answer models. Example contexts are fictitious; no empirical claims."""
from pathlib import Path
from html import escape
import json
from author_chapter import fig,box
ROOT=Path(__file__).resolve().parent
E={e['number']:e for e in json.loads((ROOT/'QA'/'exercises.json').read_text())};A={};P=[];BLOCKS={}
def ans(n,items,criteria=None):
 if len(items)!=len(E[n]['subquestions']):raise ValueError((n,'coverage'))
 A[n]={'number':n,'subquestions':[],'criteria':criteria or []}
 b=f'<div class="answer-block" data-answer="{n}"><h3>Opgave {n} · {E[n]["title"]}</h3>'
 for i,(sol,why) in enumerate(items):
  key=f'{n}{chr(97+i)}';A[n]['subquestions'].append({'id':key,'answer':sol,'why':why})
  b+=f'<p data-answer-question="{key}"><b>{chr(97+i)}.</b> {sol}<br><span class="why"><i>Waarom:</i> {why}</span></p>'
 if criteria:b+='<p class="small"><b>Beoordelingscriteria:</b> '+'; '.join(criteria)+'. Andere correct onderbouwde antwoorden zijn mogelijk.</p>'
 BLOCKS[n]=b+'</div>'
 return BLOCKS[n]
def page(section,title,body):P.append({'section':section,'title':title,'body':body})
def build():
 page('3.3.1','Import, export en alternatieve kosten', '''
<div class="kicker">BOEK 3 · HOOFDSTUK 3 · ANTWOORDEN</div>
# Internationale handel
Controleer niet alleen het eindantwoord. Let ook op het gekozen brongegeven, de economische uitleg en de eenheid. Bij open vragen zijn gelijkwaardige formuleringen mogelijk.
<div class="box small"><b>Afronding</b><br>Bewaar tussenuitkomsten. Rond geld zo nodig af op centen en procenten op twee decimalen. Geef de periode bij hoeveelheden en totale bedragen. De cijfers hier leveren meestal gehele uitkomsten op.</div>
'''+ans(1,[
('De opgegeven mogelijkheid is het gebruik van het lokaal door de tekenclub.','Alternatieve kosten zijn het voordeel van de beste niet-gekozen mogelijkheid; er is geen geldbedrag gegeven.'),
('Productiemiddelen voor tassen kunnen niet tegelijk voor andere producten worden gebruikt. Het land geeft andere productie op.','Hetzelfde schaarsteprobleem keert terug, maar de actoren zijn nu producenten in landen.')
])+ans(2,[
('Hout uit Osta is import van Nera. Meubels naar Osta zijn export van Nera.','De richting van de levering wordt bekeken vanuit Nera.'),
('Er ontbreekt een vergelijking van de alternatieve kosten: hoeveel andere productie wordt opgegeven, vergeleken met een ander land?','Een winkelprijs is niet hetzelfde als opgegeven andere productie.')
])+ans(3,[
('“Sol heeft voor beide producten minder middelen nodig dan Terra.” Dat toont een absoluut voordeel van Sol.','Dit vergelijkt de benodigde middelen voor hetzelfde product.'),
('“Terra offert daarvoor minder instrumenten op.” Terra heeft een comparatief voordeel bij kleding.','De vergelijking gaat nu over alternatieve kosten.'),
('“Terra kan zich meer richten op <b>kleding</b>, omdat het daarvoor relatief minder <b>instrumenten</b> opgeeft.”','Het gekozen product volgt uit de lagere alternatieve kosten, niet uit de hoogste absolute productie.')
]))
 page('3.3.1','Bronfeit, gevolg en grens',ans(4,[
('Minder materiaal voor dezelfde kwaliteit kan de kosten verlagen. Daardoor kan de producent bijvoorbeeld goedkoper aanbieden en aantrekkelijker worden voor de inkoper.','De verbetering vereist dat het kostenvoordeel relevant is voor de verkoop; een prijsdaling is niet gegeven.'),
('Minder betrouwbare levering kan klanten kosten als zij de rugzakken op een bepaald tijdstip nodig hebben.','Een lage prijs is niet het enige koopcriterium in de bron.'),
('Niet zeker. Nodig is informatie over hoeveel waarde de inkoper hecht aan op tijd leveren vergeleken met de mogelijke besparing.','De twee veranderingen werken in tegengestelde richting; de bron geeft hun onderlinge gewicht niet.'),
('De bron vergelijkt niet de opgegeven andere productie in Canto met die in een ander land. Er is dus geen bewijs voor een comparatief voordeel.','Lager materiaalgebruik bij één product is nog geen vergelijking van alternatieve kosten.')
])+ans(5,[
('Riva. Het maakt beide producten met minder productiemiddelen, bij verwaarloosbare kwaliteitsverschillen.','Dat is de absolute vergelijking uit de bron.'),
('Riva richt zich meer op gereedschap; Sora meer op servies. Sora geeft voor extra servies minder gereedschap op.','Sora heeft lagere alternatieve kosten van servies; Riva’s relatieve kracht ligt bij gereedschap.'),
('Bijvoorbeeld servies van Sora naar Riva: export voor Sora en import voor Riva.','Eén levering heeft twee benamingen door het verschillende gezichtspunt.'),
('Sora kan ondanks zijn absolute nadeel een comparatief voordeel bij servies hebben en daaruit handelsmogelijkheden halen. De ruilafspraken moeten voor beide partijen aantrekkelijk zijn.','Absoluut minder productief zijn sluit een lagere alternatieve kost niet uit.')
]))
 page('3.3.1','Doeloefening · Aster en Brin',ans(6,[
('De tentdoekproducent levert minder defecten bij dezelfde prijs. Die hogere kwaliteit maakt zijn aanbod aantrekkelijker.','De bron ondersteunt een kwaliteitsverklaring, niet een lagere-prijsverklaring.'),
('De uitspraak is te breed. De bron noemt binnenlandse producenten die de order verliezen en bevat geen gegevens over werknemers in andere bedrijfstakken.','Het voordeel voor de winnaar van de order geldt niet automatisch voor alle anderen.')
])+ans(7,[
('Aster heeft bij beide producten een absoluut voordeel: het heeft voor pompen én jassen minder productiemiddelen nodig, bij dezelfde kwaliteit.','Dit brongegeven vergelijkt middelen per product.'),
('Brin heeft een comparatief voordeel bij jassen: het offert daarvoor relatief minder pompen op. Aster heeft een comparatief voordeel bij pompen.','De alternatieve kosten bepalen de relatieve specialisatie, ook als Aster absoluut sterker is in beide activiteiten.'),
('Aster specialiseert zich meer in pompen; Brin meer in jassen. Jassen van Brin naar Aster zijn export van Brin en import van Aster. Omgekeerd kunnen pompen naar Brin gaan.','De handelsstromen passen bij de relatieve voordelen.'),
('De ruilafspraken moeten voor beide partijen aantrekkelijk zijn ten opzichte van zelf produceren. Het op tijd leveren maakt Asters pompen bovendien aantrekkelijk voor buitenlandse kopers.','De eerste uitspraak gaat over wederzijds voordeel; de tweede over een concreet concurrentiekenmerk.'),
('Onjuist als algemene conclusie. Jassenmakers in Aster kunnen klanten verliezen aan import uit Brin. De bron vermeldt dat nadeel uitdrukkelijk.','Minder middelen per product en mogelijk gezamenlijk handelsvoordeel bewijzen niet dat alle inwoners winnen.')
]))
 page('3.3.1','Bonus en herhaling',ans(8,[
('De advertentie zegt iets over de verkoopprijs. Zij bewijst niet dat het land voor extra koekjes relatief minder andere productie opgeeft dan een ander land.','Een prijsvergelijking en een vergelijking van alternatieve kosten beantwoorden verschillende vragen.'),
('Bijvoorbeeld: “Land A en land B maken koekjes en brood met dezelfde productiemiddelen. Voor extra koekjes geeft land A minder brood op dan land B.” Dan heeft A bij koekjes een comparatief voordeel.','De toegevoegde bron beschrijft de benodigde vergelijking rechtstreeks, zonder getallen.')
],['prijs en alternatieve kosten onderscheiden','twee landen en twee activiteiten benoemen','een heldere vergelijking van opgegeven andere productie'])+ans(9,[
('Procentuele stijging = (25 − 20) / 20 × 100% = <b>25%</b>.','De oude prijs van € 20 is de basis.'),
('Daling = (20 − 25) / 25 × 100% = <b>−20%</b>. De procentuele daling is dus niet even groot als de stijging.','Bij de terugkeer is € 25 de oude prijs; de basis is veranderd.')
])+ans(10,[
('CS van deze koper = betalingsbereidheid − prijs = 35 − 25 = <b>€ 10</b>.','Deze koper betaalt € 10 minder dan hij maximaal wilde betalen.'),
('TO = P × Q = 25 × 40 = <b>€ 1.000</b>. Dit is het geld dat de winkel ontvangt. Voor gezamenlijk CS zijn de betalingsbereidheden van alle kopers nodig.','Ontvangsten en kopersvoordeel zijn verschillende economische grootheden.')
])+box('Herhaal bij een fout','Voor procentuele veranderingen: §1.1.2. Voor consumentensurplus: §2.3.1. Voor TO: §2.1.2.','box small'))
 page('3.3.2','Bij één prijs twee hoeveelheden', '''
## Wereldmarktprijs, import en export
'''+ans(11,[
('Qv = 100 − 2 × 20 = <b>60 producten per week</b>. Qa = 2 × 20 − 20 = <b>20 producten per week</b>.','Je vult dezelfde gegeven prijs in twee verschillende functies in.'),
('Qv = 60 hoort bij binnenlandse kopers. Qa = 20 hoort bij binnenlandse producenten.','Vraag meet verbruik bij deze prijs; aanbod meet binnenlandse productie.')
])+ans(12,[
('Import = Qv − Qa = 70 − 30 = <b>40 kratten per week</b>.','De buitenlandse levering vult het verschil aan.'),
('70 is het totale binnenlandse verbruik. Daarvan worden 30 kratten binnenlands geproduceerd; alleen 40 komen van buiten.','Binnenlands verbruik bestaat hier uit binnenlandse productie plus import.')
])+ans(13,[
('De wereldprijslijn is P = € 20. Het punt op A bij Qa = 40 bepaalt de binnenlandse productie.','Producenten kiezen hun aanbod bij die prijs.'),
('Het punt op V bij Qv = 80 bepaalt het verbruik. De pijl toont de 40 tassen die het buitenland levert.','80 gevraagde tassen minus 40 binnenlandse tassen geeft de import.'),
('De prijs daalt van € 30 naar € 20. Kopers betalen minder, terwijl binnenlandse producenten minder per tas ontvangen.','Eén prijsverandering werkt verschillend voor betalen en ontvangen.')
]))
 page('3.3.2','Een gegeven grafiek aanvullen',ans(14,[
('Binnenlandse productie is <b>40 paren per week</b>; verbruik is <b>80 paren per week</b>. “Productie” hoort bij Qa = 40; “verbruik” bij Qv = 80.','De twee punten liggen op verschillende lijnen bij dezelfde prijs.'),
('Import = 80 − 40 = <b>40 paren per week</b>. Markeer het horizontale verschil tussen Q = 40 en Q = 80.','Er wordt meer binnenlands verbruikt dan geproduceerd.'),
('Kopers betalen € 10 in plaats van € 15; hun CS stijgt. Binnenlandse producenten ontvangen minder en leveren minder; hun PS daalt.','De prijsdaling vergroot het kopersvoordeel en verkleint het producentenvoordeel.')
])+fig('3.3.2_ans_14','Antwoordfiguur bij opgave 14. Productie 40, verbruik 80 en import 40 paren per week.')+ans(15,[
('Bij € 15: productie 30, verbruik 90. Import = 90 − 30 = <b>60 boxen per week</b>.','De wereldprijs ligt beneden de prijs zonder handel.'),
('De prijs voor producenten daalt van € 20 naar € 15. Hun productie daalt van 60 naar 30 boxen per week.','Bij een lagere prijs willen binnenlandse producenten minder leveren.'),
('CS stijgt. Niet iedereen wint: binnenlandse producenten verliezen surplus door de lagere prijs.','Een stijgend totaal is verenigbaar met een daling bij één groep.')
]))
 page('3.3.2','Doeloefening · Kampeermatten',ans(16,[
('Export = Qa − Qv = 90 − 50 = <b>40 kg kaas per week</b>.','Buitenlandse kopers nemen het binnenlandse productieoverschot af.'),
('Producenten ontvangen € 8 in plaats van € 6 per kg. Binnenlandse kopers moeten die hogere prijs ook betalen. PS stijgt en CS daalt.','De uitvoermogelijkheid is gunstig voor verkopers, niet automatisch voor binnenlandse kopers.'),
('Vela is klein en prijsnemend: zijn export verandert de gegeven wereldmarktprijs niet.','Dat is de expliciete modelaanname uit de bron.')
])+ans(17,[
('Bij P = € 30: Qa = <b>60 matten</b> en Qv = <b>100 matten per week</b>. Import = 100 − 60 = <b>40 matten per week</b>.','De wereldmarkt vult het verschil tussen verbruik en productie.'),
('Zonder handel: P = € 40 en Q = 80. Met import: P = € 30 en Qa = 60. Binnenlandse producenten ontvangen minder en produceren minder.','De lagere gegeven prijs leidt tot beweging langs de aanbodlijn.'),
('Het binnenlandse CS stijgt: kopers betalen minder en het verbruik neemt toe van 80 naar 100 matten.','Een lagere prijs vergroot het verschil met de betalingsbereidheid voor kopers.'),
('De conclusie is onjuist. Binnenlandse producenten verliezen surplus, ook als CS + PS samen stijgt.','Het totaal zegt niet dat ieder onderdeel toeneemt.'),
('Noro is volgens de bron klein en prijsnemend. Zijn handelsomvang heeft geen invloed op de wereldprijs.','Dit is een expliciete modelaanname, geen algemeen bewijs voor elk land.')
])+fig('3.3.2_ans_17','Antwoordfiguur bij opgave 17. Het horizontale verschil bij € 30 is de import.'))
 page('3.3.2','Modelgrenzen en herhaling',ans(18,[
('De aanname van beschikbare handel zonder transportproblemen gaat voor het dorp niet op.','Een lage prijs in de haven betekent niet dat het product ook in het dorp beschikbaar is.'),
('De uitspraak is te sterk. Je moet onder meer weten of en tegen welke vervoerskosten graan het dorp kan bereiken.','Zonder bereikbaarheid kun je de wereldprijs niet rechtstreeks als dorpsprijs gebruiken.')
],['de geschonden aanname noemen','havenprijs en bereikbare lokale prijs onderscheiden','aanvullende vervoersinformatie benoemen'])+ans(19,[
('Runo heeft een comparatief voordeel bij schoenen: het offert daarvoor minder meetapparatuur op.','De relevante vergelijking is de opgegeven andere productie.'),
('Ook een land met een absoluut nadeel in beide activiteiten kan een comparatief voordeel in één activiteit hebben. Runo kan zich meer op schoenen richten en die uitvoeren.','Het absolute voordeel bepaalt niet alleen de zin van handel.')
])+ans(20,[
('TO = 5 × 80 = <b>€ 400 per week</b>. GO = 400 / 80 = <b>€ 5 per product</b>.','Totaal gaat over de hele verkoop; gemiddeld over één product.'),
('Extra TO = 5 × 10 = <b>€ 50 per week</b>. MO = ΔTO / ΔQ = 50 / 10 = <b>€ 5 per product</b>.','Elk extra verkocht product levert bij de vaste prijs hetzelfde bedrag op.')
])+box('Herhaal bij een fout','Import en export: figuren 2 en 3 van §3.3.2. Marginale opbrengst: §§2.1.3 en 3.2.1.','box small'))
 page('3.3.3','De belaste hoeveelheid kiezen', '''
## Protectionisme
'''+ans(21,[
('Opbrengst = belasting per eenheid × belaste hoeveelheid = 3 × 40 = <b>€ 120 per week</b>.','Alleen de eenheden waarop de belasting werkelijk geldt, tellen mee.'),
('De vermenigvuldiging gebruikt de belaste hoeveelheid. Bij een invoerheffing zijn dat alleen ingevoerde producten; bij de beschreven algemene belasting zijn alle genoemde eenheden belast.','Het instrument bepaalt de juiste grondslag.')
])+ans(22,[
('Import = 90 − 60 = <b>30 borden per week</b>. Alleen over deze 30 ontvangt de overheid € 2 per bord.','60 borden zijn binnenlands geproduceerd en vallen niet onder deze invoerheffing.'),
('90 is het totale verbruik, niet de import. De breedte moet 90 − 60 = 30 zijn.','De rechthoek stelt alleen ontvangsten over geïmporteerde eenheden voor.')
])+ans(23,[
('De grenzen zijn Qa = 50 en Qv = 70. Het verschil is 70 − 50 = <b>20 geïmporteerde flessen per week</b>.','De import vult aan wat binnenlandse producenten niet leveren.'),
('De grenzen zijn € 20 en € 25 per fles. Het verschil van <b>€ 5 per fles</b> is de invoerheffing.','De wereldprijs blijft gelijk; de heffing verklaart het verschil met de binnenlandse prijs.'),
('Oppervlakte = 20 × 5 = <b>€ 100 per week</b>. Importeurs dragen dit bedrag af aan de overheid. Het is geen ontvangst voor binnenlandse producenten.','Die producenten profiteren van de hogere verkoopprijs, maar ontvangen de belasting niet.')
]))
 page('3.3.3','Twee veranderingen en een beleidsdoel',ans(24,[
('Binnenlandse prijs = wereldprijs + heffing. Begin: 10 + 2 = <b>€ 12</b>. Alleen wereldprijs omlaag: 8 + 2 = <b>€ 10</b>. Alleen heffing omhoog: 10 + 4 = <b>€ 14</b>. Beide: 8 + 4 = <b>€ 12 per boek</b>.','Volgens de bron blijft in elk van deze situaties import bestaan; daarom mag de prijsregel worden gebruikt.'),
('Bij alleen een lagere wereldprijs daalt de binnenlandse prijs van € 12 naar € 10. Verbruik stijgt en binnenlandse productie daalt, zodat import toeneemt.','De vraag- en aanbodlijn blijven gelijk; alleen de gekozen prijs verandert.'),
('Bij beide veranderingen blijft de binnenlandse prijs € 12. Door de onveranderde lijnen blijven productie, verbruik en import gelijk aan het begin.','De twee prijseffecten heffen elkaar precies op.'),
('De leerling bekijkt alleen de heffing. De wereldprijs daalt tegelijk met hetzelfde bedrag als de heffing stijgt.','Een verandering van één component bepaalt niet alleen de som.')
])+ans(25,[
('Import na heffing = 70 − 30 = <b>40 paraplu’s per week</b>. Opbrengst = 2 × 40 = <b>€ 80 per week</b>.','De import na de maatregel, niet het oude of totale verbruik, is belast.'),
('Rechthoek van Q = 30 tot Q = 70 en van P = € 10 tot P = € 12. Breedte 40 paraplu’s per week; hoogte € 2 per paraplu.','Breedte maal hoogte is de eerder berekende € 80 per week.'),
('Ja, het model toont meer binnenlandse productie: 20 → 30 paraplu’s per week. Kopers betalen echter € 12 in plaats van € 10 en gebruiken minder.','Een bereikt productiedoel kan samengaan met een nadeel voor kopers.'),
('Nee. Bij gratis vergunningen zonder invoerheffing ontvangt de overheid niet automatisch geld per geïmporteerde paraplu.','Een hoeveelheidsgrens is geen belastingbetaling.')
]))
 page('3.3.3','Doeloefening · Schoolrugzakken',ans(27,[
('Import = 100 − 60 = <b>40 rugzakken per week</b>. Heffingsopbrengst = 10 × 40 = <b>€ 400 per week</b>.','De heffing wordt alleen over de resterende import ontvangen.'),
('Arceer de rechthoek tussen Q = 60 en Q = 100, en P = € 20 en P = € 30. Breedte: <b>40 rugzakken per week</b>; hoogte: <b>€ 10 per rugzak</b>.','Hoeveelheid per week maal euro per rugzak geeft euro per week.'),
('Binnenlandse producenten ontvangen € 30 in plaats van € 20 en leveren 60 in plaats van 40 rugzakken. Kopers betalen meer en gebruiken 100 in plaats van 120 rugzakken.','De hogere binnenlandse prijs werkt in tegengestelde richting op aanbod en vraag.'),
('Het productiedoel wordt ondersteund door de stijging van 40 naar 60. Maar scholieren betalen meer, zodat “voor iedereen gunstig” niet volgt.','Een doel over productie is niet hetzelfde als een oordeel over alle groepen.'),
('Het alternatief geeft vergunningen gratis en heft geen invoerheffing. Er is dus geen vergelijkbare betaling per ingevoerde rugzak aan de overheid.','Zelfs bij dezelfde importhoeveelheid hoeft de opbrengst niet dezelfde te zijn.')
])+fig('3.3.3_ans_27','Antwoordfiguur bij opgave 27. De rechthoek heeft een oppervlakte van € 400 per week.'))
 page('3.3.3','Grenzen, bonus en herhaling',ans(26,[
('De mogelijke importprijs is 12 + 9 = € 21. Maar de binnenlandse markt bereikt al bij <b>€ 18</b> evenwicht zonder import. € 21 wordt dus niet de binnenlandse prijs.','De prijsregel voor voortgaande import geldt hier niet meer.'),
('Import = <b>0 producten</b> en opbrengst = 9 × 0 = <b>€ 0</b>.','Zonder import zijn er geen ingevoerde eenheden waarover de heffing wordt ontvangen.')
])+ans(28,[
('Een hogere prijs en productie kunnen ondersteunen dat de beschermde producenten meer kunnen afzetten. Ze bewijzen niet dat in het hele land meer banen ontstaan. Zelfs het aantal banen in deze bedrijfstak is niet rechtstreeks gegeven.','Het verband tussen productie, werkgelegenheid en andere bedrijfstakken ontbreekt.'),
('Bijvoorbeeld gegevens over personeelsinzet bij de beschermde producenten en over werkgelegenheid in andere bedrijfstakken die met hogere inkoopprijzen of minder verkoop te maken krijgen.','Voor een landelijke conclusie zijn gegevens buiten deze ene productie-uitkomst nodig.')
],['productie niet gelijkstellen aan banen','sector en heel land onderscheiden','twee relevante informatiebehoeften noemen'])+ans(29,[
('Algemene belasting: 2 × 100 = <b>€ 200</b>. Invoerheffing: 2 × 30 = <b>€ 60</b>.','De belaste hoeveelheid verschilt.'),
('Een gelijk bedrag per product wordt met verschillende hoeveelheden vermenigvuldigd.','Het tarief alleen bepaalt de totale ontvangsten niet.')
])+ans(30,[
('%ΔP = (12 − 10) / 10 × 100% = 20%. %ΔQv = (90 − 100) / 100 × 100% = −10%. Ev = −10% / 20% = <b>−0,5</b>.','Beide percentages gebruiken de oude waarde.'),
('|Ev| = 0,5 &lt; 1, dus <b>prijsinelastisch</b>.','De hoeveelheid reageert procentueel minder sterk dan de prijs.')
]))
 page('3.3.4','Gemengde bronkeuze', '''
## Gemengde opgaven
'''+ans(31,[
('<b>Comparatief voordeel.</b> De vraag gaat over hoeveel andere productie wordt opgegeven.','Dat zijn alternatieve kosten, niet de absolute hoeveelheid benodigde middelen.'),
('<b>Import.</b> Het gaat om wat uit het buitenland wordt gekocht.','Binnenlands verbruik kan deels met binnenlandse productie worden geleverd.')
])+ans(32,[
('Export = Qa − Qv = 100 − 60 = <b>40 kg appels per week</b>.','Het buitenland koopt het verschil tussen productie en binnenlands verbruik.'),
('De teler ontvangt € 3 in plaats van € 2 per kg; de koper betaalt juist die hogere prijs.','Dezelfde prijsstijging is een voordeel voor de verkoper en een nadeel voor de koper.')
])+ans(33,[
('Toren geeft voor extra verpakkingen relatief veel scheepsonderdelen op. Vale geeft daarvoor minder op. Verpakkingen uit Vale kopen kan dus passen bij specialisatie op basis van comparatief voordeel.','Toren kan absoluut sterker zijn en toch een hogere alternatieve kost van verpakkingen hebben.'),
('De levering is export vanuit Vale en import vanuit Toren.','De grens wordt vanuit twee kanten bekeken.'),
('De verpakkingen komen op tijd aan. Dat ondersteunt een voordeel in betrouwbare levering.','Concurrentiepositie gaat ook over leveringskenmerken, niet alleen over productie-efficiëntie.'),
('De bron spreekt de uitspraak tegen: een lokale verpakkingsproducent in Toren verliest een klant.','Voordeel voor één inkopend bedrijf betekent geen voordeel voor alle bedrijven.')
]))
 page('3.3.4','Een beleidseffect erkennen en begrenzen',ans(34,[
('Import = 90 − 70 = <b>20 doeken per week</b>. Opbrengst = 3 × 20 = <b>€ 60 per week</b>.','Alleen de resterende import wordt belast.'),
('De binnenlandse producent ontvangt € 12 in plaats van € 9 en kan 70 in plaats van 50 doeken leveren.','De heffing beperkt de concurrentiedruk van de goedkope import.'),
('De koper moet € 12 in plaats van € 9 betalen; het verbruik daalt van 110 naar 90.','De bescherming heeft een prijs voor gebruikers.'),
('Bijvoorbeeld: “Het productiedoel wordt ondersteund: binnenlandse productie stijgt van 50 naar 70. Dat maakt de heffing niet gunstig voor iedereen, omdat kopers meer betalen.”','De conclusie gebruikt het gekozen criterium en benoemt een tegengesteld belang.')
])+ans(36,[
('De aanname dat de producten volledig gelijkwaardig zijn. De bron noemt verschillen in levensduur en levertijd.','Dan is één prijs niet het enige relevante onderscheid.'),
('Een koper die snel een jas nodig heeft, kan de snelle levering belangrijk vinden. Een andere koper kan meer waarde hechten aan lange levensduur.','Verschillende voorkeuren kunnen bij gelijke prijzen toch verschillende keuzes geven.'),
('Bijvoorbeeld: “In het model met gelijkwaardige jassen is een gelijk prijskaartje voldoende voor die vergelijking. In de bron zijn de jassen niet gelijkwaardig; de voorkeur van de koper bepaalt mede de keuze.”','Je trekt een modelconclusie niet zonder controle door naar een andere situatie.')
],['de gelijkwaardigheidsaanname herkennen','beide bronkenmerken gebruiken','de conclusie beperken tot wat model en bron ondersteunen']))
 page('3.3.4','Doeloefening · Regenjassen',ans(35,[
('Pelta offert voor extra jassen minder machineproductie op. Het heeft dus lagere alternatieve kosten van jassen, ook al gebruikt Nerin absoluut minder middelen voor beide producten.','De bron maakt het verschil tussen absoluut en comparatief voordeel expliciet.'),
('Import = 100 − 60 = <b>40 jassen per week</b>. Opbrengst = 5 × 40 = <b>€ 200 per week</b>.','De import na de heffing bepaalt de ontvangsten.'),
('Jassenmakers ontvangen € 15 in plaats van € 10 en produceren 60 in plaats van 40 jassen. Kopers betalen € 5 meer en gebruiken 100 in plaats van 120.','De stijgende binnenlandse prijs helpt aanbieders en benadeelt gebruikers.'),
('Rechthoek van Q = 60 tot 100 en van P = € 10 tot 15. Breedte = <b>40 jassen per week</b>; hoogte = <b>€ 5 per jas</b>.','Deze oppervlakte is heffing maal ingevoerde hoeveelheid.'),
('Volgens bron C zijn de vergunningen gratis en is er geen invoerheffing. De overheid ontvangt dus niet hetzelfde bedrag per ingevoerde jas.','Een importgrens creëert niet automatisch belastingontvangsten.'),
('Het productiedoel wordt ondersteund: productie stijgt van 40 naar 60. Maar gezinnen betalen € 15 in plaats van € 10 per jas. De conclusie “voor alle inwoners gunstig” is daarom te breed.','De twee concrete gegevens laten zien dat doelbereik en gevolgen voor alle groepen niet samenvallen.')
])+fig('3.3.4_ans_35','Antwoordfiguur bij opgave 35. Alleen de 40 ingevoerde jassen bepalen de breedte.'))
 page('3.3.4','Afsluitende herhaling',ans(37,[
('Belasting per product = 12 − 9 = <b>€ 3</b>. Opbrengst = 3 × 40 = <b>€ 120 per week</b>.','Het verschil tussen kopersprijs en verkopersontvangst is de belastingwig.'),
('De bron zegt dat alle 40 producten belast zijn. Een invoerheffing betreft alleen ingevoerde producten; een deel van de binnenlandse verkoop kan binnenlands geproduceerd zijn.','De bron en de regeling bepalen welke hoeveelheid belast is.')
])+ans(38,[
('TO = 8 × 100 = <b>€ 800 per week</b>. Winst = TO − TK = 800 − 650 = <b>€ 150 per week</b>.','Winst is wat van de opbrengst overblijft na alle opgegeven kosten.'),
('De winst maakt toetreding aantrekkelijk. Door toetreding stijgt het marktaanbod, waardoor de prijs daalt bij gelijkblijvende vraag. Onder de opgegeven concurrentie- en kostenvoorwaarden verdwijnt de economische winst op lange termijn.','Vrije toetreding kan de extra winstmogelijkheid wegnemen.')
])+box('De hoofdstukcheck in woorden','<b>Specialisatie:</b> vergelijk de opgegeven andere productie.<br><b>Handel:</b> lees Qa en Qv bij dezelfde prijs; bepaal het verschil en de richting.<br><b>Bescherming:</b> gebruik de import na de maatregel en controleer of import blijft. Beoordeel daarna het doel én de gevolgen voor groepen.','box summary')+'''
### Beoordelen van open antwoorden
Een antwoord hoeft niet letterlijk met dit antwoordboek overeen te komen. Het moet wel het juiste begrip gebruiken, op de relevante bron steunen en geen sterkere conclusie trekken dan die bron toelaat.

Een verwijzing naar “de economie” is vaak te algemeen. Vraag door: gaat het om kopers, binnenlandse producenten, buitenlandse aanbieders of de overheid? En gaat het om een prijs, een hoeveelheid, een totaalbedrag of een welzijnsoordeel?
''')
 # Keep numerical exercise order while retaining each target on one page.
 P[9]['body']=BLOCKS[24]+'''

| Situatie | Wereldprijs | Heffing | Binnenlandse prijs |
|---|---:|---:|---:|
| Begin | € 10 | € 2 | € 12 |
| Alleen wereldprijs daalt | € 8 | € 2 | € 10 |
| Alleen heffing stijgt | € 10 | € 4 | € 14 |
| Beide | € 8 | € 4 | € 12 |

'''+box('De beslissende vergelijking','De heffing is een onderdeel van de binnenlandse prijs. De wereldprijs kan tegelijk veranderen. Beoordeel daarom niet alleen één onderdeel.','box small')
 P[11]['body']=BLOCKS[28]+BLOCKS[29]+BLOCKS[30]+box('Let op de grens','Een hogere heffing geeft niet automatisch hogere ontvangsten. Als er geen invoer meer plaatsvindt, is de grondslag nul.','box small')
 P[13]['body']=BLOCKS[34]+fig('3.3.4_fig_2','Bij opgave 34: benoem niet alleen de richting, maar verbind elke groep aan een concreet prijs- of hoeveelheidsgegeven.')+box('Onderbouwde conclusie','“De productie neemt toe” erkent het genoemde doel. “Daarom wint iedereen” gaat verder dan de gegevens. Deze twee uitspraken zijn niet gelijkwaardig.','box small')
 P[15]['body']=BLOCKS[36]+BLOCKS[37]+BLOCKS[38]+box('Hoofdstukcheck','Specialisatie: vergelijk alternatieve kosten. Handel: bepaal Qa en Qv bij één prijs. Bescherming: belast alleen de ingevoerde hoeveelheid en benoem de afzonderlijke gevolgen.','box small')
 P.insert(10,{'section':'3.3.3','title':'Van tarief naar opbrengst','body':BLOCKS[25]+BLOCKS[26]+fig('3.3.3_ans_25','Antwoordfiguur bij opgave 25. Alleen de 40 ingevoerde paraplu’s bepalen de breedte.')})
 (ROOT/'Antwoorden.md').write_text('\n\n'.join('<!-- PAGE '+json.dumps({k:p[k] for k in ['section','title']},ensure_ascii=False)+' -->\n\n'+p['body'] for p in P),encoding='utf8')
 (ROOT/'QA'/'answers.json').write_text(json.dumps(list(A.values()),ensure_ascii=False,indent=2))
 print('Answer pages designed',len(P),'Questions',sum(len(a['subquestions']) for a in A.values()))
if __name__=='__main__':build()
