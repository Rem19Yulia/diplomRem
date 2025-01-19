Дипломная работа

По теме: Сравнение различных подходов к реализации асинхронного программирования: asyncio, threading и multiprocessing.
Реализовать асинхронные задачи с использованием asyncio, threading и multiprocessing, сравнить их производительность и уместность для различных типов задач.







Автор: Ремнева Юлия Владимировна






Оглавление дипломной работы:
1.	Введение – 3 стр.
     - Обоснование выбора темы – 3 стр.
     - Цели и задачи исследования – 3 стр.
2.	Основные понятия и определения – 3 стр.
3.	Краткое сравнение методов – 4 стр.
4.	Метод asyncio – 7 стр.
- Файловая структура проекта – 7 стр.
- Что выполняет asyncio в этом коде – 8 стр.
- Вывод – 9 стр.
5. Метод threading – 10 стр.
- Файловая структура проекта – 10 стр.
- Что выполняет threading в этом коде – 12 стр.
6. Метод multiprocessing – 13 стр.
- Файловая структура проекта – 13 стр.
- Что выполняет multiprocessing в этом коде – 17 стр.
7. Заключение
-  Почему treading и multiprocessing не подходят для задач ввода-вывода– 18 стр.
- Выводы – 20 стр.
- Почему asyncio и multiprocessing не подходят для не сложных задач, требующих параллельного выполнения – 20 стр.
- Выводы – 
- Почему threading и asyncio могут быть не лучшими выборами для задач парсинга, таких как выполнение поисковых запросов от пользователя – 21 стр. 
- Почему лучше использовать Multiprocessing для парсинга – 22 стр.
- Выводы – 23 стр.









Обоснование выбора темы

Асинхронное программирование в Python играет важную роль в разработке высокопроизводительных и масштабируемых приложений. 
Основные подходы к асинхронному программированию:
1.	Threading — использование потоков для выполнения задач параллельно в рамках одного процесса.
2.	Multiprocessing — запуск нескольких процессов для выполнения задач одновременно с возможностью задействования нескольких ядер процессора.
3.	Asyncio — использование библиотеки asyncio для асинхронного выполнения задач с использованием синтаксиса async/await.
Каждый подход имеет свои сильные и слабые стороны в зависимости от специфики задачи. 

Цели и задачи исследования
    Цель исследования заключается в оценке производительности и уместности каждого подхода в зависимости от типа задач.
    Этот проект посвящен сравнительному анализу трех ключевых подходов к асинхронному программированию: asyncio, threading и multiprocessing. Асинхронное программирование позволяет выполнять задачи параллельно, не блокируя основной поток выполнения программы. 

Основные понятия и определения
1. Корутин - это специальный тип функции в Python, который может приостанавливать свое выполнение и возобновлять его позже. Корутины используются для асинхронного программирования и позволяют выполнять несколько операций одновременно, не блокируя основной поток выполнения. 
2. async - это ключевое слово в Python, которое используется для определения корутины. Функция, объявленная с помощью async def, становится корутиной и может использовать await для приостановки своего выполнения. 
3. await - это ключевое слово, используемое внутри корутин для приостановки их выполнения до тех пор, пока не завершится другая корутина или асинхронная операция. Оно позволяет другим корутинам выполняться в это время, что делает асинхронное программирование более эффективным.
 4. CPU-bound задачи - это задачи, которые требуют значительных вычислительных ресурсов и времени процессора для выполнения. Примеры включают сложные математические вычисления, обработку изображений и другие задачи, требующие интенсивных вычислений. 
