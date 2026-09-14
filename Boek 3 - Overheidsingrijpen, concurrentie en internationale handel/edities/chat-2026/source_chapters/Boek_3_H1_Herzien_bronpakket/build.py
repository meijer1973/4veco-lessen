"""Rebuild locally: python build_all.py. Edit page Markdown to revise text directly.
The optional revise_*.py scripts reconstruct the authored revision from revision_base/.
Dependencies: weasyprint markdown-it-py beautifulsoup4 cairosvg pymupdf.
"""
from pathlib import Path
import re,json,base64,runpy
from markdown_it import MarkdownIt
from bs4 import BeautifulSoup
from weasyprint import HTML
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'output'; OUT.mkdir(exist_ok=True)
md=MarkdownIt('commonmark',{'html':True}).enable('table')
CSS=(ROOT/'print.css').read_text()
def render_md(body):
    pat=re.compile(r'(<div\b[^>]*>)([\s\S]*?)(</div>)')
    def f(m):
        inn=m.group(2)
        if '\n\n' in inn or re.search(r'^\|',inn,re.M):return m.group(1)+'\n'+md.render(inn.strip())+'\n'+m.group(3)
        return m.group(0)
    body=re.sub(r'(</(?:div|a)>)[ \t]*\n(?=#)',r'\1\n\n',body)
    return md.render(pat.sub(f,body))
def page_chunks(path):
    chunks=re.split(r'<!-- PAGE (.*?) -->',path.read_text(),flags=re.S)
    for i in range(1,len(chunks),2):
        p=json.loads(chunks[i]);p['body']=chunks[i+1].strip();yield p

def build(pages,stem,title,kind='student'):
    chunks=[]
    for n,p in enumerate(pages,1):
        head='' if n==1 or re.search(r'^# ',p['body'],re.M) or p['body'].lstrip().startswith('## ') else f'<div class="page-title">{p["section"]} · {p["title"]}</div>'
        chunks.append(f'<section class="page {kind}" data-designed-page="{n}">'+head+render_md(p['body'])+'</section>')
    soup=BeautifulSoup('\n'.join(chunks),'html.parser')
    for img in soup.find_all('img'):
        f=ROOT/img['src']
        if not f.exists():raise FileNotFoundError(f)
        img['src']='data:'+('image/svg+xml' if f.suffix=='.svg' else 'image/png')+';base64,'+base64.b64encode(f.read_bytes()).decode()
    extra='' if kind=='student' else ('html{font-size:10.8pt;line-height:1.36;} .formula{font-size:10pt;}' if kind=='answer' else 'html{font-size:10.7pt;}')
    html='<!doctype html><html lang="nl"><head><meta charset="utf-8"><title>'+title+'</title><style>'+CSS+extra+'</style></head><body>'+str(soup)+'</body></html>'
    (OUT/(stem+'.html')).write_text(html)
    doc=HTML(string=html,base_url=str(ROOT)).render()
    doc.write_pdf(OUT/(stem+'.pdf'))
    mapping=[]
    for n,pg in enumerate(doc.pages,1):
        nums=set()
        for el in pg._page_box.descendants():
            e=getattr(el,'element',None)
            if e is not None and e.get('data-designed-page'):nums.add(int(e.get('data-designed-page')))
        mapping.append({'pdf_page':n,'designed_pages':sorted(nums)})
    (ROOT/'QA'/(stem+'_page_map.json')).write_text(json.dumps(mapping,indent=2))
    overflow=[m for m in mapping if m['designed_pages']!=[m['pdf_page']]]
    print(stem,'physical:',len(doc.pages),'designed:',len(pages),'map drift:',overflow[:10])
    return doc
if __name__=='__main__':
    if not (ROOT/'chapter-order.json').exists():
        g=runpy.run_path(str(ROOT/'author_chapter.py'))
        pages=g['PAGES']
    else:pages=[p for f in json.loads((ROOT/'chapter-order.json').read_text()) for p in page_chunks(ROOT/f)]
    build(pages,'Boek_3_H1_Overheidsingrijpen','Boek 3 · Hoofdstuk 3.1 · Overheidsingrijpen')
    for source,stem,title,kind in [('Antwoorden.md','Boek_3_H1_Antwoorden','Antwoorden · Overheidsingrijpen','answer'),('Docenteninformatie.md','Boek_3_H1_Docenteninformatie','Docenteninformatie · Overheidsingrijpen','teacher'),('Beoordeling_en_wijzigingen.md','Boek_3_H1_Beoordeling_en_wijzigingen','Beoordeling en wijzigingen · Overheidsingrijpen','teacher')]:
        if (ROOT/source).exists():build(list(page_chunks(ROOT/source)),stem,title,kind)
