# L-CP6A Remediation Report

Date: 2026-05-19
Status: CLOSED PASS WITH FLAGS; READY FOR REFERENCES-TEAM CP.6a RECHECK

## What Changed

- Renamed active Chapter 1.3 to `1.3 Hoofdstuk Aanbod en marktevenwicht`.
- Archived stale costs/revenue paragraph slots from active Book 1 Chapter 1.3.
- Migrated former `1.4.1 Marktevenwicht` into active-v5 `1.3.2 Marktevenwicht`.
- Migrated former `1.4.2 Verschuivingen` into active-v5 `1.3.3 Verschuivingen en nieuw evenwicht`.
- Re-scoped `1.3.4 Gemengde opgaven` to supply, demand, equilibrium, and shifts.
- Updated review and quality-ref records to preserve non-final v5/CP-6 status.
- Rebuilt `1.3.2`, `1.3.3`, `1.3.4`, Chapter 1.3, and the aggregate Book 1
  markdown/HTML/PDF through platform-owned workflow.
- Removed inherited excluded-cost exercise leakage from the migrated `1.3.3`
  source and excluded non-print-scope cost terms from the Book 1 glossary.

## Validation Result

Green:

- `node scripts\validate-chapter.js "..\4veco-lessen\Boek 1 - Grondslagen, vraag en aanbod\1.3 Hoofdstuk Aanbod en marktevenwicht"`
- `node scripts\check-book.js --paragraph-mode part-a --paragraph-profile publisher-print "..\4veco-lessen\Boek 1 - Grondslagen, vraag en aanbod"` -> 26/26
- `node scripts\check-book-print-scope.js "..\4veco-lessen\Boek 1 - Grondslagen, vraag en aanbod"` -> 12/12
- `node scripts\check-course-target-exercises-v5.js` -> 54 records, 12/12/14/16
- `npm.cmd run agent:index`
- focused Jest: `scripts/tests/check-book-print-scope.test.js` + `scripts/tests/check-book.test.js` -> 7/7
- full platform Jest -> 515 passed / 8 skipped

## CP-6 Status

This sprint prepares lesson-side evidence for references-team re-evaluation.
It does not close CP-6 or Year 1.
