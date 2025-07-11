from dotenv import load_dotenv
import os

load_dotenv()  # Загружает переменные из .env

SPAMCHECKER_API_KEY = os.getenv("SPAMCHECKER_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")