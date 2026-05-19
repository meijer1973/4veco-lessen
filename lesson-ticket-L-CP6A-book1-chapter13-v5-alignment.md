# Lesson Team Ticket L-CP6A: Book 1 Chapter 1.3 v5 Alignment Remediation

Status: closed pass with flags

Owner: lesson team

Created: 2026-05-19

Source handoff: platform `CP.6a Book 1 Chapter 1.3 Lesson-Side Alignment`

Closure: 2026-05-19

Closure evidence:

- Sprint plan: `archive/sprints/L-CP6A/L-CP6A-sprint-plan.md`
- Technical QA: `archive/sprints/L-CP6A/L-CP6A-technical-qa-report.md`
- Closure log: `archive/sprints/L-CP6A/L-CP6A-closure-log.md`
- Handoff: `archive/sprints/L-CP6A/L-CP6A-handoff-to-references.md`

The lesson-side mismatch is fixed with carried conditions. CP-6 and Year 1 are
not closed by this ticket.

## Problem

The `1.3.2` / `1.3.3` source/lesson mismatch is still open.

Active v5 defines Book 1 Chapter 1.3 as:

| Paragraph | Active v5 title |
|---|---|
| 1.3.1 | Aanbod |
| 1.3.2 | Marktevenwicht |
| 1.3.3 | Verschuivingen en nieuw evenwicht |
| 1.3.4 | Gemengde opgaven: aanbod en marktevenwicht |

Current lesson-side output is mixed:

| Surface | Current 1.3.2 | Current 1.3.3 | State |
|---|---|---|---|
| Chapter folders and chapter plan | Kostenstructuren | Opbrengsten | stale for active v5 Book 1 |
| Chapter markdown | Kostenstructuren | Opbrengsten | stale for active v5 Book 1 |
| Aggregate Book 1 markdown / HTML | Marktevenwicht | Verschuivingen en nieuw evenwicht | already v5-titled, but not enough to prove validated remediation |

The aggregate Book 1 headings alone do not close the mismatch. The chapter folders, chapter plan, chapter-level markdown, navigation, generated book surfaces, review files, and quality refs must be aligned and validated through an authorized lesson-side remediation/regeneration sprint.

## Evidence To Read First

Platform evidence:

- `4veco-platform/reports/sprints/CP.6a-result.md`
- `4veco-platform/reports/reference-planning/CP.6a-lesson-side-alignment.md`
- `4veco-platform/references/data/sprints/CP.6a-lesson-side-alignment.json`
- `4veco-platform/reports/review-gates/GATE-CP6-year-1-paragraph-coverage/human-interview.md`
- `4veco-platform/references/reference-team-roadmap.md`

Lesson-side evidence:

- `lessen-team-roadmap.md`
- `course_blueprint_v5.md`
- `Boek 1 - Grondslagen, vraag en aanbod/1.3 Hoofdstuk Aanbod en kosten/_chapter-plan.md`
- `Boek 1 - Grondslagen, vraag en aanbod/1.3 Hoofdstuk Aanbod en kosten/1.3.2 Kostenstructuren/`
- `Boek 1 - Grondslagen, vraag en aanbod/1.3 Hoofdstuk Aanbod en kosten/1.3.3 Opbrengsten/`
- `Boek 1 - Grondslagen, vraag en aanbod/1.4 Hoofdstuk Marktevenwicht en marginale analyse/1.4.1 Marktevenwicht/`
- `Boek 1 - Grondslagen, vraag en aanbod/1.4 Hoofdstuk Marktevenwicht en marginale analyse/1.4.2 Verschuivingen/`

## Required Outcome

Run a later authorized lesson-side remediation/regeneration sprint that makes Book 1 Chapter 1.3 consistently match active v5:

1. `1.3.1 Aanbod`
2. `1.3.2 Marktevenwicht`
3. `1.3.3 Verschuivingen en nieuw evenwicht`
4. `1.3.4 Gemengde opgaven: aanbod en marktevenwicht`

The existing `1.4.1 Marktevenwicht` and `1.4.2 Verschuivingen` material are likely source material for the v5 `1.3.2` and `1.3.3` positions, but they must not be counted as done until regenerated or moved through the approved workflow and reviewed.

Carry forward and fix the known `PASS WITH FLAGS` items:

| Existing material | Maps to | Known flags to resolve or explicitly carry |
|---|---|---|
| 1.4.1 Marktevenwicht | v5 1.3.2 | limited start hints; ambiguous subsidy question; duplicated exercises |
| 1.4.2 Verschuivingen | v5 1.3.3 | incorrect forward reference; exercise 8e ambiguity problem; duplicated exercises |

Current `1.3.2 Kostenstructuren` and `1.3.3 Opbrengsten` must not be counted as Book 1 Chapter 1.3 coverage under active v5. Preserve or regenerate them for their active-v5 Book 2 destinations:

| Current Book 1 material | Active v5 destination |
|---|---|
| 1.3.2 Kostenstructuren | 2.1.1 Kostenstructuren |
| 1.3.3 Opbrengsten | 2.1.2 Opbrengsten, winst en break-even |

## In Scope

- Write an operational sprint plan before changing lesson output.
- Use the platform build workflow; do not hand-patch generated lesson output.
- Align Chapter 1.3 folder structure, chapter plan, chapter markdown, paragraph files, generated HTML/PDF where applicable, book aggregate files, navigation/landing surfaces, review records, and quality refs.
- Fix or explicitly carry the `PASS WITH FLAGS` items from current `1.4.1` and `1.4.2`.
- Record the survival route for displaced costs/revenue material.
- Produce a lesson-team closure log with exact changed/generated files, validation commands, and the lesson commit SHA.
- Hand proof back to the references team so CP-6 can re-evaluate the source/lesson mismatch.

## Out Of Scope

- CP-6 closure.
- Year-1 closure.
- Target-exercise promotion to `reviewed_final`.
- Placeholder finalization for `1.1.4`, `1.2.4`, or `1.3.4`.
- Unit minting or protected reference mutation.
- Full Book 2 production beyond recording the survival route for costs/revenue.
- Diagnostics, adaptive routing, mastery, sequencing, student-facing AI, summative use, PV projection, or PV machine promotion.

## Acceptance Criteria

- Chapter 1.3 no longer presents `1.3.2 Kostenstructuren` or `1.3.3 Opbrengsten` as Book 1 active-v5 paragraph slots.
- Chapter 1.3 consistently presents `1.3.2 Marktevenwicht` and `1.3.3 Verschuivingen en nieuw evenwicht` across folders, chapter plan, chapter markdown, book markdown/HTML/PDF, and navigation.
- `1.3.4 Gemengde opgaven` is scoped to supply, demand, equilibrium, and shifts; it does not cram costs/revenue theory back into Book 1.
- Review files and quality refs for the regenerated/moved paragraphs are current and do not hide carried flags.
- The lesson repo records the generated file list and validation results.
- The platform references team receives the lesson commit SHA and validation evidence before any later CP-6 closure proposal treats the mismatch as resolved.

## Minimum Validation Commands

Run from `4veco-platform` unless a future sprint plan names a stricter command set:

```bash
node scripts/check-book.js --paragraph-mode part-a --paragraph-profile publisher-print "../4veco-lessen/Boek 1 - Grondslagen, vraag en aanbod"
node scripts/check-course-target-exercises-v5.js
npm.cmd run agent:index
```

Also run current paragraph/chapter validators for every regenerated paragraph and any companion surfaces actually touched by the sprint. If the sprint changes generated web/game surfaces, run the relevant deploy/link/data checks and screenshot QA required by the platform workflow.

## Stop Conditions

- Stop if the sprint would hand-edit generated output instead of regenerating through the platform workflow.
- Stop if costs/revenue are silently kept as Book 1 `1.3.2` / `1.3.3` coverage.
- Stop if the existing `1.4.1` / `1.4.2` flags are hidden or dropped without review.
- Stop if any artifact claims CP-6 or Year 1 is closed.
- Stop if protected reference mutation is needed; route that through the references team and the appropriate CLI/human gate first.

## Handoff Back To References Team

When this ticket is completed, send the references team:

- lesson repo commit SHA;
- platform commit SHA used for generation;
- list of changed/generated lesson files;
- sprint plan and closure log paths;
- validation command outputs;
- review/quality-ref paths for `1.3.2`, `1.3.3`, and `1.3.4`;
- explicit statement whether the CP.6a mismatch is fixed, still blocked, or fixed with carried conditions.
