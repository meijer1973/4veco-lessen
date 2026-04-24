var NEWS_DETECTIVE_DATA = {
  "meta": {
    "parNr": "1.1.2",
    "parName": "Percentages en indexcijfers"
  },
  "article": {
    "headline": "CBS: inflatie in maart 2026 is 2,7 procent",
    "body": "Het CBS meldt dat consumentengoederen en -diensten in maart 2026 gemiddeld 2,7 procent duurder waren dan een jaar eerder. Zo een inflatiecijfer is een procentuele verandering van het algemene prijspeil. Om zulke prijsontwikkelingen door de tijd te vergelijken gebruikt het CBS indexcijfers: een basisjaar krijgt waarde 100 en latere waarden worden daaraan gerelateerd.",
    "source": "CBS",
    "sourceDate": "2026-04",
    "sourceUrl": "https://www.cbs.nl/nl-nl/nieuws/2026/15/inflatie-in-maart-2-7-procent",
    "visualAlt": "Indexgrafiek waarin een basisjaar 100 is en latere prijzen hoger liggen"
  },
  "rounds": [
    {
      "type": "concept",
      "question": "Welk begrip helpt het meest om het CBS-inflatiecijfer te begrijpen?",
      "options": [
        {
          "text": "Procentuele verandering: prijzen zijn gemiddeld 2,7% hoger dan een jaar eerder",
          "correct": true,
          "feedback": "Juist. Inflatie is een procentuele stijging van een prijsniveau ten opzichte van een eerdere periode."
        },
        {
          "text": "Alternatieve kosten: huishoudens geven andere aankopen op",
          "correct": false,
          "feedback": "Dat kan een gevolg zijn, maar het cijfer zelf is een procentuele prijsverandering."
        },
        {
          "text": "Indexpunten: inflatie is altijd het verschil tussen twee indexcijfers",
          "correct": false,
          "feedback": "Indexpunten kunnen helpen, maar de claim 2,7% is al een procentuele verandering."
        },
        {
          "text": "Schaarste: er zijn te weinig producten",
          "correct": false,
          "feedback": "Schaarste kan prijzen beinvloeden, maar dit nieuws gaat over meten met procenten en indexcijfers."
        }
      ]
    },
    {
      "type": "consequence",
      "question": "Zet de meetketen in de juiste volgorde.",
      "chain": [
        {
          "text": "CBS meet prijzen van een pakket consumentengoederen en diensten",
          "position": 0
        },
        {
          "text": "Die prijzen worden vergeleken met een eerdere periode of basiswaarde",
          "position": 1
        },
        {
          "text": "De verandering wordt uitgedrukt als percentage of indexcijfer",
          "position": 2
        },
        {
          "text": "Leerlingen moeten het verschil tussen indexpunten en procenten bewaken",
          "position": 3
        }
      ],
      "distractors": [
        {
          "text": "Elke winkelprijs stijgt met exact hetzelfde percentage"
        },
        {
          "text": "Het basisjaar krijgt index 0"
        }
      ]
    },
    {
      "type": "model",
      "question": "Welk rekenmodel past bij een prijs van 100 naar 102,7?",
      "options": [
        {
          "id": "procentuele-verandering",
          "label": "Procentuele verandering",
          "description": "(nieuw - oud) / oud x 100% = (102,7 - 100) / 100 x 100% = 2,7%",
          "correct": true,
          "feedback": "Juist. De oude waarde staat in de noemer."
        },
        {
          "id": "absolute-verandering",
          "label": "Absolute verandering",
          "description": "Nieuw - oud = 2,7 punten",
          "correct": false,
          "feedback": "Dit geeft alleen het verschil in punten, niet de procentuele verandering."
        },
        {
          "id": "alternatieve-kosten",
          "label": "Alternatieve kosten",
          "description": "De waarde van het beste niet-gekozen alternatief",
          "correct": false,
          "feedback": "Dat is een ander concept uit 1.1.1."
        }
      ]
    },
    {
      "type": "error",
      "fakeAnalysis": "Een leerling schrijft: \"De inflatie is 2,7 indexpunten, dus de prijzen zijn 2,7 euro duurder. Het maakt niet uit welk basisjaar het CBS gebruikt, want indexpunten en procenten zijn hetzelfde.\"",
      "errorPhrase": "indexpunten en procenten zijn hetzelfde",
      "errorExplanation": "De fout is dat indexpunten en procenten door elkaar worden gehaald. Een verschil in indexcijfers is een aantal indexpunten. Een procentuele verandering bereken je door het verschil te delen door de oude waarde of het oude indexcijfer.",
      "distractorPhrases": [
        "2,7 euro duurder",
        "welk basisjaar het CBS gebruikt",
        "2,7 indexpunten"
      ]
    }
  ],
  "lesLink": "Dit nieuws komt terug bij indexcijfers, inflatie en het verschil tussen indexpunten en procentuele verandering."
};
