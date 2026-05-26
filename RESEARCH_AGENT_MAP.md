# Research Agent Map

Agent-executable access and traversal specification for the `4veco-lessen` lesson-material corpus.

This file is for remote research agents. It is not just a repository orientation note: every path, namespace, and template below is intended to be fetchable through raw GitHub URL construction or readable through a GitHub connector.

This map is **complete**, not partial. It covers every layer of the repository: top-level planning and curriculum sources, the per-book directory tree, the chapter and paragraph artifact families, the companion-output family, the shared engine layer, and the per-paragraph quality logs. Nothing in this repo is intentionally out of scope for a research agent reading this map.

## Minimal Research Guidance

The lesson-material corpus answers:

- which lesson material is published and at what level (book, chapter, paragraph)
- which paragraph variants exist (textbook artifacts, companion handouts, companion games, presentation, summary)
- which planning state and quality verdict applies to each paragraph
- which assets (figures, worked examples, exercises, news visuals) anchor the visual layer
- which shared engines render the interactive companion games
- how future exam-target paragraphs should trace official exam prompts, source annexes, correction-model steps, and MTU/operation requirements to teaching and practice surfaces

Repository boundary:

- `4veco-lessen` contains generated and student-facing lesson output: book, chapter, paragraph, companion, asset, and shared-runtime files.
- Authoring and build logic lives in `4veco-platform`: generators, engines, source data, skills, validators, references, and reports are maintained there.
- Copied shared engines in `shared/` are platform-managed deploy output. Do not hand-edit them here; inspect and change the source engine files in `4veco-platform`.
- Generated lesson artifacts must be checked in this repo, not in the platform repo. A platform builder, source file, or roadmap entry does not prove the student-facing artifact currently exists.
- Agents must not infer platform capability from generated lesson artifacts alone. A lesson artifact shows current output, not necessarily the source logic that produced it.
- For cross-repo questions, read both repository maps before concluding anything:
  - `4veco-lessen/RESEARCH_AGENT_MAP.md`
  - `4veco-platform/RESEARCH_AGENT_MAP.md`

This repository is a **generated student-facing target**, not a content authoring platform. The platform repo (`4veco-platform`) builds into this one. When a research question is about *how* output is produced, redirect to the platform repo; when the question is *what is currently published*, this repo is the authoritative source.

When a planning document and a generated artifact disagree, inspect both. The planning document records intent; the generated artifact records the last successful build.

Exam-target paragraph note: this repo can show whether a paragraph, source
object, companion surface, or quality log exists. It does not own the
exam-ingestion contract. For official exam-question ingestion, source-annex
coverage, correction-model decomposition, MTU mapping, and answer-operation
requirements, inspect `4veco-platform` first, then confirm generated lesson
artifacts here.

## Access Layer

Repository:

```text
https://github.com/meijer1973/4veco-lessen
```

Raw base URL:

```text
https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/
```

Agents MUST construct file URLs as:

```text
<raw_base_url><relative_path>
```

Example:

```text
lessen-team-roadmap.md ->
https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/lessen-team-roadmap.md
```

Access rules:

- All file references in this document are relative paths from the repository root.
- Use forward slashes in constructed URLs.
- Preserve spaces, parentheses, commas, en-dashes (`–`, U+2013), and Dutch characters in relative paths; URL-encode them only when required by the HTTP client. Book folder names contain ` - ` (space hyphen space) and `, `; chapter folder names contain ` `; artifact filenames contain ` – ` (space en-dash space).
- Directories are path namespaces, not fetch targets.
- Fetch files only by declared path, declared namespace search, or declared path template.
- Use exact paths from this file or `AGENT_GITHUB_ENTRY.md` when possible; these curated files are more reliable than GitHub search results.
- Use `reports/github-agent-index-platform.md` and `reports/github-agent-index-lessen.md` from `4veco-platform` for file-existence checks.
- Use GitHub search mainly for discovery, not proof. Confirm discoveries by fetching exact paths or checking the generated inventory.
- Some artifacts are large binaries (PDF up to ~5 MB, PPTX, DOCX, HTML up to ~7 MB for assembled-book HTML). Range-requests or connector access may be required.
- If raw URL access fails, retry through authenticated GitHub connector access before concluding the file is unavailable.

## Entry Points

Human-readable:

- `index.html` (top-level landing — book list)
- `AGENT_GITHUB_ENTRY.md` (one-page GitHub orientation for agents)
- `AGENTS.md` (operating rules for any agent acting on this repo)
- `specifications/product-end-state.md` (canonical product north star)
- `specifications/companion-core-specifications.md` (stable companion specifications)
- `lessen-team-roadmap.md` (sprint ledger, mission, current status, guardrails)
- `course_blueprint_v5.md` (active four-book / four-test-week curriculum-source baseline)
- `plan-1.1.1-part-b-clarity-audit.md` (active plan document at root)
- `Boek 1 - Grondslagen, vraag en aanbod/index.html` (book-level landing)
- `Boek 1 - Grondslagen, vraag en aanbod/Boek 1 Grondslagen, vraag en aanbod – boek.md`
- `Boek 1 - Grondslagen, vraag en aanbod/1.1 Hoofdstuk Economisch denken en rekenen/_chapter-plan.md`
- `Boek 1 - Grondslagen, vraag en aanbod/1.1 Hoofdstuk Economisch denken en rekenen/1.1.1 Schaarste en economisch denken/_paragraph-plan.md`

