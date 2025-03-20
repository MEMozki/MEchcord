import asyncio
import aiohttp
from .websocket import DiscordWebSocket
from .http import HTTPClient

class Client:
    def __init__(self, token, intents=513):
        self.token = token
        self.intents = intents
        self.session = aiohttp.ClientSession() 
        self.ws = None
        self.commands = {}
        self.event_handlers = {}
        self.http = HTTPClient(token, session=self.session)

    async def on_event(self, event_name, data):
        handler = self.event_handlers.get(event_name)
        if handler:
            await handler(data)

    def event(self, coro):
        self.event_handlers[coro.__name__] = coro
        return coro

    def command(self, name=None):
        def decorator(func):
            cmd_name = name or func.__name__
            self.commands[cmd_name] = func
            return func
        return decorator

    async def send_message(self, channel_id, message):
        endpoint = f"/channels/{channel_id}/messages"
        payload = {"content": message}
        return await self.http.request("POST", endpoint, json=payload)

    async def start(self):
        self.ws = DiscordWebSocket(self.token, self.intents, self.session, client=self)
        await self.ws.connect()

    def run(self):
        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(self.start())
        except KeyboardInterrupt:
            loop.run_until_complete(self.session.close())
            print("[!] Bot shutdown.")
