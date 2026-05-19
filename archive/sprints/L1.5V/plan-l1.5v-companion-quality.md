# L1.5V Companion Quality Polish + Pilot Lock-in for §1.1.1 — Whole-Sprint Execution Plan

Generated 2026-05-09 against platform main `5dcaf2a` and worktree `C:/Projects/4veco/4veco-platform-companion` on branch `content/1.1.1-companion-quality` (uncommitted skill+wiring edits already in place).

## 0. Findings from required reading (must read before executing the plan)

These shape the plan; the plan body assumes them. Surface them up-front so the executor and reviewer share the same baseline.

### 0.1. Registry vs roadmap: the 4-step B02 is already canonical

`references/machine/micro-teaching-units.json` lines 2640-2666 already define B02 with the canonical 4-step procedure verbatim matching the roadmap. The roadmap section "Canonical procedure decision (recorded 2026-05-09)" framed B02 as something to "decide", but the registry decision was already made and committed prior to this sprint. **There is no registry change to make in B1.** Bucket B1 (registry update) is a no-op for the JSON; the only B1 work left is the `_paragraph-plan.md` rewrite (Concept 3 row + visual-anchor row for `1.1.1_fig_3`), which is data the platform reads via humans and surfaces.

### 0.2. Vaardigheden builder is already 4-step

`build-scripts/content/book-1/b1-111-vaardigheden.js` line 386 already encodes `B02_PROCEDURE` verbatim from the registry. Skill 2 (line 480-548) already shows 4 steps. **Bucket C is not blocked on Bucket B for the vaardigheden builder itself**; it still depends on B for the per-paragraph plan and on the visual fig_3 (3-step → 4-step) and on the OTHER surfaces that haven't been migrated yet.

### 0.3. 3-step legacy lives on five surfaces and the fig_3 generator

Legacy 3-step references (must all flip to 4-step in B):
- `b1-111-visual-variants.js` lines 131-176 (`processSvg`, fig_3 generator: 3 cards "Alternatieven / Opbrengsten / Opgeven")
- `b1-111-samenvatting.js` lines 9, 303, 306 (cell rij 3 kolom 1 header: "Economisch denken — 3 stappen")
- `b1-111-presentatie.js` lines 10, 15, 261, 266, 271, 275, 281, 308, 418 (slide 5 + handout text)
- `b1-111-inoefening.js` lines 420, 451 ("3 stappen van economisch denken")
- `b1-111-opgaven.js` lines 6, 364, 466, 488, 495, 605 (instructie + question stems "3-stappen-procedure")
- `_paragraph-plan.md` lines 15, 30, 69, 103, 112, 139 (procedure-stappen-plan + visuelen-toewijzing).

Game data is already canonical: `shared/procedure/1.1.1.js` is 4-step ("Procedure volgt B02 ... letterlijk (4 stappen)"); `source-data/book-1/reasoning/1.1.1.csv` rows 6-9 are B-type 3-column scaffolds whose structure_label already centers on "Alternatieven opsommen → Opbrengst per alternatief → Beste niet-gekozen". A-type rows 2-5 use a different mental model ("Situatie herkennen → Schaarste benoemen → Alternatieve kosten") and don't expose a step count. C-type rows are misconception scaffolds, also not step-counted. **Game data needs no B-step rewrite**, but a regression check confirms.

### 0.4. The voorkennis builder also has no B02 procedure to rewrite

`b1-111-voorkennis.js` is intentionally pre-B02: it teaches arithmetic, bar-chart reading, and intuition-for-choice. It does not teach B02 as a procedure (confirmed by the review file §5). So Bucket B propagation does not touch the voorkennis builder; Bucket D items for voorkennis stand alone.

### 0.5. `convert_vaardigheden.py` has the SAME list-item bug as `convert_voorkennis.py`

`convert_vaardigheden.py` lines 619-654: section content loop branches on `heading2 / paragraph / begrippen / formula_box / asset_image / callouts / samenvatting`, and again silently drops `list_item`. The voorkennis review only audited voorkennis, but the bug is in both converters. Bucket A2 (the converter list-rendering fix) MUST patch both converters to avoid a parallel HF-2 hard-fail surfacing on vaardigheden the next time the review agent inspects it.

