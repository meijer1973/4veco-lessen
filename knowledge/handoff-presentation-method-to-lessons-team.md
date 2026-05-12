# Handoff: PowerPoint Production Method

**From:** Innovation Team (collab work 3, Sprint I2 — flowchart prototype)
**To:** Lessons Team
**Date:** 2026-04-27
**Status:** Method ready for adoption; skill updates recommended before production rollout.

---

## TL;DR

We rebuilt a flowchart-heavy paragraph deck (1.2.2 Vraagfactoren) from a set of mockups, this time as **code-generated native PowerPoint** instead of hand-edited slides. The result is editable, geometrically precise, reproducible, and roughly 4× smaller on disk than the manual version. This document describes the method so the lessons team can adopt it for their own presentation work, and lists concrete improvements we suggest making to the existing skills before doing so.

The method does **not** require Claude. It is a normal Node + PptxGenJS workflow that any team member can run, edit, and re-run.

---

## What we built (reference artifact)

- Source mockups: `Boek 1 - Grondslagen, vraag en aanbod/1.2 Hoofdstuk Vraag/1.2.2 Vraagfactoren/improved_powerpoint_slides_png/` (8 PNG slide designs)
- Builder script: `1.2.2 Vraagfactoren/build_presentation_v2.js`
- Output deck: `1.2.2 Vraagfactoren – presentatie-flowchart-prototype-v2-Claude.pptx`

The builder is one Node file living next to the paragraph it produces. Re-running it overwrites the deck. Nothing else changes.

---

## Why this method, in one paragraph

Presentations that get hand-edited drift over time. Colors don't match across slides. Box widths walk by one or two pixels per slide. PowerPoint silently rounds positions and corrupts files when XML is touched manually (the file we received was literally named "Repaired 1"). When a teacher asks for a small wording change six months later, nobody remembers which color the green cards used. Code-generated decks fix all of this: the deck **is** the script. Open the script, change a value, re-run, ship.

---

## The method, in seven steps

### 1. Sketch first as PNGs (mockup contract)

Draw the slides as static images first — Figma, Excalidraw, even a quick AI sketch. This is the **design contract**. Once you have it, the work shifts from "what should this look like" to "how do I translate this layout into code". Keep mockups committed to the paragraph folder under `improved_powerpoint_slides_png/` (or similar). They become the visual diff target.

### 2. Steal the palette from a strong reference

Don't pick colors from scratch. Open a PowerPoint file you like (`.pptx` is a zip — `unzip -p file.pptx ppt/slides/slide1.xml`), pull the exact `srgbClr` hex values, and put them in a single `C` constant at the top of the builder. The deck we built uses the v1 palette: deep navy `050F25`, red `FF6B5B`, green-tinted `2E5E3A` / `E8F4EC`, amber-tinted `8A5A0E` / `FDF3E0`, cream `F9F7F1`. Reusing these means the new deck visually belongs in the existing book.

### 3. Build with one shape per slide region, never with screenshots

Each slide is a sequence of `addShape`, `addText`, `addImage` calls. **Do not embed mockup PNGs into the deck** — the deck must be editable. The mockups are the contract; the code is the artifact. Side benefit: file size drops from ~1.1 MB per embedded mockup to ~40 KB per slide of native shapes.

### 4. Define small reusable helpers

Pull out the repeated visual idioms into helpers at the top of the builder:

- `darkBg(slide)` / `lightBg(slide)` — slide background + top accent line
- `darkFooter(slide, page)` / `lightFooter(slide, page)` — page number circle + breadcrumb
- `topTag(slide, "FACTORENKAART", color)` — letter-spaced section label
- `numBadge(slide, x, y, n, color)` — numbered circle for steps
- `arrow(slide, x1, y1, x2, y2, color)` — directional connector with arrowhead
- `pillCard(slide, {...})` — rounded rectangle with centered text

Six helpers cover most of a deck. They take ~80 lines of code and they make every subsequent slide three lines instead of thirty.

### 5. Render graphs as inline SVG, then `sharp` to PNG

PowerPoint's native shape tools cannot draw an economically correct demand curve. Don't try. Build the graph as an SVG string (full control over axes, labels, dashed gridlines, arrowhead markers, point coordinates), then convert with `sharp` and embed:

