# Boek 3 — Hoofdstuk 3: Internationale handel

## Printeditie 1.0

Nieuw geschreven volgens de door de gebruiker aangeleverde **Book 3 outline v2**
(6 september 2026). De bijbehorende Book 4-outline bewaakt de grens met de
latere monopolie- en arbeidsmarktstof. De inhoudelijke indeling van deze
bijlagen heeft voor deze opdracht voorrang op de oudere repository-indeling.

Dit pakket wijzigt geen live repository, examenprogramma of geregistreerde
doelopgave. De vier doelopgaven zijn voor deze editie geschreven vanuit de
ontwerpbriefs. De casussen, landen en cijfers zijn fictieve lesvoorbeelden.

## Bestanden voor gebruik

| Bestand in `output/` | Omvang |
|---|---:|
| `Boek_3_H3_Internationale_handel.pdf` | 38 pagina's |
| `Boek_3_H3_Antwoorden.pdf` | 17 pagina's |
| `Boek_3_H3_Docenteninformatie.pdf` | 7 pagina's |

Het leerlinghoofdstuk bevat 3 uitgewerkte voorbeelden, 38 genummerde opgaven
met 108 deelvragen en 22 verschillende didactische figuren. Het antwoordboek
bevat alle antwoorden, toelichtingen en 5 aanvullende oplossingsfiguren.
De antwoorden tellen niet mee bij het maximum van 40 leerlingpagina's.

Druk het leerlinghoofdstuk op **A4, ware grootte, dubbelzijdig, lange zijde**.
De bronnen en vragen van opgave 35 staan op tegenoverliggende pagina's **34–35**.
De doelopgaven zijn opgaven **7, 17, 27 en 35**. De kernroute is niet gelijk aan
alle gedrukte opgaven: zie de docenteninformatie voor de lesselecties en de
optionele begeleide route. De lesduur is een te toetsen ontwerpschatting.

## Bewerkbare bronnen

- `00 Inleiding.md`, `3.3.1 manuscript.md` t/m `3.3.4 manuscript.md`, `05 Overzicht.md`:
  leerlingtekst in leesvolgorde volgens `chapter-order.json`.
- `Antwoorden.md`, `Docenteninformatie.md`: bewerkbare aanvullende manuscripten.
- `3.3 Internationale handel – hoofdstuk.md`: automatisch samengestelde kopie.
- `_assets/`: vector-SVG's plus PNG-versies. `make_assets.py` bevat de vergelijkingen,
  diagramopbouw en uitvoerbare grafiekspecificaties.
- `paragrafen/`: aparte paragraaf-, opgaven- en antwoord-PDF's met Markdown en assets.
  De gemengde paragraaf heeft geen aparte nieuwe-theorievariant.
- `_chapter-plan.md`: inhoudelijke afstemming en keuze van leerroute.
- `bronnen/`: de twee aangeleverde outlines, hun hashes en het bron-/toegangsregister.
- `QA/`: opgaven, antwoorddekking, nieuwe doelen, figuurgeometrie, export- en paginakaarten,
  controleverslag en visuele zelfcontrole.

De **PDF-extracten behouden de oorspronkelijke gedrukte hoofdstukpaginering**.
Daardoor blijven verwijzingen kloppen. Verwijzingen naar eerdere paragrafen
veronderstellen dat het complete hoofdstuk beschikbaar is. De hoofdbron voor
wijzigingen blijft het manuscript in de bovenliggende map; opnieuw exporteren
vervangt de afgeleide kopieën in `paragrafen/`.

## Opnieuw bouwen

Gebruik Python 3.11 of nieuwer en installeer de pakketten uit `requirements.txt`.
WeasyPrint en CairoSVG gebruiken daarnaast de op het besturingssysteem
beschikbare Pango/Cairo-bibliotheken. Voor dezelfde typografie moeten **Lato**
en een passende monospacefallback beschikbaar zijn. Lettertypebestanden zijn
niet meegeleverd. Een andere fontinstallatie kan de pagina-indeling veranderen;
de validatie signaleert dan eventuele paginaoverloop.

```bash
python -m pip install -r requirements.txt
python build_all.py
```

`build_all.py` maakt achtereenvolgens de figuren, alle drie hoofd-PDF's, de
paragraafextracten en het controleverslag. Een mislukte stap stopt de build.
**Bewerk de Markdown-bronnen** om tekst te wijzigen. Een wijziging in de
opgavenstructuur moet ook terugkomen in `QA/exercises.json`, `QA/answers.json`,
`QA/authored-targets.json` en de desbetreffende controlegevallen.

De `author_*.py`-scripts bewaren de oorspronkelijke auteursversie. Voer ze
alleen bewust uit om die versie te herstellen; ze overschrijven handmatige
manuscriptwijzigingen. Een normale herbouw roept ze daarom niet aan.

## Controles en grenzen

`python validate.py` controleert onder meer:

- aanwezigheid, volgorde en afstemming van alle opgaven en antwoorden;
- de zeven voorgeschreven oefenkoppen en de plaats van de samenvatting;
- afzonderlijk herberekende oefenuitkomsten en modelwaarden;
- feitelijke SVG-eindpunten, markeringen en polygonen tegenover de vergelijkingen;
- afbakening van import, export en invoerheffingsopbrengst;
- PDF-pagina-aantallen, tekstselectie, inhoudslinks, paginadrift en bestandsverwijzingen.

De controle is **geen onafhankelijke didactische review en geen klasproef**.
De pagina's zijn daarnaast gerenderd en door de auteur visueel beoordeeld.
Een ruwe telling van controles is geen maat voor leerwinst: lees het
controleverslag en de docenteninformatie voor wat daadwerkelijk is nagekeken.

Dit hoofdstuk introduceert geen cijfermatige comparatieve-kostenroutine,
ruilverhoudingsgrenzen, arbeidsproductiviteitsformules, wisselkoers- of
betalingsbalansmodel. Er is geen geclaimde bewerking van de in het outline
historisch genoemde examenvraag uit 2022.
