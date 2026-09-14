"""Deterministic, editable SVG figures. Numbers are authored teaching models.
Run before build.py. SVG and PNG are supplied; PDF embeds vectors.
"""
from pathlib import Path
from html import escape
import json, math
import cairosvg
ROOT=Path(__file__).resolve().parent; A=ROOT/'_assets'; A.mkdir(exist_ok=True)
INK='#183247'; BLUE='#17688f'; TEAL='#227064'; ORANGE='#a76322'; GRAY='#596d7c'
BG='#f4f7f9'; LINE='#cbd7df'
GEOMETRY=[]
def txt(x,y,s,size=16,color=INK,weight='normal',anchor='start'):
    return f'<text x="{x:.3f}" y="{y:.3f}" font-family="Lato,DejaVu Sans,sans-serif" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="{anchor}">{escape(str(s))}</text>'
def line(x1,y1,x2,y2,color=INK,width=2,dash=''):
    return f'<line x1="{x1:.4f}" y1="{y1:.4f}" x2="{x2:.4f}" y2="{y2:.4f}" stroke="{color}" stroke-width="{width}" '+(f'stroke-dasharray="{dash}"' if dash else '')+'/>'
def rect(x,y,w,h,fill=BG,stroke=LINE):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{fill}" stroke="{stroke}"/>'
def arrow(x1,y1,x2,y2,col=BLUE):
    ang=math.atan2(y2-y1,x2-x1);ln=8
    x3=x2-ln*math.cos(ang-.4);y3=y2-ln*math.sin(ang-.4)
    x4=x2-ln*math.cos(ang+.4);y4=y2-ln*math.sin(ang+.4)
    return line(x1,y1,x2,y2,col,2)+f'<path d="M{x3},{y3} L{x2},{y2} L{x4},{y4}" fill="none" stroke="{col}" stroke-width="2"/>'
def save(name,body,h=340):
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="720" height="{h}" viewBox="0 0 720 {h}"><rect width="720" height="{h}" rx="8" fill="{BG}"/>'+body+'</svg>'
    (A/(name+'.svg')).write_text(svg,encoding='utf-8')
    cairosvg.svg2png(bytestring=svg.encode(),write_to=str(A/(name+'.png')),output_width=1440,output_height=h*2)

