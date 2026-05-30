# GAME-UX-3A Sprint Plan: Shared Task-Type UX Foundation

Date: 2026-05-30

Status: closed through platform GAME-UX-3A sprint record.

## Goal

Implement the shared task-type shell foundation required by the product and
companion specifications. The shell must support task families used by
target-equivalent exit tickets, checkpoint-only local checks, graph/table
practice, math/calculation practice, exam-style answer-form requirements, and
later reasoning tasks where the student action overlaps.

## Scope

In scope:

- platform task-shell runtime files;
- platform focused task-shell tests;
- platform deploy/shell load hooks;
- `lessen-team-roadmap.md`;
- this lesson-side archive record.

Out of scope:

- generated lesson output;
- lesson source-data mutation;
- target-exercise mutation;
- protected reference mutation;
- candidate storage or candidate writes;
- diagnostics, mastery, sequencing, summative use, AI, PV, Scale Gate 1, or
  student/product use.

## Procedure

1. Record the platform sprint plan, baseline, and planning review.
2. Implement task-shell validation, deterministic checking, self-check
   behavior, neutral feedback, and boundary flags.
3. Implement static UI/CSS render helpers for the accepted task families.
4. Add deploy-copy and exit-ticket shell-load hooks without running deploy.
5. Add focused tests for task-family coverage and product-boundary wording.
6. Update the lesson and platform roadmaps so GAME-UX-3A is closed and
   ENGINE-OP-1 is the active next dependency.
7. Refresh maps/indexes and validate the platform sprint bundle.

## Proof

The platform-side GAME-UX-3A sprint bundle records the full acceptance tests,
diff summary, and repository publication proof. This lesson archive exists so
future lesson-roadmap readers can find the task-shell foundation that unblocks
ENGINE-OP-1, GRAPH-UX-2, MATH-UX-2, and L1.7B-Q2 planning.
