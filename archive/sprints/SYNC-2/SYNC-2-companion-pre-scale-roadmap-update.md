# SYNC-2 Companion Pre-Scale Roadmap Update

Date: 2026-05-22
Status: CLOSED PASS

## Purpose

Update the lesson and reference roadmaps after strategic review identified a
pre-scale product-sprawl risk in the companion layer.

This is a roadmap-only sync. It does not change generated lesson output,
platform generators, protected references, target exercises, MTUs, or student
product behavior.

## Inputs Read

- `lessen-team-roadmap.md`
- `../4veco-platform/references/reference-team-roadmap.md`
- `../4veco-platform/docs/roadmaps/roadmap-version-index.json`
- `../4veco-platform/docs/roadmaps/roadmap-version-index.md`
- local repository search for `exit`, `ticket`, `checkpoint`, `afsluiting`, and
  `escape`

## Finding

The lesson roadmap already covered L1.7A readiness review and L2.0 house-style
cleanup, but it did not sharply define:

- an exit-ticket game or companion-completion contract;
- a serious quality upgrade for the three second-row games;
- a landing-page information architecture sprint to avoid card-dump scaling.

Local platform search found an untracked candidate prototype:

```text
../4veco-platform/knowledge/exit-ticket-game-1.1.1.zip
```

Because it is untracked, this roadmap update records it as a source-control gap
for L1.7B rather than adding the binary.

## Changes Made

Lesson roadmap:

- inserted `L1.7B Exit Ticket Game MVP + Companion Completion Contract`;
- inserted `L1.7C Three-Aspect Game Quality Upgrade`;
- inserted `L1.7D Paragraph Landing Page Information Architecture Cleanup`;
- moved L2.0 after L1.7A-D in the intended sequence;
- updated Scale Gate 1 so broad companion scaling requires the companion-set
  contract, game-row rubric, and landing-page IA;
- added detailed sprint sections and short-term deliverable notes.

Reference roadmap:

- bumped the active roadmap to
  `v2.65-lesson-companion-pre-scale-gates`;
- archived v2.64 as
  `docs/roadmaps/outdated/reference-team-roadmap-v2.64-gate-ex2-pass-with-conditions.md`;
- added a tracking dependency that broad companion/product scaling must wait for
  lesson L1.7A-D and L2.0;
- updated the roadmap version index.

## Boundaries Preserved

This update authorizes none of the following:

- generated lesson output mutation;
- protected reference mutation;
- target-exercise promotion;
- placeholder finalization;
- unit minting;
- broad companion scaling;
- diagnostics;
- adaptive routing;
- mastery/sequencing;
- student-facing AI;
- summative use;
- PV projection;
- PV machine promotion.

## Validation

Roadmap-only validation:

- local searches confirm the exit-ticket prototype is not repository-tracked;
- `node build-scripts/references/check-roadmap-version-index.js` passed with
  68 entries;
- `npm.cmd run dashboard:internal` passed;
- `npm.cmd run agent:index` passed;
- `node build-scripts/sprints/emit-url-index.js` and `--check` passed.
