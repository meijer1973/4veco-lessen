"""
Chapter assembler: combines test preparation paragraph markdown files into a single chapter PDF.
Follows the econ-chapter-assembler skill.

Produces:
  - 1.5 Toetsvoorbereiding – hoofdstuk.md / .html / .pdf
  - 1.5 Toetsvoorbereiding – antwoorden.md / .html / .pdf

WeasyPrint is strongly preferred over headless Chrome: Chrome ignores
`break-inside: avoid` on block elements, which causes test questions to
be split across pages. WeasyPrint honors it.

WeasyPrint needs the MSYS2 DLLs (Pango, Cairo, …) on PATH. Append them
to PATH — never prepend, or the MSYS2 Python shadows the system Python
and the `import weasyprint` in this script fails.
"""
import base64, re, os, subprocess, sys, shutil, glob
from pathlib import Path

_MSYS2 = r"C:\msys64\mingw64\bin"
if os.path.isdir(_MSYS2) and _MSYS2 not in os.environ.get("PATH", ""):
    os.environ["PATH"] = os.environ.get("PATH", "") + os.pathsep + _MSYS2

BASE = Path(__file__).parent
MODULE = BASE  # paragraphs are inside the chapter folder
ASSET_DIR = BASE / "_assets"

# ---------------------------------------------------------------------------
# Front page content (Chapter 5: Test Preparation for Book 1)
# ---------------------------------------------------------------------------
FRONT_PAGE_HTML = """<div class="chapter-front">

<h1>Hoofdstuk 5 \u2014 Toetsvoorbereiding</h1>

<h2>Inhoud</h2>

<table>
<thead><tr><th>\u00a7</th><th>Onderwerp</th></tr></thead>
<tbody>
<tr><td>1.5.1</td><td>Actieve samenvatting</td></tr>
<tr><td>1.5.2</td><td>Examenvaardigheden</td></tr>
<tr><td>1.5.3</td><td>Integratieoefening</td></tr>
<tr><td>1.5.4</td><td>Proeftoets</td></tr>
</tbody>
</table>

<h2>Leerdoelen</h2>

<p>Na dit hoofdstuk kun je:</p>

<ul>
<li>De kernbegrippen uit hoofdstukken 1\u20134 actief ophalen en toepassen</li>
<li>Schaarste, alternatieve kosten en economisch denken herkennen en berekenen</li>
<li>Procentuele veranderingen en indexcijfers correct berekenen (inclusief de valkuil indexpunten \u2260 procenten)</li>
<li>De vraaglijn en aanbodlijn tekenen, aflezen en interpreteren</li>
<li>Het verschil uitleggen tussen een beweging langs en een verschuiving van een vraaglijn of aanbodlijn</li>
<li>Kostenstructuren berekenen (TK, TCK, TVK, GTK, GVK, GCK) en het spreidingseffect verklaren</li>
<li>TO, GO en winst berekenen en het break-evenpunt bepalen</li>
<li>Het marktevenwicht berekenen (Qv = Qa) en een nieuw evenwicht na een verschuiving</li>
<li>MK en MO berekenen en de winstmaximalisatieregel (MO = MK) toepassen</li>
<li>Examenvragen correct structureren: \u2018bereken\u2019 met alle stappen, \u2018leg uit\u2019 met causale keten</li>
<li>Concepten uit meerdere hoofdstukken combineren in \u00e9\u00e9n samenhangende context</li>
<li>Een toets onder tijdsdruk maken en je eigen antwoorden beoordelen</li>
</ul>

<h2>Ben je er klaar voor?</h2>

<p>Je hebt geleerd over schaarste en keuzes, over vraag en aanbod, over kosten en opbrengsten, en over marktevenwicht en marginale analyse. Maar kun je al die puzzelstukken ook samenvoegen als het erop aankomt? In dit hoofdstuk bereid je je voor op de eindtoets. Je herhaalt actief de theorie, traint je examenvaardigheden, lost een integratieoefening op die alle hoofdstukken combineert, en maakt een volledige proeftoets onder examencondities. Geen nieuwe theorie \u2014 alleen oefenen, oefenen, oefenen.</p>

</div>
"""

