# Book 2 report repair — independent review

## 1. Scope and current inputs

Reviewed on 2026-09-20 by `/root/review_book2`, independently of repair author `/root`. This record covers report B2-01 through B2-04, their assembly mechanism, and the two small contents-page improvements also named in the report. It does not establish full paragraph, curriculum, or classroom acceptance.

Baseline: lessons `1056488b67b16c14cc83557a8b8497e2b9985370`; platform `9f25adf07641a30ddeb27706f12e32434f581275`. Reused evidence: the supplied 2026-09-18 report's review of unchanged chapters, plus direct baseline confirmation recorded in `baseline-review.md`. The report was treated as evidence; the user's request and shared repository instructions determined the task.

Applied platform `AGENTS.md`, `BUILD-CHAPTER.md`, `docs/workflows/part-a-review.md`, `skills/econ-paragraph-review.md`, `skills/economic-graph.md`, `references/authored/economic_mathematical_precision_reference.md`, `textbook-rendered-page-acceptance-standard.md`, and `textbook-figure-standard.md`. This is an existing edition assembly repair, not new paragraph closure, so no historical paragraph review was relabelled or bound retrospectively.

Review manifest SHA256: `406fca18fac77d334c6824c2291ff6a7c761a1be82cc58c5ba7ea478507883f2`

The bound file is the edition's new `repair-manifest.json`. It identifies current assembly data, background, generated shared cover PNG, and three complete PDFs. Original delivery and chapter records retain historical meaning. The following reviewed platform source hashes provide the builder binding absent from the lesson-only manifest:

| Platform file | SHA256 |
|---|---|
| `build-scripts/books/build_book2_chat.py` | `5b69176506090783f90479a1313ad8b022b19bfbbed558b94ef722fe9bef2b58` |
| `build-scripts/books/verify_book2_chat.py` | `ae62dd965815a7ed10d57101c6034de715f460f262887c74789553439475c550` |
| `build-scripts/books/test_book2_chat.py` | `526ecf4f5b85035aa473a09d4cd7b396070fb6290c8bee400473f1e18bbb6de0` |
| `build-scripts/books/requirements-book2-chat.txt` | `e18ec39506a9295ab460c467bb053b0c00631e68d70393733e466419c8219b23` |

## 2. Verdict

PASS for the bounded report repair and inspected assembly. No unresolved actionable findings.

This verdict applies only to the file identities above. It is not a new paragraph PASS or permission to publish, deploy, merge, or make curriculum/product-use claims. Subsequent substantive code, cover, assembly-data or output changes require a focused recheck.

## 3. Findings and repair disposition

| Finding | Independently checked result | Disposition |
|---|---|---|
| B2-01 duplicate overview destination | Actual final annotation objects: all four overview rectangles on student PDF p37 target p72; all five on p73 target p109. Named destinations are `h2-overzicht` and `h3-overzicht`. Other chapter and answer navigation remains local to its chapter. | Closed; `blocks: false` |
| B2-02 PS area and label | Actual final vectors form a triangle above supply, below P*, and left of Q*. PS label lies inside; area below supply is neutral. CS remains below demand and above P*. Identical repaired cover appears in all three bundles. | Closed; `blocks: false` |
| B2-03 TKG/GTK | Cover table uses GTK and unit €/stuk. Plot contains only TK/TO on a total-euro axis, so average and total units are no longer mixed. | Closed; `blocks: false` |
| B2-04 incompatible table/graph | Formula, table, line geometry, intercepts, and break-even point agree; independent arithmetic and final vector coordinates documented below. | Closed; `blocks: false` |
| Contents-page improvements | Student paragraph titles agree with the edition paragraph exports. All three contents pages say PDF-pagina and explain that printed page numbers restart by chapter. Starts remain student 3/37/73, answers 3/23/41, teacher 3/8/14. | Closed; `blocks: false` |

