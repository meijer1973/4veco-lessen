# SYNC-1 Roadmap Reconciliation Log

Date: 2026-05-18
Status: CLOSED PASS

## Purpose

Reconcile the lesson and reference roadmaps after the L1.5P, L1.5Q, and L1.6
closures. The strategy decision is foundation hardening before broad lesson
scaling.

## Baseline Read

- `lessen-team-roadmap.md`
- `C:\Projects\4veco\4veco-platform\references\reference-team-roadmap.md`
- `C:\Projects\4veco\4veco-platform\docs\roadmaps\roadmap-version-index.json`
- `C:\Projects\4veco\4veco-platform\docs\roadmaps\roadmap-version-index.md`
- `C:\Projects\4veco\4veco-platform\knowledge\three Year blue print.md`
- `C:\Projects\4veco\4veco-platform\references\SOURCE_OF_TRUTH.md`
- platform research maps and URL-index generators

## Plan

1. Record the current cross-team truth: L1.5P, L1.5Q, and L1.6 are closed,
   but broad lesson scaling is not approved.
2. Reframe lesson `L1.7` as `L1.7A Scaling Readiness And Flag Triage Gate`.
3. Add `L2.0 Book 1 Flag Burn-down And House-Style Cleanup` and
   `Scale Gate 1`.
4. Move the reference roadmap to `v2.45-post-l16-foundation-hardening`.
5. Insert `REF-CT0` before `REF-CT1`, and move `R14.1` earlier as curriculum
   versioning support.
6. Archive the previous reference roadmap version and update the roadmap
   version index.
7. Treat `knowledge/three Year blue print.md` as a non-authoritative planning
   prototype, not a source of truth.
8. Repair stale roadmap-map pointers that still referenced removed
   `knowledge/platform-team-roadmap.md` and `knowledge/three-month-roadmap.md`.
9. Regenerate derived URL/dashboard reports and run focused validation.

## Stop Conditions

- Stop if the active roadmap index still points to v2.44.
- Stop if either roadmap implies broad scaling is approved.
- Stop if the rough three-year blueprint is promoted as authoritative.
- Stop if stale research-map paths still point to missing roadmap files.
- Stop if blocked uses are loosened: diagnostics, adaptive routing, mastery,
  sequencing, student-facing AI, summative use, PV projection, or PV machine
  promotion.

## Outputs

- Updated `lessen-team-roadmap.md`.
- Updated platform `references/reference-team-roadmap.md`.
- Archived platform
  `docs/roadmaps/outdated/reference-team-roadmap-v2.44-s9a-d04-cli-mutation.md`.
- Updated platform roadmap version index JSON and Markdown.
- Updated platform research maps and generated URL/dashboard outputs.

## Validation

- `node build-scripts\references\check-roadmap-version-index.js` passed.
- `node build-scripts\sprints\emit-url-index.js --check` passed.
- Search confirmed current maps/generated reports no longer reference missing
  `knowledge/platform-team-roadmap.md` or `knowledge/three-month-roadmap.md`.
- `git diff --check` passed for both repositories.

## Decision

SYNC-1 closes PASS. The next lesson-side item is L1.7A readiness/flag triage.
The next reference-side item is REF-CT0 three-year prototype normalisation and
MTU classification. Broad lesson scaling remains paused.
