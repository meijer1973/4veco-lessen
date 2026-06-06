# Product End-State Specification

Date: 2026-05-29
Status: CANONICAL PRODUCT NORTH STAR; CHANGE ONLY BY EXPLICIT REVIEW

## Purpose

This file states the intended end state of the 4veco learning product in one
stable place. It exists outside the roadmap and outside individual sprint
plans so active planning cannot drift by gradually weakening the product
definition.

Roadmap entries, sprint plans, review packets, platform handoffs, and closure
records may choose a smaller implementation scope, but they must not present a
smaller scope as the full product unless the missing work is assigned to a
named follow-up sprint or explicitly waived by human decision with stated
consequences.

## Strategic Vision Relationship

The canonical strategic product vision lives in
`specifications/product-vision.md`. That file defines why 4veco exists, where
it should build advantage, where competitive parity is required, and how
agents should make trade-offs during longer work.

This file remains the canonical operational product end-state: the
student-facing route and completeness definition.

## Change Notes

- 2026-06-06: added the strategic vision relationship after VISION-1 created
  `specifications/product-vision.md` as the canonical strategic product
  vision. Affected surface: specification authority and agent trade-off
  routing. Approval route: VISION-1 at explicit human request. Consequence:
  future work should use product vision for strategic trade-offs and this file
  for operational student-route completeness.
- 2026-05-29: added the shared operational UI requirement after the
  engine-operationalization roadmap report. Affected surface: shared skill-map
  route, task-type shell, practice games, exit-ticket/checkpoint interaction,
  and Scale Gate proof. Approval route: SYNC-4 roadmap/specification update at
  human request. Consequence: future engine work must prove student-visible
  route and task interaction quality, not only contracts, routing, or runtime
  architecture.
- 2026-05-29: corrected exit-ticket semantics from readiness-to-try to
  target-equivalent proof and strengthened exam-ingestion end-product
  integration. Affected surface: exit ticket, completion language, shared
  task-type shell, official-exam target paragraphs, answer models, and Scale
  Gate proof. Approval route: SPEC-ET-1 specification correction at human
  request. Consequence: future exit-ticket work must prove same-level
  operation-chain and answer-form coverage before local paragraph-completion
  language is allowed.
- 2026-05-31: clarified that advisory short checks remain part of the
  intended product route but are separate from target-equivalent exit tickets.
  Affected surface: checkpoint/check route, next-step advice, shared task-type
  shell, exit-ticket semantics, and Scale Gate proof. Approval route:
  GAME-ARCH-1 architecture decision sprint at human request. Consequence:
  short checks may provide local route advice, but they are not a
  target-equivalent proof and may not replace the separate exit ticket.
- 2026-06-01: clarified the product-proof track before Scale Gate 1. Affected
  surface: first-three-paragraph proof, advisory short checks, target-equivalent
  exit tickets, shared route affordance, skill-map product surface,
  task-family coverage, and dual-coding task decisions. Approval route:
  SYNC-PRODUCT-1 roadmap/spec alignment at human request. Consequence:
  Scale Gate 1 must wait for coherent product proof across the first three
  paragraphs or an explicit human waiver with stated consequences.
- 2026-06-01: added structured choice task-family expansion to the shared
  task-type shell baseline. Affected surface: cloze text, multi-select,
  matching pairs, step ordering, two-tier choice, assertion-reason tasks,
  reasoning migration, short checks, and target-equivalent exit-ticket design.
  Approval route: roadmap/spec alignment at human request after the
  multiple-choice family report. Consequence: future task-family work must add
  these as reviewed student actions with schemas, feedback, focus/keyboard
  proof, and product-boundary checks, not as generic quiz variety or weak
  target-proof substitutes.
- 2026-06-03: added context-first shared task source ingestion. Affected
  surface: shared task-type shell, exam/textbook source reconstruction,
  graph/table/source practice, exit-ticket design, and Scale Gate proof.
  Approval route: SYNC-TASK-CONTEXT-INGEST-1 at human request. Consequence:
  source context must be represented as first-class task context blocks before
  task-family questions, with reconstructed tables/SVG/flow/formula blocks and
  source traceability before route adoption.
