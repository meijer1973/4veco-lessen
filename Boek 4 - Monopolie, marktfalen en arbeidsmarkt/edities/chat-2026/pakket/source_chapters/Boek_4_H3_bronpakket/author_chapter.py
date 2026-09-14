"""Create the initial manuscripts and the source exercise registry.
Run only intentionally: this overwrites Markdown edits. build.py only renders.
"""
from author_common import *
section('front')
page('Arbeidsmarkt','''<div class="kicker">BOEK 4 · HOOFDSTUK 3 · ECONOMIE 4 VWO</div>
<div class="cover-title">Arbeidsmarkt</div>
<div class="lead">Als de prijs loon heet</div>

Een werkgever zoekt personeel. Een werknemer zoekt een baan. Je herkent vraag en aanbod, maar de rollen zijn anders dan bij het kopen van een product. Dit hoofdstuk maakt die vertaling stap voor stap.

<div class="contents">
<a href="#s431"><b>4.3.1 Arbeidsvraag en arbeidsproductiviteit <span>2</span></b>Arbeid, productie en loonkosten per product.</a>
<a href="#s432"><b>4.3.2 Arbeidsaanbod, participatie en evenwicht <span>12</span></b>Wie doet mee? Welk loon brengt vraag en aanbod bij elkaar?</a>
<a href="#s433"><b>4.3.3 Werkloosheid en veranderingen <span>20</span></b>Tellen, verklaren en een nieuw evenwicht onderzoeken.</a>
<a href="#s434"><b>4.3.4 Minimumloon <span>29</span></b>Loonvloer, werkgelegenheid en totale loonsom.</a>
<a href="#s435"><b>4.3.5 Vakbonden, cao en arbeidsmarktbeleid <span>37</span></b>Een voorstel beoordelen met berekeningen en argumenten.</a>
<a href="#s436"><b>4.3.6 Gemengde opgaven: arbeidsmarkt <span>44</span></b>Zelf de passende gegevens en methode kiezen.</a>
<a href="#overzicht"><b>Hoofdstukoverzicht en begrippen <span>49</span></b>Formules, eenheden en betekenis bij elkaar.</a>
</div>
'''+box('Na dit hoofdstuk','Je kunt productie naar arbeidsinzet vertalen, deelname en werkloosheid berekenen, loon en werkgelegenheid in een model bepalen en arbeidsmarktbeleid beoordelen met een passende berekening en een onderbouwde conclusie.','goals')+
'''<p class="school-note">Alle bedrijven, regio’s, voorstellen en cijfers in de opgaven zijn geconstrueerde lesvoorbeelden. Lonen zijn illustratief, geen actuele wettelijke tarieven. Je werkt in je schrift; gebruik de gegeven grafieken waar de opgave dat vraagt. Antwoorden staan in een apart antwoordboek.</p>''')
import author_431,author_432,author_433,author_434,author_435,author_436
section('back')
page('Hoofdstukoverzicht','''<a id="overzicht"></a>
# Arbeidsmarkt in één overzicht

### Eerst rollen en eenheden
Werkgevers **vragen arbeid**; huishoudens **bieden arbeid aan**. Loon **w** is euro per uur, tenzij de bron anders zegt. Hoeveelheid **L** kan personen of arbeidsuren zijn. Eén fte is een voltijd-equivalent, geen persoon.

'''+table(['Vraag','Rekenroute','Eenheid of controle'],[['Hoe productief is arbeid?','productie / arbeidsinzet','Bij uren: producten per arbeidsuur.'],['Hoeveel arbeid is nodig?','productie / productiviteit','Gebruik dezelfde periode.'],['Wat kost arbeid per product?','uurkosten / productie per uur','Euro per product.'],['Hoeveel fte is dit?','totale uren / uren voltijdbaan','Beide in dezelfde periode.']])+
'''### Wie telt mee in welk percentage?
'''+table(['Maatstaf','Teller','Noemer'],[['Bruto-participatie','Werkenden + werklozen','Bevolking in de opgegeven groep'],['Netto-participatie','Werkenden','Dezelfde bevolking'],['Werkloosheidspercentage','Werklozen','Beroepsbevolking']])+
'''Deel de teller door de noemer en vermenigvuldig met 100%. Vacatures worden niet van het aantal werklozen afgetrokken.

### Een arbeidsmarktmodel gebruiken
**Evenwicht:** stel Lᵥ = Lₐ, los op naar w, vul terug in en geef betekenis aan de eenheden.

**Verandering:** benoem de oorzaak en de verschuivende lijn. Een verandering van alleen het loon is een beweging langs een lijn. Geef aan of loon kan aanpassen.

**Minimumloon:** bepaal eerst het vrije evenwicht. Alleen een hogere loonvloer bindt. Bereken dan vraag, aanbod en de betaalde arbeid. Gebruik voor de loonsom bij personen:

'''+formula('loonsom per week = w × uren per persoon × werkenden')+
'''### Een cao of beleid beoordelen
Bereken de loonkosten per product, neem opgegeven extra kosten mee en toets aan het criterium. Met hetzelfde basisjaar geldt: **kostenindex = index uurkosten / index productiviteit × 100**. Noem ook een voorwaarde. Een kostenvoordeel per product is nog geen bewijs van meer banen.
''')
page('Begrippenlijst', '''# Begrippenlijst
<div class="glossary-columns">
<p><b>Arbeidsaanbod</b><br>Arbeid die huishoudens bij een bepaald loon willen aanbieden. In bevolkingsbronnen wordt het actuele aanbod in personen vaak met de beroepsbevolking aangeduid.</p>
<p><b>Arbeidsproductiviteit</b><br>Productie per eenheid arbeidsinzet, bijvoorbeeld per gewerkt uur.</p>
<p><b>Arbeidsvraag</b><br>Arbeid die werkgevers bij een bepaald loon willen inzetten. In de gebruikte tellingen: werkgelegenheid plus vacatures.</p>
<p><b>Beroepsbevolking</b><br>Werkenden plus werklozen, binnen het gekozen leeftijdsbereik.</p>
<p><b>Bindend minimumloon</b><br>Loonvloer boven het vrije evenwichtsloon, die dat evenwicht uitsluit.</p>
<p><b>Bruto-arbeidsparticipatie</b><br>Beroepsbevolking als percentage van de bevolking in de opgegeven groep.</p>
<p><b>Cao</b><br>Collectieve arbeidsovereenkomst: gezamenlijke afspraken over arbeidsvoorwaarden.</p>
<p><b>Conjuncturele werkloosheid</b><br>Werkloosheid door te weinig vraag naar goederen en diensten.</p>
<p><b>Evenwichtsloon</b><br>Loon waarbij arbeidsvraag en arbeidsaanbod in het model gelijk zijn.</p>
<p><b>Flexwerk</b><br>Werk met bijvoorbeeld tijdelijke contracten of wisselende uren.</p>
<p><b>Frictiewerkloosheid</b><br>Werkloosheid doordat zoeken en overstappen tijd kost. Hier onderdeel van structurele werkloosheid.</p>
<p><b>Fte</b><br>Fulltime-equivalent: arbeidsduur omgerekend naar voltijdbanen.</p>
<p><b>Loonkosten per product</b><br>Loonkosten gedeeld door de geproduceerde hoeveelheid.</p>
<p><b>Loonsom</b><br>Totale loonbetaling voor daadwerkelijk betaalde arbeid in een periode.</p>
<p><b>Minimumloon</b><br>Ondergrens aan het loon; niet automatisch het feitelijk betaalde loon.</p>
<p><b>Netto-arbeidsparticipatie</b><br>Werkenden als percentage van de bevolking in de opgegeven groep.</p>
<p><b>Niet-beroepsbevolking</b><br>Mensen zonder betaald werk die niet recent zoeken of niet direct beschikbaar zijn.</p>
<p><b>Structurele werkloosheid</b><br>Werkloosheid door onder meer een blijvend veranderde vraag naar arbeid of een slechte aansluiting tussen werk en werknemers.</p>
<p><b>Vacature</b><br>Arbeidsplaats waarvoor nog iemand wordt gezocht.</p>
<p><b>Vakbond</b><br>Organisatie die belangen van werknemers behartigt en over arbeidsvoorwaarden kan onderhandelen.</p>
<p><b>Werkgelegenheid</b><br>De bezette arbeidsplaatsen of hoeveelheid verrichte arbeid; let op personen, banen, uren of fte.</p>
<p><b>Werkloze beroepsbevolking</b><br>Mensen zonder betaald werk die recent hebben gezocht en direct beschikbaar zijn.</p>
<p><b>Zzp’er</b><br>Zelfstandige zonder personeel, niet hetzelfde als een flexwerknemer.</p>
</div>
<p class="school-note">Begripscontrole: CBS, Arbeidsdeelname; kerncijfers en begrippen arbeidsvolume (geraadpleegd 8 september 2026). Cao: Rijksoverheid, Wat is een cao? De docententoelichting bevat de bronverantwoording. Alle numerieke gevallen in dit hoofdstuk zijn eigen lesmodellen.</p>
''')
assert len(PAGES)==50,len(PAGES)
assert len(EXERCISES)==50,len(EXERCISES)
finish_sources()
