# L-PV0 Proof Track Plan

Sprint: `L-PV0 - PV-G4 Lesson Proof Track Planning`
Date: 2026-05-14
Owner: lesson team
Status: CLOSED - plan executed through L-PV4; HCS human review pending

## Baseline Check

The current platform PV-G4 intake report still records `0/2` lesson-side
proofs. The earlier `L1.5D-B02` and `L1.4-PARITY` work is useful cleanup
evidence, but it is not yet formal PV-G4 proof-record evidence.

Current repo check before execution:

- `4veco-platform/reports/json/procedure-visual-lesson-regression-proof-intake.json`
  reports no proof records.
- Existing PV records are in `references/data/procedure-visual/`; no PV
  machine promotion is authorized.
- `shared/procedure/1.1.1.js` in the lesson target still contains student-facing
  `(unit B02)` in the procedure-game description.
- The paragraph-level `1.1.1 paragraaf.md` is on the four-step route, but the
  assembled chapter/book markdown still contains old three-step wording. The
  proof validator must catch these aggregate surfaces.

## Proof Candidates

### Proof 001

Paragraph/surface:

- `1.1.1 Schaarste en economisch denken`
- procedure game plus Part A/Part B procedure parity

PV records:

- procedure template: `choose_by_opportunity_cost_flow`
- visual state: `flowchart_opportunity_cost_choice`
- unit-template link: `B02:choose_by_opportunity_cost_flow`

Formal step order:

1. `list_alternatives`
2. `calculate_payoffs`
3. `rank_not_chosen`
4. `interpret_net_choice_value`

Proof type:

- procedure game maps to formal PV steps
- answer model and lesson surfaces validate against the same step order

### Proof 002

Surface:

- bounded lesson-owned A61 table-trace pilot surface

PV records:

- procedure template: `select_table_values_trace`
- visual state: `table_trace_source_values_selected`
- unit-template link: `A61:select_table_values_trace`

Formal step order:

1. `read_question_target`
2. `check_table_headers_units`
3. `select_needed_values`
4. `label_selected_values`

Proof type:

- pilot surface validates a different PV step order and visual anchor
- no student-facing PV publication is claimed

Rationale: this gives a second proof that is materially different from B02
without pretending a full new paragraph has been completed inside this gate.

## Artifact Locations

Lesson-owned artifacts:

- `pv-g4-proof-records/PVG4-proof-001.json`
- `pv-g4-proof-records/PVG4-proof-002.json`
- `pv-g4-proof-records/pilot-surfaces/a61-table-trace-pilot.json`
- `pv-g4-proof-records/reports/PVG4-proof-001-procedure-contract-report.json`
- `pv-g4-proof-records/reports/PVG4-proof-002-a61-table-trace-report.json`
- `pv-g4-proof-records/HCS-PV-G4-lesson-regression-review-packet.md`

Platform-owned tooling:

- `references/data/procedure-visual/lesson-procedure-contracts.json`
- `scripts/validate-procedure-contracts.js`
- `build-scripts/content/book-1/b1-111-procedure-data.js`
- `build-scripts/references/build-pv-g4-lesson-proof-records.js`
- updated PV-G4 intake builder/checker

## Validation Commands

Required before the HCS packet is considered ready:

```powershell
node scripts\validate-procedure-contracts.js --book-root "..\4veco-lessen\Boek 1 - Grondslagen, vraag en aanbod"
node scripts\validate-paragraph.js --mode complete --profile student-web "..\4veco-lessen\Boek 1 - Grondslagen, vraag en aanbod\1.1 Hoofdstuk Economisch denken en rekenen\1.1.1 Schaarste en economisch denken"
node scripts\validate-paragraph.js --mode part-a --profile publisher-print "..\4veco-lessen\Boek 1 - Grondslagen, vraag en aanbod\1.1 Hoofdstuk Economisch denken en rekenen\1.1.1 Schaarste en economisch denken"
node scripts\validate-paragraph.js --mode complete --profile student-web "..\4veco-lessen\Boek 1 - Grondslagen, vraag en aanbod\1.1 Hoofdstuk Economisch denken en rekenen\1.1.2 Percentages en indexcijfers"
npm.cmd run check:book -- "..\4veco-lessen\Boek 1 - Grondslagen, vraag en aanbod"
node build-scripts\references\build-pv-g4-lesson-proof-records.js
node build-scripts\references\build-procedure-visual-lesson-regression-proof-intake.js
node build-scripts\references\check-procedure-visual-lesson-regression-proof-intake.js
```

## No-Hand-Patch Evidence

The proof records must distinguish:

- platform source/tool changes;
- generated lesson output changes produced by platform scripts;
- lesson-owned proof-record artifacts.

For proof 001, generated procedure data must be written by
`b1-111-procedure-data.js`, not edited directly in the lesson target. Chapter
and book aggregate outputs must be rebuilt by their existing build scripts if
they are touched.

For proof 002, the pilot surface is a lesson-owned proof artifact, not a
student-facing generated output.

## Non-Goals

- no PV records move to `references/machine`;
- no student-facing PV projection;
- no adaptive, diagnostic, mastery, sequencing, AI, or summative use;
- no screenshot-only proof;
- no hand-patched generated lesson output as proof evidence.

## Stop Conditions

Stop before HCS submission if any of these are true:

- fewer than two complete proof records exist;
- the B02 proof still exposes `B02` in student-facing generated text/data;
- the procedure contract validator cannot catch count, order, label/keyword,
  surface, or code-leakage drift;
- the second proof does not validate an existing PV record;
- validation requires a new PV machine registry or student-facing PV
  publication;
- generated lesson output has to be manually patched to make the proof pass.

## Acceptance Tests

- The plan names exactly two proof candidates and their PV records.
- The artifact paths are explicit.
- The validation commands are reproducible.
- The no-hand-patch evidence path is explicit.
- The PV boundary remains blocked unless HCS later authorizes a separate gate.
