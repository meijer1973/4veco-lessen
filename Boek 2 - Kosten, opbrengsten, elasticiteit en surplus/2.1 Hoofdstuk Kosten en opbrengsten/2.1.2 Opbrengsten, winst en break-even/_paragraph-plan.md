# Paragraph plan - 2.1.2 Opbrengsten, winst en break-even

## Status

Golden-candidate Part A textbook rewrite. The upstream target exercise record is still `migrated_from_v4_needs_v5_review`; this package does not promote the registry status to `reviewed_final`.

## Target trace

Target source: `references/authored/course-target-exercises.json`, record `2.1.2 Opbrengsten, winst en break-even`.

The target exercise is the bakery revenue/profit/break-even chain:

- uses the bakery from §2.1.1 / migrated v4 §1.3.2;
- selling price: €1,50 per loaf;
- prior cost function: `TK = 500 + 0,80Q`;
- write `TO` as a function of `Q`;
- calculate `TO` and winst at `Q = 500` and `Q = 1000`;
- calculate `GO = TO / Q` at `Q = 500` and observe `GO = P` when price is constant;
- find break-even algebraically with `TO = TK`;
- draw `TK` and `TO`, mark break-even, and indicate winst at `Q = 1000`.

## Canonical terminology

Use these terms consistently:

- `Q`: aantal verkochte producten / productieomvang where production equals sales;
- `P`: prijs per product;
- `TO`: totale opbrengst;
- `GO`: gemiddelde opbrengst;
- `TK`: totale kosten;
- `winst = TO - TK`;
- `break-even`: `TO = TK`, winst is nul.

Avoid introducing `MO` or marginal logic in this paragraph. That belongs to §2.1.3.

## Target operation chain

1. Read the selling price and cost function from the source.
2. Write `TO = P × Q`.
3. Use the given or previously built `TK`.
4. Calculate `TO`, `TK` and `winst = TO - TK` at requested production levels.
5. Calculate `GO = TO / Q` and state why `GO = P` under a constant selling price.
6. Find break-even by setting `TO = TK` and solving for `Q`.
7. Represent the result in a `TK`-`TO` graph: intersection is break-even; at a chosen `Q`, winst/verlies is the vertical distance.

## Visual route

- Figure 1: source-to-formula schema. It binds price, cost function, `TO`, `GO`, winst and break-even into one reusable route.
- Figure 2: `TK`-`TO` graph for the bakery. It must show formulas, the break-even intersection and the vertical winst gap at `Q = 1000`.

Visual-load rule: keep graph labels formula-based and unit-based. Do not add loose numeric point labels. The exact values belong in tables and answer calculations.

## Misconceptions to foreground

- Wrong: high sales automatically mean profit.
- Correct: profit requires `TO > TK`.
- Wrong: `GO` is profit per product.
- Correct: `GO = TO / Q`; with constant price, `GO = P`. Winst per product would require costs too.
- Wrong: the profit in a `TK`-`TO` graph is the entire area between lines over a range of `Q`.
- Correct: profit at a selected `Q` is the vertical distance `TO - TK` at that `Q`.
- Wrong: a break-even point always exists.
- Correct: if the selling price is not above the variable cost per unit, extra sales do not cover fixed costs.

## Practice route

- Startoefeningen: write `TO`, compute simple winst and `GO`.
- Guided table exercise: calculate `TO`, `TK`, winst and classify loss/profit.
- Break-even exercise: solve `TO = TK` in a short context.
- Graph exercise: read Figure 2 and identify `TO`, `TK`, break-even and vertical winst distance.
- Zelfstandige oefeningen: fresh production contexts with break-even and whole-unit rounding.
- Herhaling/doeloefening: combine cost structure from §2.1.1 with revenue and break-even.
- Denkertje: no feasible break-even if price is below variable cost per unit.

## Review checklist for agents

A reviewer should reject revisions that:

- teach `TO`, `GO`, winst and break-even as separate definitions without a single source-to-conclusion route;
- let students compute winst without explicitly using the same `Q` for `TO` and `TK`;
- imply that `GO` is profit per product;
- shade the wrong graph region and thereby teaches area-under-curve reasoning in a total-cost/total-revenue graph;
- skip the whole-unit interpretation after a fractional break-even result;
- use lowercase subquestion labels instead of `A.`, `B.`, `C.`, ...;
- leave answers without formula, substitution, unit and economic interpretation.
