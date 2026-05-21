# L-CP6E Technical QA Report

Date: 2026-05-21
Status: GREEN; READY FOR REFERENCES CP.6f RECHECK

## Scope

L-CP6E remediates the `1.1.3 Grafieken en tabellen` Part A figure-numbering
blocker reported by platform CP.6e.

The sprint changed the owning Part A source and regenerated affected outputs.
It does not close CP-6 or Year 1.

## Source Fix

Changed source:

- `1.1.3 Grafieken en tabellen – paragraaf.md`
- `_assets/1.1.3_fig_2.svg`
- `_assets/1.1.3_fig_2.png`
- `_assets/1.1.3_fig_3.svg`
- `_assets/1.1.3_fig_3.png`

The axis-convention visual is now `Figuur 2`.
The interpolation visual is now `Figuur 3`.

## Generated Outputs

Regenerated through existing build scripts:

- paragraph Part A HTML/PDF via paragraph `build_pdf.py`;
- Chapter 1.1 aggregate markdown, HTML, and PDF via `build_chapter.py`;
- Book 1 aggregate markdown, HTML, and PDF via platform `build-book.py --book 1`.

The paragraph `build_pdf.py` also refreshed `opgaven` and `antwoorden`
HTML/PDF outputs. Their source markdown was not changed.

## Focused Figure-Order Check

```text
1.1.3 Grafieken en tabellen – paragraaf.md first-use: 1 -> 2 -> 3
1.1.3 Grafieken en tabellen – paragraaf.html first-use: 1 -> 2 -> 3
1.1.3 Grafieken en tabellen – paragraaf.pdf first-use: 1 -> 2 -> 3
```

PDF text was checked with `pdftotext -layout`.

## Validation Results

| Command | Result | Notes |
|---|---:|---|
| `node scripts/validate-paragraph.js --mode part-a --profile publisher-print "../4veco-lessen/Boek 1 - Grondslagen, vraag en aanbod/1.1 Hoofdstuk Economisch denken en rekenen/1.1.3 Grafieken en tabellen"` | PASS | Paragraph 1.1.3 passed all checks; Part A PDFs present; 6 image refs resolve. |
| `node scripts/validate-chapter.js "../4veco-lessen/Boek 1 - Grondslagen, vraag en aanbod/1.1 Hoofdstuk Economisch denken en rekenen"` | PASS | Chapter 1.1 passed. Existing orphaned 1.1.1 web/slide asset warnings remain non-blocking and unrelated to L-CP6E. |
| `node scripts/check-book.js --paragraph-mode part-a --paragraph-profile publisher-print "../4veco-lessen/Boek 1 - Grondslagen, vraag en aanbod"` | PASS | Book health passed 26/26. |
| `node scripts/check-book-print-scope.js "../4veco-lessen/Boek 1 - Grondslagen, vraag en aanbod"` | PASS | Book 1 print scope remains 12/12 paragraphs. |
| `node scripts/check-course-target-exercises-v5.js` | PASS | v5 target exercises remain total=54, books=1:12, 2:12, 3:14, 4:16. |
| `npm.cmd run dashboard:internal` | PASS | Platform internal dashboard regenerated. |
| `npm.cmd run agent:index` | PASS | GitHub agent indexes regenerated for platform and lesson repos. |
| `node build-scripts/sprints/emit-url-index.js` | PASS | URL index regenerated. |
| `node build-scripts/sprints/emit-url-index.js --check` | PASS | URL index confirmed current. |
| `npm.cmd test` | PASS | Full platform Jest passed: 515 tests, 8 skipped, 30 suites passed, 6 skipped. Fixture warning output is expected from validator negative tests. |

## Review And Quality Evidence

- `1.1.3-review.md` now records the figure-order check as PASS and keeps the
  repeated worked-example issue as accepted/non-blocking standalone scaffolding.
- `1.1.3-quality-ref.yaml` now records Part A as `PASS WITH FLAGS`.
- The remaining Part A flag is not the CP.6e blocker: `opgaven.md` repeats the
  worked example for standalone exercise use, which CP.6e accepted as
  non-blocking.

## Boundary Check

No artifact claims:

- CP-6 closure;
- Year-1 closure;
- target-exercise promotion;
- placeholder finalization;
- protected reference mutation;
- diagnostics, adaptive routing, mastery/sequencing, student-facing AI,
  summative use, PV projection, or PV machine promotion.

## Platform Commit Used

Generation and validation used platform commit:

```text
caab49c5d9cdc361f0ae01097aeebd16a60342d0
```
