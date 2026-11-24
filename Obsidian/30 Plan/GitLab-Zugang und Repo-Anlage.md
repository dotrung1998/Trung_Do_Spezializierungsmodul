---
titel: GitLab-Zugang und Repo-Anlage
stand: 2026-11-23
---

# GitLab-Zugang und Repo-Anlage

Ablauf für den eigenen Arbeitsbereich im JLU-GitLab: VPN, Anmeldung, Projekt, Struktur,
Push. Regeln aus [[GitLab-Leitfaden (Quelle)]].

## Befund 23.11.2026 (auf dem eigenen Mac geprüft)

| Prüfung | Ergebnis |
|---|---|
| DNS `gitlab.ub.uni-giessen.de` | 134.176.5.21 (`fb06srv-u101831.sport.uni-giessen.de`); Google- und Cloudflare-DoH liefern dieselbe Adresse |
| TCP 443 von außen | Timeout nach 5 s, keine HTTP-Antwort |
| Gegenprobe `www.uni-giessen.de` | 302 in unter einer Sekunde, gleiches Netz |
| Cisco Secure Client | 5.1.17.1876 installiert, Socket-Filter-Extension `activated enabled`, **kein VPN-Profil** (`/opt/cisco/secureclient/profile` fehlt) |
| VPN-Antrag | HRZ: für Studierende nur im Bedarfsfall, Antrag einer Lehrperson an support@hrz.uni-giessen.de |

