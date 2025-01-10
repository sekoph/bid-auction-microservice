import httpx

async def fetch_data(url, headers=None):
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()  # Raise error if the request fails
        return response.json()