# Product End-State Specification

Date: 2026-05-26
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

## End-State Sentence

For every paragraph, 4veco gives the student a visible route from current
readiness to target-exercise readiness.

## Product Definition

4veco is an exercise-first, generated, review-gated vwo-economics learning
system in which every paragraph is built backward from the paragraph target
exercise. The student-facing product is not a textbook plus loose companion
games. It is a coherent learning route: the student starts by finding out what
they already can do, receives the explanation and practice route needed to
close the gap, and ends with a check that determines whether they are ready to
attempt the paragraph target exercise.

At full maturity, the strongest target exercises are official CvTE-style or
CvTE-derived tasks. Official exam-target paragraphs must trace prompt, source
annexes, figures, tables, graphs, correction model, point allocation,
answer-construction requirements, concepts, calculations, graph/table/source
operations, reasoning steps, and MTU/lesson implications into the paragraph
plan and generated student route.

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

The student follows a route that fits the learning need. The practice layer may
include guided practice, procedure support, reasoning game, old skill-tree math
practice, graph/table practice, basis/midden/verrijking, or mixed practice.

`Stappenplan` is procedure support. It must not silently replace the primary
math skill-tree practice route where that route is scoped to the paragraph.

### Check

The exit ticket is not merely a short quiz. Its product purpose is to check
whether the student is ready to try the paragraph target exercise.

That means it must cover the paragraph target skills, decompose the target
exercise into operations, test the operation chain at an appropriate level, use
answer forms that match the skill type, and give neutral next-step feedback.

Completion language may only become target-exercise-readiness language after a
reviewed readiness standard proves that coverage. Until then, checkpoint copy
must stay non-summative and local.

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

### 6. Generated, reproducible, source-controlled product

Reusable UI, generators, engines, data contracts, and deploy logic belong in
`C:\Projects\4veco\4veco-platform`. Generated lesson artifacts belong in
`C:\Projects\4veco\4veco-lessen`.

Generated lesson output may not be hand-patched to satisfy a sprint. If a
student-facing output needs to change because of production logic, change the
platform source or handoff the platform work.

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
- the exit ticket checks readiness for the target exercise, not just recall of
  isolated facts;
- every answer-model operation in the target exercise is covered somewhere in
  the route as taught, practised, scaffolded, prior knowledge, or explicitly
  out of scope;
- visual artifacts actually contain the visuals needed for the skill being
  taught;
- the landing page exposes a coherent route:
  `Start -> Leer -> Oefen -> Check -> Verdiep`;
- review gates pass for economics correctness, learning quality, student
  affordance, visual quality, source-output parity, and product-boundary
  claims.

## Maturity Labels

These labels must stay distinct:

- **Published paragraph complete:** the generated student-facing paragraph
  exists and passes its applicable validators and reviews.
- **Companion-pilot complete:** a bounded companion or game surface is accepted
  for controlled pilot use.
- **Target-exercise-readiness complete:** the route and exit ticket cover the
  target exercise operation chain well enough to say the student is ready to
  try the target exercise.
- **Scale-ready:** the product, metadata, review gates, rendered evidence, and
  boundary language are strong enough for broader controlled production.

Calling something a pilot, MVP, or controlled checkpoint may reduce immediate
scope, but it does not change the end-state definition. Missing end-state work
must be named and routed to a follow-up sprint.

## Required Use

Future work that touches paragraph completeness, exit tickets, game-row
architecture, official exam ingestion, Scale Gate 1, or review standards must
cite this file as an acceptance baseline.

At minimum, the following roadmap items must explicitly preserve this
specification:

- `L1.7B-MAP`
- `L1.7B-P23`
- `L1.7B-Q2`
- `GATE-L1.7B-Q2`
- `REV-STD-1`
- `Scale Gate 1`
- `L-EX0`
- `L-EX1`

## Standing Quality-Log Items

| Issue | Severity | Surface | Next action |
|---|---:|---|---|
| Product end-state was distributed across repository maps, agent prompts, roadmap entries, and sprint plans instead of stated once. | medium-high | platform specs / roadmap / agent prompts | Keep this canonical file linked from lesson and platform operating docs. |
| Exit-ticket semantics are not yet fully target-exercise-readiness evidence. | high | companion / exit ticket / roadmap | Complete metadata alignment and Q2 readiness work before using readiness language broadly. |
| Exam ingestion end state exists conceptually but not as a full ingestion object. | medium-high | platform references / exam ingestion | Keep `L-EX0` and `L-EX1` as product-infrastructure work, not just content work. |
| Companion pilot status can be confused with product completeness. | medium | lesson roadmap / reviews | Keep explicit distinction between published paragraph complete, companion-pilot complete, target-readiness complete, and scale-ready. |
