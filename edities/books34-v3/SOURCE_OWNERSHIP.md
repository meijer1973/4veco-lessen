# Bronbestanden en gegenereerde bestanden

Deze indeling geldt voor de actuele v3-routeherziening. Zie de [platformbouwroute](https://github.com/meijer1973/4veco-platform/blob/main/build-scripts/books/EXERCISE-ROUTES.md) en [wijzigings- en timingnotities](ROUTE-REVISION-2026-09-21.md).

| Bestand | Eigenaarschap en juiste wijzigingsplaats |
|---|---|
| `books/book-N/chapters/N.M/*.md` | Bewerkbare inhoud: hoofdstukinleiding, paragraafmanuscripten, antwoorden en docenttekst. Niet door de bouwscripts herschreven. |
| `books/book-N/chapters/N.M/_assets/*.svg` | Bewerkbare figuurbronnen. Een zichtbaar opschrift zit in de SVG, niet alleen in de bestandsnaam. |
| Bijbehorende `_assets/*.png` | Rasterversies van de SVG. Werk ze bij wanneer de SVG verandert. Voor de vijf herstelde antwoordfiguren: `python build/rasterize_answer_labels.py`. |
| `books/book-N/chapters/N.M/print.css` | Bewerkbare hoofdstukstijl. De boekassembler neemt de stijl van het eerste hoofdstuk als uitgangspunt voor het boekvoorwerk. |
| `chapter-order.json` en `curriculum/chapter-config.json` | Bewerkbare selectie, volgorde en grenzen van de bronbestanden. |
| `books/book-N/book-matter/back.md` | Bewerkbare **gedrukte** begrippenlijst en formule-/werkwijzeoverzicht. De assembler schrijft dit bestand niet meer terug. Een benodigde opmaakomsluiting wordt alleen in het geheugen toegevoegd. |
| `books/book-N/book-matter/glossary.json` | Termeninventaris/telling; alleen deze JSON aanpassen verandert de gedrukte definities in `back.md` niet. Houd beide bij een inhoudelijke wijziging consistent. |
| `books/book-N/book-matter/front.md` | **Gegenereerd** door `4veco-platform/build-scripts/books/books34_assemble.py`, inclusief inhoudsopgave en paginanummers. Pas colofon/inleiding en voorwerkteksten aan in de `front`, `seq`, `boundary`, `body` en `table`-sjablonen van dat script, niet in `front.md`. |
| `books/book-N/book-matter/print.css` | **Gegenereerd** uit de hoofdstukstijl plus de expliciete aanvullingen in `4veco-platform/build-scripts/books/books34_assemble.py`. Een handmatige wijziging aan dit gegenereerde bestand wordt overschreven. |
| `output/*.html`, `output/*.pdf`, `*_page_map.json`, `paragraph-pdfs/` | Gegenereerde publicatie-/controle-uitvoer. Bronwijziging → betreffende hoofdstukken bouwen → boeken samenstellen → records/paragraafexports vernieuwen. |
| `outlines/*.md` | Aangenomen v3-outlinebronnen. De pedagogische amendementen worden door het platform toegepast; actuele PDF-leeskopieën komen uit `books34_outlines.py`. |
| `curriculum/targets/*.json`, gecombineerd doelbestand, catalogus en `target-excerpts/` | Gegenereerd uit de echte manuscripten/antwoorden, outlines, lesroutes en paginamap met `4veco-platform/build-scripts/books/books34_records.py`. Wijzig bij een reparatie de bron of extractor, niet alleen één afgeleide JSON. |
| `checks/route-revision-*.json` | Actuele controles voor deze revisie. Overige checks blijven de eerdere leveringscontrole. De ontvangen v3-bewijsbestanden staan apart in `provenance/received-v3-checks/`; zij zijn geen stilzwijgende goedkeuring van gewijzigde bestanden. |

`build/build_all.py` verwijst naar de naastliggende platformcontroller. De ontvangen `build/assemble.py` en `build/records.py` zijn historische templates, niet de huidige ingang. De platformcontroller voert de afhankelijkheden in de juiste volgorde uit. Het verandert de originele leerlingmanuscripten, antwoordteksten, docentteksten en `back.md` niet. Het bouwt gegenereerd voorwerk, uitvoer en records opnieuw. Voer daarna de aparte platformverificatie uit; die schrijft nieuwe revisiechecks zonder historische controles te overschrijven.

Historische assetnamen met een oud paragraaf-/opgavenummer blijven toegestaan wanneer alle verwijzingen kloppen. Het zichtbare opschrift en de koppeling aan de **actuele** opgave moeten wel overeenstemmen. `checks/figure-label-contract.json` legt dat voor de vijf R1-figuren vast; de controle vergelijkt ook met het actuele doelrecord.
