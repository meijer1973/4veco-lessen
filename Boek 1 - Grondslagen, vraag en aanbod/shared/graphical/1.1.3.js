var GRAPHICAL_GAME_DATA = {
  "schema_version": 1,
  "meta": {
    "parNr": "1.1.3",
    "parName": "Grafieken en tabellen",
    "title": "Grafieken lezen"
  },
  "aspect": "grafische voorstelling",
  "student_title": "Grafieken en tabelwaarden lezen",
  "student_subtitle": "Lees eerst titel, as en eenheid. Kies daarna pas waarden en reken rustig verder.",
  "internal_pv_boundary": {
    "student_facing_pv_projection": false,
    "pv_machine_promotion": false,
    "adaptive_or_diagnostic_use": false,
    "mastery_or_sequencing_use": false,
    "ai_or_summative_use": false
  },
  "challenges": [
    {
      "id": "bar-ice-quantity-200",
      "type": "bar_value_read",
      "title": "Lees een waarde uit de bron",
      "prompt": "Hoeveel ijsjes worden verkocht bij prijs EUR 2,00?",
      "target_label": "EUR 2,00",
      "graph": {
        "type": "bar",
        "title": "IJsjesverkoop per prijs",
        "x_label": "prijs",
        "y_label": "aantal verkocht",
        "unit": "ijsjes",
        "series": [
          {
            "label": "EUR 1,00",
            "value": 500
          },
          {
            "label": "EUR 1,50",
            "value": 400
          },
          {
            "label": "EUR 2,00",
            "value": 300
          },
          {
            "label": "EUR 2,50",
            "value": 200
          },
          {
            "label": "EUR 3,00",
            "value": 100
          }
        ]
      },
      "expected_answer": {
        "kind": "number",
        "value": 300,
        "unit": "ijsjes",
        "tolerance": 0
      },
      "feedback_steps": [
        {
          "label": "Bron",
          "text": "De grafiek toont ijsjesverkoop bij verschillende prijzen."
        },
        {
          "label": "Waarden",
          "text": "Zoek het label EUR 2,00. De staaf hoort bij 300 ijsjes."
        },
        {
          "label": "Berekening",
          "text": "Er is hier geen formule nodig. Je leest de bronwaarde af."
        }
      ]
    },
    {
      "id": "line-broodjes-price-350",
      "type": "line_value_read",
      "title": "Lees de prijs bij een hoeveelheid",
      "prompt": "Welke prijs hoort bij 150 broodjes?",
      "target_label": "150 broodjes",
      "graph": {
        "type": "line",
        "title": "Broodjesverkoop",
        "x_label": "hoeveelheid",
        "y_label": "prijs",
        "unit": "euro",
        "series": [
          {
            "label": "100 broodjes",
            "value": 4
          },
          {
            "label": "150 broodjes",
            "value": 3.5
          },
          {
            "label": "200 broodjes",
            "value": 3
          },
          {
            "label": "250 broodjes",
            "value": 2.5
          },
          {
            "label": "300 broodjes",
            "value": 2
          }
        ]
      },
      "expected_answer": {
        "kind": "number",
        "value": 3.5,
        "unit": "euro",
        "tolerance": 0.05
      },
      "feedback_steps": [
        {
          "label": "Bron",
          "text": "De grafiek koppelt hoeveelheid broodjes aan prijs."
        },
        {
          "label": "Waarden",
          "text": "Bij 150 broodjes hoort het punt op EUR 3,50."
        },
        {
          "label": "Berekening",
          "text": "Lees de waarde met eenheid: EUR 3,50."
        }
      ]
    },
    {
      "id": "bar-ice-percentage-change",
      "type": "graph_values_percentage_change",
      "title": "Gebruik twee bronwaarden",
      "prompt": "Bereken de procentuele verandering van EUR 1,00 naar EUR 2,00.",
      "graph": {
        "type": "bar",
        "title": "IJsjesverkoop per prijs",
        "x_label": "prijs",
        "y_label": "aantal verkocht",
        "unit": "ijsjes",
        "series": [
          {
            "label": "EUR 1,00",
            "value": 500
          },
          {
            "label": "EUR 1,50",
            "value": 400
          },
          {
            "label": "EUR 2,00",
            "value": 300
          },
          {
            "label": "EUR 2,50",
            "value": 200
          },
          {
            "label": "EUR 3,00",
            "value": 100
          }
        ]
      },
      "expected_answer": {
        "kind": "percentage_change",
        "old_label": "EUR 1,00",
        "new_label": "EUR 2,00",
        "value": -40,
        "unit": "%",
        "tolerance": 0.1
      },
      "feedback_steps": [
        {
          "label": "Bron",
          "text": "De vraag vergelijkt de verkoop bij EUR 1,00 met de verkoop bij EUR 2,00."
        },
        {
          "label": "Waarden",
          "text": "Oud = 500 ijsjes en nieuw = 300 ijsjes. Het verschil is -200."
        },
        {
          "label": "Berekening",
          "text": "-200 / 500 x 100% = -40%. De verkoop daalt met 40%."
        }
      ]
    },
    {
      "id": "line-water-index",
      "type": "line_value_read",
      "title": "Lees een indexachtige waarde",
      "prompt": "Wat is de verkoopindex in juni als januari 100 is?",
      "target_label": "juni",
      "graph": {
        "type": "line",
        "title": "Verkoopindex flesjes water",
        "x_label": "periode",
        "y_label": "index",
        "unit": "index",
        "series": [
          {
            "label": "januari",
            "value": 100
          },
          {
            "label": "juni",
            "value": 70
          }
        ]
      },
      "expected_answer": {
        "kind": "number",
        "value": 70,
        "unit": "index",
        "tolerance": 0
      },
      "feedback_steps": [
        {
          "label": "Bron",
          "text": "De grafiek gebruikt januari als basis: januari = 100."
        },
        {
          "label": "Waarden",
          "text": "Het punt bij juni staat op 70."
        },
        {
          "label": "Berekening",
          "text": "Index 70 betekent dat de verkoop 30% lager is dan in januari."
        }
      ]
    },
    {
      "id": "line-water-percentage-change",
      "type": "graph_values_percentage_change",
      "title": "Controleer een journalistieke claim",
      "prompt": "Bereken de procentuele verandering van januari naar juni.",
      "graph": {
        "type": "line",
        "title": "Verkoop flesjes water",
        "x_label": "periode",
        "y_label": "aantal per week",
        "unit": "flesjes",
        "series": [
          {
            "label": "januari",
            "value": 500
          },
          {
            "label": "juni",
            "value": 350
          }
        ]
      },
      "expected_answer": {
        "kind": "percentage_change",
        "old_label": "januari",
        "new_label": "juni",
        "value": -30,
        "unit": "%",
        "tolerance": 0.1
      },
      "feedback_steps": [
        {
          "label": "Bron",
          "text": "Je vergelijkt januari met juni, dus januari is de oude waarde."
        },
        {
          "label": "Waarden",
          "text": "Oud = 500 en nieuw = 350. Het verschil is -150."
        },
        {
          "label": "Berekening",
          "text": "-150 / 500 x 100% = -30%. Dat is niet precies een derde."
        }
      ]
    }
  ]
};
