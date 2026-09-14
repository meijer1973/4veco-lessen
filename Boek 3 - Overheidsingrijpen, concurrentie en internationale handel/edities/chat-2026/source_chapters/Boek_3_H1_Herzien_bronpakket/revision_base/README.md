# Boek 3 · Hoofdstuk 3.1 · Overheidsingrijpen

## Direct gebruiken

`output/Boek_3_H1_Overheidsingrijpen.pdf` is het leerlinghoofdstuk van **40 pagina’s**.
`output/Boek_3_H1_Antwoorden.pdf` is het antwoordboek van **28 pagina’s**.
`output/Boek_3_H1_Docenteninformatie.pdf` bevat **7 pagina’s** met lesplanning,
afstemming en onderwijs-/controlegrenzen.

Afdrukken: A4, ware grootte/100%, dubbelzijdig, omslaan langs de lange zijde.
De bronnen en vragen van de gemengde doeloefening staan op tegenoverliggende
pagina’s 38–39. Schrijf uitwerkingen in een schrift; werk grafiekvragen uit in de
meegeleverde basisgrafieken. Bonus en begeleide inoefening zijn niet allebei
verplichte aanvullingen op de gewone lesroute.

## Inhoud en bronkeuze

Vijf theorieparagrafen (belasting, belastingdruk/welvaartsverlies, subsidie,
maximumprijs en minimumprijs/quota) plus één consolidatieparagraaf. Er zijn
48 opgaven met 131 deelvragen en vijf volledig uitgewerkte voorbeelden.
De zes targets zijn nieuw geschreven vanuit de aangeleverde outlines v2.
Zij zijn niet overgenomen uit de oudere repositoryregistry en hebben geen
veronderstelde officiële target- of examenstatus.

De twee originele bijlagen staan ongewijzigd in `bronnen/`; hun SHA-256-identiteit
en de geraadpleegde repositoryreferentie staan in `bronnen/source_manifest.json`.
De repositoryrichtlijnen sturen de oefenvolgorde en grafische uitvoering, niet
het vervangen van de nieuwere outline. Er is niets naar GitHub geschreven.

## Bronbestanden

- `chapter-order.json` benoemt de lees- en bouwvolgorde van de acht leerlingmanuscripten.
- `00 Inleiding.md`, `3.1.1 manuscript.md` tot en met `3.1.6 manuscript.md` en
  `07 Overzicht.md`: bewerkbare leerlingtekst, ingedeeld in expliciete pagina’s.
- `Antwoorden.md` en `Docenteninformatie.md`: bewerkbare tegenhangers.
- De twee bestanden `3.1 Overheidsingrijpen – ... .md` zijn samengevoegde
  leeskopieën; de build leest de afzonderlijke manuscripten, niet deze kopieën.
- `exercises.json`, `answers.json` en `targets-authored.json`: opgave-/antwoordindexen.
- `_assets/`: 42 oorspronkelijke SVG-figuren met bijbehorende PNG-bestanden.
  SVG is in de PDF opgenomen als vectorbeeld; PNG dient als gebruikskopie.
- `paragrafen/`: twaalf PDF-uitsneden (leerling/antwoorden per paragraaf),
  met behoud van de oorspronkelijke hoofdstukpaginering. Gebruik het volledige
  hoofdstuk voor alle interne paginaverwijzingen.
- `QA/`: controle-uitkomsten en lokale inhoudelijke/visuele review.

## Opnieuw bouwen

Gebruikte Python-pakketten staan exact in `requirements.txt`. Voor identieke
regelval zijn de lokaal geïnstalleerde fonts **Lato** en **DejaVu Sans Mono** nodig;
fontbestanden worden niet meegeleverd. WeasyPrint/CairoSVG vereisen hun normale
systeemcomponenten (onder meer Pango/Cairo). Een andere fontomgeving kan de
pagina-indeling veranderen; de validator meldt dan geen geldige 40-pagina-editie.

```sh
python -m pip install -r requirements.txt
python build_all.py
```

Deze opdracht maakt de figuren, bouwt de drie PDF’s, voert de lokale controles
uit en exporteert de paragraafuitsneden. `build.py` bouwt alleen de documenten;
`validate.py` schrijft altijd `QA/validation.json` en stopt met een foutcode bij
een mislukte controle.

De `author_*.py`-bestanden bewaren de oorspronkelijke auteurstekst. Zij zijn
**geen noodzakelijke stap bij een gewone herbouw**. Het uitvoeren ervan
overschrijft de bijbehorende Markdown met die oorspronkelijke tekst. Maak
vóór een redactie een kopie, en werk bij gewijzigde opgaven de JSON-indexen en
controleverwachtingen bewust mee bij. Laat een controle niet alleen verdwijnen
omdat hij een wijziging signaleert.

## Grenzen van de bewijsvoering

De getallen en beleidsbronnen zijn fictief. De wiskunde is lokaal herberekend;
de pagina’s zijn gerenderd en bekeken. Dat vervangt geen onafhankelijke
vakinhoudelijke beoordeling, proefles of officiële examenprogramma-audit.
De 55-minutenroutes zijn planningen; bij eerste inzet is 7–9 lessen voor het
hoofdstuk een realistischer reservering dan zes gegarandeerde lessen. De
leerlingdoelen worden niet verlaagd voor de ondersteuningsroute.
