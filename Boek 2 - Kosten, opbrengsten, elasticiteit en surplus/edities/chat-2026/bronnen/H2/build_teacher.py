"""Render the local teacher guide; does not alter repository authority."""
from build import ROOT, OUTPUT, render_markdown, embedded_html
from weasyprint import HTML

def build_teacher():
    src=(ROOT/'Docenten_en_bouwverantwoording.md').read_text()
    sections=src.split('<!-- PAGEBREAK -->')
    body=''.join('<section class="page teacher">'+render_markdown(x)+'</section>' for x in sections)
    text=embedded_html(body,'Docenteninformatie · Elasticiteit',extra_css='''
@page { @top-left {content:"4veco / Docenteninformatie";} }
.teacher h1{font-size:23pt;}
.teacher h2{font-size:15pt;}
.teacher h3{font-size:11.5pt;}
.teacher{font-size:10.3pt;line-height:1.31;}
.teacher table{font-size:9pt;line-height:1.25;}
.teacher th,.teacher td{padding:4pt;}
.teacher p{margin-bottom:7pt;}
.teacher code{font-size:8.4pt;font-family:Lato,sans-serif;overflow-wrap:anywhere;}
.hash{font-size:8.7pt;overflow-wrap:anywhere;}
''')
    (OUTPUT/'Boek_2_H2_Docenteninformatie.html').write_text(text)
    doc=HTML(string=text,base_url=str(ROOT)).render()
    doc.write_pdf(OUTPUT/'Boek_2_H2_Docenteninformatie.pdf')
    print('Teacher PDF:',len(doc.pages),'pages; designed:',len(sections))
    if len(doc.pages)!=len(sections):raise ValueError('Teacher page overflow; inspect layout')
    return len(doc.pages)
if __name__=='__main__':build_teacher()
