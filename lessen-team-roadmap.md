# Lessen Team Roadmap

## Sprint Ledger

The currently-active sprint sits at the top. Future sprints follow in sequence.
Closed sprints are recorded separately in the "Closed Sprints" section below.

| Sprint | Name | Completed | Current State |
|--------|------|-----------|---------------|
| L1.5P | Boek 1 Print-Edition Cut for Publisher | no | **URGENT** — publisher hand-off in a few weeks (as of 2026-05-11; owner to fill in exact date). Trim Boek 1 to print page budget; first candidate to remove from print is `1.5 Hoofdstuk Toetsvoorbereiding` (move to website-only). Other long stretches and full answer keys reviewed for print/web split. Runs in parallel with the companion-quality stream; does not block L1.4. |
| L1.5D | Authored Content As Web | **2026-05-11** | **CLOSED 2026-05-11 PASS WITH FLAGS**. D1 (DOCX-as-web for samenvatting + nieuws) and D2 (PPTX-as-web for presentatie) both shipped. v2 lead review returned FAIL with eight blockers (B1–B8); remediation cycle closed all eight: B1+B2 mobile responsive CSS at 390px (platform `362f0e2`), B7 detect_card_stack x-column filter (platform `6646bec`), B5+B6 validator gates D1 web outputs + BUILD-PARAGRAPH.md 24→27 contract (platform `b90b918`), B4 validate-chapter.js structured verdict parser (platform `e04d160`), B8 PPTX accessibility — 14pt floor across deck + speaker notes + AA contrast tokens (platform `830ebf4`). Selector-presence regression test added (`l1-5d-v2-mobile-fixes.test.js`). v3 lead review returned **PASS WITH FLAGS**: validators 27/27 + 26/26 + 454/0/7 jest + audit 0 sub-14pt + 0 contrast violations all green. Two non-blocking flags remain: long Dutch compound nouns on slide 1's dark-hero body line and nieuws cell-title still wrap with mid-word breaks at 390px (logged as platform follow-up, not reopening the sprint). |
| L1.5V | Companion Quality Polish + Pilot Lock-in for 1.1.1 | **2026-05-09** | **CLOSED 2026-05-09**. 17 platform commits on `content/1.1.1-companion-quality` + 2 lessen commits on `main`. All 4 hard fails + QA-1 from the original `1.1.1-companion-visual-review.md` resolved; verification sub-agent verdict **PASS WITH FLAGS** (3 non-blocking flags: visual-internal `alt. kosten` shorthand documented as scope decision, Team B reference HTMLs untracked-by-design, optional CSS polish on vaardigheden checklist trailer). Buckets A+B+C+D+E+F all closed. Validator `--mode complete` flips green: `OK Paragraph 1.1.1 PASSED all checks`. Jest 441/0/7 (69 new regression tests vs baseline). Pilot lock-in delivered: `BUILD-PARAGRAPH.md` carries Common pre-conditions section + clean Part A / Part B split, every skill in `skills/` has a `pipeline:` frontmatter label, `validate-paragraph.js` has F2 fixes (split Part A / Part B review gates, structured verdict parser, schema_version 2 awareness), `1.1.1-quality-ref.yaml` migrated to schema_version 2 with `partA:` + `companion:` blocks. L1.4 unblocked. |
| L1.4 | First Pipeline Regression Paragraph | no | **L1.5V Bucket F CLOSED 2026-05-09 — pilot lock-in delivered, L1.4 unblocked.** Still after L1.5D D2 (which itself resumes after L1.5V close, now satisfied). Paused 2026-04-30 (was active since 2026-04-25). Building `1.1.2 Percentages en indexcijfers` runs against the cleaned-up Part A / Part B QC pipeline established by §1.1.1's pilot lock-in (BUILD-PARAGRAPH.md restructured, validator modes split + schema_version 2 quality-ref). Triple regression purpose stays: layout + games (on reworked unit-register `c21ee14`) + DOCX/PPTX-as-web on fresh content. May test PV formula/table templates only if PV.2/PV.3 are ready; must not wait for full PV completion. |
| L1.5B | Layout Round 2 — Generator Items | no | After L1.4. Originally L1.5. Acts on what L1.4 surfaced + the deferred round-2 item #3 (split valkuilen pitfalls) + the deferred item #1 (per-section card accents — reclassified as generator-touching by L1.5A planner). |
| L1.5G | Three-Aspect Game Coverage | no | After L1.5B. Bring the user's graphical-game prototype into the platform; one working prototype per learning aspect (reasoning, calculation, graphical). Architectural constraint: each game accepts adaptive input via localStorage; existing 5 games get a light refactor for the same seam. Graphical-game semantics must align with PV records where they exist. |
| L1.6 | Second Pipeline Regression Paragraph | no | After L1.5G. Third Book 1 paragraph build confirms Round 2 layout + the new graphical game + the adaptive-input seam survive a fresh end-to-end build, with at least one procedure/visual sequence generated from or validated against PV data if the PV registry is available. |
| L1.7 | Post-Layout Scaling Decision | no | After L1.6. Decide whether to expand broadly once L1.3A-C through L1.5G have proven the layout, web-doc, and game pipelines survive two independent paragraph builds; include PV readiness in the scaling decision. |
| L2.1 | Book 1 Release Polish | no | Teacher-facing polish continues under the Book 1 health gate. |
| L2.2 | Book 2 Part A Textbook Layer | no | Start Book 2 Part A only under the chapter/paragraph hard gates. |

## Closed Sprints

Closed sprints in reverse-chronological order. The full record of each sprint
remains in the "Sprint Details" section further down.

| Sprint | Name | Closed | One-line summary |
|--------|------|--------|-------|
| L1.5A | Easy Layout Round 2 | 2026-05-01 | Shipped book-root back-link guard (platform `5b8c216`) + BI static back-link (platform `b9c5085`); lessen-side `2a8455b` regenerated. Verification: SHIPPED CLEAN, all 4 baseline gates green. Platform PR https://github.com/meijer1973/4veco-platform/pull/2 open at close awaiting merge to platform main. Item #1 reclassified as generator-touching, deferred to L1.5B. |
| L1.3C | PowerPoint Presentation Improvement | 2026-04-25 | `1.1.1` PPTX regenerated with adapted slide visuals; teacher-supporting slide rules + read-through QA gate documented in `econ-pptx-templates`; LibreOffice roundtrip clean. |
| L1.3B | Companion SVGs And Light/Dark Visual Variants | 2026-04-25 | `lib-visual-surfaces.js` is the shared SURFACES/THEMES module; light/dark symmetry validator enforced; news visual on the variant system; game-visuals decision recorded per paragraph. |
| L1.3A | Basic HTML Layout And Front-End Usability | 2026-04-25 | `1.1.1` companions on shared platform layout/theme; converters and landing-page generator landed in platform; browser smoke + technical gates green. |
| L1.2 | Second Companion Technical Probe | (pre-restructure) | `1.1.2` proved the technical pattern can repeat; probe materials were removed for didactic rebuild. |
| L1.1 | First Companion Technical Pilot | (pre-restructure) | `1.1.1` passes the current complete technical gate. |
| L0.5 | Green Gate Handoff | (pre-restructure) | Book 1 Part A and the platform/book health routine are green. |

## Roadmap Metadata

