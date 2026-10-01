"""Editable replacement pages for Book 2. No font files are distributed.
Run with ReportLab installed. Lato is read from the local font installation.
All coordinates are in points measured down from the top of an A4 page.
"""
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, Color, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT,TA_CENTER
import math,os
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'work/replacements';OUT.mkdir(parents=True,exist_ok=True)
FONTS=Path(os.environ.get('BOOK2_FONT_DIR','/usr/share/fonts/truetype/lato'))
for name,file in [('Lato','Lato-Regular.ttf'),('LatoBold','Lato-Bold.ttf'),('LatoHeavy','Lato-Heavy.ttf'),('LatoItalic','Lato-Italic.ttf')]:
    pdfmetrics.registerFont(TTFont(name,str(FONTS/file)))
pdfmetrics.registerFontFamily('Lato',normal='Lato',bold='LatoBold',italic='LatoItalic',boldItalic='LatoBold')
W,H=595.2756,841.8898; L,R=54,545.2756; WIDTH=R-L
NAVY='#183e51';BLUE='#007da2';MUTED='#557184';ORANGE='#a14f08';TEAL='#008574'
PALE='#eef4f6'; PALEBLUE='#eaf4f8'; PALEORANGE='#faf2e7'; LINE='#cedfe6'
C=None

def text(txt,x,y,w=WIDTH,size=10.6,leading=14,font='Lato',color=NAVY,align=TA_LEFT,maxh=None):
    st=ParagraphStyle('p',fontName=font,fontSize=size,leading=leading,textColor=HexColor(color),alignment=align,spaceAfter=0)
    p=Paragraph(txt,st);ww,hh=p.wrap(w,1000)
    if maxh is not None and hh>maxh+.01:raise ValueError((txt[:90],hh,maxh))
    p.drawOn(C,x,H-y-hh)
    return hh

def rect(x,y,w,h,fill=PALE,stroke=None,lw=.5):
    C.setFillColor(HexColor(fill));C.setStrokeColor(HexColor(stroke or fill));C.setLineWidth(lw)
    C.rect(x,H-y-h,w,h,fill=1,stroke=bool(stroke))

def line(x1,y1,x2,y2,color=LINE,width=.6):
    C.setStrokeColor(HexColor(color));C.setLineWidth(width);C.line(x1,H-y1,x2,H-y2)

def panel(y,h,fill=PALE,accent=BLUE,x=L,w=WIDTH):
    rect(x,y,w,h,fill);rect(x,y,2,h,accent)

def begin(tag,printed,title,nav=False,chapter=1):
    global C
    C=canvas.Canvas(str(OUT/f'{tag}.pdf'),pagesize=(W,H),pageCompression=1,invariant=1)
    C.setTitle(title);C.setAuthor('4veco')
    text('4veco / Boek 2',L,21,200,8.5,10,color=MUTED)
    chaptertitle={1:'2.1 Kosten en opbrengsten',2:'2.2 Elasticiteit',3:'2.3 Surplus en welvaart'}[chapter]
    C.setFillColor(HexColor(MUTED));C.setFont('Lato',8.5);C.drawRightString(R,H-29.5,chaptertitle)
    text(title,L,51,WIDTH,17.6,21.1,font='LatoHeavy',maxh=22)
    line(L,78,R,78,BLUE,1)
    if nav:
        labels=[('Begrippen',19),('Berekenen',20),('Stijgende MK',21),('Linoprint',22),('Atelier Boog',23)]
        x=L
        for j,(name,num) in enumerate(labels):
            s=f'{name} · {num}'; fs=8.1
            text(s,x,87,130,fs,10,font='LatoBold' if num==printed else 'Lato',color=NAVY if num==printed else MUTED)
            tw=pdfmetrics.stringWidth(s,'LatoBold' if num==printed else 'Lato',fs)
            if j<4:line(x+tw+10,88,x+tw+10,97,LINE,.8)
            x+=tw+21
        line(L,104,R,104,LINE,.5)
    text('Economie · 4 vwo',L,813,200,8,10,color=MUTED)
    C.setFont('Lato',9);C.setFillColor(HexColor(NAVY));C.drawRightString(R,H-822,str(printed))

def end():C.showPage();C.save()

def heading(txt,y,size=12.3):return text(txt,L,y,WIDTH,size,15,font='LatoBold')

def formula(txt,x,y,w=WIDTH,size=13,color=BLUE):
    return text(txt,x,y,w,size,size*1.22,font='LatoBold',color=color)

def fraction(label,num,den,x,y,w=WIDTH,size=14.0,tail='',color=BLUE):
    """A real fraction with an unambiguous numerator and denominator."""
    C.setFont('LatoBold',size);C.setFillColor(HexColor(color))
    labelw=pdfmetrics.stringWidth(label,'LatoBold',size)+7
    fracw=max(pdfmetrics.stringWidth(num,'LatoBold',size),pdfmetrics.stringWidth(den,'LatoBold',size))+10
    tailw=pdfmetrics.stringWidth(tail,'LatoBold',size)+7 if tail else 0
    if labelw+fracw+tailw>w:raise ValueError(('fraction too wide',label,num,den,labelw+fracw+tailw,w))
    C.drawString(x,H-y-22,label)
    C.drawCentredString(x+labelw+fracw/2,H-y-11,num)
    line(x+labelw,y+16,x+labelw+fracw,y+16,color,1)
    C.drawCentredString(x+labelw+fracw/2,H-y-31,den)
    if tail:C.drawString(x+labelw+fracw+7,H-y-22,tail)
    return 36

