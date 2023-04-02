import asyncio
import websockets
from keyRecConf import HOST, PORT

CLIENT = set()

async def handler(websocket):
    CLIENT.add(websocket)
    try:
        async for message in websocket:
            await broadcast(message, websocket)
    finally:
        CLIENT.remove(websocket)

async def send(websocket, message):
    try:
        await websocket.send(message)
    except websockets.exceptions.ConnectionClosed:
        pass

async def broadcast(message, sender):
    CLIENT_EXCLUDE = CLIENT.copy()
    CLIENT_EXCLUDE.remove(sender)
    if CLIENT_EXCLUDE:
        await asyncio.wait([asyncio.create_task(send(websocket, message)) for websocket in CLIENT_EXCLUDE])

async def main():
    async with websockets.serve(handler, HOST, PORT):
        await asyncio.Future()  # run forever

asyncio.run(main())
