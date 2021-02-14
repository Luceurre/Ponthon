import asyncio

async def server():
    async def connection_callback(reader, writer):
        print("got connection.")
        writer.close()
        await writer.wait_closed()

    s = await asyncio.start_server(connection_callback, host="localhost", port=5000)
    async with s:
        print("Starting server.")
        await s.serve_forever()

asyncio.run(server())
