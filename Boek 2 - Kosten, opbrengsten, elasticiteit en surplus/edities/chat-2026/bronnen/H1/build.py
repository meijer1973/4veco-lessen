"""Build the standalone print edition. Python 3; weasyprint, markdown-it-py, beautifulsoup4.
Run: python make_assets.py && python build.py
No network or external fonts are required. Fonts are resolved from the local system.
"""
from pathlib import Path
import base64, re, json, sys
from markdown_it import MarkdownIt
from bs4 import BeautifulSoup
from weasyprint import HTML

ROOT=Path(__file__).resolve().parent
OUTPUT=ROOT/'output'; OUTPUT.mkdir(exist_ok=True)
def load_pages():
    pages=[]
    for name in json.loads((ROOT/'chapter-order.json').read_text()):
        text=(ROOT/name).read_text()
        chunks=re.split(r'<!-- PAGE (.*?) -->',text,flags=re.S)
        if len(chunks)<3:
            raise ValueError(f'No page metadata in {name}')
        for i in range(1,len(chunks),2):
            p=json.loads(chunks[i]);p['body']=chunks[i+1].strip();pages.append(p)
    return pages
PAGES=load_pages()
md=MarkdownIt('commonmark',{'html':True,'breaks':False}).enable('table')
CSS='''
@page {size:A4; margin:17mm 18mm 17mm 19mm;
 @top-left {content:"4veco  /  Boek 2";font-family:Lato,sans-serif;font-size:8.5pt;color:#536777;}
 @top-right {content:"2.1  Kosten en opbrengsten";font-family:Lato,sans-serif;font-size:8.5pt;color:#536777;}
 @bottom-left {content:"Economie · 4 vwo";font-family:Lato,sans-serif;font-size:8pt;color:#536777;}
 @bottom-right {content:counter(page);font-family:Lato,sans-serif;font-size:9pt;color:#183247;}
}
@page:first {@top-left{content:none;}@top-right{content:none;}}
* {box-sizing:border-box;}
html{font-family:Lato,"DejaVu Sans",sans-serif;font-size:11.2pt;line-height:1.32;color:#183247;}
body{margin:0;}
p{margin:0 0 6pt;orphans:3;widows:3;}
.page{break-before:page;}
.page:first-child{break-before:auto;}
.page-title{font-size:18pt;line-height:1.13;font-weight:800;border-bottom:1.5pt solid #17688f;padding:0 0 8pt;margin:0 0 12pt;}
h1{font-size:25pt;line-height:1.13;margin:5pt 0 12pt;font-weight:800;break-after:avoid;}
h2{font-size:17pt;line-height:1.15;color:#17688f;margin:10pt 0 8pt;break-after:avoid;}
h3{font-size:12.5pt;line-height:1.22;margin:11pt 0 7pt;break-after:avoid;}
h2:first-child,h3:first-child{margin-top:0;}
a{color:inherit;text-decoration:none;}
.kicker{letter-spacing:1pt;color:#17688f;font-size:9pt;font-weight:800;margin:0 0 12pt;}
.box,.definition,.formula,.source,.route{padding:7pt 10pt;margin:8pt 0 9pt;break-inside:avoid;background:#f2f6f8;border-left:3pt solid #17688f;}
.box p:last-child,.definition p:last-child,.formula p:last-child,.source p:last-child{margin-bottom:0;}
.definition{background:#f4f7f8;padding:7pt 10pt;margin:7pt 0 9pt;}
.formula{font-family:"DejaVu Sans Mono",monospace;font-size:11.3pt;line-height:1.6;background:#eef5f6;border-left-color:#227064;}
.goals{font-size:10.7pt;line-height:1.38;}
.summary{font-size:10.5pt;line-height:1.5;}
.warning{border-left-color:#ad601b;background:#fbf5ed;}
.source{border-left-color:#536777;font-size:10.6pt;}
.route{font-size:10.2pt;line-height:1.3;}
.calculation{font-family:"DejaVu Sans Mono",monospace;line-height:1.55;margin:8pt 0 10pt;padding:8pt 13pt;background:#f3f6f7;break-inside:avoid;}
.exercise{break-inside:avoid;border:0.6pt solid #d5dfe5;border-radius:3pt;padding:8pt 10pt;margin:0 0 10pt;background:white;}
.exercise>p:first-child{margin-top:0;}
.exercise>p:last-child{margin-bottom:0;}
.exercise>p{margin-bottom:6pt;}
.exercise>b:first-child{display:block;margin-bottom:7pt;font-size:12pt;}
.target{border-top:3pt solid #17688f;}
table{border-collapse:collapse;width:100%;margin:7pt 0 9pt;font-size:10.1pt;line-height:1.27;table-layout:auto;break-inside:avoid;}
th{background:#edf2f5;font-weight:700;vertical-align:bottom;text-align:left;border-bottom:1pt solid #9dabb7;}
td,th{padding:4.4pt 5pt;border-bottom:0.55pt solid #dce4e9;}
td{vertical-align:top;} tr:nth-child(even) td{background:#f8fafb;}
figure{margin:10pt 0 11pt;break-inside:avoid;}
figure img{display:block;width:100%;height:auto;}
figcaption{font-size:9.3pt;line-height:1.3;color:#536777;margin:5pt 0 0;}
.small{font-size:9.4pt;line-height:1.33;}
.muted{color:#536777;}
.cover-title{font-size:38pt;line-height:1.05;letter-spacing:-0.6pt;font-weight:900;margin:14pt 0 14pt;}
.lead{font-size:14.5pt;line-height:1.3;margin:0 0 13pt;color:#17688f;}
.contents{margin:12pt 0 12pt;}
.contents a{display:block;border-top:0.6pt solid #cbd7df;padding:6pt 0;}
.contents b{display:block;font-size:12pt;}
.contents span{display:block;color:#536777;font-size:10.5pt;margin-top:2pt;}
.answer h2{margin-top:16pt;}
.answer p{margin-bottom:7pt;}
.answer .why{font-size:10.6pt;color:#455c6d;}
.answer .exercise{break-inside:auto;}
.answer .answer-block{break-inside:avoid;margin-bottom:10pt;}
.teacher{font-size:10.7pt;}
.teacher table{font-size:9.1pt;}
'''
def render_markdown(body):
    # Parse Markdown inside authoring divs as well, while preserving figure/table markup.
    pat=re.compile(r'(<div\b[^>]*>)([\s\S]*?)(</div>)')
    def sub(m):
        inner=m.group(2)
        if '\n\n' in inner or re.search(r'^\|',inner,re.M):
            return m.group(1)+'\n'+md.render(inner.strip())+'\n'+m.group(3)
        return m.group(0)
    body=re.sub(r'(</(?:div|a)>)[ \t]*\n(?=#)', r'\1\n\n', body)
    body=pat.sub(sub,body)
    return md.render(body)

