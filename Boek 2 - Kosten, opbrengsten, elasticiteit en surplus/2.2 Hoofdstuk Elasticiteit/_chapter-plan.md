# Chapter Plan: 2.2 Elasticiteit

Version: `BOOK2-TEXTBOOK-PRODUCTION-1-22-plan-v1`.
Date: 2026-09-05. Author: elasticity_planning. Accountable integrator: codex-root.
Status: draft for independent planning review and subsequent exact-plan owner decision.
Lane: Part A textbook. This is an internal control artifact, not student copy.

## Book foundation check

Canonical semantics come from `references/authored/book-outlines/book-2-outline.md`,
especially Chapter spine, §2.2, foundation dimensions and retrieval schedule.
Metadata supplies current pins and lifecycle only; this plan is not a second outline.

| Required pin | Exact value |
|---|---|
| v6 path / version | `references/owned/course-blueprint-v6-three-year.md`; `v6-three-year umbrella` |
| v6 canonical-LF SHA-256 | `72fb1bc8c7b4843ac5cf4c29acfb9d117b6118eeaa1cd5fe5229604dfe412e6e` |
| v5 path / version | `references/owned/course-blueprint-v5.md`; `v5` |
| v5 canonical-LF SHA-256 | `61130f10e7b8b6417641436f0995be090db04b11075d02878ae0a51c12b497c7` |
| Outline path / version | `references/authored/book-outlines/book-2-outline.md`; `book-2-outline-v3-review-ready` |
| Outline semantic SHA-256 / status | `919c39f64dd212dba37b62902a5bb2e2ce6388c6020a0491e1621017ae2192a1`; `approved_with_holds` |
| Current registry canonical-LF SHA-256 | `d3d7163ad82e0ddcf2f9ae1cbfa653335c96cb46762e8125bd594583f5d5885e` |
| Frozen twelve-record package SHA-256 | `914d1a39f18f8f9b7cf7fad938d2c42f9c2bc19671d94c24be151b1da0371310` |
| Chapter-plan path | `Boek 2 - Kosten, opbrengsten, elasticiteit en surplus/2.2 Hoofdstuk Elasticiteit/_chapter-plan.md` |
| Chapter-plan version / hash | Version above; full canonical-LF hash recorded externally in `reports/sprints/BOOK2-TEXTBOOK-PRODUCTION-1-22-planning-evidence.md` to avoid a self-referential hash |
| Platform planning base | `4b78edfaca8554937ef4abf3296ef2e4cd366be1` (descendant of green merged PR231 `96416b6b5bd57094576e9aba0a42d682584ec479`) |
| Lesson source baseline | `f09fd6e88edc5049b026b16b0158e7e188091d2d` |
| Currentness evidence | Structural, approved-outline and `chapter_planning --chapter 2.2` checks PASS on 2026-09-05; exact commands in planning evidence |

Target record hashes use `sha256(JSON.stringify(record))` with repository property order.
All four target statuses remain exactly `candidate_review_ready`; the immutable
activation and owner grant, not a renamed status, establish approved frozen targets.

| ID / kind | Target record SHA-256 | Part A plan reference relative to this chapter |
|---|---|---|
| 2.2.1 / theory | `61b54bde03d60be241092479cfcea8820e8187220f8f454dc9fef5045c8ea288` | `2.2.1 Prijselasticiteit/2.2.1-textbook-plan.md` |
| 2.2.2 / theory | `8ce56143aef61b0e67aae5b179f6e5f3fe547192bc776a42c43101cb5a70fa2e` | `2.2.2 Elasticiteit en omzet/2.2.2-textbook-plan.md` |
| 2.2.3 / theory | `9a3a29bcedc16739b74b66b2bb8e136b37e86c7f5cfee3ee35ea37c4bdeed1c5` | `2.2.3 Inkomenselasticiteit en kruiselingse elasticiteit/2.2.3-textbook-plan.md` (future reviewed input; not authored here) |
| 2.2.4 / gemengde_opgaven | `4e0840ddf202ce4906ee05cd4dde97c0f3577885c34f0b9613ea18760aad7519` | `2.2.4 Gemengde opgaven elasticiteit/2.2.4-textbook-plan.md` (future reviewed input; not authored here) |

### Approved replacement lineage, not registry normalization

The outline's older §2.2 rationale describes an empty prior list and two inelastic
cinema/petrol cases. Those are historical descriptions, not current target facts.
The stronger current frozen §2.2.1 target explicitly names Book 1 retrieval and
compares Nova (`Ev=-0.8`) with StreamNow (`Ev=-2`). §2.2.2 now contains both cases
and an explicit local-rule/finite-change question. Do not reuse petrol as the target.

