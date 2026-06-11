# Paragraph Landing Layout V2

Status: CANONICAL PARAGRAPH LANDING BASELINE.
Approved by human direction in LANDING-V2-PARAGRAPH-ROUTE-REPLACEMENT.

This layout replaces the previous generated paragraph landing model. Future
work may extend this model, but may not rebuild from or preserve the old
paragraph landing structure unless explicitly approved by human review.

## Product End State

The paragraph landing page is the operational student route for one paragraph.
It must make the route visible as one coherent interface, not as a loose list of
textbook pages, downloads, and games. It implements the product end-state
requirement that every paragraph gives the student a visible route from current
readiness to local target-equivalent proof.

## Non-Negotiable Requirements

- The V2 layout replaces the old paragraph landing structure.
- Do not revive or extend the old paragraph landing structure without human
  review.
- The page uses one shared DOM structure for light and dark mode.
- Every paragraph renders the same six-row route structure.
- Missing future surfaces remain visible as explicit disabled placeholders.
- Placeholder tiles must not contain fake links or silent no-op links.
- Student-facing labels must not expose internal MTU, operation, or route codes.
- The generator owns the output; generated lesson output must not be
  hand-patched to satisfy this layout.

## Required Row Contract

1. Start
   - Instapquiz voorkennis
   - Nieuws-detective

2. Skill-tree games
   - Redeneren
   - Rekenen
   - Grafieken

3. Leer
   - Uitleg vaardigheden
   - PowerPoint-presentatie
   - Skill engine / leerpad

4. Oefen
   - Begeleide oefeningen
   - Zelfstandige oefeningen
   - Adaptieve oefenroute

5. Check
   - Korte check
   - Exit ticket

6. Open & verdiep
   - Lesboek openen
   - Opgaven & antwoorden or equivalent source/check material
   - Aanvullend materiaal

## Tile Availability States

`available`

The tile links to a generated artifact.

`in-preparation`

The tile is visible but disabled with copy such as `In voorbereiding`. It has no
fake link and no silent no-op.

`not-scoped`

Use only when a paragraph type genuinely does not need a tile. This should be
rare and must be justified in generator rules.

## Data Mapping Contract

### Start

- Instapquiz voorkennis: prefer `files.voorbereiden.instapquiz`; otherwise
  `in-preparation`.
- Nieuws-detective: prefer `files.voorbereiden.nieuwsdetective`; otherwise
  `in-preparation`.
- The old separate voorkennis document is not a third Start tile by default.

### Skill-tree Games

- Redeneren: prefer `files.oefenen.redeneerSpel`.
- Rekenen: prefer scoped `files.oefenen.wiskundevaardigheden` / skilltree
  route.
- Grafieken: prefer `files.oefenen.grafiekenspel`.

These tiles stay in the second row. Do not bury them inside Oefen or Verdiep.

### Leer

- Uitleg vaardigheden: prefer `files.leren.vaardigheden.html`.
- PowerPoint-presentatie: prefer `files.leren.presentatie.html` or `.pptx`.
- Skill engine: prefer a current student-facing skill-map / route surface when
  present; otherwise `in-preparation`.

The skill engine is a student product surface. It should show relevant
paragraph skills, local route, current focus, and useful next action without
internal codes or unsupported mastery claims.

### Oefen

- Begeleide oefeningen: prefer `files.oefenen.begeleide.interactief`.
- Zelfstandige oefeningen: prefer `files.lesboek.opgaven.html`, with answers as
  a secondary link where appropriate.
- Adaptieve oefenroute: placeholder or local-advice route only. Allowed wording
  includes `voorgestelde volgende oefening` and `lokaal advies`. Forbidden
  wording includes diagnostics, mastery, automatic sequencing, grade, and
  pass/fail claims.

### Check

- Korte check: prefer `files.check.shortCheck`; otherwise `in-preparation`.
- Exit ticket: prefer `files.check.exitTicket`; otherwise `in-preparation`.

The short check and exit ticket are separate surfaces with different authority.
Do not use one current file to pretend both surfaces exist.

### Open & Verdiep

- Lesboek openen: prefer `files.lesboek.paragraaf.html`; offer PDF as secondary
  download only if present.
- Opgaven & antwoorden: prefer `files.lesboek.opgaven.html` plus
  `files.lesboek.antwoorden.html`.
- Aanvullend materiaal: prefer samenvatting, nieuws met visual, YouTube, and
  extra source material.

This row replaces the old broad Verdiep block. Useful legacy resources may
appear here only inside this row structure.

## Styling Contract

Light mode is the primary product baseline:

- warm paper background;
- clean left sidebar;
- breadcrumb/topbar;
- large hero block;
- right-side leerpad panel;
- six route chips;
- row label column;
- card grid;
- soft shadows;
- low visual clutter;
- clear category accents.

Dark mode uses the same DOM structure, navigation pattern, row model, tile
hierarchy, and spacing, with only theme-token changes for background, surfaces,
borders, muted text, accent contrast, and shadow strength.

Do not implement the earlier dashboard-style dark mode with status cards,
avatar, streak panel, or different navigation.

## Core-Requirement Checklist

- [ ] Generated paragraph pages render the six V2 rows.
- [ ] Start row contains Instapquiz voorkennis and Nieuws-detective.
- [ ] Skill-tree games row contains Redeneren, Rekenen, and Grafieken.
- [ ] Leer row contains Uitleg vaardigheden, PowerPoint-presentatie, and Skill
      engine / leerpad.
- [ ] Oefen row contains Begeleide oefeningen, Zelfstandige oefeningen, and
      Adaptieve oefenroute.
- [ ] Check row contains Korte check and Exit ticket as separate tiles.
- [ ] Open & verdiep row contains Lesboek openen, Opgaven & antwoorden, and
      Aanvullend materiaal.
- [ ] Missing future surfaces are explicit disabled placeholders.
- [ ] No tile has a fake link or silent no-op.
- [ ] Light and dark mode share one layout.
- [ ] Rendered light, dark, and narrow/mobile proof exists for review.
