from pathlib import Path
import fitz
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parents[1]
selections={
 'student':('Boek_4_Compleet.pdf',[1,2,3,4,5,6,38,39,42,43,44,45,95,98,99,102,103,104,148,149,152,153,154,155,156,157,158,159,160,161,162]),
 'answers':('Boek_4_Compleet_Antwoorden.pdf',[1,2,3,22,23,46,47,64]),
 'teacher':('Boek_4_Compleet_Docenteninformatie.pdf',[1,2,3,9,10,11,19,20,21,28])}
for kind,(fn,pages) in selections.items():
 folder=R/'qa/renders'/kind;folder.mkdir(parents=True,exist_ok=True)
 doc=fitz.open(R/'output'/fn)
 thumbs=[]
 for pn in pages:
  pix=doc[pn-1].get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False)
  path=folder/f'p{pn:03d}.png';pix.save(path)
  im=Image.open(path);im.thumbnail((360,510));thumbs.append((im,pn))
 for i in range(0,len(thumbs),6):
  sheet=Image.new('RGB',(1140,1110),'#e9ecef');draw=ImageDraw.Draw(sheet)
  for j,(im,pn) in enumerate(thumbs[i:i+6]):
   x=10+(j%3)*380;y=10+(j//3)*550;sheet.paste(im,(x,y+23));draw.text((x,y),f'{kind} / {pn}',fill='black')
  sheet.save(folder/f'contact_{i:02d}.jpg',quality=90)