```javascript
const png = await svgToPng(buildDemandGraphSvg(), 720, 540);
slide.addImage({ data: png, x: 0.6, y: 1.85, w: 5.3, h: 3 });
```

This gives geometric precision (the kind the `economic-graph` skill demands) without manual fiddling. The graph is regenerated from code each build — no stale embedded images.

### 6. Render-and-verify loop with LibreOffice + pdftoppm

After every change, run the deck through LibreOffice headless and convert to PNG:

```bash
soffice --headless --convert-to pdf --outdir /tmp/check "deck.pptx"
pdftoppm -r 96 -png "/tmp/check/deck.pdf" /tmp/check/slide
```

You now have eight `slide-N.png` files. Open them, compare to the mockups, fix issues, repeat. This loop caught two real bugs in our work that visual inspection in PowerPoint would have missed:

- `charSpacing` rendered far more aggressively in LibreOffice than in PowerPoint, exploding section labels into one-character-per-column.
- A footer bar overlapped the bottom takeaway on slide 7 because positions added up to past the footer line.

If the deck looks good in both LibreOffice **and** PowerPoint, it will look good for any teacher.

### 7. Speaker notes are non-negotiable

Every slide gets `slide.addNotes("...")` with the teaching script: what to say, what to ask, what the common misconception is. This is not optional. A presentation without notes is a teacher's problem, not a finished artifact. The notes also feed Sprint I7 (speaker-notes-to-speech) downstream, so the work pays double.

---

## What we recommend the lessons team change

### Change 1 — Stop hand-editing slides for any deck longer than ~3 slides

If a deck is going to live and be edited and shipped to teachers, build it from a script. Hand-edited decks accumulate drift, get "Repaired" by PowerPoint, and become impossible to update consistently. Keep hand-editing for one-off or throwaway material.

### Change 2 — One builder file per paragraph, committed next to the paragraph

The convention we used: `build_presentation_v2.js` sits in the paragraph folder, alongside `– paragraaf.md`, `– opgaven.md`, `_assets/`, and the output `.pptx`. Re-running the script regenerates the deck. The script **is** the deck's source code. Treat it like one.

### Change 3 — Move every "color" into one palette object

If you grep the existing decks you'll find the same blue used at three slightly different hex codes. Define a `C` constant once, reference it everywhere. When the design language tightens (Sprint I3), one edit propagates to every deck.

### Change 4 — Stop drawing graphs in PowerPoint

