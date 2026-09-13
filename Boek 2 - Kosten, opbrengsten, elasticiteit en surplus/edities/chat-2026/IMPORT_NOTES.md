# Importnotities — Boek 2

## Besluit voor deze opdracht

De eigenaar vraagt het in de chat voltooide Boek 2 beschikbaar te maken in de repository, met zo weinig mogelijk inhoudelijke wijzigingen. Deze opdracht is een bestands- en navigatie-import met een roadmapactualisering, geen nieuwe schrijf- of diepgaande inhoudsreviewronde.

De ongewijzigde geleverde PDF’s zijn de referentie voor deze editie. De bewerkbare hoofdstukbronnen zijn behouden met hun bestaande mappenstructuur. De pakketnamen zijn alleen ingekort tot `H1`, `H2` en `H3`; de bestanden erin zijn niet aangepast. Relatieve paden binnen ieder hoofdstukpakket blijven intact.

## Status correct lezen

- Het boek is geschreven en als volledige bundel samengesteld.
- Opname op een branch of in een PR is nog niet hetzelfde als opname op repository-main. De integrator legt de werkelijke publicatiestatus en commit(s) vast in het PR-/opleveringsbericht.
- Bestaande bronmanifesten, lokale reviews en validatierapporten zijn historische meegeleverde documentatie. Hun oude verwijzingen, hashes en statusregels worden niet herschreven of opnieuw gedateerd.
- Er is voor deze import geen nieuwe gedetailleerde inhoudsreview uitgevoerd. Er wordt geen nieuwe `reviewed_final`-, targetgelijkwaardigheids-, platform-CI- of classroom-tested-status toegekend.

## Aandachtspunten zonder nieuwe schrijfopdracht

De H1-bron verantwoording beschrijft reeds eigen doelopgavenaanpassingen, waaronder SmoothBox. De versie wordt niet teruggeschreven naar een ouder targetrecord om een importcheck tevreden te stellen. Een toekomstige formele aansluiting op het targetregister is apart werk wanneer dat nodig blijkt.

De bestaande omslag, inhoudsopgave en hoofdstukpaginering blijven behouden. Geen herontwerp van de omslag, nieuwe doorlopende paginering of uitbreiding met voor-/nawerk in deze opdracht.

## Bestandscontrole

Voer `python verify_files.py` uit vanuit deze map of roep het script via zijn pad aan. Het controleert de bytes van alle oorspronkelijke meegeleverde bestanden, zonder het boek te herbouwen of inhoudelijk te herbeoordelen. `delivery-manifest.json` registreert ook de oorspronkelijke archiefnamen en hun checksums.

De drie bronpakketten bevatten hun eigen bouwscripts en afhankelijkheidsbestanden. De oorspronkelijke complete bron-ZIP bevat geen aparte boekassembler; de geleverde complete PDF’s zijn daarom direct te importeren uitvoer. Een nieuwe assembler of rendermigratie is geen vereiste om de uitgave op te nemen.