- 2026-06-01: added constrained construction task-family expansion to the
  shared task-type shell baseline. Affected surface: sentence builders,
  formula builders, cloze tile selection, source-value/source-chain builders,
  label placement, graph/table representation tasks, reasoning migration, and
  exit-ticket operation-chain proof. Approval route: roadmap/spec alignment at
  human request after the constrained-construction task report. Consequence:
  future task-family work must prefer building answers from parts when that
  better matches the target operation, and must not present token/tile
  construction as a shallow recognition game.
- 2026-06-06: clarified shared-task/check-surface integrity after renewed
  human review found that accepted graph-task decisions were not preserved in a
  retry packet. Affected surface: advisory short checks, target-equivalent
  exit-ticket candidates, graph/table task-shell controls, selector
  distractors, and human-review evidence. Approval route:
  CHECKSURFACE-POLICY-REGRESSION-1 at explicit human/lead-review request.
  Consequence: future check-surface proof must show independent surfaces, no
  answer-giving scaffolds, plausible distractors, graph/table action fidelity,
  regression-memory checks, and student-facing quality before a renewed human
  gate.

## End-State Sentence

For every paragraph, 4veco gives the student a visible route from current
readiness to local target-equivalent proof for the paragraph target exercise.

## Product Definition

4veco is an exercise-first, generated, review-gated vwo-economics learning
system in which every paragraph is built backward from the paragraph target
exercise. The student-facing product is not a textbook plus loose companion
games. It is a coherent learning route: the student starts by finding out what
they already can do, receives the explanation and practice route needed to
close the gap, and ends with a target-equivalent proof task that checks whether
they can complete the paragraph target-exercise operation chain at the same
cognitive level with matching answer forms.

At full maturity, every paragraph has two distinct Check surfaces: an advisory
short check for feedback, hints, repair, and local next-step advice; and a
separate target-equivalent exit ticket that proves the paragraph target
exercise can be completed locally and non-summatively. A sprint may leave one
of those surfaces missing only by naming the missing surface as a follow-up or
blocker.

At full maturity, shared tasks use a context-first structure when an exercise
depends on a source: source/context block first, then one or more task-family
questions derived from that context. Context blocks include text stimulus,
source excerpts, semantic tables, reconstructed SVG graphs/figures/flowcharts,
formulas, captions, source labels, alt text, and student-facing references
such as Bron, Tabel, Figuur, Formule, and Schema.

At full maturity, the strongest target exercises are official CvTE-style or
CvTE-derived tasks. Official exam-target paragraphs must trace prompt, source
annexes, figures, tables, graphs, correction model, point allocation,
answer-construction requirements, concepts, calculations, graph/table/source
operations, reasoning steps, and MTU/lesson implications into the paragraph
plan and generated student route.

## Exam-Ingestion End State

At full maturity, official CvTE questions and CvTE-derived questions are not
merely reference data. They are one of the strongest sources for paragraph
target exercises and target-equivalent exit tickets.

For an exam-target paragraph, the student route must trace the official
prompt, source annexes, figures/tables/graphs, correction model, point
allocation, answer-construction requirements, concepts, calculations,
graph/table/source operations, reasoning operations, and answer-writing
requirements into:

- the paragraph plan;
- the explanation;
- the practice route;
- the skill-map route;
- the shared task-type UI;
- the exit ticket;
- the answer model;
- review gates.

The exit ticket for an exam-target paragraph must be target-equivalent to the
exam-style target exercise and must check the operation and answer-form chain
required by the official correction model.

## Shared Operational UI

The student route must be visible as one operational interface, not as separate
engines that only share data behind the scenes.

At full maturity, companion interaction is organized around:

- a shared skill-map / route layer that shows the relevant skill subset,
  current paragraph target, recommended next skill, local practice progress,
  and next practice link without exposing internal MTU or operation codes;
- a shared task-type shell that provides common interaction patterns,
  validation hooks, neutral feedback, retry/self-check behavior, keyboard/focus
  behavior, screenshot-QA expectations, and product-boundary language;
- practice engines for reasoning, math/calculation, graph/table work, and
  target-equivalent checkpoint composition that consume the route layer and
  reuse the task shell where the interaction type overlaps.

