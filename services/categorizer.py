# from openai import AsyncOpenAI

# client = AsyncOpenAI(api_key="org-d9LtPMuQUvOEjX3KYs1iSjuf")

# async def categorize_text(text: str) -> str:
#     prompt = (
#         "Категоризируй жалобу по одной из категорий: техническая, оплата, другое.\n"
#         f"Жалоба: \"{text}\"\n"
#         "Ответ только одной категорией:"
#     )
#     try:
#         response = await client.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=[{"role": "user", "content": prompt}],
#             temperature=0,
#         )
#         category = response.choices[0].message.content.lower().strip()
#         print("OpenAI category result:", category)
#         return category if category in ["техническая", "оплата", "другое"] else "другое"
#     except Exception as e:
#         print("OpenAI API error:", e)
#         return "другое"


from services.gpt import ask_gpt


VALID_CATEGORIES = {"техническая", "оплата", "другое"}

async def categorize_text(text: str) -> str:
    prompt = (
        "Категоризируй жалобу по одной из категорий: техническая, оплата, другое.\n"
        f"Жалоба: \"{text}\"\n"
        "Ответ только одной категорией и без точек или ещё чего"
    )
    return await ask_gpt(prompt, VALID_CATEGORIES)
