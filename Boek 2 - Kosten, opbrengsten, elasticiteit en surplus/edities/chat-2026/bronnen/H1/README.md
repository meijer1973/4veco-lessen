# Boek 2 – Hoofdstuk 2.1: Kosten en opbrengsten

**Actuele bouwroute:** [platformcontroller](https://github.com/meijer1973/4veco-platform/blob/main/build-scripts/books/EXERCISE-ROUTES.md); [revisie en timing](../../ROUTE-REVISION-2026-09-21.md). De hieronder beschreven lokale scripts zijn ontvangen bouwonderdelen. Gebruik voor nieuwe uitvoer de platformcontroller.


Nieuwe lokale printeditie voor 4 vwo, 6 september 2026. Het leerlingenhoofdstuk telt 34 pagina’s inclusief uitleg en alle opgaven; antwoorden staan afzonderlijk op 20 pagina’s. De volledige docenteninformatie telt 5 pagina’s.

## Lezen en printen

De definitieve PDF’s en zelfstandige HTML-bestanden staan in `output/`. Print het leerlingenhoofdstuk op A4, ware grootte. Bij dubbelzijdig afdrukken: omslaan aan de lange zijde. De SmoothBox-bronnen en vragen zijn als spread op pagina 32–33 geplaatst. De bestanden in `paragrafen/` zijn afzonderlijke PDF- en Markdown-exports; paginanummers blijven gelijk aan de bovenliggende bundel.

## Bewerken: Markdown is de bron

Bewerk de zes bestanden in `manuscript/`, in de volgorde van `chapter-order.json`. Iedere ontworpen pagina begint met een `<!-- PAGE {...} -->`-regel met metadata. De rest is Markdown met enkele HTML-kaders, tabellen en figuurverwijzingen.

Het centrale antwoordenmanuscript is `2.1 Kosten en opbrengsten – antwoorden.md`. De docenteninformatie staat in `Docenten_en_bouwverantwoording.md`. `2.1 Kosten en opbrengsten – hoofdstuk.md` en de inhoud van `paragrafen/` zijn afgeleide exports, geen tweede bron van waarheid.

De grafieken zijn zelfstandig bewerkbare SVG’s, met bijbehorende PNG’s, in `_assets/`. Bewerk voor een reproduceerbare wijziging ook `make_assets.py`. De PNG’s worden ingebed in de PDF’s en HTML. Er worden geen externe afbeeldingen of lettertypebestanden meegeleverd.

## Herbouwen

Benodigd: Python 3.11 of hoger, WeasyPrint met de bijbehorende systeemafhankelijkheden, `markdown-it-py`, `beautifulsoup4`, `cairosvg` en `pymupdf`. De oorspronkelijke bouw gebruikte het lokaal geïnstalleerde lettertype **Lato**. Bij ontbreken daarvan wordt een systeemlettertype gebruikt; dat kan de regelafbreking veranderen. Controleer dan opnieuw iedere pagina. Geen netwerkverbinding is nodig tijdens de bouw.

```bash
python make_assets.py
python build.py
python build_answers.py
python build_teacher.py
python export_paragraphs.py
python validate.py
```

`build.py` meldt de werkelijke paginatelling en eventuele overloop van ontworpen pagina’s. `validate.py` schrijft `validation-report.json`. Een groene lokale technische controle vervangt geen inhoudelijke review of de officiële repositorygates. Bekijk na iedere inhoudelijke, typografische of grafische wijziging de opnieuw gerenderde PDF’s.

## Bronnen en status

Zie `source-manifest.json` voor de geraadpleegde repositoryversie en bronpaden, en de docenteninformatie voor de leerdoelenkoppeling, lesplanning en doelopgavenwijzigingen. De bestaande hoofdstuktekst is niet als schrijfbron gebruikt. De nieuwe uitleg en oefenroute zijn opgebouwd rond de actuele doelen.

De productiecapaciteitsformulering en met name de twee-dagenversie van SmoothBox zijn bewuste wijzigingen ten opzichte van de bevroren targetrecords. Ze zijn transparant verantwoord. Deze bundel is **niet gepusht, gemerged of als officiële repositoryrelease goedgekeurd**. Onafhankelijke inhoudelijke review, eigenaarbesluit over de aangepaste targets, officiële repositoryvalidatie en een praktijktest van de lestijd blijven afzonderlijke stappen vóór een officiële golden-example-status.

## Inhoud van het pakket

- `manuscript/`: canonieke leerlingteksten met paginametadata.
- `2.1 Kosten en opbrengsten – antwoorden.md`: canoniek antwoordmodel.
- `Docenten_en_bouwverantwoording.md`: doelen, planning, keuzes, bronnen en overdracht.
- `_assets/`: 17 SVG/PNG-paren en controleerbare curvegegevens.
- `output/`: volledige PDF- en zelfstandige HTML-versies.
- `paragrafen/`: afgeleide PDF- en Markdown-exports per paragraaf.
- Bouwscripts, bronmanifest en lokaal validatierapport.

Alle bedragen en ondernemingen in de opgaven zijn didactische voorbeelden. De opgaven worden niet gepresenteerd als officiële CvTE-examenopgaven.
