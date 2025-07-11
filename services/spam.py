import httpx
from config import SPAMCHECKER_API_KEY

API_URL = "https://api.apilayer.com/spamchecker?threshold=4"  # Порог установлен на 4

async def check_spam(text: str) -> bool:
    headers = {
        "apikey": SPAMCHECKER_API_KEY,
        "Content-Type": "text/plain"
    }
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(API_URL, headers=headers, content=text.encode("utf-8"))
            response.raise_for_status()
            data = response.json()
            print("Spam check result:", data)
            # Пример ответа: {"score": 4, "is_spam": true}
            return data.get("is_spam", False)
    except Exception as e:
        print("Spam check error:", e)
        return False  # В случае ошибки считаем, что это не спам
