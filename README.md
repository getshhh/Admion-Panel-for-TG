## Описание
- Эта админка для Telegram позволяет пользователям вводить ID пользователя и получать доступ к функциям администратора.

## Функции
- Ввод ID пользователя: пользователь вводит ID пользователя в текстовое поле.
- Проверка ID: при нажатии кнопки "Готово" админка проверяет, был ли введен ID. Если ID не введен, то пользователю отображается сообщение об ошибке.
- Переход к функциям администратора: если ID введен, пользователь переходит на страницу функций администратора, где может выполнять различные задачи.

## Структура проекта
- app.py: файл, содержащий код для запуска Flask-приложения.
- bot.py: файл, содержащий код для создания бота и его настройки.
- static: папка, содержащая статические файлы CSS и HTML.
- main.css: файл CSS для основной страницы админки.
- batton.css: файл CSS для страницы функций администратора.
- index.html: файл HTML для основной страницы админки.
- base.html: файл HTML для основной страницы админки.
- G_batton.html: файл HTML для страницы функций администратора.
- batton.html: файл HTML для страницы функций администратора.

## ак запустить проект
- Установите зависимости: pip install aiogram flask aiohttp
- Запустите Flask-приложение: python app.py
- Запустите бота: python bot.py

## Как использовать админку
- Отправьте сообщение боту с текстом /start.
- Введите ID пользователя в текстовое поле на странице админки.
- Нажмите кнопку "Готово".
- Если ID введен, вы будете перенаправлены на страницу функций администратора.
## Важно
- Убедитесь, что вы заменили 'YOUR_API_TOKEN' на свой собственный токен Telegram Bot API в файле bot.py.
- Убедитесь, что вы запустили Flask-приложение и бота правильно.
- Если вы на Localhost, то используйте ngork