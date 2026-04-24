var NEWS_DETECTIVE_DATA = {
  "meta": {
    "parNr": "1.1.1",
    "parName": "Schaarste en economisch denken"
  },
  "article": {
    "headline": "Woningtekort blijft groot: honderdduizenden wachten op sociale huur",
    "body": "Het tekort aan woningen in Nederland blijft oplopen. Meer dan 390.000 mensen staan op de wachtlijst voor een sociale huurwoning, terwijl er veel minder woningen vrijkomen dan er jaarlijks bijkomen op de lijst. De overheid moet kiezen: investeren in nieuwbouw, voorrang geven aan bepaalde groepen, of huurprijzen reguleren. Elke keuze heeft winnaars en verliezers — en gaat ten koste van andere uitgaven.",
    "source": "NOS/CBS",
    "sourceDate": "2024",
    "sourceUrl": "https://nos.nl/artikel/woningtekort-nederland",
    "visualAlt": "Grafiek met woningvraag versus beschikbare woningen in Nederland"
  },
  "rounds": [
    {
      "type": "concept",
      "question": "Welk economisch basisconcept ligt aan deze situatie ten grondslag?",
      "options": [
        {
          "text": "Schaarste — meer behoeften (woningzoekenden) dan beschikbare middelen (woningen)",
          "correct": true,
          "feedback": "Juist! Dit is het schoolvoorbeeld van schaarste: 390.000 wachtenden tegenover veel minder vrijkomende woningen. Omdat behoeften groter zijn dan middelen, moeten er keuzes worden gemaakt."
        },
        {
          "text": "Zeldzaamheid — woningen zijn een zeldzaam product",
          "correct": false,
          "feedback": "Niet juist. Zeldzaamheid en schaarste zijn niet hetzelfde. Er zijn miljoenen woningen in Nederland — niet zeldzaam. Het gaat om de verhouding: méér vraag dan aanbod. Dat is schaarste."
        },
        {
          "text": "Alternatieve kosten van de bewoners",
          "correct": false,
          "feedback": "Alternatieve kosten spelen wel mee (zie de volgende ronde), maar het onderliggende basisconcept is schaarste. Zonder schaarste zouden er geen keuzes met alternatieve kosten nodig zijn."
        },
        {
          "text": "Vraag en aanbod op de woningmarkt",
          "correct": false,
          "feedback": "Vraag en aanbod komen in §1.2 en verder aan bod. Voor deze paragraaf ligt het antwoord eerder: schaarste is het startpunt dat vraag-en-aanbodanalyse pas mogelijk maakt."
        }
      ]
    },
    {
      "type": "consequence",
      "question": "Wat is een plausibele keten van oorzaak en gevolg?",
      "chain": [
        { "text": "Wachtlijst groeit — méér behoeften dan beschikbare woningen", "position": 0 },
        { "text": "Overheid moet kiezen: nieuwbouw, voorrang of prijsregulering", "position": 1 },
        { "text": "Elk budget voor wonen gaat ten koste van onderwijs, zorg of infrastructuur", "position": 2 },
        { "text": "Woningzoekenden ondervinden de alternatieve kosten van uitblijvende keuzes", "position": 3 }
      ],
      "distractors": [
        { "text": "Huizenprijzen dalen automatisch als de wachtlijst groeit" },
        { "text": "De markt lost het tekort op zonder overheidsinterventie" }
      ]
    },
    {
      "type": "model",
      "question": "Welk denkmodel past het beste bij deze beleidssituatie?",
      "options": [
        {
          "id": "schaarste-keuze",
          "label": "Schaarste-model: behoeften > middelen → keuze met alternatieve kosten",
          "description": "Woningzoekenden (behoefte) zijn groter dan beschikbare woningen (middel). De overheid moet kiezen hoe het budget wordt ingezet; elke keuze heeft een niet-gekozen alternatief.",
          "correct": true,
          "feedback": "Juist! Dit is precies het 1.1.1-model. Schaarste dwingt een keuze af, en elke keuze heeft alternatieve kosten — dat wat opgegeven wordt (bijvoorbeeld: €1 mld voor nieuwbouw = €1 mld niet voor zorg)."
        },
        {
          "id": "kosten-baten",
          "label": "Kosten-batenanalyse (optimaliseren)",
          "description": "Maatschappelijke kosten en baten kwantificeren om de beste maatregel te bepalen.",
          "correct": false,
          "feedback": "Kosten-batenanalyse is een vervolgstap die bij latere paragrafen hoort. Voor 1.1.1 is het schaarste-model met alternatieve kosten de juiste lens."
        },
        {
          "id": "marktevenwicht",
          "label": "Marktevenwichtsmodel (vraag = aanbod)",
          "description": "Prijsvorming door het snijpunt van vraag en aanbod op een markt.",
          "correct": false,
          "feedback": "Marktevenwicht komt in §1.4 en verder. Voor 1.1.1 gebruik je het schaarste-model — de voorafgaande conceptuele laag."
        }
      ]
    },
    {
      "type": "error",
      "fakeAnalysis": "Een journalist schrijft: \"Het woningtekort is een probleem van zeldzaamheid, niet van schaarste. Als de overheid gewoon meer geld vrijmaakt voor wonen, is het probleem opgelost zonder keuzes. De alternatieve kosten zijn de huur die mensen zouden betalen als er wel genoeg woningen waren.\"",
      "errorPhrase": "zonder keuzes",
      "errorExplanation": "De fout is 'zonder keuzes'. Méér geld voor wonen betekent minder geld voor iets anders (onderwijs, zorg, defensie). Dat is precies de kern van schaarste: een overheidsbudget is zelf ook beperkt. Elke extra euro voor wonen is een euro die elders niet kan worden uitgegeven — dat zijn de alternatieve kosten van het beleid. Geen keuze maken ís ook een keuze, met eigen alternatieve kosten.",
      "distractorPhrases": [
        "zeldzaamheid, niet van schaarste",
        "de huur die mensen zouden betalen",
        "een probleem van zeldzaamheid"
      ]
    }
  ],
  "lesLink": "Dit concept komt terug bij: alternatieve kosten bij overheidsbeleid, en markten voor schaarse goederen (§1.2)"
};
