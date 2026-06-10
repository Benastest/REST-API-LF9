# Python Basis-Image
FROM python:3.11

# Arbeitsordner im Container
WORKDIR /app

# Requirements kopieren
COPY requirements.txt .

# Abhängigkeiten installieren
RUN pip install --no-cache-dir -r requirements.txt

# Restlichen Code kopieren
COPY . .

# Port veröffentlichen
EXPOSE 5000

# Startbefehl für deine API
CMD ["python", "benas-Umsetzung-API.py"]