"""Export the four paragraph views without reflowing accepted chapter pages."""
from pathlib import Path
import json, re
import fitz

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'paragrafen'
SPECS = [
    ('4.1.1', 'Monopolie kenmerken', (2, 9), (5, 9), (1, 4)),
    ('4.1.2', 'Marginale opbrengst bij monopolie', (10, 20), (15, 20), (5, 9)),
    ('4.1.3', 'Winstmaximalisatie bij monopolie', (21, 31), (27, 31), (10, 16)),
    ('4.1.4', 'Gemengde opgaven monopolie', (32, 36), (32, 36), (17, 20)),
]

def pages_md(text: str) -> list[str]:
    return [v for v in re.split(r'(?=<!-- PAGE )', text) if v.strip()]

def cut_pdf(src: fitz.Document, start: int, end: int, dest: Path, title: str):
    target = fitz.open()
    target.insert_pdf(src, from_page=start-1, to_page=end-1)
    target.set_metadata({'title': title, 'subject': '4 vwo · Boek 4 · Monopolie'})
    target.xref_set_key(target.pdf_catalog(), 'Lang', '(nl-NL)')
    target.set_page_labels([{'startpage': 0, 'prefix': '', 'style': 'D', 'firstpagenum': start}])
    target.save(dest, garbage=4, deflate=True)
    # This checks that no text or page was lost during the crop/export.
    with fitz.open(dest) as check:
        assert len(check) == end-start+1
        assert all(check[j].get_text() == src[start-1+j].get_text() for j in range(len(check)))


def main():
    OUT.mkdir(exist_ok=True)
    ans_parts = pages_md((ROOT/'Antwoorden.md').read_text())
    student = fitz.open(ROOT/'output/Boek_4_H1_Monopolie.pdf')
    answers = fitz.open(ROOT/'output/Boek_4_H1_Antwoorden.pdf')
    records = []
    for sid, title, full, exercises, answer in SPECS:
        folder = OUT/f'{sid} {title}'
        folder.mkdir(exist_ok=True)
        text = (ROOT/f'{sid} manuscript.md').read_text()
        for variant, span, doc in [('paragraaf', full, student), ('opgaven', exercises, student), ('antwoorden', answer, answers)]:
            stem = f'{sid} {title} – {variant}'
            cut_pdf(doc, *span, folder/(stem+'.pdf'), stem)
            if variant == 'antwoorden':
                manuscript = '\n\n'.join(ans_parts[answer[0]-1:answer[1]])
            elif variant == 'opgaven' and sid != '4.1.4':
                # Preserve the PAGE marker for the first exercise page.
                chunks = pages_md(text)
                first = next(i for i,c in enumerate(chunks) if '## Startopgaven' in c)
                manuscript = '\n\n'.join(chunks[first:])
            else:
                manuscript = text
            # Folder depth is paragrafen/<name>/, so the shared assets are two levels up.
            manuscript = manuscript.replace('_assets/', '../../_assets/')
            (folder/(stem+'.md')).write_text(manuscript, encoding='utf-8')
            records.append({'paragraph':sid, 'variant':variant, 'source_pages_inclusive':span,
                            'file':str((folder/(stem+'.pdf')).relative_to(ROOT)),
                            'pages':span[1]-span[0]+1, 'text_preserved':True})
    student.close(); answers.close()
    (ROOT/'QA/paragraph_exports.json').write_text(json.dumps(records,ensure_ascii=False,indent=2))
    print(f'Exported and verified {len(records)} paragraph PDF views plus Markdown.')

if __name__=='__main__':
    main()
