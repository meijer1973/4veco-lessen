# Visuele eindcontrole — hoofdstuk 3.2

## Reikwijdte

Lokale controle door de producerende assistent. Dit is geen onafhankelijke specialistische beoordeling, geen repository-CI en geen klaslokaalonderzoek. De bestandsidentiteiten van de gecontroleerde eindversies staan in `release-manifest.json`.

## Uitgevoerd

Alle 38 leerlingpagina’s, 23 antwoordpagina’s en 7 docentpagina’s zijn via PyMuPDF naar PNG gerenderd. De volledige reeks contactvellen is bekeken; grafiek- en doelpagina’s zijn aanvullend op grotere schaal bekeken. Een tweede renderer, Poppler `pdftoppm`, is gebruikt voor leerlingpagina 19, antwoordpagina 17 en docentpagina 4.

Gecontroleerd: zichtbare tekst, paginawisselingen, oefeningen bij hun context, assen en eenheden, verschillende Q/q-schalen, grafieklabels, winstvlakken, kleur/markering, inhoudsverwijzingen en de spread 34–35.

## Correcties vóór vrijgave

- Opbrengst- en kostenschalen van de gekoppelde ondernemingsgrafieken kregen de expliciete aanduiding P, MK en GTK in euro per kg.
- Een steile nieuwe aanbodlijn had zijn label aanvankelijk buiten de zichtbare grafiek. De labelpositie wordt nu teruggebracht naar een werkelijk zichtbaar punt op de lijn; de numerieke curve blijft ongewijzigd.
- De visuele beslisroute op leerlingpagina 19 is opgenomen in de echte paginabron. Een extra bron-/assetcontrole voorkomt dat een figuur alleen in de bronmap staat maar niet in het hoofdstuk verschijnt.
- De gemengde paragraaf begint opnieuw met figuur 1; de vraagverwijzing op pagina 35 is daarop afgestemd.
- Geassembleerde Markdown wordt bij iedere bouw rechtstreeks uit dezelfde pagina-Manuscripten opgebouwd als de PDF. Zo kan de controletekst niet afwijken van de gebouwde inhoud.

## Einduitkomst

Geen afgebroken pagina-inhoud, lege pagina’s, ontbrekende figuren of vervangingsblokjes aangetroffen in de bekeken eindversies. De figuren zijn vectorafbeeldingen in de PDF. Alle drie eindboeken blijven binnen hun ontworpen paginatelling: 38 / 23 / 7. De lokale machinecontrole eindigt zonder fouten; zie `validation.json` voor iedere concrete check.

## Resterende onzekerheid

Werktempo, begrip en het effect van de gekozen steunstappen zijn niet in een klas gemeten. De lesplanning gebruikt vijf kernlessen, met twee lessen voor de nieuwe combinatie van differentiatie en optimalisatie; voor eerste gebruik wordt 5–7 lessen geadviseerd. Formele target-registergoedkeuring en onafhankelijke didactische beoordeling vallen niet onder deze lokale aflevering.
