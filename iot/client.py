# need to build something that accepts GET and POST from an IoT device 
# and loads that into the database in a way that makes sense and that can be connected later



import asyncio
import websockets

async def receive_data():
    while True:
        uri = "ws://192.168.10.129"
        async with websockets.connect(uri) as websocket:
            message = await websocket.recv()
            print(f"<<< {message}")



if __name__ == "__main__":
    asyncio.run(receive_data())