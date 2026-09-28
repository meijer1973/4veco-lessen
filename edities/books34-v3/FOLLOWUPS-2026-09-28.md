# Boeken 3 en 4: navigatie, antwoordkop en docentadvies

Deze beperkte opvolger gebruikt de samengevoegde getekende-elasticiteitsrevisie
als basis: Lessons `794cd54fe68f9b9a1bb413462373a133a459345c`, Platform
`1761cb96ef25da67b7830fade96e17d7a4db53ac`. De acht getekende
elasticiteitsfragmenten en de bestaande berekeningen blijven behouden.

## Wat is gewijzigd?

- **NAV1:** de hoofdstukinhouden van 3.1, 3.3, 4.2 en 4.3 zijn ook in de
  complete leerlingboeken klikbaar. De assembler bewaart alle 99 annotaties
  voor 25 vermeldingen, inclusief rechthoeken, doelpagina en doelpositie.
  De hoofdstukbronnen 3.2 en 4.1 bevatten zelf geen dergelijke koppelingen;
  deze opvolger voegt daar geen nieuwe navigatie toe. De hoofdinhouden blijven
  werken. Alle leerlingpagina's behouden hun tekst, beeld en paginanummer.
- **Antwoordkop:** boven opgaven 29/30 in §3.2.3 staat nu “Herhaling 29 en 30”,
  op lokale antwoordpagina 17 en pagina 51 van het complete antwoordboek.
  De antwoorden zelf zijn ongewijzigd.
- **TIMING34:** alle 25 theorieparagrafen hebben een concreet, uitsluitend
  docentgericht planningsadvies. Reserveer voorlopig twee lessen van 55 minuten.
  Les 1 omvat startopgaven, motivatie, uitleg, voorbeeld, samenvatting/overgangen
  en begeleid oefenen. Les 2 biedt ruimte voor afronding van begeleiding,
  zelfstandig werk, de volledige doeloefening en feedback. De lesgrens is flexibel.
  Bij 3.1.2, 3.1.3, 3.1.5, 4.2.4 en 4.2.5 houdt de docent extra uitloop vrij.

Het advies is **geen gemeten tijd en geen bewezen 110-minutenfit**. Noteer de
werkelijke lees-, reken-, teken-, bespreek- en feedbacktijd per fase en pas de
volgende planning aan. De opdracht om bruikbare docentaanbevelingen te leveren
is hiermee ingevuld; de empirische lestijd is niet vastgesteld. De eerdere
onvolledige schattingen, onbekende totaaltijden en vijf bekende conflicten blijven
in `curriculum/lesson-routes-v3.json` herkenbaar. Voor de uitdagende route begroot
de docent ook de bonus; herhaling is aanvullend bij beide routes. De
[canonieke routeafspraak](https://github.com/meijer1973/4veco-platform/blob/main/skills/econ-exercise-builder.md#21-the-routes-and-the-constraint)
blijft leidend.

De zes gemengde paragrafen (3.1.6, 3.2.4, 3.3.4, 4.1.5, 4.2.7 en 4.3.5)
behouden hun bestaande structuur en krijgen geen automatische tweelessenplanning.
Er zijn geen oefeningen, antwoorden, doelen, paragrafen of curriculumlessen
toegevoegd of geschrapt. De leerlingtekst en Part B veranderen niet.

## Bouw en actuele controle

Volg de [platformbouwroute](https://github.com/meijer1973/4veco-platform/blob/main/build-scripts/books/BOOKS34-FOLLOWUPS.md).
De bewerkbare bronnen zijn de zes `Docenteninformatie.md`-bestanden en
`books/book-3/chapters/3.2/Antwoorden.md`. De platformcontroller bouwt het
antwoordhoofdstuk expliciet vóór assemblage, daarna docenthoofdstukken,
boekvoorwerk, complete delen en records. Alle 32 afhankelijke publicatiepaden
(waarvan 14 PDFs) worden gecontroleerd; onveranderde paginamappen blijven gelijk.
De vier antwoordbronhashes van hoofdstuk 3.2 en het gecombineerde doelbestand
worden via de recordgenerator bijgewerkt. Alle 31 doelinhouden en statussen blijven.

De complete delen blijven Boek 3 **132 / 74 / 22** pagina's en Boek 4
**166 / 68 / 28** pagina's (leerling / antwoorden / docent). Boek 4-antwoorden,
paragraafexports en ongewijzigde afhankelijkheden behouden de geaccepteerde bytes.

`books34-followups-revision.json` in de repositoryroot en de platformpin binden
de actuele bestanden. `checks/followups-build.json` en
`checks/followups-verification.json` beschrijven de nieuwe bouw en controle.
Oude manifesten, pins, ontvangstgegevens en reviewrapporten blijven historische
bewijzen. Zij zijn niet herschreven om deze wijzigingen te accepteren. De
onafhankelijke review en exacte CI-paarbinding staan bij de gekoppelde PRs.
Deze opvolger verleent geen nieuwe doelgoedkeuring of toestemming tot samenvoegen.