Also kein DNS- oder Browserfehler, sondern eine host-spezifische Sperre. Das deckt sich
mit dem Kick-off vom 20.11.2026 („GitLab derzeit nur über VPN erreichbar"). Die
GitLab-Doku behauptet, HTTPS sei aus dem ganzen Internet erreichbar; für die Planung
gilt der Befund. **Nicht geprüft:** ob es im Uninetz oder über VPN wirklich aufgeht —
das zeigt erst der erste Login.

## 1. VPN beantragen — blockiert alles Weitere

Studierende bekommen den VPN-Zugang nicht selbst, sondern nur, wenn eine Lehrperson ihn
beantragt. Die Betreuung hat im Kick-off zugesagt, das in der Woche ab 23.11.2026 zu
organisieren. Kommt keine Mail: kurze Nachricht an die Betreuung, Betreff
„VPN-Zugang für das JLU-GitLab".

```
Guten Tag Herr Busse,

für die Arbeit im JLU-GitLab brauche ich einen VPN-Zugang. Von meinem Anschluss
aus ist gitlab.ub.uni-giessen.de nicht erreichbar: Der Name löst auf, aber TCP 443
läuft in einen Timeout. www.uni-giessen.de ist im selben Netz erreichbar.

Könnten Sie den Zugang für mich bei support@hrz.uni-giessen.de beantragen?

Name: [Name]
Matrikelnummer: [Matrikelnummer]
HRZ-Kennung: [HRZ-Kennung]

Vielen Dank
[Name]
```

Vor Ort (Campus, eduroam) braucht es kein VPN; dort ist der Zugangstest schneller.

## 2. Client einrichten (macOS)

Bereits installiert: `/Applications/Cisco`, App-Version 5.1.17.1876 — neuer als die auf
der HRZ-Seite genannte 5.1.16.194, also nicht downgraden.

1. „Cisco Secure Client" öffnen.
2. Links „VPN" wählen.
3. Im Serverfeld „Add new VPN connection …" wählen; Adresse `vpn.uni-giessen.de`,
   Anzeigename `JLU`.
4. „Connect". Benutzer: HRZ-Kennung (g-/s-/n-/j-), Passwort: HRZ- bzw. Netzpasswort.
5. Prüfen: Schloss-Symbol in der Menüleiste, danach
   `curl -s -o /dev/null -w '%{http_code}' https://gitlab.ub.uni-giessen.de/`
   → 200 oder 302.

Download nur mit HRZ-Login:
<https://www.uni-giessen.de/de/fbz/svc/hrz/svc/netz/campus/vpn>

## 3. Anmelden

<https://gitlab.ub.uni-giessen.de> → Reiter „JLU (g-/s-/n-/j-)" → HRZ-Kennung und
Passwort → Nutzungsbedingungen akzeptieren. Die erste Anmeldung legt das Konto an;
danach die Kennung per Mail an die Betreuung, damit sie ins Gesamtrepo `project-jlu`
einlädt.

## 4. Projekt anlegen — Gruppe und Name

**Keine Gruppe.** Der Leitfaden sagt „im eigenen Namensraum". Im Dialog „Project URL"
also den eigenen Namen auswählen, nicht `project-jlu` und nicht `jlugitlab`. Eine Gruppe
braucht nur die gemeinsame Team-Ablage, und auch die ist laut Leitfaden ein Projekt
(`team-gamma`) im Namensraum einer Person.

Name nach Schema `team-nummer-kurzthema`: klein, Bindestriche, keine Umlaute.

| Arbeit | Repo-Name |
|---|---|
| 3.1 | `gamma-3-1-konsistenz` |
| 3.2 | `gamma-3-2-aktualitaet` |
| 3.3 | `gamma-3-3-auffindbarkeit` |
| 3.4 | `gamma-3-4-verstaendlichkeit` |
| 3.5 | `gamma-3-5-mehrsprachigkeit` |

Den Slug von Hand setzen: bei Umlauten wird er nicht zuverlässig automatisch erzeugt
(„verständlichkeit" wird sonst `verstandlichkeit`). Endgültig erst nach der Zuteilung am
27.11.2026, 11:00 — vorher ist der Name geraten.

Sichtbarkeit **privat**, „Initialize repository with a README" ankreuzen.

## 5. Betreuung einladen

Manage → Members → Invite members → „Sebastian Busse" suchen (oder die Adresse aus dem
Kick-off) → Rolle **Reporter** → Invite. Reporter liest und kommentiert, ändert nichts.

## 6. Mindeststruktur

```
README.md          Fragestellung als erster Absatz, Hypothesen, Aufruf des Codes, Stand
docs/              Projektplan, Wochenplan, datierte Entscheidungen
data/DATASHEET.md  Quellen, Abrufdatum, Umfang, Aufbau, bekannte Lücken
data/raw/          nicht im Repo (.gitignore)
data/processed/    kleine Ergebnisse im Repo
src/               Code
notebooks/         Exploration
tests/             Prüfungen des Codes
requirements.txt
.gitignore
```

`report/` ergänzen, weil der Bericht dort liegt. **Nicht** ins GitLab-Repo:
`report/private.tex` (Matrikelnummer), `report/main.pdf` und `report/expose.pdf` bis zur
Abgabe — dieselben Regeln wie in der `.gitignore` des GitHub-Repos. Das Abgabepdf kommt
erst zum Stichtag in den Abgabeordner.

## 7. Git über HTTPS, nicht SSH

SSH geht laut JLU-Doku nur über VPN; HTTPS mit Token funktioniert überall, wo das GitLab
erreichbar ist.

1. GitLab → Avatar → Edit profile → Access Tokens → Add new token: Name `macbook-git`,
   Ablauf 2027-04-01, Scope `write_repository` (enthält Lesen). Token einmal kopieren.
2. `git clone https://gitlab.ub.uni-giessen.de/[HRZ-Kennung]/gamma-3-1-konsistenz.git`
3. Beim ersten Push fragt git nach Benutzer (= HRZ-Kennung) und Passwort (= Token);
   macOS legt beides im Schlüsselbund ab.
4. Token nie in eine Datei, nie in den Vault, nie in ein Issue. Bei Verlust widerrufen
   und neu erzeugen.

## 8. Abgabe

Die Betreuung legt ein Abgaberepo an und gibt kurz vor dem 01.04.2027 Schreibrechte.
Dort einen Ordner mit **exakt dem Repo-Namen** anlegen und Bericht als PDF plus Code-
und Datenstand hineinlegen.

## Offene Punkte

- VPN-Antrag: gestellt? bestätigt?
- Zuteilung 27.11.2026: welcher Name gilt.
- Erster Login und erster Push: erst dann ist der Zugang belegt.

## Bezug

[[GitLab-Leitfaden (Quelle)]] · [[Prüfungsleistung ohne Vortrag]] · [[Status]] ·
[[Datenquellen]]
