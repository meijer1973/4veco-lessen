"""Build styled PDF from markdown following the econ-pdf-builder skill."""
import base64, re, os, subprocess, sys
from pathlib import Path

ASSET_DIR = os.path.join(os.path.dirname(__file__), "_assets")

CSS = """<style>
@page {
  size: A4;
  margin: 2cm 2.2cm 2.2cm 3.2cm;
  @bottom-left   { content: "1.5.2 Examenvaardigheden"; font-family: Arial, sans-serif; font-size: 9pt; color: #555; }
  @bottom-center { content: counter(page) " / " counter(pages);  font-family: Arial, sans-serif; font-size: 9pt; color: #555; }
}

body {
  font-family: Arial, 'DejaVu Sans', sans-serif;
  font-size: 11pt;
  line-height: 1.45;
  color: #1a1a1a;
  max-width: 100%;
}

p { margin: 0 0 10pt 0; }

h1 {
  font-size: 18pt; font-weight: bold; color: #1A5276;
  border-bottom: 1.5px solid #1A5276; padding-bottom: 5pt;
  margin-top: 0; margin-bottom: 18pt; break-after: avoid;
}

h2 {
  font-size: 14pt; font-weight: bold; color: #1A5276;
  border-bottom: 1px solid #999; padding-bottom: 4pt;
  margin-top: 22pt; margin-bottom: 12pt; break-after: avoid;
}

h3 {
  font-size: 12pt; font-weight: bold; color: #1a1a1a;
  margin-top: 16pt; margin-bottom: 6pt; break-after: avoid;
}

h1 + p, h2 + p, h3 + p { break-before: avoid; }
h1, h2, h3 { orphans: 3; widows: 3; }

blockquote {
  background: #F4F7FA; border-left: 3px solid #1A5276;
  padding: 8pt 12pt; margin: 12pt 0;
  font-size: 10.5pt; line-height: 1.4; break-inside: avoid;
}
blockquote p { margin: 0 0 6pt 0; }
blockquote p:last-child { margin-bottom: 0; }
blockquote strong:first-child { color: #1A5276; }

table {
  border-collapse: collapse; width: 100%;
  margin: 12pt 0; font-size: 10.5pt; break-inside: avoid;
}
th {
  background: #EDF0F3; color: #1a1a1a; font-weight: bold;
  padding: 3pt 6pt; text-align: left; border: 1px solid #999;
}
td { border: 1px solid #999; padding: 2pt 6pt; }
tr:nth-child(even) td { background: #FAFBFC; }

figure { margin: 14pt 0; break-inside: avoid; text-align: center; }
figure img { max-width: 100%; width: 100%; display: block; margin: 0 auto; }
figcaption { font-weight: bold; font-size: 10.5pt; color: #1a1a1a; text-align: left; margin-top: 6pt; }

img { max-width: 100%; width: 100%; display: block; margin: 14pt auto; break-inside: avoid; }
p + figure, p + p > img { break-before: avoid; }

.exercise { margin-bottom: 14pt; orphans: 2; widows: 2; }
.exercise > p:first-child { break-after: avoid; page-break-after: avoid; }
.exercise p { margin: 0 0 1pt 0; }

code {
  background: #EDF2F7; padding: 1pt 5pt; border-radius: 3px;
  font-family: 'Consolas', 'DejaVu Sans Mono', monospace; font-size: 10pt;
}

hr { border: none; border-top: 1px solid #BBB; margin: 18pt 0; }
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
        full = os.path.join(ASSET_DIR, os.path.basename(path))
        if os.path.exists(full):
            b64 = base64.b64encode(open(full, "rb").read()).decode()
            return f'![{alt}](data:image/png;base64,{b64})'
        print(f"  Warning: missing {full}")
        return match.group(0)
    return re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', replacer, md)


def wrap_exercises(html):
    """Wrap each Oefening block in a div for page-break control."""
    html = re.sub(
        r'<p><strong>(Oefening \d+)',
        r'</div><div class="exercise"><p><strong>\1',
        html
    )
    html = html.replace('</div><div class="exercise">',
                        '<div class="exercise">', 1)
    html = re.sub(r'(<h[23])', r'</div>\1', html)
    return html


def build_pdf(md_path, output_path):
    """Build a styled PDF from a markdown file."""
    md = Path(md_path).read_text(encoding="utf-8")
    md = embed_images(md)
    md = re.sub(r'[⬜🟨🟥]\s*(LIGHT|MEDIUM|HEAVY)', '', md)
    md = re.sub(r'```\s*\nGRAPH SPEC:.*?\n```\s*\n', '', md, flags=re.DOTALL)

    result = subprocess.run(
        ["pandoc", "--from=markdown", "--to=html5", "--standalone"],
        input=md.encode("utf-8"), capture_output=True
    )
    result.stdout = result.stdout.decode("utf-8")
    result.stderr = result.stderr.decode("utf-8")
    if result.returncode != 0:
        print(f"Pandoc error: {result.stderr}")
        sys.exit(1)
    html = result.stdout

    html = re.sub(r'<style>\s*/\* Default styles provided by pandoc.*?</style>', '', html, flags=re.DOTALL)
    html = wrap_exercises(html)
    html = html.replace("</head>", CSS + "</head>")

    html_path = output_path.replace(".pdf", ".html")
    Path(html_path).write_text(html, encoding="utf-8")

    try:
        import weasyprint
        weasyprint.HTML(string=html).write_pdf(output_path)
        print(f"PDF created: {output_path}")
        return
    except Exception as e:
        print(f"Weasyprint unavailable ({type(e).__name__}). Trying headless Chrome.")

    chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    abs_output = os.path.abspath(output_path)
    abs_html = os.path.abspath(html_path)
    if os.path.exists(chrome):
        result = subprocess.run([
            chrome, "--headless", "--disable-gpu", "--no-pdf-header-footer",
            f"--print-to-pdf={abs_output}",
            "file:///" + abs_html.replace("\\", "/")
        ], capture_output=True, text=True)
        if os.path.exists(output_path):
            print(f"PDF created via headless Chrome: {output_path}")
        else:
            print(f"Chrome PDF generation failed: {result.stderr}")
    else:
        print(f"HTML saved: {html_path}")


if __name__ == "__main__":
    base = os.path.dirname(__file__)
    for stem in ["opgaven", "antwoorden"]:
        md_file = os.path.join(base, f"1.5.2 Examenvaardigheden \u2013 {stem}.md")
        pdf_file = os.path.join(base, f"1.5.2 Examenvaardigheden \u2013 {stem}.pdf")
        if os.path.exists(md_file):
            print(f"\nBuilding {stem}...")
            build_pdf(md_file, pdf_file)
        else:
            print(f"Skipping {stem}: {md_file} not found")
