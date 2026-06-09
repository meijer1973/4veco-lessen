import base64
import re
import subprocess
import sys
from pathlib import Path

ASSET_DIR = Path(__file__).parent / "_assets"
FOOTER = Path(__file__).parent.name

CSS = f"""<style>
@page {{
  size: A4;
  margin: 2cm 2.2cm 2.2cm 3.2cm;
  @bottom-left {{ content: "{FOOTER}"; font-family: Arial, sans-serif; font-size: 9pt; color: #555; }}
  @bottom-center {{ content: counter(page) " / " counter(pages); font-family: Arial, sans-serif; font-size: 9pt; color: #555; }}
}}
body {{ font-family: Arial, 'DejaVu Sans', sans-serif; font-size: 11pt; line-height: 1.45; color: #1a1a1a; max-width: 100%; }}
h1 {{ font-size: 18pt; color: #1A5276; border-bottom: 1.5px solid #1A5276; padding-bottom: 5pt; margin-top: 0; margin-bottom: 18pt; break-after: avoid; }}
h2 {{ font-size: 14pt; color: #1A5276; border-bottom: 1px solid #999; padding-bottom: 4pt; margin-top: 22pt; margin-bottom: 12pt; break-after: avoid; }}
h3 {{ font-size: 12pt; color: #1a1a1a; margin-top: 16pt; margin-bottom: 6pt; break-after: avoid; }}
h1 + p, h2 + p, h3 + p {{ break-before: avoid; }}
h1, h2, h3 {{ orphans: 3; widows: 3; }}
p {{ margin: 0 0 10pt 0; }}
table {{ border-collapse: collapse; width: 100%; max-width: 100%; margin: 12pt 0; font-size: 10.5pt; break-inside: avoid; }}
th {{ background: #EDF0F3; font-weight: bold; padding: 3pt 6pt; text-align: left; border: 1px solid #999; }}
td {{ border: 1px solid #999; padding: 2pt 6pt; }}
th:first-child, td:first-child {{ width: 8%; max-width: 42pt; white-space: nowrap; text-align: right; padding-left: 4pt; padding-right: 4pt; }}
.procedure-table {{ width: 100%; table-layout: fixed; break-inside: auto; page-break-inside: auto; font-size: 10.5pt; margin-top: 6pt; line-height: 1.22; }}
.procedure-table th:nth-child(1), .procedure-table td:nth-child(1) {{ width: 8%; max-width: 8%; text-align: center; }}
.procedure-table th:nth-child(2), .procedure-table td:nth-child(2) {{ width: 34%; text-align: left; white-space: normal; }}
.procedure-table th:nth-child(3), .procedure-table td:nth-child(3) {{ width: 58%; text-align: left; white-space: normal; }}
.procedure-table th, .procedure-table td {{ padding: 2pt 5pt; }}
tr:nth-child(even) td {{ background: #FAFBFC; }}
img {{ max-width: 100%; width: 100%; display: block; margin: 14pt auto; break-inside: avoid; }}
blockquote {{ background: #F4F7FA; border-left: 3px solid #1A5276; padding: 8pt 12pt; margin: 12pt 0; font-size: 10.5pt; line-height: 1.4; break-inside: avoid; }}
blockquote p {{ margin: 0 0 6pt 0; }}
blockquote p:last-child {{ margin-bottom: 0; }}
blockquote strong:first-child {{ color: #1A5276; }}
code {{ background: #EDF2F7; padding: 1pt 5pt; border-radius: 3px; font-family: Consolas, 'DejaVu Sans Mono', monospace; font-size: 10pt; white-space: nowrap; }}
hr {{ border: none; border-top: 1px solid #BBB; margin: 18pt 0; }}
ul, ol {{ margin: 0 0 10pt 0; padding-left: 20pt; }}
li {{ margin-bottom: 4pt; }}
</style>"""


def embed_images(md):
    def replacer(match):
        alt = match.group(1)
        ref = match.group(2).replace('.svg', '.png')
        full = ASSET_DIR / Path(ref).name
        if full.exists():
            b64 = base64.b64encode(full.read_bytes()).decode()
            return f"![{alt}](data:image/png;base64,{b64})"
        print(f"Warning: missing image {full}")
        return match.group(0)
    return re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", replacer, md)


def build_pdf(md_path, output_path):
    md = Path(md_path).read_text(encoding='utf-8')
    md = embed_images(md)
    result = subprocess.run(
        ['pandoc', '--from=markdown', '--to=html5', '--standalone'],
        input=md.encode('utf-8'),
        capture_output=True,
    )
    if result.returncode != 0:
        print(result.stderr.decode('utf-8', errors='replace'))
        sys.exit(result.returncode)
    html = result.stdout.decode('utf-8')
    html = html.replace('</head>', CSS + '</head>')
    html_path = output_path.replace('.pdf', '.html')
    Path(html_path).write_text(html, encoding='utf-8')
    import weasyprint
    weasyprint.HTML(string=html).write_pdf(output_path)
    print(f"PDF created: {output_path}")


if __name__ == '__main__':
    base = Path(__file__).parent
    for suffix in ['paragraaf', 'opgaven', 'antwoorden']:
        matches = list(base.glob(f'* – {suffix}.md'))
        if not matches:
            matches = [
                path for path in base.glob(f'*{suffix}.md')
                if path.name.endswith(f'– {suffix}.md')
            ]
        if not matches:
            print(f"Skipping {suffix}: no markdown found")
            continue
        md = matches[0]
        build_pdf(str(md), str(md).replace('.md', '.pdf'))
