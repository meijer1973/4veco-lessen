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
      "description": "Bereken in drie stappen een stijging of daling in procenten.",
      "steps": [
        {
          "type": "given",
          "label": "Gegeven",
          "text": "Een oude waarde en een nieuwe waarde, bijvoorbeeld een prijs van EUR 600 naar EUR 648."
        },
        {
          "type": "choose",
          "label": "Stap 1",
          "options": [
            {
              "text": "Noteer de oude waarde en de nieuwe waarde",
              "correct": true
            },
            {
              "text": "Tel oude en nieuwe waarde bij elkaar op",
              "correct": false,
              "feedback": "Je vergelijkt twee waarden; optellen helpt niet om de verandering te meten."
            },
            {
              "text": "Kies de hoogste waarde als noemer",
              "correct": false,
              "feedback": "De noemer is altijd de oude waarde, niet automatisch de hoogste."
            }
          ]
        },
        {
          "type": "choose",
          "label": "Stap 2",
          "options": [
            {
              "text": "Bereken (nieuw - oud) / oud x 100%",
              "correct": true
            },
            {
              "text": "Bereken (nieuw - oud) / nieuw x 100%",
              "correct": false,
              "feedback": "Dit is de klassieke fout: deel door de oude waarde."
            },
            {
              "text": "Bereken nieuw / oud zonder x 100%",
              "correct": false,
              "feedback": "Dan krijg je een verhouding, geen procentuele verandering."
            }
          ]
        },
        {
          "type": "choose",
          "label": "Stap 3",
          "options": [
            {
              "text": "Interpreteer het teken: positief is stijging, negatief is daling",
              "correct": true
            },
            {
              "text": "Maak elke uitkomst positief",
              "correct": false,
              "feedback": "Een minteken is betekenisvol: het geeft een daling aan."
            },
            {
              "text": "Rond altijd af op hele tientallen",
              "correct": false,
              "feedback": "Rond alleen af als de opdracht daarom vraagt."
            }
          ]
        },
        {
          "type": "given",
          "label": "Resultaat",
          "text": "Je hebt de procentuele stijging of daling berekend ten opzichte van de oude waarde."
        }
      ]
    },
    {
      "id": "indexcijfer",
      "title": "Indexcijfer berekenen",
      "icon": "fa-chart-line",
      "description": "Zet een waarde om naar een indexcijfer met basisjaar 100.",
      "steps": [
        {
          "type": "given",
          "label": "Gegeven",
          "text": "Een basiswaarde en een waarde in een ander jaar."
        },
        {
          "type": "choose",
          "label": "Stap 1",
          "options": [
            {
              "text": "Bepaal het basisjaar en zet dat op index 100",
              "correct": true
            },
            {
              "text": "Kies het hoogste jaar als basisjaar",
              "correct": false,
              "feedback": "Het basisjaar staat in de opdracht of wordt bewust gekozen."
            },
            {
              "text": "Zet het eerste getal op index 0",
              "correct": false,
              "feedback": "Een indexreeks gebruikt 100 voor het basisjaar."
            }
          ]
        },
        {
          "type": "choose",
          "label": "Stap 2",
          "options": [
            {
              "text": "Bereken waarde / basiswaarde x 100",
              "correct": true
            },
            {
              "text": "Bereken basiswaarde / waarde x 100",
              "correct": false,
              "feedback": "Dan draai je de verhouding om."
            },
            {
              "text": "Bereken waarde - basiswaarde",
              "correct": false,
              "feedback": "Dat is een absoluut verschil, geen indexcijfer."
            }
          ]
        },
        {
          "type": "choose",
          "label": "Stap 3",
          "options": [
            {
              "text": "Interpreteer: boven 100 is hoger, onder 100 is lager dan het basisjaar",
              "correct": true
            },
            {
              "text": "Interpreteer elk indexcijfer als eurobedrag",
              "correct": false,
              "feedback": "Een indexcijfer is een verhoudingsgetal, geen eurobedrag."
            },
            {
              "text": "Noem elk verschil tussen indexcijfers een procent",
              "correct": false,
              "feedback": "Dat verschil heet indexpunten."
            }
          ]
        },
        {
          "type": "given",
          "label": "Resultaat",
          "text": "Je hebt de waarde vergeleken met het basisjaar."
        }
      ]
    }
  ]
};
