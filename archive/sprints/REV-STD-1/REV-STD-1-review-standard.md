# REV-STD-1 Review Standard

Date: 2026-06-10
Status: IMPLEMENTED; REQUIRED FOR FUTURE LEAD REVIEW AND REVIEW PACKETS

## Core Rule

A review may carry limitations, but it may not carry a broken version of the
original specification as an ordinary flag. If a sprint ships narrower behavior
than the original assignment, the roadmap must name the later sprint or gate
that restores the specified product, or the human waiver must state the
consequence.

`PASS WITH FLAGS` is allowed only when every non-negotiable requirement in the
sprint's core objective is met and the remaining flags sit outside that core
objective.

## Required Baselines

Every review packet that touches companion adoption, first-three product proof,
review gates, or Scale Gate 1 must cite:

- `specifications/product-end-state.md`;
- the original sprint or gate specification;
- the relevant stable companion specification section from
  `specifications/companion-core-specifications.md`;
- non-negotiable requirements;
- student-facing product role;
- implementation scope and deliberately unbuilt scope;
- evidence inspected;
- a core-requirement checklist.

If the current roadmap framing conflicts with `product-end-state.md` or the
original sprint/gate specification, the conflict is a review finding. It cannot
be hidden by the current narrowed framing.

## Finding Classifications

`core_requirement_met`

The required item is proven by cited evidence.

`quality_improvement_available`

The requirement is met, but a named improvement would raise quality. It blocks
no current claim or authority unless the review explicitly says otherwise.

`minor_carry_flag`

The issue is outside the sprint's core objective. It may remain after closure
only when named, owned, and routed to a later action.

`scale_blocker`

The issue may allow the current bounded objective to close, but blocks a named
later claim or authority such as product-route adoption, target-equivalent
reliance, Scale Gate 1, product use, or broad scaling.

`core_spec_failure`

The sprint did not meet a required part of its original specification. It must
return REVISE, FAIL, or PAUSE. It cannot be carried in PASS WITH FLAGS.

## Finding Fields

Every finding or carried flag must state:

- source;
- classification;
- what it blocks;
- what it does not block;
- proof required to close;
- owner or next route.

## Verdict Rules

PASS:

All core requirements are met. Remaining notes are either
`core_requirement_met` evidence or `quality_improvement_available` items that
block no claim.

PASS WITH FLAGS:

Allowed only when:

- all non-negotiable requirements are met;
- no `core_spec_failure` remains;
- flags are explicitly named;
- each flag states blocks / does-not-block / proof-to-close;
- every carried flag is outside the sprint's core objective.

REVISE:

Required when the primary student route is wrong, the product implements a
weaker product than specified, a required game/check/exit-ticket behavior is
missing, or review depends on narrowed scope language to excuse failure of the
original objective.

FAIL:

Required when student-facing output is misleading, product implies mastery,
diagnosis, grading, or sequencing without authorization, generated output was
hand-patched, or source-of-truth metadata is invalid and used for claims.

PAUSE:

Required when the platform cannot support the requested product safely, the
team cannot determine the source of truth, or a fix requires a platform
architecture decision before responsible continuation.

## Lead-Review Output Requirement

Lead review must include a `Finding Classification` section with this table:

| Finding | Classification | Blocks | Does not block | Proof required to close |
|---|---|---|---|---|

For `PASS WITH FLAGS`, the result JSON must also include `lead_review.findings`
and any `lead_review.flags`, using the same classification vocabulary.

## Review Packet Requirement

Review packets must include:

- product-end-state baseline citation;
- original sprint or gate specification;
- non-negotiable requirements;
- core-requirement checklist;
- evidence inspected;
- finding classification instructions;
- stop conditions for missing core evidence;
- explicit product-boundary statement.

## Flag Budget

- Default maximum: three carried flags per sprint.
- More than three carried flags requires a PAUSE check or explicit lead-review
  explanation.
- Any flag touching the primary student route, target-equivalent reliance,
  source-of-truth metadata, product-route adoption, or scale authorization is
  at least a `scale_blocker`.

## Scale Gate Rule

Scale Gate 1 may not close while unresolved `core_spec_failure` findings remain
unless a human waiver explicitly records the waived requirement and the
consequence. Scale Gate 1 may inherit `scale_blocker` findings only when each
one says exactly what claim remains blocked and what proof is required to close
it.
