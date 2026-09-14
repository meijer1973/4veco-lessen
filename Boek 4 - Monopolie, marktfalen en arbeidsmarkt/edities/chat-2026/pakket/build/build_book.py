#!/usr/bin/env python3
"""Assemble the delivered Book 4 PDFs without reflowing their teaching content.

Requirements: PyMuPDF, reportlab, Pillow. Fonts are resolved locally, never bundled.
Inputs and their SHA-256 values are recorded in QA/input_hashes.json.
Preserves all supplied Book 4 chapter PDFs; only navigation is edited.
Only navigation and page numbers are edited during PDF assembly.
"""
from __future__ import annotations
import argparse, io, json, re, hashlib, subprocess, os
from pathlib import Path
from copy import deepcopy
from collections import defaultdict
import fitz
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4

ROOT=Path(__file__).resolve().parents[1]
W,H=A4
LEFT=53.85827; RIGHT=544.25197; WIDTH=RIGHT-LEFT
INK='#183247'; BLUE='#17688f'; MUTED='#536777'; PALE='#f2f6f8'; RULE='#d5dfe5'
M=json.loads((ROOT/'manifest.json').read_text())
CH=M['chapters']
GLOSS=json.loads((ROOT/'book-matter/glossary.json').read_text())
FORMULAS=json.loads((ROOT/'book-matter/formulas.json').read_text())
FONT_PATHS={}

def find_font(style: str)->str:
    names={'Regular':'Lato-Regular.ttf','Bold':'Lato-Bold.ttf','Heavy':'Lato-Heavy.ttf','Black':'Lato-Black.ttf','Italic':'Lato-Italic.ttf'}
    directories = [Path('/usr/share/fonts/truetype/lato')]
    if os.environ.get('LATO_FONT_DIR'):
        directories.insert(0, Path(os.environ['LATO_FONT_DIR']))
    if os.environ.get('WINDIR'):
        directories.append(Path(os.environ['WINDIR'])/'Fonts')
    if os.environ.get('LOCALAPPDATA'):
        directories.append(Path(os.environ['LOCALAPPDATA'])/'Microsoft/Windows/Fonts')
    directories += [Path.home()/'Library/Fonts',Path('/Library/Fonts')]
    for directory in directories:
        expected=directory/names[style]
        if expected.exists(): return str(expected)
    try:
        query='Lato' if style=='Regular' else 'Lato:style='+style
        path=subprocess.check_output(['fc-match','-f','%{file}',query],text=True).strip()
        if Path(path).exists(): return path
    except (OSError,subprocess.CalledProcessError): pass
    raise RuntimeError('Install the Lato family locally; no font files are distributed in this package.')

for style in ['Regular','Bold','Heavy','Black','Italic']:
    path=find_font(style); FONT_PATHS[style]=path
    pdfmetrics.registerFont(TTFont('Lato'+style,path))
pdfmetrics.registerFontFamily('LatoRegular',normal='LatoRegular',bold='LatoBold',italic='LatoItalic',boldItalic='LatoBold')
ST={
 'body':ParagraphStyle('body',fontName='LatoRegular',fontSize=11.3,leading=15.4,textColor=colors.HexColor(INK),spaceAfter=8),
 'small':ParagraphStyle('small',fontName='LatoRegular',fontSize=9.4,leading=12.5,textColor=colors.HexColor(MUTED),spaceAfter=6),
 'lead':ParagraphStyle('lead',fontName='LatoRegular',fontSize=14,leading=19,textColor=colors.HexColor(BLUE),spaceAfter=12),
 'h2':ParagraphStyle('h2',fontName='LatoBold',fontSize=14,leading=18,textColor=colors.HexColor(BLUE),spaceAfter=7),
 'formula':ParagraphStyle('formula',fontName='LatoRegular',fontSize=11.7,leading=18,textColor=colors.HexColor(INK),spaceAfter=4),
 'table':ParagraphStyle('table',fontName='LatoRegular',fontSize=10.2,leading=13.6,textColor=colors.HexColor(INK)),
 'toc':ParagraphStyle('toc',fontName='LatoRegular',fontSize=10.65,leading=14,textColor=colors.HexColor(INK)),
 'gloss':ParagraphStyle('gloss',fontName='LatoRegular',fontSize=10.8,leading=14.3,textColor=colors.HexColor(INK)),
}

def escape(t):
    return str(t).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

def page_offsets(kind):
    n=4 if kind=='student' else 2
    offsets=[]; blanks=[]
    for ch in CH:
        if n%2: blanks.append(n); n+=1
        offsets.append(n)
        with fitz.open(ROOT/ch[kind]) as d:n+=len(d)
    return offsets,n,blanks

