# Boek 4 — Hoofdstuk 2: Marktvormen en marktfalen

Zelfstandige printuitgave voor economie, 4 vwo. Bouwdatum: 8 september 2026.

## Uitgave

- Leerlingtekst: **60 pagina’s**, inclusief inleiding, uitleg, opgaven, overzicht en begrippenlijst.
- Antwoordboek: **24 pagina’s**, los van de leerlingtekst.
- Docenteninformatie: **9 pagina’s**, los van de leerlingtekst.
- **60 opgaven, 169 deelvragen, 6 volledig uitgewerkte voorbeelden en 7 nieuw ontworpen doeloefeningen.**
- 32 figuren in de leerlingtekst en 12 oplossingsfiguurverwijzingen in het antwoordboek; één figuur wordt gedeeld. Er zijn 43 unieke SVG/PNG-paren.

Alle bronteksten, bedragen en functies voor de oefeningen zijn nieuw ontworpen leermodellen, geen actuele bedrijfsgegevens of overgenomen officiële examenvragen. De doeloefeningen werken de ontwerpbrieven uit de meegeleverde outline uit. Dit pakket wijzigt geen repository, doelregister of eerder geleverd boek.

## Ontwerpprioriteit

De actuele gebruikersopdracht bepaalt het maximum van 60 leerlingpagina’s. De aangeleverde v2-outlines bepalen inhoud, volgorde en afbakening. De online repositoryrichtlijnen bepalen onder meer de geprinte oefenroute en grafische precisie. De oudere repositoryhoofdstukken zijn geen inhoudelijke basis voor deze nieuwe tekst. De outlinebestanden zijn ongewijzigd opgeslagen in `sources/`.

De geprinte kernroute is Startopgaven → Zelfstandige oefening → Doeloefening. Begeleide inoefening is een ondersteuningsoptie. Bonus en afsluitende herhaling worden niet allemaal opgeteld bij de verplichte lestijd. Voor beide externe-effectenparagrafen is een tweelessenroute voorzien; de complete kern is daar niet als één les van 55 minuten gepresenteerd.

## Bestanden

- `output/`: definitieve leerling-, antwoord- en docenten-PDF’s plus zelfstandige HTML-bestanden.
- `paragrafen/`: zeven leerlingexports en zeven antwoordexports, met oorspronkelijke hoofdstukpaginanummers.
- `00 Inleiding.md`, `4.2.1 manuscript.md` t/m `4.2.7 manuscript.md`, `08 Overzicht.md`: rechtstreeks bewerkbare leerlingtekst met expliciete paginamarkeringen.
- `Antwoorden.md`, `Docenteninformatie.md`: bewerkbare bijbehorende teksten.
- `4.2 Marktvormen en marktfalen – hoofdstuk.md`: tijdens de bouw samengestelde leerlingbron.
- `_assets/`: berekende vectorfiguren (SVG) en PNG-spiegels.
- `author_*.py`: gestructureerde auteursbronnen, inclusief elke vraag en het bijbehorende antwoord.
- `make_assets.py`: figuurproductie met functies, punten, arceringen en geometrisch controlebestand.
- `print.css`, `build.py`: A4-opmaak, HTML/PDF-bouw, paginacontrole en navigatie.
- `validate.py`, `QA/`: rekencontroles, daadwerkelijke SVG-coördinaten, vraag-/antwoorddekking, bronnen, paginering en lokale visuele-reviewnotities.
- `sources/source-register.json`: bronidentiteiten, gelezen repositorybereiken en taakafbakening.

## Opnieuw bouwen

Getest met Python 3.13.5 en de versies in `requirements.txt`. WeasyPrint/CairoSVG vereisen de bijbehorende systeembibliotheken voor Pango, Cairo en fontconfig. De opmaak gebruikt lokaal geïnstalleerd Lato, met DejaVu Sans als terugval. Er zijn geen fontbestanden meegeleverd. Andere geïnstalleerde fonts of rendererversies kunnen paginering beïnvloeden.

```bash
python -m pip install -r requirements.txt
python build_all.py
```

Deze standaardroute gebruikt de bestaande Markdown. Zij regenereert de SVG/PNG-bestanden, bouwt drie PDF’s, valideert de vaste uitgave en maakt de losse paragraafexports. Een inhoudelijke wijziging kan vereisen dat vastgelegde verwachte uitkomsten en paginaplan bewust worden aangepast; fouten worden niet stilzwijgend genegeerd.

Wie de auteursmodules bewerkt en vragen plus antwoorden samen wil regenereren gebruikt:

```bash
python build_all.py --regenerate-manuscripts
```

**Let op:** deze optie overschrijft rechtstreekse Markdown-wijzigingen. Bewerk dus óf de auteursmodules óf de gegenereerde Markdown bewust. Bij inhoudelijke revisies moeten de vraag-/antwoordregistratie en de controleverwachtingen eveneens aansluiten. Na elke revisie blijven een rekenkundige en visuele beoordeling noodzakelijk.

## Drukken en gebruik

A4, werkelijke grootte, dubbelzijdig, omslaan aan de lange zijde. De bronnen en vragen van de gemengde doeloefening staan op de tegenoverliggende pagina’s **56–57**. De leerlingtekst heeft klikbare inhoud en paragraafbladwijzers. Antwoorden staan uitsluitend in het afzonderlijke antwoordboek.

De lesduur is een ontwerpschatting, geen gemeten klassenuitkomst. De lokale controles vormen geen onafhankelijke externe review of officiële examenprogramma-/repositoryvrijgave. Lees `QA/visual-review.md` en de docenteninformatie voor de precieze reikwijdte.
