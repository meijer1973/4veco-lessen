# REV-STD-1 Review Standard Draft

Date: 2026-05-26
Status: DRAFT; TO BE REVIEWED IN REV-STD-1

## Core Rule

A controlled pilot may carry limitations, but it may not carry a broken version
of the original specification. If a sprint ships a narrower product than the
original assignment, the roadmap must name how the team will reach the actual
product.

`Pilot` and `MVP` describe scope. They do not excuse missing non-negotiable
requirements.

## Flag Levels

`minor_carry_flag`

An issue outside the sprint's core objective. It may remain after closure if it
is named, low-risk, and assigned to a later route.

`scale_blocker`

An issue that may allow controlled pilot closure but blocks scale reliance. It
must be visible to the next gate and cannot be ignored by Scale Gate 1.

`core_spec_failure`

An issue that means the sprint did not meet its stated specification. It must
return REVISE, FAIL, or PAUSE.

## Verdict Rules

PASS:

All core requirements are met. Remaining issues are cosmetic or clearly outside
scope.

PASS WITH FLAGS:

Allowed only when:

- the product meets the sprint's core specification;
- flags are explicitly named;
- flags do not affect the student's primary route;
- flags do not affect source-of-truth metadata;
- flags do not affect target-exercise readiness;
- flags do not affect scale authorization.

REVISE:

Required when:

- the primary student route is wrong;
- the product implements a weaker product than specified;
- a core game/exit-ticket requirement is missing;
- review depends on pilot/MVP language to excuse failure of the original
  objective.

FAIL:

Required when:

- student-facing output is misleading;
- product implies mastery, diagnosis, or grading without authorization;
- generated output was hand-patched;
- source-of-truth metadata is invalid and visible or used for claims.

PAUSE:

Required when:

- the platform cannot support the requested product safely;
- the team cannot determine the source of truth;
- a fix requires a platform architecture decision.

## Required Review Packet Fields

Every future review packet should include:

- original sprint specification;
- non-negotiable requirements;
- student-facing product role;
- implementation scope and what was deliberately not built;
- evidence inspected;
- core-requirement checklist;
- flag table with level, source sprint, consequence, and next action;
- explicit distinction between pilot, controlled production, and scale-ready.

## Lead Review Rules

- PASS WITH FLAGS is forbidden if any non-negotiable requirement fails.
- A flag carried across two consecutive sprints becomes a gate question.
- A carried scale blocker cannot be ignored by the next scale gate.
- Technical QA cannot substitute for teacher-learning-quality review.
- If a sprint is reframed as an MVP/pilot during implementation, the review
  must confirm whether the reframed product still meets the original
  specification or name the follow-up sprint that will restore it.

## Flag Budget

- Default maximum: three carried flags per sprint.
- More than three carried flags requires a PAUSE check or explicit lead-review
  explanation.
- Any flag touching the primary student route, target-exercise readiness,
  source-of-truth metadata, or scale authorization is at least a
  `scale_blocker`.
