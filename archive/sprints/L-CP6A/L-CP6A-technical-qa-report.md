# L-CP6A Technical QA Report

Date: 2026-05-19
Status: GREEN

## Scope

L-CP6A remediated the lesson-side Book 1 Chapter 1.3 mismatch from platform
CP.6a. The sprint changed generated lesson output only through the platform-owned
remediation script and existing paragraph/chapter/book build workflow.

## Commands Run

Platform source and generation:

```powershell
node --check build-scripts\sprints\l-cp6a-remediate-book1-chapter13.js
node build-scripts\sprints\l-cp6a-remediate-book1-chapter13.js
```

Paragraph/chapter/book regeneration:

```powershell
python build_pdf.py
python build_chapter.py
python build-scripts\books\build-book.py --book 1
```

The paragraph build command was run in:

- `1.3.2 Marktevenwicht`
- `1.3.3 Verschuivingen en nieuw evenwicht`
- `1.3.4 Gemengde opgaven`

Validation:

```powershell
node scripts\validate-chapter.js "..\4veco-lessen\Boek 1 - Grondslagen, vraag en aanbod\1.3 Hoofdstuk Aanbod en marktevenwicht"
node scripts\check-book.js --paragraph-mode part-a --paragraph-profile publisher-print "..\4veco-lessen\Boek 1 - Grondslagen, vraag en aanbod"
node scripts\check-book-print-scope.js "..\4veco-lessen\Boek 1 - Grondslagen, vraag en aanbod"
node scripts\check-course-target-exercises-v5.js
npm.cmd run agent:index
npm.cmd test -- --runInBand scripts/tests/check-book-print-scope.test.js scripts/tests/check-book.test.js
npm.cmd test -- --runInBand
```

## Results

- Chapter 1.3 validation: passed, 0 errors / 0 warnings.
- Book health: passed, 26/26 checks.
- Book print scope: passed, 12/12 print paragraphs.
- v5 target-exercise count: passed, total 54 with book counts 12/12/14/16.
- Agent index generation: passed; platform and lesson GitHub-agent indexes were regenerated.
- Focused book Jest: passed, 2 suites / 7 tests.
- Full platform Jest: passed, 30 suites passed / 6 skipped; 515 tests passed / 8 skipped.
- Stale visible print-content scan against assembled Book 1 markdown: no matches for active blockers.

## Notes

`check-book.js` still discovers historical online chapters 1.4 and 1.5 in the
book folder and validates them. The printed Book 1 aggregate is controlled by
the v5 manifest and `check-book-print-scope.js`; it contains only the 12 active
count-bearing paragraphs.

No deploy/student-web regeneration was required because this ticket touched
Part A chapter/book output and not companion web/game surfaces.
