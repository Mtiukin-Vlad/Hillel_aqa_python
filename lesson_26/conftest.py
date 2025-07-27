import pytest
import random
import string
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.registration_page import RegistrationPage


@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    drv = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield drv
    drv.quit()


@pytest.fixture()
def registration_page(driver):
    page = RegistrationPage(driver)
    page.open()
    return page


@pytest.fixture()
def random_email():
    random_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return f"testuser_{random_part}@example.com"
