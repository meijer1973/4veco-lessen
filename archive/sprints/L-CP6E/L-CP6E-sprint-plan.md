# L-CP6E Sprint Plan: 1.1.3 Part A Figure Numbering Remediation

Date: 2026-05-21
Status: CLOSED PASS WITH FLAGS
Owner: lesson team
Source handoff: platform CP.6e Focused 1.1.3 Part A Re-Review

## Goal

Clear the remaining `1.1.3 Grafieken en tabellen` Part A figure-numbering
blocker by making first-use figure references sequential in the live lesson
source and regenerated publisher-print outputs.

The expected first-use order is:

```text
Figuur 1 -> Figuur 2 -> Figuur 3
```

This sprint does not close CP-6 or Year 1.

## Baseline Evidence

Read before implementation:

- `reports/sprints/CP.6e-plan.md`
- `reports/sprints/CP.6e-result.md`
- `reports/reference-planning/CP.6e-113-part-a-rereview.md`
- `reports/reference-planning/CP.6e-113-part-a-remediation-handoff.md`
- `references/data/sprints/CP.6e-113-part-a-rereview.json`
- `reports/review-gates/GATE-CP6-year-1-paragraph-coverage/human-interview.md`
- `references/reference-team-roadmap.md`
- `lessen-team-roadmap.md`
- `Boek 1 - Grondslagen, vraag en aanbod/1.1 Hoofdstuk Economisch denken en rekenen/1.1.3 Grafieken en tabellen/_paragraph-plan.md`
- `Boek 1 - Grondslagen, vraag en aanbod/1.1 Hoofdstuk Economisch denken en rekenen/1.1.3 Grafieken en tabellen/1.1.3 Grafieken en tabellen – paragraaf.md`
- `Boek 1 - Grondslagen, vraag en aanbod/1.1 Hoofdstuk Economisch denken en rekenen/1.1.3 Grafieken en tabellen/1.1.3-review.md`
- `Boek 1 - Grondslagen, vraag en aanbod/1.1 Hoofdstuk Economisch denken en rekenen/1.1.3 Grafieken en tabellen/1.1.3-quality-ref.yaml`

Baseline finding:

- CP.6e records failed clearance because the live paragraph first mentions
  figures in the sequence `1 -> 3 -> 2`.
- The repeated worked example in `opgaven.md` is accepted by CP.6e as
  standalone-exercise scaffolding and is not the current hard blocker.

## Owning Source And Regeneration Route

The owning lesson source is:

```text
Boek 1 - Grondslagen, vraag en aanbod/
  1.1 Hoofdstuk Economisch denken en rekenen/
    1.1.3 Grafieken en tabellen/
      1.1.3 Grafieken en tabellen – paragraaf.md
      _assets/1.1.3_fig_2.*
      _assets/1.1.3_fig_3.*
```

Generated outputs must be rebuilt through the existing platform/lesson build
route:

- paragraph publisher-print outputs via the paragraph `build_pdf.py`;
- Chapter 1.1 aggregate outputs via the chapter `build_chapter.py`;
- Book 1 aggregate outputs via `python build-scripts/books/build-book.py --book 1`;
- indexes/maps via platform scripts where roadmap or archive files change.

Do not hand-edit generated HTML/PDF output as a shortcut.

## Implementation Procedure

1. Confirm the local worktree is clean enough to identify this sprint's changes.
2. Update the Part A paragraph source so the axis-convention figure is `Figuur
   2` and the interpolation figure is `Figuur 3`.
3. Keep asset naming aligned with visible figure labels by swapping the
   `_assets/1.1.3_fig_2.*` and `_assets/1.1.3_fig_3.*` contents or names, then
   update the paragraph image references accordingly.
4. Rebuild the paragraph Part A outputs using the paragraph build script.
5. Rebuild the Chapter 1.1 aggregate and Book 1 aggregate outputs.
6. Verify first-use order in:
   - `paragraaf.md`;
   - `paragraaf.html`;
   - `paragraaf.pdf` if text extraction is available, otherwise record that PDF
     was regenerated from the verified source/HTML.
