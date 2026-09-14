from pathlib import Path
import re,json,hashlib,unicodedata
from bs4 import BeautifulSoup
import fitz
R=Path(__file__).resolve().parents[1]
TITLES=['Monopolie','Marktvormen en marktfalen','Arbeidsmarkt']
ENDS=['Monopolie','Marktvormen_en_marktfalen','Arbeidsmarkt']
M={'book':{'nr':4,'title':'Monopolie, marktfalen en arbeidsmarkt','edition':'Samengestelde editie','year':2026},'cover':'inputs/cover.png','chapters':[]}
G={}
for nr,(title,end) in enumerate(zip(TITLES,ENDS),1):
 S=R/'source_chapters'/f'Boek_4_H{nr}_bronpakket'
 intro=BeautifulSoup((S/'00 Inleiding.md').read_text(),'html.parser')
 ch={'nr':nr,'id':f'4.{nr}','title':title,'student':f'inputs/Boek_4_H{nr}_{end}.pdf','answers':f'inputs/Boek_4_H{nr}_Antwoorden.pdf','teacher':f'inputs/Boek_4_H{nr}_Docenteninformatie.pdf','paragraphs':[],'intro_entries':[]}
 for a in intro.select('.contents a'):
  pn=int(a.select_one('span').text.strip());a.select_one('span').extract();t=a.select_one('b').get_text(' ',strip=True)
  t=re.sub(r'\s+',' ',t).replace(' · ',' ').strip()
  e={'title':t,'local_page':pn}
  ch['intro_entries'].append(e)
  if re.match(r'4\.\d\.\d',t):ch['paragraphs'].append(e)
 ch['pages']=len(fitz.open(R/ch['student']))
 # First heading of each answer, including target exercises whose heading level differs.
 for kind in ['student','answers']:
  d=fitz.open(R/ch[kind]);loc={}
  for i,p in enumerate(d):
   for line in p.get_text().splitlines():
    m=re.match(r'^Opgave\s+(\d+[A-Z]?)\b',line)
    if m and m.group(1) not in loc: loc[m.group(1)]=i+1
  ch[kind+'_exercises']=loc
 assert set(ch['student_exercises'])==set(ch['answers_exercises']),nr
 ch['answer_exercises']=ch.pop('answers_exercises')
 overview=next(S.glob('* Overzicht.md'));txt=overview.read_text()
 if nr==1:
  part=txt.split('# Begrippen\n',1)[1];entries=[]
  for line in part.splitlines():
   if line.startswith('| ') and not line.startswith('| Begrip'):
    cells=[c.strip() for c in line.strip('|').split('|')]
    if len(cells)==2:entries.append(cells)
 else:
  html=BeautifulSoup(txt,'html.parser');entries=[]
  for p in html.select('.glossary-columns p'):
   term=p.b.get_text(' ',strip=True);p.b.extract();definition=p.get_text(' ',strip=True);entries.append((term,definition))
 for term,definition in entries:
  key=term.casefold()
  if key not in G:G[key]={'term':term,'definitions':[]}
  G[key]['definitions'].append({'text':definition,'chapter':nr,'local_page':ch['pages'],'source_file':str(overview.relative_to(R))})
 ch['mixed_target']={'nr':[35,58,49][nr-1], 'local_spread':[[34,35],[56,57],[46,47]][nr-1]}
 M['chapters'].append(ch)
(R/'manifest.json').write_text(json.dumps(M,ensure_ascii=False,indent=2))
G=sorted(G.values(),key=lambda e:unicodedata.normalize('NFKD',e['term'].casefold()))
(R/'book-matter/glossary.json').write_text(json.dumps(G,ensure_ascii=False,indent=2))
hashes={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (R/'inputs').glob('*')}
(R/'qa/input_hashes.json').write_text(json.dumps(hashes,indent=2))
print('Glossary',len(G),'definitions',sum(len(e['definitions']) for e in G))
for ch in M['chapters']:print(ch['id'],ch['pages'],len(ch['paragraphs']),len(ch['answer_exercises']),ch['paragraphs'])
