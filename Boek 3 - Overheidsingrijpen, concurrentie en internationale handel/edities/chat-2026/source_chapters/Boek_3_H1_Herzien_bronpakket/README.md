# Boek 3 · Hoofdstuk 3.1 · Overheidsingrijpen — herziene editie

## Direct gebruiken

- `output/Boek_3_H1_Overheidsingrijpen.pdf`: **48 leerlingpagina’s**, voorheen 40.
- `output/Boek_3_H1_Antwoorden.pdf`: **31 pagina’s** met alle antwoorden.
- `output/Boek_3_H1_Docenteninformatie.pdf`: **10 pagina’s**, inclusief de herbeoordeling.
- `output/Boek_3_H1_Beoordeling_en_wijzigingen.pdf`: de afzonderlijke beoordeling en wijzigingentabel (**2 pagina’s**).

A4, ware grootte/100%, dubbelzijdig, omslaan langs de lange zijde. De bronnen en vragen van de gemengde doeloefening staan tegenover elkaar op 46–47. De zes paragraafnummers en alle bestaande opgavenummers blijven bruikbaar. Nieuwe opgaven: **22A, 40A en 47A**. Totaal: **51 opgaven / 141 deelvragen**. De zes doeloefeningen behouden alle 31 deelvragen; alleen een paginaverwijzing is bijgewerkt. De antwoorden op deze targets zijn inhoudelijk ongewijzigd.

## Wat verandert en wat niet?

Acht pagina’s versterken de stappen tussen uitleg en samengestelde berekening. De gecontroleerde belastingdrukvergelijking en de subsidieverliesfiguur staan nu vóór de doeloefeningen. Er is extra steun voor subsidieboekhouding, opkoop versus minimumprijs, en de quotumroute. Bonus 17 is herschreven als een vergelijking van grafiekasschalen. De maximumprijsparagraaf blijft inhoudelijk intact. Er zijn geen nieuwe leerdoelen, formele beleidsmodellen of externe-effectberekeningen toegevoegd.

Dit is een didactische herbeoordeling van de werkelijk geleverde tekst, niet een meting van leerresultaten. Uit de oude versie blijkt niet welke passage destijds letterlijk is geschrapt vanwege de paginalimiet. De review beschrijft daarom concrete zwakke overgangen, zonder zulke schrappingen te verzinnen.

## Inhoudelijke basis

De door de gebruiker aangewezen Book 3 en Book 4 outlines v2 blijven de inhoudelijke basis. De originele bestanden en hashes staan in `bronnen/`. De actuele repository-oefenrichtlijnen zijn opnieuw gelezen via de GitHub-connector. De zes targets zijn auteursopgaven op basis van de aangeleverde briefs, geen officiële examenvragen of stilzwijgend geïntegreerde registry-records. Deze aflevering wijzigt geen GitHub-repository.

## Bewerken en opnieuw bouwen

Bewerk de Markdown-bestanden in `chapter-order.json` en de antwoord-/docentenmanuscripten. De twee samengestelde `3.1 Overheidsingrijpen – ... .md` bestanden zijn leeskopieën. Bij gewijzigde vragen moeten ook `exercises.json`, `answers.json` en de bewust beschreven controleverwachtingen worden bijgewerkt.

```sh
python -m pip install -r requirements.txt
python build_all.py
```

De build genereert de figuren, vier documenten, lokale controles en twaalf paragraafuitsneden. De bestaande tekst wordt niet opnieuw geschreven. Lato en DejaVu Sans Mono moeten lokaal beschikbaar zijn; fontbestanden worden niet meegeleverd. Een gewijzigde fontomgeving kan reflow veroorzaken; de paginacontrole signaleert dit.

Om precies deze auteursherziening vanuit de bewaarde oude manuscriptversie te reconstrueren:

```sh
python revise_chapter.py
python revise_answers.py
python revise_teacher.py
python build_all.py
```

**Let op:** `revise_*.py` overschrijft latere handmatige Markdown-edits. `revision_base/` bewaart de eerdere tekst, indexen en auteurscripts uitsluitend voor vergelijking/herkomst. Voer de oude auteurscripts daar niet uit als normale buildstap.

## Controle en overdracht

`_assets/` bevat **47 SVG/PNG-paren**; de PDF bevat vectorfiguren. `QA/validation.json` controleert rekencases, daadwerkelijke SVG-objecten, antwoorddekking, behoud van targets en paginering. `QA/LOCAL_REVIEW.md` registreert de uitgevoerde visuele inspectie. `QA/page_concordance.json` en `.csv` zetten oude losse hoofdstukpagina’s om naar deze editie.

De negen uitgewerkte lesroutes van 55 minuten zijn ramingen. Begeleide oefeningen zijn een route met extra steun, niet een extra verplichte stap voor iedereen. Reken bij eerste inzet op ongeveer negen lessen, met zo nodig één of twee extra feedback-/ondersteuningslessen. De controles vervangen geen onafhankelijke vakreview, klasproef of officiële examenvalidatie.
