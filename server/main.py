import asyncio
import websockets
import signal
import sys

from server.config import HOST, PORT
from server.websocket_handler import receive_audio

def exit_gracefully(signum, frame):
    print("Exiting...")
    sys.exit(0)

async def main():
    async with websockets.serve(receive_audio, HOST, PORT):
        print(f"WebSocket server running at ws://{HOST}:{PORT}")
        await asyncio.Future()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, exit_gracefully)
    asyncio.run(main())