# ---------------------------------------------------------------------------
# Paragraph source files (in order)
# Test prep chapter: different file types per paragraph
# ---------------------------------------------------------------------------
PARAGRAPHS = [
    {
        "dir": MODULE / "1.5.1 Actieve samenvatting",
        "para": "1.5.1 Actieve samenvatting \u2013 samenvatting.md",
        "answers": "1.5.1 Actieve samenvatting \u2013 antwoorden.md",
        "asset_prefix": "_assets/",
    },
    {
        "dir": MODULE / "1.5.2 Examenvaardigheden",
        "para": "1.5.2 Examenvaardigheden \u2013 opgaven.md",
        "answers": "1.5.2 Examenvaardigheden \u2013 antwoorden.md",
        "asset_prefix": "_assets/",
    },
    {
        "dir": MODULE / "1.5.3 Integratieoefening",
        "para": "1.5.3 Integratieoefening \u2013 opgaven.md",
        "answers": "1.5.3 Integratieoefening \u2013 antwoorden.md",
        "asset_prefix": "_assets/",
    },
    {
        "dir": MODULE / "1.5.4 Proeftoets",
        "para": "1.5.4 Proeftoets \u2013 toets.md",
        "answers": "1.5.4 Proeftoets \u2013 antwoorden.md",
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
  @bottom-left   { content: "Hoofdstuk 5 \u2014 Toetsvoorbereiding"; font-family: Arial, sans-serif; font-size: 9pt; color: #555; }
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

/* === EXERCISES ===
   Each numbered question is atomic: never split across pages. If the
   question doesn't fit in the remaining space, the renderer pushes the
   whole block to the next page. Only exceptions are questions longer
   than a page, which must split — but those don't exist in a test. */
.exercise {
  margin-bottom: 14pt;
  orphans: 3;
  widows: 3;
  break-inside: avoid;
  page-break-inside: avoid;
}

.exercise > p:first-child {
  break-after: avoid;
  page-break-after: avoid;
}

.exercise p {
  margin: 0 0 1pt 0;
}

/* === OPGAVE INTRO (h2 + context + table/figure + hr) ===
   Every opgave starts on a fresh page so the intro always has a full
   page of space for its context and questions. The intro is kept whole
   and the first question is forced to follow it on the same page. */
.opgave-intro {
  break-before: page;
  page-break-before: always;
  break-inside: avoid-page;
  break-after: avoid;
  page-break-after: avoid;
}

.opgave-intro + .exercise {
  break-before: avoid;
  page-break-before: avoid;
}

.opgave-intro h2,
.opgave-intro p,
.opgave-intro figure,
.opgave-intro table,
.opgave-intro blockquote {
  break-after: avoid;
  page-break-after: avoid;
}

/* An hr inside the intro doubles as visual separation above the first
   question; collapse its top margin so it hugs the table/figure. */
.opgave-intro hr {
  margin-top: 8pt;
  margin-bottom: 6pt;
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


def collect_assets():
    """Collect all paragraph assets into the chapter _assets/ folder."""
    os.makedirs(str(ASSET_DIR), exist_ok=True)
    count = 0
    for asset in sorted(glob.glob(str(MODULE / "*" / "_assets" / "*"))):
        dest = ASSET_DIR / os.path.basename(asset)
        shutil.copy2(asset, str(dest))
        count += 1
    print(f"Collected {count} assets into {ASSET_DIR}")


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
    """Wrap each Opgave/Oefening/Vraag block — or any numbered test/answer
    question like <p><strong>N</strong> <em>(Xp)</em>… — in a div so
    page-break rules (.exercise > p:first-child { break-after: avoid })
    keep the question number with its content."""
    html = re.sub(
        r'<p><strong>((?:Opgave|Oefening|Vraag)\s+\d+)',
        r'</div><div class="exercise"><p><strong>\1',
        html
    )
    # Bare numbered questions: <p><strong>12</strong> <em>(4p)</em> …
    html = re.sub(
        r'<p><strong>(\d+)</strong>\s*<em>\(',
        r'</div><div class="exercise"><p><strong>\1</strong> <em>(',
        html
    )
    html = html.replace('</div><div class="exercise">',
                        '<div class="exercise">', 1)
    html = re.sub(r'(<h[1-3])', r'</div>\1', html)
    # Don't close exercises before <hr>. The hr inside an opgave intro
    # needs to stay within the .opgave-intro wrapper; adding </div>
    # before it would close the wrapper prematurely. The closing
    # `</div>` before the next heading handles end-of-exercise cleanup.
    return html


def wrap_opgave_intros(html):
    """Wrap each opgave's intro block (h2 + context text/table/figure/
    blockquote up to and including the first <hr />) in a div so it
    stays on the same page as its first question.

    Only matches `Opgave N` h2 headings — other h2s in the chapter
    (e.g. samenvatting-sections) are left alone. Also requires that no
    `.exercise` div appears between the h2 and the hr, which excludes
    answer-booklet opgaven (no intro there)."""
    pattern = re.compile(
        r'(<h2[^>]*>[^<]*?Opgave[^<]*?</h2>'
        r'(?:(?!<div class="exercise"|<h2).)*?'
        r'<hr\s*/?>)',
        re.DOTALL
    )
    return pattern.sub(r'<div class="opgave-intro">\1</div>', html)


def rebalance_table_columns(html):
    """Analyze tables and set column widths proportional to content length."""
    import html as html_mod
    from html.parser import HTMLParser

    class CellExtractor(HTMLParser):
        def __init__(self):
            super().__init__()
            self.tables = []
            self.current_table = None
            self.current_row = None
            self.current_cell = None
            self.in_cell = False
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
        parts.append(f'\n<div style="break-before: page;"></div>\n\n{md.strip()}')

    return "\n\n".join(parts)


def assemble_answers():
    """Assemble answer booklet from all paragraph answer files."""
    parts = ["# Antwoorden Hoofdstuk 5 \u2014 Toetsvoorbereiding"]

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

    # Wrap opgave intros so each opgave's context stays with its questions
    html = wrap_opgave_intros(html)

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
    # 0. Collect all paragraph assets
    print("=== Collecting assets ===")
    collect_assets()

    # 1. Assemble chapter markdown
    print("\n=== Assembling chapter ===")
    chapter_md = assemble_chapter()
    chapter_md_path = BASE / "1.5 Toetsvoorbereiding \u2013 hoofdstuk.md"
    chapter_md_path.write_text(chapter_md, encoding="utf-8")
    print(f"Markdown saved: {chapter_md_path}")

    # 2. Assemble answer booklet markdown
    print("\n=== Assembling answer booklet ===")
    answers_md = assemble_answers()
    answers_md_path = BASE / "1.5 Toetsvoorbereiding \u2013 antwoorden.md"
    answers_md_path.write_text(answers_md, encoding="utf-8")
    print(f"Markdown saved: {answers_md_path}")

    # 3. Build PDFs
    print("\n=== Building chapter PDF ===")
    md_to_pdf(chapter_md, "1.5 Toetsvoorbereiding \u2013 hoofdstuk")

    print("\n=== Building answer booklet PDF ===")
    md_to_pdf(answers_md, "1.5 Toetsvoorbereiding \u2013 antwoorden")

    print("\n=== Done ===")
