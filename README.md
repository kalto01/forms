# forms
Web-приложение для определения заполненных форм.

Входные данные для веб-приложения:
Список полей со значениями в теле POST запроса.

Выходные данные:
Имя наиболее подходящей данному списку полей формы, 
при отсутствии совпадений с известными формами произвести типизацию полей на лету и вернуть список полей с их типами.

Использован следующий стек:
1. fastapi
2. tinydb




Шаги для запуска проекта:
1. установить пакеты pip install -r requirements.txt
2. запустить проект uvicorn main:app --reload 


Шаги для запуска тестов:
1. pytest src/tests.py

> Данные уже хранятся в database.json