OFF,S_END,_=page_offsets('student')
AOFF,A_END,A_BLANK=page_offsets('answers')
TOFF,T_END,T_BLANK=page_offsets('teacher')

def bp(ch:int,page:int)->int:return OFF[ch-1]+page

class Matter:
    """Fixed-page front matter and source-derived back matter, with measured flow."""
    def __init__(self,path,first_number=1,kind='student'):
        self.path=path;self.kind=kind;self.first=first_number;self.n=0;self.links=[];self.pages=[]
        self.c=canvas.Canvas(str(path),pagesize=A4,pageCompression=1)
        self.c.setTitle('Boek 4 — '+M['book']['title'])
        self.active=False;self.y=0
    def footer(self,number):
        c=self.c;c.setFillColor(colors.HexColor(MUTED));c.setFont('LatoRegular',8)
        c.drawString(LEFT,21,'Economie · 4 vwo')
        c.setFillColor(colors.HexColor(INK));c.setFont('LatoRegular',9)
        c.drawRightString(RIGHT,20.7,str(number))
    def new(self,title='',kicker='BOEK 4 · ECONOMIE · 4 VWO',footer=True):
        if self.active:self.c.showPage()
        self.active=True;self.n+=1;self.y=H-53
        number=self.first+self.n-1
        self.pages.append({'local_page':self.n,'book_page':number,'title':title})
        if footer:self.footer(number)
        if kicker:
            self.c.setFillColor(colors.HexColor(BLUE));self.c.setFont('LatoBold',9)
            self.c.drawString(LEFT,self.y,kicker);self.y-=32
        if title:
            self.c.setFillColor(colors.HexColor(INK));self.c.setFont('LatoHeavy',27)
            self.c.drawString(LEFT,self.y,title);self.y-=22
    def p(self,text,style='body',gap=5,indent=0,width=None):
        width=width or WIDTH-indent
        para=Paragraph(text,ST[style]);_,h=para.wrap(width,H)
        if self.y-h<52:raise RuntimeError(f'Overflow on matter page {self.n}: {text[:70]}')
        para.drawOn(self.c,LEFT+indent,self.y-h);self.y-=h+gap
        return h
    def heading(self,text):self.y-=8;self.p(escape(text),'h2',4)
    def box(self,title,body,note=None):
        pars=[Paragraph('<b>'+escape(title)+'</b>',ST['table']),Paragraph(body,ST['formula'])]
        if note:pars.append(Paragraph(note,ST['small']))
        table=Table([[p] for p in pars],colWidths=[WIDTH])
        table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),colors.HexColor(PALE)),('LINEBEFORE',(0,0),(0,-1),2.5,colors.HexColor(BLUE)),('LEFTPADDING',(0,0),(-1,-1),11),('RIGHTPADDING',(0,0),(-1,-1),11),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),4)]))
        _,h=table.wrap(WIDTH,H)
        if self.y-h<52:raise RuntimeError('Box overflow '+title)
        table.drawOn(self.c,LEFT,self.y-h);self.y-=h+10
    def table(self,head,rows,widths):
        data=[[Paragraph('<b>'+escape(x)+'</b>',ST['table']) for x in head]]
        data += [[Paragraph(str(x),ST['table']) for x in r] for r in rows]
        t=Table(data,colWidths=widths)
        t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor(PALE)),('LINEBELOW',(0,0),(-1,0),.8,colors.HexColor(MUTED)),('LINEBELOW',(0,1),(-1,-1),.45,colors.HexColor(RULE)),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7)]))
        _,h=t.wrap(WIDTH,H)
        if self.y-h<50:raise RuntimeError('Table overflow')
        t.drawOn(self.c,LEFT,self.y-h);self.y-=h+12
    def tocrow(self,text,page,level=0,extra=None):
        if level==0:
            self.y-=9
            self.c.setFillColor(colors.HexColor(PALE));self.c.rect(LEFT,self.y-24,WIDTH,29,fill=1,stroke=0)
            style=ParagraphStyle('ct',parent=ST['toc'],fontName='LatoBold',fontSize=12.2,leading=15,textColor=colors.HexColor(BLUE))
            pad=8
        else:style=ST['toc'];pad=10
        pp=Paragraph(escape(text),style);_,h=pp.wrap(WIDTH-pad-46,H)
        pp.drawOn(self.c,LEFT+pad,self.y-h)
        self.c.setFont('LatoBold' if level==0 else 'LatoRegular',10.65);self.c.setFillColor(colors.HexColor(INK))
        self.c.drawRightString(RIGHT-6,self.y-10.65,str(page))
        self.links.append({'page':self.n-1,'rect':[LEFT,H-self.y-3,RIGHT,H-self.y+h+4],'target':page-1})
        self.y-=max(h+7,28 if level==0 else 21)
        if extra:self.p(extra,'small',2,indent=pad)
        if self.y<47:raise RuntimeError('TOC overflow')
    def save(self):self.c.save();return self

