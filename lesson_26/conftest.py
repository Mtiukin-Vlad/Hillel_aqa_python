import pytest
import random
import string
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from pages.registration_page import RegistrationPage


@pytest.fixture(scope="session")
def driver():
    """
    Я відкриваю браузер і переходжу на сайт із логіном і паролем у URL.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    drv = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    drv.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
    yield drv
    drv.quit()


@pytest.fixture()
def open_signup_form(driver):
    """
    Я повертаю функцію, яка натискає на кнопку 'Sign up', щоб відкрити форму реєстрації.
    """
    def _open():
        btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(RegistrationPage.SIGNUP_BUTTON)
        )
        btn.click()
    return _open


@pytest.fixture()
def fill_registration_form(driver):
    """
    повертаю функцію, яка дозволяє мені заповнити форму довільними даними,
    включаючи окремий пароль та повтор пароля.
    """
    def _fill(name, lastname, email, password, repeatPassword):
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationPage.NAME_INPUT)
        )
        driver.find_element(*RegistrationPage.NAME_INPUT).send_keys(name)
        driver.find_element(*RegistrationPage.LASTNAME_INPUT).send_keys(lastname)
        driver.find_element(*RegistrationPage.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationPage.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationPage.REPASSWORD_INPUT).send_keys(repeatPassword)

    return _fill


@pytest.fixture()
def submit_form(driver):
    """
    повертаю функцію, яка натискає кнопку сабміту та завершує процес реєстрації.
    """
    def _submit():
        driver.find_element(*RegistrationPage.SUBMIT_BUTTON).click()
    return _submit


@pytest.fixture()
def random_email():
    """
    генерую унікальний емейл для реєстрації.
    """
    random_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return f"testuser_{random_part}@example.com"
