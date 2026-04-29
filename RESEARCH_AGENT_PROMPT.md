# Research Agent Prompt

You are researching the `4veco-lessen` lesson-material corpus.

## Repository Access

Repository:

```text
https://github.com/meijer1973/4veco-lessen
```

Raw base URL:

```text
https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/
```

Repository map:

```text
https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/RESEARCH_AGENT_MAP.md
```

Construct file URLs as:

```text
<raw_base_url><relative_path>
```

Example:

```text
lessen-team-roadmap.md ->
https://raw.githubusercontent.com/meijer1973/4veco-lessen/main/lessen-team-roadmap.md
```

Folder names contain spaces, commas, and parentheses; artifact filenames contain ` – ` (space en-dash space, U+2013). Preserve these in relative paths and URL-encode them only when the HTTP client requires it.

If a raw URL returns 404, do not immediately conclude that the file is absent. Verify path spelling, en-dash vs hyphen, and branch, then try the GitHub connector or repository search. Some artifacts are large binaries (PDF up to ~5 MB, assembled-book HTML up to ~7 MB); range-requests or connector access may be required.

### Note on agents that cannot construct URLs

Some research environments (notably planning Claude in claude.ai) only fetch URLs that have appeared as literal `https://...` strings in context — they cannot concatenate a base URL with a relative path. For those agents, this map includes parallel `<section_name> (full URLs):` blocks listing concrete paths as complete raw-GitHub URLs. Template entries with `<book-title>` / `N.M.K` placeholders are not directly fetchable and are not enumerated; substitute them per-task using the encoding rules above (`%20` for spaces, `%2C` for commas, `%E2%80%93` for en-dashes). There is also a single-fetch entry point in the platform repo linking every key surface across both repositories:

```text
https://raw.githubusercontent.com/meijer1973/4veco-platform/main/reports/url-index.md
```

Fetch the URL index first if you cannot construct URLs from relative paths.

### GitHub Pages site

This repository is also published as a static site via GitHub Pages (the repo contains `.nojekyll`, so files are served as-is including underscored and dotted paths).

Site base URL:

```text
https://meijer1973.github.io/4veco-lessen/
```

Construct site URLs as `<site_base_url><url-encoded-relative-path>`. Spaces become `%20`, commas become `%2C`, and the en-dash `–` (U+2013) used in artifact filenames becomes `%E2%80%93`. Pointing at a directory alone is not enough on this host — for HTML you usually need the explicit filename (only the top-level and book-level directories have an `index.html` that the host will auto-resolve at the directory URL).

Use the site URL when you want the rendered student-facing experience (HTML companion games, paragraph HTML with stylesheet, assembled-chapter or assembled-book HTML, PDFs in the browser). Use the raw GitHub URL when you want the unrendered source bytes (markdown, JSON, YAML, JS, CSS, plan files).

Exact-file examples covering each artifact family:

```text
# Top-level landing
https://meijer1973.github.io/4veco-lessen/index.html

# Book landing
https://meijer1973.github.io/4veco-lessen/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/index.html

# Assembled book (HTML and PDF)
https://meijer1973.github.io/4veco-lessen/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/Boek%201%20Grondslagen%2C%20vraag%20en%20aanbod%20%E2%80%93%20boek.html
https://meijer1973.github.io/4veco-lessen/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/Boek%201%20Grondslagen%2C%20vraag%20en%20aanbod%20%E2%80%93%20boek.pdf

# Assembled chapter (HTML and PDF)
https://meijer1973.github.io/4veco-lessen/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/1.1%20Hoofdstuk%20Economisch%20denken%20en%20rekenen/1.1%20Economisch%20denken%20en%20rekenen%20%E2%80%93%20hoofdstuk.html
https://meijer1973.github.io/4veco-lessen/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/1.1%20Hoofdstuk%20Economisch%20denken%20en%20rekenen/1.1%20Economisch%20denken%20en%20rekenen%20%E2%80%93%20antwoorden.html

# Paragraph index (companion landing for the paragraph)
https://meijer1973.github.io/4veco-lessen/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/1.1%20Hoofdstuk%20Economisch%20denken%20en%20rekenen/1.1.1%20Schaarste%20en%20economisch%20denken/index.html

# Paragraph textbook artifacts (HTML and PDF)
https://meijer1973.github.io/4veco-lessen/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/1.1%20Hoofdstuk%20Economisch%20denken%20en%20rekenen/1.1.1%20Schaarste%20en%20economisch%20denken/1.1.1%20Schaarste%20en%20economisch%20denken%20%E2%80%93%20paragraaf.html
https://meijer1973.github.io/4veco-lessen/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/1.1%20Hoofdstuk%20Economisch%20denken%20en%20rekenen/1.1.1%20Schaarste%20en%20economisch%20denken/1.1.1%20Schaarste%20en%20economisch%20denken%20%E2%80%93%20opgaven.html
https://meijer1973.github.io/4veco-lessen/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/1.1%20Hoofdstuk%20Economisch%20denken%20en%20rekenen/1.1.1%20Schaarste%20en%20economisch%20denken/1.1.1%20Schaarste%20en%20economisch%20denken%20%E2%80%93%20antwoorden.html
https://meijer1973.github.io/4veco-lessen/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/1.1%20Hoofdstuk%20Economisch%20denken%20en%20rekenen/1.1.1%20Schaarste%20en%20economisch%20denken/1.1.1%20Schaarste%20en%20economisch%20denken%20%E2%80%93%20paragraaf.pdf

# Companion HTML — uitleg, begeleide inoefening, games
https://meijer1973.github.io/4veco-lessen/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/1.1%20Hoofdstuk%20Economisch%20denken%20en%20rekenen/1.1.1%20Schaarste%20en%20economisch%20denken/1.1.1%20Schaarste%20en%20economisch%20denken%20%E2%80%93%20uitleg%20voorkennis.html
https://meijer1973.github.io/4veco-lessen/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/1.1%20Hoofdstuk%20Economisch%20denken%20en%20rekenen/1.1.1%20Schaarste%20en%20economisch%20denken/1.1.1%20Schaarste%20en%20economisch%20denken%20%E2%80%93%20uitleg%20vaardigheden.html
https://meijer1973.github.io/4veco-lessen/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/1.1%20Hoofdstuk%20Economisch%20denken%20en%20rekenen/1.1.1%20Schaarste%20en%20economisch%20denken/1.1.1%20Schaarste%20en%20economisch%20denken%20%E2%80%93%20begeleide%20inoefening.html
https://meijer1973.github.io/4veco-lessen/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/1.1%20Hoofdstuk%20Economisch%20denken%20en%20rekenen/1.1.1%20Schaarste%20en%20economisch%20denken/1.1.1%20Schaarste%20en%20economisch%20denken%20%E2%80%93%20instapquiz.html
https://meijer1973.github.io/4veco-lessen/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/1.1%20Hoofdstuk%20Economisch%20denken%20en%20rekenen/1.1.1%20Schaarste%20en%20economisch%20denken/1.1.1%20Schaarste%20en%20economisch%20denken%20%E2%80%93%20wiskundevaardigheden.html
https://meijer1973.github.io/4veco-lessen/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/1.1%20Hoofdstuk%20Economisch%20denken%20en%20rekenen/1.1.1%20Schaarste%20en%20economisch%20denken/1.1.1%20Schaarste%20en%20economisch%20denken%20%E2%80%93%20stappenplan.html
https://meijer1973.github.io/4veco-lessen/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/1.1%20Hoofdstuk%20Economisch%20denken%20en%20rekenen/1.1.1%20Schaarste%20en%20economisch%20denken/1.1.1%20Schaarste%20en%20economisch%20denken%20%E2%80%93%20redeneer-spel.html
https://meijer1973.github.io/4veco-lessen/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/1.1%20Hoofdstuk%20Economisch%20denken%20en%20rekenen/1.1.1%20Schaarste%20en%20economisch%20denken/1.1.1%20Schaarste%20en%20economisch%20denken%20%E2%80%93%20nieuws-detective.html

# Companion Office artifacts (download — open with appropriate reader)
https://meijer1973.github.io/4veco-lessen/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/1.1%20Hoofdstuk%20Economisch%20denken%20en%20rekenen/1.1.1%20Schaarste%20en%20economisch%20denken/1.1.1%20Schaarste%20en%20economisch%20denken%20%E2%80%93%20samenvatting.docx
https://meijer1973.github.io/4veco-lessen/Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod/1.1%20Hoofdstuk%20Economisch%20denken%20en%20rekenen/1.1.1%20Schaarste%20en%20economisch%20denken/1.1.1%20Schaarste%20en%20economisch%20denken%20%E2%80%93%20presentatie.pptx

# Substitution rule for any paragraph
# Replace the three placeholders, keep the rest of the path identical:
#   {book-folder}     e.g. Boek%201%20-%20Grondslagen%2C%20vraag%20en%20aanbod
#   {chapter-folder}  e.g. 1.1%20Hoofdstuk%20Economisch%20denken%20en%20rekenen
#   {paragraph}       e.g. 1.1.1%20Schaarste%20en%20economisch%20denken
# Pattern:
#   https://meijer1973.github.io/4veco-lessen/{book-folder}/{chapter-folder}/{paragraph}/{paragraph}%20%E2%80%93%20{variant}.{ext}
# where {variant} is one of: paragraaf | opgaven | antwoorden | uitleg%20voorkennis |
#   uitleg%20vaardigheden | begeleide%20inoefening | instapquiz | wiskundevaardigheden |
#   stappenplan | redeneer-spel | nieuws-detective | samenvatting | presentatie |
#   nieuws%20met%20visual | begeleide%20inoefening%20%E2%80%93%20vragen |
#   begeleide%20inoefening%20%E2%80%93%20antwoorden | basis%20%E2%80%93%20vragen |
#   basis%20%E2%80%93%20antwoorden | midden%20%E2%80%93%20vragen |
#   midden%20%E2%80%93%20antwoorden | verrijking%20%E2%80%93%20vragen |
#   verrijking%20%E2%80%93%20antwoorden | youtube-videos
# and {ext} is one of: html | pdf | docx | pptx (depending on variant)
```

