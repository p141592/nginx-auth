import asyncio
from aiohttp import web
import aioredis

routes = web.RouteTableDef()


USERS = dict(
    username=dict(
        id="1",
        password="good",
        name="Name"
    )
)


def get_payload(user):
    return user


@routes.get('/ping')
async def ping(request):
    return web.Response(text="auth_center")


@routes.get('/ping-redis')
async def ping_redis(request):
    conn = await aioredis.create_connection('redis://redis', loop=asyncio.get_event_loop())
    val = await conn.execute('PING')
    conn.close()
    await conn.wait_closed()
    return web.Response(status=200 if val else 500, text='')


@routes.post('/authentication')
async def authentication(request):
    # {"auth-type": "password", "data": {"username": "", "password": ""}}
    data = await request.json()
    data = data.get('data')
    _user = USERS.get(data.get('username'))
    _login = _user.get('password') == data.get('password')
    if _user.get('password') != data.get('password'):
        return web.json_response(status=403)

    return web.json_response(data=get_payload(_user), status=200)


@routes.get('/check-user')
async def check_user(request):
    # Берем Authentication заголовок
    # Разбираем его
    #
    return web.json_response()


@routes.get('/')
async def index(request):
    return web.Response(text="auth_center")

app = web.Application()
app.add_routes(routes)
web.run_app(app, port=80)
