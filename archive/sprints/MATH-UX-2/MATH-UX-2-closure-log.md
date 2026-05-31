# Lesson Archive: MATH-UX-2 Closure Log

Generated: 2026-05-31

Status: closed PASS WITH FLAGS after platform lead-review round 2.

## Summary

Platform MATH-UX-2 integrated the GAME-UX-3A shared task shell into the live
generated Book 1 `1.1.2 Percentages en indexcijfers` math route.

The route now renders calculation practice through shared task-shell controls
for:

- numeric input;
- calculation/work capture;
- final-answer entry;
- percentage/index notation;
- unit/notation field behavior.

Checkpoint-style calculation tasks are proven as a non-published fixture with
`targetReadinessEvidence: false`.

## Validation Evidence

Platform validation records:

- `reports/sprints/MATH-UX-2-lead-review-round2.md`
- `reports/sprints/MATH-UX-2-student-route-proof.md`
- `reports/sprints/MATH-UX-2-checkpoint-calculation-task-fixture.md`
- `reports/sprints/MATH-UX-2-screenshot-manifest.md`
- `reports/sprints/MATH-UX-2-screenshots/manifest.json`
- `build-scripts/sprints/check-math-ux2-route-output.js`

Lesson target validation passed:

```bash
npm.cmd run check:book -- "../4veco-lessen/Boek 1 - Grondslagen, vraag en aanbod"
```

## Boundary

This closes calculation UI integration only. It does not authorize
target-equivalent completion language, diagnostics, adaptive routing,
mastery/sequencing, summative use, PV, Scale Gate 1, or student/product use.

Next operational sprint: `REASON-UX-2`.
