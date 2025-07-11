import httpx

async def get_geo_data(ip: str) -> dict:
    url = "http://ip-api.com/batch"
    payload = [{"query": ip, "fields": "city,country,countryCode,query", "lang": "ru"}]
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=payload)
            response.raise_for_status()
            data = response.json()
            return data[0] if data else {}
    except Exception as e:
        print("Geo API error:", e)
        return {}