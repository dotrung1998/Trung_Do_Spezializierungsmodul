---
titel: Board
stand: 2026-11-21
kanban-plugin: basic
---

# Board — Project JLU

> **Ziehen zwischen den Spalten** geht mit dem Community-Plugin **Kanban**
> (Einstellungen → Community-Plugins → Durchsuchen → „Kanban" → Installieren, dann diese
> Datei im Kanban-Modus öffnen). Ohne Plugin bleibt die Datei ein normales Protokoll.
>
> **Automatik:** `_tools/board_sync.py` läuft täglich um 08:00 über
> `_tools/daily.sh` (launchd `com.projectjlu.daily`). Das Skript liest die `\todo`-Stellen
> im Bericht und verschiebt Karten: offen → **To Do**, erledigt → **Done**. Karten ohne
> Berichts-ID (Mail, GitLab, Korpus) fasst es nicht an.
>
> Letzter Abgleich: 2026-11-21

## To Do

- [ ] **A.1 · Faktkatalog: zwölf Sachverhaltstypen festlegen** #person — Entscheidung mit Team Gamma, Grundlage für Kapitel 4.2 und Anhang A.1 · → [[Offene Entscheidungen]] · [[Methodik]]
- [ ] **A.3 · Modell, Prompt-Version und Umgebung festlegen** #person — Entscheidung, danach Anhang A.3 und der Lauf · → [[Offene Entscheidungen]] · [[LaTeX-Bericht]]
- [ ] **MAIL1 · Themenwünsche P1/P2 an die Betreuung senden** #person · fällig 2026-11-26 · → [[E-Mail 1 – Themenwünsche]]
- [ ] **GITLAB · Im JLU-GitLab anmelden und HRZ-Kennung melden** #person · → [[GitLab-Leitfaden (Quelle)]]
- [ ] **MAIL2 · Kurzexposé mit expose.pdf senden** #person — erst nach der Zuteilung am 27.11., 11:00 · → [[E-Mail 2 – Kurzexposé]]
- [ ] **KORPUS · Korpus einfrieren und Datenblatt v1 anlegen** #team — Stichtag, Hashes, Ausschlüsse; blockiert die sieben Messkarten · → [[Datenquellen]] · [[Methodik]]
- [ ] **GOLD · Goldstandard aufbauen und doppelt annotieren** #team — Voraussetzung für 6.2 und 7.2 · braucht: KORPUS · blockiert: KORPUS offen · → [[Methodik]]
- [ ] **6.1 · Abweichungsraten je Sachverhaltstyp** #ai — Tabelle mit Wilson-Intervall; entscheidet H1 · braucht: KORPUS · blockiert: KORPUS offen · → [[Methodik]] · [[LaTeX-Bericht]]
- [ ] **6.2 · Verfahrensvergleich** #ai — Precision, Recall, F1 je Variante, Recall-Differenz · braucht: GOLD · blockiert: GOLD offen · → [[Methodik]] · [[LaTeX-Bericht]]
- [ ] **6.3 · Fehleranalyse** #ai — Häufigkeit je Fehlerklasse aus A.4, je ein Beispiel · braucht: KORPUS · blockiert: KORPUS offen · → [[Methodik]] · [[LaTeX-Bericht]]
- [ ] **6.4 · Fall 2: Versionsartefakt** #ai — aus dem klassifizierten Fundbestand, nicht von Hand gewählt · braucht: KORPUS · blockiert: KORPUS offen · → [[Methodik]] · [[LaTeX-Bericht]]
- [ ] **7.2 · Urteil je Hypothese** #ai — bestätigt / teilweise / widerlegt, mit der Zahl aus Kapitel 6 · braucht: 6.1, 6.2 · blockiert: 6.1, 6.2 offen · → [[Hypothesen 3.1]] · [[LaTeX-Bericht]]
- [ ] **8 · Fazit: die eine Zahl** #ai — Abweichungsrate oder Anteil echter Widersprüche, mit Intervall · braucht: 7.2 · blockiert: 7.2 offen · → [[LaTeX-Bericht]]
- [ ] **ZUS · Zusammenfassung: Ergebnissatz** #ai — dieselbe Zahl in einem Satz · braucht: 8 · blockiert: 8 offen · → [[LaTeX-Bericht]]

## Doing

## Done

- [x] **LIT · 13 zitierte Quellen am Original geprüft** #ai — zwei Fehlzuschreibungen korrigiert · → [[Literatur]]
- [x] **TEXT · Berichtstext 29 von 38 Lücken geschlossen** #ai — Kapitel 1–8, A.2, A.4, A.5 · → [[LaTeX-Bericht]]
- [x] **URL · Umbruch nach „https:" behoben** #ai — Feldformat mit unteilbarer Box · → [[LaTeX-Bericht]]

%% kanban:settings
```
{"kanban-plugin":"basic"}
```
%%
