# Oefenroutes — revisie 21 september 2026

Deze revisie voert de expliciete nieuwe pedagogische afspraak van de eigenaar uit. De [canonieke Part A-afspraak](https://github.com/meijer1973/4veco-platform/blob/main/skills/econ-exercise-builder.md#21-the-routes-and-the-constraint) bepaalt de routes, sectierollen en tijdsbegroting. Begeleide inoefening hoort voor de meeste leerlingen bij normaal leren. De uitdagende route biedt minder tussenstappen en extra uitdaging, met dezelfde doeloefening en de bonus. Herhaling is extra bij beide routes. Startopgaven leveren geen automatische routeselectie of scoredrempel op.

Opgaven, antwoorden, nummering, leerdoelen en inhoudelijke figuren blijven behouden. Alle routemeldingen, hoofdstukinleidingen, inleidingen op begeleide inoefening en docentteksten zijn op elkaar afgestemd. Het afzonderlijke Part B-companiontraject verandert niet.

## Bouw en bewijs

Volg de [platformbouwroute](https://github.com/meijer1973/4veco-platform/blob/main/build-scripts/books/EXERCISE-ROUTES.md) vanuit gekoppelde worktrees. De huidige manifesten binden de gewijzigde bronnen, bouwtemplates en uitvoer. Oude ontvangstmanifesten en reviewrapporten blijven historische bewijzen; zij keuren de nieuwe tekst niet automatisch goed. De nieuwe onafhankelijke review en exacte commits staan bij de gekoppelde PRs.

De controle vergelijkt opgaven, doelen, definities, formules, figuren en antwoordbronnen met de samengevoegde Book 2-correctiebaseline `e2843b47`. De PDF-controle vergelijkt de nieuw ingevoegde hoofdstukpagina’s met de huidige hoofdstuk-PDFs en controleert inhoudskoppelingen en paginering. Het platform bewaart het SHA-pin van het gesloten actuele bestandsmanifest `exercise-route-revision.json` in de lesrepositoryroot. Een nieuwe bouw kan andere PDF-hashes opleveren door omgeving, paden en PDF-identifiers; de uitvoer wordt ook op tekst, pixels en navigatie gecontroleerd.

## Boeken 3 en 4: open tijdsvragen

Alle 25 theorieparagrafen hebben een onvolledige oude begroting: begeleide inoefening ontbrak en soms werd maar een deel van het zelfstandig werk geselecteerd. De overige oude selecties telden meestal al 55 minuten (52 minuten in §4.2.3); de volledige normale route is dus niet onderbouwd als één les. De vijf eerder gemelde conflicten 3.1.2, 3.1.3, 3.1.5, 4.2.4 en 4.2.5 blijven daarnaast afzonderlijk herkenbaar. Nieuwe sets moeten vanaf het ontwerp de complete normale route meenemen; bestaande sets krijgen aanvullende lestijd en een eerlijke open begroting.

`curriculum/lesson-routes-v3.json` bewaart de eerdere schatting onder `previous_estimate`, geeft de werkelijke sectie-/opgavenummers voor beide routes en laat het volledige theorietotaal onbekend. De docent-PDFs bevatten de gedetailleerde uitleg en timingwaarschuwingen. De bonus is onderdeel van de uitdagende route en vraagt daar extra tijd. Geen opgaven of doelen zijn geschrapt.

## Gemengde structuuruitzonderingen

| Paragraaf | Voorbereiding → doeloefening | Bestaande aanvullende onderdelen |
|---|---|---|
| 3.1.6 | 46, 47, 47A en bestaande denksteun → 48 | Geen aparte bonus of herhaling. |
| 3.2.4 | 31–34 en bestaande controle → 35 | Bonus 36; herhaling 37. |
| 3.3.4 | 31–34 → 35 | Bonus 36; herhaling 37–38. |
| 4.1.5 | 41, 41A, 42–44 → 45 | Verdere gemengde oefening 46–48; geen benoemde bonus/herhaling. |
| 4.2.7 | 55–57 → 58 | Extra gemengde oefening 59; herhaling 60; geen bonussectie. |
| 4.3.5 | 37–39 → 40 | Bonus 41; geen herhalingssectie. |

Gebruik de bestaande hoofdstukuitleg en denkstappen bij de voorbereiding. §4.1.5 geeft dit compact in de inleidende tekst; de andere paragrafen hebben een korte aanwijzing bij de opgaven. Er zijn geen ontbrekende standaardsecties verzonnen. Oude geselecteerde gemengde routes blijven schattingen van hun selectie, niet van alle gedrukte taken of extra ondersteuning.

## Publicatie en historie

Complete leerling-/antwoord-/docentdelen blijven Boek 3: 132/74/22 en Boek 4: 166/68/28 pagina’s. Alle 31 paragrafen behouden hun ID en doel. Targetstatus blijft `candidate_review_ready`; deze revisie verleent geen nieuwe curriculumgoedkeuring.

`MANIFEST.sha256.json`, `provenance/`, `historical-inputs/`, de ontvangen controles en de ontvangen bouwscripts (behalve de huidige dunne `build_all.py`-verwijzing) blijven historische ontvangstgegevens. De oude volledige manifestcontrole hoort bij een ongewijzigde ontvangstkopie. Gebruik voor de huidige revisie de aparte platformcontrole en `checks/route-revision-*.json`.
