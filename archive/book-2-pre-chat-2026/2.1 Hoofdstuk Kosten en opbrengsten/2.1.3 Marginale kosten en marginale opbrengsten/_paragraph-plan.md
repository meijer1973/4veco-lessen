# Paragraph plan - 2.1.3 Marginale kosten en marginale opbrengsten

## Status

Golden-candidate Part A textbook rewrite. The upstream target exercise record is still `migrated_from_v4_needs_v5_review`; this package does not promote the registry status to `reviewed_final`.

## Target trace

Target source: `references/authored/course-target-exercises.json`, record `2.1.3 Marginale kosten en marginale opbrengsten`.

The target exercise is a table-first marginal-thinking chain:

- firm 1: `TK = 200 + 3Q`, `TO = 8Q`, fixed price €8 per unit;
- table values for `Q = 0, 10, 20, 30, 40, 50`;
- students calculate `TK`, `TO`, `winst`, `MK` and `MO`;
- `MK` and `MO` are calculated as `ΔTK / ΔQ` and `ΔTO / ΔQ`, not by reading a single total row;
- students notice that `MK` is constant for the linear cost function;
- students notice that `MO` is constant and equals price when price is constant;
- firm 2: `TK = 100 + Q²`, fixed price €30, table for `Q = 0, 5, 10, 15, 20`;
- students observe that `MK` increases for the quadratic cost function;
- students explain in words what `MK` and `MO` tell you.

## Scope boundary

This paragraph introduces marginal concepts and table calculation only.

Do **not** teach:

- derivatives/differentiation;
- the profit-maximisation rule `MO = MK`;
- monopoly marginal revenue;
- marginal analysis from a continuous graph.

Those belong to later paragraphs. Here the student must first understand marginal thinking as: *what changes when production or sales increases by one unit?*

## Canonical terminology

Use these terms consistently:

- `Q`: productieomvang / aantal verkochte producten;
- `TK`: totale kosten;
- `TO`: totale opbrengst;
- `winst = TO - TK`;
- `MK`: marginale kosten, the extra cost per extra product;
- `MO`: marginale opbrengst, the extra revenue per extra product;
- `ΔQ`: the step in quantity between two rows;
- `ΔTK`: the change in total costs between two rows;
- `ΔTO`: the change in total revenue between two rows.

## Target operation chain

1. Read `TK`, `TO` or the price from the source.
2. Fill `TK`, `TO` and `winst` for each requested `Q`.
3. Compare each row with the previous row.
4. Write the step size `ΔQ`.
5. Calculate `ΔTK` and `ΔTO`.
6. Calculate `MK = ΔTK / ΔQ` and `MO = ΔTO / ΔQ`.
7. Describe the pattern: constant, rising or falling.
8. Explain the economic meaning of `MK` and `MO` in words.

## Visual route

- Figure 1: row-to-row marginal route. It shows that marginal values live between two table rows, and that raw differences must be divided by the quantity step when the table jumps by more than one product.
- Figure 2: pattern comparison for linear versus quadratic cost functions. It avoids a cluttered graph and instead uses interval cards to show constant versus rising `MK`.

Visual-load rule: keep numbers only where they teach the row-to-row operation. Avoid decorative graph labels and avoid making the figure a second answer table.

## Misconceptions to foreground

- Wrong: `MK` is the same as `TK`.
- Correct: `MK` is the change in `TK` per extra product.
- Wrong: if `TK` rises by 30 when `Q` rises by 10, then `MK = 30`.
- Correct: `MK = 30 / 10 = 3` per product.
- Wrong: `MO` is the same as total revenue.
- Correct: `MO` is the change in `TO` per extra product.
- Wrong: `MO` always equals price.
- Correct: `MO = P` only when every extra product is sold at the same price.
- Wrong: this paragraph already teaches profit maximisation.
- Correct: it only prepares the marginal concepts needed later.

## Practice route

- Startoefeningen: define `MK`/`MO`, calculate from two rows, and protect the step-size correction.
- Guided table exercise: fill totals first, then marginal values between rows.
- Independent exercises: linear cost and quadratic cost contexts.
- Herhaling: combine `TK`, `TO`, winst, `MK` and `MO` from cost and revenue source data.
- Doeloefening: target-equivalent table with the exact two target firms.
- Denkertje: compare raw differences from different step sizes and explain why division by `ΔQ` is required.

## Review checklist for agents

A reviewer should reject revisions that:

- calculate marginal values from one row instead of from two rows;
- forget to divide by `ΔQ` when the table step is larger than 1;
- introduce differentiation or `MO = MK` as the lesson goal;
- let students fill `MK`/`MO` before they have calculated `TK`/`TO` and winst;
- use graph labels as answer-giving decoration rather than table-operation support;
- use lowercase subquestion labels instead of `A.`, `B.`, `C.`, ...;
- leave answer models without formula, substitution, unit and economic interpretation.