def make_student_front(path,gloss_start,formula_start):
    b=Matter(path)
    b.new(kicker='',footer=False)
    img=Image.open(ROOT/M['cover']);iw,ih=img.size;scale=min(W/iw,H/ih);dw,dh=iw*scale,ih*scale
    b.c.setFillColor(colors.HexColor('#edf5f9'));b.c.rect(0,0,W,H,fill=1,stroke=0)
    b.c.drawImage(str(ROOT/M['cover']),(W-dw)/2,(H-dh)/2,width=dw,height=dh)
    b.new('Colofon')
    b.p('Monopolie, marktfalen en arbeidsmarkt','lead',14)
    b.table(['Uitgave','Gegevens'],[
        ['Reeks','4veco · Economie'],['Boek en doelgroep','Boek 4 · 4 vwo'],
        ['Editie','Samengestelde editie · 2026'],
        ['Opbouw','Drie hoofdstukken, zeventien paragrafen'],
        ['Leerlinghoofdstukken','38 + 60 + 50 pagina’s; de oorspronkelijke hoofdstukindeling is behouden.'],
        ['Aanvullende delen','Een afzonderlijk antwoordboek en een afzonderlijke docentenhandleiding.'],
        ['Omslag','De laatst gekozen omslagafbeelding met het middenpaneel Prijsdiscriminatie. Ongewijzigd en zonder afsnijden opgenomen.']
    ],[128,WIDTH-128])
    b.heading('Over deze bundeling')
    b.p('De drie hoofdstukken zijn als bestaande pagina’s samengevoegd. De uitleg, oefeningen, tabellen, grafieken en opgavennummers zijn behouden. Paginanummers, inhoudsopgaven en plaatselijke paginaverwijzingen zijn aangepast aan de doorlopende boekpaginering.')
    b.p('Achterin staan een gezamenlijke begrippenlijst en een formule- en aanpakoverzicht, ontleend aan de hoofdstukken. De begrippenlijst behoudt ook de verschillende hoofdstukgebonden formuleringen wanneer een begrip op meer plaatsen wordt uitgelegd.','small')
    b.heading('Gebruik van bronnen en beelden')
    b.p('De ondernemingen, markten, regio’s en bedragen in de opgaven zijn geconstrueerde lesvoorbeelden. De modelvoorwaarden staan bij de uitleg en bronnen. Illustratieve lonen zijn geen actuele wettelijke tarieven.','small')
    b.p('De omslag is een illustratie, geen rekenbron. Gebruik voor berekeningen, notatie en grafische redeneringen de uitgewerkte figuren en tabellen in de hoofdstukken.','small')
    b.new('Voorwoord')
    b.p('Van de keuze van één onderneming<br/>naar gevolgen voor de samenleving','lead',14)
    b.p('Een aanbieder verhoogt zijn prijs. Een fabriek veroorzaakt overlast voor omwonenden. Werkgevers zoeken personeel, terwijl sommige mensen geen baan vinden. In dit boek onderzoek je welke keuzes partijen maken en wie daarvan de gevolgen ondervindt.')
    b.p('In <b>hoofdstuk 1</b> bereken je de afzet, prijs en winst van een monopolist. <b>Hoofdstuk 2</b> richt zich op surplus, verdeling, externe effecten en beleidskeuzes. In <b>hoofdstuk 3</b> pas je vertrouwde marktmethoden toe op loon, werkgelegenheid en arbeidsmarktbeleid.')
    b.heading('Zo gebruik je dit boek')
    b.p('Lees de uitleg en bestudeer het uitgewerkte voorbeeld. Met de startopgaven haal je voorkennis op en controleer je het eerste begrip. De begeleide inoefening biedt extra steun. Daarna oefen je zelfstandig en pas je de methode toe in de doeloefening.')
    b.box('De kernroute','Startopgaven → Zelfstandige oefening → Doeloefening',
          'Extra hulp nodig? Maak eerst Begeleide inoefening. De docent bepaalt welke bonus- en herhalingsopgaven je daarnaast maakt.')
    b.p('Elk hoofdstuk eindigt met gemengde opgaven. Daar kies je zelf de passende methode. Schrijf de formule, de ingevulde waarden, de uitkomst en de eenheid op. Onderbouw een conclusie met de bron en lees welke modelvoorwaarden gelden.')
    b.p('De antwoorden staan in een afzonderlijk antwoordboek. Zoek met het hoofdstuknummer én het opgavenummer: de nummering begint in elk hoofdstuk opnieuw. De inhoudsopgave en de naslag achterin helpen je de uitleg terug te vinden.')
    b.new('Inhoud')
    b.p('Alle paginanummers verwijzen naar dit leerlingboek.','small',1)
    for i,ch in enumerate(CH):
        b.tocrow(ch['id']+'  '+ch['title'],OFF[i]+1)
        for para in ch['paragraphs']:b.tocrow(para['title'],OFF[i]+para['local_page'],1)
        overview=ch['pages']-1
        b.tocrow('Hoofdstukoverzicht en begrippen',OFF[i]+overview,1)
    b.tocrow('Begrippenlijst',gloss_start)
    b.tocrow('Formule- en aanpakoverzicht',formula_start)
    return b.save()