Machine-readable:

```json
{
  "entry_points": [
    "Boek 1 - Grondslagen, vraag en aanbod/deploy-config.json",
    "Boek 1 - Grondslagen, vraag en aanbod/1.1 Hoofdstuk Economisch denken en rekenen/1.1.1 Schaarste en economisch denken/1.1.1-quality-ref.yaml",
    "Boek 1 - Grondslagen, vraag en aanbod/1.1 Hoofdstuk Economisch denken en rekenen/1.1.2 Percentages en indexcijfers/1.1.2-quality-ref.yaml",
    "Boek 1 - Grondslagen, vraag en aanbod/1.1 Hoofdstuk Economisch denken en rekenen/1.1.3 Grafieken en tabellen/1.1.3-quality-ref.yaml",
    "Boek 1 - Grondslagen, vraag en aanbod/1.1 Hoofdstuk Economisch denken en rekenen/1.1.4 Gemengde opgaven/1.1.4-quality-ref.yaml"
  ]
}
```

entry_points (full URLs):

- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/index.html
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/AGENTS.md
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/specifications/product-end-state.md
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/specifications/companion-core-specifications.md
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/lessen-team-roadmap.md
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/course_blueprint_v5.md
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/plan-1.1.1-part-b-clarity-audit.md
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/index.html
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/Boek%201%20Grondslagen%2C%20vraag%20en%20aanbod%20%E2%80%93%20boek.md
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/1.1%20Hoofdstuk%20Economisch%20denken%20en%20rekenen/_chapter-plan.md
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/1.1%20Hoofdstuk%20Economisch%20denken%20en%20rekenen/1.1.1%20Schaarste%20en%20economisch%20denken/_paragraph-plan.md
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/deploy-config.json
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/1.1%20Hoofdstuk%20Economisch%20denken%20en%20rekenen/1.1.1%20Schaarste%20en%20economisch%20denken/1.1.1-quality-ref.yaml
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/1.1%20Hoofdstuk%20Economisch%20denken%20en%20rekenen/1.1.2%20Percentages%20en%20indexcijfers/1.1.2-quality-ref.yaml
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/1.1%20Hoofdstuk%20Economisch%20denken%20en%20rekenen/1.1.3%20Grafieken%20en%20tabellen/1.1.3-quality-ref.yaml
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/1.1%20Hoofdstuk%20Economisch%20denken%20en%20rekenen/1.1.4%20Gemengde%20opgaven/1.1.4-quality-ref.yaml

Cross-repo entry point (4veco-platform):

- https://raw.githubusercontent.com/meijer1973/4veco-platform/main/RESEARCH_AGENT_MAP.md
- https://raw.githubusercontent.com/meijer1973/4veco-platform/main/RESEARCH_AGENT_MAP_REFERENCES.md
- https://raw.githubusercontent.com/meijer1973/4veco-platform/main/AGENTS.md

URL index (single fetch unlocks the rest of the surface, served from the platform repo):

- https://raw.githubusercontent.com/meijer1973/4veco-platform/main/reports/url-index.md

## Index Anchors

`4veco-lessen` does not yet have one central manifest. Use these files as manifest-like navigation anchors. Read these first; they connect planning intent to the generated artifacts on disk.

```json
{
  "repo_operating_rules": "AGENTS.md",
  "product_end_state_spec": "specifications/product-end-state.md",
  "companion_core_spec": "specifications/companion-core-specifications.md",
  "team_roadmap": "lessen-team-roadmap.md",
  "closed_lesson_ticket_cp6a_chapter13_alignment": "lesson-ticket-L-CP6A-book1-chapter13-v5-alignment.md",
  "course_blueprint": "course_blueprint_v5.md",
  "active_root_plan": "plan-1.1.1-part-b-clarity-audit.md",
  "exam_reference_pdf": "vw-1022-a-25-1-o.pdf",
  "top_landing": "index.html",
  "book_deploy_config_template": "Boek N - <book-title>/deploy-config.json",
  "book_landing_template": "Boek N - <book-title>/index.html",
  "book_assembled_md_template": "Boek N - <book-title>/Boek N <book-title> – boek.md",
  "chapter_plan_template": "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/_chapter-plan.md",
  "chapter_assembled_md_template": "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M <chapter-title> – hoofdstuk.md",
  "paragraph_plan_template": "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/_paragraph-plan.md",
  "paragraph_quality_ref_template": "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K-quality-ref.yaml",
  "paragraph_review_template": "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K-review.md"
}
```

index_anchors (full URLs):

Concrete index-anchor files (templates with `<book-title>` / `N.M.K` placeholders are not fetchable until substituted; only the concrete anchors are listed here):

- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/AGENTS.md
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/specifications/product-end-state.md
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/specifications/companion-core-specifications.md
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/lessen-team-roadmap.md
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/lesson-ticket-L-CP6A-book1-chapter13-v5-alignment.md
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/course_blueprint_v5.md
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/plan-1.1.1-part-b-clarity-audit.md
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/vw-1022-a-25-1-o.pdf
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/index.html

Use these index anchors before free-form browsing. The plan files state intent, the quality-ref YAML records last-known machine-checkable state, and the review markdown records the human-pass verdict.

## Path Registry

