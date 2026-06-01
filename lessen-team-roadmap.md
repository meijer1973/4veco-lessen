# Lessen Team Roadmap

## Sprint Ledger

The currently-active sprint sits at the top. Future sprints follow in sequence.
Recent closed prerequisites may remain in the ledger for continuity, but they
must not sit above the active sprint. Closed sprints are also recorded in the
"Closed Sprints" section below.
Sprint plans, review records, QA reports, closure logs, and screenshot evidence
for closed work live under `archive/sprints/<sprint-id>/`.

Stable product specifications live in:

- `specifications/product-end-state.md`
- `specifications/companion-core-specifications.md`

Roadmap and sprint updates must not silently weaken those files. Any conflict
requires an explicit specification-change review or a named follow-up sprint
that restores the full product.

## Product Proof Track Before Scale Gate 1

Scale Gate 1 is blocked until the first three paragraphs operate as a coherent
student-visible product. The goal is not more isolated engine progress; the
goal is a route a student can follow:

`Start -> Leer -> Oefen -> Check -> Verdiep`

Core standard:

- every paragraph eventually has both an advisory short check and a separate
  target-equivalent exit ticket;
- short checks may provide hidden/clickable hints, repair feedback, and local
  route advice;
- exit tickets must be same-level proof tasks and must not become hint-heavy
  learning exercises;
- shared task-type UI is the default for overlapping graph/table, calculation,
  reasoning, and checkpoint actions;
- structured choice task families (`cloze_text`, `multi_select`,
  `matching_pairs`, `step_ordering`, `two_tier_choice`, and
  `assertion_reason`) are reviewed student actions, not quiz variety or weak
  substitutes for richer target-operation proof;
- constrained construction task families (`cloze_tile_select`,
  `sentence_builder`, `formula_builder`, `source_value_selection`,
  `source_chain_builder`, and `label_placement`) ask students to build the
  required reasoning, formula, source, graph, or answer chain from parts; they
  are operation-chain proof types, not decorative game formats;
- route items in graph, math, reasoning, and skill-map panels must be
  actionable;
- the skill map must become a visible student product surface;
- dual coding is a task-quality requirement where it improves learning;
- `GATE-PRODUCT-3P` must inspect rendered student paths before Scale Gate 1.

| Sprint | Name | Completed | Current State |
|--------|------|-----------|---------------|
| SYNC-PRODUCT-1 | Product Proof Roadmap Alignment | **2026-06-01** | **CLOSED ROADMAP/SPECIFICATION ALIGNMENT / NO GENERATED OUTPUT.** Platform aligned both roadmaps and stable specs around the Product Proof Track before Scale Gate 1: short check plus target-equivalent exit ticket, shared task UI, visible/actionable skill map, route affordance, dual-coding task decisions, and three-paragraph product proof. No implementation, generated lesson output, diagnostics, adaptive routing, mastery/sequencing, summative use, PV, Scale Gate 1, or product-wide use was authorized. |
| CHECK-SHORT-EXIT-1 | Paragraph Check Surface Inventory And Contract | **2026-06-01** | **CLOSED AUDIT/CONTRACT / NO GENERATED OUTPUT.** Platform inventory records `1.1.1` as advisory `Korte check` only with missing target-equivalent exit ticket, `1.1.2` as reviewed local target-equivalent exit ticket with missing advisory short check, and `1.1.3` as missing both short check and target-equivalent graph/table exit ticket. No generated output, source exit-ticket writes, engine implementation, diagnostics, mastery/sequencing, student-facing AI, summative use, PV, Scale Gate 1, or product-wide use was authorized. |
| STANDARD-EXERCISES-1 | Unified Standard Exercise Coverage Audit | **2026-06-01** | **CLOSED AUDIT/CONTRACT / NO GENERATED OUTPUT.** Platform coverage matrix records math, graph/table, and reviewed `1.1.2` exit-ticket actions as mostly covered by existing shared task-shell families; `structured_short_response` is runtime-supported but needs standard documentation and UX hardening; reasoning requires standard expansion for step ordering, causal chains, claim/reason/evidence, flow diagrams, classification with explanation, and source-based explanation. Guided practice and procedure support remain learning/support surfaces, not target-equivalent proof. No generated output, implementation, diagnostics, adaptive routing, mastery/sequencing, summative use, PV, Scale Gate 1, or product-wide use was authorized. |
| TASK-SHELL-UX-2 | Shared Task Shell UX Hardening | **2026-06-01** | **CLOSED PASS WITH FLAGS / GENERATED OUTPUT THROUGH PLATFORM DEPLOY ONLY.** Platform added separate unit/notation fields for calculation-work tasks, hidden/collapsible task-shell hints where allowed, controlled labelled feedback regions, and exit-ticket display rules that suppress pre-attempt criteria and answer-revealing placeholders while keeping source criteria for validation. Generated Book 1 shared output was refreshed through deploy only. Flags: improve future screenshot manifest DOM proof, continue reasoning standard expansion in `REASON-STD-1`, and preserve source/render boundaries in future exit tickets. No target-equivalent authority was broadened; `1.1.1` remains advisory, `1.1.3` exit-ticket source remains absent, and no diagnostics, mastery/sequencing, PV, Scale Gate 1, or product-wide use is authorized. |
| TASK-FAMILY-CHOICE-1 | Structured Choice Task-Family Contract | **2026-06-01** | **CLOSED CONTRACT / NO IMPLEMENTATION OR GENERATED OUTPUT.** Platform defined shared-shell contracts for `cloze_text`, `multi_select`, `matching_pairs`, `step_ordering`, `two_tier_choice`, and `assertion_reason`, including response shapes, validation/evaluation owners, feedback owners, focus/keyboard expectations, use cases, and target-proof limits. No engine implementation, generated output, target-equivalent reliance, diagnostics, mastery/sequencing, PV, Scale Gate 1, or product-wide use was authorized. |
| TASK-FAMILY-CONSTRUCT-1 | Constrained Construction Task-Family Contract | **2026-06-01** | **CLOSED CONTRACT / NO IMPLEMENTATION OR GENERATED OUTPUT.** Platform defined construction contracts for `cloze_tile_select`, `sentence_builder`, `formula_builder`, `source_value_selection`, `source_chain_builder`, and `label_placement`, including token/tile-bank rules, distractor policy, ordering/placement semantics, accessibility expectations, use cases, and operation-chain proof limits. No engine implementation, generated output, target-equivalent reliance, diagnostics, mastery/sequencing, PV, Scale Gate 1, or product-wide use was authorized. |
| TASK-FAMILY-CLOZE-TILE-1 | Cloze Tile-Select Task-Family Implementation | **2026-06-01** | **CLOSED PASS WITH FLAGS / NO GENERATED LESSON OUTPUT.** Platform added `cloze_tile_select` as a deterministic shared task-shell family with inline blanks, selectable tile bank, distractor validation, default no-reuse behavior, exact `{ blanks }` response matching, shared UI helpers, wrapper collection support, focused tests, rendered report fixture, proof JSON, and checker. Flags: unrelated `knowledge/exit-ticket-game-1.1.1.zip` remains unstaged/out of scope; product-route screenshots remain required before adoption. No source-data writes, generated output, target-equivalent reliance, diagnostics, mastery/sequencing, PV, Scale Gate 1, or product-wide use was authorized. |
| TASK-FAMILY-SENTENCE-1 | Sentence Builder Task-Family Implementation | **2026-06-01** | **CLOSED PASS WITH FLAGS / NO GENERATED LESSON OUTPUT.** Platform added `sentence_builder` as a deterministic shared task-shell family with fragment bank, ordered construction zone, clear/remove/reorder controls, distractor validation, default no-reuse behavior, exact `{ tokens }` response matching, shared UI helpers, wrapper collection support, focused tests, rendered report fixture, proof JSON, and checker. Flags: unrelated `knowledge/exit-ticket-game-1.1.1.zip` remains unstaged/out of scope; product-route screenshots and rendered interaction proof remain required before adoption. No source-data writes, generated output, target-equivalent reliance, diagnostics, mastery/sequencing, PV, Scale Gate 1, or product-wide use was authorized. |
| TASK-FAMILY-FORMULA-1 | Formula Builder Task-Family Implementation | no | Platform adds `formula_builder` so students construct formulas from symbols or terms before calculation work, including percentage change, index numbers, elasticity, revenue, profit, and later marginal/average procedures. |
| TASK-FAMILY-CLOZE-1 | Cloze Text Task-Family Implementation | no | Platform adds inline `cloze_text` as the highest-priority bridge between recognition and open response, with proof for index-points-versus-percent, formula substitution, source-value labels, and causal statements. |
| TASK-FAMILY-MULTI-1 | Multi-Select Task-Family Implementation | no | Platform adds `multi_select` with exact-set matching, practice-only partial self-check where approved, and feedback for missing required options or selected distractors. |
| TASK-FAMILY-ORDER-1 | Step-Ordering Task-Family Implementation | no | Platform adds shared `step_ordering` for procedure-control and reasoning-sequence tasks so reasoning can migrate out of private engine-only ordering logic. |
| TASK-FAMILY-SOURCE-1 | Source Value And Chain Builder Implementation | no | Platform adds `source_value_selection` and `source_chain_builder` so students select multiple source/table/graph values and label them as old/new, x/y, price/quantity, cause/effect, or source-to-operation-to-answer chains. |
| TASK-FAMILY-LABEL-1 | Label-Placement Task-Family Implementation | no | Platform adds `label_placement` for graph, table, formula, and representation tasks such as axes, lines, intersections, units, index labels, and curve-shift components. Requires visual, keyboard/focus, mobile, and dark-mode proof. |
| TASK-FAMILY-MATCH-1 | Matching-Pairs Task-Family Implementation | no | Platform adds `matching_pairs` for concept/definition, graph-element/meaning, source-value/label, formula-component/interpretation, and event/curve-shift tasks. |
| TASK-FAMILY-TWO-TIER-1 | Two-Tier Choice Task-Family Implementation | no | Platform adds answer-plus-reason `two_tier_choice` for misconception repair and explanation-quality feedback without diagnostics or mastery claims. |
| TASK-FAMILY-ASSERTION-1 | Assertion-Reason Task-Family Implementation | no | Platform adds `assertion_reason` only after the higher-priority families exist; it must remain a reviewed compact reasoning task, not default quiz variety. |
| GATE-TASK-FAMILY-1 | Structured Choice And Construction Task-Family Review | no | Human/lead review of rendered output, feedback, schema/validation, focus/keyboard behavior, and target-proof boundaries before these structured choice or construction families are relied on in reasoning migration, check implementation, product proof, or Scale Gate 1. |
| GAME-ROUTE-AFFORDANCE-1 | Clickable Route Items For Non-Exit Practice Games | no | Make graph/math/reasoning/skill-map route items actionable. Preserve existing `1.1.2` exit-ticket route links and add regression guard. |
| SKILLMAP-PRODUCT-1 | Student Skill Map Product Surface | no | Make the skill map accessible and useful as a student-facing route overview for the first three paragraphs. |
| REASON-STD-1 | Reasoning Game Unified Exercise Migration | no | Bring reasoning task types into the shared standard, including step-by-step and flow-diagram tasks; decide refactor versus rebuild. |
| DUAL-CODING-STD-1 | Dual-Coding Exercise Standard | no | Require task authors and reviewers to decide when visual, graph/table, or flow-diagram interaction is needed. |
| ENGINE-UNIFY-1 | Unified Engine Experience Refactor Plan | no | Decide keep/wrap/refactor/rebuild/deprecate for graph, math, reasoning, check, route, hint, feedback, and accessibility models around the shared route and task shell. |
| CHECK-SHORT-EXIT-2 | Implement Both Check Types For First Three Paragraphs | no | Ensure `1.1.1`-`1.1.3` each have an advisory short check and target-equivalent exit ticket, or explicit blockers. |
| SCALE-PROOF-3P | Three-Paragraph Product Proof | no | Produce student-path proof for landing, Start, Leer, Oefen, skill map, practice task, advisory short check, target-equivalent exit ticket, feedback, and next action for `1.1.1`-`1.1.3`. |
| GATE-PRODUCT-3P | Human Product Readiness Review | no | Human review of the three-paragraph product before Scale Gate 1. PASS WITH FLAGS may not carry missing core product requirements. |
| Scale Gate 1 | Foundation Hardening Scale Gate | no | Blocked until the Product Proof Track closes or a human waiver explicitly records consequences. |

## Engine Operationalization Track

The next engine work must prove student-visible operational progress, not only
contract or runtime architecture. The required sequence is:

```text
GATE-MTU-H4 (closed PASS WITH CONDITIONS for routing only)
-> MTU-H4A (closed planning packet)
-> GATE-MTU-H4A (closed PASS WITH CONDITIONS)
-> MTU-H4B (closed execution packet)
-> GATE-MTU-H4B (closed PASS WITH CONDITIONS)
-> MTU-H4C (closed bounded execution)
-> SPEC-ET-1 (closed specification correction)
-> EX-LESSON-1 (closed route-trace handoff)
-> GAME-UX-3A (closed shared task-shell foundation)
-> ENGINE-OP-1 (closed operational proof audit with flags)
-> SKILLMAP-OP-1 (closed student-visible route)
-> LEAD-REVIEW-1 (closed process repair)
-> LEAD-REVIEW-2 (closed strict validation hardening)
-> GRAPH-UX-2 (closed graph/task-shell integration)
-> MATH-UX-2 (closed math/task-shell integration)
-> REASON-UX-2 (closed reasoning/task-shell integration)
-> GAME-ARCH-1 (closed architecture decision)
-> GAME-ARCH-2 (closed architecture plan)
-> GATE-ENGINE-1 (closed PASS WITH FLAGS)
-> GRAPH-REFINE-1 (closed planning/preparation with flags)
-> MATH-REFINE-1 (closed planning/preparation with flags)
-> REASON-REFINE-1 (closed planning/preparation with flags)
-> CHECK-Q2-PLAN (closed planning/preparation with flags)
-> L1.7B-Q2 (closed implementation candidate with flags; completion copy held)
-> GATE-L1.7B-Q2 (closed PASS WITH FLAGS; exact 1.1.2 copy packet authorized)
-> L1.7B-Q2-COPY (closed exact 1.1.2 copy enablement)
-> SYNC-PRODUCT-1 (closed product-proof roadmap/spec alignment)
-> CHECK-SHORT-EXIT-1 (closed audit/contract)
-> STANDARD-EXERCISES-1 (closed audit/contract)
-> TASK-SHELL-UX-2 (closed implementation/proof)
-> TASK-FAMILY-CHOICE-1
-> TASK-FAMILY-CONSTRUCT-1
-> TASK-FAMILY-CLOZE-TILE-1 (closed PASS WITH FLAGS)
-> TASK-FAMILY-SENTENCE-1 (closed PASS WITH FLAGS)
-> TASK-FAMILY-FORMULA-1
-> TASK-FAMILY-CLOZE-1
-> TASK-FAMILY-MULTI-1
-> TASK-FAMILY-ORDER-1
-> TASK-FAMILY-SOURCE-1
-> TASK-FAMILY-LABEL-1
-> TASK-FAMILY-MATCH-1
-> TASK-FAMILY-TWO-TIER-1
-> TASK-FAMILY-ASSERTION-1
-> GATE-TASK-FAMILY-1
-> GAME-ROUTE-AFFORDANCE-1
-> SKILLMAP-PRODUCT-1
-> REASON-STD-1
-> DUAL-CODING-STD-1
-> ENGINE-UNIFY-1
-> CHECK-SHORT-EXIT-2
-> SCALE-PROOF-3P
-> GATE-PRODUCT-3P
-> REV-STD-1
-> Scale Gate 1
```

Scale Gate 1 may not treat the four-engine architecture as product progress
unless a student can see a coherent route, practise through the correct task
interface, receive useful neutral feedback, and understand the next action.
It also may not run until the Product Proof Track reaches `GATE-PRODUCT-3P`
or a human waiver explicitly records consequences.

