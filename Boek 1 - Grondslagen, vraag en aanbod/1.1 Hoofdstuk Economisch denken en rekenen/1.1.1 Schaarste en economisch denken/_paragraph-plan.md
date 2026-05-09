# Paragraph Plan: 1.1.1 Schaarste en economisch denken

Source of truth for all Part B builders (presentatie, voorkennis, vaardigheden, nieuws, samenvatting, begeleide inoefening, opgavensets, quiz, reasoning, newsdetective, procedure).

Pedagogical type: **intro** — narrative-first (named characters: Lisa met €20, boer met 10 ha, Eva met 4 uur vrije tijd).

---

## Key concepts

| # | Concept | Definition (1 sentence) | Formula | Graph type needed |
|---|---------|------------------------|---------|-------------------|
| 1 | Schaarste | Behoeften zijn groter dan de beschikbare middelen, waardoor keuzes onvermijdelijk zijn. | — | F. Infographic/flowchart (behoeften vs middelen) |
| 2 | Alternatieve kosten | De opbrengst van het beste niet-gekozen alternatief bij een keuze. | `alt.kosten = opbrengst beste niet-gekozen alternatief` | H. Custom — keuzediagram (twee alternatieven naast elkaar) |
| 3 | Economisch denken (4-stappen procedure B02) | Systematisch alternatieven vergelijken: (1) benoem alternatieven; (2) bereken opbrengst per alternatief; (3) rangschik — beste niet-gekozen = alternatieve kosten; (4) bereken nettowaarde = opbrengst − alternatieve kosten. | — | F. Flowchart (vier stappen) |
| 4 | Totale opbrengst bij inzet van een schaars middel | Opbrengst = eenheden schaars middel × opbrengst per eenheid. | `TO = q × o` | G. Bar chart (vergelijking alternatieven) |

Unit alignment: concepts 1 en 2 komen rechtstreeks uit het unit-register (B01, B02). Concept 3 is een verbale uitwerking van de procedure van B02. Concept 4 is rekentechnisch een deelvaardigheid zonder eigen unit (het is simpele vermenigvuldiging, geen A-vaardigheid).

---

## Visuals plan

Alle vijf onderstaande visuals bestaan als Part A-bronmateriaal in `_assets/` als SVG+PNG. Voor companion-output is letterlijk hergebruik niet meer de bedoeling: gebruik deze bestanden als bron voor concept, data en geometrie, maar maak surface-adapted varianten voor web, presentatie, docx en samenvatting.

| Filename | Graph type | Used by | Description | Parameters |
|---|---|---|---|---|
| `1.1.1_fig_1` | F. Infographic | presentatie (schaarste-slide), voorkennis (concept intro), samenvatting | Behoeften-trechter (onbegrensd) → schaarste-filter → keuze | — |
| `1.1.1_fig_2` | H. Keuzediagram | presentatie (alt.kosten-slide), vaardigheden (skill 1), samenvatting | Twee alternatieven naast elkaar met opbrengst; pijl wijst het niet-gekozen alternatief aan als "alternatieve kosten" | — |
| `1.1.1_fig_3` | F. Flowchart | presentatie (economisch-denken-slide), vaardigheden (skill 2 procedure), stappenplan-game | 4-stappenflow B02: Alternatieven → Opbrengsten → Rangschik (alt. kosten) → Nettowaarde | — |
| `1.1.1_we_1` | H. Custom | presentatie (worked example), vaardigheden (skill 2 worked example), begeleide inoefening (scaffold) | Tarwe vs maïs op 10 ha, winst per ha en totaal, met alt.kosten-annotatie | Tarwe €500/ha · Maïs €350/ha · 10 ha |
| `1.1.1_ex_1` | G. Bar chart | begeleide inoefening (scaffold voor opgave 1), opgavensets (basis) | Winst/ha voor 3 gewassen: tarwe, maïs, zonnebloemen | Tarwe €500 · Maïs €350 · Zonnebloemen €300 |

**Optioneel extra visual** (nieuwsopdracht): zie §Nieuws-plan — mogelijk nieuw.

---

## Visual variants plan

Visual anchor = hetzelfde concept en dezelfde data, niet hetzelfde boekplaatje. Iedere surface krijgt een passende variant met eigen verhoudingen, typografie, contrast, annotaties en kleurbehandeling.

