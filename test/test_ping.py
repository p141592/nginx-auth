import requests
import redis
from .values import *


def test_auth_center_connect():
    r = requests.get(f'{AUTH_CENTER}/ping')
    assert r.status_code == 200
    assert r.text.strip() == 'auth_center'


def test_web_backend_connect():
    r = requests.get(f'{WEB_BACKEND}/ping')
    assert r.status_code == 200
    assert r.text.strip() == 'web_backend'


def test_redis_connect():
    r = redis.Redis(host=f'{REDIS}', port=6379, db=0)
    result = False
    try:
        result = r.ping()
    except ConnectionError:
        pass

    assert result


def test_nginx_connect():
    """Проверка коннекта до nginx"""
    r = requests.get(f'{NGINX}/ping')
    assert r.status_code == 200
    assert r.text.strip() == 'pong'


def test_auth_center_redis():
    r = requests.get(f'{AUTH_CENTER}/ping-redis')
    assert r.status_code == 200
