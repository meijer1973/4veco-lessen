# REV-STD-1 Inherited Flag Table Draft

Date: 2026-05-26
Status: DRAFT; TO BE COMPLETED DURING REV-STD-1

This draft makes Scale Gate 1 inherit the flags that cannot be treated as
ordinary carry items.

| Source | Flag | Level | Consequence Before Scale Gate 1 | Required Route |
|--------|------|-------|----------------------------------|----------------|
| L1.7C / L1.7D | `Rekenen` primary route currently points to `stappenplan` where the old skill-tree math game should be primary. | core_spec_failure until restored | Scale Gate 1 cannot claim the three-game row is aligned. | L1.7C-MATH |
| L1.7B-R / GATE-L1.7B | Exit-ticket metadata uses `A43`/`A04` while paragraph-plan skills are `B01`/`B02`. | scale_blocker | Metadata may not be used for target-exercise readiness, diagnostics, mastery, sequencing, target-exercise promotion, PV, CP-6/Year-1, or scaling evidence. | L1.7B-MAP |
| L1.7B-R / GATE-L1.7B | `1.1.1` checkpoint is a short non-summative check, not target-exercise-readiness evidence. | scale_blocker | Exit tickets cannot support stronger readiness or completion claims. | L1.7B-Q2 + GATE-L1.7B-Q2 |
| L1.7B-R / GATE-L1.7B | Current checkpoint task form is MC-only. | scale_blocker for calculation/graph paragraphs | Do not generalize to `1.1.2` or `1.1.3` unless task forms match their target exercises or a platform handoff is recorded. | L1.7B-P23 |
| L1.7C | Graph and reasoning game variants remain limited. | scale_blocker | Do not treat the current game row as broad scale quality. | L1.7C-MATH / later game-row scaling |
| L2.0 | `1.1.4` quality-ref remains legacy `FLAG`; consolidation exercise content has unresolved graph-drawing/profit-formula flags. | scale_blocker for consolidation scaling | Do not treat consolidation pages as final reviewed content. | future consolidation quality-ref/content review |
| L1.7D / L2.0 | Screenshot QA is representative, not an operational Scale Gate matrix. | scale_blocker for broad visual QA | Scale Gate 1 needs a sampling matrix covering route patterns and device/theme/focus expectations. | REV-STD-1 / Scale Gate 1 preparation |

REV-STD-1 must verify this table against current evidence and decide whether
any row requires reopening, revision, or platform handoff before Scale Gate 1.
