# 2.1.4 Gemengde opgaven: kosten en opbrengsten - paragraph plan

## Status

- Type: `gemengde_opgaven`
- Introduces new theory: no
- Upstream registry status: `placeholder_needs_review`
- Local package status: golden-candidate integration target proposal

## Governance note

The upstream v5 target registry contains only a placeholder for `2.1.4`. This package therefore does not claim to implement a reviewed final target exercise. It proposes a high-quality integration target that combines the operation chains from `2.1.1`, `2.1.2`, and `2.1.3`.

## Prior paragraphs integrated

| Prior paragraph | Reused operations | Must stay consistent |
| --- | --- | --- |
| 2.1.1 Kostenstructuren | `TCK`, `TVK`, `TK`, `GCK`, `GVK`, `GTK` | Total first, averages after totals. `GCK` falls when fixed costs are spread over more products. |
| 2.1.2 Opbrengsten, winst en break-even | `TO`, `GO`, `winst`, `TO = TK`, graph with profit/loss zones | Break-even is an equality, not a vague graph intersection only. Profit at one `Q` is a vertical distance. |
| 2.1.3 Marginale kosten en marginale opbrengsten | `MK = ΔTK / ΔQ`, `MO = ΔTO / ΔQ` | Marginal values are between rows. Do not introduce differentiation or `MO = MK` as a maximisation rule. |

## Local target exercise

Context: SmoothBox sells lunchboxes.

Sources:

- fixed costs: €1,200 per day;
- variable costs under normal production: €2.00 per lunchbox;
- sales price: €5.00 per lunchbox;
- rush-order table for quantities above 700.

Subquestions:

A. Derive `TCK`, `TVK`, `TK`, and `TO` formulas from the source.
B. Calculate totals, averages, profit, and explain the change in `GCK`.
C. Calculate break-even and interpret it using the graph.
D. Calculate `MK` and `MO` from a rush-order table between rows.
E. Evaluate a student claim about profitability after break-even.

## Canonical integrated procedure

1. Read and mark source values.
2. Decide which formula family is needed: cost, revenue/profit, average, break-even, or marginal.
3. Calculate totals before averages.
4. Calculate profit as `TO - TK`.
5. For break-even, set `TO = TK`.
6. For marginal values, use two consecutive rows and divide by `ΔQ`.
7. End with an economic sentence that uses the calculated result.

## Visual plan

| Figure | Purpose | Golden-example rule |
| --- | --- | --- |
| Figure 1 | Integration route from source to answer | Makes mixed-exercise workflow visible. |
| Figure 2 | Clean `TK`/`TO` graph | Formula labels only; no numeric-only point labels; profit shown as vertical distance at one `Q`. |
| Figure 3 | Marginal-values-between-rows reminder | Prevents the common error of treating `ΔTK` as `MK` when `ΔQ` is larger than 1. |

## Misconception targets

- Students copy numbers from sources without deciding what the number represents.
- Students calculate averages before computing totals.
- Students treat break-even as "where the graph looks close" instead of `TO = TK`.
- Students think every product after break-even is equally profitable.
- Students forget to divide `ΔTK` and `ΔTO` by `ΔQ` when table steps are larger than 1.
