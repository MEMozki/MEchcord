import aiohttp
import asyncio
import json

class DiscordWebSocket:
    def __init__(self, token, intents, session, client):
        self.token = token
        self.intents = intents
        self.session = session
        self.gateway = "wss://gateway.discord.gg/?v=10&encoding=json"
        self.client = client

    async def connect(self):
        async with self.session.ws_connect(self.gateway) as ws:
            identify = {
                "op": 2,
                "d": {
                    "token": self.token,
                    "intents": self.intents,
                    "properties": {
                        "$os": "linux",
                        "$browser": "mechcord",
                        "$device": "mechcord"
                    }
                }
            }
            await ws.send_json(identify)
            print("The bot has been launched.\n© MEchcord, 2025.")

            async for msg in ws:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    data = json.loads(msg.data)
                    print(f"[!] Received event: {data}")
                    event_type = data.get("t")
                    event_data = data.get("d")
                    if event_type:
                        await self.client.on_event(event_type, event_data)
                elif msg.type == aiohttp.WSMsgType.ERROR:
                    print("[!] WebSocket error.")
                    break
