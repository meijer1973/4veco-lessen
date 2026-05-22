# SYNC-3 Shared Skill-Map Roadmap Update

Date: 2026-05-22
Status: CLOSED PASS

## Purpose

Record the roadmap-only sync that makes the scalable game architecture explicit:
three practice engines plus one shared skill-map / skill-tree engine.

This sprint does not implement engine code, mutate generated lesson output, or
authorize product-use changes.

## Inputs Read

- `lessen-team-roadmap.md`
- `../4veco-platform/references/reference-team-roadmap.md`
- `../4veco-platform/docs/roadmaps/roadmap-version-index.json`
- `../4veco-platform/AGENTS.md`
- `../CLAUDE.md`

## Changes

Lesson roadmap:

- added `L1.7C-0 Shared Skill-Map Engine Contract` between L1.7B and L1.7C;
- revised L1.7B so the exit-ticket MVP uses compact checkpoint mode once the
  shared engine exists;
- revised L1.7C so `Redeneren`, `Rekenen`, and `Grafieken` remain separate
  practice engines but consume one shared skill-map contract;
- revised L1.7D so landing-page cleanup consumes the shared skill-map/game
  architecture instead of exposing three separate skill-tree UIs or a full
  unfiltered catalog;
- updated Scale Gate 1, L2.0 sequencing, and short-term deliverables.

Platform roadmap:

- bumped the references roadmap to `v2.66-shared-skill-map-engine-tracking`;
- added `GAME-UX-1 Shared Skill-Map Engine Architecture` as platform support for
  lesson L1.7C-0;
- updated `LESSON-SCALE-1`, Product Gate, critical path, and immediate-next
  wording so broad companion scaling remains blocked until the shared route
  architecture is explicit;
- refreshed roadmap version indexes and GitHub-facing indexes.

## Architecture Recorded

Shared support engine:

- progression display;
- aspect filtering;
- recommended next skill;
- prerequisites and dependency route;
- locked/open/completed states;
- stars/progress;
- compact, route, and full display modes.

Practice engines:

- `Redeneren`;
- `Rekenen`;
- `Grafieken`.

The shared skill-map engine is not a fourth game.

## Boundaries Preserved

No sprint created by this update may authorize:

- adaptive diagnostics;
- mastery decisions;
- automatic sequencing;
- student-facing AI;
- grading or summative use;
- PV projection;
- PV machine promotion;
- broad companion scaling.

## Source-Control Note

The local prototype candidate
`../4veco-platform/knowledge/exit-ticket-game-1.1.1.zip` remains untracked. This
sync records it as input for L1.7B but does not add the binary to source control.

## Validation

Planned validation for this roadmap-only sync:

```powershell
node build-scripts\references\check-roadmap-version-index.js
npm.cmd run dashboard:internal
npm.cmd run agent:index
node build-scripts\sprints\emit-url-index.js
node build-scripts\sprints\emit-url-index.js --check
```

## Closure

SYNC-3 closes when both roadmaps and roadmap indexes are committed and pushed.
