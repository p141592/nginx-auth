from aiohttp import web

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


@routes.get('/ping')
async def ping(request):
    return web.Response(text="auth_center")

@routes.get('/ping_redis')
async def ping(request):
    return web.Response(text="auth_center")
    # Create Redis connection
    connection = yield from asyncio_redis.Connection.create(host='127.0.0.1', port=6379)

    # Set a key
    yield from connection.set('my_key', 'my_value')

    # When finished, close the connection.
    connection.close()
    
app = web.Application()
app.add_routes(routes)
web.run_app(app)
