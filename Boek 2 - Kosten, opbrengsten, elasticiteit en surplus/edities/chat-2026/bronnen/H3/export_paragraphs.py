"""Export per-paragraph sources and PDFs without changing the chapter pagination.
The student PDFs are exact page extracts of the checked chapter. Answer extracts
are rendered separately; all figure assets used by each paragraph are included.
"""
from pathlib import Path
import re,json,shutil
import fitz
from weasyprint import HTML
from build import ROOT,OUTPUT,render_markdown,embedded_html

SPECS=[
('2.3.1','Consumentensurplus',2,9,5,True),
('2.3.2','Producentensurplus en totaal surplus',10,19,13,True),
('2.3.3','Pareto-efficiëntie en welvaartsverlies',20,30,24,True),
('2.3.4','Gemengde opgaven',31,36,31,False)]

def export():
    answers=(ROOT/'2.3 Surplus en welvaart – antwoorden.md').read_text()
    source=fitz.open(OUTPUT/'Boek_2_H3_Surplus_en_welvaart.pdf')
    manifest=[]
    for pid,title,start,end,exercise_start,is_theory in SPECS:
        folder=ROOT/'paragrafen'/f'{pid} {title}';folder.mkdir(parents=True,exist_ok=True)
        infile=next((ROOT/'manuscript').glob(pid+' *'))
        full=infile.read_text()
        exercises=full[full.index('## Uitgewerkt voorbeeld'):] if is_theory else full
        if is_theory:
            (folder/f'{pid} {title} – paragraaf.md').write_text(full)
            d=fitz.open();d.insert_pdf(source,from_page=start-1,to_page=end-1);d.save(folder/f'{pid} {title} – paragraaf.pdf');d.close()
        (folder/f'{pid} {title} – opgaven.md').write_text(f'# Opgaven {pid} · {title}\n\n'+exercises if is_theory else full)
        d=fitz.open();d.insert_pdf(source,from_page=exercise_start-1,to_page=end-1);d.save(folder/f'{pid} {title} – opgaven.pdf');d.close()
        match=re.search(r'^# '+re.escape(pid)+r' [\s\S]*?(?=^# |\Z)',answers,re.M)
        if not match:raise ValueError('Missing answers '+pid)
        ans=match.group(0).strip()
        (folder/f'{pid} {title} – antwoorden.md').write_text(ans+'\n')
        html=embedded_html('<main class="answer">'+render_markdown(re.sub(r'^([1-9])\) ',r'\1\\) ',ans,flags=re.M))+'</main>',f'Antwoorden {pid}', '@page { @top-left {content:"4veco / Antwoorden";} } .answer{font-size:11.1pt;line-height:1.33;}')
        HTML(string=html,base_url=str(ROOT)).write_pdf(folder/f'{pid} {title} – antwoorden.pdf')
        assets=folder/'_assets';assets.mkdir(exist_ok=True)
        refs=set(re.findall(r'_assets/([^"\s)>]+\.svg)',full+'\n'+ans))
        for ref in refs:
            for ext in ['.svg','.png']:
                src=ROOT/'_assets'/Path(ref).with_suffix(ext)
                shutil.copy2(src,assets/src.name)
        (folder/'build_pdf.py').write_text('''"""Rebuild the full checked chapter, then renew all paragraph exports."""\nfrom pathlib import Path\nimport subprocess,sys\nroot=Path(__file__).resolve().parents[2]\nsubprocess.run([sys.executable,str(root/'build_all.py')],check=True)\n''')
        manifest.append({'id':pid,'title':title,'student_pages':[start,end],'exercise_pages':[exercise_start,end],'theory':is_theory,'assets':sorted(refs),'folder':str(folder.relative_to(ROOT))})
    source.close()
    (ROOT/'paragrafen/manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
    print('Exported four paragraphs; student PDFs retain printed chapter page numbers.')
if __name__=='__main__':export()
