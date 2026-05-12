var QUIZ_DATA = {
  "meta": {
    "parNr": "1.1.2",
    "parName": "Percentages en indexcijfers",
    "subtitle": "Test of je percentages, indexcijfers en de indexpuntenvalkuil herkent.",
    "testTopics": [
      "Procentuele verandering berekenen",
      "Indexcijfers berekenen en interpreteren",
      "Indexpunten en procentuele verandering onderscheiden",
      "Veelgemaakte fouten met de basiswaarde"
    ]
  },
  "categories": {
    "procent": {
      "name": "Procentuele verandering",
      "colors": {
        "bg": "#E8F8F5",
        "text": "#0B5E5A",
        "bar": "#148F83"
      }
    },
    "index": {
      "name": "Indexcijfers",
      "colors": {
        "bg": "#EBF5FB",
        "text": "#154360",
        "bar": "#1A5276"
      }
    },
    "indexpunten": {
      "name": "Indexpunten",
      "colors": {
        "bg": "#FEF5E7",
        "text": "#BA6A1C",
        "bar": "#E67E22"
      }
    },
    "fouten": {
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
      "category": "procent",
      "difficulty": 1,
      "q": "Een prijs stijgt van EUR 600 naar EUR 648. Wat is de procentuele stijging?",
      "options": [
        "8%",
        "7,4%",
        "48%",
        "6%"
      ],
      "answer": 0,
      "rationale": "Het verschil is 48. Deel door de oude prijs: 48 / 600 x 100% = 8%."
    },
    {
      "category": "procent",
      "difficulty": 1,
      "q": "Welke waarde staat onder de breukstreep bij procentuele verandering?",
      "options": [
        "De oude waarde",
        "De nieuwe waarde",
        "Het verschil",
        "Het gemiddelde"
      ],
      "answer": 0,
      "rationale": "Je vergelijkt met het startpunt. Daarom deel je door de oude waarde."
    },
    {
      "category": "procent",
      "difficulty": 3,
      "q": "Een loon daalt van EUR 2.000 naar EUR 1.900. Wat is de procentuele verandering?",
      "options": [
        "-5%",
        "-10%",
        "5,3%",
        "-100%"
      ],
      "answer": 0,
      "rationale": "Het verschil is -100. -100 / 2000 x 100% = -5%."
    },
    {
      "category": "index",
      "difficulty": 1,
      "q": "Wat betekent index 100?",
      "options": [
        "Het basisjaar",
        "Een stijging van 100%",
        "Een daling van 0%",
        "Het duurste jaar"
      ],
      "answer": 0,
      "rationale": "Het basisjaar krijgt altijd index 100."
    },
    {
      "category": "index",
      "difficulty": 2,
      "q": "Een mandje kost EUR 120 in het basisjaar en EUR 150 later. Wat is het indexcijfer?",
      "options": [
        "125",
        "80",
        "25",
        "120"
      ],
      "answer": 0,
      "rationale": "150 / 120 x 100 = 125."
    },
    {
      "category": "index",
      "difficulty": 3,
      "q": "Wat betekent index 80?",
      "options": [
        "20% lager dan het basisjaar",
        "80% lager dan het basisjaar",
        "80 euro",
        "20 indexpunten hoger"
      ],
      "answer": 0,
      "rationale": "Index 80 ligt 20 onder 100, dus 20% lager dan het basisjaar."
    },
    {
      "category": "indexpunten",
      "difficulty": 2,
      "q": "Een index stijgt van 125 naar 135. Hoeveel indexpunten is dat?",
      "options": [
        "10 indexpunten",
        "8 indexpunten",
        "10%",
        "8%"
      ],
      "answer": 0,
      "rationale": "135 - 125 = 10 indexpunten."
    },
    {
      "category": "indexpunten",
      "difficulty": 3,
      "q": "Een index stijgt van 125 naar 135. Wat is de procentuele verandering?",
      "options": [
        "8%",
        "10%",
        "7,4%",
        "35%"
      ],
      "answer": 0,
      "rationale": "10 / 125 x 100% = 8%."
    },
    {
      "category": "indexpunten",
      "difficulty": 2,
      "q": "Wanneer zijn indexpunten en procenten toevallig gelijk?",
      "options": [
        "Als het oude indexcijfer 100 is",
        "Altijd",
        "Als het nieuwe indexcijfer 100 is",
        "Nooit"
      ],
      "answer": 0,
      "rationale": "Bij oud = 100 geldt verschil / 100 x 100%, dus het puntenverschil is dan gelijk aan procenten."
    },
    {
      "category": "fouten",
      "difficulty": 2,
      "q": "Een leerling deelt bij 200 naar 250 door 250. Wat gaat fout?",
      "options": [
        "De leerling gebruikt de nieuwe waarde als basis",
        "De leerling vergeet het verschil",
        "De leerling berekent indexpunten",
        "De leerling rondt te vroeg af"
      ],
      "answer": 0,
      "rationale": "Bij procentuele verandering deel je door de oude waarde."
    },
    {
      "category": "fouten",
      "difficulty": 3,
      "q": "Inflatie stijgt van 2,7% naar 2,8%. Welke uitspraak is het preciesst?",
      "options": [
        "De inflatie stijgt met 0,1 procentpunt",
        "De prijzen stijgen met 0,1%",
        "De inflatie verdubbelt bijna",
        "De index stijgt met 2,8 punten"
      ],
      "answer": 0,
      "rationale": "Bij percentages naast elkaar spreek je hier over procentpunten."
    },
    {
      "category": "fouten",
      "difficulty": 2,
      "q": "Een index van 112 betekent:",
      "options": [
        "12% hoger dan het basisjaar",
        "112% hoger dan het basisjaar",
        "12 euro duurder",
        "112 indexpunten hoger dan het vorige jaar"
      ],
      "answer": 0,
      "rationale": "Het basisjaar is 100. 112 is 12% hoger dan de basis."
    }
  ]
};