5. I/O-bound задачи - это задачи, которые в основном зависят от операций ввода-вывода, таких как чтение и запись файлов, сетевые запросы и взаимодействие с базами данных. Эти задачи часто блокируют выполнение программы, ожидая завершения операций ввода-вывода. 
6. GIL (Global Interpreter Lock) - это механизм в CPython, который обеспечивает потокобезопасность, позволяя только одному потоку выполнять байт-код Python в любой момент времени. Это ограничивает параллелизм в многопоточных приложениях и делает потоки менее эффективными для CPU-bound задач. 
7. Байт-код - это промежуточный код, который генерируется интерпретатором Python после компиляции исходного кода. Байт-код выполняется виртуальной машиной Python (PVM) и является более низким уровнем, чем исходный код, но более высоким, чем машинный код. 
8. CPython GIL - это GIL, специфичный для реализации Python, известной как CPython. Он ограничивает выполнение байт-кода Python в многопоточных приложениях, что может привести к снижению производительности при использовании потоков для CPU-bound задач.

Краткое сравнение методов
Асинхронное программирование в Python предоставляет разработчикам несколько подходов для выполнения параллельных задач. Рассмотрю каждый метод по трём параметрам: описание, преимущества, недостатки.
1.	asyncio — это библиотека для написания асинхронного кода с использованием корутин. Она позволяет выполнять несколько операций одновременно, не блокируя основной поток выполнения программы. 
Как работает: asyncio использует цикл событий, который управляет выполнением корутин. Корутину можно приостановить с помощью ключевого слова await, что позволяет другим корутинам выполняться в это время.
 Преимущества 
- Эффективность для I/O-bound задач: asyncio отлично подходит для работы с сетевыми запросами, файловыми операциями и другими задачами, связанными с вводом-выводом. 
- Легковесность: Корутину легче создать и управлять ею по сравнению с потоками, что позволяет экономить ресурсы. 
- Простота использования: Синтаксис с async и await делает код более читаемым и понятным.
 Недостатки 
- Неэффективность для CPU-bound задач: Все корутины выполняются в одном потоке, что делает asyncio неэффективным для задач, требующих значительных вычислительных ресурсов.
 - Сложность отладки: Асинхронный код может быть сложнее отлаживать из-за его нелинейной природы. 

2.	threading - это модуль, который позволяет создавать и управлять потоками в Python. Потоки могут выполняться параллельно, что позволяет программе выполнять несколько задач одновременно. 
Как работает: Каждый поток выполняет свою задачу, и потоки могут блокироваться на вводе-выводе, позволяя другим потокам продолжать выполнение. 
Преимущества
 - Подходит для I/O-bound задач: Потоки могут эффективно обрабатывать операции ввода-вывода, такие как сетевые запросы или чтение/запись файлов. 
- Простота использования: Легко создавать и управлять потоками, что делает их удобными для параллельного выполнения кода.
Недостатки
- GIL (Global Interpreter Lock): в CPython GIL ограничивает выполнение байт-кода Python, что делает потоки неэффективными для CPU-bound задач. 
- Сложность синхронизации: Необходимость синхронизации между потоками может привести к ошибкам и усложнению кода. 
 3. multiprocessing — это модуль, который позволяет создавать процессы, которые могут выполняться параллельно. Каждый процесс имеет свой собственный интерпретатор Python и память.
 Как работает: multiprocessing создает отдельные процессы, которые могут выполняться на разных ядрах процессора, что позволяет эффективно использовать многоядерные системы. 
Преимущества
 - Эффективность для CPU-bound задач: Каждый процесс может выполнять вычисления независимо, что позволяет обойти ограничения GIL.
 - Многоядерная поддержка: Позволяет использовать все доступные ядра процессора для выполнения задач. 
Недостатки
 - Высокая накладная стоимость: Создание и управление процессами требует больше ресурсов по сравнению с потоками. 
- Сложность обмена данными: Обмен данными между процессами может быть сложным и требует использования очередей или других механизмов. 

Выбор между asyncio, threading и multiprocessing зависит от типа задач, которые мы хотим решить:
-asyncio для I/O-bound задач, когда важна высокая производительность и низкое потребление ресурсов. 
-threading для простых параллельных задач, особенно если они связаны с вводом-выводом.
 - multiprocessing для задач, требующих значительных вычислительных ресурсов, чтобы эффективно использовать многоядерные процессоры. Каждый из этих подходов имеет свои сильные и слабые стороны. Рассмотрим их на примере.

