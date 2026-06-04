from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from TTS.api import TTS

import os
import uuid

app = FastAPI()

# Static folders
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/output", StaticFiles(directory="output"), name="output")

# Create output directory
os.makedirs("uploads", exist_ok=True)
os.makedirs("output", exist_ok=True)

print("Loading XTTS v2 model...")

tts = TTS(
    model_name="tts_models/multilingual/multi-dataset/xtts_v2"
)

print("XTTS model loaded successfully!")

@app.get("/", response_class=HTMLResponse)
def home():

    with open("templates/index.html", "r", encoding="utf-8") as file:
        return HTMLResponse(content=file.read())

@app.post("/generate")
async def generate_audio(request: Request):

    form = await request.form()

    text = form.get("text")

    # fallback to English if language missing
    lang = form.get("lang") or "en"

    filename = f"{uuid.uuid4()}.wav"

    filepath = f"output/{filename}"

    print("TEXT =", text)
    print("LANG =", lang)
    
    voice_mode = form.get("voice_mode")

    if voice_mode == "clone":

        voice_file = form.get("voice")

        voice_filename = f"{uuid.uuid4()}.wav"

        voice_path = f"uploads/{voice_filename}"

        with open(voice_path, "wb") as buffer:
            buffer.write(await voice_file.read())

    if voice_mode == "clone":

        tts.tts_to_file(
            text=text,
            speaker_wav=voice_path,
            language=lang,
            file_path=filepath
        )

    else:

        tts.tts_to_file(
            text=text,
            speaker="Ana Florence",
            language=lang,
            file_path=filepath
        )

    return {
        "audio_url": f"/output/{filename}"
    }