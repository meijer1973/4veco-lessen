from author_common import *
section('4.3.5')
page('Samen afspraken maken',begin('Meer loon én ruimte voor scholing?',
'Je kunt uitleggen wat vakbonden en werkgevers in een cao afspreken. Je kunt loon- en productiviteitsveranderingen vergelijken. Je kunt met een berekening, mechanisme en voorwaarde een beleidsvoorstel beoordelen.',
'Werknemers willen meer loon en tijd om zich te ontwikkelen. Werkgevers willen voldoende goede medewerkers en beheersbare kosten. Een afspraak kan over beide gaan. Beoordeel daarom het hele voorstel, niet alleen het loonpercentage.')+
box('Definitie · cao','Een collectieve arbeidsovereenkomst bevat schriftelijke afspraken over arbeidsvoorwaarden voor een groep werknemers. Eén of meer werkgevers of werkgeversorganisaties sluiten haar met één of meer werknemersorganisaties, zoals vakbonden.','definition')+
fig('bargaining','De cao kan loon, werktijden, verlof en scholing combineren. Het is geen afspraak van iedere werknemer afzonderlijk.')+
'''Een **vakbond** behartigt belangen van werknemers. Zij kan namens hen onderhandelen over collectieve arbeidsvoorwaarden. Werkgevers kunnen samen worden vertegenwoordigd door een werkgeversorganisatie.

**Flexwerk** betreft werk met bijvoorbeeld een tijdelijk contract of wisselende uren. Een **zzp’er** werkt als zelfstandige zonder personeel. Dat is niet hetzelfde als een werknemer met een flexibel contract. De bron moet duidelijk maken welke groep een voorstel betreft.

Deze begrippen zeggen nog niet automatisch iets over productiviteit, inkomen of baanzekerheid in één concrete situatie. De institutionele beschrijving van de cao sluit aan bij Rijksoverheid; alle voorstellen in de opgaven zijn fictief.
''')
page('Van loonafspraak naar kosten en werk', '''### Vergelijk geen losse groeipercentages
De bekende verhouding uit §4.3.1 blijft gelden: **loonkosten per product = uurkosten / productie per uur**. Stel dat de uurkosten 5% stijgen en de productiviteit 12,5%. Reken dan beide bedragen per product uit.

'''+fig('cao_costs','Een stijging van de uurkosten kan samengaan met een daling van de loonkosten per product.')+
formula('index loonkosten per product =<br>(index uurkosten / index arbeidsproductiviteit) × 100')+
'''Met hetzelfde basisjaar: 105 / 112,5 × 100 = **93,33**. De kosten per product dalen dus met **6,67%**. Het verschil 12,5% − 5% = 7,5% is niet de exacte uitkomst. De twee grootheden staan in een verhouding.

### Vraag steeds hoe een voorstel werkt
Een afgesproken hoger loon verandert de beloning. Scholing kan vaardigheden verbeteren en de productie per uur verhogen. Scholing kan ook helpen om een bestaande vacature te vullen. Dat zijn verschillende mechanismen.

Een grotere productiviteit vermindert benodigde uren bij **gelijkblijvende productie**, maar maakt extra productie mogelijk. Hoeveel mensen uiteindelijk werken, hangt ook af van de opdrachten en de arbeidsduur. Alleen lagere loonkosten per product bewijzen dus geen banengroei.
'''+box('Criterium → bewijs → voorwaarde','Bijvoorbeeld: beoordeel of kosten per product dalen; gebruik uurkosten en productiviteit als bewijs; vermeld dat opleidingskosten, kwaliteit en andere kosten ertoe doen. Een advies is sterker als je duidelijk zegt waarop het berust.','summary'))
page('Uitgewerkt voorbeeld',heading('Uitgewerkt voorbeeld')+
source('Cao-voorstel voor keukentextiel','Vakbonden en werkgevers bespreken meer loon en scholing. Uurloon en volledige uurkosten stijgen beide met 5%. De uurkosten gaan van € 24 naar € 25,20. Productiviteit stijgt door het nieuwe werkproces van 4 naar 4,5 producten per uur. De opleiding kost in het eerste jaar daarnaast € 0,25 per geproduceerd product. Andere kosten per product en kwaliteit blijven gelijk. Het criterium is: dalen de kosten van arbeid plus opleiding per product?')+
'''### 1 · Benoem de afspraak en de partijen
Werknemersorganisaties en werkgevers maken een collectieve afspraak over loon en scholing. Een cao betreft dus meer dan alleen de verkoopprijs van een arbeidsuur.

### 2 · Bereken de loonkosten per product
Oud: € 24 / 4 = **€ 6 per product**.<br>
Nieuw: € 25,20 / 4,5 = **€ 5,60 per product**.<br>
Verandering: (5,60 − 6) / 6 × 100% ≈ **−6,67%**.

Controle met indexcijfers: 105 / 112,5 × 100 = 93,33. De kostenindex ligt 6,67 onder 100.

### 3 · Neem de extra kosten uit de bron mee
Arbeid plus opleiding: € 5,60 + € 0,25 = **€ 5,85 per product**.<br>
Verschil met eerst: € 6 − € 5,85 = **€ 0,15 lager per product**.

### 4 · Geef een begrensd oordeel
Het voorstel voldoet aan het genoemde kostencriterium, **als de veronderstelde productiviteitswinst wordt gehaald**. Het loon per uur stijgt terwijl de kosten van arbeid plus opleiding per product dalen.

Daaruit volgt niet dat automatisch meer werknemers nodig zijn. Als de productie gelijk blijft, zijn door de hogere productiviteit minder uren nodig. Extra opdrachten kunnen die uitkomst veranderen. De bron geeft geen complete voorspelling van de werkgelegenheid.
'''+box('Samenvatting §4.3.5','Een cao legt collectieve arbeidsvoorwaarden vast. Vergelijk loonkosten en productiviteit per product, niet met een losse aftrekking. Beoordeel beleid met een criterium, brongegevens en voorwaarden. In §4.3.6 kies je zelf de passende berekening en verklaring.','summary'))
page('Start en een voorstel lezen',start()+
ex('Index en verhouding','Een broodjesfabriek had uurkosten van € 20. Die worden € 22. De productiviteit was en blijft 5 broodjes per arbeidsuur.',[
('Bereken de index van de uurkosten met de oude situatie als 100.',ans('€ 22 / € 20 × 100 = <b>110</b>.','De index vergelijkt de nieuwe waarde met dezelfde oude basis.')),
('Bereken de nieuwe loonkosten per broodje.',ans('€ 22 / 5 = <b>€ 4,40 per broodje</b>.','Bij gelijkblijvende productiviteit worden de hogere uurkosten over hetzelfde aantal producten verdeeld.'))])+ 
ex('Wie onderhandelt?', 'Een bedrijfstak bespreekt gezamenlijke loon- en scholingsafspraken.',[
('Welke twee soorten organisaties kunnen deze cao met elkaar afsluiten?',ans('Een of meer werknemersorganisaties, zoals vakbonden, en een of meer werkgevers of werkgeversorganisaties.','Het gaat om collectieve afspraken tussen de partijen op de arbeidsmarkt, niet om een individueel koopcontract van consumenten.'))])+guided()+
ex('Controleer beide tellers','In een tapijtfabriek gaan volledige uurkosten van € 30 naar € 31,50 en productiviteit van 5 naar 6 producten per uur. Andere kosten per product veranderen niet.',[
('Bereken eerst de oude en nieuwe loonkosten per product.',ans('Oud: € 30 / 5 = <b>€ 6 per product</b>. Nieuw: € 31,50 / 6 = <b>€ 5,25 per product</b>.','Je vergelijkt twee bedragen met dezelfde eenheid.')),
('Bereken daarna de procentuele verandering van die kosten.',ans('(5,25 − 6) / 6 × 100% = <b>−12,5%</b>.','De productiviteit groeit sterker dan de volledige uurkosten.'))]))
page('Zelf een argument opbouwen',guided().replace('## Begeleide inoefening','<div class="continuation">Begeleide inoefening · vervolg</div>')+
ex('Van berekening naar voorwaarde','Een reparatiebedrijf verwacht loonkosten per reparatie van € 12 vóór en € 11,40 na scholing. De scholing kost € 0,80 per reparatie extra. De kwaliteit en alle overige kosten blijven gelijk.',[
('Tel eerst de nieuwe arbeids- en scholingskosten per reparatie op. Beoordeel of het voorstel aan het criterium “lagere kosten per reparatie” voldoet.',ans('Nieuw = € 11,40 + € 0,80 = <b>€ 12,20 per reparatie</b>. Dat is € 0,20 hoger dan € 12: het voorstel voldoet <b>niet</b> aan dit kostencriterium.','Je moet de extra scholingskosten meenemen; alleen lagere loonkosten zijn niet genoeg.')),
('Kan iemand het voorstel toch steunen? Geef één mogelijk ander criterium, zonder te doen alsof de bron dat voordeel bewijst.',ans('Bijvoorbeeld grotere inzetbaarheid of aantrekkelijker werk. Dat kan een ander criterium zijn, maar de bron toont niet aan hoe groot dat voordeel is.','Verschillende beoordelingscriteria kunnen tot andere voorkeuren leiden.'))])+heading('Zelfstandige oefening')+
ex('Twee indices','In een sector is de index van volledige uurkosten 108 en die van arbeidsproductiviteit 104. Beide gebruiken hetzelfde basisjaar = 100.',[
('Bereken de index en procentuele verandering van de loonkosten per product.',ans('108 / 104 × 100 = <b>103,85</b> afgerond. De kosten per product stijgen met <b>3,85%</b>.','Delen door de productiviteitsindex geeft de kosten van dezelfde hoeveelheid productie.'))])+ 
ex('Scholing bij openstaande banen','Een regio heeft werkloze winkelmedewerkers en vacatures voor monteurs. Een scholingsplan leert kandidaten de benodigde techniek. De bron vermeldt dat zij na scholing aan de functie-eisen voldoen, maar niet dat werkgevers extra orders krijgen.',[
('Leg één mechanisme uit waarmee het plan werkloosheid kan verminderen. Leg ook uit wat je niet over de totale arbeidsvraag kunt concluderen.',ans('De scholing verbetert de aansluiting tussen kandidaten en bestaande vacatures. Daardoor kunnen meer vacatures worden vervuld. Extra totale arbeidsvraag is niet aangetoond: de bron geeft geen extra orders of nieuwe arbeidsplaatsen.','Een betere match is iets anders dan meer gevraagde arbeidsplaatsen.'))]))
page('Doeloefening',heading('Doeloefening')+
ex('Cao in de houtbewerking','Vakbonden en werkgeversorganisaties bespreken loon en scholing. Uurloon en volledige uurkosten stijgen beide 5%. De tabel geeft het plan voor het eerste jaar.'+
table(['Grootheid','Oud','Met plan'],[['Volledige uurkosten','€ 30','€ 31,50'],['Productiviteit (delen/uur)','5','5,5'],['Extra opleidingskosten per deel','€ 0','€ 0,20']])+ 'Kwaliteit en overige kosten per deel blijven gelijk. De productiviteitsverbetering moet in de praktijk nog worden gehaald. Het beoordelingscriterium is: lagere kosten van arbeid plus opleiding per deel. Een werkgever zegt bovendien: “Dit plan zorgt gegarandeerd voor meer banen.”',[
('Benoem de partijen die hier een cao willen afsluiten en noem de twee onderdelen van de afspraak.',ans('Vakbonden namens werknemers en werkgeversorganisaties namens werkgevers. De afspraak gaat over <b>loon en scholing</b>.','De cao is een collectieve arbeidsvoorwaardelijke afspraak.')),
('Bereken de loonkosten per deel vóór en na het plan en hun procentuele verandering. Rond pas het eindantwoord af.',ans('Oud = 30 / 5 = <b>€ 6 per deel</b>. Nieuw = 31,50 / 5,5 = <b>€ 5,72727… ≈ € 5,73 per deel</b>. (5,72727… − 6) / 6 × 100% ≈ <b>−4,55%</b>.','De productiviteit stijgt 10%, sterker dan de uurkosten van 5%.')),
('Beoordeel het plan met het gegeven kostencriterium. Neem de opleiding mee en noem een voorwaarde.',ans('Arbeid plus opleiding = 5,72727… + 0,20 = <b>€ 5,92727… ≈ € 5,93 per deel</b>. Lager dan € 6, dus het plan voldoet, <b>mits de productiviteitswinst wordt gehaald</b>.','De winst in loonkosten per deel is groter dan de extra opleidingskosten.')),
('Beoordeel de garantie van meer banen. Betrek de productie en arbeidsduur bij je antwoord.',ans('De garantie volgt niet. Bij dezelfde productie zijn minder arbeidsuren nodig. Meer orders kunnen de productie en arbeidsinzet verhogen; een andere arbeidsduur per persoon verandert ook het aantal personen. De bron geeft die uitkomsten niet.','Kosten per product zijn niet hetzelfde als het totale aantal banen.'))],points=[2,3,3,2]))
page('Denkertje en herhaling',heading('Denkertje / Bonusopgave')+
ex('Een contractlabel is geen verklaring','Twee schoonmaakbedrijven hebben evenveel betaalde uren en dezelfde omzet. Het ene gebruikt tijdelijke werknemers, het andere vaste werknemers. Een commentator zegt: “Tijdelijk werk is dus productiever.”',[
('Beoordeel de redenering. Formuleer welke informatie je nodig hebt voor een goede productiviteitsvergelijking en benoem één ander criterium dat een werknemer belangrijk kan vinden.',
'Het contractlabel bewijst geen hogere productie per uur. Voor een vergelijking zijn onder meer dezelfde soort en kwaliteit van diensten, gemeten productie en gewerkte uren nodig. Dezelfde omzet kan uit andere prijzen bestaan. Een werknemer kan bijvoorbeeld voorspelbare uren of inkomenszekerheid belangrijk vinden.<br><b>Beoordelingscriteria:</b> verwerpt een conclusie uit alleen het label; onderscheidt omzet van productie; noemt een relevante ontbrekende grootheid en een ander criterium.')])+heading('Herhaling / Herhaling en interleaving')+
ex('Een bekende subsidie','Een gemeente vergoedt € 25 per afgeronde cursus. Er worden 40 cursussen afgerond. De bron geeft geen cijfers over externe baten of overige kosten.',[
('Bereken de gemeentelijke uitgaven. Kun je alleen daarmee de welvaartswinst bepalen?',ans('Uitgaven = € 25 × 40 = <b>€ 1.000</b>. De welvaartswinst is hiermee niet te bepalen: effecten op deelnemers, aanbieders, andere partijen en kosten ontbreken.','Een subsidiebedrag is een overdracht en niet op zichzelf het totale maatschappelijke voordeel. Herhaal bij moeite §§3.1.3 en 4.2.5.'))])+
box('Terugblik','Een sterk advies bevat een criterium, een controleerbare berekening, een economische oorzaak-gevolgketen en een voorwaarde. Het hoeft geen stellige voorspelling te zijn.','summary'))
