import asyncio

from timer import time
import aiohttp

URL = 'https://httpbin.org/uuid'


async def fetch(session, url):
    async with session.get(url) as response:
        json_response = await response.json()
        print(json_response['uuid'])


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, URL) for _ in range(100)]
        await asyncio.gather(*tasks)


@time(1, 1)
def func():
    asyncio.get_event_loop().run_until_complete(main())