def make_back(path):
    b=Matter(path,first_number=S_END+1)
    for i,e in enumerate(GLOSS):
        label=Paragraph('<b>'+escape(e['term'])+'</b>',ST['gloss'])
        lh=label.wrap(WIDTH-62,H)[1]
        pieces=[]
        for d in e['definitions']:
            prefix=('<b>4.'+str(d['chapter'])+':</b> ') if len(e['definitions'])>1 else ''
            pp=Paragraph(prefix+escape(d['text']),ST['gloss']);ph=pp.wrap(WIDTH-62,H)[1]
            pieces.append((pp,ph,d))
        needed=lh+3+sum(h+4 for _,h,_ in pieces)+12
        if i==0 or b.y-needed<60:
            b.new('Begrippenlijst' if i==0 else 'Begrippenlijst · vervolg',kicker='BOEK 4 · NASLAG')
            b.p('Formuleringen uit de hoofdstukken. De paginaverwijzing leidt naar de oorspronkelijke begrippenlijst.','small',10)
        y0=b.y;label.drawOn(b.c,LEFT,b.y-lh);b.y-=lh+3
        for pp,ph,d in pieces:
            yy=b.y;pp.drawOn(b.c,LEFT,b.y-ph);b.y-=ph+4
            pn=bp(d['chapter'],d['local_page'])
            b.c.setFillColor(colors.HexColor(BLUE));b.c.setFont('LatoBold',10)
            b.c.drawRightString(RIGHT,yy-10,str(pn))
            b.links.append({'page':b.n-1,'rect':[LEFT,H-yy-2,RIGHT,H-b.y+2],'target':pn-1})
        b.y-=8;b.c.setStrokeColor(colors.HexColor(RULE));b.c.setLineWidth(.4);b.c.line(LEFT,b.y+3,RIGHT,b.y+3)
    gp=b.n;fs=S_END+gp+1
    for f in FORMULAS:
        b.new(f['title'],kicker='BOEK 4 · FORMULE- EN AANPAKOVERZICHT · '+f['chapter'])
        b.p(f['intro'],'body',10)
        for box in f['boxes']:b.box(box['title'],box['formula'],box.get('note'))
        pn=bp(f['source_chapter'],f['source_page'])
        b.p('Gebaseerd op '+f['source']+' en de bijbehorende uitleg. Zie ook p. '+str(pn)+'.','small')
        b.links.append({'page':b.n-1,'rect':[LEFT,H-b.y-24,RIGHT,H-b.y+4],'target':pn-1})
    return b.save(),gp,fs

def make_answer_front(path):
    b=Matter(path,kind='answers')
    b.new('Antwoorden',kicker='4VECO · BOEK 4 · GEZAMENLIJK ANTWOORDBOEK')
    b.p('Monopolie, marktfalen en arbeidsmarkt','lead',16)
    b.p('Dit antwoordboek bundelt de uitwerkingen bij de drie leerlinghoofdstukken. De oorspronkelijke volgorde, opgavennummers, berekeningen, toelichtingen en oplossingsfiguren zijn behouden.')
    b.table(['Hoofdstuk','Opgaven','Aantal'],[[c['id']+' '+c['title'],f'1–{len(c["answer_exercises"])}',str(len(c['answer_exercises']))] for c in CH],[280,100,WIDTH-380])
    b.heading('Eerst een eigen poging')
    b.p('Vergelijk niet alleen het eindgetal. Controleer de gebruikte gegevens, de gekozen methode, de eenheden en de betekenis van je antwoord. Gebruik bij grafiekvragen ook de oplossingsfiguur.')
    b.box('Zo vind je de uitwerking','Hoofdstuknummer + opgavenummer',
          'De nummering begint per hoofdstuk opnieuw. Opgave 7 in hoofdstuk 4.1 is dus een andere opgave dan opgave 7 in hoofdstuk 4.2. In de PDF heeft iedere opgave een eigen bladwijzer.')
    b.p('Bij uitlegvragen kan een andere formulering ook juist zijn wanneer zij door de bron wordt gedragen. De hoofdstukken lichten hun eigen afrondingsafspraken en beoordelingscriteria toe.','body')
    b.p('De paginanummers in dit antwoordboek lopen door en staan los van de paginanummers in het leerlingboek.','small')
    b.new('Inhoud',kicker='BOEK 4 · ANTWOORDEN')
    b.p('Gebruik de bladwijzers om direct naar een opgave te gaan.','small',1)
    for i,ch in enumerate(CH):
        b.tocrow(ch['id']+'  '+ch['title'],AOFF[i]+1)
        for k,para in enumerate(ch['paragraphs']):
            a=para['local_page'];z=ch['paragraphs'][k+1]['local_page'] if k+1<len(ch['paragraphs']) else ch['pages']-1
            ex=[n for n,pn in ch['student_exercises'].items() if a<=pn<z]
            assert ex,(ch['id'],para)
            first=min(ex,key=lambda s:int(s));last=max(ex,key=lambda s:int(s))
            title=para['title']
            # Explicit exercise ranges placed below keep paragraph names unambiguous.
            b.tocrow(title,AOFF[i]+ch['answer_exercises'][first],1)
    return b.save()