def embedded_html(body,title,extra_css=''):
    soup=BeautifulSoup(body,'html.parser')
    for img in soup.find_all('img'):
        path=ROOT/img['src']
        if not path.exists(): raise FileNotFoundError(path)
        typ='image/png' if path.suffix=='.png' else 'image/svg+xml'
        img['src']='data:'+typ+';base64,'+base64.b64encode(path.read_bytes()).decode()
    return '<!doctype html><html lang="nl"><head><meta charset="utf-8"><title>'+title+'</title><style>'+CSS+extra_css+'</style></head><body>'+str(soup)+'</body></html>'

def build_chapter():
    html=[]
    for i,p in enumerate(PAGES):
        heading='' if i==0 or re.search(r'^# ',p['body'],re.M) else f'<div class="page-title">{p["section"]} · {p["title"]}</div>'
        html.append(f'<section class="page" data-designed-page="{i+1}">{heading}'+render_markdown(p['body'])+'</section>')
    out=embedded_html('\n'.join(html),'Boek 2 · Hoofdstuk 2.1 · Kosten en opbrengsten')
    (OUTPUT/'Boek_2_H1_Kosten_en_opbrengsten.html').write_text(out)
    doc=HTML(string=out,base_url=str(ROOT)).render()
    doc.write_pdf(OUTPUT/'Boek_2_H1_Kosten_en_opbrengsten.pdf')
    page_map=[]
    for n,pg in enumerate(doc.pages,1):
        markers=set()
        for b in pg._page_box.descendants():
            el=getattr(b,'element',None)
            if el is not None and el.get('data-designed-page'):markers.add(el.get('data-designed-page'))
        page_map.append({'pdf_page':n,'designed_pages':sorted(markers,key=int)})
    (OUTPUT/'page_map.json').write_text(json.dumps(page_map,indent=2))
    (ROOT/'2.1 Kosten en opbrengsten – hoofdstuk.md').write_text('\n\n<div class="page-break"></div>\n\n'.join(p['body'] for p in PAGES))
    print('Chapter PDF:',len(doc.pages),'pages; designed:',len(PAGES))
    print('Overflow mapping:',[x for x in page_map if x['pdf_page']!=int(x['designed_pages'][0])])
    return len(doc.pages)

if __name__=='__main__':build_chapter()
