# QUALITY-STD-1 Sprint Plan

Date: 2026-05-26
Status: CLOSED PASS

## Goal

Move quality-driving language to the planning point where agents form the work,
not only to review gates after implementation.

## Context

Human feedback found that the repositories already had strong review language,
but future agents needed operational planning language that defines what good
looks like before implementation starts.

## Quality Standard

The expected outcome is a complete, coherent, student-usable implementation of
the stated specification within the authorized scope. Passing tests, producing
files, or rendering a surface is not sufficient unless the output supports the
intended student action, preserves canonical terminology and procedures, and
has proof from the relevant review gates.

## Specification Fulfilment Matrix

| Specification requirement | Implementation evidence required | Review/proof required | Status |
|---|---|---|---|
| Planning docs define a quality floor | AGENTS/spec/build docs updated | diff review | complete |
| Sprint plans prove specification fulfilment | platform checker requires matrix and proof sections | focused checker tests | complete |
| Quality improvements are classified | plan template/checker language requires classification | focused checker tests | complete |
| Closure requires proof, not file existence | plan checker requires proof-to-close section | focused checker tests | complete |

## Quality Improvement Candidates

| Candidate improvement | Classification | Reason |
|---|---|---|
| Add quality-standard enforcement to sprint-plan checker | `include_now` | Directly prevents weak plans from passing. |
| Update all historical sprint plans | `reject_scope_creep` | Historical files should remain traceable unless reopened. |
| Leave REV-STD-1 for wider review-template hardening | `defer_named_follow_up` | This sprint targets planning pressure; REV-STD-1 still owns review packet reform. |

## Allowed Paths

- `AGENTS.md`
- `specifications/companion-core-specifications.md`
- `lessen-team-roadmap.md`
- `archive/sprints/QUALITY-STD-1/`
- `../4veco-platform/AGENTS.md`
- `../4veco-platform/BUILD-PARAGRAPH.md`
- `../4veco-platform/docs/sprints/README.md`
- `../4veco-platform/agents/lead-reviewer-agent.md`
- `../4veco-platform/build-scripts/sprints/check-sprint-plan.js`
- `../4veco-platform/build-scripts/sprints/check-sprint-plan.test.js`
- active platform sprint records updated only where needed for validator
  compatibility

## Forbidden Paths

- generated lesson output
- protected reference data under `references/machine/` or
  `references/external/`
- historical sprint-plan rewrites outside reopened current-operational records

## Inputs

- `specifications/product-end-state.md`
- `specifications/companion-core-specifications.md`
- platform `AGENTS.md`
- platform `BUILD-PARAGRAPH.md`
- platform `build-scripts/sprints/check-sprint-plan.js`
- current GAME-UX-2 sprint plan as checker compatibility example

## Outputs

- updated quality-driven execution language in both repo instructions;
- updated companion core specification;
- updated platform paragraph-build guidance;
- stricter platform sprint-plan checker and focused tests;
- current plan updates needed so existing bundle validation still passes.

## Operationalized sprint procedure

1. Read the stable product and companion specifications, both repo instructions,
   current sprint checker, and current GAME-UX-2 plan.
2. Add positive operational quality language before implementation points:
   repo instructions, companion spec, paragraph-build guidance, sprint docs,
   and lead-review instructions.
3. Update the sprint-plan checker so a plan must include quality standard,
   specification fulfilment matrix, quality improvement candidates, and proof
   required to close. Stop if the checker cannot distinguish quality planning
   from review-only language.
4. Add focused checker tests. Stop if a plan can still pass without rendered
   output proof, student-facing proof, or follow-up language.
5. Update current operational sprint records only as needed for validator
   compatibility. Do not rewrite historical archives.
6. Run active scope-language checks, focused tests, sprint-bundle checks, full
   platform Jest, map/index refreshes, and inventory checks before closure.

## Acceptance Tests

```bash
npm.cmd test -- --runInBand build-scripts/sprints/check-sprint-plan.test.js
node build-scripts/sprints/check-sprint-plan.js reports/sprints/GAME-UX-2-plan.md
node build-scripts/sprints/check-sprint-bundle.js GAME-UX-2 --complete
npm.cmd run check:scope-language
npm.cmd test
```

## Proof Required to Close

Close only when proof shows that the stricter checker passes focused tests,
GAME-UX-2 still validates as a completed sprint bundle, active scope-language
checks pass, full platform Jest passes, and refreshed maps/indexes/inventories
are current.

## Rollback Plan

Revert the quality-standard documentation changes, sprint-plan checker changes,
focused tests, and current-plan compatibility updates. Do not touch generated
lesson output or protected reference data.

## Human Review Required

No separate human review is required for this governance sprint. REV-STD-1
remains the later human-review-standard hardening sprint.

## Next Step

If work continues after this sprint, proceed to the L1.7B-MAP human review.
