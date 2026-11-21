---
titel: Methodik
stand: 2026-11-21
---

# Methodik — messen statt behaupten

Gilt für 3.1 vollständig, für 3.2 in den Teilen Korpus, Label, Metriken und
Reproduzierbarkeit. Das ist das Rückgrat des Berichts und der Grund, warum die Arbeit
in einem Data-Analytics-Modul besteht.

## Grundprinzip

Jede Aussage im Bericht hat vier Bestandteile: **Bezugsgröße, Stichprobe, Messgröße,
Unsicherheit.** „Viele Fristen weichen ab" ist keine Aussage. „Von 34 Frist-Angaben in
7 Dokumenten weichen 9 ab (26 %, 95 %-KI [14 %, 43 %])" ist eine.

## 1. Analyseeinheit: der Sachverhalt

Ein Sachverhalt ist ein Tupel:

```
Fakt = (entität, attribut, wert, gültigkeitsintervall, quelle, fundstelle)
```

Beispiel:

| Feld | Wert |
|---|---|
| entität | M.Sc. Data Analytics |
| attribut | Bewerbungsfrist_WiSe |
| wert | 2027-01-15 |
| gültigkeitsintervall | 2026-06-01 … 2027-01-15 |
| quelle | webseite_studiengang (doc_id 17) |
| fundstelle | „Bewerbungsschluss ist der 15. Januar" (Zeichen 1840–1885) |

Diese Form ist die wichtigste Entscheidung der ganzen Arbeit. Sie erzwingt, dass
„derselbe Sachverhalt" definiert ist, statt im Gespräch zu verschwimmen. Alles Weitere
folgt daraus.

## 2. Korpus