| Concept visual | Source/base | Built variants | Notes |
|---|---|---|---|
| Schaarste: behoeften versus middelen | `1.1.1_fig_1.svg/png` | `1.1.1_fig_1_slide.svg/png`; `1.1.1_fig_1_doc.svg/png`; `1.1.1_fig_1_summary.svg/png`; `1.1.1_fig_1_web_light.svg/png`; `1.1.1_fig_1_web_dark.svg/png` | Slide/doc/summary/web variants replace literal textbook reuse. |
| Alternatieve kosten: wat geef je op | `1.1.1_fig_2.svg/png` | `1.1.1_fig_2_slide.svg/png`; `1.1.1_fig_2_doc.svg/png`; `1.1.1_fig_2_summary.svg/png`; `1.1.1_fig_2_web_light.svg/png`; `1.1.1_fig_2_web_dark.svg/png` | Used in presentation, vaardigheden, summary, and guided scaffolding. |
| Economisch denken in stappen | `1.1.1_fig_3.svg/png` | `1.1.1_fig_3_slide.svg/png`; `1.1.1_fig_3_doc.svg/png`; `1.1.1_fig_3_summary.svg/png`; `1.1.1_fig_3_web_light.svg/png`; `1.1.1_fig_3_web_dark.svg/png` | Keeps the same procedure anchor but adapts layout per surface. |
| Tarwe versus Mais worked example | `1.1.1_we_1.svg/png` | `1.1.1_we_1_slide.svg/png`; `1.1.1_we_1_doc.svg/png`; `1.1.1_we_1_summary.svg/png`; `1.1.1_we_1_web_light.svg/png`; `1.1.1_we_1_web_dark.svg/png` | Used in presentation, vaardigheden, summary, and guided scaffolding. |
| Winst per hectare drie gewassen | `1.1.1_ex_1.svg/png` | `1.1.1_ex_1_doc.svg/png`; `1.1.1_ex_1_web_light.svg/png`; `1.1.1_ex_1_web_dark.svg/png` | Eerste test voor `uitleg voorkennis`; web gets separate light/dark variants. |
| Woningmarkt: vraag versus aanbod sociale huur | `1.1.1_news_woningtekort.svg/png` | `1.1.1_news_woningtekort_doc.svg/png`; `1.1.1_news_woningtekort_web_light.svg/png`; `1.1.1_news_woningtekort_web_dark.svg/png` | Produced by `b1-111-nieuws.js` via the shared SURFACES/THEMES palette. No slide/summary variants — news does not appear in the presentation or summary. |

### Game visuals decision (L1.3B)

Voor paragraaf 1.1.1 krijgen de game- en interactieve surfaces geen eigen concept-visual slot:

- Noch de HTML-shells (`instapquiz.html`, `redeneer-spel.html`, `stappenplan.html`, `nieuws-detective.html`) noch de bijbehorende data-objects (reasoning / quiz / procedure / newsdetective) dragen vandaag een `visualAsset`-veld. Ze tonen gegenereerde UI en tekst; geen geadopteerde concept-afbeelding.
- Voor deze paragraaf is dat voldoende: de schaarste- en alternatieve-kosten-figuren (`fig_1`, `fig_2`, `we_1`, `ex_1`) worden al gedekt door de voorkennis-, vaardigheden- en begeleide-inoefening-pagina's. Games voegen hier spelmechaniek toe, geen extra conceptueel plaatje.
- Revisit per paragraaf. Als een latere paragraaf een concept heeft dat alléén binnen een game leesbaar wordt (bv. een grafiek die hoort bij een redeneerscenario), wordt het per-paragraaf-besluit opnieuw genomen en naar het platformteam geëscaleerd voor een shell-aanpassing.

---

## Presentation outline

Theorie + uitgewerkt voorbeeld. Geen opgaveninstructies (B9 hard rule). Narrative-first: open met Lisa en €20.

1. **Title slide**: "Schaarste en economisch denken" — editorial title, subtitle "Waarom kun je niet alles hebben?"
2. **Narrative hook**: Lisa heeft €20, wil bioscoop (€12) én boek (€15) → beide kan niet. *Geen visual.*
3. **Concept: Schaarste** — definitie + tabel (scholier/boer/overheid) + figuur `1.1.1_fig_1_slide.png`. Pitfall callout: "schaarste ≠ weinig".
4. **Concept: Alternatieve kosten** — definitie + Lisa-voorbeeld uitgewerkt + figuur `1.1.1_fig_2_slide.png`. Pitfall callout: "alternatieve kosten ≠ prijs".
5. **Concept: Economisch denken** — 4-stappen procedure (B02) + figuur `1.1.1_fig_3_slide.png`.
6. **Uitgewerkt voorbeeld — tarwe vs maïs**: procedure stap-voor-stap toegepast + figuur `1.1.1_we_1_slide.png`.
7. **Samenvatting** (theorie-slide): bullets met de vijf kernpunten uit de samenvatting.
8. **Afsluiting**: terugkoppeling naar Lisa — "in de volgende paragraaf: hoe meten we verschillen in geld?".