```json
{
  "root": "https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/",
  "declared_path_namespaces": [
    ".",
    "specifications",
    "archive/sprints/SPEC-END-STATE",
    "Boek 1 - Grondslagen, vraag en aanbod",
    "Boek 1 - Grondslagen, vraag en aanbod/_assets",
    "Boek 1 - Grondslagen, vraag en aanbod/shared",
    "Boek 1 - Grondslagen, vraag en aanbod/shared/newsdetective",
    "Boek 1 - Grondslagen, vraag en aanbod/shared/procedure",
    "Boek 1 - Grondslagen, vraag en aanbod/shared/questions",
    "Boek 1 - Grondslagen, vraag en aanbod/shared/reasoning",
    "Boek 1 - Grondslagen, vraag en aanbod/shared/skilltree",
    "Boek 1 - Grondslagen, vraag en aanbod/1.1 Hoofdstuk Economisch denken en rekenen",
    "Boek 1 - Grondslagen, vraag en aanbod/1.1 Hoofdstuk Economisch denken en rekenen/_assets",
    "Boek 1 - Grondslagen, vraag en aanbod/1.1 Hoofdstuk Economisch denken en rekenen/1.1.1 Schaarste en economisch denken",
    "Boek 1 - Grondslagen, vraag en aanbod/1.1 Hoofdstuk Economisch denken en rekenen/1.1.1 Schaarste en economisch denken/_assets",
    "Boek 1 - Grondslagen, vraag en aanbod/1.1 Hoofdstuk Economisch denken en rekenen/1.1.1 Schaarste en economisch denken/svg",
    "Boek 1 - Grondslagen, vraag en aanbod/1.1 Hoofdstuk Economisch denken en rekenen/1.1.2 Percentages en indexcijfers",
    "Boek 1 - Grondslagen, vraag en aanbod/1.1 Hoofdstuk Economisch denken en rekenen/1.1.3 Grafieken en tabellen",
    "Boek 1 - Grondslagen, vraag en aanbod/1.1 Hoofdstuk Economisch denken en rekenen/1.1.4 Gemengde opgaven",
    "Boek 1 - Grondslagen, vraag en aanbod/1.2 Hoofdstuk Vraag",
    "Boek 1 - Grondslagen, vraag en aanbod/1.3 Hoofdstuk Aanbod en marktevenwicht",
    "Boek 1 - Grondslagen, vraag en aanbod/1.4 Hoofdstuk Marktevenwicht en marginale analyse",
    "Boek 1 - Grondslagen, vraag en aanbod/1.5 Hoofdstuk Toetsvoorbereiding"
  ],
  "root_doc_paths": [
    "AGENTS.md",
    "specifications/product-end-state.md",
    "specifications/companion-core-specifications.md",
    "lessen-team-roadmap.md",
    "course_blueprint_v5.md",
    "plan-1.1.1-part-b-clarity-audit.md",
    "vw-1022-a-25-1-o.pdf",
    "index.html",
    ".gitignore",
    ".nojekyll"
  ],
  "book_root_paths": [
    "Boek 1 - Grondslagen, vraag en aanbod/deploy-config.json",
    "Boek 1 - Grondslagen, vraag en aanbod/index.html",
    "Boek 1 - Grondslagen, vraag en aanbod/Boek 1 Grondslagen, vraag en aanbod – boek.md",
    "Boek 1 - Grondslagen, vraag en aanbod/Boek 1 Grondslagen, vraag en aanbod – boek.html",
    "Boek 1 - Grondslagen, vraag en aanbod/Boek 1 Grondslagen, vraag en aanbod – boek.pdf"
  ],
  "shared_engine_paths": [
    "Boek 1 - Grondslagen, vraag en aanbod/shared/theme.js",
    "Boek 1 - Grondslagen, vraag en aanbod/shared/voorkennis.js",
    "Boek 1 - Grondslagen, vraag en aanbod/shared/voorkennis.css",
    "Boek 1 - Grondslagen, vraag en aanbod/shared/quiz-engine.js",
    "Boek 1 - Grondslagen, vraag en aanbod/shared/quiz-ui.js",
    "Boek 1 - Grondslagen, vraag en aanbod/shared/quiz.css",
    "Boek 1 - Grondslagen, vraag en aanbod/shared/reasoning-engine.js",
    "Boek 1 - Grondslagen, vraag en aanbod/shared/reasoning-ui.js",
    "Boek 1 - Grondslagen, vraag en aanbod/shared/reasoning.css",
    "Boek 1 - Grondslagen, vraag en aanbod/shared/skilltree-engine.js",
    "Boek 1 - Grondslagen, vraag en aanbod/shared/skilltree-ui.js",
    "Boek 1 - Grondslagen, vraag en aanbod/shared/skilltree.css",
    "Boek 1 - Grondslagen, vraag en aanbod/shared/newsdetective-engine.js",
    "Boek 1 - Grondslagen, vraag en aanbod/shared/newsdetective-ui.js",
    "Boek 1 - Grondslagen, vraag en aanbod/shared/newsdetective.css",
    "Boek 1 - Grondslagen, vraag en aanbod/shared/procedure-engine.js",
    "Boek 1 - Grondslagen, vraag en aanbod/shared/procedure-ui.js",
    "Boek 1 - Grondslagen, vraag en aanbod/shared/procedure.css",
    "Boek 1 - Grondslagen, vraag en aanbod/shared/skilltree/base-elements.js",
    "Boek 1 - Grondslagen, vraag en aanbod/shared/skilltree/explanations.js"
  ],
  "shared_per_paragraph_data_template": [
    "Boek N - <book-title>/shared/questions/N.M.K.js",
    "Boek N - <book-title>/shared/reasoning/N.M.K.js",
    "Boek N - <book-title>/shared/reasoning/meta-categories.js",
    "Boek N - <book-title>/shared/skilltree/N.M.K.js",
    "Boek N - <book-title>/shared/procedure/N.M.K.js",
    "Boek N - <book-title>/shared/newsdetective/N.M.K.js"
  ],
  "chapter_artifact_template": [
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/_chapter-plan.md",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/build_chapter.py",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M <chapter-title> – hoofdstuk.md",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M <chapter-title> – hoofdstuk.html",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M <chapter-title> – hoofdstuk.pdf",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M <chapter-title> – antwoorden.md",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M <chapter-title> – antwoorden.html",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M <chapter-title> – antwoorden.pdf"
  ],
  "paragraph_textbook_template": [
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/_paragraph-plan.md",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/build_pdf.py",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K-quality-ref.yaml",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K-review.md",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – paragraaf.md",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – paragraaf.html",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – paragraaf.pdf",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – opgaven.md",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – opgaven.html",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – opgaven.pdf",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – antwoorden.md",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – antwoorden.html",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – antwoorden.pdf"
  ],
  "paragraph_companion_html_template": [
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/index.html",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – instapquiz.html",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – wiskundevaardigheden.html",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – stappenplan.html",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – redeneer-spel.html",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – nieuws-detective.html",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – uitleg voorkennis.html",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – uitleg vaardigheden.html",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – begeleide inoefening.html",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – youtube-videos.html"
  ],
  "paragraph_companion_office_template": [
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – uitleg voorkennis.docx",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – uitleg vaardigheden.docx",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – nieuws met visual.docx",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – samenvatting.docx",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – presentatie.pptx",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – begeleide inoefening – vragen.docx",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – begeleide inoefening – antwoorden.docx",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – basis – vragen.docx",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – basis – antwoorden.docx",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – midden – vragen.docx",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – midden – antwoorden.docx",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – verrijking – vragen.docx",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – verrijking – antwoorden.docx"
  ],
  "toetsvoorbereiding_paragraph_overrides": [
    "Boek N - <book-title>/N.M Hoofdstuk Toetsvoorbereiding/N.M.1 Actieve samenvatting/N.M.1 Actieve samenvatting – samenvatting.{md,html,pdf}",
    "Boek N - <book-title>/N.M Hoofdstuk Toetsvoorbereiding/N.M.4 Proeftoets/N.M.4 Proeftoets – toets.{md,html,pdf}",
    "Boek N - <book-title>/N.M Hoofdstuk Toetsvoorbereiding/N.M.4 Proeftoets/N.M.4 Proeftoets – toetsmatrijs.{md,html,pdf}"
  ],
  "asset_template": [
    "Boek N - <book-title>/_assets/{paragraph-id}_{type}_{n}.{svg,png}",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/_assets/{paragraph-id}_{type}_{n}.{svg,png}",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/_assets/{paragraph-id}_{type}_{n}_{surface}.{svg,png}",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/svg/{paragraph-id}-<name>.svg"
  ]
}
```

