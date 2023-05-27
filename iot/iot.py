'''
import asyncio
import websockets

async def hello(websocket):
    name = await websocket.recv()
    print(f"<<< {name}")

async def main():
    async with websockets.serve(hello, "192.168.10.69", 8080):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())

'''