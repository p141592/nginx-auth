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
    return web.Response(text="web_backend")


app = web.Application()
app.add_routes(routes)
web.run_app(app)