No proof remains required to close these findings. The original chapter content/exercises were not rewritten; no unrelated exercise or teaching-content acceptance is claimed.

## 4. Economics and actual drawing proof

Independently recomputed TK=500+10Q and TO=20Q. For Q=0/50/100/150, TK is 500/1000/1500/2000, TO is 0/1000/2000/3000, W is −500/0/500/1000, and GTK is undefined/20/15/13.33 after rounding to cents. Every printed cell agrees. Visible Q axis uses stuks, total axis uses euro totaal, and average units are explicit in the table.

Read the final PDF drawing commands through PyMuPDF, independently of the builder's returned values. In the 1055×1491 design coordinates, orange TK runs from (94,715) to (304,625); purple TO runs from (94,745) to (304,565). With the visible scales, these are exactly the model endpoints. The black break-even marker is centered at (164,685), equivalent to Q=50 and total value €1000.

The conceptual market uses P_v=18−Q and P_a=2+Q, giving Q*=8 and P*=10. Actual PDF demand endpoints are (727,565)/(982,775), supply endpoints (727,789)/(982,579), intersection marker (863,677), and dashed guides (727,677)→(863,677)→(863,817). The actual CS polygon is (727,565)/(727,677)/(863,677); PS is (727,789)/(727,677)/(863,677). These give the proper areas. Label bounding boxes lie in their respective regions, and curves are directly identified without relying on colour alone.

The central raster elasticity panel was checked visually against the original cover: price +10% with quantity −20%, price −10% with quantity +5%, E_p=%ΔQ_v/%ΔP, |E_p|>1 elastisch and |E_p|<1 inelastisch remain intact. These examples imply −2 and−0.5, respectively. No new contradictory economics was introduced.

## 5. Final rendered-page, teacher and student coverage

Personally inspected full-page Poppler PNGs at normal reading scale, not just cropped figures or source files. All three covers and all three contents pages were inspected, plus student PDF pp37,72,73,109 (the affected link openings and endpoints). Files are under `C:/wt/book 2/review/rendered/`; exact proof-file hashes are in `independent-evidence.json`.

Changed page proofs: `student-001.png`, `student-002.png`, `answers-01.png`, `answers-02.png`, `teacher-01.png`, `teacher-02.png`. Link-page proofs: `student-link37-037.png`, `student-link72-072.png`, `student-link73-073.png`, `student-link109-109.png`.

No clipped text, overlapping labels, table overflow, missing/blank pages, missing images, broken glyphs, incorrect numeric cells or stale plots were observed. The cost table and axes remain readable at full-page scale. The contents headings and descriptions fit their panels. No page reflow occurs in the chapter bodies.

Teacher perspective: the cover no longer conflicts with the taught surplus definition, and the corrected overview link reaches the intended chapter recap. Chapter, answer and teacher page starts remain stable, so existing lesson references still work. No goal, exercise, worked answer or prerequisite changed.

Typical student perspective: quantity and euro units distinguish the two representations; GTK has the same abbreviation as the book; the PS label sits in the area it names. The PDF-page explanation makes the reset printed pagination understandable. A student using either overview hyperlink arrives at that chapter's overview. No extra online step or hidden teacher explanation was introduced.

## 6. Executed checks and warnings

Executed independently from the platform worktree with `C:/Python314/python.exe`:

- `build-scripts/books/verify_book2_chat.py` — exit 0; 455 unchanged delivered files match their historical hashes, all 180 chapter pages preserve exact text and identical 72 dpi rasters, all 105 link annotations retain their rectangles and semantic targets/view coordinates, bundle page counts 110/57/19, cover geometry PASS.
- `-m unittest discover -s build-scripts/books -p test_book2_chat.py -v` — exit 0; all 3 tests pass, covering duplicate names with both /Dest and /A /GoTo, unresolved names, and external actions.
- Separate pypdf read of final annotation objects confirms the H2/H3 overview targets for every clickable rectangle. Separate Git-blob read of original contents pages confirms they had no clickable annotations to preserve.
- Full-page Poppler renders completed successfully for the 10 inspected pages.

