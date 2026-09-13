# Boek 2, hoofdstuk 3 — Surplus en welvaart

Zelfstandige, nieuw geschreven drukeditie voor 4 vwo. Datum: 6 september 2026.

## Uitvoer

- `output/Boek_2_H3_Surplus_en_welvaart.pdf`: **38 pagina’s**, inclusief opening, theorie, voorbeelden, opgaven en overzicht.
- `output/Boek_2_H3_Antwoorden.pdf`: **17 pagina’s**, antwoorden bij alle 38 opgaven.
- `output/Boek_2_H3_Docenteninformatie.pdf`: **6 pagina’s**, didactische verantwoording, lesplanning en bronnen.
- `paragrafen/`: Markdown- en PDF-uitvoer per paragraaf, met de bijbehorende beeldbestanden.

Het leerlinghoofdstuk bevat drie uitgewerkte voorbeelden, vier doeloefeningen met samen 22 oorspronkelijke deelvragen, 38 genummerde opgaven en 27 instructieve figuren. Opgavenummers beginnen per paragraaf opnieuw. De elf aanvullende oplossingsfiguren staan uitsluitend in het antwoordenboek.

De contexten en vragen van de doeloefeningen volgen de gelezen doelregistratie; alle uitleg en overige oefenopgaven zijn nieuw gemaakt. De bestaande hoofdstuktekst van hoofdstuk 3 uit de repository is niet gebruikt. De lokale renderer en vormgevingsbasis zijn aangepast uit het eerder geleverde hoofdstuk 2.

## Bronbestanden

De hoofdstukvolgorde staat in `chapter-order.json`. De bewerkbare leerlingtekst staat in `manuscript/`. De commentaarregels `<!-- PAGE {...} -->` markeren ontworpen pagina’s en bevatten hoofdstuk- en paginatitels. `build.py` controleert of de gerealiseerde pagina’s één-op-één aansluiten.

De volledige antwoorden en de docenteninformatie zijn afzonderlijke Markdown-bestanden in de hoofdmap. `make_assets.py` bevat alle figuurspecificaties; `_assets/geometry-data.json` legt functies, snijpunten, veelhoeken en oppervlakten vast. SVG en PNG zijn beide meegeleverd; de PDF gebruikt de scherpe SVG-versie.

`paragrafen/` wordt opnieuw uit de hoofdbronnen gegenereerd. Bewerk daarom bij voorkeur de bronnen in de hoofdmap, niet alleen de exports. De leerling-PDF’s per paragraaf zijn exacte uitsneden van de hoofdstuk-PDF en behouden de hoofdstukpaginanummers. De losse antwoorden-PDF’s worden afzonderlijk gezet.

## Bouwen

Python 3. De geteste afhankelijkheden zijn vastgelegd in `requirements.txt`.

```bash
python -m pip install -r requirements.txt
python build_all.py
```

De bouwscripts gebruiken geen netwerk en schrijven niet naar GitHub. Installeer zo nodig de voor WeasyPrint en Cairo benodigde systeembibliotheken. Voor dezelfde typografie moeten **Lato** en **DejaVu** lokaal beschikbaar zijn. Er worden geen lettertypebestanden meegestuurd. Met andere beschikbare lettertypen kan de tekst anders afbreken; controleer dan opnieuw de pagina-indeling.

Het volledige bouwcommando maakt de figuren, drie boeken, paragraafexports en het lokale validatierapport. Een controlefout levert een niet-nul afsluitcode op.

## Controleren

```bash
python validate.py
```

Zie `QA/validation-report.json` en `QA/VALIDATION.md` voor de getoetste berekeningen, doelvragen, opgaven/antwoorden, beeldverwijzingen, beeldgeometrie en pagina’s. Verwachte numerieke uitkomsten zijn apart van de beeldgenerator vastgelegd. Gebieden worden bovendien onafhankelijk via antiderivatieven en de veelhoeksformule nagerekend.

`QA/LOCAL_REVIEW.md` beschrijft de aanvullende visuele en inhoudelijke zelfcontrole. Dit is **geen onafhankelijke specialistreview, geen officiële platform-CI en geen bewijs van leerlingbeheersing**. De lestijden zijn schattingen; §2.3.3 vraagt bij minder zekere voorkennis bij voorkeur twee lessen.

## Bronnen en status

`provenance/source-register.json` geeft de geraadpleegde bronpaden en blob-ID’s. `provenance/target-transcription.json` is een handmatige controletranscriptie van de vier gelezen doelrecords, niet een volledige download van de doelregistratie.

De GitHub-verbinding kon beide repositorykaarten en de inhoudelijke bronnen lezen. Directe raw-downloads waren in de werkomgeving niet beschikbaar. Historische gereedheidslabels en eventuele repositorygates zijn niet door deze losse uitgave gewijzigd of vrijgegeven. De repositories blijven ongewijzigd.

## Drukken

A4, werkelijke grootte, dubbelzijdig, omslaan over de lange zijde. De 38 leerlingpagina’s blijven binnen de grens van 40. De bronnen en vragen van de gemengde doeloefening staan op de tegenoverliggende pagina’s 34–35. Antwoorden en docenteninformatie zijn niet in die 38 pagina’s opgenomen.
