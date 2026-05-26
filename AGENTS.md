# 4veco-lessen Instructions

you are a senior developer

This repository is the student-facing lesson-material target. Do not treat it
as the place where production logic lives.

## Build Rule

Build, generate, validate, and refactor lesson materials through the companion
repository:

`C:\Projects\4veco\4veco-platform`

Use the platform repo's build scripts, validators, skills, references, and
workflow docs. In particular, read and follow:

- `4veco-platform/AGENTS.md`
- `4veco-platform/BUILD-PARAGRAPH.md`
- `4veco-platform/BUILD-CHAPTER.md`
- `4veco-platform/build-scripts/README.md`

## Do Not

- Do not invent new local build scripts in this repo when the platform has or
  should have the workflow.
- Do not hand-build generated outputs here as a one-off workaround.
- Do not edit machine-owned reference data from here.

## Allowed Here

Direct edits in this repo should be limited to lesson content or generated
artifacts when the platform workflow explicitly calls for writing them here.
If the task changes how materials are produced, make that change in
`4veco-platform` first.

## Product End-State

Use `specifications/product-end-state.md` as the canonical north star for the
student-facing product. The end state is a generated, review-gated learning
route for every paragraph: the student moves from current readiness to
target-exercise readiness through `Start -> Leer -> Oefen -> Check ->
Verdiep`.

Roadmap entries, sprint plans, review packets, and closure records may choose
a smaller controlled scope, but they must not present that smaller scope as the
full product unless the missing work is assigned to a named follow-up sprint or
explicitly waived by human decision with stated consequences.

## Exam-Target Paragraph End-State

The lesson side is being prepared for paragraphs whose target exercise is an
official CvTE economics exam question.

An exam-target paragraph must build backward from the official question,
source annexes, figures/tables/graphs, official correction model, point
allocation, and answer-construction requirements. The paragraph plan must make
every official answer-model step traceable to one of:

- taught explicitly in Part A;
- practised in textbook opgaven;
- scaffolded in begeleide inoefening;
- repeated in a companion/game surface;
- assumed as prior knowledge with MTU evidence;
- deliberately out of scope, with reason.

Do not build or patch this directly in generated lesson output. Use the
platform exam-ingestion overlay, MTU mapping, paragraph-plan contract, and
build workflow once the reference team has authorized the relevant EX/L-EX
sprint.

## Read first

- Use `specifications/product-end-state.md` as the stable product north star before roadmap, sprint, review, or Scale Gate work.
- Use `specifications/companion-core-specifications.md` as the stable companion-surface specification.
- Use `../CLAUDE.md` "Working agreement — how Claude operates in this repo" for the seven non-negotiable operating rules (read-first, sanity-check-plans, be-honest-about-mistakes, quality-over-patchwork). Applies to every task.
- Use [BUILD-PARAGRAPH.md](C:\Projects\4veco\4veco-platform\BUILD-PARAGRAPH.md) as the end-to-end guide for building a complete paragraph.
- Use [BUILD-CHAPTER.md](C:\Projects\4veco\4veco-platform\BUILD-CHAPTER.md) as the end-to-end guide for assembling paragraphs into a chapter.
- Use `AGENTS.md` for repo overview, architecture, deploy rules, and quality standards.
- Use `build-scripts/README.md` from the platform repo for the distinction between platform generators, converters, reference implementations, and utilities.

## Senior developer operating discipline

Agents in this repository must behave like senior developers, not ticket closers.

## Quality-Driven Execution

Agents must optimize for specification fulfilment, not ticket closure.

A completed task must satisfy the stated specification within the authorized
scope. Passing tests, producing files, or avoiding forbidden claims is not
sufficient when the student-facing route, learning design, rendered output, or
review evidence remains weak.

For every non-trivial task, the plan must state:

1. the quality floor;
2. the specification requirements being fulfilled;
3. the evidence needed to prove fulfilment;
4. the review gate that will judge student-facing quality;
5. any higher-quality improvements that can be included without scope drift;
6. any omitted requirements as named follow-up work or explicit blockers.

If the plan cannot explain how the work will meet the specification, the plan
is not ready.

For any non-trivial sprint, roadmap, gate, reference-system, production, or architecture task:

- read the relevant roadmap, sprint plan, source files, validators, and prior reports before acting
- write or update a sprint plan before implementation
- make the plan operational, not merely formal: it must expand the roadmap description into concrete procedure, decision points, outputs, acceptance tests, and stop conditions
- log the plan in the expected sprint files before executing
- follow the plan as written
- if the plan is too thin or misses a requirement from the roadmap, stop and fix the plan before continuing
- before moving past a review gate, verify the required artifacts exist and validators pass

Human-review gates require actual review artifacts. Do not treat a casual "OK", "continue", or inferred approval as a completed human review when the plan requires an interview, decision record, or gate-closure file. 
All other requirements for sprints are also  required for the Human review. So a checkable plan is made beforehand and that plan is tested afterwards. That will make sure that there is an actual log of the interview. 


### Sprint agent structure

For roadmap sprints, use a separated-agent workflow:

- a planning/review subagent checks the sprint outline, baseline needs, required logs, stop conditions, and missing roadmap instructions before execution. The Planning agent checks whether the plan has a clear statement about the generated output including which files should be generated .
- the main agent executes the sprint and owns final integration
- specialist subagents may be used for bounded pedagogy, evidence, data-integrity, or code-review questions
- a verification subagent should review the finished artifacts or test plan. Do a thorough check on all required files are present including the basic plan  and other required logs, but also the other required files that were mentioned as output in the plan.

The main agent remains accountable. Subagents advise, test, or produce bounded artifacts; they do not replace the roadmap, validators, human gates, or final integration judgement.
