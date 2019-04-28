import requests

from .values import *


def test_nginx_auth_center():
    r = requests.get(f'{NGINX}/ping/auth-center')
    assert r.status_code == 200
    assert r.text.strip() == 'auth_center'


def test_nginx_web_backend():
    r = requests.get(f'{NGINX}/ping/web-backend')
    assert r.status_code == 200
    assert r.text.strip() == 'web_backend'


def test_nginx_redis():
    r = requests.get(f'{NGINX}/ping/redis')
    assert r.status_code == 200
    assert r.text.strip() == 'redis_pong'


def test_auth_center_proxy_pass():
    r = requests.get(f'{NGINX}/auth/')
    assert r.status_code == 200
    assert r.text.strip() == 'auth_center index'

    r = requests.get(f'{NGINX}')
    assert r.status_code == 200
    assert r.text.strip() == 'web_backend index'

    r = requests.get(f'{NGINX}/auth/ping_redis')
    assert r.status_code == 200

    r = requests.get(f'{NGINX}/auth/check_jwt')
    assert r.status_code != 404

    r = requests.get(f'{NGINX}/auth/refresh_token')
    assert r.status_code != 404

    r = requests.get(f'{NGINX}/auth/login')
    assert r.status_code != 404

    r = requests.get(f'{NGINX}/auth/logout')
    assert r.status_code != 404


def test_web_backend_proxy_pass():
    r = requests.get(f'{NGINX}/get_data')
    assert r.status_code == 200
    assert r.text.strip() == 'web_backend'

    r = requests.get(f'{NGINX}/auth_request', headers={"Authentication": "Anonymous"})
    assert r.status_code == 403

    r = requests.get(f'{NGINX}/auth_request', headers={"Authentication": "Some"})
    assert r.status_code == 200
