from aiohttp import web

routes = web.RouteTableDef()


@routes.get('/ping')
async def ping(request):
    return web.Response(text="web_backend")


@routes.get('/get-data')
async def get_data(request):
    return web.Response(text="get_data")


@routes.get('/auth-request')
async def auth_request(request):
    _auth = request.headers.get('Authentication')
    return web.Response(status=200 if _auth != 'Anonymous' else 403, text=_auth)


@routes.get('/')
async def index(request):
    return web.Response(text="web_backend")

app = web.Application()
app.add_routes(routes)
web.run_app(app, port=80)