| Sprint | Name | Completed | Current State |
|--------|------|-----------|---------------|
| TASK-SHELL-UX-2 | Shared Task Shell UX Hardening | **2026-06-01** | **CLOSED PASS WITH FLAGS / GENERATED OUTPUT THROUGH PLATFORM DEPLOY ONLY.** Platform produced `reports/sprints/TASK-SHELL-UX-2-ui-contract.md`, screenshot proof, `reports/json/task-shell-ux2-proof.json`, and checker `build-scripts/sprints/check-task-shell-ux2.js`. It added unit/notation support, controlled feedback, hidden hints where allowed, and exit-ticket display suppression for criteria/answer placeholders. Round-1 lead review returned REVISE for placeholder leaks; round 2 passed after correction. Records: platform `reports/sprints/TASK-SHELL-UX-2-result.md`. |
| TASK-FAMILY-CHOICE-1 | Structured Choice Task-Family Contract | **2026-06-01** | **CLOSED CONTRACT / NO IMPLEMENTATION OR GENERATED OUTPUT.** Platform produced `reports/sprints/TASK-FAMILY-CHOICE-1-contract.md`, `reports/json/task-family-choice-contract.json`, and checker `build-scripts/sprints/check-task-family-choice1-contract.js`. Records: platform `reports/sprints/TASK-FAMILY-CHOICE-1-result.md`. |
| TASK-FAMILY-CONSTRUCT-1 | Constrained Construction Task-Family Contract | **2026-06-01** | **CLOSED CONTRACT / NO IMPLEMENTATION OR GENERATED OUTPUT.** Platform produced `reports/sprints/TASK-FAMILY-CONSTRUCT-1-contract.md`, `reports/json/task-family-construction-contract.json`, and checker `build-scripts/sprints/check-task-family-construct1-contract.js`. Records: platform `reports/sprints/TASK-FAMILY-CONSTRUCT-1-result.md`. |
| TASK-FAMILY-CLOZE-TILE-1 | Cloze Tile-Select Task-Family Implementation | **2026-06-01** | **CLOSED PASS WITH FLAGS / NO GENERATED LESSON OUTPUT.** Platform implemented selectable-tile cloze runtime support and proof artifacts only. Product-route adoption and screenshots remain later work. Records: platform `reports/sprints/TASK-FAMILY-CLOZE-TILE-1-result.md`. |
| TASK-FAMILY-SENTENCE-1 | Sentence Builder Task-Family Implementation | **2026-06-01** | **CLOSED PASS WITH FLAGS / NO GENERATED LESSON OUTPUT.** Platform implemented sentence and causal-chain building from word or fragment banks with strict token-sequence validation and shared-shell wrapper support. Product-route adoption and screenshots remain later work. Records: platform `reports/sprints/TASK-FAMILY-SENTENCE-1-result.md`. |
| TASK-FAMILY-FORMULA-1 | Formula Builder Task-Family Implementation | no | Platform implementation sprint for formula construction from formula blocks or symbols before calculation-work tasks. |
| TASK-FAMILY-CLOZE-1 | Cloze Text Task-Family Implementation | no | Platform implementation sprint for inline cloze text as the first bridge between recognition and constructed response. |
| TASK-FAMILY-MULTI-1 | Multi-Select Task-Family Implementation | no | Platform implementation sprint for multi-select tasks with exact set matching and approved practice-only partial feedback. |
| TASK-FAMILY-ORDER-1 | Step-Ordering Task-Family Implementation | no | Platform implementation sprint for shared step-ordering tasks needed by procedure and reasoning standardization. |
| TASK-FAMILY-SOURCE-1 | Source Value And Chain Builder Implementation | no | Platform implementation sprint for multi-value source selection plus source-to-value-to-operation-to-answer chain construction for graph/table/source tasks. |
| TASK-FAMILY-LABEL-1 | Label-Placement Task-Family Implementation | no | Platform implementation sprint for graph, formula, and representation label-placement interactions with visual and keyboard/focus proof. |
| TASK-FAMILY-MATCH-1 | Matching-Pairs Task-Family Implementation | no | Platform implementation sprint for matching-pairs tasks with accessible rendered proof. |
| TASK-FAMILY-TWO-TIER-1 | Two-Tier Choice Task-Family Implementation | no | Platform implementation sprint for answer-plus-reason tasks used for misconception repair without diagnostics or mastery claims. |
| TASK-FAMILY-ASSERTION-1 | Assertion-Reason Task-Family Implementation | no | Platform implementation sprint for compact assertion-reason reasoning checks after higher-priority families exist. |
| GATE-TASK-FAMILY-1 | Structured Choice And Construction Task-Family Review | no | Review rendered output and boundaries before structured choice or construction families are used for reasoning migration, check implementation, product proof, or Scale Gate 1. |
| STANDARD-EXERCISES-1 | Unified Standard Exercise Coverage Audit | **2026-06-01** | **CLOSED AUDIT/CONTRACT / NO GENERATED OUTPUT.** Platform produced `reports/sprints/STANDARD-EXERCISES-1-exercise-family-audit.md`, `reports/json/standard-exercise-family-coverage.json`, and checker `build-scripts/sprints/check-standard-exercises1-coverage.js`. It keeps shared task-shell coverage for math, graph/table, and reviewed `1.1.2` exit-ticket actions, flags `structured_short_response` for documentation/UX hardening, routes missing reasoning families to `REASON-STD-1`, and keeps guided practice/procedure support outside target-equivalent proof. Records: platform `reports/sprints/STANDARD-EXERCISES-1-result.md`. |
| CHECK-SHORT-EXIT-1 | Paragraph Check Surface Inventory And Contract | **2026-06-01** | **CLOSED AUDIT/CONTRACT / NO GENERATED OUTPUT.** Platform produced the first three paragraph check-surface inventory. Findings: `1.1.1` has only advisory `Korte check` and lacks target-equivalent A43/B01/B02 proof; `1.1.2` has approved local target-equivalent proof/copy and lacks a separate advisory short check; `1.1.3` lacks both check surfaces and still needs graph/table target-equivalent proof work. Records: platform `reports/sprints/CHECK-SHORT-EXIT-1-result.md`. |
| SYNC-PRODUCT-1 | Product Proof Roadmap Alignment | **2026-06-01** | **CLOSED ROADMAP/SPECIFICATION ALIGNMENT / NO GENERATED OUTPUT.** Platform aligned the roadmaps and stable specs around the next Product Proof Track before Scale Gate 1. It makes explicit that every paragraph eventually needs both an advisory short check and separate target-equivalent exit ticket, non-exit route items need actions, the skill map is a student product surface, dual coding is a task-quality decision, and the first three paragraphs must pass product proof before Scale Gate 1. No implementation, generated output, diagnostics, adaptive routing, mastery/sequencing, summative use, PV, Scale Gate 1, or product-wide use was authorized. Records: platform `reports/sprints/SYNC-PRODUCT-1-result.md`. |
| MATH-UX-2 | Math Game + Checkpoint UI Integration | **2026-05-31** | **CLOSED LIVE MATH/CALCULATION TASK-SHELL INTEGRATION / GENERATED OUTPUT THROUGH PLATFORM DEPLOY ONLY.** Platform integrated the GAME-UX-3A shared task shell into the generated Book 1 `1.1.2` math route. `A38` and `A39` now cover numeric input, calculation/work capture, final-answer entry, percentage/index notation, and unit/notation field behavior through validated task-shell families, with labelled retry/self-check feedback and desktop/mobile light/dark screenshot proof. Checkpoint-style calculation tasks are proven by a non-published fixture using `ExitTicketEngine`/`ExitTicketUI` with `targetReadinessEvidence: false`; no `1.1.2` exit-ticket source or page was created. This closes calculation UI integration only; it authorizes no target-equivalent completion language, diagnostics, adaptive routing, mastery/sequencing, summative use, PV, Scale Gate 1, or student/product use. Records: `archive/sprints/MATH-UX-2/`. |
| GRAPH-UX-2 | Graph Game + Checkpoint UI Integration | **2026-05-31** | **CLOSED LIVE GRAPH/TABLE TASK-SHELL INTEGRATION / GENERATED OUTPUT THROUGH PLATFORM DEPLOY ONLY.** Platform integrated the GAME-UX-3A shared task shell into the generated Book 1 `1.1.3` graph route. The route now covers table-value selection, graph reading, economic axis convention, interpolation, point placement, graph-construction substitute, calculation/work capture, and a less-labelled graph variant, with the route panel visible before task controls on mobile. Checkpoint-style graph tasks are proven by a non-published fixture using `ExitTicketEngine`/`ExitTicketUI` with `targetReadinessEvidence: false`; no `1.1.3` exit-ticket source or page was created. This closes graph/table UI integration only; it authorizes no target-equivalent completion language, diagnostics, adaptive routing, mastery/sequencing, summative use, PV, Scale Gate 1, or student/product use. Records: `archive/sprints/GRAPH-UX-2/`. |
| SKILLMAP-OP-1 | Student-Visible Skill-Map Route | **2026-05-31** | **CLOSED LIVE ROUTE-VISIBILITY SPRINT / GENERATED OUTPUT THROUGH PLATFORM DEPLOY ONLY.** Platform added a route-display catalog, per-surface route scopes for Book 1 `1.1.1`, `1.1.2`, and `1.1.3`, shared route panels in reasoning, graph/table, procedure support, and math/calculation surfaces, and desktop/mobile screenshot proof. Students now see paragraph target, recommended focus, local progress, and practice action without internal MTU codes. This closes route visibility only; it authorizes no target-equivalent completion language, diagnostics, adaptive routing, mastery/sequencing, summative use, PV, Scale Gate 1, or student/product use. Records: `archive/sprints/SKILLMAP-OP-1/`. |
| ENGINE-OP-1 | Four-Engine Operational Proof Audit | **2026-05-31** | **CLOSED AUDIT / PASS WITH FLAGS FOR EVIDENCE ONLY.** Platform produced screenshots, a screenshot manifest, student-path trace, and operational audit for `1.1.1`, `1.1.2`, and `1.1.3` without mutating generated lesson output or protected references. Findings: `1.1.3` graph practice is the strongest current operational route and gives neutral source/value/calculation feedback; `1.1.2` math practice is restored and scoped; `1.1.1` check remains a local short check only; generated output does not yet use the GAME-UX-3A shared task shell; `1.1.2` and `1.1.3` have no target-equivalent checkpoint route; and shared skill-map route panels are empty or mis-scoped in several places. Records: `archive/sprints/ENGINE-OP-1/`. |
| GAME-UX-3A | Shared Task-Type UX Foundation | **2026-05-30** | **CLOSED PLATFORM RUNTIME FOUNDATION / NO GENERATED LESSON OUTPUT.** Platform added a shared task-shell engine, static UI renderer, CSS, exit-ticket shell load hooks, deploy copy support, focused tests, fixtures, and closure records. Supported task families now include numeric input, calculation/work capture, final-answer entry, unit/notation field, short constructed response, table-value selection, graph reading, point placement, graph-construction substitute, and structured reasoning. The shell preserves neutral feedback, retry/self-check states, keyboard/focus hooks, and no mastery, diagnostic, sequencing, summative, AI, PV, or product-use claims. ENGINE-OP-1 proved that generated output did not yet use the shell; GRAPH-UX-2, MATH-UX-2, and REASON-UX-2 have since integrated it into live graph/table, math/calculation, and reasoning routes. `L1.7B-Q2` and `GATE-L1.7B-Q2` still own target-equivalent checkpoint status. Records: `archive/sprints/GAME-UX-3A/`. |
| EX-LESSON-1 | Exam-Ingestion End-State Integration | **2026-05-30** | **CLOSED HANDOFF / NO GENERATED OUTPUT.** Updated paragraph-plan requirements, paragraph-build guidance, companion/textbook authoring guidance, and review prompts so official CvTE and CvTE-derived target exercises trace prompt, source annexes, graphs/tables/figures, correction model, point allocation, answer-construction requirements, concepts, calculations, graph/table/source operations, reasoning operations, and answer-writing requirements into the explanation, skill-map route, shared task shell, target-equivalent exit ticket, and answer model. Produced the platform EX-LESSON-1 exam-target route checklist. This closes the route-trace handoff only; it authorizes no generated output, protected reference mutation, target-exercise mutation, diagnostics, mastery, sequencing, summative use, PV, Scale Gate 1, or student/product use. Records: `archive/sprints/EX-LESSON-1/`. |
| MTU-H4C | Answer-Form Bounded CLI Execution | **2026-05-30** | **CLOSED PLATFORM REFERENCE EXECUTION / NO LESSON OUTPUT.** Platform added `A80`, `A81`, and `A96`-`A99` through governed `unit-add.js` execution and rebuilt generator readiness. The new answer-form units remain generator-blocked/non-interactive until later generator implementation or no-exposure design authorizes use. No target-exercise `question_type`/`answer_form` fields, candidate storage, candidate writes, generated lesson output, diagnostics, mastery, sequencing, summative use, PV, Scale Gate 1, or student/product use were authorized. |
| REASON-UX-2 | Reasoning Game Variant And Feedback Upgrade | **2026-05-31** | **CLOSED LIVE REASONING TASK-SHELL INTEGRATION / GENERATED OUTPUT THROUGH PLATFORM DEPLOY ONLY.** Platform added a sixth reasoning mode, `Redeneerantwoord opbouwen`, using the GAME-UX-3A `structured_reasoning` task shell. Existing reasoning modes now give richer repair feedback with example chains and selected-answer comparison, while mode 5 remains self-check-only and does not count as persistent `goed` progress. The sprint produced desktop/mobile light/dark screenshot proof, route-output checks, student-experience review, accessibility review, and a real lead-review cycle that caught and repaired a UI scoping regression. This closes reasoning UI integration only; it authorizes no target-equivalent completion language, diagnostics, adaptive routing, mastery/sequencing, summative use, PV, Scale Gate 1, or student/product use. Records: `archive/sprints/REASON-UX-2/`. |
| GAME-ARCH-1 | Practice Engine Build-vs-Rebuild Decision | **2026-05-31** | **CLOSED NO-GENERATED-OUTPUT ARCHITECTURE DECISION.** Platform decided a full immediate rebuild is not justified, but continued local patching is not safe without `GAME-ARCH-2`. Keep and harden the shared route layer; keep the shared task shell; keep/refactor graph/table practice as the reference pattern; refactor math around target-exercise operation chains; refactor reasoning around answer-form and constructed-response standards; keep the short check as advisory only; keep the target-equivalent exit ticket separate; rebuild or remove duplicate engine-specific UI/state/feedback paths only through a later governed plan when they cannot consume the shared route and task shell cleanly. No generated output, target-equivalent completion language, diagnostics, adaptive routing, mastery/sequencing, summative use, PV, Scale Gate 1, or student/product use was authorized. Records: `archive/sprints/GAME-ARCH-1/`. |
| GAME-ARCH-2 | Integrated Practice Engine Architecture Plan | **2026-05-31** | **CLOSED NO-IMPLEMENTATION ARCHITECTURE PLAN.** Platform produced the canonical architecture map, route-layer API, task-shell API, module-boundary plan, file-level keep/wrap/deprecate/rebuild inventory, state ownership rules, feedback ownership rules, target-operation coverage model for `1.1.1`/`1.1.2`/`1.1.3`, and `GATE-ENGINE-1` live-output checklist. Lead review caught and corrected a missing route-engine inventory item: `engines/skill-map-engine.js` is now named as the shared route request/view-model owner. The sprint preserves advisory short checks as separate from target-equivalent exit tickets and authorizes no generated output, engine implementation, target-equivalent claims, diagnostics, adaptive routing, mastery, sequencing, student-facing AI, summative use, PV, Scale Gate 1, or product use. Records: `archive/sprints/GAME-ARCH-2/`. |
| GATE-ENGINE-1 | Four-Engine Operational Integration Review | **2026-05-31** | **CLOSED PASS WITH FLAGS / NO IMPLEMENTATION OR PRODUCT AUTHORITY.** Platform reviewed live rendered output and GAME-ARCH-2 evidence for the shared route layer, shared task shell, graph/table route, math/calculation route, reasoning route, advisory short check, and target-equivalent exit-ticket boundary. Decision: keep and harden shared route; keep shared task shell as default interaction layer; keep/refactor graph as reference pattern; refactor math around `1.1.2` target-operation chain; refactor reasoning around answer-form and constructed-response standards; keep/relabel advisory short check if needed; keep target-equivalent exit tickets separate and held for `L1.7B-Q2`/`GATE-L1.7B-Q2`. Authorized only named planning/preparation sprints. No generated output, implementation, target-equivalent completion language, diagnostics, adaptive routing, mastery/sequencing, summative use, PV, Scale Gate 1, or student/product use was authorized. Records: platform `reports/review-gates/GATE-ENGINE-1-four-engine-operational-integration/`. |
| GRAPH-REFINE-1 | Graph Route Operation-Chain Hardening Plan | **2026-05-31** | **CLOSED PLATFORM PLANNING/PREPARATION ONLY / PASS WITH FLAGS.** Platform kept GRAPH-UX-2 as useful local graph/table practice and the strongest current reference pattern, but found target-equivalent graph reliance blocked: the `1.1.3` target exercise requires price on the vertical axis and quantity on the horizontal axis, while current graph-route data contains contradictory price-as-horizontal/x wording. A later `GRAPH-REFINE-2` repair is recommended only if explicitly authorized. No implementation, generated output, target-equivalent claims, diagnostics, mastery/sequencing, Scale Gate 1, or product use was authorized. Records: platform `reports/sprints/GRAPH-REFINE-1-result.md`. |
| MATH-REFINE-1 | Math Target-Operation-Chain Hardening Plan | **2026-05-31** | **CLOSED PLATFORM PLANNING/PREPARATION ONLY / PASS WITH FLAGS.** Platform kept MATH-UX-2 as useful local A38/A39 math/calculation practice and confirmed the route should be refactored rather than rebuilt, but found target-equivalent `1.1.2` reliance blocked until explicit D31 coverage is routed and checked: the target exercise requires old/new percentage change, price-index calculation, index-to-index percentage change, and a short explanation that 108 to 112 is 4 index points, not 4 percent. A later `MATH-REFINE-2` repair is recommended only if explicitly authorized. No implementation, generated output, target-equivalent claims, diagnostics, mastery/sequencing, Scale Gate 1, or product use was authorized. Records: platform `reports/sprints/MATH-REFINE-1-result.md`. |
| REASON-REFINE-1 | Reasoning Answer-Form Integration Plan | **2026-05-31** | **CLOSED PLATFORM PLANNING/PREPARATION ONLY / PASS WITH FLAGS.** Platform kept the reasoning route and shared `structured_reasoning` task family as useful local practice, but found target-equivalent reasoning reliance blocked until answer-form-specific scaffolds are added and reviewed: generic self-check is not answer-form proof, `1.1.1` needs an A98 versus held-evaluation decision, `1.1.2` D31 explanation must coordinate with math/D31 coverage, and `1.1.3` source/table reasoning needs A81 source-use scaffolding plus graph-axis repair. No implementation, generated output, reasoning CSV edits, target-equivalent claims, diagnostics, mastery/sequencing, Scale Gate 1, or product use was authorized. Records: platform `reports/sprints/REASON-REFINE-1-result.md`. |
| CHECK-Q2-PLAN | Target-Equivalent Exit-Ticket Implementation Plan | **2026-05-31** | **CLOSED PLATFORM/LESSON PLANNING/PREPARATION ONLY / PASS WITH FLAGS.** Platform prepared the target-equivalent exit-ticket implementation plan while preserving advisory short checks as separate local advice surfaces. The plan confirms no current `1.1.1`, `1.1.2`, or `1.1.3` output is target-equivalent proof: `1.1.1` needs full A43 coverage plus an A98 versus held-evaluation decision; `1.1.2` needs explicit D31 index-point versus percentage-change coverage; `1.1.3` needs graph-axis repair and A81 source-use plus underlying answer-form coverage. Later `L1.7B-Q2` must select one paragraph and resolve or explicitly scope its blockers before implementation. No exit-ticket implementation, source-data writes, generated output, paragraph-completion language, diagnostics, mastery/sequencing, Scale Gate 1, or product use was authorized. Records: platform `reports/sprints/CHECK-Q2-PLAN-result.md`. |
| L1.7B-Q2 | Exit Ticket Target-Equivalent Implementation | **2026-06-01** | **CLOSED IMPLEMENTATION CANDIDATE / PASS WITH FLAGS / COMPLETION COPY HELD.** Platform implemented `1.1.2 Percentages en indexcijfers` as the first target-equivalent exit-ticket candidate. It checks the same target-exercise operation chain at the same cognitive level: percentage change, price-index calculation, index-to-index percentage change, and D31 index points versus percent. The sprint added source-controlled exit-ticket data, generated Book 1 output through platform deploy only, updated landing/page copy to `Exit ticket`, kept the existing `1.1.1` `Korte check` advisory-only, and captured desktop/mobile/dark/completion screenshots. Lead review round 1 returned REVISE for bogus calculation-work and contradictory-D31 matching; round 2 passed after required work-text groups, reject-text criteria, adversarial tests, and refreshed evidence. Carried flag: deterministic text-group matching is not symbolic math parsing or semantic language understanding, so `GATE-L1.7B-Q2` must explicitly review criterion sufficiency before local paragraph-completion language. No target-equivalent completion language, diagnostics, adaptive routing, mastery/sequencing, summative use, PV, Scale Gate 1, or product use was authorized. Records: platform `reports/sprints/L1.7B-Q2-result.md`. |
| GATE-L1.7B-Q2 | Exit Ticket Target-Equivalent Proof Review | **2026-06-01** | **CLOSED PASS WITH FLAGS / EXACT 1.1.2 COPY PACKET AUTHORIZED ONLY.** Platform reviewed the implemented `1.1.2 Percentages en indexcijfers` target-equivalent exit-ticket candidate and accepted the evidence baseline, full operation-chain coverage, calculation-work criteria, D31 criteria, UI/feedback, and advisory short-check boundary. Approved local non-summative copy for a later exact implementation packet only: `Je hebt laten zien dat je de eindopgave van deze paragraaf aankunt.` Deterministic text-group matching is accepted only for this reviewed local proof, not as broad symbolic/semantic proof. No direct source mutation, generated-output mutation, broad exit-ticket scaling, `1.1.1` target-equivalent claim, `1.1.3` target-equivalent claim, diagnostics, adaptive routing, mastery/sequencing, summative use, PV, Scale Gate 1, CP-6/Year-1 reliance, or product-wide use was authorized. Records: platform `reports/review-gates/GATE-L1.7B-Q2-exit-ticket-target-equivalent-proof/`. |
| L1.7B-Q2-COPY | Exact 1.1.2 Target-Equivalent Completion Copy Enablement | **2026-06-01** | **CLOSED EXACT COPY ENABLEMENT / REVIEWED 1.1.2 ONLY.** Platform set only the reviewed `1.1.2` gate/copy flags, enabled the exact local non-summative copy `Je hebt laten zien dat je de eindopgave van deze paragraaf aankunt.`, tightened exit-ticket progress so completion eligibility appears only after full reviewed proof completion, regenerated Book 1 output through platform deploy, and added a checker proving `1.1.1` remains advisory and `1.1.3` remains unapproved/absent. Lead review round 1 returned REVISE for completion-eligibility semantics and generated-output guard gaps; corrections resolved both; final round 2 closed PASS WITH FLAGS. No broad exit-ticket scaling, `1.1.1` or `1.1.3` target-equivalent status, target-exercise registry promotion, diagnostics, adaptive routing, mastery/sequencing, summative use, PV, Scale Gate 1, CP-6/Year-1 reliance, or product-wide use is authorized. Records: platform `reports/sprints/L1.7B-Q2-COPY-result.md`. |
| REV-STD-1 | Core-Spec Review Standard Hardening | no | **REQUIRED BEFORE SCALE GATE 1.** Update review packets and lead-review rules so core specification failures cannot be carried as ordinary flags. Every review packet must include `specifications/product-end-state.md`, the original sprint specification, non-negotiable requirements, and a core-requirement checklist. PASS WITH FLAGS is allowed only for issues outside the sprint's core objective. Scope-language enforcement is handled by closed `SCOPE-LANG-1`; plan-level quality-standard enforcement is handled by closed `QUALITY-STD-1`; REV-STD-1 still owns the wider review-template and lead-review-rule hardening. |
| Scale Gate 1 | Foundation Hardening Scale Gate | no | **BLOCKED.** `SPEC-ET-1`, `EX-LESSON-1`, `GAME-UX-3A`, `ENGINE-OP-1`, `SKILLMAP-OP-1`, `GRAPH-UX-2`, `MATH-UX-2`, `REASON-UX-2`, `GAME-ARCH-1`, `GAME-ARCH-2`, `GATE-ENGINE-1`, `GRAPH-REFINE-1`, `MATH-REFINE-1`, `REASON-REFINE-1`, `CHECK-Q2-PLAN`, `L1.7B-Q2`, `GATE-L1.7B-Q2`, `L1.7B-Q2-COPY`, `L1.7B-Q2-D31-STRUCT`, `SYNC-PRODUCT-1`, `MTU-H4C`, `L1.7C-MATH`, `L1.7B-MAP`, and `L1.7B-P23` are closed, but Scale Gate 1 may not run until the Product Proof Track reaches `GATE-PRODUCT-3P` and `REV-STD-1` is closed, or both are explicitly waived by human decision with stated consequences. Scale Gate 1 must use `specifications/product-end-state.md` as the north-star baseline and may not treat engine architecture, shared skill-map runtime, answer-form MTUs, exam-target route traces, task-shell runtime support, advisory short-check output, graph-route practice output, math-route practice output, reasoning self-check output, or the local `1.1.2` completion copy as broad scale proof. If target-equivalent status is waived for other paragraphs, landing-page `Check` must be labelled as local practice check or checkpoint-only status, not paragraph-completion proof. Scale Gate 1 may authorize controlled production only, not adaptive diagnostics, mastery/sequencing, student-facing AI, summative use, PV projection, or PV machine promotion. |
| SPEC-ET-1 | Exit Ticket Target-Equivalent Specification Correction | **2026-05-29** | **CLOSED PASS / SPECIFICATION CORRECTION.** Updated `specifications/product-end-state.md` and `specifications/companion-core-specifications.md` so the exit ticket is defined as a target-equivalent proof task rather than merely readiness-to-try. Added local non-summative completion-language hierarchy, strengthened exam-ingestion end-product integration, revised `L1.7B-Q2`, `GATE-L1.7B-Q2`, `GAME-UX-3A`, and Scale Gate 1 wording, and preserved all blocks on grades, diagnostics, mastery, sequencing, summative use, AI, PV, Scale Gate 1, and student/product use. Records: `archive/sprints/SPEC-ET-1/`. |
| MTU-H4A | Answer-Form CLI-Mutation Planning Packet | **2026-05-29** | **CLOSED PLATFORM SOURCE-PLANNING DEPENDENCY AFTER GATE-MTU-H4.** Prepared only a bounded answer-form planning packet: exact lane specs, held Type 4 / motiveer / classificatie lane, `bron` as source-use modifier plus underlying answer form, graph/draw/shade planning-only evidence condition, held analysis/evaluation, visible q3/q15 EX overlays, and future source/projection boundaries. This authorizes no mutation, candidate storage, candidate writes, target-exercise fields, projection refresh, lesson output, diagnostics, mastery, sequencing, summative use, PV, Scale Gate 1, or student/product use. Top operational next action is `GATE-MTU-H4A`. |
| L1.7B-P23 | Exit Ticket Target-Skill Checkpoint Designs For 1.1.2 And 1.1.3 | **2026-05-28** | **CLOSED PASS WITH FLAGS / PLATFORM HANDOFF.** Human review accepted the stop/handoff decision. Operation-chain analysis showed that `1.1.2` requires calculation/work input, final numeric answer, percentage/index notation, and short explanation; `1.1.3` requires table/graph handling, axis convention, graph drawing or point-placement substitute, interpolation, and short explanation. No `1.1.2` or `1.1.3` exit-ticket output was generated because the current engine/UI is choice-only. `Check` remains hidden until reviewed generated checkpoint output exists. Carried flags: shared task-type shell support is required, L1.7B-Q2 cannot produce target-equivalent proof for calculation/graph paragraphs until task-type support exists, and target-exercise/MTU review flags remain live. Records: `archive/sprints/L1.7B-P23/`. |
| L1.7B-MAP | Exit Ticket Skill-Metadata Alignment | **2026-05-26** | **CLOSED PASS WITH FLAGS / EVIDENCE-FLAG CARRIER.** Human review accepted the metadata alignment: `1.1.1` checkpoint-assessed metadata now uses `B01/B02`, `A04` is removed from checkpoint target/scope metadata, `metadataAlignment.targetExerciseSkillIds` records `A43/B01/B02`, and `targetReadinessEvidence` remains `false`. The metadata mismatch is fixed for the checkpoint's current role, but the current checkpoint is not target-equivalent proof because it does not cover the full `A43` operation chain. Carried flags: target-equivalent proof belongs to `L1.7B-Q2`, future checkpoint designs must use task forms appropriate to the target exercise, Scale Gate 1 may not rely on the current checkpoint as proof evidence, and the `1.1.1` target-exercise registry record still needs its separate final review path. Records: `archive/sprints/L1.7B-MAP/`. |
| L1.7C-MATH | Restore Skill-Tree Math Game + Four-Game Architecture Integrity | **2026-05-26** | **CLOSED PASS WITH FLAGS / SCALE GATE FLAG CARRIER.** First human review accepted the route restoration but returned REVISE because the restored math-game result state could show `Volgende: A39`. Targeted revision now renders the next action with student-facing skill names, replaces visible dependency-node IDs with `Vaardigheid`, adds focused source tests, and adds post-exercise screenshot QA showing `Volgende: Prijsindex (CPI) berekenen` with no internal `A##`/`B##` code. Focused human recheck closed PASS WITH FLAGS. Primary `Rekenen` now points to scoped `wiskundevaardigheden.html` for `1.1.2` and `1.1.3`; `stappenplan.html` remains `Rekenstappen` support; unscoped `1.1.1` stays collapsed as `Brede vaardigheidskaart`. Carried flags: skill-tree progress language needs Scale Gate 1 review, restored math is not target-equivalent proof evidence, keyboard/focus proof should strengthen before scale, and scoped skilltree comments need cleanup. Records: `archive/sprints/L1.7C-MATH/`. |
| QUALITY-STD-1 | Planning Quality Standard Enforcement | **2026-05-26** | **CLOSED PASS.** Added quality-driven execution language to both repo `AGENTS.md` files, inserted a Specification-Fulfilment Rule and Planning Quality Floor into `specifications/companion-core-specifications.md`, added paragraph-build quality-standard guidance, and hardened the platform sprint-plan checker so future non-trivial plans require `Quality Standard`, `Specification Fulfilment Matrix`, `Quality Improvement Candidates`, and `Proof Required to Close`. No lesson output was generated and no product-use boundary was loosened. Records: `archive/sprints/QUALITY-STD-1/`. |
| SCOPE-LANG-1 | Scope-Language Discipline Enforcement | **2026-05-26** | **CLOSED PASS.** Tightened `specifications/companion-core-specifications.md`, renamed current active roadmap/version wording away from downscoping vocabulary, and added a platform checker that blocks unauthorized restricted scope terms in active sprint plans, roadmap rows, review packets, and agent plans. Bounded scope remains allowed only with full quality inside the scope and explicit follow-up or waiver for omitted specification requirements. No lesson output was generated and no product-use boundary was loosened. Records: `archive/sprints/SCOPE-LANG-1/`. |
| SPEC-END-STATE | Product End-State Specification Canonicalization | **2026-05-26** | **CLOSED PASS.** Created `specifications/product-end-state.md` as the stable north-star definition: every paragraph should give students a visible route from current readiness to target-exercise readiness. Linked it from the companion spec, roadmap, lesson/platform AGENTS docs, platform paragraph-build docs, and repository maps. No lesson output was generated and no product-use boundary was loosened. Records: `archive/sprints/SPEC-END-STATE/`. |
| GATE-L1.7B | Exit Ticket Product-Boundary Review | **2026-05-26** | **CLOSED PASS WITH FLAGS.** The `1.1.1` checkpoint product boundary is accepted as a non-summative, practice-oriented controlled paragraph-limited `Check` surface. GATE-L1.7B does not authorize Scale Gate 1, broad scaling, CP-6/Year-1 closure, target-exercise promotion, diagnostics, mastery, sequencing, summative use, student-facing AI, PV projection, or PV machine promotion. Carried flag `GATE-L1.7B-CF1` was later resolved for checkpoint metadata scope by `L1.7B-MAP`; Scale Gate 1 still may not treat the current checkpoint as target-equivalent proof because `A43` is not covered by the task chain. Records: `archive/sprints/GATE-L1.7B/`. |
| L1.7B-R | Boundary-Safe Exit Ticket Checkpoint Resume | **2026-05-26** | **CLOSED PASS WITH FLAGS.** Platform `GAME-UX-2` completed the source-controlled exit-ticket checkpoint engine and generated lesson output through platform scripts only. Lesson output commit `5c47961269096c21a7d50bbc97c71de7984ff6e1` contains the `1.1.1` checkpoint and landing `Check` activation; historical tag `checkpoint/GAME-UX-2-exit-ticket-mvp-lesson`. Human review accepted the checkpoint as a boundary-safe, non-summative controlled paragraph-limited checkpoint surface. Green checks: platform focused checkpoint/landing/skill-map tests, full platform Jest 554 passed / 8 skipped, deploy, `1.1.1` validation, Book 1 checks, procedure contracts, target exercises, sprint bundle, and checkpoint/landing desktop/mobile light/dark screenshot QA; local focused recheck 26/26 and `1.1.1` complete student-web validation passed. Carried flag `L1.7B-R-CF1` was later resolved for checkpoint metadata scope by `L1.7B-MAP`; the checkpoint still may not be used for target-equivalent proof, diagnostics, mastery, sequencing, target-exercise promotion, CP-6/Year-1, PV, Scale Gate 1, or broad-scaling evidence. Records: `archive/sprints/L1.7B-R/`. |
| L2.0 | Book 1 Flag Burn-down And House-Style Cleanup | **2026-05-25** | **CLOSED PASS WITH FLAGS.** L2.0 defined the Book 1 student-web house-style baseline, PASS WITH FLAGS operational meaning, flag dispositions, quality-ref status language, screenshot/QA expectations, exit-ticket readiness checklist, and consolidation/gemengde-opgaven landing rule. Platform generator routes `1.1.4 Gemengde opgaven` to primary `Oefen gemengd` instead of a weak `Verdiep`-only page; chapter landing tags also show `Oefen gemengd`. Human review closed PASS WITH FLAGS with no product blocker. Green gates: focused landing Jest 2/2, deploy link/data checks 460 refs + 221 data tests, complete student-web validation for `1.1.1`-`1.1.3`, `1.1.4` publisher-print validation, Book 1 health 26/26, procedure-contract validation 341 checks, v5 target-exercise validation 54 records with 12/12/14/16, `1.1.4` desktop/mobile light/dark screenshot QA, and full platform Jest 544 passed / 8 skipped. Carried flags: `1.1.4` remains legacy `FLAG`, graph-drawing consolidation and profit-formula framing need later content review, game-row variants remain limited-scope and not scale-approved, exit-ticket target-readiness remains future work under L1.7B-P23/L1.7B-Q2/GATE-L1.7B-Q2 after L1.7B-MAP metadata closure, and L1.7C-MATH has since corrected the primary math-game route with remaining scale flags. Records: `archive/sprints/L2.0/`. |
| L1.7D | Paragraph Landing Page Information Architecture Cleanup | **2026-05-24** | **CLOSED PASS WITH FLAGS; MATH-ROUTE REGRESSION CORRECTED BY L1.7C-MATH.** Platform generator now renders paragraph landing pages as a controlled route with `Start`, `Leer`, `Oefen`, optional `Check`, and `Verdiep`. `Check` stays hidden until a reviewed exit-ticket surface exists. L1.7D intentionally routed `Rekenen` to `stappenplan` when present and demoted the full skill map to a collapsed advanced source item; L1.7C-MATH later corrected this by restoring scoped `wiskundevaardigheden.html` as the primary math route and preserving `stappenplan` as support. Summary/news/presentation/textbook/source surfaces are collapsed under `Verdiep`, and legacy Word exercise rows remain hidden from student landing pages. Human review closed PASS WITH FLAGS. Green gates: deploy link/data checks, focused landing Jest, complete student-web validation for `1.1.1`-`1.1.3`, procedure-contract validation 341 checks, Book 1 Part A health 26/26, v5 target-exercise validation 54 records with 12/12/14/16, screenshot QA for representative landings, and full platform Jest 543 passed / 8 skipped. Carried flags: calculation route is not a full numeric engine, `Check` remains future/non-summative, screenshot QA is representative, and `1.1.4` needs a dedicated consolidation landing pattern before broad scale. Records: `archive/sprints/L1.7D/`. |
| L1.7C | Three-Aspect Game Quality Upgrade | **2026-05-24** | **CLOSED PASS WITH FLAGS; RETROSPECTIVE ROUTE GAP CORRECTED BY L1.7C-MATH.** L1.7C consumed platform `GAME-UX-1` shared skill-map runtime and regenerated Book 1 through the platform workflow so `Redeneren`, `Rekenen/Stappenplan`, and `Grafieken` consume one shared compact route panel. First human review returned REVISE because the route panel could expose internal skill IDs such as `A61`; focused revision fixed the label, added an `A61` regression test, corrected `1.1.1` landing copy, and added route-panel screenshots. Focused human recheck closed PASS WITH FLAGS. Carried flags: `Grafieken` has only one less-labelled variant, `Redeneren` needs richer variants/replay value, game screenshot QA should mature, and the restored math route remains practice rather than target-equivalent proof evidence. L1.7C-MATH later restored the old skill-tree math game as primary `Rekenen` where scoped. No adaptive diagnostics, mastery, sequencing, AI, summative use, PV projection, or PV machine promotion. Records: `archive/sprints/L1.7C/`. |
| L1.7C-0 | Shared Skill-Map Engine Contract | **2026-05-23** | **CLOSED PASS WITH FLAGS.** Defined one shared skill-map / skill-tree engine contract for the three second-row practice games and compact checkpoint mode for the later exit ticket. Contract defines aspect filters (`reasoning`, `calculation`, `graphical`, explicit `mixed`), modes (`compact`, `route`, restricted `full`), state/progress language, game consumers, landing-page preview use, exit-ticket compact use, accessibility expectations, and product-use boundaries. Platform implementation has since completed in `GAME-UX-1` commit `6509895`, tag `checkpoint/GAME-UX-1-shared-skill-map-engine`. Records: `archive/sprints/L1.7C-0/L1.7C-0-sprint-plan.md`, `archive/sprints/L1.7C-0/L1.7C-0-current-state-audit.md`, `archive/sprints/L1.7C-0/L1.7C-0-shared-skill-map-contract.md`, `archive/sprints/L1.7C-0/L1.7C-0-handoff-to-platform.md`, `archive/sprints/L1.7C-0/L1.7C-0-validation-log.md`, `archive/sprints/L1.7C-0/L1.7C-0-closure-log.md`. |
| L1.7B-C | Exit Ticket Companion Contract | **2026-05-23** | **CLOSED CONTRACT-ONLY / IMPLEMENTATION PAUSED.** The old untracked draft was inspected and recorded as design evidence only. Companion-completion contract and future implementation scope exist. Implementation is not authorized because the draft is untracked, uses mastery/score/pass/evidence/adaptive-focus language, and must consume shared skill-map compact checkpoint mode before any student-facing use. Records remain under `archive/sprints/L1.7B/`: sprint plan, draft inventory, companion-completion contract, historical exit-ticket scope file, stop decision, and validation log. |
| L-EX0 | Exam-Target Paragraph Contract | no | **FUTURE CONTRACT SPRINT.** Define how the lesson team builds a paragraph when the target exercise is an official exam question under `specifications/product-end-state.md`. No broad production. Output is a paragraph-plan contract, review checklist, handoff requirements back to platform, and one dry-run plan. Requires platform EX-0 contract evidence or an explicitly bounded substitute. |
| L-EX1 | Exam-Target Paragraph Controlled Implementation | no | **FUTURE CONTROLLED IMPLEMENTATION.** Build one paragraph around a real official exam question using platform exam-ingestion data, source annexes, answer-model decomposition, MTU mapping, and companion visual/answer-model gates. Must preserve the end-state distinction between paragraph publication, target-equivalent proof, and scale readiness. No broad companion scaling or generated-output hand patching. |
| L1.7A | Scaling Readiness And Modality Gate Review | **2026-05-23** | **CLOSED PASS WITH FLAGS.** Decision sprint, not production. Green current gates: `1.1.1`/`1.1.2`/`1.1.3` complete student-web validation, the same three Part A publisher-print validations, procedure-contract validation 341 checks, Book 1 health 26/26, print scope 12/12, and v5 target-exercise count 54 with 12/12/14/16. Decision: broad companion scaling is rejected. Controlled foundation hardening may continue through L1.7B-C contract evidence, L1.7C-0, L1.7C, L1.7D, L2.0, L1.7B-R, GATE-L1.7B, then Scale Gate 1. Records: `archive/sprints/L1.7A/L1.7A-sprint-plan.md`, `archive/sprints/L1.7A/L1.7A-evidence-inventory.md`, `archive/sprints/L1.7A/L1.7A-readiness-matrix.md`, `archive/sprints/L1.7A/L1.7A-flag-triage.md`, `archive/sprints/L1.7A/L1.7A-decision-record.md`, `archive/sprints/L1.7A/L1.7A-validation-log.md`, `archive/sprints/L1.7A/L1.7A-closure-log.md`. |
| L-CP6A | Book 1 Chapter 1.3 v5 Alignment Remediation | **2026-05-19** | **CLOSED PASS WITH FLAGS.** Lesson-side CP.6a mismatch is fixed for references-team recheck, without claiming CP-6 or Year-1 closure. Active Chapter 1.3 now aligns v5 as `1.3.1 Aanbod`, `1.3.2 Marktevenwicht`, `1.3.3 Verschuivingen en nieuw evenwicht`, and `1.3.4 Gemengde opgaven`; former costs/revenue material is archived under `archive/sprints/L-CP6A/displaced-book2-material/` for Book 2 survival. Green gates: active Chapter 1.3 validation, Book 1 health 26/26, Book 1 print scope 12/12, v5 target-exercise count 54 with 12/12/14/16, focused book Jest 7/7, full platform Jest 515 passed / 8 skipped. Records: `archive/sprints/L-CP6A/L-CP6A-sprint-plan.md`, `archive/sprints/L-CP6A/L-CP6A-technical-qa-report.md`, `archive/sprints/L-CP6A/L-CP6A-closure-log.md`, `archive/sprints/L-CP6A/L-CP6A-handoff-to-references.md`. Flags: target exercises remain migrated/placeholders, inherited Part A duplicate-opgaven pattern remains a maintenance flag, and references team must re-evaluate CP.6a. |
| L-CP6E | 1.1.3 Part A Figure Numbering Remediation | **2026-05-21** | **CLOSED PASS WITH FLAGS.** Fixed the CP.6e lesson-side blocker for `1.1.3 Grafieken en tabellen`: Part A now introduces figures in first-use order `1 -> 2 -> 3` across markdown, regenerated HTML, and regenerated PDF. The axis-convention figure is now `Figuur 2`; interpolation is now `Figuur 3`; affected paragraph, Chapter 1.1, and Book 1 publisher-print outputs were rebuilt through existing build scripts. Green gates: focused markdown/HTML/PDF figure-order check, `1.1.3` Part A publisher-print validation, Chapter 1.1 validation, Book 1 health 26/26, print scope 12/12, and v5 target-exercise count 54 with 12/12/14/16. Records: `archive/sprints/L-CP6E/L-CP6E-sprint-plan.md`, `archive/sprints/L-CP6E/L-CP6E-technical-qa-report.md`, `archive/sprints/L-CP6E/L-CP6E-closure-log.md`, `archive/sprints/L-CP6E/L-CP6E-handoff-to-references.md`. Flags: repeated worked-example scaffolding in `opgaven.md` remains accepted/non-blocking; CP.6f must recheck before references-side closure reliance. |
| SYNC-1 | Roadmap Reconciliation | **2026-05-18** | **CLOSED PASS.** Log: `archive/sprints/SYNC-1/SYNC-1-roadmap-reconciliation-log.md`. Joint roadmap sync after L1.5P/L1.5Q/L1.6. Lesson and reference roadmaps now agree that broad lesson scaling is not approved yet. Coming-period focus is foundation hardening: reconcile roadmap state, normalize the rough three-year blueprint as a non-authoritative planning prototype, classify MTU/target-exercise gaps, triage lesson-side flags, and decide controlled production only through a later Scale Gate. |
| L1.6R | 1.1.3 Dual-Coding Remediation | **2026-05-19** | **CLOSED PASS WITH FLAGS.** L1.6R reopened the `1.1.3` companion quality verdict after post-closure review found a systemic dual-coding failure. First remediation fixed the main explanation surfaces; focused human review then returned REVISE because guided-practice visuals were present but not exercise-specific. Final correction added exercise-specific guided visuals for broodjes, koffie, bioscoop, and water/index and guarded visual-value concordance in focused Jest. Green gates: deploy link/data checks 417 refs + 217/217 data tests, focused L1.6R dual-coding Jest 5/5, presentation-v2 screenshot QA 30 screenshots, rich-page screenshot QA 20 screenshots, complete student-web validation, publisher-print Part A validation, procedure-contract validator 341 checks, Book 1 health 26/26, and full platform Jest 515 passed / 8 skipped. `1.1.3-quality-ref.yaml` now records `human_review_status: "pass_with_flags"`. Archive: `archive/sprints/L1.6R/`. Flags: scaffolded/value-labelled graph visuals remain acceptable MVP surfaces; later graph-reading variants should reduce direct labels; visual-value concordance should become a reusable QA gate. |
| L1.6 | Second Pipeline Regression Paragraph | **2026-05-18** | **CLOSED AS TECHNICAL PROOF; COMPANION QUALITY REMEDIATED BY L1.6R.** Sprint plan: `archive/sprints/L1.6/L1.6-sprint-plan.md`; review packet: `archive/sprints/L1.6/L1.6-human-review-packet.md`; QA: `archive/sprints/L1.6/L1.6-technical-qa-report.md`; review records: `archive/sprints/L1.6/L1.6-student-experience-review.md`, `archive/sprints/L1.6/L1.6-teacher-learning-quality-review.md`, `archive/sprints/L1.6/L1.6-human-review-record.md`, `archive/sprints/L1.6/L1.6-lead-review-summary.md`; closure log: `archive/sprints/L1.6/L1.6-closure-log.md`. L1.6 proves the fresh paragraph build, graphical-game transfer, inert adaptive seam, A61/table-value procedure contract, and v5 baseline integration. Post-closure review found that the main `1.1.3` companion explanation surfaces lacked required graph/table learning objects; L1.6R closed that companion-quality incident as PASS WITH FLAGS. Green technical gates remain historically useful; they are not sufficient for broad scaling without L1.7A readiness review. |
| L1.5Q | Course Blueprint v5 + Four Test-Week Book Plan | **2026-05-18** | **CLOSED PASS WITH FLAGS.** Created the active v5 curriculum-source baseline for the four-book/four-test-week model. Active target-exercise registry now points to v5 with 54 count-bearing records and exact counts 12/12/14/16; v4 registry is archived, v4 blueprint/meta are superseded, v5 owned blueprint/meta exist, v5 validator checks counts, web-only test-prep, placeholder semantics, and blueprint anchors. Phase B upgraded `course_blueprint_v5.md` from scaffold to curriculum-source prose and closed with regenerated owned-source, owned-content, source-document, inventory, and URL-index artifacts. Flags: migrated target exercises and gemengde-opgaven placeholders are not reviewed final; L2.4-TEA remains the later target-exercise distribution audit. Log: `archive/sprints/L1.5Q/L1.5Q-closure-log.md`. |
| L1.5P | Boek 1 Print-Edition Cut + 2026/27 12-Paragraph Scope | **2026-05-18** | **CLOSED PASS AFTER LEAD-REVIEW CORRECTION.** Printed Book 1 is generated through the platform book workflow from a 12-paragraph print manifest: chapters 1.1 and 1.2 plus a composed print chapter 1.3 (`Aanbod en marktevenwicht`). Test preparation is website-only; cost/revenue/marginal-analysis material remains online/parked for later migration. Independent lead review found duplicate opgaven and excluded body/glossary leakage after the first close; corrections are now platform-owned and regenerated. Green gates: strengthened print-scope checker 12/12, `check:book` 26/26, focused print-scope Jest 5/5, full platform Jest 502 passed / 8 skipped, markdown/PDF excluded-term scans clean, PDF generated. Logs: `archive/sprints/L1.5P/L1.5P-sprint-plan.md`, `archive/sprints/L1.5P/L1.5P-cut-survival-map.md`, `archive/sprints/L1.5P/L1.5P-closure-log.md`, `archive/sprints/L1.5P/L1.5P-lead-review-record.md`. |
| L2.1 | Book 1 Release Polish | no | Teacher-facing polish continues under the Book 1 health gate after the print scope is stable. |
| L2.2 | Book 2 Part A Textbook Layer | no | Start Book 2 Part A only after foundation-hardening gates say the v5/MTU/target-exercise path is stable enough. Do not start Book 2 full production merely because L1.5Q made v5 active. |
| L2.4-TEA | Target Exercise Distribution Audit | no | **FUTURE QUALITY SPRINT.** Do not execute until the micro-teaching-unit layer and companion-quality instruments are mature enough. Evaluate target exercises across the new book structure using MTU dependencies, teacher-learning-quality review, student-experience review, and built paragraph evidence. |
| L-PV0 | PV-G4 Lesson Proof Track Planning | **2026-05-14** | **CLOSED PASS.** Operational proof plan added in `archive/sprints/L-PV0/L-PV0-proof-track-plan.md`. Current repos were checked first: PV-G4 intake was `0/2`, `shared/procedure/1.1.1.js` still exposed `(unit B02)`, and chapter/book aggregates still carried stale three-step wording. Candidate 1 selected `1.1.1`/B02; candidate 2 selected a bounded A61 table-trace pilot. |
| L-PV1 | Procedure Contract Hardening | **2026-05-14** | **CLOSED PASS.** Platform now has a lesson procedure-contract registry and `validate-procedure-contracts.js`. The validator checks counts, formal step IDs, order, keywords, surface coverage, stale legacy wording, and student-facing internal-code leakage. Negative Jest fixtures prove wrong order, internal-code leakage, and old three-step language fail. |
| L-PV2 | Proof 001 - 1.1.1 B02 Procedure Mapping | **2026-05-14** | **CLOSED PASS.** `PVG4-proof-001` prepared for `1.1.1 Schaarste en economisch denken`, mapping the procedure game and answer/surface parity to `choose_by_opportunity_cost_flow`. `shared/procedure/1.1.1.js` is generated by platform source, carries formal step IDs, and no longer exposes `B02` in student-facing description/data. Stale chapter/book/test-prep three-step surfaces were refreshed through existing build scripts. |
| L-PV3 | Proof 002 - Fresh PV-Validated Surface | **2026-05-14** | **CLOSED PASS WITH HCS CONDITION.** `PVG4-proof-002` prepared from a bounded lesson-owned A61 table-trace pilot surface. It validates `select_table_values_trace` step order and visual anchors without claiming student-facing PV publication. HCS accepted it as proof diversity only; it is not a classroom-ready or student-facing A61 route. |
| L-PV4 | PV-G4 Intake Closure Packet | **2026-05-14** | **CLOSED / HCS PACKAGE SUBMITTED.** Two lesson-owned proof records exist under `pv-g4-proof-records/`; platform proof intake records `2/2` and the checker passes. HCS review packet was prepared and then reviewed in L-PV5. This package does not authorize PV machine promotion, student-facing PV projection, diagnostics, adaptive use, AI, sequencing, mastery, or summative use. |
| L-PV5 | Roadmap Sync After PV-G4 | **2026-05-14** | **CLOSED PASS WITH CONDITIONS LOGGED.** HCS lead review returned `PASS WITH CONDITIONS`. The evidence-freshness condition was reconciled by regenerating the lesson proof records and platform intake: both now cite lesson commit `52f9237de9e465e7f75483f6feac4e80241e8631` with `lesson_worktree_dirty_at_generation: false`, and the platform intake checker passes. A post-closure report-state cleanup made the intake and lesson HCS packet closure-aware. Proof 002 remains a bounded, non-student-facing A61 pilot only. Log: `archive/sprints/L-PV5/L-PV5-roadmap-sync-log.md`. |
| L1.5B | Layout Round 2 - Generator Items | **2026-05-14** | **CLOSED PASS.** Platform `cb216ed160a9298f7f4393034b6c1d842a387ff9` shipped generator-owned landing/index polish: domain hooks, stronger book/chapter card hierarchy, availability chips, structured per-card pitfall support, and mobile/dark wrapping fixes. Book 1 landing/index output was regenerated through `deploy.js`. Green gates: landing generator Jest, procedure-contract validator (289 checks), `1.1.1` and `1.1.2` complete student-web validation, Book 1 health 26/26, diff hygiene, and desktop/mobile light/dark screenshot QA. Closure log: `archive/sprints/L1.5B/L1.5B-closure-log.md`. |
| L1.5G-A | Graphical Game Scope Cut And Prototype Audit | **2026-05-16** | **CLOSED PASS.** Split the oversized L1.5G into L1.5G-A through L1.5G-E after checking `knowledge/grafiekmeester_representatie_arena.html`. GrafiekMeester is an 87 KB standalone product prototype with UI, state, XP, skill tree, badges, localStorage progress, and broad graph domains, so it is a design reference rather than a direct port. MVP cut: bar/line graph reading plus old/new value selection before percentage change; technical target `1.1.2` or sandbox, fresh production proof in L1.6/`1.1.3`. Artifacts: `archive/sprints/L1.5G-A/L1.5G-A-graphical-game-scope-plan.md`, `archive/sprints/L1.5G-A/L1.5G-A-prototype-extraction-matrix.md`, `archive/sprints/L1.5G-A/L1.5G-A-mvp-data-model-sketch.md`. |
| L1.5G-B | Adaptive Input Seam Contract | **2026-05-16** | **CLOSED PASS.** Platform `9014a50eb85ccbd48c0770bf677b36d75455aa48` added an inert `adaptive-seam.js` helper with localStorage key `4veco.adaptivePayload.v1`, wired quiz/newsdetective/reasoning/skilltree/procedure engines to read and store the normalized payload without using it for gameplay, added focused seam tests, updated shell builders and deploy copy list, and regenerated Book 1 game shells through `deploy.js`. Green gates: focused seam Jest 8/8, deploy link/data checks, procedure-contract validator 289 checks, `1.1.1` + `1.1.2` complete student-web validation, Book 1 health 26/26, full platform Jest 488 passed / 7 skipped. No advisor, diagnostics, adaptive routing, mastery, sequencing, AI, summative use, PV projection, or PV machine promotion. Closure log: `archive/sprints/L1.5G-B/L1.5G-B-closure-log.md`. |
| L1.5G-C | Graphical Game MVP Engine | **2026-05-16** | **CLOSED PASS.** Platform `042d7aea4f4cfbe5cd026a3a29cbb57891f795be` added the sixth game as a narrow graphical MVP: engine/UI/CSS, shell generator, data builder, tests, deploy wiring, landing-card detection, and explicit `1.1.2` pilot data. Generated output was rebuilt through `deploy.js`: `shared/graphical/1.1.2.js`, shared graphical engine files, `1.1.2 ... – grafiekenspel.html`, and the `1.1.2` landing page. Green gates: focused graphical/adaptive Jest 20/20, deploy link/data checks, `1.1.2` complete student-web validation, procedure-contract validator 289 checks, Book 1 health 26/26, platform Jest 494 passed / 8 skipped, desktop/mobile Chrome screenshot smoke. No PV projection, adaptive behavior, diagnostics, mastery, sequencing, AI, or summative use. Closure log: `archive/sprints/L1.5G-C/L1.5G-C-closure-log.md`. |
| L1.5G-D | Three-Aspect Game Routing | **2026-05-17** | **CLOSED PASS.** Platform `84ed88e78791203db779a4daecbc02589c99ed1d` added a generated three-aspect game routing layer to paragraph landing pages: `Redeneren`, `Rekenen`, and `Grafieken`, with stable `data-learning-aspect` metadata and student-facing copy. `Begeleide inoefening` is now visually separated as `Extra steun`, not treated as a fourth aspect. Generated output was rebuilt through `deploy.js` for chapter 1.1 landing pages. Green gates: landing generator Jest, deploy link/data checks, `1.1.1` + `1.1.2` complete student-web validation, procedure-contract validator 289 checks, Book 1 health 26/26, platform Jest 494 passed / 8 skipped, desktop/mobile Chrome screenshot smoke. No PV projection, adaptive behavior, diagnostics, mastery, sequencing, AI, or summative use. Closure log: `archive/sprints/L1.5G-D/L1.5G-D-closure-log.md`. |
| L1.5G-E | Integration, QA, And Review Gate | **2026-05-18** | **CLOSED PASS WITH FLAGS.** Human review first returned REVISE for answer-revealing placeholders, unsafe old/new defaults, missing checklist scaffolding, generic feedback, and quality-ref bookkeeping; focused re-review then returned REVISE because the final challenge skipped feedback and jumped to summary. Platform source fixed both rounds, generated lesson output was rebuilt through `deploy.js`, `1.1.2-quality-ref.yaml` now marks `grafiekenspel: pass_with_flags`, and screenshots confirm neutral placeholders, explicit old/new selectors, checklist, diagnostic feedback, and final-challenge feedback before summary. Green gates: graphical/adaptive Jest 23/23, deploy link/data checks 160/160, `1.1.1` + `1.1.2` complete student-web validation, procedure-contract validator 289 checks, Book 1 health 26/26, platform Jest 497 passed / 8 skipped, blocked-word search, and rendered final-feedback screenshot proof. Closure log: `archive/sprints/L1.5G-E/L1.5G-E-closure-log.md`. Flags: L1.6 must prove the graphical game/adaptive seam on a fresh paragraph; later graphical variants should reduce direct value labels; PV-G4 boundaries remain in force. |
| L1.4-PARITY | 1.1.2 Procedure And Quality Cleanup | **2026-05-13** | **CLOSED 2026-05-13 PASS WITH FLAGS.** Narrow follow-up after the post-L1.4 review. Canonicalized §1.1.2 to four-step student-facing procedures across Part A, companion pages, presentation-v2, procedure game, paragraph plan, quality-ref, and chapter plan; added an explicit 1-decimal rounding rule; fixed opgave 5c so rounded `16,7%` is not treated as exact; framed CBS April 2026 as a `snelle raming` exercise; corrected presentation-v2 route aria labels and reasoning metadata title discovery; documented skilltree A38/A39 coverage. Added validator parity gate comparing declared procedure step counts in `quality-ref.yaml` with shared procedure data. Green gates: complete student-web validation, publisher-print Part A validation, focused Jest, full `check:book`, deploy link/data checks, and presentation-v2 automated screenshot QA. Plan: `archive/sprints/L1.4-PARITY/L1.4-PARITY-sprint-plan.md`. Remaining flag: formal teacher/student review still required before final house-style promotion. |
| L1.5D-B02 | 1.1.1 Cross-Surface Parity + Bookkeeping Fix | **2026-05-12** | **CLOSED 2026-05-12 PASS**. Narrow follow-up after the second web-PowerPoint review. Fixed the §1.1.1 Part A / Part B drift to the four-step economisch-denken procedure with nettowaarde, removed student-facing `B02` unit-code labels from generated/student pages, regenerated Part A HTML/PDF + companion DOCX-derived HTML + presentation PPTX/HTML + quiz/YouTube/shared CSS through the platform workflow, fixed `convert_presentatie.py` so the official `presentatie.pptx` is selected instead of local prototype decks, and taught the link checker to ignore `*-prototype.html` baselines as non-navigation artifacts. Completion log: `archive/sprints/L1.5D-B02/L1.5D-b02-cross-surface-parity-plan.md`; refreshed Part A review: `1.1.1-review.md`. |
| L1.5O | Output Profile Simplification | **2026-05-12** | **CLOSED 2026-05-12 PASS**. Inserted before L1.4 to stop carrying Office documents through the default paragraph build. Platform validator now has explicit profiles: `student-web` (default; 14 web-first Part B files, no DOCX/PDF requirement), `legacy-full` (old 27-file contract), `office` (student-web plus DOCX exports), and `publisher-print` (the three textbook PDFs + `build_pdf.py`). `check-book.js` keeps Part A book health on `publisher-print`; paragraph 1.1.2 should use `--mode complete --profile student-web` unless Office exports are explicitly requested. Evidence: focused Jest 21/21 plus 1.1.1 validation green in `student-web`, `legacy-full`, and `publisher-print`. |
| L1.5D | Authored Content As Web | **2026-05-11** | **CLOSED 2026-05-11 PASS WITH FLAGS**. D1 (DOCX-as-web for samenvatting + nieuws) and D2 (PPTX-as-web for presentatie) both shipped. v2 lead review returned FAIL with eight blockers (B1–B8); remediation cycle closed all eight: B1+B2 mobile responsive CSS at 390px (platform `362f0e2`), B7 detect_card_stack x-column filter (platform `6646bec`), B5+B6 validator gates D1 web outputs + BUILD-PARAGRAPH.md 24→27 contract (platform `b90b918`), B4 validate-chapter.js structured verdict parser (platform `e04d160`), B8 PPTX accessibility — 14pt floor across deck + speaker notes + AA contrast tokens (platform `830ebf4`). Selector-presence regression test added (`l1-5d-v2-mobile-fixes.test.js`). v3 lead review returned **PASS WITH FLAGS**: validators 27/27 + 26/26 + 454/0/7 jest + audit 0 sub-14pt + 0 contrast violations all green. Two non-blocking flags remain: long Dutch compound nouns on slide 1's dark-hero body line and nieuws cell-title still wrap with mid-word breaks at 390px (logged as platform follow-up, not reopening the sprint). |
| L1.5V | Companion Quality Polish + Pilot Lock-in for 1.1.1 | **2026-05-09** | **CLOSED 2026-05-09**. 17 platform commits on `content/1.1.1-companion-quality` + 2 lessen commits on `main`. All 4 hard fails + QA-1 from the original `1.1.1-companion-visual-review.md` resolved; verification sub-agent verdict **PASS WITH FLAGS** (3 non-blocking flags: visual-internal `alt. kosten` shorthand documented as scope decision, Team B reference HTMLs untracked-by-design, optional CSS polish on vaardigheden checklist trailer). Buckets A+B+C+D+E+F all closed. Validator `--mode complete` flips green: `OK Paragraph 1.1.1 PASSED all checks`. Jest 441/0/7 (69 new regression tests vs baseline). Pilot lock-in delivered: `BUILD-PARAGRAPH.md` carries Common pre-conditions section + clean Part A / Part B split, every skill in `skills/` has a `pipeline:` frontmatter label, `validate-paragraph.js` has F2 fixes (split Part A / Part B review gates, structured verdict parser, schema_version 2 awareness), `1.1.1-quality-ref.yaml` migrated to schema_version 2 with `partA:` + `companion:` blocks. L1.4 unblocked. |
| L1.4 | First Pipeline Regression Paragraph | **2026-05-12** | **CLOSED 2026-05-12 PASS WITH FLAGS.** Built and then polished `1.1.2 Percentages en indexcijfers` through the platform-owned `student-web` profile after L1.5O. Delivered native student-facing HTML companions, source-aligned begeleide inoefening, interactive shared data, skilltree paragraph/chapter/all toggles, shell pages, PPTX + semantic presentation-v2 web deck, companion review, quality-ref refresh, and `_paragraph-plan.md`; no new Word exports were generated. Validation green: `validate-paragraph --mode complete --profile student-web`, `validate-paragraph --mode part-a --profile publisher-print`, local link checker/deploy data tests, focused skilltree Jest, full `check:book`, and browser screenshot QA for index, voorkennis, begeleide inoefening, wiskundevaardigheden, and presentation surfaces in representative light/dark and wide/narrow states. Flag: formal teacher/student review still needs a separate review gate before declaring this the final scaling house style. Sprint plan: `archive/sprints/L1.4/L1.4-sprint-plan.md`. |

