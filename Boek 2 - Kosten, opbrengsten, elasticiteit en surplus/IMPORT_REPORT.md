# BOOK2-CHAT-IMPORT-1 — technical import record

Date: 2026-09-14 (initial import 2026-09-13). Status: **writing/assembly complete; import and archive cleanup in PR**. This is an initial import of the owner-selected external edition, not reproduction of an edition previously committed here. No new formal content review, target approval, classroom validation or companion/product closure is claimed. Issues #223/#229 and remaining holds are unchanged.

## Delivery and placement

`Boek_2_Repository_Integratiepakket.zip` → `uitgave/` → [`edities/chat-2026/`](edities/chat-2026/README.md), preserving the entire directory tree. No previous edition was overwritten. ZIP SHA-256: `8dc9c18d19ca40d175da579bbc1c35f8d390ff659285af1051b7bbb8a477dd7b`.

All **463** supplied edition files are retained, including 459 original files listed by `delivery-manifest.json` and the four package navigation/integrity files. Original PDFs, cover, Markdown, assets, numbering and layout are unchanged. Edition-scoped `.gitattributes` disables newline normalization while keeping text files searchable and diffable. Existing repository chapter trees and their evidence remain intact.

## Technical checks

- Supplied `verify_files.py`: PASS before copying and at the final edition location; all 459 manifest-listed files match original size/SHA-256.
- Independent comparison of all 463 package files against staged Git blobs: PASS, byte-for-byte, including the four package files outside the manifest.
- All twelve book/chapter PDFs opened with `pypdf` in strict mode; every page content stream is readable. Page counts match the delivery table below.
- Poppler rendered one representative full page from each delivery PDF. Visual inspection found no corruption, missing material or clipping in this sample. Book sample pages: student 1 (cover), answers 5, teacher 5. Chapter sample pages: 5 for each PDF except H3 student page 30. This is a limited integrity sample, not a line-by-line content audit.
- All 18 ordered manuscript files (six per chapter), all twelve paragraph folders and 202 local Markdown figure references are present. Manuscript `_assets/` paths resolve through the chapter-root convention used by the supplied builders. Root/edition README navigation and source-index links resolve.
- One independent technical review of import configuration, navigation and roadmap changes found no substantive defect. Its minor stale roadmap phrase was corrected. It did not review pedagogical/economic content or confer formal approval.
- New integration/navigation prose passes diff hygiene. Whole-import `git diff --check` reports only six inherited blank-at-EOF warnings in H1/H2 derived paragraph answer exports. They remain unchanged to preserve the supplied edition; no global whitespace checks were weakened.

| PDF group | Student | Answers | Teacher guide |
|---|---:|---:|---:|
| Complete book | 110 | 57 | 19 |
| H1 / 2.1 | 34 | 20 | 5 |
| H2 / 2.2 | 36 | 18 | 6 |
| H3 / 2.3 | 38 | 17 | 6 |

## Repository checks and publication

The platform roadmap-version check passes. Generated navigation/dashboard inventories are refreshed through existing platform tools. The linked lesson/platform PRs carry actual commits, scope-check results and remote CI; required platform CI validates platform with lesson main and must not be described as proof of an unmerged lesson head. The local package/Git/PDF/source checks above cover this edition directly. No new generic import framework or CI workflow was added.

**Original workflow conflict (retained):** at lesson head `418a0e2bf149675b78c1f7fe15e6054ddaab51f9`, the existing `check-paragraph-lane-scope.js --lane textbook` reported 310 Part A paths, zero companion paths, 156 unknown paths and the edition-preservation `.gitattributes` rule as a shared-file change. Its exception mechanism cannot classify unknown paths. That result remains a failure, not a paragraph-scope PASS.

## Task-specific applicability decision and archival continuation

The owner's technical review/continuation request authorizes this explicit operation: unchanged external-edition import plus two hash-preserving archive moves. This is not ordinary paragraph authoring or a third content lane. The maintenance guide does not automatically exempt new student-facing material; the historical-reproduction route did not cover this first import. The owner's finite import/archive decision supplies the applicable scope here, with required repository CI and independent technical review retained.

