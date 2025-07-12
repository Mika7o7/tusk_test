🐍 API: Жалобы — FastAPI сервис
📌 Описание
Это backend-сервис на FastAPI, предназначенный для приёма, хранения и управления жалобами.
Сервис предоставляет REST API, который можно интегрировать с внешними системами (например, n8n), но в этом документе мы описываем только сам API.

📂 Возможности API
📥 Приём и хранение жалоб

🔍 Получение списка открытых жалоб

✅ Закрытие жалобы по ID

🛡 Проверка текста жалобы на спам через внешний API (API Layer)

🌍 Определение геолокации клиента (по IP) при создании жалобы

🤖 (Опционально) анализ текста с помощью OpenAI GPT

⚙️ Переменные окружения (.env)
Создай файл .env в корне проекта и укажи переменные:

env
Копировать
Редактировать
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
🔹 Для определения геолокации, используется тот же API Layer ключ, что и для проверки спама.

🚀 Запуск проекта
Убедитесь, что у вас установлен Python 3.10+
Далее:

bash
Копировать
Редактировать
git clone https://github.com/Mika7o7/tusk_test.git
cd tusk_test

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt


🟢 Запуск API сервера

python main.py

или через uvicorn:


uvicorn main:app --host 0.0.0.0 --port 8000 --reload
Сервер будет доступен по адресу:
http://localhost:8000

Документация:

Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc
