# L-PV1-L-PV4 Proof Track Execution Log

Date: 2026-05-14
Owner: lesson team
Status: HCS package prepared for human review

## Scope Executed

This log covers the executed part of the lesson-side PV-G4 proof track after
`L-PV0-proof-track-plan.md`:

- `L-PV1` Procedure Contract Hardening
- `L-PV2` Proof 001 - 1.1.1 B02 Procedure Mapping
- `L-PV3` Proof 002 - Fresh PV-Validated Surface
- `L-PV4` PV-G4 Intake Closure Packet

## What Changed

Platform-owned changes:

- added a lesson procedure contract registry;
- added `scripts/validate-procedure-contracts.js`;
- added negative Jest fixtures for count/order/code-leak/legacy-drift failures;
- added a platform generator for `1.1.1` procedure-game data with formal PV
  step IDs;
- added formal step IDs to the `1.1.2` procedure-game generator;
- updated the PV-G4 intake builder/checker so it reads lesson-owned proof
  records and can move from `0/2` to `2/2` without authorizing PV projection or
  machine promotion;
- added a proof-record builder for the lesson-owned HCS packet.

Lesson-owned changes:

- regenerated `shared/procedure/1.1.1.js` from platform source, removing the
  student-facing `(unit B02)` wording and adding formal step IDs;
- regenerated `shared/procedure/1.1.2.js` with formal step IDs;
- refreshed stale chapter/book/test-prep surfaces that still used old
  three-step economisch-denken language;
- rebuilt affected paragraph, chapter, and book HTML/PDF outputs through their
  existing build scripts;
- added two PV-G4 proof records and the HCS packet under
  `pv-g4-proof-records/`.

## Proof Records

Proof 001:

- `pv-g4-proof-records/PVG4-proof-001.json`
- Surface: `1.1.1 Schaarste en economisch denken`
- PV template: `choose_by_opportunity_cost_flow`
- Formal steps:
  `list_alternatives > calculate_payoffs > rank_not_chosen > interpret_net_choice_value`

Proof 002:

- `pv-g4-proof-records/PVG4-proof-002.json`
- Surface: bounded A61 table-trace pilot
- PV template: `select_table_values_trace`
- Formal steps:
  `read_question_target > check_table_headers_units > select_needed_values > label_selected_values`

HCS packet:

- `pv-g4-proof-records/HCS-PV-G4-lesson-regression-review-packet.md`

Reference-side intake:

- `4veco-platform/reports/json/procedure-visual-lesson-regression-proof-intake.json`
- `4veco-platform/reports/review-gates/GATE-PV-G4-lesson-regression/review-packet.md`

## Validation Evidence

Commands run and passing:

```powershell
npm.cmd test -- scripts/tests/procedure-contracts.test.js --runInBand
node scripts\validate-procedure-contracts.js --book-root "..\4veco-lessen\Boek 1 - Grondslagen, vraag en aanbod"
node build-scripts\references\build-pv-g4-lesson-proof-records.js
node build-scripts\references\build-procedure-visual-lesson-regression-proof-intake.js
node build-scripts\references\check-procedure-visual-lesson-regression-proof-intake.js
```

The proof-record builder also ran these commands successfully and recorded them
inside `PVG4-proof-001.json`:

```powershell
node scripts\validate-paragraph.js --mode complete --profile student-web "<1.1.1 paragraph>"
node scripts\validate-paragraph.js --mode part-a --profile publisher-print "<1.1.1 paragraph>"
node scripts\validate-paragraph.js --mode complete --profile student-web "<1.1.2 paragraph>"
npm.cmd run check:book -- "<Book 1 root>"
```

## Boundary

This package does not close PV-G4. It prepares the lesson-side evidence for HCS
human review.

Still blocked unless a later HCS/reference gate explicitly authorizes it:

- PV records in `references/machine`;
- student-facing PV projection;
- adaptive/diagnostic/mastery/sequencing/summative use;
- treating the A61 pilot as a published student surface.

## Remaining Human Gate

HCS must review:

- whether the two proof records are sufficiently diverse;
- whether proof 001 is acceptable as a real paragraph proof;
- whether proof 002 is acceptable as a bounded pilot proof rather than a full
  paragraph build;
- whether the no-hand-patch evidence is adequate;
- whether PV-G4 may close, close with conditions, or remain held.
