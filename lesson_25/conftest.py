# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def driver():
    """
    піднімаю Chrome через webdriver-manager (щоб не мучитись із версіями),
    відкриваю вікно, віддаю драйвер у тести і потім коректно його закриваю.
    """
    options = webdriver.ChromeOptions()
    # Якщо хочеш бачити браузер — закоментуй headless:
    # options.add_argument("--headless=new")
    options.add_argument("--start-maximized")

    drv = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield drv
    drv.quit()


def pytest_addoption(parser):
    """
    Я додаю в pytest CLI опцію --ttn, щоб можна було передавати номер накладної з командного рядка.
    Приклад: pytest --ttn=20450283809006
    """
    parser.addoption("--ttn", action="store", default=None, help="Номер накладної для трекінгу")


@pytest.fixture(scope="session")
def ttn(request):
    """
    Я повертаю номер накладної, якщо його передали через --ttn.
    Якщо не передали — повертаю тестовий номер (замінити на реальний!).
    """
    value = request.config.getoption("--ttn")
    return value or "20451117746596"  # <--- заміни на свій валідний номер, якщо треба
