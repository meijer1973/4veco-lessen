# Render- en inhoudscontrole · Boek 4 H1

Datum: 8 september 2026. Controle door de producerende assistent; geen onafhankelijke reviewer.

## Gecontroleerde uitvoer

- Leerlinghoofdstuk: 38 fysieke A4-pagina’s, alle pagina’s gerenderd met PDFium op 110 dpi. Contactbladen in reeksen van maximaal zes pagina’s bekeken; lastige grafieken en tabellen aanvullend op paginagrootte.
- Antwoordboek: 20 fysieke pagina’s, alle contactbladen bekeken. Met name de tweefigurenpagina 15 en de gescheiden KleurFix/prijsnemersroute gecontroleerd.
- Docenteninformatie: 7 fysieke pagina’s, alle pagina’s bekeken. De gecorrigeerde laatste twee pagina’s opnieuw gerenderd en op paginagrootte bekeken.
- Tweede renderer: Poppler (`pdftoppm`), leerlingpagina 24 (winstrechthoek, GTK, hulplijnen en tekst), visueel gelijkwaardige uitvoer zonder ontbrekende tekens of verschoven objecten.

De renderafbeeldingen zijn reviewmateriaal, geen deel van de printuitgave. Het pakket bevat de reproduceerbare PDF/HTML-uitvoer en alle figuurbronnen, niet de omvangrijke tijdelijke pagina-renders.

## Gevonden en gerepareerde punten

1. Een directe vraaglijnlabel lag te dicht bij een gemarkeerd vraagpunt. Het lijnlabel is verplaatst naar vrije ruimte verder rechts. De getallen en punten zijn niet verschoven.
2. Het MO-label in een optimalisatiefiguur stond dicht bij een routepunt. Alleen het label is verplaatst; de coördinaten bleven functiegetrouw.
3. Bij opgave 2 is de tweede vraag aangescherpt: studenten gebruiken nu expliciet de vermelde alternatieven uit de bron, zonder een extra onbewezen gevolg te moeten invullen.
4. De docentengids liep aanvankelijk op een achtste pagina over door extra bronpakket-gebruiksinformatie. Die informatie staat nu in README; de zeven inhoudelijke pagina’s zijn behouden, zonder letterverkleining.
5. De docentverwijzing naar “figuur 23” was onjuist. Het gaat om **opgave 23**; hersteld.
6. De SVG-numeriekcontrole vond afrondingsversterking bij de zeer kleine q-waarden van GTK = c + F/q. De uitvoerprecisie van polylinecoördinaten is verhoogd van vier naar acht decimalen. De economische functie, zichtbare ligging en testtolerantie bleven ongewijzigd.
7. Een automatische apparaat-/interne-routecheck zag de letters “part a” in het Nederlandse “apart aanwijzen”. De check gebruikt nu woordgrenzen; er is geen leerlingtekst verwijderd om de test te passeren.

## Inhoudelijke steekproef en dekking

Alle 107 antwoordlabels zijn gekoppeld aan hun vragen. De vier doelen zijn eigen uitwerkingen van de meegeleverde v2-briefs, geen gekopieerde registerrecords. De doeluitkomsten, bijkomende capaciteitsgevallen en omzet-/winstcontrasten zijn rationeel herberekend in `validate.py`.

Expliciet nagegaan:
- Eén prijs per plan, zonder fictieve terugbetaling op historische verkopen.
- Extra omzet als opbrengst op extra kg minus lagere opbrengst op de eerdere kg.
- ΔTO/Δq als intervalgemiddelde versus de afgeleide MO bij één hoeveelheid.
- MO/MK selecteren q; vraag/GO bepaalt P; winst gebruikt TO − TK.
- Productiecapaciteit en onvermijdbare kosten bij q = 0 zijn gegeven vóór ze nodig zijn.
- De winstrechthoek gebruikt GTK bij de gekozen hoeveelheid, niet het gebied tussen twee krommen.
- De gemengde concurrentievergelijking is uitdrukkelijk een andere markt, geen ongeautoriseerde welvaartsvergelijking.
- Geen behandeling van prijsdiscriminatie of monopoliewelvaart vóór hoofdstuk 4.2.

## Resterende grenzen

Geen bekende afgesneden teksten, overlappende functionele labels, ontbrekende figuren of lege onbedoelde pagina’s na de laatste build. Dit is een visuele producentencontrole, geen bewijs dat elk pedagogisch effect is vastgesteld. Lesminuten en leerwinst zijn niet empirisch gemeten. Bij een andere fontomgeving of gewijzigde manuscripten moeten paginering en render opnieuw beoordeeld worden.
