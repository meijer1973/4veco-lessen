"""Build the six-page teacher guide and retain explicit page mapping."""
import re,json
from weasyprint import HTML
from build import ROOT,OUTPUT,render_markdown,embedded_html

def build_teacher():
    text=(ROOT/'2.3 Docenteninformatie.md').read_text()
    parts=re.split(r'<!-- PAGE (.*?) -->',text,flags=re.S)
    pages=[]
    for i in range(1,len(parts),2):
        meta=json.loads(parts[i]);body=parts[i+1].strip()
        title='' if i==1 else '<div class="page-title">'+meta['title']+'</div>'
        pages.append(f'<section class="page teacher" data-designed-page="{len(pages)+1}">'+title+render_markdown(body)+'</section>')
    out=embedded_html('\n'.join(pages),'Docenteninformatie · Surplus en welvaart', '''
@page { @top-left {content:"4veco / Docenteninformatie";} }
.teacher{font-size:10.6pt;line-height:1.35;}
.teacher table{font-size:9.3pt;line-height:1.27;}
.teacher h3{font-size:12.5pt;}
''')
    (OUTPUT/'Boek_2_H3_Docenteninformatie.html').write_text(out)
    doc=HTML(string=out,base_url=str(ROOT)).render()
    doc.write_pdf(OUTPUT/'Boek_2_H3_Docenteninformatie.pdf')
    page_map=[]
    for n,pg in enumerate(doc.pages,1):
        marks={b.element.get('data-designed-page') for b in pg._page_box.descendants() if getattr(b,'element',None) is not None and b.element.get('data-designed-page')}
        page_map.append({'pdf_page':n,'designed_pages':sorted(marks,key=int)})
    (OUTPUT/'teacher_page_map.json').write_text(json.dumps(page_map,indent=2))
    print('Teacher guide:',len(doc.pages),'pages; designed:',len(pages))
    print('Map:',page_map)
    return len(doc.pages)
if __name__=='__main__':build_teacher()
