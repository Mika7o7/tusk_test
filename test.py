import httpx
from openai import OpenAI
from config import OPENAI_API_KEY

# Настройка прокси
proxy_url = "http://185.192.246.42:3128"

transport = httpx.HTTPTransport(proxy=proxy_url)

http_client = httpx.Client(transport=transport, timeout=30.0)

client = OpenAI(
    api_key=OPENAI_API_KEY,
    http_client=http_client,
)

# Отправка запроса к GPT
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Write a one-sentence bedtime story about a unicorn."}
    ]
)

print(response.choices[0].message.content)
