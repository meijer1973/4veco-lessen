# Boek 4 — Monopolie, marktfalen en arbeidsmarkt

Samengestelde editie voor 4 vwo, 8 september 2026.

## Uitgaven

- `output/Boek_4_Compleet.pdf` — 162 pagina’s. Omslag, colofon, voorwoord, inhoud, 148 oorspronkelijke hoofdstukpagina’s, vijf pagina’s begrippen en vijf pagina’s formule- en aanpakoverzicht.
- `output/Boek_4_Compleet_Antwoorden.pdf` — 64 pagina’s; uitwerkingen bij 148 opgaven, met opgavenbladwijzers.
- `output/Boek_4_Compleet_Docenteninformatie.pdf` — 28 pagina’s, inclusief twee bewuste blanco keerzijden (10 en 20).

## Wat behouden is

Alle 234 oorspronkelijke pagina’s uit de leerling-, antwoord- en docentenbestanden zijn opgenomen. De leerlinghoofdstukken zijn niet herschreven of opnieuw gezet. Alleen paginering, klikbestemmingen, de hoofdstukinhoudsopgaven en twee regels met expliciete lokale paginaverwijzingen zijn gewijzigd. Hoofdstuk- en opgavennummers zijn behouden.

De drie leerlinghoofdstukken staan op 5–42, 43–102 en 103–152. De doelopgavespreads blijven tegenover elkaar: 38–39, 98–99 en 148–149. De gezamenlijke begrippenlijst staat op 153–157; het formuleoverzicht op 158–162. De 58 begrippen behouden alle 62 bronformuleringen; vier termen hebben afzonderlijke toelichtingen uit twee hoofdstukken.

De laatst gekozen omslag met Prijsdiscriminatie is pixelgetrouw opgenomen. De miniatuurgrafieken op die omslag zijn geen gecontroleerde rekenbronnen. De docenteninformatie benoemt specifiek de resterende fout in de monopolyhoeveelheid en de ontbrekende optimalisatie in het middenpaneel. Er is niet stilzwijgend een andere omslag gebruikt.

## Bronbestanden

- `inputs/`: oorspronkelijke hoofdstuk-PDF’s, gekozen omslag en laatst aangeleverde v2-outlines.
- `source_chapters/`: uitgepakte oorspronkelijke hoofdstukbronpakketten, inclusief Markdown, SVG/PNG, antwoordmodellen en hun oorspronkelijke controles.
- `book-matter/`: geëxtraheerde begrippen (`glossary.json`), bronafgeleide formuleoverzichten (`formulas.json`) en paginamap van nieuw voor- en nawerk.
- `manifest.json`: hoofdstukken, lokale paragraafposities, opgaven en uitvoerbestanden.
- `build/`: assemblage en validatie. Het voorwoord en colofon staan in `build_book.py`.
- `qa/`: input-hashes, alle geregistreerde wijzigingen, uitvoermanifest, actuele assemblagecontrole en lokale visuele-reviewnotitie. De controles in `source_chapters/*/QA/` horen bij de oorspronkelijke hoofdstukproductie, niet bij een nieuwe inhoudelijke beoordeling.

## Reproduceren

Vereist: Python 3, PyMuPDF, ReportLab, Pillow, NumPy, BeautifulSoup4. Installeer Lato lokaal. Het pakket bevat geen losse fontbestanden. De assemblage zoekt standaard in systeemfontmappen; gebruik desgewenst `LATO_FONT_DIR`.

```sh
python -m pip install -r requirements.txt
python build/build_book.py
python build/validate_book.py
```

`build_book.py` weigert te bouwen als een input-hash niet meer klopt. Na een bewuste inhoudelijke vervanging van inputs kan `build/prepare_inputs.py` de manifest- en begrippenextractie vernieuwen; controleer daarna opnieuw de paginaverdeling en bronconsistentie. Voer geen hoofdstuk-auteurscript uit voor een gewone boekbundeling.

De grafieken en onderwijsinhoud zijn niet opnieuw door specialisten of tegen actuele exameneisen beoordeeld. De boekcontrole vergelijkt alle bronpagina’s buiten de geregistreerde navigatiegebieden, inclusief ongewijzigde tekst en woordposities. De gekozen omslag wordt ook op exacte ingesloten pixels gecontroleerd.

## Afdrukken

A4, werkelijke grootte (100%), dubbelzijdig, omslaan over de lange zijde. Alle hoofdstukopeningen beginnen rechts. Antwoorden blijven buiten het leerlingboek. De oorspronkelijke verwijzingen in de hoofdstukhandleidingen zijn lokale leerlingpaginanummers; de omzettingstabel voorin de gezamenlijke docentenhandleiding zet deze om.

Er zijn geen wijzigingen naar repositories geschreven. Er zijn geen school-, uitgever-, contact- of licentiegegevens verzonnen.