def make_teacher_front(path):
    b=Matter(path,kind='teacher')
    b.new('Docenteninformatie',kicker='4VECO · BOEK 4 · GEZAMENLIJKE HANDLEIDING')
    b.p('Monopolie, marktfalen en arbeidsmarkt','lead',14)
    b.p('Deze bundel bevat de drie eerder vervaardigde hoofdstukhandleidingen. Leerdoelen, lesroutes, afbakeningen, bronverantwoording en oorspronkelijke kwaliteitsnotities blijven bij hun hoofdstuk staan.')
    for i,ch in enumerate(CH):b.tocrow(ch['id']+'  '+ch['title'],TOFF[i]+1)
    b.heading('Drie gescheiden uitgaven')
    b.table(['Uitgave','Inhoud'],[
        ['Leerlingboek','Omslag, colofon, voorwoord, volledige inhoud, de drie hoofdstukken, begrippenlijst en formule- en aanpakoverzicht.'],
        ['Antwoordboek','Alle uitwerkingen bij 148 opgaven. Eigen doorlopende paginanummers en opgavenbladwijzers.'],
        ['Docenteninformatie','De drie oorspronkelijke handleidingen plus deze assemblage- en pagineringsnotities.']
    ],[130,WIDTH-130])
    b.p('De hoofdstukken volgen de aangeleverde v2-outlines. Bij deze bundeling zijn geen nieuwe lesdoelen, opgaven of economische modellen toegevoegd. De leerstofpagina’s blijven 38, 60 en 50 pagina’s lang.','small')
    b.p('De controle bij bundeling betreft volledigheid, paginering, verwijzingen, links en behoud van tekst en figuren. De oorspronkelijke inhoudelijke toets- en lestijdclaims zijn niet opnieuw gevalideerd. De repositories zijn niet gewijzigd.','small')
    b.new('Leeswijzer bij de bundeling',kicker='BOEK 4 · ASSEMBLAGENOTITIES')
    b.p('Paginaverwijzingen in de oorspronkelijke hoofdstukhandleidingen verwijzen naar de losse leerlinghoofdstukken. Gebruik de onderstaande omzetting voor het complete leerlingboek.','body',10)
    b.table(['Leerlinghoofdstuk','Boekpagina’s','Omzetting'],[[ch['id']+' '+ch['title'],f'{OFF[i]+1}–{OFF[i]+ch["pages"]}',f'Lokaal + {OFF[i]}'] for i,ch in enumerate(CH)],[245,105,WIDTH-350])
    b.heading('Bronnen en vragen blijven tegenover elkaar')
    b.table(['Gemengde doeloefening','Los hoofdstuk','Leerlingboek'],[[ch['id']+f' · Opgave {ch["mixed_target"]["nr"]}', '–'.join(str(p) for p in ch['mixed_target']['local_spread']), '–'.join(str(p+OFF[i]) for p in ch['mixed_target']['local_spread'])] for i,ch in enumerate(CH)],[220,115,WIDTH-335])
    b.heading('Geregistreerde assemblagewijzigingen')
    b.p('Alle hoofdstukpagina’s zijn behouden. Alleen paginanummers, klikbestemmingen, de hoofdstukinhoudsopgaven en twee tekstregels met expliciete leerlingpaginaverwijzingen zijn bijgewerkt. De nieuwe naslag hergebruikt de definities en rekenroutes uit de hoofdstukken.','small')
    b.heading('Let op bij de gekozen omslag')
    b.p('De laatst gekozen afbeelding is ongewijzigd opgenomen. De miniatuurgrafieken zijn geen betrouwbare instructiebron. Links staat de markering bij het snijpunt van vraag en MK in plaats van de hoeveelheid uit MO = MK. Het middenpaneel laat gekozen prijzen zien zonder de segmentoptimalisatie te onderbouwen. Gebruik de correcte rekenroute en oplossingsgrafieken uit de hoofdstukken; de omslag is geen vervanging daarvan.','small')
    b.p('Er zijn geen nieuwe school-, uitgever-, contact- of licentiegegevens verzonnen. De meegeleverde bronbestanden en oorspronkelijke hoofdstukverantwoording blijven de herkomst vastleggen.','small')
    return b.save()