The owner-approved package was reviewed at `b614577f19c6e8a95c9981256aa125e56d26cd79`,
with content decision at
`6d6f42226987f9ef9977f46dbb869455a88c25e2/reports/sprints/BOOK2-TARGET-AUTHORITY-REMEDIATION-1-owner-review-20260905.md`.
The separate integration grant is
`6e35f4fe0aeaa448da9476469294ccd45775232d/reports/sprints/BOOK2-TARGET-INTEGRATION-1-owner-authorization.md`;
activation commit is `206c018478654db781cc879e7ea36adcd9ef600c`.
PR231 merge/main CI completed the integration gate. None of this approves these
previously unseen teaching plans. Registry-normalization decision proposed here:
**no registry mutation is needed or authorized**. Preserve the frozen registry,
semantic outline, historical approvals and historical read-only lesson snapshot.

### Holds and exact current actions

Current action: `chapter_planning`. Foundation verdict: `PASS_FOR_CHAPTER_PLANNING`.
This is not a production or learning-quality verdict. All five open holds are
accounted for below; no release is made by this planning assignment.

| Hold | Scope match for 2.2? | Blocks chapter_planning? | Explicit permits / resolution for current action | Effect now | Later effect |
|---|---|---|---|---|---|
| H-221-PRIOR (open) | §2.2.1 within chapter | No | Neither; resolution is goal_owner_decision | NOT_APPLICABLE to this action | Blocks §2.2.1 approved_goal_use and paragraph_production until exact reviewed retrieval plan owner approval |
| H-22-ELASTIC-CONTRAST (open) | §§2.2.1–2.2.2 | No | Neither; resolution is goal_owner_decision | NOT_APPLICABLE to this action | Blocks those paragraphs' approved_goal_use and paragraph_production until reviewed teaching/practice contrast owner approval |
| H-BOOK2-ROOT-PLAN (open) | Book 2 | No | chapter_planning explicitly permitted; resolution book_plan_repair | PERMITS | Blocks book_readiness and whole_book_assembly; root handles separately |
| H-CHAPTER-23-PLAN (open) | No, Chapter 2.3 | No | chapter_planning permitted, but outside scope | NOT_APPLICABLE | Chapter 2.3 and whole-book actions remain governed separately |
| H-213-OPC2 (open) | No, §2.1.3/long route | No | Neither; resolution target_authority_repair | NOT_APPLICABLE | Formal output-choice teaching remains outside this project |

The released H-OUTLINE-OWNER, H-229-221-CANDIDATE, H-229-222-CANDIDATE,
H-229-223-CANDIDATE, H-229-224-CANDIDATE and H-229-EI-SUPERSESSION retain
their exact metadata evidence and have effect RELEASED. H-MERGE-GOVERNANCE is
historical PR226 evidence, not a reusable grant to merge this new payload.
All other released paragraph holds are outside this chapter; no historical
approval is rewritten. Full evidence remains in the pinned metadata.

## Scope, dependencies and build order

| Paragraph | Canonical role and prerequisite decision | Non-goals / downstream |
|---|---|---|
| §2.2.1 | Calculate signed Ev, classify magnitude, explain context. §1.1.2 percentages and §1.2 demand/substitute reasoning are previously_taught_retrieval_required; Ev ratio/classification is new_formal_learning. | No Ei/Ek, optimization or universal causal claims. Prepares §§2.2.2–2.2.4. |
| §2.2.2 | Link Ev to observed TO and bounded local direction. §2.2.1 Ev and §2.1.2 TO are previously_taught_retrieval_required after reviewed teaching exists. Local rule with finite-change check is new_formal_learning. | No optimal price, profit inference, retention or unlimited prediction. Prepares §2.2.4 and later pricing/incidence. |
| §2.2.3 | Extend to Ei/Ek and isolate changes in a supplied multivariable function. Retrieve §2.2.1 and Book 1 substitutes/complements/functions. Ei/Ek are new_formal_learning; familiar Book 1 labels are preview_or_familiarity_only. | No simultaneous causal inference, welfare claims or unrestricted forecasts. Prepares §2.2.4. |
| §2.2.4 | Source-rich consolidation of all three theory routes, with §2.1.2 TO. Classify individual prerequisites from reviewed evidence. | No new formula/theory, profit or causal generalization. Prepares later integrated demand/pricing work. |

These classifications describe curricular design, not observed learner security.
If a learner cannot execute retrieval, use printed support and teacher checking;
classify that learner need as previously_taught_not_secure_enough_to_assume rather
than silently skipping instruction. No preview fills a target-coverage cell.

Build waves after owner teaching-plan decisions: §2.2.1 first; §§2.2.2 and 2.2.3
after its reviewed handoff (2.2.2 also needs reviewed §2.1.2); §2.2.4 after all
three reviewed theory paragraphs; chapter assembly last. Every paragraph builder
uses its own claimed paired worktrees. Root is sole integrator; independent
reviewers, not builders, own paragraph/QC/quality acceptance. Planning can proceed
while these later production preconditions remain unmet.

## Shared conventions and deliberate context reuse

- Write `Ev=%ΔQv/%ΔP`, retaining the sign; use `|Ev|` only for classification.
  Elasticity is dimensionless, not a percentage. Percent calculations use old bases.
- Name the object, units and period: Nova tickets/week, StreamNow subscriptions/month;
  never compare their absolute TO levels as if periods or markets were identical.