Warnings investigated:

1. pypdf 6.13.2 emits `Annotation sizes differ: N vs. 0` during append. Its `_writer.py` first clones pages excluding /Annots (line 2757), which triggers `generic/_link.py`'s intermediate comparison, then reinserts filtered annotations (line 2799). Final files retain every checked annotation with the proper target. Non-blocking for the reviewed files; do not suppress future verification failures on that basis.
2. Poppler emitted display-font lookup warnings for Symbol/ArialUnicode. The final rendered pages show correct euro symbols, arrows, minus signs, Greek notation and other inspected glyphs. Non-blocking for these proofs.

The assembly code fixes the owning merge mechanism, validates original chapter-byte identities, preserves explicit view coordinates, and derives both graph and table from editable data. The chapter-local source anchors and PDFs already worked independently and remain untouched. New code is deliberately edition-specific, not evidence for arbitrary future inputs.


## 7. Supplemental closure review: lane ownership and documentation

Reviewed the subsequent bounded lane-checker change, its regression test, platform `build-scripts/books/BOOK2-CHAT.md`, and lesson `CORRECTIES-2026-09-20.md`. PASS; no actionable findings remain. The documents accurately describe the delivered chapter inputs, new source-based assembly, corrected economics, verification, and limits of historical versus current evidence.

The classifier adds only 11 exact filenames under the exact Book 2 chat-2026 edition prefix. This accurately assigns Part A ownership to its assembly and review artifacts; it does not grant content acceptance, relax an unknown-file failure, or exempt the whole edition. Existing companion classification precedes Part A classification. The original delivery manifest, unknown PDFs, unrelated runtime files, nested assembly files and another edition remain outside this new classification.

Independently executed direct Node assertions: all 11 exact paths classify as Part A; they pass textbook scope and fail companion scope; unknown, nested, suffix and sibling-edition variants remain unknown; genuine `2.2.1 - korte-check.html` and `index.html` remain Part B and fail textbook scope. The initial test used a bare short-check filename that was unknown under existing suffix rules. The author corrected it to the genuine Part B path and added the explicit category assertion; this precision issue is resolved. The independent Jest invocation `node node_modules/jest/bin/jest.js build-scripts/workflows/check-paragraph-lane-scope.test.js --runInBand` completed with exit 0: 1 suite, 26 tests passed.

| Additional reviewed file | SHA256 |
|---|---|
| Platform `build-scripts/workflows/check-paragraph-lane-scope.js` | `f6ac31ac7b337ef73e2a4b5b1aa71bf1bc874373c7992597cdce48ff6df9d610` |
| Platform `build-scripts/workflows/check-paragraph-lane-scope.test.js` | `ba9613f2539a3fd825041ddaaf2feb1253fc680ca47fadd62ce808bdf35efa8c` |
| Platform `build-scripts/books/BOOK2-CHAT.md` | `f9d3295748ab1085916fcb8ba741bf5841acd7c96cbfaa45dc5b19c550d0b64b` |
| Lesson edition `CORRECTIES-2026-09-20.md` | `383fc1d531f7a96e9a96c16d1d025865ac0772242451cdaf4ee96bfda9c7dfa7` |

The builder subsequently received only an explicit `newline="\n"` argument for manifest writing. Its current hash appears in section 1. The manifest now uses LF and has the current single binding above. Independently confirmed that replacing its LF with CRLF reproduces the previous reviewed SHA256 `246c4d35bf662ca4b4511ee9968f56eebe92b86fa7ca5c7abfa6034e8208375d` exactly. All six bound input/output hashes are unchanged, including the three PDFs and cover PNG, so the rendered proofs and substantive findings remain current. This record and the accompanying evidence JSON are written with LF.
