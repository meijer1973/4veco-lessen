# Book 4 — revised theory explanations: overview of changes

**Date:** 16 November 2026
**Basis:** current v3 edition, `4veco-lessen` at `01ebd47` (`edities/books34-v3/books/book-4`), platform at `82e6cb3f`.
**Status:** review proposal. The governed edition is not changed.

## What is in this folder for Book 4

| File | What it is |
|---|---|
| `Boek_4_Compleet_v3_theorie-herzien.pdf` | The complete student book, 166 pages, with the revised theory. |
| `Boek_4_theorie_voor-en-na.pdf` | The 18 changed pages side by side: current edition left, revision right. |
| `manuscripten/4.x/4.x.y manuscript.md` | The eleven edited manuscripts. |
| `theorie-wijzigingen.diff` | Exact text differences per manuscript. |

## How Book 4 differs from Book 3

Book 4's theory was already stronger than Book 3's. Most results came with their reason, examples came before rules, and the misconception boxes sat next to the idea they belong to. A rewrite on the scale of Book 3 would have changed text that was already good.

So this revision is targeted: 22 edits in 11 of the 14 theory paragraphs, on 18 pages. Three paragraphs are unchanged (4.2.6, 4.3.2, 4.3.3). No example, number, table or figure changed.

## What was and was not changed

Changed: specific sentences in the explanation pages, worked examples and five *Onthouden* boxes.

Not changed:

- All exercises, from *Startopgaven* onward: byte-identical in every manuscript.
- All *Lesdoelen*.
- All examples and their numbers, all tables, all figures and their pages.
- Chapter openers, mixed paragraphs, chapter overviews, glossary, formula pages, front matter.
- Page count, page numbers, outline (24 entries) and all 74 internal links.
- Stylesheet, fonts and components.

## Changes per paragraph

Page numbers are those of the complete book.

### 4.1.1 Toetreding, uittreding en langetermijnevenwicht (p. 7–10)

- p. 7: *normale beloning* is now explained as what the entrepreneur could have earned elsewhere with his time and money.
- p. 8: says why firms enter (the € 100 is profit above the normal reward) and why entry stops at zero economic profit. **One explanation was wrong and is corrected.** The text said a firm sells less "because there are more firms serving the market". A price taker sells less because the price fell: at € 6, MO = MK gives q = 40. The text now shows that calculation.
- p. 9: a loss is tied to earning less than the normal reward, which is why firms leave; the price rise is stated.
- p. 10: the worked example says why the end point is the minimum of GTK.

### 4.1.2 Monopolie: kenmerken (p. 17–18)

- p. 17: explains why the monopolist's demand curve slopes down: it is the market demand curve, and selling more means reaching buyers who value the product less.
- p. 18: *Onthouden* was a chain of arrows; it is now four sentences.

### 4.1.3 Marginale opbrengst bij monopolie (p. 24, 28)

- p. 24: after the opening figure, one sentence turns the € 100 into € 10 per extra kg and sets it against the price of € 14. The paragraph's central point (MO below P) is now visible on the first page.
- p. 28: *Onthouden* rewritten as sentences, with the reason why MO lies below P.

### 4.1.4 Winstmaximalisatie bij monopolie (p. 40)

- p. 40: *Onthouden* rewritten as the steps of the method in sentences.

### 4.2.1 Welvaartseffecten van monopolie (p. 56)

- p. 56: a new short paragraph answers the question the page raises but did not answer: why does the monopolist stop at 20 when units 21 to 30 are worth more to buyers than they cost? Because selling them means lowering the price for all customers, so MO lies below MK there. This is the cause of the welfare loss on the next page.

### 4.2.2 Prijsdiscriminatie (p. 63, 65)

- p. 63: the opening asks why the hall does not charge everyone the same price. The theory never answered it. A short paragraph now does: with one price the hall either loses price-sensitive visitors or asks too little from the others.
- p. 65: the worked example says which group gets the higher price and why.

### 4.2.3 Marktvormen vergelijken (p. 71)

- p. 71: explains why product differences give a firm some room to set its own price, and makes the interdependence in an oligopoly concrete.

### 4.2.4 Negatieve externe effecten (p. 82)

- p. 82: *Onthouden* rewritten from an arrow chain into sentences, including why the same tax that lowered welfare in Book 3 can raise it here.

### 4.2.5 Positieve externe effecten (p. 93)

- p. 93: *Onthouden* rewritten from an arrow chain into sentences.

### 4.3.1 Arbeidsvraag en arbeidsproductiviteit (p. 114, 117)

- p. 114: the sentence about bicycles and mechanics started with "dus" but did not follow from the lines before it. It now states the idea first: employers want labour for what they can make and sell with it.
- p. 117: says why labour demand falls when the wage rises: an employer uses labour as long as it yields more than it costs.

### 4.3.4 Minimumloon (p. 142)

- p. 142: adds why demand falls and supply rises at the higher wage, and why employment equals labour demand (employers decide how many people they hire).

## Points to decide before integration

- **Five *Onthouden* boxes changed** (4.1.2, 4.1.3, 4.1.4, 4.2.4, 4.2.5). Lesdoelen are untouched.
- **4.1.1, p. 8** contains the one substantive correction. It is worth a second pair of eyes.
- **Integration is a separate step**, as for Book 3: a new revision record, rebuilt paragraph PDFs and refreshed target-record source hashes. The presentations for §4.1.1, §4.3.2 and §4.3.5 were not checked against the new wording.

## How this was verified

- Same pinned renderer and fonts as for Book 3. The unchanged Book 4, rebuilt before any edit, was identical to the repository PDF on all 166 pages.
- The rebuilt chapters have 48, 60 and 44 pages with no overflow.
- Against the accepted book: 166 pages, identical outline, identical links, text changed on exactly the 18 pages listed above, and no pixel difference on any other page.
- Every changed page was inspected as rendered.

## Known limitations

- **No independent review.** The edits and the checks are mine alone.
- **One page is close to the bottom margin.** Page 142 has 34 pt left.