### 0.6. `validate-paragraph.js` already reads `*-companion-visual-review.md` — but as a side effect of a buggy filename match

Lines 343-350: `rootFiles.find(f => f === '${parNr}-review.md' || f.endsWith('-review.md'))`. The `endsWith('-review.md')` clause matches BOTH `1.1.1-review.md` AND `1.1.1-companion-visual-review.md`. `find` returns the first hit in fs.readdir order, which on Windows tends to be alphabetical: `1.1.1-companion-visual-review.md` < `1.1.1-review.md`, so the companion review wins. That is why current main FAILs `--mode complete` with "Review has 6 unresolved FAIL item(s): 1.1.1-companion-visual-review.md" even though `1.1.1-review.md` may be clean.

This is good news for Bucket F shrinkage (the validator already integrates the companion review's FAIL state) but BAD news for Bucket E2 design: the integration is unintentional, fragile, picks ONE file at random, and silently ignores the other. F-plan should treat this as a defect to fix, not a design.

The roadmap's claim "validate-paragraph.js ALREADY reads `*-companion-visual-review.md` and FAILs the paragraph if the verdict is FAIL" is therefore **partially true**: it counts FAIL tokens in whichever file the find happens to return first. Surface this contradiction to the user before F-execute.

### 0.7. Skill / agent / review-file alignment is good

The new skill `skills/econ-companion-artifacts.md` "Do not return PASS if" list (line 230-238) maps onto the agent's "FAIL if" list (line 250-257) one-for-one. The voorkennis review file applied them faithfully. There is no contradiction between authoring spec, review spec, and the realised review.

### 0.8. AGENTS.md / BUILD-PARAGRAPH.md / agents/README.md uncommitted edits

These three uncommitted edits and the two new skill files (`skills/econ-companion-artifacts.md` + mirror `.claude/commands/econ-companion-artifacts.md`) form the **first commit** of this branch, dependency of every other item.

### 0.9. Baseline gate state at branch creation

- `npx jest`: green (372/0/7).
- `node scripts/deploy.js`: green (Team B reference HTMLs trigger non-blocking unreachability warnings; expected).
- `npm run check:book` + `validate-paragraph.js --mode complete`: FAIL on review FAIL token count (per 0.6). This will flip to PASS automatically once Buckets A-D land and the review agent re-runs and overwrites `1.1.1-companion-visual-review.md` with PASS / PASS WITH FLAGS.

### 0.10. Style ID `Heading1` collision — also affects `b1-111-vaardigheden.js`?

Roadmap A5 says "If the same pattern exists for `b1-111-vaardigheden.js`, fix in parallel." A grep is the cheapest gate: confirm before A5 ships.

---

## 1. Sprint structure

Six buckets, one feature branch (`content/1.1.1-companion-quality` off platform main `5dcaf2a`), one PR at end. Per-item commits per the roadmap's Sub-agent-driven workflow item 3.

Dependency order (items, not buckets, to surface fine-grained sequencing):
- A0 (skill-wiring-baseline commit) → A1, A4 (parallel) → A2 (parallel with A3) → A3 → A5
- B1 (plan rewrite) → B2 (fig_3 visual) → B3a-e (per-surface 3→4) → B4 (regenerate)
- C1-C6: depend on A1+A4+B done
- D1-D3: depend on A1+A4 done (D2 also needs A2; D3 also needs A3)
- E1-E3: parallel with A-D, finalised after F
- F-plan: parallel with A-D; gated on user approval before F-execute; F-execute runs after F-plan; F-verify after F-execute

The closure proof for the whole sprint is the Verification sub-agent's report PLUS a fresh `1.1.1-companion-visual-review.md` from re-running the review agent (verdict PASS or PASS WITH FLAGS).

---

## 2. Bucket A — Shared platform fixes (ship FIRST)

### A0. Land the new skill + wiring edits as the branch's baseline commit

This is not a roadmap-numbered item, but it is mandatory before A1 because the skill defines the rules A1-A5 honour.

- Files touched (companion worktree):
  - `skills/econ-companion-artifacts.md` (new, untracked — already authored)
  - `.claude/commands/econ-companion-artifacts.md` (new, untracked — mirror of skill)
  - `AGENTS.md` (modified — paired authoring spec line)
  - `BUILD-PARAGRAPH.md` (modified — Phase 6a author + review line)
  - `agents/README.md` (modified — paired authoring spec block)
- Before/after sketch: untracked → tracked + 3 doc-only diffs that reference the skill. No code change.
- Gates after this item: `npx jest` (must stay green); `node scripts/deploy.js` (must stay green); no validator change expected (still FAIL on the existing review file).
- Browser/DOCX smoke target: none.
- Estimated commits: 1.
- Depends on: nothing (clean branch state).
- Risk flags: none. Doc-only.

### A1. Strip `COMPANION VISUAL` label from shared visual frame

- Files touched:
  - `build-scripts/lib/lib-visual-surfaces.js` (line 131 — the production-label `text(...)` emit in the non-slide branch)
- Before/after sketch:
  - Before: lines 128-134 emit a panel rect, then a `text(... "COMPANION VISUAL" ...)`, then title, then subtitle.
  - After: drop the COMPANION VISUAL `text(...)` call entirely. Keep the title (now visually first label) and subtitle. Adjust `contentY` only if the title position changes; preferred is to keep title at `m + 82` so callers don't shift. The label removal frees ~30 px of vertical room above the title, which is safe (tested visually post-regen).
- Gates: `npx jest`. New regression test recommended: `engines/tests/visual-surfaces-no-prod-label.test.js` that requires `/COMPANION VISUAL/` to NOT appear anywhere in the SVG strings emitted by the five `b1-111-visual-variants.js` visuals × five surfaces. Make the test mode-aware so summary/doc/web_light/web_dark/slide all assert. This regression test is the gate that catches HF-1 if it returns.
- Browser/DOCX smoke target: open `_assets/1.1.1_ex_1_web_light.svg`, `_assets/1.1.1_fig_1_web_light.svg`, `_assets/1.1.1_we_1_web_light.svg` directly in the browser; confirm no "COMPANION VISUAL" string anywhere; confirm titles still legible. Re-run vaardigheden.html and voorkennis.html in browser to confirm web variants picked up.
- Estimated commits: 1 (combined: lib edit + variant regen + new jest test). Could split to 2 if the regen volume warrants a separate commit.
- Depends on: A0.
- Risk flags: any other paragraph that has imported `lib-visual-surfaces.js` will lose the label after the next regen. **By design — that's the point.** Currently §1.1.1 is the only book-1 paragraph using these visuals; book-3 paragraphs use `legacy-target/`. Confirm no other paragraph regenerates as part of `b1-XXX-visual-variants.js` runs in this sprint. If any do, surface them — they may be out of scope but can also have the regression test catch.

### A2. Render normal-section list items in BOTH companion converters

This is the single fix that resolves HF-2 at root. The voorkennis review only flagged voorkennis (its scope), but the same code defect exists in the vaardigheden converter (per finding 0.5). Fix once, consistently.

- Files touched:
  - `build-scripts/lib/convert_voorkennis.py` (lines 548-588 — section content loop)
  - `build-scripts/lib/convert_vaardigheden.py` (lines 619-654 — section content loop)
- Before/after sketch: in the per-section content loop, the proper fix is to **buffer consecutive list_items into a single `<ul>`** and flush the buffer when a non-`list_item` element appears or the section ends. Add CSS hook `.section-list { ... }` in `shared/voorkennis.css` so the fix applies to all paragraphs.
- Gates: `npx jest`. NEW jest test required: `engines/tests/companion-html-list-rendering.test.js` that builds a tiny throwaway DOCX with a normal-section List Paragraph item, runs the converter on it, and asserts the rendered HTML contains `<ul>` and `<li>`. After: `node scripts/deploy.js`, `npm run check:book`, `validate-paragraph.js --mode complete`.
- Browser/DOCX smoke target: open `1.1.1 ... uitleg voorkennis.html` — worked-example section shows three Stap-1/2/3 bullets; bar-chart section shows three x-as/y-as/schaal bullets. Open `1.1.1 ... uitleg vaardigheden.html` — list items render as `<ul>/<li>`.
- Estimated commits: 1.
- Depends on: A0.
- Risk flags: All Book-1 paragraphs' companion HTMLs re-render with new `<ul>` rendering. Visually inspect a second paragraph if any other Book-1 voorkennis/vaardigheden HTMLs exist.

### A3. Voorkennis checklist next-step routing block

- Files touched:
  - `build-scripts/lib/convert_voorkennis.py` (lines 602-617 — checklist render)
  - Optionally `build-scripts/content/book-1/b1-111-voorkennis.js` if route data is sourced from the builder (preferred: hard-code the canonical route table from `skills/econ-companion-artifacts.md` line 191-198 in the converter).
- Before/after sketch: after the checklist `</div>` close, add a `checklist-route` block with two route lines (alles afgevinkt → vaardigheden + presentatie; nog niet → relevante sectie + instapquiz). URLs use `prefix` variable already in `process_paragraph`.
- Gates: `npx jest`. NEW jest test: `engines/tests/companion-html-checklist-routes.test.js` asserts the rendered HTML contains a `checklist-route` block with at least one `<a href=...>` link after a checklist.
- Browser/DOCX smoke target: open voorkennis.html, scroll to bottom, confirm "Wat nu?" block. Click both links, confirm they resolve.
- Estimated commits: 1.
- Depends on: A0.
- Risk flags: every paragraph's voorkennis.html will end with a routing block. Routes are paragraph-local; required-file list ensures no 404.

### A4. Meaningful alt-text infrastructure

- Files touched:
  - `_paragraph-plan.md` (visuelen-toewijzing section): add alt-text column or registry subsection.
  - `b1-111-voorkennis.js`, `b1-111-vaardigheden.js`, `b1-111-samenvatting.js`, `b1-111-presentatie.js`, `b1-111-inoefening.js` (all builders that embed images via `embedAssetImage`).
  - `convert_voorkennis.py`, `convert_vaardigheden.py` (descr parsing).
  - New: `build-scripts/content/book-1/b1-111-alt-text.js` — alt-text registry mapping concept-base → meaningful description.
- Before/after sketch: builder accepts `altText` parameter; emits `descr="asset-alt:<text>"` (new convention). Converter recognizes `asset-alt:` prefix and uses it as both DOCX `descr` and HTML `alt`. Backward compat: `asset:` prefix logs a warning. Builder fails loudly if `ALT[base]` missing.
- Gates: `npx jest`. NEW jest test: `engines/tests/companion-alt-text-meaningful.test.js` asserts every embedded asset's HTML `alt` is ≥10 chars + contains a space + isn't asset-id-shaped.
- Browser/DOCX smoke target: devtools inspect `<img>` for `1.1.1_ex_1`; alt = "Staafdiagram met opbrengst per gewas: tarwe €500 per hectare, maïs €350, zonnebloemen €300." Word right-click image → Edit Alt Text shows same string.
- Estimated commits: 2 (split: registry + builders → commit 1; converter + jest test → commit 2). Or 1 if diff small.
- Depends on: A0.
- Risk flags: all 5 §1.1.1 builders touch `embedAssetImage` signature. Other paragraphs share the helper; smoke check.

### A5. Fix duplicate `Heading1` style ID

- Files touched: `b1-111-voorkennis.js` (line 350); possibly `b1-111-vaardigheden.js` (verify with grep).
- Before/after sketch: rename `id: "Heading1"` → `id: "VkHeading1"` (or remove custom style, use built-in).
- Gates: `npx jest`. NEW jest test: `engines/tests/docx-style-ids-unique.test.js` parses styles.xml. Plus run `python build-scripts/render_docx.py --renderer artifact-tool .../uitleg voorkennis.docx` and confirm no `Argument_AddingDuplicateWithKey, Heading1`.
- Browser/DOCX smoke target: open regenerated voorkennis.docx in Word; confirm headings render correctly. Inspect artifact-tool PNG export.
- Estimated commits: 1.
- Depends on: A0 + A4 (if A4 changed builder image-embed signature).
- Risk flags: rename could affect Word styling. Side-by-side compare with old PDF.

---

## 3. Bucket B — Canonical procedure 3 → 4 step propagation

Per finding 0.1 the registry is already canonical. So B1 is reduced to plan rewrite + visual + downstream surfaces.

### B1. Paragraph plan rewrite

- Files touched: `_paragraph-plan.md` lines 15, 30, 69, 103, 112, 139, 174.
- Before/after sketch: each "3-stappen / 3 stappen" → 4-step canonical wording from B02 registry. Line 174's didactic-variant note: rewrite or delete (roadmap chose 4 steps everywhere).
- Gates: `npx jest`, validate-paragraph.
- Estimated commits: 1 (lessen-side).
- Depends on: A0.
- Risk flags: lessen-side commit, separate from platform branch.

### B2. fig_3 visual: 3 cards → 4 cards

- Files touched: `b1-111-visual-variants.js` lines 131-176 (`processSvg`).
- Before/after sketch: 3-card → 4-card layout; recompute cardW for 4 cards. Bottom-example sentence updates to mention netto-waarde. All 5 surface variants (doc/slide/summary/web_light/web_dark) regenerate from same source.
- Gates: `npx jest`. Optional NEW jest test: `engines/tests/fig-3-step-count.test.js` asserts exactly 4 numbered cards. After: `node b1-111-visual-variants.js`, `node scripts/deploy.js`.
- Browser/DOCX smoke target: open each `_assets/1.1.1_fig_3_*.{png,svg}`. Confirm 4 cards visible, all labels readable, no overlap, arrows visible.
- Estimated commits: 1.
- Depends on: A1.
- Risk flags: summary surface (compact 760×440) tight at 4 cards; may need font scale-down or 2×2 stack.

### B3. Content surfaces (3 → 4 step)

- B3a `b1-111-vaardigheden.js`: already 4-step (finding 0.2). **No-op**, smoke-confirm only.
- B3b `b1-111-samenvatting.js` cell rij 3 kolom 1: header + body labels flip to 4 steps. Risk: cell may overflow; smoke check.
- B3c `b1-111-presentatie.js` slide 5: title + 4 bullets + handout text + closing recap. Risk: slide overflow.
- B3d `b1-111-inoefening.js`: Luuk exercise instructie + recap (lines 420, 451) flip.
- B3e `b1-111-opgaven.js` (lines 6, 364, 466, 488, 495, 605): instructie + question stems flip; verify answer keys still match.

### B4. Regenerate-and-verify

- Full per-builder regen + `npx jest` + `deploy.js` + `check:book` + validate-paragraph (will still FAIL on review file until verification sub-agent re-runs review at end of sprint).
- Manual diff per the roadmap: every rendered surface shows step 4 ("Vergelijk opbrengst..."), none shows legacy 3-step header.
- Estimated commits: regen rolls into per-builder commits (B3b-e separate commits with their per-file regen as part of the same commit).

---

## 4. Bucket C — Vaardigheden-specific (after A + B)

### C1. Visual-text synchronization (Lisa €20 / bioscoop €12 / boek €15)

- Files touched: `b1-111-vaardigheden.js` skill 1 narrative + cross-ref `b1-111-visual-variants.js` `scarcitySvg`. Roadmap C1 default: simpler 2-wish framing.
- Risk flags: fig_1 also embeds in samenvatting cell + presentatie slide 3. If fig_1 changes, those re-render and need narrator alignment.

### C2. Worked-example text-completeness (tarwe/maïs explicit table)

- Files touched: `b1-111-vaardigheden.js` skill 2 worked example (lines 510-525). Replace `bullet`/`p` with explicit Table: 5 rows tarwe/maïs/best-niet-gekozen/alt.kosten/nettowaarde.
- Risk: requires generic-table render branch in `convert_vaardigheden.py`. Bundle into A2 (preferred).

### C3. Schaarste checks as structured HTML

- Files touched: `b1-111-vaardigheden.js` skill 1 — replace `tipBox(...)` with `numberedList([...])` so converter sees `list_item`.
- Depends on A2.

### C4. Import Team B scaffold under B01/B02

- Files touched: `b1-111-vaardigheden.js`. Adds three sub-blocks under skill 2: keuzekaart pre-organizer; "prijs en kosten" pitfall; granular checklist + route advice as final block.
- **Constraint**: stay at TWO top-level sections; reviewer must confirm no scope creep into 5+ sections.

### C5. Vaardigheden routing block

- Mirrors A3's idea on vaardigheden: 4 route lines (procedure / BI / basisopgaven / midden+verrijking).
- Bundles with C1+C2+C3 in single commit.

### C6. Visual quality polish

- Terminology fixes (`Mais` → `maïs`, `alt.kosten` → `alternatieve kosten`, no English equivalents). Light/dark contrast WCAG AA.
- NEW jest test: `engines/tests/companion-terminology.test.js` asserts no rendered HTML contains forbidden tokens.

---

## 5. Bucket D — Voorkennis-specific (after A)

### D1. Caption mirroring alt text on bar-chart

- Files touched: `b1-111-voorkennis.js` line 464 + new caption paragraph after `figExImage`.

### D2. Worked-example steps survive regeneration (parity check)

- No commit; verification only, attached to A2 verification.

### D3. Checklist routing block wiring + GitHub Pages link spot-check

- No commit; verification only, attached to A3.

---

## 6. Bucket E — Part A QC integration

### E1. Extend §1.1.1 quality records

- Files touched: `1.1.1-quality-ref.yaml`. Add `companion:` block: `review_verdict`, `last_reviewed`, `hard_fails_open`, `procedure_b02_step_count`, `assets_meaningful_alt`, `checklist_route_present`, `artifact_tool_render_clean`.
- Depends on F-plan deciding final schema.

### E2. Decide validator behavior on companion-review FAIL

- No-op until F-plan returns. Per finding 0.6 the current "integration" is buggy filename match.

### E3. Re-record §1.1.1 closure under chosen schema

- Last commit of sprint (lessen-side). Populate Part A (carry-forward) + Part B (post-regen + final review verdict).

---

## 7. Bucket F — Part A / Part B quality-cycle separation (SHAPE only)

### F-plan inputs

Platform: `BUILD-PARAGRAPH.md`, `BUILD-CHAPTER.md`, `scripts/validate-paragraph.js` (modes + finding 0.6), `skills/` dir listing, `agents/econ-companion-visual-review.md`, `AGENTS.md`.
Lessen: §1.1.1 paragraph folder content listing, `1.1.1-review.md`, `1.1.1-companion-visual-review.md`, `1.1.1-quality-ref.yaml`, roadmap L1.5V Bucket F + L1.4 entry.

### F-plan deliverable shape

Markdown design proposal saved to `docs/L1.5V/F-plan-part-a-b-separation.md`:

1. Mixed-scope section list with proposed split.
2. Final shape of `BUILD-PARAGRAPH.md`: one-file three-section vs two-file split.
3. Validator behaviour: confirm `--mode part-a/part-b/complete`; close gap so `complete` aggregates BOTH review files (resolves finding 0.6).
4. Quality-record schema (resolves E1).
5. Skill ownership table.
6. Test taxonomy.
7. Migration plan (§1.1.1 only).

### F-plan gating

F-plan delivers for user review BEFORE F-execute. Plan-output sub-agent does NOT produce F-plan content.

### F-execute likely items

- F1: restructure `BUILD-PARAGRAPH.md`.
- F2: adjust `validate-paragraph.js` (fix finding 0.6 buggy match).
- F3: implement quality-record schema; migrate §1.1.1.
- F4: update skill files where ownership unclear.
- F5: adjust `agents/README.md` + cross-references.
- F6: update `CLAUDE.md` + `AGENTS.md` "Quality control" sections.

### F-verify

End-to-end on §1.1.1; each gate runs separately Part A and Part B; both pass; aggregate passes. Optional regression: inject HF defects, expect FAIL, revert.

### F closure → L1.4 unblocked

---

## 8. Dependency graph

```
A0 (skill+wiring baseline commit)
  ├─ A1 (production label) ──► B2 (fig_3 4-step) ──► C1 ──► C4
  │                                                        ▲
  │                                                        │
  ├─ A4 (alt text infra) ──► A5 (Heading1 collision)       │
  │      │                                                  │
  │      └─► D1 (caption mirrors alt)                       │
  │                                                          │
  ├─ A2 (list rendering, both converters) ──► C2 ──► C3 ──┘
  │      │
  │      └─► D2 (worked-example parity check)
  │
  └─ A3 (checklist routing voorkennis) ──► C5 (vaardigheden routing reuses CSS)
         │
         └─► D3 (link target spot check)

B1 (plan rewrite, lessen-side) ──► B3a (vaardigheden no-op) 
                              ──► B3b (samenvatting) ──┐
                              ──► B3c (presentatie) ───┤
                              ──► B3d (inoefening) ────┼─► B4 verify
                              ──► B3e (opgaven) ───────┘

C6 (terminology + light/dark)  depends on A1, B2.

E1 (quality-ref schema) ──► E3 (record closure values, last commit)
E2 = no-op pending F-plan
F-plan ──► (user approval) ──► F-execute (F1..F6) ──► F-verify ──► E3

Verification sub-agent (closing): re-runs review agent on both surfaces ──► overwrites 1.1.1-companion-visual-review.md ──► validate-paragraph flips to PASS ──► sprint can land PR.
```

---

## 9. Risk register

| Item | Conflict surface | Mitigation |
|---|---|---|
| A1 (label strip) | Platform-side change to shared frame layout | Re-fetch origin/main; rebase if needed |
| A2 (converter list rendering, BOTH converters) | Same defect family in OTHER converters (samenvatting/nieuws/begeleide-inoefening) | Pre-A2 grep; if found, expand scope or document follow-up |
| A4 (alt-text infra) | `embedAssetImage` signature shared across builders | Re-fetch origin/main; document `asset-alt:` convention in BUILD-PARAGRAPH |
| A5 (Heading1 collision) | `render_docx.py` parallel changes | Run artifact-tool before AND after |
| B2 (fig_3 4-step) | Platform-side change to `b1-111-visual-variants.js` | Re-fetch origin/main |
| B3c (presentatie slide 5) | L1.5D D2 PPTX-as-web work (paused) | Verify D2 still paused |
| C2 (worked-example table) | A2 generic_table rendering | Bundle into A2 |
| F2 (validator modes) | Platform-side `validate-paragraph.js` PRs | Coordinate via PR if parallel work in flight |
| F3 (quality-record schema) | E1 gates on F | Hold E1 commit until F-plan lands |
| Cross-repo two-commit boundary | Platform PR + lessen regen + lessen content commits | Push order: platform → regen → lessen |

---

## 10. Gate-per-defect map

| Defect | Bucket item | Gate |
|---|---|---|
| HF-1 (`COMPANION VISUAL`) | A1 | NEW jest `visual-surfaces-no-prod-label.test.js` |
| HF-2 (HTML drops list items) | A2 (both converters) | NEW jest `companion-html-list-rendering.test.js` |
| HF-3 (no checklist routing) | A3 | NEW jest `companion-html-checklist-routes.test.js` |
| HF-4 (filename-like alt) | A4 | NEW jest `companion-alt-text-meaningful.test.js` |
| QA-1 (Heading1 style collision) | A5 | NEW jest `docx-style-ids-unique.test.js` + artifact-tool render |
| 3 vs 4 step procedure mismatch | B (B1+B2+B3) | NEW jest `fig-3-step-count.test.js` + `companion-procedure-step-count.test.js` |
| Wrong terminology (Mais, alt.kosten) | C6 | NEW jest `companion-terminology.test.js` |
| Visual-text desync | C1 | Manual visual smoke + reviewer Pass 3 |
| Two top-level sections only | C4 | Manual reviewer pass |
| Validator agglomerates Part A + Part B FAILs | F2 | NEW jest `validate-paragraph-modes.test.js` |

---

## 11. Recommended commit plan

Platform side (companion worktree):
1. `chore(skill): land econ-companion-artifacts skill + AGENTS/BUILD-PARAGRAPH/agents-README wiring` — A0
2. `fix(visual-surfaces): drop COMPANION VISUAL production label + jest regression` — A1
3. `fix(converters): render normal-section list items as <ul>/<li> in voorkennis + vaardigheden + jest regression` — A2
4. `feat(converter-voorkennis): emit Wat-nu? routing block after checklist + jest regression` — A3
5. `feat(builders): meaningful alt-text via asset-alt: convention + b1-111-alt-text.js registry + jest regression` — A4
6. `fix(builder-voorkennis): rename custom Heading1 style ID + artifact-tool jest regression` — A5
7. `feat(visual-variants-1.1.1): replace fig_3 3-step → 4-step (B02) + jest step-count regression` — B2
8. `chore(presentatie-1.1.1): slide 5 + handout 3-step → 4-step propagation` — B3c
9. `chore(samenvatting-1.1.1): cell rij 3 kolom 1 3-step → 4-step propagation` — B3b
10. `chore(inoefening-1.1.1): BI scaffold 3-step → 4-step propagation` — B3d
11. `chore(opgaven-1.1.1): basis/midden/verrijking 3-step → 4-step + procedure-step-count regression` — B3e
12. `feat(vaardigheden-1.1.1): visual-text sync + tarwe/maïs table + structured schaarste-checks + Wat-nu? routing` — C1+C2+C3+C5
13. `feat(vaardigheden-1.1.1): import Team B keuzekaart + prijs-vs-kosten pitfall under B02` — C4
14. `chore(visuals-1.1.1): terminology fixes + dark-light contrast polish + jest regression` — C6
15. `feat(voorkennis-1.1.1): caption mirroring alt text on bar-chart visual` — D1

Lessen side (push after platform PR merges):
16. `content(1.1.1): paragraph-plan 3-step → 4-step propagation; remove didactic-variant exemption` — B1
17. `content(1.1.1): regenerated DOCX/HTML/PPTX/SVG/PNG after L1.5V Bucket A-D platform fixes` — regen-only
18. `content(1.1.1): quality-ref companion: section + closure record post-review` — E1+E3+new review file

F-plan (separate gated sub-agent task):
19. `docs(L1.5V): F-plan Part A / Part B quality-cycle separation design proposal` — saved as `docs/L1.5V/F-plan-part-a-b-separation.md`. **STOPS for user review.**

After user approval:
20-25. F-execute commits (F1..F6) + matching jest regression for validator modes (F2 → finding 0.6 fix).
26. F-verify report under `docs/L1.5V/F-verify-1.1.1.md`.

After all commits land: PR to platform main, then lessen push.

---

## Critical files for implementation

- `C:/Projects/4veco/4veco-platform-companion/build-scripts/lib/lib-visual-surfaces.js`
- `C:/Projects/4veco/4veco-platform-companion/build-scripts/lib/convert_voorkennis.py`
- `C:/Projects/4veco/4veco-platform-companion/build-scripts/lib/convert_vaardigheden.py`
- `C:/Projects/4veco/4veco-platform-companion/build-scripts/content/book-1/b1-111-voorkennis.js`
- `C:/Projects/4veco/4veco-platform-companion/build-scripts/content/book-1/b1-111-visual-variants.js`
- `C:/Projects/4veco/4veco-platform-companion/scripts/validate-paragraph.js`
