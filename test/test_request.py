import pytest
import requests
import redis
from .values import *


## Проверка доступности сервисов
def test_auth_center_connect():
    r = requests.get(f'{AUTH_CENTER}/ping')
    assert r.status_code == 200


def test_web_backend_connect():
    r = requests.get(f'{WEB_BACKEND}/ping')
    assert r.status_code == 200


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


#


## Проверка соединений NGINX
def test_nginx_auth_center():
    r = requests.get(f'{NGINX}/ping/auth-center')
    assert r.status_code == 200


def test_nginx_web_backend():
    r = requests.get(f'{NGINX}/ping/auth-backend')
    assert r.status_code == 200


def test_nginx_redis():
    r = requests.get(f'{NGINX}/ping/redis')
    assert r.status_code == 200
#
