"""Karteikarten-Inhalte: BBT – Normen, HOAI, Kosten (DIN 276), Flächen (DIN 277)."""

SKETCH_TOLERANZTRICHTER = """
<div style="background:#ffffff;border-radius:8px;padding:12px;max-width:440px">
<svg viewBox="0 0 360 230" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="monospace" font-size="10">
<line x1="40" y1="15" x2="40" y2="195" stroke="#5d6a63"/>
<line x1="40" y1="105" x2="345" y2="105" stroke="#5d6a63"/>
<polygon points="70,30 135,55 200,67 265,80 330,105 265,130 200,143 135,155 70,180"
  fill="#fbe3d6" stroke="#d9480f" stroke-width="2"/>
<line x1="40" y1="105" x2="330" y2="105" stroke="#1d2420" stroke-dasharray="4 3"/>
<text x="36" y="33" text-anchor="end" fill="#1d2420">+30%</text>
<text x="36" y="108" text-anchor="end" fill="#1d2420">0</text>
<text x="36" y="183" text-anchor="end" fill="#1d2420">−30%</text>
<text x="345" y="99" text-anchor="end" fill="#5d6a63">Kostenvorgabe</text>
<text x="200" y="12" text-anchor="middle" fill="#5d6a63">zulässige Abweichung</text>
<g fill="#1d2420" text-anchor="middle">
<text x="70" y="208">KR</text><text x="135" y="208">KS</text><text x="200" y="208">KB</text>
<text x="265" y="208">KA</text><text x="330" y="208">KF</text></g>
<g fill="#5d6a63" text-anchor="middle">
<text x="70" y="222">LPH 1</text><text x="135" y="222">LPH 2</text><text x="200" y="222">LPH 3</text>
<text x="265" y="222">LPH 6/7</text><text x="330" y="222">LPH 8</text></g>
</svg></div>
"""

SKETCH_DIN277 = """
<div style="background:#ffffff;border-radius:8px;padding:12px;max-width:440px">
<svg viewBox="0 0 360 175" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="monospace" font-size="11">
<rect x="10" y="10" width="340" height="40" rx="3" fill="#1d2420"/>
<text x="180" y="34" text-anchor="middle" fill="#ffffff">Brutto-Grundfläche BGF</text>
<rect x="10" y="60" width="250" height="40" rx="3" fill="#d9480f"/>
<text x="135" y="84" text-anchor="middle" fill="#ffffff">Netto-Raumfläche NRF</text>
<rect x="265" y="60" width="85" height="40" rx="3" fill="#c9d0c8"/>
<text x="307" y="78" text-anchor="middle" fill="#1d2420">Konstr.-GF</text>
<text x="307" y="92" text-anchor="middle" fill="#1d2420">KGF</text>
<rect x="10" y="110" width="150" height="40" rx="3" fill="#fbe3d6" stroke="#d9480f"/>
<text x="85" y="134" text-anchor="middle" fill="#1d2420">Nutzfläche NUF</text>
<rect x="165" y="110" width="45" height="40" rx="3" fill="#fbe3d6" stroke="#d9480f"/>
<text x="187" y="134" text-anchor="middle" fill="#1d2420">TF</text>
<rect x="215" y="110" width="45" height="40" rx="3" fill="#fbe3d6" stroke="#d9480f"/>
<text x="237" y="134" text-anchor="middle" fill="#1d2420">VF</text>
<text x="10" y="168" fill="#5d6a63">BGF = NRF + KGF   ·   NRF = NUF + TF + VF</text>
</svg></div>
"""

