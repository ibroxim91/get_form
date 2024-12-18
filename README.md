
# Описание проекта
## Этот проект включает в себя два приложения, Django и FastAPI, а также контейнер с MongoDB для хранения данных. Каждый проект имеет свой собственный docker-compose файл для запуска. Дополнительно предоставляется скрипт для тестирования API, который можно запустить  локально.

## Структура проекта

![Sxema](project_folders.png)

## Установка и запуск
Шаг 1: Установка Docker и Docker Compose
Прежде чем начать, убедитесь, что Docker и Docker Compose установлены на вашем компьютере.

Для Linux / macOS:
``` bash

# Установите Docker (если он еще не установлен)
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

# Установите Docker Compose (если он еще не установлен)
``` bash 
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
Для Windows:
Скачайте и установите Docker Desktop с официального сайта.

Шаг 2: Запуск Docker контейнеров
Запуск с помощью docker-compose:
Перейдите в каталог проекта, где находятся оба docker-compose.yml файла.

Для запуска Django приложения: Перейдите в папку с проектом Django:

``` bash

cd get_form_django_drf

#Запустите контейнеры:

docker-compose up --build

# или 

make project-up  # linux, macos

# Для запуска FastAPI приложения: Перейдите в папку с проектом FastAPI:


cd get_form_fast_api
#Запустите контейнеры:


docker-compose up --build

# или

make project-up  # linux, macos

```

## Или можно запустить оба проекта одновременно:
Перейдите в папку, содержащую оба проекта, и используйте следующие команды для запуска контейнеров для Django и FastAPI.

``` bash 
#Запустите контейнеры:


docker-compose up --build

```


## Шаг 3: Запуск тестов с помощью скрипта
Скрипт для Linux/macOS (run.sh):
Для запуска тестов API, используйте скрипт run.sh:

Откройте терминал и перейдите в каталог проекта.
Сделайте файл исполнимым:
``` bash

chmod +x run.sh
# Запустите скрипт:


./run.sh

```

Скрипт для Windows (run.bat):
Для запуска тестов API, используйте скрипт run.bat:

Откройте командную строку и перейдите в каталог проекта.
Запустите скрипт:
``` bash

run.bat

```

## Шаг 4: Тестирование API
Скрипт script.py выполняет тестирование API для обоих приложений (Django и FastAPI). Для того чтобы протестировать, скрипт выполняет POST-запросы к эндпоинту /get_form. Убедитесь, что контейнеры Django и FastAPI работают, прежде чем запускать тесты.

Пример тестирования:
Введите тестовые данные для форм в script.py.
Скрипт выполнит запросы и выведет результат.
python

# Пример данных для тест запроса


``` bash
payload = {
    "name": "Contact Form",
    "lead_email": "email@mail.ru",
    "user_phone": "+78991234567",
    "submission_date": "15.10.2024"
}

```

# Запуск теста
test_get_form()
Примечания:
Скрипт автоматически проверяет статус ответа и выводит сообщение о прохождении теста.
Убедитесь, что ваши контейнеры с Django и FastAPI работают на портах 8000 и 8001 соответственно.
Используйте порт 8000 для проверки проекта Django и 8001 для Fast Api.

## Тестировать  с помощью Postman
Также можно  тестировать  с помощью Postman. для этого импортируйте файл Get Form.postman_collection.json из репозитория в программу Postman