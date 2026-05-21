# Lesson Team Ticket L-CP6E: 1.1.3 Part A Figure Numbering Remediation

Status: open, not started

Owner: lesson team

Created: 2026-05-21

Source handoff: platform `CP.6e Focused 1.1.3 Part A Re-Review`

References-team consequence: CP.6f cannot clear the `1.1.3` Part A blocker until this lesson-side remediation is completed and handed back with evidence.

CP-6 and Year 1 are not closed by this ticket.

## Problem

The `1.1.3 Grafieken en tabellen` Part A figure-numbering flag is still open.

The platform CP.6e re-review checked the live lesson output and found that `1.1.3 Grafieken en tabellen – paragraaf.md` still mentions `Figuur 3` before `Figuur 2`.

Current first-use sequence:

```text
1 -> 3 -> 2
```

Expected first-use sequence:

```text
1 -> 2 -> 3
```

The current `1.1.3-quality-ref.yaml` still records the Part A verdict as `FLAG`, so references-team CP-6 cannot treat this blocker as cleared.

## Evidence To Read First

Platform evidence:

- `4veco-platform/reports/sprints/CP.6e-plan.md`
- `4veco-platform/reports/sprints/CP.6e-result.md`
- `4veco-platform/reports/reference-planning/CP.6e-113-part-a-rereview.md`
- `4veco-platform/reports/reference-planning/CP.6e-113-part-a-remediation-handoff.md`
- `4veco-platform/references/data/sprints/CP.6e-113-part-a-rereview.json`
- `4veco-platform/references/reference-team-roadmap.md`

Lesson-side evidence:

- `lessen-team-roadmap.md`
- `Boek 1 - Grondslagen, vraag en aanbod/1.1 Hoofdstuk Economisch denken en rekenen/1.1.3 Grafieken en tabellen/_paragraph-plan.md`
- `Boek 1 - Grondslagen, vraag en aanbod/1.1 Hoofdstuk Economisch denken en rekenen/1.1.3 Grafieken en tabellen/1.1.3 Grafieken en tabellen – paragraaf.md`
- `Boek 1 - Grondslagen, vraag en aanbod/1.1 Hoofdstuk Economisch denken en rekenen/1.1.3 Grafieken en tabellen/1.1.3 Grafieken en tabellen – paragraaf.html`
- `Boek 1 - Grondslagen, vraag en aanbod/1.1 Hoofdstuk Economisch denken en rekenen/1.1.3 Grafieken en tabellen/1.1.3 Grafieken en tabellen – paragraaf.pdf`
- `Boek 1 - Grondslagen, vraag en aanbod/1.1 Hoofdstuk Economisch denken en rekenen/1.1.3 Grafieken en tabellen/1.1.3-review.md`
- `Boek 1 - Grondslagen, vraag en aanbod/1.1 Hoofdstuk Economisch denken en rekenen/1.1.3 Grafieken en tabellen/1.1.3-quality-ref.yaml`

Check the local directory before editing so the sprint uses exact paths for every regenerated output.

## Required Outcome

Run a later authorized lesson-side remediation/regeneration sprint that makes the Part A paragraph figure references sequential on first use:

1. `Figuur 1`
2. `Figuur 2`
3. `Figuur 3`

The remediation must also update or regenerate the affected Part A surfaces and review evidence so the references team can run CP.6f against current proof.

## In Scope

- Write an operational sprint plan before changing lesson output.
- Use the platform build workflow; do not hand-patch generated lesson output as a shortcut.
- Fix the `1.1.3` Part A figure-reference ordering in the source/generation route that owns the paragraph.
- Regenerate affected Part A output, including markdown, HTML, PDF, and any aggregate chapter/book surfaces that the sprint plan identifies as downstream outputs.
- Re-run or refresh the Part A review evidence so the figure-numbering flag is either cleared or explicitly carried with rationale.
- Update `1.1.3-quality-ref.yaml` only through the appropriate lesson/platform workflow and only if the review evidence supports the new status.
- Produce a lesson-team closure log with exact changed/generated files, validation commands, and the lesson commit SHA.
- Hand proof back to the references team so CP.6f can recheck the `1.1.3` Part A blocker.

## Out Of Scope

- CP-6 closure.
- Year-1 closure.
- Target-exercise promotion to `reviewed_final`.
- Placeholder finalization for `1.1.4`, `1.2.4`, or `1.3.4`.
- Unit minting or protected reference mutation.
- Broad Book 1 flag burn-down beyond the exact `1.1.3` Part A figure-numbering issue.
- Companion Part B redesign unless the chosen regeneration route proves it is directly affected.
- Diagnostics, adaptive routing, mastery, sequencing, student-facing AI, summative use, PV projection, or PV machine promotion.

## Acceptance Criteria

- `1.1.3 Grafieken en tabellen – paragraaf.md` first mentions figures in the sequence `1 -> 2 -> 3`.
- The regenerated `paragraaf.html` and `paragraaf.pdf` present the same sequential figure order.
- Any affected chapter/book aggregate surfaces are regenerated or explicitly proven unaffected.
- `1.1.3-review.md` and `1.1.3-quality-ref.yaml` no longer hide stale Part A evidence; the figure-numbering flag is either cleared or explicitly carried with current rationale.
- The lesson repo records the generated file list and validation results.
- The references team receives the lesson commit SHA and validation evidence before CP.6f treats the blocker as resolved.

## Minimum Validation Commands

Run from `4veco-platform` unless a future sprint plan names a stricter command set:

```bash
node scripts/validate-paragraph.js --mode part-a --profile publisher-print "../4veco-lessen/Boek 1 - Grondslagen, vraag en aanbod/1.1 Hoofdstuk Economisch denken en rekenen/1.1.3 Grafieken en tabellen"
node scripts/check-book.js --paragraph-mode part-a --paragraph-profile publisher-print "../4veco-lessen/Boek 1 - Grondslagen, vraag en aanbod"
node scripts/check-course-target-exercises-v5.js
npm.cmd run agent:index
```

Also run the current paragraph/chapter/book validators for every regenerated surface actually touched by the sprint. If the sprint changes generated web/game surfaces, run the relevant deploy/link/data checks and screenshot QA required by the platform workflow.

## Stop Conditions

- Stop if the sprint would hand-edit generated output instead of fixing the owning source/generator route.
- Stop if the figure-numbering issue cannot be fixed without changing the paragraph's learning design or visual set; route that as a planning decision before editing.
- Stop if review evidence remains stale or contradicts the quality ref.
- Stop if any artifact claims CP-6 or Year 1 is closed.
- Stop if protected reference mutation is needed; route that through the references team and the appropriate CLI/human gate first.

## Handoff Back To References Team

When this ticket is completed, send the references team:

- lesson repo commit SHA;
- platform commit SHA used for generation;
- list of changed/generated lesson files;
- sprint plan and closure log paths;
- validation command outputs;
- updated Part A review path;
- updated quality-ref path;
- explicit statement whether the `1.1.3` Part A figure-numbering blocker is fixed, still blocked, or fixed with carried conditions.
