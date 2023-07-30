from timer import time
import requests

URL = 'https://httpbin.org/uuid'


def fetch(session, url):
    with session.get(url) as response:
        print(response.json()['uuid'])


@time(1, 1)
def main():
    with requests.Session() as session:
        for _ in range(100):
            fetch(session, URL)