Generated: 2026-04-23
Updated: 2026-04-25 after Sprint L1.3A-C close — basic HTML layout, companion SVG variant system with light/dark symmetry validator, and PPTX teacher-supporting slide rules all landed in platform; L1.4 (pipeline regression on `1.1.2 Percentages en indexcijfers`) is now active.
Updated: 2026-04-30 — sprint sequence restructured. L1.4 paused to ship layout polish + web-native authored content first; L1.5 split into L1.5A (single-paragraph-safe items, active now) and L1.5B (generator-touching items, after L1.4). New L1.5D (DOCX/PPTX as web) sequenced before L1.4 because both should be tested against L1.4's fresh-paragraph regression. New L1.5G (three-aspect games coverage) sequenced after L1.5B with adaptive-ready architecture as a cross-cutting constraint. L1.4 resumes with triple-purpose scope: layout + games + web-docs regression on fresh content.
Updated: 2026-05-01 — added the PV Consumption Rule after leadership approved the Procedure-Visual Backbone. The lesson repo remains a generated target and consumer: L1.5G aligns the graphical game with platform/reference PV records, L1.6 proves one PV-backed or PV-validated procedure/visual sequence on a fresh paragraph, and L1.7 includes PV readiness before scaling.
Updated: 2026-05-01 — Sprint Ledger reorganized: active sprint sits at the top, future sprints follow, and closed sprints moved to a separate "Closed Sprints" archive. L1.5A closed (lessen `2a8455b` shipped, platform PR #2 open at close); L1.5D promoted to active sprint.
Updated: 2026-05-09 — L1.5V (Vaardigheden Quality Polish for 1.1.1) inserted between L1.5D D1 and L1.5D D2. Triggered by a Team B reference draft that surfaced visual-text mismatches, scaffold gaps, and a canonical-procedure ambiguity in the existing `uitleg vaardigheden.html`. Canonical procedure decision recorded: B02 is 4-step (was 3-step in `_paragraph-plan.md`), driving registry update + propagation across vaardigheden, samenvatting, presentatie, stappenplan, BI, opgaven. L1.5D D1 shipped 2026-05-08; PR #3 awaiting merge before L1.5V branches off main. L1.5D D2 paused, resumes after L1.5V.
Updated: 2026-05-11 (later) — L1.5D **CLOSED PASS WITH FLAGS** after a v2-review remediation cycle. D1 (DOCX-as-web for samenvatting + nieuws) shipped earlier; D2 (PPTX-as-web for presentatie, slide-by-slide with prev/next/keyboard/sidebar) shipped this session. Then v2 lead-review returned FAIL with 8 blockers (mobile responsive overflow at 390px on all three D1+D2 web surfaces, caption absorbed into card subtitle, D1 web files ungated in validator, stale 24-file Part B doc, chapter validator using token-grep instead of structured verdict, PPTX accessibility 56 sub-18pt runs + 2.9:1 contrast). All 8 closed across platform commits 362f0e2 / 6646bec / b90b918 / e04d160 / 830ebf4 + regression test ae60dc6. v3 lead-review returned PASS WITH FLAGS — gates green (27/27 validator, 26/26 check:book, 454/0/7 jest, 0 sub-14pt audit, 0 contrast violations), two non-blocking flags on mid-word Dutch compound-noun wraps logged as platform follow-up. L1.4 (pipeline regression on §1.1.2) and L1.5B (Layout Round 2 generator items) are now both unblocked.
Updated: 2026-05-11 — added Sprint L1.5P (Boek 1 Print-Edition Cut for Publisher) as a parallel urgent sprint; publisher hand-off in a few weeks. Added the "Adaptive learning replaces three-track differentiation" subsection to the architecture chapter to record that basis/middenopgaven/verrijking will be deprecated next school year (2026/27 cohort) in favor of a dynamic adaptive `begeleide inoefening`, with the repo-wide audit scoped explicitly out of this roadmap. Lesboek section added to the platform landing-page builder (`build-landing-page.js`): every paragraph index now shows the textbook source (`paragraaf` HTML + PDF, `opgaven`/`antwoorden` HTML + PDF) as a final row at the bottom — landed on §1.1.1's regenerated index.
Updated: 2026-05-09 (later) — L1.5V scope EXPANDED to "Companion Quality Polish + Pilot Lock-in for 1.1.1" after (a) the `econ-companion-visual-review` agent ran on `uitleg voorkennis` and returned FAIL with four hard-fail defects + QA-1 (DOCX style collision), several of which are upstream platform issues shared with vaardigheden, and (b) the user direction that §1.1.1 is the pilot paragraph and L1.5V is the moment to set up the Part A / Part B build skill, quality test, and review-agent pipeline cleanly before L1.4 starts paragraph 2. New buckets E (Part A QC integration — fold in the previously deferred quality-record schema extension) and F (Part A / Part B QC pipeline separation pilot, gating L1.4) added. New platform skill `skills/econ-companion-artifacts.md` is the authoring spec; `agents/econ-companion-visual-review.md` is the closure gate. PR #3 merged; L1.5V branches off platform main as `content/1.1.1-companion-quality`. L1.4 row updated to mark Bucket F closure as a pre-condition. See full sprint detail below for the six-bucket item list and per-item workflow that pairs the skill with the review agent on every iteration.
Source: split from `knowledge/three-month-roadmap.md` after Sprint 0.5 sign-off

## Mission

Own the material side of delivery:

- Book 1 release polish
- Book 2 Part A textbook production
- companion MVP work, treated as an active pilot until quality and usability are good enough to scale

## Current Status

Sprint 0.5 is signed off for Part A textbook/book production.

That means:

- Book 1 Part A is green.
- Book 2 Part A can start.
- Companion production may continue, but it is still pilot work.

The first companion pilot has now been run, and the technical pattern has also
been repeated for a second paragraph. The 1.1.2 probe materials were removed
after the technical test because that paragraph must be recreated with explicit
teaching and didactic design instructions. That does not finish the companion pilot.
The main current issue is companion layout, image integration, and front-end
usability: the materials need to feel more usable, readable, navigable, and
visually coherent before this pattern is repeated across many paragraphs. Images and
graphs should no longer feel like pasted textbook assets. They must be adapted
to the surface where they appear: web pages, PowerPoint presentations, Word
documents, summaries, and interactive/game pages can each need different layout,
contrast, scale, and annotation treatment.

Important boundary:

- A complete paragraph plus companion pipeline is not yet routine.
- The first companion paragraph proves that the workflow can run, not that the
  output design is good enough.
- Bulk companion production should wait until layout/UI improvements are
  integrated into the platform workflow.
- Bulk companion production should also wait until visual assets have a
  platform-owned variant workflow, including light/dark web variants where
  graphics contain labels, axes, fills, backgrounds, or other theme-sensitive
  elements.

## Team Guardrails

- Keep Book 1 green while editing:

```powershell
npm.cmd run check:book -- "..\4veco-lessen\Boek 1 - Grondslagen, vraag en aanbod"
```

- Reviews and quality refs are mandatory artifacts, not optional paperwork.
- Rebuild affected paragraph/chapter/book HTML/PDF whenever source markdown or assets change.
- Do not scale companion production until the pilot has passed both technical validation and layout/usability review:

```powershell
node scripts\validate-paragraph.js --mode complete "<paragraph-folder>"
```

- Every layout or user-interface improvement must be integrated in the platform, not patched into one generated lesson file.
- Every visual or image-integration improvement must also be integrated in the platform. Do not hand-paste one-off images into generated lesson files.
- Reusable UI work belongs in `C:\Projects\4veco\4veco-platform`: templates, shared CSS/JS, converters, generators, validators, or build scripts.
- Reusable visual work belongs there too: SVG builders, surface-variant renderers, converter support for light/dark web images, and rules for PowerPoint/game/doc variants.
- Generated output in `4veco-lessen` may show the result, but it should not become the source of truth for UI changes.

## PV Consumption Rule: Visual Backbone Alignment

The lesson repository remains a generated student-facing target. Procedure-visual semantics live in the platform/reference layer, starting with the Procedure-Visual Registry under `4veco-platform/references/data/procedure-visual/`.

L1.5G graphical-game work must align with the Procedure-Visual Registry where PV records exist. The graphical prototype may not hard-code a separate semantic model for operations, visual states, or procedure sequences that the PV layer already defines.

L1.6 must use one fresh paragraph build to prove at least one procedure/visual sequence can be generated from or validated against PV data, if the PV registry and validator have reached the required gate.

L1.7 scaling decision must include PV readiness: procedure consistency, visual semantic anchors, surface variants, game mapping, answer-model alignment, and generator-block controls.

## Layout Reference

Use this local legacy/rewire file as a reference input for the next companion UI pass:

```text
file:///C:/Projects/4veco/3-Module-3-rewire-test/3.1%20Hoofdstuk%201%20-%20Markten/3.1.1%20Paragraaf%201%20-%20Markt%20en%20marktstructuur/1.%20Voorbereiden/3.1.1%20Markt%20en%20marktstructuur%20%E2%80%93%20uitleg%20voorkennis.html
```

This is not the end state. It is better than the current companion layout and is
useful because it already shows several patterns worth studying:

- sidebar navigation by section
- mobile menu toggle and overlay
- hero section with section cards
- domain badges and domain-colored section headers
- clearer content blocks, formula boxes, callouts, summary tables, and checklist
- more obvious document structure for students

The task is not to copy this file by hand. The task is to turn the useful parts
of this direction into a platform-owned companion layout system.

## Architecture: adaptive-ready from L1.5G onward

The companion's eventual end-state is adaptive paragraphs: after a student takes
a first quiz, an advisor surfaces guidance ("focus here next, skip this, try the
harder variant") and the games adapt to that guidance — difficulty, focus, or
sequencing. That advisor and its evaluation logic are not built in this roadmap.

But L1.5G builds the seam in place so the adaptive layer can wire in later
without re-engineering the games. Concretely:

- Every game (the graphical prototype landing in L1.5G plus the existing five —
  quiz, newsdetective, reasoning, skilltree, procedure) accepts an adaptive
  payload at runtime by reading a well-defined localStorage key.
- Today the payload is empty / paragraph-default; games behave as they do now.
- Tomorrow a post-quiz advisor populates that key; games read it and adapt
  without engine changes.

Implication for L1.5G scope: existing games get a light refactor to expose the
same hook the new graphical game implements, even though no advisor writes to
it yet. Doing this in L1.5G — alongside the new game — is cheaper than
retrofitting all six games under pressure later.

Out of scope for this roadmap: building the advisor, defining the payload
schema beyond a placeholder, or shipping any adaptive behavior. Those are a
later sprint cycle.

### Adaptive learning replaces three-track differentiation (next-year cycle)

The current three-track differentiation method — basisopgaven /
middenopgaven / verrijkingsopgaven (three pre-authored static handouts at
fixed difficulty) — will be deprecated next school year (2026/27 cohort).
It is replaced by a dynamic, adaptive version of `begeleide inoefening`:
same exercise companion surface, but items, hints, and difficulty are
chosen at runtime against the same adaptive-payload seam that L1.5G
builds for the games. One adaptive exercise surface, not three static
handouts.

This is a future sprint cycle, scheduled after L1.7. It is not built in
this roadmap; the only thing this roadmap carries is the shared seam, so
the dynamic `begeleide inoefening` can wire onto the same localStorage
payload when the advisor lands.

Repo-wide changeover note (for the future adaptive-learning sprint, not
now): when the three-track method is dropped, every reference to it must
be updated in one deliberate pass — the landing-page builder section
"Opgaven" and its `HIDE_TASK_ROWS` flag, paragraph plans
(`_paragraph-plan.md`) that name the three tracks, exercise builders
(`b1-XYZ-opgaven.js` and the per-track DOCX builders), companion-skill
and review-agent rules that assume the three-track scaffold, fixtures
under `engines/tests/` and `references/`, and this roadmap's own mentions
of basis / midden / verrijking. The changeover sprint must include a
deliberate repo-wide audit so the deprecation does not leave half-renamed
references behind.

## Sprint Details

### Sprint L0.5: Green Gate Handoff

Completed: yes.

Purpose:

- accept the platform/book health routine as good enough for controlled material work
- keep Book 1 Part A green
- allow controlled companion pilot work

Evidence:

- `check:book` passes for Book 1.
- `validate-paragraph.js` supports the flat paragraph layout.
- companion output may be produced under the documented platform workflow.

### Sprint L1.1: First Companion Technical Pilot

Completed: yes.

Purpose:

- run one real companion paragraph through the complete Part B workflow
- expose platform, validator, build, layout, and usability gaps before scaling

Current state:

- `1.1.1 Schaarste en economisch denken` has a full companion set.
- The complete technical validator passes.
- A platform-team quality-gate review has been created for validator/source/quality-ref gaps.

Exit criteria:

- one pilot paragraph passes complete-mode validation. Done for `1.1.1`.
- known source/quality-gate gaps are handed to the platform team. Done in the platform quality-gate review.

### Sprint L1.2: Second Companion Technical Probe

Completed: yes.

Purpose:

Prove that the current companion workflow can repeat once content/data inputs exist.

Evidence:

- `1.1.2 Percentages en indexcijfers` has been used as the second technical probe.
- The platform roadmap records it as passing complete-mode validation.
- This proves technical repeatability, not final companion quality.
- The generated 1.1.2 test materials have been cleared and must not be used as lesson content.

Exit criteria:

- two Book 1 companion paragraphs pass complete-mode validation during technical probing. Observed for `1.1.1` and `1.1.2`; 1.1.2 now awaits didactic rebuild.
- repeated setup steps are saved or documented in the platform workflow.
- remaining risks are moved to layout/usability and quality-gate work.

### Sprint L1.3A: Basic HTML Layout And Front-End Usability

Completed: yes.

Closed: 2026-04-25.

Purpose:

Make the basic companion HTML pages easier to read, navigate, and use before
scaling the companion pipeline.

Scope:

- `uitleg voorkennis.html`
- `uitleg vaardigheden.html`
- `begeleide inoefening.html`
- paragraph `index.html`
- game shell pages only where navigation or framing is visibly weak

Current evidence:

- `1.1.1` default `uitleg voorkennis.html` now uses the shared platform layout instead of only the rollback/test filename.
- `1.1.1` `begeleide inoefening.html` now uses the shared platform theme layer.
- `1.1.1` `uitleg vaardigheden.html` remains on the shared theme layer after deploy reskin and now avoids duplicate/oversized legacy back-link SVG behavior.
- Browser smoke passed for `uitleg voorkennis`, `uitleg vaardigheden`, and `begeleide inoefening` at desktop/mobile widths in light and dark mode.
- Technical gates passed after regeneration: deploy link/data checks, complete paragraph validation, and Book 1 `check:book`.

Work:

- Compare current Book 1 companion pages against the improved rewire reference file.
- Improve navigation, mobile behavior, hierarchy, callouts, section scanning, and visual consistency.
- Keep the layout implementation in the platform: shared CSS/JS, converters, templates, and build scripts.
- Rerun the pilot output after platform changes.
- Browser-check the improved pages on desktop and mobile widths in light and dark mode.

Exit criteria:

- The basic `1.1.1` companion HTML pages have improved layout/usability from platform-owned sources.
- The improved layout can be regenerated, not hand-maintained.
- The local reference file has been used as input, but the result is a new Book 1 companion design direction.
- Link/reachability and browser smoke checks pass for the improved companion pages in light and dark mode.
- A human usability review signs off that this layout is good enough to use as the scaling baseline.

### Sprint L1.3B: Companion SVGs And Light/Dark Visual Variants

Completed: yes.

Closed: 2026-04-25.

Purpose:

Replace raw copy-pasted textbook imagery with proper companion SVGs and
surface-specific variants, including explicit light/dark web visuals where
needed.

Current evidence:

- `SURFACES` and `THEMES` are now a single platform-owned module (`4veco-platform/build-scripts/lib/lib-visual-surfaces.js`). Both the figure/worked-example/exercise builder (`b1-111-visual-variants.js`) and the news builder (`b1-111-nieuws.js`) import from it.
- The news visual `1.1.1_news_woningtekort` is now produced through the shared variant system: `doc`, `web_light`, `web_dark` surface variants plus a canonical base file, with the Word document embedding the `_doc` PNG instead of a raw base screenshot.
- `b1-111-visual-variants.js` still regenerates slide, doc, summary, web-light, and web-dark variants for `1.1.1` figures/worked examples/exercises. Byte-diff after the shared-lib refactor was empty.
- `1.1.1` `uitleg voorkennis.html`, `uitleg vaardigheden.html`, and `begeleide inoefening.html` use light/dark image swapping where themed visuals exist.
- Browser smoke confirmed the correct light/dark image sources on desktop and mobile (pre-refactor; re-check after the news variant regeneration is still needed).
- `validate-paragraph.js --mode complete` now enforces `_web_light`/`_web_dark` symmetry: any variant declared without its counterpart (in `_paragraph-plan.md`) fails the gate. 6 pair(s) pass for 1.1.1 today. Platform unit tests green; a temp fixture confirmed the new FAIL path fires.
- The game/interactive visuals decision for 1.1.1 is recorded in `1.1.1/_paragraph-plan.md` §"Game visuals decision (L1.3B)": no concept-visual slot for this paragraph; revisit per-paragraph.

Work:

- Treat Part A textbook images as source material, not finished companion artwork.
- Replace literal book-image copy-pasting with adapted SVGs or regenerated visuals that fit each companion surface.
- Define visual variants per surface where needed: slide, docx, summary thumbnail, web-light, web-dark, and game/interactive variants.
- Make web visuals adaptable to light and dark mode. Any graphic with text, axes, fills, backgrounds, or low-contrast colors needs explicit light and dark variants.
- Make sure visual changes are implemented in the platform through SVG builders, surface-variant renderers, converter support, templates, and validators where needed.
- Decide whether game/interactive pages need explicit concept-visual slots or whether their current generated UI is sufficient for this paragraph.

Exit criteria:

- `1.1.1` companion images are adapted to their surfaces rather than copy-pasted from textbook material.
- Web pages use the correct light/dark image variants where graphics need theme-specific treatment.
- Word documents, summaries, and interactive/game surfaces use visuals sized and composed for their actual use.
- The improved visual variants can be regenerated from platform-owned builders, not hand-maintained.
- `validate-paragraph.js --mode complete` still passes after visual regeneration.

### Sprint L1.3C: PowerPoint Presentation Improvement

Completed: yes.

Closed: 2026-04-25.

Purpose:

Improve the companion PowerPoint so it is a classroom-ready presentation, not a
deck with pasted book images.

Current evidence:

- The `1.1.1` presentation builder regenerated the PPTX using adapted slide visuals.
- The generated PPTX round-tripped through LibreOffice successfully.
- Complete paragraph validation still passes after regeneration.

Work:

- Make PowerPoint visuals fit the presentation layout: readable from the back of class, aligned with slide typography, and not just pasted as book screenshots.
- Use slide-specific visual variants with clear composition, contrast, scale, and annotation treatment.
- Keep PowerPoint improvements in the platform presentation builder and reusable visual-variant workflow.
- Review the slide narrative, teacher flow, visual hierarchy, and classroom readability.

Exit criteria:

- The `1.1.1` PPTX uses visuals sized and composed for presentation use.
- The presentation can be regenerated from platform-owned sources.
- The deck opens/round-trips without repair.
- A presentation-quality review signs off before the deck pattern is reused across more paragraphs.

### Sprint L1.5A: Easy Layout Round 2

Completed: yes.

Closed: 2026-05-01.

Active 2026-04-30 → 2026-05-01 (pulled forward of L1.4 to ship single-
paragraph-safe layout fixes while the platform team was at a stable point —
`c21ee14` closed the unit-register gap with
`fix(skilltree): hide generator-blocked catalog units`).

Purpose:

Ship the low-risk subset of the rolled-back round-2 layout candidates from the
2026-04-29 attempt — the items that can be validated against `1.1.1` alone, do
not touch generators in ways that need a fresh-paragraph regression, and
include the one observable Pages regression introduced by round-1.

Pre-flight done:

- Platform baseline gate suite green on `c21ee14` (jest 364 pass, deploy.js
  link+data tests pass, check:book 26/26, validate-paragraph 1.1.1 complete
  pass) on 2026-04-30.
- Layout worktree staged at `C:/Projects/4veco/4veco-platform-layout` on branch
  `layout/1.1.1-round-2-redo` from `c21ee14`.

Shipped scope (per L1.5A planner sub-agent classification):

- Item #0 — book-index back-link guard. Platform commit
  `5b8c216 fix(voorkennis): skip back-link injection on book-root landing`.
  Adds a 3-line guard in `engines/voorkennis.js#injectBackLink` skipping
  injection when `document.body.dataset.layout === 'landing-book-v1'`. Fixes
  the `Overzicht` link 404 introduced by round-1 commit `3db70d8`.
- Item #2 — Begeleide-Inoefening static back-link via converter. Platform
  commit `b9c5085 feat(bi-converter): emit static back-link in shared-CSS
  hero`. Adds the standard `<a class="back-link" href="../index.html">` to
  the BI hero in `convert_begeleide_inoefening.py`'s shared_prefix branch,
  mirroring the voorkennis pattern. Removes the brief flash of un-back-
  linked hero before JS runs.

Deferred to L1.5B (per L1.5A planner sub-agent reclassification):

- Item #1 — per-section accent on chapter/book index cards. Planner found
  that `.section-card` does not exist in the platform (cards are
  `.chapter-card` ~line 499 and `.para-card` ~line 542 in
  `build-landing-page.js`); they currently carry an inline 5-color palette
  accent, not the editorial 3-token system; editorial accent CSS rules
  require a `data-domain` attribute or matching class hook the cards do not
  carry. Implementation requires editing the generator (`build-landing-
  page.js` renderBookPage / renderChapterPage emission sites) — out of
  L1.5A scope, in L1.5B scope.

Out of scope, explicitly:

- Item #3 from rolled-back round-2 (split "Valkuilen en misvattingen" into
  per-card pitfalls) — touches `build-landing-page.js` generator structure,
  needs L1.4's fresh-paragraph regression to be safe. Deferred to L1.5B.
- DOCX/PPTX-as-web work — separate sprint L1.5D.
- New game work — separate sprint L1.5G.

Closing evidence:

- Platform PR https://github.com/meijer1973/4veco-platform/pull/2 opened from
  `layout/1.1.1-round-2-redo` to platform `main`. **Open at close**, awaiting
  merge.
- Lessen `2a8455b L1.5A: ship book-root back-link guard + BI static back-link`
  pushed to `origin/main`.
- Verification sub-agent on 2026-05-01 reported "L1.5A SHIPPED CLEAN":
  - Static HTML book root and chapter index emit the correct `data-layout`
    markers (`landing-book-v1` / `landing-chapter-v1`).
  - Deployed `shared/voorkennis.js` line 66 contains the
    `dataset.layout === 'landing-book-v1'` guard.
  - BI page has `<a class="back-link" href="../index.html">` with
    `Terug naar overzicht`, ordered before the `hero-badge` (correct DOM
    insertion).
  - Pages root URL returns HTTP 200 and lists Boek 1.
  - Baseline gates on the layout worktree: jest 364 pass / 6 skipped / 0
    failed; deploy.js link + 99 data tests pass; `npm run check:book` 26/26;
    `validate-paragraph.js --mode complete` for `1.1.1` PASSED.

Exit criteria (all met):

- selected items shipped via PR to platform `main`; lessen-side regenerated
  and pushed ✓ (PR open, lessen pushed)
- `validate-paragraph.js --mode complete` for `1.1.1` still passes ✓
- deploy.js + check:book + jest match the 2026-04-30 baseline ✓
- Pages browser-smoke confirms each item's expected change is live ✓
- the book-index `Overzicht` 404 link is gone ✓ (deployed `voorkennis.js`
  carries the guard; runtime no longer injects on the book root)

Open follow-ups:

- Merge platform PR #2 to durably land the fix on platform `main`. Until
  then, anyone running `deploy.js` from platform `main` regenerates without
  the guard. Lessen-side artifacts on Pages are unaffected — they already
  reflect the fix.
- After PR merge, update memory `project_open-regressions.md` to mark the
  back-link 404 regression resolved.

### Sprint L1.5D: Authored Content As Web

Completed: no.

Position: after L1.5A, before L1.4. Two-phase, single sprint.

Purpose:

Render authored Word and PowerPoint content natively on the paragraph pages so
students can read it in the same surface as the rest of the companion (light
and dark, mobile and desktop, sidebar navigation). Keep the original Office
files downloadable for users who want them. Move toward video-like classroom
material by surfacing PowerPoint speaker notes and (stretch) reading them
aloud.

Phase D1 — DOCX as web:

Some prior work exists; this phase consolidates and ships it.

- Render Word document content as web HTML on the paragraph page surface,
  using the platform-owned converter pipeline (extend
  `convert_voorkennis.py` / `convert_vaardigheden.py` / a new docx-content
  converter as appropriate).
- Light/dark theme variants throughout, matching the editorial CSS direction
  established in L1.3A.
- Keep the original `.docx` available as a download from the paragraph page.
- Link/reachability and complete-mode validation pass on `1.1.1` after
  regeneration.

Phase D2 — PPTX as web:

- Render slide content as web HTML on the paragraph page (slide-by-slide,
  navigable, light/dark-aware).
- Speaker notes shown below each slide on the web surface.
- Keep the original `.pptx` available as a download from the paragraph page.
- Stretch goal: text-to-speech readout of speaker notes via the Web Speech
  API, gated behind a "play" control. Pushes the surface toward
  video-like content. May not work on every browser; ship as
  progressive-enhancement, not core.

Exit criteria:

- DOCX content for `1.1.1` renders as web on the paragraph page with download
  link; passes the same gates the prior HTML conversions pass.
- PPTX content for `1.1.1` renders as web on the paragraph page with speaker
  notes and download link; passes gates.
- Where a paragraph uses a PV-backed visual state, web-rendered authored
  content preserves the same semantic visual anchor across docx/html/pptx
  surfaces. This is an acceptance criterion only; L1.5D does not build the PV
  schema.
- Both phases land in platform-owned converters / builders / templates, not
  hand-edited into generated output.
- `validate-paragraph.js --mode complete` for `1.1.1` continues to pass.

### Sprint L1.5V: Companion Quality Polish for 1.1.1

Completed: no.

Active 2026-05-09. Expanded scope after the `econ-companion-visual-review`
agent ran on `uitleg voorkennis` (review file
`1.1.1 Schaarste en economisch denken/1.1.1-companion-visual-review.md`)
and returned **FAIL** with four hard-fail defects plus a DOCX QA failure.
The voorkennis defects are largely **shared platform issues** (visual
frame, converter list rendering, checklist routing, alt-text emission)
that also constrain `uitleg vaardigheden`. Fixing them once unblocks
both surfaces. The original vaardigheden-only scope from the Team B
reference draft is retained as a sub-bucket of the expanded sprint.

Purpose:

Bring **both** companion explainer surfaces for §1.1.1 to a verdict of
PASS or PASS WITH FLAGS under `agents/econ-companion-visual-review.md`:

- `1.1.1 Schaarste en economisch denken – uitleg voorkennis.html` (and
  matching `.docx`).
- `1.1.1 Schaarste en economisch denken – uitleg vaardigheden.html`.

For vaardigheden, integrate the strongest didactic improvements from a
Team B reference draft (`uitleg vaardigheden team b.html`) into Team
A's platform-consistent two-section structure (B01 schaarste
herkennen, B02 alternatieve kosten berekenen). Team A stays the
implementation baseline because it is closer to the platform structure
(canonical skill sections, generated companion layout, themed web
visual hooks); Team B is treated as a quality-improvement source, not
a competing production baseline.

