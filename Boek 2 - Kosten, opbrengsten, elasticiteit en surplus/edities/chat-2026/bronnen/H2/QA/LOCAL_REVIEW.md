# Lokale eindcontrole · hoofdstuk 2.2

Datum: 6 september 2026. Reikwijdte: deze zelfstandige printeditie, niet een repositoryrelease. Dit is een controle door de auteur/bouwer en geen onafhankelijke specialistische review.

## Afgeronde controles

| Onderdeel | Resultaat | Bewijs |
|---|---|---|
| Leerlingomvang | 36 pagina’s; maximum 40. | PDF en `output/page_map.json`; alle 36 geplande pagina’s passen zonder overloop. |
| Antwoorden | 18 pagina’s; 38 opgaven compleet. | Centraal antwoordenmanuscript, PDF en nummeringscontrole. |
| Docenteninformatie | 6 pagina’s zonder overloop. | PDF en `build_teacher.py`. |
| Doelgetrouwheid | Vier contexten en 21 deelvragen behouden. | Excerpten in `provenance/target_questions.json`; tekstvergelijking na normalisatie van opmaak/witruimte. |
| Oefenvolgorde | Alle zeven H2-onderdelen in de drie theorieparagrafen. | Manuscripten en `validate.py`. |
| Bewerkingendekking | Uitgewerkt voorbeeld, begeleide en zelfstandige voorbereiding aanwezig. | De afstemmingstabellen in de docenteninformatie. |
| Rekenen | Procenten, Ev/Ei/Ek, oude/nieuwe TO en functie-scenario’s gecontroleerd. | Expliciete rekenfixtures in `validate.py`; elke test in `validation-report.json`. |
| Figuren | 13 SVG/PNG-paren; correcte maatvoering en getalovereenstemming. | `make_assets.py`, `_assets/geometry-data.json` en controles op bereik/oppervlakte/tekstgrenzen. |
| Drukweergave | Alle 60 pagina’s van de drie hoofddocumenten visueel bekeken. | Gerenderde pagina’s en contactbladen tijdens de bouw; voorbeelden van compacte doelpagina’s en grafieken afzonderlijk vergroot bekeken. |
| Overdracht | Aparte paragraaf-, opgaven- en antwoordenexports beschikbaar. | `paragraph-exports.json` en de map `paragrafen/`. |

De laatste volledige bouw eindigde met **397 lokale controles geslaagd, 0 mislukt**. Dit aantal telt afzonderlijke controles op structuur, rekenen, brongetrouwheid en uitvoer. Het is geen kwaliteitscijfer en geen empirisch bewijs van leerwinst.

## Correcties tijdens de controle

- Verticale strepen in de absolute-waardetabel HTML-veilig gemaakt, zodat de tabel niet in extra kolommen uiteenviel.
- Procentuele noemers, dimensieloze elasticiteit en nuldeling expliciet gecontroleerd.
- Een begeleide Ek-context gewijzigd in skateboards/wieltjes om onbedoeld hergebruik van de zelfstandige consolecontext te voorkomen; antwoorden tegelijk aangepast.
- De afsluitende observatiefiguur bevat geen misleidende causale pijlen bij gelijktijdige veranderingen van prijs, reclame en inkomen.
- De StreamPlus-functie heeft expliciet een eigen regionale uitgangssituatie; er is geen ongegeven geografisch label aan bron A toegevoegd.
- Automatische lijstnummering in het gemengde antwoordmodel vervangen door vaste deelvraagnummers 1–6; een PDF-tekstcontrole bewaakt deze nummering.
- Afgebroken korte antwoordstaarten opnieuw gepagineerd. De volledige StreamPlus-uitwerking staat samen op één antwoordpagina. Lettergrootte en witruimte zijn daarna opnieuw visueel beoordeeld.

## Bewaakte inhoudelijke grenzen

De kleine-veranderingregel voor omzet is geen universele regel voor oude-waarde-elasticiteiten over grote stappen. De Ei-classificatie blijft de drie categorieën van deze methode. Bij Ek zijn beide goederen zichtbaar. Bij functies worden scenario’s teruggezet. Bonusopgaven vragen een andere voorstelling of kritische interpretatie en voeren geen verborgen verplichte optimalisatiestof in.

## Open, eerlijk benoemde toetsing

Niet uitgevoerd: onafhankelijke docentreview, leerlingproef, representatieve tijdmeting, officiële repository-currentness- en integratievalidators. Die stappen blijven nodig voor formele opname of een aantoonbare klasprestatieclaim. Vooral §2.2.3 kan twee lessen vergen. Er is niets naar GitHub geschreven of gemergd.
