import asyncio
from aiohttp import web
import aioredis

routes = web.RouteTableDef()


# Auth Center
# Имеет подключение к REDIS
#
# Занимается:
#
# выдачей/проверкой/обновлением JWT
# Xранит базу пользователей
# Регистрирует новых пользователей
# Форма авторизации по паролю
# Авторизация по одноразовому коду
# Авторизация по oauth
# Содержит механику обмена Oauth токена на данные пользователя
# Методы:
# check_jwt
#
# Получает JWT, разбирает его, проверяет статус пользователя, возвращает результат
#
# refresh_token
#
# Принимает refresh token и JWT. Проверяет JWT на blacklist Генерирует новый. Старый отправляет в blacklist с expired == его времени жизни Новый -- в whitelist по времени его жизни
#
# logout
#
# Принимает JWT, кладет его в blacklist
#
# login
#
# Генерирует JWT/refresh token, кладет его в whitelist

USERS = dict(
    test="good"
)


@routes.get('/ping')
async def ping(request):
    return web.Response(text="auth_center")


@routes.get('/ping_redis')
async def ping_redis(request):
    conn = await aioredis.create_connection('redis://redis', loop=asyncio.get_event_loop())
    val = await conn.execute('PING')
    conn.close()
    await conn.wait_closed()
    return web.Response(status=200 if val else 500, text='')


@routes.get('/check_jwt')
async def check_jwt(request):
    # Разобрать JWT, проверить пользователя

    return web.Response(text="auth_center")


@routes.get('/refresh_token')
async def refresh_token(request):
    # Проверить refresh_token
    # Отправить старый JWT в blacklist
    # Положить новый JWT в whitelist
    return web.Response(text="refresh_token")


@routes.get('/login')
async def login(request):
    # Создать JWT/refresh_token
    # Положить JWT в whitelist
    return web.Response(text="login")


@routes.get('/logout')
async def logout(request):
    # Положить JWT в blacklist
    data = await request.json()
    print(data)
    return web.Response(text="logout")


@routes.get('/')
async def index(request):
    return web.Response(text="auth_center")

app = web.Application()
app.add_routes(routes)
web.run_app(app, port=80)
