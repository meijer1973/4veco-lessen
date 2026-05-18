var PROCEDURE_DATA = {
  "meta": {
    "parNr": "1.1.3",
    "parName": "Grafieken en tabellen"
  },
  "procedures": [
    {
      "id": "tabelwaarden-selecteren",
      "title": "Tabelwaarden selecteren voor een berekening",
      "icon": "fa-table",
      "description": "Kies de juiste bronwaarden voordat je met procenten, indexcijfers of grafieken rekent.",
      "procedure_template_id": "select_table_values_trace",
      "steps": [
        {
          "type": "given",
          "label": "Gegeven",
          "text": "Een vraag met een tabel of bron."
        },
        {
          "type": "choose",
          "label": "Stap 1",
          "formal_step_id": "read_question_target",
          "options": [
            {
              "text": "Lees de vraag en bepaal welke grootheid, periode, rij of kolom nodig is",
              "correct": true
            },
            {
              "text": "Pak het eerste getal dat je ziet",
              "correct": false,
              "feedback": "Deze stap klinkt snel, maar je mist dan bron, label of eenheid."
            },
            {
              "text": "Begin direct met procenten rekenen",
              "correct": false,
              "feedback": "Deze stap klinkt snel, maar je mist dan bron, label of eenheid."
            }
          ]
        },
        {
          "type": "choose",
          "label": "Stap 2",
          "formal_step_id": "check_table_headers_units",
          "options": [
            {
              "text": "Controleer bron, tabelkop, rijlabel, kolomlabel en eenheid",
              "correct": true
            },
            {
              "text": "Negeer de eenheid als het getal duidelijk is",
              "correct": false,
              "feedback": "Deze stap klinkt snel, maar je mist dan bron, label of eenheid."
            },
            {
              "text": "Gebruik alleen de tabeltitel",
              "correct": false,
              "feedback": "Deze stap klinkt snel, maar je mist dan bron, label of eenheid."
            }
          ]
        },
        {
          "type": "choose",
          "label": "Stap 3",
          "formal_step_id": "select_needed_values",
          "options": [
            {
              "text": "Selecteer de oude waarde, nieuwe waarde of gevraagde waarde voordat je rekent",
              "correct": true
            },
            {
              "text": "Selecteer alle waarden in de tabel",
              "correct": false,
              "feedback": "Deze stap klinkt snel, maar je mist dan bron, label of eenheid."
            },
            {
              "text": "Kies altijd de grootste waarde",
              "correct": false,
              "feedback": "Deze stap klinkt snel, maar je mist dan bron, label of eenheid."
            }
          ]
        },
        {
          "type": "choose",
          "label": "Stap 4",
          "formal_step_id": "label_selected_values",
          "options": [
            {
              "text": "Noteer de gekozen waarden met label zodat de berekening controleerbaar is",
              "correct": true
            },
            {
              "text": "Schrijf alleen het eindantwoord op",
              "correct": false,
              "feedback": "Deze stap klinkt snel, maar je mist dan bron, label of eenheid."
            },
            {
              "text": "Laat de labels weg om sneller te werken",
              "correct": false,
              "feedback": "Deze stap klinkt snel, maar je mist dan bron, label of eenheid."
            }
          ]
        },
        {
          "type": "given",
          "label": "Resultaat",
          "text": "Je hebt controleerbare bronwaarden voor je berekening."
        }
      ]
    },
    {
      "id": "grafiek-aflezen",
      "title": "Waarden aflezen uit een grafiek",
      "icon": "fa-chart-line",
      "description": "Lees een waarde af door titel, assen, schaal en eenheid te controleren.",
      "steps": [
        {
          "type": "given",
          "label": "Gegeven",
          "text": "Een economische grafiek en een gevraagde waarde."
        },
        {
          "type": "choose",
          "label": "Stap 1",
          "formal_step_id": "read_graph_title_axes",
          "options": [
            {
              "text": "Lees titel, assen en eenheden",
              "correct": true
            },
            {
              "text": "Begin bij het hoogste punt",
              "correct": false,
              "feedback": "Deze stap klinkt snel, maar je mist dan bron, label of eenheid."
            },
            {
              "text": "Negeer de aslabels",
              "correct": false,
              "feedback": "Deze stap klinkt snel, maar je mist dan bron, label of eenheid."
            }
          ]
        },
        {
          "type": "choose",
          "label": "Stap 2",
          "formal_step_id": "find_requested_value",
          "options": [
            {
              "text": "Zoek de gevraagde waarde op de juiste as",
              "correct": true
            },
            {
              "text": "Zoek de waarde op een willekeurige as",
              "correct": false,
              "feedback": "Deze stap klinkt snel, maar je mist dan bron, label of eenheid."
            },
            {
              "text": "Gebruik de legenda als antwoord",
              "correct": false,
              "feedback": "Deze stap klinkt snel, maar je mist dan bron, label of eenheid."
            }
          ]
        },
        {
          "type": "choose",
          "label": "Stap 3",
          "formal_step_id": "trace_to_graph",
          "options": [
            {
              "text": "Trek denkbeeldig een lijn naar de grafiek en naar de andere as",
              "correct": true
            },
            {
              "text": "Schat zonder naar de schaal te kijken",
              "correct": false,
              "feedback": "Deze stap klinkt snel, maar je mist dan bron, label of eenheid."
            },
            {
              "text": "Draai de assen om",
              "correct": false,
              "feedback": "Deze stap klinkt snel, maar je mist dan bron, label of eenheid."
            }
          ]
        },
        {
          "type": "choose",
          "label": "Stap 4",
          "formal_step_id": "estimate_or_interpolate",
          "options": [
            {
              "text": "Bepaal of je exact afleest of moet interpoleren",
              "correct": true
            },
            {
              "text": "Rond altijd naar het dichtstbijzijnde honderd",
              "correct": false,
              "feedback": "Deze stap klinkt snel, maar je mist dan bron, label of eenheid."
            },
            {
              "text": "Noem elke schatting exact",
              "correct": false,
              "feedback": "Deze stap klinkt snel, maar je mist dan bron, label of eenheid."
            }
          ]
        },
        {
          "type": "given",
          "label": "Resultaat",
          "text": "Je hebt een waarde met eenheid en eventueel ongeveer-teken."
        }
      ]
    }
  ]
};