def table(headers,rows,y,widths=None,x=L,w=WIDTH,size=9.8,rowheight=None):
    if widths is None:widths=[w/len(headers)]*len(headers)
    ps=ParagraphStyle('cell',fontName='Lato',fontSize=size,leading=size*1.22,textColor=HexColor(NAVY))
    ph=ParagraphStyle('head',parent=ps,fontName='LatoBold',fontSize=size-.2,leading=size*1.22)
    def par(v,st):return Paragraph(str(v).replace('\n','<br/>'),st)
    data=[[par(v,ph)for v in headers]]+[[par(v,ps)for v in row]for row in rows]
    t=Table(data,colWidths=widths,hAlign='LEFT',rowHeights=rowheight)
    sty=[('VALIGN',(0,0),(-1,-1),'MIDDLE'),('BACKGROUND',(0,0),(-1,0),HexColor('#eaf1f4')),
         ('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),
         ('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5),
         ('LINEBELOW',(0,0),(-1,0),.6,HexColor('#adbfca')),
         ('LINEBELOW',(0,1),(-1,-1),.4,HexColor('#dce5ea'))]
    for i in range(2,len(data),2):sty.append(('BACKGROUND',(0,i),(-1,i),HexColor('#f7f9fa')))
    t.setStyle(TableStyle(sty));tw,th=t.wrap(w,1000);t.drawOn(C,x,H-y-th);return th

# 19: meaning precedes notation. Preserve the approved example and distinctions.
begin('theory19',19,'2.1.3 · Marginaal: wat komt er bij?',True)
text('<b>Wat kosten die tien extra producten?</b> Bij 40 producten zijn de totale kosten € 260. Bij 50 producten zijn ze € 300. De tien extra producten kosten samen € 40. Dat is nog niet het bedrag <b>per extra product</b>.',L,115,maxh=43)
panel(166,48)
text('<b>Lesdoelen</b><br/>Je kunt winst, MK en MO uit een tabel berekenen, constante en stijgende MK vergelijken en het verschil tussen gemiddeld en marginaal uitleggen.',L+11,174,WIDTH-22,10.0,13,maxh=40)
panel(225,100,PALEORANGE,ORANGE)
text('Marginale kosten (MK)',L+12,234,WIDTH-24,12.3,15,font='LatoBold')
text('De extra totale kosten <b>per extra geproduceerd product</b>.',L+12,255,WIDTH-24,10.6,14)
fraction('MK =','extra kosten','aantal extra producten',L+12,279,WIDTH-24,15,color=ORANGE)
panel(335,100,PALEBLUE,BLUE)
text('Marginale opbrengsten (MO)',L+12,344,WIDTH-24,12.3,15,font='LatoBold')
text('De extra totale opbrengst <b>per extra verkocht product</b>.',L+12,365,WIDTH-24,10.6,14)
fraction('MO =','extra opbrengsten','aantal extra verkochte producten',L+12,389,WIDTH-24,15)
text('Bij een stap van meerdere producten bereken je het <b>gemiddelde over alleen die extra producten</b>. Gebruik bedragen en hoeveelheden uit dezelfde periode.',L,445,WIDTH,10.4,13.5,maxh=28)
rect(L,483,WIDTH,74,'#f5f8f9',LINE)
text('<b>Eerst</b><br/>40 producten; totale kosten € 260',L+12,492,209,10.5,14,align=TA_CENTER)
text('<b>Daarna</b><br/>50 producten; totale kosten € 300',L+265,492,209,10.5,14,align=TA_CENTER)
text('→',L+232,500,28,17,20,align=TA_CENTER)
line(L+12,525,R-12,525)
text('<b>€ 40 extra kosten ÷ 10 extra producten = € 4 per extra product</b>',L+12,536,WIDTH-24,10.6,14,align=TA_CENTER)
text('Figuur 1. Bepaal eerst wat erbij komt. Deel dat bedrag daarna door het aantal extra producten.',L,563,WIDTH,8.4,11,color=MUTED)
heading('Gemiddeld of marginaal? Twee verschillende vragen',585)
cw=(WIDTH-12)/2
panel(608,126,'#edf5f3',TEAL,L,cw);panel(608,126,PALEORANGE,ORANGE,L+cw+12,cw)
text('<b>GTK: alle 50 producten</b>',L+10,618,cw-20,11.3,14)
text('Wat kost één product gemiddeld?',L+10,639,cw-20,9.9,13)
fraction('GTK =','300','50',L+10,658,cw-20,12.5,'= € 6',TEAL)
text('Alle € 300 kosten verdeeld over<br/><b>alle 50 producten</b>.',L+10,701,cw-20,9.8,12.4)
x=L+cw+12
text('<b>MK: de 10 extra producten</b>',x+10,618,cw-20,11.3,14)
text('Wat kost een extra product in de stap?',x+10,639,cw-20,9.8,13)
fraction('MK =','40','10',x+10,658,cw-20,12.5,'= € 4',ORANGE)
text('Alleen € 40 extra kosten verdeeld over<br/><b>de 10 extra producten</b>.',x+10,701,cw-20,9.8,12.4)
text('<b>Onthoud:</b> € 40 is de toename van de totale kosten, niet MK. Je deelt hier door <b>10</b> extra producten, niet door de nieuwe hoeveelheid 50. De korte notatie met Δ volgt op p. 20.',L,745,WIDTH,10.1,13.2,maxh=40)
end()

# 20: separate cost and revenue tracks, interval identity explicit.
begin('theory20',20,'2.1.3 · Eerst verschillen bepalen, dan delen',True)
heading('Dezelfde woordformule, een handige afkorting',115)
text('Δ spreek je uit als <b>delta</b>. Het betekent verandering: de nieuwe waarde min de oude waarde. De letters verkorten de woordformules; de betekenis blijft hetzelfde.',L,136,WIDTH,10.4,13.6,maxh=28)
panel(173,73)
formula('MK = ΔTK / ΔQ',L+12,182,210,12)
formula('MO = ΔTO / ΔQ',L+12,211,210,12)
text('ΔTK = extra kosten = TK nieuw − TK oud<br/>ΔTO = extra opbrengsten = TO nieuw − TO oud<br/>ΔQ = extra producten = Q nieuw − Q oud',L+217,182,WIDTH-229,9.8,17,maxh=53)
text('Een onderneming heeft de volgende functies. Q is in producten per week. De capaciteit is 40 producten per week; alle producten worden verkocht.',L,257,WIDTH,10.4,13.5,maxh=28)
formula('Totale kosten: TK = 100 + 3Q',L,292,WIDTH,11.2)
formula('Totale opbrengst: TO = 8Q',L,310,WIDTH,11.2)
th=table(['Q\nproducten/week','TK\n€/week','TO\n€/week','Bij de stap 10 → 30'],[[0,100,0,''],[10,130,80,'Oude rij'],[30,190,240,'Nieuwe rij']],335,[100,90,90,WIDTH-280],size=9.7)
heading('1  Kies de stap en bereken de extra hoeveelheid',449)
text('Van Q = 10 naar Q = 30 komen er <b>30 − 10 = 20 producten</b> bij. Zo’n stap tussen twee hoeveelheden heet een <b>interval</b>. De noemer is dus 20.',L,471,WIDTH,10.4,13.4,maxh=28)
heading('2  Bereken de extra bedragen; deel daarna door 20',510)
cw=(WIDTH-12)/2;panel(535,91,PALEORANGE,ORANGE,L,cw);panel(535,91,PALEBLUE,BLUE,L+cw+12,cw)
text('<b>Kosten</b><br/>Extra kosten: 190 − 130 = € 60',L+10,544,cw-20,10.4,14)
fraction('MK =','60','20',L+10,578,cw-20,12.8,'= € 3',ORANGE)
text('<b>Opbrengst</b><br/>Extra opbrengst: 240 − 80 = € 160',L+cw+22,544,cw-20,10.4,14)
fraction('MO =','160','20',L+cw+22,578,cw-20,12.8,'= € 8')
text('Per extra product: <b>€ 3 kosten en € 8 opbrengst</b>; samen € 60 en € 160 voor 20 producten.',L,636,WIDTH,10.2,13.4,maxh=14)
heading('3  Zet de uitkomst bij de laatste rij van de stap',664)
table(['Q','Stap','Extra producten','MK\n€/extra product','MO\n€/extra product'],[[0,'—','—','—','—'],[10,'0 → 10',10,'30 / 10 = 3','80 / 10 = 8'],[30,'10 → 30',20,'60 / 20 = 3','160 / 20 = 8']],687,[36,70,99,143,WIDTH-348],size=8.8)
text('De stap verdubbelt, maar MK en MO blijven gelijk. — betekent: geen vorige rij, niet nul.',L,784,WIDTH,9.2,11.5,color=MUTED)
end()

# 21: retain the original model and distinguish fixed from marginal cost.
begin('theory21',21,'2.1.3 · Constante en stijgende MK',True)
text('SchaalWerk maakt keramische schalen. Voor extra productie is steeds meer betaald werk per extra schaal nodig. De werkplaats blijft gelijk; de capaciteit is <b>12 schalen per week</b>.',L,115,WIDTH,10.6,14,maxh=42)
panel(166,69)
formula('TK = 80 + Q²  (euro per week)',L+12,176,WIDTH-24,13)
text('TCK blijft € 80 per week. Het variabele deel is Q²: bij 4 schalen is dat 4 × 4 = € 16; bij 8 schalen is het 8 × 8 = € 64.',L+12,201,WIDTH-24,10.3,13.4,maxh=28)
heading('Evenveel extra schalen, steeds méér extra kosten',249)
table(['Q\nschalen/week','TK\n€/week','Extra kosten\n€ per stap','Extra\nschalen','MK\n€ per extra schaal'],[[0,80,'—','—','—'],[4,96,'96 − 80 = 16',4,'16 / 4 = 4'],[8,144,'144 − 96 = 48',4,'48 / 4 = 12'],[12,224,'224 − 144 = 80',4,'80 / 4 = 20']],273,[76,69,140,66,WIDTH-351],size=9.5)
text('Elke stap bevat <b>4 extra schalen</b>. De extra kosten zijn achtereenvolgens € 16, € 48 en € 80. Daardoor stijgen de kosten per extra schaal: <b>€ 4 → € 12 → € 20</b>.',L,415,WIDTH,10.5,13.7,maxh=28)
# Vector curve with calibrated axes, equal horizontal steps and changing vertical steps.
gx,gy,gw,gh=L+48,463,WIDTH-81,156
X=lambda q:gx+q/12*gw
Y=lambda k:gy+gh-k/240*gh
for val in [0,80,160,240]:
    line(gx,Y(val),gx+gw,Y(val),'#e4eaee',.5)
    text(str(val),gx-35,Y(val)-5,28,8.6,10,color=MUTED,align=2)
for q in [0,4,8,12]:
    line(X(q),gy,X(q),gy+gh,'#eef1f3',.5);text(str(q),X(q)-14,gy+gh+7,28,8.6,10,color=MUTED,align=TA_CENTER)
line(gx,gy+gh,gx+gw+6,gy+gh,NAVY,.8);line(gx,gy+gh,gx,gy-5,NAVY,.8)
p=C.beginPath();p.moveTo(X(0),H-Y(80))
for i in range(1,241):q=i*.05;p.lineTo(X(q),H-Y(80+q*q))
C.setStrokeColor(HexColor(ORANGE));C.setLineWidth(1.6);C.drawPath(p)
for a,b,inc in [(0,4,16),(4,8,48),(8,12,80)]:
    C.saveState();C.setDash(3,2);line(X(a),Y(80+a*a),X(b),Y(80+a*a),MUTED,.7);line(X(b),Y(80+a*a),X(b),Y(80+b*b),MUTED,.7);C.restoreState()
    text('+ 4 schalen',X(a)+2,Y(80+a*a)+5,X(b)-X(a)-4,8.5,10,color=MUTED,align=TA_CENTER)
    # Labels alongside the vertical difference, inside the plot.
    text(f'+ € {inc}',X(b)+5 if inc==16 else X(b)-53,(Y(80+a*a)+Y(80+b*b))/2-6,49,8.6,10,color=ORANGE,align=0 if inc==16 else 2)
    C.setFillColor(HexColor(ORANGE));C.circle(X(b),H-Y(80+b*b),2.1,fill=1,stroke=0)
text('TK = 80 + Q²',X(7),gy-5,150,10.0,12,color=ORANGE,font='LatoBold')
C.saveState();C.translate(L+9,H-(gy+gh/2+33));C.rotate(90);C.setFont('Lato',9);C.setFillColor(HexColor(MUTED));C.drawString(0,0,'TK (€ per week)');C.restoreState()
text('Hoeveelheid Q (schalen per week)',gx,gy+gh+23,gw,9.2,12,color=MUTED,align=TA_CENTER)
text('Figuur 2. De kromme lijn is TK. De hulplijnen tonen de extra kosten bij telkens vier extra schalen.',L,657,WIDTH,8.4,11,color=MUTED)
heading('Constante kosten zijn iets anders dan constante MK',679)
text('Dezelfde € 80 vaste kosten zit in beide totaalbedragen en valt bij het aftrekken weg. De extra kosten komen hier uit Q², dat steeds sneller groeit. Bij het model TK = 100 + 3Q op p. 20 blijft MK juist € 3.',L,701,WIDTH,10.4,13.6,maxh=42)
panel(751,36,PALEORANGE,ORANGE)
text('<b>Een interval is niet één product.</b> MK = € 12 bij de stap 4 → 8 is een gemiddelde voor die vier extra schalen. Niet iedere schaal hoeft afzonderlijk precies € 12 extra te kosten.',L+10,758,WIDTH-20,9.4,11.8,maxh=25)
end()

# 22: one enterprise, no concatenated formula strings.
begin('theory22',22,'2.1.3 · Uitgewerkt voorbeeld: Linoprint',True)
text('<b>Dezelfde aanpak bij twee ondernemingen.</b> Bereken winst binnen één tabelrij. Bereken MK en MO tussen twee rijen. Linoprint heeft constante MK; op p. 23 volgt Atelier Boog met stijgende MK.',L,115,WIDTH,10.6,14,maxh=43)
panel(167,88)
text('<b>Linoprint</b> · capaciteit: 20 prints per week.<br/>Q is in prints per week; TK en TO zijn in euro per week.',L+11,176,WIDTH-22,10.5,13.7,maxh=28)
formula('Totale kosten: TK = 120 + 2Q',L+11,213,WIDTH-22,12.2)
formula('Totale opbrengst: TO = 6Q',L+11,234,WIDTH-22,12.2)
heading('1  Bereken de winst binnen elke rij',270)
formula('Winst = totale opbrengst − totale kosten',L,292,WIDTH,12.7)
text('Bij Q = 5: winst = 30 − 130 = <b>−€ 100 per week</b>. Je gebruikt hierbij alle opbrengsten en alle kosten van dezelfde hoeveelheid.',L,317,WIDTH,10.4,13.5,maxh=28)
table(['Q\nprints/week','TK\n€/week','TO\n€/week','Winst\n€/week','MK\n€/extra print','MO\n€/extra print'],[[0,120,0,'−120','—','—'],[5,130,30,'−100',2,6],[10,140,60,'−80',2,6],[15,150,90,'−60',2,6]],356,[76,73,73,81,94,WIDTH-397],size=9.5)
heading('2  Bereken MK tussen twee rijen: van 0 naar 5 prints',496)
text('Er komen 5 − 0 = <b>5 prints</b> bij. De extra kosten zijn 130 − 120 = <b>€ 10</b>.',L,517,WIDTH,10.5,13.8)
panel(541,51,PALEORANGE,ORANGE)
fraction('MK =','extra kosten','extra prints',L+10,550,268,12.2,color=ORANGE)
fraction('=','10','5',L+278,550,WIDTH-288,12.2,'= € 2 per extra print',ORANGE)
heading('3  Bereken MO voor dezelfde stap',606)
text('De extra opbrengst is 30 − 0 = <b>€ 30</b>. Deel ook dit bedrag door de 5 extra prints.',L,627,WIDTH,10.4,13.5)
panel(651,51,PALEBLUE,BLUE)
fraction('MO =','extra opbrengsten','extra verkochte prints',L+10,660,268,12.2)
fraction('=','30','5',L+278,660,WIDTH-288,12.2,'= € 6 per extra print')
text('<b>Waar staan de uitkomsten?</b> Bij Q = 5, de laatste rij van de stap 0 → 5. De volgende stappen geven dezelfde MK en MO. De variabele kosten nemen telkens met € 2 per extra print toe; iedere extra verkochte print levert € 6 op.',L,715,WIDTH,10.4,13.5,maxh=42)
panel(768,25,PALE)
text('<b>— is niet nul:</b> bij de eerste rij ontbreekt een eerdere tabelrij om mee te vergelijken.',L+10,774,WIDTH-20,9.6,12)
end()

# 23: another model, same separate calculations; explicit final comparison.
begin('theory23',23,'2.1.3 · Uitgewerkt voorbeeld: Atelier Boog',True)
panel(116,88)
text('<b>Atelier Boog</b> · capaciteit: 8 kunstwerkjes per week.<br/>Q is in kunstwerkjes per week; TK en TO zijn in euro per week.',L+11,125,WIDTH-22,10.5,13.7,maxh=28)
formula('Totale kosten: TK = 40 + Q²',L+11,162,WIDTH-22,12.2)
formula('Totale opbrengst: TO = 12Q',L+11,183,WIDTH-22,12.2)
heading('1  Bereken weer de winst binnen elke rij',218)
text('Bij Q = 2: winst = 24 − 44 = <b>−€ 20 per week</b>. MK en MO bereken je daarna over de stap vanaf de vorige rij.',L,239,WIDTH,10.4,13.5,maxh=28)
table(['Q\nkunstwerkjes/week','TK\n€/week','TO\n€/week','Winst\n€/week','MK\n€/extra stuk','MO\n€/extra stuk'],[[0,40,0,'−40','—','—'],[2,44,24,'−20',2,12],[4,56,48,'−8',6,12],[6,76,72,'−4',10,12]],278,[103,63,63,75,94,WIDTH-398],size=9.2)
heading('2  Bereken MK: extra kosten gedeeld door extra producten',418)
text('Elke stap bevat 2 extra kunstwerkjes. De extra kosten worden steeds groter.',L,439,WIDTH,10.3,13.4)
panel(461,95,PALEORANGE,ORANGE)
text('<b>Stap 0 → 2:</b>&nbsp;&nbsp; MK = (44 − 40) / 2 = <b>€ 2 per extra kunstwerkje</b><br/><b>Stap 2 → 4:</b>&nbsp;&nbsp; MK = (56 − 44) / 2 = <b>€ 6 per extra kunstwerkje</b><br/><b>Stap 4 → 6:</b>&nbsp;&nbsp; MK = (76 − 56) / 2 = <b>€ 10 per extra kunstwerkje</b>',L+11,474,WIDTH-22,10.6,26,maxh=80)
heading('3  Bereken MO voor dezelfde stap',570)
text('Voor de eerste stap komen er 2 verkopen en € 24 opbrengst bij.',L,591,WIDTH,10.4,13.5)
panel(614,48,PALEBLUE,BLUE)
fraction('MO =','24 − 0','2 − 0',L+11,622,WIDTH-22,12.7,'= € 12 per extra kunstwerkje')
text('MO blijft in elke stap € 12 door de vaste verkoopprijs. Bij Linoprint blijft MO om dezelfde reden € 6 per print. <b>Het verschil zit hier in MK:</b> constant bij Linoprint, stijgend bij Atelier Boog.',L,674,WIDTH,10.4,13.5,maxh=42)
panel(727,66)
text('<b>Onthoud: winst binnen één rij; MK en MO tussen twee rijen.</b><br/>Gemiddeld gaat over alle producten; marginaal over de extra producten. Deel door het echte aantal extra producten. MO is geen winst: bij Linoprint is de totale winst bij Q = 15 nog −€ 60. Je gebruikt hier geen afgeleiden en bepaalt nog geen winstmaximum.',L+11,736,WIDTH-22,9.8,12.4,maxh=51)
end()

# Printed 5: same worked example, each cost formula in its own row.
begin('worked05',5,'2.1.1 · Van kostenposten naar een conclusie')
heading('Uitgewerkt voorbeeld',91,16)
text('PlakLab maakt stickers. Het betaalt € 220 huur en € 80 abonnementskosten per maand. Folie kost € 0,80 en inkt € 0,20 per sticker. De capaciteit is 600 stickers per maand. Vergelijk een productie van 150 en 300 stickers in dezelfde maand.',L,118,WIDTH,10.6,14,maxh=56)
heading('Stap 1  Deel de kosten in en leg uit waarom',180)
table(['Kostenpost','Soort kosten','Reden'],[['Huur en abonnementen','Constant','Het totale maandbedrag blijft gelijk.'],['Folie en inkt','Variabel','Het totale bedrag groeit met het aantal stickers.']],203,[147,87,WIDTH-234],size=10.0)
heading('Stap 2  Stel de functies op',292)
text('Per sticker zijn de variabele kosten € 0,80 + € 0,20 = € 1. De totale bedragen zijn in euro per maand.',L,313,WIDTH,10.4,13.5,maxh=28)
panel(346,72)
formula('TCK = 220 + 80 = 300',L+12,355,WIDTH-24,11.7)
formula('TVK = 1 × Q = Q',L+12,376,WIDTH-24,11.7)
formula('TK = TCK + TVK = 300 + Q',L+12,397,WIDTH-24,11.7)
heading('Stap 3  Bereken totale en gemiddelde kosten',432)
text('Vul eerst Q in. Deel daarna ieder totaalbedrag door datzelfde aantal stickers.',L,453,WIDTH,10.3,13.4)
table(['Q\nstickers/maand','TCK\n€/maand','TVK\n€/maand','TK\n€/maand'],[[150,300,'1 × 150 = 150','300 + 150 = 450'],[300,300,'1 × 300 = 300','300 + 300 = 600']],475,[105,82,140,WIDTH-327],size=9.6)
table(['Q\nstickers/maand','GCK\n€/sticker','GVK\n€/sticker','GTK\n€/sticker'],[[150,'300 / 150 = 2,00','150 / 150 = 1,00','450 / 150 = 3,00'],[300,'300 / 300 = 1,00','300 / 300 = 1,00','600 / 300 = 2,00']],567,[105,129,129,WIDTH-363],size=9.5)
heading('Stap 4  Verbind de cijfers aan het verhaal',662)
text('TCK blijft € 300. TVK verdubbelt, maar TK stijgt van € 450 naar € 600 en verdubbelt niet. GCK halveert: dezelfde € 300 wordt over tweemaal zoveel stickers verdeeld. GVK blijft € 1. Daardoor daalt GTK van € 3 naar € 2, niet naar € 1,50. Beide hoeveelheden passen binnen de capaciteit.',L,683,WIDTH,10.2,13.1,maxh=53)
panel(741,52)
text('<b>Onthoud</b> · Constant of variabel? Kijk naar het totale bedrag bij een andere Q.<br/>Gemiddeld: deel het betreffende totaal door Q, met Q > 0. Totaal is in € per periode; gemiddeld in € per product.<br/>GVK blijft alleen gelijk als de variabele kosten per product gelijk blijven. Hierna voeg je opbrengsten toe.',L+11,749,WIDTH-22,9.4,12,maxh=41)
end()

# Printed 13: revenue, profit and break-even equations have separate lines.
begin('worked13',13,'2.1.2 · Het hele reken- en tekenproces')
heading('Uitgewerkt voorbeeld',91,16)
text('WafelWagen heeft TK = 250 + 2Q. Het verkoopt wafels voor een vaste prijs van € 5. De capaciteit is 150 wafels per dag. Bereken opbrengsten, winst en break-even en geef de uitkomsten ook in een grafiek weer.',L,118,WIDTH,10.6,14,maxh=43)
heading('Stap 1  Stel TO op en verklaar GO',174)
panel(197,59)
formula('TO = P × Q = 5Q',L+12,206,WIDTH-24,12)
formula('GO = TO / Q = 5Q / Q = € 5 per wafel  (Q > 0)',L+12,233,WIDTH-24,12)
text('Ieder verkocht exemplaar heeft dezelfde prijs. Daarom is GO hier gelijk aan P.',L,265,WIDTH,10.3,13.4)
heading('Stap 2  Vul Q in en trek TK van TO af',292)
table(['Q\nwafels/dag','TO\n€/dag','TK\n€/dag','Winst = TO − TK\n€/dag'],[[50,'5 × 50 = 250','250 + 2 × 50 = 350','250 − 350 = −100'],[100,'5 × 100 = 500','250 + 2 × 100 = 450','500 − 450 = 50']],315,[83,126,149,WIDTH-358],size=9.6)
text('Bij 50 wafels is er € 100 verlies; bij 100 wafels is er € 50 winst.',L,407,WIDTH,10.4,13.5)
heading('Stap 3  Los TO = TK op en duid de uitkomst',434)
panel(457,83)
formula('5Q = 250 + 2Q',L+12,466,WIDTH-24,11.8)
formula('3Q = 250',L+12,489,WIDTH-24,11.8)
formula('Q = 250 / 3 = 83,333… wafels per dag',L+12,512,WIDTH-24,11.8)
text('Het snijpunt ligt bij Q ≈ 83,33. De opbrengst is daar 5 × 83,333… ≈ € 416,67. Gebruik de onafgeronde Q. Het eerste gehele aantal zonder verlies is <b>84 wafels per dag</b>: TO is dan € 420, TK € 418 en de winst € 2. Dit past binnen de capaciteit.',L,550,WIDTH,10.4,13.5,maxh=54)
heading('Stap 4  Teken en controleer',616)
text('Gebruik figuur 2 op de vorige pagina als controle. Horizontaal staan wafels per dag; verticaal euro per dag. TO begint bij nul en TK bij € 250. Benoem de lijnen en markeer het snijpunt. Links is er verlies, rechts winst. Bij Q = 100 is de winst een <b>verticale afstand van € 50</b>, geen oppervlakte.',L,637,WIDTH,10.3,13.4,maxh=54)
panel(703,90)
text('<b>Onthoud</b>',L+11,711,WIDTH-22,10.8,13)
text('<b>Opbrengst:</b> TO = P × Q<br/><b>Per product:</b> GO = TO / Q; bij een vaste prijs geldt GO = P<br/><b>Winst:</b> Winst = TO − TK; een negatieve uitkomst is verlies<br/><b>Break-even:</b> TO = TK; maak onderscheid tussen het snijpunt en het eerste gehele aantal zonder verlies.',L+11,731,WIDTH-22,9.7,12.6,maxh=64)
end()
print('Rendered',len(list(OUT.glob('*.pdf'))),'replacement pages')
