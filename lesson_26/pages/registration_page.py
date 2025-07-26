from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from . import registration_locators as loc

class RegistrationPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        self.driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")

    def open_signup_form(self):
        self.wait.until(EC.element_to_be_clickable(loc.SIGNUP_BUTTON)).click()

    def fill_form(self, name, lastname, email, password, repeatPassword):
        self.wait.until(EC.visibility_of_element_located(loc.NAME_INPUT))
        self.driver.find_element(*loc.NAME_INPUT).send_keys(name)
        self.driver.find_element(*loc.LASTNAME_INPUT).send_keys(lastname)
        self.driver.find_element(*loc.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*loc.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*loc.REPASSWORD_INPUT).send_keys(repeatPassword)

    def submit(self):
        self.driver.find_element(*loc.SUBMIT_BUTTON).click()

    def get_success_text(self):
        return self.wait.until(EC.visibility_of_element_located(loc.SUCCESS_TEXT)).text
