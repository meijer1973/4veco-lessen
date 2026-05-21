# L-CP6E Handoff To References

Date: 2026-05-21
Status: READY FOR CP.6f RECHECK

## Handoff Statement

The lesson-side `1.1.3` Part A figure-numbering blocker is fixed.

The paragraph, regenerated HTML, and regenerated PDF now first mention figures
in this order:

```text
Figuur 1 -> Figuur 2 -> Figuur 3
```

The correction was made through the lesson source and regenerated publisher
outputs. Generated HTML/PDF were not hand-patched.

## Evidence Paths

- Sprint plan: `archive/sprints/L-CP6E/L-CP6E-sprint-plan.md`
- Technical QA: `archive/sprints/L-CP6E/L-CP6E-technical-qa-report.md`
- Closure log: `archive/sprints/L-CP6E/L-CP6E-closure-log.md`
- Updated Part A review: `Boek 1 - Grondslagen, vraag en aanbod/1.1 Hoofdstuk Economisch denken en rekenen/1.1.3 Grafieken en tabellen/1.1.3-review.md`
- Updated quality ref: `Boek 1 - Grondslagen, vraag en aanbod/1.1 Hoofdstuk Economisch denken en rekenen/1.1.3 Grafieken en tabellen/1.1.3-quality-ref.yaml`

## Validation Evidence

Passed:

- focused markdown/HTML/PDF figure first-use check;
- `validate-paragraph` for `1.1.3` Part A publisher-print;
- `validate-chapter` for Chapter 1.1;
- `check-book` Book 1 publisher-print, 26/26;
- `check-book-print-scope`, 12/12;
- `check-course-target-exercises-v5`, total 54 with 12/12/14/16.

## Commits

Platform commit used for generation and validation:

```text
caab49c5d9cdc361f0ae01097aeebd16a60342d0
```

Lesson commit SHA:

```text
Recorded in the final push/report after this handoff is committed.
```

## Remaining Conditions

- CP-6 is not closed by this lesson-side correction.
- Year 1 is not closed by this lesson-side correction.
- The repeated worked-example pattern in `opgaven.md` remains visible as an
  accepted/non-blocking standalone-exercise scaffolding flag.
- CP.6f should decide whether the references-side `1.1.3` Part A blocker can be
  cleared based on the current lesson commit.
