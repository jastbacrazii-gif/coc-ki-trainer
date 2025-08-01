import streamlit as st
import os

# Wasserzeichen als Kommentar:
# Dieses Programm gehört Cornelius Wolf

st.title("CoC KI Trainer - Video Upload und Download")

# Upload-Funktion für Videos
uploaded_video = st.file_uploader("Lade dein Angriffs-Video hoch", type=["mp4", "mov", "avi"])

if uploaded_video is not None:
    # Speicherpfad
    if not os.path.exists("videos"):
        os.makedirs("videos")

    video_path = os.path.join("videos", uploaded_video.name)

    # Speichern des Videos auf dem Server (temporär)
    with open(video_path, "wb") as f:
        f.write(uploaded_video.getbuffer())

    st.success(f"Video '{uploaded_video.name}' wurde gespeichert!")

    # Video in der App abspielen
    st.video(video_path)

    # Download-Button anzeigen, um Video auf deinen PC zu laden
    with open(video_path, "rb") as f:
        video_bytes = f.read()

    st.download_button(
        label="Video herunterladen",
        data=video_bytes,
        file_name=uploaded_video.name,
        mime="video/mp4"
    )

