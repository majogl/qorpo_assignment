Run with following command to run as a gunicorn server from folder server_example
gunicorn "app:app()" -b 0.0.0.0:8000 -k aiohttp.worker.GunicornWebWorker

simply run app.py to run as regular aiohttp server
