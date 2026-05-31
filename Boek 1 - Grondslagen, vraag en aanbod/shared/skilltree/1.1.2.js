/**
 * Skill Tree data for 1.1.2 Percentages en indexcijfers
 * activeSkills: null = full catalog source, not the default student route
 */
window.SKILL_TREE_DATA = {
    parNr: "1.1.2",
    parName: "Percentages en indexcijfers",
    activeSkills: ["A38","A39"],
    chapterSkills: ["A38","A39","A42","A43"],
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
            "paragraphTarget": "Procentuele verandering en indexcijfers controleerbaar berekenen.",
            "routePurpose": "Gebruik het redeneer-spel om de rekenstappen en betekenis van percentages hardop te ordenen.",
            "aspectFilter": "calculation",
            "skillScope": [
                "A38",
                "A39"
            ],
            "targetSkills": [
                "A38",
                "A39"
            ],
            "practiceHref": "1.1.2 Percentages en indexcijfers – redeneer-spel.html",
            "practiceLabel": "Open redeneer-spel"
        },
        "calculation": {
            "title": "Oefenroute Rekenen",
            "paragraphTarget": "Procentuele verandering en indexcijfers controleerbaar berekenen.",
            "routePurpose": "Oefen eerst procentuele verandering en daarna indexcijfers met zichtbare tussenstappen.",
            "aspectFilter": "calculation",
            "skillScope": [
                "A38",
                "A39"
            ],
            "targetSkills": [
                "A38",
                "A39"
            ],
            "practiceHref": "1.1.2 Percentages en indexcijfers – wiskundevaardigheden.html",
            "practiceLabel": "Open rekenroute"
        },
        "graphical": {
            "title": "Oefenroute Grafieken",
            "paragraphTarget": "Grafiekwaarden aflezen en gebruiken in procent- of indexberekeningen.",
            "routePurpose": "Lees eerst de grafiekwaarde, kies daarna de berekening die bij de vraag hoort.",
            "aspectFilter": "graphical",
            "skillScope": [
                "A62",
                "A63",
                "A38",
                "A39"
            ],
            "targetSkills": [
                "A62",
                "A63",
                "A38",
                "A39"
            ],
            "practiceHref": "1.1.2 Percentages en indexcijfers – grafiekenspel.html",
            "practiceLabel": "Open grafiekenspel"
        },
        "checkpoint": {
            "title": "Route naar de paragraaf-check",
            "paragraphTarget": "Procentuele verandering en indexcijfers controleerbaar berekenen.",
            "routePurpose": "De check moet dezelfde reken- en antwoordstappen vragen als de eindopgave.",
            "aspectFilter": "calculation",
            "skillScope": [
                "A38",
                "A39"
            ],
            "targetSkills": [
                "A38",
                "A39"
            ]
        }
    }
};
