# Nederlandse notatie en woordformules — 1 oktober 2026

Deze begrensde revisie verwerkt het aangeleverde pakket van 25 september in de actuele bewerkbare editie. De Library-kopie waaruit het proefboek is gemaakt, verschilt van de repositorybasis. Alleen de gevraagde wijzigingen zijn overgenomen; het proefboek is geen bouwinvoer. De herkomst en originele pakketmanifesten staan in `provenance/notation-20261001/`. Die map bewaart historische aanwijzingen en is geen actuele bouwinstructie.

## Bronnen en bouw

Bewerk `bronnen/H*/manuscript/` voor de leerlingtekst, het hoofdstukbestand `*antwoorden.md` voor antwoorden en `*Docenten*.md` voor docenteninformatie. Theorie bestaat uit bewerkbare tekst, echte breuken, semantische tabellen en afzonderlijke figuren. De zeven opnieuw ingedeelde pagina’s zijn eenmalig uit de aangeleverde vormgeving naar die componenten overgezet. De grafiek van SchaalWerk staat als bewerkbare geometrie in `_assets/notation-20261001/page-023.json` en behoudt TK = 80 + Q² en Q = 0–12.

Vanuit de gekoppelde platformcheckout:

```text
python -X utf8 build-scripts/books/rebuild_book2_notation.py --all
python -X utf8 build-scripts/books/verify_book2_notation.py
node build-scripts/maintenance/check-books34-v3-import.js --require-tracked
```

Gebruik de gepinde Pythonafhankelijkheden in `requirements-exercise-routes.txt` en de Lato/DejaVu-fontomgeving van deze editie. Figuren en tekstrendering lopen in aparte processen: samen veroorzaakten hun native fontbibliotheken in de lokale Windowsomgeving een heapfout. Bouwresultaten worden pas geaccepteerd na een foutloze volledige bouw en controles. `--assemble` controleert de bestaande huidige bronregistratie; het accepteert geen stilzwijgend gewijzigde hoofdstukken.

`notation-chapter-inputs.json`, `notation-navigation.json`, `notation-page-map.json`, `notation-assembly-manifest.json` en `notation-verification.json` beschrijven de huidige versie. De oudere `signed-*`, `route-*`, importbewijzen en het 43-pagina-extract blijven historische, ongewijzigde bewijsstukken. Het nieuwe 46-pagina-extract en het vijfpagina-extract van §2.1.3 worden uit het complete nieuwe boek opgebouwd.

## Wijzigingen en behouden inhoud

- Qv en Qa vervangen Qd en Qs in de leerlingtekst, antwoorden en docenteninformatie. De uitleg over twee notaties is vervangen door de Nederlandse definities. Negen herhalingskoppen heten nu “Herhaling en combineren”.
- §2.1.3 toont eerst de woordbreuken en introduceert daarna Δ. Linoprint en Atelier Boog hebben elk een pagina. PlakLab, WafelWagen, het kostenoverzicht en geselecteerde vraag-/aanbodberekeningen scheiden onafhankelijke formules duidelijker.
- SportLint, opgave 5, heeft MK- en MO-invulkolommen. Het antwoord bevat de volledige tabel en dezelfde berekeningen: MK = 4 en MO = 9 voor beide intervallen.
- Alle 114 genummerde oefeningen, gegevens, leerdoelen en doelhandelingen blijven behouden. De huidige targetautoriteit is ongewijzigd; Qd→Qv en Qs→Qa in doelfragmenten zijn alleen equivalente notatie. Er is geen nieuwe curriculum- of PV-vrijgave.
- De normale route met begeleide inoefening, de getekende elasticiteitsuitleg en de eerdere omslagcorrecties blijven behouden. Boek 1, Boeken 3/4 en Part B wijzigen niet.

## Paginering en gebruik

| Bundel | Hoofdstukpagina’s | Fysieke pagina’s | Gedrukte pagina’s |
|---|---|---:|---|
| Leerlingenboek | 35 / 36 / 38 | 111 | 1–109 |
| Antwoorden | 21 / 18 / 17 | 58 | 1–56 |
| Docenteninformatie | 5 / 6 / 6 | 19 | 1–17 |

Omslag en inhoudsopgave blijven ongenummerd. In het leerlingenboek is alleen §2.1.3 één pagina langer: theorie 19–23, startopgaven 24 en SportLint 25. Oude gedrukte pagina’s vanaf 23 verschuiven één positie; hoofdstuk 2.2 begint op 36, hoofdstuk 2.3 op 72. De extra antwoordpagina volgt uit de volledige SportLint-uitwerking; hiervoor zijn geen antwoorden geschrapt of samengedrukt.

De hoofdinhoudsopgaven hebben nu 15 / 3 / 3 klikbare regels; samen met de hoofdstuklinks zijn er 101 / 47 / 3 links. Paginanummers, bladwijzers, overzichtslinks en de koppelingen vanuit paragraafexports worden op hun huidige bestemmingen gecontroleerd. Opgavenexports beginnen bij de eerste echte opgave, inclusief de bestaande gedeelde theorie/startpagina in §2.3.2, zodat eerdere theorie niet onbedoeld als opgavenblad wordt meegeleverd.

**Docenten:** de extra leerlingpagina verschuift de dubbelzijdige paginavouw. SmoothBox 33–34, StreamPlus 67–68 en de gemengde doelopgave van hoofdstuk 2.3 op 105–106 staan achter elkaar, maar niet tegenover elkaar. Houd het bronblad tijdens het werken los beschikbaar of laat leerlingen terugbladeren. Er is geen extra blanco pagina ingevoegd om dit te verbergen.

De eerdere timingbeperking blijft staan: voor de negen theorieparagrafen van Boek 2 is geen gemeten begroting van de volledige ondersteunde route beschikbaar. De extra uitleg geeft geen onderbouwing voor een 55-minutenclaim. Plan naar behoefte extra lestijd; de doeloefening en begeleiding blijven volledig beschikbaar.

## Bewijs

De bron-/uitvoerregistratie is een afzonderlijk begrensd vervolg op de geaccepteerde Git-basis, geen hernieuwde goedkeuring van oude hashes. De platform-PR bevat de onafhankelijke review met dekking van alle twaalf paragrafen en bindt het nieuwe revisiemanifest. De lokale controles vergelijken hoofdstukken en exports met de volledige bundels, inclusief tekst, pixels, paginanummers en links. Het actuele manifest is bewijs van de gecontroleerde bestanden; het geeft op zichzelf geen mergebevoegdheid.

De afzonderlijke actiecheck `lesson_authoring` voor §2.3.3 meldt nog de bestaande `H-CHAPTER-23-PLAN`-hold voor nieuwe hoofdstukproductie; §2.1.3 slaagt. Deze door de eigenaar gevraagde revisie gebruikt de eerder geaccepteerde chat-2026-editie en de route voor begrensde revisies. De huidige controle dekt dit verschil en de publicatieafhankelijkheden; zij is geen vrijgave van de open hold of van nieuwe curriculumproductie.
