# SYNC-4 Engine Operationalization Roadmap Update

Date: 2026-05-29
Status: CLOSED PASS

## Purpose

Record the roadmap/specification sync that makes the shared task-type UI part
of the product end state and turns the engine roadmap from architecture proof
into student-visible operational proof.

This sprint does not implement engine code, mutate generated lesson output, or
authorize product-use changes.

## Inputs Read

- user-provided engine-operationalization report
- `lessen-team-roadmap.md`
- `specifications/product-end-state.md`
- `specifications/companion-core-specifications.md`
- `../4veco-platform/references/reference-team-roadmap.md`
- `../4veco-platform/docs/roadmaps/roadmap-version-index.json`
- `../4veco-platform/reports/sprints/SYNC-4-plan.md`
- `../4veco-platform/AGENTS.md`
- `../CLAUDE.md`

## Changes

Lesson specifications:

- added the shared operational UI requirement to the product end-state
  specification;
- added the shared task-type shell specification to the companion core
  specification;
- clarified that architecture-only proof is not enough for Scale Gate or
  controlled engine scaling.

Lesson roadmap:

- renamed the next platform dependency to `GAME-UX-3A Shared Task-Type UX
  Foundation`;
- added `ENGINE-OP-1`, `SKILLMAP-OP-1`, `GRAPH-UX-2`, `MATH-UX-2`,
  `REASON-UX-2`, `GAME-ARCH-1`, and `GATE-ENGINE-1`;
- revised Scale Gate 1 and short-term deliverables so broad companion scaling
  waits for live student-route proof.

Platform roadmap:

- bumped the references roadmap to `v3.11-engine-operationalization-track`;
- archived the v3.10 snapshot;
- kept `GATE-MTU-H4` as the active next action;
- inserted the same operational engine proof sequence after GATE-MTU-H4.

## Boundaries Preserved

No sprint created by this update may authorize:

- protected reference mutation;
- external-source mutation;
- machine-reference mutation;
- unit minting;
- answer-skill candidate storage or candidate writes;
- target-exercise mutation;
- generated projection refresh;
- generated lesson output;
- diagnostics;
- adaptive routing;
- mastery decisions;
- automatic sequencing;
- student-facing AI;
- grading or summative use;
- PV projection;
- PV machine promotion;
- Scale Gate 1 closure.

## Validation

Planned validation for this roadmap/specification sync:

```powershell
node build-scripts\sprints\check-sprint-plan.js reports\sprints\SYNC-4-plan.md
node build-scripts\sprints\check-sprint-bundle.js SYNC-4
node build-scripts\sprints\check-sprint-bundle.js SYNC-4 --complete
node build-scripts\references\check-roadmap-version-index.js
npm.cmd run check:scope-language
node build-scripts\sprints\emit-url-index.js --check
git diff --check
git -C ..\4veco-lessen diff --check
```

## Closure

SYNC-4 closes when both roadmaps, specifications, sprint records, version
indexes, and repository maps are committed and pushed.

Next operational action: run `GATE-MTU-H4`; after that, proceed to
`GAME-UX-3A` only if the gate closure authorizes the needed downstream
planning path.
