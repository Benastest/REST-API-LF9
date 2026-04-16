# REST-API-LF9

Dieses Projekt enthält zwei Beispiel-Implementierungen einer einfachen Todo-Listen-REST-API mit Flask.

## Installieren

1. Python 3 verwenden.
2. Optional ein virtuelles Umfeld erstellen:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Die benötigten Bibliotheken installieren:

```bash
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

## Starten

- Für die Datei `beispiel-server.py`:

```bash
python3 beispiel-server.py
```

- Für die Datei `benas-Umsetzung-API.py`:

```bash
python3 benas-Umsetzung-API.py
```

Der Server läuft dann unter `http://127.0.0.1:5000`.

## Hinweise

- `requirements.txt` enthält die benötigten Python-Abhängigkeiten.
- `.gitignore` sorgt dafür, dass lokale virtuelle Umgebungen und temporäre Dateien nicht im Repository landen.
