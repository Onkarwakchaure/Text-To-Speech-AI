# AI Text To Speech

An AI-powered multilingual Text-to-Speech web application built with FastAPI and XTTS v2.

## Features

* English Text-to-Speech
* Hindi Text-to-Speech
* XTTS v2 Voice Cloning
* MP3 Upload Support
* WAV Upload Support
* MP3 Audio Output
* Browser Audio Playback
* Download Generated Audio
* Modern Web Interface
* Automatic Temporary File Cleanup

## Tech Stack

### Backend

* FastAPI
* Python
* Coqui XTTS v2

### Frontend

* HTML
* CSS
* JavaScript

### Audio Processing

* Pydub
* FFmpeg

### Version Control

* Git
* GitHub

## How It Works

### Default Voice Mode

1. Enter text
2. Select language
3. Generate speech
4. Listen or download MP3

### Voice Cloning Mode

1. Upload a voice sample (MP3 or WAV)
2. Enter text
3. Generate speech
4. XTTS clones the uploaded voice
5. Listen or download MP3

## Supported Languages

* English (en)
* Hindi (hi)

## Installation

### Clone Repository

```bash
git clone https://github.com/Onkarwakchaure/Text-To-Speech-AI.git
cd Text-To-Speech-AI
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Run Application

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

## Project Status

Version: 1.0

Completed Features:

* Text-to-Speech
* Hindi Support
* Voice Cloning
* MP3 Upload Support
* MP3 Output Support
* Browser Playback
* GitHub Integration

## Future Improvements

* Additional Built-in Voices
* Marathi Support
* Better UI/UX
* Deployment
* User Accounts
* Cloud Storage

## Author

Onkar Wakchaure

GitHub:
https://github.com/Onkarwakchaure
