import asyncio
import websockets


def convert_speech_to_text(speech):
    return "Hello"+speech


async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = convert_speech_to_text(name)

    await websocket.send(greeting)
    print(f"> {greeting}")


start_server = websockets.serve(hello, "localhost", 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()