import aiohttp
import asyncio


class RequestSender:
    ENDPOINT = "/"

    async def get(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.ENDPOINT) as response:
                print(await response.json())
                return response


class HttpBinHeaders(RequestSender):
    ENDPOINT = "/headers"


class RequestManager:
    BASE_URL = "https://httpbin.org"
    SESSION = None

    headers = HttpBinHeaders()

    async def initialize_manager(self):
        self.SESSION = aiohttp.ClientSession()


manager = RequestManager()
await manager.initialize_manager()


# loop = asyncio.get_event_loop()
# loop.run_until_complete(HttpBinHeaders().get())