## Closed Sprints

Closed sprints in reverse-chronological order. The full record of each sprint
remains in the "Sprint Details" section further down.

| Sprint | Name | Closed | One-line summary |
|--------|------|--------|-------|
| LEAD-REVIEW-2 | Lead-Review Strict Validation | 2026-05-31 | Closed PASS WITH FLAGS. Platform hardened sprint-bundle validation so future sprint IDs cannot bypass lead review by backdating, human-review gates cannot use exemptions, lead-review reports must carry real structure/evidence, and PASS WITH FLAGS requires structured carried-flag disposition. |
| LEAD-REVIEW-1 | Lead-Review Protocol Repair | 2026-05-31 | Closed PASS WITH FLAGS. Platform repaired sprint lead-review enforcement, proved future human gates fail without pre-human-gate lead-review metadata, and ran real lead-reviewer-agent audits for the recent non-MTU/non-human-gated sprint bundles while excluding MTU human-gated sprints by explicit user direction. |
| SPEC-ET-1 | Exit Ticket Target-Equivalent Specification Correction | 2026-05-29 | Closed PASS. Corrected product and companion specs so exit tickets are target-equivalent proof tasks, added completion-language hierarchy, strengthened exam-ingestion route trace, and updated the pre-scale roadmap rows. |
| SPEC-END-STATE | Product End-State Specification Canonicalization | 2026-05-26 | Closed PASS. Created `specifications/product-end-state.md` as the canonical end-state baseline and linked it from lesson/platform operating docs, the companion spec, roadmap, and repository maps. |
| L1.7C-MATH | Restore Skill-Tree Math Game + Four-Game Architecture Integrity | 2026-05-26 | Closed PASS WITH FLAGS after focused recheck. Scoped `wiskundevaardigheden.html` is restored as primary `Rekenen` for `1.1.2` and `1.1.3`; `stappenplan.html` remains `Rekenstappen` support; `Volgende: A39`-style ID leakage is fixed. |
| GATE-L1.7B | Exit Ticket Product-Boundary Review | 2026-05-26 | Closed PASS WITH FLAGS. The `1.1.1` checkpoint remains a non-summative controlled paragraph-limited `Check` surface; `A43/A04` versus `B01/B02` metadata mismatch is carried as a scale blocker. |
| L1.7B-R | Boundary-Safe Exit Ticket Checkpoint Resume | 2026-05-26 | Closed PASS WITH FLAGS after GAME-UX-2 generated source-controlled `1.1.1` checkpoint output. Accepted as checkpoint-only evidence, not target-equivalent proof evidence. |
| L2.0 | Book 1 Flag Burn-down And House-Style Cleanup | 2026-05-25 | Closed PASS WITH FLAGS. Recorded house-style baseline, PASS WITH FLAGS meaning, flag disposition, quality-ref standard, exit-ticket readiness checklist, screenshot expectations, and `1.1.4` consolidation route. |
| L1.7D | Paragraph Landing Page Information Architecture Cleanup | 2026-05-24 | Closed PASS WITH FLAGS. Landing pages use `Start`, `Leer`, `Oefen`, optional reviewed `Check`, and `Verdiep`; later L1.7C-MATH corrected the math-route regression. |
| L1.7C | Three-Aspect Game Quality Upgrade | 2026-05-24 | Closed PASS WITH FLAGS after route-label fix. Shared route panel accepted for controlled paragraph-limited use; retrospective math-route gap was split to and corrected by L1.7C-MATH. |
| L1.7C-0 | Shared Skill-Map Engine Contract | 2026-05-23 | Closed PASS WITH FLAGS. Defined the shared route/skill-map contract for reasoning, math, graph, landing previews, and checkpoint compact mode. |
| L1.7B-C | Exit Ticket Companion Contract | 2026-05-23 | Closed contract-only. Old untracked draft recorded as design evidence; implementation paused until source-controlled, non-summative platform output exists. |
| L1.7A | Scaling Readiness And Modality Gate Review | 2026-05-23 | Closed PASS WITH FLAGS. Rejected broad companion scaling and authorized only controlled foundation hardening before Scale Gate 1. |
| L1.5A | Easy Layout Round 2 | 2026-05-01 | Shipped book-root back-link guard (platform `5b8c216`) + BI static back-link (platform `b9c5085`); lessen-side `2a8455b` regenerated. Verification: SHIPPED CLEAN, all 4 baseline gates green. Platform PR https://github.com/meijer1973/4veco-platform/pull/2 open at close awaiting merge to platform main. Item #1 reclassified as generator-touching, deferred to L1.5B. |
| L1.3C | PowerPoint Presentation Improvement | 2026-04-25 | `1.1.1` PPTX regenerated with adapted slide visuals; teacher-supporting slide rules + read-through QA gate documented in `econ-pptx-templates`; LibreOffice roundtrip clean. |
| L1.3B | Companion SVGs And Light/Dark Visual Variants | 2026-04-25 | `lib-visual-surfaces.js` is the shared SURFACES/THEMES module; light/dark symmetry validator enforced; news visual on the variant system; game-visuals decision recorded per paragraph. |
| L1.3A | Basic HTML Layout And Front-End Usability | 2026-04-25 | `1.1.1` companions on shared platform layout/theme; converters and landing-page generator landed in platform; browser smoke + technical gates green. |
| L1.2 | Second Companion Technical Probe | (pre-restructure) | `1.1.2` proved the technical pattern can repeat; probe materials were removed for didactic rebuild. |
| L1.1 | First Companion Technical Pilot | (pre-restructure) | `1.1.1` passes the current complete technical gate. |
| L0.5 | Green Gate Handoff | (pre-restructure) | Book 1 Part A and the platform/book health routine are green. |

## Roadmap Metadata

