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
    r = requests.get(f'{NGINX}/auth-request', headers={"Authentication": "Anonymous"}, verify=False)
    assert r.status_code == 403

    # Отправка запроса на авторизованный
    r = requests.get(f'{NGINX}/auth-request', headers={"Authentication": "Some"}, verify=False)
    assert r.status_code == 200


def test_get_payload():
    # Отправка запроса на получение JWT
    r = requests.post(
        f'{NGINX}/auth/authentication',
        json={"auth-type": "password", "data": {"username": "username", "password": "bad"}}, verify=False
    )
    assert r.status_code == 403

    r = requests.post(
        f'{NGINX}/auth/authentication',
        json={"auth-type": "password", "data": {"username": "username", "password": "good"}}, verify=False
    )
    assert r.status_code == 200
