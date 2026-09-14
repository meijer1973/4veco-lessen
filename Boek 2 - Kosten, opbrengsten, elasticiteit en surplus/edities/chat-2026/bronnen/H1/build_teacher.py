from build import ROOT, OUTPUT, render_markdown, embedded_html
from weasyprint import HTML

def build_teacher():
    src=(ROOT/'Docenten_en_bouwverantwoording.md').read_text()
    sections=src.split('<!-- PAGEBREAK -->')
    body=''.join('<section class="page teacher">'+render_markdown(x)+'</section>' for x in sections)
    text=embedded_html(body,'Docenteninformatie · Kosten en opbrengsten',extra_css='''
@page { @top-left {content:"4veco / Docenteninformatie";} }
.teacher h1{font-size:23pt;}
.teacher h2{font-size:16pt;}
.teacher h3{font-size:12pt;}
.teacher{font-size:10.3pt;line-height:1.29;}
.teacher table{font-size:9pt;line-height:1.26;}
.teacher th,.teacher td{padding:4pt;}
.teacher p{margin-bottom:7pt;}
''')
    (OUTPUT/'Boek_2_H1_Docenteninformatie.html').write_text(text)
    doc=HTML(string=text,base_url=str(ROOT)).render()
    doc.write_pdf(OUTPUT/'Boek_2_H1_Docenteninformatie.pdf')
    print('Teacher PDF:',len(doc.pages),'pages')
if __name__=='__main__':build_teacher()
