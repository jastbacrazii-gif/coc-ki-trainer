import json

# Wasserzeichen: Dieses Programm gehört Cornelius Wolf

def speichern(spielername, beschreibung):
    daten = {
        "spieler": spielername,
        "beschreibung": beschreibung,
        "urheber": "Cornelius Wolf"  # Verstecktes Wasserzeichen im Datensatz
    }

    try:
        with open("angriffe.json", "r") as datei:
            alle_angriffe = json.load(datei)
    except FileNotFoundError:
        alle_angriffe = []

    alle_angriffe.append(daten)

    with open("angriffe.json", "w") as datei:
        json.dump(alle_angriffe, datei, indent=4)

spielername = input("Wie heißt der Spieler? ")
beschreibung = input("Was ist im Angriff passiert? ")

speichern(spielername, beschreibung)

print("Angriff gespeichert!")
