import chromedriver_autoinstaller
import pytest
from selenium import webdriver

@pytest.fixture
def selenium_driver_elements():
    # Ініціалізація веб-драйвера для Chrome
    driver = webdriver.Chrome()

    # # Відкриття веб-сторінки
    driver.get('http://localhost:8000/elements.html')

    yield driver

    # Закриття браузера
    driver.quit()