path_registry (full URLs):

Only concrete-path keys are expanded as full URLs. Template keys (`shared_per_paragraph_data_template`, `chapter_artifact_template`, `paragraph_textbook_template`, `paragraph_companion_html_template`, `paragraph_companion_office_template`, `toetsvoorbereiding_paragraph_overrides`, `asset_template`) contain `<book-title>` / `N.M.K` / `{paragraph-id}` placeholders and are not directly fetchable; substitute them per-task using the encoding rules in the Access Layer.

root_doc_paths (full URLs):

- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/AGENTS.md
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/lessen-team-roadmap.md
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/course_blueprint_v5.md
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/plan-1.1.1-part-b-clarity-audit.md
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/vw-1022-a-25-1-o.pdf
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/index.html
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/.gitignore
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/.nojekyll

book_root_paths (full URLs):

- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/deploy-config.json
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/index.html
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/Boek%201%20Grondslagen%2C%20vraag%20en%20aanbod%20%E2%80%93%20boek.md
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/Boek%201%20Grondslagen%2C%20vraag%20en%20aanbod%20%E2%80%93%20boek.html
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/Boek%201%20Grondslagen%2C%20vraag%20en%20aanbod%20%E2%80%93%20boek.pdf

shared_engine_paths (full URLs):

- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/shared/theme.js
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/shared/voorkennis.js
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/shared/voorkennis.css
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/shared/quiz-engine.js
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/shared/quiz-ui.js
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/shared/quiz.css
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/shared/reasoning-engine.js
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/shared/reasoning-ui.js
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/shared/reasoning.css
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/shared/skilltree-engine.js
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/shared/skilltree-ui.js
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/shared/skilltree.css
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/shared/newsdetective-engine.js
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/shared/newsdetective-ui.js
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/shared/newsdetective.css
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/shared/procedure-engine.js
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/shared/procedure-ui.js
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/shared/procedure.css
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/shared/skilltree/base-elements.js
- https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/shared/skilltree/explanations.js