Minimum ≥3 SVG→PNG graphs: voldaan (4 figures ingebed). Font ≥18pt. Na `writeFile()` altijd `fixPptxFile()` + `roundtripWithLibreOffice()`.

---

## News plan

| | |
|---|---|
| **Onderwerp** | Woningschaarste in Nederland (perennial topic, hoge herkenbaarheid voor 15-16-jarigen). |
| **Article** | Kies recent NOS/RTL/Volkskrant-artikel over woningtekort, wachtlijsten sociale huur, of stijgende huizenprijzen. Kandidaat: NOS "Tekort aan woningen blijft groot …" *(nieuws-builder verifieert URL bij build-tijd)*. |
| **Summary** | 80 woorden: kernpunt = er zijn méér woningzoekenden dan beschikbare woningen (schaarste), dus moeten er keuzes worden gemaakt — wie krijgt voorrang (sociale huur), welk beleid (bouwen vs. verdelen). |
| **Visual** | Nieuw: `1.1.1_news_woningtekort.svg/png` — staafdiagram met woningvraag vs woningaanbod (fictieve maar plausibele cijfers; bron: CBS/ministerie BZK). |
| **Graph type** | G. Bar chart (twee staven naast elkaar: vraag, aanbod) — óf line chart (tekort door de tijd). |
| **Questions (5)** | 1. Herken schaarste (wat is hier het schaarse middel?). 2. Reken: hoeveel méér vraag dan aanbod? 3. Wie moet kiezen en tussen welke alternatieven? 4. Wat zijn voor woningzoekenden de alternatieve kosten? 5. Open: zou de overheid prioriteit moeten geven aan starters of aan bijstandsgerechtigden? Beredeneer. |

**Hard rules (B2-C)**: sourceUrl verplicht, SVG→PNG chart (geen placeholder), font 16/11/9pt.

---

## Summary concepts

Infographic-table-based samenvatting — één A4 met domain-gekleurde cellen (teal, markt-domain).

- [x] Definitie schaarste
- [x] Schaarste ≠ zeldzaamheid (pitfall)
- [x] Schaarste geldt voor consumenten, producenten en overheid (drieluik-tabel)
- [x] Definitie alternatieve kosten
- [x] Alternatieve kosten ≠ prijs (pitfall)
- [x] Alternatieve kosten = beste niet-gekozen alternatief (niet de som)
- [x] Procedure economisch denken (4 stappen, B02)
- [x] Mini-worked-example: tarwe vs maïs
- [x] Canonical term: "alternatieve kosten" (niet "opportunity costs" of "opportuniteitskosten")

Cell layout (table-based, B9 hard rule):

| Rij 1 | Wat is schaarste? (def + fig_1-thumbnail) | Schaarste-voorbeelden (scholier/boer/overheid) |
|---|---|---|
| Rij 2 | Alternatieve kosten (def + fig_2-thumbnail) | Pitfalls (niet ≠ prijs; niet optellen) |
| Rij 3 | Economisch denken 4 stappen B02 (fig_3-thumbnail) | Mini-worked-example tarwe/maïs |

---

## Terminologie

Gebruik canonical Dutch terms overal. Geen Engelse of Latijnse varianten.

| Term | Use everywhere | Do not use |
|---|---|---|
| schaarste | "schaarste" | "tekort" (te smal), "zeldzaamheid" (te breed) |
| alternatieve kosten | "alternatieve kosten" | "opportunity costs", "opportuniteitskosten", "gemiste kansen" |
| behoeften | "behoeften" (wensen) | "vraag" (dat is iets anders — komt in §1.2) |
| middelen | "middelen" (tijd, geld, grondstoffen) | "resources" (Engels), "hulpbronnen" (reserveer voor later) |
| economisch denken | "economisch denken" | "rationeel kiezen" (formeler, komt later) |
| opbrengst | "opbrengst" (of "waarde") | "winst" (winst = opbrengst − kosten; zie §1.3) |
| alternatief | "alternatief" / "alternatieven" | "optie" (informeler — vermijd in formele definities) |

