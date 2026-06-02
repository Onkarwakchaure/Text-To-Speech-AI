from TTS.api import TTS

print("Loading XTTS v2 model...")

tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2")

print("Generating AI speech...")

tts.tts_to_file(
    text="Hello Onkar, your application is now powered by XTTS version 2.",
    speaker="Ana Florence",
    language="en",
    file_path="xtts_output.wav"
)

print("XTTS audio generated successfully!")