Generated: 2026-04-23
Updated: 2026-04-25 after Sprint L1.3A-C close — basic HTML layout, companion SVG variant system with light/dark symmetry validator, and PPTX teacher-supporting slide rules all landed in platform; L1.4 (pipeline regression on `1.1.2 Percentages en indexcijfers`) is now active.
Updated: 2026-04-30 — sprint sequence restructured. L1.4 paused to ship layout polish + web-native authored content first; L1.5 split into L1.5A (single-paragraph-safe items, active now) and L1.5B (generator-touching items, after L1.4). New L1.5D (DOCX/PPTX as web) sequenced before L1.4 because both should be tested against L1.4's fresh-paragraph regression. New L1.5G (three-aspect games coverage) sequenced after L1.5B with adaptive-ready architecture as a cross-cutting constraint. L1.4 resumes with triple-purpose scope: layout + games + web-docs regression on fresh content.
Updated: 2026-05-01 — added the PV Consumption Rule after leadership approved the Procedure-Visual Backbone. The lesson repo remains a generated target and consumer: L1.5G aligns the graphical game with platform/reference PV records, L1.6 proves one PV-backed or PV-validated procedure/visual sequence on a fresh paragraph, and L1.7A includes PV readiness before any scaling decision.
Updated: 2026-05-01 — Sprint Ledger reorganized: active sprint sits at the top, future sprints follow, and closed sprints moved to a separate "Closed Sprints" archive. L1.5A closed (lessen `2a8455b` shipped, platform PR #2 open at close); L1.5D promoted to active sprint.
Updated: 2026-05-09 — L1.5V (Vaardigheden Quality Polish for 1.1.1) inserted between L1.5D D1 and L1.5D D2. Triggered by a Team B reference draft that surfaced visual-text mismatches, scaffold gaps, and a canonical-procedure ambiguity in the existing `uitleg vaardigheden.html`. Canonical procedure decision recorded: B02 is 4-step (was 3-step in `_paragraph-plan.md`), driving registry update + propagation across vaardigheden, samenvatting, presentatie, stappenplan, BI, opgaven. L1.5D D1 shipped 2026-05-08; PR #3 awaiting merge before L1.5V branches off main. L1.5D D2 paused, resumes after L1.5V.
Updated: 2026-05-11 (later) — L1.5D **CLOSED PASS WITH FLAGS** after a v2-review remediation cycle. D1 (DOCX-as-web for samenvatting + nieuws) shipped earlier; D2 (PPTX-as-web for presentatie, slide-by-slide with prev/next/keyboard/sidebar) shipped this session. Then v2 lead-review returned FAIL with 8 blockers (mobile responsive overflow at 390px on all three D1+D2 web surfaces, caption absorbed into card subtitle, D1 web files ungated in validator, stale 24-file Part B doc, chapter validator using token-grep instead of structured verdict, PPTX accessibility 56 sub-18pt runs + 2.9:1 contrast). All 8 closed across platform commits 362f0e2 / 6646bec / b90b918 / e04d160 / 830ebf4 + regression test ae60dc6. v3 lead-review returned PASS WITH FLAGS — gates green (27/27 validator, 26/26 check:book, 454/0/7 jest, 0 sub-14pt audit, 0 contrast violations), two non-blocking flags on mid-word Dutch compound-noun wraps logged as platform follow-up. L1.4 (pipeline regression on §1.1.2) and L1.5B (Layout Round 2 generator items) are now both unblocked.
Updated: 2026-05-11 — added Sprint L1.5P (Boek 1 Print-Edition Cut for Publisher) as a parallel urgent sprint; publisher hand-off in a few weeks. Added the "Adaptive learning replaces three-track differentiation" subsection to the architecture chapter to record that basis/middenopgaven/verrijking will be deprecated next school year (2026/27 cohort) in favor of a dynamic adaptive `begeleide inoefening`, with the repo-wide audit scoped explicitly out of this roadmap. Lesboek section added to the platform landing-page builder (`build-landing-page.js`): every paragraph index now shows the textbook source (`paragraaf` HTML + PDF, `opgaven`/`antwoorden` HTML + PDF) as a final row at the bottom — landed on §1.1.1's regenerated index.
Updated: 2026-05-09 (later) — L1.5V scope EXPANDED to "Companion Quality Polish + Pilot Lock-in for 1.1.1" after (a) the `econ-companion-visual-review` agent ran on `uitleg voorkennis` and returned FAIL with four hard-fail defects + QA-1 (DOCX style collision), several of which are upstream platform issues shared with vaardigheden, and (b) the user direction that §1.1.1 is the pilot paragraph and L1.5V is the moment to set up the Part A / Part B build skill, quality test, and review-agent pipeline cleanly before L1.4 starts paragraph 2. New buckets E (Part A QC integration — fold in the previously deferred quality-record schema extension) and F (Part A / Part B QC pipeline separation pilot, gating L1.4) added. New platform skill `skills/econ-companion-artifacts.md` is the authoring spec; `agents/econ-companion-visual-review.md` is the closure gate. PR #3 merged; L1.5V branches off platform main as `content/1.1.1-companion-quality`. L1.4 row updated to mark Bucket F closure as a pre-condition. See full sprint detail below for the six-bucket item list and per-item workflow that pairs the skill with the review agent on every iteration.
Updated: 2026-05-12 — Sprint L1.5O closed. Default paragraph validation is now web-first (`--profile student-web`), Office exports are opt-in (`--profile office` or `legacy-full`), and the three textbook PDFs move to the explicit publisher/print profile (`--profile publisher-print`). L1.4 should build `1.1.2 Percentages en indexcijfers` against the lighter student-web profile before any optional Office package is requested.
Updated: 2026-05-12 (later) — closed narrow follow-up `L1.5D-B02`. This cleaned up the §1.1.1 parity record after the second web-PowerPoint review: Part A and Part B now share the four-step economisch-denken procedure with nettowaarde; student-facing pages no longer expose `B02`; the presentation web converter now ignores prototype decks when selecting the official PowerPoint; and the regenerated artifacts/reviews are committed as bookkeeping before starting the next paragraph sprint.
Updated: 2026-05-12 (landing cleanup) — paragraph landing pages now suppress Word-download options on student-facing tiles and hide the old basis/midden/verrijking Word exercise row. The 1.1.1 landing page was regenerated from platform commit `548270c`; future paragraph builds should route students to HTML/web practice surfaces, with Office exports only when explicitly requested.
Updated: 2026-05-12 (landing language) — paragraph landing-page tiles no longer show `html` as a visible chip. The clickable tile itself is the web action; only meaningful extra choices remain visible, such as `Interactief`, `Download als PowerPoint`, and PDF links. Regenerated chapter 1.1 paragraph indexes from platform commit `6de425f`.
Updated: 2026-05-12 (L1.4 polished close) — `1.1.2 Percentages en indexcijfers` now has a polished student-web companion set generated from platform source without new Word exports. The closure pass corrected the initial too-minimal build: begeleide inoefening now follows the textbook opgaven and answer model, voorkennis/vaardigheden/samenvatting/nieuws/video pages use the 1.1.1 rich layout pattern, wiskundevaardigheden has paragraph/chapter/all skill toggles, dark/light styling is shared, and mobile/narrow CSS was visually checked. Green gates: Part A publisher-print validation, complete student-web validation, local link checker/deploy data tests, focused skilltree Jest, full `check:book`, and browser screenshot QA across representative wide/narrow and light/dark states. Remaining flag is formal teacher/student review only.
Updated: 2026-05-13 — Sprint L1.4-PARITY closed after the post-L1.4 review found substantive procedure-parity flags. §1.1.2 now uses four-step routes for procentuele verandering, indexcijfer berekenen, and indexpunten/procenten across Part A, companion pages, presentation, procedure game, quality-ref, and chapter plan. Added rounding policy, fixed opgave 5c exact/rounded control, corrected presentation-v2 route aria labels, fixed reasoning metadata for flat paragraph folders, and added a validator gate that compares declared procedure step counts with shared procedure data. Green gates: complete student-web validation, publisher-print Part A validation, focused Jest, full `check:book`, deploy link/data checks, and presentation-v2 screenshot QA.
Updated: 2026-05-14 - inserted the lesson-side PV-G4 proof track (`L-PV0` through `L-PV5`) at the top of the sprint ledger after checking the current repos. Current platform evidence still shows PV-G4 proof intake at `0/2`; the existing L1.5D-B02 and L1.4-PARITY work is useful cleanup evidence but not formal PV-G4 proof-record evidence. Also confirmed one live student-facing risk for the track: `shared/procedure/1.1.1.js` still contains `(unit B02)` in the procedure-game description, despite the quality-ref claim that generated/student pages no longer expose `B02`. PV-dependent L1.5B/L1.5G/L1.6/L1.7A work is now sequenced behind the proof track unless explicitly scoped as non-PV/non-procedure work.
Updated: 2026-05-14 (PV-G4 HCS package) - executed L-PV0 through L-PV4 and prepared the HCS human-review packet. The platform now has a procedure-contract validator and proof-record/intake workflow; lesson output now has formal step IDs for 1.1.1 and 1.1.2 procedure data; stale three-step B02 wording in chapter/book/test-prep aggregates was corrected and rebuilt. `pv-g4-proof-records/PVG4-proof-001.json` and `PVG4-proof-002.json` are present, and the platform PV-G4 intake now records `2/2` with checker green. At L-PV4 close, PV-G4 was still waiting on HCS decision; the later L-PV5 update records that decision.
Updated: 2026-05-14 (PV-G4 HCS decision) - HCS lead review returned `PASS WITH CONDITIONS`. L-PV5 reconciled the evidence-freshness condition by regenerating lesson proof records and platform intake from current authoritative artifacts; post-closure report-state cleanup now has both citing lesson commit `52f9237de9e465e7f75483f6feac4e80241e8631` with `lesson_worktree_dirty_at_generation: false`, and the platform intake checker passes. Proof 002 remains a bounded, non-student-facing A61 pilot only. PV machine promotion, student-facing PV projection, diagnostics, adaptive use, AI, sequencing, mastery, and summative use remain blocked.
Updated: 2026-05-14 (PV-G4 report-state cleanup) - the platform PV-G4 intake/report generators are closure-aware. Current generated intake and review packet status is `pass_with_conditions`, not `ready_for_hcs_review`; the lesson HCS packet is now `gate_reviewed_pass_with_conditions`. L1.5B is the next active lesson sprint and must start with a checkable sprint plan.
Updated: 2026-05-14 (L1.5B close) - L1.5B closed PASS. Platform commit `cb216ed160a9298f7f4393034b6c1d842a387ff9` added domain hooks, richer generated book/chapter landing cards, structured per-card pitfall support, and mobile/dark wrapping fixes. Book 1 landing/index output was regenerated through platform `deploy.js`; green gates include landing Jest, procedure-contract validator (289 checks), `1.1.1` + `1.1.2` complete student-web validation, Book 1 health 26/26, diff hygiene, and desktop/mobile light/dark screenshot QA. The next lesson-game work remained under the PV-G4 condition boundary and was later split into L1.5G-A through L1.5G-E.
Updated: 2026-05-16 (L1.5G split) - L1.5G was split into L1.5G-A through L1.5G-E after auditing `knowledge/grafiekmeester_representatie_arena.html`. L1.5G-A closed PASS with a scope plan, extraction matrix, and MVP data-model sketch. Direct port is rejected; first graphical MVP is graph reading and value selection only. L1.5G-B is next and must define the adaptive seam contract before any graphical engine work.
Updated: 2026-05-16 (L1.5G-B close) - L1.5G-B closed PASS. Platform commit `9014a50eb85ccbd48c0770bf677b36d75455aa48` added the inert adaptive seam helper, wired all five existing game engines to read it without behavior change, updated shell generation/deploy, and regenerated Book 1 game output through `deploy.js`. Green gates: focused seam Jest, deploy link/data checks, procedure-contract validator, `1.1.1` + `1.1.2` complete student-web validation, Book 1 health, and full platform Jest. L1.5G-C is next; it may read the seam but may not claim adaptive behavior.
Updated: 2026-05-16 (L1.5G-C close) - L1.5G-C closed PASS. Platform commit `042d7aea4f4cfbe5cd026a3a29cbb57891f795be` added the graphical-game MVP as a sixth platform game with engine/UI/CSS, shell generator, explicit `1.1.2` pilot data, tests, deploy wiring, landing-page reachability, and desktop/mobile rendered smoke checks. L1.5G-D is next; L1.5G-E remains the formal integration/review gate before L1.6.
Updated: 2026-05-17 (L1.5G-D close) - L1.5G-D closed PASS. Platform commit `84ed88e78791203db779a4daecbc02589c99ed1d` added student-facing game routing by aspect: Redeneren, Rekenen, and Grafieken. `Begeleide inoefening` is separated as guided support. Chapter 1.1 paragraph landing pages were regenerated through `deploy.js`; L1.5G-E is now the formal integration, QA, and review gate before L1.6.

Updated: 2026-05-17 (L1.5G-E technical gate) - L1.5G-E technical QA passed but the sprint is not closed. The gate found a mobile chart framing problem in `grafiekenspel`; platform source was fixed in `engines/graphical-ui.js` and `engines/graphical.css`, generated lesson output was rebuilt through `deploy.js`, and final true 390px Chrome DevTools screenshots were checked in light and dark mode. Green gates: focused graphical/adaptive Jest 20/20, deploy link/data checks 160/160, `1.1.1` + `1.1.2` complete student-web validation, procedure-contract validator 289 checks, Book 1 health 26/26, platform Jest 494 passed / 8 skipped, and blocked-word search with no internal/PV/adaptive/diagnostic claims in checked surfaces. Next action is formal student-experience and teacher-learning-quality review using `archive/sprints/L1.5G-E/L1.5G-E-human-review-packet.md`; L1.6 remains blocked until that gate is closed or the roadmap is explicitly changed.
Updated: 2026-05-17 (L1.5G-E human-review revise response) - human review returned REVISE for `grafiekenspel` because placeholders could reveal answers and the percentage-change tasks needed explicit old/new selection, a visible checklist, and diagnostic feedback. Platform source addressed those blockers, generated output was rebuilt through `deploy.js`, `1.1.2-quality-ref.yaml` included `grafiekenspel`, and screenshot evidence was refreshed for the first challenge, the percentage selector state, and wrong-new-value diagnostic feedback. Green focused gates: graphical/adaptive Jest 22/22, deploy link/data checks, `1.1.1` + `1.1.2` complete student-web validation, procedure-contract validator 289 checks, Book 1 health 26/26, and blocked-word search. L1.5G-E remained open until focused human recheck.
Updated: 2026-05-18 (L1.5G-E focused re-review revise response) - focused re-review returned REVISE because the final challenge skipped feedback and jumped straight to summary. Platform `graphical-ui.js` now renders summary only when the engine is complete and no final `lastResult` feedback is pending; the final challenge now shows diagnostic feedback and `Bron/Waarden/Berekening` first, with `Bekijk resultaat` opening the summary afterward. Added a focused UI safeguard test and regenerated lesson output through `deploy.js`. Screenshot evidence now includes desktop and true-390px mobile final-feedback states. L1.5G-E remains open until final focused human recheck accepts the revised final-feedback flow.
Updated: 2026-05-18 (L1.5G-E close) - second-revision review accepted the final-feedback fix and closed L1.5G-E as PASS WITH FLAGS. `1.1.2-quality-ref.yaml` now records `grafiekenspel: pass_with_flags`; student-experience, teacher-learning-quality, human-review, lead-review, technical-QA, and closure-log records all agree. Flags carried forward: L1.6 must prove the graphical game and adaptive seam on a fresh paragraph; later graphical-game variants should include harder graph reading without direct value labels; PV-G4 blocked-use boundaries remain active.
Updated: 2026-05-18 (L1.5P/L1.5Q/L2.4-TEA roadmap insertion) - checked local Book 1 assembly, chapter 1.3 plan, `course_blueprint_v4.md`, the platform target-exercise registry, and platform roadmap paths before updating the sequence. L1.5P is now the urgent active print track for the 2026/27 12-paragraph Book 1 scope; L1.5Q is the curriculum-source sprint for `course_blueprint_v5.md` and the four formal test-week book plan; L2.4-TEA is deferred until MTU quality and companion-review instruments are mature enough. Repository-map freshness note: the platform roadmap files exist locally under `knowledge/old/`, so any map pointing to `knowledge/platform-team-roadmap.md` or `knowledge/three-month-roadmap.md` is stale.
Updated: 2026-05-18 (L1.5P close after lead-review correction) - L1.5P closed PASS after an independent lead review found and forced correction of duplicate opgaven, excluded/stale body content, glossary leakage, and a shallow first print-scope validator. Platform book builder now supports backwards-compatible composed print chapters plus manifest-controlled print removals and glossary exclusions. Book 1 manifest now generates the 2026/27 12-paragraph print scope, and the voorwoord says the printed book has three chapters/twelve paragraphs with test preparation on the website. Generated Book 1 markdown/HTML/PDF rebuilt through `python build-scripts/books/build-book.py --book 1`. Green gates: strengthened `check-book-print-scope` 12/12, `check:book` 26/26, focused print-scope Jest 5/5, full platform Jest 502 passed / 8 skipped, markdown/PDF excluded-term scans clean. L1.5Q is now the active curriculum-source sprint.
Updated: 2026-05-18 (L1.5Q Phase A source-of-truth seam) - L1.5Q Phase A implemented the v4->v5 source migration seam before the full pedagogical rewrite. The platform now preserves the v4 target-exercise registry under `references/authored/archive/course-target-exercises-v4.json`; active `references/authored/course-target-exercises.json` declares `blueprint_version: "v5"`, points to `references/owned/course-blueprint-v5.md`, and contains 54 count-bearing records with exact counts 12/12/14/16. Gemengde-opgaven records are explicit no-new-theory placeholders, and migrated records are marked `migrated_from_v4_needs_v5_review`. New validator `scripts/check-course-target-exercises-v5.js` plus focused Jest guard the counts, web-only test-prep boundary, and placeholder semantics. Derived owned-source, owned-content, source-document, inventory, and URL-index reports were regenerated; full platform Jest, Book 1 health, print-scope check, and diff hygiene are green. L1.5Q remains active for Phase B: the final pedagogical v5 blueprint and migration review.
Updated: 2026-05-18 (L1.5Q close) - L1.5Q closed PASS WITH FLAGS. `course_blueprint_v5.md` now states the four-book/four-test-week model, exact counts 12/12/14/16, web-only test preparation, Book 1's L1.5P scope, book-level intent, migration decisions, and placeholder boundaries. Platform owned v5 blueprint/meta mirror the lesson source, active `course-target-exercises.json` remains v5 with 54 records, and the v5 checker now verifies all 54 blueprint anchors. Green gates: v5 checker, focused v5 Jest 5/5, owned-source/content/source-document checks, source manifest/document inventory, source-of-truth check, Book 1 health 26/26, print-scope 12/12, full platform Jest 507 passed / 8 skipped, and diff hygiene. L1.6 is now the next active lesson pipeline sprint.
Updated: 2026-05-18 (L1.6 technical QA) - L1.6 generated `1.1.3 Grafieken en tabellen` as the fresh student-web regression paragraph after L1.5G/L1.5Q. Platform sources now build the companion pages, presentation, shared data, graphical game data, graph/table skilltree generators, and the A61/table-value procedure contract. Technical gates are green: deploy link/data checks, `1.1.3` complete student-web validation, `1.1.3` publisher-print Part A validation, procedure-contract validator 341 checks, focused game/procedure Jest 151/151, Book 1 health 26/26, full platform Jest 510 passed / 8 skipped, presentation screenshot QA, and landing/game desktop/mobile light/dark screenshot QA. L1.6 is ready for human review but not closed; required review packet is `archive/sprints/L1.6/L1.6-human-review-packet.md`.

Updated: 2026-05-18 (L1.6 revise addressed) - L1.6 human review returned REVISE for a real semantic transfer issue: the `Broodjesverkoop` P-Q line chart in `grafiekenspel` ordered quantity labels backwards left-to-right while `1.1.3` teaches quantity on the horizontal axis. Platform source fixed the data ordering, added a graphical-data assertion for quantity line charts, rephrased the presentation speaker-note meta wording, regenerated `1.1.3`, and reran the focused gates. Review records now exist and the sprint is ready for focused human recheck, but it is not closed until the lead-review summary records a final verdict.

Updated: 2026-05-18 (L1.6 close) - focused re-review accepted the `Broodjesverkoop` graph-order fix and presentation speaker-note polish. L1.6 closed PASS WITH FLAGS. `1.1.3-quality-ref.yaml` now records `pass_with_flags`; all review records, closure log, and roadmap agree. L1.7A is next, with flags carried forward for scaffolded graphical-game MVP scope, later harder graph-reading variants, the migrated/not-final-reviewed v5 target exercise, non-blocking Part A flags, and PV-G4 blocked-use boundaries.

Updated: 2026-05-18 (SYNC-1 roadmap reconciliation) - after reading the post-L1.6 strategy paper and checking current lesson/reference roadmap state, L1.7 was reframed as `L1.7A Scaling Readiness And Flag Triage Gate`. Broad lesson scaling is not approved. The next lesson-side work is a readiness/triage decision, followed by Book 1 flag burn-down/house-style cleanup before any broader production decision. The rough three-year blueprint is treated as a non-authoritative planning prototype for the reference team, not a curriculum source of truth.

Updated: 2026-05-19 (L1.6R revise addressed) - L1.6R human review returned REVISE after confirming the main explanation surfaces now show real graph/table objects but finding that guided-practice visuals did not match several exercise prompts. Platform source now generates exercise-specific guided visuals for broodjes, koffie, bioscoop, and water/index; the focused L1.6R Jest gate includes visual-value concordance; `1.1.3-quality-ref.yaml` marks the companion status as guided-concordance revised pending human review. Green gates: deploy link/data checks 417 refs + 217/217 data tests, focused L1.6R Jest 5/5, presentation screenshot QA 30 screenshots, rich-page screenshot QA 20 screenshots, complete student-web validation, publisher-print Part A validation, procedure-contract validator 341 checks, Book 1 health 26/26, and full platform Jest 515 passed / 8 skipped. L1.6R is ready for focused human recheck but not closed.

Updated: 2026-05-19 (L1.6R close) - focused human recheck accepted the guided-practice visual-value concordance correction and closed L1.6R as PASS WITH FLAGS. `1.1.3-quality-ref.yaml` now records `human_review_status: "pass_with_flags"` and `l16r_dual_coding.status: "pass_with_flags"`. L1.6R sprint plans, review records, QA reports, closure log, and screenshots are archived under `archive/sprints/L1.6R/`. L1.7A is now the active readiness/modality gate; broad scaling remains paused until that decision is recorded.

Updated: 2026-05-21 (L-CP6E close) - CP.6e failed references-side clearance because `1.1.3` Part A still introduced figures as `1 -> 3 -> 2`. L-CP6E fixed the owning paragraph source, swapped the axis-convention and interpolation figure numbering, regenerated paragraph/Chapter 1.1/Book 1 publisher-print outputs, and updated `1.1.3-review.md` plus `1.1.3-quality-ref.yaml`. Focused markdown/HTML/PDF order checks now read `1 -> 2 -> 3`; `validate-paragraph`, `validate-chapter`, Book 1 health 26/26, print scope 12/12, and v5 target-exercise count validation pass. CP-6 and Year 1 remain open pending references-side CP.6f recheck.

Updated: 2026-05-22 (companion pre-scale roadmap update) - added three explicit pre-scale sprints after L1.7A: the original `L1.7B Exit Ticket Game MVP + Companion Completion Contract` lane, `L1.7C Three-Aspect Game Quality Upgrade`, and `L1.7D Paragraph Landing Page Information Architecture Cleanup`. The original L1.7B lane was later split into `L1.7B-C` contract-only evidence and `L1.7B-R` future MVP resume. This sharpens the foundation-hardening stance: broad companion scaling is blocked not only by quality flags, but also by product-sprawl risk. The roadmap now requires a complete companion-set contract, a reusable game-row quality rubric, and a landing-page route hierarchy before Scale Gate 1. A local untracked platform candidate exists at `../4veco-platform/knowledge/exit-ticket-game-1.1.1.zip`; L1.7B-R must either bring the prototype under source-control review or rewrite it before implementation.

Updated: 2026-05-22 (shared skill-map architecture) - added `L1.7C-0 Shared Skill-Map Engine Contract` before the three-aspect game upgrade. The roadmap now frames the scalable game architecture as three practice engines (`Redeneren`, `Rekenen`, `Grafieken`) plus one shared skill-map / skill-tree engine for progression display, aspect filtering, recommendations, prerequisites, locked/open/completed states, stars/progress, and scoped routes. The exit ticket uses compact checkpoint mode; landing IA must consume the shared architecture rather than expose separate full skill-tree UIs. Broad game and companion scaling remain blocked.

Updated: 2026-05-23 (L1.7A close) - L1.7A closed PASS WITH FLAGS as a readiness decision sprint. Current validation is green for `1.1.1` through `1.1.3`, procedure contracts, Book 1 health, print scope, and v5 target-exercise counts. Decision: not ready for broad companion scaling. Continue controlled foundation hardening through L1.7B-C contract evidence, L1.7C-0, L1.7C, L1.7D, L2.0, L1.7B-R, GATE-L1.7B, then Scale Gate 1.

Updated: 2026-05-23 (L1.7B-C contract-and-stop) - L1.7B-C inspected the local untracked exit-ticket prototype, ran its prototype unit test in a temp copy, and recorded the prototype as design evidence only. The companion-completion contract and future MVP scope now exist under `archive/sprints/L1.7B/`. Implementation is paused because the prototype is not source-controlled, uses mastery/score/pass/evidence/adaptive-focus semantics, and depends on compact checkpoint-mode skill-map behavior that did not yet exist at the time. L1.7C-0 then defined the shared skill-map engine contract; L1.7B-R remains the later safe resume path.

Updated: 2026-05-23 (L1.7C-0 close) - L1.7C-0 closed PASS WITH FLAGS as a contract sprint. The shared skill-map contract now defines one common route/progression layer for `Redeneren`, `Rekenen`, `Grafieken`, the later exit ticket, and landing-page route previews. It defines `compact`, `route`, and restricted `full` modes; aspect filters for reasoning, calculation, graphical, and explicit mixed views; non-mastery state/progress language; accessibility expectations; and product-use boundaries. Platform implementation is handed to `GAME-UX-1`; L1.7C is now active and must stop if meaningful game-row review requires that implementation first.

Updated: 2026-05-23 (GAME-UX-1 received) - Platform `GAME-UX-1` completed the shared skill-map runtime at commit `6509895`, tag `checkpoint/GAME-UX-1-shared-skill-map-engine`. L1.7C can now proceed past the prior implementation dependency. The lesson-side first block is to deploy/regenerate through the platform workflow so Book 1 actually consumes the shared engine, then audit `Redeneren`, `Rekenen`, and `Grafieken` against the L1.7C rubric. GAME-UX-1 generated no lesson output and did not import the untracked exit-ticket prototype.

Updated: 2026-05-23 (L1.7C technical QA ready) - L1.7C regenerated the Book 1 game-row surfaces through the platform workflow. `Redeneren`, `Rekenen/Stappenplan`, and `Grafieken` now load a shared compact skill-map route panel; §1.1.3 `Grafieken` also has a less-labelled `Broodjesverkoop` variant with y-axis ticks. Technical gates are green: deploy/link/data checks, complete student-web validation for `1.1.1`-`1.1.3`, procedure-contract validation 341 checks, Book 1 health 26/26, v5 target-exercise validation 54 records with 12/12/14/16, and full platform Jest 542 passed / 8 skipped. L1.7C is ready for human review, not closed.

Updated: 2026-05-23 (L1.7C targeted revise addressed) - L1.7C first human review returned REVISE because the shared route panel could show internal IDs such as `A61` in the student-facing focus line. The targeted fix now renders the focus label from the visible skill label, adds a focused `A61` regression test, refreshes `1.1.1` landing copy so it only lists available routes, and records route-panel screenshot evidence under `archive/sprints/L1.7C/L1.7C-screenshots/`. L1.7C is focused-recheck ready, not closed.

Updated: 2026-05-24 (L1.7C close) - Focused human recheck accepted the route-label fix and closed L1.7C PASS WITH FLAGS. The shared game-row route is acceptable for controlled paragraph-limited use. Carried flags: `Rekenen` remains procedure practice rather than a full numeric calculation engine, `Grafieken` has one less-labelled variant rather than a full future graph-heavy set, `Redeneren` needs richer variants and replay value before scaling, and reusable game screenshot QA should mature. L1.7D is now the active foundation-hardening sprint.

Updated: 2026-05-24 (L1.7D technical QA ready) - L1.7D implemented the paragraph landing-page information architecture through the platform generator and regenerated Book 1 landing output. Paragraph landings now use `Start`, `Leer`, `Oefen`, optional `Check`, and `Verdiep`; `Check` is hidden until a reviewed exit-ticket exists; `Oefen` exposes guided support plus scoped `Redeneren`, `Rekenen / stappenplan`, and `Grafieken` routes where available; the full skill map and source/download surfaces are collapsed under `Verdiep`. Technical gates are green: deploy/link/data checks, focused landing Jest, complete student-web validation for `1.1.1`-`1.1.3`, procedure-contract validation 341 checks, Book 1 Part A health 26/26, v5 target-exercise validation 54 records with 12/12/14/16, representative desktop/mobile light/dark screenshot QA, and full platform Jest 543 passed / 8 skipped. L1.7D is ready for human review, not closed.

Updated: 2026-05-24 (L1.7D close) - Human review accepted L1.7D as PASS WITH FLAGS. The controlled route IA is accepted for paragraph-limited use and no implementation revision is required. Carried flags: `Rekenen / stappenplan` is not a full numeric calculation engine, `Check` remains hidden until a reviewed non-summative exit-ticket exists, screenshot evidence is representative, and `1.1.4 Gemengde opgaven` needs a dedicated consolidation landing pattern before broad scale. L2.0 is now the active foundation-hardening cleanup sprint; broad companion scaling remains blocked.

Updated: 2026-05-25 (exit-ticket and Scale Gate precision) - L1.7B is split into `L1.7B-C` and `L1.7B-R`. `L1.7B-C` is the closed contract-only evidence: old untracked draft inspected, companion-completion contract recorded, future implementation scope recorded, and implementation paused. `L1.7B-R` is the future boundary-safe exit-ticket checkpoint resume and remains required before Scale Gate 1 unless explicitly waived by human decision. Added `GATE-L1.7B` as the exit-ticket product-boundary review gate. L2.0 now must classify L1.7C game-row carried flags as fix-before-scale / carry / defer and define an exit-ticket readiness checklist. Scale Gate 1 now requires or explicitly waives L2.0, L1.7B-R, GATE-L1.7B, L1.7C flag disposition, L1.7D landing IA, minimal curriculum-versioning readiness, and reference-side GATE-EX5 status.

Updated: 2026-05-25 (L2.0 technical QA ready) - L2.0 created the house-style baseline, PASS WITH FLAGS definition, flag-disposition table, quality-ref status standard, validation log, technical QA report, and human-review packet. The platform landing generator now treats consolidation/gemengde-opgaven pages as mixed-practice pages: `1.1.4 Gemengde opgaven` shows `Oefen gemengd` and no longer appears as Verdiep-only. Green gates: focused landing Jest 2/2, deploy link/data checks, complete student-web validation for `1.1.1`-`1.1.3`, `1.1.4` publisher-print validation, Book 1 health 26/26, procedure contracts 341 checks, v5 target-exercise counts 54 with 12/12/14/16, `1.1.4` desktop/mobile light/dark screenshot QA, and full platform Jest 544 passed / 8 skipped. L2.0 is ready for human review, not closed; broad companion scaling remains blocked.

Updated: 2026-05-25 (L2.0 close) - Human review accepted L2.0 as PASS WITH FLAGS. No implementation revision is required. The consolidation landing rule is accepted: `1.1.4 Gemengde opgaven` presents as `Oefen gemengd`, not as a `Verdiep`-only leftover. L2.0 also closes the house-style baseline, PASS WITH FLAGS definition, flag-disposition table, quality-ref status standard, screenshot/QA expectations, and exit-ticket readiness checklist. Carried flags: `1.1.4` remains legacy `FLAG`; graph-drawing consolidation and profit-formula framing need later content review; `Rekenen / stappenplan` is not a full numeric calculation engine; graph/reasoning game variants remain limited-scope and not scale-approved; exit-ticket implementation remains L1.7B-R/GATE-L1.7B; broad companion scaling remains blocked.

Updated: 2026-05-25 (L1.7B-R platform handoff) - L1.7B-R created its operational resume plan and stopped before implementation. The lesson team issued `archive/sprints/L1.7B-R/L1.7B-R-platform-support-request.md` for platform `GAME-UX-2`, because the platform roadmap still treats the exit-ticket checkpoint engine as a future support lane pending GATE-EX5 or explicit waiver. No old-draft import, platform runtime code, generated lesson output, landing `Check` activation, screenshot QA, or human-review packet was produced. L1.7B-R remains not checkpoint-closed; GATE-L1.7B remains blocked until a source-controlled generated checkpoint surface exists and is reviewed.

Updated: 2026-05-26 (L1.7B-R platform support received) - Platform `GAME-UX-2` completed and pushed the source-controlled exit-ticket checkpoint engine. Lesson output commit `5c47961269096c21a7d50bbc97c71de7984ff6e1` now contains generated `1.1.1` checkpoint output and landing-page `Check` activation through platform scripts only. L1.7B-R added platform-response, technical-QA, screenshot archive, and human-review packet records under `archive/sprints/L1.7B-R/`. Technical QA is green, but L1.7B-R remains open pending human review. The lead review must explicitly resolve the internal skill-scope metadata question: generated checkpoint metadata uses `A43`/`A04`, while the `1.1.1` paragraph plan names `B01`/`B02`. GATE-L1.7B remains required before Scale Gate 1.

Updated: 2026-05-26 (L1.7B-R close) - Human review accepted L1.7B-R as PASS WITH FLAGS. The `1.1.1` exit-ticket checkpoint is accepted as a boundary-safe, non-summative controlled paragraph-limited checkpoint surface. The metadata mismatch is explicitly carried as `L1.7B-R-CF1`: generated checkpoint metadata uses `A43`/`A04`, while the paragraph plan names `B01`/`B02`; this must not be used for diagnostics, mastery, sequencing, target-exercise promotion, CP-6/Year-1, PV, Scale Gate 1, or broad-scaling evidence until fixed or mapped. GATE-L1.7B is now the active required product-boundary review before Scale Gate 1.

Updated: 2026-05-26 (GATE-L1.7B packet) - Created the missing GATE-L1.7B review records under `archive/sprints/GATE-L1.7B/`: sprint plan, validation log, and human-review packet. The gate is ready for human review but not closed. No product output was generated. The packet requires the reviewer to confirm the exit-ticket product boundary and explicitly carry or resolve `L1.7B-R-CF1` before any Scale Gate 1 reliance.

Updated: 2026-05-26 (GATE-L1.7B close) - Human review accepted GATE-L1.7B as PASS WITH FLAGS. The `1.1.1` checkpoint product boundary is accepted as a non-summative, practice-oriented `Check` surface for controlled paragraph-limited use. The metadata mismatch remains live as `GATE-L1.7B-CF1`: generated checkpoint metadata uses `A43`/`A04`, while paragraph-plan skills are `B01`/`B02`. This blocks metadata reliance for diagnostics, mastery, sequencing, target-exercise promotion, CP-6/Year-1, PV, Scale Gate 1 scale evidence, or broad exit-ticket scaling until platform B-unit scoping or a reviewed mapping layer exists. Scale Gate 1 remains a separate future joint decision.

Updated: 2026-05-26 (exit-ticket quality ladder) - Added a stricter pre-scale exit-ticket quality path before Scale Gate 1: `L1.7B-MAP` for skill-metadata alignment, `L1.7B-P23` for 1.1.2/1.1.3 checkpoint designs, `L1.7B-Q2` for target-exercise-readiness checkpoint proof, and `GATE-L1.7B-Q2` for completion/readiness language. This records the human/reviewer concern that the current `1.1.1` exit ticket is only a short non-summative checkpoint surface, not a target-exercise-readiness test. Scale Gate 1 may not treat exit tickets as scale or target-readiness evidence unless metadata alignment closes and either Q2 closes or Scale Gate 1 explicitly limits exit tickets to non-summative checkpoint status.

Updated: 2026-05-26 (skill-tree math route correction) - Added `L1.7C-MATH Restore Skill-Tree Math Game Primary Route` before Scale Gate 1. Review of L1.7C-0/L1.7C/L1.7D history shows that GAME-UX-1 added the shared skill-map display layer and did not remove the old `wiskundevaardigheden` skill-tree math game, but L1.7D's landing generator made `stappenplan` the primary `Rekenen` route and pushed the old skill-tree math game into `Verdiep` as `Volledige vaardigheidskaart`. That displacement is now treated as a pre-scale route defect. L1.7C-MATH must restore the old skill-tree math game as the primary math practice route, keep `stappenplan` as support/extra steps, and re-audit the full four-part architecture: math skill-tree game, reasoning game, graph game, and shared skill-map route/display layer.

Updated: 2026-05-26 (core-spec hardening) - Tightened the pre-scale sequence after human review feedback that restricted scope-language must not weaken the original product specification. `L1.7C-MATH` was added as the first hard blocker because the primary math route was wrong; it later closed PASS WITH FLAGS. `L1.7B-MAP`, `L1.7B-P23`, `L1.7B-Q2`, and `GATE-L1.7B-Q2` now explicitly restore the exit-ticket path from short checkpoint to target-exercise-readiness evidence before stronger claims. Added `REV-STD-1 Core-Spec Review Standard Hardening` before Scale Gate 1 so PASS WITH FLAGS cannot carry core-spec failures, and Scale Gate 1 is blocked until these sprints are closed or explicitly waived by human decision with consequences.

Updated: 2026-05-26 (L1.7C-MATH technical QA) - Platform generator changes restored scoped `wiskundevaardigheden.html` as the primary `Rekenen` route for `1.1.2` and `1.1.3`, kept `stappenplan.html` visible as `Rekenstappen` support, and prevented the unscoped/full-catalog `1.1.1` skill-tree file from becoming primary practice. Lesson output was regenerated through platform deploy only. Technical QA is green: focused landing Jest 4/4, full platform Jest 555 passed / 8 skipped, deploy link/data checks 472 refs + 221 data tests, complete student-web validation for `1.1.1`-`1.1.3`, Book 1 health 26/26, procedure contracts 341 checks, target exercises 54 records with 12/12/14/16, and screenshot QA for landing/skill-tree/reasoning/graph surfaces across desktop/mobile light/dark. L1.7C-MATH is ready for human review but not closed.

Updated: 2026-05-26 (L1.7C-MATH targeted revise fix) - First L1.7C-MATH human review returned REVISE because the restored math-game result state could expose internal skill IDs such as `Volgende: A39`. Targeted platform revision now uses student-facing skill labels in result next-action copy, replaces visible dependency-node IDs with `Vaardigheid`, and extends screenshot QA to exercise the skill-tree page to a post-result state. Focused evidence shows `Volgende: Prijsindex (CPI) berekenen` and `skillTreeResultHasInternalCode: false`. Validation is green: focused visible-copy/landing Jest 14 tests, full platform Jest 557 passed / 8 skipped, complete student-web validation for `1.1.1`-`1.1.3`, Book 1 health 26/26, procedure contracts 341 checks, target exercises 54 records, and 17 screenshot QA captures. At this point L1.7C-MATH was focused-recheck ready but not closed; the later close entry records the final verdict.

Updated: 2026-05-26 (L1.7C-MATH close) - Focused human recheck accepted L1.7C-MATH as PASS WITH FLAGS. The old skill-tree math game is restored as primary `Rekenen` for scoped `1.1.2` and `1.1.3`, `stappenplan.html` remains `Rekenstappen` support, and unscoped `1.1.1` remains collapsed as `Brede vaardigheidskaart`. The prior result-state ID leak is fixed: result copy uses labels such as `Volgende: Prijsindex (CPI) berekenen`, and dependency node captions no longer expose raw `A##` IDs. Local screenshot evidence confirms 17 files including the post-result screenshot. Carried flags: skill-tree progress language must remain practice-only, restored math is not target-exercise-readiness evidence, keyboard/focus-order proof should strengthen before scale, and scoped skilltree comments need cleanup. Scale Gate 1 remains blocked by the remaining exit-ticket metadata/readiness and review-standard sprints.

Updated: 2026-05-26 (active-next roadmap correction and close-out policy) - Promoted `L1.7B-MAP` to the top of the sprint ledger as the active next sprint after L1.7C-MATH closure, moved L1.7C-MATH below the remaining open pre-scale sequence as a closed Scale Gate flag carrier, and removed L1.7C-MATH from the list of still-open Scale Gate blockers. Added an explicit sprint close-out communication policy: final chat after a sprint must state the next step if work simply continues, or state that the next step is paused pending human decision.

Updated: 2026-05-26 (L1.7B-MAP close) - Human review accepted L1.7B-MAP as PASS WITH FLAGS. The `1.1.1` checkpoint metadata now uses `B01/B02` for checkpoint-assessed target/scope fields, removes `A04`, records the target-exercise skill set as `A43/B01/B02`, and keeps `targetReadinessEvidence: false`. This resolves the prior metadata mismatch for the current checkpoint role, but it does not make the checkpoint target-exercise-readiness evidence. Scale Gate 1 remains blocked until L1.7B-P23, L1.7B-Q2, GATE-L1.7B-Q2, and REV-STD-1 close or are explicitly waived by human decision with consequences. If work continues, the next step is L1.7B-P23.

Updated: 2026-05-26 (L1.7B-P23 stop/handoff packet) - L1.7B-P23 is ready for human review. The sprint plan was upgraded to the current quality-standard format. Baseline audit and operation-chain analysis show that `1.1.2` requires calculation/work fields, final answer entry, unit or percentage/index notation, and short explanation, while `1.1.3` requires table/graph handling, economic axis convention, graph drawing or point placement, interpolation, and short explanation. The current exit-ticket engine/UI supports only choice tasks, so the sprint stopped and wrote a platform handoff instead of generating weak generic MC checks. `Check` remains hidden for `1.1.2` and `1.1.3`; no source data or generated exit-ticket output was created. If work continues, the next step is the L1.7B-P23 human review.

Updated: 2026-05-28 (L1.7B-P23 close) - Human review accepted L1.7B-P23 as PASS WITH FLAGS. The stop/handoff decision is accepted as the correct product decision: generating choice-only exit tickets for `1.1.2` and `1.1.3` would undercut the target-exercise-readiness specification. `Check` remains hidden for both paragraphs and no generated exit-ticket output was created. The next blocker is shared task-type shell support before L1.7B-Q2 can honestly produce readiness evidence for calculation or graph/table paragraphs.

Updated: 2026-05-29 (engine operationalization track) - SYNC-4 updated the
product and companion specifications so the shared task-type UI is part of the
end-state product, not exit-ticket-only implementation detail. The roadmap now
requires `GAME-UX-3A` shared task shell, `ENGINE-OP-1` student-path audit,
`SKILLMAP-OP-1` visible route work, graph/math/reasoning integration rows,
`GAME-ARCH-1` build-vs-rebuild decision, and `GATE-ENGINE-1` live-output human
review before engine scale or Scale Gate 1 reliance. This authorizes no engine
code, generated lesson output, target-exercise writes, protected reference
mutation, diagnostics, mastery, sequencing, summative use, student-facing AI,
PV projection, PV machine promotion, or student/product use.

Updated: 2026-05-29 (GATE-MTU-H4 closure) - Platform GATE-MTU-H4 closed PASS
WITH CONDITIONS for answer-form/question-type routing only. It authorizes only
`MTU-H4A` bounded answer-form planning, with a held Type 4 /
motiveer/classificatie lane, `bron` as source-use modifier plus underlying
answer form, graph/draw/shade planning-only until stronger evidence, held
analysis/evaluation, visible q3/q15 EX overlays, no candidate storage, no
target-exercise field writes, and no student/product use.

Updated: 2026-05-29 (SPEC-ET-1 close) - SPEC-ET-1 corrected the product and
companion specifications so the exit ticket is the paragraph
target-equivalent proof task rather than merely readiness-to-try. Successful
completion may justify only local non-summative paragraph-completion language
after `GATE-L1.7B-Q2` approves the same-level operation-chain and answer-form
proof. The roadmap now includes `EX-LESSON-1`, revises `GAME-UX-3A`,
`L1.7B-Q2`, `GATE-L1.7B-Q2`, and Scale Gate 1 around target-equivalent proof,
and ties official-exam ingestion to the student-facing paragraph route. This
authorizes no generated output, engine code, protected reference mutation,
target-exercise mutation, diagnostics, mastery, sequencing, summative use,
student-facing AI, PV projection, PV machine promotion, Scale Gate 1, or
student/product use.

Updated: 2026-05-30 (GAME-UX-3A close) - Platform GAME-UX-3A completed the
shared task-type UX foundation without generated lesson output or product
exposure. It added a reusable task-shell runtime, static UI renderer, CSS,
exit-ticket shell load hooks, deploy copy support, fixtures, focused tests,
and lesson-side closure records. The supported task families now include
numeric input, calculation/work capture, final-answer entry, unit/notation
field, short constructed response, table-value selection, graph reading, point
placement, graph-construction substitute, and structured reasoning. This
closes runtime foundation only. ENGINE-OP-1 has since proved that current
generated output does not yet use the shell; SKILLMAP-OP-1 has since made the
shared route visible and scoped, GRAPH-UX-2 has integrated the shell into live
graph/table output, MATH-UX-2 has integrated the shell into live
calculation/index output, REASON-UX-2 has integrated the shell into reasoning
output, and GAME-ARCH-1 has closed the build-vs-rebuild decision. GAME-ARCH-2
is now the next dependency before `GATE-ENGINE-1`, `L1.7B-Q2`,
`GATE-L1.7B-Q2`, or Scale Gate 1 rely on the shared task shell and route
system.

Updated: 2026-05-31 (ENGINE-OP-1 close) - Platform ENGINE-OP-1 completed the
four-engine operational proof audit with screenshots, a screenshot manifest,
student-path trace, and operational findings. It found real practice progress
in `1.1.3` graph work and `1.1.2` math work, but also found that generated
output does not yet use the GAME-UX-3A task shell, `1.1.2` and `1.1.3` still
have no target-equivalent checkpoint route, and several shared skill-map route
panels are empty or mis-scoped. SKILLMAP-OP-1 has since closed route-visibility
proof, GRAPH-UX-2 has since closed graph/table task-shell integration, and
MATH-UX-2 has since closed math/calculation task-shell integration. GAME-ARCH-1 has since closed. Active next sprint is GAME-ARCH-2. No target-equivalent completion
claim, Scale Gate 1, diagnostics, adaptive routing, mastery/sequencing,
summative use, AI, PV, or product use is authorized.

Updated: 2026-05-31 (GAME-ARCH-1 close) - Platform GAME-ARCH-1 completed the
no-generated-output architecture decision sprint after lead-review round 2 PASS. Decision: keep and harden
the shared skill-map route, keep the shared task shell as core architecture,
keep/refactor the graph UI direction as the reference pattern, refactor math
around target-exercise operation chains, refactor reasoning around answer-form
and constructed-response standards, keep the short check as an advisory local
checkpoint, and keep the target-equivalent exit ticket separate as a later
proof task. GAME-ARCH-2 is the required integrated practice-engine
architecture plan before GATE-ENGINE-1. GATE-ENGINE-1 must inspect live rendered output and explicitly decide
keep/refactor/rebuild/hold for each component. No generated lesson output,
target-equivalent completion claim, Scale Gate 1, diagnostics, adaptive
routing, mastery/sequencing, summative use, AI, PV, or product use is
authorized.

Updated: 2026-05-31 (GAME-ARCH-2 close) - Platform GAME-ARCH-2 completed the
integrated practice-engine architecture plan after lead-review round 2 PASS
WITH FLAGS. It produced the canonical route-layer API, task-shell API, module
boundaries, file-level keep/wrap/deprecate/rebuild inventory, state ownership,
feedback ownership, target-operation coverage model, and GATE-ENGINE-1
live-output checklist. Lead review caught and corrected the missing
`engines/skill-map-engine.js` route-engine disposition. GATE-ENGINE-1 has since
closed PASS WITH FLAGS. No generated lesson output, engine implementation,
target-equivalent claim, diagnostics, adaptive routing, mastery/sequencing,
summative use, AI, PV, or product use was authorized.

Updated: 2026-05-31 (GATE-ENGINE-1 close) - Platform GATE-ENGINE-1 closed PASS
WITH FLAGS after human review and fresh live-output inspection. Decision:
keep/harden the shared route layer, keep the shared task shell, keep/refactor
graph as reference pattern, refactor math around `1.1.2` target-operation
coverage, refactor reasoning around answer-form and constructed-response
standards, keep/relabel the advisory short check if needed, and keep
target-equivalent exit tickets separate for L1.7B-Q2/GATE-L1.7B-Q2. It
authorized only named planning/preparation sprints (`GRAPH-REFINE-1`,
`MATH-REFINE-1`, `REASON-REFINE-1`, `CHECK-Q2-PLAN`). No implementation,
generated output, target-equivalent completion language, diagnostics,
adaptive routing, mastery/sequencing, summative use, AI, PV, Scale Gate 1, or
product use is authorized.

Updated: 2026-05-31 (GRAPH-REFINE-1 close) - Platform GRAPH-REFINE-1 closed
PASS WITH FLAGS as planning/preparation only. It kept GRAPH-UX-2 as the
current graph/table reference pattern for local practice, but found that the
`1.1.3` route cannot be used as target-equivalent graph evidence yet: the
target exercise requires price on the vertical axis and quantity on the
horizontal axis, while current graph-route data still contains contradictory
price-as-horizontal/x wording. A later GRAPH-REFINE-2 repair is recommended
only if explicitly authorized. Remaining authorized planning/preparation lanes
are MATH-REFINE-1, REASON-REFINE-1, and CHECK-Q2-PLAN. No implementation,
generated output, target-equivalent completion language, diagnostics,
adaptive routing, mastery/sequencing, summative use, AI, PV, Scale Gate 1, or
product use was authorized.

Updated: 2026-05-31 (MATH-REFINE-1 close) - Platform MATH-REFINE-1 closed
PASS WITH FLAGS as planning/preparation only. It kept MATH-UX-2 as useful
local A38/A39 math/calculation practice and confirmed the route should be
refactored rather than rebuilt, but found that the `1.1.2` route cannot be
used as target-equivalent math evidence yet: the target exercise requires
explicit D31 coverage of the index-point trap, including a checked short
explanation that 108 to 112 is 4 index points, not 4 percent. A later
MATH-REFINE-2 repair is recommended only if explicitly authorized. Remaining
authorized planning/preparation lanes are REASON-REFINE-1 and CHECK-Q2-PLAN.
No implementation, generated output, target-equivalent completion language,
diagnostics, adaptive routing, mastery/sequencing, summative use, AI, PV,
Scale Gate 1, or product use was authorized.

Updated: 2026-05-31 (REASON-REFINE-1 close) - Platform REASON-REFINE-1 closed
PASS WITH FLAGS as planning/preparation only. It kept the reasoning route and
shared `structured_reasoning` task family as useful local practice, but found
that target-equivalent reasoning reliance is blocked until answer-form-specific
scaffolds are added and reviewed: generic self-check is not answer-form proof,
`1.1.1` needs an A98 versus held-evaluation decision, `1.1.2` D31 explanation
must coordinate with math/D31 coverage, and `1.1.3` source/table reasoning
needs A81 source-use scaffolding plus graph-axis repair. CHECK-Q2-PLAN has
since closed as planning/preparation only. No implementation, generated
output, reasoning CSV edits, target-equivalent completion language,
diagnostics, adaptive routing, mastery/sequencing, summative use, AI, PV,
Scale Gate 1, or product use was authorized.

Updated: 2026-05-31 (CHECK-Q2-PLAN close) - Platform CHECK-Q2-PLAN closed
PASS WITH FLAGS as planning/preparation only. It preserved the short check as
advisory local route advice and kept the target-equivalent exit ticket as a
separate proof task for L1.7B-Q2/GATE-L1.7B-Q2. It confirmed no current
`1.1.1`, `1.1.2`, or `1.1.3` output is target-equivalent proof. `1.1.1`
needs full A43 coverage plus an A98 versus held-evaluation decision, `1.1.2`
needs explicit D31 index-point versus percentage-change coverage, and `1.1.3`
needs graph-axis repair plus A81 source-use with an underlying answer form.
Future L1.7B-Q2 must select one paragraph and resolve or explicitly scope its
blockers before implementation. No source exit-ticket writes, generated
output, target-equivalent completion language, diagnostics, adaptive routing,
mastery/sequencing, summative use, AI, PV, Scale Gate 1, or product use was
authorized.

Updated: 2026-05-26 (product end-state canonicalization) - Added `SPEC-END-STATE` and created `specifications/product-end-state.md` as the canonical product north star outside the active roadmap. The end-state sentence is now fixed: for every paragraph, 4veco gives the student a visible route from current readiness to target-exercise readiness. Future exit-ticket, game-row, exam-ingestion, review-standard, and Scale Gate work must cite this baseline and may not use restricted scope-language to weaken the full product specification.

Updated: 2026-05-26 (stable companion specification) - Added `specifications/companion-core-specifications.md` as a smaller, more static specification baseline outside the active roadmap and sprint folders. Future roadmap and sprint changes must reconcile against this file; if a sprint ships a smaller bounded scope, the missing specification work must be assigned to a named follow-up sprint or changed through explicit specification review.

Updated: 2026-05-26 (scope-language enforcement) - Closed `SCOPE-LANG-1`. The companion spec now has a stricter Scope-Language Discipline section, current active roadmap/version wording is neutralized, and platform sprint checkers now block unauthorized restricted scope terms unless an explicit authorization section preserves the quality floor and names follow-up or waiver work. This does not rewrite historical archives; it prevents new planning drift.

Updated: 2026-05-26 (planning quality standard enforcement) - Closed `QUALITY-STD-1`. Both repo agent instructions now require quality-driven execution, the companion spec has a Specification-Fulfilment Rule and Planning Quality Floor, platform paragraph-build guidance includes a quality standard and fulfilment matrix, and the sprint-plan checker now fails plans that omit the quality standard, specification fulfilment matrix, quality improvement candidates, or proof required to close. REV-STD-1 remains open for wider review-packet and lead-review hardening, but future platform sprint plans now have quality pressure at plan-formation time.

Updated: 2026-05-19 (L-CP6A close) - lesson-side CP.6a remediation closed PASS WITH FLAGS. A platform-owned migration script aligned active Book 1 Chapter 1.3 to v5, archived displaced costs/revenue material for Book 2 survival, regenerated `1.3.2`, `1.3.3`, `1.3.4`, Chapter 1.3, and aggregate Book 1 output, and preserved the rule that CP-6/Year 1 are not closed here. Green gates: Chapter 1.3 validation, Book 1 health 26/26, print-scope 12/12, v5 target-exercise counts 54 with 12/12/14/16, focused book Jest 7/7, full platform Jest 515 passed / 8 skipped. References-team handoff: `archive/sprints/L-CP6A/L-CP6A-handoff-to-references.md`.
Updated: 2026-05-20 (EX-NS0 exam-ingestion north-star) - official exam-target paragraph work is now explicit as a future cross-repo endpoint. The platform side owns exam-ingestion overlays, source-annex and answer-model traceability, MTU mapping, and operation classification. The lesson side now inserts L-EX0 and L-EX1 before L2.4-TEA: first define the paragraph-plan contract and review checklist, then run one controlled pilot paragraph around a real official exam question. This update authorizes no broad production, no generated-output hand patching, no CP-6/Year-1 closure, no target-exercise promotion, and no diagnostics/adaptive/mastery/summative/student-facing AI use.
Source: split from `knowledge/three-month-roadmap.md` after Sprint 0.5 sign-off

## Mission

Own the material side of delivery:

- Book 1 release polish
- Book 1 foundation hardening and flag burn-down
- Book 2 Part A textbook production only after the foundation gates allow it
- companion bounded-scope work, treated as controlled next-step production until quality and usability are good enough to scale
- exam-target paragraph contracts, once the platform reference layer provides official exam prompt, source-annex, correction-model, MTU, and answer-operation evidence

## Current Status

Sprint 0.5 is signed off for Part A textbook/book production.

That means:

- Book 1 Part A is green.
- Book 1 print scope has completed the urgent L1.5P cut and is the current
  publisher-print baseline.
- Book 2 Part A should wait until the remaining foundation blockers clear.
  Closed prerequisites now include L1.7A, L1.7B-C, L1.7C-0, L1.7C, L1.7D,
  L2.0, L1.7B-R, GATE-L1.7B, L1.7C-MATH, L1.7B-MAP, L1.7B-P23,
  reference-side GATE-MTU-H4 routing review, MTU-H4A through MTU-H4C,
  SPEC-ET-1, EX-LESSON-1, GAME-UX-3A, ENGINE-OP-1, SKILLMAP-OP-1,
  GRAPH-UX-2, MATH-UX-2, REASON-UX-2, GAME-ARCH-1, GAME-ARCH-2,
  GATE-ENGINE-1, GRAPH-REFINE-1, and L1.7B-Q2.
  Still-open blockers are GATE-L1.7B-Q2, REV-STD-1, REF-CT0/REF-CT1, and the later scale gate unless a
  human Scale Gate waiver explicitly accepts the consequences.
- Companion production may continue only as controlled next-step production; it
  is not approved for broad scaling.

The first companion controlled-scope run has now been completed, and the technical pattern has also
been repeated for a second paragraph. The 1.1.2 probe materials were removed
after the technical test because that paragraph must be recreated with explicit
teaching and didactic design instructions. That does not finish the companion controlled-scope route.
The main current issue is companion layout, image integration, and front-end
usability: the materials need to feel more usable, readable, navigable, and
visually coherent before this pattern is repeated across many paragraphs. Images and
graphs should no longer feel like pasted textbook assets. They must be adapted
to the surface where they appear: web pages, PowerPoint presentations, Word
documents, summaries, and interactive/game pages can each need different layout,
contrast, scale, and annotation treatment.

Important boundary:

- A complete paragraph plus companion pipeline is not yet routine.
- The first companion paragraph proves that the workflow can run, not that the
  output design is good enough.
- Bulk companion production should wait until layout/UI improvements and
  quality-gate decisions are integrated into the platform workflow.
- Bulk companion production should also wait until visual assets have a
  platform-owned variant workflow, including light/dark web variants where
  graphics contain labels, axes, fills, backgrounds, or other theme-sensitive
  elements.

## Team Guardrails

- Keep Book 1 green while editing:

```powershell
npm.cmd run check:book -- "..\4veco-lessen\Boek 1 - Grondslagen, vraag en aanbod"
```

- Reviews and quality refs are mandatory artifacts, not optional paperwork.
- Stable product specifications live in `specifications/product-end-state.md`
  and `specifications/companion-core-specifications.md`; read both files
  before changing roadmap scope, sprint scope, or review criteria.
- Bounded-scope labels are not permission to undercut the stated product
  specification. If a sprint deliberately ships a smaller version, the roadmap
  must name the sprint that restores the full specified product. New sprint
  titles, roadmap rows, review packets, and agent plans must follow the
  Scope-Language Discipline section in
  `specifications/companion-core-specifications.md`.
- `PASS WITH FLAGS` may not hide a core-specification failure. A flag that
  changes the student's primary route, source-of-truth metadata,
  target-exercise readiness, or scale authorization is at least a scale blocker
  and may require REVISE/PAUSE instead of closure.
- Sprint close-out chat must state the next step if work simply continues.
  This should name the next sprint/gate/action, or explicitly say that the next
  step is paused pending human decision.
- Rebuild affected paragraph/chapter/book HTML/PDF whenever source markdown or assets change.
- Do not scale companion production until the closed foundation prerequisites
  remain intact, GRAPH-UX-2 and MATH-UX-2 remain closed as graph/math
  task-shell proof, and REASON-UX-2, GAME-ARCH-1,
  GATE-ENGINE-1, L1.7B-Q2, GATE-L1.7B-Q2, REV-STD-1, and Scale Gate 1
  explicitly clear or waive the relevant flags, define the complete
  companion-set contract, shared skill-map architecture, and shared task-type
  shell, and prove that the exit-ticket checkpoint, if included in scaling, is
  either explicitly limited to checkpoint-only status or reviewed as
  target-equivalent proof.
  The primary math practice route must keep using the skill-tree math game
  unless Scale Gate explicitly accepts a different reviewed calculation-engine
  replacement:

```powershell
node scripts\validate-paragraph.js --mode complete "<paragraph-folder>"
```

- Every layout or user-interface improvement must be integrated in the platform, not patched into one generated lesson file.
- Every visual or image-integration improvement must also be integrated in the platform. Do not hand-paste one-off images into generated lesson files.
- Reusable UI work belongs in `C:\Projects\4veco\4veco-platform`: templates, shared CSS/JS, converters, generators, validators, or build scripts.
- Reusable visual work belongs there too: SVG builders, surface-variant renderers, converter support for light/dark web images, and rules for PowerPoint/game/doc variants.
- Generated output in `4veco-lessen` may show the result, but it should not become the source of truth for UI changes.

## PV Consumption Rule: Visual Backbone Alignment

The lesson repository remains a generated student-facing target. Procedure-visual semantics live in the platform/reference layer, starting with the Procedure-Visual Registry under `4veco-platform/references/data/procedure-visual/`.

PV-G4 has HCS lead-review status `PASS WITH CONDITIONS` after L-PV0 through L-PV5. The lesson team prepared two lesson-owned proof records, HCS reviewed them, and L-PV5 reconciled the evidence-freshness condition by regenerating the proof records and platform intake from the current authoritative artifacts. Current platform evidence records `recorded_proof_count: 2/2` in `reports/json/procedure-visual-lesson-regression-proof-intake.json`, with both proofs citing lesson commit `52f9237de9e465e7f75483f6feac4e80241e8631` and `lesson_worktree_dirty_at_generation: false`. The intake generator is closure-aware and reports `pass_with_conditions`.

The L-PV track must keep these boundaries:

- no PV records are promoted into `references/machine`;
- no student-facing PV projection is authorized;
- no adaptive or diagnostic use is authorized;
- no generated lesson output is hand-patched as proof;
- no screenshot-only proof counts for PV-G4.

Proof 002 remains bounded proof diversity only: it validates the A61 table-trace PV template and visual anchors, but it is not a student-facing lesson surface and not evidence that an A61 classroom route is ready.

L1.5G graphical-game work is split into L1.5G-A through L1.5G-E. Any graphical-game semantics must align with the Procedure-Visual Registry where PV records exist; the graphical MVP may not hard-code a separate semantic model for operations, visual states, or procedure sequences that the PV layer already defines. The split track proceeds under the PV-G4 conditions, without PV machine promotion or student-facing PV projection.

L1.6 must use one fresh paragraph build to prove at least one procedure/visual sequence can be generated from or validated against PV data, using the L-PV contract/proof machinery if the PV registry and validator have reached the required gate.

L1.7A scaling-readiness gate must include PV readiness: procedure consistency, visual semantic anchors, surface variants, game mapping, answer-model alignment, proof-record completeness, and generator-block controls.

## Layout Reference

Use this local legacy/rewire file as a reference input for the next companion UI pass:

```text
file:///C:/Projects/4veco/3-Module-3-rewire-test/3.1%20Hoofdstuk%201%20-%20Markten/3.1.1%20Paragraaf%201%20-%20Markt%20en%20marktstructuur/1.%20Voorbereiden/3.1.1%20Markt%20en%20marktstructuur%20%E2%80%93%20uitleg%20voorkennis.html
```

This is not the end state. It is better than the current companion layout and is
useful because it already shows several patterns worth studying:

- sidebar navigation by section
- mobile menu toggle and overlay
- hero section with section cards
- domain badges and domain-colored section headers
- clearer content blocks, formula boxes, callouts, summary tables, and checklist
- more obvious document structure for students

The task is not to copy this file by hand. The task is to turn the useful parts
of this direction into a platform-owned companion layout system.

## Architecture: adaptive-ready from L1.5G onward

The companion's eventual end-state is adaptive paragraphs: after a student takes
a first quiz, an advisor surfaces guidance ("focus here next, skip this, try the
harder variant") and the games adapt to that guidance — difficulty, focus, or
sequencing. That advisor and its evaluation logic are not built in this roadmap.

The L1.5G split builds the seam in place without bundling it into the same gate
as the graphical-game MVP. Concretely:

- L1.5G-B defines the localStorage payload schema and safe read helper.
- The existing five games - quiz, newsdetective, reasoning, skilltree,
  procedure - must behave exactly as they do now when the payload is absent or
  default.
- The later graphical game in L1.5G-C reads the same seam.
- Tomorrow a post-quiz advisor may populate that key; that advisor is not part
  of L1.5G.

Implication for the split: L1.5G-B owns the seam contract, L1.5G-C owns the
new graphical MVP, L1.5G-D owns student routing, and L1.5G-E owns generated
output QA. None of those sub-sprints may claim adaptive behavior.

Out of scope for this roadmap: building the advisor, shipping diagnostics,
mastery routing, sequencing, AI, summative use, or any real adaptive behavior.
Those are a later sprint cycle.

### Adaptive learning replaces three-track differentiation (next-year cycle)

The current three-track differentiation method — basisopgaven /
middenopgaven / verrijkingsopgaven (three pre-authored static handouts at
fixed difficulty) — will be deprecated next school year (2026/27 cohort).
It is replaced by a dynamic, adaptive version of `begeleide inoefening`:
same exercise companion surface, but items, hints, and difficulty are
chosen at runtime against the same adaptive-payload seam that L1.5G-B
builds for the games. One adaptive exercise surface, not three static
handouts.

This is a future sprint cycle, scheduled after L1.7A. It is not built in
this roadmap; the only thing this roadmap carries is the shared seam, so
the dynamic `begeleide inoefening` can wire onto the same localStorage
payload when the advisor lands.

Repo-wide changeover note (for the future adaptive-learning sprint, not
now): when the three-track method is dropped, every reference to it must
be updated in one deliberate pass — the landing-page builder section
"Opgaven" and its `HIDE_TASK_ROWS` flag, paragraph plans
(`_paragraph-plan.md`) that name the three tracks, exercise builders
(`b1-XYZ-opgaven.js` and the per-track DOCX builders), companion-skill
and review-agent rules that assume the three-track scaffold, fixtures
under `engines/tests/` and `references/`, and this roadmap's own mentions
of basis / midden / verrijking. The changeover sprint must include a
deliberate repo-wide audit so the deprecation does not leave half-renamed
references behind.

## Sprint Details

### Sprint L0.5: Green Gate Handoff

Completed: yes.

Purpose:

- accept the platform/book health routine as good enough for controlled material work
- keep Book 1 Part A green
- allow controlled companion pilot work

Evidence:

- `check:book` passes for Book 1.
- `validate-paragraph.js` supports the flat paragraph layout.
- companion output may be produced under the documented platform workflow.

### Sprint L1.1: First Companion Technical Pilot

Completed: yes.

Purpose:

- run one real companion paragraph through the complete Part B workflow
- expose platform, validator, build, layout, and usability gaps before scaling

Current state:

- `1.1.1 Schaarste en economisch denken` has a full companion set.
- The complete technical validator passes.
- A platform-team quality-gate review has been created for validator/source/quality-ref gaps.

Exit criteria:

- one pilot paragraph passes complete-mode validation. Done for `1.1.1`.
- known source/quality-gate gaps are handed to the platform team. Done in the platform quality-gate review.

### Sprint L1.2: Second Companion Technical Probe

Completed: yes.

Purpose:

Prove that the current companion workflow can repeat once content/data inputs exist.

Evidence:

- `1.1.2 Percentages en indexcijfers` has been used as the second technical probe.
- The platform roadmap records it as passing complete-mode validation.
- This proves technical repeatability, not final companion quality.
- The generated 1.1.2 test materials have been cleared and must not be used as lesson content.

Exit criteria:

- two Book 1 companion paragraphs pass complete-mode validation during technical probing. Observed for `1.1.1` and `1.1.2`; 1.1.2 now awaits didactic rebuild.
- repeated setup steps are saved or documented in the platform workflow.
- remaining risks are moved to layout/usability and quality-gate work.

### Sprint L1.3A: Basic HTML Layout And Front-End Usability

Completed: yes.

Closed: 2026-04-25.

Purpose:

Make the basic companion HTML pages easier to read, navigate, and use before
scaling the companion pipeline.

Scope:

- `uitleg voorkennis.html`
- `uitleg vaardigheden.html`
- `begeleide inoefening.html`
- paragraph `index.html`
- game shell pages only where navigation or framing is visibly weak

Current evidence:

- `1.1.1` default `uitleg voorkennis.html` now uses the shared platform layout instead of only the rollback/test filename.
- `1.1.1` `begeleide inoefening.html` now uses the shared platform theme layer.
- `1.1.1` `uitleg vaardigheden.html` remains on the shared theme layer after deploy reskin and now avoids duplicate/oversized legacy back-link SVG behavior.
- Browser smoke passed for `uitleg voorkennis`, `uitleg vaardigheden`, and `begeleide inoefening` at desktop/mobile widths in light and dark mode.
- Technical gates passed after regeneration: deploy link/data checks, complete paragraph validation, and Book 1 `check:book`.

Work:

- Compare current Book 1 companion pages against the improved rewire reference file.
- Improve navigation, mobile behavior, hierarchy, callouts, section scanning, and visual consistency.
- Keep the layout implementation in the platform: shared CSS/JS, converters, templates, and build scripts.
- Rerun the pilot output after platform changes.
- Browser-check the improved pages on desktop and mobile widths in light and dark mode.

Exit criteria:

- The basic `1.1.1` companion HTML pages have improved layout/usability from platform-owned sources.
- The improved layout can be regenerated, not hand-maintained.
- The local reference file has been used as input, but the result is a new Book 1 companion design direction.
- Link/reachability and browser smoke checks pass for the improved companion pages in light and dark mode.
- A human usability review signs off that this layout is good enough to use as the scaling baseline.

### Sprint L1.3B: Companion SVGs And Light/Dark Visual Variants

Completed: yes.

Closed: 2026-04-25.

Purpose:

Replace raw copy-pasted textbook imagery with proper companion SVGs and
surface-specific variants, including explicit light/dark web visuals where
needed.

Current evidence:

- `SURFACES` and `THEMES` are now a single platform-owned module (`4veco-platform/build-scripts/lib/lib-visual-surfaces.js`). Both the figure/worked-example/exercise builder (`b1-111-visual-variants.js`) and the news builder (`b1-111-nieuws.js`) import from it.
- The news visual `1.1.1_news_woningtekort` is now produced through the shared variant system: `doc`, `web_light`, `web_dark` surface variants plus a canonical base file, with the Word document embedding the `_doc` PNG instead of a raw base screenshot.
- `b1-111-visual-variants.js` still regenerates slide, doc, summary, web-light, and web-dark variants for `1.1.1` figures/worked examples/exercises. Byte-diff after the shared-lib refactor was empty.
- `1.1.1` `uitleg voorkennis.html`, `uitleg vaardigheden.html`, and `begeleide inoefening.html` use light/dark image swapping where themed visuals exist.
- Browser smoke confirmed the correct light/dark image sources on desktop and mobile (pre-refactor; re-check after the news variant regeneration is still needed).
- `validate-paragraph.js --mode complete` now enforces `_web_light`/`_web_dark` symmetry: any variant declared without its counterpart (in `_paragraph-plan.md`) fails the gate. 6 pair(s) pass for 1.1.1 today. Platform unit tests green; a temp fixture confirmed the new FAIL path fires.
- The game/interactive visuals decision for 1.1.1 is recorded in `1.1.1/_paragraph-plan.md` §"Game visuals decision (L1.3B)": no concept-visual slot for this paragraph; revisit per-paragraph.

Work:

- Treat Part A textbook images as source material, not finished companion artwork.
- Replace literal book-image copy-pasting with adapted SVGs or regenerated visuals that fit each companion surface.
- Define visual variants per surface where needed: slide, docx, summary thumbnail, web-light, web-dark, and game/interactive variants.
- Make web visuals adaptable to light and dark mode. Any graphic with text, axes, fills, backgrounds, or low-contrast colors needs explicit light and dark variants.
- Make sure visual changes are implemented in the platform through SVG builders, surface-variant renderers, converter support, templates, and validators where needed.
- Decide whether game/interactive pages need explicit concept-visual slots or whether their current generated UI is sufficient for this paragraph.

Exit criteria:

- `1.1.1` companion images are adapted to their surfaces rather than copy-pasted from textbook material.
- Web pages use the correct light/dark image variants where graphics need theme-specific treatment.
- Word documents, summaries, and interactive/game surfaces use visuals sized and composed for their actual use.
- The improved visual variants can be regenerated from platform-owned builders, not hand-maintained.
- `validate-paragraph.js --mode complete` still passes after visual regeneration.

### Sprint L1.3C: PowerPoint Presentation Improvement

Completed: yes.

Closed: 2026-04-25.

Purpose:

Improve the companion PowerPoint so it is a classroom-ready presentation, not a
deck with pasted book images.

Current evidence:

- The `1.1.1` presentation builder regenerated the PPTX using adapted slide visuals.
- The generated PPTX round-tripped through LibreOffice successfully.
- Complete paragraph validation still passes after regeneration.

Work:

- Make PowerPoint visuals fit the presentation layout: readable from the back of class, aligned with slide typography, and not just pasted as book screenshots.
- Use slide-specific visual variants with clear composition, contrast, scale, and annotation treatment.
- Keep PowerPoint improvements in the platform presentation builder and reusable visual-variant workflow.
- Review the slide narrative, teacher flow, visual hierarchy, and classroom readability.

Exit criteria:

- The `1.1.1` PPTX uses visuals sized and composed for presentation use.
- The presentation can be regenerated from platform-owned sources.
- The deck opens/round-trips without repair.
- A presentation-quality review signs off before the deck pattern is reused across more paragraphs.

### Sprint L1.5A: Easy Layout Round 2

Completed: yes.

Closed: 2026-05-01.

Active 2026-04-30 → 2026-05-01 (pulled forward of L1.4 to ship single-
paragraph-safe layout fixes while the platform team was at a stable point —
`c21ee14` closed the unit-register gap with
`fix(skilltree): hide generator-blocked catalog units`).

Purpose:

Ship the low-risk subset of the rolled-back round-2 layout candidates from the
2026-04-29 attempt — the items that can be validated against `1.1.1` alone, do
not touch generators in ways that need a fresh-paragraph regression, and
include the one observable Pages regression introduced by round-1.

Pre-flight done:

- Platform baseline gate suite green on `c21ee14` (jest 364 pass, deploy.js
  link+data tests pass, check:book 26/26, validate-paragraph 1.1.1 complete
  pass) on 2026-04-30.
- Layout worktree staged at `C:/Projects/4veco/4veco-platform-layout` on branch
  `layout/1.1.1-round-2-redo` from `c21ee14`.

Shipped scope (per L1.5A planner sub-agent classification):

- Item #0 — book-index back-link guard. Platform commit
  `5b8c216 fix(voorkennis): skip back-link injection on book-root landing`.
  Adds a 3-line guard in `engines/voorkennis.js#injectBackLink` skipping
  injection when `document.body.dataset.layout === 'landing-book-v1'`. Fixes
  the `Overzicht` link 404 introduced by round-1 commit `3db70d8`.
- Item #2 — Begeleide-Inoefening static back-link via converter. Platform
  commit `b9c5085 feat(bi-converter): emit static back-link in shared-CSS
  hero`. Adds the standard `<a class="back-link" href="../index.html">` to
  the BI hero in `convert_begeleide_inoefening.py`'s shared_prefix branch,
  mirroring the voorkennis pattern. Removes the brief flash of un-back-
  linked hero before JS runs.

Deferred to L1.5B (per L1.5A planner sub-agent reclassification):

- Item #1 — per-section accent on chapter/book index cards. Planner found
  that `.section-card` does not exist in the platform (cards are
  `.chapter-card` ~line 499 and `.para-card` ~line 542 in
  `build-landing-page.js`); they currently carry an inline 5-color palette
  accent, not the editorial 3-token system; editorial accent CSS rules
  require a `data-domain` attribute or matching class hook the cards do not
  carry. Implementation requires editing the generator (`build-landing-
  page.js` renderBookPage / renderChapterPage emission sites) — out of
  L1.5A scope, in L1.5B scope.

Out of scope, explicitly:

- Item #3 from rolled-back round-2 (split "Valkuilen en misvattingen" into
  per-card pitfalls) — touches `build-landing-page.js` generator structure,
  needs L1.4's fresh-paragraph regression to be safe. Deferred to L1.5B.
- DOCX/PPTX-as-web work — separate sprint L1.5D.
- New game work - split into L1.5G-A through L1.5G-E.

Closing evidence:

- Platform PR https://github.com/meijer1973/4veco-platform/pull/2 opened from
  `layout/1.1.1-round-2-redo` to platform `main`. **Open at close**, awaiting
  merge.
- Lessen `2a8455b L1.5A: ship book-root back-link guard + BI static back-link`
  pushed to `origin/main`.
- Verification sub-agent on 2026-05-01 reported "L1.5A SHIPPED CLEAN":
  - Static HTML book root and chapter index emit the correct `data-layout`
    markers (`landing-book-v1` / `landing-chapter-v1`).
  - Deployed `shared/voorkennis.js` line 66 contains the
    `dataset.layout === 'landing-book-v1'` guard.
  - BI page has `<a class="back-link" href="../index.html">` with
    `Terug naar overzicht`, ordered before the `hero-badge` (correct DOM
    insertion).
  - Pages root URL returns HTTP 200 and lists Boek 1.
  - Baseline gates on the layout worktree: jest 364 pass / 6 skipped / 0
    failed; deploy.js link + 99 data tests pass; `npm run check:book` 26/26;
    `validate-paragraph.js --mode complete` for `1.1.1` PASSED.

Exit criteria (all met):

- selected items shipped via PR to platform `main`; lessen-side regenerated
  and pushed ✓ (PR open, lessen pushed)
- `validate-paragraph.js --mode complete` for `1.1.1` still passes ✓
- deploy.js + check:book + jest match the 2026-04-30 baseline ✓
- Pages browser-smoke confirms each item's expected change is live ✓
- the book-index `Overzicht` 404 link is gone ✓ (deployed `voorkennis.js`
  carries the guard; runtime no longer injects on the book root)

Open follow-ups:

- Merge platform PR #2 to durably land the fix on platform `main`. Until
  then, anyone running `deploy.js` from platform `main` regenerates without
  the guard. Lessen-side artifacts on Pages are unaffected — they already
  reflect the fix.
- After PR merge, update memory `project_open-regressions.md` to mark the
  back-link 404 regression resolved.

### Sprint L1.5D: Authored Content As Web

Completed: 2026-05-14.

Position: after L1.5A, before L1.4. Two-phase, single sprint.

Purpose:

Render authored Word and PowerPoint content natively on the paragraph pages so
students can read it in the same surface as the rest of the companion (light
and dark, mobile and desktop, sidebar navigation). Keep the original Office
files downloadable for users who want them. Move toward video-like classroom
material by surfacing PowerPoint speaker notes and (stretch) reading them
aloud.

Phase D1 — DOCX as web:

Some prior work exists; this phase consolidates and ships it.

- Render Word document content as web HTML on the paragraph page surface,
  using the platform-owned converter pipeline (extend
  `convert_voorkennis.py` / `convert_vaardigheden.py` / a new docx-content
  converter as appropriate).
- Light/dark theme variants throughout, matching the editorial CSS direction
  established in L1.3A.
- Keep the original `.docx` available as a download from the paragraph page.
- Link/reachability and complete-mode validation pass on `1.1.1` after
  regeneration.

Phase D2 — PPTX as web:

- Render slide content as web HTML on the paragraph page (slide-by-slide,
  navigable, light/dark-aware).
- Speaker notes shown below each slide on the web surface.
- Keep the original `.pptx` available as a download from the paragraph page.
- Stretch goal: text-to-speech readout of speaker notes via the Web Speech
  API, gated behind a "play" control. Pushes the surface toward
  video-like content. May not work on every browser; ship as
  progressive-enhancement, not core.

Exit criteria:

- DOCX content for `1.1.1` renders as web on the paragraph page with download
  link; passes the same gates the prior HTML conversions pass.
- PPTX content for `1.1.1` renders as web on the paragraph page with speaker
  notes and download link; passes gates.
- Where a paragraph uses a PV-backed visual state, web-rendered authored
  content preserves the same semantic visual anchor across docx/html/pptx
  surfaces. This is an acceptance criterion only; L1.5D does not build the PV
  schema.
- Both phases land in platform-owned converters / builders / templates, not
  hand-edited into generated output.
- `validate-paragraph.js --mode complete` for `1.1.1` continues to pass.

### Sprint L1.5D-B02: 1.1.1 Cross-Surface Parity + Bookkeeping Fix

Completed: yes, 2026-05-12.

Purpose:

- close the second review finding that Part A and Part B disagreed on the
  economisch-denken procedure;
- keep `B02` as an internal repository skill code, but remove it from
  student-facing copy;
- stabilize the web PowerPoint conversion enough that local prototype decks do
  not contaminate generated official output;
- document the follow-up before paragraph 1.1.2 starts.

Delivered:

- Part A paragraaf/opgaven/antwoorden now use the same four-step
  economisch-denken procedure as the companion surfaces, including
  nettowaarde.
- Student-facing HTML/SVG/JS/markdown for 1.1.1 no longer exposes `B02`; review
  and plan files may still use the code internally.
- The presentation builder adds semantic navigation metadata and student-facing
  labels; the web converter renders option comparisons as grouped cards and
  uses sprekersnotities terminology.
- `convert_presentatie.py` selects the exact official `presentatie.pptx` when
  present, instead of accidentally converting local prototype decks.
- The link checker ignores intentionally unlinked `*-prototype.html` baselines.
- Review/bookkeeping artifacts were added or refreshed:
  `archive/sprints/L1.5D-B02/L1.5D-b02-cross-surface-parity-plan.md`, `1.1.1-review.md`, and the
  L1.5D review/handoff logs.

Evidence:

- `npm run check:platform` passed.
- `validate-paragraph.js --mode complete --profile student-web` passed for
  1.1.1.
- `validate-paragraph.js --mode complete --profile publisher-print` passed for
  1.1.1.
- `npm run check:book` passed for Boek 1.
- `check-sprint-plan.js` passed for the L1.5D-B02 plan.
- A student-facing `B02` sweep over generated HTML/SVG/JS and Part A markdown
  returned clean.
- Platform source commit: `52a0d77` (`Fix 1.1.1 parity and presentation web
  conversion`).

### Sprint L1.5O: Output Profile Simplification

Completed: yes, 2026-05-12.

Purpose:

- make paragraph 1.1.2 cheaper and lighter to build by stopping DOCX files from being default outputs;
- keep the three textbook PDFs for a deliberate publisher/print pipeline;
- keep old 1.1.1 / legacy-full validation available for regression checks.

Delivered:

- `validate-paragraph.js` supports `student-web`, `legacy-full`, `office`, and `publisher-print` profiles.
- `student-web` is the direct validator default and requires the 14 web-first Part B files, not the old 27-file DOCX contract.
- `office` / `legacy-full` explicitly require DOCX exports.
- `publisher-print` explicitly requires `paragraaf.pdf`, `opgaven.pdf`, `antwoorden.pdf`, and `build_pdf.py`.
- `check-book.js` keeps Part A book health on `publisher-print` by default.
- Paragraph landing pages no longer offer Word downloads on web-backed tiles
  and no longer show the legacy basis/midden/verrijking Word exercise row.
- Paragraph landing-page tiles no longer show developer-facing `html` format
  badges; remaining small action chips are student-facing choices.
- `BUILD-PARAGRAPH.md`, `build-scripts/README.md`, and this roadmap record the split.

Evidence:

- Focused Jest: 21/21 tests passed.
- `1.1.1` passed `--mode complete --profile student-web`.
- `1.1.1` passed `--mode complete --profile legacy-full`.
- `1.1.1` passed `--mode part-a --profile publisher-print`.
- Landing-page regression: `scripts/tests/build-landing-page.test.js` passed;
  platform commit `548270c`.
- Landing tile language cleanup: `scripts/tests/build-landing-page.test.js`
  passed; platform commit `6de425f`.

Operational rule for L1.4:

- Build `1.1.2 Percentages en indexcijfers` with `--mode complete --profile student-web`.
- Do not generate Office exports unless the requested product explicitly needs them.
- Treat textbook PDFs as publisher-print outputs, not routine student-web artifacts.

### Sprint L1.5V: Companion Quality Polish for 1.1.1

Completed: 2026-05-09.

Active 2026-05-09. Expanded scope after the `econ-companion-visual-review`
agent ran on `uitleg voorkennis` (review file
`1.1.1 Schaarste en economisch denken/1.1.1-companion-visual-review.md`)
and returned **FAIL** with four hard-fail defects plus a DOCX QA failure.
The voorkennis defects are largely **shared platform issues** (visual
frame, converter list rendering, checklist routing, alt-text emission)
that also constrain `uitleg vaardigheden`. Fixing them once unblocks
both surfaces. The original vaardigheden-only scope from the Team B
reference draft is retained as a sub-bucket of the expanded sprint.

Purpose:

Bring **both** companion explainer surfaces for §1.1.1 to a verdict of
PASS or PASS WITH FLAGS under `agents/econ-companion-visual-review.md`:

- `1.1.1 Schaarste en economisch denken – uitleg voorkennis.html` (and
  matching `.docx`).
- `1.1.1 Schaarste en economisch denken – uitleg vaardigheden.html`.

For vaardigheden, integrate the strongest didactic improvements from a
Team B reference draft (`uitleg vaardigheden team b.html`) into Team
A's platform-consistent two-section structure (B01 schaarste
herkennen, B02 alternatieve kosten berekenen). Team A stays the
implementation baseline because it is closer to the platform structure
(canonical skill sections, generated companion layout, themed web
visual hooks); Team B is treated as a quality-improvement source, not
a competing production baseline.

