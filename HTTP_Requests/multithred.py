from timer import time
from concurrent.futures import ThreadPoolExecutor
import requests

URL = 'https://httpbin.org/uuid'


def fetch(session, url):
    with session.get(url) as response:
        print(response.json()['uuid'])


@time(1, 1)
def main():
    if __name__ == '__main__':
        with ThreadPoolExecutor(max_workers=100) as executor:
            with requests.Session() as session:
                executor.map(fetch, [session] * 100, [URL] * 100)
                executor.shutdown(wait=True)
