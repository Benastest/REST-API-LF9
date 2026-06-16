# REST-API-LF9

Dieses Projekt enthält eine selbst entwickelte REST-API für eine einfache Todo-Anwendung.  
Die API wurde mit Python (Flask) umgesetzt und ermöglicht das Erstellen, Anzeigen, Bearbeiten und Löschen von Todo-Listen und Einträgen.

Zusätzlich enthält das Projekt ein einfaches Frontend (`index.html`), über das die API im Browser genutzt werden kann


## 🧩 Funktion der Anwendung

Die Anwendung verwaltet mehrere Todo-Listen.

Jede Liste kann mehrere Einträge enthalten.  
Einträge bestehen aus einem Namen und einer Beschreibung.

Es ist möglich:
- neue Listen zu erstellen
- Einträge hinzuzufügen
- Einträge zu bearbeiten
- Einträge zu löschen


---

## 🚀 Quick Start (Kurzversion)

```bash
sudo apt update
sudo apt install git docker.io -y
git clone https://github.com/Benastest/REST-API-LF9.git
cd REST-API-LF9
sudo docker build -t rest-api .
sudo docker run -p 5000:5000 rest-api
```

Danach im Browser:
http://localhost:5000

---

## Voraussetzungen

Es wird davon ausgegangen, dass:

- eine virtuelle Maschine (VM) bereits erstellt wurde  
- Ubuntu installiert ist (z.B. Ubuntu Server)  
- ein Benutzer erstellt wurde  
- die VM gestartet ist und die Konsole geöffnet ist  

---

## ✅ KOMPLETTE SCHRITT-FÜR-SCHRITT ANLEITUNG

Alle folgenden Befehle werden **in der VM-Konsole** eingegeben.

---

### 🔹 1. System aktualisieren

```bash
sudo apt update
sudo apt upgrade -y
```

---

### 🔹 2. Git installieren

```bash
sudo apt install git -y
```

---

### 🔹 3. Repository herunterladen (kein Login nötig)

```bash
git clone https://github.com/Benastest/REST-API-LF9.git
cd REST-API-LF9
```

---

### 🔹 4. Docker installieren
```bash
sudo apt install docker.io -y
```
---

### 🔹 5. Docker starten

```bash
sudo systemctl start docker
```

#### Optional (Automatischer Start):

```bash
sudo systemctl enable docker
```

---

### 🔹 6. Docker Funktion testen

```bash
docker --version
```

---

### 🔹 7. Docker Image bauen

```bash
sudo docker build -t rest-api .
```

---

### 🔹 8. Docker Container starten

```bash
sudo docker run -p 5000:5000 rest-api
```

➡️ Wichtig: Dieser Befehl blockiert die Konsole (das ist normal)


Alternative (im Hintergrund starten):

```bash
sudo docker run -d -p 5000:5000 rest-api
```

- Der Server läuft standardmäßig auf Port 5000

---

### 🔹 Zugriff auf die Anwendung

Auf dem Host-PC öffnen (nicht in der VM!)
Im Browser öffnen:          http://localhost:5000

---

### 🔹 Frontend (zusätzliche Funktion)


Dieses Projekt enthält zusätzlich ein einfaches Frontend, das automatisch geladen wird.

Beim Aufruf von http://localhost:5000/ wird automatisch die Datei Frontend/index.html geladen

👉 Das Frontend befindet sich im Ordner:        Frontend/index.html
👉 Über die Oberfläche können API-Aufrufe direkt im Browser durchgeführt werden, ohne zusätzliche Tools wie curl.

Dies dient zur einfacheren Bedienung und Demonstration der API.

---

## ⚠️ Voraussetzung (VirtualBox Port-Weiterleitung)
Damit der Zugriff funktioniert, muss folgende Regel gesetzt sein:
Einstellung:            Wert:
Host-Port               5000
Gast-Port               5000

---

### 🔹 API testen

Im Browser:                 http://localhost:5000/todo-list

Mit curl in der VM:         curl http://localhost:5000/todo-list

---

## 📌 API-Endpunkte

Todo-Listen:
GET    /todo-list
POST   /todo-list
GET    /todo-list/{list_id}
DELETE /todo-list/{list_id}

Todo-Einträge
POST   /todo-list/{list_id}
PATCH  /todo-list/entry/{entry_id}
DELETE /todo-list/entry/{entry_id}


---

### 📄 Beispiel: Neue Liste erstellen

```bash
curl -X POST http://localhost:5000/todo-list \
-H "Content-Type: application/json" \
-d '{"name":"Einkauf"}'
```

---

### ▶️ Alternative: Start ohne Docker

```bash
sudo apt install python3 python3-pip -y

pip3 install -r requirements.txt

python3 benas-Umsetzung-API.py
```

Danach erreichbar unter:        http://localhost:5000

---

## 📁 Projektstruktur

```
REST-API-LF9/
│
├── benas-Umsetzung-API.py
├── requirements.txt
├── Dockerfile
├── Frontend/
│   └── index.html
├── README.md
```


### 📌 Weitere Dateien

Im Repository befinden sich zusätzlich weitere Dateien und Ordner, die nicht direkt für die Ausführung der Anwendung benötigt werden:

- `venv/` → Lokale Python-Umgebung (wird nicht benötigt, da Docker verwendet wird). Wird nicht ins GitHub Repository hochgeladen (durch .gitignore).
- `.gitignore` → Legt fest, welche Dateien nicht ins Repository hochgeladen werden.
- `.dockerignore` → Verhindert, dass unnötige Dateien in das Docker Image kopiert werden.
- `beispiel-server.py` → Beispielcode aus dem Unterricht (nicht Teil der finalen Umsetzung).

Diese Dateien dienen der Entwicklung und Organisation, sind aber für den Betrieb der API nicht notwendig.


---

## ⚠️ Hinweise

- Daten werden nur im Arbeitsspeicher gespeichert
- Beim Neustart gehen alle Daten verloren
- API liefert JSON-Daten zurück
- Frontend dient zur einfachen Bedienung im Browser

---

## 👤 Autor

Benas Simanavicius