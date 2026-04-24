var QUIZ_DATA = {
  "meta": {
    "parNr": "1.1.2",
    "parName": "Percentages en indexcijfers",
    "subtitle": "Oefen met procentuele verandering, indexcijfers en de valkuil indexpunten versus procenten.",
    "testTopics": [
      "Procentuele verandering berekenen",
      "Indexcijfers berekenen",
      "Indexpunten en procenten uit elkaar houden",
      "Inflatie interpreteren"
    ]
  },
  "categories": {
    "procent": {
      "name": "Procentuele verandering",
      "colors": {
        "bg": "#EBF5FB",
        "text": "#154360",
        "bar": "#1A5276"
      }
    },
    "index": {
      "name": "Indexcijfers",
      "colors": {
        "bg": "#E8F8F5",
        "text": "#0B5E5A",
        "bar": "#148F83"
      }
    },
    "valkuil": {
      "name": "Indexpunten vs procenten",
      "colors": {
        "bg": "#F9EBEA",
        "text": "#922B21",
        "bar": "#C0392B"
      }
    },
    "inflatie": {
      "name": "Inflatie toepassen",
      "colors": {
        "bg": "#FEF5E7",
        "text": "#BA6A1C",
        "bar": "#E67E22"
      }
    }
  },
  "questions": [
    {
      "category": "procent",
      "difficulty": 1,
      "q": "Een jas stijgt van EUR 80 naar EUR 88. Wat is de procentuele stijging?",
      "options": [
        "10%",
        "8%",
        "11%",
        "12,5%"
      ],
      "answer": 0,
      "rationale": "(88 - 80) / 80 x 100% = 10%. Je deelt door de oude waarde."
    },
    {
      "category": "procent",
      "difficulty": 1,
      "q": "Welke waarde staat in de noemer bij procentuele verandering?",
      "options": [
        "De oude waarde",
        "De nieuwe waarde",
        "Het verschil",
        "Het gemiddelde"
      ],
      "answer": 0,
      "rationale": "Je meet de verandering ten opzichte van waar je vandaan komt: de oude waarde."
    },
    {
      "category": "procent",
      "difficulty": 3,
      "q": "Een prijs daalt van EUR 250 naar EUR 200. Wat is de procentuele verandering?",
      "options": [
        "-20%",
        "-25%",
        "20%",
        "25%"
      ],
      "answer": 0,
      "rationale": "(200 - 250) / 250 x 100% = -20%. Het minteken betekent daling."
    },
    {
      "category": "index",
      "difficulty": 1,
      "q": "Wat is het indexcijfer van het basisjaar?",
      "options": [
        "100",
        "0",
        "1",
        "Het prijsniveau in euro"
      ],
      "answer": 0,
      "rationale": "Het basisjaar krijgt altijd index 100."
    },
    {
      "category": "index",
      "difficulty": 2,
      "q": "Een product kost in het basisjaar EUR 40 en later EUR 50. Wat is het indexcijfer?",
      "options": [
        "125",
        "80",
        "110",
        "25"
      ],
      "answer": 0,
      "rationale": "50 / 40 x 100 = 125."
    },
    {
      "category": "index",
      "difficulty": 3,
      "q": "Een indexcijfer is 96. Wat betekent dat ten opzichte van het basisjaar?",
      "options": [
        "De waarde is 4% lager dan in het basisjaar",
        "De waarde is 96% lager",
        "De waarde is 96 euro",
        "De waarde is 4 indexpunten hoger"
      ],
      "answer": 0,
      "rationale": "Onder 100 betekent lager dan het basisjaar. 96 is 4% onder 100."
    },
    {
      "category": "valkuil",
      "difficulty": 1,
      "q": "Een index stijgt van 120 naar 130. Hoeveel indexpunten is de stijging?",
      "options": [
        "10 indexpunten",
        "10%",
        "8,3 indexpunten",
        "30 indexpunten"
      ],
      "answer": 0,
      "rationale": "Het verschil in indexcijfers is 130 - 120 = 10 indexpunten."
    },
    {
      "category": "valkuil",
      "difficulty": 2,
      "q": "Een index stijgt van 120 naar 130. Wat is de procentuele stijging?",
      "options": [
        "8,3%",
        "10%",
        "30%",
        "120%"
      ],
      "answer": 0,
      "rationale": "(130 - 120) / 120 x 100% = 8,3%. Indexpunten zijn geen procenten."
    },
    {
      "category": "valkuil",
      "difficulty": 3,
      "q": "Wanneer is een stijging van 10 indexpunten ook precies 10%?",
      "options": [
        "Als het oude indexcijfer 100 is",
        "Altijd",
        "Als het nieuwe indexcijfer 100 is",
        "Nooit"
      ],
      "answer": 0,
      "rationale": "Alleen vanaf 100 geldt: 10 / 100 x 100% = 10%."
    },
    {
      "category": "inflatie",
      "difficulty": 1,
      "q": "Wat betekent inflatie van 2,7%?",
      "options": [
        "Het algemeen prijspeil is gemiddeld 2,7% hoger dan een jaar eerder",
        "Alle producten zijn exact 2,7% duurder",
        "Het indexcijfer is altijd 2,7",
        "De koopkracht stijgt met 2,7%"
      ],
      "answer": 0,
      "rationale": "Inflatie is een gemiddelde procentuele stijging van het prijspeil."
    },
    {
      "category": "inflatie",
      "difficulty": 2,
      "q": "Als prijzen 12% hoger liggen dan het basisjaar, welk indexcijfer hoort daarbij?",
      "options": [
        "112",
        "12",
        "88",
        "120"
      ],
      "answer": 0,
      "rationale": "Basisjaar 100 plus 12% stijging geeft index 112."
    },
    {
      "category": "inflatie",
      "difficulty": 3,
      "q": "Waarom kan jouw persoonlijke inflatie anders voelen dan het CBS-cijfer?",
      "options": [
        "Omdat het CBS een gemiddeld mandje gebruikt en jouw uitgavenpatroon kan afwijken",
        "Omdat indexcijfers geen percentages zijn",
        "Omdat inflatie alleen over benzine gaat",
        "Omdat prijzen nooit dalen"
      ],
      "answer": 0,
      "rationale": "Inflatie is gebaseerd op een gemiddeld pakket goederen en diensten. Jouw eigen mandje kan anders zijn."
    }
  ]
};
