"""Five additional exact SVG figures. Retains baseline figures and records."""
from pathlib import Path
import json
from html import escape
import make_assets as g
ROOT=Path(__file__).resolve().parent

def txt(x,y,s,size=17,fill=g.INK,anchor='start',weight='normal'):
 return f'<text x="{x:.4f}" y="{y:.4f}" font-family="Lato,DejaVu Sans,sans-serif" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}">{escape(s)}</text>'

def ledger():
 w,h=800,255
 s=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><rect width="800" height="255" rx="8" fill="#f7fafb"/>']
 s += [txt(24,30,'Dezelfde schaal: elk bedrag is euro per dag',18,weight='bold')]
 rows=[(70,'Zonder belasting',[(180,'CS 180',g.BLUE),(180,'PS 180',g.GREEN)]),(143,'Met belasting',[(80,'CS 80',g.BLUE),(80,'PS 80',g.GREEN),(160,'O 160',g.PURPLE),(40,'W 40',g.GOLD)])]
 records=[]
 for y,title,segments in rows:
  s.append(txt(24,y+28,title,17));x=200
  for value,label,color in segments:
   bw=value/360*562
   s.append(f'<rect x="{x:.4f}" y="{y}" width="{bw:.4f}" height="43" fill="{color}" fill-opacity="0.17" stroke="{color}" stroke-width="1.2" data-euros="{value}"/>')
   s.append(txt(x+bw/2,y+27,label,16,color,'middle','bold'))
   records.append({'euros':value,'x':x,'y':y,'width':bw,'height':43})
   x+=bw
 s.append(txt(200,223,'Nieuwe welvaartsmaat: CS + PS + O = 320. W telt niet mee.',17,weight='bold'))
 s.append('</svg>')
 g.save('3.1.2_rev_ledger',''.join(s),{'type':'ledger','scale':562/360,'bars':records,'before':360,'after':320,'loss':40})

def scales():
 s=['<svg xmlns="http://www.w3.org/2000/svg" width="800" height="335" viewBox="0 0 800 335"><rect width="800" height="335" rx="8" fill="#f7fafb"/>']
 rec=[]
 for off,top,step in [(0,16,4),(400,32,8)]:
  x0,x1,yt,yb=off+55,off+374,58,253
  X=lambda q:x0+(x1-x0)*q/140
  Y=lambda p:yb-(yb-yt)*p/top
  s.append(txt(off+203,27,f'P-as tot € {top}',18,anchor='middle',weight='bold'))
  s.append(txt(off+55,48,'P (€ per product)',15,weight='bold'))
  for q in [0,20,40,60,80,100,120,140]:
   s.append(f'<line x1="{X(q):.4f}" y1="{yt}" x2="{X(q):.4f}" y2="{yb}" stroke="#dce5e9" stroke-width="0.65"/>')
   s.append(txt(X(q),yb+22,str(q),14,anchor='middle'))
  for p in range(0,top+1,step):
   s.append(f'<line x1="{x0}" y1="{Y(p):.4f}" x2="{x1}" y2="{Y(p):.4f}" stroke="#dce5e9" stroke-width="0.65"/>')
   s.append(txt(x0-9,Y(p)+5,str(p),14,anchor='end'))
  s.append(f'<path d="M{x0} {yt} V{yb} H{x1}" fill="none" stroke="{g.INK}" stroke-width="1.6"/>')
  ends=[(X(0),Y(14)),(X(140),Y(0))]
  s.append(f'<line x1="{ends[0][0]:.4f}" y1="{ends[0][1]:.4f}" x2="{ends[1][0]:.4f}" y2="{ends[1][1]:.4f}" stroke="{g.BLUE}" stroke-width="2.8" data-role="demand"/>')
  s.append(txt(X(112),Y(2.8)-15,'V',17,g.BLUE,weight='bold'))
  s.append(txt(off+209,303,'Q (producten per week)',15,anchor='middle',weight='bold'))
  rec.append({'origin':[x0,yb],'xscale':(x1-x0)/140,'yscale':(yb-yt)/top,'endpoints':ends,'equation':[14,-.1]})
 s.append('</svg>')
 g.save('3.1.2_rev_scales',''.join(s),{'type':'scale_comparison','panels':rec})

if __name__=='__main__':
 old=json.loads((ROOT/'QA/figure_geometry.json').read_text())
 # Re-running does not duplicate revision records.
 old=[r for r in old if '_rev_' not in r['file']]
 ledger();scales()
 g.graph('3.1.5_rev_nopurchase',14,.1,2,.1,140,16,'krat appels','per week','floor',10,policy=None)
 g.graph('3.1.5_rev_quota_base',26,.2,8,.1,100,28,'krat paprika','per week','base',0)
 g.graph('3.1.5_rev_quota_answer',26,.2,8,.1,100,28,'krat paprika','per week','quota',40)
 (ROOT/'QA/figure_geometry.json').write_text(json.dumps(old+g.RECORDS,ensure_ascii=False,indent=2))
 print('Additional figures:',len(g.RECORDS))
