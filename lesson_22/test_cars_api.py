import pytest
import logging

logger = logging.getLogger('test_logger')

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
    def test_search_cars(self, auth_session, sort_by, limit):
        params = {}
        if sort_by is not None:
            params['sort_by'] = sort_by
        if limit is not None:
            params['limit'] = limit

        logger.info(f"Відправляю GET /cars з параметрами: {params}")
        response = auth_session.get(f"http://127.0.0.1:8080/cars", params=params)
        logger.info(f"Статус відповіді: {response.status_code}")
        assert response.status_code == 200

        cars = response.json()
        logger.info(f"Отримано {len(cars)} машин")

        # Перевіряю ліміт (якщо вказано)
        if limit is not None:
            assert len(cars) <= limit

        # Перевіряю сортування (якщо вказано)
        if sort_by:
            values = [car[sort_by] for car in cars]
            assert values == sorted(values), f"Список не відсортований за {sort_by}"