The skill map is a student product surface, not only infrastructure. It should
show the relevant paragraph skills, local route, current focus, what each game
or check practises, and an actionable next practice link without exposing
internal codes or claiming mastery.

Visible route items in graph, math, reasoning, and skill-map panels must be
actionable. Each route item should have a student-facing label, purpose, status
or focus, and a direct target action or an explicit fallback. Silent dead route
items are product defects.

The shared task-type shell must support, at minimum, numeric input,
calculation/work capture, final-answer entry, unit/notation fields, short
constructed response, table-value selection, graph reading, point placement or
graph-construction substitute, structured reasoning, step ordering, step/chain
interactions where needed, cloze text, multi-select, matching pairs,
two-tier choice, assertion-reason, cloze tile selection, sentence builders,
formula builders, source-value and source-chain builders, and label-placement
interactions, plus neutral feedback/retry/self-check states.

Structured choice and constrained construction families are not quiz variety.
A new choice-like or construction family is appropriate only when the current
task families cannot represent the student action. It must define the student
action, response shape, validation/evaluation owner, feedback owner, focus and
keyboard behavior, product-boundary flags, and route/checkpoint use case.
Generic choice-only checks may not substitute for calculation, graph/table,
reasoning, or target-equivalent proof unless the target exercise action itself
is genuinely choice-like. Token, tile, word-bank, formula-bank, and label-bank
interactions are valuable only when the fragments force the same reasoning,
formula, source, graph, or answer-construction structure required by the target
exercise.

The task shell is not an exit-ticket-only feature. It is the common interaction
foundation for graph/table practice, math/calculation practice,
target-equivalent exit tickets, and checkpoint-only local checks. Reasoning
practice may use the same shell where constructed response, structured
reasoning, feedback, or self-check behavior overlaps.

Advisory short checks are also part of the end-state route. They are light,
local checks that help a student decide what to do next: practise a named
skill, use a named game, proceed to the exit ticket, or continue for now while
revisiting a weak skill later. A short check is not a target-equivalent proof,
not a grade, not a diagnostic classification, not an automatic sequence
decision, and not a paragraph-completion claim.

Engine architecture is product progress only when a student can see the route,
practise the right task through the right interaction, receive useful local
feedback, and understand what to do next. Architecture-only proof is not enough
for Scale Gate or controlled engine scaling.

## Student Route

### Start

The student begins with an instapquiz or voorkennis check. This is not a grade,
summative diagnostic, mastery decision, or automatic sequencing claim. It
answers: "Where am I now, and what should I do next?"

### Leer

The student receives the core explanation, with stable terminology, canonical
procedures, and dual-coded visuals. Procedures, terminology, visual anchors,
and approaches must remain consistent across textbook, companion pages, games,
practice routes, review records, and answer models.

### Oefen

The student follows a route that fits the learning need. The standard
student-facing exercise block after start exercises is `Zelfstandige oefening`,
not `Verdieping`. The practice layer may include guided practice, procedure
support, reasoning game, old skill-tree math practice, graph/table practice,
differentiated support, optional stretch tasks, or mixed practice.

`Verdieping` may describe optional enrichment outside the core post-start
exercise sequence, but it must not become the default label for normal
independent paragraph exercises.

`Stappenplan` is procedure support. It must not silently replace the primary
math skill-tree practice route where that route is scoped to the paragraph.

Practice engines must make the relevant skill route visible enough for the
student to understand which skill they are practising, why the current game or
task fits the paragraph target, and what next action is useful. A shared
task-type UI should be reused when graph/table, calculation, constructed
response, or checkpoint tasks ask students to perform the same kind of action.

### Check

Every paragraph should eventually include an advisory short check before the
exit ticket. A short check answers: "How is this going, and what should I do
next?" It may give
local, non-binding advice such as practising a named game, going to the exit
ticket, or continuing for now while revisiting a named weak skill later. It may
not claim that the student has proven the paragraph target exercise.

The exit ticket is not merely a short quiz and is separate from the short
check. Its product purpose is to check the same target-exercise operation chain
at the same cognitive level, using answer forms that match the paragraph
target exercise. It is the paragraph target-equivalent proof task.

