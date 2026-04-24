# Paragraph Plan: 1.1.2 Percentages en indexcijfers

Source of truth for all Part B builders (presentatie, voorkennis, vaardigheden, nieuws, samenvatting, begeleide inoefening, opgavensets, quiz, reasoning, newsdetective, procedure).

Pedagogical type: **calculation** - formula-first with repeated worked examples. The constant approach is: identify old/new values, calculate relative to the old value, then interpret the sign or index movement.

---

## Key concepts

| # | Concept | Definition (1 sentence) | Formula | Graph type needed |
|---|---------|------------------------|---------|-------------------|
| 1 | Procentuele verandering | De verandering van een waarde als percentage van de oude waarde. | `(nieuw - oud) / oud x 100%` | Bar/bridge chart |
| 2 | Oude waarde als noemer | Bij een stijging of daling deel je altijd door de waarde waar je vandaan komt. | `verandering / oud` | Error callout |
| 3 | Indexcijfer | Een waarde uitgedrukt ten opzichte van een basisjaar met index 100. | `(waarde / basiswaarde) x 100` | Line chart |
| 4 | Indexpunten versus procenten | Een verschil tussen indexcijfers is een aantal indexpunten; procentuele verandering bereken je opnieuw met de oude index als noemer. | `(nieuw index - oud index) / oud index x 100%` | Comparison chart |

---

## Visuals plan

Alle onderstaande visuals bestaan al in `_assets/` als SVG+PNG vanuit Part A. Part B hergebruikt ze om dual coding te borgen.

| Filename | Graph type | Used by | Description | Parameters |
|---|---|---|---|---|
| `1.1.2_fig_1` | Bar/bridge chart | presentatie, voorkennis, vaardigheden, samenvatting | Smartphoneprijs van EUR 600 naar EUR 648; absolute stijging EUR 48 wordt 8% van de oude prijs. | Oud 600, nieuw 648 |
| `1.1.2_fig_2` | Line/index chart | presentatie, vaardigheden, nieuws met visual, samenvatting | Boodschappenmandje met basisjaar 2021 = 100 en index 125 in 2023. | Basis 120, nieuw 150 |
| `1.1.2_fig_3` | Comparison/error chart | presentatie, vaardigheden, samenvatting | Index 125 naar 135: 10 indexpunten maar 8% stijging. | Oud index 125, nieuw 135 |
| `1.1.2_we_1` | Worked example chart | presentatie, begeleide inoefening | Benzineprijs 2022-2024 als indexreeks. | 1,80 -> 1,98 -> 1,89 |

---

## Presentation outline

Theorie + uitgewerkt voorbeeld. Geen opgave-instructies.

1. **Title slide**: "Percentages en indexcijfers" - waarom bedragen vergelijken met procenten?
2. **Smartphone hook**: EUR 48 duurder is 8%; absolute en relatieve verandering naast elkaar.
3. **Procedure 1**: procentuele verandering berekenen in drie stappen, met `1.1.2_fig_1.png`.
4. **Indexcijfers**: basisjaar = 100, boodschappenmandje naar index 125, met `1.1.2_fig_2.png`.
5. **Valkuil**: indexpunten zijn geen procenten, met `1.1.2_fig_3.png`.
6. **Uitgewerkt voorbeeld**: benzineprijs 2022-2024, met `1.1.2_we_1.png`.
7. **Samenvatting**: oude waarde als noemer; basisjaar; indexpunten vs procenten.

Minimum >=3 SVG->PNG graphs: voldaan.

---

## News plan

| | |
|---|---|
| **Onderwerp** | Inflatie in Nederland en de consumentenprijsindex. |
| **Article** | CBS, "Inflatie in maart 2,7 procent", gepubliceerd in april 2026. |
| **Source URL** | https://www.cbs.nl/nl-nl/nieuws/2026/15/inflatie-in-maart-2-7-procent |
| **Summary** | CBS meldt dat consumentengoederen en -diensten in maart 2026 2,7% duurder waren dan een jaar eerder. Dit is een herkenbare context om het verschil tussen prijsstijging, procentuele verandering en indexcijfers te oefenen. |
| **Visual** | Hergebruik `1.1.2_fig_2.png` als indexanker; leerlingen koppelen nieuws over inflatie aan het idee basisjaar = 100. |
| **Questions** | 1. Wat betekent 2,7% inflatie? 2. Welke oude waarde hoort in de noemer? 3. Waarom is CPI een indexcijfer? 4. Wat is het verschil tussen indexpunten en procenten? 5. Waarom kan een gemiddeld inflatiecijfer per huishouden anders voelen? |

---

## Summary concepts

