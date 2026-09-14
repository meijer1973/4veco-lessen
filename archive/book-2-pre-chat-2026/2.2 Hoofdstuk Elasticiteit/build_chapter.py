import base64
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).parent
ASSET_DIR = BASE / "_assets"
CHAPTER = "2.2 Elasticiteit"

PARAGRAPHS = [
    ("2.2.1 Prijselasticiteit", "paragraaf", "antwoorden"),
    ("2.2.2 Elasticiteit en omzet", "paragraaf", "antwoorden"),
    ("2.2.3 Inkomenselasticiteit en kruiselingse elasticiteit", "paragraaf", "antwoorden"),
    ("2.2.4 Gemengde opgaven elasticiteit", "opgaven", "antwoorden"),
]

CSS = """<style>
@page {
  size: A4;
  margin: 2cm 2.2cm 2.2cm 3.2cm;
  @bottom-left   { content: "Hoofdstuk 2.2 - Elasticiteit"; font-family: Arial, sans-serif; font-size: 9pt; color: #555; }
  @bottom-center { content: counter(page) " / " counter(pages); font-family: Arial, sans-serif; font-size: 9pt; color: #555; }
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

.chapter-front li { margin-bottom: 2pt; }

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

table { border-collapse: collapse; width: 100%; margin: 12pt 0; font-size: 10.5pt; break-inside: avoid; }
th { background: #EDF0F3; font-weight: bold; padding: 3pt 6pt; text-align: left; border: 1px solid #999; }
td { border: 1px solid #999; padding: 2pt 6pt; }
tr:nth-child(even) td { background: #FAFBFC; }
img { max-width: 100%; width: 100%; display: block; margin: 14pt auto; break-inside: avoid; }
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

code { background: #EDF2F7; padding: 1pt 5pt; border-radius: 3px; font-family: Consolas, 'DejaVu Sans Mono', monospace; font-size: 10pt; }
hr { border: none; border-top: 1px solid #BBB; margin: 18pt 0; }
em { color: #444; }
ul, ol { margin: 0 0 10pt 0; padding-left: 20pt; }
ol[type="a"] { list-style-type: lower-alpha; }
li { margin-bottom: 4pt; }
.page-break { break-before: page; }
.exercise {
  margin-bottom: 14pt;
  orphans: 2;
  widows: 2;
}
.exercise > p:first-child {
  break-after: avoid;
  page-break-after: avoid;
}
.exercise p { margin: 0 0 1pt 0; }
</style>"""

FRONT = """<div class="chapter-front">

# Hoofdstuk 2.2 - Elasticiteit

## Inhoud

| Paragraaf | Onderwerp |
|---|---|
| 2.2.1 | Prijselasticiteit |
| 2.2.2 | Elasticiteit en omzet |
| 2.2.3 | Inkomenselasticiteit en kruiselingse elasticiteit |
| 2.2.4 | Gemengde opgaven: elasticiteit |

## Leerdoelen

Na dit hoofdstuk kun je:

- procentuele prijsverandering en procentuele hoeveelheidsverandering berekenen;
- prijselasticiteit van de vraag berekenen met `Ev = %dQv / %dP`;
- signed `Ev` opschrijven en daarna met `|Ev|` bepalen of de vraag elastisch of inelastisch is;
- uitleggen waarom consumenten sterk of zwak reageren op een prijsverandering;
- `TO = P x Q` gebruiken om omzet voor en na een prijsverandering te berekenen;
- uitleggen waarom elasticiteit bepaalt of omzet stijgt of daalt;
- een voorzichtig omzetadvies geven zonder winst of kosten te gebruiken.
- inkomenselasticiteit berekenen en normale, inferieure, noodzakelijke en luxe goederen correct onderscheiden;
- kruiselingse elasticiteit berekenen en substituten of complementen herkennen;
- een vraagfunctie met meerdere variabelen gebruiken door een factor tegelijk te veranderen;
- gemengde bronnen lezen, relevante gegevens kiezen en je antwoord structureren;
- `Ev`, `TO`, `Ei`, `Ek` en vraagfuncties combineren in een voorzichtig economisch advies.

## Waarom elasticiteit belangrijk is

Een prijsverandering lijkt eenvoudig: de prijs gaat omhoog of omlaag. Voor een onderneming is de echte vraag wat klanten daarna doen. Elasticiteit helpt je om die reactie te meten, te berekenen en in gewone taal uit te leggen. Daarna kun je beoordelen wat er met de omzet gebeurt, en hoe inkomen of de prijs van andere producten de vraag mee kunnen bepalen. In de gemengde opgaven oefen je die vaardigheden samen in langere bronnen.

</div>
"""


def fs_path(path):
    resolved = Path(path).resolve()
    text = str(resolved)
    if os.name != "nt" or text.startswith("\\\\?\\"):
        return text
    if text.startswith("\\\\"):
        return "\\\\?\\UNC\\" + text.lstrip("\\")
    return "\\\\?\\" + text


def read_utf8(path):
    with open(fs_path(path), "r", encoding="utf-8") as handle:
        return handle.read()


