# Boek 4 · Hoofdstuk 3 · Arbeidsmarkt

**Leerlingboek: 50 pagina's. Antwoorden: 18 pagina's. Docenteninformatie: 8 pagina's.**

Dit pakket bevat de volledige lokale editie voor 4 vwo: vijf theorie-/toepassingsparagrafen en één gemengde paragraaf. De inhoud volgt de twee door de gebruiker aangeleverde v2-outlines; de nieuw geschreven doeloefeningen werken hun ontwerpbriefs uit. De gevallen en getallen zijn eigen lesmodellen, geen officiële examenopgaven of actuele Nederlandse arbeidsmarktgegevens. Er is niets naar de repositories geschreven.

## Bestanden

- `output/`: de drie definitieve PDF's en zelfstandige HTML-weergaven.
- `4.3 Arbeidsmarkt – hoofdstuk.md`: samengevoegd leerlingmanuscript.
- `4.3.1 manuscript.md` t/m `4.3.6 manuscript.md`: tekst per paragraaf.
- `Antwoorden.md`, `Docenteninformatie.md`: de twee aanvullende manuscripten.
- `_assets/`: bewerkbare SVG's en PNG-uitvoeringen. De PDF bevat vectorfiguren.
- `paragrafen/`: zes afzonderlijke paragraaf-PDF's en Markdown voor uitleg, opgaven en antwoorden. De PDF-uitsneden behouden de hoofdstukpaginanummers.
- `sources/`: de ongewijzigde aangeleverde outlines en een bronregister met rol, adres en bestandshash.
- `QA/`: vraag-antwoordregister, grafiekgeometrie, paginakaarten, reken- en structuurcontrole, visuele review en herbouwcontrole.

Er zijn 50 opgaven met 92 geletterde deelvragen. Sommige deelvragen combineren enkele bekende rekenhandelingen. De zes doeloefeningen bevatten samen 24 deelvragen. Het leerlingboek gebruikt 24 figuurplaatsingen; het antwoordboek bevat acht figuurplaatsingen. Eén figuur komt in beide voor. Het generatorpakket bevat ook vier niet-gebruikte varianten voor bewerking; die tellen niet mee als onderwijsfiguur.

## Reproduceren

Getest met Python 3.13.5, de versies in `requirements.txt`, WeasyPrint en de systeemlettertypen Lato en DejaVu Sans / DejaVu Sans Mono. Lettertypebestanden worden niet meegeleverd. Voor WeasyPrint en CairoSVG zijn de gebruikelijke systeembibliotheken voor Pango/Cairo vereist. Een andere lettertypeomgeving kan regels en pagina's anders afbreken: controleer dan de PDF opnieuw.

```bash
python -m pip install -r requirements.txt
python build_all.py
```

**Let op:** `author_431.py` t/m `author_436.py` en de overige `author_*.py`-bestanden zijn de auteurssjablonen met de tekst en antwoorden. `build_all.py` genereert de Markdown opnieuw en overschrijft handmatige wijzigingen daarin. Het script maakt ook alle figuren, PDF's en paragraafuitsneden en voert de controles uit. Een mislukte stap stopt de bouw.

Voor alleen het opnieuw opmaken van handmatig gewijzigde Markdown:

```bash
python build.py
```

Pas bij inhoudelijke wijzigingen ook de auteurssjablonen, vraag-antwoordregistratie en bijbehorende onafhankelijke controles aan. Gebruik `python validate.py` voor de bestaande editiecontrole en `python export_paragraphs.py` voor de afzonderlijke uitsneden. Het leerlingboek mag niet boven 50 pagina's uitkomen. Geplande pagina's die anders afbreken geven een foutmelding.

## Wat de controles wel en niet aantonen

De rekencontrole bevat onafhankelijk genoteerde rekengevallen voor uitleg, voorbeelden en opgaven. Zij controleert ook een selectie van de daadwerkelijk afgedrukte antwoordwaarden. De grafiekcontrole leest de werkelijke SVG-lijnen, punten en loonsomrechthoek terug. Andere controles betreffen ontbrekende afbeeldingen, één-op-één vraag-antwoorddekking, de zeven oefenkoppen, de paginering, navigatie en tekst buiten de PDF-pagina. De gedetailleerde onderdelen staan in `QA/validation_report.json`; het totale aantal tests is geen kwaliteits- of leereffectscore.

De gerenderde bladzijden zijn daarnaast visueel nagekeken. De review is lokale redactionele controle, geen onafhankelijke specialistische goedkeuring, repository-CI of gemeten leerwinst. De lestijden in de docenteninformatie zijn ontwerpschattingen. Het materiaal is niet getest bij leerlingen.

## Gebruik en drukken

A4, werkelijke grootte, dubbelzijdig, omslaan over de lange zijde. De bronnen en vragen van gemengde doeloefening 49 staan op tegenoverliggende pagina's 46–47. Het leerlingboek bevat geen antwoordmodellen. Antwoorden en docentmateriaal zijn afzonderlijke bestanden.

De bronregisters onderscheiden duidelijk: de outline bepaalt de inhoudelijke volgorde en grenzen; de geraadpleegde repositorybestanden bepalen de werkvorm; CBS en Rijksoverheid ondersteunen alleen de aangegeven begripsomschrijvingen. De lokale productie promoveert geen voorstel tot formeel goedgekeurde doelopgave.