CARDS = [
    {
        "id": 1, "topic": "Normen",
        "q": "Wodurch charakterisieren sich DIN-Normen: Wer gibt sie heraus? Wann gelten sie? "
             "Was kann es bedeuten, wenn sie nicht eingehalten werden?",
        "a": """
- Herausgeber: **DIN – Deutsches Institut für Normung e.V.**, eine privatwirtschaftliche Institution.
- Private technische Regelwerke mit **Empfehlungscharakter**: verbindlich nur, wenn sie vertraglich
  vereinbart oder per Gesetz/Verordnung eingeführt sind.
- Sie gelten oft als **allgemein anerkannte Regeln der Technik**. Werden sie dann nicht eingehalten,
  liegt in der Regel ein **Baumangel** vor.
""",
    },
    {
        "id": 2, "topic": "Normen",
        "q": "Definieren Sie den Begriff „Allgemein anerkannte Regeln der Technik“.",
        "a": """
Technische Regeln, die in der Wissenschaft als theoretisch richtig anerkannt sind, den nach
neuestem Erkenntnisstand ausgebildeten Fachleuten bekannt sind und sich in der **Praxis dauerhaft
bewährt** haben.
""",
    },
    {
        "id": 3, "topic": "HOAI",
        "q": "Was bedeutet die Abkürzung HOAI, und was regelt sie?",
        "a": """
- **Honorarordnung für Architekten und Ingenieure**
- Regelt die Honorare und beschreibt die Leistungen, die Architektur- und Ingenieurbüros
  üblicherweise erbringen (Leistungsbilder).
""",
    },
    {
        "id": 4, "topic": "HOAI",
        "q": "Das Leistungsbild für Gebäude und Innenräume nach HOAI hat in jeder Leistungsphase "
             "2 Teile. Welche? Was unterscheidet sie?",
        "a": """
- **Grundleistungen**: zur ordnungsgemäßen Erfüllung erforderlich, werden in der Regel immer geschuldet.
- **Besondere Leistungen**: müssen zusätzlich vereinbart werden; dafür steht dem Planer
  zusätzliches Honorar zu.
""",
    },
    {
        "id": 5, "topic": "HOAI",
        "q": "Nennen Sie mind. 6 der 9 Leistungsphasen der HOAI.",
        "a": """
1. Grundlagenermittlung
2. Vorplanung
3. Entwurfsplanung
4. Genehmigungsplanung
5. Ausführungsplanung
6. Vorbereitung der Vergabe
7. Mitwirkung bei der Vergabe
8. Objektüberwachung (Bauüberwachung)
9. Objektbetreuung
""",
    },
    {
        "id": 6, "topic": "HOAI",
        "q": "Mit welchen Leistungsphasen hat der Bautechniker i.d.R. hauptsächlich zu tun?",
        "a": """
- LPH 6 – Vorbereitung der Vergabe
- LPH 7 – Mitwirkung bei der Vergabe
- LPH 8 – Objektüberwachung
""",
    },
    {
        "id": 7, "topic": "Kosten",
        "q": "Welcher Zusammenhang besteht zwischen der DIN 276 und der DIN 277?",
        "a": """
- **DIN 276** regelt die **Kosten im Bauwesen** (Kostengruppen, Stufen der Kostenermittlung).
- **DIN 277** regelt die **Grundflächen und Rauminhalte** von Bauwerken.
- Flächen und Rauminhalte der DIN 277 sind die **Bezugsgrößen** für Kostenkennwerte nach DIN 276,
  z.B. €/m² BGF oder €/m³ BRI.
""",
    },
    {
        "id": 8, "topic": "Kosten",
        "q": "Was versteht man unter „Bauwerkskosten“?",
        "a": """
Die Summe der Kostengruppen **300 (Bauwerk – Baukonstruktionen)** und
**400 (Bauwerk – Technische Anlagen)** nach DIN 276.
""",
    },
    {
        "id": 9, "topic": "Kosten",
        "q": "Nennen Sie die acht Kostengruppen der ersten Ebene (DIN 276).",
        "a": """
- **100** Grundstück
- **200** Vorbereitende Maßnahmen
- **300** Bauwerk – Baukonstruktionen
- **400** Bauwerk – Technische Anlagen
- **500** Außenanlagen und Freiflächen
- **600** Ausstattung und Kunstwerke
- **700** Baunebenkosten
- **800** Finanzierung

*Stand DIN 276:2018. Früher: KG 200 „Herrichten und Erschließen“, KG 500 „Außenanlagen“.*
""",
    },
    {
        "id": 10, "topic": "Kosten",
        "q": "Wie verhält man sich, wenn Kosten nicht eindeutig einer Kostengruppe zugeordnet "
             "werden können?",
        "a": """
- Der Kostengruppe zuordnen, der sie **überwiegend** bzw. sachlich am ehesten entsprechen,
  oder sinnvoll **aufteilen**.
- Die Zuordnung **dokumentieren** und im ganzen Projekt **einheitlich** beibehalten.
- Keine Kosten doppelt erfassen.
""",
    },
    {
        "id": 11, "topic": "Kosten",
        "q": "Erläutern Sie die „ausführungsorientierte“ Gliederung der Kosten: Wie werden Kosten "
             "gegliedert? Wann kommt sie zur Anwendung?",
        "a": """
- Gliederung nach **Gewerken / Leistungsbereichen / Vergabeeinheiten**
  (z.B. Erdarbeiten, Mauerarbeiten, Betonarbeiten – wie im StLB oder in der VOB/C).
- Anwendung bei **Vergabe und Ausführung** (LPH 6–8): Leistungsverzeichnisse, Kostenanschlag,
  Abrechnung, Vergleich mit Angeboten.
""",
    },
    {
        "id": 12, "topic": "Kosten",
        "q": "Erläutern Sie die „bauteilorientierte“ Gliederung der Kosten: Wie werden Kosten "
             "gegliedert? Wann kommt sie zur Anwendung?",
        "a": """
- Gliederung nach **Bauteilen / Kostengruppen der DIN 276**
  (z.B. 320 Gründung, 330 Außenwände, 340 Innenwände, 350 Decken, 360 Dächer).
- Anwendung in den **Planungsphasen** (LPH 1–3): Kostenrahmen, Kostenschätzung,
  Kostenberechnung, Vergleich mit Kostenkennwerten.
""",
    },
    {
        "id": 13, "topic": "Kostensteuerung",
        "q": "Was versteht man unter Kostenkontrolle und Kostensteuerung? Erläutern Sie beide Begriffe.",
        "a": """
- **Kostenkontrolle**: Vergleich einer aktuellen Kostenermittlung mit einer früheren bzw. mit der
  Kostenvorgabe (Soll-Ist-Vergleich). Abweichungen werden festgestellt und begründet.
- **Kostensteuerung**: gezieltes Eingreifen in Planung und Ausführung, um die Kostenentwicklung zu
  beeinflussen, vor allem bei Abweichungen von der Kostenvorgabe
  (z.B. Standards ändern, Alternativen wählen, Umfang reduzieren).

*Merksatz: Kontrolle stellt fest, Steuerung handelt.*
""",
    },
    {
        "id": 14, "topic": "Kostensteuerung",
        "q": "Was ist ein „Toleranztrichter“ für Bausummenüberschreitungen? Erläutern Sie dies mit "
             "einer Skizze.",
        "a": """
Der Toleranztrichter zeigt, dass die **zulässige Abweichung** der Kostenermittlungen mit
fortschreitender Planung **kleiner** wird, weil die Planung genauer wird. Er dient zur Beurteilung,
ob eine Überschreitung noch toleriert wird oder ein Planungsfehler (Haftung des Planers) vorliegt.
""",
        "sketch": SKETCH_TOLERANZTRICHTER,
        "a2": """
- Kostenrahmen ca. ±30–40 %
- Kostenschätzung ca. ±20–30 %
- Kostenberechnung ca. ±10–20 %
- Kostenanschlag ca. ±5–10 %
- Kostenfeststellung: tatsächliche Kosten

*Richtwerte aus Literatur und Rechtsprechung, nicht in der Norm festgelegt.
Bei vereinbarter Kostenobergrenze gibt es keine Toleranz.*
""",
    },
    {
        "id": 15, "topic": "Kostensteuerung",
        "q": "Was ist eine Kostenvorgabe?",
        "a": """
Die Festlegung der Kosten durch den Bauherrn als **Obergrenze** (Kostenobergrenze, darf nicht
überschritten werden) oder als **Zielgröße** für die Planung. Sie ist Maßstab für Kostenkontrolle
und Kostensteuerung; Grundlage ist meist das verfügbare Budget.
""",
    },
    {
        "id": 16, "topic": "Flächen",
        "q": "Wozu kann eine Flächenermittlung nach DIN 277 genutzt werden?",
        "a": """
- Bezugsgröße für **Kostenermittlung und Kostenkennwerte** (z.B. €/m² BGF)
- **Wirtschaftlichkeit** und Flächeneffizienz bewerten (z.B. NUF/BGF)
- **Vergleich** von Entwürfen und Gebäuden
- Bedarfsplanung und Raumprogramm prüfen
- Grundlage für Bewirtschaftung, Nutzungskosten und Mietflächen
""",
    },
    {
        "id": 17, "topic": "Flächen",
        "q": "Stellen Sie in einer Skizze dar, wie BGF, NRF, KGF, NUF, VF und TF nach DIN 277 "
             "zusammenhängen.",
        "a": "",
        "sketch": SKETCH_DIN277,
        "a2": """
- **BGF** Brutto-Grundfläche: Gesamtfläche aller Grundrissebenen
- **KGF** Konstruktions-Grundfläche: Wände, Stützen, Pfeiler
- **NRF** Netto-Raumfläche: nutzbare Fläche zwischen den Bauteilen
- **NUF** Nutzungsfläche: Flächen für die eigentliche Nutzung
- **TF** Technikfläche: Haustechnik, z.B. Heizraum
- **VF** Verkehrsfläche: Flure, Treppen, Aufzüge
""",
    },
]

LEVELS = [
    {"name": "Level 1 · Normen & HOAI", "goal": "Grundlagen: DIN-Normen, Regeln der Technik, HOAI",
     "ids": [1, 2, 3, 4, 5, 6]},
    {"name": "Level 2 · Kosten DIN 276", "goal": "Kostengruppen, Bauwerkskosten, Gliederungen",
     "ids": [7, 8, 9, 10, 11, 12]},
    {"name": "Level 3 · Kostensteuerung", "goal": "Kontrolle, Steuerung, Toleranztrichter, Kostenvorgabe",
     "ids": [13, 14, 15]},
    {"name": "Level 4 · Flächen DIN 277", "goal": "Nutzen der Flächenermittlung und Flächenaufbau",
     "ids": [16, 17]},
    {"name": "Level 5 · Abschlussprüfung", "goal": "Alle 17 Karten gemischt – wie in der Klausur",
     "ids": list(range(1, 18))},
]
