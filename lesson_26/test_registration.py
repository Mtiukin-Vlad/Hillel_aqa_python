from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.registration_page import RegistrationPage


def test_successful_registration(driver, open_signup_form, fill_registration_form, submit_form, random_email):
    """
    відкриваю форму, заповнюю валідні дані, сабмічу й перевіряю, що реєстрація успішна.
    """
    open_signup_form()  # Я відкриваю форму реєстрації

    fill_registration_form(
        name="Vladyslav",
        lastname="Matiukhin",
        email=random_email,
        password="Q2ZQ3E!sNZfHr45",
        repeatPassword="Q2ZQ3E!sNZfHr45"
    )

    submit_form()  # Я сабмічу форму

    try:
        # Чекаю на повідомлення про успішну реєстрацію
        success = WebDriverWait(driver, 1).until(
            EC.visibility_of_element_located(RegistrationPage.SUCCESS_TEXT)
        )
        assert "registration complete" in success.text.lower()
    except TimeoutException:
        # Якщо повідомлення про успіх не з'явилось — реєстрація вважається неуспішною
        assert False, "Реєстрація неуспішна: повідомлення про успішну реєстрацію не знайдено"