Short checks and practice routes may use hints, but those hints should be
clickable or collapsed by default. Exit tickets must not expose learning hints,
answer-revealing scaffolding, or teaching-mode feedback before the student
attempts the task unless a later review explicitly approves purely
interface-level help.

Short check and exit-ticket pairs must preserve surface independence. The
short check may sample a lighter local context and route the student to useful
practice; the exit ticket must remain a separate target-equivalent candidate
with its own context, answer form, feedback, and authority flags. Graph/table
check surfaces must ask the student to perform graph/table actions rather than
recognize a visible solution. Controls that contain only correct choices,
intervals, conclusions, labels, or fragments are not valid checks.

If the student completes the exit ticket correctly, the product may say that
the student has demonstrated they can complete the paragraph target exercise or
can now proceed to the paragraph target exercise. This is a local
non-summative paragraph-completion claim, not a grade, diagnostic
classification, adaptive-routing decision, automatic sequencing decision, or
long-term mastery claim.

That means it must cover the paragraph target skills, decompose the target
exercise into operations, test the complete reviewed operation chain at the
same level, use answer forms that match the target exercise, and give neutral
next-step feedback.

Completion language may only become target-equivalent paragraph-completion
language after a reviewed proof standard establishes that coverage. Until then,
checkpoint copy must stay non-summative and local.

The checkpoint should consume the shared task-type shell rather than inventing
separate interaction rules for calculation, graph/table, unit/notation, or
short-response tasks.

### Verdiep

Students who are ready can move into transfer, richer contexts, news or
application work, additional exam-like practice, or broader skill-map views
without crowding the first decision route.

## Non-Negotiable Product Properties

### 1. Exercise-first, not syllabus-first

The target exercise is the anchor. Concepts, procedures, visuals, games, and
explanations are justified by whether they help students solve the target
exercise. For exam-target paragraphs, every official answer-model step must be
taught, practised, scaffolded, marked as prior knowledge, or explicitly out of
scope.

### 2. Route-aware differentiation, not premature adaptive claims

The product may offer different next practice routes based on quiz/check
outcomes, but it may not claim diagnostics, mastery, summative assessment,
automatic sequencing, grading, student-facing AI, PV projection, or PV machine
promotion unless a later explicit gate authorizes those claims.

### 3. Affordance is part of the learning design

A student should always know:

- what to do now;
- what to do next;
- which route fits their current state.

Routing, affordance, cognitive load, visual-instruction alignment,
source-output parity, and procedure fidelity are review criteria, not
decoration.

### 4. Motivation comes from clarity, progress, and achievable challenge

The product should not depend mainly on superficial game elements. It should
motivate by making progress visible, reducing uncertainty, giving a manageable
next step, and keeping the task within reach.

Practice-progress language must remain practice-progress language. It must not
become mastery, grade, pass/fail, diagnostic, or sequencing language by
accident.

### 5. Quality gates inspect actual student-facing output

Passing source checks, validators, or technical QA is not enough. Review gates
must inspect rendered student-facing output and compare it with the original
specification, including economics correctness, learning quality, student
affordance, visual quality, source-output parity, procedure fidelity, and
product-boundary language.

Before Scale Gate 1, the first three paragraphs must be treated as the product
proof set. Review must trace the full student path from landing page through
Start, Leer, Oefen, skill map, practice task, advisory short check, exit
ticket, and next action. Engine architecture, task-shell availability, and a
single approved local `1.1.2` completion copy are not broad product proof.

### 6. Generated, reproducible, source-controlled product

Reusable UI, generators, engines, data contracts, and deploy logic belong in
`C:\Projects\4veco\4veco-platform`. Generated lesson artifacts belong in
`C:\Projects\4veco\4veco-lessen`.

Generated lesson output may not be hand-patched to satisfy a sprint. If a
student-facing output needs to change because of production logic, change the
platform source or handoff the platform work.

### 7. Operational UI proof before engine scaling

Shared contracts, route engines, generators, and task shells must be judged by
student-visible behavior. Before engine scaling, review evidence must show what
the student sees on the landing page, which route opens, which skill subset is
visible, what task is played, what feedback appears, and whether the route
helps the student move toward the paragraph target exercise.

## Paragraph End-State Completeness

A paragraph is not end-state complete merely because files exist. It is
complete when all of the following are true:

