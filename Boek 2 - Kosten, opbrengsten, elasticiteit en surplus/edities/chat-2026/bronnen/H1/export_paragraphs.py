"""Export paragraph PDFs and Markdown views from the chapter manuscripts."""
from pathlib import Path
import re,json,shutil
import fitz
from build import ROOT,PAGES
TITLES={'2.1.1':'Kostenstructuren','2.1.2':'Opbrengsten, winst en break-even','2.1.3':'Marginale kosten en marginale opbrengsten','2.1.4':'Gemengde opgaven'}

def write_pdf_range(src,path,start,end):
    out=fitz.open();out.insert_pdf(src,from_page=start,to_page=end)
    out.set_metadata({'title':path.stem,'author':'4veco','subject':'Economie 4 vwo · lokale printeditie'})
    out.save(path,garbage=4,deflate=True);out.close()

def export():
    out=ROOT/'paragrafen';out.mkdir(exist_ok=True)
    chapter=fitz.open(ROOT/'output/Boek_2_H1_Kosten_en_opbrengsten.pdf')
    answers=fitz.open(ROOT/'output/Boek_2_H1_Antwoorden.pdf')
    ansstarts={x[1].split()[0]:x[2]-1 for x in answers.get_toc() if x[0]==1 and x[1].startswith('2.1.')}
    ansmd=(ROOT/'2.1 Kosten en opbrengsten – antwoorden.md').read_text()
    summary={}
    for sec,title in TITLES.items():
        folder=out/f'{sec} {title}';folder.mkdir(exist_ok=True)
        pages=[(i,p) for i,p in enumerate(PAGES) if p['section']==sec]
        text='\n\n'.join(p['body'] for _,p in pages)
        head=f'# {sec} {title}\n\n'
        if sec!='2.1.4':
            (folder/f'{sec} {title} – paragraaf.md').write_text(head+text)
            write_pdf_range(chapter,folder/f'{sec} {title} – paragraaf.pdf',pages[0][0],pages[-1][0])
            exercise_start=next(i for i,p in pages if '## Uitgewerkt voorbeeld' in p['body'])
            exercise_text='\n\n'.join(p['body'] for i,p in pages if i>=exercise_start)
        else:
            exercise_start=pages[0][0];exercise_text=text
        (folder/f'{sec} {title} – opgaven.md').write_text(head+exercise_text)
        write_pdf_range(chapter,folder/f'{sec} {title} – opgaven.pdf',exercise_start,pages[-1][0])
        # Source answer sections are delineated by their H1 headings.
        atext=re.search(r'^# '+re.escape(sec)+r' [\s\S]*?(?=^# 2\.1\.|\Z)',ansmd,re.M).group()
        (folder/f'{sec} {title} – antwoorden.md').write_text(atext)
        start=ansstarts[sec];following=[v for v in ansstarts.values() if v>start]
        end=min(following)-1 if following else len(answers)-1
        write_pdf_range(answers,folder/f'{sec} {title} – antwoorden.pdf',start,end)
        assets=set(re.findall(r'(?:src="|\]\()(_assets/[^"\)]+)',text+'\n'+atext))
        local=folder/'_assets';local.mkdir(exist_ok=True)
        for name in assets:
            path=ROOT/name
            for ext in ['.png','.svg']:
                f=path.with_suffix(ext)
                if not f.exists():raise FileNotFoundError(f)
                shutil.copy2(f,local/f.name)
        (folder/'LEESMIJ.md').write_text('Dit is een afgeleide export. Bewerk voor een herbouw de Markdown in ../../manuscript/ en het centrale antwoordenbestand, niet deze kopie. De PDF behoudt de paginanummers uit het hoofdstuk of antwoordenboek. De officiële repositoryreview is niet in deze lokale export opgenomen.\n')
        summary[sec]={'chapter_pages':[pages[0][0]+1,pages[-1][0]+1],'answer_pages':[start+1,end+1],'exercise_count':len(set(re.findall(r'Opgave (\d+)',text)))}
    (ROOT/'paragraph-exports.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2))
    print('Paragraph export complete:',summary)
if __name__=='__main__':export()
