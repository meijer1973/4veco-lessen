"""Extract paragraph PDF variants from the verified chapter; keep chapter pagination.

Exported Markdown is a readable copy, not a second content authority. Edit the
root page manuscripts and use build_all.py to regenerate all variants.
"""
from pathlib import Path
import json,re
import fitz
ROOT=Path(__file__).resolve().parent
PARA=ROOT/'paragrafen'
SPECS=[
    ('3.2.1','Volkomen concurrentie',2,9,4,1,5),
    ('3.2.2','Winstmaximalisatie',10,21,15,6,13),
    ('3.2.3','Langetermijnevenwicht',22,30,25,14,18),
    ('3.2.4','Gemengde opgaven',31,36,31,19,23),
]

def extract(source: Path,destination: Path,first: int,last: int,title: str)->None:
    with fitz.open(source) as src,fitz.open() as out:
        if not 1<=first<=last<=len(src):raise ValueError((source,first,last))
        out.insert_pdf(src,from_page=first-1,to_page=last-1)
        out.set_metadata({'title':title,'author':'4veco','subject':'Economie 4 vwo — hoofdstuk 3.2','keywords':'volkomen concurrentie, economie, 4 vwo'})
        out.save(destination,garbage=4,deflate=True)

def strip_pages(text: str)->str:
    return re.sub(r'<!-- PAGE .*? -->\s*','',text).strip()+'\n'

def main()->None:
    fullanswers=(ROOT/'Antwoorden.md').read_text(encoding='utf8')
    chunks=re.split(r'<!-- PAGE .*? -->',fullanswers)[1:]
    report=[]
    for sid,name,start,end,ex_start,ans_start,ans_end in SPECS:
        directory=PARA/f'{sid} {name}';directory.mkdir(parents=True,exist_ok=True)
        prefix=f'{sid} {name}'
        text=(ROOT/f'{sid} manuscript.md').read_text(encoding='utf8')
        if sid!='3.2.4':
            extract(ROOT/'output'/'Boek_3_H2_Volkomen_concurrentie.pdf',directory/f'{prefix} – paragraaf.pdf',start,end,f'{sid} {name}')
            (directory/f'{prefix} – paragraaf.md').write_text(strip_pages(text).replace('_assets/','../../_assets/'),encoding='utf8')
            exercises=text[text.index('## Uitgewerkt voorbeeld'):]
        else:exercises=text
        extract(ROOT/'output'/'Boek_3_H2_Volkomen_concurrentie.pdf',directory/f'{prefix} – opgaven.pdf',ex_start,end,f'Opgaven {sid}')
        (directory/f'{prefix} – opgaven.md').write_text(f'# Opgaven {sid} — {name}\n\n'+strip_pages(exercises).replace('_assets/','../../_assets/'),encoding='utf8')
        extract(ROOT/'output'/'Boek_3_H2_Antwoorden.pdf',directory/f'{prefix} – antwoorden.pdf',ans_start,ans_end,f'Antwoorden {sid}')
        selected='\n\n'.join(chunks[ans_start-1:ans_end])
        (directory/f'{prefix} – antwoorden.md').write_text(f'# Antwoorden {sid} — {name}\n\n'+strip_pages(selected).replace('_assets/','../../_assets/'),encoding='utf8')
        spec={'paragraph':sid,'student_pages':[start,end],'exercise_pages':[ex_start,end],'answer_pages':[ans_start,ans_end],'page_numbering':'original chapter pages retained'}
        report.append(spec)
    (ROOT/'QA'/'paragraph_exports.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
    print('Paragraph exports:',len(report),'— PDF files:',len(list(PARA.rglob('*.pdf'))))
if __name__=='__main__':main()
