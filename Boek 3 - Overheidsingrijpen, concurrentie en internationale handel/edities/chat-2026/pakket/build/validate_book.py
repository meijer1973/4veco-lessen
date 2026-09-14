#!/usr/bin/env python3
"""Validate book assembly against the preserved input PDFs, not new content claims."""
from pathlib import Path
import json,hashlib,re
import fitz
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
M=json.loads((ROOT/'manifest.json').read_text())
A=json.loads((ROOT/'QA/assembly_manifest.json').read_text())
checks=[];diffs=[]
def check(name,ok,detail=''):
 checks.append({'check':name,'pass':bool(ok),'detail':detail})
for p,h in json.loads((ROOT/'QA/input_hashes.json').read_text()).items():
 check('unchanged_input:'+p,hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h)
for kind,out in zip(['student','answers','teacher'],A['outputs']):
 doc=fitz.open(ROOT/out['file']);records=json.loads((ROOT/f'QA/{kind}_page_map.json').read_text())
 check(kind+':page_count',len(doc)==out['pages'])
 check(kind+':all_source_pages',len(records)==out['source_pages'])
 check(kind+':chapters_within_authorized_limits', all(ch['pages']<=ch.get('student_page_limit',40) for ch in M['chapters']))
 check(kind+':chapter_recto_starts',all(n%2 for n in out['chapter_starts']))
 actual_blanks=[i+1 for i,p in enumerate(doc) if not p.get_text().strip() and len(p.get_images())==0]
 check(kind+':only_planned_blanks',actual_blanks==out['intentional_blank_pages'],str(actual_blanks))
 check(kind+':page_dimensions',all(abs(p.rect.width-595.2756)<.1 and abs(p.rect.height-841.8898)<.1 for p in doc))
 links=[l for p in doc for l in p.get_links()]
 check(kind+':all_internal_links_resolve',all(l.get('kind')==fitz.LINK_GOTO and 0<=l.get('page',-1)<len(doc) for l in links))
 check(kind+':bookmarks_resolve',all(1<=n<=len(doc) for _,_,n in doc.get_toc()))
 srcs={}
 for r in records:
  src=srcs.setdefault(r['source'],fitz.open(ROOT/r['source']))
  orig=src[r['local_page']-1];new=doc[r['book_page']-1]
  # All original page geometry is retained; differences allowed only in audited edit boxes.
  mat=fitz.Matrix(1.25,1.25)
  oldpix=orig.get_pixmap(matrix=mat,alpha=False)
  newpix=new.get_pixmap(matrix=mat,alpha=False)
  a=np.frombuffer(oldpix.samples,dtype=np.uint8).reshape(oldpix.height,oldpix.width,3)
  b=np.frombuffer(newpix.samples,dtype=np.uint8).reshape(newpix.height,newpix.width,3)
  d=np.any(np.abs(a.astype(np.int16)-b.astype(np.int16))>3,axis=2)
  for e in r['edits']:
   rect=fitz.Rect(e.get('output_rect',e['rect']));rect.x0-=1.8;rect.x1+=1.8;rect.y0-=1.8;rect.y1+=1.8
   x0,y0,x1,y1=[int(round(v*1.25)) for v in rect]
   d[max(0,y0):min(len(d),y1+1),max(0,x0):min(d.shape[1],x1+1)]=False
  errors=int(d.sum())
  check(f'{kind}:render_conservation:{r["source"]}:{r["local_page"]}',errors==0,str(errors))
  if errors:diffs.append({'kind':kind,'source_page':r['local_page'],'book_page':r['book_page'],'unexpected_pixels':errors})
  # Non-edited text words and their positions must also be conserved.
  masks=[fitz.Rect(e.get('output_rect',e['rect']))+(-.2,-.2,.2,.2) for e in r['edits']]
  def untouched(p):
   return sorted([w for w in p.get_text('words') if not any(fitz.Rect(w[:4]).intersects(box) for box in masks)],key=lambda w:(round(w[1],1),w[0]))
  ow,nw=untouched(orig),untouched(new)
  same=len(ow)==len(nw) and all(x[4]==y[4] and max(abs(a-b) for a,b in zip(x[:4],y[:4]))<.025 for x,y in zip(ow,nw))
  check(f'{kind}:text_geometry:{r["book_page"]}',same,f'{len(ow)} / {len(nw)} untouched words')
  # Continuous number in the expected footer location, avoiding other digits in the text.
  footer=new.get_text(clip=fitz.Rect(480,801,550,832)).strip()
  check(f'{kind}:page_number:{r["book_page"]}',footer==str(r['book_page']),footer)
  for e in r['edits']:
   if e['reason']=='inline_page_reference':
    text=new.get_text(clip=fitz.Rect(e['rect'])+(-2,-2,2,2))
    nums=re.findall(r'pagina(?:’s|\x27s)?\s+(\d+)',e['new'],re.I)
    check(f'{kind}:updated_reference:{r["book_page"]}:{e["old"][:30]}',all(n in text for n in nums),text.strip())
 for src in srcs.values():src.close()
 if kind=='student':
  check('student:cover_image_embedded',bool(doc[0].get_images()))
  check('student:documented_typo_removed',all('Qsubub' not in doc[p].get_text() for p in range(4,128)))
  for ch,opg,spread in [(1,'48',[50,51]),(2,'36',[86,87]),(3,'35',[124,125])]:
   text=' '.join(doc[p-1].get_text() for p in spread)
   check('student:spread_'+str(ch),spread[0]%2==0 and spread[1]==spread[0]+1 and 'Opgave '+opg in text)
  t=doc[3].get_text()
  for chapter in M['chapters']:
   for para in chapter['paragraphs']:
    check('student:full_contents:'+para['section'],para['section'] in t)
 doc.close()
report={'checks':len(checks),'passed':sum(x['pass'] for x in checks),'failed':sum(not x['pass'] for x in checks),'source_pages_render_compared':sum(o['source_pages'] for o in A['outputs']),'comparison':'All source pages rendered at 90 dpi; No raster differences above 3/255 allowed outside recorded input/output edit boxes plus 1.8-point antialias margin. The three-level tolerance accounts for decimal/color rounding during PDF redaction, with unedited word text and positions separately checked to 0.025 pt. Semantic content review is outside this assembly test.','unexpected_differences':diffs,'items':checks}
(ROOT/'QA/validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps({k:v for k,v in report.items() if k not in ['items','unexpected_differences']},ensure_ascii=False,indent=2));print('FAILURES',json.dumps([x for x in checks if not x['pass']][:12],ensure_ascii=False,indent=2))
raise SystemExit(1 if report['failed'] else 0)
