# L-CP6A Sprint Plan: Book 1 Chapter 1.3 v5 Alignment Remediation

Date: 2026-05-19
Status: CLOSED PLAN; IMPLEMENTED THROUGH PLATFORM WORKFLOW ON 2026-05-19

## Purpose

Resolve the open CP.6a lesson-side mismatch for active-v5 Book 1 Chapter 1.3.
The current print book is already v5-composed, but the chapter source tree still
presents `1.3.2 Kostenstructuren` and `1.3.3 Opbrengsten` as active Book 1
Chapter 1.3 slots. L-CP6A aligns the lesson-side chapter structure with active
v5 without closing CP-6 or Year 1.

Active v5 Chapter 1.3 target:

1. `1.3.1 Aanbod`
2. `1.3.2 Marktevenwicht`
3. `1.3.3 Verschuivingen en nieuw evenwicht`
4. `1.3.4 Gemengde opgaven: aanbod en marktevenwicht`

## Read-First Evidence

Read and use these as sprint authority:

- `lesson-ticket-L-CP6A-book1-chapter13-v5-alignment.md`
- `lessen-team-roadmap.md`
- `course_blueprint_v5.md`
- `../4veco-platform/AGENTS.md`
- `../4veco-platform/BUILD-CHAPTER.md`
- `../4veco-platform/BUILD-PARAGRAPH.md`
- `../4veco-platform/build-scripts/README.md`
- `../4veco-platform/reports/sprints/CP.6a-result.md`
- `../4veco-platform/reports/reference-planning/CP.6a-lesson-side-alignment.md`
- `../4veco-platform/references/data/sprints/CP.6a-lesson-side-alignment.json`
- `../4veco-platform/reports/review-gates/GATE-CP6-year-1-paragraph-coverage/human-interview.md`
- `../4veco-platform/references/reference-team-roadmap.md`

## Baseline Finding

- Chapter folders and chapter-level markdown still expose old Book 1 slots:
  `1.3.2 Kostenstructuren` and `1.3.3 Opbrengsten`.
- The Book 1 print manifest already composes a v5 print chapter from
  `1.4.1 Marktevenwicht` and `1.4.2 Verschuivingen`, but that print-only
  composition is not sufficient for online/chapter-source alignment.
- Current `1.4.1` and `1.4.2` reviews are `PASS WITH FLAGS`; these flags must
  be fixed or explicitly carried in the migrated `1.3.2` and `1.3.3` records.
- Costs and revenue material must survive as parked/future Book 2 material, not
  remain as active Book 1 `1.3.2` / `1.3.3` coverage.

## Operating Rule

Generated lesson output must not be hand-patched. The remediation will be
implemented through a platform-owned script that performs the move/renumber,
content fixes, survival archiving, chapter assembly, and book rebuild steps in a
repeatable way. Direct manual edits in the lesson repo are limited to sprint
plans, review/closure records, and roadmap bookkeeping.

## Implementation Phases

### Phase 1 - Platform Remediation Script

Create a platform sprint script, tentatively:

`../4veco-platform/build-scripts/sprints/l-cp6a-remediate-book1-chapter13.js`

The script must:

- verify the expected stale baseline before mutating lesson files;
- archive displaced `1.3.2 Kostenstructuren` and `1.3.3 Opbrengsten` under
  `archive/sprints/L-CP6A/displaced-book2-material/`;
- record their v5 survival destinations:
  - `1.3.2 Kostenstructuren` -> `2.1.1 Kostenstructuren`;
  - `1.3.3 Opbrengsten` -> `2.1.2 Opbrengsten, winst en break-even`;
- create/update the active Chapter 1.3 folder as
  `1.3 Hoofdstuk Aanbod en marktevenwicht`;
- copy/migrate source material from:
  - `1.4.1 Marktevenwicht` -> `1.3.2 Marktevenwicht`;
  - `1.4.2 Verschuivingen` -> `1.3.3 Verschuivingen en nieuw evenwicht`;
- renumber file names, markdown headings, internal references, footer labels,
  asset file names, image references, quality refs, and review files from
  `1.4.1`/`1.4.2` to `1.3.2`/`1.3.3`;
- keep original `1.4` material reachable as historical/parked material, but not
  counted as active Book 1 Chapter 1.3 coverage.

### Phase 2 - Content Corrections

The script or an explicit platform-owned content step must fix or carry the
known flags:

- `1.3.2 Marktevenwicht`:
  - add short start hints for early exercises or explicitly carry this as a
    non-blocking scaffold flag;
  - remove ambiguity from the electric-bicycle subsidy question by specifying
    whether the subsidy is for consumers or producers;
  - record that duplicated exercises in `paragraaf.md` and `opgaven.md` are a
    current Part A pattern unless this sprint removes the duplication.
