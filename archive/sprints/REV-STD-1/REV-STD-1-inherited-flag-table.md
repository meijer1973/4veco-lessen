# REV-STD-1 Inherited Flag Table

Date: 2026-06-10
Status: CURRENT; MIRRORED FROM PLATFORM REV-STD-1 FLAG-DISPOSITION REPORT

Canonical detailed report:
`../4veco-platform/reports/sprints/REV-STD-1-flag-disposition.md`

## Rule

A carried flag blocks only the claim or authority it names. It must not be
treated as an ordinary note if it touches product-route adoption,
target-equivalent reliance, source-of-truth metadata, core student route,
Scale Gate 1, or product-use authority.

## Current Inheritance Table

| ID | Status | Finding | Blocks | Does not block | Proof required to close |
|---|---|---|---|---|---|
| REVSTD1-REVIEW-STANDARD-HARDENING | stale | core_requirement_met | Nothing after REV-STD-1 closure | Remaining product-proof gates | REV-STD-1 checker and lead-review schema-v3 fixture pass |
| REVSTD1-LESSON-GATE-SHARED-STALE | stale | core_requirement_met | Nothing after roadmap sync | CHECK-SHORT-EXIT-2 and adoption-preparation | Lesson roadmap cites platform gate closure and preserves boundaries |
| REVSTD1-SHARED-TASK-INGEST-CARRY | scope_boundary | scale_blocker | Product-route adoption, target-equivalent proof claims, Scale Gate reliance on this lane alone | CHECK-SHORT-EXIT-2 planning and adoption-preparation | Later rendered product-route adoption gate approves named shared-task hardening concerns |
| REVSTD1-CHECK-SHORT-EXIT-2 | missing_evidence_blocker | scale_blocker | CHECK-SHORT-EXIT-2 closure, SCALE-PROOF-3P, GATE-PRODUCT-3P, Scale Gate 1, new 1.1.1/1.1.3 completion language | Packet publication and direct human review | Returned direct human comments, resolution log, closure artifacts, and v3 finding classifications |
| REVSTD1-SCALE-PROOF-3P | missing_evidence_blocker | scale_blocker | Scale Gate 1 and three-paragraph product-proof claim | CHECK-SHORT-EXIT-2 review and GATE-PRODUCT-3P planning | Rendered first-three student-path proof |
| REVSTD1-GATE-PRODUCT-3P | missing_evidence_blocker | scale_blocker | Scale Gate 1 and product-readiness approval | Evidence preparation and non-authorizing packet work | Human product-readiness review using REV-STD-1 classifications |
| REVSTD1-SCALE-GATE-1 | real_blocker | scale_blocker | Scale Gate 1, broad scaling, diagnostics/adaptive/mastery/summative/PV claims | Bounded adoption-preparation and review packets | Close or explicitly waive CHECK-SHORT-EXIT-2, SCALE-PROOF-3P, GATE-PRODUCT-3P, and downstream reasoning/adoption blockers |
| REVSTD1-GAME-ROUTE-AFFORDANCE | real_blocker | scale_blocker | Coherent first-three product route proof and Scale Gate route-affordance reliance | Historical exact 1.1.2 copy boundary and adoption-preparation planning | Rendered route evidence with actionable items and regression guard |
| REVSTD1-SKILLMAP-PRODUCT | real_blocker | scale_blocker | First-three product proof and Scale Gate skill-map reliance | Existing route-layer runtime evidence | Rendered student-facing skill-map proof with actionable route links and no internal-code exposure |
| REVSTD1-REASONING-ADOPTION | missing_evidence_blocker | scale_blocker | Reasoning product-route adoption, replacement claims, target-equivalent reasoning proof, Scale Gate reliance | Bounded local reasoning-practice evidence | Route-specific playable/rendered proof and human gate approval for reasoning follow-ups |
| REVSTD1-DUAL-CODING-TASK-SELECTION | scope_boundary | scale_blocker | Broad dual-coding task-selection standard claim and Scale Gate reliance on unfinished policy | Closed source-context visual standard and task-specific decisions | Target-operation task-selection policy |
| REVSTD1-ENGINE-UNIFY | real_blocker | scale_blocker | Unified engine architecture readiness and Scale Gate reliance on unresolved unification | Reviewed local route/surface evidence | Reviewed keep/wrap/refactor/rebuild/deprecate plan |
| REVSTD1-CHECKSURFACE-113-EXEMPLAR | missing_evidence_blocker | scale_blocker | 1.1.3 product-route adoption, target-readiness approval, Scale Gate reliance on exemplar alone | Bounded specialist acceptance and held candidate status | Classroom/live or human-testable evidence, mobile state screenshots, graph/formula/feedback proof, and correct/retry automation |
| REVSTD1-ANSWER-FORM-GENERATOR | scope_boundary | scale_blocker | Answer-form product-route adoption and generator-backed exposure for blocked A-domain units | Reviewed A96 bounded proof, design records, zero-leak hardening | Generator implementation, route-specific rendered proof, reviewed adoption, no-exposure guard proof |
| REVSTD1-TASK-FAMILY-ADOPTION | scope_boundary | scale_blocker | Product-route adoption and target-equivalent reliance on task families without route proof | Family contract/runtime acceptance and adoption-preparation | Route-specific rendered proof, specialist/lead review, target-operation fit |
| REVSTD1-TASK-SHELL-UX-CARRY | non_blocking_carry_flag | minor_carry_flag | Future claim that screenshot manifest DOM proof is fully mature | Current task-shell UX closure and REV-STD-1 closure | Later checker/report for manifest DOM proof and source/render parity |
| REVSTD1-CI-RUNNER-MONITOR | non_blocking_carry_flag | minor_carry_flag | Nothing now | REV-STD-1 closure, Scale Gate evidence review, product-proof work | Future CI failure triage if runner labels change |
| REVSTD1-HISTORICAL-DRAFT-FLAGS | historical_archive_flag | core_requirement_met | Nothing current | REV-STD-1 closure and current product-proof work | Preserve as historical evidence only |
| REVSTD1-PRODUCT-BOUNDARY | scope_boundary | core_requirement_met | Unauthorized product-boundary claims | Bounded review-standard hardening and evidence preparation | Later explicit gate or human waiver if boundaries change |

## Historical Rows Retired From The Draft

- Math primary route displacement is closed by `L1.7C-MATH`.
- Checkpoint metadata mismatch is closed for the current checkpoint role by
  `L1.7B-MAP`.
- The checkpoint-only boundary is now represented by the current
  target-equivalent and product-proof blockers rather than by the old draft row.
- MC-only task-form limitations are superseded by `L1.7B-P23`, shared task
  family work, and the current check-surface/product-proof blockers.

Scale Gate 1 must inherit the current table above, not the retired draft rows.
