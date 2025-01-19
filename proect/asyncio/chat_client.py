import asyncio

async def chat_client():
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)

    while True:
        message = input("Введите сообщение: ")
        writer.write(message.encode())
        await writer.drain()

        if message.strip().lower() == 'exit':
            break

    writer.close()
    await writer.wait_closed()  # Рекомендуется дождаться закрытия

asyncio.run(chat_client())
