/**
 * Skill Tree data for 1.1.1 Schaarste en economisch denken
 * activeSkills: null = full catalog source, not the default student route
 */
window.SKILL_TREE_DATA = {
    parNr: "1.1.1",
    parName: "Schaarste en economisch denken",
    activeSkills: null,
    chapterSkills: null,
    newSkills: ["A01","A02","A03","A04","A05","A06","A07","A08","A09","A10","A11","A12","A13","A14","A15","A16","A17","A18","A19","A21","A22","A23","A24","A25","A26","A27","A28","A29","A30","A31","A32","A33","A34","A35","A36","A37","A38","A39","A40","A41","A42","A43","A44","A61","A62","A63","A95"],
    skillMapDefaults: {
        "mode": "compact",
        "aspectFilter": "mixed",
        "maxVisibleAvailable": 4,
        "allowFullView": false
    },
    skillMapRoutes: {
        "reasoning": {
            "title": "Oefenroute Redeneren",
            "paragraphTarget": "Schaarste en alternatieve kosten herkennen in keuzes.",
            "routePurpose": "Oefen hoe je een keuze uitlegt vanuit schaarste en het opgeofferde alternatief.",
            "aspectFilter": "reasoning",
            "skillScope": [
                "B01",
                "B02"
            ],
            "targetSkills": [
                "B02"
            ],
            "practiceHref": "1.1.1 Schaarste en economisch denken – redeneer-spel.html",
            "practiceLabel": "Open redeneer-spel"
        },
        "calculation": {
            "enabled": false
        },
        "graphical": {
            "enabled": false
        },
        "checkpoint": {
            "title": "Route naar de paragraaf-check",
            "paragraphTarget": "Schaarste en alternatieve kosten herkennen in keuzes.",
            "routePurpose": "Gebruik dezelfde begrippen in de check als in het redeneer-spel.",
            "aspectFilter": "reasoning",
            "skillScope": [
                "B01",
                "B02"
            ],
            "targetSkills": [
                "B02"
            ]
        }
    }
};
