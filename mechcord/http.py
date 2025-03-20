import aiohttp
import json

class HTTPClient:
    BASE_URL = "https://discord.com/api/v10"
    
    def __init__(self, token, session=None):
        self.token = token
        self.session = session if session else aiohttp.ClientSession(headers={
            "Authorization": f"Bot {self.token}",
            "Content-Type": "application/json"
        })

    async def request(self, method, endpoint, **kwargs):
        url = f"{self.BASE_URL}{endpoint}"
        async with self.session.request(method, url, **kwargs) as response:
            data = await response.json()
            return data

    async def close(self):
        await self.session.close()
