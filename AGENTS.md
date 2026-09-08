# 4veco Lessons — Agent Entry

This repository contains lesson content and student-facing materials for VWO 4
economics. The companion repository, `../4veco-platform`, owns production logic,
engines, generators, validators, shared skills, and integration tooling.

## Shared operating rules

Read [the platform operating guide](../4veco-platform/AGENTS.md) first. It is
canonical for planning and quality requirements, task-dependent reading,
branch/worktree safety and ownership, protected references, review evidence,
publication, PR readiness, integration, and completion reporting. Those rules
apply to work in this repository; this entry does not maintain a second copy.
Use its direct review-packet-comment protocol for human review.

## Read next — select the activity

Read only the workflow relevant to the current activity, including that
workflow's applicable requirements. If the task expands, load the additional
route before starting the new activity.

| Activity | Starting point |
|---|---|
| Read-only investigation or routine maintenance | Affected lesson files and the corresponding platform source/validators. Use local repository search; research maps are lookup references. |
| Textbook paragraph / Part A | Platform [lane vocabulary](../4veco-platform/docs/workflows/paragraph-lane-vocabulary.md) and [textbook runbook](../4veco-platform/docs/workflows/textbook-paragraph-lane.md). |
| Companion paragraph / Part B | Platform [lane vocabulary](../4veco-platform/docs/workflows/paragraph-lane-vocabulary.md), [companion runbook](../4veco-platform/docs/workflows/web-companion-paragraph-lane.md), and [companion specifications](specifications/companion-core-specifications.md). |
| Chapter or book assembly | Platform [BUILD-CHAPTER.md](../4veco-platform/BUILD-CHAPTER.md) and the chapter plan. |
| Complete paragraph or cross-lane verification | Platform [BUILD-PARAGRAPH.md](../4veco-platform/BUILD-PARAGRAPH.md), the full reference used when that scope is required. |
| Roadmap, sprint, review, or Scale Gate | Relevant roadmap/original requirements, [product vision](specifications/product-vision.md), and [product end state](specifications/product-end-state.md); use the shared operating guide's gates. |
| Production logic, generation, or build ownership | Platform [build-scripts/README.md](../4veco-platform/build-scripts/README.md) and the applicable lane/skill. |
| PR readiness or paired integration | Platform [readiness policy](../4veco-platform/docs/review/pr-readiness-routing-policy.md) and [integration policy](../4veco-platform/docs/review/pr-integration-lane-policy.md), including their bundle requirements. |

Paragraph assignments start with their lane runbook. The full paragraph manual
and chapter guide are references for their respective activities, not mandatory
reading for every lesson-repository task.

## Lesson content and generated output

- Build, generate, validate, and refactor lesson materials through platform
  tooling. Do not invent lesson-local build scripts when the platform has or
  should own the workflow.
- If the task changes how materials are produced, change platform source first.
  Do not hand-build or hand-edit generated outputs as a one-off workaround.
- Direct edits here are limited to lesson content or generated artifacts when
  the platform workflow explicitly calls for writing them here. Follow each
  artifact's source/generator ownership and the applicable lane boundaries.
- Do not edit machine-owned reference data from this repository. Use the
  platform's authorized reference workflow and its protected-source rules.
- Keep the paired platform and lesson worktrees together under the task folder;
  run the shared worktree preflight from the platform worktree with the lesson
  path supplied through `--worktree`.

## Product and exam-target requirements

Before roadmap, paragraph-build, companion, exit-ticket, exam-ingestion, or
Scale Gate work, use [product vision](specifications/product-vision.md) for
strategic direction and [product end state](specifications/product-end-state.md)
for the operational north star. Companion work also follows
[companion specifications](specifications/companion-core-specifications.md).

The intended companion route is
`Start -> Leer -> Check -> Oefen -> Exit ticket`, with an advisory short check
and a separate target-equivalent exit ticket. A smaller deliverable is not the
full product: name missing requirements as follow-up work or record an explicit
human waiver with consequences.

For official-exam targets, build backward from the CvTE question, source
annexes/figures, correction model, points, and answer-construction requirements.
Use the platform exam-ingestion overlay, MTU mapping, paragraph-plan contract,
and build workflow after the reference team authorizes the relevant EX/L-EX
sprint. Do not patch this authority into generated lesson output. The plan
must trace every official answer-model step to explicit teaching, textbook
practice, scaffolding, companion practice, prior knowledge with MTU evidence,
or a justified exclusion, as required by the shared operating guide.
