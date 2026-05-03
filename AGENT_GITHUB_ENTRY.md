# GitHub Agent Entry - 4veco Lessen

This repo is the generated, student-facing lesson-material corpus for 4veco. It contains published book, chapter, paragraph, companion, asset, and shared-runtime output.

The authoring and build platform lives in the companion repo `4veco-platform`. For cross-repo work, start by reading both `RESEARCH_AGENT_MAP.md` files.

| Question type | Inspect first |
|---|---|
| Does a generated lesson artifact currently exist for students? | `4veco-lessen` |
| Which book/chapter/paragraph files are published now? | `4veco-lessen` |
| Is a PDF, HTML page, DOCX, PPTX, image, or companion page present? | `4veco-lessen` |
| How is a lesson, game, visual, validator, or reference generated? | `4veco-platform` |
| Which engine/source/template should be changed? | `4veco-platform` |
| Why did a generated artifact look or behave this way? | `4veco-lessen`, then `4veco-platform` |
| Is a copied `shared/` engine file authoritative? | `4veco-platform` |

Common mistakes:

- Searching only `4veco-lessen` and concluding the build logic is absent.
- Searching only `4veco-platform` and concluding a lesson artifact does not exist.
- Hand-editing copied `shared/` engine files here instead of changing platform-managed sources.
- Treating generated files here as proof that the platform has no newer source, validator, or roadmap requirement.
- Building a Book 1-specific status system instead of using repository maps and the generated file inventory from `4veco-platform`.

Useful entry points:

- `RESEARCH_AGENT_MAP.md`
- `AGENTS.md`
- `lessen-team-roadmap.md`
- `course_blueprint_v4.md`
- `index.html`
- `4veco-platform/reports/github-agent-index-lessen.md` after running `npm run agent:index` in `4veco-platform`
