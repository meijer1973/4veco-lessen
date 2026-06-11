# REV-STD-1 Sprint Plan

Date: 2026-05-26
Updated: 2026-06-10
Status: CLOSED PASS WITH FLAGS / REVIEW-STANDARD HARDENING ONLY

## Sprint Name

Core-Spec Review Standard Hardening

## Problem

Recent sprints carried forward too many flags. Some carried flags were not
secondary issues; they were violations of original product specifications.

Examples:

- the exit ticket was accepted as a short checkpoint even though the intended
  product path is target-exercise readiness;
- the `Rekenen` route displaced the old skill-tree math game;
- shared skill-map architecture was reviewed too weakly after one consumer was
  effectively swapped;
- technical QA passed while product semantics remained incomplete.

A good product should be the default outcome of a sprint. `Pilot` and `MVP`
are scope labels, not excuses to undercut the stated specification.

## Purpose

Update review packets, lead-review rules, and flag handling so a core
specification failure cannot be carried as an ordinary flag. If the team
deliberately ships a narrower product than the original specification, the
roadmap must name the sprint that restores the full specified product.

## Read-First Evidence

- `specifications/product-end-state.md`
- `specifications/companion-core-specifications.md`
- `lessen-team-roadmap.md`
- `archive/sprints/L1.7C/L1.7C-human-review-packet.md`
- `archive/sprints/L1.7C/L1.7C-lead-review-summary.md`
- `archive/sprints/L1.7D/L1.7D-human-review-packet.md`
- `archive/sprints/L1.7D/L1.7D-lead-review-summary.md`
- `archive/sprints/L1.7B-R/L1.7B-R-human-review-packet.md`
- `archive/sprints/L1.7B-R/L1.7B-R-lead-review-summary.md`
- `archive/sprints/GATE-L1.7B/GATE-L1.7B-human-review-packet.md`
- `archive/sprints/GATE-L1.7B/GATE-L1.7B-lead-review-summary.md`
- `archive/sprints/L2.0/L2.0-human-review-packet.md`
- `archive/sprints/L2.0/L2.0-lead-review-summary.md`
- `archive/sprints/L2.0/L2.0-quality-ref-status-standard.md`
- `archive/sprints/L2.0/L2.0-flag-disposition.md`

## Required Work

1. Define five finding classifications:
   - `core_requirement_met`;
   - `quality_improvement_available`;
   - `minor_carry_flag`;
   - `scale_blocker`;
   - `core_spec_failure`.
2. Update review-packet templates or packet instructions so every review
   includes:
   - `specifications/product-end-state.md`;
   - original sprint specification, including the relevant section of
      `specifications/companion-core-specifications.md`;
   - non-negotiable requirements;
   - student-facing product role;
   - evidence inspected;
   - core-requirement checklist;
   - explicit distinction between pilot, controlled production, and
     scale-ready.
3. Update lead-review rules:
   - PASS WITH FLAGS is forbidden if any non-negotiable requirement fails;
   - a flag carried across two consecutive sprints becomes a gate question;
   - a carried scale blocker cannot be ignored by the next scale gate;
   - technical QA cannot substitute for teacher-learning-quality review.
4. Add a flag budget:
   - max 3 carried flags per sprint unless lead review explains why more is not
     a PAUSE condition;
   - any flag touching student route, target-exercise readiness,
     source-of-truth metadata, or scale authorization becomes at least a scale
     blocker.
5. Apply the standard retroactively to:
   - L1.7C;
   - L1.7D;
   - L1.7B-R;
   - GATE-L1.7B;
   - L2.0.
6. Produce an inherited-flag table for Scale Gate 1.
7. Verify that any roadmap or sprint plan that narrows the specification names
   the follow-up sprint or gate that restores the full product.

## Review Verdict Definitions

PASS:

All core requirements are met. Remaining issues are cosmetic or clearly outside
scope.

PASS WITH FLAGS:

Allowed only when the product meets the sprint's core specification and flags
do not affect the student's primary route, source-of-truth metadata,
target-exercise readiness, or scale authorization.

REVISE:

Required when the primary student route is wrong, the product implements a
weaker product than specified, a core game/exit-ticket requirement is missing,
or review depends on "controlled pilot" language to excuse failure of the
original objective.

FAIL:

Required when student-facing output is misleading, product implies
mastery/diagnosis/grading without authorization, generated output was
hand-patched, or source-of-truth metadata is invalid and visible or used for
claims.

PAUSE:

Required when the platform cannot support the requested product safely, the team
cannot determine the source of truth, or a fix requires a platform architecture
decision.

## Expected Outputs

- `archive/sprints/REV-STD-1/REV-STD-1-review-standard.md`
- `archive/sprints/REV-STD-1/REV-STD-1-inherited-flag-table.md`
- confirmed baseline use of `specifications/companion-core-specifications.md`
  in future review packets;
- updated review-packet template/instructions, if such a platform-owned or
  lesson-owned template exists;
- platform `reports/sprints/REV-STD-1-flag-disposition.md`
- platform `reports/sprints/REV-STD-1-flag-disposition.json`
- platform `build-scripts/sprints/check-rev-std1-flag-disposition.js`

## Acceptance Criteria

- Future review packets separate core specification from optional improvement.
- Future review packets cite `specifications/product-end-state.md` and
  `specifications/companion-core-specifications.md` where relevant.
- PASS WITH FLAGS cannot hide core failure.
- Scale Gate 1 has an explicit inherited-flag table.
- Review agents are instructed to compare output against the original
  specification, not only the current narrowed framing.
- The standard explicitly distinguishes bounded scope from specification drift.

## Stop Conditions

- Stop if the review template lives in platform-owned workflow code and a
  platform handoff is needed before editing it.
- Stop if retroactive classification finds a core-spec failure that requires
  reopening or revising a closed sprint before Scale Gate 1.
- Stop if the inherited-flag table cannot identify the source sprint,
  consequence, and next required action for each scale blocker.