def graph(name,title,demand=None,supply=None,newdemand=None,points=(),wage=None,shade_bill=False,gap=None,xmax=200,ymax=30,unit='L (personen)',h=350,labels=True):
    """Demand/supply passed as L=intercept+slope*w. Inverse curve for rendering."""
    x0,y0,pw,ph=82,275,495,218
    X=lambda x:x0+x/xmax*pw;Y=lambda y:y0-y/ymax*ph
    body=txt(25,29,title,18,BLUE,'bold')
    pyvals=set(w for q,w,lab in points)
    if wage is not None:pyvals.add(wage)
    ticks_y=sorted(pyvals | {float(y) for y in range(0,int(ymax)+1,5 if ymax>=25 else 4)
                 if all(abs(Y(y)-Y(v))>13 for v in pyvals)})
    for y in ticks_y:
        body+=line(x0,Y(y),x0+pw,Y(y),LINE,.65)+txt(x0-12,Y(y)+5,f'{y:g}',13,INK if y in pyvals else GRAY,anchor='end')
    step=40 if xmax>=160 else 20
    pxvals=set(q for q,w,lab in points)
    ticks_x=sorted(pxvals | {float(x) for x in range(0,int(xmax)+1,step)
                 if all(abs(X(x)-X(v))>22 for v in pxvals)})
    for x in ticks_x:
        body+=line(X(x),y0,X(x),y0+4,INK,1)+txt(X(x),y0+21,f'{x:g}',13,INK if x in pxvals else GRAY,anchor='middle')
    body+=arrow(x0,y0,x0+pw+16,y0,INK)+arrow(x0,y0,x0,44,INK)
    body+=txt(96,49,'w (€ per uur)',13,INK)+txt(x0+pw/2,326,unit,15,INK,anchor='middle')
    if shade_bill:
        q,w=shade_bill
        body+=f'<rect x="{X(0)}" y="{Y(w)}" width="{X(q)-X(0)}" height="{Y(0)-Y(w)}" fill="#d7e8e2" stroke="{TEAL}" stroke-width="1"/>'
        body+=txt(X(q/2),Y(w/2),'w × L',16,TEAL,'bold','middle')
    for nm,fn,col,ds in [('arbeidsvraag',demand,BLUE,''),('arbeidsaanbod',supply,TEAL,''),('vraag nieuw',newdemand,ORANGE,'7 4')]:
        if fn is None:continue
        a,b=fn; iv=-a/b;sl=1/b
        lo,hi=0,xmax
        crossings=[0,xmax,(0-iv)/sl,(ymax-iv)/sl]
        valid=sorted(set(x for x in crossings if -1e-8<=x<=xmax+1e-8 and -1e-8<=iv+sl*x<=ymax+1e-8))
        if len(valid)<2:raise ValueError((name,nm,valid))
        lo,hi=valid[0],valid[-1];coords=[X(lo),Y(iv+sl*lo),X(hi),Y(iv+sl*hi)]
        body+=f'<line data-curve="{nm}" x1="{coords[0]:.4f}" y1="{coords[1]:.4f}" x2="{coords[2]:.4f}" y2="{coords[3]:.4f}" stroke="{col}" stroke-width="3" '+(f'stroke-dasharray="{ds}"' if ds else '')+'/>'
        GEOMETRY.append({'file':name,'curve':nm,'L_intercept':a,'L_slope':b,'xmax':xmax,'ymax':ymax,'plot':[x0,y0,pw,ph],'endpoint_data':[[lo,iv+sl*lo],[hi,iv+sl*hi]],'svg_coordinates':coords})
    # Direct legend to right, outside the plot (keeps crossing lines legible).
    yleg=79
    for nm,fn,col,ds in [('Lᵥ · vraag',demand,BLUE,''),('Lₐ · aanbod',supply,TEAL,''),('Lᵥ nieuw',newdemand,ORANGE,'6 4')]:
        if fn is None:continue
        body+=line(600,yleg-5,625,yleg-5,col,3,ds)+txt(600,yleg+15,nm,13,col,'bold');yleg+=49
    if wage is not None:
        body+=line(X(0),Y(wage),X(xmax),Y(wage),ORANGE,2,'5 4')
        body+=txt(600,242,f'w = {wage:g}',14,ORANGE,'bold')
    for q,w,lab in points:
        body+=line(X(q),Y(w),X(q),y0,GRAY,1,'4 4')+line(x0,Y(w),X(q),Y(w),GRAY,1,'4 4')
        body+=f'<circle data-point="{escape(lab)}" cx="{X(q):.4f}" cy="{Y(w):.4f}" r="4" fill="{INK}"/>'
        body+=txt(X(q),Y(w)-13,lab,14,INK,'bold','middle')

    if gap:
        q1,q2,w=gap
        body+=line(X(q1),Y(w),X(q2),Y(w),ORANGE,4)
        body+=txt(600,284,f'verschil: {q2-q1:g}',13,ORANGE,'bold')
    save(name,body,h)

def actors():
    b=txt(26,30,'Zelfde mensen, andere rollen',19,BLUE,'bold')
    for y,title,left,right,flow,pay in [(55,'Goederenmarkt','Huishoudens','Bedrijven','producten','betaling'),(205,'Arbeidsmarkt','Huishoudens','Werkgevers','arbeid','loon')]:
        b+=txt(28,y+4,title,16,BLUE,'bold')
        b+=rect(28,y+21,175,87,'#e5eef3')+rect(517,y+21,175,87,'#e5eef3')
        b+=txt(115,y+52,left,16,INK,'bold','middle')+txt(604,y+52,right,16,INK,'bold','middle')
        if title=='Goederenmarkt':
            b+=txt(115,y+77,'vragers',15,BLUE,anchor='middle')+txt(604,y+77,'aanbieders',15,TEAL,anchor='middle')
            b+=arrow(505,y+40,217,y+40,TEAL)+txt(361,y+33,flow,14,TEAL,anchor='middle')
            b+=arrow(215,y+86,505,y+86,BLUE)+txt(361,y+80,pay,14,BLUE,anchor='middle')
        else:
            b+=txt(115,y+77,'aanbieders',15,TEAL,anchor='middle')+txt(604,y+77,'vragers',15,BLUE,anchor='middle')
            b+=arrow(215,y+40,505,y+40,TEAL)+txt(361,y+33,flow,14,TEAL,anchor='middle')
            b+=arrow(505,y+86,215,y+86,BLUE)+txt(361,y+80,pay,14,BLUE,anchor='middle')
    save('actor_bridge',b,335)

