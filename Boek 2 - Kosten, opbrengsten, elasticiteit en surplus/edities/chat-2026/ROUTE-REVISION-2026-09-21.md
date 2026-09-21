# Oefenroutes — revisie 21 september 2026

Deze revisie voert de expliciete nieuwe pedagogische afspraak van de eigenaar uit. De [canonieke Part A-afspraak](https://github.com/meijer1973/4veco-platform/blob/main/skills/econ-exercise-builder.md#21-the-routes-and-the-constraint) bepaalt de routes, sectierollen en tijdsbegroting. Begeleide inoefening hoort voor de meeste leerlingen bij normaal leren. De uitdagende route biedt minder tussenstappen en extra uitdaging, met dezelfde doeloefening en de bonus. Herhaling is extra bij beide routes. Startopgaven leveren geen automatische routeselectie of scoredrempel op.

Opgaven, antwoorden, nummering, leerdoelen en inhoudelijke figuren blijven behouden. Alle routemeldingen, hoofdstukinleidingen, inleidingen op begeleide inoefening en docentteksten zijn op elkaar afgestemd. Het afzonderlijke Part B-companiontraject verandert niet.

## Bouw en bewijs

Volg de [platformbouwroute](https://github.com/meijer1973/4veco-platform/blob/main/build-scripts/books/EXERCISE-ROUTES.md) vanuit gekoppelde worktrees. De huidige manifesten binden de gewijzigde bronnen, bouwtemplates en uitvoer. Oude ontvangstmanifesten en reviewrapporten blijven historische bewijzen; zij keuren de nieuwe tekst niet automatisch goed. De nieuwe onafhankelijke review en exacte commits staan bij de gekoppelde PRs.

De controle vergelijkt opgaven, doelen, definities, formules, figuren en antwoordbronnen met de samengevoegde Book 2-correctiebaseline `e2843b47`. De PDF-controle vergelijkt de nieuw ingevoegde hoofdstukpagina’s met de huidige hoofdstuk-PDFs en controleert inhoudskoppelingen en paginering. Het platform bewaart het SHA-pin van het gesloten actuele bestandsmanifest `exercise-route-revision.json` in de lesrepositoryroot. Een nieuwe bouw kan andere PDF-hashes opleveren door omgeving, paden en PDF-identifiers; de uitvoer wordt ook op tekst, pixels en navigatie gecontroleerd.

## Boek 2: open tijdsvragen

Alle negen theorieparagrafen moeten opnieuw worden begroot inclusief begeleide inoefening en alle zelfstandige oefening. De gedetailleerde fasen en echte opgavenummers staan in de docentbron en docent-PDF. Er is geen nieuwe 55-minutengarantie.

| Paragraaf | Eerdere selectie zonder begeleiding | Eerder genoemde begeleide tijd / gevolg |
|---|---:|---|
| 2.1.1 | 52 min | Ontbreekt; geselecteerd zelfstandig werk en doel waren onvolledig. |
| 2.1.2 | 53 min | Ontbreekt; geselecteerd zelfstandig werk en doel waren onvolledig. |
| 2.1.3 | 55 min | 10–15 min: ten minste 65–70 min, plus overig zelfstandig werk. |
| 2.2.1 | 50 min | 8–15 min: 58–65 min. |
| 2.2.2 | 55 min | 8–15 min: 63–70 min. |
| 2.2.3 | 55 min | 8–15 min of meer: 63–70 min of meer. |
| 2.3.1–2.3.3 | Elk 55 min | Begeleide tijd niet afzonderlijk onderbouwd. |

Dit zijn oude ontwerpschattingen, geen klassikale metingen. Plan aanvullende lestijd; schrap geen opgaven en versmal de doeloefening niet. De bonus vraagt een afzonderlijke begroting binnen de uitdagende route.

## Gemengde structuuruitzonderingen

| Paragraaf | Bestaande voorbereiding en doel | Aanvullende onderdelen |
|---|---|---|
| 2.1.4 | Opgaven 1–4 → doel 5 | Bonus 6; herhaling 7. |
| 2.2.4 | Opgaven 1–4 → doel 5 | Bonus 6; hoofdstukcheck 7, geen afzonderlijke herhalingssectie. |
| 2.3.4 | Opgaven 1–2 en bestaande denksteun → doel 3 | Bonus 4; herhaling 5–7. |

Deze paragrafen hebben geen aparte begeleide sectie. Gebruik de uitleg en denkstappen uit het hoofdstuk bij de voorbereiding; maak het doel zelfstandig. De eerdere geselecteerde planningen van 52/55/55 minuten zijn geen begroting van alle gedrukte oefening of extra begeleiding. Er zijn geen nieuwe secties of opgaven bedacht.

## Eerdere reparaties behouden

Platform PR253 en lesson PR55 waren op 21 september samengevoegd vóór deze revisie. Hun historische `repair-manifest.json` blijft ongewijzigd. De gerepareerde cover en hoofdstukoverzichtskoppelingen blijven behouden. De huidige assembler accepteert de gewijzigde hoofdstukken alleen via `--revised-chapters`, `route-chapter-inputs.json` en `route-assembly-manifest.json`. De complete bundels blijven 110/57/19 pagina’s.