- `1.3.3 Verschuivingen en nieuw evenwicht`:
  - correct the forward reference so it points to `1.3.4 Gemengde opgaven`;
  - remove cost/revenue exercise material that relies on old Book 1 `1.3.2`
    costs coverage;
  - fix the old exercise 8e ambiguity by making the question match the actual
    price/quantity effect, or record a clear carried flag if it cannot be fixed
    safely in this sprint;
  - preserve duplicated-exercise status honestly.
- `1.3.4 Gemengde opgaven`:
  - scope to supply, demand, equilibrium, and shifts;
  - exclude costs/revenue/break-even theory from active Book 1 consolidation.

### Phase 3 - Chapter and Book Regeneration

Regenerate through the existing platform/authorized chapter workflow:

- update `build_chapter.py` for the v5 Chapter 1.3 structure;
- regenerate:
  - `1.3 Aanbod en marktevenwicht - hoofdstuk.md/html/pdf`;
  - `1.3 Aanbod en marktevenwicht - antwoorden.md/html/pdf`;
  - Book 1 aggregate `boek.md/html/pdf`;
  - any chapter/book `_assets` affected by renumbering;
  - landing/navigation surfaces if they still expose stale chapter/paragraph
    names.

Do not generate or alter companion game/web surfaces unless the chapter
remediation actually touches them. If companion surfaces are touched, add the
deploy/link/data/screenshot QA required by the platform workflow.

### Phase 4 - Review and Quality Records

Create or update lesson records:

- `L-CP6A-survival-map.md`
- `L-CP6A-remediation-report.md`
- `L-CP6A-technical-qa-report.md`
- `L-CP6A-closure-log.md`
- `L-CP6A-handoff-to-references.md`
- `1.3.2-quality-ref.yaml`
- `1.3.2-review.md`
- `1.3.3-quality-ref.yaml`
- `1.3.3-review.md`
- `1.3.4-quality-ref.yaml`
- `1.3.4-review.md`

The review/quality records must state whether each inherited flag is fixed or
carried. They must not mark target exercises `reviewed_final`, close CP-6, or
close Year 1.

### Phase 5 - Validation

Run from `../4veco-platform` unless otherwise noted:

```powershell
node scripts/check-book.js --paragraph-mode part-a --paragraph-profile publisher-print "../4veco-lessen/Boek 1 - Grondslagen, vraag en aanbod"
node scripts/check-course-target-exercises-v5.js
node scripts/validate-chapter.js "../4veco-lessen/Boek 1 - Grondslagen, vraag en aanbod/1.3 Hoofdstuk Aanbod en marktevenwicht"
python build-scripts/books/build-book.py --book 1
node scripts/check-book-print-scope.js "../4veco-lessen/Boek 1 - Grondslagen, vraag en aanbod"
npm.cmd run agent:index
```

Add paragraph-level validators for `1.3.2`, `1.3.3`, and `1.3.4` after their
final folder paths are known. If web companion surfaces are touched, run
`scripts/deploy.js`, `scripts/check-links.js`, data checks, and screenshot QA.

## Acceptance Criteria

- Active Chapter 1.3 no longer contains `1.3.2 Kostenstructuren` or
  `1.3.3 Opbrengsten` as Book 1 paragraph folders, chapter-plan entries,
  chapter markdown headings, navigation entries, or quality-ready records.
- Chapter 1.3 consistently presents `1.3.2 Marktevenwicht` and
  `1.3.3 Verschuivingen en nieuw evenwicht` across folders, filenames,
  markdown, PDFs, chapter assembly, Book 1 aggregate, navigation, reviews, and
  quality refs.
- `1.3.4 Gemengde opgaven` is scoped to supply, demand, equilibrium, and
  shifts, with no hidden costs/revenue theory reintroduced into Book 1.
- Displaced costs/revenue material has a visible survival route for Book 2.
- Validation commands and generated file lists are recorded in the closure log.
- Handoff to references includes lesson commit SHA, platform commit SHA,
  changed/generated file list, validation evidence, review/quality-ref paths,
  and an explicit CP.6a mismatch status.

## Stop Conditions

Stop and report instead of forcing closure if:

- the remediation would require manual generated-output edits not owned by a
  platform script or existing platform workflow;
- costs/revenue would remain active Book 1 `1.3.2` / `1.3.3` coverage;
- inherited `1.4.1` / `1.4.2` flags cannot be fixed or honestly carried;
- any artifact would claim CP-6 closure, Year 1 closure, target-exercise
  promotion, placeholder finalization, protected reference mutation, or unit
  minting;
- validation fails and the fix would expand into Book 2 production, adaptive
  behavior, diagnostics, mastery, sequencing, student-facing AI, summative use,
  PV projection, or PV machine promotion.
