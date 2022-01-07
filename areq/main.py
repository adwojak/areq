import aiohttp
import asyncio


class RequestSender:
    ENDPOINT = "/"

    async def get(self):
        # TODO Temporary solution - need to move session to manager
        async with aiohttp.ClientSession() as session:
            async with session.get(self.ENDPOINT) as response:
                print(await response.json())
                return response


class HttpBinHeaders(RequestSender):
    ENDPOINT = "https://httpbin.org/headers"
    # ENDPOINT = "/headers"


class RequestManager:
    BASE_URL = "https://httpbin.org"

    headers = HttpBinHeaders()


manager = RequestManager()


loop = asyncio.get_event_loop()
loop.run_until_complete(manager.headers.get())
