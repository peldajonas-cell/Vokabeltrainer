# Wortkasten

Englisch-Vokabeltrainer fürs iPad. Gelernt wird in 9 Lernmodi. Jeder Modus hat seine eigene Lernkartei mit 5 Fächern. Lernstand und Statistik liegen nur auf dem Gerät, auf dem gelernt wird. Es gibt keine Konten und es werden keine persönlichen Daten übertragen.

**Adresse der App:** https://peldajonas-cell.github.io/vokabeltrainer-Paula/

---

## Einmalig einrichten

### 1. Website einschalten (GitHub, ca. 2 Minuten)
1. In Safari github.com öffnen und das Repository **vokabeltrainer-Paula** aufrufen.
2. **Settings** öffnen. Auf dem iPad ggf. über „…“ oder nach rechts wischen.
3. Links **Pages** wählen.
4. Unter „Build and deployment“ bei **Source** „Deploy from a branch“ einstellen und bei **Branch** `main` und `/ (root)` wählen, dann **Save**.
5. 1–3 Minuten warten. Oben auf der Pages-Seite erscheint dann „Your site is live at …“.

### 2. App aufs Kinder-iPad
1. In **Safari** (nicht Chrome) die Adresse oben öffnen.
2. Auf **Teilen** tippen (Quadrat mit Pfeil), dann **„Zum Home-Bildschirm“**, dann **Hinzufügen**.
3. Ab jetzt die App **nur über dieses Icon** öffnen. Wichtig: Nur dort bleibt der Lernstand dauerhaft gespeichert. Safari selbst löscht Website-Daten nach einiger Zeit ohne Nutzung.

### 3. Eltern-PIN festlegen
In der App oben rechts auf **Eltern** tippen und eine 4-stellige PIN festlegen. Am besten eine andere als die Gerätesperre.

### 4. Claude schützen (wenn das Kind dein iPad nutzt)
- Lange auf das Claude-Icon tippen, dann **„Face ID erforderlich“**. Claude ist erst ab 18 erlaubt.
- Optional: Mit **Einstellungen → Bedienungshilfen → Geführter Zugriff** bleibt das iPad während des Lernens in der App.

---

## Im Alltag

### Neue Vokabeln
1. Das Kind tippt in der App auf **„Vokabeln fotografieren“**, nimmt Fotos oder Screenshots auf und schickt sie per **„An Eltern senden“** über Nachrichten.
2. Du gibst die Fotos im Claude-Chat „Vokabeltrainer“ weiter.
3. Claude erkennt die Vokabeln, schreibt Beispielsätze und legt die Lektion hier ins Repository.
4. Beim nächsten Öffnen erscheint sie beim Kind automatisch („Neu dazugekommen“).

### Fortschritt ansehen
Am Kinder-iPad: **Eltern → PIN → Überblick**
- Lernzeit, Lerntage, Trefferquote
- Stand pro Lernmodus (Fächer 1–5)
- Problemwörter und vom Kind ergänzte Wörter
- Unter **Vokabeln** pro Wort eine Ampelzeile für alle Modi

### Sicherung
**Eltern → Einstellungen → Sicherungscode kopieren**, z. B. ab und zu in eine Notiz einfügen. Damit lässt sich der Lernstand auch auf einem neuen Gerät wiederherstellen.

---

## So lernt die App

| Modus | Richtung |
|---|---|
| Karteikarte | Englisch → Deutsch |
| Multiple Choice | Englisch → Deutsch |
| Paare zuordnen | Englisch ↔ Deutsch |
| Satz verstehen | Englisch → Deutsch |
| Eintippen | Deutsch → Englisch |
| Hören & Schreiben | Hören → Englisch |
| Lückensatz | Deutsch → Englisch |
| Satzbau | Deutsch → Englisch |
| Formen eintippen | Grundform → Simple Past, Past Participle (nur unregelmäßige Verben) |

- **Eine Kartei pro Modus:** Eine richtige Antwort bringt das Wort in diesem Modus ein Fach weiter. Es kommt nach 1, 2, 4, 7 bzw. 14 Tagen wieder dran. Eine falsche Antwort setzt nur diesen Modus zurück auf Fach 1.
- **Neue Wörter** starten mit Karteikarte, Multiple Choice und Paaren. Die Schreib- und Satzmodi kommen dazu, sobald das Wort in einem davon Fach 2 erreicht hat.
- **„Sicher“** ist ein Wort erst, wenn es in allen möglichen Modi mindestens Fach 4 hat.
- **„Gezielt üben“** verschiebt keine Fächer.

---

## Technik (für Claude / Updates)

```
src/app.html            Quelle der App (auch die Claude-Vorschau)
index.html              Website-Version, erzeugt mit: python3 tools/build_index.py
lektionen/*.txt         Vokabellisten, eine Zeile pro Vokabel:
                        # Lektion: Name
                        Englisch ; Deutsch ; Satz Englisch ; Satz Deutsch ; Formen (go - went - gone)
lektionen.json          erzeugt mit: python3 tools/build_lessons.py
icon.png                Icon für den Home-Bildschirm
```

- Mehrere richtige englische Antworten werden mit `/` getrennt.
- Die IDs der Vokabeln entstehen aus Lektionsname und englischem Wort. Bleiben beide gleich, bleibt auch der Lernstand erhalten. Lektionen deshalb nach dem Veröffentlichen nicht mehr umbenennen.
- Was im Eltern-Bereich gelöscht oder bearbeitet wurde, überschreibt die Website nicht.
