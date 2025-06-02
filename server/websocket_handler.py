import json
import uuid
from server.config import SAMPLE_RATE, SAMPLES_WIDTH, DEFAULT_CLIENT_CONFIG
from server.transcriber import transcribe_and_send

connected_clients = {}
client_buffers = {}
client_configs = {}

async def receive_audio(websocket, path):
    client_id = str(uuid.uuid4())
    connected_clients[client_id] = websocket
    client_buffers[client_id] = bytearray()
    client_configs[client_id] = DEFAULT_CLIENT_CONFIG.copy()

    print(f"Client {client_id} connected")

    try:
        async for message in websocket:
            if isinstance(message, bytes):
                client_buffers[client_id].extend(message)
            elif isinstance(message, str):
                config = json.loads(message)
                if config.get('type') == 'config':
                    client_configs[client_id] = config['data']
                    continue

            buffer = client_buffers[client_id]
            if len(buffer) > int(client_configs[client_id]['chunk_length_seconds']) * SAMPLE_RATE * SAMPLES_WIDTH:
                await transcribe_and_send(client_id, websocket, buffer, client_configs[client_id])
                client_buffers[client_id].clear()

    except Exception as e:
        print(f"Client {client_id} error: {e}")
    finally:
        print(f"Client {client_id} disconnected")
        del connected_clients[client_id]
        del client_buffers[client_id]
