from aiohttp import web
import ccxt
import asyncpg

routes = web.RouteTableDef()

@routes.get('/price/{currency}')
async def get_price(request):
    """
    make request to get {currency} info from online resource, parse
    and save it to db

    Kedze nemam API kluc a vytvarat si tam ucet sa mi nepodarilo aby som 
    ho vygeneroval bez toho aby som tam dal info o sebe ktore tam dat nechcem,
    nemozem toto bohuzial zaradit do kodu.

    kucoin = getattr(ccxt, "kucoin")()
    kucoin.apiKey = API_KEY
    orders = kucoin.fetchOpenOrders(f"{request.match_info["currency"]}/USDT")

    async with asyncpg.create_pool
    """
    async with asyncpg.create_pool("postgres://postgres:password@0.0.0.0:5432/test") as pool:
        async with pool.acquire() as conn:
            for order in orders:
                await conn.execute(f"""
                INSERT INTO currencies(currency, date_, price)
                VALUES({order["currency"].split('/')[0]}, {order["timestamp"]}, {order["price"]})
                """)
    pass

@routes.get('/price/history?page={page}')
async def get_history(request):
    """
    display records from database in groups of {page}
    if {page} is not defined, use 10 as default

    simple SQL query, 
    f"SELECT * FROM currencies, LIMIT 10, OFFSET {request.match_info["page"]} * 10"
    """
    pass

@routes.delete('/price/history')
async def delete_all_records(request):
    """
    deletes all records in database
    
    again, just a query
    DELETE FROM currencies
    """
    pass