Use SVG (or, for very simple cases, the `economic-graph` skill's helpers). PowerPoint shape-drawing for an MK/GTK/GVK trio or a shifting demand curve is a guaranteed source of geometric error and will fail review.

### Change 5 — Add the LibreOffice render check to the deck QA checklist

PowerPoint will hide rendering issues that LibreOffice exposes (and vice versa). Two-engine verification is cheap (~15 seconds) and catches the bugs that teachers would otherwise hit.

### Change 6 — Treat speaker notes as part of the deliverable, not an extra

A deck without notes is half a deck. The rubric should reject decks that ship without notes per slide.

---

## Recommended skill updates

These are concrete improvements to existing skills, written so they can be applied without further design work.

### `econ-pptx-templates` — extend with a "builder pattern" section

The current skill is a strong reference for the visual design system (palette, masters, components). It is missing the **production workflow**. Add:

- **Section: Builder file conventions.** One `build_presentation.js` per paragraaf, lives next to the paragraph markdown, output goes alongside it. Include the `NODE_PATH` workaround for globally-installed pptxgenjs and sharp on Windows (this bit us; document it once).
- **Section: Mockup-first workflow.** Mockup PNGs go into `improved_powerpoint_slides_png/` (or equivalent). They are the design contract; the code reproduces them as native shapes.
- **Section: Render-and-verify loop.** The `soffice --headless` + `pdftoppm` recipe with the exact commands. Half a page; high payoff.
- **Section: Pitfalls catalog (rendering).** Add the ones we hit:
  - `charSpacing` renders far wider in LibreOffice than expected. For letter-spaced labels, prefer `text.split("").join(" ")` over `charSpacing`. The behavior in PowerPoint vs. LibreOffice diverges enough that the explicit-spaces approach is the only portable answer.
  - The light-footer accent line sits at `y = SLIDE_H - 0.5`. Any content with `y + h > 5.1` will collide with it. Same rule for dark footer at `SLIDE_H - 0.6`.
  - SVG titles must clear top-of-graph labels — leave `m.t = 50` not `m.t = 30` if you want a label band above the axes.
- **Section: Reusable helpers.** Add the six helpers listed above (`darkBg`, `topTag`, `numBadge`, `arrow`, `pillCard`, footers) as drop-in code, not just prose. The current skill describes the *components*; what's missing is the *plumbing*.

### `economic-graph` — link explicitly to the SVG-into-pptx pattern

The skill already covers economic correctness. Add a small section showing the `svgToPng` (sharp) bridge so a graph SVG can be embedded directly into a slide via `slide.addImage({ data: ... })`. Today, anyone using the skill has to figure out the bridge themselves.

### New mini-skill: `pptx-render-check`

A tiny skill that just documents the LibreOffice + pdftoppm verification loop. Two pages. It can be invoked from any of the building skills as part of the QA gate. Avoids duplicating the recipe in three places.

### `econ-word-templates` — no changes needed for this work

The Word skill is solid; the same palette already lives there. The only suggestion is to add a one-line cross-reference: "Colors here match `econ-pptx-templates`. If you change a hex value, change both."

---

## Pitfalls catalog (carry these forward)

| Pitfall | Symptom | Mitigation |
|---|---|---|
| Globally-installed pptxgenjs / sharp not found | `Cannot find module 'pptxgenjs'` from a paragraph folder | Set `NODE_PATH=C:/Users/<you>/AppData/Roaming/npm/node_modules` before `node build...` |
| `charSpacing: 22` explodes in LibreOffice | Each letter on its own line | Use `text.split("").join(" ")` for letter-spaced labels |
| Footer overlap | Bottom card clipped | Keep content `y + h ≤ 5.05` for light footer, `≤ 5.0` for dark footer |
| SVG title clipped | Title cuts into axis area | Set graph SVG `m.t ≥ 50` |
| Reused option object | Shadow appears on the wrong shape | Use `shadow()` factory, not a shared variable |
| `breakLine: true` for bullets | All bullets render as one paragraph | Use `items.join("\n")` with `bullet: true` |
| Hex colors with `#` prefix | Corrupts the pptx | Always pass plain hex, no `#` |
| Manual `.pptx` edits | "Repaired" suffix appears, file silently corrupts | Edit the builder, never the binary |

---

## Suggested next actions for the lessons team

1. **Read the v2 builder end to end.** It is ~600 lines of straightforward JavaScript. The patterns will land faster from the code than from this document.
2. **Pick one upcoming paragraph** (graph-heavy preferred — Sprint I1 territory) and rebuild it using the builder pattern. Use the existing helpers; add ones you need. Don't invent a new design system.
3. **Run the LibreOffice render check on it.** Compare against PowerPoint's own render. File any divergence as a pitfall to add to the catalog above.
4. **Send the rubric team the failure modes you hit.** Sprint I3 needs them as input. Bug reports are evidence; opinions are not.
5. **Decide whether to fold the builder pattern into `econ-pptx-templates` or split it into a new `econ-pptx-builder` skill.** Our recommendation: extend the existing skill — the design system and the builder belong together.

---

## What is *not* in scope for this handoff

- Web-native delivery (Sprint I5). The builder produces `.pptx`; web rendering is a separate experiment.
- Speaker-notes narration (Sprint I7). The notes are written; turning them into audio is downstream.
- Rubric revision (Sprint I3). The pitfalls catalog above is input to that work, not a replacement for it.
- Bulk migration of existing decks. Adopt the method on new work first; migrate older decks only when they need substantive changes anyway.

---

## Open questions for the lessons team

- Is `Boek 1 - …/X.Y Hoofdstuk …/X.Y.Z paragraaf/build_presentation.js` the right home for the builder, or should builders live centrally in the platform repo with a paragraph argument? (We chose local; arguments either way.)
- Should the QA checklist require both PowerPoint **and** LibreOffice render to pass, or only one? (Innovation team's view: both, because teachers use both.)
- Should we ship a `Makefile` or `npm run build:pres -- 1.2.2` wrapper, or is `node build_presentation_v2.js` per folder good enough? (Innovation team's view: wrapper once we have ≥3 builder scripts in flight.)

We are happy to walk through the v2 builder live with anyone on the lessons team. Ping us in the collab thread.

— Innovation Team, collab work 3