FZ_FONTS={s:fitz.Font(fontfile=p) for s,p in FONT_PATHS.items()}
def fontstyle(name):
    n=name.lower()
    if 'italic' in n:return 'Italic'
    if 'ultra' in n or 'black' in n:return 'Black'
    if 'heavy' in n:return 'Heavy'
    if 'bold' in n:return 'Bold'
    return 'Regular'

def rgb(num):return (((num>>16)&255)/255,((num>>8)&255)/255,(num&255)/255)

def line_records(p):
    return [l for b in p.get_text('dict')['blocks'] for l in b.get('lines',[]) if l['spans']]

def rewrite_line(p,line,new_spans,ops,label):
    r=fitz.Rect(line['bbox']);r.x0-=.08;r.x1+=.08;r.y0+=.12;r.y1-=.12
    if label != 'continuous_page_number':
        p.add_redact_annot(r,fill=False,cross_out=False)
    old=''.join(s['text'] for s in line['spans']);new=''.join(new_spans)
    ops.append({'rect':list(r),'line':line,'new_spans':new_spans,'reason':label,'old':old,'new':new})

def replace_page_refs(line,offset):
    spans=line['spans']; texts=[s['text'] for s in spans]
    full=''.join(texts)
    pattern=r'\bpagina(?:’s|\x27s)?\s+(\d+)(?:[–−-](\d+))?'
    replacements=[]
    for m in re.finditer(pattern,full,re.I):
        for g in [1,2]:
            if m.group(g):replacements.append((m.start(g),m.end(g),str(int(m.group(g))+offset)))
    if not replacements:return None
    # Assign each match to its original span (numeric references in these inputs do not span runs).
    starts=[];n=0
    for t in texts:starts.append(n);n+=len(t)
    for a,z,v in reversed(replacements):
        for k,start in reversed(list(enumerate(starts))):
            if start<=a and z<=start+len(texts[k]):
                texts[k]=texts[k][:a-start]+v+texts[k][z-start:];break
        else:raise RuntimeError('A page reference crosses font runs; needs explicit handling.')
    return texts

def execute_ops(page,ops):
    if not ops:return
    if any(op['reason'] != 'continuous_page_number' for op in ops):
        page.apply_redactions(images=0,graphics=0,text=0)
    for op in ops:
        if op.get('right_aligned'):
            sp=op['line']['spans'][0];font=FZ_FONTS[fontstyle(sp['font'])];text=op['new'];size=sp['size']
            tw=fitz.TextWriter(page.rect);x=op['line']['bbox'][2]-font.text_length(text,fontsize=size)
            tw.append((x,sp['origin'][1]),text,font=font,fontsize=size)
            op['output_rect'] = list(fitz.Rect(op['rect']) | fitz.Rect(x,sp['origin'][1]-font.ascender*size,op['line']['bbox'][2],sp['origin'][1]-font.descender*size))
            tw.write_text(page,color=rgb(sp['color']))
        else:
            spans=op['line']['spans'];x=spans[0]['origin'][0];x0=x
            fragments=[]
            for sp,text in zip(spans,op['new_spans']):
                font=FZ_FONTS[fontstyle(sp['font'])];size=sp['size']
                fragments.append((x,sp['origin'][1],text,font,size,sp['color']))
                x+=font.text_length(text,fontsize=size)
            width=x-x0;oldwidth=op['line']['bbox'][2]-x0
            # Preserve the existing line box; avoid reflow into a neighbour or a graph.
            scale=min(1.0,oldwidth/width) if width else 1
            if scale<.94:raise RuntimeError(f'Excessive line scaling {scale:.3f}: {op["old"]}')
            base=fitz.Point(x0,spans[0]['origin'][1])
            for x,y,text,font,size,color in fragments:
                tw=fitz.TextWriter(page.rect);tw.append((x,y),text,font=font,fontsize=size)
                tw.write_text(page,color=rgb(color),morph=(base,fitz.Matrix(scale,1)))
            op['horizontal_scale']=scale


