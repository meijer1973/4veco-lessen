"""
Chapter assembler: combines paragraph markdown files into a single chapter PDF.
Follows the econ-chapter-assembler skill.

Produces:\n  - 1.3 Aanbod en marktevenwicht – hoofdstuk.md / .html / .pdf\n  - 1.3 Aanbod en marktevenwicht – antwoorden.md / .html / .pdf\n"""
import base64, re, os, subprocess, sys
from pathlib import Path

BASE = Path(__file__).parent
MODULE = BASE  # paragraphs are inside the chapter folder
ASSET_DIR = BASE / "_assets"

# ---------------------------------------------------------------------------
# Front page content (from active v5 chapter 1.3: Supply and Market Equilibrium)
# ---------------------------------------------------------------------------
FRONT_PAGE_HTML = """<div class="chapter-front">

<h1>Hoofdstuk 3 — Aanbod en marktevenwicht</h1>

<h2>Inhoud</h2>

<table>
<thead><tr><th>§</th><th>Onderwerp</th></tr></thead>
<tbody>
<tr><td>1.3.1</td><td>Aanbod</td></tr>
<tr><td>1.3.2</td><td>Marktevenwicht</td></tr>
<tr><td>1.3.3</td><td>Verschuivingen en nieuw evenwicht</td></tr>
<tr><td>1.3.4</td><td>Gemengde opgaven</td></tr>
</tbody>
</table>

<h2>Leerdoelen</h2>

<p>Na dit hoofdstuk kun je:</p>

<ul>
<li>Een aanbodlijn tekenen en interpreteren</li>
<li>Het verschil uitleggen tussen een beweging langs de aanbodlijn en een verschuiving van de aanbodlijn</li>
<li>Aanbodfactoren benoemen en gebruiken om verschuivingen te verklaren</li>
<li>Het marktevenwicht berekenen door Qv = Qa op te lossen</li>
<li>Een aanbodoverschot of vraagoverschot herkennen en berekenen</li>
<li>Een nieuw evenwicht berekenen na een verschuiving van vraag of aanbod</li>
<li>Uitleggen wanneer een prijs- of hoeveelheidsverandering eenduidig of onzeker is</li>
</ul>

<h2>Vraag en aanbod komen samen</h2>

<p>In dit hoofdstuk kijk je eerst naar de aanbodkant van de markt. Daarna breng je vraag en aanbod samen: je berekent het marktevenwicht en onderzoekt wat er gebeurt als vraag of aanbod verschuift. Kosten, opbrengsten en marginale analyse horen niet meer bij de gedrukte versie van Boek 1; die stof komt later terug.</p>

</div>"""

# ---------------------------------------------------------------------------
# Paragraph source files (in order)
# ---------------------------------------------------------------------------
PARAGRAPHS = [
    {
        "dir": MODULE / "1.3.1 Aanbod",
        "para": "1.3.1 Aanbod \u2013 paragraaf.md",
        "answers": "1.3.1 Aanbod \u2013 antwoorden.md",
        "asset_prefix": "_assets/",
    },
    {
        "dir": MODULE / "1.3.2 Marktevenwicht",
        "para": "1.3.2 Marktevenwicht \u2013 paragraaf.md",
        "answers": "1.3.2 Marktevenwicht \u2013 antwoorden.md",
        "asset_prefix": "_assets/",
    },
    {
        "dir": MODULE / "1.3.3 Verschuivingen en nieuw evenwicht",
        "para": "1.3.3 Verschuivingen en nieuw evenwicht \u2013 paragraaf.md",
        "answers": "1.3.3 Verschuivingen en nieuw evenwicht \u2013 antwoorden.md",
        "asset_prefix": "_assets/",
    },
    {
        "dir": MODULE / "1.3.4 Gemengde opgaven",
        "para": "1.3.4 Gemengde opgaven \u2013 opgaven.md",
        "answers": "1.3.4 Gemengde opgaven \u2013 antwoorden.md",
        "asset_prefix": "_assets/",
    },
]

