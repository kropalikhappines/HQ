# Учебная платформа

## Описание

Учебная платформа представляет собой веб-приложение для создания и управления онлайн-курсами и уроками. Это приложение может быть использовано для обучения и обучения студентов и учащихся.
Этот проект создан в качестве теста от компании HQ
## Требования

- Python 3.9+
- Django 4.2.5+
- Django REST framework 3.14+
- SQLite

## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/kropalikhappines/HQ.git
2. Создайте и активируйте виртуальное окружение:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ./venv/Scripts/activate

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt

4. Примените миграции:
   ```bash
   python manage.py makemigration
   python manage.py migrate

5. Запустите сервер:
   ```bash
   python manage.py runserver

## Использование

Создайте учетную запись суперпользователя:
   ```bash
   python manage.py createsuperuser
   ```
Зайдите в админ-панель по адресу http://127.0.0.1:8000/admin/ и добавьте продукты и уроки.

Используйте API для доступа к данным (см. раздел "API" ниже).

## API
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

## Лицензия
MIT

## Авторы
Лазарев Арслан Витальевич - lazarevarslan@yandex.ru, arsik30394@gmail.com
