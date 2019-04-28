import requests

from .values import *


def test_nginx_auth_center():
    r = requests.get(f'{NGINX}/ping/auth-center', verify=False)
    assert r.status_code == 200
    assert r.text.strip() == 'auth_center'


def test_nginx_web_backend():
    r = requests.get(f'{NGINX}/ping/web-backend', verify=False)
    assert r.status_code == 200
    assert r.text.strip() == 'web_backend'


def test_nginx_redis():
    r = requests.get(f'{NGINX}/ping/redis', verify=False)
    assert r.status_code == 200
    assert r.text.strip() == 'redis_pong'


def test_auth_center_proxy_pass():
    r = requests.get(f'{NGINX}/auth/ping-redis', verify=False)
    assert r.status_code == 200

    r = requests.get(f'{NGINX}/check-jwt', verify=False)
    assert r.status_code != 404

    r = requests.get(f'{NGINX}/refresh-token', verify=False)
    assert r.status_code != 404

    r = requests.get(f'{NGINX}/login', verify=False)
    assert r.status_code != 404

    r = requests.get(f'{NGINX}/logout', verify=False)
    assert r.status_code != 404


def test_web_backend_proxy_pass():
    r = requests.get(f'{NGINX}/', verify=False)
    assert r.status_code == 200
    assert r.text.strip() == 'web_backend'

    r = requests.get(f'{NGINX}/get-data', verify=False)
    assert r.status_code == 200
