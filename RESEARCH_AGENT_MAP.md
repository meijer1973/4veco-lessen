# Repository map — 4veco Lessons

Use this lookup for lesson locations and their relationships.
[AGENTS.md](AGENTS.md) supplies the shared operating-guide route;
[GitHub access](AGENT_GITHUB_ENTRY.md) covers remote files and rendered pages.
Inspect only the areas relevant to the question.

## Locations

| Looking for | Location or relationship |
|---|---|
| Exact current artifact paths | [Generated lesson inventory](https://github.com/meijer1973/4veco-platform/blob/main/reports/github-agent-current-lessen.md). Confirm at the investigated commit; the inventory is a snapshot. |
| Literal file URLs or complete machine inventory | [URL index](https://raw.githubusercontent.com/meijer1973/4veco-platform/main/reports/url-index.md), [complete lesson index](https://github.com/meijer1973/4veco-platform/blob/main/reports/github-agent-index-lessen.json) |
| Student entry | [index.html](index.html) → book → chapter → paragraph landing pages |
| Active curriculum baseline | [course_blueprint_v5.md](course_blueprint_v5.md); platform owns subsequent curriculum authority and Book 2's current outline/holds. |
| Book 2 default delivered print edition | [Student book, answers, teacher guide, chapters and editable sources](Boek%202%20-%20Kosten%2C%20opbrengsten%2C%20elasticiteit%20en%20surplus/README.md) — chat edition 2026; [older paragraph trees are archived](archive/book-2-pre-chat-2026/README.md) with their own history. |
| Book 2 planning and approved use | [Platform Part A checklist](https://github.com/meijer1973/4veco-platform/blob/main/docs/workflows/part-a-start.md) → [canonical outline](https://github.com/meijer1973/4veco-platform/blob/main/references/authored/book-outlines/book-2-outline.md) and its current metadata |
| Product direction or route acceptance | [Vision](specifications/product-vision.md), [end state](specifications/product-end-state.md), [companion specification](specifications/companion-core-specifications.md) |
| Sprint state or an outstanding obligation | [Lesson roadmap](lessen-team-roadmap.md); read the relevant section and its evidence. Roadmap prose does not establish artifact existence or current review. |
| Build source, engine, skill or validator | [Platform map](https://github.com/meijer1973/4veco-platform/blob/main/RESEARCH_AGENT_MAP.md). Local checkout: `../4veco-platform/`. |
| Historical decision or regression | [Archive navigation](archive/README.md). Book 1 output remains frozen; examples are not authorization to retrofit it. |

## Artifact relationships

Discover exact names from the inventory or directory listing before constructing
a path. Book/chapter/paragraph folders contain their identifier and Dutch title.
Artifact names commonly use ` – ` (space, en dash U+2013, space), not a hyphen.

| Layer | What to inspect |
|---|---|
| Book | `Boek N - <title>/`: deploy configuration, landing page, assembled book and shared runtime/data. |
| Chapter | `N.M Hoofdstuk <title>/`: chapter plan, `build_chapter.py`, assembled chapter and answers. |
| Paragraph Part A | `N.M.K <title>/`: `– paragraaf`, `– opgaven`, `– antwoorden` sources and HTML/PDF outputs; `build_pdf.py`, textbook plan, foundation, snapshot, review and handoff. |
| Paragraph Part B | The same paragraph folder: landing/route HTML, games, presentation and companion plan/review; game data under book `shared/`. Artifact families depend on the assigned paragraph type/profile. |
| Assets | Paragraph `_assets/` and optional source `svg/`; chapter/book asset copies derive from paragraph assets. |
| Consolidation or test preparation | Type-specific names such as `samenvatting`, `toets` and `toetsmatrijs`; inspect the platform [paragraph-type contract](https://github.com/meijer1973/4veco-platform/blob/main/scripts/lib/paragraph-types.js). |
| Review | `N.M.K-quality-ref.yaml` and lane-specific review/snapshot records. [Part A review](https://github.com/meijer1973/4veco-platform/blob/main/docs/workflows/part-a-review.md) explains current evidence and unchanged-edition reproduction. |

## Tracing evidence

Paragraph source → platform renderer/thin wrapper → paragraph HTML/PDF →
chapter/book assembly. A source correction may leave older assembled output
stale; inspect the resulting files when judging the student experience.

Platform engines → lesson `shared/` copies → companion pages and data.
Trace behavior problems back to the owning platform source.

Plans describe intent; generated files show the last build; a review attests
only its named scope and committed/snapshotted inputs. Existence alone does not
prove review or completeness. A missing optional companion is not automatically
a defect in a textbook-only assignment.
## Selected Books 3 and 4

- Book 3: [complete PDFs, chapters and all editable sources](Boek%203%20-%20Overheidsingrijpen%2C%20concurrentie%20en%20internationale%20handel/README.md); [current outline adoption](https://github.com/meijer1973/4veco-platform/blob/codex/import-books34-outlines-20260914/references/authored/book-outlines/book-3-outline.meta.json).
- Book 4: [complete PDFs, chapters and all editable sources](Boek%204%20-%20Monopolie%2C%20marktfalen%20en%20arbeidsmarkt/README.md); [current outline adoption](https://github.com/meijer1973/4veco-platform/blob/codex/import-books34-outlines-20260914/references/authored/book-outlines/book-4-outline.meta.json).

Current lookup: platform `node build-scripts/references/books34-selected-structure.js 3.3.1`. Validation: `node build-scripts/maintenance/check-books34-chat-import.js --require-paired --require-tracked`. Numeric IDs require revision `book34-chat-v2-20260914`; archive IDs do not transfer target approval. Integration is prepared/in PR.
