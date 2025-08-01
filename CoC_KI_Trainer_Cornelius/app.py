import streamlit as st
import json
import os

# Wasserzeichen als Kommentar:
# Dieses Programm gehört Cornelius Wolf

st.title("CoC KI Trainer - Video Upload")

# Ordner für Video-Uploads
UPLOAD_DIR = "videos"  # Du hattest 'videos' verwendet - behalten wir so

# Stelle sicher, dass der Ordner existiert
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# Upload-Funktion für Videos
uploaded_video = st.file_uploader("Lade dein Angriffs-Video hoch", type=["mp4", "mov", "avi"])

if uploaded_video is not None:
    video_path = os.path.join(UPLOAD_DIR, uploaded_video.name)

    # Speichern des Videos
    with open(video_path, "wb") as f:
        f.write(uploaded_video.getbuffer())
    st.success(f"Video '{uploaded_video.name}' wurde gespeichert!")

# Beispiel: Angriffe aus JSON laden und anzeigen
def lade_angriffe():
    try:
        with open("angriffe.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

angriffe = lade_angriffe()

st.header("Bisher gespeicherte Angriffe")

for a in angriffe:
    st.write(f"Spieler: {a['spieler']}, Beschreibung: {a['beschreibung']}")



