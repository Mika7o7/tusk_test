# import httpx

# API_KEY = "BhzU0dpwhywaAud8YaTs3Nt5tmtNTms7"
# API_URL = "https://api.apilayer.com/sentiment/analysis"

# async def analyze_sentiment(text: str) -> str:
#     headers = {
#         "apikey": API_KEY,
#         "Content-Type": "text/plain"  # важно!
#     }

#     payload = text

#     try:
#         async with httpx.AsyncClient() as client:
#             response = await client.post(API_URL, headers=headers, content=payload)
#             response.raise_for_status()
#             result = response.json()
#             print("Sentiment API result:", result)
#             return result.get("sentiment", "unknown")
#     except Exception as e:
#         print("Sentiment API error:", e)
#         return "unknown"


from services.gpt import ask_gpt

VALID_SENTIMENTS = {"положительная", "нейтральная", "отрицательная"}

async def analyze_sentiment(text: str) -> str:
    prompt = (
        "Определи тональность жалобы: положительная, нейтральная или отрицательная\n"
        f"Жалоба: \"{text}\"\n"
        "Ответ только одним словом и без точек или ещё чего"
    )
    return await ask_gpt(prompt, VALID_SENTIMENTS, retries=5)