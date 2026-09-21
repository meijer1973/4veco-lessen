# Correcties naar aanleiding van de controle van 18 september 2026

Deze gerichte revisie herstelt B2-01 tot en met B2-04 uit
`Boek_2_Controle_op_slordigheden_2026-09-18.md`. Uitgangspunt is lescommit
`1056488b67b16c14cc83557a8b8497e2b9985370` met platformcommit
`9f25adf07641a30ddeb27706f12e32434f581275`.

| Bevinding | Herstel |
|---|---|
| B2-01 | De platformassembler zet benoemde hoofdstuklinks vóór samenvoeging om naar hun eigen paginabestemming. Het H2-overzicht blijft op PDF-pagina 72; alle vijf klikvlakken van het H3-overzicht gaan van PDF-pagina 73 naar 109. De uitgevoerde bestemmingen heten `h2-overzicht` en `h3-overzicht`. |
| B2-02 | Producentensurplus wordt uitsluitend boven de aanbodlijn en onder P* gekleurd. Het label staat volledig binnen die driehoek. Het gebied onder aanbod blijft neutraal. |
| B2-03 | De tabel gebruikt GTK en vermeldt €/stuk. Gemiddelde kosten worden niet op de as voor totale bedragen getekend. |
| B2-04 | Grafiek en tabel gebruiken dezelfde bronwaarden: TK = 500 + 10Q en TO = 20Q. Het snijpunt is Q = 50, TK = TO = € 1.000. Bij Q = 0 zijn TK = € 500 en W = −€ 500; GTK is daar niet gedefinieerd. GTK bij Q = 150 wordt afgerond op € 13,33. |

De twee kleine redactionele aanbevelingen zijn meegenomen in de opnieuw
opgebouwde bundelinhoudsopgaven: expliciet **PDF-pagina** met uitleg over de
hoofdstuknummering, en paragraaftitels die overeenkomen met de hoofdstukken.

## Bron en bouwroute

De oorspronkelijke hoofdstuk-PDF's hebben correcte lokale links. Hun bytes,
manuscripten, opgaven, antwoorden en pagina-indeling blijven behouden. De
samengevoegde bundels worden volledig opnieuw opgebouwd met de naastgelegen
platformrepository, niet handmatig achteraf in een PDF-editor aangepast:

```text
python build-scripts/books/build_book2_chat.py --lesson-root ../4veco-lessen
python build-scripts/books/verify_book2_chat.py --lesson-root ../4veco-lessen
```

Zie de platformhandleiding `build-scripts/books/BOOK2-CHAT.md` voor vereisten en
regressietests. [assembly.json](assembly.json) bevat de samenstelling,
inhoudsopgaven en rekenwaarden. De nieuwe achtergrond
`_assets/book2-cover-background.png` is gemaakt met de ingebouwde ImageGen-tool;
het [gebruikte prompt](cover-background-prompt.txt) beschrijft uitsluitend het
leegmaken van de twee foutieve diagramvlakken. De assembler tekent daar de
controleerbare vectorfiguren en tabel overheen. De bestaande gedeelde PNG is
een render van deze definitieve omslag.

## Controle en herkomst

De gerichte controle vergelijkt alle 180 hoofdstukpagina's in de drie bundels
met de negen losse hoofdstukken: zowel tekst als gerenderde pixels zijn gelijk.
Alle 105 oorspronkelijke linkvlakken zijn behouden en komen uit op de juiste
hoofdstukpagina en positie. De bundels tellen nog 110, 57 en 19 pagina's.
De drie omslagen zijn identiek. De feitelijke PDF-vectoren, tabelcellen en
labelgrenzen worden gecontroleerd, naast visuele inspectie van de gewijzigde
pagina's. Zie [onafhankelijke beoordeling](CORRECTIES-REVIEW-2026-09-20.md).

Het [oorspronkelijke manifest](delivery-manifest.json), `verify_files.py` en
de meegeleverde hoofdstukreviews blijven historische importgegevens. Hun hashes
zijn niet achteraf herschreven. `verify_files.py` meldt daarom terecht vier
verschillen ten opzichte van de oorspronkelijke levering. Gebruik voor deze
revisie de platformverifier met het [reparatiemanifest](repair-manifest.json):
die controleert de vier vervangingen en de 455 overige leveringsbestanden.

Deze beoordeling betreft de gerapporteerde slordigheden en hun afhankelijkheden;
zij is geen nieuwe volledige vakinhoudelijke of didactische goedkeuring van
alle paragrafen. Integratie in main blijft een afzonderlijke handeling.
