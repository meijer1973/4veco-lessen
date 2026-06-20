// AUTO-COPIED FROM 4veco-platform/engines/ — DO NOT EDIT HERE
/**
 * SkillTree Base Elements (bundled).
 * Self-contained: catalog SKILLS + generators + layer display data.
 * Bundled at deploy time from references/machine/micro-teaching-units.json
 * and engines/skilltree/generators.js.
 */
(function (root, factory) {
    if (typeof module !== 'undefined' && module.exports) {
        module.exports = factory();
    } else {
        root.SKILL_TREE_ELEMENTS = factory();
    }
})(typeof self !== 'undefined' ? self : this, function () {
    'use strict';

    /* ── helpers ─────────────────────────────────────────────── */
    var ri = function (a, b) { return a + Math.floor(Math.random() * (b - a + 1)); };
    var pick = function (arr) { return arr[Math.floor(Math.random() * arr.length)]; };
    var round1 = function (n) { return Math.round(n * 10) / 10; };
    var round2 = function (n) { return Math.round(n * 100) / 100; };

    /**
     * Build an MC step from a correct answer and distractor candidates.
     * Returns { q, mode:'mc', options:[4], correctIdx, hint, expl }.
     */
    var mcStep = function (q, correct, distractors, hint, expl) {
        var pool = [];
        for (var i = 0; i < distractors.length; i++) {
            if (distractors[i] !== correct) pool.push(distractors[i]);
        }
        // Deduplicate
        var seen = {};
        var unique = [];
        for (var j = 0; j < pool.length; j++) {
            var key = String(pool[j]);
            if (!seen[key]) { seen[key] = true; unique.push(pool[j]); }
        }
        // Pad if needed
        while (unique.length < 3) {
            var offset = ri(1, 5) * (Math.random() < 0.5 ? 1 : -1);
            var candidate = typeof correct === 'number' ? correct + offset : correct + '*';
            if (String(candidate) !== String(correct) && !seen[String(candidate)]) {
                seen[String(candidate)] = true;
                unique.push(candidate);
            }
        }
        var opts = unique.slice(0, 3);
        var insertAt = ri(0, 3);
        opts.splice(insertAt, 0, correct);
        return { q: q, mode: 'mc', options: opts, correctIdx: insertAt, hint: hint, expl: expl };
    };

    var GEN = {};

    GEN.A01 = function () {
        var slope = ri(2, 6), intercept = slope * ri(10, 25);
        var correct = -slope;
        var step3 = mcStep(
            'De vraaglijn is Qv = ' + intercept + ' + ? \u00D7 P. Wat is de co\u00EBffici\u00EBnt van P?',
            correct,
            [slope, -intercept, intercept, slope + 1, -(slope - 1)],
            'De vraag daalt, dus de co\u00EBffici\u00EBnt is negatief.',
            'Qv = ' + intercept + ' \u2212 ' + slope + 'P, dus de co\u00EBffici\u00EBnt is \u2212' + slope + '.'
        );
        return {
            context: 'De vraag naar een product daalt met ' + slope + ' stuks per euro prijsverhoging. Bij een prijs van \u20AC0 is de vraag ' + intercept + ' stuks.',
            steps: [
                { q: 'Hoeveel is de vraag bij P = 0?', a: intercept, hint: 'Dit staat direct in de opgave.', expl: 'Bij P = 0 is Qv = ' + intercept + '.' },
                { q: 'Met hoeveel stuks daalt de vraag per euro prijsverhoging?', a: slope, hint: 'Zoek het woord \'daalt\' in de tekst.', expl: 'Per euro stijging daalt de vraag met ' + slope + '.' },
                step3
            ]
        };
    };

    GEN.A02 = function () {
        var Q = ri(5, 20), b = ri(2, 5), d = ri(1, 4);
        var c = ri(10, 40), a = c + Q * (b + d);
        var orderStep = {
            q: 'Zet de oplosstappen in de juiste volgorde.',
            mode: 'order',
            blocks: [
                'Deel door de co\u00EBffici\u00EBnt van Q',
                'Breng Q-termen naar \u00E9\u00E9n kant',
                'Breng constanten naar de andere kant'
            ],
            correctOrder: [1, 2, 0],
            hint: 'Eerst verzamelen, dan isoleren, dan delen.',
            expl: 'Stap 1: Q-termen verzamelen \u2192 Stap 2: constanten apart \u2192 Stap 3: delen door co\u00EBffici\u00EBnt.'
        };
        return {
            context: 'Los op: ' + a + ' \u2212 ' + b + 'Q = ' + c + ' + ' + d + 'Q',
            steps: [
                orderStep,
                { q: 'Tel +' + b + 'Q bij beide kanten op. Hoeveel Q staat er rechts?', a: b + d, hint: 'Rechts stond ' + d + 'Q, daar komt ' + b + 'Q bij: ' + d + ' + ' + b + ' = ' + (b + d) + '.', expl: a + ' = ' + c + ' + ' + d + 'Q + ' + b + 'Q = ' + c + ' + ' + (b + d) + 'Q' },
                { q: 'Trek ' + c + ' af aan beide kanten: ' + a + ' \u2212 ' + c + ' = ?', a: a - c, hint: 'Trek ' + c + ' af van ' + a + '.', expl: a + ' \u2212 ' + c + ' = ' + (a - c) + ', dus ' + (b + d) + 'Q = ' + (a - c) },
                { q: 'Los op: ' + (b + d) + 'Q = ' + (a - c) + '. Q = ?', a: Q, hint: 'Deel ' + (a - c) + ' door ' + (b + d) + '.', expl: 'Q = ' + (a - c) + ' \u00F7 ' + (b + d) + ' = ' + Q }
            ]
        };
    };

    GEN.A03 = function () {
        var b = pick([2, 4, 5]), aOver = ri(10, 30), a = b * aOver;
        var coefQ = round2(1 / b);
        var correctCoef = -coefQ;
        var step2 = mcStep(
            'Wat is de co\u00EBffici\u00EBnt van Q?',
            correctCoef,
            [coefQ, -1 / (b + 1), 1 / b, -b, b],
            'Je deelt \u2212Q door ' + b + '. Let op: het teken blijft negatief.',
            'P = ' + aOver + ' \u2212 ' + coefQ + 'Q, dus de co\u00EBffici\u00EBnt is \u2212' + coefQ + '.'
        );
        return {
            context: 'Schrijf om: Qv = ' + a + ' \u2212 ' + b + 'P  \u2192  P = ?',
            steps: [
                { q: 'Herschrijf naar P = \u2026 Wat is de constante term?', a: aOver, hint: 'Isoleer ' + b + 'P aan \u00E9\u00E9n kant en deel alles door ' + b + '.', expl: b + 'P = ' + a + ' \u2212 Q \u2192 P = ' + a + '/' + b + ' \u2212 Q/' + b + ' \u2192 constante = ' + aOver },
                step2
            ]
        };
    };

    GEN.A04 = function () {
        var a = ri(30, 80), b = pick([2, 3, 4, 5]), Q = ri(3, 15);
        var ans = a - b * Q;
        var mcFirst = mcStep(
            'Wat bereken je eerst?',
            b + ' \u00D7 ' + Q,
            [a + ' \u2212 ' + b, a + ' \u00D7 ' + Q, Q + ' \u2212 ' + b, a + ' + ' + b],
            'Eerst vermenigvuldigen, dan aftrekken.',
            'Eerst ' + b + ' \u00D7 ' + Q + ' uitrekenen, dan pas aftrekken van ' + a + '.'
        );
        return {
            context: 'Gegeven: P = ' + a + ' \u2212 ' + b + 'Q. Bereken P als Q = ' + Q + '.',
            steps: [
                mcFirst,
                { q: 'Bereken ' + b + ' \u00D7 ' + Q + ' = ?', a: b * Q, hint: 'Vermenigvuldig ' + b + ' met ' + Q + '.', expl: b + ' \u00D7 ' + Q + ' = ' + (b * Q) },
                { q: 'P = ' + a + ' \u2212 ' + (b * Q) + ' = ?', a: ans, hint: 'Trek ' + (b * Q) + ' af van ' + a + '.', expl: 'P = ' + a + ' \u2212 ' + (b * Q) + ' = ' + ans }
            ]
        };
    };

    GEN.A10 = function () {
        var base = ri(4, 20) * 2, height = ri(4, 20) * 2;
        var area = 0.5 * base * height;
        return {
            context: 'Bereken de oppervlakte van een driehoek met basis = ' + base + ' en hoogte = ' + height + '.',
            steps: [
                { q: 'Bereken de oppervlakte (\u00BD \u00D7 basis \u00D7 hoogte).', a: area, hint: 'Oppervlakte = \u00BD \u00D7 ' + base + ' \u00D7 ' + height, expl: 'Oppervlakte = \u00BD \u00D7 ' + base + ' \u00D7 ' + height + ' = ' + area }
            ]
        };
    };

    GEN.A11 = function () {
        var a = ri(1, 4), b = ri(3, 12), c = ri(10, 100);
        var mcConst = mcStep(
            'Wat is de afgeleide van de constante ' + c + '?',
            0,
            [c, 1, -c, c / 2],
            'Wat gebeurt er met een constante bij differenti\u00EBren?',
            'De afgeleide van een constante is altijd 0.'
        );
        return {
            context: 'Bepaal de afgeleide van f(Q) = ' + a + 'Q\u00B2 + ' + b + 'Q + ' + c + '.',
            steps: [
                { q: 'Wat is de afgeleide van ' + a + 'Q\u00B2? Geef de co\u00EBffici\u00EBnt van Q.', a: 2 * a, hint: 'Bij differenti\u00EBren: vermenigvuldig de co\u00EBffici\u00EBnt met de macht.', expl: a + 'Q\u00B2 \u2192 ' + (2 * a) + 'Q' },
                { q: 'Wat is de afgeleide van ' + b + 'Q?', a: b, hint: 'De afgeleide van bQ is gewoon b.', expl: b + 'Q \u2192 ' + b },
                mcConst
            ]
        };
    };

    GEN.A05 = function () {
        var b = pick([2, 3, 4, 5]), alphaDiv = ri(8, 25), alpha = b * alphaDiv;
        var d = pick([1, 2, 3, 4]), cDiv = ri(3, 12), c = d * cDiv;
        var mcSnijpunt = mcStep(
            'Wat stel je gelijk aan nul om het snijpunt met de P-as te vinden?',
            'Q',
            ['Q', 'P', 'Qv \u2212 Qa', 'P \u2212 Q'],
            'Het snijpunt met de P-as is het punt waar de hoeveelheid nul is.',
            'Op de P-as is Q = 0. Je vult Q = 0 in om P te berekenen.'
        );
        return {
            context: 'Qv = ' + alpha + ' \u2212 ' + b + 'P en Qa = \u2212' + c + ' + ' + d + 'P.\nBepaal de snijpunten met de P-as.',
            steps: [
                mcSnijpunt,
                { q: 'Bij welke prijs is de gevraagde hoeveelheid nul? (snijpunt vraaglijn met P-as)', a: alphaDiv, hint: 'Vul Qv = 0 in en los op naar P.', expl: '0 = ' + alpha + ' \u2212 ' + b + 'P \u2192 P = ' + alpha + '/' + b + ' = ' + alphaDiv },
                { q: 'Bij welke prijs begint het aanbod? (snijpunt aanbodlijn met P-as)', a: cDiv, hint: 'Vul Qa = 0 in en los op naar P.', expl: '0 = \u2212' + c + ' + ' + d + 'P \u2192 P = ' + c + '/' + d + ' = ' + cDiv }
            ]
        };
    };

    GEN.A06 = function () {
        var b = ri(2, 5), d = ri(1, 4), Ps = ri(8, 25);
        var maxC = Math.min(50, d * Ps - 1);
        if (maxC < 2) return GEN.A06();
        var c = ri(2, maxC);
        var a = (b + d) * Ps - 2 * c;
        if (a <= 0) return GEN.A06();
        var alpha = a + c;
        var Qs = alpha - b * Ps;
        if (Qs <= 0) return GEN.A06();
        var orderEvenwicht = {
            q: 'Zet de stappen voor het berekenen van het marktevenwicht in de juiste volgorde.',
            mode: 'order',
            blocks: [
                'Vul P* in om Q* te berekenen',
                'Stel Qv = Qa',
                'Los op naar P'
            ],
            correctOrder: [1, 2, 0],
            hint: 'Eerst gelijkstellen, dan oplossen, dan invullen.',
            expl: 'Stap 1: Qv = Qa \u2192 Stap 2: los op naar P* \u2192 Stap 3: vul P* in voor Q*.'
        };
        return {
            context: 'Qv = ' + alpha + ' \u2212 ' + b + 'P  en  Qa = \u2212' + c + ' + ' + d + 'P. Bereken het marktevenwicht.',
            steps: [
                orderEvenwicht,
                { q: 'Stel Qv = Qa en los op. P* = ?', a: Ps, hint: alpha + ' \u2212 ' + b + 'P = \u2212' + c + ' + ' + d + 'P \u2192 ' + (b + d) + 'P = ' + (alpha + c), expl: 'P* = ' + (alpha + c) + ' \u00F7 ' + (b + d) + ' = ' + Ps },
                { q: 'Q* = ?', a: Qs, hint: 'Vul P* in bij Qv: ' + alpha + ' \u2212 ' + b + '\u00D7' + Ps, expl: 'Q* = ' + Qs }
            ]
        };
    };

    GEN.A07 = function () {
        var a = ri(30, 80), b = ri(1, 4);
        var mcQ2 = mcStep(
            'Wat is de co\u00EBffici\u00EBnt van Q\u00B2?',
            -b,
            [b, -a, a, -(b + 1), b - 1],
            '\u2212' + b + 'Q \u00D7 Q = \u2212' + b + 'Q\u00B2. De co\u00EBffici\u00EBnt is negatief.',
            'TO = ' + a + 'Q \u2212 ' + b + 'Q\u00B2, dus de co\u00EBffici\u00EBnt van Q\u00B2 is \u2212' + b + '.'
        );
        return {
            context: 'De vraaglijn is P = ' + a + ' \u2212 ' + b + 'Q. Stel de TO-functie op (TO = P \u00D7 Q).',
            steps: [
                { q: 'TO = P \u00D7 Q = (' + a + ' \u2212 ' + b + 'Q) \u00D7 Q. Werk de haakjes uit. Wat is de co\u00EBffici\u00EBnt van Q?', a: a, hint: a + ' \u00D7 Q \u2192 co\u00EBffici\u00EBnt is ' + a + '.', expl: 'De eerste term is ' + a + 'Q.' },
                mcQ2
            ]
        };
    };

    GEN.A08 = function () {
        var a = round1(ri(1, 5) * 0.5), b = ri(5, 20), c = ri(50, 300);
        var Q = ri(5, 15);
        var vk = round1(a * Q * Q + b * Q);
        var mcVK = mcStep(
            'Wat zijn de vaste kosten?',
            c,
            [b, a, round1(a + b), round1(a * Q * Q)],
            'De vaste kosten zijn de kosten als er niets geproduceerd wordt (Q = 0).',
            'TK(0) = ' + c + '. De constante term is de vaste kosten.'
        );
        return {
            context: 'TK = ' + a + 'Q\u00B2 + ' + b + 'Q + ' + c,
            steps: [
                mcVK,
                { q: 'Bereken de variabele kosten bij Q = ' + Q + '.', a: vk, hint: 'De variabele kosten zijn TK minus de vaste kosten. Of: de termen m\u00E9t Q.', expl: 'TVK = ' + a + '\u00D7' + (Q * Q) + ' + ' + b + '\u00D7' + Q + ' = ' + vk }
            ]
        };
    };

    GEN.A09 = function () {
        var a1 = pick([1, 2]), c1 = ri(4, 12);
        var a2 = pick([1, 2]), c2 = ri(4, 12);
        var coefA = round2(1 / a1), constA = round2(-c1 / a1);
        var coefB = round2(1 / a2), constB = round2(-c2 / a2);
        var coefCol = round2(coefA + coefB);
        var constCol = round2(constA + constB);
        var orderB4 = {
            q: 'Zet de stappen voor het opstellen van de collectieve aanbodfunctie in de juiste volgorde.',
            mode: 'order',
            blocks: [
                'Schrijf individuele functies om naar Q = f(P)',
                'Tel de Q-functies van alle bedrijven op',
                'Vereenvoudig de collectieve functie'
            ],
            correctOrder: [0, 1, 2],
            hint: 'Eerst omschrijven, dan optellen, dan vereenvoudigen.',
            expl: 'Stap 1: Omschrijven naar Q = f(P) \u2192 Stap 2: Optellen \u2192 Stap 3: Vereenvoudigen.'
        };
        return {
            context: 'Bedrijf A: P = ' + a1 + 'Qa + ' + c1 + '\nBedrijf B: P = ' + a2 + 'Qb + ' + c2 + '\nStel de collectieve aanbodfunctie op.',
            steps: [
                orderB4,
                { q: 'Herschrijf het aanbod van A naar Qa = \u2026P + \u2026 Wat is de co\u00EBffici\u00EBnt van P?', a: coefA, hint: 'P = ' + a1 + 'Qa + ' + c1 + ' \u2192 ' + a1 + 'Qa = P \u2212 ' + c1 + ' \u2192 deel door ' + a1, expl: 'Qa = ' + coefA + 'P + (' + constA + '). De co\u00EBffici\u00EBnt van P is ' + coefA + '.' },
                { q: 'Wat is de constante in Qa = ' + coefA + 'P + ?', a: constA, hint: '\u2212' + c1 + ' \u00F7 ' + a1 + ' = ? (let op het minteken!)', expl: 'Qa = ' + coefA + 'P + (' + constA + '). De constante is ' + constA + '.' },
                { q: 'Herschrijf het aanbod van B naar Qb = \u2026P + \u2026 Wat is de co\u00EBffici\u00EBnt van P?', a: coefB, hint: 'P = ' + a2 + 'Qb + ' + c2 + ' \u2192 deel door ' + a2, expl: 'Qb = ' + coefB + 'P + (' + constB + '). De co\u00EBffici\u00EBnt van P is ' + coefB + '.' },
                { q: 'Wat is de constante in Qb = ' + coefB + 'P + ?', a: constB, hint: '\u2212' + c2 + ' \u00F7 ' + a2 + ' = ? (let op het minteken!)', expl: 'Qb = ' + coefB + 'P + (' + constB + '). De constante is ' + constB + '.' },
                { q: 'Tel de co\u00EBffici\u00EBnten van P op voor de collectieve aanbodfunctie. Wat is de co\u00EBffici\u00EBnt van P in Qcol?', a: coefCol, hint: 'Co\u00EBffici\u00EBnt A was ' + coefA + ', co\u00EBffici\u00EBnt B was ' + coefB + '. Tel op.', expl: coefA + ' + ' + coefB + ' = ' + coefCol },
                { q: 'Wat is de constante in Qcol = ' + coefCol + 'P + ?', a: constCol, hint: 'Constante A was ' + constA + ', constante B was ' + constB + '. Tel op.', expl: constA + ' + (' + constB + ') = ' + constCol + '. De collectieve aanbodfunctie is Qcol = ' + coefCol + 'P + (' + constCol + ').' }
            ]
        };
    };

    GEN.A12 = function () {
        var a = ri(30, 80), b = ri(1, 4);
        var mcMO = mcStep(
            'Wat is de co\u00EBffici\u00EBnt van Q in MO?',
            -(2 * b),
            [2 * b, -b, b, -(2 * b + 1), 2 * b - 1],
            'Wat is de afgeleide van \u2212' + b + 'Q\u00B2? Let op het teken.',
            'MO = ' + a + ' \u2212 ' + (2 * b) + 'Q, dus de co\u00EBffici\u00EBnt is \u2212' + (2 * b) + '.'
        );
        return {
            context: 'TO = ' + a + 'Q \u2212 ' + b + 'Q\u00B2. Bepaal de MO-functie (= afgeleide van TO).',
            steps: [
                { q: 'Wat is de constante term in MO?', a: a, hint: 'MO is de afgeleide van TO naar Q. Wat is de afgeleide van ' + a + 'Q?', expl: 'MO begint met ' + a },
                mcMO,
                { q: 'Bij welke Q is MO = 0?', a: round1(a / (2 * b)), hint: 'Stel MO = 0 en los op naar Q.', expl: 'Q = ' + a + ' \u00F7 ' + (2 * b) + ' = ' + round1(a / (2 * b)) }
            ]
        };
    };

    GEN.A13 = function () {
        var a = round1(pick([0.5, 1, 1.5, 2])), b = ri(5, 20), c = ri(50, 200);
        var mcMK = mcStep(
            'Wat is de co\u00EBffici\u00EBnt van Q in MK?',
            round1(2 * a),
            [a, round1(a / 2), round1(2 * a + 1), round1(a * a)],
            'MK is de afgeleide van TK. Wat is de afgeleide van ' + a + 'Q\u00B2?',
            a + 'Q\u00B2 \u2192 ' + round1(2 * a) + 'Q (vermenigvuldig co\u00EBffici\u00EBnt met macht).'
        );
        return {
            context: 'TK = ' + a + 'Q\u00B2 + ' + b + 'Q + ' + c + '. Bepaal de MK-functie.',
            steps: [
                mcMK,
                { q: 'Wat is de constante in MK?', a: b, hint: 'Wat is de afgeleide van ' + b + 'Q?', expl: 'MK = ' + round1(2 * a) + 'Q + ' + b }
            ]
        };
    };

    GEN.A14 = function () {
        var a = pick([0.5, 1, 2]), b = ri(5, 15), c = ri(50, 200);
        var Q = ri(5, 20);
        var tk = round1(a * Q * Q + b * Q + c);
        var gtk = round2(tk / Q);
        var mcGTK = mcStep(
            'Hoe bereken je de GTK?',
            'TK / Q',
            ['TK \u2212 Q', 'TK \u00D7 Q', 'Q / TK'],
            'GTK staat voor Gemiddelde Totale Kosten.',
            'GTK = TK gedeeld door Q. "Gemiddelde" betekent: delen door de hoeveelheid.'
        );
        return {
            context: 'TK = ' + a + 'Q\u00B2 + ' + b + 'Q + ' + c + '. Bereken GTK bij Q = ' + Q + '.',
            steps: [
                mcGTK,
                { q: 'Bereken eerst TK bij Q = ' + Q + '.', a: tk, hint: 'Vul Q = ' + Q + ' in de kostenfunctie in en reken stap voor stap uit.', expl: 'TK = ' + a + '\u00D7' + (Q * Q) + ' + ' + (b * Q) + ' + ' + c + ' = ' + tk },
                { q: 'Bereken nu GTK.', a: gtk, hint: 'GTK = TK gedeeld door Q.', expl: 'GTK = ' + tk + ' \u00F7 ' + Q + ' = ' + gtk }
            ]
        };
    };

    GEN.A15 = function () {
        var P1 = pick([5, 8, 10, 12, 15, 20, 25, 40, 50]);
        var pctP = pick([5, 10, 20, 25, 50]);
        var deltaP = P1 * pctP / 100;
        if (deltaP < 1 || deltaP % 1 !== 0) return GEN.A15();
        var P2 = P1 + deltaP;
        var Q1 = pick([40, 50, 60, 80, 100, 120, 150, 200]);
        var pctQ = pick([-5, -10, -15, -20, -25, -30, -40, -50]);
        var deltaQ = Q1 * pctQ / 100;
        if (deltaQ % 1 !== 0) return GEN.A15();
        var Q2 = Q1 + deltaQ;
        if (Q2 <= 0) return GEN.A15();
        var Ev = round2(pctQ / pctP);
        var absEv = Math.abs(Ev);
        var elastic = absEv > 1 ? 'elastisch' : absEv < 1 ? 'inelastisch' : 'eenheidselastisch';
        var mcInterp = mcStep(
            'De Ev = ' + Ev + '. De vraag is\u2026',
            elastic,
            ['elastisch', 'inelastisch', 'eenheidselastisch', 'perfect elastisch'],
            '|Ev| > 1 \u2192 elastisch, |Ev| < 1 \u2192 inelastisch, |Ev| = 1 \u2192 eenheidselastisch.',
            '|Ev| = ' + absEv + (absEv > 1 ? ' > 1 \u2192 elastisch.' : absEv < 1 ? ' < 1 \u2192 inelastisch.' : ' = 1 \u2192 eenheidselastisch.')
        );
        // Error step: 3 attempts at %ΔQ, one uses wrong base value (P2 instead of Q1)
        var wrongPctQ = round2(((Q2 - Q1) / P2) * 100);
        var errorStep = {
            q: 'E\u00E9n van deze berekeningen van %\u0394Qv bevat een fout. Welke?',
            mode: 'error',
            shownSteps: [
                { text: '%\u0394Qv = (' + Q2 + ' \u2212 ' + Q1 + ') / ' + Q1 + ' \u00D7 100 = ' + pctQ + '%', isError: false },
                { text: '%\u0394Qv = (' + Q2 + ' \u2212 ' + Q1 + ') / ' + P2 + ' \u00D7 100 = ' + wrongPctQ + '%', isError: true },
                { text: '%\u0394Qv = ' + deltaQ + ' / ' + Q1 + ' \u00D7 100 = ' + pctQ + '%', isError: false }
            ],
            hint: 'Bij procentuele verandering deel je altijd door de oorspronkelijke waarde.',
            expl: 'Stap 2 deelt door ' + P2 + ' (de nieuwe prijs) in plaats van door ' + Q1 + ' (de oorspronkelijke hoeveelheid). Dat is fout!'
        };
        // Shuffle error step position so the error isn't always in the middle
        var errIdx = ri(0, 2);
        var errSteps = errorStep.shownSteps.slice();
        var errItem = errSteps.splice(1, 1)[0]; // remove the error from position 1
        errSteps.splice(errIdx, 0, errItem);     // insert at random position
        errorStep.shownSteps = errSteps;

        return {
            context: 'De prijs stijgt van \u20AC' + P1 + ' naar \u20AC' + P2 + '.\nDe gevraagde hoeveelheid daalt van ' + Q1 + ' naar ' + Q2 + '.\nBereken de prijselasticiteit van de vraag.',
            steps: [
                { q: 'Bereken de procentuele verandering van de prijs (%\u0394P).', a: pctP, hint: '%\u0394P = (\u0394P / P\u2081) \u00D7 100 = (' + deltaP + ' / ' + P1 + ') \u00D7 100', expl: '%\u0394P = (' + deltaP + ' / ' + P1 + ') \u00D7 100 = ' + pctP + '%' },
                errorStep,
                { q: 'Bereken nu zelf %\u0394Qv.', a: pctQ, hint: '%\u0394Q = ((Q\u2082 \u2212 Q\u2081) / Q\u2081) \u00D7 100 = ((' + Q2 + ' \u2212 ' + Q1 + ') / ' + Q1 + ') \u00D7 100', expl: '%\u0394Q = ((' + Q2 + ' \u2212 ' + Q1 + ') / ' + Q1 + ') \u00D7 100 = ' + pctQ + '%' },
                { q: 'Bereken de prijselasticiteit (Ev = %\u0394Q / %\u0394P).', a: Ev, hint: 'Deel de procentuele verandering van Q door die van P.', expl: 'Ev = ' + pctQ + ' / ' + pctP + ' = ' + Ev },
                mcInterp
            ]
        };
    };

    GEN.A16 = function () {
        var Pb1 = pick([5, 8, 10, 15, 20, 25]);
        var pctPb = pick([-20, -10, 10, 20, 25, 50]);
        var deltaPb = Pb1 * pctPb / 100;
        if (deltaPb % 1 !== 0 || deltaPb === 0) return GEN.A16();
        var Pb2 = Pb1 + deltaPb;
        if (Pb2 <= 0) return GEN.A16();
        var Qa1 = pick([40, 50, 60, 80, 100, 120, 200]);
        var pctQa = pick([-20, -10, -5, 5, 10, 15, 20, 25]);
        var deltaQa = Qa1 * pctQa / 100;
        if (deltaQa % 1 !== 0 || deltaQa === 0) return GEN.A16();
        var Qa2 = Qa1 + deltaQa;
        if (Qa2 <= 0) return GEN.A16();
        var Ekr = round2(pctQa / pctPb);
        var goodA = pick(['brood', 'koffie', 'fietsen', 'laptops', 'boeken', 'schoenen']);
        var goodB = pick(['boter', 'thee', 'auto\u2019s', 'tablets', 'e-readers', 'laarzen']);
        var relation = Ekr > 0 ? 'substituten' : 'complementen';
        var mcRelation = mcStep(
            'Ekr = ' + Ekr + '. ' + goodA + ' en ' + goodB + ' zijn\u2026',
            relation,
            ['substituten', 'complementen', 'onafhankelijke goederen', 'inferieure goederen'],
            'Ekr > 0 \u2192 substituten, Ekr < 0 \u2192 complementen.',
            'Ekr = ' + Ekr + (Ekr > 0 ? ' > 0 \u2192 substituten.' : ' < 0 \u2192 complementen.')
        );
        return {
            context: 'De prijs van ' + goodB + ' verandert van \u20AC' + Pb1 + ' naar \u20AC' + Pb2 + '.\nDe gevraagde hoeveelheid ' + goodA + ' verandert van ' + Qa1 + ' naar ' + Qa2 + '.\nBereken de kruiselasticiteit.',
            steps: [
                { q: 'Bereken de procentuele prijsverandering van ' + goodB + ' (%\u0394Pb).', a: pctPb, hint: '%\u0394Pb = ((' + Pb2 + ' \u2212 ' + Pb1 + ') / ' + Pb1 + ') \u00D7 100', expl: '%\u0394Pb = (' + deltaPb + ' / ' + Pb1 + ') \u00D7 100 = ' + pctPb + '%' },
                { q: 'Bereken de procentuele hoeveelheidsverandering van ' + goodA + ' (%\u0394Qa).', a: pctQa, hint: '%\u0394Qa = ((' + Qa2 + ' \u2212 ' + Qa1 + ') / ' + Qa1 + ') \u00D7 100', expl: '%\u0394Qa = (' + deltaQa + ' / ' + Qa1 + ') \u00D7 100 = ' + pctQa + '%' },
                { q: 'Bereken de kruiselasticiteit (Ekr = %\u0394Qa / %\u0394Pb).', a: Ekr, hint: 'Deel %\u0394Qa door %\u0394Pb.', expl: 'Ekr = ' + pctQa + ' / ' + pctPb + ' = ' + Ekr },
                mcRelation
            ]
        };
    };

    GEN.A17 = function () {
        var Y1 = pick([1500, 2000, 2500, 3000, 4000, 5000]);
        var pctY = pick([5, 10, 20, 25]);
        var deltaY = Y1 * pctY / 100;
        if (deltaY % 1 !== 0) return GEN.A17();
        var Y2 = Y1 + deltaY;
        var Q1 = pick([40, 50, 60, 80, 100, 120, 200]);
        var pctQ = pick([-10, -5, 5, 10, 15, 20, 25, 30, 40]);
        var deltaQ = Q1 * pctQ / 100;
        if (deltaQ % 1 !== 0 || deltaQ === 0) return GEN.A17();
        var Q2 = Q1 + deltaQ;
        if (Q2 <= 0) return GEN.A17();
        var Ey = round2(pctQ / pctY);
        var good = pick(['bioscoopkaartjes', 'brood', 'tweedehands kleding', 'restaurantbezoeken', 'luxe horloges', 'biologische groenten']);
        var goodType = Ey > 1 ? 'luxe goed' : Ey > 0 ? 'normaal (noodzakelijk) goed' : 'inferieur goed';
        var mcType = mcStep(
            'Ey = ' + Ey + '. ' + good.charAt(0).toUpperCase() + good.slice(1) + ' is een\u2026',
            goodType,
            ['luxe goed', 'normaal (noodzakelijk) goed', 'inferieur goed', 'Giffen-goed'],
            'Ey > 1 \u2192 luxe, 0 < Ey < 1 \u2192 noodzakelijk, Ey < 0 \u2192 inferieur.',
            'Ey = ' + Ey + (Ey > 1 ? ' > 1 \u2192 luxe goed.' : Ey > 0 ? ', 0 < Ey < 1 \u2192 normaal (noodzakelijk) goed.' : ' < 0 \u2192 inferieur goed.')
        );
        return {
            context: 'Het inkomen stijgt van \u20AC' + Y1 + ' naar \u20AC' + Y2 + ' per maand.\nDe gevraagde hoeveelheid ' + good + ' verandert van ' + Q1 + ' naar ' + Q2 + '.\nBereken de inkomenselasticiteit.',
            steps: [
                { q: 'Bereken de procentuele inkomensverandering (%\u0394Y).', a: pctY, hint: '%\u0394Y = (\u0394Y / Y\u2081) \u00D7 100 = (' + deltaY + ' / ' + Y1 + ') \u00D7 100', expl: '%\u0394Y = (' + deltaY + ' / ' + Y1 + ') \u00D7 100 = ' + pctY + '%' },
                { q: 'Bereken de procentuele hoeveelheidsverandering (%\u0394Q).', a: pctQ, hint: '%\u0394Q = ((' + Q2 + ' \u2212 ' + Q1 + ') / ' + Q1 + ') \u00D7 100', expl: '%\u0394Q = (' + deltaQ + ' / ' + Q1 + ') \u00D7 100 = ' + pctQ + '%' },
                { q: 'Bereken de inkomenselasticiteit (Ey = %\u0394Q / %\u0394Y).', a: Ey, hint: 'Deel %\u0394Q door %\u0394Y.', expl: 'Ey = ' + pctQ + ' / ' + pctY + ' = ' + Ey },
                mcType
            ]
        };
    };

    GEN.A19 = function () {
        var b = ri(2, 4), d = ri(1, 3), Ps = ri(10, 20);
        var maxC = Math.min(d * Ps - 1, Math.floor((b + d) * Ps / 2) - 1);
        if (maxC < 2) return GEN.A19();
        var c = ri(2, maxC);
        var alpha = (b + d) * Ps - c;
        var Qs = d * Ps - c;
        if (Qs <= 2) return GEN.A19();
        var pIntercept = round1(alpha / b);
        var cs = round1(0.5 * Qs * (pIntercept - Ps));
        var mcCS = mcStep(
            'Wat is de vorm van het consumentensurplus in de grafiek?',
            'Driehoek tussen vraaglijn, prijslijn en P-as',
            ['Rechthoek onder de vraaglijn', 'Driehoek tussen aanbodlijn en prijslijn', 'Het verschil tussen vraag en aanbod'],
            'Het CS is het gebied boven de prijs en onder de vraaglijn.',
            'Het consumentensurplus is een driehoek: basis = Q*, hoogte = Pmax \u2212 P*.'
        );
        return {
            context: 'Qv = ' + alpha + ' \u2212 ' + b + 'P en Qa = \u2212' + c + ' + ' + d + 'P.\nEvenwicht: P* = ' + Ps + ', Q* = ' + Qs + '.\nBereken het consumentensurplus.',
            steps: [
                mcCS,
                { q: 'Bepaal het snijpunt van de vraaglijn met de P-as.', a: pIntercept, hint: 'Het snijpunt met de P-as vind je door Q = 0 in te vullen.', expl: 'Qv = 0 \u2192 ' + alpha + ' = ' + b + 'P \u2192 Pmax = ' + pIntercept },
                { q: 'Bereken het consumentensurplus.', a: cs, hint: 'CS is een driehoek met basis Q* en hoogte Pmax \u2212 P*.', expl: 'CS = \u00BD \u00D7 ' + Qs + ' \u00D7 (' + pIntercept + ' \u2212 ' + Ps + ') = ' + cs }
            ]
        };
    };

    GEN.A95 = function () {
        var bMO = ri(2, 6), bMK = ri(1, 4);
        var totalB = bMO + bMK;
        var Qs = ri(3, 15);
        var aMK = ri(5, 20);
        var aMO = aMK + totalB * Qs;
        return {
            context: 'MO = ' + aMO + ' \u2212 ' + bMO + 'Q en MK = ' + aMK + ' + ' + bMK + 'Q.\nBij welke Q is de winst maximaal?',
            steps: [
                { q: 'Stel MO = MK en los op. Q* = ?', a: Qs, hint: aMO + ' \u2212 ' + bMO + 'Q = ' + aMK + ' + ' + bMK + 'Q \u2192 ' + totalB + 'Q = ' + (aMO - aMK), expl: 'Q* = ' + (aMO - aMK) + ' \u00F7 ' + totalB + ' = ' + Qs }
            ]
        };
    };

    GEN.A21 = function () {
        var a = ri(40, 80), b = ri(1, 3), tkA = pick([0.5, 1, 2]), tkB = ri(5, 15), tkC = ri(50, 200);
        var Q = ri(5, 15);
        var to = round1(a * Q - b * Q * Q);
        var tk = round1(tkA * Q * Q + tkB * Q + tkC);
        var profit = round1(to - tk);
        var wrongProfit = round1(to + tk);
        var errorS3 = {
            q: 'E\u00E9n van deze winstberekeningen bevat een fout. Welke?',
            mode: 'error',
            shownSteps: [
                { text: 'Winst = TO \u2212 TK = ' + to + ' \u2212 ' + tk + ' = ' + profit, isError: false },
                { text: 'Winst = TO + TK = ' + to + ' + ' + tk + ' = ' + wrongProfit, isError: true },
                { text: 'Winst = ' + a + '\u00D7' + Q + ' \u2212 ' + b + '\u00D7' + (Q * Q) + ' \u2212 (' + tkA + '\u00D7' + (Q * Q) + ' + ' + tkB + '\u00D7' + Q + ' + ' + tkC + ') = ' + profit, isError: false }
            ],
            hint: 'Winst = TO \u2212 TK, niet TO + TK.',
            expl: 'De fout telt TO en TK op in plaats van af te trekken. Winst = TO \u2212 TK.'
        };
        // Shuffle error position
        var errS3Items = errorS3.shownSteps.slice();
        var errS3Item = errS3Items.splice(1, 1)[0];
        errS3Items.splice(ri(0, 2), 0, errS3Item);
        errorS3.shownSteps = errS3Items;
        return {
            context: 'TO = ' + a + 'Q \u2212 ' + b + 'Q\u00B2 en TK = ' + tkA + 'Q\u00B2 + ' + tkB + 'Q + ' + tkC + '.\nBereken de winst bij Q = ' + Q + '.',
            steps: [
                errorS3,
                { q: 'Bereken TO bij Q = ' + Q + '.', a: to, hint: 'TO = ' + a + 'Q \u2212 ' + b + 'Q\u00B2. Vul Q = ' + Q + ' in.', expl: 'TO = ' + a + '\u00D7' + Q + ' \u2212 ' + b + '\u00D7' + (Q * Q) + ' = ' + to },
                { q: 'Bereken TK bij Q = ' + Q + '.', a: tk, hint: 'Vul Q = ' + Q + ' in de kostenfunctie in.', expl: 'TK = ' + tkA + '\u00D7' + (Q * Q) + ' + ' + tkB + '\u00D7' + Q + ' + ' + tkC + ' = ' + tk },
                { q: 'Bereken de winst.', a: profit, hint: 'Winst = TO \u2212 TK.', expl: 'Winst = ' + to + ' \u2212 ' + tk + ' = ' + profit }
            ]
        };
    };

    GEN.A22 = function () {
        var P = ri(30, 60);
        var a = pick([0.5, 1, 2]);
        var Q1 = ri(3, 8), Q2 = ri(Q1 + 4, Q1 + 12);
        var b = round1(P - a * (Q1 + Q2));
        var c = round1(a * Q1 * Q2);
        if (b < 0) return GEN.A22();
        var orderS4 = {
            q: 'Zet de stappen voor een break-even berekening in de juiste volgorde.',
            mode: 'order',
            blocks: [
                'Stel TO = TK',
                'Herschrijf naar aQ\u00B2 + bQ + c = 0',
                'Los op met de abc-formule'
            ],
            correctOrder: [0, 1, 2],
            hint: 'Eerst gelijkstellen, dan herschrijven, dan oplossen.',
            expl: 'Stap 1: TO = TK \u2192 Stap 2: alles naar \u00E9\u00E9n kant \u2192 Stap 3: abc-formule.'
        };
        return {
            context: 'TO = ' + P + 'Q en TK = ' + a + 'Q\u00B2 + ' + b + 'Q + ' + c + '.\nBij welke hoeveelheden is er break-even?',
            steps: [
                orderS4,
                { q: 'Stel TO = TK en herschrijf naar de vorm \u2026Q\u00B2 + \u2026Q + \u2026 = 0. Wat is de co\u00EBffici\u00EBnt van Q?', a: round1(b - P), hint: P + 'Q = ' + a + 'Q\u00B2 + ' + b + 'Q + ' + c + '. Breng alles naar \u00E9\u00E9n kant.', expl: a + 'Q\u00B2 + (' + b + ' \u2212 ' + P + ')Q + ' + c + ' = 0 \u2192 co\u00EBffici\u00EBnt = ' + round1(b - P) },
                { q: 'Bereken de kleinste break-even hoeveelheid.', a: Q1, hint: 'Los de kwadratische vergelijking op met de abc-formule.', expl: 'Q\u2081 = ' + Q1 },
                { q: 'Bereken de grootste break-even hoeveelheid.', a: Q2, hint: 'De tweede oplossing van dezelfde vergelijking.', expl: 'Q\u2082 = ' + Q2 + '. Tussen Q=' + Q1 + ' en Q=' + Q2 + ' maakt het bedrijf winst.' }
            ]
        };
    };

    GEN.A23 = function () {
        var b = ri(2, 5), d = ri(1, 4), Ps = ri(10, 25);
        var maxC = Math.min(d * Ps - 1, Math.floor((b + d) * Ps / 2) - 1);
        if (maxC < 3) return GEN.A23();
        var c = ri(3, maxC);
        var alpha = (b + d) * Ps - c;
        var Qs = d * Ps - c;
        if (Qs <= 2) return GEN.A23();
        var heffing = ri(2, 8);
        var newC = c + d * heffing;
        var newPs = round1((alpha + newC) / (b + d));
        var newQs = round1(alpha - b * newPs);
        if (newQs <= 0) return GEN.A23();
        var mcS5 = mcStep(
            'Wat verandert er aan de aanbodfunctie na een heffing van \u20AC' + heffing + '?',
            'De aanbodcurve schuift omhoog (naar links)',
            ['De aanbodcurve schuift omlaag (naar rechts)', 'De vraagcurve schuift naar links', 'Beide curves schuiven'],
            'Een heffing bij de producent verhoogt de kosten per stuk.',
            'De producent ontvangt P \u2212 heffing, waardoor de aanbodcurve omhoog (naar links) schuift.'
        );
        return {
            context: 'Qv = ' + alpha + ' \u2212 ' + b + 'P en Qa = \u2212' + c + ' + ' + d + 'P.\nDe overheid heft \u20AC' + heffing + ' per stuk bij de producent.\nBereken het nieuwe evenwicht.',
            steps: [
                mcS5,
                { q: 'Wat is de nieuwe constante in de aanbodfunctie na de heffing?', a: newC, hint: 'De producent ontvangt P \u2212 ' + heffing + '. Vul dat in bij Qa.', expl: 'Qa = \u2212' + c + ' + ' + d + '(P \u2212 ' + heffing + ') = \u2212' + newC + ' + ' + d + 'P' },
                { q: 'Bereken de nieuwe evenwichtsprijs.', a: newPs, hint: 'Stel de nieuwe Qa gelijk aan Qv en los op naar P.', expl: alpha + ' \u2212 ' + b + 'P = \u2212' + newC + ' + ' + d + 'P \u2192 P* = ' + newPs },
                { q: 'Bereken de nieuwe evenwichtshoeveelheid.', a: newQs, hint: 'Vul de nieuwe P* in bij Qv.', expl: 'Q* = ' + alpha + ' \u2212 ' + b + '\u00D7' + newPs + ' = ' + newQs }
            ]
        };
    };

    GEN.A24 = function () {
        var n = ri(2, 4);
        var aInd = ri(1, 3), cInd = ri(4, 10);
        var testP = cInd + aInd * ri(2, 6);
        var qInd = (testP - cInd) / aInd;
        var qCol = n * qInd;
        var mcS6 = mcStep(
            'Hoe vind je de minimumprijs waarvoor er wordt aangeboden?',
            'Vul Qi = 0 in en los op naar P',
            ['Vul P = 0 in en los op naar Q', 'Stel Qv = Qa', 'Neem de afgeleide van de aanbodfunctie'],
            'Het aanbod begint bij de prijs waar Qi precies nul is.',
            'Qi = 0 invullen geeft de minimumprijs. Pas vanaf die prijs wordt er aangeboden.'
        );
        return {
            context: n + ' identieke bedrijven, elk met individueel aanbod: P = ' + aInd + 'Qi + ' + cInd + '.\nBepaal het collectieve aanbod.',
            steps: [
                mcS6,
                { q: 'Vanaf welke prijs wordt er aangeboden?', a: cInd, hint: 'Schrijf om naar Qi als functie van P. Bij welke P is Qi = 0?', expl: 'Qi = (P \u2212 ' + cInd + ') / ' + aInd + '. Minimumprijs = ' + cInd },
                { q: 'Bereken Qi per bedrijf bij P = ' + testP + '.', a: qInd, hint: 'Vul P = ' + testP + ' in bij Qi = (P \u2212 ' + cInd + ') / ' + aInd + '.', expl: 'Qi = (' + testP + ' \u2212 ' + cInd + ') / ' + aInd + ' = ' + qInd },
                { q: 'Bereken het collectieve aanbod bij P = ' + testP + '.', a: qCol, hint: 'Er zijn ' + n + ' identieke bedrijven.', expl: 'Qcol = ' + n + ' \u00D7 ' + qInd + ' = ' + qCol }
            ]
        };
    };

    GEN.A25 = function () {
        var b = ri(2, 5), d = ri(1, 4), Ps = ri(8, 20);
        var maxC = Math.min(d * Ps - 1, Math.floor((b + d) * Ps / 2) - 1);
        if (maxC < 2) return GEN.A25();
        var c = ri(2, maxC);
        var alpha = (b + d) * Ps - c;
        var Qs = d * Ps - c;
        if (Qs <= 2) return GEN.A25();
        var Pmin = Ps + ri(2, 6);
        var QvMin = alpha - b * Pmin;
        var QaMin = -c + d * Pmin;
        if (QvMin <= 0 || QaMin <= 0) return GEN.A25();
        var overschot = QaMin - QvMin;
        if (overschot <= 0) return GEN.A25();
        return {
            context: 'Qv = ' + alpha + ' \u2212 ' + b + 'P en Qa = \u2212' + c + ' + ' + d + 'P.\nDe overheid stelt een minimumprijs van \u20AC' + Pmin + '.\nAnalyseer het effect.',
            steps: [
                { q: 'Bereken de evenwichtsprijs zonder overheidsingrijpen.', a: Ps, hint: 'Stel Qv = Qa en los op naar P.', expl: 'P* = (' + alpha + '+' + c + ') \u00F7 ' + (b + d) + ' = ' + Ps },
                { q: 'Bereken de gevraagde hoeveelheid bij de minimumprijs.', a: QvMin, hint: 'Vul P = ' + Pmin + ' in bij Qv.', expl: 'Qv = ' + alpha + ' \u2212 ' + b + '\u00D7' + Pmin + ' = ' + QvMin },
                { q: 'Bereken de aangeboden hoeveelheid bij de minimumprijs.', a: QaMin, hint: 'Vul P = ' + Pmin + ' in bij Qa.', expl: 'Qa = \u2212' + c + ' + ' + d + '\u00D7' + Pmin + ' = ' + QaMin },
                { q: 'Bereken het overschot op de markt.', a: overschot, hint: 'Overschot = aanbod \u2212 vraag.', expl: 'Overschot = ' + QaMin + ' \u2212 ' + QvMin + ' = ' + overschot },
                mcStep(
                    'Er is een overschot van ' + overschot + ' stuks. Wat is het gevolg?',
                    'Aanbieders kunnen niet alles kwijt',
                    ['Consumenten kunnen niet genoeg kopen', 'De prijs zal dalen naar het evenwicht', 'Er ontstaat een zwarte markt met hogere prijzen'],
                    'Bij een minimumprijs is het aanbod groter dan de vraag.',
                    'Bij een overschot produceren aanbieders meer dan consumenten willen kopen.'
                )
            ]
        };
    };

    GEN.A26 = function () {
        var b = ri(2, 5), d = ri(1, 4), Ps = ri(10, 25);
        var maxC = Math.min(d * Ps - 1, Math.floor((b + d) * Ps / 2) - 1);
        if (maxC < 2) return GEN.A26();
        var c = ri(2, maxC);
        var alpha = (b + d) * Ps - c;
        var Qs = d * Ps - c;
        if (Qs <= 2) return GEN.A26();
        var Pmax = Ps - ri(2, Math.min(6, Ps - 2));
        if (Pmax <= 0) return GEN.A26();
        var QvMax = alpha - b * Pmax;
        var QaMax = -c + d * Pmax;
        if (QaMax <= 0) return GEN.A26();
        var tekort = QvMax - QaMax;
        if (tekort <= 0) return GEN.A26();
        return {
            context: 'Qv = ' + alpha + ' \u2212 ' + b + 'P en Qa = \u2212' + c + ' + ' + d + 'P.\nDe overheid stelt een maximumprijs van \u20AC' + Pmax + '.\nAnalyseer het effect.',
            steps: [
                { q: 'Bereken de evenwichtsprijs zonder overheidsingrijpen.', a: Ps, hint: 'Stel Qv = Qa en los op naar P.', expl: 'P* = (' + alpha + '+' + c + ') \u00F7 ' + (b + d) + ' = ' + Ps },
                { q: 'Bereken de gevraagde hoeveelheid bij de maximumprijs.', a: QvMax, hint: 'Vul P = ' + Pmax + ' in bij Qv.', expl: 'Qv = ' + alpha + ' \u2212 ' + b + '\u00D7' + Pmax + ' = ' + QvMax },
                { q: 'Bereken de aangeboden hoeveelheid bij de maximumprijs.', a: QaMax, hint: 'Vul P = ' + Pmax + ' in bij Qa.', expl: 'Qa = \u2212' + c + ' + ' + d + '\u00D7' + Pmax + ' = ' + QaMax },
                { q: 'Bereken het tekort op de markt.', a: tekort, hint: 'Tekort = vraag \u2212 aanbod.', expl: 'Tekort = ' + QvMax + ' \u2212 ' + QaMax + ' = ' + tekort },
                mcStep(
                    'Er is een tekort van ' + tekort + ' stuks. Wat is een waarschijnlijk gevolg?',
                    'Er kan een zwarte markt ontstaan',
                    ['De prijs daalt verder', 'Producenten gaan meer produceren', 'Het tekort lost zichzelf op'],
                    'Bij een maximumprijs is de vraag groter dan het aanbod.',
                    'Bij een tekort zijn er consumenten die meer willen betalen. Dat cre\u00EBert ruimte voor een zwarte markt.'
                )
            ]
        };
    };

    GEN.A27 = function () {
        var b = ri(2, 5), d = ri(1, 4), Ps = ri(10, 25);
        var maxC = Math.min(d * Ps - 1, Math.floor((b + d) * Ps / 2) - 1);
        if (maxC < 3) return GEN.A27();
        var c = ri(3, maxC);
        var alpha = (b + d) * Ps - c;
        var Qs = d * Ps - c;
        if (Qs <= 2) return GEN.A27();
        var subsidie = ri(2, 8);
        var newC = c - d * subsidie;
        var newPs = round1((alpha + newC) / (b + d));
        var newQs = round1(alpha - b * newPs);
        if (newQs <= 0 || newPs <= 0) return GEN.A27();
        var totaalSubsidie = round1(subsidie * newQs);
        var mcS9 = mcStep(
            'Wat verandert er aan de aanbodfunctie na een subsidie van \u20AC' + subsidie + '?',
            'De aanbodcurve schuift omlaag (naar rechts)',
            ['De aanbodcurve schuift omhoog (naar links)', 'De vraagcurve schuift naar rechts', 'De vraagcurve schuift naar links'],
            'Een subsidie verlaagt de kosten per stuk voor de producent.',
            'De producent ontvangt P + subsidie, waardoor de aanbodcurve omlaag (naar rechts) schuift.'
        );
        return {
            context: 'Qv = ' + alpha + ' \u2212 ' + b + 'P en Qa = \u2212' + c + ' + ' + d + 'P.\nDe overheid geeft een subsidie van \u20AC' + subsidie + ' per stuk aan de producent.\nBereken het nieuwe evenwicht.',
            steps: [
                mcS9,
                { q: 'Wat is de nieuwe constante in de aanbodfunctie na de subsidie?', a: newC, hint: 'De producent ontvangt P + ' + subsidie + '. Vul dat in bij Qa.', expl: 'Qa = \u2212' + c + ' + ' + d + '(P + ' + subsidie + ') = ' + newC + ' + ' + d + 'P' },
                { q: 'Bereken de nieuwe evenwichtsprijs.', a: newPs, hint: 'Stel de nieuwe Qa gelijk aan Qv en los op naar P.', expl: alpha + ' \u2212 ' + b + 'P = ' + newC + ' + ' + d + 'P \u2192 P* = ' + newPs },
                { q: 'Bereken de nieuwe evenwichtshoeveelheid.', a: newQs, hint: 'Vul de nieuwe P* in bij Qv.', expl: 'Q* = ' + alpha + ' \u2212 ' + b + '\u00D7' + newPs + ' = ' + newQs },
                { q: 'Bereken de totale subsidie-uitgaven van de overheid.', a: totaalSubsidie, hint: 'Totale subsidie = subsidie per stuk \u00D7 hoeveelheid.', expl: 'Totaal = ' + subsidie + ' \u00D7 ' + newQs + ' = ' + totaalSubsidie }
            ]
        };
    };

    GEN.A28 = function () {
        // MK = GTK oplossen: find Q where MK equals GTK
        // TK = aQ² + bQ + c → MK = 2aQ + b, GTK = aQ + b + c/Q
        // MK = GTK → 2aQ + b = aQ + b + c/Q → aQ = c/Q → Q = √(c/a)
        // Choose Q first for clean numbers: c = a × Q²
        var Qstar = ri(5, 15);
        var a = pick([0.5, 1, 1.5, 2]);
        var bk = ri(3, 12);
        var c = round1(a * Qstar * Qstar);
        // Test value for steps 1 and 2 (different from Qstar)
        var Qtest = Qstar + pick([-2, -1, 1, 2]);
        if (Qtest <= 0) Qtest = Qstar + 2;
        var mkTest = round1(2 * a * Qtest + bk);
        var gtkTest = round2(a * Qtest + bk + c / Qtest);
        var mcS10 = mcStep(
            'Wat betekent het punt waar MK = GTK economisch gezien?',
            'Het minimum van de GTK-curve (effici\u00EBnte schaal)',
            ['Het punt van maximale winst', 'Het break-even punt', 'Het punt waar de productie stopt'],
            'De MK-curve snijdt de GTK-curve altijd in het laagste punt.',
            'Waar MK = GTK bereikt de GTK zijn minimum. Dit heet de effici\u00EBnte schaal.'
        );
        return {
            context: 'TK = ' + a + 'Q\u00B2 + ' + bk + 'Q + ' + c + '.\nBij welke hoeveelheid is MK = GTK?',
            steps: [
                mcS10,
                { q: 'Stel de MK-functie op. Wat is MK bij Q = ' + Qtest + '?', a: mkTest, hint: 'MK is de afgeleide van TK. MK = ' + round1(2 * a) + 'Q + ' + bk + '.', expl: 'MK = ' + round1(2 * a) + '\u00D7' + Qtest + ' + ' + bk + ' = ' + mkTest },
                { q: 'Stel de GTK-functie op. Wat is GTK bij Q = ' + Qtest + '?', a: gtkTest, hint: 'GTK = TK/Q = ' + a + 'Q + ' + bk + ' + ' + c + '/Q.', expl: 'GTK = ' + a + '\u00D7' + Qtest + ' + ' + bk + ' + ' + c + '/' + Qtest + ' = ' + gtkTest },
                { q: 'Stel MK = GTK en los Q op.', a: Qstar, hint: round1(2 * a) + 'Q + ' + bk + ' = ' + a + 'Q + ' + bk + ' + ' + c + '/Q. Vereenvoudig: ' + a + 'Q = ' + c + '/Q.', expl: a + 'Q = ' + c + '/Q \u2192 Q\u00B2 = ' + round1(c / a) + ' \u2192 Q = ' + Qstar }
            ]
        };
    };

    GEN.A18 = function () {
        var landen = [
            ['Nederland', 'Duitsland'], ['Frankrijk', 'Spanje'],
            ['Japan', 'Zuid-Korea'], ['Belgi\u00EB', 'Denemarken']
        ];
        var producten = [
            ['kaas', 'wijn'], ['auto\u2019s', 'kleding'],
            ['elektronica', 'textiel'], ['machines', 'voedsel']
        ];
        var landPaar = pick(landen);
        var prodPaar = pick(producten);
        // Land 1 can produce maxA1 of product A or maxB1 of product B
        var maxA1 = ri(3, 12) * 10, maxB1 = ri(3, 12) * 10;
        var maxA2 = ri(3, 12) * 10, maxB2 = ri(3, 12) * 10;
        // Alternatieve kosten product A = hoeveel B je opgeeft per eenheid A
        var akA1 = round2(maxB1 / maxA1);
        var akA2 = round2(maxB2 / maxA2);
        // Ensure different comparative advantages (not equal)
        if (akA1 === akA2) return GEN.A18();
        var laagsteAK = akA1 < akA2 ? akA1 : akA2;
        return {
            context: landPaar[0] + ' kan ' + maxA1 + ' ' + prodPaar[0] + ' of ' + maxB1 + ' ' + prodPaar[1] + ' produceren.\n' + landPaar[1] + ' kan ' + maxA2 + ' ' + prodPaar[0] + ' of ' + maxB2 + ' ' + prodPaar[1] + ' produceren.\nBepaal het comparatief voordeel bij ' + prodPaar[0] + '.',
            steps: [
                { q: 'Bereken de alternatieve kosten van ' + prodPaar[0] + ' voor ' + landPaar[0] + ' (in eenheden ' + prodPaar[1] + ').', a: akA1, hint: 'Hoeveel ' + prodPaar[1] + ' geeft ' + landPaar[0] + ' op per eenheid ' + prodPaar[0] + '? Deel ' + maxB1 + ' door ' + maxA1 + '.', expl: 'AK = ' + maxB1 + ' / ' + maxA1 + ' = ' + akA1 + ' ' + prodPaar[1] + ' per ' + prodPaar[0] },
                { q: 'Bereken de alternatieve kosten van ' + prodPaar[0] + ' voor ' + landPaar[1] + ' (in eenheden ' + prodPaar[1] + ').', a: akA2, hint: 'Hoeveel ' + prodPaar[1] + ' geeft ' + landPaar[1] + ' op per eenheid ' + prodPaar[0] + '? Deel ' + maxB2 + ' door ' + maxA2 + '.', expl: 'AK = ' + maxB2 + ' / ' + maxA2 + ' = ' + akA2 + ' ' + prodPaar[1] + ' per ' + prodPaar[0] },
                { q: 'Wat zijn de laagste alternatieve kosten? (het land met comparatief voordeel)', a: laagsteAK, hint: 'Vergelijk de twee alternatieve kosten. De laagste wint.', expl: 'Laagste AK = ' + laagsteAK + ', dus ' + (akA1 < akA2 ? landPaar[0] : landPaar[1]) + ' heeft het comparatief voordeel bij ' + prodPaar[0] + '.' },
                mcStep(
                    'Welk land moet zich specialiseren in ' + prodPaar[0] + '?',
                    akA1 < akA2 ? landPaar[0] : landPaar[1],
                    [landPaar[0], landPaar[1], 'Beide landen', 'Geen van beide'],
                    'Het land met de laagste alternatieve kosten specialiseert zich.',
                    (akA1 < akA2 ? landPaar[0] : landPaar[1]) + ' heeft de laagste AK (' + laagsteAK + ') en specialiseert zich dus in ' + prodPaar[0] + '.'
                )
            ]
        };
    };

    /* ── Eindbazen ──────────────────────────────────────────── */

    GEN.A29 = function () {
        var P = ri(40, 70);
        var a = pick([0.5, 1, 2]);
        var Q1 = ri(3, 8), Q2 = ri(Q1 + 5, Q1 + 15);
        var b = round1(P - a * (Q1 + Q2));
        var c = round1(a * Q1 * Q2);
        if (b < 0) return GEN.A29();
        var Qmid = Math.round((Q1 + Q2) / 2);
        var profitMid = round1(P * Qmid - (a * Qmid * Qmid + b * Qmid + c));
        var orderE1 = {
            q: 'Zet de stappen van een volledige break-even analyse in de juiste volgorde.',
            mode: 'order',
            blocks: [
                'Stel TO = TK op',
                'Herschrijf naar aQ\u00B2 + bQ + c = 0',
                'Bereken break-even Q met abc-formule',
                'Bereken de winst bij een gegeven Q'
            ],
            correctOrder: [0, 1, 2, 3],
            hint: 'Eerst opstellen, dan herschrijven, dan oplossen, dan interpreteren.',
            expl: 'TO = TK \u2192 herschrijven \u2192 abc-formule \u2192 winst bij specifiek punt.'
        };
        return {
            context: 'Een producent verkoopt voor P = ' + P + '.\nTK = ' + a + 'Q\u00B2 + ' + b + 'Q + ' + c + '.\nVoer een volledige break-even analyse uit.',
            steps: [
                orderE1,
                { q: 'Stel TO = TK en herschrijf naar \u2026Q\u00B2 + \u2026Q + \u2026 = 0. Wat is de co\u00EBffici\u00EBnt van Q?', a: round1(b - P), hint: P + 'Q = ' + a + 'Q\u00B2 + ' + b + 'Q + ' + c + '. Breng alles naar \u00E9\u00E9n kant.', expl: a + 'Q\u00B2 + (' + b + ' \u2212 ' + P + ')Q + ' + c + ' = 0 \u2192 co\u00EBffici\u00EBnt = ' + round1(b - P) },
                { q: 'Bereken de kleinste break-even hoeveelheid.', a: Q1, hint: 'Gebruik de abc-formule.', expl: 'Q\u2081 = ' + Q1 },
                { q: 'Bereken de grootste break-even hoeveelheid.', a: Q2, hint: 'De tweede oplossing van dezelfde vergelijking.', expl: 'Q\u2082 = ' + Q2 },
                { q: 'Bereken de winst bij Q = ' + Qmid + '.', a: profitMid, hint: 'Winst = TO \u2212 TK. Bereken beide bij Q = ' + Qmid + '.', expl: 'TO = ' + (P * Qmid) + ', TK = ' + round1(a * Qmid * Qmid + b * Qmid + c) + ', Winst = ' + profitMid }
            ]
        };
    };

    GEN.A30 = function () {
        var b = ri(2, 5), d = ri(1, 4);
        var Ps = ri(8, 20);
        var maxC = Math.min(d * Ps - 2, Math.floor((b + d) * Ps / 2) - 1);
        if (maxC < 2) return GEN.A30();
        var c = ri(2, maxC);
        var alpha = (b + d) * Ps - c;
        var Qs = d * Ps - c;
        if (Qs <= 2) return GEN.A30();
        var pMax = round1(alpha / b);
        var cs = round1(0.5 * Qs * (pMax - Ps));
        return {
            context: 'Qv = ' + alpha + ' \u2212 ' + b + 'P en Qa = \u2212' + c + ' + ' + d + 'P.\nBereken het consumentensurplus volledig.',
            steps: [
                { q: 'Bereken de evenwichtsprijs.', a: Ps, hint: 'Stel Qv = Qa en los op naar P.', expl: 'P* = (' + alpha + '+' + c + ') \u00F7 ' + (b + d) + ' = ' + Ps },
                { q: 'Bereken de evenwichtshoeveelheid.', a: Qs, hint: 'Vul P* in bij Qv of Qa.', expl: 'Q* = ' + alpha + ' \u2212 ' + b + '\u00D7' + Ps + ' = ' + Qs },
                { q: 'Bepaal het snijpunt van de vraaglijn met de P-as.', a: pMax, hint: 'Bij welke prijs is de gevraagde hoeveelheid nul?', expl: 'Q = 0 \u2192 ' + alpha + ' = ' + b + 'P \u2192 Pmax = ' + pMax },
                (function () {
                    var wrongCS = round1(0.5 * Ps * (pMax - Qs));
                    var errE2 = {
                        q: 'E\u00E9n van deze CS-berekeningen bevat een fout. Welke?',
                        mode: 'error',
                        shownSteps: [
                            { text: 'CS = \u00BD \u00D7 ' + Qs + ' \u00D7 (' + pMax + ' \u2212 ' + Ps + ') = ' + cs, isError: false },
                            { text: 'CS = \u00BD \u00D7 ' + Ps + ' \u00D7 (' + pMax + ' \u2212 ' + Qs + ') = ' + wrongCS, isError: true },
                            { text: 'CS = \u00BD \u00D7 Q* \u00D7 (Pmax \u2212 P*) = \u00BD \u00D7 ' + Qs + ' \u00D7 ' + round1(pMax - Ps) + ' = ' + cs, isError: false }
                        ],
                        hint: 'De basis van de driehoek is Q*, de hoogte is Pmax \u2212 P*.',
                        expl: 'De fout verwisselt Q* en P* in de formule. De basis is altijd de hoeveelheid.'
                    };
                    var items = errE2.shownSteps.slice();
                    var item = items.splice(1, 1)[0];
                    items.splice(ri(0, 2), 0, item);
                    errE2.shownSteps = items;
                    return errE2;
                })(),
                { q: 'Bereken het consumentensurplus.', a: cs, hint: 'CS is een driehoek met basis Q* en hoogte Pmax \u2212 P*.', expl: 'CS = \u00BD \u00D7 ' + Qs + ' \u00D7 (' + pMax + ' \u2212 ' + Ps + ') = ' + cs }
            ]
        };
    };

    GEN.A31 = function () {
        var n1 = ri(2, 3), n2 = ri(1, 2);
        var a1 = pick([1, 2]), c1 = ri(4, 10);
        var a2 = pick([1, 2, 3]), c2 = ri(6, 14);
        var testP = Math.max(c1, c2) + ri(4, 10);
        var q1 = round1((testP - c1) / a1);
        var q2 = round1((testP - c2) / a2);
        var qTot = round1(n1 * q1 + (testP >= c2 ? n2 * q2 : 0));
        var orderE3 = {
            q: 'Zet de stappen voor het bepalen van het collectieve aanbod in de juiste volgorde.',
            mode: 'order',
            blocks: [
                'Bereken het aanbod per bedrijf bij de gegeven prijs',
                'Vermenigvuldig met het aantal bedrijven per groep',
                'Tel het aanbod van alle groepen bij elkaar op'
            ],
            correctOrder: [0, 1, 2],
            hint: 'Eerst individueel, dan per groep, dan totaal.',
            expl: 'Stap 1: Q per bedrijf \u2192 Stap 2: \u00D7 aantal bedrijven \u2192 Stap 3: groepen optellen.'
        };
        return {
            context: 'Groep A: ' + n1 + ' bedrijven, elk P = ' + a1 + 'Q + ' + c1 + '\nGroep B: ' + n2 + ' bedrijf(ven), elk P = ' + a2 + 'Q + ' + c2 + '\nBepaal het collectieve aanbod.',
            steps: [
                orderE3,
                { q: 'Bereken het aanbod per bedrijf van groep A bij P = ' + testP + '.', a: q1, hint: 'Schrijf om: Qa = (P \u2212 ' + c1 + ') / ' + a1 + '. Vul P in.', expl: 'Qa = (' + testP + ' \u2212 ' + c1 + ') / ' + a1 + ' = ' + q1 },
                { q: 'Bereken het totale aanbod van groep A.', a: round1(n1 * q1), hint: 'Er zijn ' + n1 + ' bedrijven in groep A.', expl: n1 + ' \u00D7 ' + q1 + ' = ' + round1(n1 * q1) },
                { q: 'Bereken het aanbod per bedrijf van groep B bij P = ' + testP + '.', a: q2, hint: 'Schrijf om: Qb = (P \u2212 ' + c2 + ') / ' + a2 + '. Vul P in.', expl: 'Qb = (' + testP + ' \u2212 ' + c2 + ') / ' + a2 + ' = ' + q2 },
                { q: 'Bereken het totale collectieve aanbod.', a: qTot, hint: 'Tel het totale aanbod van beide groepen op.', expl: 'Qcol = ' + round1(n1 * q1) + ' + ' + round1(n2 * q2) + ' = ' + qTot }
            ]
        };
    };

    GEN.A32 = function () {
        var b = ri(2, 4), d = ri(1, 3);
        var Ps = ri(10, 20), heffing = ri(3, 8);
        var maxC = Math.min(d * Ps - 2, Math.floor((b + d) * Ps / 2) - 1);
        if (maxC < 3) return GEN.A32();
        var c = ri(3, maxC);
        var alpha = (b + d) * Ps - c;
        var Qs = d * Ps - c;
        if (Qs <= 5) return GEN.A32();
        var newC = c + d * heffing;
        var Pn = round1((alpha + newC) / (b + d));
        var Qn = round1(alpha - b * Pn);
        if (Qn <= 0) return GEN.A32();
        var dwl = round1(0.5 * (Qs - Qn) * heffing);
        var orderE4 = {
            q: 'Zet de stappen voor het berekenen van het welvaartsverlies in de juiste volgorde.',
            mode: 'order',
            blocks: [
                'Bereken het oude evenwicht',
                'Pas de aanbodfunctie aan voor de heffing',
                'Bereken het nieuwe evenwicht',
                'Bereken het welvaartsverlies als driehoek'
            ],
            correctOrder: [0, 1, 2, 3],
            hint: 'Je moet eerst beide evenwichten kennen voordat je het verschil kunt berekenen.',
            expl: 'Oud evenwicht \u2192 aanpassen aanbod \u2192 nieuw evenwicht \u2192 DWL = \u00BD \u00D7 \u0394Q \u00D7 heffing.'
        };
        return {
            context: 'Qv = ' + alpha + ' \u2212 ' + b + 'P, Qa = \u2212' + c + ' + ' + d + 'P.\nHeffing: \u20AC' + heffing + '/stuk.\nBereken het welvaartsverlies.',
            steps: [
                orderE4,
                { q: 'Bereken de oude evenwichtsprijs.', a: Ps, hint: 'Stel Qv = Qa en los op naar P.', expl: 'P* = (' + alpha + '+' + c + ') \u00F7 ' + (b + d) + ' = ' + Ps },
                { q: 'Bereken de oude evenwichtshoeveelheid.', a: Qs, hint: 'Vul P* in bij Qv.', expl: 'Q* = ' + alpha + ' \u2212 ' + b + '\u00D7' + Ps + ' = ' + Qs },
                { q: 'Wat is de nieuwe constante in Qa na de heffing?', a: newC, hint: 'De producent ontvangt P \u2212 ' + heffing + '. Vul dat in.', expl: 'Qa = \u2212' + c + ' + ' + d + '(P \u2212 ' + heffing + ') \u2192 constante = ' + newC },
                { q: 'Bereken de nieuwe evenwichtsprijs.', a: Pn, hint: 'Stel de nieuwe Qa gelijk aan Qv en los op.', expl: 'P_nieuw = (' + alpha + '+' + newC + ') \u00F7 ' + (b + d) + ' = ' + Pn },
                { q: 'Bereken de nieuwe evenwichtshoeveelheid.', a: Qn, hint: 'Vul de nieuwe P* in bij Qv.', expl: 'Q_nieuw = ' + alpha + ' \u2212 ' + b + '\u00D7' + Pn + ' = ' + Qn },
                { q: 'Bereken het welvaartsverlies.', a: dwl, hint: 'Het welvaartsverlies is een driehoek. Wat zijn de basis en hoogte?', expl: 'DWL = \u00BD \u00D7 (' + Qs + ' \u2212 ' + round1(Qn) + ') \u00D7 ' + heffing + ' = ' + dwl }
            ]
        };
    };

    GEN.A33 = function () {
        var P = ri(25, 50);
        var a = pick([0.5, 1, 1.5, 2]), bk = ri(3, 12), ck = ri(50, 200);
        var Qs = round1((P - bk) / (2 * a));
        if (Qs <= 0 || Qs !== Math.round(Qs * 10) / 10) return GEN.A33();
        var tk = round1(a * Qs * Qs + bk * Qs + ck);
        var gtk = round2(tk / Qs);
        var profitPerUnit = round2(P - gtk);
        var totalProfit = round1(profitPerUnit * Qs);
        var mcE5 = mcStep(
            'Wat is de voorwaarde voor optimale productie bij volkomen mededinging?',
            'P = MK',
            ['MO = MK', 'P = GTK', 'TO = TK'],
            'Bij VM is de prijs gegeven. De producent is een prijsnemer.',
            'Bij VM geldt P = MO (horizontale vraaglijn). Dus MO = MK wordt P = MK.'
        );
        return {
            context: 'Marktprijs P = ' + P + ' (volledige mededinging).\nTK = ' + a + 'Q\u00B2 + ' + bk + 'Q + ' + ck + '.\nBepaal de optimale productie en winst.',
            steps: [
                mcE5,
                { q: 'Bepaal de optimale productiehoeveelheid Q*.', a: Qs, hint: 'Bij volledige mededinging geldt: P = MK. Bepaal eerst MK.', expl: 'MK = ' + round1(2 * a) + 'Q + ' + bk + '. P = MK \u2192 Q* = (' + P + ' \u2212 ' + bk + ') \u00F7 ' + round1(2 * a) + ' = ' + Qs },
                { q: 'Bereken TK bij de optimale hoeveelheid.', a: tk, hint: 'Vul Q* = ' + Qs + ' in de kostenfunctie in.', expl: 'TK = ' + a + '\u00D7' + Qs + '\u00B2 + ' + bk + '\u00D7' + Qs + ' + ' + ck + ' = ' + tk },
                { q: 'Bereken GTK bij de optimale hoeveelheid.', a: gtk, hint: 'GTK = TK gedeeld door Q.', expl: 'GTK = ' + tk + ' \u00F7 ' + Qs + ' = ' + gtk },
                { q: 'Bereken de winst per stuk.', a: profitPerUnit, hint: 'Winst per stuk = prijs minus gemiddelde kosten.', expl: 'Winst/stuk = ' + P + ' \u2212 ' + gtk + ' = ' + profitPerUnit },
                { q: 'Bereken de totale winst.', a: totalProfit, hint: 'Totale winst = winst per stuk \u00D7 hoeveelheid.', expl: 'Totale winst = ' + profitPerUnit + ' \u00D7 ' + Qs + ' = ' + totalProfit }
            ]
        };
    };

    GEN.A34 = function () {
        var b = ri(2, 4), d = ri(1, 3);
        var Ps = ri(15, 25);
        var c = ri(5, d * Ps - 2);
        var a = (b + d) * Ps + c;
        var Qs = a - b * Ps;
        var Pw = Ps - ri(3, 7);
        var Qd = a - b * Pw;
        var Qsup = Math.max(0, -c + d * Pw);
        var importR = ri(2, 5);
        var QdNew = a - b * (Pw + importR);
        var QsupNew = Math.max(0, -c + d * (Pw + importR));
        var govRev = round1(importR * (QdNew - QsupNew));
        if (Qsup < 0 || QsupNew < 0 || QdNew <= QsupNew) return GEN.A34();
        var orderE6 = {
            q: 'Zet de analysestappen voor een invoerrecht in de juiste volgorde.',
            mode: 'order',
            blocks: [
                'Bereken vraag en aanbod bij de wereldmarktprijs',
                'Bereken de import zonder invoerrecht',
                'Bereken vraag en aanbod bij Pw + invoerrecht',
                'Bereken de overheidsinkomsten'
            ],
            correctOrder: [0, 1, 2, 3],
            hint: 'Begin met de situatie zonder ingrijpen, dan met invoerrecht.',
            expl: 'Uitgangssituatie \u2192 import berekenen \u2192 nieuwe situatie \u2192 overheidsinkomsten.'
        };
        return {
            context: 'Qv = ' + a + ' \u2212 ' + b + 'P, Qa = \u2212' + c + ' + ' + d + 'P.\nWereldmarktprijs Pw = ' + Pw + '. Invoerrecht: \u20AC' + importR + '/stuk.\nAnalyseer de effecten.',
            steps: [
                orderE6,
                { q: 'Bereken de binnenlandse vraag bij de wereldmarktprijs.', a: Qd, hint: 'Vul Pw = ' + Pw + ' in bij Qv.', expl: 'Qd = ' + a + ' \u2212 ' + b + '\u00D7' + Pw + ' = ' + Qd },
                { q: 'Bereken het binnenlandse aanbod bij de wereldmarktprijs.', a: Qsup, hint: 'Vul Pw = ' + Pw + ' in bij Qa.', expl: 'Qs = \u2212' + c + ' + ' + d + '\u00D7' + Pw + ' = ' + Qsup },
                { q: 'Hoeveel wordt er ge\u00EFmporteerd zonder invoerrecht?', a: Qd - Qsup, hint: 'Import = binnenlandse vraag \u2212 binnenlands aanbod.', expl: 'Import = ' + Qd + ' \u2212 ' + Qsup + ' = ' + (Qd - Qsup) },
                { q: 'Wat is de nieuwe binnenlandse prijs na het invoerrecht?', a: Pw + importR, hint: 'Het invoerrecht wordt opgeteld bij de wereldmarktprijs.', expl: 'P_nieuw = ' + Pw + ' + ' + importR + ' = ' + (Pw + importR) },
                { q: 'Hoeveel wordt er ge\u00EFmporteerd m\u00E9t invoerrecht?', a: QdNew - QsupNew, hint: 'Bereken vraag en aanbod bij de nieuwe prijs en trek af.', expl: 'Import = ' + QdNew + ' \u2212 ' + QsupNew + ' = ' + (QdNew - QsupNew) },
                { q: 'Bereken de overheidsinkomsten uit het invoerrecht.', a: govRev, hint: 'Overheidsinkomsten = tarief \u00D7 ge\u00EFmporteerde hoeveelheid.', expl: importR + ' \u00D7 ' + (QdNew - QsupNew) + ' = ' + govRev }
            ]
        };
    };

    GEN.A35 = function () {
        var aP = ri(60, 120), bP = ri(1, 4);
        var aTK = pick([0.5, 1, 2]), bTK = ri(5, 20), cTK = ri(50, 200);
        var Qs = round1((aP - bTK) / (2 * bP + 2 * aTK));
        if (Qs <= 0 || Qs !== Math.round(Qs * 10) / 10) return GEN.A35();
        var Pstar = round1(aP - bP * Qs);
        var TO = round1(Pstar * Qs);
        var TK = round1(aTK * Qs * Qs + bTK * Qs + cTK);
        var profit = round1(TO - TK);
        var wrongQs = round1(aP / (2 * bP));
        var errorE7 = {
            q: 'E\u00E9n van deze methoden voor winstmaximalisatie bevat een fout. Welke?',
            mode: 'error',
            shownSteps: [
                { text: 'MO = MK: ' + aP + ' \u2212 ' + (2 * bP) + 'Q = ' + round1(2 * aTK) + 'Q + ' + bTK + ' \u2192 Q = ' + Qs, isError: false },
                { text: 'MO = 0: ' + aP + ' \u2212 ' + (2 * bP) + 'Q = 0 \u2192 Q = ' + wrongQs, isError: true },
                { text: 'MO = ' + aP + ' \u2212 ' + (2 * bP) + 'Q en MK = ' + round1(2 * aTK) + 'Q + ' + bTK, isError: false }
            ],
            hint: 'De monopolist maximaliseert winst bij MO = MK, niet bij MO = 0.',
            expl: 'MO = 0 geeft de opbrengstmaximaliserende hoeveelheid, niet de winstmaximaliserende.'
        };
        var errE7Items = errorE7.shownSteps.slice();
        var errE7Item = errE7Items.splice(1, 1)[0];
        errE7Items.splice(ri(0, 2), 0, errE7Item);
        errorE7.shownSteps = errE7Items;
        return {
            context: 'Monopolist: P = ' + aP + ' \u2212 ' + bP + 'Q.\nTK = ' + aTK + 'Q\u00B2 + ' + bTK + 'Q + ' + cTK + '.\nBepaal de maximale winst.',
            steps: [
                errorE7,
                { q: 'Bepaal de winstmaximaliserende hoeveelheid Q*.', a: Qs, hint: 'Stel MO = MK. Bepaal eerst MO en MK uit de gegeven functies.', expl: 'MO = ' + aP + ' \u2212 ' + (2 * bP) + 'Q, MK = ' + round1(2 * aTK) + 'Q + ' + bTK + '. MO = MK \u2192 Q* = ' + Qs },
                { q: 'Bereken de prijs die de monopolist vraagt.', a: Pstar, hint: 'Vul Q* in de vraaglijn (P = \u2026).', expl: 'P* = ' + aP + ' \u2212 ' + bP + '\u00D7' + Qs + ' = ' + Pstar },
                { q: 'Bereken de totale opbrengst.', a: TO, hint: 'TO = P* \u00D7 Q*.', expl: 'TO = ' + Pstar + ' \u00D7 ' + Qs + ' = ' + TO },
                { q: 'Bereken de totale kosten bij Q*.', a: TK, hint: 'Vul Q* in de kostenfunctie.', expl: 'TK = ' + aTK + '\u00D7' + Qs + '\u00B2 + ' + bTK + '\u00D7' + Qs + ' + ' + cTK + ' = ' + TK },
                { q: 'Bereken de maximale winst.', a: profit, hint: 'Winst = TO \u2212 TK.', expl: 'Winst = ' + TO + ' \u2212 ' + TK + ' = ' + profit }
            ]
        };
    };

    GEN.A36 = function () {
        var a1 = ri(60, 100), b1 = ri(1, 3);
        var a2 = ri(80, 140), b2 = ri(2, 5);
        var mk = ri(10, 25);
        var Q1 = round1((a1 - mk) / (2 * b1));
        var Q2 = round1((a2 - mk) / (2 * b2));
        if (Q1 <= 0 || Q2 <= 0) return GEN.A36();
        var P1 = round1(a1 - b1 * Q1);
        var P2 = round1(a2 - b2 * Q2);
        var profit1 = round1((P1 - mk) * Q1);
        var profit2 = round1((P2 - mk) * Q2);
        var totalProfit = round1(profit1 + profit2);
        var orderE8 = {
            q: 'Zet de stappen voor prijsdiscriminatie in de juiste volgorde.',
            mode: 'order',
            blocks: [
                'Stel MO = MK op voor elke markt apart',
                'Bereken Q* per markt',
                'Bepaal de prijs per markt via de vraaglijn',
                'Bereken de winst per markt en tel op'
            ],
            correctOrder: [0, 1, 2, 3],
            hint: 'Bij prijsdiscriminatie optimaliseer je elke markt apart.',
            expl: 'Per markt: MO = MK \u2192 Q* \u2192 P* \u2192 winst. Totaal = som van deelmarkten.'
        };
        return {
            context: 'Prijsdiscriminatie. MK = ' + mk + ' (constant).\nMarkt 1: P\u2081 = ' + a1 + ' \u2212 ' + b1 + 'Q\u2081\nMarkt 2: P\u2082 = ' + a2 + ' \u2212 ' + b2 + 'Q\u2082',
            steps: [
                orderE8,
                { q: 'Bepaal de optimale hoeveelheid op markt 1.', a: Q1, hint: 'Stel MO\u2081 = MK en los op. MO\u2081 is de afgeleide van TO\u2081.', expl: 'MO\u2081 = ' + a1 + ' \u2212 ' + (2 * b1) + 'Q\u2081 = ' + mk + ' \u2192 Q\u2081 = ' + Q1 },
                { q: 'Welke prijs vraagt de monopolist op markt 1?', a: P1, hint: 'Vul Q\u2081 in de vraagfunctie van markt 1.', expl: 'P\u2081 = ' + a1 + ' \u2212 ' + b1 + '\u00D7' + Q1 + ' = ' + P1 },
                { q: 'Bepaal de optimale hoeveelheid op markt 2.', a: Q2, hint: 'Stel MO\u2082 = MK en los op.', expl: 'MO\u2082 = ' + a2 + ' \u2212 ' + (2 * b2) + 'Q\u2082 = ' + mk + ' \u2192 Q\u2082 = ' + Q2 },
                { q: 'Welke prijs vraagt de monopolist op markt 2?', a: P2, hint: 'Vul Q\u2082 in de vraagfunctie van markt 2.', expl: 'P\u2082 = ' + a2 + ' \u2212 ' + b2 + '\u00D7' + Q2 + ' = ' + P2 },
                { q: 'Bereken de winst op markt 1.', a: profit1, hint: 'Winst = (prijs \u2212 MK) \u00D7 hoeveelheid.', expl: 'Winst\u2081 = (' + P1 + ' \u2212 ' + mk + ') \u00D7 ' + Q1 + ' = ' + profit1 },
                { q: 'Bereken de winst op markt 2.', a: profit2, hint: 'Winst = (prijs \u2212 MK) \u00D7 hoeveelheid.', expl: 'Winst\u2082 = (' + P2 + ' \u2212 ' + mk + ') \u00D7 ' + Q2 + ' = ' + profit2 },
                { q: 'Bereken de totale winst.', a: totalProfit, hint: 'Tel de winst van beide markten op.', expl: 'Totaal = ' + profit1 + ' + ' + profit2 + ' = ' + totalProfit }
            ]
        };
    };

    GEN.A37 = function () {
        // Lange-termijnevenwicht VM: MK = GTK → find Q, then price, verify profit = 0
        // Same number strategy as S10: Q first, c = a × Q²
        var Qstar = ri(5, 15);
        var a = pick([0.5, 1, 1.5, 2]);
        var bk = ri(3, 12);
        var c = round1(a * Qstar * Qstar);
        var mkStar = round1(2 * a * Qstar + bk);
        var gtkStar = round2(a * Qstar + bk + c / Qstar);
        // At MK = GTK, price = MK = GTK (by definition), so profit = 0
        return {
            context: 'Volkomen mededinging, lange termijn.\nTK = ' + a + 'Q\u00B2 + ' + bk + 'Q + ' + c + '.\nBepaal het lange-termijnevenwicht.',
            steps: [
                { q: 'Stel MK = GTK en los Q op.', a: Qstar, hint: 'MK = ' + round1(2 * a) + 'Q + ' + bk + ', GTK = ' + a + 'Q + ' + bk + ' + ' + c + '/Q. Stel gelijk en vereenvoudig.', expl: a + 'Q = ' + c + '/Q \u2192 Q\u00B2 = ' + round1(c / a) + ' \u2192 Q* = ' + Qstar },
                { q: 'Bereken MK bij Q* = ' + Qstar + '.', a: mkStar, hint: 'MK = ' + round1(2 * a) + 'Q + ' + bk + '. Vul Q* in.', expl: 'MK = ' + round1(2 * a) + '\u00D7' + Qstar + ' + ' + bk + ' = ' + mkStar },
                { q: 'Wat is de lange-termijn evenwichtsprijs?', a: mkStar, hint: 'Op lange termijn bij VM geldt: P = MK = GTK.', expl: 'P = MK(Q*) = ' + mkStar },
                { q: 'Bereken GTK bij Q* (ter verificatie).', a: gtkStar, hint: 'GTK = ' + a + 'Q + ' + bk + ' + ' + c + '/Q. Vul Q* = ' + Qstar + ' in.', expl: 'GTK = ' + a + '\u00D7' + Qstar + ' + ' + bk + ' + ' + c + '/' + Qstar + ' = ' + gtkStar + ' \u2248 P \u2713' },
                { q: 'Wat is de winst per stuk op lange termijn?', a: 0, hint: 'Bij lange-termijnevenwicht bij VM geldt P = GTK.', expl: 'Winst/stuk = P \u2212 GTK = ' + mkStar + ' \u2212 ' + gtkStar + ' \u2248 0 (afrondingsverschil)' },
                mcStep(
                    'De economische winst is nul. Waarom blijven bedrijven toch produceren?',
                    'Ze maken normale winst (ondernemersbeloning zit in de kosten)',
                    ['Ze hopen dat de prijs stijgt', 'Ze zijn verplicht om door te gaan', 'Ze maken eigenlijk wel winst maar die is verborgen'],
                    'Denk aan het verschil tussen economische winst en boekhoudkundige winst.',
                    'Bij economische winst = 0 is de ondernemersbeloning al verrekend in TK. Het bedrijf maakt "normale winst".'
                )
            ]
        };
    };

    GEN.A38 = function () {
        var oldValue = ri(50, 200);
        var pct = pick([-25, -20, -10, -5, 5, 10, 20, 25]);
        var newValue = round1(oldValue * (1 + pct / 100));
        var diff = round1(newValue - oldValue);
        var pctText = String(pct);
        var pctComma = pctText.replace('.', ',');
        return {
            context: 'Een waarde verandert van ' + oldValue + ' naar ' + newValue + '. Bereken de procentuele verandering.',
            steps: [
                {
                    q: 'Bereken nieuw minus oud.',
                    mode: 'task_shell',
                    hint: 'Trek de oude waarde af van de nieuwe waarde.',
                    expl: 'Verschil = ' + newValue + ' - ' + oldValue + ' = ' + diff + '.',
                    taskShell: {
                        id: 'a38-difference',
                        family: 'numeric_input',
                        skillLabel: 'Verschil berekenen',
                        purpose: 'Bepaal eerst de verandering in dezelfde eenheid als de bron.',
                        prompt: 'Bereken nieuw minus oud.',
                        interaction: { inputLabel: 'Verschil', placeholder: 'Bijvoorbeeld -10' },
                        expected: { kind: 'number', value: diff, tolerance: Math.max(0.05, Math.abs(diff) * 0.01) },
                        feedback: {
                            matchTitle: 'Verschil klopt',
                            matchText: 'Je hebt nieuw en oud in de juiste volgorde afgetrokken.',
                            retryTitle: 'Controleer de volgorde',
                            retryText: 'Gebruik nieuw min oud: ' + newValue + ' - ' + oldValue + '.'
                        },
                        practiceRoute: { label: 'Terug naar rekenroute', href: '#skilltree-app' }
                    }
                },
                {
                    q: 'Laat de berekening van de procentuele verandering zien.',
                    mode: 'task_shell',
                    hint: 'Gebruik: (nieuw - oud) / oud x 100.',
                    expl: '(' + diff + ' / ' + oldValue + ') x 100 = ' + pct + '%.',
                    taskShell: {
                        id: 'a38-work',
                        family: 'calculation_work_capture',
                        skillLabel: 'Procentuele verandering',
                        purpose: 'Maak je rekenwerk controleerbaar met formule, invulling en antwoord.',
                        prompt: 'Laat de berekening van de procentuele verandering zien.',
                        interaction: {
                            workLabel: 'Berekening',
                            finalAnswerLabel: 'Eindantwoord met procentteken',
                            finalAnswerPlaceholder: 'Bijvoorbeeld ' + pctText + '%'
                        },
                        expected: {
                            kind: 'self_check',
                            criteria: [
                                'Je gebruikt (nieuw - oud) / oud x 100.',
                                'Oud = ' + oldValue + ' en nieuw = ' + newValue + ' staan zichtbaar in je berekening.',
                                'Je eindantwoord heeft een procentteken.'
                            ]
                        },
                        feedback: {
                            selfCheckTitle: 'Vergelijk je berekening',
                            selfCheckText: 'Loop formule, invulling en procentteken na voordat je verder gaat.',
                            retryTitle: 'Schrijf eerst je uitwerking',
                            retryText: 'Noteer formule, waarden en eindantwoord zodat je jezelf kunt controleren.'
                        },
                        practiceRoute: { label: 'Terug naar rekenroute', href: '#skilltree-app' }
                    }
                },
                {
                    q: 'Geef het eindantwoord met procentteken.',
                    mode: 'task_shell',
                    hint: 'Schrijf de uitkomst als percentage.',
                    expl: 'De procentuele verandering is ' + pct + '%.',
                    taskShell: {
                        id: 'a38-final-answer',
                        family: 'final_answer_entry',
                        skillLabel: 'Eindantwoord noteren',
                        purpose: 'Sluit de berekening af met de juiste notatie.',
                        prompt: 'Geef het eindantwoord met procentteken.',
                        interaction: { inputLabel: 'Eindantwoord', placeholder: pctText + '%' },
                        expected: { kind: 'text', accepted: [pctText + '%', pctText + ' %', pctComma + '%', pctComma + ' %'] },
                        feedback: {
                            matchTitle: 'Antwoord met notatie klopt',
                            matchText: 'Je antwoord bevat de berekende procentuele verandering en het procentteken.',
                            retryTitle: 'Controleer getal en teken',
                            retryText: 'Gebruik de uitkomst van je berekening en zet er een procentteken achter.'
                        },
                        practiceRoute: { label: 'Terug naar rekenroute', href: '#skilltree-app' }
                    }
                },
                {
                    q: 'Welke notatie hoort achter een procentuele verandering?',
                    mode: 'task_shell',
                    hint: 'Een procentuele verandering noteer je als percentage.',
                    expl: 'Achter een procentuele verandering zet je %.',
                    taskShell: {
                        id: 'a38-notation',
                        family: 'unit_notation_field',
                        skillLabel: 'Procentnotatie',
                        purpose: 'Controleer dat je de juiste notatie gebruikt.',
                        prompt: 'Welke notatie hoort achter een procentuele verandering?',
                        interaction: { inputLabel: 'Notatie', placeholder: 'Bijvoorbeeld %' },
                        expected: { kind: 'text', accepted: ['%', 'procent', 'procentteken'] },
                        feedback: {
                            matchTitle: 'Juiste notatie',
                            matchText: 'Een procentuele verandering noteer je met een procentteken.',
                            retryTitle: 'Kies de procentnotatie',
                            retryText: 'Een verandering in procenten krijgt het teken %.'
                        },
                        practiceRoute: { label: 'Terug naar rekenroute', href: '#skilltree-app' }
                    }
                }
            ]
        };
    };

    GEN.A39 = function () {
        var basePrice = ri(40, 120);
        var index = pick([85, 90, 95, 105, 110, 115, 120, 125]);
        var currentPrice = round1(basePrice * index / 100);
        var previousIndex = pick([90, 95, 100, 105, 110]);
        if (previousIndex === index) previousIndex += 5;
        var inflation = round2((index - previousIndex) / previousIndex * 100);
        var inflationText = String(inflation);
        var inflationComma = inflationText.replace('.', ',');
        return {
            context: 'Een boodschappenmand kost in het basisjaar ' + basePrice + '. In het doeljaar kost dezelfde mand ' + currentPrice + '.',
            steps: [
                {
                    q: 'Bereken de prijsindex van het doeljaar.',
                    mode: 'task_shell',
                    hint: 'Index = mandprijs doeljaar / mandprijs basisjaar x 100.',
                    expl: 'Index = ' + currentPrice + ' / ' + basePrice + ' x 100 = ' + index + '.',
                    taskShell: {
                        id: 'a39-index-numeric',
                        family: 'numeric_input',
                        skillLabel: 'Prijsindex berekenen',
                        purpose: 'Gebruik het basisjaar als 100 en bereken de index van het doeljaar.',
                        prompt: 'Bereken de prijsindex van het doeljaar.',
                        interaction: { inputLabel: 'Prijsindex', placeholder: 'Bijvoorbeeld 105' },
                        expected: { kind: 'number', value: index, tolerance: 0.05 },
                        feedback: {
                            matchTitle: 'Index klopt',
                            matchText: 'Je hebt de doeljaarprijs gedeeld door de basisjaarprijs en vermenigvuldigd met 100.',
                            retryTitle: 'Controleer basisjaar en doeljaar',
                            retryText: 'Gebruik mandprijs doeljaar / mandprijs basisjaar x 100.'
                        },
                        practiceRoute: { label: 'Terug naar rekenroute', href: '#skilltree-app' }
                    }
                },
                {
                    q: 'Laat zien hoe je de inflatie uit de indexcijfers berekent.',
                    mode: 'task_shell',
                    hint: 'Gebruik de aanpak voor procentuele verandering op de indexwaarden.',
                    expl: 'Inflatie = (' + index + ' - ' + previousIndex + ') / ' + previousIndex + ' x 100 = ' + inflation + '%.',
                    taskShell: {
                        id: 'a39-inflation-work',
                        family: 'calculation_work_capture',
                        skillLabel: 'Inflatie uit indexcijfers',
                        purpose: 'Gebruik de oude index als noemer en laat de rekenstap zien.',
                        prompt: 'Laat zien hoe je de inflatie uit de indexcijfers berekent.',
                        interaction: {
                            workLabel: 'Berekening',
                            finalAnswerLabel: 'Eindantwoord met procentteken',
                            finalAnswerPlaceholder: 'Bijvoorbeeld ' + inflationText + '%'
                        },
                        expected: {
                            kind: 'self_check',
                            criteria: [
                                'Oude index = ' + previousIndex + ' en nieuwe index = ' + index + ' staan zichtbaar.',
                                'Je deelt het indexverschil door de oude index.',
                                'Je eindantwoord heeft een procentteken.'
                            ]
                        },
                        feedback: {
                            selfCheckTitle: 'Vergelijk je indexberekening',
                            selfCheckText: 'Loop oude index, nieuwe index, noemer en procentteken na.',
                            retryTitle: 'Schrijf eerst je uitwerking',
                            retryText: 'Noteer de twee indexcijfers en deel het verschil door de oude index.'
                        },
                        practiceRoute: { label: 'Terug naar rekenroute', href: '#skilltree-app' }
                    }
                },
                {
                    q: 'Geef de inflatie met procentteken.',
                    mode: 'task_shell',
                    hint: 'Schrijf de procentuele verandering tussen de indexcijfers op.',
                    expl: 'De inflatie is ' + inflation + '%.',
                    taskShell: {
                        id: 'a39-final-answer',
                        family: 'final_answer_entry',
                        skillLabel: 'Inflatie noteren',
                        purpose: 'Sluit de indexberekening af met een percentage.',
                        prompt: 'Geef de inflatie met procentteken.',
                        interaction: { inputLabel: 'Inflatie', placeholder: inflationText + '%' },
                        expected: { kind: 'text', accepted: [inflationText + '%', inflationText + ' %', inflationComma + '%', inflationComma + ' %'] },
                        feedback: {
                            matchTitle: 'Inflatie juist genoteerd',
                            matchText: 'Je antwoord bevat de procentuele verandering tussen de indexcijfers.',
                            retryTitle: 'Controleer getal en procentteken',
                            retryText: 'Gebruik de uitkomst van je indexberekening en zet er een procentteken achter.'
                        },
                        practiceRoute: { label: 'Terug naar rekenroute', href: '#skilltree-app' }
                    }
                },
                {
                    q: 'Hoe noteer je de prijsindex van het doeljaar zonder er inflatie van te maken?',
                    mode: 'task_shell',
                    hint: 'Een indexcijfer krijgt geen procentteken.',
                    expl: 'De prijsindex noteer je als ' + index + ', met basisjaar 100.',
                    taskShell: {
                        id: 'a39-index-notation',
                        family: 'unit_notation_field',
                        skillLabel: 'Indexnotatie',
                        purpose: 'Houd indexcijfer en inflatiepercentage uit elkaar.',
                        prompt: 'Hoe noteer je de prijsindex van het doeljaar zonder er inflatie van te maken?',
                        interaction: { inputLabel: 'Indexnotatie', placeholder: String(index) },
                        expected: { kind: 'text', accepted: [String(index), 'index ' + index, 'indexcijfer ' + index] },
                        feedback: {
                            matchTitle: 'Indexnotatie klopt',
                            matchText: 'Een prijsindex noteer je als indexcijfer met basisjaar 100, niet als inflatiepercentage.',
                            retryTitle: 'Laat het procentteken weg',
                            retryText: 'Schrijf het indexcijfer zelf op; inflatie bereken je pas tussen twee indexcijfers.'
                        },
                        practiceRoute: { label: 'Terug naar rekenroute', href: '#skilltree-app' }
                    }
                }
            ]
        };
    };

    GEN.A61 = function () {
        var oldValue = pick([120, 160, 200, 400, 500]);
        var change = pick([-80, -60, -40, 40, 60, 80]);
        var newValue = oldValue + change;
        var row = pick(['januari', 'maart', 'juni', 'week 1']);
        var nextRow = pick(['juni', 'week 2', 'september', 'december']);
        return {
            context: 'Een tabel toont verkoop per periode.\n' + row + ': ' + oldValue + ' stuks.\n' + nextRow + ': ' + newValue + ' stuks.\nSelecteer de bronwaarden voor een berekening.',
            steps: [
                mcStep(
                    'Wat moet je eerst uit de vraag halen?',
                    'welke perioden en welke grootheid nodig zijn',
                    ['het grootste getal', 'de kleur van de tabel', 'alle getallen in de bron'],
                    'Lees eerst de vraag, niet meteen de getallen.',
                    'Je bepaalt eerst welke periode, rij, kolom of grootheid nodig is.'
                ),
                {
                    q: 'Welke oude waarde hoort bij ' + row + '?',
                    a: oldValue,
                    hint: 'Kijk naar de rij of kolom met label ' + row + '.',
                    expl: row + ' is de oude situatie: ' + oldValue + ' stuks.'
                },
                {
                    q: 'Welke nieuwe waarde hoort bij ' + nextRow + '?',
                    a: newValue,
                    hint: 'Kijk naar de rij of kolom met label ' + nextRow + '.',
                    expl: nextRow + ' is de nieuwe situatie: ' + newValue + ' stuks.'
                },
                mcStep(
                    'Waarom noteer je de labels oud en nieuw bij de waarden?',
                    'dan is de berekening controleerbaar',
                    ['dan wordt het antwoord altijd positief', 'dan hoef je geen eenheid te gebruiken', 'dan kun je de tabel overslaan'],
                    'Een los getal heeft weinig betekenis.',
                    'Met labels zoals oud = ' + oldValue + ' en nieuw = ' + newValue + ' is duidelijk wat je berekent.'
                )
            ]
        };
    };

    GEN.A62 = function () {
        var labels = ['A', 'B', 'C', 'D'];
        var values = labels.map(function(_, i) { return 40 + i * 20 + ri(0, 3) * 5; });
        var idx = ri(0, labels.length - 1);
        return {
            context: 'Een staafdiagram toont aantallen per categorie:\n' + labels.map(function(label, i) { return label + ': ' + values[i]; }).join(', ') + '.\nLees de gevraagde staaf af.',
            steps: [
                mcStep(
                    'Wat controleer je voordat je de staafhoogte leest?',
                    'titel, eenheid en categorie-label',
                    ['alleen de hoogste staaf', 'alleen de kleur', 'alleen het aantal staven'],
                    'Een staaf heeft pas betekenis met label en eenheid.',
                    'Je controleert titel, eenheid en categorie-label voordat je leest.'
                ),
                {
                    q: 'Welke waarde hoort bij categorie ' + labels[idx] + '?',
                    a: values[idx],
                    hint: 'Zoek categorie ' + labels[idx] + ' en lees de hoogte af.',
                    expl: 'Categorie ' + labels[idx] + ' heeft waarde ' + values[idx] + '.'
                },
                mcStep(
                    'Waarom kijk je naar de schaal van de as?',
                    'om te zien hoe grote stappen tussen de lijnen zijn',
                    ['om de titel te vervangen', 'om de categorie te raden', 'om alle waarden gelijk te maken'],
                    'De schaal bepaalt hoe je tussen lijnen leest.',
                    'De schaal vertelt of een afstand bijvoorbeeld 10, 20 of 100 eenheden betekent.'
                )
            ]
        };
    };

    GEN.A63 = function () {
        var first = ri(80, 140);
        var second = first + pick([-30, -20, 20, 30]);
        var third = second + pick([-20, 20, 40]);
        var years = ['2023', '2024', '2025'];
        var values = [first, second, third];
        var idx = ri(0, 2);
        return {
            context: 'Een lijngrafiek toont waarden per jaar:\n2023: ' + first + ', 2024: ' + second + ', 2025: ' + third + '.\nLees het gevraagde punt af.',
            steps: [
                mcStep(
                    'Wat lees je eerst bij een lijngrafiek?',
                    'titel, assen, eenheden en meetpunten',
                    ['alleen de stijging', 'alleen het laatste punt', 'alleen de lijnkleur'],
                    'De lijn verbindt meetpunten; eerst moet je weten wat ze voorstellen.',
                    'Titel, assen, eenheden en meetpunten geven de betekenis.'
                ),
                {
                    q: 'Welke waarde hoort bij ' + years[idx] + '?',
                    a: values[idx],
                    hint: 'Zoek het jaar ' + years[idx] + ' en lees het punt op de verticale schaal.',
                    expl: 'Bij ' + years[idx] + ' hoort waarde ' + values[idx] + '.'
                },
                mcStep(
                    'Wanneer gebruik je interpolatie?',
                    'als de gevraagde waarde tussen twee bekende punten ligt',
                    ['als de waarde exact als punt getekend is', 'als je de aslabels overslaat', 'als de grafiek daalt'],
                    'Interpoleren betekent schatten tussen bekende punten.',
                    'Je gebruikt interpolatie alleen tussen twee bekende punten.'
                )
            ]
        };
    };

    GEN.A40 = function () {
        var kind = pick(['consumentensurplus', 'producentensurplus', 'belastingopbrengst', 'welvaartsverlies']);
        var correctRegion = {
            consumentensurplus: 'tussen vraagcurve en prijs, links van Q',
            producentensurplus: 'tussen prijs en aanbodcurve, links van Q',
            belastingopbrengst: 'rechthoek: heffing per stuk x verhandelde hoeveelheid',
            welvaartsverlies: 'driehoek tussen oude en nieuwe hoeveelheid'
        }[kind];
        return {
            context: 'Je krijgt een P-Q diagram en moet het gebied voor ' + kind + ' arceren.',
            steps: [
                mcStep(
                    'Welk gebied hoort bij ' + kind + '?',
                    correctRegion,
                    [
                        'tussen vraagcurve en prijs, links van Q',
                        'tussen prijs en aanbodcurve, links van Q',
                        'rechthoek: heffing per stuk x verhandelde hoeveelheid',
                        'driehoek tussen oude en nieuwe hoeveelheid',
                        'alles onder de aanbodcurve'
                    ],
                    'Bepaal eerst welke economische grootheid gevraagd wordt.',
                    kind + ' hoort bij: ' + correctRegion + '.'
                ),
                {
                    q: 'Zet de arceerstappen in de juiste volgorde.',
                    mode: 'order',
                    blocks: [
                        'Bepaal welke grootheid gevraagd wordt',
                        'Zoek de grenzen van het gebied',
                        'Arceer de gesloten figuur en label die'
                    ],
                    correctOrder: [0, 1, 2],
                    hint: 'Eerst herkennen, dan grenzen zoeken, dan tekenen.',
                    expl: 'Je voorkomt een verkeerd gebied door eerst de definitie en grenzen vast te leggen.'
                }
            ]
        };
    };

    GEN.A41 = function () {
        var intercept = ri(4, 16);
        var slope = pick([1, 2, 3, 4]);
        var amount = ri(2, 8);
        var isTax = Math.random() < 0.5;
        var newIntercept = isTax ? intercept + amount : intercept - amount;
        return {
            context: 'De inverse aanbodfunctie is P = ' + intercept + ' + ' + slope + 'Q. Er komt een ' + (isTax ? 'heffing' : 'subsidie') + ' van ' + amount + ' per stuk.',
            steps: [
                mcStep(
                    'Wat gebeurt er met de aanbodcurve in P-vorm?',
                    isTax ? 'heffing: aanbod schuift omhoog' : 'subsidie: aanbod schuift omlaag',
                    ['heffing: aanbod schuift omhoog', 'heffing: aanbod schuift omlaag', 'subsidie: aanbod schuift omhoog', 'subsidie: aanbod schuift omlaag'],
                    'Denk vanuit de kosten per extra product.',
                    (isTax ? 'Een heffing verhoogt' : 'Een subsidie verlaagt') + ' de prijs die aanbieders nodig hebben bij elke hoeveelheid.'
                ),
                { q: 'Wat wordt de nieuwe constante term in de inverse aanbodfunctie?', a: newIntercept, hint: (isTax ? 'Tel de heffing erbij op.' : 'Trek de subsidie ervan af.'), expl: 'Nieuwe constante = ' + intercept + (isTax ? ' + ' : ' - ') + amount + ' = ' + newIntercept + '.' },
                {
                    q: 'Zet de aanpak in de juiste volgorde.',
                    mode: 'order',
                    blocks: [
                        'Schrijf aanbod in inverse vorm',
                        'Verwerk heffing of subsidie in de constante term',
                        'Stel de nieuwe aanbodfunctie gelijk aan vraag'
                    ],
                    correctOrder: [0, 1, 2],
                    hint: 'Eerst de vorm goed zetten, dan verschuiven, dan evenwicht oplossen.',
                    expl: 'De fout zit vaak in de richting van de verschuiving; daarom werk je eerst in P-vorm.'
                }
            ]
        };
    };

    GEN.A42 = function () {
        var curve = pick(['vraagcurve', 'aanbodcurve']);
        var direction = pick(['rechts', 'links']);
        var label = curve === 'vraagcurve' ? 'D' : 'S';
        return {
            context: 'Teken een verschuiving van de ' + curve + ' naar ' + direction + ' met een oud-en-nieuw diagram.',
            steps: [
                mcStep(
                    'Welke labels gebruik je voor de oude en nieuwe curve?',
                    label + ' en ' + label + "'",
                    [label + ' en ' + label + "'", 'P en Q', "E en E'", 'MK en MO'],
                    'Vraag is D, aanbod is S. De nieuwe curve krijgt een accent.',
                    'De oude curve is ' + label + ', de nieuwe curve is ' + label + "'."
                ),
                mcStep(
                    'Welke richting krijgen de verschuivingspijlen?',
                    'horizontaal',
                    ['horizontaal', 'verticaal', 'diagonaal', 'langs de curve'],
                    'Een verschuiving laat zien hoeveel Q verandert bij dezelfde P.',
                    'De pijlen zijn horizontaal omdat je de hoeveelheid bij gelijke prijs vergelijkt.'
                ),
                {
                    q: 'Zet de tekenstappen in de juiste volgorde.',
                    mode: 'order',
                    blocks: [
                        'Teken en label de oude curve',
                        'Teken en label de nieuwe curve',
                        'Plaats horizontale pijlen tussen oud en nieuw'
                    ],
                    correctOrder: [0, 1, 2],
                    hint: 'Het oude beeld blijft zichtbaar.',
                    expl: 'Een verschuivingsdiagram toont altijd oud, nieuw en richting.'
                }
            ]
        };
    };

    GEN.A43 = function () {
        var qA = ri(2, 9), qB = ri(2, 9), qC = ri(2, 9);
        var pA = ri(3, 12), pB = ri(3, 12), pC = ri(3, 12);
        var winA = qA * pA, winB = qB * pB, winC = qC * pC;
        var total = winA + winB + winC;
        return {
            context: 'Een leerling verdeelt tijd over drie activiteiten.\nA: ' + qA + ' uur x ' + pA + ' winst per uur.\nB: ' + qB + ' uur x ' + pB + ' winst per uur.\nC: ' + qC + ' uur x ' + pC + ' winst per uur.',
            steps: [
                { q: 'Bereken de winst van activiteit A.', a: winA, hint: 'Hoeveelheid x winst per eenheid.', expl: 'A = ' + qA + ' x ' + pA + ' = ' + winA + '.' },
                { q: 'Bereken de winst van activiteit B.', a: winB, hint: 'Hoeveelheid x winst per eenheid.', expl: 'B = ' + qB + ' x ' + pB + ' = ' + winB + '.' },
                { q: 'Bereken de totale winst van de gekozen mix.', a: total, hint: 'Tel de winst van A, B en C op.', expl: 'Totaal = ' + winA + ' + ' + winB + ' + ' + winC + ' = ' + total + '.' },
                mcStep(
                    'Welke activiteiten tel je mee?',
                    'alleen de daadwerkelijk gekozen activiteiten',
                    ['alleen de daadwerkelijk gekozen activiteiten', 'alle mogelijke alternatieven', 'alleen de activiteit met hoogste winst per uur', 'alleen de niet-gekozen alternatieven'],
                    'De vraag gaat over deze allocatie.',
                    'Totale winst hoort bij wat echt gekozen is, niet bij de gemiste alternatieven.'
                )
            ]
        };
    };

    GEN.A44 = function () {
        var w1 = ri(14, 20);
        var w2 = w1 - ri(2, 4);
        var w3 = w2 - ri(2, 4);
        var w4 = w3 - ri(2, 4);
        var price = pick([w2, w3 + 1, w3, w4 + 1]);
        var values = [w1, w2, w3, w4];
        var demanded = values.filter(function (v) { return v >= price; }).length;
        var totalWtp = values.slice(0, demanded).reduce(function (sum, v) { return sum + v; }, 0);
        return {
            context: 'Betalingsbereidheid per extra eenheid: 1e=' + w1 + ', 2e=' + w2 + ', 3e=' + w3 + ', 4e=' + w4 + '. De marktprijs is ' + price + '.',
            steps: [
                mcStep(
                    'Welke vorm heeft de individuele vraagcurve?',
                    'een dalende stapfunctie',
                    ['een dalende stapfunctie', 'een stijgende rechte lijn', 'een horizontale prijslijn', 'een U-vormige kostencurve'],
                    'Elke extra eenheid heeft een eigen betalingsbereidheid.',
                    'Per eenheid teken je een horizontale stap op de hoogte van de betalingsbereidheid.'
                ),
                { q: 'Hoeveel eenheden koopt deze consument bij prijs ' + price + '?', a: demanded, hint: 'Tel elke eenheid met betalingsbereidheid groter dan of gelijk aan de prijs.', expl: demanded + ' eenheid/eenheden hebben betalingsbereidheid >= ' + price + '.' },
                { q: 'Wat is de totale betalingsbereidheid voor deze gekochte eenheden?', a: totalWtp, hint: 'Tel de betalingsbereidheid van de gekochte eenheden op.', expl: 'Totale betalingsbereidheid = ' + values.slice(0, demanded).join(' + ') + ' = ' + totalWtp + '.' },
                {
                    q: 'Zet de tekenstappen in de juiste volgorde.',
                    mode: 'order',
                    blocks: [
                        'Zet P op de verticale as en Q op de horizontale as',
                        'Teken per eenheid een horizontale stap',
                        'Laat de stappen dalen als betalingsbereidheid afneemt'
                    ],
                    correctOrder: [0, 1, 2],
                    hint: 'Eerst assen, dan stappen, dan controleren of de curve daalt.',
                    expl: 'Een individuele vraagcurve uit betalingsbereidheid is trapsgewijs.'
                }
            ]
        };
    };

    var SKILLS = [
            {
                    "id": "A01",
                    "name": "Lineaire functie opstellen",
                    "layer": 0,
                    "needs": [],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Stel een lineaire functie op (y = ax + b) vanuit een economische context, zoals een vraag- of aanbodfunctie."
            },
            {
                    "id": "A02",
                    "name": "Vergelijking oplossen",
                    "layer": 0,
                    "needs": [],
                    "aspects": [
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Los een vergelijking met één onbekende op, bijvoorbeeld door twee functies aan elkaar gelijk te stellen."
            },
            {
                    "id": "A03",
                    "name": "Functie omschrijven (P↔Q)",
                    "layer": 0,
                    "needs": [],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Schrijf een functie om van P als functie van Q naar Q als functie van P, of andersom."
            },
            {
                    "id": "A04",
                    "name": "Substitueren",
                    "layer": 0,
                    "needs": [],
                    "aspects": [
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Vul een waarde in een functie in en bereken het resultaat."
            },
            {
                    "id": "A05",
                    "name": "Snijpunt met P-as berekenen",
                    "layer": 0,
                    "needs": [],
                    "aspects": [
                            "grafisch",
                            "rekenen"
                    ],
                    "desc": "Bereken het snijpunt van een functie met de verticale as (P-as) door Q = 0 in te vullen."
            },
            {
                    "id": "A06",
                    "name": "Evenwichtsprijs & -hoeveelheid",
                    "layer": 1,
                    "needs": [
                            "A01",
                            "A02"
                    ],
                    "aspects": [
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Bereken de evenwichtsprijs en -hoeveelheid door vraag en aanbod aan elkaar gelijk te stellen."
            },
            {
                    "id": "A07",
                    "name": "TO-functie opstellen",
                    "layer": 1,
                    "needs": [
                            "A01",
                            "A03"
                    ],
                    "aspects": [
                            "grafisch",
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Stel de totale opbrengstfunctie op: TO = P × Q. Schrijf de vraagfunctie om zodat P in Q is uitgedrukt."
            },
            {
                    "id": "A08",
                    "name": "TK-functie herkennen",
                    "layer": 1,
                    "needs": [
                            "A01"
                    ],
                    "aspects": [
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Herken en werk met de totale kostenfunctie (TK), vaak gegeven als TK = vaste kosten + variabele kosten × Q."
            },
            {
                    "id": "A09",
                    "name": "Collectief aanbod",
                    "layer": 1,
                    "needs": [
                            "A03"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Tel individuele aanbodfuncties op tot een collectieve aanbodfunctie."
            },
            {
                    "id": "A10",
                    "name": "Oppervlakte driehoek",
                    "layer": 1,
                    "needs": [
                            "A04"
                    ],
                    "aspects": [
                            "grafisch",
                            "rekenen"
                    ],
                    "desc": "Bereken de oppervlakte van een driehoek in een grafiek: ½ × basis × hoogte."
            },
            {
                    "id": "A11",
                    "name": "Afgeleide bepalen",
                    "layer": 1,
                    "needs": [
                            "A01"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Bepaal de afgeleide van een functie. Bijvoorbeeld: als TO = 5Q², dan is MO = 10Q."
            },
            {
                    "id": "A12",
                    "name": "MO bepalen met afgeleide",
                    "layer": 2,
                    "needs": [
                            "A11",
                            "A07"
                    ],
                    "aspects": [
                            "grafisch",
                            "rekenen"
                    ],
                    "desc": "Bepaal marginale opbrengst door eerst TO op te stellen en daarvan de afgeleide naar Q te nemen."
            },
            {
                    "id": "A13",
                    "name": "MK bepalen",
                    "layer": 2,
                    "needs": [
                            "A11",
                            "A08"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Bepaal de marginale kosten (MK) door de afgeleide van de TK-functie te nemen."
            },
            {
                    "id": "A14",
                    "name": "GTK bepalen",
                    "layer": 2,
                    "needs": [
                            "A08"
                    ],
                    "aspects": [
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Bereken de gemiddelde totale kosten: GTK = TK / Q."
            },
            {
                    "id": "A15",
                    "name": "Prijselasticiteit van de vraag",
                    "layer": 1,
                    "needs": [
                            "A04",
                            "A38"
                    ],
                    "aspects": [
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Bereken de prijselasticiteit: Ev = %ΔQv / %ΔP. Bepaal of de vraag elastisch of inelastisch is."
            },
            {
                    "id": "A16",
                    "name": "Kruiselasticiteit",
                    "layer": 2,
                    "needs": [
                            "A15"
                    ],
                    "aspects": [
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Bereken de kruiselasticiteit: Ekr = %ΔQa / %ΔPb. Bepaal of goederen substituten of complementen zijn."
            },
            {
                    "id": "A17",
                    "name": "Inkomenselasticiteit",
                    "layer": 2,
                    "needs": [
                            "A15"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Bereken de inkomenselasticiteit: Ei = %ΔQ / %ΔY. Bepaal of een goed normaal, inferieur of luxe is."
            },
            {
                    "id": "A18",
                    "name": "Comparatief voordeel bepalen",
                    "layer": 3,
                    "needs": [],
                    "aspects": [
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Vergelijk de alternatieve kosten van twee producenten om te bepalen wie een comparatief voordeel heeft."
            },
            {
                    "id": "A19",
                    "name": "Surplus berekenen (CS/PS)",
                    "layer": 3,
                    "needs": [
                            "A06",
                            "A10"
                    ],
                    "aspects": [
                            "grafisch",
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Bereken het consumenten- of producentensurplus als driehoeksoppervlakte in de vraag-/aanbodgrafiek."
            },
            {
                    "id": "A21",
                    "name": "Winst = TO − TK",
                    "layer": 3,
                    "needs": [
                            "A07",
                            "A08",
                            "A04"
                    ],
                    "aspects": [
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Bereken de winst door de totale opbrengst min de totale kosten: W = TO − TK."
            },
            {
                    "id": "A22",
                    "name": "Break-even (TO = TK)",
                    "layer": 3,
                    "needs": [
                            "A07",
                            "A08",
                            "A02"
                    ],
                    "aspects": [
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Vind de break-evenhoeveelheid door TO = TK op te lossen. Bij dit punt is de winst nul."
            },
            {
                    "id": "A23",
                    "name": "Evenwicht met heffing",
                    "layer": 3,
                    "needs": [
                            "A06",
                            "A01",
                            "A15"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Bereken het nieuwe marktevenwicht nadat de overheid een heffing (accijns) heeft opgelegd, en analyseer hoe de heffing verdeeld wordt tussen consument en producent."
            },
            {
                    "id": "A24",
                    "name": "Collectief aanbod bepalen",
                    "layer": 3,
                    "needs": [
                            "A09",
                            "A03"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Bepaal het collectieve aanbod vanuit meerdere individuele aanbieders en bereken het marktevenwicht."
            },
            {
                    "id": "A25",
                    "name": "Minimumprijs analyseren",
                    "layer": 3,
                    "needs": [
                            "A06"
                    ],
                    "aspects": [
                            "grafisch",
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Analyseer het effect van een minimumprijs: bereken het vraagoverschot en het welvaartsverlies."
            },
            {
                    "id": "A26",
                    "name": "Maximumprijs analyseren",
                    "layer": 3,
                    "needs": [
                            "A06"
                    ],
                    "aspects": [
                            "grafisch",
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Analyseer het effect van een maximumprijs: bereken het vraagoverschot en de gevolgen voor consumenten."
            },
            {
                    "id": "A27",
                    "name": "Subsidie analyseren",
                    "layer": 3,
                    "needs": [
                            "A06",
                            "A01"
                    ],
                    "aspects": [
                            "grafisch",
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Bereken het effect van een subsidie op het marktevenwicht, de prijs en de verdeling van het voordeel."
            },
            {
                    "id": "A28",
                    "name": "MK = GTK oplossen",
                    "layer": 3,
                    "needs": [
                            "A13",
                            "A14"
                    ],
                    "aspects": [
                            "grafisch",
                            "rekenen"
                    ],
                    "desc": "Vind de hoeveelheid waar MK = GTK. Dit is het minimum van de GTK-curve (efficiënte schaal)."
            },
            {
                    "id": "A29",
                    "name": "Break-even analyse",
                    "layer": 4,
                    "needs": [
                            "A22"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Voer een volledige break-evenanalyse uit: vind de break-evenhoeveelheid en bepaal winst/verlies bij een gegeven Q."
            },
            {
                    "id": "A30",
                    "name": "Consumentensurplus",
                    "layer": 4,
                    "needs": [
                            "A19"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Bereken het consumentensurplus voor en na een beleidsverandering en bepaal het verschil."
            },
            {
                    "id": "A31",
                    "name": "Individueel → collectief aanbod",
                    "layer": 4,
                    "needs": [
                            "A24"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Ga van individuele aanbodcurves naar de collectieve aanbodcurve en bereken het marktevenwicht."
            },
            {
                    "id": "A32",
                    "name": "Welvaartsverlies belasting",
                    "layer": 5,
                    "needs": [
                            "A19",
                            "A23"
                    ],
                    "aspects": [
                            "grafisch",
                            "rekenen"
                    ],
                    "desc": "Bereken het welvaartsverlies (deadweight loss) dat ontstaat door een belasting als driehoeksoppervlakte."
            },
            {
                    "id": "A33",
                    "name": "Optimale productie bij VM",
                    "layer": 4,
                    "needs": [
                            "A13",
                            "A14",
                            "A04"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Bepaal de optimale productie bij volkomen mededinging: produceer waar P = MK en bereken de winst."
            },
            {
                    "id": "A34",
                    "name": "Effecten invoerrecht",
                    "layer": 5,
                    "needs": [
                            "A19",
                            "A23",
                            "A06"
                    ],
                    "aspects": [
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Analyseer de effecten van een invoerrecht op binnenlandse productie, consumptie, import en welvaart."
            },
            {
                    "id": "A35",
                    "name": "Max. winst monopolist",
                    "layer": 5,
                    "needs": [
                            "A21",
                            "A04"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Bereken de maximale winst van een monopolist: vind Q waar MO = MK, bepaal P en reken W = TO − TK uit."
            },
            {
                    "id": "A36",
                    "name": "Prijsdiscriminatie",
                    "layer": 5,
                    "needs": [
                            "A21"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Bereken de winst bij prijsdiscriminatie: de monopolist rekent verschillende prijzen in verschillende markten."
            },
            {
                    "id": "A37",
                    "name": "Lange-termijnevenwicht VM",
                    "layer": 5,
                    "needs": [
                            "A28"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Bepaal het lange-termijnevenwicht bij volkomen mededinging: P = MK = GTK (minimale GTK)."
            },
            {
                    "id": "A38",
                    "name": "Procentuele verandering berekenen",
                    "layer": 0,
                    "needs": [],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Bereken de procentuele verandering met %Δ = (nieuw − oud) / oud × 100, en pas dit toe op prijzen, hoeveelheden, indexcijfers en reële variabelen."
            },
            {
                    "id": "A39",
                    "name": "Prijsindex (CPI) berekenen",
                    "layer": 1,
                    "needs": [
                            "A38"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Bereken een prijsindex als mandprijs-jaar-t / mandprijs-basisjaar × 100, en interpreteer het getal als relatieve prijsverandering ten opzichte van basisjaar = 100."
            },
            {
                    "id": "A40",
                    "name": "Welvaartsgebied op P–Q diagram arceren",
                    "layer": 2,
                    "needs": [
                            "A10"
                    ],
                    "aspects": [
                            "grafisch"
                    ],
                    "desc": "Identificeer en arceer de juiste welvaartsregio op een P–Q diagram: consumentensurplus, producentensurplus, belastingopbrengst-rechthoek, welvaartsverlies-driehoek, subsidie-rechthoek, monopoliewinst-rechthoek, of tarief-DWL."
            },
            {
                    "id": "A41",
                    "name": "Na-belasting of na-subsidie aanbodfunctie afleiden",
                    "layer": 1,
                    "needs": [
                            "A03"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Leid de na-belasting aanbodfunctie af door de heffing per eenheid bij de inverse aanbodfunctie op te tellen; bij een subsidie trek je de subsidie per eenheid af. Vervolgens los je Qa_nieuw = Qv op voor het nieuwe evenwicht."
            },
            {
                    "id": "A42",
                    "name": "Grafische verschuiving met voor-en-na pijlen",
                    "layer": 1,
                    "needs": [],
                    "aspects": [
                            "grafisch"
                    ],
                    "desc": "Teken een grafische verschuiving (vraag- of aanbodcurve) met zowel de oude als de nieuwe curve, gelabeld D / D' of S / S', en geef de richting aan met pijlen tussen de oude en nieuwe positie."
            },
            {
                    "id": "A43",
                    "name": "Totale winst uit gemengde allocatie berekenen",
                    "layer": 3,
                    "needs": [],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Bereken de totale winst van een verdeling van beperkte middelen over meerdere activiteiten door per activiteit (hoeveelheid × winst/eenheid) te berekenen en op te tellen."
            },
            {
                    "id": "A44",
                    "name": "Individuele stapfunctie-vraagcurve tekenen uit betalingsbereidheid",
                    "layer": 2,
                    "needs": [],
                    "aspects": [
                            "grafisch"
                    ],
                    "desc": "Teken de individuele vraagcurve van één consument als een stapfunctie: voor elke eenheid een horizontale stap op de hoogte van de betalingsbereidheid voor die eenheid."
            },
            {
                    "id": "A61",
                    "name": "Tabelwaarden selecteren voor berekening",
                    "layer": 0,
                    "needs": [],
                    "aspects": [
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Selecteer in een economische tabel de waarden die nodig zijn voor een berekening: juiste rij, kolom, periode en oude/nieuwe waarde."
            },
            {
                    "id": "A62",
                    "name": "Waarden aflezen uit staafdiagram",
                    "layer": 0,
                    "needs": [],
                    "aspects": [
                            "grafisch"
                    ],
                    "desc": "Lees een waarde af uit een staafdiagram door context, labels, eenheid en schaal te controleren voordat je de staafhoogte gebruikt."
            },
            {
                    "id": "A63",
                    "name": "Waarden aflezen uit lijngrafiek",
                    "layer": 0,
                    "needs": [],
                    "aspects": [
                            "grafisch"
                    ],
                    "desc": "Lees een punt of periode af uit een lijngrafiek door context, aslabels, eenheden, schaal en eventuele interpolatie expliciet te controleren."
            },
            {
                    "id": "A95",
                    "name": "MO = gegeven MK-functie oplossen",
                    "layer": 1,
                    "needs": [
                            "A02"
                    ],
                    "aspects": [
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Los MO = MK op wanneer de MK-functie in de opgave staat en niet uit TK hoeft te worden afgeleid."
            }
    ];
    var ROUTE_SKILLS = [
            {
                    "id": "A01",
                    "name": "Lineaire functie opstellen",
                    "layer": 0,
                    "needs": [],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Stel een lineaire functie op (y = ax + b) vanuit een economische context, zoals een vraag- of aanbodfunctie."
            },
            {
                    "id": "A02",
                    "name": "Vergelijking oplossen",
                    "layer": 0,
                    "needs": [],
                    "aspects": [
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Los een vergelijking met één onbekende op, bijvoorbeeld door twee functies aan elkaar gelijk te stellen."
            },
            {
                    "id": "A03",
                    "name": "Functie omschrijven (P↔Q)",
                    "layer": 0,
                    "needs": [],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Schrijf een functie om van P als functie van Q naar Q als functie van P, of andersom."
            },
            {
                    "id": "A04",
                    "name": "Substitueren",
                    "layer": 0,
                    "needs": [],
                    "aspects": [
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Vul een waarde in een functie in en bereken het resultaat."
            },
            {
                    "id": "A05",
                    "name": "Snijpunt met P-as berekenen",
                    "layer": 0,
                    "needs": [],
                    "aspects": [
                            "grafisch",
                            "rekenen"
                    ],
                    "desc": "Bereken het snijpunt van een functie met de verticale as (P-as) door Q = 0 in te vullen."
            },
            {
                    "id": "A06",
                    "name": "Evenwichtsprijs & -hoeveelheid",
                    "layer": 1,
                    "needs": [
                            "A01",
                            "A02"
                    ],
                    "aspects": [
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Bereken de evenwichtsprijs en -hoeveelheid door vraag en aanbod aan elkaar gelijk te stellen."
            },
            {
                    "id": "A07",
                    "name": "TO-functie opstellen",
                    "layer": 1,
                    "needs": [
                            "A01",
                            "A03"
                    ],
                    "aspects": [
                            "grafisch",
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Stel de totale opbrengstfunctie op: TO = P × Q. Schrijf de vraagfunctie om zodat P in Q is uitgedrukt."
            },
            {
                    "id": "A08",
                    "name": "TK-functie herkennen",
                    "layer": 1,
                    "needs": [
                            "A01"
                    ],
                    "aspects": [
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Herken en werk met de totale kostenfunctie (TK), vaak gegeven als TK = vaste kosten + variabele kosten × Q."
            },
            {
                    "id": "A09",
                    "name": "Collectief aanbod",
                    "layer": 1,
                    "needs": [
                            "A03"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Tel individuele aanbodfuncties op tot een collectieve aanbodfunctie."
            },
            {
                    "id": "A10",
                    "name": "Oppervlakte driehoek",
                    "layer": 1,
                    "needs": [
                            "A04"
                    ],
                    "aspects": [
                            "grafisch",
                            "rekenen"
                    ],
                    "desc": "Bereken de oppervlakte van een driehoek in een grafiek: ½ × basis × hoogte."
            },
            {
                    "id": "A11",
                    "name": "Afgeleide bepalen",
                    "layer": 1,
                    "needs": [
                            "A01"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Bepaal de afgeleide van een functie. Bijvoorbeeld: als TO = 5Q², dan is MO = 10Q."
            },
            {
                    "id": "A12",
                    "name": "MO bepalen met afgeleide",
                    "layer": 2,
                    "needs": [
                            "A11",
                            "A07"
                    ],
                    "aspects": [
                            "grafisch",
                            "rekenen"
                    ],
                    "desc": "Bepaal marginale opbrengst door eerst TO op te stellen en daarvan de afgeleide naar Q te nemen."
            },
            {
                    "id": "A13",
                    "name": "MK bepalen",
                    "layer": 2,
                    "needs": [
                            "A11",
                            "A08"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Bepaal de marginale kosten (MK) door de afgeleide van de TK-functie te nemen."
            },
            {
                    "id": "A14",
                    "name": "GTK bepalen",
                    "layer": 2,
                    "needs": [
                            "A08"
                    ],
                    "aspects": [
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Bereken de gemiddelde totale kosten: GTK = TK / Q."
            },
            {
                    "id": "A15",
                    "name": "Prijselasticiteit van de vraag",
                    "layer": 1,
                    "needs": [
                            "A04",
                            "A38"
                    ],
                    "aspects": [
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Bereken de prijselasticiteit: Ev = %ΔQv / %ΔP. Bepaal of de vraag elastisch of inelastisch is."
            },
            {
                    "id": "A16",
                    "name": "Kruiselasticiteit",
                    "layer": 2,
                    "needs": [
                            "A15"
                    ],
                    "aspects": [
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Bereken de kruiselasticiteit: Ekr = %ΔQa / %ΔPb. Bepaal of goederen substituten of complementen zijn."
            },
            {
                    "id": "A17",
                    "name": "Inkomenselasticiteit",
                    "layer": 2,
                    "needs": [
                            "A15"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Bereken de inkomenselasticiteit: Ei = %ΔQ / %ΔY. Bepaal of een goed normaal, inferieur of luxe is."
            },
            {
                    "id": "A18",
                    "name": "Comparatief voordeel bepalen",
                    "layer": 3,
                    "needs": [
                            "B02"
                    ],
                    "aspects": [
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Vergelijk de alternatieve kosten van twee producenten om te bepalen wie een comparatief voordeel heeft."
            },
            {
                    "id": "A19",
                    "name": "Surplus berekenen (CS/PS)",
                    "layer": 3,
                    "needs": [
                            "A06",
                            "A10"
                    ],
                    "aspects": [
                            "grafisch",
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Bereken het consumenten- of producentensurplus als driehoeksoppervlakte in de vraag-/aanbodgrafiek."
            },
            {
                    "id": "A21",
                    "name": "Winst = TO − TK",
                    "layer": 3,
                    "needs": [
                            "A07",
                            "A08",
                            "A04"
                    ],
                    "aspects": [
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Bereken de winst door de totale opbrengst min de totale kosten: W = TO − TK."
            },
            {
                    "id": "A22",
                    "name": "Break-even (TO = TK)",
                    "layer": 3,
                    "needs": [
                            "A07",
                            "A08",
                            "A02"
                    ],
                    "aspects": [
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Vind de break-evenhoeveelheid door TO = TK op te lossen. Bij dit punt is de winst nul."
            },
            {
                    "id": "A23",
                    "name": "Evenwicht met heffing",
                    "layer": 3,
                    "needs": [
                            "A06",
                            "A01",
                            "A15"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Bereken het nieuwe marktevenwicht nadat de overheid een heffing (accijns) heeft opgelegd, en analyseer hoe de heffing verdeeld wordt tussen consument en producent."
            },
            {
                    "id": "A24",
                    "name": "Collectief aanbod bepalen",
                    "layer": 3,
                    "needs": [
                            "A09",
                            "A03"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Bepaal het collectieve aanbod vanuit meerdere individuele aanbieders en bereken het marktevenwicht."
            },
            {
                    "id": "A25",
                    "name": "Minimumprijs analyseren",
                    "layer": 3,
                    "needs": [
                            "A06"
                    ],
                    "aspects": [
                            "grafisch",
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Analyseer het effect van een minimumprijs: bereken het vraagoverschot en het welvaartsverlies."
            },
            {
                    "id": "A26",
                    "name": "Maximumprijs analyseren",
                    "layer": 3,
                    "needs": [
                            "A06"
                    ],
                    "aspects": [
                            "grafisch",
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Analyseer het effect van een maximumprijs: bereken het vraagoverschot en de gevolgen voor consumenten."
            },
            {
                    "id": "A27",
                    "name": "Subsidie analyseren",
                    "layer": 3,
                    "needs": [
                            "A06",
                            "A01"
                    ],
                    "aspects": [
                            "grafisch",
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Bereken het effect van een subsidie op het marktevenwicht, de prijs en de verdeling van het voordeel."
            },
            {
                    "id": "A28",
                    "name": "MK = GTK oplossen",
                    "layer": 3,
                    "needs": [
                            "A13",
                            "A14"
                    ],
                    "aspects": [
                            "grafisch",
                            "rekenen"
                    ],
                    "desc": "Vind de hoeveelheid waar MK = GTK. Dit is het minimum van de GTK-curve (efficiënte schaal)."
            },
            {
                    "id": "A29",
                    "name": "Break-even analyse",
                    "layer": 4,
                    "needs": [
                            "A22"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Voer een volledige break-evenanalyse uit: vind de break-evenhoeveelheid en bepaal winst/verlies bij een gegeven Q."
            },
            {
                    "id": "A30",
                    "name": "Consumentensurplus",
                    "layer": 4,
                    "needs": [
                            "A19"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Bereken het consumentensurplus voor en na een beleidsverandering en bepaal het verschil."
            },
            {
                    "id": "A31",
                    "name": "Individueel → collectief aanbod",
                    "layer": 4,
                    "needs": [
                            "A24"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Ga van individuele aanbodcurves naar de collectieve aanbodcurve en bereken het marktevenwicht."
            },
            {
                    "id": "A32",
                    "name": "Welvaartsverlies belasting",
                    "layer": 5,
                    "needs": [
                            "A19",
                            "A23"
                    ],
                    "aspects": [
                            "grafisch",
                            "rekenen"
                    ],
                    "desc": "Bereken het welvaartsverlies (deadweight loss) dat ontstaat door een belasting als driehoeksoppervlakte."
            },
            {
                    "id": "A33",
                    "name": "Optimale productie bij VM",
                    "layer": 4,
                    "needs": [
                            "A13",
                            "A14",
                            "A04"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Bepaal de optimale productie bij volkomen mededinging: produceer waar P = MK en bereken de winst."
            },
            {
                    "id": "A34",
                    "name": "Effecten invoerrecht",
                    "layer": 5,
                    "needs": [
                            "A19",
                            "A23",
                            "A06"
                    ],
                    "aspects": [
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Analyseer de effecten van een invoerrecht op binnenlandse productie, consumptie, import en welvaart."
            },
            {
                    "id": "A35",
                    "name": "Max. winst monopolist",
                    "layer": 5,
                    "needs": [
                            "A21",
                            "A04"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Bereken de maximale winst van een monopolist: vind Q waar MO = MK, bepaal P en reken W = TO − TK uit."
            },
            {
                    "id": "A36",
                    "name": "Prijsdiscriminatie",
                    "layer": 5,
                    "needs": [
                            "A21"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Bereken de winst bij prijsdiscriminatie: de monopolist rekent verschillende prijzen in verschillende markten."
            },
            {
                    "id": "A37",
                    "name": "Lange-termijnevenwicht VM",
                    "layer": 5,
                    "needs": [
                            "A28"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Bepaal het lange-termijnevenwicht bij volkomen mededinging: P = MK = GTK (minimale GTK)."
            },
            {
                    "id": "A38",
                    "name": "Procentuele verandering berekenen",
                    "layer": 0,
                    "needs": [],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Bereken de procentuele verandering met %Δ = (nieuw − oud) / oud × 100, en pas dit toe op prijzen, hoeveelheden, indexcijfers en reële variabelen."
            },
            {
                    "id": "A39",
                    "name": "Prijsindex (CPI) berekenen",
                    "layer": 1,
                    "needs": [
                            "A38"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Bereken een prijsindex als mandprijs-jaar-t / mandprijs-basisjaar × 100, en interpreteer het getal als relatieve prijsverandering ten opzichte van basisjaar = 100."
            },
            {
                    "id": "A40",
                    "name": "Welvaartsgebied op P–Q diagram arceren",
                    "layer": 2,
                    "needs": [
                            "A10"
                    ],
                    "aspects": [
                            "grafisch"
                    ],
                    "desc": "Identificeer en arceer de juiste welvaartsregio op een P–Q diagram: consumentensurplus, producentensurplus, belastingopbrengst-rechthoek, welvaartsverlies-driehoek, subsidie-rechthoek, monopoliewinst-rechthoek, of tarief-DWL."
            },
            {
                    "id": "A41",
                    "name": "Na-belasting of na-subsidie aanbodfunctie afleiden",
                    "layer": 1,
                    "needs": [
                            "A03"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Leid de na-belasting aanbodfunctie af door de heffing per eenheid bij de inverse aanbodfunctie op te tellen; bij een subsidie trek je de subsidie per eenheid af. Vervolgens los je Qa_nieuw = Qv op voor het nieuwe evenwicht."
            },
            {
                    "id": "A42",
                    "name": "Grafische verschuiving met voor-en-na pijlen",
                    "layer": 1,
                    "needs": [],
                    "aspects": [
                            "grafisch"
                    ],
                    "desc": "Teken een grafische verschuiving (vraag- of aanbodcurve) met zowel de oude als de nieuwe curve, gelabeld D / D' of S / S', en geef de richting aan met pijlen tussen de oude en nieuwe positie."
            },
            {
                    "id": "A43",
                    "name": "Totale winst uit gemengde allocatie berekenen",
                    "layer": 3,
                    "needs": [
                            "B02"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Bereken de totale winst van een verdeling van beperkte middelen over meerdere activiteiten door per activiteit (hoeveelheid × winst/eenheid) te berekenen en op te tellen."
            },
            {
                    "id": "A44",
                    "name": "Individuele stapfunctie-vraagcurve tekenen uit betalingsbereidheid",
                    "layer": 2,
                    "needs": [
                            "D35"
                    ],
                    "aspects": [
                            "grafisch"
                    ],
                    "desc": "Teken de individuele vraagcurve van één consument als een stapfunctie: voor elke eenheid een horizontale stap op de hoogte van de betalingsbereidheid voor die eenheid."
            },
            {
                    "id": "A61",
                    "name": "Tabelwaarden selecteren voor berekening",
                    "layer": 0,
                    "needs": [],
                    "aspects": [
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Selecteer in een economische tabel de waarden die nodig zijn voor een berekening: juiste rij, kolom, periode en oude/nieuwe waarde."
            },
            {
                    "id": "A62",
                    "name": "Waarden aflezen uit staafdiagram",
                    "layer": 0,
                    "needs": [],
                    "aspects": [
                            "grafisch"
                    ],
                    "desc": "Lees een waarde af uit een staafdiagram door context, labels, eenheid en schaal te controleren voordat je de staafhoogte gebruikt."
            },
            {
                    "id": "A63",
                    "name": "Waarden aflezen uit lijngrafiek",
                    "layer": 0,
                    "needs": [],
                    "aspects": [
                            "grafisch"
                    ],
                    "desc": "Lees een punt of periode af uit een lijngrafiek door context, aslabels, eenheden, schaal en eventuele interpolatie expliciet te controleren."
            },
            {
                    "id": "A95",
                    "name": "MO = gegeven MK-functie oplossen",
                    "layer": 1,
                    "needs": [
                            "A02"
                    ],
                    "aspects": [
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Los MO = MK op wanneer de MK-functie in de opgave staat en niet uit TK hoeft te worden afgeleid."
            },
            {
                    "id": "B01",
                    "name": "Schaarste als kerneconomisch probleem",
                    "layer": 1,
                    "needs": [],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Herken schaarste als de basisvoorwaarde van alle economische keuzes: middelen (tijd, geld, grondstoffen) zijn beperkt terwijl wensen onbeperkt zijn, waardoor keuzes onvermijdelijk zijn."
            },
            {
                    "id": "B02",
                    "name": "Alternatieve kosten in een keuze-situatie",
                    "layer": 2,
                    "needs": [
                            "B01"
                    ],
                    "aspects": [
                            "verbaal",
                            "rekenen"
                    ],
                    "desc": "Identificeer de alternatieve kosten van een keuze als de opbrengst van het beste niet-gekozen alternatief, en bereken deze expliciet wanneer de cijfers gegeven zijn."
            },
            {
                    "id": "D01",
                    "name": "Accijnsopbrengst uit grafiek",
                    "layer": 5,
                    "needs": [
                            "D05"
                    ],
                    "aspects": [
                            "grafisch",
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Bepaal accijnsopbrengst door verhandelde hoeveelheid na belasting met belastingbedrag te vermenigvuldigen."
            },
            {
                    "id": "D02",
                    "name": "Constante kosten en winst",
                    "layer": 1,
                    "needs": [],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Constante kosten beïnvloeden break-even analyse maar niet het MO = MK optimum."
            },
            {
                    "id": "D03",
                    "name": "Consumentensurplus en accijns",
                    "layer": 5,
                    "needs": [
                            "D05",
                            "A30"
                    ],
                    "aspects": [
                            "grafisch",
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Accijns verhoogt prijs, consumenten betalen meer, consumentensurplus daalt."
            },
            {
                    "id": "D05",
                    "name": "Evenwicht bij accijns",
                    "layer": 4,
                    "needs": [
                            "A23"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Bereken nieuw evenwicht en accijnsopbrengst na invoering van een heffing."
            },
            {
                    "id": "D06",
                    "name": "Vraagreactie via prijselasticiteit interpreteren",
                    "layer": 2,
                    "needs": [
                            "A15"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Gebruik de prijselasticiteit van de vraag (Ev) om te voorspellen hoe Qv reageert op een prijsverandering en verklaar het resultaat in context."
            },
            {
                    "id": "D07",
                    "name": "Heffing afwentelingspercentage berekenen",
                    "layer": 1,
                    "needs": [
                            "D42",
                            "A38"
                    ],
                    "aspects": [
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Bereken welk percentage van een heffing bij consumenten en producenten terechtkomt nadat de euro-bedragen van de belastingdruk bekend zijn."
            },
            {
                    "id": "D08",
                    "name": "Heffing tegen overconsumptie",
                    "layer": 2,
                    "needs": [
                            "A15"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Analyseer of een heffing overconsumptie tegengaat via veranderde vraag."
            },
            {
                    "id": "D09",
                    "name": "Homogene en heterogene goederen",
                    "layer": 1,
                    "needs": [],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Homogene goederen zijn identiek; heterogene goederen verschillen in kwaliteit of kenmerken."
            },
            {
                    "id": "D10",
                    "name": "Vraag/aanbod-verschuiving bij conjunctuurschok",
                    "layer": 3,
                    "needs": [
                            "A06",
                            "D33"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Analyseer hoe een conjunctuurschok de collectieve vraaglijn of aanbodlijn verschuift en wat dit doet met evenwichtsprijs en -hoeveelheid."
            },
            {
                    "id": "D11",
                    "name": "Inkomenselasticiteit berekenen en interpreteren",
                    "layer": 3,
                    "needs": [
                            "A17"
                    ],
                    "aspects": [
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Bereken Ei uit twee waarnemingen en interpreteer de uitkomst in de context van het goed."
            },
            {
                    "id": "D12",
                    "name": "Kruiselasticiteit en substituten",
                    "layer": 3,
                    "needs": [
                            "A16"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Bepaal uit kruiselasticiteit of goederen substituten zijn en analyseer vraagverschuivingen."
            },
            {
                    "id": "D13",
                    "name": "Kostenstijging en aanbodverschuiving",
                    "layer": 3,
                    "needs": [
                            "A06",
                            "D33"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Analyseer hoe een stijging van productiekosten (zoals loon per eenheid product) de collectieve aanbodlijn verschuift en doorwerkt in evenwichtsprijs."
            },
            {
                    "id": "D14",
                    "name": "Marktfalen en overheidsinterventie beoordelen",
                    "layer": 6,
                    "needs": [
                            "F18",
                            "F02",
                            "G02",
                            "A35",
                            "D28"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Beoordeel of marktwerking tot een doelmatige uitkomst leidt en of overheidsinterventie gerechtvaardigd is."
            },
            {
                    "id": "D15",
                    "name": "Marktvormen classificeren",
                    "layer": 1,
                    "needs": [],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Classificeer markten aan hand van aantal aanbieders, aard van goederen en toetreding."
            },
            {
                    "id": "D16",
                    "name": "Minimumprijs en werkloosheid",
                    "layer": 3,
                    "needs": [
                            "D34",
                            "L10"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Minimumloon boven marktloon veroorzaakt vraagoverschot van arbeid en werkloosheid."
            },
            {
                    "id": "D17",
                    "name": "Monopolie minimaal verlies",
                    "layer": 3,
                    "needs": [
                            "A14"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Onderneming met alleen vaste kosten heeft MK = 0, dus MK = GVK. Minimaal verlies waar prijs totale opbrengst dekt."
            },
            {
                    "id": "D18",
                    "name": "Monopolie met prijsdiscriminatie",
                    "layer": 6,
                    "needs": [
                            "D24",
                            "A36"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Bepaal hoe monopolist winst behaalt via prijsdiscriminatie over verschillende markten."
            },
            {
                    "id": "D19",
                    "name": "Subsidie en Pareto-efficiëntie",
                    "layer": 5,
                    "needs": [
                            "D20",
                            "A27"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Leg uit of een subsidie-evenwicht Pareto-efficiënt is."
            },
            {
                    "id": "D20",
                    "name": "Pareto-efficiëntie in marktevenwicht",
                    "layer": 4,
                    "needs": [
                            "A19"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Leg uit wanneer een marktevenwicht Pareto-efficiënt is."
            },
            {
                    "id": "D21",
                    "name": "Prijsdiscriminatie over inkomensgroepen",
                    "layer": 7,
                    "needs": [
                            "D18",
                            "D28"
                    ],
                    "aspects": [
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Analyseer hoe bedrijven prijzen differentieren en welvaartsgevolgen per inkomensgroep."
            },
            {
                    "id": "D22",
                    "name": "Prijsdiscriminatie en subsidies",
                    "layer": 4,
                    "needs": [
                            "D24",
                            "A27"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Herken of subsidies prijsdiscriminatie veroorzaken en analyseer gevolgen."
            },
            {
                    "id": "D24",
                    "name": "Drie voorwaarden prijsdiscriminatie",
                    "layer": 2,
                    "needs": [
                            "D35",
                            "D15"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Leg uit de drie voorwaarden voor prijsdiscriminatie: voldoende marktmacht, scheidbare deelmarkten met verschillende prijselasticiteiten en betalingsbereidheid."
            },
            {
                    "id": "D25",
                    "name": "Prijselasticiteit en omzet",
                    "layer": 2,
                    "needs": [
                            "A15"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Bij inelastische vraag leidt grotere hoeveelheid tot lagere prijs; totale omzet kan dalen."
            },
            {
                    "id": "D26",
                    "name": "Soorten variabele kosten classificeren",
                    "layer": 2,
                    "needs": [
                            "A08"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Onderscheid tussen degressief, progressief en proportioneel variabele kosten."
            },
            {
                    "id": "D27",
                    "name": "Substituten en complementen",
                    "layer": 1,
                    "needs": [],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Substituten vervangen elkaar; complementen worden samen gebruikt."
            },
            {
                    "id": "D28",
                    "name": "Welvaart en surplus-effect",
                    "layer": 5,
                    "needs": [
                            "A19",
                            "A30"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Prijsverlaging verhoogt consumentensurplus; effect op producentensurplus verschilt per geval."
            },
            {
                    "id": "D29",
                    "name": "Welvaartsverlies bij subsidie",
                    "layer": 6,
                    "needs": [
                            "A32"
                    ],
                    "aspects": [
                            "grafisch",
                            "rekenen"
                    ],
                    "desc": "Bepaal en arceer het deadweight loss ontstaan door subsidies als gevolg van allocatieve inefficientie."
            },
            {
                    "id": "D30",
                    "name": "Winstmaximalisatie MO = MK",
                    "layer": 4,
                    "needs": [
                            "A12",
                            "A13"
                    ],
                    "aspects": [
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Winstmaximale hoeveelheid vind je waar marginale opbrengst gelijk is aan marginale kosten."
            },
            {
                    "id": "D31",
                    "name": "Indexpunt versus procentuele verandering",
                    "layer": 2,
                    "needs": [
                            "A38",
                            "A39"
                    ],
                    "aspects": [
                            "verbaal",
                            "rekenen"
                    ],
                    "desc": "Onderscheid een indexpunt-verandering (absoluut verschil tussen twee indexcijfers) van een procentuele verandering (relatief verschil); beide kunnen leiden tot totaal andere conclusies bij hoge indexwaarden."
            },
            {
                    "id": "D32",
                    "name": "Verschuiving versus beweging langs de curve",
                    "layer": 1,
                    "needs": [],
                    "aspects": [
                            "verbaal",
                            "grafisch"
                    ],
                    "desc": "Onderscheid een beweging langs de vraag- of aanbodcurve (veroorzaakt door eigen-prijsverandering) van een verschuiving van de curve (veroorzaakt door een andere factor dan eigen prijs)."
            },
            {
                    "id": "D33",
                    "name": "Vraag- en aanbodverschuivingsfactoren benoemen",
                    "layer": 2,
                    "needs": [
                            "D32"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Noem en herken de standaard verschuivingsfactoren: voor vraag (inkomen, voorkeuren, prijzen substituten/complementen, verwachtingen) en voor aanbod (inputprijzen, technologie, aantal aanbieders, verwachtingen, overheidsbeleid)."
            },
            {
                    "id": "D34",
                    "name": "Bindende prijsregulering: voorwaarde voor effect",
                    "layer": 2,
                    "needs": [
                            "A06"
                    ],
                    "aspects": [
                            "verbaal",
                            "grafisch"
                    ],
                    "desc": "Herken dat een maximumprijs alleen effect heeft als deze onder het evenwicht ligt, en een minimumprijs alleen als deze erboven ligt; anders is de regulering niet-bindend en heeft geen invloed op uitkomst."
            },
            {
                    "id": "D35",
                    "name": "Betalingsbereidheid definiëren",
                    "layer": 1,
                    "needs": [],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Definieer betalingsbereidheid als de maximale prijs die een consument bereid is te betalen voor één extra eenheid van een goed; deze kan dalen naarmate meer eenheden al gekocht zijn."
            },
            {
                    "id": "D36",
                    "name": "Beslisregel: koop als P ≤ betalingsbereidheid",
                    "layer": 2,
                    "needs": [
                            "D35"
                    ],
                    "aspects": [
                            "verbaal",
                            "rekenen"
                    ],
                    "desc": "Pas de consumentenbeslissingsregel toe: een consument koopt een extra eenheid precies dan wanneer zijn betalingsbereidheid voor die eenheid ≥ de marktprijs P; gebruik dit om de individuele vraag bij een gegeven P te bepalen."
            },
            {
                    "id": "D37",
                    "name": "Wet van de vraag verbaal uitleggen",
                    "layer": 3,
                    "needs": [
                            "D35",
                            "D36"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Leg uit waarom de vraagcurve dalend is: bij een lagere prijs vinden meer consumenten het waardevol om te kopen (hun betalingsbereidheid overschrijdt de prijs), en individuele consumenten zijn bereid meer eenheden te kopen doordat hun dalende betalingsbereidheid dan nog steeds boven P ligt."
            },
            {
                    "id": "D38",
                    "name": "GCK daalt door spreiding van constante kosten",
                    "layer": 3,
                    "needs": [
                            "D02"
                    ],
                    "aspects": [
                            "verbaal",
                            "rekenen"
                    ],
                    "desc": "Leg uit dat gemiddelde constante kosten dalen wanneer dezelfde constante kosten over meer producten worden verdeeld."
            },
            {
                    "id": "D39",
                    "name": "Totale surplus als CS plus PS",
                    "layer": 6,
                    "needs": [
                            "D28"
                    ],
                    "aspects": [
                            "grafisch",
                            "rekenen"
                    ],
                    "desc": "Bereken totale surplus als de som van consumentensurplus en producentensurplus."
            },
            {
                    "id": "D40",
                    "name": "Surplusrekening bij marktinterventie controleren",
                    "layer": 7,
                    "needs": [
                            "D39"
                    ],
                    "aspects": [
                            "grafisch",
                            "rekenen"
                    ],
                    "desc": "Controleer of de veranderingen in surplus, overheidsinkomsten of -uitgaven en verloren surplus samen consistent zijn."
            },
            {
                    "id": "D41",
                    "name": "Belastingwig en Pc/Pp grafisch labelen",
                    "layer": 5,
                    "needs": [
                            "D05"
                    ],
                    "aspects": [
                            "grafisch",
                            "verbaal"
                    ],
                    "desc": "Label in een P-Q diagram de consumentenprijs Pc, producentenprijs Pp, belastingwig t = Pc - Pp en de verhandelde hoeveelheid Qt na een heffing."
            },
            {
                    "id": "D42",
                    "name": "Belastingdruk in eurobedragen berekenen",
                    "layer": 0,
                    "needs": [],
                    "aspects": [
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Bereken in euro per eenheid welk deel van een heffing door consument en producent wordt gedragen."
            },
            {
                    "id": "D43",
                    "name": "Subsidie-evenwicht en effectieve prijzen bepalen",
                    "layer": 2,
                    "needs": [
                            "A41"
                    ],
                    "aspects": [
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Bepaal na een subsidie de consumentenprijs Pc, de effectieve producentenontvangst Pp en de nieuwe hoeveelheid."
            },
            {
                    "id": "D45",
                    "name": "Incidentie verklaren met relatieve elasticiteiten",
                    "layer": 2,
                    "needs": [
                            "A15"
                    ],
                    "aspects": [
                            "verbaal",
                            "grafisch"
                    ],
                    "desc": "Leg uit dat de relatief minder elastische kant van de markt meer belastingdruk draagt of meer subsidievoordeel ontvangt."
            },
            {
                    "id": "D46",
                    "name": "Kostenstijging doorberekenen als pass-through share",
                    "layer": 3,
                    "needs": [],
                    "aspects": [
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Bereken welk percentage van een kostenstijging in de prijs wordt doorberekend en houd dit gescheiden van de procentuele prijsverandering in A93."
            },
            {
                    "id": "D47",
                    "name": "Gelijktijdige vraag- en aanbodverschuiving analyseren",
                    "layer": 4,
                    "needs": [
                            "A06",
                            "A42",
                            "D13",
                            "D32",
                            "D33"
                    ],
                    "aspects": [
                            "verbaal",
                            "grafisch"
                    ],
                    "desc": "Analyseer bij gelijktijdige verschuivingen van vraag en aanbod welke richting van het marktevenwicht bepaald is en welke zonder relatieve grootte ambigu blijft."
            },
            {
                    "id": "E01",
                    "name": "Intergenerationele ruil",
                    "layer": 2,
                    "needs": [
                            "E02"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Analyseer hoe pensioenstelsels intergenerationele ruil faciliteren."
            },
            {
                    "id": "E02",
                    "name": "Intertemporele ruil in pensioenstelsels",
                    "layer": 1,
                    "needs": [],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Leg uit hoe pensioenen ruil over tijd vertegenwoordigen."
            },
            {
                    "id": "E03",
                    "name": "Kapitaaldekking en renteeffecten",
                    "layer": 5,
                    "needs": [
                            "E02",
                            "H15"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Analyseer hoe rentes de betaalbaarheid van kapitaalgedekte pensioenen onder druk zetten."
            },
            {
                    "id": "E04",
                    "name": "Omslagstelsel (AOW)",
                    "layer": 3,
                    "needs": [
                            "E01",
                            "E02"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Omslagstelsel: werkenden betalen premie voor huidige uitkeringen; gevoelig voor vergrijzing."
            },
            {
                    "id": "E05",
                    "name": "Pensioenkorting en intergenerationele solidariteit",
                    "layer": 5,
                    "needs": [
                            "E04",
                            "H01"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Analyseer hoe een korting op pensioenuitkeringen de solidariteit tussen jongere premiebetalers en oudere ontvangers beïnvloedt."
            },
            {
                    "id": "E06",
                    "name": "Voorraad- en stroomgrootheden onderscheiden",
                    "layer": 1,
                    "needs": [],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Onderscheid tussen voorraad- en stroomgrootheden."
            },
            {
                    "id": "E07",
                    "name": "Koop- versus huurlasten vergelijken",
                    "layer": 5,
                    "needs": [
                            "E02",
                            "H15"
                    ],
                    "aspects": [
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Vergelijk netto woonlasten van kopen en huren door rente, aflossing, onderhoud en huurprijs systematisch tegen elkaar af te zetten."
            },
            {
                    "id": "F01",
                    "name": "Berovingsprobleem herkennen",
                    "layer": 1,
                    "needs": [],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Bij relatiespecifieke investeringen loopt de investerende partij het risico dat de ander na de investering het contract heronderhandelt of verbreekt."
            },
            {
                    "id": "F02",
                    "name": "Collectief goed classificeren",
                    "layer": 1,
                    "needs": [],
                    "aspects": [
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Herken collectieve goederen aan hand van excludeerbaarheid en rivaliteit."
            },
            {
                    "id": "F03",
                    "name": "Dominante strategie",
                    "layer": 1,
                    "needs": [],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Dominante strategie is de beste keuze voor een speler ongeacht wat de ander doet."
            },
            {
                    "id": "F04",
                    "name": "Dominante strategieën in pay-off matrix",
                    "layer": 2,
                    "needs": [
                            "F03"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Identificeer dominante strategieën van beide spelers in een pay-off matrix en bepaal de uitkomst waarbij elke speler zijn dominante strategie kiest."
            },
            {
                    "id": "F05",
                    "name": "Emissierechten als prikkel",
                    "layer": 5,
                    "needs": [
                            "F07",
                            "F10"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Verhandelbare emissierechten zetten een prijs op vervuiling, waardoor bedrijven een prikkel krijgen om uitstoot te verminderen of schoner te produceren."
            },
            {
                    "id": "F06",
                    "name": "Heffing op externe effecten als innovatieprikkel",
                    "layer": 3,
                    "needs": [
                            "F07"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Een heffing op negatieve externe effecten verhoogt de private kosten van vervuilen en geeft bedrijven daarmee een prikkel om te investeren in schonere technologie."
            },
            {
                    "id": "F07",
                    "name": "Overproductie bij negatieve externe effecten",
                    "layer": 2,
                    "needs": [
                            "F16"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Bij negatieve externe effecten liggen de maatschappelijke kosten hoger dan de private kosten, waardoor de markt meer produceert dan maatschappelijk optimaal is."
            },
            {
                    "id": "F08",
                    "name": "Verloren surplus door negatieve externe effecten",
                    "layer": 3,
                    "needs": [
                            "F07"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Productie of consumptie voorbij het maatschappelijk optimum leidt tot verloren surplus: het verschil tussen maatschappelijke kosten en baten op de extra eenheden."
            },
            {
                    "id": "F09",
                    "name": "Gevangenendilemma",
                    "layer": 2,
                    "needs": [
                            "F03"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Situatie waarbij dominante strategie leidt tot suboptimale uitkomst voor beide spelers."
            },
            {
                    "id": "F10",
                    "name": "Internalisatie van externe effecten",
                    "layer": 4,
                    "needs": [
                            "F07",
                            "F08"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Door de externe kosten of baten via heffing, subsidie of rechten in de prijs op te nemen, komt de marktuitkomst dichter bij het maatschappelijk optimum."
            },
            {
                    "id": "F11",
                    "name": "Lumpsum-subsidie bij positieve externe effecten",
                    "layer": 5,
                    "needs": [
                            "F10"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Een lumpsum-subsidie vergoedt de producent voor positieve externe effecten zonder de marginale beslissing te verstoren, zodat een maatschappelijk gewenste activiteit rendabel wordt."
            },
            {
                    "id": "F12",
                    "name": "Nash-evenwicht in pay-off matrix",
                    "layer": 2,
                    "needs": [
                            "F03"
                    ],
                    "aspects": [
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Bepaal het Nash-evenwicht in een pay-off matrix: de uitkomst waarbij geen van beide spelers zijn strategie wil veranderen gegeven de keuze van de ander."
            },
            {
                    "id": "F13",
                    "name": "Berovingsprobleem op de arbeidsmarkt",
                    "layer": 2,
                    "needs": [
                            "F01"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Pas het berovingsprobleem toe op de arbeidsmarkt: kortere opzegtermijnen verhogen het risico voor werkgevers op relatiespecifieke scholingsinvesteringen, wat loonkosten en investeringsbereidheid beïnvloedt."
            },
            {
                    "id": "F14",
                    "name": "Concentratie-externaliteiten analyseren",
                    "layer": 4,
                    "needs": [
                            "F08"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Analyseer hoe ruimtelijke of sectorale concentratie van economische activiteit negatieve externe effecten versterkt en wanneer ingrijpen maatschappelijk gewenst is."
            },
            {
                    "id": "F15",
                    "name": "Verzonken kosten negeren in beslissingen",
                    "layer": 1,
                    "needs": [],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Verzonken kosten zijn niet terugvorderbare uitgaven uit het verleden en horen geen rol te spelen in toekomstgerichte beslissingen; alleen toekomstige opbrengsten en kosten tellen mee."
            },
            {
                    "id": "F16",
                    "name": "MPC–MSC en MPB–MSB onderscheiden",
                    "layer": 1,
                    "needs": [],
                    "aspects": [
                            "verbaal",
                            "grafisch"
                    ],
                    "desc": "Onderscheid private van sociale marginale kosten/opbrengsten: bij een negatief extern effect is MSC = MPC + externe kost/eenheid, bij een positief extern effect is MSB = MPB + externe baat/eenheid."
            },
            {
                    "id": "F17",
                    "name": "Over- en onderproductiegap bij externaliteiten",
                    "layer": 2,
                    "needs": [
                            "A06",
                            "F16"
                    ],
                    "aspects": [
                            "rekenen",
                            "grafisch"
                    ],
                    "desc": "Bereken de productie-gap tussen marktuitkomst en sociaal optimum: bij negatieve externaliteiten produceert de markt Q_markt > Q_sociaal (overproductie); bij positieve externaliteiten Q_markt < Q_sociaal (onderproductie)."
            },
            {
                    "id": "F18",
                    "name": "Pigou-heffing en corrigerende subsidie bepalen",
                    "layer": 3,
                    "needs": [
                            "F16",
                            "F17",
                            "A41"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Bepaal de omvang van de corrigerende overheidsinstrument: een Pigou-heffing gelijk aan de externe kost per eenheid (bij negatieve externaliteiten) of een subsidie gelijk aan de externe baat per eenheid (bij positieve externaliteiten) laat de marktuitkomst samenvallen met het sociaal optimum."
            },
            {
                    "id": "F19",
                    "name": "Maatschappelijke kosten verbaal herkennen",
                    "layer": 0,
                    "needs": [],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Herken dat een keuze, productie of consumptie kosten veroorzaakt die niet door de directe gebruiker of producent worden gedragen."
            },
            {
                    "id": "F20",
                    "name": "Maatschappelijke kosten uitleggen met voorbeeld",
                    "layer": 1,
                    "needs": [
                            "F19"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Geef een contextspecifiek voorbeeld van maatschappelijke of externe kosten en leg uit waarom die kosten bij anderen of de samenleving terechtkomen."
            },
            {
                    "id": "G01",
                    "name": "Risicoinschatting en averechtse selectie",
                    "layer": 3,
                    "needs": [
                            "G10",
                            "G02"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Betere risicoinschatting door verzekeraars vermindert informatieasymmetrie en verkleint daardoor averechtse selectie op de verzekeringsmarkt."
            },
            {
                    "id": "G02",
                    "name": "Averechtse selectie herkennen",
                    "layer": 2,
                    "needs": [
                            "G10"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Herken averechtse selectie als gevolg van informatieasymmetrie op markten."
            },
            {
                    "id": "G03",
                    "name": "Onderlinge risicopool zonder informatieasymmetrie",
                    "layer": 2,
                    "needs": [
                            "G10"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "In een kleine, vertrouwde risicopool ontbreekt informatieasymmetrie omdat deelnemers elkaars risicoprofiel kennen, waardoor averechtse selectie en moreel wangedrag beperkt blijven."
            },
            {
                    "id": "G04",
                    "name": "Eigen risico en moral hazard",
                    "layer": 2,
                    "needs": [
                            "G10"
                    ],
                    "aspects": [
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Eigen risico geeft verzekerden een prikkel om voorzichtiger te handelen."
            },
            {
                    "id": "G05",
                    "name": "Belangentegenstelling in principaal-agentrelatie",
                    "layer": 2,
                    "needs": [
                            "G06"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "In een principaal-agentrelatie verschillen de belangen van principaal en agent, waardoor de agent keuzes kan maken die ten koste gaan van de principaal."
            },
            {
                    "id": "G06",
                    "name": "Principaal-agentprobleem identificeren",
                    "layer": 1,
                    "needs": [],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Identificeer principaal-agentrelaties en de problemen die daaruit voortvloeien."
            },
            {
                    "id": "G07",
                    "name": "Transactiekosten berekenen en interpreteren",
                    "layer": 1,
                    "needs": [],
                    "aspects": [
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Bereken de totale transactiekosten van een ruil door zoek-, onderhandel- en controlekosten bij elkaar op te tellen en beoordeel of de ruil na aftrek nog rendabel is."
            },
            {
                    "id": "G08",
                    "name": "Risicodeling via gemeenschappelijk fonds",
                    "layer": 1,
                    "needs": [],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Een gemeenschappelijk fonds vlakt individuele risico's uit door premies te bundelen en kostenverschillen tussen deelnemers te compenseren."
            },
            {
                    "id": "G09",
                    "name": "Gepersonaliseerde premies ondermijnen solidariteit",
                    "layer": 2,
                    "needs": [
                            "G08"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Premies gebaseerd op individuele risicoprofielen verkleinen de herverdeling tussen lage- en hogerrisicogroepen en ondermijnen zo de solidariteit in een collectieve verzekering."
            },
            {
                    "id": "G10",
                    "name": "Informatieasymmetrie verzekeringsmarkt",
                    "layer": 1,
                    "needs": [],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Informatieongelijkheid tussen verzekeraar en klant kan selectie- en moraalrisicoproblemen veroorzaken."
            },
            {
                    "id": "G11",
                    "name": "Wisselkoersrisico bij internationale handel",
                    "layer": 1,
                    "needs": [],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Bij betalingen in vreemde valuta leidt een ongunstige wisselkoersverandering tussen contractmoment en betalingsmoment tot lagere reële opbrengsten voor de exporteur of hogere kosten voor de importeur."
            },
            {
                    "id": "G12",
                    "name": "Verzekeringspremie berekenen uit verwachte schade",
                    "layer": 1,
                    "needs": [
                            "A38"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Bereken een verzekeringspremie als verwachte schade (kans × schadebedrag) plus opslag voor administratiekosten en risico-/winstmarge; interpreteer verschillen in premie tussen risicogroepen."
            },
            {
                    "id": "H01",
                    "name": "AOW-leeftijd als houdbaarheidsinstrument",
                    "layer": 4,
                    "needs": [
                            "E04"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Leg uit hoe een hogere AOW-leeftijd via premiegrondslag en uitkeringsduur de houdbaarheid van het AOW-stelsel verbetert bij vergrijzing."
            },
            {
                    "id": "H02",
                    "name": "AIQ (arbeidsinkomenquote) berekenen",
                    "layer": 1,
                    "needs": [
                            "A02"
                    ],
                    "aspects": [
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Bereken de arbeidsinkomenquote: (arbeidsinkomen / nationaal inkomen) x 100%."
            },
            {
                    "id": "H03",
                    "name": "Armington-elasticiteit en importbeleid",
                    "layer": 2,
                    "needs": [
                            "A15"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Bereken de Armington-elasticiteit en beoordeel daarmee hoe sterk importvraag reageert op een prijsverandering van binnenlandse versus buitenlandse varianten."
            },
            {
                    "id": "H04",
                    "name": "Belastingschijven berekening",
                    "layer": 1,
                    "needs": [
                            "A02"
                    ],
                    "aspects": [
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Belastingdruk bepaald aan hand van marginaal tarief en betreffende schijven."
            },
            {
                    "id": "H05",
                    "name": "Circulaire economie in groen bbp",
                    "layer": 1,
                    "needs": [],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Leg uit hoe circulaire productie via minder milieuschade en minder grondstofgebruik het groen bbp per hoofd verhoogt."
            },
            {
                    "id": "H06",
                    "name": "Totale CO2-uitstoot berekenen",
                    "layer": 2,
                    "needs": [
                            "A06"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Bereken totale milieueffect van marktveranderingen door per-eenheid emissie met hoeveelheid te vermenigvuldigen."
            },
            {
                    "id": "H07",
                    "name": "Vergrijzing, spaarquote en rente",
                    "layer": 5,
                    "needs": [
                            "H01"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Hogere sparende populatie vergroot kapitaalaanbod, wat de evenwichtsrente drukt."
            },
            {
                    "id": "H08",
                    "name": "Denivellering en progressieve belasting",
                    "layer": 2,
                    "needs": [
                            "H04"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Denivellering treedt op wanneer belastingveranderingen het verschil in netto-inkomsten tussen inkomensgroepen verkleinen."
            },
            {
                    "id": "H09",
                    "name": "Kostenvoordeel exporteurs als protectionisme",
                    "layer": 3,
                    "needs": [
                            "H03"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Beargumenteer wanneer een kostenvoordeel voor binnenlandse exporteurs (bv. gratis toegewezen emissierechten) feitelijk werkt als protectionisme tegen buitenlandse concurrenten."
            },
            {
                    "id": "H10",
                    "name": "Gini-coefficient bij recessie",
                    "layer": 1,
                    "needs": [],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Gini-coefficient stijgt tijdens recessie door werkloosheidsconcentratie en toename inkomensongelijkheid."
            },
            {
                    "id": "H11",
                    "name": "Groen bbp en CO2",
                    "layer": 3,
                    "needs": [
                            "H05",
                            "H06"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Lagere CO2-uitstoot vergroot groen bbp; minder productie wegens minder emissierechten verkleint het."
            },
            {
                    "id": "H12",
                    "name": "Houdbaarheidssaldo",
                    "layer": 5,
                    "needs": [
                            "H01"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Het houdbaarheidssaldo geeft aan of overheidsvoorzieningen op lange termijn betaalbaar blijven; stijgende grijze druk verslechtert het saldo."
            },
            {
                    "id": "H13",
                    "name": "Minimumuurloon: kostenkanaal naar concurrentiepositie",
                    "layer": 4,
                    "needs": [
                            "D13"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Redeneer via het kostenkanaal hoe een hoger minimumuurloon de internationale concurrentiepositie kan verslechteren."
            },
            {
                    "id": "H14",
                    "name": "Minimumuurloon: vraagkanaal naar bbp-groei",
                    "layer": 2,
                    "needs": [
                            "I14"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Redeneer via het bestedingskanaal hoe een hoger minimumuurloon de consumptie en daarmee de bbp-groei kan verhogen."
            },
            {
                    "id": "H15",
                    "name": "Nominale rente op staatsobligaties verklaren",
                    "layer": 4,
                    "needs": [
                            "H30",
                            "H31"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Verklaar bewegingen in de nominale rente op staatsobligaties vanuit vraag-en-aanbod op de obligatiemarkt en risicoperceptie."
            },
            {
                    "id": "H16",
                    "name": "Soepeler ontslagrecht en werkgeversrisico",
                    "layer": 1,
                    "needs": [],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Leg uit hoe versoepeling van ontslagrecht het aannamerisico voor werkgevers verlaagt en het effect op werkgelegenheid beredeneer."
            },
            {
                    "id": "H17",
                    "name": "Arbeidsproductiviteit, werkgelegenheid en lange termijn",
                    "layer": 5,
                    "needs": [
                            "H13"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Onderscheid het korte-termijn werkgelegenheidseffect van productiviteitsverhogende investeringen van het lange-termijn concurrentie-effect."
            },
            {
                    "id": "H18",
                    "name": "Progressief tarief berekenen",
                    "layer": 2,
                    "needs": [
                            "H04"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Bereken totale belasting bij progressieve tarieven en analyseer stimulansen."
            },
            {
                    "id": "H19",
                    "name": "Publiek kapitaal en staatsschuldquote",
                    "layer": 2,
                    "needs": [
                            "H21"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Leg uit hoe investeringen in publiek kapitaal op lange termijn staatsschuldquote kunnen verlagen."
            },
            {
                    "id": "H20",
                    "name": "Spaarsaldo en betalingsbalans",
                    "layer": 2,
                    "needs": [
                            "H21"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Interpreteer positieve en negatieve particuliere spaarsalda."
            },
            {
                    "id": "H21",
                    "name": "Staatsschuldquote berekenen",
                    "layer": 1,
                    "needs": [],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Bereken staatsschuldquote = staatsschuld / bbp x 100% en bepaal drempels voor duurzaamheid."
            },
            {
                    "id": "H22",
                    "name": "Belastingtariefaanpassing en secundaire inkomenseffecten",
                    "layer": 3,
                    "needs": [
                            "H04",
                            "H08"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Analyseer hoe een wijziging in belastingtarieven via veranderd besteedbaar inkomen de vraag en daarmee secundaire inkomenseffecten oproept."
            },
            {
                    "id": "H23",
                    "name": "Belastingwig en uitverdieneffect op arbeidsaanbod",
                    "layer": 3,
                    "needs": [
                            "H18"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Leg uit hoe een hogere belastingwig via het substitutie-effect het arbeidsaanbod verkleint (uitverdieneffect)."
            },
            {
                    "id": "H24",
                    "name": "Wisselkoers en depreciatie",
                    "layer": 1,
                    "needs": [
                            "A38"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Bereken wisselkoerseffecten van depreciatie en leg uit hoe deze reële inkomens beïnvloeden."
            },
            {
                    "id": "H25",
                    "name": "Wisselkoers, export en bbp-groei",
                    "layer": 2,
                    "needs": [
                            "H24"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Leg uit hoe een depreciatie van de wisselkoers via goedkopere export tot hogere bbp-groei kan leiden."
            },
            {
                    "id": "H27",
                    "name": "Productiefunctie Y = A·f(K, L) toepassen",
                    "layer": 6,
                    "needs": [
                            "H17"
                    ],
                    "aspects": [
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Pas de productiefunctie Y = A·f(K, L) toe: verklaar hoe groei in kapitaal K, arbeid L en totale factorproductiviteit A bijdraagt aan lange-termijn productie; herken afnemend grensproduct wanneer K óf L alleen toeneemt."
            },
            {
                    "id": "H28",
                    "name": "Betalingsbalans: saldo lopende rekening",
                    "layer": 2,
                    "needs": [
                            "H24"
                    ],
                    "aspects": [
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Bereken het saldo op de lopende rekening van de betalingsbalans uit netto-export (goederen + diensten), primair inkomen (netto-factorinkomen uit buitenland) en secundair inkomen (overdrachten); interpreteer een overschot als binnenlandse besparingen > investeringen."
            },
            {
                    "id": "H29",
                    "name": "Obligatie als verhandelbaar schuldpapier",
                    "layer": 1,
                    "needs": [],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Benoem wat een obligatie is — een verhandelbaar schuldpapier met vaste nominale waarde, couponrente en looptijd — en onderscheid de primaire markt (emissie/veiling door de uitgever) van de secundaire markt (handel tussen beleggers)."
            },
            {
                    "id": "H30",
                    "name": "Vraag en aanbod op de obligatiemarkt",
                    "layer": 2,
                    "needs": [
                            "H29",
                            "D32"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Leg uit hoe vraag en aanbod op de secundaire obligatiemarkt samen de obligatiekoers bepalen. Noem de drie belangrijkste demand-shifters (risicoperceptie, alternatieve rendementen, inflatieverwachting) en de belangrijkste supply-shifter (nieuwe uitgiften door overheid of bedrijven)."
            },
            {
                    "id": "H31",
                    "name": "Inverse relatie obligatiekoers en rente",
                    "layer": 3,
                    "needs": [
                            "H29",
                            "H30"
                    ],
                    "aspects": [
                            "verbaal",
                            "rekenen"
                    ],
                    "desc": "Leg uit dat obligatiekoers en effectief rendement omgekeerd bewegen: bij gelijke couponstroom betekent een hogere aankoopkoers een lager effectief rendement, en omgekeerd."
            },
            {
                    "id": "I01",
                    "name": "Anticyclisch begrotingsbeleid",
                    "layer": 1,
                    "needs": [],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Beschrijf hoe de overheid in laagconjunctuur bestedingen verhoogt of belastingen verlaagt en in hoogconjunctuur het omgekeerde doet om de conjunctuurcyclus af te vlakken."
            },
            {
                    "id": "I02",
                    "name": "Automatische stabilisatoren via inkomensoverdrachten",
                    "layer": 2,
                    "needs": [
                            "I01"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Leg uit hoe inkomensoverdrachten zoals WW en bijstand automatisch meebewegen met de conjunctuur en zo de bestedingen stabiliseren zonder nieuw beleid."
            },
            {
                    "id": "I03",
                    "name": "Renteongevoeligheid van investeringen bij ondergrens",
                    "layer": 6,
                    "needs": [
                            "I17"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Leg uit waarom bedrijfsinvesteringen beperkt reageren op renteverlagingen als de vraag laag is of de effectieve ondergrens nominale rente nadert."
            },
            {
                    "id": "I04",
                    "name": "CAO-looptijd en loonrigiditeit",
                    "layer": 4,
                    "needs": [
                            "L19"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Leg uit hoe langere CAO-looptijden loonaanpassingen vertragen en daarmee de flexibiliteit van de arbeidsmarkt en de effectiviteit van conjunctuurbeleid beïnvloeden."
            },
            {
                    "id": "I05",
                    "name": "Rentebesluit van centrale bank",
                    "layer": 6,
                    "needs": [
                            "I17",
                            "I07"
                    ],
                    "aspects": [
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Bepaal op basis van inflatie, outputgap en duaal mandaat of een centrale bank de beleidsrente verhoogt, verlaagt of constant houdt."
            },
            {
                    "id": "I06",
                    "name": "Deflatiespiraal",
                    "layer": 1,
                    "needs": [],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Leg uit hoe dalende prijzen consumenten en bedrijven aanzetten tot uitstel van bestedingen en investeringen, waardoor de laagconjunctuur zichzelf versterkt."
            },
            {
                    "id": "I07",
                    "name": "IS-MB-GA-model: outputgap en inflatie",
                    "layer": 5,
                    "needs": [
                            "I10",
                            "I14"
                    ],
                    "aspects": [
                            "grafisch",
                            "verbaal"
                    ],
                    "desc": "Analyseer met het IS-MB-GA-model hoe een schok via outputgap en inflatie doorwerkt op rente, bbp en prijsniveau."
            },
            {
                    "id": "I08",
                    "name": "Keynesiaans kruis: verschuivingen analyseren",
                    "layer": 2,
                    "needs": [
                            "I14"
                    ],
                    "aspects": [
                            "grafisch",
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Analyseer hoe een verandering in autonome bestedingen (C, I, G of X−M) de geplande bestedingen verschuift en via de multiplier een nieuw evenwicht op Y = bestedingen oplevert."
            },
            {
                    "id": "I09",
                    "name": "Koopkrachtbehoud bij inflatie berekenen",
                    "layer": 1,
                    "needs": [
                            "A02"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Bereken de nominale loon- of uitkeringsstijging die nodig is om de koopkracht gelijk te houden bij een gegeven inflatiepercentage."
            },
            {
                    "id": "I10",
                    "name": "Loonrigiditeit en helling GA-curve",
                    "layer": 4,
                    "needs": [
                            "L19"
                    ],
                    "aspects": [
                            "grafisch",
                            "verbaal"
                    ],
                    "desc": "Leg uit hoe starre lonen leiden tot een vlakkere GA-curve op korte termijn en hoe flexibele lonen de curve steiler maken."
            },
            {
                    "id": "I11",
                    "name": "Monetair beleid: starre versus flexibele arbeidsmarkt",
                    "layer": 7,
                    "needs": [
                            "I10",
                            "I05"
                    ],
                    "aspects": [
                            "grafisch",
                            "verbaal"
                    ],
                    "desc": "Vergelijk het effect van een renteverlaging op bbp en prijsniveau tussen een starre en een flexibele arbeidsmarkt en verklaar het verschil via de helling van de GA-curve."
            },
            {
                    "id": "I12",
                    "name": "Wisselkoerskanaal van rentebeleid",
                    "layer": 6,
                    "needs": [
                            "I17",
                            "I20"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Leg uit hoe een renteverlaging via kapitaaluitstroom leidt tot depreciatie van de valuta en daarmee de exportcompetitiviteit vergroot."
            },
            {
                    "id": "I13",
                    "name": "Monetair trilemma",
                    "layer": 7,
                    "needs": [
                            "I12"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Analyseer waarom een land hooguit twee van de drie doelen — vaste wisselkoers, vrij kapitaalverkeer en zelfstandig rentebeleid — tegelijk kan bereiken."
            },
            {
                    "id": "I14",
                    "name": "Multiplier en lekkages",
                    "layer": 1,
                    "needs": [],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Leg uit hoe een toename van autonome bestedingen via de multiplier een groter inkomenseffect oproept en hoe belastingen, spaarneiging en import als lekkages de multiplier verkleinen."
            },
            {
                    "id": "I15",
                    "name": "Outputgap bij vraag- en aanbodschokken",
                    "layer": 6,
                    "needs": [
                            "I07",
                            "I14"
                    ],
                    "aspects": [
                            "grafisch",
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Analyseer hoe een positieve of negatieve vraag- of aanbodschok de feitelijke productie ten opzichte van het potentieel bbp verschuift en een output gap veroorzaakt."
            },
            {
                    "id": "I16",
                    "name": "Overheidssaldo en conjunctuur",
                    "layer": 2,
                    "needs": [
                            "H21"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Leg uit hoe belastingontvangsten en overheidsuitgaven samen het overheidssaldo bepalen en hoe dit saldo met de conjunctuur meebeweegt."
            },
            {
                    "id": "I17",
                    "name": "Rentebeleid en transmissiemechanisme",
                    "layer": 5,
                    "needs": [
                            "H15"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Leg uit hoe een renteverhoging via duurder krediet consumptie en investeringen afremt en hoe een renteverlaging deze bestedingen stimuleert."
            },
            {
                    "id": "I18",
                    "name": "Reële waarde van nominaal eigen risico",
                    "layer": 2,
                    "needs": [
                            "I09"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Leg uit hoe inflatie de reële last van een nominaal vast eigen risico verlaagt en waarom herziening nodig is om het beleidsdoel vast te houden."
            },
            {
                    "id": "I19",
                    "name": "Wisselkoerseffect van monetair beleid op conjunctuur",
                    "layer": 7,
                    "needs": [
                            "I12",
                            "H24"
                    ],
                    "aspects": [
                            "rekenen",
                            "verbaal"
                    ],
                    "desc": "Leg uit hoe rentebeleid via de wisselkoers de netto export verandert en zo de binnenlandse conjunctuur beïnvloedt."
            },
            {
                    "id": "I20",
                    "name": "Internationale kapitaalmobiliteit en rentepariteit",
                    "layer": 2,
                    "needs": [
                            "H24"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Leg uit waarom een relatief hogere binnenlandse rente buitenlands kapitaal aantrekt en een relatieve renteverlaging kapitaal doet wegvloeien; deze kapitaalbewegingen drijven via vraag en aanbod op de valutamarkt de wisselkoers."
            },
            {
                    "id": "L01",
                    "name": "Waarde marginaal product (VMP)",
                    "layer": 1,
                    "needs": [],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Bereken VMP = marginaal product × prijs per eenheid output uit een tabel met aflopende marginale productiviteit, en gebruik VMP als grens voor de individuele arbeidsvraag."
            },
            {
                    "id": "L02",
                    "name": "Inhuurregel VMP ≥ W",
                    "layer": 2,
                    "needs": [
                            "L01"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Bepaal hoeveel werkenden een werkgever aanneemt door VMP per werkende met het loon W te vergelijken: neem aan zolang VMP ≥ W, stop zodra VMP < W."
            },
            {
                    "id": "L03",
                    "name": "Afgeleide vraag (derived demand)",
                    "layer": 1,
                    "needs": [],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Leg uit waarom de vraag naar arbeid een afgeleide vraag is: werkgevers vragen arbeid omdat consumenten de eindproducten willen kopen, niet omdat arbeid zelf gewenst is."
            },
            {
                    "id": "L04",
                    "name": "Arbeidsvraagcurve tekenen uit VMP",
                    "layer": 2,
                    "needs": [
                            "L01"
                    ],
                    "aspects": [
                            "grafisch"
                    ],
                    "desc": "Teken de individuele arbeidsvraagcurve van een werkgever door VMP per werkende op de verticale as en de werknemersrij op de horizontale as uit te zetten; het resultaat is de dalende VMP-curve."
            },
            {
                    "id": "L05",
                    "name": "Beroepsbevolking, niet-beroepsbevolking, werkloze beroepsbevolking",
                    "layer": 1,
                    "needs": [],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Definieer beroepsbevolking (iedereen van 15–75 die werkt of werk zoekt), niet-beroepsbevolking (wel die leeftijd maar werkt niet en zoekt geen werk) en werkloze beroepsbevolking (zoekt werk, heeft nog geen baan)."
            },
            {
                    "id": "L06",
                    "name": "Bruto participatiegraad berekenen",
                    "layer": 2,
                    "needs": [
                            "L05"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Bereken de bruto participatiegraad = beroepsbevolking / bevolking 15–75 × 100, en interpreteer het resultaat als het percentage dat actief is op de arbeidsmarkt."
            },
            {
                    "id": "L07",
                    "name": "Werkloosheidspercentage berekenen",
                    "layer": 2,
                    "needs": [
                            "L05"
                    ],
                    "aspects": [
                            "rekenen"
                    ],
                    "desc": "Bereken het werkloosheidspercentage = werkloze beroepsbevolking / beroepsbevolking × 100; de noemer is de beroepsbevolking, niet de totale bevolking."
            },
            {
                    "id": "L08",
                    "name": "Effect van loonstijging op participatiegraad",
                    "layer": 3,
                    "needs": [
                            "L05",
                            "L06"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Leg uit dat een aanhoudende loonstijging mensen uit de niet-beroepsbevolking kan trekken naar de beroepsbevolking, waardoor de participatiegraad stijgt."
            },
            {
                    "id": "L09",
                    "name": "Krappe versus ruime arbeidsmarkt",
                    "layer": 2,
                    "needs": [
                            "L05"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Herken een krappe arbeidsmarkt (arbeidsvraag > arbeidsaanbod, oplopende lonen) versus een ruime arbeidsmarkt (arbeidsaanbod > arbeidsvraag, dalende lonen en oplopende werkloosheid)."
            },
            {
                    "id": "L10",
                    "name": "Arbeidsmarktevenwicht als transfer van goederenmarkt",
                    "layer": 2,
                    "needs": [
                            "A02",
                            "A04",
                            "A06"
                    ],
                    "aspects": [
                            "rekenen",
                            "grafisch"
                    ],
                    "desc": "Pas het goederenmarkt-evenwichtsraamwerk toe op de arbeidsmarkt door W voor P en werkenden voor Q te substitueren; los Qa = Qv op voor W* en bereken de evenwichtswerkgelegenheid."
            },
            {
                    "id": "L11",
                    "name": "Conjuncturele werkloosheid",
                    "layer": 2,
                    "needs": [
                            "L05"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Definieer conjuncturele werkloosheid als werkloosheid door tekortschietende bestedingen tijdens laagconjunctuur; verdwijnt als de economie herstelt."
            },
            {
                    "id": "L12",
                    "name": "Structurele werkloosheid",
                    "layer": 2,
                    "needs": [
                            "L05"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Definieer structurele werkloosheid als werkloosheid door blijvende mismatch tussen vaardigheden en vraag (bijvoorbeeld door automatisering of sectorverschuiving); blijft bestaan zonder gericht beleid."
            },
            {
                    "id": "L13",
                    "name": "Frictiewerkloosheid",
                    "layer": 2,
                    "needs": [
                            "L05"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Definieer frictiewerkloosheid als kortdurende werkloosheid tijdens het zoeken naar een nieuwe baan; is normaal en zelfs gezond op een dynamische arbeidsmarkt."
            },
            {
                    "id": "L14",
                    "name": "Werkloosheid classificeren uit context",
                    "layer": 3,
                    "needs": [
                            "L11",
                            "L12",
                            "L13"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Classificeer een werkloosheidssituatie als conjunctureel, structureel of frictioneel op basis van de oorzaak (bestedingstekort, skills-mismatch, of tussen-banen-zoektijd)."
            },
            {
                    "id": "L15",
                    "name": "Beleidsinstrument koppelen aan type werkloosheid",
                    "layer": 4,
                    "needs": [
                            "L14"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Koppel het juiste beleidsinstrument aan elk type werkloosheid: fiscale stimulus voor conjunctureel, herscholing/onderwijs voor structureel, vacaturebemiddeling voor frictioneel."
            },
            {
                    "id": "L16",
                    "name": "Werknemers- en werkgeverssurplus bij minimumloon",
                    "layer": 4,
                    "needs": [
                            "A02",
                            "A04",
                            "A06",
                            "A10",
                            "A19",
                            "L10"
                    ],
                    "aspects": [
                            "rekenen",
                            "grafisch"
                    ],
                    "desc": "Bereken werknemerssurplus (arbeidsmarkt-CS) en werkgeverssurplus (arbeidsmarkt-PS) voor en na invoering van een minimumloon; identificeer welvaartsverlies als de \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"verloren driehoek\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\" bij W_min > W*."
            },
            {
                    "id": "L17",
                    "name": "CAO als bindende loonafspraak",
                    "layer": 4,
                    "needs": [
                            "D16"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Leg uit dat een CAO (collectieve arbeidsovereenkomst) dat lonen boven het evenwichtsloon afspreekt werkt als een bindend minimumloon voor de gehele sector, met werkloosheid als gevolg."
            },
            {
                    "id": "L18",
                    "name": "Voordelen en nadelen van vakbonden",
                    "layer": 5,
                    "needs": [
                            "L17"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Noem voordelen van vakbonden voor werkenden (hogere lonen, betere voorwaarden, collectieve onderhandelingsmacht) en nadelen (hogere loonkosten voor werkgevers, lagere werkgelegenheid, insiders vs outsiders)."
            },
            {
                    "id": "L19",
                    "name": "Loonstarheid",
                    "layer": 3,
                    "needs": [
                            "L09"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Definieer loonstarheid als de neiging van lonen om traag (vooral omlaag) aan te passen aan veranderingen in arbeidsmarkt-omstandigheden, met als gevolg persistente werkloosheid na een negatieve schok."
            },
            {
                    "id": "L20",
                    "name": "Loonflexibiliteit versus actief arbeidsmarktbeleid",
                    "layer": 4,
                    "needs": [
                            "L19"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Vergelijk twee beleidsreacties op werkloosheid: verlagen van de loonvloer (wacht op loondaling) versus actief arbeidsmarktbeleid (herscholing, bemiddeling); beoordeel op effectiviteit per type werkloosheid."
            },
            {
                    "id": "L21",
                    "name": "Standpuntbepaling minimumloon",
                    "layer": 5,
                    "needs": [
                            "L16"
                    ],
                    "aspects": [
                            "verbaal"
                    ],
                    "desc": "Schrijf een beoordeel-antwoord over het minimumloon dat beide kanten benoemt: hogere lonen voor wie nog werk heeft versus werkloosheid voor wie uitgeprijsd wordt; onderbouw met surplus-berekeningen."
            }
    ];
    var GENERATOR_BLOCKED_SKILLS = [
            {
                    "id": "A20",
                    "name": "Winstmaximum oplossen met afgeleide MO en MK",
                    "generator": "GEN_A20",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A45",
                    "name": "P-Q grafiek tekenen uit tabel",
                    "generator": "GEN_A45",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A46",
                    "name": "Waarden aflezen en interpoleren in P-Q grafiek",
                    "generator": "GEN_A46",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A47",
                    "name": "Collectieve vraag uit tabellen optellen",
                    "generator": "GEN_A47",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A48",
                    "name": "Collectieve vraagfunctie algebraisch optellen",
                    "generator": "GEN_A48",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A49",
                    "name": "Aanbodcurve tekenen met economenassen",
                    "generator": "GEN_A49",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A50",
                    "name": "GVK en GCK berekenen",
                    "generator": "GEN_A50",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A51",
                    "name": "Overschot en tekort bij niet-evenwichtsprijs berekenen",
                    "generator": "GEN_A51",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A52",
                    "name": "MK en MO uit tabelverschillen berekenen",
                    "generator": "GEN_A52",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A53",
                    "name": "MK benaderen uit kwadratische TK-functie",
                    "generator": "GEN_A53",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A54",
                    "name": "Winstoptimum controleren met Q-1, Q en Q+1",
                    "generator": "GEN_A54",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A55",
                    "name": "Gevraagde hoeveelheid voorspellen met elasticiteit",
                    "generator": "GEN_A55",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A56",
                    "name": "Korte zijde bepalen bij bindende prijs",
                    "generator": "GEN_A56",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A57",
                    "name": "Afwentelingspercentage berekenen",
                    "generator": "GEN_A57",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A58",
                    "name": "Subsidie-uitgaven berekenen",
                    "generator": "GEN_A58",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A59",
                    "name": "Opkoopkosten bij minimumprijs berekenen",
                    "generator": "GEN_A59",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A60",
                    "name": "Vraagfunctie inverteren bij quotumhoeveelheid",
                    "generator": "GEN_A60",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A64",
                    "name": "Aandelen aflezen uit cirkeldiagram",
                    "generator": "GEN_A64",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A65",
                    "name": "Absolute hoeveelheid berekenen uit aandeel en totaal",
                    "generator": "GEN_A65",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A66",
                    "name": "Basiswaarde en vergelijkingswaarde in bron bepalen",
                    "generator": "GEN_A66",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A67",
                    "name": "Procentuele verandering berekenen vanuit tabel",
                    "generator": "GEN_A67",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A68",
                    "name": "Procentuele verandering berekenen vanuit staafdiagram",
                    "generator": "GEN_A68",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A69",
                    "name": "Procentuele verandering berekenen vanuit lijngrafiek",
                    "generator": "GEN_A69",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A70",
                    "name": "Percentagepuntverandering in aandeel herkennen",
                    "generator": "GEN_A70",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A72",
                    "name": "Indexcijfer berekenen vanuit tabel",
                    "generator": "GEN_A72",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A73",
                    "name": "Indexverandering aflezen uit lijngrafiek",
                    "generator": "GEN_A73",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A74",
                    "name": "Procentuele verandering berekenen vanuit indexcijfers",
                    "generator": "GEN_A74",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A75",
                    "name": "Totale winst berekenen uit opbrengsten- en kostentabel",
                    "generator": "GEN_A75",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A76",
                    "name": "Totale winst berekenen uit P, GTK en Q",
                    "generator": "GEN_A76",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A77",
                    "name": "Break-even aflezen uit TO-TK-grafiek",
                    "generator": "GEN_A77",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A78",
                    "name": "Winst of verlies aflezen uit TO-TK-grafiek",
                    "generator": "GEN_A78",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A79",
                    "name": "Maximale winst bepalen uit TO-TK-tabel",
                    "generator": "GEN_A79",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A80",
                    "name": "Noem of geef-aan antwoord geven",
                    "generator": "GEN_A80",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A81",
                    "name": "Bron gebruiken in een antwoord",
                    "generator": "GEN_A81",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A82",
                    "name": "Elasticiteit berekenen uit tabelwaarden",
                    "generator": "GEN_A82",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A83",
                    "name": "Prijselasticiteit van de vraag berekenen uit P-Q-grafiek",
                    "generator": "GEN_A83",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A84",
                    "name": "Omzetverandering beoordelen met elasticiteit uit bron",
                    "generator": "GEN_A84",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A85",
                    "name": "Totale opbrengst puntberekening: TO = P x Q",
                    "generator": "GEN_A85",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A86",
                    "name": "TVK berekenen uit constante variabele kosten",
                    "generator": "GEN_A86",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A87",
                    "name": "Onbekende vaste kosten berekenen uit winstvergelijking",
                    "generator": "GEN_A87",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A88",
                    "name": "Schaalfactoren in examencijfers toepassen",
                    "generator": "GEN_A88",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A89",
                    "name": "GO herkennen als prijsfunctie van de monopolist",
                    "generator": "GEN_A89",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A90",
                    "name": "MO bepalen uit lineaire GO-regel zonder afgeleiden",
                    "generator": "GEN_A90",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A91",
                    "name": "MO = gegeven MK oplossen",
                    "generator": "GEN_A91",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A92",
                    "name": "Nieuwe prijs bepalen na winstmaximaliserende Q",
                    "generator": "GEN_A92",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A93",
                    "name": "Procentuele prijsverandering na kostenverandering",
                    "generator": "GEN_A93",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A94",
                    "name": "MO = P en afgeleide MK oplossen",
                    "generator": "GEN_A94",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A96",
                    "name": "Bereken-vraag beantwoorden",
                    "generator": "GEN_A96",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A97",
                    "name": "Leg-uit-dat antwoord opbouwen",
                    "generator": "GEN_A97",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A98",
                    "name": "Leg-uit-of antwoord opbouwen",
                    "generator": "GEN_A98",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            },
            {
                    "id": "A99",
                    "name": "Leg uit met voorbeeld beantwoorden",
                    "generator": "GEN_A99",
                    "status": "missing_generator_implementation",
                    "studentFacingSkilltreeUseAllowed": false
            }
    ];

    var LAYER_NAMES = ['Fundament', 'Bouwstenen', 'Marginale grootheden', 'Samengesteld', 'Gevorderd', 'Eindbazen'];
    var LAYER_COLORS = [
        { bg:'#1a3353', text:'#7cb9e8', glow:'rgba(26,82,118,0.35)' },
        { bg:'#2a1f4e', text:'#b8a9e8', glow:'rgba(136,78,160,0.3)' },
        { bg:'#1a3a3a', text:'#7dcec0', glow:'rgba(30,132,120,0.3)' },
        { bg:'#1a3a2a', text:'#7dcea0', glow:'rgba(30,132,73,0.3)' },
        { bg:'#3a1a2a', text:'#e07a9a', glow:'rgba(180,60,100,0.3)' },
        { bg:'#4a2a1a', text:'#f0b27a', glow:'rgba(230,126,34,0.3)' }
    ];

    return {
        SKILLS: SKILLS,
        ROUTE_SKILLS: ROUTE_SKILLS,
        GENERATOR_BLOCKED_SKILLS: GENERATOR_BLOCKED_SKILLS,
        LAYER_NAMES: LAYER_NAMES,
        LAYER_COLORS: LAYER_COLORS,
        GEN: GEN,
        helpers: { ri: ri, pick: pick, round1: round1, round2: round2, mcStep: mcStep }
    };
});
