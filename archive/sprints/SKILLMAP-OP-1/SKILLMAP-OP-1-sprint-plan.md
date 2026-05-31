# Sprint SKILLMAP-OP-1: Student-Visible Skill-Map Route

Date: 2026-05-31

Platform plan:
`../../4veco-platform/reports/sprints/SKILLMAP-OP-1-plan.md`

## Lesson-Side Scope

The sprint was allowed to update the Book 1 deploy manifest and generated
automated output through platform deploy/build commands only.

Allowed lesson-side changes:

- `Boek 1 - Grondslagen, vraag en aanbod/deploy-config.json`
- generated automated route output produced by `4veco-platform/scripts/deploy.js`
- lesson roadmap/archive status records

Forbidden lesson-side changes:

- hand-patched generated HTML/CSS/JS/data
- lesson content rewrites outside generated automated route output
- target-equivalent completion language
- diagnostics, adaptive routing, mastery, sequencing, student-facing AI,
  summative use, PV projection, Scale Gate 1, or student/product use

## Quality Floor

The generated student route had to show a coherent paragraph target, relevant
skill subset, recommended focus, local progress, and practice action without
internal MTU codes.

## Evidence

Evidence lives in the platform sprint bundle:

- `reports/sprints/SKILLMAP-OP-1-student-route-proof.md`
- `reports/sprints/SKILLMAP-OP-1-screenshot-manifest.md`
- `reports/sprints/SKILLMAP-OP-1-screenshots/`
- `build-scripts/sprints/check-skillmap-op1-route-output.js`

