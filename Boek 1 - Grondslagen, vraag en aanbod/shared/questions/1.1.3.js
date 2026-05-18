var QUIZ_DATA = {
  "meta": {
    "parNr": "1.1.3",
    "parName": "Grafieken en tabellen",
    "subtitle": "Test of je tabellen, assen, grafieken en data-claims goed leest.",
    "testTopics": [
      "Tabelkoppen en eenheden herkennen",
      "Prijs en hoeveelheid op de juiste as zetten",
      "Waarden aflezen en interpoleren",
      "Misleidende grafieken herkennen"
    ]
  },
  "categories": {
    "tabel": {
      "name": "Tabellen",
      "colors": {
        "bg": "#E8F8F5",
        "text": "#0B5E5A",
        "bar": "#148F83"
      }
    },
    "grafiek": {
      "name": "Grafieken",
      "colors": {
        "bg": "#EBF5FB",
        "text": "#154360",
        "bar": "#1A5276"
      }
    },
    "interpolatie": {
      "name": "Interpoleren",
      "colors": {
        "bg": "#FEF5E7",
        "text": "#BA6A1C",
        "bar": "#E67E22"
      }
    },
    "kritisch": {
      "name": "Kritisch kijken",
      "colors": {
        "bg": "#F9EBEA",
        "text": "#922B21",
        "bar": "#C0392B"
      }
    }
  },
  "questions": [
    {
      "category": "tabel",
      "difficulty": 1,
      "q": "Waar kijk je eerst naar bij een tabel?",
      "options": [
        "Kolomkoppen en eenheden",
        "Alleen het grootste getal",
        "De kleur van de tabel",
        "De laatste rij"
      ],
      "answer": 0,
      "rationale": "De koppen en eenheden vertellen wat de getallen betekenen."
    },
    {
      "category": "grafiek",
      "difficulty": 1,
      "q": "Welke as gebruikt economie meestal voor prijs P?",
      "options": [
        "Verticale as",
        "Horizontale as",
        "Legenda",
        "Geen as"
      ],
      "answer": 0,
      "rationale": "In P-Q grafieken staat prijs op de verticale as."
    },
    {
      "category": "grafiek",
      "difficulty": 2,
      "q": "Een punt (300; 2,00) in een P-Q grafiek betekent:",
      "options": [
        "Q = 300 en P = 2,00",
        "P = 300 en Q = 2,00",
        "Index 300",
        "2 procent"
      ],
      "answer": 0,
      "rationale": "Hoeveelheid staat horizontaal, prijs verticaal."
    },
    {
      "category": "interpolatie",
      "difficulty": 2,
      "q": "Wat doe je bij interpoleren?",
      "options": [
        "Een waarde tussen twee bekende punten schatten",
        "Een waarde buiten de grafiek verzinnen",
        "Altijd afronden op nul",
        "De assen omdraaien"
      ],
      "answer": 0,
      "rationale": "Interpolatie ligt tussen bekende punten."
    },
    {
      "category": "kritisch",
      "difficulty": 2,
      "q": "Waarom kan een grafiek misleidend lijken?",
      "options": [
        "De as begint niet bij nul",
        "De titel staat bovenaan",
        "De tabel heeft rijen",
        "De lijn heeft punten"
      ],
      "answer": 0,
      "rationale": "Een ingezoomde as kan een klein verschil groot laten lijken."
    },
    {
      "category": "tabel",
      "difficulty": 3,
      "q": "Een claim vergelijkt 500 met 300. Welke basis gebruik je voor procentuele verandering?",
      "options": [
        "500",
        "300",
        "200",
        "800"
      ],
      "answer": 0,
      "rationale": "De oude waarde staat in de noemer."
    },
    {
      "category": "interpolatie",
      "difficulty": 3,
      "q": "Tussen 400 bij EUR 1,50 en 300 bij EUR 2,00 ligt EUR 1,75. Welke hoeveelheid past bij een rechte lijn?",
      "options": [
        "350",
        "375",
        "300",
        "400"
      ],
      "answer": 0,
      "rationale": "EUR 1,75 ligt precies in het midden, dus de hoeveelheid ook."
    },
    {
      "category": "kritisch",
      "difficulty": 3,
      "q": "Een kop zegt: verkoop daalt 50%. Wat moet je vragen?",
      "options": [
        "Tussen welke twee waarden wordt vergeleken?",
        "Welke kleur heeft de staaf?",
        "Is de titel kort genoeg?",
        "Wie tekende de lijn?"
      ],
      "answer": 0,
      "rationale": "Een percentage heeft altijd een vergelijkingsbasis nodig."
    },
    {
      "category": "grafiek",
      "difficulty": 3,
      "q": "Welke fout maakt een leerling die prijs P op de horizontale as zet in een P-Q grafiek?",
      "options": [
        "De economie-conventie wordt omgedraaid",
        "De tabel wordt automatisch fout",
        "De eenheid euro verdwijnt",
        "De lijn moet altijd stijgen"
      ],
      "answer": 0,
      "rationale": "In economie staat P verticaal en Q horizontaal."
    },
    {
      "category": "tabel",
      "difficulty": 2,
      "q": "Waarom schrijf je 'oud = 500 ijsjes' in plaats van alleen '500'?",
      "options": [
        "Het label maakt de berekening controleerbaar",
        "Het antwoord wordt dan altijd positief",
        "Je hoeft dan geen formule te gebruiken",
        "De grafiek wordt dan overbodig"
      ],
      "answer": 0,
      "rationale": "Een getal zonder label is moeilijk te controleren."
    }
  ]
};
