# Boek 4 · Hoofdstuk 1 · Monopolie

## Uitgave

Dit pakket bevat de nieuw geschreven hoofdstukuitgave voor **4 vwo**. De aangeleverde **Book 4 outline proposal v2, 6 september 2026**, bepaalt de inhoud, volgorde en grenzen. De Book 3-outline bepaalt de aansluiting. De nieuw geschreven doeloefeningen werken de doelbriefs uit; zij zijn geen formeel gepromoveerde records uit het repositoryregister.

| Bestand in `output/` | Pagina’s | Inhoud |
|---|---:|---|
| `Boek_4_H1_Monopolie.pdf` | 38 | Volledig leerlinghoofdstuk, inclusief uitleg, voorbeelden, alle opgaven, overzicht en begrippen |
| `Boek_4_H1_Antwoorden.pdf` | 20 | Alle 107 deelvragen, met berekeningen, verklaringen en acht oplossingsfiguren |
| `Boek_4_H1_Docenteninformatie.pdf` | 7 | Afstemming, lesplanning, modelvoorwaarden en reviewnotities |

Het leerlinghoofdstuk bevat 38 genummerde opgaven, drie uitgewerkte voorbeelden en vier doeloefeningen met 22 deelvragen. Er zijn 23 leerlingfiguren (22 genummerde figuren en het openingsschema) en acht antwoordfiguren. Elk van de 31 figuren heeft een SVG-bron en een PNG-versie.

### Paragrafen

| Paragraaf | Onderwerp | Hoofdstukpagina’s |
|---|---|---:|
| 4.1.1 | Monopolie: kenmerken | 2–9 |
| 4.1.2 | Marginale opbrengst bij monopolie | 10–20 |
| 4.1.3 | Winstmaximalisatie bij monopolie | 21–31 |
| 4.1.4 | Gemengde opgaven: monopolie | 32–36 |
| — | Overzicht en begrippen | 37–38 |

De PDF-weergaven in `paragrafen/` zijn uitsneden uit de geaccepteerde hoofdstuk-PDF’s: geen afzonderlijke heropmaak. Ze behouden de hoofdstukpaginanummers. De opgavenversie van de gemengde paragraaf is gelijk aan de volledige gemengde paragraaf: daar is geen nieuwe theorieles.

## Lesgebruik

Print het leerlinghoofdstuk op A4, werkelijke grootte, dubbelzijdig, omslaan over de lange zijde. De bronnen en vragen bij opgave 35 staan op tegenoverliggende pagina’s 34–35. Antwoorden horen niet in het leerlinghoofdstuk.

De kernroute is Startopgaven → Zelfstandige oefening → Doeloefening. Begeleide inoefening is een optionele ondersteuningsroute naar dezelfde doelen. Bonus is buiten de kern; herhaling kan huiswerk zijn. De docentengids begroot een korte route maar adviseert vijf tot zeven lessen bij eerste gebruik. Deze tijden zijn schattingen, geen metingen.

De inhoud loopt tot de ondernemingskeuze onder monopolie. Welvaartseffecten en prijsdiscriminatie blijven bestemd voor §4.2.1 en §4.2.2. Oefenbedrijven, bronnen en cijfers zijn fictief. Er wordt geen nieuwe externe examenprogramma-audit of onafhankelijke specialistische goedkeuring geclaimd.

## Bewerkbare bronnen

De primaire tekstbestanden staan in de pakketroot:

- `00 Inleiding.md`, de vier `4.1.n manuscript.md`-bestanden en `05 Overzicht.md` vormen het leerlinghoofdstuk in de volgorde van `chapter-order.json`.
- `Antwoorden.md` en `Docenteninformatie.md` zijn de andere twee manuscripten.
- `print.css` bepaalt typografie, paginamarges, koppen, tabellen, figuren en kaders.
- `make_assets.py` bevat de grafiekmodellen, coördinatentransformaties en diagrammen; `_assets/` bevat hun SVG- en PNG-uitvoer.
- De samengestelde `4.1 Monopolie – hoofdstuk.md` en de bestanden in `paragrafen/` zijn afgeleid. Bewerk de primaire manuscripten, niet alleen deze kopieën.

De `author_*.py`-bestanden bewaren het oorspronkelijke schrijf-recept. **Voer die niet uit na handmatige manuscriptwijzigingen**: ze zouden de oorspronkelijke tekst opnieuw wegschrijven. De normale build gebruikt ze niet. Bij wijzigingen aan vraagnummering of doelstructuur moeten ook de QA-registers worden bijgewerkt en inhoudelijk gecontroleerd.

## Opnieuw bouwen

Gebruik een Python-omgeving met de pakketten uit `requirements.txt` en de systeembibliotheken die WeasyPrint/Cairo nodig hebben. Het ontwerp gebruikt lokaal geïnstalleerde **Lato** met **DejaVu Sans** als fallback. Er zijn geen fontbestanden in dit pakket. Andere fonts of bibliotheekversies kunnen regel- en pagina-afbrekingen beïnvloeden.

```bash
python -m pip install -r requirements.txt
python build_all.py
```

De build maakt de figuren, de drie PDF’s en zelfstandige HTML-weergaven, voert de lokale controles uit en exporteert de twaalf paragraafweergaven. Ontbrekende bronnen, figuren of falende controles stoppen de build. Voor de build zelf is geen repositorytoegang nodig.

De `<!-- PAGE ... -->`-markeringen in de manuscripten leggen de bedoelde paginagrenzen vast. Controleer na elke tekstwijziging de werkelijke paginatelling en de render; behoud het maximum van 40 leerlingpagina’s. Gebruik de lege ruimte niet automatisch voor meer verplichte taken: leesbaarheid en de haalbare lesroute zijn de eerste criteria.

## Controle en herkomst

`QA/validation.json` registreert **644 geslaagde lokale controles** op de geleverde editie. Ze omvatten rationele herberekening van modellen, vergelijking van de werkelijke SVG-coördinaten met functies, vraag-antwoorddekking, koppenvolgorde, assets, bronhashes en PDF-paginering. `QA/paragraph_exports.json` controleert de tekstbehoudende uitsneden. `QA/visual-review.md` benoemt de handmatige rendercontrole en doorgevoerde reparaties.

`bronnen/` bewaart de twee aangeleverde outlines ongewijzigd. `QA/source-register.json` vermeldt welke repositoryrichtlijnen via de GitHub-connector zijn gelezen, inclusief blob-ID’s. De directe HTTP-downloadpoging vanuit de sandbox mislukte door DNS; de connectorlezingen van de kaarten en relevante richtlijnen waren wel succesvol. De repositoryrichtlijnen worden daarom niet als volledig gedownloade bronkopieën gepresenteerd.

Deze controles zijn uitgevoerd door dezelfde assistent die de uitgave vervaardigde. Ze zijn geen onafhankelijke peerreview en geen toets van leerwinst in een klas. De live repositories, oudere hoofdstukken en eerdere uitgaven zijn niet gewijzigd.
