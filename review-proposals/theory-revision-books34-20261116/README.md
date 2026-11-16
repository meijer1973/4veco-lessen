# Review proposal: revised theory explanations, Books 3 and 4

**Date:** 16 November 2026
**Basis:** lessons `01ebd47`, platform `82e6cb3f`; edition `edities/books34-v3`.
**Status:** proposal for review. The governed edition under `edities/books34-v3` is not changed by this folder. Not for merge as it stands.

## What this is

The owner asked for better theory explanations in Books 3 and 4 without extra pages, without touching the exercises and without changing the layout. This folder holds the result for review: revised student books, the edited manuscripts and the exact text differences.

| | Book 3 | Book 4 |
|---|---|---|
| Pages in the complete student book | 132 (unchanged) | 166 (unchanged) |
| Pages with changed text | 38 | 18 |
| Theory paragraphs edited | 11 of 11 | 11 of 14 |
| Kind of revision | Rewrite of the explanation pages | 22 targeted edits |
| Example numbers changed | One table (§3.2.2, p. 62) | None |
| *Onthouden* boxes changed | 2 | 5 |
| Lesdoelen changed | None | None |
| Exercises changed | None (byte-identical) | None (byte-identical) |

Book 4's theory was already stronger than Book 3's, which is why its revision is smaller.

## How to review

1. Open `boek-3/Boek_3_theorie_voor-en-na.pdf` and `boek-4/Boek_4_theorie_voor-en-na.pdf`. Each spread shows the current page on the left and the revised page on the right, for changed pages only.
2. Read `boek-3/OVERZICHT-WIJZIGINGEN.md` and `boek-4/OVERZICHT-WIJZIGINGEN.md` for what changed per paragraph and why.
3. Use `theorie-wijzigingen.diff` in each folder for the exact wording.
4. The complete revised books are `Boek_3_Compleet_v3_theorie-herzien.pdf` and `Boek_4_Compleet_v3_theorie-herzien.pdf`.

Two places deserve a second pair of eyes:

- **Book 3, §3.2.2, p. 62.** The table was replaced by one that shrinks the step towards q = 60. This is the only place where example numbers changed.
- **Book 4, §4.1.1, p. 8.** One explanation was corrected: a price taker sells less after entry because the price fell, not because there are more firms.

## What stayed the same

- Every exercise section, from *Startopgaven* onward, is byte-identical to the current manuscripts.
- All figures, their numbers, captions and pages; all Lesdoelen.
- Page counts, page numbers, outlines and internal links of both complete books.
- Stylesheet, fonts and components.

## How it was built and checked

- Built in a scratch copy of the edition with the pinned renderer (WeasyPrint 68.0, PyMuPDF 1.26.7, Lato and DejaVu fonts) and the platform's current assembler, `build-scripts/books/books34_followups_assemble.py`.
- Before any edit, the unchanged sources reproduced the repository PDFs: all 120 Book 3 chapter pages and all 166 pages of the complete Book 4 were pixel-identical.
- After the edits: no overflow in any chapter; against the accepted complete books the outline and links are identical and the text differs on exactly the pages listed in the overviews.
- Every changed page was inspected as rendered.

## What is not done

- **No independent review.** The revision and the checks were done by one agent; no teacher or second reader has looked at the text.
- **Not integrated.** Chapter and paragraph PDFs, complete books, page maps and target-record source hashes in the edition still belong to the current text. Adopting this proposal needs a new revision record in the platform repository and a full dependent rebuild.
- **Presentations not checked.** Classroom presentations that quote theory wording were not compared with the new text.
- **Six untouched Book 3 pages differ by a hair.** On pages 26, 28, 29, 30, 42 and 52 a few words sit 0.011 pt further left. The text is identical and the shift is not visible; the October maintenance note records the same renderer effect on p. 124.

## Adopting the proposal later

The edited manuscripts are in `boek-3/manuscripten/` and `boek-4/manuscripten/`, under the same chapter and file names as in `edities/books34-v3/books/book-N/chapters/`. Copy them over the current manuscripts only as part of a governed successor revision.