Метод asyncio
Для примера я написала код асинхронного чат-сервера на Python с использованием asyncio. Позволяет нескольким клиентам подключаться и обмениваться сообщениями. Этот сервер будет отправлять сообщения всем подключенным клиентам, создавая простое чат-приложение.

Файловая структура проекта
 

Директория asyncio содержит в себе два файла: chat_klient.py отвечает за подключение клиентов, сообщения и chat_servise.py отвечает за запуск чат-сервера.
Файл chat_servise.py
1. Подключение клиентов: Когда клиент подключается, его writer добавляется в множество clients, что позволяет серверу отслеживать всех подключенных клиентов.
clients = set() - Множество для хранения подключенных клиентов
async def handle_client(reader, writer): # Добавление нового клиента clients.add(writer) address = writer.get_extra_info('peername') print(f"Подключен: {address}")
2.	Чтение сообщений: Сервер читает сообщения от клиента. Если сообщение пустое, это означает, что клиент отключился. 

try: while True: data = await reader.read(100) message = data.decode().strip() if not message: break # Если сообщение пустое, клиент отключился
3.	Рассылка сообщений: Когда сервер получает сообщение, он отправляет его всем другим клиентам, кроме отправителя. 

# Отправка сообщения всем клиентам
            for client in clients:
                if client != writer:  # Не отправляем сообщение обратно отправителю
                    client.write(f"{address}: {message}\n".encode())
                    await client.drain()  # Ожидание, пока данные будут отправлены

4.	Обработка отключений: Если клиент отключается, его writer удаляется из множества clients, и сервер выводит информацию об отключении.

# Удаление клиента при отключении clients.remove(writer) print(f"Отключен: {address}") writer.close()

Что выполняет asyncio в этом коде: 
1. Создание сервера: 
- asyncio.start_server(handle_client, '127.0.0.1', 8888) создает TCP-сервер, который будет слушать на локальном адресе 127.0.0.1 и порту 8888. Когда клиент подключается, вызывается функция handle_client, которая обрабатывает взаимодействие с этим клиентом.
 2. Обработка клиентов: 
- Функция handle_client является корутиной, которая принимает два параметра: reader и writer. Эти объекты используются для чтения данных от клиента и отправки данных обратно клиенту.
 - clients.add(writer) добавляет нового клиента в множество clients, чтобы можно было отправлять сообщения всем подключенным клиентам.
 3. Чтение данных: 
- data = await reader.read(100) — это асинхронная операция, которая ожидает, пока данные будут доступны для чтения от клиента. await позволяет другим корутинам выполняться в это время, не блокируя основной поток. 
4. Отправка сообщений:
- После получения сообщения от клиента, сервер отправляет это сообщение всем другим подключенным клиентам с помощью client.write(...) и await client.drain(). await client.drain() ожидает, пока данные будут отправлены, что также позволяет другим операциям выполняться в это время. 
5. Обработка отключений: - Если клиент отключается (например, отправляет пустое сообщение), сервер удаляет клиента из множества clients и закрывает соединение с помощью writer.close().
 6. Запуск сервера: - asyncio.run(main()) запускает основную корутину main, которая инициализирует сервер и начинает его работу. asyncio.run управляет циклом событий, необходимым для выполнения асинхронного кода. 
 Вывод: таким образом, asyncio в этом примере позволяет эффективно обрабатывать множество подключений клиентов одновременно, используя асинхронные операции для чтения и записи данных, что делает сервер более отзывчивым и способным обрабатывать большое количество клиентов без блокировок.