# ---------------------------------------------------------------------------
# CSS (same as per-paragraph builds, with front page additions)
# ---------------------------------------------------------------------------
CSS = """<style>
@page {
  size: A4;
  margin: 2cm 2.2cm 2.2cm 3.2cm;
  @bottom-left   { content: "Hoofdstuk 3 \u2014 Aanbod en marktevenwicht"; font-family: Arial, sans-serif; font-size: 9pt; color: #555; }
  @bottom-center { content: counter(page) " / " counter(pages);  font-family: Arial, sans-serif; font-size: 9pt; color: #555; }
}

body {
  font-family: Arial, 'DejaVu Sans', sans-serif;
  font-size: 11pt;
  line-height: 1.45;
  color: #1a1a1a;
  max-width: 100% !important;
  padding: 0 !important;
  margin: 0 !important;
}

p { margin: 0 0 10pt 0; }

/* === FRONT PAGE === */
.chapter-front h1 {
  font-size: 24pt;
  color: #1A5276;
  border-bottom: 3px solid #1A5276;
  padding-bottom: 8px;
  margin-top: 0;
  margin-bottom: 14px;
}

.chapter-front { break-after: page; }

.chapter-front p {
  font-size: 11pt;
  line-height: 1.4;
  margin: 0 0 8pt 0;
}

.chapter-front h2 {
  font-size: 14pt;
  margin-top: 14pt;
  margin-bottom: 6pt;
  padding-bottom: 4pt;
}

.chapter-front ul {
  font-size: 11pt;
  line-height: 1.35;
  margin: 0 0 8pt 0;
}

.chapter-front li {
  margin-bottom: 2pt;
}

/* === HEADINGS === */
h1 {
  font-size: 18pt;
  font-weight: bold;
  color: #1A5276;
  border-bottom: 1.5px solid #1A5276;
  padding-bottom: 5pt;
  margin-top: 0;
  margin-bottom: 18pt;
  break-after: avoid;
}

h2 {
  font-size: 14pt;
  font-weight: bold;
  color: #1A5276;
  border-bottom: 1px solid #999;
  padding-bottom: 4pt;
  margin-top: 22pt;
  margin-bottom: 12pt;
  break-after: avoid;
}

h3 {
  font-size: 12pt;
  font-weight: bold;
  color: #1a1a1a;
  margin-top: 16pt;
  margin-bottom: 6pt;
  break-after: avoid;
}

h1 + p, h2 + p, h3 + p { break-before: avoid; }
h1, h2, h3 { orphans: 3; widows: 3; }

/* === DEFINITION / FORMULA / WARNING BOXES === */
blockquote {
  background: #F4F7FA;
  border-left: 3px solid #1A5276;
  padding: 8pt 12pt;
  margin: 12pt 0;
  font-size: 10.5pt;
  line-height: 1.4;
  break-inside: avoid;
}

blockquote p { margin: 0 0 6pt 0; }
blockquote p:last-child { margin-bottom: 0; }
blockquote strong:first-child { color: #1A5276; }

/* === TABLES === */
table {
  border-collapse: collapse;
  width: 100%;
  margin: 12pt 0;
  font-size: 10.5pt;
  break-inside: avoid;
}

th {
  background: #EDF0F3;
  color: #1a1a1a;
  font-weight: bold;
  padding: 3pt 6pt;
  text-align: left;
  border: 1px solid #999;
}

td {
  border: 1px solid #999;
  padding: 2pt 6pt;
}

tr:nth-child(even) td { background: #FAFBFC; }

/* === FIGURES === */
figure {
  margin: 14pt 0;
  break-inside: avoid;
  text-align: center;
}

figure img {
  max-width: 100%;
  width: 100%;
  display: block;
  margin: 0 auto;
}

figcaption {
  font-weight: bold;
  font-size: 10.5pt;
  color: #1a1a1a;
  text-align: left;
  margin-top: 6pt;
}

img {
  max-width: 100%;
  width: 100%;
  display: block;
  margin: 14pt auto;
  break-inside: avoid;
}

p + figure, p + p > img { break-before: avoid; }

/* === EXERCISES === */
.exercise {
  margin-bottom: 14pt;
  orphans: 2;
  widows: 2;
}

.exercise > p:first-child {
  break-after: avoid;
  page-break-after: avoid;
}

.exercise p {
  margin: 0 0 1pt 0;
}

/* === MISC === */
code {
  background: #EDF2F7;
  padding: 1pt 5pt;
  border-radius: 3px;
  font-family: 'Consolas', 'DejaVu Sans Mono', monospace;
  font-size: 10pt;
}

hr {
  border: none;
  border-top: 1px solid #BBB;
  margin: 18pt 0;
}

em { color: #444; }
ul, ol { margin: 0 0 10pt 0; padding-left: 20pt; }
ol[type="a"] { list-style-type: lower-alpha; }
li { margin-bottom: 4pt; }
</style>"""