def write_utf8(path, text):
    with open(fs_path(path), "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


def find_markdown(folder_name, suffix):
    folder = BASE / folder_name
    matches = list(folder.glob(f"* \u2013 {suffix}.md"))
    if not matches:
        raise FileNotFoundError(f"No {suffix}.md found in {folder}")
    return matches[0]


def without_first_h1(markdown):
    lines = markdown.splitlines()
    if lines and lines[0].startswith("# "):
        return "\n".join(lines[1:]).lstrip()
    return markdown


def exercise_block(markdown):
    text = without_first_h1(markdown).lstrip()
    match = re.search(r"^##\s+Opgaven\b", text, re.MULTILINE)
    if match:
        return text[match.start():].lstrip()
    return f"## Opgaven\n\n{text}"


def has_embedded_exercises(markdown):
    return bool(
        re.search(r"^##\s+Opgaven\b", markdown, re.MULTILINE)
        or re.search(r"^###\s+Startoefeningen\b", markdown, re.MULTILINE)
    )


def copy_assets():
    ASSET_DIR.mkdir(exist_ok=True)
    for folder_name, _, _ in PARAGRAPHS:
        source = BASE / folder_name / "_assets"
        if not os.path.exists(fs_path(source)):
            continue
        for asset in source.iterdir():
            if asset.is_file() and asset.suffix.lower() in {".svg", ".png"}:
                shutil.copy2(asset, ASSET_DIR / asset.name)


def assemble(kind):
    parts = []
    if kind == "hoofdstuk":
        parts.append(FRONT)
    else:
        parts.append(f"# Antwoorden hoofdstuk 2.2 - Elasticiteit\n")

    for folder_name, body_suffix, answer_suffix in PARAGRAPHS:
        if kind == "hoofdstuk" and body_suffix == "paragraaf":
            para_path = find_markdown(folder_name, "paragraaf")
            opgaven_path = find_markdown(folder_name, "opgaven")
            text = read_utf8(para_path)
            if not has_embedded_exercises(text):
                exercises = exercise_block(read_utf8(opgaven_path))
                text = f"{text}\n\n{exercises}"
        else:
            suffix = body_suffix if kind == "hoofdstuk" else answer_suffix
            md_path = find_markdown(folder_name, suffix)
            text = read_utf8(md_path)
        parts.append('<div class="page-break"></div>')
        parts.append(text)

    return "\n\n".join(parts)


def embed_images(md):
    def replacer(match):
        alt = match.group(1)
        ref = match.group(2).replace(".svg", ".png")
        full = ASSET_DIR / Path(ref).name
        if os.path.exists(fs_path(full)):
            with open(fs_path(full), "rb") as handle:
                b64 = base64.b64encode(handle.read()).decode()
            return f"![{alt}](data:image/png;base64,{b64})"
        print(f"Warning: missing image {full}")
        return match.group(0)

    return re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", replacer, md)


def wrap_exercises(html):
    token_re = re.compile(
        r'(<h2[^>]*>\s*Opgave\s+\d+\b|<p><strong>Opgave\s+\d+\b|'
        r'<div class="page-break"></div>|<h1\b|</body>)',
        re.IGNORECASE,
    )
    pieces = []
    last = 0
    open_exercise = False

    for match in token_re.finditer(html):
        token = match.group(0)
        lower = token.lower()
        pieces.append(html[last:match.start()])

        is_exercise_start = (
            (lower.startswith('<h2') or lower.startswith('<p><strong>'))
            and re.search(r'opgave\s+\d+\b', token, re.IGNORECASE)
        )

        if is_exercise_start:
            if open_exercise:
                pieces.append('</div>')
            pieces.append('<div class="exercise">')
            pieces.append(token)
            open_exercise = True
        else:
            if open_exercise:
                pieces.append('</div>')
                open_exercise = False
            pieces.append(token)

        last = match.end()

    pieces.append(html[last:])
    if open_exercise:
        pieces.append('</div>')
    return ''.join(pieces)


def build_pdf(md_path, pdf_path):
    md = embed_images(read_utf8(md_path))
    result = subprocess.run(
        ["pandoc", "--from=markdown", "--to=html5", "--standalone"],
        input=md.encode("utf-8"),
        capture_output=True,
    )
    if result.returncode != 0:
        print(result.stderr.decode("utf-8", errors="replace"))
        sys.exit(result.returncode)

    html = result.stdout.decode("utf-8")
    front_marker = html.find('class="chapter-front"')
    if front_marker != -1:
        page_break_idx = html.find('<div class="page-break">', front_marker)
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

    html = re.sub(
        r'<style>\s*/\* Default styles provided by pandoc.*?</style>',
        '',
        html,
        flags=re.DOTALL,
    )
    html = html.replace("</head>", CSS + "</head>")
    html = "\n".join(line.rstrip() for line in html.splitlines()) + "\n"
    html_path = str(pdf_path).replace(".pdf", ".html")
    write_utf8(html_path, html)

    import weasyprint

    weasyprint.HTML(string=html).write_pdf(fs_path(pdf_path))
    print(f"PDF created: {pdf_path}")


if __name__ == "__main__":
    copy_assets()
    for kind in ["hoofdstuk", "antwoorden"]:
        md_path = BASE / f"{CHAPTER} \u2013 {kind}.md"
        pdf_path = BASE / f"{CHAPTER} \u2013 {kind}.pdf"
        write_utf8(md_path, assemble(kind))
        build_pdf(md_path, pdf_path)
