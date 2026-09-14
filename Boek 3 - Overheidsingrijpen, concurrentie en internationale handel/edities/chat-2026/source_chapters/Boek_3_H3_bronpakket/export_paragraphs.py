"""Create editable paragraph sources and lossless PDF extracts of the chapter.
The PDF extracts deliberately retain the chapter's printed page numbers and references.
"""
from pathlib import Path
import re, shutil, json
import fitz
from build import page_chunks
ROOT = Path(__file__).resolve().parent
SPECS = [
    ('3.3.1','Waarom landen handelen',2,10,5,1,4),
    ('3.3.2','Wereldmarktprijs, import, export en welvaart',11,20,15,5,8),
    ('3.3.3','Protectionisme',21,30,25,9,13),
    ('3.3.4','Gemengde opgaven internationale handel',31,37,31,14,17),
]
def extract(source: Path, dest: Path, first: int, last: int, title: str):
    with fitz.open(source) as src, fitz.open() as out:
        out.insert_pdf(src, from_page=first-1, to_page=last-1, links=False)
        out.set_metadata({'title':title, 'author':'4veco', 'subject':'Paragraafextract; oorspronkelijke hoofdstukpaginering behouden'})
        out.set_page_labels([{'startpage':0, 'prefix':'', 'style':'D', 'firstpagenum':first}])
        out.save(dest, garbage=4, deflate=True)

def main():
    student=ROOT/'output/Boek_3_H3_Internationale_handel.pdf'
    answers=ROOT/'output/Boek_3_H3_Antwoorden.pdf'
    answer_pages=list(page_chunks(ROOT/'Antwoorden.md'))
    manifest=[]
    for code,title,lo,hi,exlo,alo,ahi in SPECS:
        folder=ROOT/'paragrafen'/f'{code} {title}'
        folder.mkdir(parents=True,exist_ok=True)
        text=(ROOT/f'{code} manuscript.md').read_text()
        head='paragraaf' if code!='3.3.4' else 'opgaven'
        mainstem=f'{code} {title} – {head}'
        (folder/f'{mainstem}.md').write_text(text,encoding='utf-8')
        extract(student,folder/f'{mainstem}.pdf',lo,hi,f'{code} {title}')
        if code!='3.3.4':
            start=text.index('## Uitgewerkt voorbeeld')
            # Retain page markers for explicit layout, with first example's metadata.
            example_page=next(p for p in page_chunks(ROOT/f'{code} manuscript.md') if '## Uitgewerkt voorbeeld' in p['body'])
            prefix='<!-- PAGE '+json.dumps({k:v for k,v in example_page.items() if k!='body'},ensure_ascii=False)+' -->\n\n'
            (folder/f'{code} {title} – opgaven.md').write_text(prefix+text[start:],encoding='utf-8')
            extract(student,folder/f'{code} {title} – opgaven.pdf',exlo,hi,f'Opgaven {code} {title}')
        ap=[p for p in answer_pages if p['section']==code]
        atext='\n\n'.join('<!-- PAGE '+json.dumps({k:v for k,v in p.items() if k!='body'},ensure_ascii=False)+' -->\n\n'+p['body'] for p in ap)
        (folder/f'{code} {title} – antwoorden.md').write_text(atext,encoding='utf-8')
        extract(answers,folder/f'{code} {title} – antwoorden.pdf',alo,ahi,f'Antwoorden {code} {title}')
        assets=set(re.findall(r'_assets/([^"\s)]+)',text+atext))
        adir=folder/'_assets';adir.mkdir(exist_ok=True)
        for name in assets:
            for suffix in ['.svg','.png']:
                f=ROOT/'_assets'/Path(name).with_suffix(suffix)
                shutil.copy2(f,adir/f.name)
        (folder/f'{code}-textbook-handoff.md').write_text(f'''# Overdracht {code}

Deze lokale editie is nieuw geschreven volgens de door de gebruiker aangeleverde Book 3-outline v2.
De gebruikte doelen, doelopgave en oefenroute zijn vastgelegd in `_chapter-plan.md`,
`QA/authored-targets.json` en de docenteninformatie van het hoofdstuk.
Er is geen wijziging van het doelregister of een merge-/publicatiebesluit uitgevoerd.

De PDF-extracten behouden de gedrukte hoofdstukpaginering ({lo}–{hi});
de antwoorden behouden pagina {alo}–{ahi} van het antwoordboek.
Gebruik het complete hoofdstuk voor verwijzingen naar voorafgaande paragrafen.
De oefening-PDF begint bij het uitgewerkte voorbeeld en bevat de compacte samenvatting.
Het hoofdstuk en alle extracten zijn tekstdoorzoekbaar; grafieken bestaan daarnaast als SVG en PNG.

Tekstwijzigingen: bewerk het bovenliggende `{code} manuscript.md` en `Antwoorden.md`,
voer `python build_all.py` uit; deze extracten worden opnieuw gegenereerd.
''',encoding='utf-8')
        manifest.append({'paragraph':code,'student_chapter_pages':[lo,hi],'exercise_pages':[exlo,hi],
                         'answer_book_pages':[alo,ahi],'folder':str(folder.relative_to(ROOT))})
    (ROOT/'QA/paragraph-exports.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    print('Paragraph exports:',len(manifest))
if __name__=='__main__':main()