def embed_images(md):
    """Replace image references with base64-embedded PNGs."""
    def replacer(match):
        alt = match.group(1)
        path = match.group(2).replace(".svg", ".png")
        full = ASSET_DIR / os.path.basename(path)
        if full.exists():
            b64 = base64.b64encode(full.read_bytes()).decode()
            return f'![{alt}](data:image/png;base64,{b64})'
        print(f"  Warning: missing {full}")
        return match.group(0)
    return re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', replacer, md)


def wrap_exercises(html):
    """Wrap each Opgave block in a div for page-break control."""
    html = re.sub(
        r'<p><strong>(Opgave \d+)',
        r'</div><div class="exercise"><p><strong>\1',
        html
    )
    html = html.replace('</div><div class="exercise">',
                        '<div class="exercise">', 1)
    html = re.sub(r'(<h[23])', r'</div>\1', html)
    return html



def rebalance_table_columns(html):
    """Analyze tables and set column widths proportional to content length."""
    import html as html_mod
    from html.parser import HTMLParser

    class CellExtractor(HTMLParser):
        """Extract cell text content and structure from a table."""
        def __init__(self):
            super().__init__()
            self.tables = []
            self.current_table = None
            self.current_row = None
            self.current_cell = None
            self.in_cell = False
            self.depth = 0
        def handle_starttag(self, tag, attrs):
            if tag == 'table': self.current_table = []
            elif tag == 'tr' and self.current_table is not None: self.current_row = []
            elif tag in ('td', 'th') and self.current_row is not None:
                self.current_cell = ''; self.in_cell = True
        def handle_endtag(self, tag):
            if tag in ('td', 'th') and self.in_cell:
                self.current_row.append(self.current_cell.strip())
                self.current_cell = None; self.in_cell = False
            elif tag == 'tr' and self.current_row is not None:
                if self.current_row: self.current_table.append(self.current_row)
                self.current_row = None
            elif tag == 'table' and self.current_table is not None:
                self.tables.append(self.current_table); self.current_table = None
        def handle_data(self, data):
            if self.in_cell: self.current_cell += data

    parser = CellExtractor()
    parser.feed(html)
    tables = list(re.finditer(r'<table[^>]*>.*?</table>', html, re.DOTALL))
    if len(tables) != len(parser.tables): return html
    modified = 0; offset = 0
    for i, (match, cells) in enumerate(zip(tables, parser.tables)):
        if not cells or len(cells) < 2: continue
        ncols = max(len(row) for row in cells)
        if ncols < 2: continue
        max_lens = [0] * ncols
        for row in cells:
            for j, cell in enumerate(row):
                if j < ncols: max_lens[j] = max(max_lens[j], len(cell))
        total_chars = sum(max_lens)
        if total_chars == 0: continue
        raw = [max(max_lens[j], 2) for j in range(ncols)]
        total_raw = sum(raw)
        widths = [max(8, round(r / total_raw * 100)) for r in raw]
        total_w = sum(widths)
        if total_w != 100: widths[widths.index(max(widths))] += 100 - total_w
        cols = ''.join(f'\n<col style="width: {w}%" />' for w in widths)
        colgroup = f'<colgroup>{cols}\n</colgroup>\n'
        table_html = match.group()
        existing_cg = re.search(r'<colgroup>.*?</colgroup>\s*', table_html, re.DOTALL)
        if existing_cg:
            new_table = table_html[:existing_cg.start()] + colgroup + table_html[existing_cg.end():]
        else:
            tag_end = table_html.index('>') + 1
            new_table = table_html[:tag_end] + '\n' + colgroup + table_html[tag_end:]
        start = match.start() + offset; end = match.end() + offset
        html = html[:start] + new_table + html[end:]
        offset += len(new_table) - len(table_html); modified += 1
    print(f"  Rebalanced columns on {modified} tables")
    return html




def rewrite_asset_paths(md, old_prefix):
    """Rewrite image paths to point to the chapter _assets/ folder."""
    md = md.replace(f']({old_prefix}', '](_assets/')
    return md


def assemble_chapter():
    """Assemble chapter markdown from front page + paragraphs."""
    parts = [FRONT_PAGE_HTML.strip()]

    for p in PARAGRAPHS:
        md_path = p["dir"] / p["para"]
        if not md_path.exists():
            print(f"ERROR: missing {md_path}")
            sys.exit(1)
        md = md_path.read_text(encoding="utf-8")
        md = rewrite_asset_paths(md, p["asset_prefix"])
        # Page break before each paragraph
        parts.append(f'\n<div style="break-before: page;"></div>\n\n{md.strip()}')

    return "\n\n".join(parts)


