from typing import List

from aiohttp import web


class Book:
    def __init__(self, name: str, pages: int):
        self.name = name
        self.pages = pages

    def __str__(self):
        return f"{self.name}: {self.pages}"


BOOKS: List[Book] = []


async def base_handler(request: web.Request):
    data = "Hello World"
    return web.Response(text=data, status=200)


async def post_handler(request: web.Request):
    json_params = await request.json()
    if "name" not in json_params or "pages" not in json_params:
        return web.Response(text='No "name" or "pages" params in request!', status=400)
    try:
        pages = int(json_params["pages"])
        name = str(json_params["name"])
        BOOKS.append(Book(name, pages))
        return web.Response(text='OK!', status=200)
    except ValueError:
        return web.Response(text='Page bilo ne chislom!', status=400)


async def get_books(request: web.Request):
    return web.Response(text=str([str(book) for book in BOOKS]), status=200)


async def delete_handler(request: web.Request):
    json_params = await request.json()
    if "name" not in json_params:
        return web.Response(text='No "name" param in json!', status=400)
    try:
        for i in range(len(BOOKS) - 1, -1, -1):
            if BOOKS[i].name == str(json_params["name"]):
                # del BOOKS[i]  # Удалят что угодно
                BOOKS.pop(i)  # То же самое, но красиво.
        return web.Response(text='OK!', status=200)
    except ValueError:
        return web.Response(text='name was not string!', status=400)


async def put_handler(request: web.Request):
    json_params = await request.json()
    if "name" not in json_params and "pages" not in json_params:
        return web.Response(text='No "name" or "pages" param in json!', status=400)
    try:
        pages = int(json_params["pages"])
        for book in BOOKS:
            if book.name == str(json_params["name"]):
                book.pages = pages
        return web.Response(text='OK!', status=200)
    except ValueError:
        return web.Response(text='name supposed to be string and pages supposed to be int', status=400)


app = web.Application()
app.add_routes([web.post('/books', post_handler),
                web.get('/books', get_books),
                web.delete('/books', delete_handler),
                web.put('/books', put_handler)
                ])
web.run_app(app, host="127.0.0.1", port=8080)
