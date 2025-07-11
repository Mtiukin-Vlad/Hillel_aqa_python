import pytest
import requests
from requests.auth import HTTPBasicAuth
import logging

# Настраиваем логирование один раз (можно сделать и тут, чтобы не дублировать)
logger = logging.getLogger('test_logger')
if not logger.hasHandlers():
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    file_handler = logging.FileHandler('test_search.log', mode='w')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

BASE_URL = "http://127.0.0.1:8080"


@pytest.fixture(scope='class')
def auth_session():
    session = requests.Session()
    auth_response = session.post(
        f"{BASE_URL}/auth",
        auth=HTTPBasicAuth('test_user', 'test_pass')
    )
    assert auth_response.status_code == 200, "Аутентифікація не вдалася"
    access_token = auth_response.json().get('access_token')
    assert access_token is not None, "Токен доступу не отримано"
    session.headers.update({'Authorization': 'Bearer ' + access_token})

    logger.info("Аутентифікація пройшла успішно, токен додано в заголовки")

    yield session  # вернули обʼєкт сесії для використання в тестах

    session.close()
    logger.info("Сесію закрив")
