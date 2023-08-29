# Сайт "Blog by Django 4"

Blog by Django 4 - веб-приложение разработанное с помощью веб-фреймворка Django.

## Возможности сайта

- Регистрация и вход в систему для каждого пользователя по email либо по аккаунту Github/Google;
- Сброс пароля по почте, указанной при регистрации;
- Редактирование информации и изображения аватара в личном кабинете;
- Полнотекстовый поиск постов по триграммному сходству;
- Отображение схожих постов по числу имеющихся у них общих тегов;
- Добавлена пагинация (3 поста на страницу)
- Добавлена карта сайта
- Реализован API

## Требования

- Python (версия 3.10.8)
- Django (версия 4.2.1)
- Bootstrap (версия 5.x)
- Браузер с поддержкой HTML5 и CSS3

## Установка и настройка

1. Клонируйте репозиторий приложения на вашу локальную машину:
```
https://github.com/Comandosss/blog.git
```

2. Создайте виртуальное окружение
```
python -m venv env
```
  
3. Установите необходимые зависимости, используя pip:
```
pip install -r requirements.txt
```

4. Создайте базу данных и выполните миграции:
```
python manage.py migrate
```

5. Запустите сервер разработки Django:
```
python manage.py runserver
```

6. Откройте браузер и перейдите по адресу [http://localhost:8000](http://localhost:8000) для доступа к приложению.

## Использование

## Лицензия

[MIT License](LICENSE)
