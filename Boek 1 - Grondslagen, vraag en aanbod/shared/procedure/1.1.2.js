var PROCEDURE_DATA = {
  "meta": {
    "parNr": "1.1.2",
    "parName": "Percentages en indexcijfers"
  },
  "procedures": [
    {
      "id": "procentuele-verandering",
      "title": "Procentuele verandering berekenen",
      "icon": "fa-percent",
      "description": "Bereken hoeveel een waarde stijgt of daalt ten opzichte van de oude waarde.",
      "steps": [
        {
          "type": "given",
          "label": "Gegeven",
          "text": "Een oude waarde en een nieuwe waarde."
        },
        {
          "type": "choose",
          "label": "Stap 1",
          "options": [
            {
              "text": "Bepaal de oude waarde en de nieuwe waarde",
              "correct": true
            },
            {
              "text": "Begin met de nieuwe waarde als basis",
              "correct": false,
              "feedback": "Dit verandert de basis van de berekening en levert een verkeerd antwoord op."
            },
            {
              "text": "Tel oud en nieuw bij elkaar op",
              "correct": false,
              "feedback": "Deze stap klinkt logisch, maar past niet bij deze procedure."
            }
          ]
        },
        {
          "type": "choose",
          "label": "Stap 2",
          "options": [
            {
              "text": "Bereken het verschil: nieuw min oud",
              "correct": true
            },
            {
              "text": "Deel nieuw direct door oud",
              "correct": false,
              "feedback": "Dit verandert de basis van de berekening en levert een verkeerd antwoord op."
            },
            {
              "text": "Gebruik alleen het hoogste getal",
              "correct": false,
              "feedback": "Deze stap klinkt logisch, maar past niet bij deze procedure."
            }
          ]
        },
        {
          "type": "choose",
          "label": "Stap 3",
          "options": [
            {
              "text": "Deel het verschil door de oude waarde en vermenigvuldig met 100",
              "correct": true
            },
            {
              "text": "Deel door de nieuwe waarde",
              "correct": false,
              "feedback": "Dit verandert de basis van de berekening en levert een verkeerd antwoord op."
            },
            {
              "text": "Laat x 100 weg",
              "correct": false,
              "feedback": "Deze stap klinkt logisch, maar past niet bij deze procedure."
            }
          ]
        },
        {
          "type": "choose",
          "label": "Stap 4",
          "options": [
            {
              "text": "Benoem stijging of daling op basis van het teken",
              "correct": true
            },
            {
              "text": "Rond altijd af naar een positief getal",
              "correct": false,
              "feedback": "Dit verandert de basis van de berekening en levert een verkeerd antwoord op."
            },
            {
              "text": "Noem elk verschil indexpunten",
              "correct": false,
              "feedback": "Deze stap klinkt logisch, maar past niet bij deze procedure."
            }
          ]
        },
        {
          "type": "given",
          "label": "Resultaat",
          "text": "Je hebt de procentuele stijging of daling berekend."
        }
      ]
    },
    {
      "id": "indexcijfer",
      "title": "Indexcijfer berekenen",
      "icon": "fa-chart-line",
      "description": "Zet een waarde om naar een index met basisjaar 100.",
      "steps": [
        {
          "type": "given",
          "label": "Gegeven",
          "text": "Een basisjaar en een waarde in een doeljaar."
        },
        {
          "type": "choose",
          "label": "Stap 1",
          "options": [
            {
              "text": "Kies het basisjaar en geef dit index 100",
              "correct": true
            },
            {
              "text": "Kies automatisch het hoogste jaar",
              "correct": false,
              "feedback": "Dit verandert de basis van de berekening en levert een verkeerd antwoord op."
            },
            {
              "text": "Kies het jaar met de hoogste prijs",
              "correct": false,
              "feedback": "Deze stap klinkt logisch, maar past niet bij deze procedure."
            }
          ]
        },
        {
          "type": "choose",
          "label": "Stap 2",
          "options": [
            {
              "text": "Bepaal de waarde in het doeljaar",
              "correct": true
            },
            {
              "text": "Gebruik het gemiddelde van alle jaren",
              "correct": false,
              "feedback": "Dit verandert de basis van de berekening en levert een verkeerd antwoord op."
            },
            {
              "text": "Gebruik alleen het verschil in euro's",
              "correct": false,
              "feedback": "Deze stap klinkt logisch, maar past niet bij deze procedure."
            }
          ]
        },
        {
          "type": "choose",
          "label": "Stap 3",
          "options": [
            {
              "text": "Deel de doeljaarwaarde door de basisjaarwaarde en vermenigvuldig met 100",
              "correct": true
            },
            {
              "text": "Deel de basis door het doeljaar",
              "correct": false,
              "feedback": "Dit verandert de basis van de berekening en levert een verkeerd antwoord op."
            },
            {
              "text": "Trek 100 af voordat je deelt",
              "correct": false,
              "feedback": "Deze stap klinkt logisch, maar past niet bij deze procedure."
            }
          ]
        },
        {
          "type": "choose",
          "label": "Stap 4",
          "options": [
            {
              "text": "Interpreteer het indexcijfer ten opzichte van 100",
              "correct": true
            },
            {
              "text": "Lees het indexcijfer als eurobedrag",
              "correct": false,
              "feedback": "Dit verandert de basis van de berekening en levert een verkeerd antwoord op."
            },
            {
              "text": "Noem elk indexcijfer automatisch inflatie",
              "correct": false,
              "feedback": "Deze stap klinkt logisch, maar past niet bij deze procedure."
            }
          ]
        },
        {
          "type": "given",
          "label": "Resultaat",
          "text": "Je ziet hoeveel hoger of lager de waarde is dan in het basisjaar."
        }
      ]
    },
    {
      "id": "indexpunten-procenten",
      "title": "Indexpunten en procenten onderscheiden",
      "icon": "fa-not-equal",
      "description": "Voorkom dat je indexpunten verwart met procentuele verandering.",
      "steps": [
        {
          "type": "given",
          "label": "Gegeven",
          "text": "Een oud indexcijfer en een nieuw indexcijfer."
        },
        {
          "type": "choose",
          "label": "Stap 1",
          "options": [
            {
              "text": "Bepaal het oude indexcijfer",
              "correct": true
            },
            {
              "text": "Begin met index 100, ook als dat niet het oude jaar is",
              "correct": false,
              "feedback": "Dit verandert de basis van de berekening en levert een verkeerd antwoord op."
            },
            {
              "text": "Gebruik het hoogste indexcijfer",
              "correct": false,
              "feedback": "Deze stap klinkt logisch, maar past niet bij deze procedure."
            }
          ]
        },
        {
          "type": "choose",
          "label": "Stap 2",
          "options": [
            {
              "text": "Bepaal het nieuwe indexcijfer",
              "correct": true
            },
            {
              "text": "Gebruik het basisjaar in plaats van het nieuwe jaar",
              "correct": false,
              "feedback": "Dit verandert de basis van de berekening en levert een verkeerd antwoord op."
            },
            {
              "text": "Gebruik het gemiddelde van beide indexcijfers",
              "correct": false,
              "feedback": "Deze stap klinkt logisch, maar past niet bij deze procedure."
            }
          ]
        },
        {
          "type": "choose",
          "label": "Stap 3",
          "options": [
            {
              "text": "Bereken het verschil in indexpunten",
              "correct": true
            },
            {
              "text": "Noem dit verschil meteen procenten",
              "correct": false,
              "feedback": "Dit verandert de basis van de berekening en levert een verkeerd antwoord op."
            },
            {
              "text": "Deel eerst door 100",
              "correct": false,
              "feedback": "Deze stap klinkt logisch, maar past niet bij deze procedure."
            }
          ]
        },
        {
          "type": "choose",
          "label": "Stap 4",
          "options": [
            {
              "text": "Deel door het oude indexcijfer, vermenigvuldig met 100 en benoem beide eenheden apart",
              "correct": true
            },
            {
              "text": "Deel door het nieuwe indexcijfer",
              "correct": false,
              "feedback": "Dit verandert de basis van de berekening en levert een verkeerd antwoord op."
            },
            {
              "text": "Schrijf indexpunten met een procentteken",
              "correct": false,
              "feedback": "Deze stap klinkt logisch, maar past niet bij deze procedure."
            }
          ]
        },
        {
          "type": "given",
          "label": "Resultaat",
          "text": "Je kunt uitleggen waarom 125 naar 135 gelijk is aan 10 indexpunten maar 8 procent."
        }
      ]
    }
  ]
};
