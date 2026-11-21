---
titel: "Leitfaden: Arbeiten mit GitLab in Project JLU"
quelle: "Project JLU/gitlab-leitfaden.md"
stand: 2026-11-20
hash: dd7216a0400b
automatisch: true
---

> Automatisch eingelesen aus `Project JLU/gitlab-leitfaden.md` am 2026-11-21.
> Diese Notiz nicht bearbeiten — inhaltliche Arbeit gehört in die
> handgeschriebenen Notizen, diese Datei wird beim nächsten Lauf überschrieben.

<!-- Quelle: Planungsmodul Project JLU WiSe 2026/27, Fassung v3, und Absprache vom 19.11.2026. Stand 19.11.2026. Entwurf zur Besprechung im Kick-off. -->

# Leitfaden: Arbeiten mit GitLab in Project JLU

Entwurf zur Besprechung im Kick-off am Fr 20.11.2026. Die Regeln werden dort gemeinsam festgelegt und gelten danach verbindlich.

Der sichere Umgang mit Git und GitLab ist Teil der Arbeit in Project JLU. Sie verwalten Ihr Repo selbst, so wie es in Softwareprojekten üblich ist.

## Wer was verwaltet

| Was                                                                                       | Wer verwaltet es | Wer hat Zugriff                                         |
|-------------------------------------------------------------------------------------------|------------------|---------------------------------------------------------|
| Gesamtrepo `project-jlu` mit Steckbriefen, Projekt-Karte und Protokollen der Gesamtgruppe | Betreuung        | alle Teilnehmenden, nur lesen                           |
| Ihr eigenes Repo für Ihre Einzelarbeit                                                    | Sie              | Sie und die Betreuung                                   |
| Abgaberepo                                                                                | Betreuung        | alle Teilnehmenden, Schreibrechte nur im Abgabezeitraum |
| Gemeinsame Ablage des Teams, etwa für Teamprotokolle                                      | das Team         | das Team und die Betreuung                              |

## Ihr Repo anlegen

1. Melden Sie sich unter <https://gitlab.ub.uni-giessen.de> an und legen Sie in Ihrem eigenen Namensraum ein neues, leeres Projekt an.
2. Benennen Sie es nach dem Schema Team, Nummer, Kurzthema, etwa `alpha-1-1-ordnungen-pdf` oder `gamma-3-4-verstaendlichkeit`.
3. Stellen Sie die Sichtbarkeit auf **privat**.
4. Laden Sie die Betreuung als Mitglied mit der Rolle **Reporter** ein. Damit kann die Betreuung lesen, Issues anlegen und kommentieren, aber nichts an Ihrem Code ändern.
5. Legen Sie die gemeinsame Mindeststruktur an (unten) und schreiben Sie in die `README.md` als Erstes Ihre Fragestellung.
6. Schicken Sie den Link zu Ihrem Repo per Mail an die Betreuung.

Für die gemeinsame Ablage des Teams legt eine Person ein Repo nach demselben Muster an, etwa `team-alpha`, und lädt das Team und die Betreuung ein.

## Gemeinsame Mindeststruktur

```
README.md          Fragestellung, Hypothesen, Aufruf des Codes, aktueller Stand
docs/              Projektplan, Wochenplan, datierte Entscheidungen
data/DATASHEET.md  Datenblatt: Quellen, Abrufdatum, Umfang, Aufbau, bekannte Lücken
data/raw/          Rohdaten, nicht im Repo (Eintrag in .gitignore)
data/processed/    aufbereitete Ergebnisse, im Repo, wenn sie klein sind
src/               Code
notebooks/         Exploration
tests/             Prüfungen des Codes
requirements.txt   verwendete Pakete mit Versionen
.gitignore         Rohdaten, .env, virtuelle Umgebungen, Caches
```

Innerhalb dieser Struktur gestalten Sie Ihr Repo so, wie es zu Ihrer Arbeit passt.

## Worauf Sie achten

- **Keine Zugangsdaten im Repo:** keine Passwörter, Tokens oder API-Schlüssel, auch nicht in alten Commits. Legen Sie sie in eine Datei `.env`, die in der `.gitignore` steht. Was einmal gepusht wurde, gilt als offengelegt und muss erneuert werden.
- **Keine personenbezogenen oder vertraulichen Daten im Repo.** Im Zweifel vorher die Betreuung fragen.
- **Große Dateien nicht ins Repo:** Je Projekt stehen in der Regel bis zu 1 GB zur Verfügung. Rohdaten bleiben außerhalb, das Datenblatt beschreibt, woher sie stammen und wie man sie erneut erzeugt. Für große Dateien, die ins Repo müssen, gibt es Git LFS.
- **Regelmäßig committen und pushen** ist empfohlen. So bleiben Ihre Änderungen nachvollziehbar und liegen nicht nur auf Ihrem Rechner. Eine gute Commit-Nachricht sagt kurz, was sich geändert hat.
- **Nachvollziehbar arbeiten:** Entscheidungen mit Datum in `docs/` festhalten, offene Aufgaben als Issues anlegen.
- **Vereinbarung zur Weiterverwendung:** Sie erhalten noch ein Formular, das Sie unterschreiben. Darin verpflichten Sie sich, Ihren Code unter einer Creative-Commons-Lizenz mit Namensnennung zu veröffentlichen, damit er weiterverwendet werden kann, auch an der JLU. Welche Lizenz genau, wird noch festgelegt. Außerdem stimmen Sie der maschinellen Verarbeitung Ihrer Abgabe zu. Bis zur Veröffentlichung bleibt Ihr Repo privat.

## Protokolle

- Treffen der Gesamtgruppe protokolliert die Betreuung im Gesamtrepo unter `protokolle/`.
- Treffen eines Teams ohne die Betreuung protokolliert das Team selbst in seiner gemeinsamen Ablage.
- Ein Ergebnisprotokoll hält fest, was entschieden wurde, wer was bis wann erledigt und welche Fragen offen sind. Dateiname: Datum und Anlass, etwa `2026-12-03_teamtreffen.md`.

## Abgabe

1. Für die Abgabe legt die Betreuung ein eigenes Abgaberepo an. Kurz vor dem Stichtag erhalten Sie dort Schreibrechte.
2. Legen Sie im Abgaberepo einen Ordner mit dem Namen Ihres Repos an, etwa `alpha-1-1-ordnungen-pdf/`, und legen Sie dort alles ab, was zur Abgabe gehört: den Bericht als PDF und den Stand von Code und Daten, mit dem die Ergebnisse entstanden sind.
3. Mit dem Stichtag [Datum folgt] enden die Schreibrechte. Abgegeben ist, was bis dahin im Abgaberepo liegt.
4. Im Abgaberepo sind die Abgaben aller Teilnehmenden für alle sichtbar.

## Zum Einstieg

- Dokumentation von GitLab: <https://docs.gitlab.com>
- Hinweise zum Einstieg in Git folgen.
- Fragen zu Git und GitLab gehören in ein Issue im Gesamtrepo, damit alle von den Antworten profitieren.