- [x] Procentuele verandering = verandering gedeeld door oude waarde
- [x] Positief betekent stijging; negatief betekent daling
- [x] Indexcijfer = waarde ten opzichte van basisjaar 100
- [x] Basisjaar altijd expliciet benoemen
- [x] Indexpunten zijn geen procenten
- [x] Bij verandering tussen indexcijfers deel je door het oude indexcijfer
- [x] Smartphonevoorbeeld, boodschappenmandje en benzinevoorbeeld keren terug in meerdere builders

---

## Terminologie

| Term | Use everywhere | Do not use |
|---|---|---|
| procentuele verandering | "procentuele verandering" | "percentage verschil" zonder noemer |
| oude waarde | "oude waarde" / "waarde waar je vandaan komt" | "kleinste waarde" |
| nieuwe waarde | "nieuwe waarde" | "hoogste waarde" |
| basisjaar | "basisjaar" | "startjaar" als losse term zonder index = 100 |
| indexcijfer | "indexcijfer" | "indexgetal" |
| indexpunten | "indexpunten" | "procentpunten" bij indexcijfers |
| inflatie | "inflatie" als procentuele stijging van het algemeen prijspeil | "alles wordt duurder" zonder percentage |

---

## Exercise distribution

| Level | Count | Topics | Question type |
|---|---|---|---|
| **Basis** | 6 | oude/nieuwe waarde herkennen, eenvoudige procentuele stijging/daling, index basisjaar 100 | korte rekenopgaven |
| **Midden** | 5 | indexreeks, verandering tussen indexcijfers, koopkrachtcontext | rekenopgaven met uitleg |
| **Verrijking** | 4 | samengestelde procenten, eerst +20% dan -20%, inflatiegevoel versus CPI | open redeneeropgaven |

---

## Skills & prior knowledge

**Prior knowledge**:

- Rekenen met breuken en decimalen.
- Vermenigvuldigen met 100.
- Grafieken en tabellen globaal lezen.
- Schaarste en keuze uit 1.1.1 als context, maar niet als rekenvoorwaarde.

**Skills**:

- Procentuele verandering berekenen.
- Indexcijfer berekenen.
- Procentuele verandering tussen indexcijfers berekenen.
- De indexpunten/procenten-valkuil herkennen.

---

## Procedure-stappen-plan (unified experience)

| Skill | Canonical steps |
|---|---|
| Procentuele verandering berekenen | 1. Noteer de oude waarde en de nieuwe waarde. 2. Bereken `(nieuw - oud) / oud x 100%`. 3. Interpreteer: positief = stijging, negatief = daling. |
| Indexcijfer berekenen | 1. Bepaal het basisjaar en zet dat op 100. 2. Bereken `(waarde / basiswaarde) x 100`. 3. Interpreteer: boven 100 = hoger dan basisjaar, onder 100 = lager dan basisjaar. |
| Verandering tussen indexcijfers berekenen | 1. Noteer het oude en nieuwe indexcijfer. 2. Bereken `(nieuw index - oud index) / oud index x 100%`. 3. Benoem expliciet: het verschil in indexpunten is niet hetzelfde als procentuele verandering. |

Deze stappen moeten in vaardigheden, stappenplan-game, presentatie en begeleide inoefening dezelfde labels en volgorde houden.

---

## Visuelen-toewijzing (dual coding)

| Visual | presentatie | vaardigheden | voorkennis | samenvatting | begeleide inoefening | nieuws |
|---|---|---|---|---|---|---|
| `1.1.2_fig_1.png` | slide 2/3 | procentuele verandering | oude/nieuwe waarde | ja | basisvoorbeeld | - |
| `1.1.2_fig_2.png` | slide 4 | indexcijfers | basisjaar | ja | middenvoorbeeld | ja |
| `1.1.2_fig_3.png` | slide 5 | indexpunten-valkuil | - | ja | verrijking | - |
| `1.1.2_we_1.png` | slide 6 | worked example | - | ja | scaffold | - |

---

## Game data outlines

### Quiz

Categorieen:

- procentuele-verandering
- indexcijfers
- indexpunten-valkuil
- toepassing-inflatie

### Newsdetective

CBS-inflatiebericht gebruiken om claim, oorzaak-gevolg, modelkeuze en foutanalyse te oefenen.

### Reasoning

Zes tot twaalf scenario's rond stijging/daling, indexreeks en foutieve interpretaties. Minimaal drie structuurtypen met twee vragen per type.

### Procedure

Drie procedures: procentuele verandering, indexcijfer berekenen, verandering tussen indexcijfers.

### Skilltree

Voor deze scaling sprint: `skilltree: { "skills": null }` zodat de generator dezelfde proven path als `1.1.1` gebruikt. Een smallere vaardighedenset kan later worden gekozen als de skilltree-map inhoudelijk wordt aangescherpt.