The explicit replacement scope verification is platform [`build-scripts/maintenance/check-book2-chat-import.js`](https://github.com/meijer1973/4veco-platform/blob/codex/import-book2-chat-20260913/build-scripts/maintenance/check-book2-chat-import.js). It reads both declared final commits, requires clean matching checkouts, compares the full PR diffs to enumerated paths, checks the imported and archived Git trees, requires exact per-file relocation records, retains the reviewed `.gitattributes` blob and checks current navigation links. Its tests reject modified/missing delivery files, non-preserving archive moves, unrelated files, altered relocation evidence, recreated active trees and changed preservation attributes. It does not suppress or modify ordinary paragraph validation, claim full paragraph/content validation, or grant merge authority.

The finite boundary is:

1. The 463-file edition at tree `909aa0d98e808512da7c7355a328eadf99b8e65b`.
2. The two old chapter trees, moved from the Book 2 root to [`archive/book-2-pre-chat-2026/`](../archive/book-2-pre-chat-2026/README.md): Chapter 2.1 tree `93ad9730baa7743513929040d91a07d93c5baafa`, Chapter 2.2 tree `d6a2aa9d87971469205c1ca302c8890d3e88ca6f`. All 144 files retain their bytes and modes from lesson commit `3e63e82cd335405f383cd76f13b51b774b8b0571`. No unique lesson material was deleted. The explanatory README is outside those trees.
3. Lesson `.gitattributes` (exact reviewed blob only), Book 2 README/import record, repository map, lesson roadmap, archive README/relocations/indexes; platform textbook roadmap/ledger/version index, generated lesson inventories and internal dashboard.
4. Only the named task-specific checker and its tests. No shared renderer, target registry, global classifier or CI workflow changes.

The archive uses existing per-file relocation metadata and the existing archive-index generator. Historical regression readers may use `build-scripts/lib/historical-paths.js` with the registered originals; original-commit links preserve historical document context. Current download/source discovery resolves to the chat edition and all twelve paragraph exports. Active consumer/test searches found no production reader needing the old active chapter paths: generic paragraph/chapter tests use constructed fixtures, while the named old MTU readiness checker pins its own historical lesson/index commit and is not evidence for this edition. The final-pair local suite and archive checks verify affected behavior without substituting the chat edition into those historical fixtures.

Run from the platform checkout after committing both repositories:

```powershell
node build-scripts/maintenance/check-book2-chat-import.js --platform-head <full-platform-SHA> --lesson-head <full-lesson-SHA>
node build-scripts/maintenance/check-archive-cleanup.js --require-paired
npm.cmd test -- --maxWorkers=2
```

The PR verification record gives the actual final SHAs and results. Required hosted platform CI still checks lesson main; the explicit local run checks the named final pair. Mark the existing PRs ready only after preservation, scope, affected tests, required CI and the independent technical review are complete. No new textbook page review is requested.

Paired worktrees: `C:/wt/book integration/4veco-lessen` and `C:/wt/book integration/4veco-platform`. Both use `codex/import-book2-chat-20260913`, owner `codex-book2-import`, task `BOOK2-CHAT-IMPORT-1`. Baselines: lessons `0acaaa97443e5c4fee34f7da8a12ccd5db62d762`; platform `85b0f347f3070e005eae3f35f0b11ce6eac71b4d`. Governance freshness and both worktree ownership preflights passed.

Platform [textbook roadmap](https://github.com/meijer1973/4veco-platform/blob/main/docs/roadmaps/textbook/textbook-production-roadmap.md), its sprint ledger/version index, and the [lesson roadmap](../lessen-team-roadmap.md) distinguish completed writing/assembly from repository integration. Fresh H2/H3 production and book assembly are superseded. Platform [PR #231](https://github.com/meijer1973/4veco-platform/pull/231) is confirmed merged on 2026-09-05 at `96416b6b5bd57094576e9aba0a42d682584ec479`; its activation is not repeated.

Next action: review the linked PRs and their CI. Record **integrated on main** only after an explicitly authorized merge, with the actual commit/link. This task does not authorize automatic merge or branch-protection bypass.