Asset type tokens: `fig` (concept figure), `we` (worked example), `ex` (exercise visual), `news` (news visual). Surface variant tokens: `doc` (Word), `slide` (PowerPoint), `summary` (samenvatting), `web_light`, `web_dark`. Asset folders are stratified: paragraph `_assets/` holds the surface-variant set; chapter `_assets/` and book `_assets/` hold the concept/`base` set copied for chapter and book PDF assembly.

## Path Construction

Use these templates only after loading the relevant index anchor or directory listing.

```json
{
  "raw_file": "<raw_base_url>{relative_path}",
  "paragraph_textbook_artifact": "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – {paragraaf|opgaven|antwoorden}.{md|html|pdf}",
  "paragraph_companion_artifact": "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – {variant}.{html|docx|pptx}",
  "chapter_artifact": "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M <chapter-title> – {hoofdstuk|antwoorden}.{md|html|pdf}",
  "book_artifact": "Boek N - <book-title>/Boek N <book-title> – boek.{md|html|pdf}",
  "asset": "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/_assets/{paragraph-id}_{type}_{n}[_{surface}].{svg|png}",
  "shared_paragraph_data": "Boek N - <book-title>/shared/{game}/N.M.K.js"
}
```

If a constructed path fails, apply `Failure Handling`.

## Layer Semantics

```json
{
  "root_planning_and_reference": {
    "epistemic_role": "operating rules, course blueprint, sprint state, and one external exam reference",
    "contains": "AGENTS.md, lessen-team-roadmap.md, course_blueprint_v5.md, plan-*.md, vw-*.pdf, top-level index.html",
    "preferred_use": "understand mission, current sprint, blueprint scope, and external alignment",
    "edit_policy": "AGENTS.md and roadmap edited only as planning updates; course_blueprint_v5.md and the exam PDF are read-only references; index.html is hand-maintained"
  },
  "book_layer": {
    "epistemic_role": "per-book deploy config, landing page, and assembled-book artifacts",
    "contains": "deploy-config.json, index.html, '<book> – boek.{md,html,pdf}', book-level _assets/ (cumulative)",
    "preferred_use": "list which paragraphs belong to which book, and read assembled-book content",
    "edit_policy": "deploy-config.json and index.html are platform-generated; '– boek.*' artifacts are platform-built; do not hand-edit"
  },
  "shared_engine_layer": {
    "epistemic_role": "auto-copied platform engines (read-only here) plus per-paragraph data files for the five companion games",
    "contains": "shared/<game>-engine.js, shared/<game>-ui.js, shared/<game>.css, shared/theme.js, shared/voorkennis.{js,css}, shared/{questions,reasoning,skilltree,procedure,newsdetective}/<paragraph-id>.js",
    "preferred_use": "trace which engine drives a companion HTML; inspect which game-data files exist per paragraph",
    "edit_policy": "engine files are auto-copied from 4veco-platform/engines/ — DO NOT EDIT here; per-paragraph data files are platform-generated; report drift back to platform"
  },
  "chapter_layer": {
    "epistemic_role": "per-chapter plan and assembled-chapter artifacts",
    "contains": "_chapter-plan.md, build_chapter.py, '<chapter> – hoofdstuk.{md,html,pdf}', '<chapter> – antwoorden.{md,html,pdf}', chapter-level _assets/ (paragraph subset)",
    "preferred_use": "read chapter intent (build order, dependencies, dual coding, procedure plan) and assembled chapter PDF/HTML",
    "edit_policy": "_chapter-plan.md is hand-maintained planning input; assembled artifacts are regenerated by build_chapter.py via platform"
  },
  "paragraph_textbook_layer": {
    "epistemic_role": "the canonical textbook artifacts at paragraph level",
    "contains": "_paragraph-plan.md, build_pdf.py, '<paragraph> – paragraaf.{md,html,pdf}', '<paragraph> – opgaven.{md,html,pdf}', '<paragraph> – antwoorden.{md,html,pdf}', paragraph _assets/ (surface variants), per-paragraph svg/ folder for hand-authored SVG sources",
    "preferred_use": "read the published lesson body, exercise set, and answer key for any paragraph",
    "edit_policy": "all generated; regenerate via platform pipelines (BUILD-PARAGRAPH.md). _paragraph-plan.md is the planning input feeding the companion build."
  },
  "paragraph_companion_layer": {
    "epistemic_role": "companion handouts, presentation, and interactive games for a paragraph",
    "contains": "five game HTMLs (instapquiz, wiskundevaardigheden, stappenplan, redeneer-spel, nieuws-detective), companion handouts (uitleg voorkennis, uitleg vaardigheden, begeleide inoefening, drie differentiatie-niveaus basis/midden/verrijking, samenvatting, nieuws met visual), presentatie.pptx, youtube-videos.html, paragraph index.html, and 'Lees dit als je niet weet hoe je moet beginnen met deze les.docx'",
    "preferred_use": "inspect which surfaces have been built for a paragraph; verify which paragraphs are pilot vs not-yet-built",
    "edit_policy": "companion outputs are pilot-state and only fully built for selected paragraphs (currently 1.1.1); regenerate via platform pipelines, never hand-build"
  },
  "toetsvoorbereiding_paragraph_layer": {
    "epistemic_role": "the chapter-5 (Toetsvoorbereiding) variant of the paragraph layer with different artifact names",
    "contains": "'– samenvatting.{md,html,pdf}' (1.5.1), '– toets.{md,html,pdf}' and '– toetsmatrijs.{md,html,pdf}' (1.5.4), plus '– antwoorden' for each",
    "preferred_use": "the toetsvoorbereiding chapter does not follow the paragraaf/opgaven naming pattern; account for its overrides before searching",
    "edit_policy": "all generated; treat overrides as the authoritative naming for chapter 5"
  },
  "quality_log_layer": {
    "epistemic_role": "per-paragraph machine-readable and human-readable quality records",
    "contains": "<paragraph-id>-quality-ref.yaml (asset inventory, content-presence flags, review verdict), <paragraph-id>-review.md (QC pass narrative)",
    "preferred_use": "discover which paragraphs are complete, which have flagged issues, and which assets are missing",
    "edit_policy": "regenerated alongside the paragraph; do not hand-edit"
  },
  "asset_layer": {
    "epistemic_role": "image and SVG inventory at three nested levels",
    "contains": "paragraph-level _assets/ (surface variants: doc, slide, summary, web_light, web_dark), chapter-level _assets/ (paragraph subset, base only), book-level _assets/ (cumulative across paragraphs); per-paragraph svg/ folder (hand-authored SVG sources where used)",
    "preferred_use": "verify visuals exist for a paragraph and which surface variants are available",
    "edit_policy": "regenerated by platform; the chapter and book copies are derivative of the paragraph copy"
  }
}
```

