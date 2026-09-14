"""Export all seven paragraphs from the completed, validated PDFs.
Printed chapter page numbers are retained; bookmarks are made local.
"""
from pathlib import Path
import json
import fitz
from author_common import TITLES
R=Path(__file__).resolve().parent
O=R/'paragrafen';O.mkdir(exist_ok=True)
student_starts=[3,11,19,25,36,47,53]
student_ends=[10,18,24,35,46,52,58]
manifest=[]
for kind,filename in [('leerling','Boek_4_H2_Marktvormen_en_marktfalen.pdf'),('antwoorden','Boek_4_H2_Antwoorden.pdf')]:
    with fitz.open(R/'output'/filename) as src:
        toc=src.get_toc()
        if kind=='leerling': starts,ends=student_starts,student_ends
        else:
            starts=[next(p for level,t,p in toc if level==1 and t.startswith(sec)) for sec in TITLES]
            ends=[p-1 for p in starts[1:]]+[len(src)]
        for (sec,title),first,last in zip(TITLES.items(),starts,ends):
            dest=fitz.open();dest.insert_pdf(src,from_page=first-1,to_page=last-1)
            local_toc=[]
            for level,t,p in toc:
                if first<=p<=last:local_toc.append([level,t,p-first+1])
            if local_toc:dest.set_toc(local_toc)
            dest.set_metadata({'title':f'{sec} {title} – {kind}','subject':'4 vwo · Boek 4 · Hoofdstuk 2'})
            name=f'{sec} – {kind}.pdf';dest.save(O/name,garbage=4,deflate=True);dest.close()
            manifest.append({'section':sec,'kind':kind,'file':f'paragrafen/{name}','source':filename,'source_pages':[first,last],'page_count':last-first+1})
(R/'QA/paragraph-exports.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
print('Paragraph exports:',len(manifest))
