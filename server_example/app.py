import asyncio
from aiohttp import web

from handlers import routes

def app():
    app = web.Application()
    app.add_routes(routes)
    return app

if __name__ == '__main__':
    web.run_app(app())