## Evidence Hierarchy

Use this hierarchy when evidence conflicts:

1. The paragraph markdown source — `<paragraph> – paragraaf.md`, `– opgaven.md`, `– antwoorden.md` — is the authoritative student-facing text.
2. The paragraph plan — `_paragraph-plan.md` — is the authoritative intent record (key concepts, formulas, visuals plan, surface variants, companion plan).
3. The chapter plan — `_chapter-plan.md` — anchors cross-paragraph conventions (notation, colours, dual coding, procedures).
4. The deploy-config — `deploy-config.json` — is the authoritative paragraph-list per book.
5. The quality-ref YAML — `<id>-quality-ref.yaml` — is the authoritative completeness/asset record.
6. The review markdown — `<id>-review.md` — is the authoritative human-pass verdict.
7. Assembled artifacts (`– hoofdstuk.{html,pdf}`, `– boek.{html,pdf}`) reflect the last build only; if they disagree with the paragraph markdown, trust the paragraph markdown and flag the assembly as stale.
8. The team roadmap — `lessen-team-roadmap.md` — is planning state, not factual evidence about generated artifacts.
9. The course blueprint — `course_blueprint_v5.md` — is upstream curriculum design, not proof that any paragraph implements it.
10. Companion artifacts (HTML games, DOCX, PPTX) are controlled-scope surfaces; absence of a companion is not a defect unless the paragraph is in a closed companion sprint.

Do not infer that an artifact exists from the plan. Always confirm by listing the directory or fetching the file.

## Agent Traversal Protocol

Agents MUST follow this sequence:

1. Load this map.
2. Load `AGENTS.md` (operating rules),
   `specifications/product-end-state.md` (product north star),
   `specifications/companion-core-specifications.md` (companion baseline), and
   `lessen-team-roadmap.md` (sprint state).
   - Determine which sprint is active and which paragraphs are in scope for companion-output research.
3. Load the relevant book's deploy-config and landing page:
   - `Boek N - <book-title>/deploy-config.json`
   - `Boek N - <book-title>/index.html`
4. For chapter or paragraph questions, load the relevant plan files first:
   - chapter task -> `<chapter>/_chapter-plan.md`
   - paragraph task -> `<paragraph>/_paragraph-plan.md` (if present), otherwise the paragraph's `– paragraaf.md`
5. For state questions, load the per-paragraph quality records:
   - `<paragraph>/<id>-quality-ref.yaml`
   - `<paragraph>/<id>-review.md`
6. For visual questions, list the paragraph `_assets/` directory and read the surface-variant filenames before opening any artifact.
7. For companion questions, list the paragraph directory and inventory which of the companion HTML/DOCX/PPTX templates are present.
8. For game-engine questions, load:
   - the engine source under `Boek N - <book-title>/shared/<game>-engine.js`
   - the per-paragraph data file under `Boek N - <book-title>/shared/<game>/<paragraph-id>.js`
   - the companion HTML shell that loads them
9. For chapter-5 (Toetsvoorbereiding), apply the `toetsvoorbereiding_paragraph_overrides` template; do not search for `– paragraaf` / `– opgaven` filenames there.
10. Search declared namespaces only when the indexes do not answer the question.
    - Prefer Dutch search terms for lesson content, concepts, exercises, and didactic vocabulary.
    - Use English terms for filenames, build scripts, planning language, and roadmap entries.
11. For machine-readable questions, prefer YAML/JSON over markdown.
    - `deploy-config.json` is the paragraph registry per book.
    - `<id>-quality-ref.yaml` is the per-paragraph completeness record.
    - If YAML and review markdown disagree, treat the review markdown as the human-authored verdict and the YAML as the machine snapshot, and report the mismatch.
12. Label every conclusion as one of:
    - verified from source artifact
    - verified from plan or quality log
    - inferred from assembled artifact (chapter/book)
    - interpretation
    - proposal
    - unresolved issue

