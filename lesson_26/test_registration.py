from selenium.common.exceptions import TimeoutException

def test_successful_registration(registration_page, random_email):
    registration_page.open_signup_form()
    registration_page.fill_form(
        name="Vladyslav",
        lastname="Matiukhin",
        email=random_email,
        password="Q2ZQ3E!sNZfHr45",
        repeatPassword="Q2ZQ3E!sNZfHr45"
    )
    registration_page.submit()
    try:
        text = registration_page.get_success_text()
        assert "registration complete" in text.lower()
    except TimeoutException:
        assert False, "Реєстрація неуспішна: повідомлення про успішну реєстрацію не знайдено"
