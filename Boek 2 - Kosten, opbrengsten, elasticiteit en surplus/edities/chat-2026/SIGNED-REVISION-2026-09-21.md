# Book 2: current native theory and printed pagination

Edit student text in `bronnen/H*/manuscript/*.md`, answers and teacher guidance
in the chapter-root authored Markdown, and bounded figures in
`bronnen/H*/_assets/theory-20260921/page-NNN.json`. Generated HTML, chapter PDFs,
paragraph exports and manifests are not editable sources. Package PDFs and old
chapter-root builders remain historical evidence, not current build inputs.

The owning [platform build guide](https://github.com/meijer1973/4veco-platform/blob/codex/book2-theory-signed-20260921/build-scripts/books/BOOK2-SIGNED.md)
contains the current commands, validation and source-ownership rules. Locally,
read `build-scripts/books/BOOK2-SIGNED.md` in the adjacent platform worktree.
Use its complete `rebuild_book2_signed.py --all` path after manuscript changes;
assembly alone rejects stale source records. Review a changed revision inventory
and platform pin before publication.

The cover and contents are unnumbered. Printed numbering then runs continuously
through each book: students 1–108, answers 1–55, teacher material 1–17.
`print-pagination.json` defines this convention. Chapter and paragraph exports
retain the book numbers. Main/chapter contents, compact navigation labels,
reference tables and teacher references use these numbers. Physical PDF pages
remain separate machine identifiers in `signed-page-map.json`; its `printed_page`
field supplies the reader-facing number. Complete PDF viewer labels agree.

The complete PDFs still contain 110/57/19 physical pages. The 43-page reading
extract in `boek/Boek_2_Theorie_43_Herziene_Paginas.pdf` is generated from the
current complete student book. Its adjacent JSON records the source and output
hashes plus extraction, physical and printed page numbers and manuscript hashes.
Use the complete book for clickable navigation; the extract preserves printed
book numbers without unresolved links. Distribute paragraph folders together
because external paragraph links use relative chapter paths.

The canonical signed-elasticity policy is the platform precision reference §15.
The normal guided route and §2.2.4 Hoofdstukcheck 7 label remain intact. No exercise
content, learning goals, numbering or point/status fields change with pagination.
Historical import/repair/route receipts remain unchanged. Current evidence is in
the [portable print-review record](https://github.com/meijer1973/4veco-platform/blob/codex/book2-theory-signed-20260921/reports/review-gates/book2-print-review-20260921/README.md).

The 34 complete-route timing budgets across Books 2–4, active Books 3/4 signed
retrieval alignment and Books 3/4 NAV1 chapter-contents links remain separate
named follow-ups. No 55-minute fit or lifecycle release is claimed. Part B is
unchanged. PDF byte hashes depend on the build environment; compare text,
geometry and rendered pages as well as hashes.