## Dependency Flow

```text
course blueprint + chapter plan + paragraph plan
        |
        v
paragraph markdown (paragraaf/opgaven/antwoorden) + assets
        |
        v
paragraph HTML/PDF (build_pdf.py via platform)
        |
        v
chapter assembled HTML/PDF (build_chapter.py via platform)
        |
        v
book assembled HTML/PDF + book index.html + deploy-config.json
        |
        v
companion artifacts (game HTML, DOCX handouts, PPTX, samenvatting, begeleide inoefening)
        |
        v
quality-ref.yaml + review.md  (per-paragraph quality log)
        |
        v
lessen-team-roadmap.md  (sprint ledger reflects pass/fail)
```

Rules:

- Upstream plan changes can invalidate every downstream artifact in the chain.
- The paragraph markdown is the source of truth for content; the chapter and book artifacts are assemblies.
- The shared engine layer is upstream of every companion HTML game; an engine-file change can affect every paragraph that loads it.
- Companion artifacts depend on the paragraph plan and the paragraph markdown but do not feed back into either.
- The quality log and the roadmap are observational — they do not produce content.

## Research Task Routing

```json
{
  "course_overview": [
    "course_blueprint_v5.md",
    "lessen-team-roadmap.md",
    "index.html",
    "Boek 1 - Grondslagen, vraag en aanbod/index.html"
  ],
  "current_sprint_status": [
    "lessen-team-roadmap.md",
    "AGENTS.md",
    "plan-1.1.1-part-b-clarity-audit.md"
  ],
  "book_inventory": [
    "Boek N - <book-title>/deploy-config.json",
    "Boek N - <book-title>/index.html",
    "Boek N - <book-title>/Boek N <book-title> – boek.md"
  ],
  "chapter_research": [
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/_chapter-plan.md",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M <chapter-title> – hoofdstuk.md",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M <chapter-title> – antwoorden.md"
  ],
  "paragraph_textbook_research": [
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/_paragraph-plan.md",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – paragraaf.md",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – opgaven.md",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – antwoorden.md"
  ],
  "paragraph_companion_research": [
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/index.html",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – uitleg voorkennis.html",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – uitleg vaardigheden.html",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – instapquiz.html",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – wiskundevaardigheden.html",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – stappenplan.html",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – redeneer-spel.html",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – nieuws-detective.html",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – begeleide inoefening.html",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – samenvatting.docx",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – presentatie.pptx"
  ],
  "differentiation_levels_research": [
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – basis – vragen.docx",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – basis – antwoorden.docx",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – midden – vragen.docx",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – midden – antwoorden.docx",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – verrijking – vragen.docx",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – verrijking – antwoorden.docx"
  ],
  "asset_research": [
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/_assets",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/svg",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/_assets",
    "Boek N - <book-title>/_assets"
  ],
  "engine_research": [
    "Boek N - <book-title>/shared/quiz-engine.js",
    "Boek N - <book-title>/shared/skilltree-engine.js",
    "Boek N - <book-title>/shared/skilltree/base-elements.js",
    "Boek N - <book-title>/shared/skilltree/explanations.js",
    "Boek N - <book-title>/shared/reasoning-engine.js",
    "Boek N - <book-title>/shared/reasoning/meta-categories.js",
    "Boek N - <book-title>/shared/newsdetective-engine.js",
    "Boek N - <book-title>/shared/procedure-engine.js",
    "Boek N - <book-title>/shared/voorkennis.js",
    "Boek N - <book-title>/shared/theme.js"
  ],
  "per_paragraph_game_data_research": [
    "Boek N - <book-title>/shared/questions/N.M.K.js",
    "Boek N - <book-title>/shared/skilltree/N.M.K.js",
    "Boek N - <book-title>/shared/reasoning/N.M.K.js",
    "Boek N - <book-title>/shared/procedure/N.M.K.js",
    "Boek N - <book-title>/shared/newsdetective/N.M.K.js"
  ],
  "quality_status": [
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K-quality-ref.yaml",
    "Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K-review.md"
  ],
  "exam_alignment": [
    "vw-1022-a-25-1-o.pdf",
    "course_blueprint_v5.md",
    "Boek 1 - Grondslagen, vraag en aanbod/1.5 Hoofdstuk Toetsvoorbereiding"
  ],
  "exam_target_paragraph_research": [
    "lessen-team-roadmap.md",
    "AGENTS.md",
    "course_blueprint_v5.md"
  ],
  "toetsvoorbereiding_research": [
    "Boek N - <book-title>/N.M Hoofdstuk Toetsvoorbereiding/_chapter-plan.md",
    "Boek N - <book-title>/N.M Hoofdstuk Toetsvoorbereiding/N.M.1 Actieve samenvatting/N.M.1 Actieve samenvatting – samenvatting.md",
    "Boek N - <book-title>/N.M Hoofdstuk Toetsvoorbereiding/N.M.2 Examenvaardigheden/N.M.2 Examenvaardigheden – paragraaf.md",
    "Boek N - <book-title>/N.M Hoofdstuk Toetsvoorbereiding/N.M.3 Integratieoefening/N.M.3 Integratieoefening – paragraaf.md",
    "Boek N - <book-title>/N.M Hoofdstuk Toetsvoorbereiding/N.M.4 Proeftoets/N.M.4 Proeftoets – toets.md",
    "Boek N - <book-title>/N.M Hoofdstuk Toetsvoorbereiding/N.M.4 Proeftoets/N.M.4 Proeftoets – toetsmatrijs.md"
  ],
  "platform_handoff": [
    "AGENTS.md"
  ]
}
```