Authoring spec + review gate:

- **Skill** (authoring + regeneration): `skills/econ-companion-artifacts.md`
  on the platform side. New as of 2026-05-09. It encodes the
  platform-wide rules for student-facing companion artifacts and is
  required reading before edits.
- **Review agent** (closure gate): `agents/econ-companion-visual-review.md`.
  Already used to produce the §1.1.1 voorkennis review that triggered
  the scope expansion. The skill's "Review before delivery" checklist
  is identical in shape to the agent's pass sequence so they cannot
  drift.

Canonical procedure decision (recorded 2026-05-09):

The canonical procedure for B02 is **4-step**, not the 3-step verbal
expansion that the current `_paragraph-plan.md` declares. The 4 steps:

1. Benoem alle beschikbare alternatieven voor het schaarse middel.
2. Bereken voor elk alternatief de opbrengst of verwachte opbrengst.
3. Rangschik de alternatieven; het hoogste niet-gekozen alternatief
   is de alternatieve kosten.
4. Vergelijk de opbrengst van de gekozen optie met de alternatieve
   kosten om de nettowaarde te beoordelen.

This decision propagates beyond vaardigheden: the `_paragraph-plan.md`
Concept 3 description, the `1.1.1_fig_3` flowchart visual, the
samenvatting cell 5, the presentatie slide 5, the stappenplan game,
the begeleide-inoefening scaffold, and the opgaven references all
need updating to the 4-step form. L1.5V owns the registry change and
the vaardigheden-side propagation; the other surfaces regenerate
mechanically once the registry is right.

