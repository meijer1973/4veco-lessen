"""Extract six paragraph PDFs without reflow; preserve chapter page numbers."""
from pathlib import Path
import json, re
import fitz
from bs4 import BeautifulSoup
from author_common import TITLES
ROOT=Path(__file__).resolve().parent
RANGES={'4.3.1':(2,11),'4.3.2':(12,19),'4.3.3':(20,28),'4.3.4':(29,36),'4.3.5':(37,43),'4.3.6':(44,48)}
e=json.loads((ROOT/'QA/exercises.json').read_text()); manifest=[]
doc=fitz.open(ROOT/'output/Boek_4_H3_Arbeidsmarkt.pdf')
for sec,(start,end) in RANGES.items():
    d=ROOT/'paragrafen'/sec;d.mkdir(parents=True,exist_ok=True)
    title=TITLES[sec].replace(':',' –')
    filename=f'{sec} {title} – paragraaf.pdf'
    p=fitz.open();p.insert_pdf(doc,from_page=start-1,to_page=end-1)
    p.set_metadata({'title':f'{sec} {TITLES[sec]}','subject':'Boek 4 · Arbeidsmarkt · 4 vwo'})
    p.set_toc([[1,sec+' '+TITLES[sec],1]]);p.save(d/filename,garbage=4,deflate=True);p.close()
    text=(ROOT/f'{sec} manuscript.md').read_text().replace('src="_assets/','src="../../_assets/')
    (d/f'{sec} {title} – paragraaf.md').write_text(text)
    startheading='## Uitgewerkt voorbeeld' if sec!='4.3.6' else '## Gemengde oefening'
    body=text[text.index(startheading):] if startheading in text else text
    (d/f'{sec} {title} – opgaven.md').write_text('# Opgaven '+sec+'\n\n'+body)
    ans='# Antwoorden '+sec+' · '+TITLES[sec]+'\n\n'
    for ex in [x for x in e if x['section']==sec]:
        ans+=f'## Opgave {ex["number"]} · {ex["title"]}\n\n'
        for q in ex['questions']:ans+=f'**{q["label"]}.** '+q['answer']+'\n\n'
        if ex['answer_fig']:ans+='![Uitwerking opgave '+str(ex['number'])+'](../../_assets/'+ex['answer_fig']+'.svg)\n\n'
    (d/f'{sec} {title} – antwoorden.md').write_text(ans)
    manifest.append({'id':sec,'chapter_pages':[start,end],'page_count':end-start+1,'pdf':str((d/filename).relative_to(ROOT))})
(ROOT/'QA/paragraph-exports.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
print('Exported six paragraph PDFs and their editable manuscripts; original chapter page numbers retained.')