Файл chat_klient.py
Служит для запуска основного кода в файле и передаче сообщений. В данном коде asyncio используется для создания асинхронного клиента чата, который подключается к серверу и отправляет сообщения, а также:
 1. Установка соединения - reader, writer = await asyncio.open_connection('127.0.0.1', 8888) - это асинхронная операция, которая устанавливает TCP-соединение с сервером, работающим на локальном адресе 127.0.0.1 и порту 8888. Использование await позволяет другим корутинам выполняться в это время, не блокируя основной поток. 
2. Цикл ввода сообщений - внутри бесконечного цикла while True клиент ожидает ввода сообщения от пользователя с помощью input("Введите сообщение: "). После ввода сообщения оно отправляется на сервер.
 3. Отправка сообщения - writer.write(message.encode()) - это асинхронная операция, которая отправляет закодированное сообщение на сервер.
 4. Ожидание завершения отправки - await writer.drain() - это асинхронная операция, которая ожидает, пока все данные будут отправлены. Это позволяет убедиться, что данные действительно отправлены на сервер, прежде чем продолжить выполнение программы. 
5. Проверка на выход - если пользователь вводит сообщение "exit", программа выходит из цикла и завершает работу.
 6. Закрытие соединения - writer.close() - это асинхронная операция, которая закрывает соединение с сервером. 
7. Запуск клиента - asyncio.run(chat_client()) - это функция, которая запускает основную корутину chat_client, управляя циклом событий, необходимым для выполнения асинхронного кода. 
Таким образом, asyncio в этом примере позволяет клиенту чата работать асинхронно, устанавливать соединение с сервером, отправлять сообщения и обрабатывать ввод пользователя, не блокируя выполнение программы.

Метод threading
Для примера я создала код с использованием threading для пользовательского интерфейса, в котором пользователь загружает фото со своего устройства. Пользовалась библиотеками Tkinter и threading, которые позволяют пользователю загружать свое фото. В этом примере используется поток для загрузки изображения, чтобы интерфейс оставался отзывчивым.
Файловая структура проекта
 
Рисунок 2
В директории threading содержится файл interface.py, в котором находится основной код. Разберём содержание:
1.	Устанавливаем необходимые библиотеки - pip install pillow
2.	 Импортируем необходимые модули из Tkinter, Pillow и threading
import tkinter as tk 
from Tkinter import filedialog 
from PIL import Image, ImageTk 
import threading

3.	Функция upload_image - открывает диалоговое окно для выбора файла изображения. Если файл выбран, создается новый поток для загрузки изображения.

4.	Функция load_image - загружает изображение из выбранного файла и создает объект PhotoImage. Затем вызывает функцию update_image для обновления метки с изображением.


5.	 Функция update_image - обновляет метку с изображением в основном потоке, используя метод after, чтобы избежать проблем с многопоточностью. 

6.	Создание основного окна - создаем основное окно приложения и задаем его заголовок. 
root = tk.Tk()
 root.title("Загрузка изображения с использованием потоков")

7.	 Кнопка загрузки изображения - создаем кнопку, которая вызывает функцию upload_image при нажатии.

8.	  Метка для изображения - создаем метку, в которой будет отображаться загруженное изображение.
label = tk.Label(root)
 label.pack(pady=20)

9.	  Запуск основного цикла root.mainloop() - запускаем основной цикл приложения, чтобы интерфейс оставался активным. 

Теперь пользователь может загружать изображение, и интерфейс будет оставаться отзывчивым во время загрузки. Как это выглядит показано на рисунке 3 и рисунке 4

Что выполняет функция threading в этом коде
В данном коде библиотека threading выполняет несколько важных функций:
1.	Асинхронная загрузка изображения - использование потоков позволяет загружать изображение в фоновом режиме, не блокируя основной поток интерфейса. Это означает, что пользователь может продолжать взаимодействовать с интерфейсом (например, нажимать кнопки или закрывать окно), пока изображение загружается. 

2.	Улучшение отзывчивости интерфейса - без использования потоков, если бы загрузка изображения выполнялась в основном потоке, интерфейс стал бы неотзывчивым (замерз бы) до завершения загрузки. Это может создать плохой пользовательский опыт, особенно если изображение большое или загрузка занимает много времени. 


