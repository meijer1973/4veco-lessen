# L-CP6A Closure Log

Date: 2026-05-19
Verdict: PASS WITH FLAGS

## Decision

L-CP6A is closed on the lesson side. Book 1 Chapter 1.3 now consistently presents
the active-v5 scope:

1. `1.3.1 Aanbod`
2. `1.3.2 Marktevenwicht`
3. `1.3.3 Verschuivingen en nieuw evenwicht`
4. `1.3.4 Gemengde opgaven`

This fixes the lesson-side CP.6a mismatch for re-evaluation, but it does not
close CP-6, Year 1, or any target-exercise final-review gate.

## Changed / Generated File Groups

- Platform workflow:
  - `build-scripts/sprints/l-cp6a-remediate-book1-chapter13.js`
  - `build-scripts/books/book-manifests/book-1.json`
  - regenerated platform/lesson GitHub-agent index reports
- Lesson output:
  - renamed active chapter folder to `1.3 Hoofdstuk Aanbod en marktevenwicht`
  - migrated former `1.4.1 Marktevenwicht` into active `1.3.2 Marktevenwicht`
  - migrated former `1.4.2 Verschuivingen` into active `1.3.3 Verschuivingen en nieuw evenwicht`
  - rewrote `1.3.4 Gemengde opgaven` to consolidate supply, demand, equilibrium, and shifts only
  - rebuilt Chapter 1.3 markdown/HTML/PDF and answer booklet
  - rebuilt aggregate Book 1 markdown/HTML/PDF
- Archive/sprint records:
  - `archive/sprints/L-CP6A/displaced-book2-material/`
  - `archive/sprints/L-CP6A/old-chapter13-assembly/`
  - `archive/sprints/L-CP6A/L-CP6A-sprint-plan.md`
  - `archive/sprints/L-CP6A/L-CP6A-survival-map.md`
  - `archive/sprints/L-CP6A/L-CP6A-remediation-report.md`
  - `archive/sprints/L-CP6A/L-CP6A-technical-qa-report.md`
  - `archive/sprints/L-CP6A/L-CP6A-handoff-to-references.md`

## Validation

Green gates:

- `validate-chapter.js` for active Chapter 1.3: passed.
- `check-book.js --paragraph-mode part-a --paragraph-profile publisher-print`: 26/26.
- `check-book-print-scope.js`: 12/12 active print paragraphs.
- `check-course-target-exercises-v5.js`: 54 records, counts 12/12/14/16.
- `npm.cmd run agent:index`: passed.
- focused book Jest: 7/7.
- full platform Jest: 515 passed / 8 skipped.

## Flags Carried

- `1.3.2`, `1.3.3`, and `1.3.4` target-exercise states are migrated or placeholders, not `reviewed_final`.
- The inherited Part A pattern where exercises appear both in `paragraaf.md` and `opgaven.md` remains a maintenance flag.
- CP-6 and Year 1 remain reference-team decisions.
- Historical online chapters 1.4 and 1.5 remain in the repo but are excluded from the printed v5 Book 1 aggregate.
- Displaced costs/revenue material is archived for Book 2 survival; no Book 2 production is claimed.

## Commit SHA

The exact lesson and platform commit SHAs are reported after commit/push in the
handoff message to the references team. This file is part of the lesson commit
that carries the remediation evidence.
