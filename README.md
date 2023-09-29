# Учебная платформа

## Описание

Учебная платформа представляет собой веб-приложение для создания и управления онлайн-курсами и уроками. Это приложение может быть использовано для обучения и обучения студентов и учащихся.

## Требования

- Python 3.9+
- Django 4.2.5+
- Django REST framework 3.14+
- SQLite

## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/kropalikhappines/HQ.git
Создайте и активируйте виртуальное окружение:

python -m venv venv
source venv/bin/activate
./venv/Scripts/activate

Установите зависимости:

pip install -r requirements.txt

Примените миграции:

python manage.py migrate

Запустите сервер:

python manage.py runserver

Использование

Создайте учетную запись суперпользователя:

python manage.py createsuperuser

Зайдите в админ-панель по адресу http://127.0.0.1:8000/admin/ и добавьте продукты и уроки.

Используйте API для доступа к данным (см. раздел "API" ниже).

API
Получение списка всех продуктов
URL: /api/products/

Метод: GET

Получение списка всех уроков
URL: /api/lessons/

Метод: GET

Получение списка уроков по продукту
URL: /api/products/{product_id}/lessons/

Метод: GET

Примечание: Замените {product_id} на ID конкретного продукта.

Лицензия
MIT

Авторы
Лазарев Арслан Витальевич - lazarevarslan@yandex.ru, arsik30394@gmail.com
