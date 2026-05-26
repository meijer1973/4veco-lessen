# SCOPE-LANG-1 Sprint Plan

Date: 2026-05-26
Status: CLOSED PASS

## Goal

Harden both repositories against accidental downscoping language in active
planning surfaces.

## Context

Human review found that certain scope labels had become planning attractors:
agents were treating bounded implementation language as permission to weaken
the specification. The stable companion specification already said this was
not allowed, but the rule needed stronger wording and mechanical enforcement.

## Allowed Paths

- `specifications/companion-core-specifications.md`
- `specifications/product-end-state.md`
- `lessen-team-roadmap.md`
- `RESEARCH_AGENT_MAP.md`
- `../4veco-platform/references/reference-team-roadmap.md`
- `../4veco-platform/docs/roadmaps/roadmap-version-index.*`
- `../4veco-platform/reports/sprints/GAME-UX-2-*`
- `../4veco-platform/references/data/sprints/GAME-UX-2.*.json`
- `../4veco-platform/build-scripts/sprints/check-scope-language.js`
- `../4veco-platform/build-scripts/sprints/check-sprint-plan.js`
- `../4veco-platform/build-scripts/sprints/check-sprint-bundle.js`
- `../4veco-platform/package.json`

## Forbidden Paths

- Generated lesson output
- Protected reference data under `references/machine/` or
  `references/external/`
- Historical archive rewrites outside the current sprint records

## Procedure

1. Tighten the stable companion specification with a scope-language discipline
   section.
2. Rename current active roadmap and platform planning wording to bounded-scope
   wording.
3. Add a platform checker for restricted scope terms in active planning
   surfaces.
4. Wire the checker into sprint-plan and sprint-bundle validation.
5. Add focused tests for unauthorized terms, historical archive exclusion, and
   explicit authorization blocks.
6. Refresh maps/indexes and validate active surfaces.

## Acceptance

- Active roadmaps no longer normalize reduced-quality scope labels.
- Sprint checkers fail on unauthorized reintroduction.
- The companion spec states that bounded scope never lowers quality.
- Historical archives remain traceable.

## Next Step

If work continues after this sprint, proceed to the L1.7B-MAP human review.
