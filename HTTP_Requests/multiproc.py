from timer import time
from multiprocessing.pool import Pool
import requests

URL = 'https://httpbin.org/uuid'


def fetch(session, url):
    with session.get(url) as response:
        print(response.json()['uuid'])


@time(1, 1)
def main():
    if __name__ == '__main__':
        with Pool() as pool:
            with requests.Session() as session:
                pool.starmap(fetch, [(session, URL) for _ in range(100)])
