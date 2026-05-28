# -*- coding: utf-8 -*-
"""
Todo-Listen-REST-API (Flask)
---------------------------------
Diese Datei implementiert die REST-Endpunkte exakt gemäß der vorgegebenen
Spezifikation der Berufsschule (IFA43):

  - GET    /todo-list/{list_id}                 -> Alle Einträge einer Liste
  - GET    /todo-list                           -> Alle Listen
  - POST   /todo-list                           -> Neue Liste anlegen
  - DELETE /todo-list/{list_id}                 -> Liste + Einträge löschen
  - POST   /todo-list/{list_id}                 -> Eintrag zu Liste hinzufügen
  - PATCH  /todo-list/entry/{entry_id}          -> Eintrag aktualisieren
  - DELETE /todo-list/entry/{entry_id}          -> Eintrag löschen

Statuscodes (pro Endpunkt wie in der Spezifikation beschrieben):
  200, 201, 204, 400, 404 (zusätzlich Handler für 405/500)

Starten:
  $ pip install flask
  $ python todo_api.py

Danach ist der Server auf http://127.0.0.1:5000 erreichbar.

Hinweis:
- Diese Implementierung verwendet eine In-Memory-Datenhaltung (Listen von Dicts)
  nur für Lern- und Demo-Zwecke. Beim Neustart gehen Daten verloren.
- Alle IDs sind vom Typ string (UUID4).
"""

from __future__ import annotations
import uuid
from typing import Dict, List, Optional
from flask import Flask, request, jsonify

# ---------------------------------------------------------------------------
# Flask-App initialisieren
# ---------------------------------------------------------------------------
app = Flask(__name__)

# ---------------------------------------------------------------------------
# Beispiel-Daten (In-Memory)
# ---------------------------------------------------------------------------
# Feste Beispiel-IDs für reproduzierbare Tests
TODO_LIST_1_ID = "1318d3d1-d979-47e1-a225-dab1751dbe75"
TODO_LIST_2_ID = "3062dc25-6b80-4315-bb1d-a7c86b014c65"
TODO_LIST_3_ID = "44b02e00-03bc-451d-8d01-0c67ea866fee"

# Beispiel-Listen
todo_lists: List[Dict] = [
    {"id": TODO_LIST_1_ID, "name": "Einkaufsliste"},
    {"id": TODO_LIST_2_ID, "name": "Arbeit"},
    {"id": TODO_LIST_3_ID, "name": "Privat"},
]

# Beispiel-Einträge (verwenden Feldname 'list_id' gemäß Spezifikation)
todos: List[Dict] = [
    {"id": str(uuid.uuid4()), "name": "Milch", "description": "", "list_id": TODO_LIST_1_ID},
    {"id": str(uuid.uuid4()), "name": "Arbeitsblätter ausdrucken", "description": "", "list_id": TODO_LIST_2_ID},
    {"id": str(uuid.uuid4()), "name": "Kinokarten kaufen", "description": "", "list_id": TODO_LIST_3_ID},
    {"id": str(uuid.uuid4()), "name": "Eier", "description": "Bio bitte", "list_id": TODO_LIST_1_ID},
]

# ---------------------------------------------------------------------------
# CORS (vereinfacht, damit Swagger/Browser-Tests funktionieren)
# ---------------------------------------------------------------------------
@app.after_request
def apply_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,DELETE,PATCH,OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

# ---------------------------------------------------------------------------
# Hilfsfunktionen
# ---------------------------------------------------------------------------

def find_list(list_id: str) -> Optional[Dict]:
    return next((l for l in todo_lists if l["id"] == list_id), None)


def find_entry(entry_id: str) -> Optional[Dict]:
    return next((e for e in todos if e["id"] == entry_id), None)


# ---------------------------------------------------------------------------
# Endpunkte gemäß Spezifikation
# ---------------------------------------------------------------------------

// Zum testen ob die API läuft, einfacher Endpunkt auf "/"
@app.route("/")
def home():
    return {"message": "API läuft!"}


@app.route("/todo-list", methods=["GET"])
def get_all_lists():
    """Liefert alle Todo-Listen zurück (200)."""
    return jsonify(todo_lists), 200


@app.route("/todo-list", methods=["POST"])
def create_list():
    """Fügt eine neue Todo-Liste hinzu.

    Request-Body: { "name": "..." }
    Responses:
      201 - Liste erstellt (gibt ganze Liste inkl. generierter id zurück)
      400 - Ungültiger Body
    """
    data = request.get_json(silent=True)
    if not data or not isinstance(data, dict) or not data.get("name"):
        return jsonify({"error": "Ungültiger Request-Body: Feld 'name' fehlt oder ist leer."}), 400

    new_list = {
        "id": str(uuid.uuid4()),
        "name": str(data["name"]).strip(),
    }
    todo_lists.append(new_list)
    return jsonify(new_list), 201


