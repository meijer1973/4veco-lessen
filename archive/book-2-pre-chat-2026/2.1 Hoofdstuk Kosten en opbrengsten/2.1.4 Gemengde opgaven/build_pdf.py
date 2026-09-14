import base64
import re
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).parent
ASSET_DIR = BASE / "_assets"
FOOTER = BASE.name

CSS = f"""<style>
@page {{
  size: A4;
  margin: 2cm 2.2cm 2.2cm 3.2cm;
  @bottom-left {{ content: "{FOOTER}"; font-family: Arial, sans-serif; font-size: 9pt; color: #555; }}
  @bottom-center {{ content: counter(page) " / " counter(pages); font-family: Arial, sans-serif; font-size: 9pt; color: #555; }}
}}

body {{
  font-family: Arial, 'DejaVu Sans', sans-serif;
  font-size: 11pt;
  line-height: 1.45;
  color: #1a1a1a;
  max-width: 100%;
}}

p {{ margin: 0 0 10pt 0; }}

h1 {{
  font-size: 18pt;
  font-weight: bold;
  color: #1A5276;
  border-bottom: 1.5px solid #1A5276;
  padding-bottom: 5pt;
  margin-top: 0;
  margin-bottom: 18pt;
  break-after: avoid;
}}

h2 {{
  font-size: 14pt;
  font-weight: bold;
  color: #1A5276;
  border-bottom: 1px solid #999;
  padding-bottom: 4pt;
  margin-top: 22pt;
  margin-bottom: 12pt;
  break-after: avoid;
}}

h3 {{
  font-size: 12pt;
  font-weight: bold;
  color: #1a1a1a;
  margin-top: 16pt;
  margin-bottom: 6pt;
  break-after: avoid;
}}

h1 + p, h2 + p, h3 + p {{ break-before: avoid; }}
h1, h2, h3 {{ orphans: 3; widows: 3; }}

table {{
  border-collapse: collapse;
  width: 100%;
  margin: 12pt 0;
  font-size: 10.5pt;
  break-inside: avoid;
}}

th {{
  background: #EDF0F3;
  color: #1a1a1a;
  font-weight: bold;
  padding: 3pt 6pt;
  text-align: left;
  border: 1px solid #999;
}}

td {{ border: 1px solid #999; padding: 2pt 6pt; }}
tr:nth-child(even) td {{ background: #FAFBFC; }}

.wide-table {{
  width: 100%;
  table-layout: fixed;
  break-inside: auto;
  page-break-inside: auto;
  font-size: 10pt;
  line-height: 1.18;
}}

.wide-table th, .wide-table td {{
  padding: 2pt 3pt;
  white-space: normal;
}}

.wide-table th:first-child, .wide-table td:first-child {{
  width: 16%;
  text-align: left;
}}

.wide-table th:not(:first-child), .wide-table td:not(:first-child) {{
  text-align: center;
}}

blockquote {{
  background: #F4F7FA;
  border-left: 3px solid #1A5276;
  padding: 8pt 12pt;
  margin: 12pt 0;
  font-size: 10.5pt;
  line-height: 1.4;
  break-inside: avoid;
}}

img {{
  max-width: 100%;
  width: 100%;
  display: block;
  margin: 14pt auto;
  break-inside: avoid;
}}

code {{
  background: #EDF2F7;
  padding: 1pt 5pt;
  border-radius: 3px;
  font-family: Consolas, 'DejaVu Sans Mono', monospace;
  font-size: 10pt;
}}

hr {{ border: none; border-top: 1px solid #BBB; margin: 18pt 0; }}
ul, ol {{ margin: 0 0 10pt 0; padding-left: 20pt; }}
li {{ margin-bottom: 4pt; }}
</style>"""


def find_markdown(suffix):
    matches = list(BASE.glob(f"* \u2013 {suffix}.md"))
    if not matches:
        matches = [
            path for path in BASE.glob(f"*{suffix}.md")
            if path.name.endswith(f"\u2013 {suffix}.md")
        ]
    if not matches:
        raise FileNotFoundError(f"No {suffix}.md found in {BASE}")
    return matches[0]


def embed_images(markdown):
    def replacer(match):
        alt = match.group(1)
        ref = match.group(2).replace(".svg", ".png")
        full = ASSET_DIR / Path(ref).name
        if full.exists():
            b64 = base64.b64encode(full.read_bytes()).decode()
            return f"![{alt}](data:image/png;base64,{b64})"
        print(f"Warning: missing image {full}")
        return match.group(0)

    return re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", replacer, markdown)


def build_pdf(md_path, output_path):
    markdown = embed_images(md_path.read_text(encoding="utf-8"))
    result = subprocess.run(
        ["pandoc", "--from=markdown+raw_html", "--to=html5", "--standalone"],
        input=markdown.encode("utf-8"),
        capture_output=True,
    )
    if result.returncode != 0:
        print(result.stderr.decode("utf-8", errors="replace"))
        sys.exit(result.returncode)

    html = result.stdout.decode("utf-8").replace("</head>", CSS + "</head>")
    html_path = output_path.with_suffix(".html")
    html_path.write_text(html, encoding="utf-8")

    import weasyprint

    weasyprint.HTML(string=html).write_pdf(output_path)
    print(f"PDF created: {output_path}")


if __name__ == "__main__":
    for suffix in ["opgaven", "antwoorden"]:
        md_path = find_markdown(suffix)
        build_pdf(md_path, md_path.with_suffix(".pdf"))
