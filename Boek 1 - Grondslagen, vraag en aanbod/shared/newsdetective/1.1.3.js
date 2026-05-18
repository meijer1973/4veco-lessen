var NEWS_DETECTIVE_DATA = {
  "meta": {
    "parNr": "1.1.3",
    "parName": "Grafieken en tabellen"
  },
  "article": {
    "headline": "Grafiek laat kleine daling groot lijken",
    "body": "Een winkelketen toont twee weken verkoopcijfers. Week 1 heeft 520 verkopen en week 2 heeft 500 verkopen. De grafiek begint op 490, waardoor de daling veel groter lijkt dan in een grafiek die bij nul begint.",
    "source": "Oefenbron",
    "sourceDate": "fictieve lessituatie",
    "sourceUrl": "https://example.com/oefenbron-grafieken",
    "visualAlt": "Twee staafgrafieken met dezelfde data maar verschillende verticale schaal"
  },
  "rounds": [
    {
      "type": "concept",
      "question": "Welke controle is hier het belangrijkst?",
      "options": [
        {
          "text": "Controleren waar de verticale as begint",
          "correct": true,
          "feedback": "Juist. De schaal bepaalt hoe groot het verschil lijkt."
        },
        {
          "text": "Alleen kijken welke staaf hoger is",
          "correct": false,
          "feedback": "Dat is te snel; kijk eerst naar de schaal."
        },
        {
          "text": "De grafiek negeren",
          "correct": false,
          "feedback": "Grafieken zijn nuttig, maar je moet ze kritisch lezen."
        },
        {
          "text": "Alleen de kleur van de staaf vergelijken",
          "correct": false,
          "feedback": "Kleur kan helpen, maar de schaal en eenheid bepalen de betekenis."
        }
      ]
    },
    {
      "type": "consequence",
      "question": "Zet de controle in de juiste volgorde.",
      "chain": [
        {
          "text": "Lees de titel en bron",
          "position": 0
        },
        {
          "text": "Controleer de as en eenheid",
          "position": 1
        },
        {
          "text": "Lees de waarden af",
          "position": 2
        },
        {
          "text": "Beoordeel of de kop bij de data past",
          "position": 3
        }
      ],
      "distractors": [
        {
          "text": "Begin met het percentage gokken"
        },
        {
          "text": "Kijk alleen naar de langste staaf"
        }
      ]
    },
    {
      "type": "model",
      "question": "Welke aanpak past bij 520 naar 500?",
      "options": [
        {
          "id": "procentuele-verandering",
          "label": "Procentuele verandering berekenen",
          "description": "Je vergelijkt nieuw met oud.",
          "correct": true,
          "feedback": "Ja. Het verschil is -20 en de basis is 520."
        },
        {
          "id": "assen-omdraaien",
          "label": "Assen omdraaien",
          "description": "Je wisselt x en y.",
          "correct": false,
          "feedback": "Dat lost de claim niet op."
        },
        {
          "id": "alleen-aflezen",
          "label": "Alleen de hoogste waarde noemen",
          "description": "Je noemt alleen week 1.",
          "correct": false,
          "feedback": "Je moet vergelijken."
        }
      ]
    },
    {
      "type": "error",
      "fakeAnalysis": "De grafiek begint bij 490, dus de verkoop is bijna helemaal ingestort.",
      "errorPhrase": "bijna helemaal ingestort",
      "errorExplanation": "De verkoop daalt van 520 naar 500. Dat is 20 minder, dus ongeveer 3,8% daling. De ingezoomde as maakt het beeld dramatischer dan de data.",
      "distractorPhrases": [
        "begint bij 490",
        "verkoop",
        "grafiek"
      ]
    }
  ],
  "lesLink": "Gebruik de grafiekcheck: titel, as, eenheid, waarde, conclusie."
};
