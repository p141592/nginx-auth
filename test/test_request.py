import os
import requests

e = os.environ.get


def test_head():
    """Проверка создержания заголовка запроса
    Проверка подмены токена на ID пользователя"""


def test_nginx_connect():
    """Проверка nginx"""

    r = requests.get(f'http://{e("NGINX")}:8000')
    assert r.status_code == 200
