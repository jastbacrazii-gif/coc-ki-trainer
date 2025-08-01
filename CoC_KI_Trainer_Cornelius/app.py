import streamlit as st
import json
import os

# Wasserzeichen als Kommentar:
# Dieses Programm gehört Cornelius Wolf

st.title("CoC KI Trainer - Video Upload")

# Upload-Funktion für Videos
uploaded_video = st.file_uploader("Lade dein Angriffs-Video hoch", type=["mp4", "mov", "avi"])

if uploaded_video is not None:
    # Speicherpfad
    if not os.path.exists("videos"):
        os.makedirs("videos")

    video_path = os.path.join("videos", uploaded_video.name)

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