Authoring spec + review gate:

- **Skill** (authoring + regeneration): `skills/econ-companion-artifacts.md`
  on the platform side. New as of 2026-05-09. It encodes the
  platform-wide rules for student-facing companion artifacts and is
  required reading before edits.
- **Review agent** (closure gate): `agents/econ-companion-visual-review.md`.
  Already used to produce the §1.1.1 voorkennis review that triggered
  the scope expansion. The skill's "Review before delivery" checklist
  is identical in shape to the agent's pass sequence so they cannot
  drift.

Canonical procedure decision (recorded 2026-05-09):

The canonical procedure for B02 is **4-step**, not the 3-step verbal
expansion that the current `_paragraph-plan.md` declares. The 4 steps:

1. Benoem alle beschikbare alternatieven voor het schaarse middel.
2. Bereken voor elk alternatief de opbrengst of verwachte opbrengst.
3. Rangschik de alternatieven; het hoogste niet-gekozen alternatief
   is de alternatieve kosten.
4. Vergelijk de opbrengst van de gekozen optie met de alternatieve
   kosten om de nettowaarde te beoordelen.

This decision propagates beyond vaardigheden: the `_paragraph-plan.md`
Concept 3 description, the `1.1.1_fig_3` flowchart visual, the
samenvatting cell 5, the presentatie slide 5, the stappenplan game,
the begeleide-inoefening scaffold, and the opgaven references all
need updating to the 4-step form. L1.5V owns the registry change and
the vaardigheden-side propagation; the other surfaces regenerate
mechanically once the registry is right.

Required changes — grouped by bucket. Bucket A (shared platform fixes)
ships first because both voorkennis and vaardigheden surfaces depend
on it; Bucket B (canonical procedure) is a hard prerequisite for all
B02-using surfaces; Buckets C and D are surface-specific.

#### Bucket A — Shared platform fixes (ship FIRST)

These are upstream defects from the §1.1.1 voorkennis review that also
affect the vaardigheden surface or any future paragraph's companions.
Fixing them once unblocks both surfaces and reduces L1.4 risk.

**A1. Strip production label `COMPANION VISUAL` from shared visual
frame.**
- Source: `build-scripts/lib/lib-visual-surfaces.js:131` emits the
  label in the shared visual frame for non-slide variants.
- Fix: remove or guard the label so student-facing doc / web_light /
  web_dark / summary surfaces never carry it. (Slide internal use, if
  any, may stay during build, but no rendered student surface should
  show it.)
- Regenerate: rerun `b1-111-visual-variants.js`, then DOCX/HTML/PPTX
  for §1.1.1 so the label disappears from every existing variant.
- Acceptance: no asset under `_assets/` for §1.1.1 contains the text
  `COMPANION VISUAL`; review agent's hard-fail on production labels
  cannot trigger.

**A2. `convert_voorkennis.py` renders normal-section list items.**
- Source: `build-scripts/lib/convert_voorkennis.py:548-588` only
  renders paragraphs / formulas / assets / callouts / summaries; there
  is no branch for normal-section `list_item`. As a result the HTML
  drops worked-example steps (`b1-111-voorkennis.js:430-434`) and
  bar-chart reading bullets (`:456-459`) that exist in the DOCX.
- Fix: teach the converter to emit `<ul>/<li>` (or `<ol>/<li>`
  where source signals ordered) for normal-section list items, with
  an associated CSS hook so `voorkennis.css` styles them.
- Acceptance: regenerated voorkennis.html contains the worked-example
  steps and the x-axis / y-axis / scale bullets that exist in the
  DOCX; review agent's source-output-parity hard-fail cannot trigger.

**A3. Voorkennis checklist emits next-step routing.**
- Source: `convert_voorkennis.py:602-617` generates the checklist
  HTML without a route block, and `b1-111-voorkennis.js` does not
  author one.
- Fix: add a generated next-action block after the checklist —
  "alles afgevinkt → ga verder naar Uitleg vaardigheden / Presentatie";
  "nog niet → herhaal sectie X / doe Instapquiz". Use the route table
  in `skills/econ-companion-artifacts.md` as the canonical mapping.
- Acceptance: regenerated voorkennis.html ends with a visible,
  keyboard-accessible next-action block; review agent's affordance
  hard-fail cannot trigger.

**A4. Meaningful alt-text infrastructure for visuals.**
- Source: HTML emits `alt="1.1.1_ex_1"` (filename-like) and DOCX
  emits `descr="asset:1.1.1_ex_1"` (asset-id-like).