def assemble_answers():
    """Assemble answer booklet from all paragraph answer files."""
    parts = ["# Antwoorden Hoofdstuk 3 \u2014 Aanbod en marktevenwicht"]

    for p in PARAGRAPHS:
        ans_path = p["dir"] / p["answers"]
        if not ans_path.exists():
            print(f"ERROR: missing {ans_path}")
            sys.exit(1)
        md = ans_path.read_text(encoding="utf-8")
        md = rewrite_asset_paths(md, p["asset_prefix"])
        parts.append(f'\n<div style="break-before: page;"></div>\n\n{md.strip()}')

    return "\n\n".join(parts)


def md_to_pdf(md, output_stem):
    """Convert markdown string to HTML and PDF."""
    md = embed_images(md)

    # Strip difficulty rating emojis
    md = re.sub(r'[\u2B1C\U0001F7E8\U0001F7E5]\s*(LIGHT|MEDIUM|HEAVY)', '', md)

    # Strip GRAPH SPEC code blocks
    md = re.sub(r'```\s*\nGRAPH SPEC:.*?\n```\s*\n', '', md, flags=re.DOTALL)

    # Pandoc: markdown -> HTML5
    result = subprocess.run(
        ["pandoc", "--from=markdown", "--to=html5", "--standalone"],
        input=md.encode("utf-8"), capture_output=True
    )
    if result.returncode != 0:
        print(f"Pandoc error: {result.stderr.decode()}")
        sys.exit(1)
    html = result.stdout.decode("utf-8")

    # Wrap exercises — only in content after the front page div
    front_marker = html.find('class="chapter-front"')
    if front_marker != -1:
        page_break_idx = html.find('<div style="break-before: page;">', front_marker)
        if page_break_idx != -1:
            close_idx = html.rfind('</div>', front_marker, page_break_idx)
            if close_idx != -1:
                split_at = close_idx + len('</div>')
                html = html[:split_at] + wrap_exercises(html[split_at:])
            else:
                html = html[:page_break_idx] + wrap_exercises(html[page_break_idx:])
        else:
            html = wrap_exercises(html)
    else:
        html = wrap_exercises(html)

    # Rebalance table column widths based on content
    html = rebalance_table_columns(html)

    # Strip Pandoc default stylesheet, then inject our own
    html = re.sub(r'<style>\s*/\* Default styles provided by pandoc.*?</style>', '', html, flags=re.DOTALL)
    html = html.replace("</head>", CSS + "</head>")

    # Save HTML
    html_path = str(BASE / f"{output_stem}.html")
    Path(html_path).write_text(html, encoding="utf-8")
    print(f"HTML created: {html_path}")

    # Save PDF
    pdf_path = str(BASE / f"{output_stem}.pdf")
    try:
        import weasyprint
        weasyprint.HTML(string=html).write_pdf(pdf_path)
        print(f"PDF created: {pdf_path}")
        return
    except Exception as e:
        print(f"Weasyprint unavailable ({type(e).__name__}). Trying headless Chrome.")

    chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    abs_output = os.path.abspath(pdf_path)
    abs_html = os.path.abspath(html_path)
    if os.path.exists(chrome):
        result = subprocess.run([
            chrome,
            "--headless",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={abs_output}",
            "file:///" + abs_html.replace("\\", "/")
        ], capture_output=True, text=True)
        if os.path.exists(pdf_path):
            print(f"PDF created via headless Chrome: {pdf_path}")
        else:
            print(f"Chrome PDF generation failed: {result.stderr}")
    else:
        print(f"No PDF engine available. HTML saved: {html_path}")


if __name__ == "__main__":
    # 1. Assemble chapter markdown
    print("=== Assembling chapter ===")
    chapter_md = assemble_chapter()
    chapter_md_path = BASE / "1.3 Aanbod en marktevenwicht \u2013 hoofdstuk.md"
    chapter_md_path.write_text(chapter_md, encoding="utf-8")
    print(f"Markdown saved: {chapter_md_path}")

    # 2. Assemble answer booklet markdown
    print("\n=== Assembling answer booklet ===")
    answers_md = assemble_answers()
    answers_md_path = BASE / "1.3 Aanbod en marktevenwicht \u2013 antwoorden.md"
    answers_md_path.write_text(answers_md, encoding="utf-8")
    print(f"Markdown saved: {answers_md_path}")

    # 3. Build PDFs
    print("\n=== Building chapter PDF ===")
    md_to_pdf(chapter_md, "1.3 Aanbod en marktevenwicht \u2013 hoofdstuk")

    print("\n=== Building answer booklet PDF ===")
    md_to_pdf(answers_md, "1.3 Aanbod en marktevenwicht \u2013 antwoorden")

    print("\n=== Done ===")
