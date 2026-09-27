# Boeken 3 en 4 — actuele v3-uitgave

**Getekende prijselasticiteit, 26 september 2026:** [actuele bouwroute en afbakening](SIGNED-RETRIEVAL-2026-09-26.md). Twee leerlingvragen en zes antwoordtoelichtingen vergelijken Ev rechtstreeks met −1 en 0. De bestaande berekeningen, doelen, nummering en routes blijven behouden. De antwoordhoofdstukken zijn expliciet herbouwd; deze opvolger krijgt eigen bewijs en vervangt geen historische review.

**Routeherziening 21 september 2026:** [wijzigingen, tijdsconflicten en structuuruitzonderingen](ROUTE-REVISION-2026-09-21.md). De oorspronkelijke levering hieronder is de historische basis; de actuele tekst en uitvoer zijn opnieuw gebouwd.

**Levering:** `book34-v3-r1-r5-20260916` · **curriculum:** `book34-lesson-balance-v3-20260915`.

Dit pakket vervangt de eerdere v3-levering. De vijf figuurnummers, context-export, registervoorbereiding en UTF-8-afhandeling zijn hersteld. De aanvullende reviewinstructies zijn verwerkt in de actuele handoff. **Alleen dit pakket is nodig; voeg de oude extra herstelopdracht niet opnieuw toe.**

## De complete boeken

| Boek | Leerlingboek | Antwoorden | Docenteninformatie |
|---|---|---|---|
| **3** | [132 pagina’s](books/book-3/output/Boek_3_Compleet_v3.pdf) | [74 pagina’s](books/book-3/output/Boek_3_Compleet_Antwoorden_v3.pdf) | [22 pagina’s](books/book-3/output/Boek_3_Compleet_Docenteninformatie_v3.pdf) |
| **4** | [166 pagina’s](books/book-4/output/Boek_4_Compleet_v3.pdf) | [68 pagina’s](books/book-4/output/Boek_4_Compleet_Antwoorden_v3.pdf) | [28 pagina’s](books/book-4/output/Boek_4_Compleet_Docenteninformatie_v3.pdf) |

De hoofdstukken tellen respectievelijk **48/34/38** en **48/60/44** leerlingpagina’s. De indeling blijft **14 paragrafen (6+4+4)** en **17 (5+7+5)**. Alle **31 manuscripten en paragraaf-PDFs**, de zes hoofdstukken met antwoorden en docentmateriaal, 31 gevulde kandidaat-doelrecords en de bewerkbare bronnen zijn aanwezig.

De inhoud en nummering blijven behouden: **276 opgaven, 734 deelvragen**. Alleen de acht genoemde vraag-/antwoordfragmenten zijn later tekstueel aangepast. De 31 targets bevatten **156 deelvragen**. De eerdere vijf figuurcorrecties en de routeherziening blijven behouden.

## Begin hier

Begin met [de huidige getekende-elasticiteitsrevisie](SIGNED-RETRIEVAL-2026-09-26.md); de [routeherziening](ROUTE-REVISION-2026-09-21.md) blijft de voorgeschiedenis. Historische integratiecontext staat in [HANDOFF.md](HANDOFF.md) en [de concrete v2→v3-migratie](integration/V3_MIGRATION.md). Controleer alleen een ongewijzigde oorspronkelijke ontvangstkopie met:

```text
python verify_manifest.py
```

[Het herstelrapport](checks/REPAIR_REPORT.md) vermeldt wat al is uitgevoerd, welke tests slagen en welke werkzaamheden bij de daadwerkelijke repository-integratie horen. Het [eindoverzicht](COMPLETION.md) geeft de korte versie.

## Bronnen, bouw en navigatie

- [Bron-/generatorverdeling](SOURCE_OWNERSHIP.md): hoofdstukmanuscripten en `back.md` zijn bron; boek-`front.md` en boek-`print.css` worden gegenereerd.
- [Bouwomgeving en Windows-instructies](BUILD_ENVIRONMENT.md): gepinde Pythonpakketten, native libraries en gebruikte fonts, zonder fontbestanden te verspreiden.
- [Book 3-outline](outlines/Boek_3_Boekopzet_v3.pdf) en [Book 4-outline](outlines/Boek_4_Boekopzet_v3.pdf), met bewerkbare Markdown ernaast.
- [Besluit en migratie](outlines/book34-v3-decision-and-migration.md), [volledige ID-migratie](outlines/paragraph-migration-v2-to-v3.csv), [paginamap](curriculum/book-page-map-v3.json), [lesroutes](curriculum/lesson-routes-v3.json) en [targetcatalogus](curriculum/target-catalog-v3.csv).
- [Record-only controleweergave](checks/target-consumer-preview.html): alle 31 targets worden uit JSON en geregistreerde figuren weergegeven, zonder manuscriptfallback.

`build/build_all.py` verwijst naar de platformcontroller voor alle afhankelijke uitvoer. Voer daarna de aparte platformrevisiecontrole uit. Het vernieuwt geen afleveringsmanifest. `provenance/` bewaart de ontvangen v3-identiteit en eerdere review/bewijsbestanden als historie; `historical-inputs/` bewaart de eerdere boeken en de uitgestelde les. Zij zijn geen actuele instructies of onafhankelijke goedkeuring van deze reparatie.

## Afbakening

De v3-repositorymigratie en de eerdere Boek 2-reparaties zijn al samengevoegd. Deze routeherziening krijgt eigen gekoppelde PRs en actuele CI. De 31 targets blijven **`candidate_review_ready`**. De bestaande vijf lestijdproblemen blijven open; alle overige theorieparagrafen vragen eveneens een volledige begroting inclusief begeleiding. De latere cao-/vakbondsdoelen en bestaande v2-historie veranderen niet.