def population(name,total,working,unemployed,title='Van bevolking naar beroepsbevolking'):
    labor=working+unemployed;other=total-labor
    b=txt(24,29,title,18,BLUE,'bold')+rect(185,49,350,50,'#e4eef3')
    b+=txt(360,70,'Bevolking 15 tot 75 jaar',16,INK,'bold','middle')+txt(360,90,f'{total:,} personen'.replace(',','.'),15,INK,anchor='middle')
    b+=arrow(288,100,209,137)+arrow(463,100,562,137)
    b+=rect(32,141,329,57,'#e1eee8')+rect(420,141,267,57)
    b+=txt(196,164,'Beroepsbevolking',16,TEAL,'bold','middle')+txt(196,185,f'{labor:,}'.replace(',','.'),17,TEAL,'bold','middle')
    b+=txt(553,164,'Niet-beroepsbevolking',15,INK,'bold','middle')+txt(553,185,f'{other:,}'.replace(',','.'),17,INK,'bold','middle')
    b+=arrow(129,199,115,230)+arrow(269,199,293,230)
    for x,t,n in [(20,'Werkzaam',working),(219,'Werkloos',unemployed)]:
        b+=rect(x,236,178,60,'#ffffff')+txt(x+89,258,t,15,INK,'bold','middle')+txt(x+89,282,f'{n:,}'.replace(',','.'),17,INK,'bold','middle')
    b+=txt(437,245,'Niet iedereen zonder',14,GRAY)+txt(437,267,'betaald werk telt',14,GRAY)+txt(437,289,'als werkloos.',14,GRAY)
    save(name,b,320)

def vacancies():
    b=txt(25,29,'Werkenden staan in beide tellingen',19,BLUE,'bold')
    sx=30;scale=.58
    for y,label,right,n,c in [(78,'Beroepsbevolking','100 werklozen',100,ORANGE),(181,'Arbeidsvraag in de bron','60 vacatures',60,BLUE)]:
        b+=txt(30,y-8,label,16,INK,'bold')
        b+=rect(sx,y,900*scale,43,'#dfebe7')+txt(sx+900*scale/2,y+27,'900 werkenden',16,TEAL,'bold','middle')
        b+=rect(sx+900*scale,y,n*scale,43,'#f1e5d9')
        b+=txt(552,y+66,right,14,c,'bold','middle')
    b+=txt(25,296,'1.000 − 960 = 40 is 100 werklozen − 60 vacatures, niet het aantal werklozen.',15,INK)
    save('vacancy_overlap',b,325)

def productivity():
    b=txt(25,30,'Productieverandering én productiviteit bepalen de uren',18,BLUE,'bold')
    cols=[('Oorspronkelijk','2.400 producten','4 per arbeidsuur','600 arbeidsuren'),('Zelfde productie','2.400 producten','5 per arbeidsuur','480 arbeidsuren'),('Meer opdrachten','3.300 producten','5 per arbeidsuur','660 arbeidsuren')]
    for j,parts in enumerate(cols):
        x=20+j*235;b+=rect(x,59,216,175,'#ffffff')
        for i,t in enumerate(parts):b+=txt(x+108,88+39*i,t,16 if i==0 else 15,BLUE if i in [0,3] else INK,'bold' if i in [0,3] else 'normal','middle')
    b+=txt(360,268,'Bij 3.000 producten en 5 producten per uur blijven 600 uren nodig.',16,INK,anchor='middle')
    b+=txt(360,296,'Dit rekenschema is geen bewijs dat werkgelegenheid altijd daalt.',15,GRAY,anchor='middle')
    save('productivity_paths',b,322)

def units():
    b=txt(24,30,'Personen, uren en voltijdbanen zijn verschillende maten',18,BLUE,'bold')
    b+=rect(26,62,200,129,'#e5eef3')+txt(126,92,'6 personen',21,BLUE,'bold','middle')+txt(126,122,'ieder 20 uur',17,INK,anchor='middle')+txt(126,150,'per week',16,INK,anchor='middle')
    b+=arrow(239,125,294,125)+rect(306,62,174,129,'#e1eee8')+txt(393,92,'120 uur',21,TEAL,'bold','middle')+txt(393,124,'arbeidsinzet',16,INK,anchor='middle')+txt(393,151,'per week',16,INK,anchor='middle')
    b+=arrow(493,125,535,125)+rect(547,62,149,129,'#ffffff')+txt(621,96,'3 fte',23,INK,'bold','middle')+txt(621,127,'120 ÷ 40',16,INK,anchor='middle')
    b+=txt(360,230,'In dit voorbeeld is een voltijdbaan 40 uur per week.',16,INK,anchor='middle')
    b+=txt(360,263,'De zes personen verdwijnen niet doordat je hun uren omrekent naar fte.',15,GRAY,anchor='middle')
    save('units',b,294)

