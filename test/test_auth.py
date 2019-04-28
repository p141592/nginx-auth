import json

import requests

from .values import *

# Авторизованный метод с JWT
# refresh JWT и запрос со старым JWT
# Запрос с новым JWT
# logout и авторизованный метод c JWT
# Не авторизованный запрос по всем 3мя JWT


def test_auth_request():
    # Отправка запроса на не авторизованный URL
    r = requests.get(f'{NGINX}/auth_request', headers={"Authentication": "Anonymous"})
    assert r.status_code == 403

    # Отправка запроса на авторизованный
    r = requests.get(f'{NGINX}/auth_request', headers={"Authentication": "Some"})
    assert r.status_code == 200


def test_get_jwt():
    # Отправка запроса на получение JWT
    r = requests.post(f'{NGINX}/auth/login', json=json.dumps({"username": "test", "password": "bad"}))
    assert r.status_code == 403

    r = requests.post(f'{NGINX}/auth/login', json=json.dumps({"username": "test", "password": "good"}))
    assert r.status_code == 200
    _jwt = r.json()
    print(_jwt)