@app.route("/todo-list/<list_id>", methods=["GET"])
def get_entries_for_list(list_id: str):
    """Liefert alle Einträge einer Todo-Liste.

    Responses:
      200 - OK (Array von TodoEntry)
      404 - Ungültige Listen-ID
    """
    if not find_list(list_id):
        return jsonify({"error": "Liste nicht gefunden."}), 404

    entries = [e for e in todos if e["list_id"] == list_id]
    return jsonify(entries), 200


@app.route("/todo-list/<list_id>", methods=["DELETE"])
def delete_list(list_id: str):
    """Löscht eine komplette Todo-Liste mit allen Einträgen.

    Responses:
      204 - Erfolgreich gelöscht
      404 - Ungültige Listen-ID
    """
    lst = find_list(list_id)
    if not lst:
        return jsonify({"error": "Liste nicht gefunden."}), 404

    # Liste löschen
    todo_lists.remove(lst)

    # Zugehörige Einträge löschen
    global todos
    todos = [e for e in todos if e["list_id"] != list_id]

    return "", 204


@app.route("/todo-list/<list_id>", methods=["POST"])
def add_entry_to_list(list_id: str):
    """Fügt einen Eintrag zu einer bestehenden Todo-Liste hinzu.

    Request-Body: { "name": "...", "description": "..." }
    Responses:
      201 - Eintrag erstellt (gibt den Eintrag zurück)
      400 - Ungültiger Body
      404 - Ungültige Listen-ID
    """
    if not find_list(list_id):
        return jsonify({"error": "Liste nicht gefunden."}), 404

    data = request.get_json(silent=True)
    if not data or not isinstance(data, dict):
        return jsonify({"error": "Ungültiger Request-Body."}), 400

    name = str(data.get("name") or "").strip()
    description = str(data.get("description") or "").strip()

    if not name or "description" not in data:
        return jsonify({"error": "Felder 'name' und 'description' sind erforderlich."}), 400

    new_entry = {
        "id": str(uuid.uuid4()),
        "name": name,
        "description": description,
        "list_id": list_id,
    }
    todos.append(new_entry)
    return jsonify(new_entry), 201


@app.route("/todo-list/entry/<entry_id>", methods=["PATCH"])
def update_entry(entry_id: str):
    """Aktualisiert einen bestehenden Eintrag (teilweise).

    Request-Body: { "name"?: "...", "description"?: "..." }
    Responses:
      200 - Eintrag aktualisiert (gibt den Eintrag zurück)
      400 - Ungültiger Body
      404 - Ungültige Eintrags-ID
    """
    entry = find_entry(entry_id)
    if not entry:
        return jsonify({"error": "Eintrag nicht gefunden."}), 404

    data = request.get_json(silent=True)
    if not data or not isinstance(data, dict):
        return jsonify({"error": "Ungültiger Request-Body."}), 400

    updated = False
    if "name" in data:
        entry["name"] = str(data["name"]).strip()
        updated = True
    if "description" in data:
        entry["description"] = str(data["description"]).strip()
        updated = True

    if not updated:
        return jsonify({"error": "Keine gültigen Felder zum Aktualisieren übergeben."}), 400

    return jsonify(entry), 200


@app.route("/todo-list/entry/<entry_id>", methods=["DELETE"])
def delete_entry(entry_id: str):
    """Löscht einen einzelnen Eintrag einer Todo-Liste.

    Responses:
      204 - Erfolgreich gelöscht
      404 - Ungültige Eintrags-ID
    """
    entry = find_entry(entry_id)
    if not entry:
        return jsonify({"error": "Eintrag nicht gefunden."}), 404

    todos.remove(entry)
    return "", 204


# ---------------------------------------------------------------------------
# Fehler-Handler (allgemein)
# ---------------------------------------------------------------------------
@app.errorhandler(404)
def handle_404(e):
    return jsonify({"error": "Nicht gefunden."}), 404


@app.errorhandler(405)
def handle_405(e):
    return jsonify({"error": "Methode nicht erlaubt."}), 405


@app.errorhandler(500)
def handle_500(e):
    return jsonify({"error": "Interner Serverfehler."}), 500


# ---------------------------------------------------------------------------
# App-Start
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
