---
titel: Literatur
stand: 2026-11-21
pruefstand: gegen Verlags-, Norm- und Repository-Seiten geprüft am 2026-11-21
---

# Literatur

Regel: jede Angabe mit URL oder DOI, ein Satz „wofür", ein Satz „Einschränkung".
Wo die Primärquelle nicht eingesehen werden konnte, steht `[nicht verifiziert]` mit dem
Grund — nicht „zu prüfen" als Dauerzustand.

## Prüfstand: die fünf offenen Einträge

| Eintrag | Ergebnis | Was geändert wurde |
|---|---|---|
| DIN SPEC 33429 | **bestätigt, aber falsches Jahr** | Es ist nicht 2023, sondern **DIN SPEC 33429:2025-03**, 60 Seiten, kostenlos. Vollständige Angabe ergänzt. |
| ISO/IEC 25024 | **bestätigt** | Vollständiger Titel lautet „Systems and software engineering — … — Measurement of data quality", Edition 1, 2015-10, 45 Seiten; Status 2022 bestätigt. |
| Batini et al. 2009 | **bestätigt** | Autoren, Band 41(3), Article 16, Seiten 1–52 und DOI ergänzt. |
| Li et al. 2016 | **bestätigt** | Autorenliste vollständig, 17(2), 1–16, DOI ergänzt. |
| Fetterly et al. 2003 | **bestätigt** | Schreibweise **Fetterly** (nicht „Feyerly"), Seiten 669–678, DOI ergänzt; Journalfassung 2004 nachgewiesen. |

Zusätzlich bei der Prüfung gefunden und korrigiert, weil es sonst ein Zitierfehler
geworden wäre:

- **„Kumar, S., et al. (2020)" existiert nicht.** Die Autoren des Surveys mit DOI
  10.1145/3369876 sind **Mallawaarachchi, Meegahapola, Madhushanka, Heshan, Meedeniya,
  Jayarathna**. Der Name war falsch und ist ersetzt.
- **Weiss 2022** hat zwei Autoren (Weiss & Meurers), kein „et al.".
- **Der Policy-Readability-Aufsatz** ist von **Ruohonen**, nicht von „der Europäischen
  Union". Eintrag ersetzt.
- **Reineke 2005** ließ sich nicht belegen und ist **entfernt**; für 3.5 fehlt damit eine
  belastbare Quelle (siehe „Was noch fehlt").

---

## A. Rahmen: Informations- und Datenqualität

**Wang, R. Y., & Strong, D. M. (1996).** Beyond accuracy: What data quality means to
data consumers. *Journal of Management Information Systems*, 12(4), 5–33.
→ Kanonische empirische Herleitung von 15 Qualitätsdimensionen in vier Kategorien
(intrinsisch, kontextuell, repräsentational, Zugang). Wofür: Begründung, warum
„Informationsqualität" mehr ist als Korrektheit, und warum das Projekt fünf Dimensionen
untersucht.
Einschränkung: Empirie aus Wirtschaftsdaten der 1990er; auf Web-Informationsangebote nur
übertragen, nicht direkt anwendbar.

**ISO/IEC 25012:2008.** *Software engineering — Software product Quality Requirements and
Evaluation (SQuaRE) — Data quality model.* Genf: ISO/IEC. Edition 1, 2008-12.
<https://www.iso.org/standard/35736.html>
→ 15 Qualitätsmerkmale, darunter *Consistency* („attributes that are free from
contradiction and are coherent with other data in a specific context of use"),
*Currentness* („of the right age in a specific context of use"), *Completeness*,
*Accuracy*, *Understanding*. Wofür: zitierfähige Definition der eigenen Dimension und
Abgrenzung der fünf Team-Dimensionen gegeneinander.
Einschränkung: Standard für strukturierte Daten in Systemen, nicht für Webseiten; die
Übertragung ist selbst zu begründen. Status: 2025 zur Bestätigung überprüft, damit
aktuell gültig. **Normtext kostenpflichtig und nicht eingelesen** — zitiert wird die
Definition nach Katalog und Sekundärliteratur (u. a. Guerra-García et al. 2023).

**ISO/IEC 25024:2015.** *Systems and software engineering — Systems and software Quality
Requirements and Evaluation (SQuaRE) — Measurement of data quality.* Genf: ISO/IEC.
Edition 1, 2015-10, 45 S. <https://www.iso.org/standard/35749.html>
→ Definiert Messgrößen zu den Merkmalen aus 25012 (Basismaße je Merkmal, Zielentitäten,
Anwendung im Datenlebenszyklus). Wofür: Vorbild für die Formulierung eigener Messgrößen
(Zähler, Nenner, Skala), statt Kennzahlen frei zu erfinden.
Einschränkung: 2022 zur Bestätigung überprüft, also aktuell. **Normtext kostenpflichtig
und nicht eingelesen**; zitiert wird der Anwendungsbereich nach ISO-Katalog.
Hinweis zur Zitierweise: nicht „25024" allein schreiben, sondern mit Jahr und Titel —
die SQuaRE-Reihe hat mehrere Teile.

**Batini, C., Cappiello, C., Francalanci, C., & Maurino, A. (2009).** Methodologies for
data quality assessment and improvement. *ACM Computing Surveys*, 41(3), Article 16,
1–52. <https://doi.org/10.1145/1541880.1541883>
→ Systematik von Bewertungsverfahren (intrinsisch vs. nutzungsbasiert), Vergleich über
Phasen, Techniken, Dimensionen und Systemtypen. Wofür: Einordnung, ob Qualität aus den
Daten selbst oder aus ihrer Nutzung bewertet wird — genau die Entscheidung, die bei 3.1
ansteht, und ein Beleg dafür, dass es dafür etablierte Verfahrensklassen gibt.
Einschränkung: Überblick von 2009, also vor der LLM-Extraktion; die Verfahrensklassen
gelten, die Werkzeuge nicht.

## B. Konsistenz und Widersprüche (3.1)

**Thorne, J., Vlachos, A., Christodoulopoulos, C., & Mittal, A. (2018).** FEVER: A
large-scale dataset for fact extraction and verification. In *Proceedings of NAACL-HLT
2018*, 809–819. <https://aclanthology.org/N18-1074.pdf>
→ 185.445 Aussagen, Labels Supported / Refuted / NotEnoughInfo, mit Belegstellen.
Wofür: Referenzrahmen für „wie prüft man eine Aussage gegen Quellen", und Beleg dafür,
dass selbst starke Systeme bei diesem Task früh bei rund 50 % lagen.
Einschränkung: englisch, Wikipedia-basiert, keine Domänentexte.

**Bowman, S. R., Angeli, G., Potts, C., & Manning, C. D. (2015).** A large annotated
corpus for learning natural language inference. In *Proceedings of EMNLP 2015*, 632–642.
→ SNLI, Grundlage der NLI-Familie. Wofür: „Contradiction Detection" als Baustein, wenn
zwei Fließtext-Aussagen verglichen werden.
Einschränkung: Hypothesen synthetisch erzeugt; die Verteilung weicht von echten
Verwaltungstexten ab (siehe nächster Eintrag).

**Conneau, A., Rinott, R., Lample, G., Williams, A., Bowman, S. R., Schwenk, H., &
Stoyanov, V. (2018).** XNLI: Evaluating cross-lingual sentence representations. In
*Proceedings of EMNLP 2018*, 2475–2485. <https://aclanthology.org/D18-1269.pdf>
→ NLI in 15 Sprachen, **inklusive Deutsch**. Wofür: Beleg, dass ein deutsches
NLI-Modell verfügbar und evaluiert ist — die Sprachfrage muss nicht selbst gelöst werden.
Einschränkung: Übersetzungsdaten, keine juristischen Register.

**Pielka, M., Rode, F., Pucknat, L., Deußer, T., & Sifa, R. (2022).** A Linguistic
Investigation of Machine Learning based Contradiction Detection Models: An Empirical
Analysis and Future Perspectives. *ICMLA 2022*, 5 S.
<https://arxiv.org/abs/2210.10434>
→ Prüft, ob SNLI und ein selbst erhobenes deutsches Korpus dieselben Widerspruchstypen
enthalten; Ergebnis: nein, synthetische Daten sind zu einfach. Wofür: **wichtiges
Argument im Bericht**, warum ein eigenes deutsches Goldstandardset nötig ist und warum
man ein NLI-Modell nicht ungeprüft auf Verwaltungstexte anwendet.
Einschränkung: kleines Korpus, kurzer Konferenzbeitrag. Autoren und Venue am 21.11.2026
an der arXiv-Seite geprüft (v1, 19.10.2022; „Accepted at ICMLA 2022“). DOI:
<https://doi.org/10.48550/arXiv.2210.10434> — für das Literaturverzeichnis die
IEEE-Fassung nehmen, falls der Tagungsband zugänglich ist.

**Li, Y., Gao, J., Meng, C., Li, Q., Su, L., Zhao, B., Fan, W., & Han, J. (2016).**
A survey on truth discovery. *ACM SIGKDD Explorations Newsletter*, 17(2), 1–16.
<https://doi.org/10.1145/2897350.2897352>
→ Wie man aus widersprüchlichen Angaben mehrerer Quellen einen Wert schätzt
(Quellenzuverlässigkeit, iterative Schätzung, Majority Voting als Grenzfall). Wofür:
theoretischer Anker für die Frage, welche Quelle bei Widerspruch „recht" hat — und Beleg
dafür, dass die JLU das nicht trivial lösen kann.
Einschränkung: Ausgabe datiert Dezember 2015, online 25.02.2016; Zitierjahr 2016 ist
üblich, im Verzeichnis einheitlich halten.

**Bleiholder, J., & Naumann, F. (2009).** Data fusion. *ACM Computing Surveys*, 41(1),
Article 1, 1–41. <https://doi.org/10.1145/1456650.1456651>
→ Systematik des Zusammenführens widersprüchlicher Datensätze (Konfliktlösung,
Deduplizierung, Qualitätsbewertung). Wofür: Abgrenzung im Related Work — „Abweichung
melden" (3.1) ist nicht „Werte zusammenführen"; wer fusioniert, muss entscheiden, und
diese Entscheidung ist selbst ein Qualitätsproblem.
Einschränkung: Ausgabe Dezember 2008, online 15.01.2009 — Zitierjahr je nach Vorgabe
2008 oder 2009; eines wählen und durchhalten.

## C. Aktualität, Veraltung, Linkverfall (3.2)

**Klein, M., Van de Sompel, H., Sanderson, R., Shankar, H., Balakireva, L., Zhou, K.,
& Tobin, R. (2014).** Scholarly Context Not Found: One in Five Articles Suffers from
Reference Rot. *PLoS ONE*, 9(12), e115253.
<https://doi.org/10.1371/journal.pone.0115253>
→ Jeder fünfte Artikel betroffen; bei STM-Artikeln mit Web-Referenzen sieben von zehn.
Wofür: harte Vergleichszahl für „wie verbreitet ist Veraltung" — der eigene Befund
bekommt einen Bezugspunkt.
Einschränkung: wissenschaftliche Literatur, nicht Hochschul-Webseiten.

**Jones, S. M., Van de Sompel, H., Shankar, H., Klein, M., Tobin, R., & Grover, C.
(2016).** Scholarly Context Adrift: Three out of Four URI References Lead to Changed
Content. *PLoS ONE*, 11(12), e0167475.
<https://doi.org/10.1371/journal.pone.0167475>
→ 75 % der Verweise führen zu **verändertem** Inhalt, nicht nur zu totem Link. Wofür:
die konzeptionelle Kernunterscheidung der Arbeit — *link rot* ≠ *content drift*. Genau
die Unterscheidung, die in [[3.2 Aktualität]] als Viererteilung auftaucht.
Einschränkung: Stichprobe aus wissenschaftlichen Artikeln.

**Cho, J., & Garcia-Molina, H. (2000).** Synchronizing a database to improve freshness.
In *Proceedings of the 2000 ACM SIGMOD International Conference on Management of Data*,
117–128. <https://doi.org/10.1145/342009.335391>
→ 270 Websites über vier Monate; über 40 % der Seiten in `.com` ändern sich täglich,
`.edu`- und `.gov`-Seiten sind deutlich statischer. Wofür: begründete Erwartung, dass
JLU-Seiten langsamer veralten als kommerzielle — und damit eine prüfbare Vorab-Annahme.
Einschränkung: Daten von 1999/2000; Änderungsraten haben sich seither verschoben.

**Cho, J., & Garcia-Molina, H. (2003).** Effective page refresh policies for Web
crawlers. *ACM Transactions on Database Systems*, 28(4), 390–426.
<https://doi.org/10.1145/958942.958945>
→ Formales Frische-Maß und Poisson-Modell für Seitenänderungen. Wofür: Definition von
„Aktualität" als messbare Größe statt Gefühl; Vorlage für eigene Metriken.
Einschränkung: Optimierungsziel Suchmaschine, nicht Informationsqualität.

**Fetterly, D., Manasse, M., Najork, M., & Wiener, J. (2003).** A large-scale study of
the evolution of web pages. In *Proceedings of the 12th International Conference on
World Wide Web (WWW '03)*, 669–678. <https://doi.org/10.1145/775152.775246>
→ 150 Mio. Seiten über elf Wochen; Änderungsraten nach Top-Level-Domain, Größe und Typ;
rund 65 % der Seiten ohne Änderung im Beobachtungszeitraum. Wofür: Vergleichsbasis für
die eigene Stichprobe und Beleg, dass Domain und Seitentyp die Änderungsrate prägen.
Einschränkung: Web von 2003. Erweiterte Fassung: *Software: Practice and Experience*
34(2), 213–237 (2004), <https://doi.org/10.1002/spe.577>.

**Mallawaarachchi, V., Meegahapola, L., Madhushanka, R., Heshan, E., Meedeniya, D., &
Jayarathna, S. (2020).** Change Detection and Notification of Web Pages: A Survey.
*ACM Computing Surveys*, 53(1), Article 15, 1–35.
<https://doi.org/10.1145/3369876>
→ Systematik von Änderungserkennung: was als Änderung zählt, wie man Rauschen
(Navigation, Banner, Datumsanzeigen) trennt, welche Vergleichsverfahren es gibt.
Wofür: direkt anwendbar beim Vergleich von Seitenfassungen — und Beleg, dass Boilerplate
das Hauptproblem ist.
Einschränkung: Ingenieursperspektive, wenig zu inhaltlicher Bewertung.
Hinweis: Dieser Survey lief in einer früheren Fassung dieser Notiz unter dem falschen
Verfassernamen „Kumar et al."; die Angabe ist korrigiert.

**Pew Research Center (2024).** When Online Content Disappears.
<https://www.pewresearch.org/data-labs/2024/05/17/when-online-content-disappears>
→ 38 % der 2013 existierenden Webseiten sind zehn Jahre später nicht mehr erreichbar.
Wofür: aktuelle, allgemein verständliche Kennzahl für die Einleitung.
Einschränkung: Report eines Think Tanks, keine Peer-Review; als Illustration, nicht als
Beleg im Methodenteil verwenden.

**Massicotte, M., & Botter, K. (2017).** Reference Rot in the Repository: A Case Study
of Electronic Theses and Dissertations (ETDs) in an Academic Library. *Information
Technology and Libraries*, 36(1). <https://doi.org/10.6017/ital.v36i1.9598>
→ 23 % Linkverfall, davon etwa die Hälfte mit Content Drift. Wofür: methodisches
Vorbild — eine Studie, die beide Größen getrennt berichtet, so wie es hier geplant ist.

## D. Verständlichkeit (3.4)

**Amstad, T. (1978).** *Wie verständlich sind unsere Zeitungen?* Dissertation,
Universität Zürich.
→ Deutsche Anpassung der Flesch-Formel: `FRE = 180 − ASL − 58,5 × ASW`
(ASL = mittlere Satzlänge in Wörtern, ASW = mittlere Silbenzahl je Wort).
Wofür: Index 1 von 3; in TextLab und vielen Werkzeugen implementiert.
`[nicht verifiziert]` Titel und Umfangsangabe stammen aus gängiger Zitation und
Sekundärstellen (u. a. „Amstad 1978, S. 78ff"), die Dissertation selbst wurde nicht
eingesehen. Vor der Abgabe im Katalog der Zentralbibliothek Zürich prüfen oder durch
eine Quelle ersetzen, die die Formel primär belegt.

**Bamberger, R., & Vanecek, E. (1984).** *Lesen – Verstehen – Lernen – Schreiben.*
Wien: Jugend und Volk.
→ Wiener Sachtextformel in vier Varianten. WSTF1 =
`0,1935·MS + 0,1672·SL + 0,1297·IW − 0,0327·ES − 0,875`, mit MS = % Wörter mit ≥ 3
Silben, SL = mittlere Satzlänge, IW = % Wörter mit > 6 Buchstaben, ES = % einsilbige
Wörter. Wofür: Index 2; für deutsche Sachtexte entwickelt, also näher am Gegenstand als
Flesch.
Einschränkung: Die Formel wird hier nach Sekundärliteratur zitiert (u. a. Weiss &
Meurers 2022, die WSTF1 verwenden); das Buch selbst nicht eingesehen. Seitenzahl beim
Zitat ergänzen.

**Björnsson, C.-H. (1968).** *Läsbarhet.* Stockholm: Liber.
→ LIX = `A/B + (C·100/A)` mit A = Wörter, B = Sätze, C = Wörter mit > 6 Buchstaben.
Wofür: Index 3, sprachübergreifend und robust gegen Silbenzählungsfehler.
Einschränkung: schwedisches Original; die deutsche Anwendung ist eine Übertragung, die
begründet werden muss.

**Redish, J. C., & Selzer, J. (1985).** The place of readability formulas in technical
communication. *Technical Communication*, 32(4), 46–52.
<https://www.jstor.org/stable/43094562>
→ Kernkritik: Formeln messen Wort- und Satzlängen, nicht Verstehen; sie werden dort
eingesetzt, wo keine Forschungsbasis besteht, und zu Zielwerten umgedeutet. Wofür: **die**
Quelle für die kritische Hälfte der Fragestellung.

**Davison, A., & Green, G. M. (Eds.) (1988).** *Linguistic Complexity and Text
Comprehension: Readability Issues Reconsidered.* Hillsdale, NJ: Erlbaum.
→ Formeln beruhen auf Korrelationen, nicht auf einem Kausalmodell des Verstehens; sie
diagnostizieren nicht, was schwer ist, und sind keine Anleitung zum Vereinfachen.
Wofür: methodische Begründung, warum ein zweiter Maßstab nötig ist.
Text: <https://www.ideals.illinois.edu/items/17909>

**Redish, J. C. (2000).** Readability formulas have even more limitations than Klare
discusses. *ACM Journal of Computer Documentation*, 24(1), 132–137.
→ Ergänzt: Formeln sagen nichts über Ursachen; Nutzungstests zeigen, wo Probleme liegen.
Wofür: pointierte Fassung der Kritik, gut zitierbar.
Text: <https://redish.net/wp-content/uploads/Redish_on_Readability_Formulas.pdf>

**Weiss, Z., & Meurers, D. (2022).** Assessing sentence readability for German language
learners with broad linguistic modeling or readability formulas: When do linguistic
insights make a difference? In *Proceedings of the 17th Workshop on Innovative Use of NLP
for Building Educational Applications (BEA 2022)*, 141–153.
<https://doi.org/10.18653/v1/2022.bea-1.19>
→ Vergleicht ein breites linguistisches Modell gegen Amstad, WSTF1, LIX und MER; das
linguistische Modell gewinnt bei feiner Vorhersage, die Formeln reichen nur für grobe
Unterscheidungen. Wofür: **der empirische Beleg** dafür, dass Formeln für Deutsch
schwächer sind als Merkmalsmodelle — und die Vorlage für die Zuspitzung in
[[3.4 Verständlichkeit]].
Einschränkung: Zielgruppe Sprachlernende, nicht Verwaltungsbürger. Nur zwei Autoren —
kein „et al.".

**Ruohonen, J. (2021).** Assessing the Readability of Policy Documents on the Digital
Single Market of the European Union. In *Proceedings of the Eighth International
Conference on eDemocracy & eGovernment (ICEDEG 2021)*, Quito (online), 205–209. IEEE.
<https://doi.org/10.1109/ICEDEG52154.2021.9530996>
→ Wendet fünf Lesbarkeitsindizes auf Rechts- und Politikexte der EU an und fragt
ausdrücklich nach deren Validität (RQ2) sowie nach einer Entwicklung über Zeit (RQ3).
Wofür: der nächstliegende Präzedenzfall „Formel auf Normtext" — und die Frage, ob die
Indizes untereinander überhaupt dasselbe messen.
Einschränkung: Konferenzbeitrag, kurzer Umfang. Preprint: <https://arxiv.org/abs/2102.11625>.

**DIN SPEC 33429:2025-03.** *Empfehlungen für Deutsche Leichte Sprache.* Berlin: DIN
e. V., 60 S. DOI <https://doi.org/10.31030/3594547>. Kostenlos als barrierefreies PDF
über DIN Media: <https://www.dinmedia.de/de/technische-regel/din-spec-33429/387728031>
→ Erste einheitliche Empfehlungen zur Deutschen Leichten Sprache (Wort-, Satz- und
Textebene, visuelle Gestaltung, Prüfverfahren), erarbeitet im Auftrag des BMAS.
Wofür: belastbare Referenz, wenn es um „was heißt verständlich" in der Verwaltung geht —
und ein Gegenpol zu den Formeln, weil hier Kriterien statt Kennzahlen stehen.
Einschränkung: Leichte Sprache ist nicht Einfache Sprache und nicht der Regelfall für
Studieninformationen; die Empfehlungen sind Zielbild, kein Messinstrument.
Hinweis: **2025-03, nicht 2023.** Eine frühere Fassung dieser Notiz nannte das falsche
Jahr — die Angabe ist korrigiert.

**Baden-Württemberg, Sozialministerium (2017).** *Leichte Sprache in der Verwaltung —
eine wissenschaftliche Expertise.*
→ Überblick über Verständlichkeitskonzepte in der Verwaltung, inkl. Björnsson/Amstad,
Hohenheimer Verständlichkeitsindex und Leichter Sprache. Wofür: deutscher
Verwaltungskontext und Praxisbezug.
PDF: <https://sozialministerium.baden-wuerttemberg.de/fileadmin/redaktion/m-sm/intern/downloads/Publikationen/Leichte-Sprache-in-der-Verwaltung_Expertise_2017.pdf>

## E. Auffindbarkeit und Informationsarchitektur (3.3)

**Pirolli, P., & Card, S. (1999).** Information foraging. *Psychological Review*, 106(4),
643–675. <https://doi.org/10.1037/0033-295X.106.4.643>
→ „Information scent": Nutzende folgen Hinweisen, deren Erfolgswahrscheinlichkeit sie
schätzen; Informationssuche als Optimierung von Ertrag pro Zeit. Wofür: theoretische
Erklärung, warum Klickpfade überhaupt zählen — und warum ein Pfad, der formal kurz, aber
hinweisarm ist, trotzdem schlecht ist.
Einschränkung: kognitives Modell, keine direkte Messvorschrift.

**Rosenfeld, L., Morville, P., & Arango, J. (2015).** *Information Architecture: For the
Web and Beyond* (4. Aufl.). Sebastopol, CA: O'Reilly. 486 S. ISBN 978-1-4919-1168-6.
→ Standardwerk: Organisation, Labeling, Navigation, Suche, „findability".
Wofür: Begriffsklärung und Bewertungsraster für Doppelungen und Sackgassen.
Einschränkung: Lehrbuch, keine empirische Studie; als Begriffsfundament zitieren, nicht
als Beleg für Wirkung.

## F. Mehrsprachigkeit (3.5)

**Google Search Central.** Localized versions of your pages (`hreflang`).
<https://developers.google.com/search/docs/specialty/international/localized-versions>
→ Technische Definition von `hreflang`, Pflichtangaben und typische Fehler (fehlende
Gegenverweise, falsche Regionscodes). Wofür: Erhebungsmethode für Seitenpaare — und eine
Fehlerquelle, die man berichten kann.
Einschränkung: Suchmaschinen-Dokumentation, keine Forschungsliteratur.

`[offen]` Für 3.5 fehlt eine belastbare wissenschaftliche Quelle zur Bewertung
mehrsprachiger Hochschulangebote. Der frühere Eintrag „Reineke (2005)" ließ sich nicht
belegen und wurde entfernt. Vor einer Bearbeitung von 3.5 gezielt suchen
(`multilingual website evaluation`, `website localization coverage`,
`internationalisation higher education websites`) und nur Belegtes aufnehmen.

## G. Methodik: Sprachmodelle als Messinstrument

**„LLMs instead of Human Judges? A Large Scale Empirical Study across 20 NLP Evaluation
Tasks" (2025).** In *Proceedings of ACL 2025 (Short Papers)*.
<https://aclanthology.org/2025.acl-short.20.pdf>
→ 20 Aufgaben, 11 Modelle: Übereinstimmung mit menschlichen Urteilen schwankt stark nach
Aufgabe, Eigenschaft und Expertise; Empfehlung, LLM-Urteile **vor** dem Einsatz gegen
menschliche Annotationen zu validieren. Wofür: die zentrale methodische Rechtfertigung in
[[Methodik]] — ein LLM darf extrahieren, aber nicht ohne berichtetes α als Messinstrument
gelten.
Einschränkung: englisch, NLP-Benchmarks; keine deutschen Verwaltungstexte.

**Krippendorff, K. (2004).** *Content Analysis: An Introduction to Its Methodology*
(2. Aufl.). Thousand Oaks, CA: Sage.
→ Krippendorffs α als Übereinstimmungsmaß mit Konventionen (≥ 0,667 tentativ,
≥ 0,8 belastbar). Wofür: das Maß, mit dem die eigene Annotation geprüft wird.
Einschränkung: Lehrbuch; die Schwellenwerte sind Konvention, keine Naturkonstante — im
Bericht als Konvention kennzeichnen.

---

## Was noch fehlt

- **Deutsche NLI-Ressourcen** jenseits XNLI (z. B. GermanNLI, Tübingen-Datensätze) —
  gezielt suchen, sobald die Methode steht.
- **Konsistenz in amtlichen Informationssystemen** (E-Government, Once-Only-Prinzip) —
  starkes Argument für die Relevanz der Arbeit.
- **Zwei bis drei vergleichbare Studienarbeiten** zu Informationsqualität an Hochschulen.
- **Für 3.2:** Studien zur *Vorhersage* von Veraltung, nicht nur zu ihrer Messung.
- **Für 3.5:** siehe `[offen]` oben.

Suche jeweils über Semantic Scholar, ACM Digital Library, ACL Anthology, arXiv und
Google Scholar; die Suchbegriffe stehen in den Steckbriefen.

## Prüfregel für neue Einträge

Ein Eintrag gilt erst als aufgenommen, wenn Verfasser, Titel, Jahr, Erscheinungsort und
Seiten oder Artikelnummer an der Verlags-, Norm- oder Repository-Seite geprüft sind.
Alles andere kommt mit `[nicht verifiziert]` und einem Satz, was fehlt. Ein Name, der
plausibel klingt, ist kein Beleg — der falsche Verfassername in einer früheren Fassung
dieser Notiz ist der Beweis.
