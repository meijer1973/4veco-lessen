# Boek 3 — herziene complete editie

Overheidsingrijpen, volkomen concurrentie en internationale handel · 4 vwo

## Deze herziening

Hoofdstuk 3.1 is na een inhoudelijke herbeoordeling uitgebreid van 40 naar **48 pagina’s**. Hoofdstukken 3.2 en 3.3 en de gekozen omslag zijn inhoudelijk ongewijzigd. De navigatie van het complete boek is aan de nieuwe paginering aangepast.

De beoordeling en concrete veranderingen staan in het herziene bronpakket van 3.1. Er komen drie gerichte oefeningen bij (22A, 40A, 47A); bonus 17 is vernieuwd. Alle zes doeloefeningen van hoofdstuk 3.1 behouden hun inhoud. De oude uitgave is niet overschreven.

## Bestanden

- `Boek_3_Compleet.pdf`: **136 pagina’s**; voorwerk 1–4, hoofdstukken 5–128, begrippenlijst 129–131, formuleoverzicht 132–135; lege keerzijde 136.
- `Boek_3_Compleet_Antwoorden.pdf`: **76 pagina’s**; 71 antwoordbronpagina’s en bladwijzers naar alle **127 oefeningen**. Lege pagina’s 34, 58 en 76 bewaren de juiste dubbelzijdige indeling.
- `Boek_3_Compleet_Docenteninformatie.pdf`: **28 pagina’s**; herziene H1-handleiding en ongewijzigde H2/H3-handleidingen. Lege pagina’s 20 en 28 zijn bewust.
- `inputs/`: herziene drie H1-PDF’s, ongewijzigde zes H2/H3-PDF’s, oorspronkelijke v2-outlines.
- `hoofdstuk-bronpakketten/`: herzien bronarchief van H1 plus oorspronkelijke H2/H3-bronarchieven.
- `manifest.json`: paginering, alfanumerieke oefenindex en opbouw.
- `book-matter/`: begrippenlijst met aangepaste herkomstpagina’s en leeskopie van het boekvoor-/nawerk.
- `build/`: PDF-behoudende assemblage en bijbehorende validator.
- `QA/`: bronidentiteiten, oude vergelijkingshashes, paginamappen, geregistreerde navigatie-ingrepen en controleverslag.

## Afdrukken en terugzoeken

A4, ware grootte/100%, dubbelzijdig, lange zijde. De omslag is evenredig op A4 geplaatst; hij is niet bijgesneden, vervormd of inhoudelijk aangepast.

| Hoofdstuk | Losse leerlingpagina’s | In het boek | Optellen bij losse pagina |
|---|---:|---:|---:|
| 3.1 Overheidsingrijpen | 1–48 | 5–52 | 4 |
| 3.2 Volkomen concurrentie | 1–38 | 53–90 | 52 |
| 3.3 Internationale handel | 1–38 | 91–128 | 90 |

Hoofdstuk 3.1 blijft onder zijn nieuwe budget van 50; de andere hoofdstukken blijven onder 40. Bron/vragen-spreads: **50–51**, **86–87**, **124–125**. Docentenverwijzingen horen bij de losse hoofdstukken; de gezamenlijke leeswijzer bevat bovenstaande omzetting. De historische herbeoordeling achter H1 noemt uitdrukkelijk de oorspronkelijke 40-pagina-editie.

## Reproduceren

```sh
python -m pip install -r requirements.txt
python build/build_book.py
python build/validate_book.py
```

Lato moet lokaal geïnstalleerd zijn; lettertypebestanden worden niet meegeleverd. Gebruik zo nodig `LATO_FONT_DIR`. De assembler wijzigt alleen pagina-navigatie in de PDF-invoer en laat hoofdstukken niet opnieuw vloeien. Bronnen worden gecontroleerd met `QA/input_hashes.json`. De eerdere inputhashes staan afzonderlijk bewaard voor herkomst, niet als actieve bouwinvoer.

De editable H1-bronnen kunnen met hun eigen build worden herzien; een nieuwe hoofdstukinhoud vereist vervolgens bewust vernieuwde invoer, paginamap, oefenindex en controleverwachtingen.

## Controlegrenzen

De 219 gebruikte leerling-, antwoord- en docentbronpagina’s zijn allemaal gerenderd en vergeleken met hun samengestelde tegenhangers. Buiten geregistreerde navigatievakken zijn woordtekst, woordpositie en rasterbeeld behouden. Nieuwe boekpagina’s zijn gerenderd en bekeken. Dit is lokale assemblagecontrole, geen onafhankelijke vakreview, klasproef of nieuwe examenvalidatie. Er is niet naar GitHub geschreven. Geen niet-aangeleverde licentie-, school- of uitgeversgegevens zijn verzonnen.