3.	Обработка изображений в фоновом режиме - поток, созданный с помощью threading.Thread, выполняет функцию load_image, которая отвечает за открытие и обработку изображения. Это позволяет избежать задержек в пользовательском интерфейсе. 

4.	 Безопасное обновление интерфейса - метод label.after(0, update_image, photo) используется для безопасного обновления метки с изображением в основном потоке. Это важно, поскольку многие GUI-библиотеки, включая Tkinter, не поддерживают обновление интерфейса из других потоков. Использование after позволяет запланировать выполнение функции update_image в основном потоке, что предотвращает возможные проблемы с многопоточностью. 

Таким образом, threading в данном коде обеспечивает плавную и отзывчивую работу пользовательского интерфейса, позволяя пользователю загружать изображения без задержек.

Метод multiprocessing
Для примера я создала код «Парсинг по поиску запроса от пользователя» с использованием функции multiprocessing. 
Файловая структура проекта
 
Рисунок 5 – структура

 1. Импорт библиотек: 
- `requests`: библиотека для выполнения HTTP-запросов. 
- `BeautifulSoup`: библиотека для парсинга HTML и XML документов. 
- `Pool` из `multiprocessing` позволяет создавать пул процессов для параллельного выполнения функций.
 ```python def search_query(query): ```
 
2. Определение функции `search_query`:
 - Эта функция принимает строку `query` (поисковый запрос) и выполняет поиск в DuckDuckGo. 
```python url = f'https://duckduckgo.com/?q={query}' ``` 

3. Формирование URL: 
- Формируется URL для выполнения запроса к DuckDuckGo с использованием переданного поискового запроса. 
```python try: response = requests.get(url) ``` 

4. Выполнение HTTP-запроса: 
- Блок `try` используется для обработки возможных ошибок при выполнении запроса. 
- `response = requests.get(url)`: выполняется GET-запрос к сформированному URL, и результат сохраняется в переменной 
`response`. ```python response.raise_for_status() # Проверка на успешный ответ (код 200) ``` 

5. Проверка успешности ответа: 
- `response.raise_for_status()`: проверяет, был ли ответ успешным (код 200). Если нет, выбрасывается исключение.
 ```python except requests.RequestException as e: print(f"Ошибка при выполнении запроса для '{query}': {e}") return [] # Возвращаем пустой список в случае ошибки ```

 6. Обработка ошибок:
 - Если возникает ошибка при выполнении запроса (например, проблемы с сетью), блок `except` перехватывает исключение.
 - Выводится сообщение об ошибке, указывающее, для какого запроса произошла ошибка.
 - Функция возвращает пустой список, чтобы избежать дальнейших ошибок при обработке результатов. 
```python soup = BeautifulSoup(response.text, 'html.parser') ```

 7. Парсинг HTML-ответа:
 - Ответ от сервера (HTML-код) передается в `BeautifulSoup` для парсинга. `soup` теперь содержит структуру HTML-документа. 
```python results = [] ```

 8. Создание списка для результатов:
 - Создается пустой список `results` для хранения заголовков и ссылок. 
```python for item in soup.find_all('a', class_='result__a'): ```

 9. Извлечение заголовков результатов поиска: 
- Цикл `for` проходит по всем элементам `<a>` с классом `result__a`, которые представляют собой результаты поиска.
 ```python title = item.get_text() link = item['href'] ``` 

10. Сохранение заголовков и ссылок: 
- Для каждого элемента извлекается текст (заголовок) с помощью `item.get_text()` и ссылка с помощью `item['href']`.
 ```python results.append((title, link)) ```

 11. Добавление результатов в список: 
- Заголовок и ссылка добавляются в список `results` в виде кортежа `(title, link)`. ```python return results ``` 
12. Возврат результатов:
 - Функция возвращает список результатов поиска. 
