var QUIZ_DATA = {
  "meta": {
    "parNr": "1.1.1",
    "parName": "Schaarste en economisch denken",
    "subtitle": "Test je kennis van schaarste, alternatieve kosten en de 4-stappenprocedure voor economisch denken, inclusief nettowaarde. Deze instapquiz bereidt je voor op de oefeningen.",
    "testTopics": [
      "Schaarste herkennen in dagelijkse situaties",
      "Alternatieve kosten berekenen",
      "De 4-stappenprocedure voor economisch denken, inclusief nettowaarde",
      "Misconcepties rond schaarste en alternatieve kosten"
    ]
  },
  "categories": {
    "schaarste": {
      "name": "Schaarste herkennen",
      "colors": {
        "bg": "#E8F8F5",
        "text": "#0B5E5A",
        "bar": "#148F83"
      }
    },
    "altkosten": {
      "name": "Alternatieve kosten",
      "colors": {
        "bg": "#EBF5FB",
        "text": "#154360",
        "bar": "#1A5276"
      }
    },
    "procedure": {
      "name": "Procedure economisch denken",
      "colors": {
        "bg": "#FEF5E7",
        "text": "#BA6A1C",
        "bar": "#E67E22"
      }
    },
    "misconcepties": {
      "name": "Misconcepties",
      "colors": {
        "bg": "#F9EBEA",
        "text": "#922B21",
        "bar": "#C0392B"
      }
    }
  },
  "questions": [
    {
      "category": "schaarste",
      "difficulty": 1,
      "q": "Wat is de economische definitie van schaarste?",
      "options": [
        "Behoeften zijn groter dan de beschikbare middelen, dus moeten er keuzes worden gemaakt",
        "Een product is zeldzaam en daardoor duur",
        "Er is te weinig geld in een samenleving",
        "De vraag naar een product stijgt plotseling"
      ],
      "answer": 0,
      "rationale": "Schaarste betekent dat behoeften groter zijn dan beschikbare middelen — daardoor is kiezen onvermijdelijk. Zeldzaamheid of prijs is iets anders."
    },
    {
      "category": "schaarste",
      "difficulty": 1,
      "q": "In een supermarkt liggen 500 pakken melk. Er komen 100 klanten die elk 1 pak willen. Is er sprake van schaarste?",
      "options": [
        "Nee, want het aanbod is groter dan de vraag",
        "Ja, want melk is een schaars product",
        "Ja, want iedereen betaalt voor de melk",
        "Nee, want melk is nooit schaars"
      ],
      "answer": 0,
      "rationale": "Schaarste gaat om de verhouding tussen behoeften en middelen. 500 pakken voor 100 klanten — middelen > behoeften, dus geen schaarste."
    },
    {
      "category": "schaarste",
      "difficulty": 2,
      "q": "Een student heeft 4 uur vrije tijd en wil drie dingen doen die elk 2 uur kosten. Is er schaarste?",
      "options": [
        "Ja, want de student wil 6 uur aan activiteiten maar heeft maar 4 uur",
        "Nee, want tijd is geen economisch middel",
        "Nee, want de student kan alles gratis doen",
        "Ja, maar alleen als de student ook geld nodig heeft"
      ],
      "answer": 0,
      "rationale": "De behoefte aan tijd (6 uur) is groter dan het beschikbare middel (4 uur). Schaarste gaat ook over tijd, niet alleen over geld."
    },
    {
      "category": "schaarste",
      "difficulty": 3,
      "q": "Welke uitspraak over schaarste is correct?",
      "options": [
        "Schaarste geldt voor consumenten, producenten en de overheid — iedereen moet kiezen bij beperkte middelen",
        "Schaarste geldt alleen voor arme mensen met weinig geld",
        "Schaarste verdwijnt als de productie stijgt",
        "Schaarste is hetzelfde als zeldzaamheid"
      ],
      "answer": 0,
      "rationale": "Schaarste is universeel: ook een miljardair kiest hoe hij zijn tijd besteedt, een boer hoe hij zijn land verdeelt, een overheid hoe het budget wordt ingezet. Schaarste ≠ zeldzaamheid — het gaat om behoeften > middelen."
    },
    {
      "category": "altkosten",
      "difficulty": 1,
      "q": "Wat zijn alternatieve kosten?",
      "options": [
        "De opbrengst van het beste niet-gekozen alternatief",
        "De prijs die je betaalt voor een product",
        "De som van alle niet-gekozen alternatieven",
        "Het verschil tussen twee alternatieven"
      ],
      "answer": 0,
      "rationale": "Alternatieve kosten zijn de opbrengst (waarde) van het beste alternatief dat je opgeeft. Niet de prijs, niet de som."
    },
    {
      "category": "altkosten",
      "difficulty": 1,
      "q": "Lisa heeft €20. Ze koopt een bioscoopkaartje van €12. Het alternatief was een boek van €15. Wat zijn haar alternatieve kosten?",
      "options": [
        "Het leesplezier van het boek ter waarde van €15",
        "€12 (de bioscoopprijs)",
        "€8 (wat overblijft van haar €20)",
        "€27 (bioscoop + boek)"
      ],
      "answer": 0,
      "rationale": "Alternatieve kosten = de waarde van wat je opgeeft. Lisa geeft het boek op — de waarde daarvan (€15 aan leesplezier) is haar alternatieve kosten."
    },
    {
      "category": "altkosten",
      "difficulty": 2,
      "q": "Een boer heeft 8 hectare. Tarwe levert €500/ha op, maïs €350/ha, zonnebloemen €300/ha. Hij kiest zonnebloemen. Wat zijn zijn alternatieve kosten?",
      "options": [
        "€4.000 (de tarweopbrengst die hij misloopt)",
        "€2.400 (de zonnebloemopbrengst)",
        "€5.200 (tarwe + maïs opgeteld)",
        "€2.800 (de maïsopbrengst)"
      ],
      "answer": 0,
      "rationale": "Tarwe is het beste niet-gekozen alternatief: 8 × €500 = €4.000. Alternatieve kosten = één alternatief (het beste), niet de som."
    },
    {
      "category": "altkosten",
      "difficulty": 2,
      "q": "Eva heeft een vrije middag (4 uur). Opties: bijles geven (€40), studeren (€30 aan betere cijfers), film kijken (€15). Ze kiest studeren. Wat zijn haar alternatieve kosten?",
      "options": [
        "€40 (bijles geven)",
        "€55 (bijles + film samen)",
        "€15 (film kijken)",
        "€30 (de opbrengst van haar keuze)"
      ],
      "answer": 0,
      "rationale": "Het beste niet-gekozen alternatief is bijles geven (€40). Dat zijn Eva's alternatieve kosten — niet de som van alle niet-gekozen opties."
    },
    {
      "category": "altkosten",
      "difficulty": 3,
      "q": "Een overheid besteedt €100 miljoen extra aan onderwijs. Alternatieven waren: wegen (€80 mln waarde), zorg (€95 mln waarde), defensie (€60 mln waarde). Wat zijn de alternatieve kosten?",
      "options": [
        "€95 mln — de waarde van zorg, het beste niet-gekozen alternatief",
        "€235 mln — alle niet-gekozen alternatieven opgeteld",
        "€100 mln — het bedrag dat aan onderwijs is besteed",
        "€60 mln — de waarde van defensie, het goedkoopste alternatief"
      ],
      "answer": 0,
      "rationale": "Alternatieve kosten = waarde van het beste niet-gekozen alternatief. Zorg (€95 mln) is hoger dan wegen (€80 mln) en defensie (€60 mln). Dus €95 mln."
    },
    {
      "category": "procedure",
      "difficulty": 1,
      "q": "Wat is de eerste stap in de procedure voor economisch denken?",
      "options": [
        "Welke alternatieven zijn er?",
        "Wat zijn de alternatieve kosten?",
        "Wat is het beste alternatief?",
        "Hoeveel kost elke optie?"
      ],
      "answer": 0,
      "rationale": "De procedure begint met het in kaart brengen van alle beschikbare alternatieven. Daarna pas kijk je naar opbrengsten en alternatieve kosten."
    },
    {
      "category": "procedure",
      "difficulty": 2,
      "q": "Een boer moet kiezen tussen tarwe (€500/ha) en maïs (€350/ha) op 10 hectare. Welke stap volgt op 'Welke alternatieven zijn er?' in de procedure?",
      "options": [
        "Wat is de opbrengst van elk alternatief? (tarwe: €5.000; maïs: €3.500)",
        "Wat is de alternatieve kosten?",
        "Welk alternatief is het duurst?",
        "Hoeveel winst maakt de boer?"
      ],
      "answer": 0,
      "rationale": "Stap 2: bereken per alternatief de opbrengst. Pas daarna (stap 3) bepaal je wat je opgeeft — dat zijn de alternatieve kosten."
    },
    {
      "category": "procedure",
      "difficulty": 3,
      "q": "Je past de procedure toe. Alternatieven: A (€40), B (€30), C (€15). Je kiest A. Wat klopt?",
      "options": [
        "Nettowaarde = opbrengst A (€40) − alternatieve kosten (€30 van B) = €10",
        "Nettowaarde = €40 − €15 = €25",
        "Nettowaarde = €40 − (€30 + €15) = −€5",
        "Nettowaarde = €40 (alleen de opbrengst telt)"
      ],
      "answer": 0,
      "rationale": "Nettowaarde van de keuze = opbrengst gekozen alternatief − alternatieve kosten. Alternatieve kosten = het beste niet-gekozen alternatief (B: €30). €40 − €30 = €10."
    },
    {
      "category": "misconcepties",
      "difficulty": 2,
      "q": "Iemand zegt: 'Lucht is niet schaars, want er is overal genoeg.' Klopt dit economisch gezien?",
      "options": [
        "Ja — want er is genoeg lucht voor iedereen; behoeften ≤ middelen",
        "Nee — want alles kost geld",
        "Nee — schaarste geldt voor alle stoffen",
        "Ja — maar alleen buiten de stad"
      ],
      "answer": 0,
      "rationale": "Schaarste is geen kwestie van weinig-of-veel in absolute zin, maar van behoeften versus middelen. Lucht is ruim voldoende beschikbaar — dus niet schaars. (Schone lucht in een vervuilde stad kan wél schaars zijn.)"
    },
    {
      "category": "misconcepties",
      "difficulty": 2,
      "q": "Jan zegt: 'Ik koos de bioscoop (€12). Mijn alternatieve kosten zijn €12.' Wat klopt er niet?",
      "options": [
        "Alternatieve kosten ≠ prijs. De alternatieve kosten zijn de waarde van wat hij opgaf (bijvoorbeeld het boek van €15)",
        "Niks klopt er niet — alternatieve kosten zijn altijd gelijk aan de prijs",
        "Jan had €12 moeten aftrekken van €20",
        "Jan moet €12 + €15 bij elkaar optellen"
      ],
      "answer": 0,
      "rationale": "Alternatieve kosten zijn de opbrengst van het beste niet-gekozen alternatief — nooit gelijk aan de prijs die je betaalt. Dit is de meest gemaakte fout bij dit concept."
    },
    {
      "category": "misconcepties",
      "difficulty": 3,
      "q": "De stelling: 'De beste dingen in het leven zijn gratis' (zonlicht, frisse lucht, een wandeling). Wat zou een econoom antwoorden?",
      "options": [
        "Zelfs bij 'gratis' activiteiten geef je tijd op — de opbrengst van het best mogelijke alternatief is je alternatieve kosten",
        "Klopt — zonlicht is echt gratis en heeft geen kosten",
        "Niet relevant — economen kijken alleen naar geld",
        "Alleen als je werkt heb je alternatieve kosten"
      ],
      "answer": 0,
      "rationale": "Geldprijs = 0 betekent niet dat alternatieve kosten = 0. Tijd is ook een schaars middel: de wandeling van een uur kost je het beste alternatief dat je in dat uur had kunnen doen."
    }
  ]
};