## Agent Rules

Agents MAY:

- Fetch files via raw GitHub URLs.
- Use authenticated GitHub connector access if raw access fails or a tool cannot read PDF/DOCX/PPTX binaries.
- Search all declared namespaces.
- Use plan files, quality-ref YAML, and review markdown to discover the state of any paragraph.
- Read shared engine files for read-only inspection of how companion games work.
- Propose roadmap implications and quality issues.

Agents MUST:

- Load this map, `AGENTS.md`, and `lessen-team-roadmap.md` before drawing conclusions about repository state.
- Ground factual claims in a concrete source path, plan path, quality-log path, or performed verification step.
- Treat the entire repository as **generated output** in research context: nothing in this repo is the place to author new content, and findings about *how* something is produced redirect to `4veco-platform`.
- Treat `shared/<engine>*.js` and `shared/<engine>.css` as auto-copied platform engines (read-only here).
- Apply the `toetsvoorbereiding_paragraph_overrides` template before searching chapter 5.
- Confirm artifact existence by directory listing or fetch — do not infer existence from plan files.
- Prefer Dutch search terms for economics and lesson content.
- Report uncertainty when an artifact is missing, when a plan and an artifact disagree, or when an assembled artifact is older than its constituent paragraph markdown.
- Treat companion-layer absence (DOCX, PPTX, game HTML) as expected unless the active sprint covers that paragraph; the companion pipeline is pilot-stage.

Agents MUST NOT:

- Hand-edit any generated artifact, plan file, quality-log file, or shared engine file.
- Treat the assembled `– hoofdstuk.html`, `– boek.html`, or any companion HTML as primary evidence when the underlying paragraph markdown disagrees.
- Mint new paragraphs, rename paragraph folders, or alter `deploy-config.json` from research.
- Use the course blueprint or roadmap as evidence that an artifact exists — those are intent and plan, not proof of build.
- Read `.claude/` (gitignored, local agent settings only).
- Crawl `_assets/`, `svg/`, or shared engine binaries when the plan, paragraph markdown, or quality-ref YAML answers the question.
- Present unsupported didactic, exam-alignment, or quality conclusions as fact.

## Failure Handling

If a file cannot be retrieved:

1. Retry with the constructed raw URL.
2. Verify that the relative path uses forward slashes.
3. Verify URL encoding for spaces, parentheses, commas, and the en-dash `–` (U+2013) used in artifact filenames.
4. Verify the branch is `main`.
5. Try the GitHub blob URL: `https://github.com/meijer1973/4veco-lessen/blob/main/<relative_path>`.
6. Try authenticated GitHub connector access (especially for binary files larger than the raw-URL limit).
7. If the file is in a namespace, search that namespace by paragraph id, paragraph title, artifact suffix, asset id, or engine name.
8. If the missing file is a chapter-5 paragraph artifact, apply the `toetsvoorbereiding_paragraph_overrides` naming.
9. If the missing file is a companion artifact, confirm against the paragraph quality-ref YAML and roadmap whether that companion is expected to exist for that paragraph.
10. If the missing file is an assembled book or chapter HTML/PDF, confirm against the chapter plan whether the build is current; assembled artifacts are platform-built and may lag behind paragraph markdown.
11. Stop if a required evidence source is unavailable and no declared fallback exists.
12. Report unavailable evidence as unavailable, not absent from the corpus.

## Quality Log Schema

For each lesson-material quality issue, record:

```json
{
  "title": "",
  "scope": "book | chapter | paragraph | shared-engine | asset | companion",
  "paragraph_id": "",
  "evidence_path_or_url": "",
  "affected_artifact_family": "textbook | companion | game | asset | quality-log",
  "severity": "",
  "status": "open",
  "next_action": "",
  "target_sprint_or_decision": "",
  "platform_handoff_required": "yes | no",
  "proof_required_to_close": ""
}
```

Suggested categories:

- textbook content correctness (paragraaf/opgaven/antwoorden)
- assembled-artifact staleness (hoofdstuk/boek out of sync with paragraph markdown)
- asset gap (missing visual, missing surface variant, missing light/dark pair)
- companion completeness (missing DOCX/PPTX/game HTML for in-scope paragraph)
- engine drift (`shared/` file out of sync with `4veco-platform/engines/`)
- quality-log integrity (yaml or review.md missing or contradicting markdown)
- roadmap/ownership clarity
- exam alignment (against `vw-1022-a-25-1-o.pdf` and `course_blueprint_v5.md`)

## Output Constraints

- Cite or name supporting paths for every factual finding.
- Separate evidence, interpretation, proposal, and unresolved issue lists.
- Use raw URLs or relative paths consistently.
- Quote paragraph markdown when summarising lesson content; do not paraphrase as if it were your own writing.
- Distinguish published-paragraph status from companion controlled-scope status; the bar for "complete" differs between the two.
- Keep internal technical categories (engine drift, quality-log integrity, build staleness) inside developer-facing reports, not in any output meant for students.
- Do not produce student-facing lesson text from this map. This file is for research navigation, not lesson production. Lesson production lives in `4veco-platform`.