```python if __name__ == '__main__': ``` 

13. Проверка имени модуля: 
- Эта проверка позволяет убедиться, что код выполняется как основной модуль, а не импортируется из другого модуля.
 ```python user_query = input("Введите ваш поисковый запрос: ") ```

 14. Запрос от пользователя: 
- Программа запрашивает у пользователя ввод поискового запроса. 
```python queries = user_query.split() ```

 15. Разделение запроса на отдельные слова:
 - Ввод пользователя разбивается на отдельные слова, которые будут использоваться для параллельного поиска. 
```python with Pool(processes=4) as pool: ``` 

16. Создание пула процессов:
 - Создается пул из 4 процессов для выполнения функции `search_query` параллельно. 
```python results = pool.map(search_query, queries) ```

 17. Параллельный поиск: 
- `pool.map` применяет функцию `search_query` ко всем элементам списка `queries` параллельно, возвращая результаты в виде списка `results`. 

18. Цикл для вывода результатов:
 - Цикл проходит по всем результатам, используя `enumerate`, чтобы получить индекс и результаты для каждого запроса. 
```python print(f'Результаты для "{queries[i]}":') ```

 19. Вывод заголовка результатов:
 - Для каждого запроса выводится заголовок, указывающий, для какого запроса получены результаты. 
```python for title, link in query_results: print(f' - {title}: {link}') ``` 

20. Вывод заголовков и ссылок: 
- Вложенный цикл проходит по результатам для текущего запроса и выводит заголовок и ссылку в удобочитаемом формате. 
Таким образом, код выполняет поиск в DuckDuckGo по запросу пользователя, разбивает запрос на отдельные слова и использует параллельные процессы для ускорения поиска. 

Что выполняет multiprocessing в этом коде

В данном коде модуль multiprocessing используется для выполнения параллельных процессов, что позволяет ускорить выполнение программы, особенно при выполнении нескольких независимых задач, таких как HTTP-запросы. Подробнее рассмотрим, как именно он используется и что выполняет: 
1. Создание пула процессов: 
   with Pool(processes=4) as pool:
   
- Здесь создается пул из 4 процессов. Пул процессов позволяет управлять несколькими процессами, которые могут выполняться одновременно. Это особенно полезно для задач, которые могут быть выполнены параллельно, таких как выполнение HTTP-запросов.

 2. Параллельное выполнение функции: 
   results = pool.map(search_query, queries)
- Метод pool.map применяется для параллельного выполнения функции search_query для каждого элемента в списке queries.
 - pool.map разбивает список queries на части и распределяет их между доступными процессами в пуле. Каждый процесс выполняет функцию search_query для своего элемента списка.
 - Это позволяет одновременно отправлять несколько запросов к DuckDuckGo, что значительно ускоряет процесс поиска, особенно если запросов много.

Преимущества использования multiprocessing:
 - Ускорение выполнения: Параллельное выполнение позволяет значительно сократить общее время выполнения программы, так как несколько запросов могут обрабатываться одновременно, а не последовательно. 
- Эффективное использование ресурсов: Использование нескольких процессов позволяет более эффективно использовать ресурсы системы, особенно на многоядерных процессорах, где каждый процесс может выполняться на отдельном ядре.
 - Изоляция процессов: Каждый процесс в multiprocessing работает в своем собственном адресном пространстве, что означает, что они изолированы друг от друга. Это позволяет избежать проблем, связанных с многопоточностью, таких как гонки данных.
  Вывод: в целом, использование multiprocessing в этом коде позволяет эффективно выполнять параллельные HTTP-запросы, что делает программу более быстрой и отзывчивой. Это особенно полезно в случаях, когда необходимо выполнить множество независимых операций, таких как запросы к веб-сервисам.

Заключение по сравнению asyncio, threading и multiprocessing

