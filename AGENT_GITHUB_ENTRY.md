# GitHub access — 4veco Lessons

Start with [AGENTS.md](AGENTS.md), then the assignment's relevant files.
Use the [lesson map](RESEARCH_AGENT_MAP.md) to find unfamiliar locations.
The platform map is useful when tracing build logic; neither map requires
reading product specifications or the roadmap before an unrelated lookup.

- Repository: [4veco-lessen](https://github.com/meijer1973/4veco-lessen).
- Raw file prefix: `https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/`.
  Use the reviewed branch or full commit SHA for a PR investigation.
- Rendered site: [student landing](https://meijer1973.github.io/4veco-lessen/index.html).
  Site pages show deployed output, which may differ from a PR. Use explicit
  HTML filenames and encode spaces, commas and the U+2013 en dash.
- Exact paths: [current lesson inventory](https://github.com/meijer1973/4veco-platform/blob/main/reports/github-agent-current-lessen.md).
  For tools needing literal URLs, use the
  [URL index](https://raw.githubusercontent.com/meijer1973/4veco-platform/main/reports/url-index.md).
- Prefer local search or authenticated GitHub file/tree access when available.
  Before declaring a file absent, verify its repository, ref, filename and
  encoding. A failed unauthenticated fetch or raw directory URL is not evidence
  that the file is missing; state access limits.
- Raw files are source bytes; rendered HTML/PDF is product evidence. Plans,
  inventory snapshots and roadmaps are not substitutes for the actual artifact.
## Selected Books 3 and 4

- Book 3: [complete PDFs, chapters and all editable sources](Boek%203%20-%20Overheidsingrijpen%2C%20concurrentie%20en%20internationale%20handel/README.md); [current outline adoption](https://github.com/meijer1973/4veco-platform/blob/codex/import-books34-outlines-20260914/references/authored/book-outlines/book-3-outline.meta.json).
- Book 4: [complete PDFs, chapters and all editable sources](Boek%204%20-%20Monopolie%2C%20marktfalen%20en%20arbeidsmarkt/README.md); [current outline adoption](https://github.com/meijer1973/4veco-platform/blob/codex/import-books34-outlines-20260914/references/authored/book-outlines/book-4-outline.meta.json).

Current lookup: platform `node build-scripts/references/books34-selected-structure.js 3.3.1`. Validation: `node build-scripts/maintenance/check-books34-chat-import.js --require-paired --require-tracked`. Numeric IDs require revision `book34-chat-v2-20260914`; archive IDs do not transfer target approval. Integration is prepared/in PR.