def causes():
    b=txt(24,29,'Kijk naar de oorzaak, niet alleen naar de duur',18,BLUE,'bold')
    data=[('Conjunctureel','Minder bestedingen','→ minder opdrachten','→ minder personeel'),('Structureel','Werk of vaardigheden','passen niet meer','→ aanpassing nodig'),('Frictie','Zoeken en overstappen','kosten tijd','→ tijdelijk geen werk')]
    for i,parts in enumerate(data):
        x=20+i*235;b+=rect(x,59,216,151,'#ffffff')
        for j,t in enumerate(parts):b+=txt(x+108,89+j*31,t,16 if j==0 else 14.5,BLUE if j==0 else INK,'bold' if j==0 else 'normal','middle')
    b+=txt(360,246,'Frictiewerkloosheid rekenen we hier tot structurele werkloosheid.',15,GRAY,anchor='middle')
    save('unemployment_causes',b,275)

def bargaining():
    b=txt(24,29,'Een cao: collectieve afspraken over arbeidsvoorwaarden',18,BLUE,'bold')
    b+=rect(20,59,245,104,'#e5eef3')+txt(142,89,'Vakbond(en)',19,BLUE,'bold','middle')+txt(142,118,'vertegenwoordigen',15,INK,anchor='middle')+txt(142,144,'werknemers',16,INK,anchor='middle')
    b+=rect(455,59,245,104,'#e1eee8')+txt(578,89,'Werkgever(s)',19,TEAL,'bold','middle')+txt(578,118,'of hun',15,INK,anchor='middle')+txt(578,144,'organisatie',16,INK,anchor='middle')
    b+=arrow(268,105,448,105)+arrow(448,133,268,133)
    b+=txt(360,193,'Onderhandelen en afspraken vastleggen',17,INK,'bold','middle')+arrow(360,204,360,228)
    b+=rect(104,239,512,60,'#ffffff')+txt(360,265,'Loon · werktijd · scholing · verlof',18,BLUE,'bold','middle')+txt(360,288,'niet alleen het uurloon',15,GRAY,anchor='middle')
    save('bargaining',b,325)

def index_compare():
    b=txt(24,29,'Eén product: uurkosten delen door productie per uur',18,BLUE,'bold')
    for j,(ttl,hc,ap,unit) in enumerate([('Oud','€ 24 per uur','4 producten per uur','€ 6 per product'),('Nieuw','€ 25,20 per uur','4,5 producten per uur','€ 5,60 per product')]):
        x=25+j*355;b+=rect(x,62,315,167,'#ffffff')
        for i,s in enumerate([ttl,hc,'÷ '+ap,'= '+unit]):b+=txt(x+157,91+37*i,s,17 if i==0 else 16,BLUE if i in [0,3] else INK,'bold' if i in [0,3] else 'normal','middle')
    b+=txt(360,263,'Uurkosten: +5%. Productiviteit: +12,5%. Kosten per product: −6,67%.',15,INK,anchor='middle')
    b+=txt(360,293,'Twee groeipercentages aftrekken geeft niet de exacte verandering.',15,GRAY,anchor='middle')
    save('cao_costs',b,320)

