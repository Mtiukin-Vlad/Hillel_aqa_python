import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from tracking_page import TrackingPage  # импорт страницы


@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new")  # можно раскомментить для headless
    options.add_argument("--start-maximized")

    drv = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield drv
    drv.quit()


@pytest.fixture(scope="session")
def tracking_page(driver):
    """Создаем и возвращаем объект TrackingPage сразу с драйвером."""
    return TrackingPage(driver)


def pytest_addoption(parser):
    parser.addoption("--ttn", action="store", default=None, help="Номер накладной для трекинга")


@pytest.fixture(scope="session")
def ttn(request):
    value = request.config.getoption("--ttn")
    return value or "20451117746596"