---

## Exercise distribution

Opgavensets basis / midden / verrijking — in aanvulling op de bestaande Part A-opgaven 1–5. De Part A-set blijft zoals hij is; Part B voegt geoefende opgaven toe, gesorteerd naar Bloom-niveau.

| Level | Count | Topics | Question type |
|---|---|---|---|
| **Basis** (8) | 8 | Schaarste herkennen (ja/nee + uitleg), canonical termen matchen, eenvoudige alt.kosten-berekening bij 2 alternatieven | multiple choice (3), ja/nee + uitleg (3), korte rekenopgave (2) |
| **Midden** (6) | 6 | Alt.kosten met 3+ alternatieven, winst op schaarse middelen (ha × €/ha), 4-stappen-procedure (B02) zelfstandig toepassen in nieuwe context | rekenopgaven met stappen + uitleg |
| **Verrijking** (4) | 4 | Gemengde allocatie (zoals de buurvrouw in opgave 4), gratis-is-niet-gratis redenering, schaarste-claim kritisch beoordelen, overheidskeuze met alternatieve kosten | open redeneeropgaven + case |

Elke opgave kent bij antwoorden naar de **canonical term** uit Terminology. Basis is multiple-choice-zwaar (vlot oefenen); verrijking is open (analyse/evaluatie).

---

## Skills & prior knowledge

**Prior knowledge** (unit IDs): *none.* Dit is de eerste paragraaf van het boek — geen voorkennis uit eerdere paragrafen. Voorkennis-document dekt daarom:

- Basale rekenoperaties (vermenigvuldigen en aftrekken) als herhaling, géén A-unit omdat het sub-vaardigheidsniveau is.
- Grafiek-lezen (staafdiagram) als herhaling uit de onderbouw — géén A-unit vereist, wordt in §1.1.3 formeel opgepakt.
- Intuïtie voor "kiezen bij beperkte tijd/geld" — ingeleid via dagelijkse voorbeelden.

**Skills** (unit IDs): **B01, B02** (beide "schaarste"-domein).

- B01 "Schaarste als kerneconomisch probleem" — mastery_target = understand. Conceptuele vaardigheid: schaarste herkennen en onderbouwen.
- B02 "Alternatieve kosten in een keuze-situatie" — mastery_target = apply. Procedurele vaardigheid: beste niet-gekozen alternatief identificeren en opbrengst berekenen. Needs B01.

Optional graphs needed for voorkennis/vaardigheden: use concept bases `fig_1`, `fig_2`, `fig_3`, `we_1`, with `_doc` in Word and `_web_light`/`_web_dark` in themed HTML.

---

## Procedure-stappen-plan (unified experience)

Source of truth: `references/machine/micro-teaching-units.json`. Downstream builders (vaardigheden, stappenplan-game, presentatie slide 6, begeleide inoefening) halen stappen uit het register via unit-ID — niet hier opnieuw schrijven.

Snapshot ter documentatie (NIET authoritative):

| Unit ID | Unit name | Steps |
|---|---|---|
| B01 | Schaarste als kerneconomisch probleem | — (conceptueel, geen procedure; gebruik `kern` + `pitfalls`) |
| B02 | Alternatieve kosten in een keuze-situatie | 4 stappen: (1) benoem alternatieven voor het schaarse middel; (2) bereken opbrengst per alternatief; (3) rangschik — hoogste niet-gekozen opbrengst = alternatieve kosten; (4) vergelijk opbrengst gekozen alternatief met alternatieve kosten voor nettowaarde. |

**Update L1.5V (2026-05-09):** alle §1.1.1 surfaces gebruiken nu de canonical 4-stappen B02-procedure verbatim — geen didactische 3-stappen variant meer. Vaardigheden, stappenplan-game, presentatie slide 5, samenvatting cel rij 3, begeleide inoefening en opgaven zijn allemaal op 4 stappen gemigreerd. Het visual `1.1.1_fig_3` (alle 5 surface-variants) toont de 4 stappen verbatim. De vroegere 3-stappen-didactische tekst is gerd; reden: surface-onderlinge inconsistentie creëerde een hard-fail risk in de companion review (HF-2 procedure-fidelity).

---

## Visuelen-toewijzing (dual coding)

Elke builder die een concept met matching visual uitlegt, embed een surface-adapted variant (B-verify dual-coding checklist).

