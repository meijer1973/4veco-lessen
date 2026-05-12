var NEWS_DETECTIVE_DATA = {
  "meta": {
    "parNr": "1.1.2",
    "parName": "Percentages en indexcijfers"
  },
  "article": {
    "headline": "Inflatie in april 2026 naar 2,8 procent bij snelle raming",
    "body": "Het CBS meldde dat de inflatie in april 2026 2,8 procent was bij de snelle raming. In maart was dat 2,7 procent. Ten opzichte van maart lagen consumentenprijzen in april 1,1 procent hoger. Vanaf 2026 gebruikt de CPI het basisjaar 2025 = 100.",
    "source": "CBS",
    "sourceDate": "30 april 2026",
    "sourceUrl": "https://www.cbs.nl/nl-nl/nieuws/2026/18/inflatie-in-april-2-8-procent-bij-snelle-raming",
    "visualAlt": "Staafdiagram met inflatie en productgroepen uit de snelle raming van april 2026"
  },
  "rounds": [
    {
      "type": "concept",
      "question": "Welk begrip heb je nodig om 2,8 procent inflatie te begrijpen?",
      "options": [
        {
          "text": "Procentuele verandering van de CPI ten opzichte van een jaar eerder",
          "correct": true,
          "feedback": "Juist. Inflatie is de procentuele verandering van de consumentenprijsindex ten opzichte van dezelfde maand een jaar eerder."
        },
        {
          "text": "Indexpunten tussen twee willekeurige maanden",
          "correct": false,
          "feedback": "Indexpunten kunnen nuttig zijn, maar inflatie wordt als procentuele verandering gepubliceerd."
        },
        {
          "text": "Alleen het absolute prijsverschil in euro's",
          "correct": false,
          "feedback": "Absolute verschillen zijn niet vergelijkbaar tussen producten. Daarom gebruiken economen percentages en indexcijfers."
        },
        {
          "text": "De gemiddelde temperatuur in april",
          "correct": false,
          "feedback": "Temperatuur kan prijzen beïnvloeden, maar inflatie gaat over prijsverandering in de consumentenprijsindex."
        }
      ]
    },
    {
      "type": "consequence",
      "question": "Zet de redenering in de juiste volgorde.",
      "chain": [
        {
          "text": "CBS meet prijzen van een pakket consumentengoederen en diensten",
          "position": 0
        },
        {
          "text": "Die prijzen worden samengevat in de consumentenprijsindex",
          "position": 1
        },
        {
          "text": "De procentuele verandering van de CPI geeft inflatie",
          "position": 2
        },
        {
          "text": "Leerlingen moeten basis, periode en percentage zorgvuldig onderscheiden",
          "position": 3
        }
      ],
      "distractors": [
        {
          "text": "Een hoger indexcijfer betekent altijd hetzelfde aantal procenten extra"
        },
        {
          "text": "Inflatie is het verschil in euro's tussen twee boodschappenmandjes"
        }
      ]
    },
    {
      "type": "model",
      "question": "Welke aanpak past bij de uitspraak: prijzen waren 1,1 procent hoger dan in maart?",
      "options": [
        {
          "id": "procentuele-verandering",
          "label": "Procentuele verandering berekenen",
          "description": "Je vergelijkt april met maart en deelt het verschil door de oude waarde.",
          "correct": true,
          "feedback": "Ja. De oude waarde is maart, de nieuwe waarde is april."
        },
        {
          "id": "basisjaar",
          "label": "Alleen een basisjaar kiezen",
          "description": "Je zet een indexreeks op maar rekent geen verandering uit.",
          "correct": false,
          "feedback": "Een basisjaar is nodig voor indexcijfers, maar deze zin vraagt om een procentuele verandering tussen twee maanden."
        },
        {
          "id": "procentpunt",
          "label": "Alleen procentpunten vergelijken",
          "description": "Je noemt het verschil tussen 2,7 procent en 2,8 procent.",
          "correct": false,
          "feedback": "Dat verschil is 0,1 procentpunt. De maand-op-maand prijsverandering vraagt om een aparte procentuele vergelijking."
        }
      ]
    },
    {
      "type": "error",
      "fakeAnalysis": "De inflatie steeg van 2,7 procent naar 2,8 procent. Dat betekent dat de prijzen in april 0,1 procent duurder werden dan in maart.",
      "errorPhrase": "0,1 procent duurder",
      "errorExplanation": "Het verschil tussen 2,7 procent en 2,8 procent is 0,1 procentpunt. De CBS-tekst noemt apart dat prijzen in april 1,1 procent hoger waren dan in maart. Procentpunten en procentuele prijsveranderingen zijn dus niet hetzelfde.",
      "distractorPhrases": [
        "2,7 procent",
        "2,8 procent",
        "in april"
      ]
    }
  ],
  "lesLink": "Gebruik de lesformules om het verschil tussen percentage, procentpunt en indexpunt scherp te houden."
};
