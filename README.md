# REST-API-LF9

Dieses Projekt enthält eine selbst entwickelte REST-API für eine einfache Todo-Liste. Die API wurde mit Flask in Python implementiert und ermöglicht grundlegende CRUD-Operationen (Create, Read, Update, Delete).

`beispiel-server.py` ist nur eine beispielhafte Umsetzung die wir von unserer lehrkraft bekommen haben um eine Orientierung zu bekommen.

---

## Technologien

- Python
- Flask
- Docker
- VirtualBox (Ubunto Linux)

---

## Umgebung (Virtual Machine)

Die Anwendung wurde in einer Ubuntu VM innerhalb von VirtualBox betrieben.
Der zugriff erfolgt über Port-Weiterleitung von der VM zum Hostsystem.

Beispiel:
- VM Port: 5000
- Host Port: 5000

Aufruf im Browser:
http://localhost:5000

---

## Installation

git clone https://github.com/Benastest/REST-API-LF9
cd REST-API-LF9

Virtuelle Umgebung erstellen

python3 -m venv .venv
source .venv/bin/activate

Abhängigkeiten installieren:

pip install -r requirements.txt

---


## Starten (ohne Docker)

python3 benas-Umsetzung-API.py

Die API ist anschließend erreichbar unter:
http://127.0.0.1:5000

---

## Starten (mit Docker)

Docker Image erstellen:

docker build -t benas-rest-api .

Container starten:
docker run -p 5000:5000 benas-rest-api

Die API ist erreichbar unter:
http://locakhost:5000

---

## API-Endpunkte

Die Anwendung stellt eine REST-API bereit und gibt Daten im JSON-Format zurück. Es gibt keine grafische Benutzeroberfläche.

### Beispiel-Endpunkte

GET /
=> Prüft, ob die API läuft

GET /items
=> Alle Einträge anzeigen

POST /items
=> Neuen Eintrag erstellen

PUT /items/<id>
=> Eintrag aktualisieren

DELETE /items/<id>
=> Eintrag löschen

---

## API testen

Im Browser:
http://localhost:5000/items

Mit curl:
curl http://localhost:5000/items

---

## Projektstruktur

REST-API-LF9/
|- benas-Umsetzung-API.py       # Hauptimplementierung der API
|- beispiel-server.py           # Vorlage von der Lehrkraft
|- requirements.txt             # Python-Abhängigkeiten
|- README.md                    # Dokumentation

---


## Hinweise

- DIE API ist eine reine Backend-Anwendung ohne Benutzeroberfläche
- Daten werden im JSON-Format verarbeitet
- Die Anwednug wurde in einer Virtual Machine (Ubuntu) betrieben
- Zugriff erfolgt über VirtualBox Port-Forwarding
- Docker wird optional zur Containerisierung verwendet
- Der Ordner `.venv` oder `venv` ist nicht Teil des Repositories (.gitignore)
- `requirements.txt` enthält die benötigten Python-Abhängigkeiten.
- `.gitignore` sorgt dafür, dass lokale virtuelle Umgebungen und temporäre Dateien nicht im Repository landen.

---

# Autor

Benas Simanavicius