- Fix: introduce an alt-text map keyed by concept-base in the
  paragraph plan (`_paragraph-plan.md` visual-variants section, or a
  dedicated alt-text registry), thread it through `b1-111-voorkennis.js`,
  `b1-111-vaardigheden.js`, the other §1.1.1 builders, and the matching
  converters so both DOCX `docPr` and HTML `alt` receive a human-
  readable description (e.g. *"Staafdiagram met opbrengst per gewas:
  tarwe €500 per hectare, maïs €350, zonnebloemen €300."*). Builders
  must fall back to a clear placeholder if alt text is missing for a
  concept-base, so omissions surface in review.
- Acceptance: no rendered `alt` or `descr` is filename-like or
  asset-id-like for any visual on the two §1.1.1 explainer surfaces.

**A5. Fix duplicate `Heading1` style ID so DOCX artifact-tool render
works.**
- Source: `b1-111-voorkennis.js:350` defines a custom style id
  `Heading1` colliding with the built-in. `render_docx.py --renderer
  artifact-tool` errors with `Argument_AddingDuplicateWithKey,
  Heading1`.
- Fix: rename the custom style or align with the built-in Word style;
  rerun artifact-tool to confirm page PNG render. If the same pattern
  exists for `b1-111-vaardigheden.js`, fix in parallel.
- Acceptance: `render_docx.py --renderer artifact-tool` succeeds on
  both regenerated DOCX files and produces page PNGs.

#### Bucket B — Canonical procedure 3 → 4 step propagation

Hard prerequisite for every Bucket C item and for any other §1.1.1
surface that displays B02. This is unchanged from the previous L1.5V
plan; reproduced here so the sprint stays self-contained.

**B1. Registry / source-of-truth update.**
- `4veco-lessen/Boek 1 .../1.1.1 .../_paragraph-plan.md` Concept 3
  row: rewrite the procedure description from the 3-step verbal form
  to the 4-step canonical form. Update the visual-anchor row for
  `1.1.1_fig_3` to reference the 4-step flowchart.

**B2. Visual generator.**
- `build-scripts/content/book-1/b1-111-visual-variants.js`: replace
  the 3-step `fig_3` flowchart with a 4-step variant (slide / doc /
  summary / web_light / web_dark surfaces all regenerate from the
  same source). Step terminology must match the registry verbatim.
  Surface-adapted variants required.

**B3. Content surfaces that reference B02's procedure.**
- `b1-111-vaardigheden.js` skill 2 procedure block — 4 steps.
- `b1-111-samenvatting.js` cell 5 ("Economisch denken — 3 stappen") —
  rename header, content, and visual reference to match the 4 steps.
- `b1-111-presentatie.js` slide 5 (Concept: Economisch denken) — same.
- `b1-111-inoefening.js` BI scaffold — propagate the 4-step form.
- Opgaven (`b1-111-opgaven.js` and basis / midden / verrijking question
  docx generators) — every "3-stappen procedure" / "Welke
  alternatieven? → opbrengsten? → wat geef je op?" reference becomes
  the 4-step form.
- Game data: `source-data/book-1/reasoning/1.1.1.csv` already uses
  "alternatieve kosten" canonical vocabulary; re-check no row still
  models the 3-step procedure as canonical. Stappenplan game data, if
  any, mirrors.

**B4. Regenerate-and-verify.**
- Per-paragraph builders (visual-variants, vaardigheden, samenvatting,
  presentatie, inoefening, opgaven).
- `node scripts/deploy.js` — all 5 docx-to-web converters re-emit
  HTML with the 4-step procedure present.
- `npx jest`, `npm run check:book`, `node scripts/validate-paragraph.js
  --mode complete` — all green.
- Manual diff: every rendered surface (samenvatting.html,
  vaardigheden.html, presentatie.pptx slide 5, BI HTML, basis / midden
  / verrijking opgaven) shows step 4 ("Vergelijk opbrengst met
  alternatieve kosten om de nettowaarde te beoordelen") and none
  shows the legacy 3-step header or footer.
- The fig_3 visual on every surface (slide / doc / summary / web_light
  / web_dark) shows 4 steps with the canonical wording.

Do NOT silently bridge two competing procedures. Do NOT regenerate
piecewise: if any surface lags behind, the registry is in an
inconsistent state and the next deploy could re-introduce the 3-step
form.

#### Bucket C — Vaardigheden-specific (after Buckets A + B)

**C1. Visual-text synchronization.** Lisa with €20 / bioscoop €12 /
boek €15 — the visual must use the same numbers as the adjacent text,
or the text must explicitly explain a broader-variant visual.

**C2. Worked-example text-completeness.** Add the tarwe/maïs
arithmetic as an explicit table in the verbal channel (not only in
the visual): opbrengst tarwe (10 × €500 = €5.000), opbrengst maïs
(10 × €350 = €3.500), beste niet-gekozen alternatief (maïs = €3.500),
alternatieve kosten (€3.500), nettowaarde (€5.000 − €3.500 = €1.500).

**C3. Schaarste checks visible as structured HTML.** The "Schaarste
herkennen" section must render the three checks as `<ol><li>` (or a
styled step block), not as loose text inside a callout.

**C4. Import Team B scaffold under B01/B02.** Keep two canonical
sections; nest as subblocks: keuzekaart pre-organizer under B02 step 1;
"prijs en kosten uit elkaar houden" misconception/pitfall block under
B02; explicit tarwe/maïs calculation table as the worked example;
granular checklist + route advice as the final block. Do NOT expand
into 5+ parallel skill sections.

**C5. "Wat nu?" routing block.** Final checklist routes the student
to the next appropriate artifact based on what they couldn't do yet
(Voorkennis / Stappenplan / Begeleide inoefening / Basisopgaven /
Middenopgaven / Verrijking). Use the route table in
`skills/econ-companion-artifacts.md`.

**C6. Visual quality.** Beyond A1 (production label), apply the
spelling/contrast/variant checks: `maïs` not `Mais`, `alternatieve
kosten` not English/informal, readable contrast in light/dark,
surface-adapted web visuals with light/dark variants (no direct
base-SVG embedding), arrows visibly meaningful.

#### Bucket D — Voorkennis-specific (after Buckets A)

**D1. Convert the schaarste/budget illustration to a meaningful
caption + alt text per A4.** Aligns the chart inspection prompts with
the visible chart values (Tarwe €500, Mais €350, Zonnebloemen €300)
and adds a one-line caption that mirrors the alt text.

**D2. Confirm worked-example steps survive regeneration.** Once A2 is
in, re-render and verify the three worked-example steps and the
x/y-axis/scale bullets are present. This is a parity check, not a new
authoring step.

**D3. Confirm checklist routing block is wired into the rendered
page** per A3. Spot-check link targets resolve under GitHub Pages.

#### Bucket E — Part A quality-control integration (was deferred, now in scope)

The voorkennis review's quality-log explicitly flagged that
`X.Y.Z-quality-ref.yaml` records Part A asset state only, and the
existing `validate-paragraph.js` passes despite Part B/companion hard
fails. The team direction (2026-05-09) is to **fold this into L1.5V**
rather than defer, because L1.5V is also the moment Part B is being
formalised by the new skill + review agent — the right time to ensure
Part A and Part B both have first-class records.

**E1. Extend the §1.1.1 quality records.**
- Audit the current `1.1.1-quality-ref.yaml`. Confirm exact scope of
  what it records (Part A asset state per the review).
- Decide schema shape with the F-planning sub-agent (one record file
  with explicit Part A and Part B sections, two record files, or a
  third companion-specific record file). Default: extend the existing
  YAML with a `companion:` section that mirrors the Part A fields.
- Wire `agents/econ-companion-visual-review.md` to write/update the
  Part B section of the chosen record on every run, in addition to its
  human-readable `1.1.1-companion-visual-review.md` report.

**E2. Decide whether `validate-paragraph.js` should fail on
companion-review hard fails.**
- Current behavior: validator is independent of the visual review;
  validator-pass does not imply review-pass.
- Options to evaluate in the F-plan: (a) keep them independent and
  document that closure requires both green; (b) have validator read
  the companion-review record file and refuse close if its verdict is
  FAIL; (c) keep independent but have a wrapper script (`scripts/
  qc-paragraph.js` or similar) that runs both and aggregates.
- This is a Bucket-F-shaped decision and is mostly handled there;
  E2 records the dependency and lists §1.1.1 as the proving paragraph.

**E3. Re-record §1.1.1 closure under the chosen schema.**
- Once E1 + the relevant Bucket F decisions are made, populate the
  Part A record (carry-forward from existing) and the Part B record
  (from the post-Bucket-A-D regen + final review-agent verdict).
  §1.1.1 then serves as the canonical example for paragraph 2 (L1.4)
  to follow.

#### Bucket F — Part A / Part B quality-cycle separation (pilot lock-in before L1.4)

**Why this is in L1.5V.** §1.1.1 is the pilot paragraph: every skill,
test, agent, and quality record we touch here becomes the template
that paragraph 2 (L1.4 = §1.1.2) builds against. The current build
documentation, validator, and quality records mix Part A (textbook
markdown + assets) and Part B (companion HTML/DOCX/PPTX/games + index)
together, which is confusing now that Part B has its own authoring
spec (`skills/econ-companion-artifacts.md`) and review agent
(`agents/econ-companion-visual-review.md`). L1.4 should not start
under that ambiguity. **L1.4 is gated on Bucket F closing.**

**F-plan (sub-agent).** Audit + propose-design pass. The F-planning
sub-agent surveys the current state and produces a written design
proposal for user review before any F-execute work begins.

Audit inputs:
- `BUILD-PARAGRAPH.md` — read in full; tag every paragraph as Part A,
  Part B, or A+B; identify mixed-scope sections (Phase 6 / 6a, the
  A-verify / B-verify checklists, the validate-paragraph mode flags).
- `BUILD-CHAPTER.md` — same audit at chapter scope.
- `scripts/validate-paragraph.js` — list current modes (`complete`,
  `part-a`, `part-b`?) and their actual gate coverage; check if mode
  semantics match the BUILD-PARAGRAPH documented split.
- Skills: `econ-textbook-paragraph` (Part A producer),
  `econ-companion-artifacts` (Part B umbrella), `econ-explainer-docs`,
  `econ-exercise-builder`, `econ-pptx-templates`, `econ-word-templates`,
  `econ-paragraph-review`, `econ-quality-control`, `econ-pdf-builder`,
  `qc-references`, `manage-references`. For each: does it own Part A,
  Part B, or both? Where does ownership leak across the line?
- Agents: `agents/econ-companion-visual-review.md` is Part B only.
  Confirm there is no equivalent Part A reviewer agent or that the
  Part A path is covered by a skill instead.
- Quality records in the lessen tree: `X.Y.Z-quality-ref.yaml`,
  `X.Y.Z-review.md`, `X.Y.Z-companion-visual-review.md`. Map each to
  its scope and consumer.
- File layout under a paragraph folder. Are Part A files (markdown,
  PDF, `_assets/`) and Part B files (`*.html`, `*.docx`, `*.pptx`,
  `index.html`, game shells) cleanly distinguishable by name and
  prefix? Decide if the layout itself benefits from a sub-folder
  split or if naming is sufficient. **Default: do not move files;
  prefer in-place scope clarification, because the lessen tree is
  generated output and physical reorganization would propagate to the
  build pipeline, the GitHub Pages URLs, and student bookmarks.**

Audit outputs (the F-plan delivers these for user review BEFORE any
F-execute work begins):
- Mixed-scope section list with proposed split.
- Proposed final shape of `BUILD-PARAGRAPH.md`: either (a) one file
  with three top-level sections (Common pre-conditions, Part A, Part B)
  or (b) split into `BUILD-PARAGRAPH-A.md` + `BUILD-PARAGRAPH-B.md`
  with a small `BUILD-PARAGRAPH.md` index. Recommend one with
  rationale.
- Proposed validator behavior: confirm `--mode part-a`, `--mode part-b`,
  `--mode complete` are present; document each mode's coverage; close
  any gap where `complete` should aggregate part-a and part-b.
- Proposed quality-record schema (resolves Bucket E1).
- Proposed skill ownership table: skill → which Part(s) it owns →
  which gate runs against its output.
- Proposed test taxonomy: which jest test suites belong to Part A,
  Part B, or shared infrastructure; whether suite naming/folder
  reflects that.
- A migration plan that touches §1.1.1 only (paragraph 2 in L1.4
  inherits the cleaned pipeline; older paragraphs are out of scope).

**F-execute (main agent + per-item sub-agents as needed).** Implement
the F-plan after user approval. One commit per coherent change. Never
move generated lesson output (per Default above) unless F-plan
explicitly requests it and the user approves.

Likely items (final list comes from F-plan):
- F1. Restructure `BUILD-PARAGRAPH.md` per the chosen shape.
- F2. Adjust `validate-paragraph.js` if a mode is missing or wrongly
  scoped; document each mode's coverage in BUILD-PARAGRAPH.
- F3. Implement the chosen quality-record schema; migrate §1.1.1's
  records.
- F4. Update skill files where Part A/Part B ownership is unclear
  (mostly: front-matter description, "When to use," "How this skill
  connects to the rest of the platform" sections).
- F5. Adjust agents/README.md and the `econ-companion-artifacts`
  skill cross-references if the F-plan changes them.
- F6. Update CLAUDE.md (project-level) and AGENTS.md "Quality control"
  sections to reflect the cleaner pipeline.

**F-verify (sub-agent).**
- Re-run end-to-end on §1.1.1 with the cleaned pipeline. Each gate
  runs separately for Part A and Part B; both must pass; the
  aggregate must pass.
- Confirm the §1.1.1 voorkennis review file (post-Bucket-A-D regen)
  is recorded in the new quality record schema.
- Confirm the gates would catch each of the original voorkennis
  review hard fails if reintroduced (regression test, conceptually:
  insert each defect, run validator + review agent, expect FAIL,
  revert).

**Closure of Bucket F is the gate to L1.4.** Roadmap row for L1.4
updated accordingly.

#### Cross-bucket workflow per item

Every item in every bucket follows the same loop, mandated by
`skills/econ-companion-artifacts.md` and gated by
`agents/econ-companion-visual-review.md`:

1. **Read** `skills/econ-companion-artifacts.md`, the matching builder
   skill (e.g. `econ-explainer-docs`), the paragraph plan, the
   canonical unit registry, the existing artifact, and the affected
   builder/converter/asset.
2. **Author / regenerate.** Edit source layer only. Never hand-edit
   `4veco-lessen/`.
3. **Verify rendered output** in browser (HTML) or by inspecting the
   DOCX/PNG export. Confirm source-output parity (bullets / tables /
   calculations / steps / labels / alt text / route block survived).
4. **Run gates.** `npx jest`, `node scripts/deploy.js`, `npm run
   check:book`, `node scripts/validate-paragraph.js --mode complete`.
5. **Run the review agent** on the regenerated surface. Hard fails
   from the agent are the same as the skill's "Do not return PASS if"
   list. Iterate until verdict is PASS or PASS WITH FLAGS for both
   surfaces.

Out of scope (deferred or not L1.5V's territory):

- The "Economisch oordeel geven" Team B section. Not a named
  answer-writing scaffold in the canonical registry; do not import as
  a fifth procedure.
- Re-rendering of all paragraphs. L1.5V scopes to §1.1.1 only.
- L1.5D D2 (PPTX-as-web). Resumes after L1.5V closes.
- File-layout reorganization of the lessen tree (Part A vs Part B
  sub-folders, URL changes). Default in F-plan is to keep the layout
  and clarify scope by naming + documentation only. Physical moves
  are a separate decision the user owns; do not let F drift into one.
- Migration of older paragraphs to the cleaned pipeline (Bucket F is
  scoped to §1.1.1 as the pilot). L1.4 uses the cleaned pipeline by
  default for paragraph 2; older paragraphs catch up opportunistically
  in later sprints.

Pre-flight (must hold before any code change):

- ✅ **Platform PR #3 merged** to platform `main` (2026-05-09). The
  converter ERROR-vs-OK contract fix (`eda176d` upstream / `5dcaf2a`
  on main) is in. The docx-as-web infrastructure L1.5V regenerations
  depend on is therefore present.
- Baseline gates green on platform `main` head: `npx jest`,
  `node scripts/deploy.js "../4veco-lessen/Boek 1 ..."`,
  `npm run check:book`, `node scripts/validate-paragraph.js --mode
  complete "..."`. Re-run before branching per
  `feedback_baseline-gate-check.md`.
- `feedback_conditional-authorization-expires.md` applies: re-verify
  platform team activity state at branch creation; do not assume idle
  from prior session.
- Stale worktrees pruned: `4veco-platform-d1d2` (was `webdocs/1.5d`,
  now merged) and `4veco-platform-layout` (was `layout/1.1.1-round-2-redo`,
  L1.5A merged) can be removed before creating the new worktree.

Sub-agent-driven workflow (per `feedback_sprint-task-workflow.md`):

1. **Whole-sprint planning sub-agent.** Survey: current source for both
   `b1-111-voorkennis.js` and `b1-111-vaardigheden.js`; matching
   converters; `_paragraph-plan.md` procedure + visual-variants
   blocks; shared `lib-visual-surfaces.js`; canonical units B01 + B02;
   Team B's `uitleg vaardigheden team b.html`; the §1.1.1 voorkennis
   review file. Produce a per-item execution plan with file paths,
   before/after sketches, gates, browser-smoke targets, structured by
   the four buckets above. Confirm the dependency order
   (Bucket A1+A4 → A2+A3 → A5 → B → C → D) and flag any item that
   should subdivide.
2. **Per-item planning sub-agent** for non-obvious items: A2 (list-
   rendering converter design), A4 (alt-text registry shape), B2
   (4-step `fig_3` visual replacement), C4 (Team B scaffold imports).
3. Main agent executes, one commit per item (or per coherent
   sub-bucket where items co-edit the same file), on a fresh branch
   `content/1.1.1-companion-quality` off platform main, in worktree
   `4veco-platform-companion`.
4. **Verification sub-agent** runs gates + Pages browser-smoke;
   compares rendered HTML against the acceptance criteria; **runs
   `agents/econ-companion-visual-review.md` on both surfaces** and
   attaches its verdict + report to the verification output.
5. PR to platform main; lessen regen + commit + push; live Pages
   browser-smoke after deploy.

Acceptance criteria (per `skills/econ-companion-artifacts.md` review
gate):

For both `uitleg voorkennis.html` and `uitleg vaardigheden.html`:

- No 3-step/4-step procedure mismatch on any rendered surface.
- Every procedure visual matches its canonical procedure in step
  count, order, and terminology.
- Visuals match adjacent text in numbers, units, and terminology (or
  text explicitly explains a broader-variant visual).
- Worked examples are text-complete (calculations visible in prose,
  not only in the visual).
- Where the artifact contains a list/checks/checklist, it renders as
  structured semantic HTML (`<ul>` / `<ol>` / `<li>`).
- No production / debug labels (`COMPANION VISUAL`, asset filenames,
  internal IDs) on any rendered student-facing visual.
- Alt text and DOCX `descr` are meaningful, not filename-like.
- Surface-adapted light / dark web visuals work.
- Final block routes the student to the right next artifact (per the
  skill's route table).
- `agents/econ-companion-visual-review.md` returns **PASS** or **PASS
  WITH FLAGS** (no hard fails) on both surfaces.
- `render_docx.py --renderer artifact-tool` succeeds on both
  regenerated DOCX files.

Proof required (per `skills/econ-companion-artifacts.md` "Required
delivery" + the review agent's closure proofs):

- Regenerated `uitleg voorkennis.html`, `uitleg voorkennis.docx`,
  `uitleg vaardigheden.html` (and `.docx` if the vaardigheden DOCX
  was edited as part of the sprint).
- Browser-verification screenshots / sub-agent fetch report for both
  surfaces, including light + dark variant smoke.
- Evidence canonical B02 procedure + `fig_3` visual now match across
  every surface that displays B02.
- Evidence the alt-text registry / map yields meaningful descriptions
  in both DOCX `descr` and HTML `alt`.
- Evidence the voorkennis checklist now ends with a routing block;
  spot-check link targets resolve under GitHub Pages.
- Source-output parity report: bullets, tables, calculations,
  checklist content, alt text, route block survive generation.
- `agents/econ-companion-visual-review.md` output for both surfaces
  with verdict PASS or PASS WITH FLAGS, saved as
  `1.1.1-companion-visual-review.md` (overwriting or versioning the
  existing voorkennis review file as the new baseline).
- `render_docx.py --renderer artifact-tool` page PNGs for both
  regenerated DOCX files, attached as artifact-tool render proof.

### Sprint L1.4: First Pipeline Regression Paragraph

Completed: 2026-05-12.

Status: closed 2026-05-12 PASS WITH FLAGS after a polish correction pass. The initial complete build was treated as insufficient because it did not show the intended scalable end product; closure required a polished student-facing baseline plus screenshot QA, not just file presence.

Target paragraph: `1.1.2 Percentages en indexcijfers` (Part A is complete; Part
B build will run against the L1.3A-C + L1.5A + L1.5D platform state).

Purpose:

Prove the platform's pipeline still works on fresh content — not just on
re-regenerations of `1.1.1`. After this restructure, L1.4 carries three
regressions at once:

1. **Layout regression.** Confirm the L1.3A-C layout direction + the L1.5A
   easy polish hold on fresh content.
2. **Games regression on the reworked unit-register.** The platform team
   completed RX.1 / RX.2 representation-and-mutation work and shipped
   `c21ee14 fix(skilltree): hide generator-blocked catalog units`. Building
   1.1.2 confirms the existing 5 games still deploy cleanly with the reworked
   micro-teaching-units before any new games are added in L1.5G-C.
3. **Web-docs regression.** Confirm the DOCX/PPTX-as-web pipeline from L1.5D
   produces correct output on a paragraph that wasn't its development target.

PV note: L1.4 may test formula/table/percentage PV templates only if PV.2/PV.3
are ready. Do not delay L1.4 waiting for the full PV track.

Work:

- Drive the full pipeline: converters (voorkennis / vaardigheden / begeleide
  inoefening), presentation builder, visual variants, paragraaf landing page,
  youtube-videos generator if in scope, plus the L1.5D DOCX/PPTX-as-web
  rendering paths.
- Pass `validate-paragraph.js --mode complete`, `check-links.js`, and
  `check:book`.
- Browser-smoke each generated page on desktop and mobile, light and dark.
- Treat every gap as a platform issue: file a fix against the relevant platform
  script. Do not hand-patch anything inside `4veco-lessen/`.
- If PV.2/PV.3 are available before the build, use `1.1.2` as a regression
  surface for one formula/table/percentage PV template or validator check.

Exit criteria:

- a second Book 1 paragraph has a complete Part B companion set that passes
  complete-mode validation
- every pipeline gap surfaced is fixed in the platform, not in generated output
- browser smoke confirms the L1.3A-C + L1.5A layout direction holds on new
  content
- the existing 5 games deploy cleanly under the reworked unit-register
- DOCX/PPTX rendered as web matches the L1.5D spec on `1.1.2`
- PV is not a blocker for L1.4; any PV check here is opportunistic and must
  come from platform/reference data, not a lesson-side hand model.

Closure evidence:

- `archive/sprints/L1.4/L1.4-sprint-plan.md` contains the executed procedure and closure log.
- `1.1.2-companion-visual-review.md` records `PASS WITH FLAGS`.
- Green gates at close: `student-web` complete validation, `publisher-print` Part A validation, deploy link/data tests, skilltree Jest, full `check:book`, and browser screenshot QA for wide/narrow plus light/dark representative states.
- Remaining flag: formal teacher/student review is still needed before final house-style lock-in.

### Sprint L-PV0: PV-G4 Lesson Proof Track Planning

Completed: 2026-05-14.

Position: closed inserted track before PV-dependent scaling work.

Purpose:

Turn the reference-side PV-G4 intake requirements into an executable lesson-team
proof plan. Current platform evidence is `recorded_proof_count: 0/2`, so the
lesson roadmap may not treat L1.5D-B02 or L1.4-PARITY as PV-G4 closure proof
until formal proof records exist.

Work:

- Read the PV-G4 proof requirements, proof template, and current proof-intake
  report from `4veco-platform/references/data/procedure-visual/` and
  `4veco-platform/reports/review-gates/GATE-PV-G4-lesson-regression/`.
- Write `archive/sprints/L-PV0/L-PV0-proof-track-plan.md` with exact proof candidates, artifact paths,
  validation commands, no-hand-patch evidence, stop conditions, and non-goals.
- Candidate 1 should be `1.1.1 Schaarste en economisch denken` mapped to
  `choose_by_opportunity_cost_flow`, unless L-PV0 finds a current blocker.
- Candidate 2 should preferably be an A61 table-trace proof for `1.1.3` or a
  bounded pilot surface, unless a better existing PV overlay is selected in the
  plan.
- Explicitly keep PV machine promotion, student-facing PV projection, adaptive
  diagnostics, and hand-patched generated output out of scope.

Exit criteria:

- the plan names two proof candidates and their PV records
- the plan states where proof artifacts live
- the plan names exact platform/lesson validation commands
- the plan proves how no-hand-patch evidence will be checked
- stop conditions are explicit and checkable before execution

Closure evidence:

- `archive/sprints/L-PV0/L-PV0-proof-track-plan.md` created and later marked closed.
- Candidate 1 selected `1.1.1` B02 / `choose_by_opportunity_cost_flow`.
- Candidate 2 selected bounded A61 table-trace pilot / `select_table_values_trace`.

### Sprint L-PV1: Procedure Contract Hardening

Completed: 2026-05-14.

Position: after L-PV0, before proof records.

Purpose:

Upgrade the current parity guard from count-only checking to a procedure
contract that catches the actual drift class seen in `1.1.1` and `1.1.2`:
step count, IDs, order, labels/keywords, required surface coverage, and
student-facing internal-code leakage.

Current repo check:

- L1.4-PARITY added a useful count guard against `quality-ref.yaml` versus
  shared procedure data.
- That is not enough for PV-G4 proof because a 4-step procedure can still have
  wrong order, wrong labels, missing formal IDs, or missing surfaces.
- `Boek 1 - Grondslagen, vraag en aanbod/shared/procedure/1.1.1.js` still has
  the phrase `(unit B02)` in the procedure description; this must be treated as
  a live student-facing leakage risk until the procedure-game UI proves
  otherwise or the generator removes it.

Work:

- Add or declare procedure contracts in the platform-owned source of truth.
- Include formal step IDs, student-facing labels, required surface keywords,
  canonical order/count, required surfaces, and PV template/unit links where
  applicable.
- Extend validators to compare count, formal step IDs where present, order,
  required keywords, required surface coverage, legacy wording, and internal
  codes such as `B02`, `A38`, or `A39` in student-facing generated pages/data.
- Add negative fixtures: 3-vs-4 drift, 4-vs-5 drift, same count wrong order,
  same count missing key step, and student-facing code leakage.

Exit criteria:

- `1.1.1` passes against the B02/economisch-denken contract
- `1.1.2` passes against its three four-step contracts
- deliberate broken fixtures fail with clear surface-specific messages
- no protected reference files are hand-edited
- no student-facing `B02` remains in generated lesson UI/data for proof 001

Closure evidence:

- Platform registry: `references/data/procedure-visual/lesson-procedure-contracts.json`.
- Validator: `scripts/validate-procedure-contracts.js`.
- Negative fixtures: `scripts/tests/procedure-contracts.test.js`.
- Green gates: focused Jest and real Book 1 procedure-contract validation.

### Sprint L-PV2: Proof 001 - 1.1.1 B02 Procedure Mapping

Completed: 2026-05-14.

Position: after L-PV1.

Purpose:

Produce the first formal lesson-owned PV-G4 proof record for `1.1.1 Schaarste
en economisch denken`, using `choose_by_opportunity_cost_flow`.

Proof scope:

- procedure game maps to formal PV steps
- answer model and companion surfaces preserve PV step order
- Part A, Part B, presentation, procedure game, quality-ref, and chapter plan
  align to the same four-step contract

Required proof record:

- `proof_id`: `PVG4-proof-001`
- `lesson_repo_commit`: lesson-team commit SHA
- `paragraph_or_surface`: `1.1.1 Schaarste en economisch denken`
- `pv_records_used`: `choose_by_opportunity_cost_flow` plus linked visual/unit
  records available in the PV overlay
- `validation_commands`: complete paragraph validation, Part A validation,
  `check:book`, procedure-contract validator, focused procedure-game tests, and
  presentation semantic checks if touched
- `generated_output_touched`: true if regenerated output changes
- `hand_patch_absent`: true with evidence
- `owner`: `lesson_team`
- `review_status`: `submitted_for_pv_g4_review`

Exit criteria:

- proof record has all PV-G4 required fields
- contract validator proves all required `1.1.1` surfaces align
- student-facing generated HTML/JS/data does not expose `B02`
- output is rebuilt through platform workflow, not hand-patched

Closure evidence:

- Proof record: `pv-g4-proof-records/PVG4-proof-001.json`.
- Contract report: `pv-g4-proof-records/reports/PVG4-proof-001-procedure-contract-report.json`.
- Platform generator: `build-scripts/content/book-1/b1-111-procedure-data.js`.
- Stale chapter/book/test-prep surfaces were rebuilt through existing build scripts.

### Sprint L-PV3: Proof 002 - Fresh PV-Validated Surface

Completed: 2026-05-14.

Position: after L-PV1 and the candidate choice in L-PV0.

Purpose:

Produce a second formal PV-G4 proof from a different lesson-side surface or
paragraph, not merely a second audit of the same B02 cleanup.

Preferred candidate:

- A61 `select_table_values_trace` on `1.1.3 Grafieken en tabellen` or a bounded
  lesson-owned pilot surface.

Alternatives:

- A07 formula trace if a suitable generated formula surface exists.
- A83 graph-stage sequence if the graphical-game path is ready, but this is
  higher risk and should not be chosen casually.
- A84 flowchart if L-PV0 decides a second flowchart proof is the best safe path.

Exit criteria:

- `PVG4-proof-002` uses a different PV template or materially different proof
  type from proof 001
- proof is not screenshot-only
- proof does not require PV records to move into `references/machine`
- proof does not authorize student-facing PV projection
- validation commands are reproducible

Closure evidence:

- Proof record: `pv-g4-proof-records/PVG4-proof-002.json`.
- Pilot surface: `pv-g4-proof-records/pilot-surfaces/a61-table-trace-pilot.json`.
- Validation report: `pv-g4-proof-records/reports/PVG4-proof-002-a61-table-trace-report.json`.
- Human-review boundary: HCS must decide whether the bounded pilot is sufficient
  as proof 002.

### Sprint L-PV4: PV-G4 Intake Closure Packet

Completed: 2026-05-14.

Position: after L-PV2 and L-PV3.

Purpose:

Submit the two lesson-owned proof records into the PV-G4 intake path and prepare
the HCS closure packet.

Work:

- Add both proof records to the PV-G4 intake surface.
- Run `build-procedure-visual-lesson-regression-proof-intake.js`.
- Run `check-procedure-visual-lesson-regression-proof-intake.js`.
- Confirm the report records `2/2` proofs and still forbids PV machine
  promotion and student-facing PV projection.
- Prepare a concise HCS packet: what the proofs show, which PV records were
  used, which lesson commits own output, which validators passed, remaining
  risks, and explicit blocked uses.

Exit criteria:

- proof intake no longer reports `0/2`
- both proof records are complete
- HCS has a review packet and recommended gate outcome
- no PV machine promotion occurs

Closure evidence:

- Lesson packet: `pv-g4-proof-records/HCS-PV-G4-lesson-regression-review-packet.md`.
- Platform intake: `reports/json/procedure-visual-lesson-regression-proof-intake.json`.
- Platform gate packet: `reports/review-gates/GATE-PV-G4-lesson-regression/review-packet.md`.
- Checker: `node build-scripts/references/check-procedure-visual-lesson-regression-proof-intake.js` passed.

### Sprint L-PV5: Roadmap Sync After PV-G4

Completed: no. Technical QA green; ready for human review.

Position: after the HCS PV-G4 decision.

Purpose:

Make lesson and reference roadmaps agree after PV-G4.

If PV-G4 passes:

- mark the reference-side PV-G4 gate closed
- update this roadmap so L1.5G consumes PV records only under the approved
  non-promotional constraints
- require L1.6 to use the proof machinery during the fresh paragraph build
- keep student-facing PV projection blocked unless a later gate authorizes it

If PV-G4 fails or passes with conditions:

- record the exact condition
- insert remediation before L1.5G/L1.6
- do not allow Sprint 8 or game/generator work to assume PV-G4 is closed

Exit criteria:

- lesson and reference roadmaps agree
- no future sprint implies PV machine promotion
- PV-dependent scaling work has an explicit go/no-go status

Closure evidence:

- HCS review plan: `pv-g4-proof-records/HCS-PV-G4-lead-review-plan.md`.
- HCS review record: `pv-g4-proof-records/HCS-PV-G4-lead-review-record.md`.
- HCS verification: `pv-g4-proof-records/HCS-PV-G4-lead-review-verification.md`.
- Sync log: `archive/sprints/L-PV5/L-PV5-roadmap-sync-log.md`.
- Reconciled platform intake: `reports/json/procedure-visual-lesson-regression-proof-intake.json` in `4veco-platform`.

Decision recorded:

- HCS lead review returned `PASS WITH CONDITIONS`.
- The evidence-freshness condition was reconciled by regenerating the lesson
  proof records and platform intake. Both now cite lesson commit
  `52f9237de9e465e7f75483f6feac4e80241e8631` with
  `lesson_worktree_dirty_at_generation: false`.
- Post-closure report-state cleanup made the platform intake and lesson HCS
  packet closure-aware so they no longer instruct the lesson team to submit an
  already-reviewed packet.
- Proof 002 remains a bounded, non-student-facing A61 pilot; it does not make
  an A61 student route classroom-ready.
- PV machine promotion, student-facing PV projection, diagnostics, adaptive
  use, AI, sequencing, mastery, and summative use remain blocked.

Go/no-go after L-PV5:

- `L1.5B` may proceed under the PV-G4 condition boundary.
- `L1.5G-A` through `L1.5G-E` replace the single broad `L1.5G`; each
  sub-sprint must use the L-PV contract/proof machinery where PV semantics are
  involved.
- `L1.6` must use the L-PV machinery for at least one procedure/visual sequence
  where PV data exists.

### Sprint L1.5B: Layout Round 2 - Generator Items

Completed: 2026-05-14.

Position: after the L-PV proof track unless explicitly scoped as non-PV and
non-procedure layout work. Originally the whole of L1.5; L1.5A was split off
and pulled forward.

Purpose:

Tighten the companion layout/front-end on the items that need fresh-paragraph
input or that touch generators. Use L1.4's findings as input plus the
deferred items from the rolled-back round-2 attempt and from L1.5A's planner.

Work:

- Consolidate P1 and P2 findings from the L1.3A-C human usability review.
- Act on anything L1.4 surfaced: accent-domain mismatches, empty-section
  states on Part-A-only paragraphs, sidebar defaults, mobile breakpoints,
  resource-card density, callout hierarchy, light/dark regressions on new
  content.
- Land the deferred round-2 item #3 (split "Valkuilen en misvattingen" into
  per-card pitfalls in `build-landing-page.js`) — generator-touching, so it
  needs L1.4's fresh-paragraph regression in the rear-view mirror.
- Land the deferred round-2 item #1 (per-section accents on chapter/book
  index cards). The L1.5A planning sub-agent reclassified this as
  generator-touching with the following evidence: `.section-card` does not
  exist in the platform; cards are emitted as `.chapter-card`
  (`build-scripts/platform/build-landing-page.js` ~line 499) and `.para-card`
  (~line 542); current accent is an inline `style="--ch-color: ${dc2.main}"`
  from a 5-color palette, not the editorial 3-token system; editorial accent
  CSS rules in `engines/voorkennis.css` require either `body[data-accent-domain]`
  or class hooks (`bg-economisch` / `border-...` / `badge-...` / `domain-...`)
  or a `data-domain` attribute, none of which the cards carry. Implementation
  requires editing the renderBookPage / renderChapterPage emission sites to
  add a `data-domain` attribute (or matching class hook) and adding matching
  CSS rules.
- Keep all changes in platform-owned CSS/JS, converters, templates, and
  build scripts. No one-off fixes in generated files.
- Rerun both `1.1.1` and the L1.4 paragraph end to end and confirm no
  regressions against the hard gates.

Exit criteria:

- layout/UI improvements land in platform sources and regenerate cleanly for
  both paragraphs
- no outstanding P1 items remain from the L1.3A-C usability review
- `validate-paragraph.js --mode complete` passes for both paragraphs

Closure evidence:

- Plan and closure: `archive/sprints/L1.5B/L1.5B-sprint-plan.md`.
- Dedicated log: `archive/sprints/L1.5B/L1.5B-closure-log.md`.
- Platform source commit:
  `cb216ed160a9298f7f4393034b6c1d842a387ff9`.
- Generated output: Book 1 root index, chapter 1.1 index, and shared
  `voorkennis.css` regenerated through platform `deploy.js`.
- Green gates: landing generator Jest, procedure-contract validator
  (289 checks), `1.1.1` complete student-web validation, `1.1.2` complete
  student-web validation, Book 1 health 26/26, diff hygiene, and
  desktop/mobile light/dark screenshot QA.

Decision:

Closed PASS. The L1.5G split track may start next, but only under the PV-G4
`PASS WITH CONDITIONS` boundary; L1.5G-A closed the scope cut and L1.5G-B is
the next implementation-planning sprint.

### Sprint L1.5G-A: Graphical Game Scope Cut And Prototype Audit

Completed: 2026-05-16.

Position: after L1.5B, before any graphical-game code migration.

Purpose:

Audit `knowledge/grafiekmeester_representatie_arena.html`, decide the first
graphical-game MVP cut, and split the oversized L1.5G into checkable
sub-sprints.

Decision:

Do not port GrafiekMeester directly. The prototype is an 87 KB standalone
product concept with UI shell, campaign/training controls, skill tree, XP,
level/streak/stars, localStorage progress, coach panel, badges, graph rendering
helpers, and broad skills across tables, bars, lines, pie charts, percentages,
index numbers, producer graphs, elasticity, and market graphs.

MVP cut:

- keep graph reading and value selection only;
- use the rhythm `bron -> waarden -> berekening`;
- first challenge types: read a bar value, read a line value, select old/new
  graph values and calculate percentage change;
- use `1.1.2` or a sandbox as the technical pilot;
- let L1.6 prove the game on a fresh paragraph, preferably `1.1.3 Grafieken en
  tabellen`.

Closure evidence:

- `archive/sprints/L1.5G-A/L1.5G-A-graphical-game-scope-plan.md`
- `archive/sprints/L1.5G-A/L1.5G-A-prototype-extraction-matrix.md`
- `archive/sprints/L1.5G-A/L1.5G-A-mvp-data-model-sketch.md`

PV/adaptive boundary:

No PV machine promotion, no student-facing PV projection, no diagnostics, no
adaptive behavior, no mastery routing, no sequencing, no AI, no summative use,
and no generated-output hand patching.

### Sprint L1.5G-B: Adaptive Input Seam Contract

Completed: 2026-05-16.

Position: after L1.5G-A, before graphical-game engine work.

Purpose:

Define the shared adaptive payload seam without building adaptive behavior.

Work:

- define one localStorage key and minimal schema;
- add a safe platform helper for reading the payload;
- update the existing five games to read the helper while preserving current
  behavior when the payload is absent/default;
- add tests proving empty/default payload causes no behavior change;
- document that no advisor, diagnostics, mastery, sequencing, AI, or summative
  use exists.

Exit criteria:

- all existing games work unchanged with no payload;
- the graphical MVP can later read the same seam;
- no student-facing adaptive claims appear.

Closure evidence:

- Platform commit `9014a50eb85ccbd48c0770bf677b36d75455aa48`.
- Lesson closure log: `archive/sprints/L1.5G-B/L1.5G-B-closure-log.md`.
- Sprint plan: `archive/sprints/L1.5G-B/L1.5G-B-adaptive-seam-plan.md`.
- Generated Book 1 game shells were rebuilt by platform `deploy.js`; no
  generated lesson output was hand-patched.
- Gates passed: focused seam Jest 8/8, deploy link/data checks, procedure
  contract validator 289 checks, `1.1.1` and `1.1.2` complete student-web
  validation, Book 1 health 26/26, full platform Jest 488 passed / 7 skipped.

### Sprint L1.5G-C: Graphical Game MVP Engine

Completed: 2026-05-16.

Position: after L1.5G-B.

Purpose:

Create a narrow platform-owned sixth game from the L1.5G-A MVP cut.

Work:

- added `engines/graphical-engine.js`, `engines/graphical-ui.js`, and
  `engines/graphical.css`;
- added `build-scripts/platform/build-graphical-shells.js`;
- added `build-scripts/content/book-1/b1-112-graphical-data.js`;
- added focused graphical engine/data tests and an adaptive-seam regression
  test for the sixth game;
- updated `scripts/deploy.js` to copy graphical engine files and generate
  shells;
- updated `build-scripts/platform/build-landing-page.js` so `grafiekenspel`
  is reachable from the paragraph landing page;
- seeded four explicit `1.1.2` challenge records: bar value read, line value
  read, bar old/new percentage change, and line/index old/new percentage
  change;
- regenerated Book 1 output through platform `deploy.js`, with no generated
  output hand-patching.

Closure evidence:

- Platform commit `042d7aea4f4cfbe5cd026a3a29cbb57891f795be`.
- Lesson closure log: `archive/sprints/L1.5G-C/L1.5G-C-closure-log.md`.
- Sprint plan: `archive/sprints/L1.5G-C/L1.5G-C-graphical-game-mvp-plan.md`.
- Generated output includes `shared/graphical/1.1.2.js`, shared graphical
  engine files, `1.1.2 Percentages en indexcijfers – grafiekenspel.html`,
  and a regenerated `1.1.2` landing page.
- Green gates: focused graphical/adaptive Jest 20/20, deploy link/data checks,
  `1.1.2` complete student-web validation, procedure-contract validator
  289 checks, Book 1 health 26/26, platform Jest 494 passed / 8 skipped, and
  desktop/mobile Chrome screenshot smoke.

Out of scope:

- full skill tree;
- XP/badges/campaign mode;
- producer/profit graphs;
- elasticity and market-equilibrium graphs;
- broad random generator universe;
- adaptive behavior beyond reading the default seam.

Decision:

Closed PASS. L1.5G-D is now the next game-track sprint. L1.5G-E remains the
formal integration/review gate before L1.6.

### Sprint L1.5G-D: Three-Aspect Game Routing

Completed: 2026-05-17.

Position: after L1.5G-C.

Purpose:

Make the companion system visibly cover reasoning, calculation, and graphical
representation without creating a pile of undifferentiated game tiles.

Work:

- defined the aspect taxonomy in platform terms:
  - `reasoning` -> Redeneren
  - `calculation` -> Rekenen
  - `graphical` -> Grafieken
- attached stable `data-learning-aspect` metadata to generated route cards;
- rendered the `Oefenen` section with a visible `Oefenroutes` block;
- separated `Begeleide inoefening` into an `Extra steun` block so it is not a
  fourth aspect;
- regenerated chapter 1.1 paragraph landing pages through platform `deploy.js`;
- kept all visible copy student-facing and concept-facing.

Exit criteria:

- each aspect has one obvious student route;
- teacher-facing planning can explain why each route exists;
- no PV/adaptive/diagnostic claims are visible to students.

Closure evidence:

- Platform commit `84ed88e78791203db779a4daecbc02589c99ed1d`.
- Sprint plan: `archive/sprints/L1.5G-D/L1.5G-D-three-aspect-routing-plan.md`.
- Closure log: `archive/sprints/L1.5G-D/L1.5G-D-closure-log.md`.
- Green gates: landing generator Jest, deploy link/data checks, `1.1.1` and
  `1.1.2` complete student-web validation, procedure-contract validator
  289 checks, Book 1 health 26/26, platform Jest 494 passed / 8 skipped, and
  desktop/mobile Chrome screenshot smoke.

Decision:

Closed PASS. L1.5G-E is now the next sprint and should be treated as the
formal integration, QA, and review gate for the split L1.5G track before L1.6.

### Sprint L1.5G-E: Integration, QA, And Review Gate

Completed: 2026-05-18.

Status update 2026-05-18: closed PASS WITH FLAGS after second-revision review
accepted the final-feedback fix.

Position: after L1.5G-D, before L1.6.

Purpose:

Close the split L1.5G track only after generated output is reachable and
visually checked.

Required checks:

- graphical engine tests;
- graphical data validator;
- deploy/link/data checks;
- `validate-paragraph --mode complete --profile student-web` for the pilot;
- `check:book`;
- procedure-contract validator if procedure-linked content appears;
- desktop/mobile and light/dark screenshot QA;
- student-experience review;
- teacher-learning-quality review if used in a real paragraph.

Closure condition:

The graphical MVP is reachable and usable in `4veco-lessen`, the adaptive seam
exists without adaptive behavior, and PV-G4 blocked-use boundaries are still
preserved.

Technical evidence prepared:

- Plan: `archive/sprints/L1.5G-E/L1.5G-E-integration-qa-review-gate-plan.md`.
- Technical QA report: `archive/sprints/L1.5G-E/L1.5G-E-technical-qa-report.md`.
- Human-review packet: `archive/sprints/L1.5G-E/L1.5G-E-human-review-packet.md`.
- Human-review record: `archive/sprints/L1.5G-E/L1.5G-E-human-review-record.md`.
- Student-experience review: `archive/sprints/L1.5G-E/L1.5G-E-student-experience-review.md`.
- Teacher-learning-quality review:
  `archive/sprints/L1.5G-E/L1.5G-E-teacher-learning-quality-review.md`.
- Lead review summary: `archive/sprints/L1.5G-E/L1.5G-E-lead-review-summary.md`.
- Closure log: `archive/sprints/L1.5G-E/L1.5G-E-closure-log.md`.
- Screenshot evidence: `archive/sprints/L1.5G-E/L1.5G-E-screenshots/`.

Technical status:

- focused graphical/adaptive tests passed, including the new graphical UI
  safeguard tests;
- deploy/link/data checks passed;
- `1.1.1` and `1.1.2` complete student-web validation passed;
- procedure-contract validator passed with 289 checks;
- Book 1 health passed 26/26;
- full platform regression passed;
- screenshot QA passed after a platform-source mobile chart fix and
  regeneration.

Human-review REVISE response:

- neutral answer placeholders replace expected-answer placeholders;
- old/new dropdowns now require explicit selection;
- a visible checklist appears before the answer form;
- wrong-answer feedback now diagnoses missing selection, wrong old/new value,
  or calculation error;
- `1.1.2-quality-ref.yaml` includes `grafiekenspel`.

Focused re-review REVISE response:

- final challenge feedback no longer jumps directly to summary;
- final wrong answer now shows diagnostic feedback and
  `Bron/Waarden/Berekening`;
- `Bekijk resultaat` opens the summary after the student has seen final
  feedback;
- screenshot evidence includes desktop and true-390px mobile final-feedback
  states.

Closure verdict:

L1.5G-E closed PASS WITH FLAGS. The final-feedback flow was accepted in the
second-revision review. Flags carried forward:

- L1.6 must prove the graphical game and adaptive seam on a fresh paragraph.
- Later graphical-game variants should include harder graph-reading tasks
  without direct value labels.
- PV-G4 boundaries remain in force.

### Superseded Original L1.5G Scope - Do Not Execute As One Sprint

Superseded: 2026-05-16 by L1.5G-A through L1.5G-E.

Historical note:

The old single-sprint scope bundled graphical-game migration, adaptive seam,
three-aspect routing, existing-game refactor, PV alignment, generated lesson
output, and QA into one gate. That scope is now intentionally retired. Use the
L1.5G-A through L1.5G-E sections above as the authoritative plan.

### Sprint L1.6: Second Pipeline Regression Paragraph

Completed: 2026-05-18.

Position: after the urgent L1.5P print cut and the L1.5Q blueprint-source
decision are safe enough not to conflict with the fresh paragraph build. L1.6
uses the L-PV proof machinery established before PV-G4 closure.

Purpose:

Confirm the L1.5B layout changes + L1.5G-C graphical game + adaptive-seam
refactor did not break the pipeline by driving the full Part B workflow end to
end on a third Book 1 paragraph. Two independent regenerations against the
post-restructure platform state is the minimum signal that the pattern is safe
to scale.

Work:

- Pick a third Book 1 paragraph (team picks — likely `1.1.3 Grafieken en
  tabellen` or `1.1.4 Gemengde opgaven`, whichever has clean Part A and a
  defensible Part B scope).
- Drive the full pipeline including the new graphical game and the DOCX/PPTX-
  as-web rendering paths; same validator + check-links + check:book gates as
  L1.4.
- Browser-smoke the generated pages in light and dark on desktop and mobile,
  including each game's prototype and the web-rendered authored content.
- Use or validate at least one procedure/visual sequence from the PV registry in
  the fresh paragraph where PV data exists and the PV-G4 gate allows it.
  Acceptable proof is one procedure game mapped to formal steps, one visual-state
  sequence used in a companion visual, or one answer model validated against PV
  step order.
- Any breakage becomes a platform fix and a regeneration; no hand-patches.

Exit criteria:

- a third Book 1 paragraph has a complete Part B companion set that passes
  complete-mode validation
- zero hand-patches remain in `4veco-lessen/` for the new paragraph
- at least one procedure/visual sequence is generated from or validated
  against PV data if the PV registry has passed the required gate
- browser smoke confirms Layout Round 2 + new graphical game + adaptive seam
  + web-rendered authored content hold on new content

Post-closure incident:

On 2026-05-19, post-closure review accepted that L1.6 was technically useful
but found a systemic dual-coding failure in the `1.1.3` companion layer. The
presentation, vaardigheden page, and guided-practice surfaces explain
graphs/tables without consistently showing the graph/table learning objects.
This does not erase the fresh-build proof, but it reopened the `1.1.3`
student-facing companion quality verdict. L1.6R later remediated this incident
and closed PASS WITH FLAGS.

### Sprint L1.6R: 1.1.3 Dual-Coding Remediation

Completed: 2026-05-19.

Position: closed incident-remediation sprint before L1.7A.

Plan: `archive/sprints/L1.6R/L1.6R-dual-coding-remediation-plan.md`.

Incident record: `archive/sprints/L1.6R/L1.6R-dual-coding-incident-record.md`.

Purpose:

Repair the `1.1.3 Grafieken en tabellen` companion layer so graph/table
procedures are visibly attached to the tables, axes, points, guide lines,
scales, and graph comparisons students must inspect.

Work:

- Rebuild the presentation through platform source so graph/table slides show
  actual visuals, not only text cards or procedure routes.
- Rebuild `uitleg vaardigheden` so each core procedure has a worked visual
  example beside the steps.
- Rebuild `begeleide inoefening` so graph/table exercises include their source
  graph or table.
- Add visual support to voorkennis, samenvatting, and nieuws met visual where
  needed.
- Add or log the platform path for a dual-coding contract, semantic
  visual-object presence check, plan-vs-artifact visual reconciliation, and
  semantic screenshot QA.
- Update review questions so graph/table paragraphs require visible evidence:
  table, axis, point, guide line, and scale comparison.
- Update quality-ref/review state so core modality absence is REVISE/FAIL, not
  PASS WITH FLAGS.

Out of scope:

- broad redesign of the graphical game
- target-exercise distribution audit
- adaptive behavior, diagnostics, mastery, sequencing, AI, or summative use
- PV projection or PV machine promotion
- hand-patching generated lesson output

Exit criteria:

- required visuals are present on presentation, vaardigheden, and guided
  practice surfaces
- every graph/table procedure has `procedure + worked visual example + student
  action`
- semantic visual QA records each required visual object and evidence
- `1.1.3` complete student-web validation passes again
- Part A publisher-print validation remains green
- procedure-contract validation and Book 1 health remain green
- review records close L1.6R as PASS WITH FLAGS or better
- L1.7A receives an explicit modality-gate result after closure

Closure state:

The first L1.6R human review returned REVISE because the guided-practice
visuals existed but did not consistently match the exercise data. The targeted
revision now uses exercise-specific visuals for broodjes, koffie, bioscoop, and
water/index and adds visual-value concordance to the focused Jest gate. Focused
human recheck accepted the correction and closed L1.6R as PASS WITH FLAGS.
Remaining flags: scaffolded/value-labelled graph visuals are acceptable for
this remediation sprint; later graph-reading variants should reduce direct
labels; visual-value concordance should become a reusable QA gate.

### Sprint L1.7A: Scaling Readiness And Modality Gate Review

Completed: yes, 2026-05-23.

Purpose:

Decide what the lesson side has actually proven and what remains too weak for
broad scaling. L1.7A is a readiness, modality, and flag-triage gate, not a
production scaling sprint.

Work:

- Review the regenerated `1.1.1` plus the L1.4 and L1.6 paragraphs after
  layout/UI and visual-integration improvements.
- Build a readiness matrix for Part A, landing pages, procedure contracts,
  semantic visual adequacy, presentation-v2, begeleide inoefening, graphical
  game, inert adaptive seam, target exercises, and PV/A61 boundaries.
- Record whether L1.6R repaired the `1.1.3` dual-coding failure or whether it
  remains a scale-blocking modality risk.
- Classify every visible flag as fix-now, carry-forward, or defer.
- Decide whether the next lesson sprint should be polish, another regression
  paragraph, controlled production, or a pause for reference hardening.
- Explicitly answer: are we ready to scale many paragraphs? Current expected
  answer is no: ready for controlled next-step production only, not broad
  scaling.
- Keep all builder scripts saved under the platform `build-scripts/content/book-1/`
  workflow.
- Separate remaining content problems from platform usability problems.
- Include PV readiness in the scaling decision: procedure consistency, visual
  semantic anchors, surface variants, game mapping, answer-model alignment,
  and generator-block controls.

Target-exercise note:

L1.7A may log visible target-exercise red flags found during readiness review,
but it does not perform the full target-exercise distribution audit. The full
audit is deferred to L2.4-TEA, after MTU quality and review instrumentation are
strong enough to support reliable judgement. L1.7A is a readiness and flag
triage sprint, not a hidden curriculum redesign sprint.

Exit criteria:

- a readiness matrix exists and covers each major pipeline area
- each current L1.6/L1.5Q flag is classified as fix-now, carry-forward, or
  defer
- the lesson team records whether the next sprint is L2.0 cleanup, another
  regression paragraph, controlled production, or reference hardening
- broad companion production is either explicitly rejected for now or given a
  narrow, evidence-bounded condition set
- PV-G4 blocked-use boundaries remain explicit

Closure state:

L1.7A closed PASS WITH FLAGS. Current validators are green, but broad companion
scaling is rejected. L1.7B-C has since paused implementation after recording
the exit-ticket companion contract; the active lesson-side work has moved
through L1.7C-0, L1.7C, and L1.7D to L2.0. Evidence and decision records live
under `archive/sprints/L1.7A/`.

### Sprint L1.7B-C: Exit Ticket Companion Contract

Completed: 2026-05-23. Status: closed contract-only / MVP paused.

Position: after L1.7A. This row records the completed contract and stop
decision from the original L1.7B work. It does not authorize implementation.

Purpose:

Define the complete paragraph companion set and decide whether an exit-ticket
game is the missing completion surface. The exit ticket remains a
non-summative retrieval/checkpoint activity, not a grade, mastery decision,
sequencing input, or adaptive diagnostic.

Completed work:

- Inspected the existing untracked exit-ticket prototype at
  `../4veco-platform/knowledge/exit-ticket-game-1.1.1.zip`.
- Recorded the prototype as design evidence only.
- Logged the prototype source-control gap.
- Ran the prototype unit test in a temporary copy.
- Recorded the companion-completion contract.
- Recorded the future MVP scope.
- Recorded the implementation stop decision.

Stop decision:

Implementation is not authorized from L1.7B-C because the prototype is
untracked, uses mastery/score/pass/evidence/adaptive-focus language, and must
consume shared skill-map compact checkpoint mode before any student-facing use.
Human review and screenshot QA were not run because no MVP was generated.

Records:

- `archive/sprints/L1.7B/L1.7B-sprint-plan.md`
- `archive/sprints/L1.7B/L1.7B-prototype-inventory.md`
- `archive/sprints/L1.7B/L1.7B-companion-completion-contract.md`
- `archive/sprints/L1.7B/L1.7B-exit-ticket-mvp-scope.md`
- `archive/sprints/L1.7B/L1.7B-stop-decision.md`
- `archive/sprints/L1.7B/L1.7B-validation-log.md`

### Sprint L1.7B-R: Boundary-Safe Exit Ticket MVP Resume

Completed: 2026-05-26. Status: closed PASS WITH FLAGS.

Position: after L2.0 and platform support planning. Platform implementation
support has been delivered under `GAME-UX-2`.

Purpose:

Resume exit-ticket implementation as a source-controlled, non-summative
checkpoint MVP. The implementation must be a platform-owned engine or wrapper,
not a one-off lesson artifact.

Work:

- Import or rewrite the prototype as source-controlled platform code.
- Remove mastery/pass/score/evidence/adaptive-focus language.
- Consume shared skill-map compact checkpoint mode from `GAME-UX-1`.
- Build one checkpoint MVP on one already-built paragraph.
- Use neutral feedback and self-check/retry affordances.
- Allow bounded guidance such as "try Redeneren next" or "review this graph
  skill" only as practice support, not diagnosis or sequencing.
- Integrate the landing-page `Check` slot through the generator: show `Check`
  only for paragraphs with reviewed exit-ticket output and keep it hidden
  elsewhere.
- Add student-experience review, teacher-learning-quality review, and
  screenshot/interaction QA.
- Keep the build owned by platform generators; no hand-patched generated output.

Out of scope:

- grading
- pass/fail thresholds
- mastery decisions
- adaptive routing or diagnostics
- sequencing
- student-facing AI
- summative use
- PV projection or PV machine promotion
- broad companion scaling

Exit criteria:

- source-controlled implementation exists or a renewed stop decision is
  recorded
- shared skill-map compact checkpoint mode is consumed
- no internal MTU codes appear in student-facing text
- no adaptive payload keys are used for routing
- landing-page `Check` activation is generator-owned and scoped to reviewed
  exit-ticket output
- validators and screenshot/interaction QA required by the platform workflow
  pass
- GATE-L1.7B is ready for human review

Closure decision, 2026-05-26:

Platform `GAME-UX-2` has produced the source-controlled checkpoint engine and
generated lesson output through platform scripts only. Lesson output commit
`5c47961269096c21a7d50bbc97c71de7984ff6e1` contains the `1.1.1` checkpoint
surface and landing-page `Check` activation. L1.7B-R technical QA is green and
human review closed PASS WITH FLAGS. Generated checkpoint metadata `A43`/`A04`
versus paragraph-plan skills `B01`/`B02` is accepted as a carried
platform/skill-map limitation, not as a closure blocker. It must be carried
into GATE-L1.7B and any scale decision.

Retrospective REV-STD-1 classification: L1.7B-R closed a checkpoint-only
product boundary. It did not satisfy the fuller exit-ticket
target-exercise-readiness specification. Metadata alignment has since closed
under L1.7B-MAP; the remaining readiness gap is assigned to L1.7B-P23,
L1.7B-Q2, and GATE-L1.7B-Q2.

Records:

- `archive/sprints/L1.7B-R/L1.7B-R-sprint-plan.md`
- `archive/sprints/L1.7B-R/L1.7B-R-baseline-audit.md`
- `archive/sprints/L1.7B-R/L1.7B-R-platform-support-request.md`
- `archive/sprints/L1.7B-R/L1.7B-R-stop-decision.md`
- `archive/sprints/L1.7B-R/L1.7B-R-validation-log.md`
- `archive/sprints/L1.7B-R/L1.7B-R-platform-response.md`
- `archive/sprints/L1.7B-R/L1.7B-R-technical-qa-report.md`
- `archive/sprints/L1.7B-R/L1.7B-R-human-review-packet.md`
- `archive/sprints/L1.7B-R/L1.7B-R-screenshots/`
- `archive/sprints/L1.7B-R/L1.7B-R-student-experience-review.md`
- `archive/sprints/L1.7B-R/L1.7B-R-teacher-learning-quality-review.md`
- `archive/sprints/L1.7B-R/L1.7B-R-human-review-record.md`
- `archive/sprints/L1.7B-R/L1.7B-R-lead-review-summary.md`
- `archive/sprints/L1.7B-R/L1.7B-R-closure-log.md`

### Gate GATE-L1.7B: Exit Ticket Product-Boundary Review

Completed: 2026-05-26. Status: closed PASS WITH FLAGS.

Purpose:

Confirm that the exit-ticket MVP is a non-summative checkpoint surface, not a
test, grade, mastery decision, adaptive diagnosis, sequencing decision, or
student-facing recommendation engine.

Review must verify:

- source-controlled implementation
- shared skill-map compact checkpoint use
- neutral feedback language
- no pass/fail thresholds
- no mastery, score, evidence, or adaptive-focus language
- no hidden adaptive payload routing behavior
- no internal MTU codes in student-facing text
- no generated-output hand patches
- no diagnostics, adaptive routing, mastery, sequencing, student-facing AI,
  summative use, PV projection, or PV machine promotion

Retrospective REV-STD-1 classification: GATE-L1.7B accepted the current
checkpoint boundary only. It does not close the original target-exercise
readiness specification and must not be used as proof that students are ready
for the paragraph target exercise.

Records prepared before review:

- `archive/sprints/GATE-L1.7B/GATE-L1.7B-sprint-plan.md`
- `archive/sprints/GATE-L1.7B/GATE-L1.7B-validation-log.md`
- `archive/sprints/GATE-L1.7B/GATE-L1.7B-human-review-packet.md`

Closure records:

- `archive/sprints/GATE-L1.7B/GATE-L1.7B-product-boundary-review.md`
- `archive/sprints/GATE-L1.7B/GATE-L1.7B-human-review-record.md`
- `archive/sprints/GATE-L1.7B/GATE-L1.7B-lead-review-summary.md`
- `archive/sprints/GATE-L1.7B/GATE-L1.7B-closure-log.md`

### Sprint SPEC-END-STATE: Product End-State Specification Canonicalization

Completed: 2026-05-26. Status: CLOSED PASS.

Position: specification-hardening sprint after stable companion specification
creation and before the remaining pre-scale exit-ticket/review-standard
sequence.

Purpose:

Create a canonical product end-state specification outside the active roadmap
so future agents compare sprint scope against the full product definition
instead of treating roadmap shorthand as the product itself.

Outputs:

- `specifications/product-end-state.md`
- `archive/sprints/SPEC-END-STATE/SPEC-END-STATE-sprint-plan.md`
- `archive/sprints/SPEC-END-STATE/SPEC-END-STATE-validation-log.md`
- `archive/sprints/SPEC-END-STATE/SPEC-END-STATE-closure-log.md`
- updated lesson and platform operating docs/maps linking to the new spec

Closure rule:

Future work that touches paragraph completeness, exit tickets, game-row
architecture, official exam ingestion, Scale Gate 1, or review standards must
preserve the end-state sentence: every paragraph gives the student a visible
route from current readiness to target-exercise readiness.

### Sprint L1.7B-MAP: Exit Ticket Skill-Metadata Alignment

Completed: 2026-05-26. Status: CLOSED PASS WITH FLAGS.

Position: after closed L1.7C-MATH; before L1.7B-P23, L1.7B-Q2, and any Scale
Gate 1 reliance on exit-ticket metadata.

Purpose:

Resolved the mismatch between the current `1.1.1` checkpoint metadata and the
paragraph-plan skills. Before this sprint, the generated checkpoint used
`A43`/`A04` as `targetSkillIds`/`skillScopeIds`, while the paragraph plan named
`B01` and `B02`. L1.7B-MAP changed the checkpoint-assessed route to `B01/B02`,
removed `A04`, recorded the target-exercise skill set as `A43/B01/B02`, and
set `targetReadinessEvidence: false`.

This sprint must preserve `specifications/product-end-state.md`: metadata
alignment is a prerequisite for later target-exercise-readiness evidence, not a
shortcut to diagnostics, mastery, sequencing, or scale claims.

Work:

- Audit the current checkpoint metadata route from platform source data to
  generated lesson output.
- Trace current metadata through platform source data, generated output,
  paragraph plan, target-exercise registry, and MTU/procedure registry.
- Decide the authoritative metadata route for exit tickets:
  paragraph-plan skills, MTU ids, target-exercise skills, or a reviewed
  mapping layer.
- Define a metadata contract covering visible task label, paragraph skill,
  MTU/procedure unit where available, target-exercise operation, and
  practice-route suggestion.
- If platform support is needed, hand off a precise platform request for
  B-unit skill-map scoping or a reviewed mapping layer.
- Add validation that no checkpoint can claim target-exercise readiness if
  metadata is unmapped.
- Add validation that no checkpoint can activate `Check` if target/scope
  metadata is invalid for the intended product role.
- Add tests or validation evidence that visible checkpoint tasks, source
  metadata, paragraph-plan skills, and target-exercise readiness records do not
  drift silently.
- Preserve the current rule that internal IDs must not appear in
  student-facing text.

Out of scope:

- target-exercise promotion
- diagnostics
- mastery decisions
- automatic sequencing
- summative use
- student-facing AI
- PV projection or PV machine promotion
- broad exit-ticket scaling

Exit criteria:

- the `A43`/`A04` versus `B01`/`B02` mismatch is fixed or represented by a
  reviewed mapping layer
- the accepted metadata route can support paragraph-plan skills and
  target-exercise-readiness evidence
- technical validation proves the route
- teacher-learning-quality review accepts the metadata route
- no student-facing internal-code leakage is introduced
- the closure record states whether exit-ticket metadata can be used as Scale
  Gate evidence or remains excluded

Closure result:

- human review closed PASS WITH FLAGS
- the metadata mismatch is fixed for the checkpoint's current paragraph-skill
  role
- current checkpoint metadata remains excluded from target-exercise-readiness
  and scale evidence
- readiness work is carried to `L1.7B-Q2`
- Scale Gate 1 may not rely on this checkpoint as target-readiness evidence

### Sprint L1.7C-MATH: Restore Skill-Tree Math Game + Four-Game Architecture Integrity

Completed: 2026-05-26. Status: CLOSED PASS WITH FLAGS.

Position: first in the pre-scale correction sequence; before Scale Gate 1 and
before any claim that the game row is aligned with the shared skill-map
architecture.

Purpose:

Restore the old `wiskundevaardigheden` skill-tree math game as the primary
`Rekenen` practice route. Keep `stappenplan` as support/step practice, not as
the replacement math game. This is a restoration/integrity sprint, not
cosmetic cleanup: the primary student math route currently points at the wrong
kind of product.

History finding:

- GAME-UX-1 implemented shared skill-map support and did not remove the old
  skill-tree math game.
- L1.7C reviewed `Stappenplan/Rekenen` as the current procedure-practice role
  and carried the missing full numeric calculation-engine flag.
- L1.7D then made `stappenplan` the primary `Rekenen` route when present and
  demoted `wiskundevaardigheden` to `Verdiep`.
- That route displacement is now a pre-scale defect.

Closure status on 2026-05-26:

- The platform landing generator now uses scoped `wiskundevaardigheden.html`
  as primary `Rekenen` when the paragraph declares concrete skill-tree skills.
- `1.1.2` and `1.1.3` now route primary `Rekenen` to the skill-tree math game.
- `stappenplan.html` remains visible as `Rekenstappen` support.
- `1.1.1` currently has an unscoped/full-catalog skill-tree file
  (`activeSkills: null`), so it is not promoted to primary `Rekenen`; it is
  available only as collapsed `Brede vaardigheidskaart`.
- Screenshot QA passed for the `1.1.2` landing, `1.1.2`
  `wiskundevaardigheden`, `1.1.2` reasoning game, and `1.1.3` graph game across
  desktop/mobile and light/dark.
- Technical QA is recorded in
  `archive/sprints/L1.7C-MATH/L1.7C-MATH-technical-qa-report.md` and
  `archive/sprints/L1.7C-MATH/L1.7C-MATH-validation-log.md`.
- First human review returned REVISE because the restored math-game result
  state could show `Volgende: A39`.
- The targeted fix now renders `Volgende: Prijsindex (CPI) berekenen`, removes
  visible dependency-node IDs, adds source regression tests, and adds
  post-exercise result screenshot QA.
- Focused human recheck closed PASS WITH FLAGS.
- Local screenshot evidence contains 17 files, including the post-result
  skill-tree screenshot.
- Carried flags: skill-tree stars/`route geoefend` language must remain
  practice-progress, restored math is not target-exercise-readiness evidence,
  keyboard/focus-order evidence should strengthen before scale, and scoped
  generated skilltree comments need cleanup.

Work:

- Review the audit in `archive/sprints/L1.7C-MATH/L1.7C-MATH-history-audit.md`.
- Use the platform handoff draft in
  `archive/sprints/L1.7C-MATH/L1.7C-MATH-platform-handoff.md` if generator
  changes are needed.
- Audit all four pieces together:
  - skill-tree math game;
  - reasoning game;
  - graph game;
  - shared skill-map / route-display layer.
- Update platform generator logic so scoped `wiskundevaardigheden.html` is the
  primary `Rekenen` route when it exists.
- Keep `stappenplan.html` visible as `Stappenplan`, `Extra steun`, or
  procedure-step practice.
- Re-check whether the skill-tree math game opens as a safe scoped calculation
  practice surface or an overloaded full catalog.
- For `Redeneren`, `Rekenen`, and `Grafieken`, prove that each game requests
  the correct aspect scope, does not default to the full catalog, can show the
  relevant skill tree or route, uses student-facing labels, and avoids
  diagnostics/mastery/sequencing/grade/summative/AI/PV claims.
- Add tests that the landing route points to `wiskundevaardigheden.html` when
  present, `stappenplan.html` remains visible as support, all three game types
  can access the shared skill-map route layer, full catalog is not the default
  student view, and internal IDs are not visible.
- Add screenshot/browser evidence for `1.1.2` landing with primary `Rekenen`
  restored, the `1.1.2` math skill-tree page after JS loads, a graph route, a
  reasoning route, and representative desktop/mobile/light/dark evidence.
- Regenerate through the platform workflow only.
- Review with student-experience and teacher-learning-quality evidence before
  closure.

Out of scope:

- deleting `stappenplan`
- generated-output hand patches
- diagnostics
- mastery decisions
- automatic sequencing
- summative use
- student-facing AI
- PV projection or PV machine promotion
- broad companion scaling

Exit criteria:

- `Rekenen` primary route points to scoped `wiskundevaardigheden.html` where
  available
- `Stappenplan` remains visible and usable as support
- Redeneren, Rekenen, and Grafieken all consume or expose the shared skill-map
  route language in the correct aspect scope
- the skill tree shown to a student is scoped to the relevant skill type by
  default
- the full catalog is not an accidental student default
- the four-part game/skill-map architecture is documented and reviewed
- technical validation and human review accept the restored route, or record
  the blocker before Scale Gate 1
- PASS WITH FLAGS is allowed only for issues outside the core game-row
  architecture; failure to restore the primary math route is REVISE/PAUSE, not
  a carry flag

### Sprint L1.7B-P23: Exit Ticket Target-Skill Checkpoint Designs For 1.1.2 And 1.1.3

Completed: 2026-05-28. Status: CLOSED PASS WITH FLAGS.

Position: after L1.7B-MAP and preferably after L1.7C-MATH if `1.1.2`
checkpoint practice links depend on the calculation route; before L1.7B-Q2
unless explicitly waived by human decision.

Purpose:

Create reviewed checkpoint designs or operational stop/handoff decisions for
`1.1.2 Percentages en indexcijfers` and `1.1.3 Grafieken en tabellen`. These
paragraphs introduce calculation/index and graph/table skills that the `1.1.1`
checkpoint does not test. This sprint may not produce weak MC-only checks
unless the paragraph target exercise is itself MC-like.

The checkpoint designs must cite `specifications/product-end-state.md` and show how each
checkpoint moves from current readiness toward target-exercise readiness, even
if the sprint closes with a platform handoff instead of generated output.

Current result:

- the operation-chain analysis is complete
- the current engine/UI is confirmed as choice-task-only
- no generated exit-ticket output was created for `1.1.2` or `1.1.3`
- shared task-type shell support is required before generated output
- human review accepted the stop/handoff decision as PASS WITH FLAGS

Work:

- Audit each paragraph's target exercise, paragraph plan, procedure contracts,
  and companion surfaces.
- Decompose each paragraph target exercise into the operation chain an exit
  ticket must probe.
- Define the exit-ticket operation chain for `1.1.2`, including calculation
  field, final answer field, and unit/percentage handling. It must cover
  selecting old/new values, calculating percentage change, calculating an
  index number, distinguishing index points from percentage change, and writing
  a final answer with percentage/index notation.
- Define the exit-ticket operation chain for `1.1.3`, including table-value
  selection, axis/graph reading, interpolation, or graph/table interpretation
  where relevant. It must cover table headings, row labels, column labels and
  units, economic axis conventions, value reading, interpolation between graph
  points, and graph/percentage claim judgement where the target exercise needs
  those operations.
- Identify UI changes needed for calculation and graph reading before building.
- Decide whether the current exit-ticket engine can support calculation field,
  final answer field, unit/percentage field, graph/table interaction, and short
  constructed response. If it cannot, stop and write a platform handoff instead
  of forcing everything into MC.
- Generate output only through the platform workflow.
- Keep `Check` hidden until a paragraph has reviewed generated checkpoint
  output.
- Stop if a `1.1.2` checkpoint would point students to an unresolved or
  displaced calculation route before L1.7C-MATH has restored or explicitly
  resolved the primary math game.

Out of scope:

- broad checkpoint scaling beyond `1.1.2` and `1.1.3`
- mastery or automatic progression claims
- summative grading
- student-facing AI
- PV projection or PV machine promotion

Exit criteria:

- `1.1.2` and `1.1.3` have reviewed checkpoint designs or a documented stop
  decision with platform handoff
- the checkpoint designs or stop decisions are based on target-exercise operation chains
- the sprint does not close with two MC-only checks that fail to cover the
  operation chains
- UI needs for calculation and graph/table reading are recorded
- student-experience and teacher-learning-quality review determine whether the
  checkpoint designs meet their target-skill probe specification or must pause for platform
  support

Closure result:

- L1.7B-P23 closed as a correct stop/handoff sprint
- no `1.1.2` or `1.1.3` generated checkpoint output was produced
- `Check` remains hidden for `1.1.2` and `1.1.3`
- shared task-type shell support is required before L1.7B-Q2 can produce
  target-equivalent proof for calculation or graph/table paragraphs
- target-exercise and MTU review flags for `1.1.2` and `1.1.3` remain live

### Sprint SPEC-ET-1: Exit Ticket Target-Equivalent Specification Correction

Completed: 2026-05-29. Status: closed PASS.

Position: after SYNC-4 made shared task-type UI part of the product end state;
before GAME-UX-3A, L1.7B-Q2, GATE-L1.7B-Q2, and Scale Gate 1 rely on exit
tickets.

Purpose:

Correct the stable product and companion specifications so the exit ticket is
the paragraph target-equivalent proof task, not merely a readiness-to-try
check.

Closure result:

- `specifications/product-end-state.md` now defines the exit ticket as a
  same-level task over the same target-exercise operation and answer-form
  chain
- `specifications/companion-core-specifications.md` now distinguishes
  checkpoint-only completion copy from `GATE-L1.7B-Q2` approved
  target-equivalent completion copy
- exam-ingestion end state is now tied to paragraph plan, explanation,
  practice route, skill-map route, shared task shell, exit ticket, answer
  model, and review gates
- no lesson output, engine code, protected reference mutation, target-exercise
  mutation, diagnostics, mastery, sequencing, summative use, AI, PV, Scale
  Gate 1, or student/product use was authorized

Records:

- `archive/sprints/SPEC-ET-1/SPEC-ET-1-sprint-plan.md`
- `archive/sprints/SPEC-ET-1/SPEC-ET-1-closure-log.md`

### Sprint EX-LESSON-1: Exam-Ingestion End-State Integration

Completed: 2026-05-30. Status: closed as route-trace handoff; no generated
output or product use authorized.

Position: after SPEC-ET-1 and before exam-target paragraph implementation,
L-EX0/L-EX1 reliance, or Scale Gate 1 reliance on official-exam target
exercises.

Purpose:

Turn the product-spec exam-ingestion end state into lesson-side build and gate
requirements. Official CvTE and CvTE-derived target exercises must trace
prompt, source annexes, figures/tables/graphs, correction model, point
allocation, answer-construction requirements, concepts, calculations,
graph/table/source operations, reasoning operations, and answer-writing
requirements into the paragraph plan, explanation, skill-map route, practice
route, shared task shell, exit ticket, and answer model.

Acceptance evidence:

- paragraph-plan checklist for exam-target paragraphs added to the platform
  paragraph-plan template
- gate checklist for official prompt/source/correction-model/answer-form trace
  recorded in the platform EX-LESSON-1 exam-target route checklist
- handoff requirements to platform exam-ingestion and answer-form systems
  recorded for GAME-UX-3A, L-EX0/L-EX1, L1.7B-Q2, GATE-L1.7B-Q2, and Scale
  Gate 1
- no generated output or protected reference mutation inside this sprint

Records:

- `archive/sprints/EX-LESSON-1/EX-LESSON-1-sprint-plan.md`
- `archive/sprints/EX-LESSON-1/EX-LESSON-1-closure-log.md`

### Platform Dependency GAME-UX-3A: Shared Task-Type UX Foundation

Completed: yes. Status: CLOSED RUNTIME FOUNDATION; live student-route proof
continues under `ENGINE-OP-1`.

Position: after MTU-H4C answer-form execution and EX-LESSON-1 route-trace
handoff, with SPEC-ET-1 target-equivalent semantics visible; before ENGINE-OP-1,
graph/math integration work, and L1.7B-Q2 target-equivalent implementation for
calculation or graph/table paragraphs.

Purpose:

Implemented the shared task-type shell described in
`specifications/product-end-state.md` and
`specifications/companion-core-specifications.md`. The shell serves exit
tickets, graph/table practice, math/calculation practice, exam-style
answer-form requirements, and later reasoning tasks where the student action
overlaps.

Required capabilities:

- numeric input with tolerance and rounding policy
- calculation/work capture
- final-answer entry
- unit or notation input for percent/index/index-point distinctions
- short constructed response with reviewed local answer model
- table-value selection
- graph reading with approximate/interpolated answers
- point placement or graph-construction substitute
- neutral feedback, retry, and self-check states
- screenshot QA and keyboard/focus QA hooks

Acceptance evidence:

- source-controlled task shell and validation support
- task-family fixtures for accepted task families
- focused platform tests for runtime validation and static UI rendering
- proof that the task shell can support target-equivalent exit tickets and
  checkpoint-only local checks without changing completion authority
- proof that exam-style answer-form requirements can be represented without
  forcing calculation, graph/table, or short-response work into choice-only
  form
- no internal MTU/operation codes in student-facing task labels
- no mastery, diagnostic, sequencing, summative, AI, PV, or product-use claims
- clear downstream handoff to ENGINE-OP-1 and the graph/math/checkpoint rows

Records:

- `archive/sprints/GAME-UX-3A/GAME-UX-3A-sprint-plan.md`
- `archive/sprints/GAME-UX-3A/GAME-UX-3A-closure-log.md`

Boundaries:

This dependency did not generate lesson output and does not authorize
diagnostics, mastery decisions, automatic
sequencing, grading or summative use, student-facing AI, PV projection, PV
machine promotion, target-exercise promotion, CP-6 or Year 1 closure, Scale
Gate 1, or broad companion scaling.

### Sprint ENGINE-OP-1: Four-Engine Operational Proof Audit

Completed: 2026-05-31. Status: closed audit evidence with flags.

Position: after GAME-UX-3A has enough task-shell behavior to inspect; before
SKILLMAP-OP-1, GRAPH-UX-2, MATH-UX-2, REASON-UX-2, and GATE-ENGINE-1.

Purpose:

Audit what students actually see and do across the shared skill-map route,
math game, graph game, reasoning game, and checkpoint route. This sprint must
not accept architecture-only proof.

Delivered evidence for `1.1.1`, `1.1.2`, and `1.1.3`:

- landing-page route trace
- opened route URL or surface
- visible skill-map state and skill subset
- game/task played
- feedback shown after a representative answer
- next-action copy
- desktop/mobile screenshots
- judgement on whether the route helps the student move toward the paragraph
  target exercise

Findings:

- `1.1.3` graph practice is the strongest current operational route and gives
  neutral source/value/calculation feedback.
- `1.1.2` math practice is restored and scoped.
- Generated output does not yet use the GAME-UX-3A task shell.
- `1.1.2` and `1.1.3` have no target-equivalent checkpoint route.
- Shared skill-map panels are empty or mis-scoped in several places.
- No implementation or generated-output mutation was performed inside the
  audit.

Records:

- `archive/sprints/ENGINE-OP-1/ENGINE-OP-1-sprint-plan.md`
- `archive/sprints/ENGINE-OP-1/ENGINE-OP-1-closure-log.md`

### Sprint SKILLMAP-OP-1: Student-Visible Skill-Map Route

Completed: no. Status: required after ENGINE-OP-1.

Position: after ENGINE-OP-1 identifies route visibility gaps; before graph,
math, reasoning, checkpoint, or Scale Gate reliance on the shared route layer.

Purpose:

Make the shared skill-map route visibly useful to the student. The student
should see the relevant skill subset, current paragraph target, recommended
next skill, route progress, and practice link without internal codes.

Required behavior:

- aspect-scoped route views for reasoning, calculation, graph/table, and
  checkpoint contexts
- recommended next skill shown in student language
- paragraph target shown without over-claiming mastery or diagnostics
- keyboard/focus, desktop/mobile, and light/dark proof
- screenshot and student-experience review evidence

### Sprint GRAPH-UX-2: Graph Game + Checkpoint UI Integration

Completed: 2026-05-31. Status: closed graph/table task-shell integration with
one non-blocking student-experience flag.

Position: after GAME-UX-3A and SKILLMAP-OP-1; before graph/table claims in
L1.7B-Q2 or Scale Gate 1.

Delivered:

- the generated Book 1 `1.1.3 Grafieken en tabellen` graph route loads and
  renders the GAME-UX-3A shared task shell
- the route covers table-value selection, graph reading, economic axis
  convention, interpolation, point placement, graph-construction substitute,
  calculation/work capture, and a less-labelled graph variant
- mobile ordering shows route, source, task shell, feedback, and next action
- checkpoint-style graph tasks are proven only as a non-published fixture with
  `targetReadinessEvidence: false`
- no `1.1.3` exit-ticket source/page was created and `Check` remains hidden

Records:

- `archive/sprints/GRAPH-UX-2/GRAPH-UX-2-sprint-plan.md`
- `archive/sprints/GRAPH-UX-2/GRAPH-UX-2-closure-log.md`

Carried flag:

- desktop first viewport can show route/source before task controls; this is a
  UI polish flag for later engine polish, not target-equivalent proof.

Boundaries:

GRAPH-UX-2 authorizes no target-equivalent completion language, diagnostics,
adaptive routing, mastery/sequencing, summative use, PV, Scale Gate 1, or
student/product use.

### Sprint MATH-UX-2: Math Game + Checkpoint UI Integration

Completed: yes. Status: closed live math/calculation task-shell integration.

Position: after GAME-UX-3A and SKILLMAP-OP-1; before calculation/index claims
in L1.7B-Q2 or Scale Gate 1.

Purpose:

Use the shared task shell for calculation operations. Produced one working
route for `1.1.2 Percentages en indexcijfers` showing the relationship between
the skill-map route, math practice, calculation feedback, and later
target-equivalent checkpoint work.

Required capabilities:

- numeric input
- calculation/work capture
- final-answer entry
- percentage/index notation
- units where relevant
- feedback on common calculation errors

Records:

- `archive/sprints/MATH-UX-2/`

Boundaries:

MATH-UX-2 authorizes no target-equivalent completion language, diagnostics,
adaptive routing, mastery/sequencing, summative use, PV, Scale Gate 1, or
student/product use.

### Sprint REASON-UX-2: Reasoning Game Variant And Feedback Upgrade

Completed: 2026-05-31. Status: closed reasoning task-shell integration proof;
not scale or target-equivalent proof.

Position: after ENGINE-OP-1 and answer-form MTU routing evidence; before
GATE-ENGINE-1.

Purpose:

Made `Redeneren` a richer practice engine by adding a shared task-shell
structured-reasoning self-check mode, preserving six dynamic modes, improving
repair feedback in existing modes, and keeping self-check completion out of
scored/persistent `goed` progress. Closure carries mobile feedback-density and
terse source-label flags to later engine/content work. No target-equivalent
completion, diagnostics, adaptive routing, mastery, summative use, PV, Scale
Gate 1, or student/product use was authorized.

### Sprint GAME-ARCH-1: Practice Engine Build-vs-Rebuild Decision

Completed: yes. Status: closed as a no-generated-output decision sprint.

Position: after ENGINE-OP-1 has audited the live route and before committing to
broad refactor or replacement work.

Purpose:

Decision: keep and harden the shared skill-map route, keep the shared task
shell as core architecture, keep/refactor the graph UI direction as the
reference pattern, refactor math around target-exercise operation chains,
refactor reasoning around answer-form and constructed-response standards, keep
the short check as an advisory local checkpoint, and keep the
target-equivalent exit ticket separate as a later proof task.

Exit criteria:

- decision record names keep/refactor/rebuild/hold per component
- GAME-ARCH-2 must define ownership, migration, validation, screenshot QA,
  short-check advice rules, target-operation coverage, and product-boundary
  checks before any code replacement starts

### Sprint GAME-ARCH-2: Integrated Practice Engine Architecture Plan

Completed: no. Status: required before GATE-ENGINE-1 can authorize scale.

Position: after GAME-ARCH-1; before GATE-ENGINE-1 and before L1.7B-Q2 relies
on the shared engine architecture.

Purpose:

Produce the canonical architecture for shared route layer, shared task shell,
graph/table module, math/calculation module, reasoning module, advisory short
check, and target-equivalent checkpoint composition. Define which current
engine files are kept, wrapped, deprecated, or rebuilt. Define state
ownership, feedback/focus ownership, short-check advice copy rules,
target-exercise operation-chain coverage requirements, and GATE-ENGINE-1 live
rendered-output proof.

Exit criteria:

- file-level keep/wrap/deprecate/rebuild list exists
- shared route/task-shell ownership is explicit
- short check remains advisory and separate from the target-equivalent exit
  ticket
- target-equivalent exit-ticket implementation remains with L1.7B-Q2 and
  GATE-L1.7B-Q2
- no generated output, diagnostics, adaptive routing, mastery, sequencing,
  summative use, AI, PV, Scale Gate 1, or product use is authorized

### Gate GATE-ENGINE-1: Four-Engine Operational Integration Review

Completed: no. Status: required before engine scale.

Position: after SKILLMAP-OP-1, GRAPH-UX-2, MATH-UX-2, REASON-UX-2,
GAME-ARCH-1, and GAME-ARCH-2; before L1.7B-Q2 or Scale Gate 1 relies on the
engine system.

Purpose:

Review live rendered output and student-path traces to decide whether the
shared skill-map, graph game, math game, reasoning game, advisory short check,
and target-equivalent checkpoint boundary operate as one coherent
student-facing route. The gate must explicitly decide keep/refactor/rebuild/
hold per component.

Required gate questions:

- Can a student see which skill they are practising and why it matters for the
  paragraph target?
- Does the correct practice engine open from the landing route?
- Does the task interaction fit the skill being practised?
- Does feedback help the student understand the local error and next action?
- Are keyboard/focus, mobile, light/dark, and screenshot QA sufficient?
- Should the team continue refactoring, rebuild one or more engines through a
  later plan, allow controlled production, or pause for roadmap correction?

### Sprint L1.7B-Q2: Exit Ticket Target-Equivalent Implementation

Completed: yes. Status: implemented target-equivalent candidate; local
completion language remains held for `GATE-L1.7B-Q2`.

Position: after L1.7B-MAP, L1.7C-MATH, L1.7B-P23, SPEC-ET-1, GAME-UX-3A, and
the relevant engine operational proof rows; before GATE-L1.7B-Q2.

Purpose:

Upgrade one paragraph checkpoint from a non-summative practice check into
target-equivalent proof. This restores the core product intent: the exit
ticket should test the same reviewed target-exercise operation and answer-form
chain at the same cognitive level, not merely answer a short recall check.

This sprint is the first required implementation of the `Check` layer described
in `specifications/product-end-state.md`.

Update 2026-06-01: Platform implemented the first candidate for
`1.1.2 Percentages en indexcijfers`. The generated output now has an
`Exit ticket` page and landing-card route, four reviewed task-shell tasks, local
feedback, desktop/mobile/dark screenshot evidence, and no target-equivalent
completion copy. Lead review round 1 returned REVISE for weak calculation-work
and D31 matching; round 2 passed after stricter work-text criteria, rejected
contradictory phrases, adversarial tests, and refreshed generated evidence.
The remaining carried flag is criterion sufficiency: `GATE-L1.7B-Q2` must
decide whether deterministic text-group matching is enough before approving
local paragraph-completion language.

Recommended first paragraph:

`1.1.2 Percentages en indexcijfers`, because it forces calculation input,
final-answer notation, percentage/index distinctions, and unit handling while
being technically simpler than graph drawing.

Work:

- Select one paragraph and name the target exercise and answer model.
- Decompose the target exercise into the operation chain the student must
  perform.
- Build checkpoint tasks that cover the complete reviewed operation and
  answer-form chain at the same cognitive level.
- Add answer types required by the paragraph: calculation field, unit field,
  reasoning step, graph/table interpretation, or short constructed response.
- Include calculation/work field, final answer field, percentage/index/unit
  field, and short explanation where needed for the chosen target exercise.
- Align metadata with paragraph-plan skills and target-exercise skills.
- Record answer-model alignment and teacher-learning-quality review.
- Preserve non-summative language and local practice feedback.

Out of scope:

- grades
- mastery decisions
- automatic progression or sequencing
- diagnostics
- summative assessment
- student-facing AI
- PV projection or PV machine promotion
- CP-6 or Year-1 closure

Exit criteria:

- checkpoint tasks cover the target-exercise operation and answer-form chain
  at the same cognitive level
- a student who completes the checkpoint correctly has demonstrated, locally
  and non-summatively, that they can complete the paragraph target exercise
- metadata alignment is accepted
- answer-model alignment is documented
- calculation/graph UI needs are met for the selected paragraph
- teacher-learning-quality review accepts the operation-chain coverage
- student-experience review accepts clarity and feedback
- PASS WITH FLAGS is allowed only for issues outside the target-equivalent
  specification; missing operation-chain coverage is REVISE/PAUSE

### Gate GATE-L1.7B-Q2: Exit Ticket Target-Equivalent Proof Review

Completed: no. Status: future required before target-equivalent completion
language.

Position: after L1.7B-Q2; before any checkpoint says a student has shown they
can complete the paragraph target exercise or may proceed to the final/target
exercise.

Purpose:

Decide exactly what the exit-ticket UI may say when all answers are correct.
The gate separates safe checkpoint-only completion language, local
target-equivalent paragraph-completion language, and prohibited mastery,
sequencing, grading, diagnostic, adaptive, or summative claims.

Allowed candidate language:

- `Je hebt deze check afgerond.` for checkpoint-only surfaces.
- `Je hebt laten zien dat je de eindopgave van deze paragraaf aankunt.` only
  for target-equivalent exit-ticket output approved by this gate.
- `Je kunt nu door naar de eindopgave.` only for target-equivalent
  exit-ticket output approved by this gate.
- `Je hebt deze paragraaf-check succesvol afgerond.` only for
  target-equivalent exit-ticket output approved by this gate.

Prohibited language unless a later explicit mastery/sequencing gate authorizes
it:

- `Je beheerst deze paragraaf.`
- `Je mag door naar de volgende paragraaf.`
- grade, score, pass/fail, diagnostic, mastery, automatic sequencing, AI,
  summative, PV, or promotion claims.

Exit criteria:

- completion-language policy exists
- UI copy examples are reviewed
- target-equivalent completion wording is allowed only for Q2-approved
  same-level proof tasks
- checkpoint-only surfaces remain limited to non-summative check-completion language
- Scale Gate 1 knows whether exit tickets are checkpoint-only or
  target-equivalent proof surfaces

### Sprint REV-STD-1: Core-Spec Review Standard Hardening

Completed: no. Status: required before Scale Gate 1.

Position: after the current correction sprints are planned; before Scale Gate
1 or any later review packet relies on `PASS WITH FLAGS` as a scale signal.

Purpose:

Update review packets, lead-review rules, and flag handling so a core
specification failure cannot be carried as an ordinary flag. A bounded scope is
allowed to be smaller in scope, but it must still meet its stated
specification. If the team deliberately ships a smaller product than the
original specification, the roadmap must name the sprint that restores the full
specified product.

Work:

- Define three flag levels:
  - `minor_carry_flag`: may remain after closure because it is outside the
    sprint core objective;
  - `scale_blocker`: may allow bounded-scope closure but blocks scale
    reliance;
  - `core_spec_failure`: must return REVISE, FAIL, or PAUSE.
- Update review-packet templates so every review includes:
  - original sprint specification;
  - non-negotiable requirements;
  - student-facing product role;
  - evidence inspected;
  - core-requirement checklist;
  - explicit distinction between bounded scope, controlled production, and scale-ready.
- Update lead-review rules:
  - PASS WITH FLAGS is forbidden if a non-negotiable requirement fails;
  - a flag carried across two consecutive sprints becomes a gate question;
  - a carried scale blocker cannot be ignored by the next scale gate;
  - technical QA cannot substitute for teacher-learning-quality review.
- Add a flag budget:
  - max 3 carried flags per sprint unless the lead review explains why more is
    not a PAUSE condition;
  - any flag touching primary student route, source-of-truth metadata,
    target-exercise readiness, or scale authorization is at least a
    `scale_blocker`.
- Apply the standard retroactively to L1.7C, L1.7D, L1.7B-R, GATE-L1.7B, and
  L2.0 so Scale Gate 1 inherits an explicit flag table.

Review verdict definitions:

- PASS: all core requirements are met; remaining issues are cosmetic or clearly
  outside scope.
- PASS WITH FLAGS: the product meets the sprint core specification and the
  flags do not affect the primary route, source-of-truth metadata,
  target-exercise readiness, or scale authorization.
- REVISE: required when the primary student route is wrong, the product
  implements a weaker product than specified, a core game/exit-ticket
  requirement is missing, or review depends on restricted scope-language to excuse a
  core failure.
- FAIL: required when student-facing output is misleading, output implies
  mastery/diagnosis/grading without authorization, generated output was
  hand-patched, or invalid source-of-truth metadata is visible or used for
  claims.
- PAUSE: required when the platform cannot support the requested product safely,
  the team cannot identify the source of truth, or a fix requires a platform
  architecture decision.

Exit criteria:

- future review packets separate core specification from optional improvement
- PASS WITH FLAGS cannot hide core failure
- Scale Gate 1 has an explicit inherited-flag table
- review agents are instructed to compare output against the original
  specification, not only the current bounded-scope framing

### Sprint L1.7C-0: Shared Skill-Map Engine Contract

Completed: 2026-05-23.

Position: closed as the contract prerequisite for L1.7C. Platform
implementation support is now completed as `GAME-UX-1`.

Purpose:

Define one shared skill-map / skill-tree engine for the game row. This is not a
fourth game. It is the common route, progression, filtering, recommendation, and
state-display layer used by `Redeneren`, `Rekenen`, and `Grafieken`.

Architecture:

- Shared support engine: skill-map engine for progression display, aspect
  filtering, recommendations, prerequisites, locked/open/completed states,
  stars/progress, compact route display, dependency route display, and full
  tree display.
- Practice engines: reasoning game, calculation game, and graphical game remain
  separate practice engines.
- Exit ticket may use the shared engine only in compact checkpoint mode.
- Landing pages may use the shared engine only to expose scoped routes, not a
  full unfiltered catalog by default.

Modes:

- `compact`: one recommended skill plus a small set of available skills; locked
  skills hidden or collapsed.
- `route`: recommended path for the active aspect/game, with prerequisites
  shown only as route context.
- `full`: complete skill map for advanced, teacher-facing, or debug view only.

Aspect filters:

- `reasoning`: reasoning, verbal, causal, and procedure-selection skills.
- `calculation`: calculation, formula, unit, and answer-field skills.
- `graphical`: graph, table, source-value, visual interpretation, and axis
  skills.
- `mixed`: combined view only when explicitly requested by a teacher-facing,
  advanced, or checkpoint context.

Work:

- Inventory current skill-tree/progression UI assumptions from the existing
  game row and exit-ticket prototype.
- Define the shared engine contract: input data, display modes, aspect filters,
  state names, progress/stars semantics, keyboard expectations, mobile/dark
  expectations, and handoff API for each practice engine.
- Define the primary affordance: `Start oefenen` / `Ga verder`.
- Define secondary affordances: skill info, dependency route, goal path, and
  full tree view.
- Define how each practice engine requests a scoped skill route.
- Define how exit ticket requests compact checkpoint mode.
- Define how landing pages reference the shared route without becoming a card
  dump or full catalog.

Out of scope:

- implementing adaptive diagnostics
- mastery decisions
- automatic sequencing
- grading or summative use
- student-facing AI
- PV projection or PV machine promotion
- broad game-row or paragraph production

Exit criteria:

- shared skill-map engine contract exists
- aspect filtering exists for reasoning, calculation, and graphical skills
- compact mode shows recommended/available skills without exposing the full
  catalog
- route and full modes are defined, with full mode restricted to advanced,
  teacher-facing, or debug view
- all three games can request a scoped skill-map view
- exit ticket compact checkpoint use is specified
- no product-use boundary is weakened
- mobile, dark-mode, and keyboard accessibility expectations are defined before
  implementation

Outcome:

- Current skill-tree audit completed. The platform already has paragraph,
  chapter, and all-skill/module views, local stars, next-skill logic, and
  landing-page aspect metadata, but it lacks the aspect-filtered shared route
  contract needed by the three games.
- Contract accepted: three practice engines plus one shared skill-map engine.
- Modes accepted: `compact`, `route`, and restricted `full`.
- Aspect filters accepted: `reasoning`, `calculation`, `graphical`, and
  explicit `mixed`.
- State/progress semantics accepted as local practice progress only; no mastery,
  diagnostic, grading, or automatic sequencing claim.
- Exit-ticket use accepted only as compact checkpoint mode.
- Landing-page use accepted only as scoped route previews, not a full catalog or
  artifact/card dump.
- Platform handoff recorded for `GAME-UX-1`.
- Platform implementation completed in `GAME-UX-1` commit `6509895`, tag
  `checkpoint/GAME-UX-1-shared-skill-map-engine`.

Records:

- `archive/sprints/L1.7C-0/L1.7C-0-sprint-plan.md`
- `archive/sprints/L1.7C-0/L1.7C-0-current-state-audit.md`
- `archive/sprints/L1.7C-0/L1.7C-0-shared-skill-map-contract.md`
- `archive/sprints/L1.7C-0/L1.7C-0-handoff-to-platform.md`
- `archive/sprints/L1.7C-0/L1.7C-0-validation-log.md`
- `archive/sprints/L1.7C-0/L1.7C-0-closure-log.md`

### Sprint L1.7C: Three-Aspect Game Quality Upgrade

Completed: 2026-05-24.

Position: closed PASS WITH FLAGS after L1.7C-0 and platform GAME-UX-1; before
broad game-row scaling.

Purpose:

Upgrade the second-row skill-practice games: `Redeneren`, `Rekenen`, and
`Grafieken`. L1.5G-D proved the routing layer exists; L1.7C must decide whether
the games themselves are good enough to repeat across many paragraphs. The
three games remain separate practice engines and must consume the shared
skill-map contract from L1.7C-0 rather than inventing three separate skill-tree
UIs.

L1.7C records:

- `archive/sprints/L1.7C/L1.7C-sprint-plan.md`
- `archive/sprints/L1.7C/L1.7C-game-row-quality-rubric.md`
- `archive/sprints/L1.7C/L1.7C-game-row-quality-matrix.md`
- `archive/sprints/L1.7C/L1.7C-game-row-baseline-audit.md`
- `archive/sprints/L1.7C/L1.7C-technical-qa-report.md`
- `archive/sprints/L1.7C/L1.7C-validation-log.md`
- `archive/sprints/L1.7C/L1.7C-human-review-packet.md`
- `archive/sprints/L1.7C/L1.7C-student-experience-review.md`
- `archive/sprints/L1.7C/L1.7C-teacher-learning-quality-review.md`
- `archive/sprints/L1.7C/L1.7C-human-review-record.md`
- `archive/sprints/L1.7C/L1.7C-lead-review-summary.md`
- `archive/sprints/L1.7C/L1.7C-screenshots/`
- `archive/sprints/L1.7C/L1.7C-closure-log.md`

Technical state:

- Book 1 was regenerated through the platform workflow.
- `Redeneren`, `Rekenen/Stappenplan`, and `Grafieken` now load the shared
  skill-map route stack.
- Each game shows a compact scoped route panel rather than an unfiltered full
  catalog.
- §1.1.3 `Grafieken` has one less-labelled `Broodjesverkoop` line-chart
  variant with y-axis ticks.
- Green validation: deploy/link/data checks, complete student-web validation
  for `1.1.1`-`1.1.3`, procedure contracts 341 checks, Book 1 health 26/26,
  v5 target-exercise counts 54 with 12/12/14/16, full platform Jest 543 passed
  / 8 skipped.
- First human review found one closure blocker: visible route focus text could
  expose internal skill IDs such as `A61`.
- Targeted fix: route UI now renders the student-facing skill label, focused
  Jest has an `A61` regression, landing-page route intro copy is generated from
  available route tiles, and route-panel screenshots are recorded.
- Focused human recheck accepted the targeted fix and closed L1.7C as PASS WITH
  FLAGS.

Work:

- Produce a reusable game-row quality rubric that includes skill-map clarity.
- Use the L1.7C-0 shared skill-map contract as the baseline for every game-row
  decision.
- Use platform `GAME-UX-1` commit `6509895` as the runtime baseline.
- Deploy/regenerate affected lesson shared runtime and game surfaces through the
  platform workflow before judging student-facing behavior.
- Give each game a scoped skill route: reasoning/verbal, calculation, or
  graph/table/visual.
- Review each game for student experience, teacher-learning quality, feedback
  quality, scaffolding, final-challenge behavior, mobile/dark rendering, replay
  value, clear success states, scoped skill-map behavior, and alignment with
  MTU/procedure/visual records where available.
- Remove answer-revealing defaults, generic feedback, unsafe auto-correct
  behavior, unclear success states, and unfiltered all-skill views.
- Graph game: add at least one harder variant with less direct value labeling.
- Calculation game: support calculation field, answer field, and unit where
  relevant.
- Reasoning game: test causal/procedural reasoning construction rather than only
  recognition.
- Keep PV/adaptive boundaries explicit.

Out of scope:

- adaptive diagnostics
- mastery/sequencing
- student-facing AI
- summative use
- PV projection or PV machine promotion
- broad paragraph production

Closure result:

- game-row rubric exists and is reusable
- each of the three games has a disposition: PASS WITH FLAGS for controlled
  pilot use
- each game consumes the shared skill-map contract with a scoped aspect route
- any MVP flags are visible and classified
- focused tests, screenshot QA, and student/teacher review evidence support the
  verdict
- lead review closes L1.7C as PASS WITH FLAGS.

### Sprint L1.7D: Paragraph Landing Page Information Architecture Cleanup

Completed: 2026-05-24.

Position: closed PASS WITH FLAGS after L1.7C; before L2.0, L1.7B-R,
GATE-L1.7B, and Scale Gate 1.

Purpose:

Prevent product sprawl. The paragraph landing page must become a controlled
learning route rather than a card dump as the companion set grows.
It must consume the shared skill-map/game architecture so the second-row games
expose consistent scoped skill routes instead of three separate skill-tree UIs
or a full unfiltered catalog.

Proposed primary route:

1. Start hier / voorkennis
2. Uitleg vaardigheden
3. Begeleide inoefening
4. Oefen in drie richtingen: Redeneren, Rekenen, Grafieken
5. Exit ticket

Secondary or expandable:

- Samenvatting
- Nieuws met visual
- Presentatie
- Lesboek
- Downloads and teacher-facing assets

Work:

- Define primary, secondary, collapsed, advanced, teacher-facing, and
  download-only surfaces.
- Limit the default visible card set.
- Group student tasks as start, learn, practise, check, and deepen.
- Consume the shared skill-map/game architecture for the game row and exit
  ticket route.
- Keep the full skill-tree/catalog view out of the default student landing page.
- Remove or demote redundant surfaces before scaling.
- Implement through platform landing-page generators only.
- Validate desktop/mobile, light/dark, keyboard navigation, and cognitive-load
  clarity.

Out of scope:

- one-off hand patches to generated landing pages
- adding new companion features beyond route/IA decisions
- adaptive routing or diagnostics
- mastery/sequencing
- student-facing AI
- summative use
- PV projection or PV machine promotion

Exit criteria:

- landing-page information architecture contract exists
- landing-page contract references the shared skill-map/game architecture
- generator implements the default visible/collapsed/teacher-download hierarchy
- a representative built paragraph passes visual QA and review
- route labels and card hierarchy are clear enough for students

### Sprint L2.0: Book 1 Flag Burn-down And House-Style Cleanup

Completed: 2026-05-25.

Position: closed after L1.7A, L1.7B-C, L1.7C-0, L1.7C, and L1.7D; before
L1.7B-R, GATE-L1.7B, Scale Gate 1, or any broad companion scaling.

Purpose:

Clean the easy and visible flags from the first three built paragraphs and
turn `1.1.1` through `1.1.3` into a trustworthy Book 1 student-web house-style
baseline.

Closed state:

- `archive/sprints/L2.0/` now contains the sprint plan, baseline audit,
  house-style baseline, flag disposition, quality-ref status standard,
  validation log, technical QA report, human-review packet, student-experience
  review, teacher-learning-quality review, human-review record, lead-review
  summary, closure log, and screenshot evidence.
- Platform generator now routes `Gemengde opgaven` consolidation pages to
  `Oefen gemengd` when exercise/answer output exists.
- `1.1.4 Gemengde opgaven` and the Chapter 1.1 landing page were regenerated
  through the platform workflow.
- Human review closed PASS WITH FLAGS with no product blocker.
- Carried flags remain for `1.1.4` legacy `FLAG`, graph-drawing consolidation,
  profit-formula framing, numeric calculation-engine work, graph/reasoning
  variants, exit-ticket implementation, and Scale Gate 1 QA sampling.

Work:

- Keep the L-CP6E `1.1.3` Part A figure-numbering fix as current evidence and
  decide the remaining duplicated worked-example policy.
- Decide whether duplicated worked examples in `opgaven.md` are intentional
  standalone-document support or unnecessary bloat.
- Review whether `1.1.1`, `1.1.2`, and `1.1.3` quality refs use consistent
  status language.
- Define what `PASS WITH FLAGS` means operationally for pilot, release, and
  scaling decisions.
- Create a concise Book 1 student-web house-style baseline from the first three
  built paragraphs.
- Classify L1.7C carried game-row flags as fix-before-scale, carry into
  controlled production, or defer:
  - `Rekenen` is not yet a full numeric calculation engine.
  - `Grafieken` has only one less-labelled variant.
  - `Redeneren` needs richer variants and replay value.
  - reusable game screenshot QA should mature.
- Define landing-page route rules after L1.7D, including that `Check` remains
  hidden until reviewed non-summative exit-ticket output exists.
- Define an exit-ticket readiness checklist for L1.7B-R.
- Define screenshot/QA expectations for future paragraph builds.

Out of scope:

- new companion/game features
- adaptive behavior
- target-exercise distribution audit
- broad paragraph production

Exit criteria:

- each easy visible Book 1 flag has a decision or fix
- house-style baseline exists and references the actual built paragraphs
- PASS WITH FLAGS operational definition exists
- game-row carried flags are classified as fix-before-scale, carry, or defer
- exit-ticket readiness checklist exists
- landing-page `Check` activation rule is explicit
- quality-ref status language standard exists
- screenshot/QA expectations exist
- Book 1 health remains green
- no generated lesson output is hand-patched

### Sprint L1.5P: Boek 1 Print-Edition Cut + 2026/27 12-Paragraph Scope

Completed: 2026-05-18.

Position: closed urgent production sprint. Publisher hand-off print scope is
now generated; L1.5Q owns the broader curriculum-source update.

Purpose:

Make printed Book 1 fit the new 2026/27 scope before publisher hand-off. This
is not just "remove the test chapter from print" anymore. Printed Book 1 must
become a 12-paragraph book: supply and demand foundations only, with test
preparation available online and cost/revenue/marginal-analysis material parked
for later books.

Current baseline checked before this roadmap update:

- `Boek 1 ... boek.md` still says the book has five chapters and presents the
  final chapter as test preparation.
- `1.3 Hoofdstuk Aanbod en kosten/_chapter-plan.md` still includes
  kostenstructuren, opbrengsten, winst/verlies, and break-even.
- `course_blueprint_v4.md` still uses the old four-theory-chapters plus
  test-preparation-chapter structure and two test moments per book.

New print scope:

| New print slot | Source today | Action |
| --- | --- | --- |
| 1.1.1 Schaarste en economisch denken | existing 1.1.1 | keep |
| 1.1.2 Percentages en indexcijfers | existing 1.1.2 | keep |
| 1.1.3 Grafieken en tabellen | existing 1.1.3 | keep |
| 1.1.4 Gemengde opgaven | existing 1.1.4 | keep |
| 1.2.1 Individuele vraag | existing 1.2.1 | keep |
| 1.2.2 Vraagfactoren | existing 1.2.2 | keep |
| 1.2.3 Van individuele naar collectieve vraag | existing 1.2.3 | keep |
| 1.2.4 Gemengde opgaven | existing 1.2.4 | keep |
| 1.3.1 Aanbod | existing 1.3.1 | keep |
| 1.3.2 Marktevenwicht | current 1.4.1 | move or alias into new chapter 1.3 |
| 1.3.3 Verschuivingen en nieuw evenwicht | current 1.4.2 | move or alias into new chapter 1.3 |
| 1.3.4 Gemengde opgaven | revised from current mixed material | rewrite so it only covers supply, demand, equilibrium, and shifts |

Material removed from Book 1 print:

| Current material | New status |
| --- | --- |
| 1.3.2 Kostenstructuren | move to new Book 2 |
| 1.3.3 Opbrengsten | move to new Book 2 |
| 1.4.3 Marginale kosten en marginale opbrengsten | move to new Book 2 |
| 1.4.4 Winstmaximalisatie | move to new Book 3 |
| 1.4.5 Gemengde opgaven | partially reusable, but not as-is |
| 1.5 Toetsvoorbereiding | website-only |

Required work:

- Write an operational L1.5P sprint plan before implementation, with generated
  output files named explicitly.
- Update the book assembly, TOC, preface, chapter pages, and print profile so
  the printed binding has exactly 12 count-bearing paragraphs.
- Make the student-facing message simple: "De toets gaat over Boek 1."
- Move test-preparation references to website-only language; do not present
  them as a printed chapter.
- Keep every cut item reachable online, archived, or recorded for migration to
  a future book.
- Do not delete useful material as part of the print cut.
- Run the platform book build/validation workflow; no hand-patched generated
  lesson output.

Out of scope:

- Full Book 2/3 migration of cut material.
- Companion/game/PV semantics work.
- Global target-exercise distribution audit.
- Cramming removed theory into oversized Book 1 paragraphs.

Exit criteria:

- Book 1 print PDF contains 12 content paragraphs only.
- The book-level TOC no longer lists the test-preparation chapter as a printed
  chapter.
- The preface says test preparation is available online.
- All removed/cut content has a survival route: online, archive, or future
  Book 2/3 migration.
- `check:book` and relevant publisher-print validators pass.
- The closure log records the exact generated outputs and validation commands.

Closure evidence:

- L1.5P first closed, then independent lead review returned REVISE because the
  TOC was clean but the generated body still had duplicate opgaven and excluded
  print-scope leakage.
- The correction pass strengthened the print-scope validator to scan visible
  body/back matter and duplicate `## Opgaven` sections.
- Final green gates: strengthened print-scope checker 12/12, `check:book`
  26/26, focused print-scope Jest 5/5, full platform Jest 502 passed / 8
  skipped, markdown/PDF excluded-term scans clean.
- Review and correction record: `archive/sprints/L1.5P/L1.5P-lead-review-record.md`.

### Sprint L1.5Q: Course Blueprint v5 + Four Test-Week Book Plan

Completed: no.

Position: after L1.5P. This is a curriculum-source sprint, not part of the
urgent publisher cut.

Purpose:

Create the authoritative v5 blueprint for the new four-book, four formal
test-week structure. The old v4 blueprint says each book has four theory
chapters plus a printed test-preparation chapter and two test moments per book;
that is no longer the intended planning model.

New principle:

Each formal test week corresponds to one book. The student-facing message is:
"The test is about this book." Test-preparation material remains available
online, but it is not part of the printed book binding and does not count toward
the theory/gemengde-opgaven paragraph budget. Optional mid-book checks may
exist as formative diagnostics or web quizzes, not as separate printed-book
units or formal test-week scopes.

Deliverables:

- `course_blueprint_v5.md`, created as a new versioned source file instead of
  silently overwriting v4.
- A four-book table of contents with paragraph counts 12 / 12 / 14 / 16.
- A test-week mapping: test week 1 -> Book 1, test week 2 -> Book 2, test week
  3 -> Book 3, test week 4 -> Book 4.
- A migration table for paragraphs moved out of Book 1 and for later
  government-intervention, monopoly, market-failure, inflation, and macro
  shifts.
- A source-of-truth update path for
  `4veco-platform/references/authored/course-target-exercises.json`, which
  currently identifies itself as blueprint version v4 and points to
  `references/owned/course-blueprint-v4.md`.

Acceptance criteria:

- The new blueprint has exact count-bearing paragraph counts: 12 / 12 / 14 /
  16.
- Test-preparation chapters are marked as web-only packages, not printed
  chapters.
- Every count-bearing paragraph has a target exercise or a target-exercise
  placeholder.
- No theory is crammed into oversized paragraphs just to meet the count.
- The prerequisite chain is rechecked after the moves.
- The platform-side target-exercise reference no longer points ambiguously to
  an obsolete v4 plan if v5 is now authoritative.

### Sprint L2.1: Book 1 Release Polish

Completed: no.

Purpose:

Do a teacher-facing review pass on Book 1 while keeping the health gate green.

Work:

- clarity
- pacing
- graph readability
- answer model usability
- exam fit

Rules:

- Keep all five chapter validators passing.
- Keep all paragraph validators passing in Part A mode.
- Any repeated manual fix should become a checklist item or a platform improvement request.

### Sprint L2.2: Book 2 Part A Textbook Layer

Completed: no.

Purpose:

Build Book 2 Part A with hard gates, after L1.5Q clarifies the v5 blueprint,
paragraph migration, and target-exercise source-of-truth path.

Required gates:

- `_chapter-plan.md`
- paragraph markdown files
- SVG/PNG pairs
- PDFs
- review files
- quality refs
- chapter assembly
- chapter validation

Book 2 should prove that the Book 1 Part A workflow is repeatable, not just a one-off success.

### Sprint L-EX0: Exam-Target Paragraph Contract

Completed: no.

Position: future contract sprint before L2.4-TEA and before any exam-target
paragraph production.

Purpose:

Define how the lesson team builds a paragraph when the target exercise is an
official exam question rather than a clean owned target exercise.

This contract must apply `specifications/product-end-state.md` to official
exam-target work: every lesson surface traces back to the official question,
source annexes, correction model, and answer-operation chain.

Inputs:

- platform exam-ingestion overlay or explicitly bounded EX-0 substitute
- official question prompt
- source annexes / figures / tables
- official correction model
- MTU decomposition
- graph/source/answer-operation requirements

Outputs:

- updated paragraph-plan contract for exam-target paragraphs
- one dry-run paragraph plan, no full production required
- review checklist for exam-target paragraphs
- handoff requirements back to platform when source annexes, answer-model
  steps, graph objects, operations, or MTUs are missing

Exit criteria:

- a reviewer can trace every official answer-model step to something taught,
  practised, scaffolded, or deliberately assumed
- no generated lesson output is hand-patched
- no broad companion scaling is authorized by this sprint
- diagnostics, adaptive routing, mastery, sequencing, student-facing AI, and
  summative use remain blocked

### Sprint L-EX1: Exam-Target Paragraph Pilot

Completed: no.

Position: future controlled pilot after L-EX0.

Purpose:

Build one paragraph around a real official exam question using platform
exam-ingestion data, source annexes, official answer-model decomposition, MTU
mapping, and companion visual/answer-model gates.

The pilot must preserve the `specifications/product-end-state.md` distinction
between a published paragraph, a companion pilot, target-exercise-readiness
evidence, and scale readiness.

Pilot focus:

- Part A: theory, worked example, opgaven, and answer model prepare the exact
  official question.
- Part B: uitleg vaardigheden, presentation, guided practice, and games repeat
  the same procedure and answer-construction route.
- Visual QA: all source tables, graphs, and figures required by the official
  question appear where students need them.
- Answer-model QA: the paragraph teaches students to produce the answer in the
  way the correction model rewards.

Exit criteria:

- one controlled paragraph passes exam-target review gates
- every answer-model operation is taught, practised, scaffolded, or justified
  as prior knowledge with MTU evidence
- carried flags are explicit
- no broad production or target-exercise distribution audit is authorized

### Sprint L2.4-TEA: Target Exercise Distribution Audit

Completed: no.

Position: future quality sprint after L1.7A and after the micro-teaching-unit
layer plus companion-quality review instruments are mature enough to support
reliable judgement.

Purpose:

Evaluate whether target exercises are well distributed across the new four-book
structure, with the right lesson load, prerequisite chain, aspect balance, and
test-week progression. Do not execute this audit during L1.5P or L1.5Q; doing
it now would mostly be subjective judgement without enough built-paragraph and
review evidence.

Inputs:

- `course_blueprint_v5.md`
- `course-target-exercises.json`
- `micro-teaching-units.json`
- paragraph plans
- built Part A paragraphs
- built Part B companion materials where available
- teacher-learning-quality review
- student-experience review
- classroom pacing evidence if available

Audit questions:

- Does each paragraph have one dominant target skill rather than three
  competing skills?
- Is the target exercise realistic for one lesson plus homework?
- Are reasoning, calculation, and graphical representation distributed
  sensibly?
- Are prerequisites actually taught before they are required?
- Are some paragraphs too light while others silently carry two lessons of
  work?
- Do gemengde opgaven consolidate rather than introduce new theory?
- Does each book form a coherent test-week scope?

Outputs:

- target-exercise audit report
- list of paragraphs to keep, split, move, or replace
- recommended updates to the target-exercise registry
- recommended micro-teaching-unit changes
- no mass rewrite unless the evidence supports it

## Lessen Team Deliverables

### Next 1 Week

- Keep Book 1 green.
- Use the L1.5P print PDF as the current publisher-print baseline.
- Use `specifications/product-end-state.md` as the north-star baseline for
  target-equivalent proof, route, and completeness claims.
- Treat `GATE-MTU-H4` through `MTU-H4C` as closed platform answer-form
  prerequisites. MTU-H4C added the bounded answer-form units but kept them
  generator-blocked/non-interactive, with no lesson output or product exposure.
  EX-LESSON-1 has supplied the exam-target route-trace handoff. GAME-UX-3A has
  supplied the shared task-shell runtime foundation without generated lesson
  output or product exposure. `ENGINE-OP-1` has audited live output and found
  route panels empty or mis-scoped, generated task-shell use absent, and
  missing `1.1.2`/`1.1.3` target-equivalent checkpoint routes. `SKILLMAP-OP-1`
  has since closed route-visibility proof, `GRAPH-UX-2` has closed
  graph/table task-shell integration, `MATH-UX-2` has closed
  math/calculation task-shell integration, `REASON-UX-2` has closed
  reasoning task-shell integration, `GAME-ARCH-1`/`GAME-ARCH-2` have
  closed architecture decision and planning, `GATE-ENGINE-1` has closed the
  operational integration review, `GRAPH-REFINE-1` has closed graph
  operation-chain planning with a target-chain repair flag, and
  `MATH-REFINE-1` has closed math operation-chain planning with a D31
  target-chain repair flag, and `REASON-REFINE-1` has closed reasoning
  answer-form planning with generic-self-check, held-lane, D31 coordination,
  and A81/source-use repair flags. The remaining active operational
  dependencies are `CHECK-Q2-PLAN`, and later `L1.7B-Q2`/`GATE-L1.7B-Q2`.
- Use the closed L1.7B-R and GATE-L1.7B records as input only for the current
  checkpoint product boundary. They do not prove target-equivalent completion.
- Preserve the L1.7C-MATH closure: primary `Rekenen` is restored to the
  skill-tree math game where scoped, while `stappenplan` remains support.
- Preserve the remaining L1.7C, L1.7D, L2.0, L1.7B-R, GATE-L1.7B,
  L1.7C-MATH, and L1.7B-MAP carried flags: game-row scaling flags remain
  classified, `Check` remains visible only for reviewed checkpoint output, the
  current `1.1.1` checkpoint is not target-equivalent proof evidence, and
  `1.1.4` content/quality-ref flags remain future review work.
- Use the L2.0 exit-ticket checklist, GATE-L1.7B carried flags,
  L1.7C-MATH closure flags, L1.7B-MAP metadata contract, L1.7B-P23 platform
  handoff, GATE-MTU-H4 through MTU-H4C closure conditions, SPEC-ET-1
  target-equivalent proof standard, EX-LESSON-1 route-trace handoff, GAME-UX-3A
  runtime foundation, ENGINE-OP-1 operational audit, SKILLMAP-OP-1
  route-visibility proof, GRAPH-UX-2 graph/table task-shell integration,
  MATH-UX-2 math/calculation task-shell integration, REASON-UX-2 reasoning
  task-shell integration, GAME-ARCH-1 architecture decision, GAME-ARCH-2
  architecture plan, GATE-ENGINE-1 operational integration closure,
  GRAPH-REFINE-1 graph operation-chain findings, MATH-REFINE-1 math
  operation-chain findings, REASON-REFINE-1 reasoning answer-form findings,
  and the SYNC-4 shared
  task-shell specification as entry conditions for the remaining
  planning/preparation lanes and later Q2 work.
- Keep L1.5Q/v5 as the active curriculum-source baseline, but do not treat
  migrated target exercises as final-reviewed.
- Continue companion controlled-scope work only where it supports the L1.7A
  decision, the closed L1.7B-C/L1.7C-0/L1.7C/L1.7D/L2.0/L1.7B-R/GATE-L1.7B/
  L1.7C-MATH/L1.7B-MAP/L1.7B-P23/SPEC-ET-1/EX-LESSON-1/GAME-UX-3A/ENGINE-OP-1/SKILLMAP-OP-1/GRAPH-UX-2/MATH-UX-2/REASON-UX-2/GATE-ENGINE-1/GRAPH-REFINE-1/MATH-REFINE-1/REASON-REFINE-1/CHECK-Q2-PLAN/L1.7B-Q2/GATE-L1.7B-Q2/L1.7B-Q2-COPY/L1.7B-Q2-D31-STRUCT/SYNC-PRODUCT-1/CHECK-SHORT-EXIT-1/STANDARD-EXERCISES-1/TASK-SHELL-UX-2/TASK-FAMILY-CHOICE-1/TASK-FAMILY-CONSTRUCT-1/TASK-FAMILY-CLOZE-TILE-1 foundation, and the open Product Proof Track:
  TASK-FAMILY-SENTENCE-1,
  TASK-FAMILY-FORMULA-1, TASK-FAMILY-CLOZE-1, TASK-FAMILY-MULTI-1,
  TASK-FAMILY-ORDER-1, TASK-FAMILY-SOURCE-1, TASK-FAMILY-LABEL-1,
  TASK-FAMILY-MATCH-1, TASK-FAMILY-TWO-TIER-1, TASK-FAMILY-ASSERTION-1,
  GATE-TASK-FAMILY-1, GAME-ROUTE-AFFORDANCE-1,
  SKILLMAP-PRODUCT-1, REASON-STD-1, DUAL-CODING-STD-1, ENGINE-UNIFY-1,
  CHECK-SHORT-EXIT-2, SCALE-PROOF-3P, GATE-PRODUCT-3P, and REV-STD-1; or
  does not conflict with source-of-truth decisions.
- Hand platform-owned UI integration work back to the platform team instead of patching generated files.
- Keep Book 2 Part A planning paused behind L1.5Q if it depends on the new
  course structure.

### Next 2-4 Weeks

- Use the L1.7A readiness decision, L1.7B-C contract-and-stop outcome,
  L1.7C-0 shared skill-map contract, L1.7C game-row closure, L1.7D landing IA
  closure, L2.0 house-style closure, L1.7B-R/GATE-L1.7B checkpoint-boundary
  closure, L1.7C-MATH math-route restoration, and L1.7B-MAP metadata alignment
  closure as the baseline. L1.7B-R and GATE-L1.7B have closed only a
  non-summative checkpoint boundary; L1.7B-MAP fixed metadata only; L1.7B-P23
  accepted a stop/handoff; SPEC-ET-1 corrected the exit-ticket end-state
  standard; EX-LESSON-1 supplied the exam-target route-trace handoff; and
  GAME-UX-3A supplied the shared task-type runtime foundation. ENGINE-OP-1
  and SKILLMAP-OP-1 have since closed operational proof and visible-route
  work. GRAPH-UX-2, MATH-UX-2, and REASON-UX-2 have since closed graph/math/
  reasoning task-shell integration proof. GATE-ENGINE-1, GRAPH-REFINE-1,
  MATH-REFINE-1, REASON-REFINE-1, CHECK-Q2-PLAN, L1.7B-Q2,
  GATE-L1.7B-Q2, L1.7B-Q2-COPY, L1.7B-Q2-D31-STRUCT,
  SYNC-PRODUCT-1, CHECK-SHORT-EXIT-1, STANDARD-EXERCISES-1, TASK-SHELL-UX-2,
  TASK-FAMILY-CHOICE-1, TASK-FAMILY-CONSTRUCT-1, and
  TASK-FAMILY-CLOZE-TILE-1 have since
  closed with local `1.1.2` proof/copy only, a first-three-paragraph
  check-surface inventory, a standard exercise-family coverage audit, and
  shared task-shell UX hardening with unit/notation and exit-ticket
  scaffold-suppression rules, structured choice/construction task-family
  contracts, and selectable-tile cloze runtime support. Complete the remaining
  Product Proof Track
  through TASK-FAMILY-SENTENCE-1,
  TASK-FAMILY-FORMULA-1, TASK-FAMILY-CLOZE-1, TASK-FAMILY-MULTI-1,
  TASK-FAMILY-ORDER-1, TASK-FAMILY-SOURCE-1, TASK-FAMILY-LABEL-1,
  TASK-FAMILY-MATCH-1, TASK-FAMILY-TWO-TIER-1, TASK-FAMILY-ASSERTION-1,
  GATE-TASK-FAMILY-1,
  GAME-ROUTE-AFFORDANCE-1, SKILLMAP-PRODUCT-1, REASON-STD-1,
  DUAL-CODING-STD-1, ENGINE-UNIFY-1, CHECK-SHORT-EXIT-2,
  SCALE-PROOF-3P, GATE-PRODUCT-3P, and REV-STD-1, or explicitly waive
  blockers with stated consequences before Scale Gate 1 if companion scaling
  is still desired.
- Keep `course_blueprint_v5.md` and the target-exercise source-of-truth path as
  the active baseline before Book 2 production.
- `1.1.1` exists as the reference companion paragraph with platform-integrated layout/UI and surface-adapted visual variants.
- A second Book 1 companion paragraph is built under L1.4 against the current platform state, surfacing any pipeline gap that a second regeneration reveals.
- Layout Round 2 (L1.5) acts on the combined findings from the L1.3A-C usability review and the L1.4 regression paragraph; changes land in platform-owned sources only.
- L1.6 remains the third-paragraph technical proof; L1.6R repaired the `1.1.3`
  companion dual-coding failure, and L1.7A decided that the evidence supports
  controlled foundation hardening only, not broad scaling.
- L1.7B-C through GATE-L1.7B closed the checkpoint product boundary only.
  L1.7B-MAP has fixed metadata alignment only. L1.7B-P23 accepted the
  stop/handoff and requires shared task-type shell support. SPEC-ET-1 corrected
  the exit-ticket standard to target-equivalent proof, and EX-LESSON-1 tied
  exam ingestion to the student route where relevant. Before scaling, GAME-UX-3A
  is closed as runtime foundation, ENGINE-OP-1 is closed as audit evidence,
  SKILLMAP-OP-1 is closed as visible-route proof, GRAPH-UX-2 is closed as
  graph/table task-shell integration proof, MATH-UX-2 is closed as
  math/calculation task-shell integration proof, REASON-UX-2 is closed as
  reasoning task-shell integration proof, and GATE-ENGINE-1 plus
  GRAPH/MATH/REASON-REFINE-1 have named the remaining operation-chain and
  answer-form blockers, L1.7B-Q2 through L1.7B-Q2-D31-STRUCT have established
  exact local `1.1.2` target-equivalent proof/copy only, and
  SYNC-PRODUCT-1 has made the first-three-paragraph Product Proof Track the
  next path before scale. Keep `Check` visible only for reviewed output,
  preserve the shared skill-map engine contract, keep the L1.7C-MATH restored
  primary math route intact, harden review standards through REV-STD-1,
  complete or explicitly waive GATE-PRODUCT-3P before Scale Gate 1, classify
  game-row carried flags, and do not permit mastery, sequencing, diagnostics,
  summative claims, PV, or broad scaling through exit tickets or game routing.
- Book 1 teacher-facing polish continues without breaking `check:book`.

### Months 1-3

- Book 1 becomes controlled-production-ready.
- Book 2 textbook layer becomes textbook-ready or close.
- Companion production decisions are based on validated, usable, regenerated companion materials with proper visual integration, not only file-count validation.

## What The Lessen Team Does Not Own

- Validator bugs and deploy/config plumbing.
- Platform-level generator refactors.
- Shared companion CSS/JS architecture.
- Converter/template changes needed to make layout improvements reproducible.
- Visual-builder, converter, and template changes needed to make image variants reproducible.
- Reference-report architecture cleanup.

Those should be escalated to the platform team instead of patched locally.

## Escalation Triggers

Bring issues back to the platform team immediately if:

- `check:book` fails because of validator/tooling behavior rather than content quality.
- A companion build is blocked by missing `deploy-config.json`, missing `shared/`, or missing generator/build-script infrastructure.
- The complete-mode validator expects artifacts that the documented toolchain cannot yet produce cleanly.
- A UI/layout improvement requires editing generated HTML directly instead of changing platform templates, converters, shared CSS/JS, or generators.
- An image/layout improvement requires pasting a one-off picture into generated output instead of changing platform visual builders, converters, templates, shared CSS/JS, or generators.
- The companion pages pass file validation but fail browser rendering, navigation, mobile usability, or basic readability checks.
- Light/dark mode makes a graphic unreadable, mismatched, or visibly pasted from the wrong theme.
