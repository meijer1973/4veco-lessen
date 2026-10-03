# Boek 1 · tweede editie (2026)

Dit is de actuele leeseditie van **Grondslagen, vraag en aanbod**, op uitdrukkelijk
verzoek van de eigenaar geïntegreerd uit het aangeleverde tweede-editiepakket.
De drie hoofdstukken bevatten twaalf paragrafen, 114 opgaven en 280 deelvragen.

- [Leerlingboek · 132 pagina’s](boek/Boek_1_Compleet_Tweede_editie.pdf)
- [Antwoorden · 66 pagina’s](boek/Boek_1_Compleet_Antwoorden_Tweede_editie.pdf)
- [Docenteninformatie · 28 pagina’s](boek/Boek_1_Compleet_Docenteninformatie_Tweede_editie.pdf)
- [Hoofdstukken en losse paragrafen](index.html)

## Bronnen en bouwen

`bronnen/H1`, `H2` en `H3` bevatten de bewerkbare paragraafmanuscripten,
antwoorden, docenteninformatie, figuren en drukstijlen. Die bestanden zijn
leidend; de gecombineerde manuscripten, HTML, PDF en paginakaarten zijn afgeleid.
Platform bezit de bouw- en controlecode. Vanuit de gekoppelde platformcheckout:

```text
python -X utf8 build-scripts/books/book1_second_edition/rebuild.py --lessons ../4veco-lessen --fonts <map-met-Lato-TTFs>
python -X utf8 build-scripts/books/book1_second_edition/publish.py --lessons ../4veco-lessen
```

Een gewone herbouw regenereert geen auteurstekst. De oorspronkelijke generatoren,
ontwerpen en onderzoeksbewijzen blijven byte-identiek in de ontvangen ZIPs onder
`references/owned/book1-second-edition-2026/received/` in het platform.
De ongewijzigde bestanden in `sources/` zijn historische ontwerpbronnen; actuele
route- en tijdsafspraken staan in het canonieke platformcontract
`skills/econ-exercise-builder.md` en de bijgewerkte docenteninformatie.

## Integratieaanpassingen

Begeleide inoefening staat in de normale route; de bonus in de uitdagende route.
De negen herhalingskoppen gebruiken “Herhaling en combineren”. De drie gemengde
paragrafen behouden hun eigen structuur, zonder verzonnen oefensecties.
Beide complete routes zijn begroot, inclusief motivatie, samenvatting en feedback.
De tijden zijn **ongemeten ontwerpschattingen**, geen gegarandeerde 55-minutenfit.

De omslag heeft gecontroleerde vectorvoorbeelden op een bewerkte illustratieve
achtergrond. Bij §1.3.1 opgave 8 is een weggegeven uitkomst verwijderd uit de
slotzin. Bij het uitgewerkte voorbeeld en §1.2.2 opgaven 18 en 19 maakt een expliciete modelaanname duidelijk
waarom de nieuwe rechte vraaglijn tot haar nulpunt getekend mag worden; de
berekeningen, vragen en antwoorden blijven gelijk.

Leerling- en antwoordpaginering blijven 132/66. De docentbundel telt nu 28 pagina’s,
waaronder de bewust lege laatste duplexpagina; de leerlingbundel heeft geen lege
pagina’s. Bronnen en vragen van de drie gemengde doelen blijven tegenover elkaar
op 40–41, 80–81 en 120–121. Lokale docentverwijzingen gebruiken de omzetting voorin.

## Editie-identiteit en grenzen

De eerste editie is volledig bewaard in `../../historisch/`, inclusief hoofdstuk
1.4, 1.5 en companionmateriaal. De oude complete-PDF-URL levert nu echt de nieuwe
PDF; de oude hoofdstuk-URL’s blijven expliciet eerste-editiemateriaal via
`../../eerste-editie.html`. Presentaties en quizzen worden niet op basis van een
gelijk paragraafnummer tot materiaal voor deze nieuwe editie verklaard.

De nieuwe doelen krijgen een eigen editie-identiteit. Oude `reviewed_final`-
status, machinekoppelingen en curriculumautoriteit worden niet geërfd. De
onafhankelijke inhoudsreview van deze editie en repository-CI zijn afzonderlijke
bewijzen; ze vormen geen nieuwe CvTE-validatie of gemeten leereffect.
Boek 2–4, hun historische bewijzen en Part B blijven inhoudelijk ongewijzigd.