if __name__=='__main__':
    actors();units();productivity();population('population',1000,600,100);population('population_we',2000,1260,140);vacancies();causes();bargaining();index_compare()
    # 4.3.1: one labour-demand relationship, then an outward shift.
    graph('demand_move','Alleen het loon verandert: beweging langs Lᵥ',(-0+160,-5),points=[(80,16,'A'),(60,20,'B')],xmax=160,ymax=32,unit='L (arbeidsuren per week)')
    graph('demand_shift','Meer orders bij hetzelfde loon: Lᵥ verschuift',(160,-5),newdemand=(180,-5),points=[(80,16,'A'),(100,16,'C')],xmax=200,ymax=40,unit='L (arbeidsuren per week)')
    graph('demand_base','Basisgrafiek: arbeidsvraag',(160,-5),xmax=160,ymax=32,unit='L (arbeidsuren per week)')
    graph('eq_intro','Dezelfde vergelijking, nu met loon en arbeid',(180,-10),(-20,10),points=[(80,10,'E')],xmax=180,ymax=20)
    graph('eq_base','Markeer loon en werkgelegenheid',(200,-8),(-24,8),xmax=200,ymax=25)
    graph('eq_we','Evenwicht in de voorbeeldsector',(160,-5),(-20,5),points=[(70,18,'E')],xmax=160,ymax=32)
    graph('eq_target','Basisgrafiek bij opgave 16',(240,-10),(-40,10),xmax=240,ymax=28)
    graph('eq_target_answer','Opgave 16 · loon € 14, werkgelegenheid 100',(240,-10),(-40,10),points=[(100,14,'E')],xmax=240,ymax=28)
    graph('eq_ind_answer','Opgave 15 · loon € 14, werkgelegenheid 88',(200,-8),(-24,8),points=[(88,14,'E')],xmax=200,ymax=25)
    graph('shift_flex','Loon past zich aan: nieuw evenwicht',(200,-10),(-40,10),(160,-10),points=[(80,12,'E₀'),(60,10,'E₁')],xmax=200,ymax=24)
    graph('shift_fixed','Loon blijft € 12: niet iedereen vindt werk',(200,-10),(-40,10),(160,-10),points=[(40,12,'vraag nieuw'),(80,12,'aanbod')],wage=12,gap=(40,80,12),xmax=200,ymax=24)
    graph('shift_we','Voorbeeld: minder opdrachten bij flexibel loon',(200,-8),(-24,8),(168,-8),points=[(88,14,'E₀'),(72,12,'E₁')],xmax=200,ymax=25)
    graph('shift_ind','Basisgrafiek: minder vraag naar arbeid',(180,-5),(-20,5),(160,-5),xmax=180,ymax=36)
    graph('shift_target','Basisgrafiek bij opgave 25',(180,-6),(-12,6),(144,-6),xmax=180,ymax=30)
    graph('shift_target_answer','Opgave 25 · van E₀ naar E₁',(180,-6),(-12,6),(144,-6),points=[(84,16,'E₀'),(66,13,'E₁')],xmax=180,ymax=30)
    graph('shift_ind_answer','Opgave 24 · loon € 18, werkgelegenheid 70',(180,-5),(-20,5),(160,-5),points=[(80,20,'E₀'),(70,18,'E₁')],xmax=180,ymax=36)
    graph('floor_nonbinding','Minimumloon € 10: evenwicht blijft bestaan',(200,-10),(-40,10),points=[(80,12,'E')],wage=10,xmax=200,ymax=24)
    graph('floor_binding','Minimumloon € 14: 60 werkenden, 100 aanbieders',(200,-10),(-40,10),points=[(60,14,'werk'),(100,14,'aanbod')],wage=14,gap=(60,100,14),xmax=200,ymax=24)
    graph('floor_bill','De loonsom gebruikt alleen betaalde arbeid',(200,-10),(-40,10),shade_bill=(60,14),wage=14,xmax=200,ymax=24)
    graph('floor_we','Voorbeeld: minimumloon € 22',(180,-5),(-20,5),wage=22,points=[(70,22,'werk'),(90,22,'aanbod')],gap=(70,90,22),xmax=180,ymax=36)
    graph('floor_guide','Basisgrafiek bij opgave 31',(180,-6),(-12,6),xmax=180,ymax=30)
    graph('floor_target','Basisgrafiek bij opgave 34',(220,-10),(-20,10),xmax=220,ymax=24)
    graph('floor_target_answer','Opgave 34 · minimumloon € 14',(220,-10),(-20,10),wage=14,points=[(80,14,'werk'),(120,14,'aanbod')],gap=(80,120,14),xmax=220,ymax=24)
    graph('floor_guide_answer','Opgave 31 · minimumloon € 18',(180,-6),(-12,6),wage=18,points=[(72,18,'werk'),(96,18,'aanbod')],gap=(72,96,18),xmax=180,ymax=30)
    graph('mixed_base','Basisgrafiek bij opgave 49',(240,-10),(-40,10),(280,-10),xmax=280,ymax=32)
    graph('mixed_answer','Opgave 49 · meer exportorders',(240,-10),(-40,10),(280,-10),points=[(100,14,'E₀'),(120,16,'E₁')],xmax=280,ymax=32)
    (ROOT/'QA'/'figure_geometry.json').write_text(json.dumps(GEOMETRY,ensure_ascii=False,indent=2))
    print('SVG/PNG pairs',len(list(A.glob('*.svg'))),'line geometry records',len(GEOMETRY))