def remove_footer_text_object(page,ops):
    """Drop only the original number's BT/ET block; do not reserialize other text.

    Delivered WeasyPrint inputs use a .75 CSS-pixel to point transformation.
    Assert the exact position match and one-only removal, instead of assuming a
    footer is the last text on every page. Avoids rounding letter spacing in
    untouched headings during a whole-stream redaction pass.
    """
    foot=[op for op in ops if op['reason']=='continuous_page_number']
    if not foot: return
    if len(foot)!=1: raise RuntimeError('Expected one footer number')
    sx,sy=foot[0]['line']['spans'][0]['origin']
    count=0
    for xref in page.get_contents():
        old=page.parent.xref_stream(xref)
        def sub(m):
            nonlocal count
            matrices=re.findall(rb'1 0 0 -1 ([\d.+-]+) ([\d.+-]+) Tm',m[0])
            if len(matrices)==1 and abs(float(matrices[0][0])*.75-sx)<.05 and abs(float(matrices[0][1])*.75-sy)<.05:
                count+=1;return b''
            return m[0]
        new=re.sub(rb'\bBT\b(?:(?!\bET\b).)*\bET\b',sub,old,flags=re.S)
        if new!=old:page.parent.update_stream(xref,b"q\n"+new+b"\nQ\n")
    if count!=1:raise RuntimeError(f'Footer block matching failed: {page.number}, {count}')

def prepare_source(ch,kind,offset):
    doc=fitz.open(ROOT/ch[kind]);record=[];alllinks=[]
    for i,page in enumerate(doc):
        originals=page.get_links()
        # Recreate named targets as unambiguous numerical destinations after assembly.
        for l in originals:
            if l.get('page',-1)>=0:
                alllinks.append({'page':offset+i,'rect':list(l['from']),'target':offset+l['page']})
            if l.get('xref',0):page.delete_link(l)
        ops=[]
        lines=line_records(page)
        for line in lines:
            full=''.join(s['text'] for s in line['spans'])
            if re.fullmatch(r'\d+',full.strip()) and line['bbox'][1]>800 and line['bbox'][0]>500:
                rewrite_line(page,line,[str(offset+i+1)],ops,'continuous_page_number');ops[-1]['right_aligned']=True
            elif kind=='student' and i==0 and re.fullmatch(r'\d+',full.strip()) and line['bbox'][0]>510 and line['bbox'][1]<790:
                rewrite_line(page,line,[str(int(full)+offset)],ops,'chapter_contents_page');ops[-1]['right_aligned']=True
            elif kind=='student':
                refs=replace_page_refs(line,offset)
                if refs:rewrite_line(page,line,refs,ops,'inline_page_reference')
        remove_footer_text_object(page,ops)
        execute_ops(page,ops)
        record.append({'source':ch[kind],'local_page':i+1,'book_page':offset+i+1,'edits':[{k:v for k,v in op.items() if k not in ['line','new_spans']} for op in ops]})
    return doc,record,alllinks


def add_links(doc,links):
    seen=set()
    for l in links:
        key=(l['page'],tuple(round(x,2) for x in l['rect']),l['target'])
        if key in seen:continue
        seen.add(key)
        if not 0<=l['target']<len(doc):raise RuntimeError('Invalid destination '+str(l))
        doc[l['page']].insert_link({'kind':fitz.LINK_GOTO,'from':fitz.Rect(l['rect']),'page':l['target'],'to':fitz.Point(0,0),'zoom':0})



