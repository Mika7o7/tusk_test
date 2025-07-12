# 🐍 API: Жалобы — FastAPI сервис

## 📌 Описание

Это backend-сервис на **FastAPI**, предназначенный для приёма, хранения и управления **жалобами**.  
Сервис предоставляет **REST API**, который можно интегрировать с внешними системами (например, n8n),  
но в этом документе описан **только сам API**.

---

## 📂 Возможности API

- 📥 Приём и хранение жалоб
- 🔍 Получение списка **открытых жалоб**
- ✅ Закрытие жалобы по ID
- 🛡 Проверка текста жалобы на **спам** через внешний API (API Layer)
- 🌍 **Определение геолокации** клиента (по IP) при создании жалобы
- 🤖 (Опционально) анализ текста с помощью **OpenAI GPT**

---

🚀 Запуск проекта

Убедитесь, что у вас установлен Python 3.10+

📥 Клонируем репозиторий
```
git clone https://github.com/Mika7o7/tusk_test.git
cd tusk_test
```
🐍 Создаём и активируем виртуальное окружение
```
python -m venv venv
source venv/bin/activate  # для Linux/macOS
# venv\Scripts\activate   # для Windows
```
📦 Устанавливаем зависимости (библиотеки)
```
pip install -r requirements.txt
```

## ⚙️ Переменные окружения (`.env`)

Создайте файл `.env` в корне проекта и укажите следующие переменные:

```env
# FastAPI settings
HOST=0.0.0.0
PORT=8000

# Database
DATABASE_URL=sqlite:///./complaints.db

# API Layer (для проверки на спам и геолокацию)
SPAMCHECKER_API_KEY=your-API-Layer-token

# OpenAI Key (опционально)
# Для анализа жалоб через OpenAI, код уже написан в test.py.
# Если у вас есть ключ — можете подключить.
# OPENAI_API_KEY=your-OpenAI-token

🔹 Для определения геолокации используется http://ip-api.com/batch.

```

🟢 Запуск API сервера


```
python3 -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

После запуска:

🧪 Тестирование API через Swagger UI
Перейдите по адресу:
📘 Swagger UI: http://localhost:8000/docs

Вы сможете протестировать все доступные эндпоинты прямо из браузера.

📡 Примеры HTTP-запросов
✅ 1. Отправка жалобы

```
POST /complaints
Content-Type: application/json

{
  "text": "Этот продукт — обман!",
  "ip": "8.8.8.8"
}

```
Ответ будет содержать информацию о жалобе, статус спама и геолокацию клиента.

📋 2. Получение всех открытых жалоб
```
GET /complaints/open
```

🔒 3. Закрытие жалобы по ID
```
PUT /complaints/{id}/close
```
Пример:
```
PUT /complaints/5/close
```


# 🌐 Интеграция с n8n (отдельно от API)
Ниже описана настройка внешнего инструмента n8n, который будет использовать данное API.

🔐 Шаг 1: Вход в n8n
Перейди по ссылке: https://whiterabbite.ru/

Войди:
```
Email: mikaohanyan881@gmail.com

Пароль: y3pA9jc%
```
## 🛠 Шаг 2: Открой workflow
  - Ссылка: https://whiterabbite.ru/workflow/knLeyLD8js9HQAVN

## 📥 Шаг 3: Настрой переменные
  - 1. Telegram
  - Токен бота: получи через @BotFather

  - ID чата: можно получить через @getmyid_bot

## Добавь в Credentials в n8n:

  - Telegram → Bot Token

  - 2. Google Sheets
    Создай таблицу в Google Sheets

  - Подключи Google Service Account

  - Разреши доступ к таблице по email из .json ключа

## В таблице должны быть колонки:
```
Дата
Текст
Тональность
```
## ✅ Как это работает:
  - n8n каждые час вызывает API → получает список новых жалоб.

  - Если жалоба "техническая" — сообщение уходит в Telegram.

  - Если "оплата" — строка добавляется в Google Sheets.

  - Затем жалоба закрывается через PUT /complaints/{id}/close.

💬 Контакты
```
Разработчик: Мика
Telegram: @mikaggwp
Email: mikaohanyan881@gmail.com
```
