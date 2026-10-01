# Integratie na beoordeling van deze proefversie

Dit pakket is een bewerkbare PDF-proef, geen voltooide repositorymigratie.
Lees eerst het revisieverslag, met name de bronafbakening. Download bij integratie
het actuele exacte main-bestand opnieuw. Neem geen andere onbedoelde verschillen
tussen de Library-kopie en de repository over.

## Bronnen en wijzigingen

1. Port de nieuwe §2.1.3-pagina’s uit `source/render_replacements.py` naar de
   actuele native manuscript/PAGE-bronnen. De bestaande vier theoriepagina’s
   worden vijf. De extra pagina is het tweede deel van het bestaande uitgewerkte
   voorbeeld, niet een nieuwe oefening of extra economische leerhandeling.
2. Neem de gerichte verbeteringen van PlakLab, WafelWagen en het H1-overzicht over.
   De overige pagina’s behouden hun pagina-budget. Vervang geen bestaande output
   zonder bijbehorende bronwijziging.
3. De acht `source/exercise*.md`-bestanden bevatten de herziene betreffende PAGE-teksten;
   de gelijknamige HTML’s zijn volledige opmaakvoorbeelden. Behoud de huidige
   begeleide/uitdagende route, gegevens, doelen, punten en oefenidentiteiten.
4. Vervang Qd/Qs door Qv/Qa in alle actieve Book2-bronnen, inclusief diagramlabels,
   antwoorden, docentenmateriaal, gegenereerde HTML’s en exports. Verwijder de
   onnodige aliasuitleg. Vervang de Nederlandse leerlingkoppen met interleaving.
   Officiële historische bronnen en bestaande reviews niet retrospectief herschrijven.
5. `companion_proposals/` bevat actuele antwoordbronvoorstellen en de relevante
   docentverwijzingen. De numerieke uitkomsten veranderen niet. Controleer bij
   een nieuwe antwoord-PDF ook de formuleopmaak, zonder dit pakket als bewijs
   voor een reeds verrichte volledige antwoordboekherziening te gebruiken.

## Bouw en nummering

Het leerlingenboek krijgt 35 + 36 + 38 = 109 body-pagina’s, plus twee ongenummerde
voorpagina’s: 111 fysieke pagina’s. Alleen de studenttoewijzing van H1 stijgt met één.
Antwoord- en docenttoewijzingen veranderen niet automatisch mee.

- Oud gedrukt 1–22 blijft 1–22, behalve dat de inhoud van oud22 over nieuw22–23 wordt verdeeld.
- Nieuw23 is de toegevoegde Atelier Boog-pagina.
- Oud23–108 wordt nieuw24–109.
- H1-overzicht: 29; §2.1.4: 30; H2-start: 36; H3-start: 72.
- H2-overzicht: 71 (fysiek73); H3-overzicht: 108 (fysiek110).

Pas `assembly.json`, PAGE-allocaties, hoofdstuk-/paragraafkaarten,
`print-pagination`, navigatie en actuele input/outputmanifesten afgeleid aan.
Controleer hardgecodeerde offsets in de owning rebuild; de oude fysieke startoffsets
van H2/H3 mogen niet blijven staan. Leid ze bij voorkeur uit de hoofdstukallocatie af.
Het oude 43-pagina-extract is historisch. Bepaal de actuele selectie uit de gekozen
bronnen en neem de extra theoriepagina en twee extra herziene voorbeelden mee
wanneer het extract alle herziene theorie moet blijven dekken.

## Algemene schrijfrichtlijn

Betekenis eerst: introduceer MK/MO met woordbreuken, daarna met Δ als afkorting.
Een onafhankelijke formule krijgt een eigen regel, tabelkolom of duidelijk eigen
kader. Gebruik geen punt of liggend streepje als losse scheiding tussen formules.
Echte rekenoperatoren en geldige gelijkheden blijven uiteraard staan.
Leg dit kort vast in de bestaande precisie-/opmaakrichtlijn; voeg geen omvangrijk
nieuw stelsel aan controles toe. Behoud de signed-elasticityconventie.

## Acceptatie

Bouw vanuit de actuele bewerkbare bronnen, niet vanuit deze PDF als bronafbeelding.
Controleer 111 studentpagina’s, alle paginaverwijzingen en daadwerkelijke linkdoelen,
geen Engelse vraag-/aanbodnotatie, geen onbedoelde herstelactie van absolute waarde,
compleet SportLint-invulraster, dezelfde vragen/getallen en leesbare formuleblokken.
Controleer de definitieve renders en de afzonderlijke antwoord-/docentexports.
Gebruik de geldende review- en integratieroute; dit pakket verleent geen mergebevoegdheid.

## Lokale reproductie van de proef-PDF

De meegeleverde baseline is nadrukkelijk de Library-kopie, niet het huidige
repositorymanifestbestand. Installeer de versies in requirements.txt en zorg
voor een lokale Lato-installatie. Fontbestanden worden niet meegeleverd.
`BOOK2_FONT_DIR` kan de locatie van de vier Lato-TTF’s aangeven.

```
python source/render_replacements.py
python source/render_standalone_exercises.py
python source/assemble_revision.py
python source/verify_revision.py
```

De opmaakreferentie gebruikt de gecontroleerde HTML’s bij oefenpagina’s. Port
latere tekstwijzigingen in de repository naar de owning manuscripten; de naastliggende
Markdown’s en HTML’s in dit proefpakket worden niet automatisch onderling gesynchroniseerd.
PDF-object-ID’s kunnen bij reproductie veranderen; de eindcontrole vergelijkt
ook daadwerkelijke tekst, getoonde pagina’s en linkbestemmingen.
