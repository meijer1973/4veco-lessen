/**
 * Skill Tree data for 1.1.3 Grafieken en tabellen
 * activeSkills: null = full catalog source, not the default student route
 */
window.SKILL_TREE_DATA = {
    parNr: "1.1.3",
    parName: "Grafieken en tabellen",
    activeSkills: ["A61","A62","A63","A38","A39"],
    chapterSkills: ["A38","A39","A61","A62","A63"],
    newSkills: [],
    skillMapDefaults: {
        "mode": "compact",
        "aspectFilter": "mixed",
        "maxVisibleAvailable": 4,
        "allowFullView": false
    },
    skillMapRoutes: {
        "reasoning": {
            "title": "Oefenroute Redeneren",
            "paragraphTarget": "Tabel- en grafiekgegevens kiezen, aflezen en uitleggen.",
            "routePurpose": "Orden de bronstappen voordat je de grafiek- of tabelvraag beantwoordt.",
            "aspectFilter": "graphical",
            "skillScope": [
                "A61",
                "A62",
                "A63"
            ],
            "targetSkills": [
                "A61",
                "A62",
                "A63"
            ],
            "practiceHref": "1.1.3 Grafieken en tabellen – redeneer-spel.html",
            "practiceLabel": "Open redeneer-spel"
        },
        "calculation": {
            "title": "Oefenroute Rekenen",
            "paragraphTarget": "Tabelwaarden selecteren en gebruiken in een berekening.",
            "routePurpose": "Kies eerst de juiste tabelwaarden; reken daarna pas verder met percentages of indexen.",
            "aspectFilter": "calculation",
            "skillScope": [
                "A61",
                "A38",
                "A39"
            ],
            "targetSkills": [
                "A61",
                "A38",
                "A39"
            ],
            "practiceHref": "1.1.3 Grafieken en tabellen – wiskundevaardigheden.html",
            "practiceLabel": "Open rekenroute"
        },
        "graphical": {
            "title": "Oefenroute Grafieken",
            "paragraphTarget": "Tabel- en grafiekgegevens kiezen, aflezen en gebruiken.",
            "routePurpose": "Oefen tabelselectie, staafdiagrammen en lijngrafieken als een samenhangende bronroute.",
            "aspectFilter": "graphical",
            "skillScope": [
                "A61",
                "A62",
                "A63",
                "A38",
                "A39"
            ],
            "targetSkills": [
                "A61",
                "A62",
                "A63"
            ],
            "practiceHref": "1.1.3 Grafieken en tabellen – grafiekenspel.html",
            "practiceLabel": "Open grafiekenspel"
        },
        "checkpoint": {
            "title": "Route naar de paragraaf-check",
            "paragraphTarget": "Tabel- en grafiekgegevens kiezen, aflezen en gebruiken.",
            "routePurpose": "De check moet bronkeuze, aflezen en antwoordvorm in dezelfde keten controleren.",
            "aspectFilter": "graphical",
            "skillScope": [
                "A61",
                "A62",
                "A63",
                "A38",
                "A39"
            ],
            "targetSkills": [
                "A61",
                "A62",
                "A63"
            ]
        }
    }
};