Почему treading и multiprocessing не подходят для задач ввода-вывода
Хотя threading и multiprocessing могут использоваться для задач ввода-вывода, они не так эффективны, как asyncio, из-за накладных расходов на создание потоков и процессов, блокировок GIL и сложности управления состоянием. asyncio предлагает более эффективный и простой способ обработки задач ввода-вывода, особенно когда необходимо обрабатывать множество соединений или операций одновременно. Разберём каждую программу по отдельности на примере задачи ввода-вывода.

1.	Threading 
Проблемы с threading для задач ввода-вывода: 
- GIL (Global Interpreter Lock): В Python существует GIL, который позволяет только одному потоку выполнять байт-код Python в любой момент времени. Это означает, что даже если есть несколько потоков, они не могут одновременно выполнять вычисления. В случае задач ввода-вывода, когда поток ожидает завершения операции (например, чтение из сети или файла), другие потоки могут не использовать CPU эффективно, так как GIL блокирует выполнение. 
- Сложность управления потоками: При использовании потоков необходимо учитывать синхронизацию и управление состоянием, что может привести к сложностям, особенно если несколько потоков обращаются к общим ресурсам. Это может привести к гонкам данных и другим проблемам. 
- Накладные расходы на создание потоков: Создание и управление потоками требует ресурсов. Если задача ввода-вывода требует большого количества потоков, это может привести к значительным накладным расходам

2.	Multiprocessing
 Проблемы с multiprocessing для задач ввода-вывода:
 - Создание процессов. Создание новых процессов более ресурсоемко, чем создание потоков. Каждый процесс имеет свое собственное адресное пространство, что требует больше памяти и времени на инициализацию. Для задач ввода-вывода, где время ожидания может быть значительным, это может быть неэффективно.
 - Сложность взаимодействия между процессами. Процессы не могут напрямую делиться памятью, что делает обмен данными между ними более сложным. Это может привести к дополнительным накладным расходам на сериализацию и десериализацию данных, что также может снизить производительность. 
- Неэффективное использование ресурсов. Если процессы используются для задач ввода-вывода, они могут простаивать, ожидая завершения операций, что приводит к неэффективному использованию ресурсов. В то время как один процесс ждет, другие процессы могут не использовать CPU, что делает их менее эффективными для задач, связанных с вводом-выводом.
 Выводы:
- Неблокирующий ввод-вывод. asyncio использует неблокирующий ввод-вывод, что позволяет программе продолжать выполнение других задач, пока ожидается завершение операции ввода-вывода. Это позволяет эффективно использовать ресурсы и обрабатывать множество соединений одновременно. 
- Легковесность. asyncio работает в одном потоке и использует корутины, что делает его более легковесным по сравнению с потоками и процессами. Это позволяет обрабатывать большое количество соединений без значительных накладных расходов.
 - Простота управления. asyncio упрощает управление состоянием и синхронизацию, так как все операции выполняются в одном потоке, что снижает вероятность гонок данных и других проблем, связанных с многопоточностью.

Почему asyncio и multiprocessing не подходят для не сложных задач, требующих параллельного выполнения
1.  Проблемы с использованием asyncio для простых задач:
 - Сложность реализации. asyncio может быть излишним для простых задач. Использование asyncio может привести к усложнению кода и увеличению времени на его разработку и отладку. 
