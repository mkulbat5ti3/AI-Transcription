import wave
import time
import os
import datetime
import json

from transformers import pipeline
from server.vad import setup_vad_pipeline
from server.translator import translate_text
from server.utils import AUDIO_DIR, get_timestamped_filename, copy_to_archive, save_text_to_archive
from server.config import SAMPLE_RATE, AUDIO_CHANNELS, SAMPLES_WIDTH, DEBUG

recognition_pipeline = pipeline("automatic-speech-recognition", model="openai/whisper-large-v3")
vad_pipeline = setup_vad_pipeline()

client_temp_buffers = {}
file_counters = {}

async def transcribe_and_send(client_id, websocket, new_audio_data, client_config):
    if client_id not in client_temp_buffers:
        client_temp_buffers[client_id] = bytearray()

    audio_data = bytes(client_temp_buffers[client_id]) + new_audio_data
    client_temp_buffers[client_id] = bytearray(audio_data)

    if client_id not in file_counters:
        file_counters[client_id] = 0

    file_name = os.path.join(AUDIO_DIR, f"{client_id}_{file_counters[client_id]}.wav")
    file_counters[client_id] += 1

    with wave.open(file_name, 'wb') as wav_file:
        wav_file.setnchannels(AUDIO_CHANNELS)
        wav_file.setsampwidth(SAMPLES_WIDTH)
        wav_file.setframerate(SAMPLE_RATE)
        wav_file.writeframes(audio_data)

    result = vad_pipeline(file_name)
    if len(result) == 0:
        os.remove(file_name)
        return

    last_segment = list(result.itersegments())[-1]

    if last_segment.end < (len(audio_data) / (SAMPLES_WIDTH * SAMPLE_RATE)) - int(client_config['chunk_offset_seconds']):
        if client_config['language']:
            asr_result = recognition_pipeline(file_name, generate_kwargs={"language": client_config['language']})
        else:
            asr_result = recognition_pipeline(file_name)

        text = asr_result['text']
        if text:
            translated = translate_text(text, client_config['translationLanguage'])

            filename_base, date_folder = get_timestamped_filename(client_id, ext="")
            save_text_to_archive(client_id, date_folder, text, f"{filename_base}")
            save_text_to_archive(client_id, date_folder, translated, f"{filename_base}_translation_{client_config['translationLanguage']}")
            copy_to_archive(file_name, client_id)

            await websocket.send(json.dumps({"type": "transcription", "text": text}))
            await websocket.send(json.dumps({"type": "translation", "text": translated}))

            client_temp_buffers[client_id].clear()

    os.remove(file_name)
