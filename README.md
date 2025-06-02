# Real-Time Transcription and Translation Server

This project provides a real-time audio transcription and translation server using:

- 🎤 **OpenAI Whisper** for speech recognition  
- 🔊 **HuggingFace Pyannote** for voice activity detection  
- 🌐 **DeepL** for translation  
- 🌍 WebSocket-based audio streaming from browser clients

---

## 🚀 Features

- Real-time voice-to-text transcription from microphone
- Automatic translation into multiple languages
- Voice activity detection to ignore silence
- Archives audio, transcripts, and translations
- Frontend UI to control streaming and view results live

---

## 📁 Project Structure

```
.
├── server/              # Backend logic
│   ├── main.py          # Server entry point
│   ├── config.py        # Env config & constants
│   ├── transcriber.py   # Transcription pipeline
│   ├── websocket_handler.py
│   ├── vad.py           # Voice Activity Detection
│   ├── translator.py    # DeepL wrapper
│   └── utils.py         # File/archive helpers
├── client/              # Web frontend
│   ├── client.html
│   ├── styles.css
│   └── utils.js
├── archive/             # Auto-created: stores transcripts/audio
├── audio_files/         # Temp audio during processing
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🛠️ Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Prepare Environment Variables

Create a `.env` file based on `.env.example`:

```bash
cp .env.example .env
```

Set your DeepL and HuggingFace API keys inside `.env`.

---

## 🌐 Run the Server

```bash
python server/main.py
```

---

## 💻 Using the Web Interface

1. Open `client/client.html` in your browser.
2. Enter your WebSocket address (e.g. `ws://localhost:8765`).
3. Click **Connect**, then **Start Streaming**.

---

## 📄 License

MIT — feel free to use, modify, and distribute with credit.

---

## 👤 Maintainer

Developed and maintained by Zayed Albloushi

---

## 🤝 Contributing

Contributions welcome! Please fork the repo and submit a pull request.