7. Update `1.1.3-review.md` and `1.1.3-quality-ref.yaml` so the figure-numbering
   blocker is recorded as fixed, while the repeated worked-example flag remains
   visible as accepted standalone-exercise scaffolding.
8. Update `lessen-team-roadmap.md` with the L-CP6E closure record.
9. Write:
   - `archive/sprints/L-CP6E/L-CP6E-technical-qa-report.md`;
   - `archive/sprints/L-CP6E/L-CP6E-closure-log.md`;
   - `archive/sprints/L-CP6E/L-CP6E-handoff-to-references.md`.
10. Run validations and stop if any required gate fails.
11. Commit and push the lesson repo, then refresh platform indexes/maps if
    needed and push those changes too.

## Validation Commands

Run from `C:\Projects\4veco\4veco-platform` unless noted:

```powershell
node scripts/validate-paragraph.js --mode part-a --profile publisher-print "../4veco-lessen/Boek 1 - Grondslagen, vraag en aanbod/1.1 Hoofdstuk Economisch denken en rekenen/1.1.3 Grafieken en tabellen"
node scripts/validate-chapter.js "../4veco-lessen/Boek 1 - Grondslagen, vraag en aanbod/1.1 Hoofdstuk Economisch denken en rekenen"
node scripts/check-book.js --paragraph-mode part-a --paragraph-profile publisher-print "../4veco-lessen/Boek 1 - Grondslagen, vraag en aanbod"
node scripts/check-book-print-scope.js "../4veco-lessen/Boek 1 - Grondslagen, vraag en aanbod"
node scripts/check-course-target-exercises-v5.js
npm.cmd run agent:index
```

Focused checks:

```powershell
# Verify first-use sequence in markdown and HTML is 1 -> 2 -> 3.
```

If roadmap/report surfaces are changed in platform indexes, also run the normal
URL/dashboard refresh commands available in the platform repo.

## Acceptance Criteria

- `1.1.3 Grafieken en tabellen – paragraaf.md` first mentions figures in the
  sequence `1 -> 2 -> 3`.
- Regenerated `paragraaf.html` shows the same sequence.
- Regenerated `paragraaf.pdf` is rebuilt from the corrected paragraph source.
- Affected Chapter 1.1 and Book 1 aggregate surfaces are regenerated or
  explicitly proven unaffected.
- `1.1.3-review.md` no longer carries the stale figure-numbering blocker.
- `1.1.3-quality-ref.yaml` no longer lists figure numbering as an unresolved
  Part A flag.
- The repeated worked-example flag remains visible as an accepted/non-blocking
  standalone-exercise scaffold unless a later quality gate changes that policy.
- Validation outputs are recorded.
- The handoff gives references team the lesson commit SHA, platform commit SHA
  used for validation/generation, changed/generated file list, and explicit
  CP.6f recheck status.

## Stop Conditions

Stop and report instead of closing if:

- the figure-numbering issue cannot be fixed without changing the paragraph's
  learning design or visual set;
- the work would require hand-editing generated HTML/PDF instead of rebuilding;
- validation fails and the failure is not clearly unrelated to this sprint;
- review evidence and quality-ref status contradict each other;
- any artifact would claim CP-6 or Year 1 is closed;
- protected reference mutation, unit minting, target-exercise promotion,
  placeholder finalization, diagnostics, adaptive routing, mastery/sequencing,
  student-facing AI, summative use, PV projection, or PV machine promotion is
  required.

## Handoff Back To References

When complete, provide:

- lesson repo commit SHA;
- platform commit SHA used for generation/validation;
- changed/generated lesson file list;
- sprint plan and closure log paths;
- validation command outputs;
- updated Part A review path;
- updated quality-ref path;
- explicit statement that the `1.1.3` Part A figure-numbering blocker is fixed,
  still blocked, or fixed with carried conditions.
