import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 8765))

SAMPLE_RATE = 16000
AUDIO_CHANNELS = 1
SAMPLES_WIDTH = 2  # 16-bit audio

DEBUG = os.getenv("DEBUG", "true").lower() == "true"

DEEPL_AUTH_KEY = os.getenv("DEEPL_AUTH_KEY")
HF_AUTH_TOKEN = os.getenv("HF_AUTH_TOKEN")

DEFAULT_CLIENT_CONFIG = {
    "language": None,
    "chunk_length_seconds": 5,
    "chunk_offset_seconds": 1,
}
