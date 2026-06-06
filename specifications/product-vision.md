# 4veco Product Vision

Status:

- CANONICAL STRATEGIC PRODUCT VISION.
- Change only by explicit human review.
- This file defines strategic direction and trade-off criteria.
- `product-end-state.md` remains the canonical operational product end-state.

## 1. One-sentence strategic vision

4veco is an open, generated, review-gated economics learning system that gives
students an efficient, understandable route from current readiness to
exam-capable performance, while giving agents a structured repository that
lets them work longer, safer, and at higher quality over time.

## 2. Product promise for students

A student should know where they are, what to do now, and what to do next. If
the required prior knowledge is present, explanations should be short and
clear enough to remove the current blocker without becoming the lesson's new
blocker.

The product should help students practise the actual operations needed for
paragraph target exercises and exams: concepts, calculations, graph/table
reading, source use, reasoning, and answer writing. It should show progress
without claiming diagnostics, grades, long-term mastery, automatic sequencing,
or summative status.

Students should experience 4veco as a usable, clear, motivating learning
route, not as a loose pile of textbook pages and games. The default route is:

`Start -> Leer -> Oefen -> Check -> Verdiep`

## 3. Product promise for teachers and adopters

4veco should remain lean, cloneable, and open-source friendly. The default
adoption path should not require accounts, server-side student data, complex
hosting, SaaS contracts, or privacy/legal overhead that blocks classroom use.

Local storage may be used for local progress and interface state where
allowed, but the product should not depend on personal-data collection. Other
schools, countries, or contexts should be able to clone and adapt the
repository. The default technical posture is static-first unless a later
explicit gate authorizes more complexity with stated consequences.

## 4. Product promise for agents

The repository itself is part of the product. Agents should be able to work
longer and produce higher quality because the repos contain explicit maps,
stable specifications, machine-readable registries, source/generator/output
boundaries, review agents, validators, sprint plans, evidence logs, quality
refs, rendered-output proof requirements, and clear stop conditions.

A task is better when it improves future agent reliability, not only when it
fixes the immediate issue.

## 5. Strategic moat / competitive advantage

The intended moat is not a single feature. It is the combination of semantic
learning decomposition, exam-grounded production, reproducible review gates,
and student-facing usability.

1. Micro Teaching Unit tree as semantic backbone

   MTUs decompose exam skills, concepts, procedures, visual operations,
   answer forms, prior knowledge, and practice needs. The MTU tree should make
   the route from not-yet-ready to exam-ready more efficient than ordinary
   textbook sequencing.

2. Exercise-first and exam-grounded architecture

   Real target exercises and official CvTE-style tasks drive paragraph design.
   Concepts, explanations, visuals, games, and answer models are justified by
   whether they help students solve target exercises.

3. Agent-scalable production system

   Repository design should let agents safely handle longer tasks through
   explicit contracts, source boundaries, validators, evidence logs, and review
   gates.

4. Visual and dual-coding quality

   Graphs, tables, diagrams, flows, formulas, and text should reinforce each
   other. Visuals are instructional objects, not decoration or pasted assets.
   Graphical and dual-coding quality can become a distinct lead over
   competitors.

5. Route affordance and student usability

   Students should not be demotivated by clunky controls, unclear buttons,
   dead route items, or hidden next steps. Affordance is a learning
   requirement, not cosmetic polish.

## 6. Competitive parity rule

Where 4veco does not seek a distinct advantage, it must still be at least as
good as credible alternatives.

Parity areas include basic readability, navigation, correctness, stable
terminology, answer models, accessibility basics, mobile usability,
teacher-facing usability, and generated PDFs/HTML that do not feel broken or
amateurish.

Advantage areas deserve deeper investment. Parity areas cannot be allowed to
become product defects.

## 7. Efficiency principle

The goal is not to cover content by page count. The goal is the shortest
reliable learning path from current readiness to target-exercise and exam
performance.

Efficiency means:

- no unnecessary question steps;
- no bloated scaffolding that obscures the actual task;
- no exercises that do not contribute to the target operation;
- no hidden prerequisite gaps;
- no mechanically easy tasks that create noise instead of learning;
- no route dead ends.

## 8. Understandability principle

A micro teaching unit should normally be explainable in about five minutes
when the required prior knowledge is present.

Explanations should be short enough to avoid becoming blockers, use canonical
terminology, show the relevant representation, connect text, formula,
graph/table, and reasoning where needed, and make the student action clear.

On a Check surface or target-equivalent proof task, understandability must not
turn into answer-giving. Help may clarify the interface, but it may not
silently teach the answer path unless a later explicit review authorizes that
surface as a learning task rather than proof.

## 9. Motivation principle

Motivation should first come from clarity, visible progress, achievable
challenge, and meaningful economics content.

Variation in controls, task forms, games, news contexts, and visuals is useful
only when it supports learning and does not become decorative complexity.

## 10. Diffusion and legal/technical simplicity

These are non-negotiable design pressures:

- static-first;
- no accounts by default;
- no server-side student tracking by default;
- no personal-data dependency;
- localStorage only for local device state/progress where appropriate;
- open-source-friendly licenses and dependencies;
- avoid SaaS lock-in;
- avoid legal/privacy complexity that makes adoption harder;
- keep cloning and local adaptation realistic.

## 11. Boundary rules

The strategic vision does not authorize:

- diagnostics;
- mastery claims;
- automatic sequencing claims;
- summative use;
- student-facing AI;
- PV projection or PV machine promotion;
- Scale Gate authority;

unless a later explicit human gate authorizes the claim with stated
consequences.

Using agents to build and review the repository is not the same as making
student-facing AI part of the product.

## 12. Vision-fit checklist for future work

Every non-trivial sprint plan should answer:

- Which product-vision pillar does this sprint strengthen?
- Is this an advantage area or a parity area?
- What student-visible improvement should result?
- What agent-reliability improvement should result?
- Does this preserve lean diffusion and low legal/technical complexity?
- Does this improve or preserve the efficient route to target-exercise/exam
  performance?
- What proof is required: source diff, generated artifact, rendered
  screenshot, validator, specialist review, human review?
- What remains missing and must be named as blocker, follow-up, or waiver?

## 13. Relationship to other canonical files

- `product-vision.md` = strategic direction and trade-off logic.
- `product-end-state.md` = operational student route and completeness
  definition.
- `companion-core-specifications.md` = companion/game/check/task-shell
  specification.
- Roadmaps = sequencing and current implementation state.
- AGENTS/BUILD docs = operating procedure for agents.
