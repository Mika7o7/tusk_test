from g4f.client import Client
import asyncio

client = Client()

VALID_CATEGORIES = {"техническая", "оплата", "другое"}
VALID_SENTIMENTS = {"положительная", "нейтральная", "отрицательная"}

async def ask_gpt(prompt: str, valid_responses: set[str], retries: int = 3) -> str:
    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0,
            )
            result = response.choices[0].message.content.strip().lower()
            print(f"GPT result (attempt {attempt+1}):", result)

            if result in valid_responses:
                return result
        except Exception as e:
            print(f"GPT error (attempt {attempt+1}):", e)

        await asyncio.sleep(1)  # Пауза между попытками
    return list(valid_responses)[-1]  # Возвращаем последнее как fallback