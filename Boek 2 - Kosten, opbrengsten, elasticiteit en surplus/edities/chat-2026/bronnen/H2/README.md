# Boek 2 · Hoofdstuk 2.2 · Elasticiteit

**Actuele bouwroute:** [platformcontroller](https://github.com/meijer1973/4veco-platform/blob/main/build-scripts/books/EXERCISE-ROUTES.md); [revisie en timing](../../ROUTE-REVISION-2026-09-21.md). De hieronder beschreven lokale scripts zijn ontvangen bouwonderdelen. Gebruik voor nieuwe uitvoer de platformcontroller.


Een nieuw geschreven Nederlandstalige printeditie voor 4 vwo. De bestaande leerlingtekst van hoofdstuk 2.2 is niet als basis gebruikt. De actuele vier doelopgaven en auteursrichtlijnen uit de 4veco-platformrepository zijn wel gevolgd. De vier doelcontexten en 21 deelvragen blijven inhoudelijk en woordelijk behouden; de rest van het hoofdstuk is nieuw gecomponeerd.

## Direct gebruiken

- `output/Boek_2_H2_Elasticiteit.pdf`: 36 leerlingpagina’s, inclusief theorie, voorbeelden, alle oefeningen en overzicht.
- `output/Boek_2_H2_Antwoorden.pdf`: 18 pagina’s met antwoorden, berekeningen, economische uitleg en criteria voor denkertjes.
- `output/Boek_2_H2_Docenteninformatie.pdf`: 6 pagina’s over lesplanning, afstemming, precisie, bronnen en controlegrenzen.
- `paragrafen/`: afgeleide PDF- en Markdownexports per paragraaf, inclusief oefeningen en antwoorden.

De leerlingeditie bevat 38 genummerde opgaven en 13 instructieve figuren. Elk opgavenummer begint per paragraaf opnieuw. Alle voorbeelden zijn fictieve onderwijscontexten; de getallen zijn geen empirische gegevens over echte bedrijven. De doelcontexten Nova en StreamNow worden bewust in §2.2.1 en §2.2.2 hergebruikt omdat de bronautoriteit die koppeling voorschrijft.

**Print:** A4, ware grootte, dubbelzijdig, omslaan aan de lange zijde. Bij een ongewijzigde paginavolgorde staan de StreamPlus-bronnen en vragen op de naast elkaar liggende pagina’s 32–33. Leerlingen werken in een schrift.

## Bronbestanden en afgeleide uitvoer

De canonieke nieuwe manuscriptbestanden staan in `manuscript/`, in de volgorde van `chapter-order.json`. Het centrale antwoordenbestand is `2.2 Elasticiteit – antwoorden.md`. De docentenbron is `Docenten_en_bouwverantwoording.md`. Bewerk deze bestanden, niet uitsluitend de PDF of een kopie in `paragrafen/`.

`make_assets.py` tekent de figuren op exacte numerieke coördinaten en exporteert SVG plus PNG. De eigenschappen waarop de figuurcontroles steunen staan in `_assets/geometry-data.json`. De PNG’s zijn 1.800 pixels breed; de SVG’s blijven bewerkbaar.

`provenance/target_questions.json` bevat de gebruikte doelvraag-excerpten. `provenance/source-register.json` bevat de gelezen repositorypaden, beschikbare Git-blobpins en het bevestigde platform-main-commit. Dit register is een bronverantwoording, geen claim dat een volledige repository is gedownload of gevalideerd.

De geplande pagina-eenheden staan als `<!-- PAGE {...} -->` in de manuscripten. De bouw controleert of elke geplande leerlingpagina inderdaad op één PDF-pagina blijft. Voeg inhoud dus niet onbeperkt toe zonder opnieuw te renderen en te controleren.

## Opnieuw bouwen

Benodigd: Python 3, de pakketten in `requirements.txt`, de native bibliotheken voor WeasyPrint/Cairo, en lokaal beschikbare lettertypen. Deze editie gebruikt Lato en DejaVu Sans/Mono. Er worden **geen lettertypebestanden** meegeleverd. Een andere font- of renderomgeving kan de paginering veranderen; de geleverde PDF’s zijn de gecontroleerde uitvoer.

Vanuit deze map:

```bash
python -m pip install -r requirements.txt
python build_all.py
```

Of stap voor stap:

```bash
python make_assets.py
python build.py
python build_answers.py
python build_teacher.py
python export_paragraphs.py
python validate.py
```

De tekstgrenscontrole van SVG’s gebruikt standaard de systeemfonts onder `/usr/share/fonts/truetype/lato/`. Op een ander systeem kunnen `FONT_REGULAR` en `FONT_BOLD` naar de eigen lokaal geïnstalleerde fonts verwijzen. De fontbestanden worden niet in het bronpakket gekopieerd.

## Didactische opbouw

Elke theorieparagraaf bevat een volledig uitgewerkt voorbeeld van de doelbewerkingen, gevolgd door een compacte samenvatting en de vaste route: Startopgaven, Begeleide inoefening, Zelfstandige oefening, Doeloefening, Denkertje / Bonusopgave en Herhaling / Herhaling en interleaving. De normale route omvat begeleide én zelfstandige oefening; zie de canonieke routeafspraak in het revisierapport.

De docenteninformatie bevat de operationele dekking per doelvraag. De oude kernbegrotingen missen begeleide inoefening en onderbouwen geen volledige 55-minutenroute. Vooral §2.2.3 kan twee lessen vragen; dit wordt niet opgelost door de doelopgave te versmallen. De bonus hoort bij de uitdagende route; herhaling is extra bij beide routes.

## Controle en grenzen

`validation-report.json` rapporteert de werkelijk uitgevoerde lokale structurele, rekenkundige, brongetrouwheids- en PDF-controles. `QA/LOCAL_REVIEW.md` beschrijft de visuele inspectie en correcties. Dit is geen onafhankelijke pedagogische review en geen bewijs van leertempo of leerresultaat.

De repositories zijn niet gewijzigd. Voor opname in de repository zijn nieuwe currentness-controles, de toepasselijke formele validators en onafhankelijke inhoudelijke en visuele review nodig. De lokale editie verandert geen bronstatus, productiehold of mergebevoegdheid.
