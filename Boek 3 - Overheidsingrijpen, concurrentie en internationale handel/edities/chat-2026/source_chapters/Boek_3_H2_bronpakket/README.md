# Boek 3 · Hoofdstuk 3.2 · Volkomen concurrentie

## Voltooide documenten

- `output/Boek_3_H2_Volkomen_concurrentie.pdf` — 38 leerlingpagina’s.
- `output/Boek_3_H2_Antwoorden.pdf` — 23 antwoordpagina’s.
- `output/Boek_3_H2_Docenteninformatie.pdf` — 7 pagina’s voor de docent.

Alleen het leerlinghoofdstuk valt onder de grens van 40 pagina’s. De drie PDF’s staan ook los bij de aflevering in de chat. Print op A4, op werkelijke grootte, dubbelzijdig met omslaan over de lange zijde. De gemengde doeloefening heeft bronnen op pagina 34 en vragen op pagina 35.

Het hoofdstuk bevat 38 genummerde opgaven, 112 gelabelde deelvragen, drie uitgewerkte voorbeelden en vier nieuw ontworpen doeloefeningen met samen 22 deelvragen. Er zijn 22 verschillende leerlingfiguren en 11 oplossingsfiguren; één oplossingsfiguur is ook een leerlingfiguur. Daarom bevat `_assets` 32 unieke SVG/PNG-paren.

## Inhoudelijke basis en status

De originele aangeleverde bestanden in `bronnen/` zijn ongewijzigde kopieën van **Book 3 outline proposal v2** en **Book 4 outline proposal v2**, beide gedateerd 6 september 2026. De opdracht van de gebruiker geeft deze nieuwe outlines voorrang op oudere repository-inhoud. De outlines geven doelbriefs, geen complete doelopgaven; de vier doeloefeningen in dit pakket zijn eigen uitwerkingen van die briefs. Er wordt geen formele vaststelling van een repository-doelregister of examenprogramma-audit geclaimd.

De actuele oefenrichtlijnen en precisierichtlijnen zijn via de GitHub-connector gelezen. Geraadpleegde paden staan in `QA/source-register.json` en de docenteninformatie. De bestaande leerlinginhoud in de repository is niet als basistekst gebruikt. Het opmaaksysteem sluit aan bij het eerder aanvaarde hoofdstuk 3.1 in de chat.

Scope: kenmerken en prijsnemerschap; nieuwe marginale optimalisatie en beperkt differentiëren; langetermijnaanpassing; gemengde toepassing. Monopolie en prijsdiscriminatie blijven buiten dit hoofdstuk. De normale beloning, de aannamen bij nul economische winst en de productiecapaciteit zijn expliciet opgenomen.

## Bewerken en opnieuw bouwen

1. Bewerk de pagina-Manuscripten in de hoofdmap. `chapter-order.json` bepaalt de leesvolgorde. Bewerk `Antwoorden.md` en `Docenteninformatie.md` voor de andere boeken.
2. Pas numerieke figuren aan in `make_assets.py`. De SVG’s blijven vectorafbeeldingen in de PDF; er worden ook PNG-versies gemaakt.
3. Installeer de Python-pakketten in `requirements.txt` en de systeemafhankelijkheden voor WeasyPrint en Cairo. Voor de geleverde typografie is een lokaal geïnstalleerde Lato-letterfamilie gebruikt; er worden geen lettertypebestanden meegeleverd.
4. Voer uit: `python build_all.py`.
5. Bekijk de nieuw gerenderde pagina’s. De validatie controleert o.a. pagina’s, opgave-antwoorden, rekenmodellen en SVG-coördinaten; zij vervangt geen visuele inspectie.

De bestanden `author_chapter.py`, `author_answers.py` en `author_teacher.py` bewaren de oorspronkelijke auteursrecepten. Zij worden **niet** door `build_all.py` gestart, omdat ze handmatig aangepaste Markdown kunnen overschrijven. De geassembleerde `3.2 Volkomen concurrentie – hoofdstuk.md` is een afgeleide kopie van dezelfde pagina-Manuscripten waarmee de PDF wordt gebouwd. Hoofdstuk en losse exports hebben dus geen concurrerende inhoudelijke bron.

## Losse paragraafexports

In `paragrafen/` staan Markdown en PDF’s per paragraaf. De theorieparagrafen hebben paragraaf-, opgaven- en antwoordenvarianten. De gemengde paragraaf heeft opgaven en antwoorden; er is geen geforceerde nieuwe-theorievariant.

De losse PDF’s zijn uitsneden van de gecontroleerde hoofdstukboeken en behouden de oorspronkelijke hoofdstukpaginanummers. Zo blijven terugverwijzingen naar pagina’s en opgaven bruikbaar. Bewerk voor inhoudelijke veranderingen de hoofdmanuscripten en genereer de uitsneden opnieuw. SVG-verwijzingen in deze Markdown wijzen naar de gedeelde map `_assets`.

## Controle en grenzen

`QA/validation.json` bevat de daadwerkelijke uitslagen van de laatste lokale controle. `QA/visual-review.md` beschrijft de visuele inspectie. `QA/figure_geometry.json` bevat de numerieke specificaties waarmee de werkelijke SVG-geometrie wordt vergeleken. `QA/paragraph_exports.json` legt alle uitgesneden paginareeksen vast.

Deze controles zijn lokaal uitgevoerd door dezelfde assistent, niet door een onafhankelijke specialist. De 55-minutenroutes zijn planningsschattingen; de nieuwe combinatie differentiëren en optimaliseren is over twee lessen verdeeld. De docentengids adviseert circa 5–7 lessen voor eerste gebruik.

Dit pakket wijzigt geen repositorybestanden, eerdere hoofdstukken of de oorspronkelijke voorstelstatus van de outlines.