Caveats for the site:

- Markdown sources (`*.md`), YAML (`*.yaml`), JSON (`*.json`), and per-paragraph game data (`shared/<game>/N.M.K.js`) are served as raw text and will not render as a webpage. Use the raw GitHub URL for those.
- The companion pipeline is pilot-stage; companion URLs only resolve for paragraphs in the active sprint scope. Hitting 404 on a companion HTML for a non-pilot paragraph is expected, not a defect.
- Chapter 5 (Toetsvoorbereiding) uses different filenames: substitute `samenvatting`, `toets`, or `toetsmatrijs` for the `paragraaf`/`opgaven` slot in the substitution rule above.
- Site state can lag behind `main` while a Pages build runs; a fresh commit is not necessarily live for ~1 minute.
- If a site URL 404s, fall back to the corresponding raw GitHub URL before concluding the artifact is missing.

## Required First Step

Start by reading:

```text
RESEARCH_AGENT_MAP.md
```

Use it as the access-and-traversal specification. It defines:

- raw URL construction
- entry points
- index anchors
- path registry
- layer semantics
- evidence hierarchy
- task routing
- failure handling

The map is navigation guidance, not a replacement for your own source evaluation.

## Research Surface

Search the entire repository unless the task explicitly narrows the scope. The map defines every layer; do not skip any of them on the assumption that "only the textbook side matters" or "only the companion side matters."

Important paths:

- `AGENTS.md`
- `lessen-team-roadmap.md`
- `course_blueprint_v4.md`
- `plan-1.1.1-part-b-clarity-audit.md`
- `vw-1022-a-25-1-o.pdf`
- `index.html`
- `Boek N - <book-title>/deploy-config.json`
- `Boek N - <book-title>/index.html`
- `Boek N - <book-title>/Boek N <book-title> – boek.{md,html,pdf}`
- `Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/_chapter-plan.md`
- `Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M <chapter-title> – {hoofdstuk,antwoorden}.{md,html,pdf}`
- `Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/_paragraph-plan.md`
- `Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K <paragraph-title> – {paragraaf,opgaven,antwoorden}.{md,html,pdf}`
- `Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K-quality-ref.yaml`
- `Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/N.M.K-review.md`
- `Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/_assets/`
- `Boek N - <book-title>/N.M Hoofdstuk <chapter-title>/N.M.K <paragraph-title>/svg/`
- `Boek N - <book-title>/shared/{quiz,reasoning,skilltree,newsdetective,procedure}-engine.js`
- `Boek N - <book-title>/shared/{questions,reasoning,skilltree,procedure,newsdetective}/N.M.K.js`

For chapter 5 (Toetsvoorbereiding) apply the artifact-name overrides documented in the map: `– samenvatting`, `– toets`, `– toetsmatrijs` replace the standard `– paragraaf` / `– opgaven` filenames. Do not assume the standard naming holds there.

For companion-layer questions, read the active sprint in `lessen-team-roadmap.md` first to know which paragraphs are in scope. The companion pipeline is pilot-stage and only fully built for selected paragraphs (currently `1.1.1`); absence elsewhere is expected, not a defect.

Use Dutch search terms for curriculum content, lesson body, exercises, didactic vocabulary, and concept names. Use English terms only when searching code, filenames, build scripts, planning language, or roadmap entries.

Use raw GitHub URLs, GitHub repository search, or GitHub connector file-read tools.

## Boundaries

Do not edit files. You are a research agent.

Treat the entire repository as **generated student-facing output**. Authoring and build logic live in the companion repo `4veco-platform`. If a research finding is about *how* an artifact is produced, the answer redirects there.

Treat these as strictly read-only research surfaces:

- `Boek N - <book-title>/shared/<engine>-engine.js`, `<engine>-ui.js`, `<engine>.css`, `theme.js`, `voorkennis.{js,css}`, and `shared/skilltree/{base-elements.js, explanations.js}`: auto-copied platform engines. Drift here is a platform-handoff issue, not a hand-edit candidate.
- `Boek N - <book-title>/deploy-config.json` and `Boek N - <book-title>/index.html`: platform-generated.
- All assembled artifacts (`– boek.{html,pdf}`, `– hoofdstuk.{html,pdf}`): platform-built.
- All paragraph artifacts (`– paragraaf/opgaven/antwoorden.{md,html,pdf}`, companion HTML/DOCX/PPTX): platform-built.
- `_assets/` and `svg/` directories: platform-built or platform-managed.
- `<id>-quality-ref.yaml` and `<id>-review.md`: regenerated alongside the paragraph.

Do not propose roadmap shifts, sprint reordering, or paragraph minting from research alone. The roadmap and the course blueprint set scope; research surfaces what is true now. If you find a gap, log it as a quality issue with platform handoff required, not as a unilateral re-plan.

Do not infer that an artifact exists from a plan file or a roadmap line. Confirm by directory listing or fetch.

The principle here is **markdown-first**: the paragraph markdown (`– paragraaf.md`, `– opgaven.md`, `– antwoorden.md`) is the source of truth for content. Assembled `– hoofdstuk.html`, `– boek.html`, and companion HTML/DOCX/PPTX reflect the last build only and may be stale. When markdown and assembled artifact disagree, trust the markdown and flag the assembly.

Note on mutation workflows: any change to engine files, generated artifacts, machine-managed configs, or reference-quality YAMLs goes through `4veco-platform` (see `4veco-platform/AGENTS.md`, `BUILD-PARAGRAPH.md`, `BUILD-CHAPTER.md`, `build-scripts/README.md`). If the requested change has no platform workflow yet, report that as a workflow gap instead of hand-editing here.

Do not read `.claude/` (gitignored, local agent settings only).

## Research Question

Replace this section with the concrete question:

```text
Question one
Question two
etc.
```

## Quality Log

Keep a quality log while researching. The purpose is to decide whether the lesson-material corpus needs platform-side updates, whether the roadmap needs new issues, or whether the quality logs themselves are out of sync with the artifacts.

Log:

1. Content errors in paragraph markdown (`– paragraaf/opgaven/antwoorden.md`) — factual mistakes, broken procedures, contradictions with the chapter plan or paragraph plan.
2. Assembled-artifact staleness — `– hoofdstuk.{html,pdf}`, `– boek.{html,pdf}`, or any companion HTML/DOCX/PPTX that disagrees with the underlying paragraph markdown.
3. Asset gaps — referenced but missing visuals, missing surface variants (`_doc`, `_slide`, `_summary`, `_web_light`, `_web_dark`), or broken light/dark symmetry where required.
4. Companion completeness — for paragraphs that are in scope per the active sprint, missing or partial companion outputs (game HTML, voorkennis/vaardigheden, begeleide inoefening, basis/midden/verrijking differentiatie, samenvatting, presentatie, nieuws met visual).
5. Engine drift — `Boek N/shared/<engine>*.js|css` files that look out of sync with the upstream platform engines, or per-paragraph data files (`shared/<game>/N.M.K.js`) that contradict the paragraph plan.
6. Quality-log integrity — `<id>-quality-ref.yaml` and `<id>-review.md` that are missing, contradict the artifacts, or claim a verdict the artifacts do not support.
7. Plan-vs-artifact disagreements — `_paragraph-plan.md` or `_chapter-plan.md` claims that the artifacts do not realise.
8. Exam-alignment concerns — discrepancies between paragraph content and `course_blueprint_v4.md` or the exam reference `vw-1022-a-25-1-o.pdf`, especially in chapter 5 (Toetsvoorbereiding).
9. Roadmap/ownership clarity — sprint state in `lessen-team-roadmap.md` that does not match the on-disk artifact reality.
10. Category suggestions if the current categories do not fit the issues you find.

For each quality issue, include:

- title
- scope (book / chapter / paragraph / shared-engine / asset / companion)
- paragraph id (if applicable)
- evidence path or source URL
- affected artifact family (textbook / companion / game / asset / quality-log)
- severity
- next action
- platform handoff required (yes / no)
- proof required to close

## Deliver

Return:

- clear conclusions
- evidence used, with paths or URLs (cite the markdown when summarising lesson content; do not paraphrase as if it were your own writing)
- important uncertainties or conflicts (especially: paragraph markdown vs assembled artifact, plan vs artifact, roadmap vs disk state)
- practical implications for the lessen-team roadmap and for handoffs back to `4veco-platform`
- quality log entries discovered during the research
- explicit distinction between "published-paragraph status" and "companion-pilot status" — the bar for "complete" differs between the two, and conflating them produces false defects
