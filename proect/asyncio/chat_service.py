import asyncio

clients = set()  # Множество для хранения подключенных клиентов

async def handle_client(reader, writer):
    # Добавление нового клиента
    clients.add(writer)
    address = writer.get_extra_info('peername')
    print(f"Подключен: {address}")

    try:
        while True:
            data = await reader.read(100)
            message = data.decode().strip()

            if not message:
                break  # Если сообщение пустое, клиент отключился

            print(f"Получено сообщение от {address}: {message}")

            # Отправка сообщения всем клиентам
            for client in clients:
                if client != writer:  # Не отправляем сообщение обратно отправителю
                    client.write(f"{address}: {message}\n".encode())
                    await client.drain()  # Ожидание, пока данные будут отправлены

    except asyncio.CancelledError:
        pass
    finally:
        # Удаление клиента при отключении
        clients.remove(writer)
        print(f"Отключен: {address}")
        writer.close()

async def main():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 8888)
    print("Сервер запущен на порту 8888")

    async with server:
        await server.serve_forever()

asyncio.run(main())