def build(kind,front,back=None,glossary_pages=0):
    offsets,end,blanks=page_offsets(kind)
    result=fitz.open();result.insert_pdf(fitz.open(front.path),links=False)
    links=deepcopy(front.links);audit=[];allblanks=[]
    if kind=='student':outlines=[[1,'Omslag',1],[1,'Colofon',2],[1,'Voorwoord',3],[1,'Inhoud',4]]
    else:outlines=[[1,'Leeswijzer',1],[1,'Inhoud' if kind=='answers' else 'Leeswijzer bij de bundeling',2]]
    for n,ch in enumerate(CH):
        while len(result)<offsets[n]:result.new_page(width=W,height=H);allblanks.append(len(result))
        src,records,sl=prepare_source(ch,kind,offsets[n]);result.insert_pdf(src,links=False)
        audit.extend(records);links.extend(sl);outlines.append([1,ch['id']+' '+ch['title'],offsets[n]+1])
        if kind=='student':
            for para in ch['paragraphs']:outlines.append([2,para['title'],offsets[n]+para['local_page']])
            outlines.append([2,'Hoofdstukoverzicht',offsets[n]+ch['pages']-1])
            outlines.append([2,'Begrippenlijst hoofdstuk '+ch['id'],offsets[n]+ch['pages']])
        elif kind=='answers':
            for ex,pn in ch['answer_exercises'].items():outlines.append([2,'Opgave '+ex,offsets[n]+pn])
        else:
            orig=fitz.open(ROOT/ch[kind])
            for level,title,pn in orig.get_toc():
                if pn>1 and level==1:outlines.append([2,title,offsets[n]+pn])
        src.close()
    if back:
        assert len(result)==S_END
        result.insert_pdf(fitz.open(back.path),links=False)
        links.extend([{**l,'page':l['page']+S_END} for l in back.links])
        outlines.append([1,'Begrippenlijst',S_END+1])
        outlines.append([1,'Formule- en aanpakoverzicht',S_END+glossary_pages+1])
        for i,f in enumerate(FORMULAS):outlines.append([2,f['title'],S_END+glossary_pages+i+1])
    if len(result)%2:result.new_page(width=W,height=H);allblanks.append(len(result))
    add_links(result,links);result.set_toc(outlines)
    result.set_metadata({'title':('Boek 4 — ' if kind=='student' else 'Boek 4 — '+ {'answers':'Antwoorden — ','teacher':'Docenteninformatie — '}[kind])+M['book']['title'],'subject':'Samengestelde editie · 4 vwo · Monopolie · Marktvormen en marktfalen · Arbeidsmarkt','author':'','keywords':'4veco, economie, 4 vwo, Boek 4','creator':'4veco · assembly from supplied chapters','producer':'PyMuPDF + ReportLab'})
    result.set_page_labels([{'startpage':0,'prefix':'','style':'D','firstpagenum':1}])
    result.xref_set_key(result.pdf_catalog(),'PageLayout','/TwoPageRight')
    result.xref_set_key(result.pdf_catalog(),'Lang','(nl-NL)')
    result.xref_set_key(result.pdf_catalog(),'PageMode','/UseOutlines')
    result.subset_fonts()
    suffix={'student':'','answers':'_Antwoorden','teacher':'_Docenteninformatie'}[kind]
    output=ROOT/'output'/f'Boek_4_Compleet{suffix}.pdf'
    result.save(output,garbage=4,deflate=True)
    (ROOT/f'qa/{kind}_page_map.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2))
    summary={'file':str(output.relative_to(ROOT)),'pages':len(result),'source_pages':sum(len(fitz.open(ROOT/ch[kind])) for ch in CH),'chapter_starts':[o+1 for o in offsets],'intentional_blank_pages':allblanks,'internal_links':sum(len(p.get_links()) for p in result),'bookmarks':len(outlines),'recorded_edits':sum(len(a['edits']) for a in audit)}
    result.close();return summary

def main():
    for f,h in json.loads((ROOT/'qa/input_hashes.json').read_text()).items():
        if hashlib.sha256((ROOT/f).read_bytes()).hexdigest()!=h:raise RuntimeError('Input changed: '+f)
    tmp=ROOT/'build/_intermediate';tmp.mkdir(exist_ok=True)
    back,gp,fs=make_back(tmp/'back.pdf')
    front=make_student_front(tmp/'front.pdf',S_END+1,fs)
    assert front.n==4
    a=make_answer_front(tmp/'answers_front.pdf');t=make_teacher_front(tmp/'teacher_front.pdf')
    summaries=[build('student',front,back,gp),build('answers',a),build('teacher',t)]
    manifest={'outputs':summaries,'glossary_entries':len(GLOSS),'glossary_source_definitions':sum(len(g['definitions']) for g in GLOSS),'glossary_pages':gp,'formula_pages':len(FORMULAS),'book_chapter_pages':sum(ch['pages'] for ch in CH),'instructional_paragraphs':sum(len(c['paragraphs']) for c in CH),'exercise_total':sum(len(c['answer_exercises']) for c in CH),'formula_start':fs,'source_spreads_in_book':[[p+OFF[i] for p in ch['mixed_target']['local_spread']] for i,ch in enumerate(CH)],'book_guidance':'skills/econ-book-builder.md: cover, colophon, preface, full contents, chapters, glossary, formula overview; answers kept separate','guidance_adaptations':'PDF-preserving stitch rather than reflow; supplied latest cover unchanged; separate answer PDFs remain paper-first; no unsupported license, school, publisher or contact asserted. All 62 source glossary definitions retained under 58 alphabetic terms.'}
    (ROOT/'qa/assembly_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
    (ROOT/'book-matter/page_map.json').write_text(json.dumps({'front':front.pages,'back':back.pages,'answers':a.pages,'teacher':t.pages},ensure_ascii=False,indent=2))
    print(json.dumps(manifest,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