- **Ein Stichtag.** Ein Abrufdatum, ein Hash je Datei, ein Datenblatt.
- **Vollständigkeit dokumentieren**, nicht behaupten: Anzahl Dokumente, Anzahl Seiten,
  Abrufdatum, Ausschlüsse (z. B. „Seiten hinter Login nicht erfasst").
- **Fassungen.** Wo möglich frühere Fassungen (Ordnungen: 1./2./3. Änderung; Webseiten:
  Wayback). Ohne Fassungen kann man Versionsartefakte nicht von Widersprüchen trennen.
- **Boilerplate entfernen.** Navigation, Footer, Cookie-Hinweise, Breadcrumbs. Sonst
  extrahiert das Modell Menüs als Inhalt — der häufigste stille Fehler.

## 3. Extraktion mit Zitatpflicht

Sprachmodell mit festem Schema (JSON, per Pydantic validiert). Jeder Wert **muss** eine
Fundstelle mitliefern: `doc_id`, Zeichen-Offset, Zitattext. Werte ohne Fundstelle werden
verworfen — nicht geschätzt.

Warum: Ein LLM liefert plausible Werte auch dort, wo keine stehen. Die Zitatpflicht macht
Halluzination billig prüfbar: ein Blick auf das Zitat, fertig. Das ist der Unterschied
zwischen einem Datensatz und einem Datenhaufen.

Zusätzlich: **Temperatur 0**, feste Prompt-Version im Repo, ein Lauf je Korpusversion.
Prompt-Änderungen sind Experimente und werden als solche dokumentiert.

## 4. Normalisierung

Ohne Normalisierung entstehen falsche Widersprüche:

| Problem | Beispiel | Regel |
|---|---|---|
| Datumsformate | 15.01.2027 / 2027-01-15 / „15. Januar" | → ISO 8601 |
| Zahlen | „6 LP" / „sechs Leistungspunkten" | → Dezimal |
| Entitätsnamen | „Data Analytics" / „M.Sc. Data Analytics" / „DA" | Aliasliste, manuell gepflegt |
| Scope | „EU-Bewerbende" vs. alle | eigenes Feld, **nie** weglassen |
| Einheiten | „90 Min." / „1,5 h" | → Minuten |

Die Aliasliste ist Handarbeit und gehört ins Repo (`data/aliases.csv`). Sie ist ein
Ergebnis, kein Hilfsmittel: Sie zeigt, wie viele Schreibweisen derselbe Studiengang hat.

## 5. Goldstandard

- **Stratifizierte Stichprobe** über Sachverhaltstypen, nicht zufällig über alle Zeilen.
  Sonst besteht der Goldstandard zu 90 % aus Modulnummern und misst nichts.
- **Zwei unabhängige Durchgänge**, dann Auflösung von Konflikten. Wenn keine zweite
  Person verfügbar ist: ein Durchgang menschlich, ein Durchgang mit einem **anderen**
  Modell, Konflikte manuell entschieden — und das offen als Einschränkung benannt.
- **Berichtet wird Krippendorffs α.** Konvention: ≥ 0,667 tentativ, ≥ 0,8 belastbar.
  α < 0,667 heißt: Das Label ist zu unscharf, nicht: die Coder waren schlecht.
- **LLM-Validierung.** Übereinstimmung LLM ↔ Mensch auf dem Goldstandard berichten.
  Erst dann darf das LLM auf den vollen Korpus losgelassen werden. Beleg:
  [[Literatur]] → Judge-Bench (2025).

## 6. Metriken

| Metrik | Formel / Definition | Warum |
|---|---|---|
| Precision | richtig erkannte Abweichungen / alle erkannten | Wie viele Meldungen sind brauchbar? |
| Recall | richtig erkannte / alle im Goldstandard | Wie viel wird übersehen? |
| F1 | harmonisches Mittel | Ein Zahl für den Vergleich von Varianten |
| Abweichungsrate je Typ | Abweichungen / Sachverhalte des Typs | Der inhaltliche Befund |
| Wilson-KI | 95 %-Intervall des Anteils | Ehrlichkeit bei kleinem n |
| α (Krippendorff) | Inter-Coder-Reliabilität | Ist das Label überhaupt messbar? |
| AUC + Kalibrierung | nur 3.2 | Taugt das Vorhersagemodell? |

**Immer je Typ berichten.** Ein globaler F1 von 0,8 kann aus 0,95 bei Modulnummern und
0,45 bei Ansprechpartnern bestehen — und dann ist die Aussage „das Verfahren funktioniert"
falsch.

## 7. Fehleranalyse

Nicht optional. 20–30 Fehlfälle manuell durchsehen und kategorisieren:

- Extraktion (Wert falsch gelesen)
- Normalisierung (richtig gelesen, falsch vereinheitlicht)
- Gruppierung (verschiedene Sachverhalte zusammengeworfen)
- Scope (Zielgruppe übersehen)
- Urteil (Modell hat Widerspruch gesehen, wo keiner ist)

Diese Tabelle ist oft der beste Abschnitt einer Arbeit: Sie zeigt, dass man das eigene
Verfahren versteht.

## 8. Reproduzierbarkeit

- `requirements.txt` mit festen Versionen, `make reproduce` als ein Befehl.
- Korpus-Hashes im Datenblatt, Prompt-Version im Repo, Seeds gesetzt.
- Keine Rohdaten im Repo, aber ein Skript, das sie erneut beschafft.
- Ein frischer Lauf erzeugt dieselben Zahlen (oder dokumentiert, warum nicht).

## 9. Was im Bericht stehen muss, auch wenn es unangenehm ist

- Stichprobengröße je Befund.
- Was **nicht** erfasst wurde (Seiten hinter Login, PDFs ohne Textebene, englische Fassungen).
- Dass die Auswahl der Sachverhalte die Ergebnisse prägt — ein anderer Faktkatalog hätte
  andere Zahlen ergeben.
- Dass ein LLM als Messinstrument ein Validierungsproblem ist, kein Werkzeugproblem.

## Bezug

[[3.1 Konsistenz]] · [[3.2 Aktualität]] · [[Hypothesen 3.1]] · [[Literatur]]

## Datenmodell und Fehlertaxonomie (21.11.2026)

Beide Artefakte stehen jetzt ausformuliert im Bericht und sind hier festgehalten, damit sie
nicht neu erfunden werden:

**Extraktionsschema (Bericht A.2).** 16 Felder in drei Ebenen: Dokument (`doc_id`,
`doc_hash`), Fakt (`entitaet`, `attribut`, `wert_raw`, `wert_norm`, `einheit`, `scope`,
`gueltig_von`, `gueltig_bis`), Fundstelle (`fundstelle_text`, `fundstelle_start`,
`fundstelle_ende`) plus Laufmetadaten (`status`, `prompt_version`, `modell`). Pflicht sind
alle außer `wert_norm`, `einheit` und den beiden Gültigkeitsdaten: Die Normalisierung darf
scheitern, ohne den Fakt zu verlieren; ein Fakt ohne Fundstelle wird dagegen nicht
geschrieben. `doc_hash` trennt Fassungen — ein zweiter Abruf ist eine neue Dokumentversion,
keine Korrektur.

**Fehlertaxonomie (Bericht A.4).** Fünf Klassen, jeweils mit Folge für die Kennzahl:
Extraktion (falscher Wert → Precision/Recall), erfundene Angabe (Precision),
Normalisierung (falsch vereinheitlicht → Precision), Gruppierung (beides), Scope
(Precision), Urteil (Precision bzw. Recall). Jeder Fall bekommt **eine** Hauptursache;
Nebenursachen nur im Protokoll. Die Klassen werden vor der Auswertung festgelegt, sonst
passt man sie dem Ergebnis an.

**Abgrenzung.** Die Abweichungstypologie (5.4) sagt, was ein Fund bedeutet; die
Fehlertaxonomie sagt, wodurch das Verfahren danebenliegt. Ein Extraktionsfehler ist in
beiden Systemen vorhanden, aber mit anderer Funktion: Ausschlussgrund dort, Kennzahl hier.

**Offen.** Häufigkeiten je Fehlerklasse und alle Abweichungsraten sind Messzahlen; sie
stehen in Kapitel 6, sobald der Lauf existiert.