Required changes — grouped by bucket. Bucket A (shared platform fixes)
ships first because both voorkennis and vaardigheden surfaces depend
on it; Bucket B (canonical procedure) is a hard prerequisite for all
B02-using surfaces; Buckets C and D are surface-specific.

#### Bucket A — Shared platform fixes (ship FIRST)

These are upstream defects from the §1.1.1 voorkennis review that also
affect the vaardigheden surface or any future paragraph's companions.
Fixing them once unblocks both surfaces and reduces L1.4 risk.

**A1. Strip production label `COMPANION VISUAL` from shared visual
frame.**
- Source: `build-scripts/lib/lib-visual-surfaces.js:131` emits the
  label in the shared visual frame for non-slide variants.
- Fix: remove or guard the label so student-facing doc / web_light /
  web_dark / summary surfaces never carry it. (Slide internal use, if
  any, may stay during build, but no rendered student surface should
  show it.)
- Regenerate: rerun `b1-111-visual-variants.js`, then DOCX/HTML/PPTX
  for §1.1.1 so the label disappears from every existing variant.
- Acceptance: no asset under `_assets/` for §1.1.1 contains the text
  `COMPANION VISUAL`; review agent's hard-fail on production labels
  cannot trigger.

**A2. `convert_voorkennis.py` renders normal-section list items.**
- Source: `build-scripts/lib/convert_voorkennis.py:548-588` only
  renders paragraphs / formulas / assets / callouts / summaries; there
  is no branch for normal-section `list_item`. As a result the HTML
  drops worked-example steps (`b1-111-voorkennis.js:430-434`) and
  bar-chart reading bullets (`:456-459`) that exist in the DOCX.
