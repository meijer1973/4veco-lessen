# SPEC-END-STATE Sprint Plan

Date: 2026-05-26
Status: ACTIVE; SPECIFICATION-HARDENING SPRINT

## Purpose

Create a canonical product end-state specification so future roadmap and sprint
updates cannot drift away from the intended product: a generated,
review-gated learning route that moves each student from current readiness to
target-exercise readiness.

This sprint does not generate lesson output and does not authorize broad
scaling, diagnostics, mastery, automatic sequencing, grading, summative use,
student-facing AI, PV projection, or PV machine promotion.

## Problem

The end-state definition is present across repository maps, operating docs,
companion specifications, review agents, roadmap entries, and exit-ticket
sprints, but it is not frozen in one small canonical file. That diffusion makes
agent drift more likely.

Recent review feedback also found that `pilot` and `MVP` labels were sometimes
used too generously. A smaller pilot may be acceptable, but it may not be
treated as the full product if it misses the original specification.

## Required Read-First Files

- `AGENTS.md`
- `RESEARCH_AGENT_MAP.md`
- `lessen-team-roadmap.md`
- `specifications/companion-core-specifications.md`
- `../4veco-platform/AGENTS.md`
- `../4veco-platform/BUILD-PARAGRAPH.md`
- `../4veco-platform/build-scripts/README.md`
- `../4veco-platform/RESEARCH_AGENT_MAP.md`

## Required Outputs

- `specifications/product-end-state.md`
- updated `specifications/companion-core-specifications.md`
- updated `lessen-team-roadmap.md`
- updated lesson `AGENTS.md`
- updated lesson `RESEARCH_AGENT_MAP.md`
- updated platform `AGENTS.md`
- updated platform `BUILD-PARAGRAPH.md`
- updated platform `build-scripts/README.md`
- updated platform/lesson repository-map references or generated indexes when
  the platform workflow requires them
- `archive/sprints/SPEC-END-STATE/SPEC-END-STATE-validation-log.md`
- `archive/sprints/SPEC-END-STATE/SPEC-END-STATE-closure-log.md`

No generated student-facing lesson HTML, PDF, or game output is expected from
this sprint.

## Procedure

1. Create the canonical product-end-state specification.
2. Link it from lesson operating docs, the companion core specification, and
   the roadmap.
3. Link it from platform operating/build docs so platform agents see the same
   north star before changing generators, engines, or paragraph workflows.
4. Update repository maps/indexes enough for GitHub-facing reviewers to find
   the new specification.
5. Record validation in this sprint folder.
6. Close this sprint only if the roadmap still keeps the current active sprint
   order intact and Scale Gate 1 remains blocked by the required pre-scale
   sprints.

## Acceptance Criteria

- The new canonical file states the exercise-first product end state.
- It defines the student route: `Start -> Leer -> Oefen -> Check -> Verdiep`.
- It distinguishes published paragraph completeness, companion-pilot
  completeness, target-exercise-readiness completeness, and scale readiness.
- It states that pilots and MVPs may reduce immediate scope but may not weaken
  the original specification.
- It is linked from the active lesson roadmap, companion specification, lesson
  AGENTS instructions, platform AGENTS instructions, and
  `BUILD-PARAGRAPH.md`.
- Future sprints `L1.7B-MAP`, `L1.7B-P23`, `L1.7B-Q2`, `GATE-L1.7B-Q2`,
  `REV-STD-1`, `Scale Gate 1`, `L-EX0`, and `L-EX1` are instructed to preserve
  or cite this baseline.
- No product-use boundary is weakened.

## Stop Conditions

Stop and report if:

- the new specification conflicts with a current human decision record;
- linking the new specification would imply Scale Gate 1 or broad scaling is
  already authorized;
- implementation would require hand-patching generated lesson output;
- the repository-map/index refresh produces unrelated generated churn that
  cannot be separated safely.
