"""Export chapter fragments without reflow. Revised chapter printed page numbers remain."""
from pathlib import Path
import fitz
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'paragrafen';OUT.mkdir(exist_ok=True)
rows=[
 ('3.1.1','Belastingen – wig en nieuw evenwicht',2,9,2,6),
 ('3.1.2','Belastingdruk en welvaartsverlies',10,18,7,10),
 ('3.1.3','Subsidies',19,27,11,16),
 ('3.1.4','Maximumprijs',28,34,17,21),
 ('3.1.5','Minimumprijs en quota',35,43,22,27),
 ('3.1.6','Gemengde opgaven – overheidsingrijpen',44,47,28,31),
]
for id,title,a,b,c,d in rows:
    for src,start,end,kind in [('Boek_3_H1_Overheidsingrijpen.pdf',a,b,'paragraaf' if id!='3.1.6' else 'opgaven'),('Boek_3_H1_Antwoorden.pdf',c,d,'antwoorden')]:
        with fitz.open(ROOT/'output'/src) as base,fitz.open() as out:
            out.insert_pdf(base,from_page=start-1,to_page=end-1,links=False)
            out.set_metadata({'title':f'{id} {title} – {kind}','author':'4veco','subject':'Uitsnede met oorspronkelijke hoofdstukpaginering'})
            out.set_page_labels([{'startpage':0,'prefix':'','style':'D','firstpagenum':start}])
            out.set_toc([[1,f'{id} {title}',1]])
            out.save(OUT/f'{id} {title} – {kind}.pdf',garbage=4,deflate=True)
print('Paragraph PDF exports:',len(list(OUT.glob('*.pdf'))))
