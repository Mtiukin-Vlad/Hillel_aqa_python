import pytest
import requests
from requests.auth import HTTPBasicAuth
import logging

# Налаштовую логування в консоль і файл
logger = logging.getLogger('test_logger')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Лог у файл
file_handler = logging.FileHandler('test_search.log', mode='w')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Лог у консоль
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

BASE_URL = "http://127.0.0.1:8080"


@pytest.fixture(scope='class')
def auth_session(request):
    session = requests.Session()
    # Роблю логін
    auth_response = session.post(
        f"{BASE_URL}/auth",
        auth=HTTPBasicAuth('test_user', 'test_pass')
    )
    assert auth_response.status_code == 200, "Аутентифікація не вдалася"
    access_token = auth_response.json().get('access_token')
    assert access_token is not None, "Токен доступу не отримано"
    session.headers.update({'Authorization': 'Bearer ' + access_token})

    logger.info("Аутентифікація пройшла успішно, токен додано в заголовки")
    request.cls.session = session
    yield
    session.close()
    logger.info("Сесію закрив")


@pytest.mark.usefixtures("auth_session")
class TestCarSearch:

    @pytest.mark.parametrize(
        "sort_by, limit",
        [
            ("price", 5),
            ("year", 3),
            ("brand", 7),
            ("engine_volume", 4),
            ("price", 10),
            (None, 5),  # без сортування
            ("year", None),  # без ліміту
        ]
    )
    def test_search_cars(self, sort_by, limit):
        params = {}
        if sort_by is not None:
            params['sort_by'] = sort_by
        if limit is not None:
            params['limit'] = limit

        logger.info(f"Відправляю GET /cars з параметрами: {params}")
        response = self.session.get(f"{BASE_URL}/cars", params=params)
        logger.info(f"Статус відповіді: {response.status_code}")
        assert response.status_code == 200

        cars = response.json()
        logger.info(f"Отримано {len(cars)} машин")

        # Перевіряю ліміт (якщо вказано)
        if limit is not None:
            assert len(cars) <= limit

        # Перевіряю сортування (якщо вказано)
        if sort_by:
            # Перевіряю, що список відсортований за sort_by
            values = [car[sort_by] for car in cars]
            assert values == sorted(values), f"Список не відсортований за {sort_by}"
