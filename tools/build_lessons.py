#!/usr/bin/env python3
"""Baut lektionen.json aus allen Textdateien in lektionen/.

Format der Textdateien:
  # Lektion: <Name>
  Englisch ; Deutsch ; Satz Englisch ; Satz Deutsch
Mehrere richtige englische Antworten mit "/" trennen.
Die IDs bleiben stabil, solange Lektionsname und englisches Wort gleich bleiben.
Damit bleibt der Lernstand auf den Geräten erhalten.
"""
import json, re, sys, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def slug(s):
    s = s.lower().replace("–", "-").replace("—", "-").replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")

def parse(path):
    lessons, cur = [], None
    for n, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line:
            continue
        m = re.match(r"^#+\s*(?:Lektion\s*:)?\s*(.+)$", line, re.I)
        if m:
            cur = {"name": m.group(1).strip(), "words": []}
            lessons.append(cur)
            continue
        parts = [p.strip() for p in (line.split("\t") if "\t" in line else line.split(";"))]
        if len(parts) < 2 or not parts[0] or not parts[1]:
            sys.exit(f"{path.name}:{n}: Zeile braucht mindestens 'Englisch ; Deutsch'")
        if cur is None:
            sys.exit(f"{path.name}:{n}: Vokabel vor der ersten '# Lektion:'-Zeile")
        w = {"en": parts[0], "de": parts[1], "sEn": parts[2] if len(parts) > 2 else "", "sDe": parts[3] if len(parts) > 3 else ""}
        if len(parts) > 4 and parts[4]:
            w["forms"] = [f.strip() for f in parts[4].split("-") if f.strip()]
        cur["words"].append(w)
    return lessons

def main():
    out = []
    for path in sorted((ROOT / "lektionen").glob("*.txt")):
        for les in parse(path):
            lid = slug(les["name"])
            seen = set()
            for w in les["words"]:
                base = f"{lid}--{slug(w['en'].split('/')[0])}"
                wid, k = base, 2
                while wid in seen:
                    wid, k = f"{base}-{k}", k + 1
                seen.add(wid)
                w["id"] = wid
            out.append({"id": lid, "name": les["name"], "words": [dict(id=w.pop("id"), **w) for w in les["words"]]})
    (ROOT / "lektionen.json").write_text(json.dumps({"version": 1, "lessons": out}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{len(out)} Lektionen, {sum(len(l['words']) for l in out)} Vokabeln")

if __name__ == "__main__":
    main()