- Fix: teach the converter to emit `<ul>/<li>` (or `<ol>/<li>`
  where source signals ordered) for normal-section list items, with
  an associated CSS hook so `voorkennis.css` styles them.
- Acceptance: regenerated voorkennis.html contains the worked-example
  steps and the x-axis / y-axis / scale bullets that exist in the
  DOCX; review agent's source-output-parity hard-fail cannot trigger.

**A3. Voorkennis checklist emits next-step routing.**
- Source: `convert_voorkennis.py:602-617` generates the checklist
  HTML without a route block, and `b1-111-voorkennis.js` does not
  author one.
- Fix: add a generated next-action block after the checklist —
  "alles afgevinkt → ga verder naar Uitleg vaardigheden / Presentatie";
  "nog niet → herhaal sectie X / doe Instapquiz". Use the route table
  in `skills/econ-companion-artifacts.md` as the canonical mapping.
- Acceptance: regenerated voorkennis.html ends with a visible,
  keyboard-accessible next-action block; review agent's affordance
  hard-fail cannot trigger.

**A4. Meaningful alt-text infrastructure for visuals.**
- Source: HTML emits `alt="1.1.1_ex_1"` (filename-like) and DOCX
  emits `descr="asset:1.1.1_ex_1"` (asset-id-like).
