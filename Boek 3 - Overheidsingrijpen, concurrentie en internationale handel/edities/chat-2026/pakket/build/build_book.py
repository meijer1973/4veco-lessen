#!/usr/bin/env python3
"""Assemble the delivered Book 3 PDFs without reflowing their teaching content.

Requirements: PyMuPDF, reportlab, Pillow. Fonts are resolved locally, never bundled.
Inputs and their SHA-256 values are recorded in QA/input_hashes.json.
Assembles the revised Chapter 3.1 and unchanged Chapters 3.2 and 3.3.
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
        self.c.setTitle('Boek 3 — '+M['book']['title'])
        self.active=False;self.y=0
    def footer(self,number):
        c=self.c;c.setFillColor(colors.HexColor(MUTED));c.setFont('LatoRegular',8)
        c.drawString(LEFT,21,'Economie · 4 vwo')
        c.setFillColor(colors.HexColor(INK));c.setFont('LatoRegular',9)
        c.drawRightString(RIGHT,20.7,str(number))
    def new(self,title='',kicker='BOEK 3 · ECONOMIE · 4 VWO',footer=True):
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
        self.y-=max(h+9,28 if level==0 else 23)
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
    b.p('Overheidsingrijpen, volkomen concurrentie<br/>en internationale handel','lead',14)
    b.table(['Uitgave','Gegevens'],[
       ['Reeks','4veco · Economie'],['Boek en doelgroep','Boek 3 · 4 vwo'],['Editie','Herziene samengestelde editie 2026'],
       ['Opbouw','Drie hoofdstukken, veertien paragrafen'],['Leerlinghoofdstukken','48 + 38 + 38 pagina’s; hoofdstuk 3.1 uitgebreid met 8 pagina’s'],
       ['Aanvullende delen','Een afzonderlijk antwoordboek en een afzonderlijke docentenhandleiding'],
       ['Omslag','De eerder gemaakte omslagafbeelding is ongewijzigd en zonder afsnijden opgenomen.'],
    ],[128,WIDTH-128])
    b.heading('Over deze bundeling')
    b.p('Hoofdstuk 3.1 is gericht herzien en uitgebreid. Hoofdstukken 3.2 en 3.3 zijn inhoudelijk behouden. De paginanummers, inhoudsopgaven en verwijzingen binnen het leerlingboek zijn aangepast aan de doorlopende boekpaginering. Paragraaf- en opgavenummers zijn behouden.')
    b.p('De kernbegrippen en het formuleoverzicht achterin zijn ontleend aan deze hoofdstukken. De uitgewerkte lesgrafieken en tabellen in de hoofdstukken zijn het uitgangspunt voor berekeningen en notatie; de omslag is een illustratie.','small')
    b.heading('Rekenmodellen en bronnen')
    b.p('Markten, ondernemingen, landen, bedragen en beleidsvoorstellen in de opgaven zijn fictieve oefensituaties. De modelvoorwaarden staan bij de uitleg en de bronnen. De vragen zijn geen officiële examenopgaven.','small')
    b.p('Herziening hoofdstuk 3.1: extra uitleg en begeleide oefening; opgaven 22A, 40A en 47A toegevoegd; bonus 17 vernieuwd. De zes doeloefeningen blijven behouden. De docentenhandleiding bevat de beoordeling en het wijzigingenoverzicht.','small')
    b.new('Voorwoord')
    b.p('Van overheidsbeleid naar de onderneming<br/>en de wereldmarkt','lead')
    b.p('Een overheid voert een belasting in. Een onderneming kiest hoeveel zij produceert. Een land koopt producten uit het buitenland. Steeds gaat het om dezelfde vragen: welke prijs geldt, welke hoeveelheid wordt verhandeld en wie merkt daarvan de gevolgen?')
    b.p('In <b>hoofdstuk 1</b> onderzoek je belastingen, subsidies, prijsgrenzen en quota. In <b>hoofdstuk 2</b> verbind je de marktprijs met de productie en winst van één onderneming. <b>Hoofdstuk 3</b> gebruikt bekende marktmodellen om internationale handel en bescherming te begrijpen.')
    b.heading('Zo gebruik je dit boek')
    b.p('Lees de uitleg en bestudeer het uitgewerkte voorbeeld. In de startopgaven haal je benodigde voorkennis op en controleer je het eerste begrip. De begeleide inoefening biedt extra steun. Die steun wordt afgebouwd, zodat je de zelfstandige oefening en de doeloefening kunt uitvoeren.')
    b.box('De kernroute','Startopgaven → Zelfstandige oefening → Doeloefening', 'Extra hulp nodig? Maak eerst Begeleide inoefening. Bonus en afsluitende herhaling zijn niet automatisch extra verplicht werk in dezelfde les.')
    b.p('Elk hoofdstuk eindigt met gemengde opgaven. Daar kies je zelf de passende aanpak. Noteer eenheden, lees de modelvoorwaarden en onderbouw een conclusie met de gegevens. Een getal alleen is niet altijd een volledig antwoord.')
    b.p('De antwoorden staan in het afzonderlijke antwoordboek. Zoek een uitwerking op met het hoofdstuknummer én het opgavenummer. Achterin dit leerlingboek vind je een gezamenlijke begrippenlijst en een formule- en aanpakoverzicht.','body')
    b.new('Inhoud')
    b.p('Alle paginanummers verwijzen naar dit leerlingboek.','small',2)
    for i,ch in enumerate(CH):
        b.tocrow(f"{ch['id']}  {ch['title']}",OFF[i]+1)
        for para in ch['paragraphs']:
            b.tocrow(para['title'].replace(' · ','  '),OFF[i]+para['local_page'],1)
        b.tocrow('Overzicht en begrippen',OFF[i]+ch['intro_entries'][-1]['local_page'],1)
    b.tocrow('Begrippenlijst',gloss_start)
    b.tocrow('Formule- en aanpakoverzicht',formula_start)
    return b.save()

def make_back(path):
    b=Matter(path,first_number=S_END+1)
    n=0
    # A measured alphabetic list, not a newly authored set of definitions.
    for i,e in enumerate(GLOSS):
        term=Paragraph('<b>'+escape(e['term'])+'</b>',ST['gloss'])
        text=Paragraph(escape(e['definition']),ST['gloss'])
        h1=term.wrap(WIDTH-75,H)[1];h2=text.wrap(WIDTH-75,H)[1]
        needed=h1+h2+14
        if i==0 or b.y-needed<63:
            b.new('Begrippenlijst' if i==0 else 'Begrippenlijst · vervolg',kicker='BOEK 3 · NASLAG')
            b.p('Kernbegrippen uit de hoofdstukken. Het paginanummer brengt je terug naar de uitleg.','small',12)
        y0=b.y
        term.drawOn(b.c,LEFT,b.y-h1);b.y-=h1+3
        text.drawOn(b.c,LEFT,b.y-h2);b.y-=h2+11
        pn=bp(e['chapter'],e['local_page'])
        b.c.setFillColor(colors.HexColor(BLUE));b.c.setFont('LatoBold',10.5);b.c.drawRightString(RIGHT,y0-11,str(pn))
        b.links.append({'page':b.n-1,'rect':[LEFT,H-y0-2,RIGHT,H-b.y],'target':pn-1})
        b.c.setStrokeColor(colors.HexColor(RULE));b.c.setLineWidth(.45);b.c.line(LEFT,b.y+4,RIGHT,b.y+4)
    glossary_pages=b.n
    formula_start=S_END+b.n+1
    b.new('Belastingen en subsidies',kicker='BOEK 3 · FORMULE- EN AANPAKOVERZICHT · 3.1')
    b.p('Pc is de kopersprijs; Pp is de verkopersontvangst vóór productiekosten. P₀ en Q₀ horen bij het vrije evenwicht. t en s zijn bedragen per verkocht product.','small',7)
    b.box('Belastingwig en belastingdruk · p. '+str(bp(1,2))+'–'+str(bp(1,11)),
          'Pc − Pp = t<br/>Last koper per stuk = Pc − P₀<br/>Last verkoper per stuk = P₀ − Pp<br/>Aandeel koper = (Pc − P₀) / t × 100%',
          'Wie de belasting afdraagt, draagt niet automatisch de hele economische last.')
    b.box('Belastingopbrengst · §3.1.2','O = t × Qt','Qt is de werkelijk verkochte hoeveelheid mét belasting, niet Q₀.')
    b.box('Subsidiewig en overheidsuitgaven · p. '+str(bp(1,19))+'–'+str(bp(1,20)),
          'Pp − Pc = s<br/>U = s × Qsub',
          'Qsub is de werkelijk verkochte hoeveelheid mét subsidie. In deze hoofdstukmodellen geldt de subsidie voor elke verkochte eenheid.')
    b.box('De welvaartsvergelijking in hoofdstuk 3.1',
          'Zonder maatregel: CS + PS<br/>Met belasting: CS + PS + O<br/>Met subsidie: CS + PS − U<br/>Welvaartsverlies = oude maat − nieuwe maat',
          'Deze vergelijking rekent zonder effecten voor buitenstaanders en zonder uitvoeringskosten. O is een overdracht; niet elke euro overheidsontvangst is welvaartsverlies.')
    b.p('Bij de rechte lijnen in de belastingvoorbeelden: W = ½ × (Q₀ − Qt) × t. In hoofdstuk 3.1 staat W voor welvaartsverlies.','small')
    b.new('Prijsgrenzen en quota',kicker='BOEK 3 · FORMULE- EN AANPAKOVERZICHT · 3.1')
    b.p('Bepaal eerst het vrije evenwicht. Controleer daarna of de maatregel bindt. Bereken pas dan de gevraagde, aangeboden en werkelijk verhandelde hoeveelheden.','body',12)
    b.box('Maximumprijs · p. '+str(bp(1,28))+'–'+str(bp(1,30)),
          'Bindend als Pmax lager is dan P₀<br/>Tekort = Qv − Qa<br/>Zonder extra aanvoer: verkopen = Qa',
          'De verkoopregel veronderstelt dat de aangeboden producten werkelijk worden verkocht. Een prijs boven P₀ als maximum laat het vrije evenwicht toe. Een lage prijs is geen aankoopgarantie.')
    b.box('Minimumprijs · p. '+str(bp(1,35))+'–'+str(bp(1,38)),
          'Bindend als Pmin hoger is dan P₀<br/>Aanbodoverschot = Qa − Qv<br/>Zonder opkoop: verkopen = Qv',
          'Een minimumprijs betekent niet vanzelf dat de overheid het overschot koopt.')
    b.box('Alleen bij volledige overheidsopkoop · §3.1.5',
          'Overheidsaankopen = Qa − Qv<br/>U = aankoopprijs × overheidsaankopen',
          'Controleer de aankoopregel en de aankoopprijs in de bron. Particuliere aankopen zijn dan niet hetzelfde als alle verkopen.')
    b.box('Productiequotum · §3.1.5',
          'Een quotum begrenst de hoeveelheid, niet rechtstreeks de prijs.',
          'Controleer of de toegestane productie lager is dan de vrije hoeveelheid. Bij volledige verkoop lees je de prijs bij de quotumhoeveelheid af op de vraaglijn. Budgetgevolgen volgen alleen uit de opgegeven regeling.')
    b.new('De concurrerende onderneming',kicker='BOEK 3 · FORMULE- EN AANPAKOVERZICHT · 3.2')
    b.p('Q hoort bij de hele markt; q bij één onderneming. De onderneming neemt de marktprijs over. De twee hoeveelheidsschalen zijn niet onderling uitwisselbaar.','body',12)
    b.box('Opbrengsten bij één vaste verkoopprijs · p. '+str(bp(2,4)),
          'TO = P × q<br/>GO = TO / q<br/>MO = ΔTO / Δq<br/>P = GO = MO',
          'GO is een bedrag per product; TO is een totaalbedrag per periode. Voor GO geldt q &gt; 0.')
    b.box('De beperkte afgeleidenregel · p. '+str(bp(2,12)),
          'TK = a × q² + b × q + c<br/>MK = 2a × q + b',
          'De afgeleide beschrijft één punt van het doorlopende model. ΔTK / Δq over een tabelstap is een intervalwaarde.')
    b.box('Productiekeuze en winst · p. '+str(bp(2,13))+'–'+str(bp(2,15)),
          'Vergelijk MO en MK; controleer de productiecapaciteit.<br/>GTK = TK / q<br/>Winst = TO − TK = (P − GTK) × q',
          'MO = MK alleen bewijst geen maximum. Controleer de richting van de marginale vergelijking en de haalbare grenzen. Lees GTK bij de gekozen q; voor GTK geldt q &gt; 0.')
    b.box('Langetermijnevenwicht · p. '+str(bp(2,25)),
          'P = GO = MO = MK = minimum GTK<br/>TO = TK → economische winst = 0',
          'Dit geldt onder de concurrentie-, kosten- en toetredingsaannames uit §3.2.3. De normale beloning zit al in TK. Nul economische winst is geen nulomzet of nulinkomen.')
    b.new('Handel en bescherming',kicker='BOEK 3 · FORMULE- EN AANPAKOVERZICHT · 3.3')
    b.p('Gebruik het model van een klein prijsnemend land met de genoemde handels- en kostenvoorwaarden. Maak onderscheid tussen binnenlandse productie, binnenlands verbruik en de handelsstroom.','body',12)
    b.box('Bij een gegeven wereldmarktprijs · p. '+str(bp(3,11))+'–'+str(bp(3,13)),
          'Binnenlandse productie = Qa<br/>Binnenlands verbruik = Qv<br/>Import = Qv − Qa, als Qv &gt; Qa<br/>Export = Qa − Qv, als Qa &gt; Qv',
          'Lees beide hoeveelheden bij dezelfde prijs. Productie is niet hetzelfde als verbruik.')
    b.box('Invoerheffing · p. '+str(bp(3,22))+'–'+str(bp(3,24)),
          'Zolang er import is:<br/>binnenlandse prijs = wereldmarktprijs + heffing<br/>Heffingsopbrengst = heffing × import na de heffing',
          'Bereken de opbrengst over de resterende import, niet over alle binnenlandse verkopen. Na het verdwijnen van import mag je niet mechanisch wereldprijs plus heffing opleggen.')
    b.box('Importquotum · §3.3.3',
          'Een maximum aan de invoer in een bepaalde periode.',
          'Een quotum beperkt de hoeveelheid. Het geeft niet automatisch dezelfde overheidsontvangsten als een invoerheffing; lees de regeling in de bron.')
    b.box('Een bronconclusie onderbouwen',
          'Gegeven → economisch mechanisme → gevolg voor de genoemde groep.',
          'Absoluut voordeel is niet hetzelfde als comparatief voordeel. Een voordeel voor producenten is geen bewijs dat iedereen wint. De afweging bij handel en bescherming blijft bron- en modelgebonden.')
    b.save()
    return b,glossary_pages,formula_start

def make_answer_front(path):
    b=Matter(path,kind='answers')
    b.new('Antwoorden',kicker='4VECO · BOEK 3 · DOCENT / ZELFCONTROLE')
    b.p('Overheidsingrijpen, volkomen concurrentie<br/>en internationale handel','lead',16)
    b.p('Dit afzonderlijke antwoordboek bundelt de uitwerkingen bij de drie hoofdstukken. De opgaven blijven genummerd per hoofdstuk. Gebruik daarom altijd beide nummers, bijvoorbeeld: hoofdstuk 3.2, opgave 17.')
    b.table(['Hoofdstuk','Opgaven','Start'],[[ch['id']+' '+ch['title'],str(len(ch['answer_exercises'])),str(AOFF[i]+1)] for i,ch in enumerate(CH)],[WIDTH-132,66,66])
    b.heading('Nakijken is vergelijken')
    b.p('Vergelijk de gekozen aanpak, de tussenstappen, de eenheden en de economische conclusie. Bij open vragen kunnen gelijkwaardige formuleringen juist zijn. De beoordelingscriteria bij de bonusopgaven laten zien wat een goed antwoord bevat.')
    b.p('De volledige uitleg en de uitgewerkte voorbeelden staan in het leerlingboek. De antwoorden zijn niet tussen de leerlingopgaven opgenomen.','body')
    b.box('Opgaven blijven herkenbaar','3.1: opgaven 1–48, aangevuld met 22A, 40A en 47A<br/>3.2: opgaven 1–38<br/>3.3: opgaven 1–38', 'Hoofdstuk 3.1 bevat de herziene uitwerkingen. De antwoorden bij 3.2 en 3.3 zijn behouden. De paginanummering loopt door; de digitale bladwijzers gaan rechtstreeks naar afzonderlijke opgaven.')
    b.new('Inhoud · antwoorden')
    b.p('Paginanummers in deze inhoudsopgave horen bij het antwoordboek.','small',1)
    for i,ch in enumerate(CH):
        b.tocrow(ch['id']+'  '+ch['title'],AOFF[i]+1)
        for para in ch['paragraphs']:
            text=para['title'].replace(' · ','  ')
            b.tocrow(text,AOFF[i]+para['answer_local_page'],1)
    b.p('De kleine opgavenummers beginnen in elk hoofdstuk opnieuw. De hoofdstuknummers maken de verwijzing uniek.','small')
    return b.save()

def make_teacher_front(path):
    b=Matter(path,kind='teacher')
    b.new('Docenteninformatie',kicker='4VECO · BOEK 3 · GEZAMENLIJKE HANDLEIDING')
    b.p('Overheidsingrijpen, volkomen concurrentie<br/>en internationale handel','lead',14)
    b.p('Deze bundel bevat de herziene handleiding van hoofdstuk 3.1 en de bestaande handleidingen van 3.2 en 3.3. Leerdoelen, lesplanningen, didactische grenzen en kwaliteitsnotities blijven bij hun oorspronkelijke hoofdstuk staan.')
    for i,ch in enumerate(CH):b.tocrow(ch['id']+'  '+ch['title'],TOFF[i]+1)
    b.heading('Drie gescheiden producten')
    b.table(['Uitgave','Doel'],[
        ['Leerlingboek','Omslag, voorwerk, alle drie de hoofdstukken, begrippenlijst en formule- en aanpakoverzicht.'],
        ['Antwoordboek','Uitwerkingen bij de bestaande opgaven; doorlopende paginering en opgavenbladwijzers.'],
        ['Docenteninformatie','De hoofdstukhandleidingen, met onderstaande leeswijzer voor de oorspronkelijke paginaverwijzingen.'],
    ],[128,WIDTH-128])
    b.p('De hoofdstukken volgen de door de opdrachtgever aangeleverde v2-outlines. De herziening van 3.1 biedt meer tussenstappen en optionele oefening, zonder nieuwe leerdoelen of doelopgaven. De lesplanning is aangepast; er volgen geen nieuwe examenclaims. De repositories zijn niet gewijzigd.','small')
    b.new('Leeswijzer bij de bundeling',kicker='BOEK 3 · ASSEMBLAGENOTITIES')
    b.p('De paginaverwijzingen in de oorspronkelijke hoofdstukhandleidingen blijven verwijzen naar de losse leerlinghoofdstukken. De tabel zet die om naar het complete leerlingboek.','body',10)
    b.table(['Leerlinghoofdstuk','Boekpagina’s','Oude verwijzing omzetten'],[[ch['id']+' '+ch['title'],f'{OFF[i]+1}–{OFF[i]+ch["pages"]}',f'Hoofdstukpagina + {OFF[i]}'] for i,ch in enumerate(CH)],[170,85,WIDTH-255])
    b.heading('Bron en vragen blijven tegenover elkaar')
    b.table(['Gemengde doeloefening','Los hoofdstuk','Leerlingboek'],[['3.1 · Opgave 48','46–47','50–51'],['3.2 · Opgave 36','34–35','86–87'],['3.3 · Opgave 35','34–35','124–125']],[220,100,WIDTH-320])
    b.heading('Geregistreerde wijzigingen')
    b.p('Hoofdstuk 3.1 telt 48 in plaats van 40 pagina’s. De herziene handleiding legt per wijziging de aanleiding uit. Alle zes doeloefeningen zijn behouden. Bij de bundeling zijn de paginanummers, inhoudsopgaven en verwijzingen aangepast. Hoofdstukken 3.2 en 3.3 zijn inhoudelijk ongewijzigd.','small')
    b.p('De omslag is ongewijzigd gebruikt op verzoek. De gegenereerde mini-diagrammen zijn geen rekenbronnen: de middentabel gebruikt bijvoorbeeld GO boven getallen die niet bij de getekende constante GO-lijn passen. Gebruik voor uitleg en berekeningen de hoofdstukfiguren.','small')
    b.p('Controle bij assemblage: volledigheid van alle bronpagina’s, bijgewerkte navigatie, behoud van opgaven en figuren, vergelijking van de paginaweergave buiten de geregistreerde wijzigingen. Dit is geen nieuwe inhoudelijke examenvalidatie of gemeten lestijdtoets.','small')
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
            elif kind=='student' and ch['nr']==2 and i==37 and line['bbox'][0]>500 and line['bbox'][1]<750 and re.fullmatch(r'\d+(?:[–-]\d+)?',full.strip()):
                new=re.sub(r'\d+',lambda m:str(int(m[0])+offset),full)
                rewrite_line(page,line,[new],ops,'chapter_glossary_reference');ops[-1]['right_aligned']=True
            elif kind=='answers' and ch['nr']==1 and i==0 and re.fullmatch(r'\d+',full.strip()) and 220<line['bbox'][1]<550:
                rewrite_line(page,line,[str(int(full)+offset)],ops,'answer_contents_page');ops[-1]['right_aligned']=True
            elif kind=='student':
                refs=replace_page_refs(line,offset)
                if refs:rewrite_line(page,line,refs,ops,'inline_page_reference')
                elif ch['nr']==1 and 'Qsubub' in full:
                    rewrite_line(page,line,[s['text'].replace('Qsubub','Qsub') for s in line['spans']],ops,'documented_notation_typo_Qsubub_to_Qsub')
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
    outlines=[]
    if kind=='student':outlines=[[1,'Colofon',2],[1,'Voorwoord',3],[1,'Inhoud',4]]
    else:outlines=[[1,'Leeswijzer',1],[1,'Inhoud' if kind=='answers' else 'Leeswijzer bij de bundeling',2]]
    for n,ch in enumerate(CH):
        while len(result)<offsets[n]:result.new_page(width=W,height=H);allblanks.append(len(result))
        src,records,sl=prepare_source(ch,kind,offsets[n]);result.insert_pdf(src,links=False)
        audit.extend(records);links.extend(sl)
        outlines.append([1,ch['id']+' '+ch['title'],offsets[n]+1])
        if kind=='student':
            for para in ch['paragraphs']:outlines.append([2,para['title'],offsets[n]+para['local_page']])
            outlines.append([2,'Overzicht en begrippen',offsets[n]+ch['intro_entries'][-1]['local_page']])
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
        for i,title in enumerate(['Belastingen en subsidies','Prijsgrenzen en quota','De concurrerende onderneming','Handel en bescherming']):
            outlines.append([2,title,S_END+glossary_pages+i+1])
    if len(result)%2:result.new_page(width=W,height=H);allblanks.append(len(result))
    add_links(result,links)
    result.set_toc(outlines)
    result.set_metadata({'title':('Boek 3 — ' if kind=='student' else 'Boek 3 — '+ {'answers':'Antwoorden — ','teacher':'Docenteninformatie — '}[kind])+M['book']['title'], 'subject':'Herziene editie · 4 vwo · Overheidsingrijpen · Volkomen concurrentie · Internationale handel','author':'','keywords':'4veco, economie, 4 vwo, Boek 3','creator':'4veco · assembly from supplied chapters','producer':'PyMuPDF + ReportLab'})
    result.set_page_labels([{'startpage':0,'prefix':'','style':'D','firstpagenum':1}])
    result.xref_set_key(result.pdf_catalog(),'PageLayout','/TwoPageRight')
    result.xref_set_key(result.pdf_catalog(),'Lang','(nl-NL)')
    result.xref_set_key(result.pdf_catalog(),'PageMode','/UseOutlines')
    result.subset_fonts()
    suffix={'student':'','answers':'_Antwoorden','teacher':'_Docenteninformatie'}[kind]
    output=ROOT/f'Boek_3_Compleet{suffix}.pdf'
    result.save(output,garbage=4,deflate=True)
    (ROOT/f'QA/{kind}_page_map.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2))
    summary={'file':output.name,'pages':len(result),'source_pages':sum(len(fitz.open(ROOT/ch[kind])) for ch in CH),'chapter_starts':[o+1 for o in offsets],'intentional_blank_pages':allblanks,'internal_links':sum(len(p.get_links()) for p in result),'bookmarks':len(outlines),'recorded_edits':sum(len(a['edits']) for a in audit)}
    result.close()
    return summary


def main():
    for f,h in json.loads((ROOT/'QA/input_hashes.json').read_text()).items():
        if hashlib.sha256((ROOT/f).read_bytes()).hexdigest()!=h:raise RuntimeError('Input changed: '+f)
    tmp=ROOT/'build/_intermediate';tmp.mkdir(exist_ok=True)
    back,gp,fs=make_back(tmp/'back.pdf')
    front=make_student_front(tmp/'front.pdf',S_END+1,fs)
    assert front.n==4
    a=make_answer_front(tmp/'answers_front.pdf');t=make_teacher_front(tmp/'teacher_front.pdf')
    summaries=[build('student',front,back,gp),build('answers',a),build('teacher',t)]
    manifest={'outputs':summaries,'glossary_entries':len(GLOSS),'glossary_pages':gp,'formula_pages':4,'book_chapter_pages':sum(ch['pages'] for ch in CH),'instructional_paragraphs':sum(len(c['paragraphs']) for c in CH),'exercise_total':sum(len(c['answer_exercises']) for c in CH),'formula_start':fs,'source_spreads_in_book':[[50,51],[86,87],[124,125]],'book_guidance':'skills/econ-book-builder.md: cover, colophon, preface, full contents, chapters, glossary, formula overview; answers kept separate','guidance_adaptations':'PDF-preserving stitch rather than reflow; supplied cover overrides template; separate answer PDFs remain paper-first; no unsupported license, school, publisher or contact asserted.'}
    (ROOT/'QA/assembly_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
    print(json.dumps(manifest,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