| Visual concept | presentatie | vaardigheden | voorkennis | samenvatting | themed web |
|---|---|---|---|---|---|
| `1.1.1_fig_1` | `1.1.1_fig_1_slide.png`, slide 3 | `1.1.1_fig_1_doc.png`, skill 1 | — | `1.1.1_fig_1_summary.png`, cel rij 1 kolom 1 | `1.1.1_fig_1_web_light.svg/png` + `1.1.1_fig_1_web_dark.svg/png` |
| `1.1.1_fig_2` | `1.1.1_fig_2_slide.png`, slide 4 | `1.1.1_fig_2_doc.png`, skill 2 | — | `1.1.1_fig_2_summary.png`, cel rij 2 kolom 1 | `1.1.1_fig_2_web_light.svg/png` + `1.1.1_fig_2_web_dark.svg/png` |
| `1.1.1_fig_3` | `1.1.1_fig_3_slide.png`, slide 5 | `1.1.1_fig_3_doc.png`, skill 2 | — | `1.1.1_fig_3_summary.png`, cel rij 3 kolom 1 | `1.1.1_fig_3_web_light.svg/png` + `1.1.1_fig_3_web_dark.svg/png` |
| `1.1.1_we_1` | `1.1.1_we_1_slide.png`, slide 6 | `1.1.1_we_1_doc.png`, skill 2 | — | `1.1.1_we_1_summary.png`, cel rij 3 kolom 2 | `1.1.1_we_1_web_light.svg/png` + `1.1.1_we_1_web_dark.svg/png` |
| `1.1.1_ex_1` | — | — | `1.1.1_ex_1_doc.png`, sectie staafdiagrammen | — | `1.1.1_ex_1_web_light.svg/png` + `1.1.1_ex_1_web_dark.svg/png` |
| `1.1.1_news_woningtekort.png` (nieuw) | — | — | — | — | — (alleen voor nieuws met visual; niet uit Part A boekbeeld) |

Begeleide inoefening: scaffoldImage-veld verplicht voor elke opgave die grafiek- of cijfervergelijking vraagt. Kandidaten: `1.1.1_we_1_doc.png` voor tarwe/maïs-opgaven, `1.1.1_ex_1_doc.png` voor drie-gewassen-uitleg, `1.1.1_fig_2_doc.png` voor alt.kosten-visualisatie; HTML gebruikt de matching web-light/web-dark conceptvariant.

---

## Game data outlines

Niet in het standaard template, maar zelfde bron van waarheid voor de 5 game-data files in `<book>/shared/`.

### Quiz (shared/questions/1.1.1.js — 15 vragen, 3–4 categorieën, ≥1 difficulty:3 per categorie)

Categorieën voorstel:
- **Schaarste herkennen** (4 vragen, moeilijkheid 1–3): ja/nee + uitleg in context.
- **Alternatieve kosten berekenen** (5 vragen, moeilijkheid 1–3): 2–3 alternatieven gegeven, beste niet-gekozen identificeren.
- **Procedure economisch denken** (3 vragen, moeilijkheid 2–3): stap-voor-stap, gegeven context.
- **Misconcepties** (3 vragen, moeilijkheid 2–3): pitfalls uit B01/B02 (schaarste ≠ weinig, alt.kosten ≠ prijs, alt.kosten ≠ som).

### Newsdetective (shared/newsdetective/1.1.1.js — 4 rounds)

Real Dutch article over woningtekort (zie §News plan). 4 rondes: (1) Claim identificeren; (2) Bron en betrouwbaarheid; (3) Schaarste- en alt.kosten-lens toepassen; (4) Eigen redenering.

### Reasoning (source-data/book-1/reasoning/1.1.1.csv → shared/reasoning/1.1.1.js — 15 regels, 5 modes)

Scenario-based reasoning rond schaarste en alt.kosten. Dekkend voor beide concepten; modes wisselen tussen causaal, vergelijkend, hypothetisch, kritisch, besluitvormend.

### Procedure (shared/procedure/1.1.1.js)

Eén procedure, gebaseerd op B02 uit het unit-register. Stappen volgen B02.procedure letterlijk (4 stappen). Context-wrapper: boer-met-10-ha of scholier-met-€20.

### Skilltree (auto-generated door deploy.js — `skilltree: {skills: null}` → alle units zichtbaar)

Geen handmatige data nodig; `shared/skilltree/1.1.1.js` al gegenereerd in commit 789643b.
