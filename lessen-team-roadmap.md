# Lessen Team Roadmap

## Sprint Ledger

| Sprint | Name | Completed | Current State |
|--------|------|-----------|---------------|
| L0.5 | Green Gate Handoff | yes | Book 1 Part A and the platform/book health routine are green. |
| L1.1 | First Companion Technical Pilot | yes | `1.1.1` passes the current complete technical gate. |
| L1.2 | Second Companion Technical Probe | yes | `1.1.2` proved the technical pattern can repeat; probe materials were removed for didactic rebuild. |
| L1.3A | Basic HTML Layout And Front-End Usability | no | Pilot run completed for `1.1.1` `uitleg voorkennis`, `uitleg vaardigheden`, and `begeleide inoefening`; needs human usability sign-off. |
| L1.3B | Companion SVGs And Light/Dark Visual Variants | no | Proper SVG/variant workflow is running for `1.1.1`; game/interactive visual slots still need a decision. |
| L1.3C | PowerPoint Presentation Improvement | no | `1.1.1` PPTX regenerated with adapted slide visuals and LibreOffice roundtrip; needs presentation-quality review. |
| L1.4 | Post-Layout Scaling Decision | no | Decide whether to expand after L1.3A-C are platform-integrated, regenerated, and reviewed. |
| L2.1 | Book 1 Release Polish | no | Teacher-facing polish continues under the Book 1 health gate. |
| L2.2 | Book 2 Part A Textbook Layer | no | Start Book 2 Part A only under the chapter/paragraph hard gates. |

## Roadmap Metadata

Generated: 2026-04-23
Updated: 2026-04-24 after companion pilot review, layout/UI reprioritization, visual-variant direction, and L1.3A-C split
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

Completed: no.

Latest run: 2026-04-24.

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

Completed: no.

Latest run: 2026-04-24.

Purpose:

Replace raw copy-pasted textbook imagery with proper companion SVGs and
surface-specific variants, including explicit light/dark web visuals where
needed.

Current evidence:

- The visual-variant builder regenerated slide, docx, summary, web-light, and web-dark variants for `1.1.1`.
- `1.1.1` `uitleg voorkennis.html`, `uitleg vaardigheden.html`, and `begeleide inoefening.html` use light/dark image swapping where themed visuals exist.
- Browser smoke confirmed the correct light/dark image sources on desktop and mobile.

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

Completed: no.

Latest run: 2026-04-24.

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

### Sprint L1.4: Post-Layout Scaling Decision

Completed: no.

Purpose:

Decide whether companion production may expand after the layout/front-end sprint.

Work:

- Review the regenerated `1.1.1` and didactically rebuilt `1.1.2` companion pages after layout/UI and visual-integration improvements.
- Decide whether to expand to 3-5 representative paragraphs.
- Keep all builder scripts saved under the platform `build-scripts/content/book-1/` workflow.
- Separate remaining content problems from platform usability problems.

Exit criteria:

- improved companion pages pass validation and browser checks
- the platform team confirms the layout and visual-variant direction is reproducible
- the lesson team has a go/no-go decision for broader companion production

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

- One improved companion paragraph exists with platform-integrated layout/UI and surface-adapted visual variants.
- The second technical companion probe remains documented as evidence, but its materials have been cleared and no broad scaling starts until layout/UI is improved.
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