- `TO=P×Q` uses price and quantity from the same observation, with all units sold
  at that observation's stated unit price. Omzet/totale opbrengst is not winst.
- Ceteris-paribus model interpretation is conditional. Two observations alone do
  not prove that own price caused the entire response or identify its determinant.
- **Ei semantics:** `Ei<0` inferieur goed; `0<Ei<1` normaal goed; `Ei>1` luxegoed.
  Leave `Ei=0` and `Ei=1` unlabeled. Do not introduce noodzakelijk goed as an Ei
  category or retain the old luxury/necessity split. Ek names both goods.
- Demand blue `#1A5276`, revenue purple `#7B2D8E`, cost amber `#E67E22`, text
  `#2D3748`. Supplement color with direct labels and patterns. No slope-as-Ev shortcut.
- Frozen Nova/StreamNow reuse across §§2.2.1–2.2.2 is deliberate. Fresh worked,
  guided and independent contexts in their plans do not duplicate each other.

## Unified procedure plan

Percentage (A38): identify old/new → calculate new−old → divide by old ×100% →
check sign and interpret. Ev (A15): note P/Q observations → calculate signed
%ΔQv and %ΔP with old bases → divide → classify magnitude → check direction
against the downward-demand model and state bounded meaning. Present the two
percent calculations in this order throughout teaching/answers; target a may
list price first without changing the calculation method.

TO (A85): select P and Q from the same situation → write TO=P×Q → substitute
and compute → check quantity scale, money and period. Repeat for the second
situation, then use A38 on TO, connect the observed result to Ev, and state
the revenue-only limit. The local rule is not mapped to D25: that unit is unrelated.
Missing/stale machine mappings remain flags, not permission to mutate the library.

## Retrieval, interleaving and visual plan

§2.2.1 explicitly prints old-base/sign retrieval plus a Book 1 substitute
explanation; its current-content check is separate within Startopgaven. §2.2.2
retrieves Ev interpretation and TO calculation, not a new profit procedure.
§2.2.3 later retrieves named numerator/denominator goods and isolates variables.
§2.2.4 consolidates only after reviewed teaching. Each closing review has one
or two short taught-content tasks; no generic graph drill is added.

§2.2.1 uses signed percentage bars plus a classification schematic and numerical
table; §2.2.2 uses exact before/after revenue rectangles and a local-rule comparison
schematic beside tables and prose. They support meaning but never add graph
construction as a target. See exact SVG/PNG filenames and geometry in the two
paragraph plans. Later §2.2.3/2.2.4 visual requirements are pinned in their own
reviewed plans; the old claim that these paragraphs need no visual assets is not
carried forward as an exemption.

## Quality floor, outputs and gates

The plans strengthen exercise-first teaching and reproducible agent evidence
(advantage), and paper usability/correctness (parity). Each eventual theory
paragraph has all seven canonical headings, compact non-heading summary, paper
short route, optional printed fading support, exact target and complete answers.
Explicit goals, meaningful varied contexts and neutral self-checking preserve the
school-fit overlay. No printed web/device direction or internal lane vocabulary.

After approvals, theory stems produce paragraaf/opgaven/antwoorden in md/html/pdf,
assets in paired SVG/PNG, build_pdf.py, independent review/quality-ref/handoff.
Consolidation produces opgaven/antwoorden only, with the same integrity/review gates.
Chapter stem `2.2 Elasticiteit` produces ` – hoofdstuk` and ` – antwoorden` in
md/html/pdf, collected `_assets/` and platform-owned build_chapter.py wrapper.
Chapter student output contains each full theory route once (including printed
guided practice), then mixed opgaven once; answer output is separate. No answers
in student chapter and no duplicate exercises. These are future outputs, not
authorization to generate them in this planning assignment.

Body, table, box and substantive figure labels must be at least 12pt at normal
print scale under the reviewed sprint floor. Simplify layout instead of shrinking.
Inspect every final page, not only contact sheets; verify source/output/asset
parity, captions, whitespace, overflow and source/question grouping. Planned gates:
independent plan review → exact owner decision → action currentness → paragraph
production → independent economics/didactics/student/visual/quality review →
chapter consistency and assembly → full rendered proof and validators → lead review.

Use `node scripts/validate-paragraph.js --mode part-a --profile student-web`
and `--profile publisher-print` per paragraph, then `node scripts/validate-chapter.js`,
lane-scope and target/currentness checks. Do not run stale output as proof of the
new plans. Classroom timing/attainment require later observation; Part B and
digital exit-ticket completeness remain separate named follow-up work. Optional
Inspectie mapping is omitted pending protected-reference refresh; no current
legal/Inspectie compliance claim is made.

Independent planning review: pending. Exact owner teaching-plan decision: pending.
Production verdicts, paragraph reviews, quality-ref and rendered proof: not produced.
Next action: independently review these three planning artifacts, correct defects,
publish exact hashes with CI/lead evidence, then request the actual owner decision
for H-221-PRIOR and H-22-ELASTIC-CONTRAST. Do not self-release either hold.