- the paragraph plan names the target exercise, target skills, prior
  knowledge, concepts, procedures, visual needs, and practice path;
- the starting quiz identifies relevant starting states and routes students to
  useful next actions;
- the explanation teaches the concepts and procedures needed for the target
  exercise;
- the practice layer gives differentiated routes for weaker, typical, and
  stronger students;
- the exit ticket is a target-equivalent proof task for the target exercise,
  not just recall of isolated facts;
- every answer-model operation in the target exercise is covered somewhere in
  the route as taught, practised, scaffolded, prior knowledge, or explicitly
  out of scope;
- visual artifacts actually contain the visuals needed for the skill being
  taught;
- task design records when text-only is acceptable, when dual coding is
  recommended, and when visual, graph/table, or flow-diagram interaction is
  required;
- the landing page exposes a coherent route:
  `Start -> Leer -> Oefen -> Check -> Verdiep`;
- practice and checkpoint surfaces show the relevant skill route, current task
  purpose, useful feedback, and next action without internal codes;
- graph/table, calculation, constructed-response, and checkpoint interactions
  use the shared task-type shell where the same action is being asked;
- review gates pass for economics correctness, learning quality, student
  affordance, visual quality, source-output parity, and product-boundary
  claims.

## Maturity Labels

These labels must stay distinct:

- **Published paragraph complete:** the generated student-facing paragraph
  exists and passes its applicable validators and reviews.
- **Companion controlled-scope complete:** a bounded companion or game surface
  is accepted for controlled paragraph-limited use.
- **Target-equivalent proof complete:** the route and exit ticket cover the
  target exercise operation and answer-form chain at the same cognitive level
  well enough to say the student has locally demonstrated that they can do the
  paragraph target exercise.
- **Scale-ready:** the product, metadata, review gates, rendered evidence, and
  boundary language are strong enough for broader controlled production.

Calling something a bounded implementation, first reviewed implementation, or
controlled checkpoint may reduce immediate scope, but it does not change the
end-state definition. Missing end-state work must be named and routed to a
follow-up sprint.

## Required Use

Future work that touches paragraph completeness, exit tickets, game-row
architecture, official exam ingestion, Scale Gate 1, or review standards must
cite this file as an acceptance baseline.

At minimum, the following roadmap items must explicitly preserve this
specification:

- `L1.7B-MAP`
- `L1.7B-P23`
- `SPEC-ET-1`
- `EX-LESSON-1`
- `L1.7B-Q2`
- `GATE-L1.7B-Q2`
- `GAME-UX-3A`
- `ENGINE-OP-1`
- `SKILLMAP-OP-1`
- `GRAPH-UX-2`
- `MATH-UX-2`
- `REASON-UX-2`
- `GAME-ARCH-1`
- `GATE-ENGINE-1`
- `REV-STD-1`
- `Scale Gate 1`
- `L-EX0`
- `L-EX1`

## Standing Quality-Log Items

| Issue | Severity | Surface | Next action |
|---|---:|---|---|
| Product end-state was distributed across repository maps, agent prompts, roadmap entries, and sprint plans instead of stated once. | medium-high | platform specs / roadmap / agent prompts | Keep this canonical file linked from lesson and platform operating docs. |
| Exit-ticket target-equivalent proof is specified but not yet implemented in generated output. | high | companion / exit ticket / roadmap | Complete GAME-UX-3A, engine operational proof, Q2 target-equivalent implementation, and GATE-L1.7B-Q2 before using local paragraph-completion language broadly. |
| Shared engine architecture exists before enough student-visible operational proof. | high | game row / skill map / task UI / checkpoint | Run `ENGINE-OP-1`, then implement shared task shell and route visibility work before controlled engine scaling. |
| Exam ingestion end state exists conceptually but not yet as a fully student-routed implementation path. | medium-high | platform references / exam ingestion / lesson route | Run `EX-LESSON-1`, then keep `L-EX0` and `L-EX1` as product-infrastructure work, not just content work. |
| Companion controlled-scope status can be confused with product completeness. | medium | lesson roadmap / reviews | Keep explicit distinction between published paragraph complete, companion controlled-scope complete, target-equivalent proof complete, and scale-ready. |
