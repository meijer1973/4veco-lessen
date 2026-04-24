// Procedure Practice Game data for 1.1.1 Schaarste en economisch denken
// Procedure volgt B02 uit references/machine/micro-teaching-units.json letterlijk (4 stappen).
// Sluit aan bij "uitleg vaardigheden" (skill: alternatieve kosten berekenen).

var PROCEDURE_DATA = {
  meta: {
    parNr: "1.1.1",
    parName: "Schaarste en economisch denken"
  },
  procedures: [
    {
      id: "altkosten-berekenen",
      title: "Alternatieve kosten berekenen",
      icon: "fa-scale-balanced",
      description: "Bepaal in vier stappen de alternatieve kosten van een keuze (unit B02)",
      steps: [
        {
          type: "given",
          label: "Gegeven",
          text: "Een schaars middel (tijd, geld, grondstoffen)\nen meerdere mogelijke manieren om het in te zetten,\nmet de opbrengst (of waarde) per alternatief."
        },
        {
          type: "choose",
          label: "Stap 1",
          options: [
            {
              text: "Benoem alle beschikbare alternatieven\nvoor het schaarse middel",
              correct: true
            },
            {
              text: "Bereken direct de opbrengst van het gekozen alternatief",
              correct: false,
              feedback: "Je moet eerst weten welke alternatieven er zijn.\nZonder alternatieven zijn er ook geen alternatieve kosten."
            },
            {
              text: "Bereken het verschil tussen twee willekeurige opties",
              correct: false,
              feedback: "Verschillen bereken je pas in stap 4.\nBegin met alle alternatieven in kaart te brengen."
            }
          ]
        },
        {
          type: "choose",
          label: "Stap 2",
          options: [
            {
              text: "Bereken voor elk alternatief de opbrengst\n(of verwachte waarde)",
              correct: true
            },
            {
              text: "Bereken alleen de opbrengst van het duurste alternatief",
              correct: false,
              feedback: "Je hebt alle opbrengsten nodig om te weten\nwelk niet-gekozen alternatief het beste is."
            },
            {
              text: "Tel alle niet-gekozen opbrengsten op",
              correct: false,
              feedback: "Alternatieve kosten zijn NIET de som van niet-gekozen alternatieven.\nEén alternatief telt: het beste niet-gekozen."
            }
          ]
        },
        {
          type: "choose",
          label: "Stap 3",
          options: [
            {
              text: "Rangschik de alternatieven; het niet-gekozen alternatief\nmet de hoogste opbrengst zijn de alternatieve kosten",
              correct: true
            },
            {
              text: "De alternatieve kosten zijn het gemiddelde\nvan de niet-gekozen opbrengsten",
              correct: false,
              feedback: "Geen gemiddelde — alternatieve kosten zijn de opbrengst\nvan één specifiek alternatief: het beste niet-gekozen."
            },
            {
              text: "De alternatieve kosten zijn de prijs\ndie je voor het gekozen alternatief betaalt",
              correct: false,
              feedback: "Klassieke misconceptie: alternatieve kosten ≠ prijs.\nHet gaat om wat je OPGEEFT, niet wat je betaalt."
            }
          ]
        },
        {
          type: "choose",
          label: "Stap 4",
          options: [
            {
              text: "Vergelijk de opbrengst van de gekozen optie met\nde alternatieve kosten om de nettowaarde te beoordelen",
              correct: true
            },
            {
              text: "Verhoog de alternatieve kosten met een risicopremie",
              correct: false,
              feedback: "Risicopremies komen bij een ander onderwerp (risico en informatie).\nVoor deze procedure is stap 4: opbrengst − alternatieve kosten."
            },
            {
              text: "Deel de opbrengst door de alternatieve kosten",
              correct: false,
              feedback: "Niet delen, maar vergelijken.\nNettowaarde = opbrengst gekozen − alternatieve kosten."
            }
          ]
        },
        {
          type: "given",
          label: "Resultaat",
          text: "Je hebt de alternatieve kosten bepaald als de opbrengst\nvan het beste niet-gekozen alternatief.\nDe nettowaarde van je keuze is:\nopbrengst gekozen alternatief − alternatieve kosten."
        }
      ]
    }
  ]
};
