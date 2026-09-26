# Getekende prijselasticiteit: beperkte opvolgende revisie

De twee leerlingvragen 3.2/29b en 3.3/30b vragen nu om Ev te vergelijken met
−1 en 0. Zes antwoordtoelichtingen sluiten daarop aan: 3.1/9b, 3.1/45a,
3.2/29b, 3.3/30b, 4.1/20b en 4.1/44a. Alle berekeningen, opgavenummers,
gegevens, doelen, routes en doelopgaven blijven behouden. De zes uitkomsten
blijven −0,5; −0,5; −0,4; −0,5; −1,5 en −2. De eerste vier zijn
prijsinelastisch; de laatste twee prijselastisch.

De canonieke afspraak staat in de
[precisiereferentie §15.1](https://github.com/meijer1973/4veco-platform/blob/main/references/authored/economic_mathematical_precision_reference.md#151-canonical-signed-elasticity-procedure).
Een afzonderlijke absolute-waardestap is niet verplicht. Een vrijwillig gebruikte,
wiskundig gelijkwaardige redenering blijft aanvaardbaar wanneer berekening en
economische interpretatie correct zijn. Exacte omzetvergelijkingen blijven P × Q;
de bestaande eindige-veranderingskanttekening bij 4.1/40 blijft intact.

## Bouw en bewijs

Volg de [platformbouwroute](https://github.com/meijer1973/4veco-platform/blob/main/build-scripts/books/BOOKS34-SIGNED.md).
De huidige dunne `build/build_all.py` verwijst naar die opvolger en geeft de
argumenten `--comparison-root` en `--report` door. De oude routecontroller
herbouwde de antwoorden niet en is niet de ingang voor deze wijziging.

Antwoordhoofdstukken 3.1, 3.2, 3.3 en 4.1 worden vóór samenstelling herbouwd.
De acht HTML/PDF/paginamap-drietallen, twee paragraafexports en drie betrokken
complete boeken worden vernieuwd. De totale paginatallen en boekoffsets blijven
gelijk: Boek 3 leerling/antwoorden 132/74 en Boek 4 antwoorden 68. De globale
paginamap is opnieuw berekend. Negentien antwoordbronhashes en twee
manuscripthashes zijn opnieuw uit de echte bronnen afgeleid; alle 31
doelopgavepayloads en kandidaatstatussen blijven gelijk.

`books34-signed-revision.json` in de repositoryroot bindt de huidige inventaris.
`checks/signed-retrieval-*.json` bevat het nieuwe bewijs. De bestaande route- en
Boek 2-manifesten, hun platformpins, eerdere reviews, ontvangstgegevens en
historische invoer blijven behouden. De opvolger controleert die historische
inventarissen op hun vaste baseline; hij geeft ze geen nieuwe reviewdatum.

## Afbakening

Dit sluit uitsluitend de zes actieve vraag-/antwoordbronnen en hun afhankelijke
publicaties aan op de getekende procedure. Het is geen programmawijde voltooiing.
NAV1, TIMING34 en de vastgehouden PV-templates blijven afzonderlijk open.
De bestaande antwoordkop “Herhaling 20 en 21” boven opgaven 29/30 in 3.2.3
(antwoordhoofdstuk p. 17; compleet antwoordenboek p. 51) is tijdens review
afzonderlijk gesignaleerd. Deze kop bestond al en valt buiten de acht wijzigingen.
`candidate_review_ready`, curriculum-/levenscyclusblokkades, Boek 1, het herziene
Boek 2 en Part B veranderen niet. Review en CI op de precieze repositoryversies
staan in de gekoppelde PRs; deze revisie verleent geen nieuwe doelgoedkeuring.