- Fix: introduce an alt-text map keyed by concept-base in the
  paragraph plan (`_paragraph-plan.md` visual-variants section, or a
  dedicated alt-text registry), thread it through `b1-111-voorkennis.js`,
  `b1-111-vaardigheden.js`, the other §1.1.1 builders, and the matching
  converters so both DOCX `docPr` and HTML `alt` receive a human-
  readable description (e.g. *"Staafdiagram met opbrengst per gewas:
  tarwe €500 per hectare, maïs €350, zonnebloemen €300."*). Builders
  must fall back to a clear placeholder if alt text is missing for a
  concept-base, so omissions surface in review.
- Acceptance: no rendered `alt` or `descr` is filename-like or
  asset-id-like for any visual on the two §1.1.1 explainer surfaces.

**A5. Fix duplicate `Heading1` style ID so DOCX artifact-tool render
works.**
- Source: `b1-111-voorkennis.js:350` defines a custom style id
  `Heading1` colliding with the built-in. `render_docx.py --renderer
  artifact-tool` errors with `Argument_AddingDuplicateWithKey,
  Heading1`.
- Fix: rename the custom style or align with the built-in Word style;
  rerun artifact-tool to confirm page PNG render. If the same pattern
  exists for `b1-111-vaardigheden.js`, fix in parallel.
- Acceptance: `render_docx.py --renderer artifact-tool` succeeds on
  both regenerated DOCX files and produces page PNGs.

#### Bucket B — Canonical procedure 3 → 4 step propagation

Hard prerequisite for every Bucket C item and for any other §1.1.1
surface that displays B02. This is unchanged from the previous L1.5V
plan; reproduced here so the sprint stays self-contained.

**B1. Registry / source-of-truth update.**
- `4veco-lessen/Boek 1 .../1.1.1 .../_paragraph-plan.md` Concept 3
  row: rewrite the procedure description from the 3-step verbal form
  to the 4-step canonical form. Update the visual-anchor row for
  `1.1.1_fig_3` to reference the 4-step flowchart.

**B2. Visual generator.**
- `build-scripts/content/book-1/b1-111-visual-variants.js`: replace
  the 3-step `fig_3` flowchart with a 4-step variant (slide / doc /
  summary / web_light / web_dark surfaces all regenerate from the
  same source). Step terminology must match the registry verbatim.
  Surface-adapted variants required.

**B3. Content surfaces that reference B02's procedure.**
- `b1-111-vaardigheden.js` skill 2 procedure block — 4 steps.
- `b1-111-samenvatting.js` cell 5 ("Economisch denken — 3 stappen") —
  rename header, content, and visual reference to match the 4 steps.
- `b1-111-presentatie.js` slide 5 (Concept: Economisch denken) — same.
- `b1-111-inoefening.js` BI scaffold — propagate the 4-step form.
- Opgaven (`b1-111-opgaven.js` and basis / midden / verrijking question
  docx generators) — every "3-stappen procedure" / "Welke
  alternatieven? → opbrengsten? → wat geef je op?" reference becomes
  the 4-step form.
- Game data: `source-data/book-1/reasoning/1.1.1.csv` already uses
  "alternatieve kosten" canonical vocabulary; re-check no row still
  models the 3-step procedure as canonical. Stappenplan game data, if
  any, mirrors.

**B4. Regenerate-and-verify.**
- Per-paragraph builders (visual-variants, vaardigheden, samenvatting,
  presentatie, inoefening, opgaven).
- `node scripts/deploy.js` — all 5 docx-to-web converters re-emit
  HTML with the 4-step procedure present.
- `npx jest`, `npm run check:book`, `node scripts/validate-paragraph.js
  --mode complete` — all green.
- Manual diff: every rendered surface (samenvatting.html,
  vaardigheden.html, presentatie.pptx slide 5, BI HTML, basis / midden
  / verrijking opgaven) shows step 4 ("Vergelijk opbrengst met
  alternatieve kosten om de nettowaarde te beoordelen") and none
  shows the legacy 3-step header or footer.
- The fig_3 visual on every surface (slide / doc / summary / web_light
  / web_dark) shows 4 steps with the canonical wording.

Do NOT silently bridge two competing procedures. Do NOT regenerate
piecewise: if any surface lags behind, the registry is in an
inconsistent state and the next deploy could re-introduce the 3-step
form.

#### Bucket C — Vaardigheden-specific (after Buckets A + B)

**C1. Visual-text synchronization.** Lisa with €20 / bioscoop €12 /
boek €15 — the visual must use the same numbers as the adjacent text,
or the text must explicitly explain a broader-variant visual.

**C2. Worked-example text-completeness.** Add the tarwe/maïs
arithmetic as an explicit table in the verbal channel (not only in
the visual): opbrengst tarwe (10 × €500 = €5.000), opbrengst maïs
(10 × €350 = €3.500), beste niet-gekozen alternatief (maïs = €3.500),
alternatieve kosten (€3.500), nettowaarde (€5.000 − €3.500 = €1.500).

**C3. Schaarste checks visible as structured HTML.** The "Schaarste
herkennen" section must render the three checks as `<ol><li>` (or a
styled step block), not as loose text inside a callout.

**C4. Import Team B scaffold under B01/B02.** Keep two canonical
sections; nest as subblocks: keuzekaart pre-organizer under B02 step 1;
"prijs en kosten uit elkaar houden" misconception/pitfall block under
B02; explicit tarwe/maïs calculation table as the worked example;
granular checklist + route advice as the final block. Do NOT expand
into 5+ parallel skill sections.

**C5. "Wat nu?" routing block.** Final checklist routes the student
to the next appropriate artifact based on what they couldn't do yet
(Voorkennis / Stappenplan / Begeleide inoefening / Basisopgaven /
Middenopgaven / Verrijking). Use the route table in
`skills/econ-companion-artifacts.md`.

**C6. Visual quality.** Beyond A1 (production label), apply the
spelling/contrast/variant checks: `maïs` not `Mais`, `alternatieve
kosten` not English/informal, readable contrast in light/dark,
surface-adapted web visuals with light/dark variants (no direct
base-SVG embedding), arrows visibly meaningful.

#### Bucket D — Voorkennis-specific (after Buckets A)

**D1. Convert the schaarste/budget illustration to a meaningful
caption + alt text per A4.** Aligns the chart inspection prompts with
the visible chart values (Tarwe €500, Mais €350, Zonnebloemen €300)
and adds a one-line caption that mirrors the alt text.

**D2. Confirm worked-example steps survive regeneration.** Once A2 is
in, re-render and verify the three worked-example steps and the
x/y-axis/scale bullets are present. This is a parity check, not a new
authoring step.

**D3. Confirm checklist routing block is wired into the rendered
page** per A3. Spot-check link targets resolve under GitHub Pages.

#### Bucket E — Part A quality-control integration (was deferred, now in scope)

The voorkennis review's quality-log explicitly flagged that
`X.Y.Z-quality-ref.yaml` records Part A asset state only, and the
existing `validate-paragraph.js` passes despite Part B/companion hard
fails. The team direction (2026-05-09) is to **fold this into L1.5V**
rather than defer, because L1.5V is also the moment Part B is being
formalised by the new skill + review agent — the right time to ensure
Part A and Part B both have first-class records.

**E1. Extend the §1.1.1 quality records.**
- Audit the current `1.1.1-quality-ref.yaml`. Confirm exact scope of
  what it records (Part A asset state per the review).
- Decide schema shape with the F-planning sub-agent (one record file
  with explicit Part A and Part B sections, two record files, or a
  third companion-specific record file). Default: extend the existing
  YAML with a `companion:` section that mirrors the Part A fields.
- Wire `agents/econ-companion-visual-review.md` to write/update the
  Part B section of the chosen record on every run, in addition to its
  human-readable `1.1.1-companion-visual-review.md` report.

**E2. Decide whether `validate-paragraph.js` should fail on
companion-review hard fails.**
- Current behavior: validator is independent of the visual review;
  validator-pass does not imply review-pass.
- Options to evaluate in the F-plan: (a) keep them independent and
  document that closure requires both green; (b) have validator read
  the companion-review record file and refuse close if its verdict is
  FAIL; (c) keep independent but have a wrapper script (`scripts/
  qc-paragraph.js` or similar) that runs both and aggregates.
- This is a Bucket-F-shaped decision and is mostly handled there;
  E2 records the dependency and lists §1.1.1 as the proving paragraph.

**E3. Re-record §1.1.1 closure under the chosen schema.**
- Once E1 + the relevant Bucket F decisions are made, populate the
  Part A record (carry-forward from existing) and the Part B record
  (from the post-Bucket-A-D regen + final review-agent verdict).
  §1.1.1 then serves as the canonical example for paragraph 2 (L1.4)
  to follow.

#### Bucket F — Part A / Part B quality-cycle separation (pilot lock-in before L1.4)

**Why this is in L1.5V.** §1.1.1 is the pilot paragraph: every skill,
test, agent, and quality record we touch here becomes the template
that paragraph 2 (L1.4 = §1.1.2) builds against. The current build
documentation, validator, and quality records mix Part A (textbook
markdown + assets) and Part B (companion HTML/DOCX/PPTX/games + index)
together, which is confusing now that Part B has its own authoring
spec (`skills/econ-companion-artifacts.md`) and review agent
(`agents/econ-companion-visual-review.md`). L1.4 should not start
under that ambiguity. **L1.4 is gated on Bucket F closing.**

**F-plan (sub-agent).** Audit + propose-design pass. The F-planning
sub-agent surveys the current state and produces a written design
proposal for user review before any F-execute work begins.

Audit inputs:
- `BUILD-PARAGRAPH.md` — read in full; tag every paragraph as Part A,
  Part B, or A+B; identify mixed-scope sections (Phase 6 / 6a, the
  A-verify / B-verify checklists, the validate-paragraph mode flags).
- `BUILD-CHAPTER.md` — same audit at chapter scope.
- `scripts/validate-paragraph.js` — list current modes (`complete`,
  `part-a`, `part-b`?) and their actual gate coverage; check if mode
  semantics match the BUILD-PARAGRAPH documented split.
- Skills: `econ-textbook-paragraph` (Part A producer),
  `econ-companion-artifacts` (Part B umbrella), `econ-explainer-docs`,
  `econ-exercise-builder`, `econ-pptx-templates`, `econ-word-templates`,
  `econ-paragraph-review`, `econ-quality-control`, `econ-pdf-builder`,
  `qc-references`, `manage-references`. For each: does it own Part A,
  Part B, or both? Where does ownership leak across the line?
- Agents: `agents/econ-companion-visual-review.md` is Part B only.
  Confirm there is no equivalent Part A reviewer agent or that the
  Part A path is covered by a skill instead.
- Quality records in the lessen tree: `X.Y.Z-quality-ref.yaml`,
  `X.Y.Z-review.md`, `X.Y.Z-companion-visual-review.md`. Map each to
  its scope and consumer.
- File layout under a paragraph folder. Are Part A files (markdown,
  PDF, `_assets/`) and Part B files (`*.html`, `*.docx`, `*.pptx`,
  `index.html`, game shells) cleanly distinguishable by name and
  prefix? Decide if the layout itself benefits from a sub-folder
  split or if naming is sufficient. **Default: do not move files;
  prefer in-place scope clarification, because the lessen tree is
  generated output and physical reorganization would propagate to the
  build pipeline, the GitHub Pages URLs, and student bookmarks.**

Audit outputs (the F-plan delivers these for user review BEFORE any
F-execute work begins):
- Mixed-scope section list with proposed split.
- Proposed final shape of `BUILD-PARAGRAPH.md`: either (a) one file
  with three top-level sections (Common pre-conditions, Part A, Part B)
  or (b) split into `BUILD-PARAGRAPH-A.md` + `BUILD-PARAGRAPH-B.md`
  with a small `BUILD-PARAGRAPH.md` index. Recommend one with
  rationale.
- Proposed validator behavior: confirm `--mode part-a`, `--mode part-b`,
  `--mode complete` are present; document each mode's coverage; close
  any gap where `complete` should aggregate part-a and part-b.
- Proposed quality-record schema (resolves Bucket E1).
- Proposed skill ownership table: skill → which Part(s) it owns →
  which gate runs against its output.
- Proposed test taxonomy: which jest test suites belong to Part A,
  Part B, or shared infrastructure; whether suite naming/folder
  reflects that.
- A migration plan that touches §1.1.1 only (paragraph 2 in L1.4
  inherits the cleaned pipeline; older paragraphs are out of scope).

**F-execute (main agent + per-item sub-agents as needed).** Implement
the F-plan after user approval. One commit per coherent change. Never
move generated lesson output (per Default above) unless F-plan
explicitly requests it and the user approves.

Likely items (final list comes from F-plan):
- F1. Restructure `BUILD-PARAGRAPH.md` per the chosen shape.
- F2. Adjust `validate-paragraph.js` if a mode is missing or wrongly
  scoped; document each mode's coverage in BUILD-PARAGRAPH.
- F3. Implement the chosen quality-record schema; migrate §1.1.1's
  records.
- F4. Update skill files where Part A/Part B ownership is unclear
  (mostly: front-matter description, "When to use," "How this skill
  connects to the rest of the platform" sections).
- F5. Adjust agents/README.md and the `econ-companion-artifacts`
  skill cross-references if the F-plan changes them.
- F6. Update CLAUDE.md (project-level) and AGENTS.md "Quality control"
  sections to reflect the cleaner pipeline.

**F-verify (sub-agent).**
- Re-run end-to-end on §1.1.1 with the cleaned pipeline. Each gate
  runs separately for Part A and Part B; both must pass; the
  aggregate must pass.
- Confirm the §1.1.1 voorkennis review file (post-Bucket-A-D regen)
  is recorded in the new quality record schema.
- Confirm the gates would catch each of the original voorkennis
  review hard fails if reintroduced (regression test, conceptually:
  insert each defect, run validator + review agent, expect FAIL,
  revert).

**Closure of Bucket F is the gate to L1.4.** Roadmap row for L1.4
updated accordingly.

#### Cross-bucket workflow per item

Every item in every bucket follows the same loop, mandated by
`skills/econ-companion-artifacts.md` and gated by
`agents/econ-companion-visual-review.md`:

1. **Read** `skills/econ-companion-artifacts.md`, the matching builder
   skill (e.g. `econ-explainer-docs`), the paragraph plan, the
   canonical unit registry, the existing artifact, and the affected
   builder/converter/asset.
2. **Author / regenerate.** Edit source layer only. Never hand-edit
   `4veco-lessen/`.
3. **Verify rendered output** in browser (HTML) or by inspecting the
   DOCX/PNG export. Confirm source-output parity (bullets / tables /
   calculations / steps / labels / alt text / route block survived).
4. **Run gates.** `npx jest`, `node scripts/deploy.js`, `npm run
   check:book`, `node scripts/validate-paragraph.js --mode complete`.
5. **Run the review agent** on the regenerated surface. Hard fails
   from the agent are the same as the skill's "Do not return PASS if"
   list. Iterate until verdict is PASS or PASS WITH FLAGS for both
   surfaces.

Out of scope (deferred or not L1.5V's territory):

- The "Economisch oordeel geven" Team B section. Not a named
  answer-writing scaffold in the canonical registry; do not import as
  a fifth procedure.
- Re-rendering of all paragraphs. L1.5V scopes to §1.1.1 only.
- L1.5D D2 (PPTX-as-web). Resumes after L1.5V closes.
- File-layout reorganization of the lessen tree (Part A vs Part B
  sub-folders, URL changes). Default in F-plan is to keep the layout
  and clarify scope by naming + documentation only. Physical moves
  are a separate decision the user owns; do not let F drift into one.
- Migration of older paragraphs to the cleaned pipeline (Bucket F is
  scoped to §1.1.1 as the pilot). L1.4 uses the cleaned pipeline by
  default for paragraph 2; older paragraphs catch up opportunistically
  in later sprints.

Pre-flight (must hold before any code change):

- ✅ **Platform PR #3 merged** to platform `main` (2026-05-09). The
  converter ERROR-vs-OK contract fix (`eda176d` upstream / `5dcaf2a`
  on main) is in. The docx-as-web infrastructure L1.5V regenerations
  depend on is therefore present.
- Baseline gates green on platform `main` head: `npx jest`,
  `node scripts/deploy.js "../4veco-lessen/Boek 1 ..."`,
  `npm run check:book`, `node scripts/validate-paragraph.js --mode
  complete "..."`. Re-run before branching per
  `feedback_baseline-gate-check.md`.
- `feedback_conditional-authorization-expires.md` applies: re-verify
  platform team activity state at branch creation; do not assume idle
  from prior session.
- Stale worktrees pruned: `4veco-platform-d1d2` (was `webdocs/1.5d`,
  now merged) and `4veco-platform-layout` (was `layout/1.1.1-round-2-redo`,
  L1.5A merged) can be removed before creating the new worktree.

Sub-agent-driven workflow (per `feedback_sprint-task-workflow.md`):

1. **Whole-sprint planning sub-agent.** Survey: current source for both
   `b1-111-voorkennis.js` and `b1-111-vaardigheden.js`; matching
   converters; `_paragraph-plan.md` procedure + visual-variants
   blocks; shared `lib-visual-surfaces.js`; canonical units B01 + B02;
   Team B's `uitleg vaardigheden team b.html`; the §1.1.1 voorkennis
   review file. Produce a per-item execution plan with file paths,
   before/after sketches, gates, browser-smoke targets, structured by
   the four buckets above. Confirm the dependency order
   (Bucket A1+A4 → A2+A3 → A5 → B → C → D) and flag any item that
   should subdivide.
2. **Per-item planning sub-agent** for non-obvious items: A2 (list-
   rendering converter design), A4 (alt-text registry shape), B2
   (4-step `fig_3` visual replacement), C4 (Team B scaffold imports).
3. Main agent executes, one commit per item (or per coherent
   sub-bucket where items co-edit the same file), on a fresh branch
   `content/1.1.1-companion-quality` off platform main, in worktree
   `4veco-platform-companion`.
4. **Verification sub-agent** runs gates + Pages browser-smoke;
   compares rendered HTML against the acceptance criteria; **runs
   `agents/econ-companion-visual-review.md` on both surfaces** and
   attaches its verdict + report to the verification output.
5. PR to platform main; lessen regen + commit + push; live Pages
   browser-smoke after deploy.

Acceptance criteria (per `skills/econ-companion-artifacts.md` review
gate):

For both `uitleg voorkennis.html` and `uitleg vaardigheden.html`:

- No 3-step/4-step procedure mismatch on any rendered surface.
- Every procedure visual matches its canonical procedure in step
  count, order, and terminology.
- Visuals match adjacent text in numbers, units, and terminology (or
  text explicitly explains a broader-variant visual).
- Worked examples are text-complete (calculations visible in prose,
  not only in the visual).
- Where the artifact contains a list/checks/checklist, it renders as
  structured semantic HTML (`<ul>` / `<ol>` / `<li>`).
- No production / debug labels (`COMPANION VISUAL`, asset filenames,
  internal IDs) on any rendered student-facing visual.
- Alt text and DOCX `descr` are meaningful, not filename-like.
- Surface-adapted light / dark web visuals work.
- Final block routes the student to the right next artifact (per the
  skill's route table).
- `agents/econ-companion-visual-review.md` returns **PASS** or **PASS
  WITH FLAGS** (no hard fails) on both surfaces.
- `render_docx.py --renderer artifact-tool` succeeds on both
  regenerated DOCX files.

Proof required (per `skills/econ-companion-artifacts.md` "Required
delivery" + the review agent's closure proofs):

- Regenerated `uitleg voorkennis.html`, `uitleg voorkennis.docx`,
  `uitleg vaardigheden.html` (and `.docx` if the vaardigheden DOCX
  was edited as part of the sprint).
- Browser-verification screenshots / sub-agent fetch report for both
  surfaces, including light + dark variant smoke.
- Evidence canonical B02 procedure + `fig_3` visual now match across
  every surface that displays B02.
- Evidence the alt-text registry / map yields meaningful descriptions
  in both DOCX `descr` and HTML `alt`.
- Evidence the voorkennis checklist now ends with a routing block;
  spot-check link targets resolve under GitHub Pages.
- Source-output parity report: bullets, tables, calculations,
  checklist content, alt text, route block survive generation.
- `agents/econ-companion-visual-review.md` output for both surfaces
  with verdict PASS or PASS WITH FLAGS, saved as
  `1.1.1-companion-visual-review.md` (overwriting or versioning the
  existing voorkennis review file as the new baseline).
- `render_docx.py --renderer artifact-tool` page PNGs for both
  regenerated DOCX files, attached as artifact-tool render proof.

### Sprint L1.4: First Pipeline Regression Paragraph

Completed: no.

Status: paused 2026-04-30, was active since 2026-04-25. Resumes after L1.5D.

Target paragraph: `1.1.2 Percentages en indexcijfers` (Part A is complete; Part
B build will run against the L1.3A-C + L1.5A + L1.5D platform state).

Purpose:

Prove the platform's pipeline still works on fresh content — not just on
re-regenerations of `1.1.1`. After this restructure, L1.4 carries three
regressions at once:

1. **Layout regression.** Confirm the L1.3A-C layout direction + the L1.5A
   easy polish hold on fresh content.
2. **Games regression on the reworked unit-register.** The platform team
   completed RX.1 / RX.2 representation-and-mutation work and shipped
   `c21ee14 fix(skilltree): hide generator-blocked catalog units`. Building
   1.1.2 confirms the existing 5 games still deploy cleanly with the reworked
   micro-teaching-units before any new games are added in L1.5G.
3. **Web-docs regression.** Confirm the DOCX/PPTX-as-web pipeline from L1.5D
   produces correct output on a paragraph that wasn't its development target.

PV note: L1.4 may test formula/table/percentage PV templates only if PV.2/PV.3
are ready. Do not delay L1.4 waiting for the full PV track.

Work:

- Drive the full pipeline: converters (voorkennis / vaardigheden / begeleide
  inoefening), presentation builder, visual variants, paragraaf landing page,
  youtube-videos generator if in scope, plus the L1.5D DOCX/PPTX-as-web
  rendering paths.
- Pass `validate-paragraph.js --mode complete`, `check-links.js`, and
  `check:book`.
- Browser-smoke each generated page on desktop and mobile, light and dark.
- Treat every gap as a platform issue: file a fix against the relevant platform
  script. Do not hand-patch anything inside `4veco-lessen/`.
- If PV.2/PV.3 are available before the build, use `1.1.2` as a regression
  surface for one formula/table/percentage PV template or validator check.

Exit criteria:

- a second Book 1 paragraph has a complete Part B companion set that passes
  complete-mode validation
- every pipeline gap surfaced is fixed in the platform, not in generated output
- browser smoke confirms the L1.3A-C + L1.5A layout direction holds on new
  content
- the existing 5 games deploy cleanly under the reworked unit-register
- DOCX/PPTX rendered as web matches the L1.5D spec on `1.1.2`
- PV is not a blocker for L1.4; any PV check here is opportunistic and must
  come from platform/reference data, not a lesson-side hand model.

### Sprint L1.5B: Layout Round 2 — Generator Items

Completed: no.

Position: after L1.4. Originally the whole of L1.5; L1.5A was split off and
pulled forward.

Purpose:

Tighten the companion layout/front-end on the items that need fresh-paragraph
input or that touch generators. Use L1.4's findings as input plus the
deferred items from the rolled-back round-2 attempt and from L1.5A's planner.

Work:

- Consolidate P1 and P2 findings from the L1.3A-C human usability review.
- Act on anything L1.4 surfaced: accent-domain mismatches, empty-section
  states on Part-A-only paragraphs, sidebar defaults, mobile breakpoints,
  resource-card density, callout hierarchy, light/dark regressions on new
  content.
- Land the deferred round-2 item #3 (split "Valkuilen en misvattingen" into
  per-card pitfalls in `build-landing-page.js`) — generator-touching, so it
  needs L1.4's fresh-paragraph regression in the rear-view mirror.
- Land the deferred round-2 item #1 (per-section accents on chapter/book
  index cards). The L1.5A planning sub-agent reclassified this as
  generator-touching with the following evidence: `.section-card` does not
  exist in the platform; cards are emitted as `.chapter-card`
  (`build-scripts/platform/build-landing-page.js` ~line 499) and `.para-card`
  (~line 542); current accent is an inline `style="--ch-color: ${dc2.main}"`
  from a 5-color palette, not the editorial 3-token system; editorial accent
  CSS rules in `engines/voorkennis.css` require either `body[data-accent-domain]`
  or class hooks (`bg-economisch` / `border-...` / `badge-...` / `domain-...`)
  or a `data-domain` attribute, none of which the cards carry. Implementation
  requires editing the renderBookPage / renderChapterPage emission sites to
  add a `data-domain` attribute (or matching class hook) and adding matching
  CSS rules.
- Keep all changes in platform-owned CSS/JS, converters, templates, and
  build scripts. No one-off fixes in generated files.
- Rerun both `1.1.1` and the L1.4 paragraph end to end and confirm no
  regressions against the hard gates.

Exit criteria:

- layout/UI improvements land in platform sources and regenerate cleanly for
  both paragraphs
- no outstanding P1 items remain from the L1.3A-C usability review
- `validate-paragraph.js --mode complete` passes for both paragraphs

### Sprint L1.5G: Three-Aspect Game Coverage

Completed: no.

Position: after L1.5B.

Purpose:

Have one working prototype per learning aspect — reasoning, calculation, and
graphical — so the companion has a complete set of game types before scaling
content. Bring the user's graphical-game prototype into the platform as the
third-aspect representative. Refactor existing games to expose the adaptive-
input seam described in the "Architecture: adaptive-ready" section, so the
later adaptive layer can wire in without engine changes.

PV constraint: the graphical-game prototype may not hard-code its own semantic
model if equivalent PV visual-state, operation, or procedure-template records
exist in the platform/reference layer. Temporary local semantics are allowed
only when documented as temporary technical debt and shaped so PV-backed data
can replace them.

Aspect mapping:

- Reasoning: `newsdetective`, `reasoning` (existing, polish to working-prototype
  quality).
- Calculation: `quiz`, `skilltree`, `procedure` (existing, polish).
- Graphical: graphical-game prototype landing in this sprint (currently outside
  the platform; bring it in).

Work:

- Bring the graphical-game prototype into `4veco-platform/engines/`. Match the
  existing engine pattern (separate `<game>.js` and `<game>-ui.js` where
  applicable; CSS in a single file; HTML-shell builder under
  `build-scripts/platform/`; data file convention under `shared/<game>/`).
- If equivalent PV visual-state, operation, or procedure-template records
  exist, the graphical-game prototype consumes or validates against them
  instead of hard-coding a separate semantic model.
- Polish each of the six engines (5 existing + 1 new graphical) to
  working-prototype quality: keyboard navigation, mobile behaviour, light/dark
  parity, deterministic output for tests where possible.
- Adaptive-seam refactor: every game accepts an adaptive payload from a
  well-defined localStorage key on init; the payload is empty / default today
  and the game behaves as it does now; the seam is in place for the future
  advisor.
- Graphical-game data accepts a PV-aligned shape with `unit_id`,
  `procedure_template_id`, `visual_state_sequence`, and `student_actions` where
  equivalent PV records exist.
- Add tests for the adaptive seam: empty payload → existing behaviour; mock
  payload → game state reflects it.

Out of scope:

- Building the post-quiz advisor or evaluation logic.
- Defining the adaptive payload schema beyond a placeholder structure.
- Shipping any actual adaptive behaviour to students.

Exit criteria:

- one working prototype exists per aspect (reasoning, calculation, graphical),
  all integrated into the platform deploy.
- the graphical prototype is PV-aligned where PV records exist, or temporary
  semantic duplication is explicitly documented as technical debt.
- all six game engines accept an adaptive payload via the same localStorage
  seam (no payload = current behaviour).
- graphical-game semantics align with existing PV records, or any temporary
  divergence is explicitly documented with a migration path back to PV.
- `validate-paragraph.js --mode complete` continues to pass for both `1.1.1`
  and the L1.4 paragraph.
- browser smoke confirms each game's prototype is reachable and functional in
  light and dark, on desktop and mobile.

### Sprint L1.6: Second Pipeline Regression Paragraph

Completed: no.

Position: after L1.5G.

Purpose:

Confirm the L1.5B layout changes + L1.5G new graphical game + adaptive-seam
refactor did not break the pipeline by driving the full Part B workflow end to
end on a third Book 1 paragraph. Two independent regenerations against the
post-restructure platform state is the minimum signal that the pattern is safe
to scale.

Work:

- Pick a third Book 1 paragraph (team picks — likely `1.1.3 Grafieken en
  tabellen` or `1.1.4 Gemengde opgaven`, whichever has clean Part A and a
  defensible Part B scope).
- Drive the full pipeline including the new graphical game and the DOCX/PPTX-
  as-web rendering paths; same validator + check-links + check:book gates as
  L1.4.
- Browser-smoke the generated pages in light and dark on desktop and mobile,
  including each game's prototype and the web-rendered authored content.
- If PV.2/PV.3/PV.4 are ready, use or validate at least one procedure/visual
  sequence from the PV registry in the fresh paragraph. Acceptable proof is one
  procedure game mapped to formal steps, one visual-state sequence used in a
  companion visual, or one answer model validated against PV step order.
- Any breakage becomes a platform fix and a regeneration; no hand-patches.

Exit criteria:

- a third Book 1 paragraph has a complete Part B companion set that passes
  complete-mode validation
- zero hand-patches remain in `4veco-lessen/` for the new paragraph
- at least one procedure/visual sequence is generated from or validated
  against PV data if the PV registry has passed the required gate
- browser smoke confirms Layout Round 2 + new graphical game + adaptive seam
  + web-rendered authored content hold on new content

### Sprint L1.7: Post-Layout Scaling Decision

Completed: no.

Purpose:

Decide whether companion production may expand broadly after two independent
paragraph builds against two successive layout states.

Work:

- Review the regenerated `1.1.1` plus the L1.4 and L1.6 paragraphs after
  layout/UI and visual-integration improvements.
- Decide whether to expand to 3-5 more representative paragraphs.
- Keep all builder scripts saved under the platform `build-scripts/content/book-1/`
  workflow.
- Separate remaining content problems from platform usability problems.
- Include PV readiness in the scaling decision: procedure consistency, visual
  semantic anchors, surface variants, game mapping, answer-model alignment,
  and generator-block controls.

Exit criteria:

- improved companion pages pass validation and browser checks
- the platform team confirms the layout and visual-variant direction is
  reproducible across three paragraphs under two layout states
- PV-backed or PV-validated pilot sequences do not require manual duplication
  across lesson surfaces before scaling
- the lesson team has a go/no-go decision for broader companion production

### Sprint L1.5P: Boek 1 Print-Edition Cut for Publisher

Completed: no.

Position: in parallel with the companion-quality stream (L1.5x). Hard
deadline: publisher hand-off in a few weeks (as of 2026-05-11; owner to
fill in exact date).

Purpose:

Trim Boek 1 to fit the publisher's print-edition page budget before the
hand-off date. The current Boek 1 build is too long for print. The
print edition does not include companion artifacts, games, or
interactive material — those stay on the website.

Scope:

- Identify which chapter(s) and paragraph(s) put Boek 1 over the page
  budget. First candidate for cutting from print:
  `1.5 Hoofdstuk Toetsvoorbereiding` (proeftoets, toetsmatrijs,
  voorbereidingstaken) — moves to website-only. Other candidates to
  review: optional extension content, verrijkingsopgaven in print, and
  full answer keys (consider moving answer keys to website only).
- For each cut item, record where the content survives online (companion
  paragraph index, website-only PDF/HTML, or companion download).
- Update the book assembly (`Boek 1 ... – boek.md`, chapter pages, book
  index) so the printed flow reads cleanly without the cut material.
- Keep the cut material reachable from the website index so a student or
  teacher who wants test-preparation still has it.
- Re-run `check:book` and chapter/paragraph validators after every cut
  to confirm link/reference integrity.

Out of scope:

- Companion polish (continues in L1.5x).
- Pipeline-regression paragraphs (L1.4, L1.6).
- Changes to chapters that are not over the page budget.

Exit criteria:

- Boek 1 print PDF fits the publisher's page budget.
- Every cut piece is reachable from the website index.
- `check:book` and all paragraph validators still pass.
- The print/web split is recorded so the website-only artifacts stay in
  scope for the future Book 1 release polish (L2.1) and the
  adaptive-learning cycle without re-discovery.

### Sprint L2.1: Book 1 Release Polish

Completed: no.

Purpose:

Do a teacher-facing review pass on Book 1 while keeping the health gate green.

Work:

- clarity
- pacing
- graph readability
- answer model usability
- exam fit

Rules:

- Keep all five chapter validators passing.
- Keep all paragraph validators passing in Part A mode.
- Any repeated manual fix should become a checklist item or a platform improvement request.

### Sprint L2.2: Book 2 Part A Textbook Layer

Completed: no.

Purpose:

Build Book 2 Part A first, with hard gates.

Required gates:

- `_chapter-plan.md`
- paragraph markdown files
- SVG/PNG pairs
- PDFs
- review files
- quality refs
- chapter assembly
- chapter validation

Book 2 should prove that the Book 1 Part A workflow is repeatable, not just a one-off success.

## Lessen Team Deliverables

### Next 1 Week

- Keep Book 1 green.
- Continue companion pilot work with layout/front-end usability and proper visual integration as the main focus.
- Hand platform-owned UI integration work back to the platform team instead of patching generated files.
- Keep Book 2 Part A planning moving only under the normal chapter gates.

### Next 2-4 Weeks

- `1.1.1` exists as the reference companion paragraph with platform-integrated layout/UI and surface-adapted visual variants.
- A second Book 1 companion paragraph is built under L1.4 against the current platform state, surfacing any pipeline gap that a second regeneration reveals.
- Layout Round 2 (L1.5) acts on the combined findings from the L1.3A-C usability review and the L1.4 regression paragraph; changes land in platform-owned sources only.
- A third Book 1 companion paragraph is built under L1.6 to confirm the Round 2 layout survives a second independent regeneration before the scaling decision.
- Book 1 teacher-facing polish continues without breaking `check:book`.

### Months 1-3

- Book 1 becomes pilot-ready.
- Book 2 textbook layer becomes textbook-ready or close.
- Companion production decisions are based on validated, usable, regenerated companion materials with proper visual integration, not only file-count validation.

## What The Lessen Team Does Not Own

- Validator bugs and deploy/config plumbing.
- Platform-level generator refactors.
- Shared companion CSS/JS architecture.
- Converter/template changes needed to make layout improvements reproducible.
- Visual-builder, converter, and template changes needed to make image variants reproducible.
- Reference-report architecture cleanup.

Those should be escalated to the platform team instead of patched locally.

## Escalation Triggers

Bring issues back to the platform team immediately if:

- `check:book` fails because of validator/tooling behavior rather than content quality.
- A companion build is blocked by missing `deploy-config.json`, missing `shared/`, or missing generator/build-script infrastructure.
- The complete-mode validator expects artifacts that the documented toolchain cannot yet produce cleanly.
- A UI/layout improvement requires editing generated HTML directly instead of changing platform templates, converters, shared CSS/JS, or generators.
- An image/layout improvement requires pasting a one-off picture into generated output instead of changing platform visual builders, converters, templates, shared CSS/JS, or generators.
- The companion pages pass file validation but fail browser rendering, navigation, mobile usability, or basic readability checks.
- Light/dark mode makes a graphic unreadable, mismatched, or visibly pasted from the wrong theme.