- Неблокирующий ввод-вывод. asyncio лучше всего подходит для задач, связанных с вводом-выводом, где время ожидания может быть значительным. Если задача проста и не требует длительных операций ввода-вывода, использование asyncio может быть избыточным, так как накладные расходы на управление асинхронными операциями могут превысить выгоды. 
- Отсутствие параллелизма. asyncio работает в одном потоке и не использует параллелизм. Если задача требует интенсивных вычислений, asyncio не сможет эффективно использовать многоядерные процессоры, что может привести к снижению производительности. 
2. Проблемы с использованием multiprocessing для простых задач: 
- Накладные расходы на создание процессов. Создание и управление процессами требует значительных ресурсов. Для простых задач, которые выполняются быстро, накладные расходы на создание процессов могут превышать время выполнения самой задачи. Это делает multiprocessing неэффективным для задач, которые не требуют длительного времени выполнения. 
- Сложность взаимодействия. Процессы имеют свои собственные адресные пространства, что делает обмен данными между ними более сложным. Для простых задач, где не требуется сложное взаимодействие, это может привести к излишней сложности и увеличению времени разработки. 
- Проблемы с производительностью. Если задача выполняется быстро, использование multiprocessing может привести к тому, что процессы будут часто создаваться и завершаться, что также может снизить общую производительность.
Выводы
Для простых задач, требующих параллельного выполнения, использование asyncio и multiprocessing может быть избыточным и неэффективным: 
- Для простых задач. Если задача не требует длительных операций ввода-вывода или интенсивных вычислений, использование потоков (threading) может быть более подходящим, так как они легче в реализации и имеют меньшие накладные расходы. 
- Для простых вычислений. Если задача требует параллельного выполнения, но не является сложной, использование потоков или даже простого последовательного выполнения может быть более эффективным, чем создание процессов или использование асинхронного программирования

Почему threading и asyncio могут быть не лучшими выборами для задач парсинга, таких как выполнение поисковых запросов от пользователя. 
1.	Проблемы с использованием threading для задач парсинга:
 - GIL (Global Interpreter Lock). В Python существует GIL, который позволяет только одному потоку выполнять байт-код Python в любой момент времени. Это означает, что даже если у вас есть несколько потоков, они не могут одновременно выполнять вычисления. При парсинге данных, который может быть ресурсоемким, это может привести к снижению производительности, так как потоки не могут эффективно использовать многоядерные процессоры. 
- Сложность управления потоками. При использовании потоков необходимо учитывать синхронизацию и управление состоянием, что может привести к сложностям, особенно если несколько потоков обращаются к общим ресурсам. Это может привести к гонкам данных, что усложняет код.
 - Накладные расходы на создание потоков. Создание и управление потоками требует ресурсов. Если задача парсинга требует большого количества потоков, это может привести к значительным накладным расходам, что делает использование потоков неэффективным. 
 2. Проблемы с использованием asyncio для задач парсинга: 
- Неблокирующий ввод-вывод. asyncio лучше всего подходит для задач, связанных с вводом-выводом, где время ожидания может быть значительным. Однако парсинг данных часто требует интенсивных вычислений и использование asyncio может не дать значительных преимуществ, так как он не использует параллелизм. 
- Сложность реализации. asyncio может привести к усложнению кода и увеличению времени на его разработку и отладку. 
- Отсутствие параллелизма. asyncio работает в одном потоке и не использует параллелизм. Если задача парсинга требует интенсивных вычислений, asyncio не сможет эффективно использовать многоядерные процессоры, что может привести к снижению производительности. 
Почему лучше использовать Multiprocessing для парсинга
 - Параллелизм. multiprocessing создает отдельные процессы, каждый из которых может выполняться на отдельном ядре процессора. Это позволяет эффективно использовать многоядерные процессоры для задач, требующих интенсивных вычислений, таких как парсинг данных.
 - Изоляция процессов. Каждый процесс имеет свое собственное адресное пространство, что позволяет избежать проблем, связанных с многопоточностью, такими как гонки данных. Это делает код более устойчивым и простым в отладке.
 - Эффективное использование ресурсов. Для задач парсинга, которые могут занимать значительное время, использование multiprocessing позволяет обрабатывать несколько запросов одновременно, что значительно ускоряет выполнение. 


Выводы
Для задач парсинга, таких как выполнение поисковых запросов от пользователя, использование threading и asyncio может быть неэффективным из-за ограничений GIL, сложности управления потоками и отсутствия параллелизма. Вместо этого multiprocessing предоставляет более подходящий подход, позволяя эффективно использовать ресурсы и обрабатывать задачи параллельно, что особенно важно для ресурсоемких операций, таких как парсинг данных.
