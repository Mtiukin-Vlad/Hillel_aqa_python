from selenium.webdriver.common.by import By

SIGNUP_BUTTON = (By.XPATH, "//button[text()='Sign up']")

NAME_INPUT = (By.NAME, "name")
LASTNAME_INPUT = (By.NAME, "lastName")
EMAIL_INPUT = (By.NAME, "email")
PASSWORD_INPUT = (By.NAME, "password")
REPASSWORD_INPUT = (By.NAME, "repeatPassword")
SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Register')]")
SUCCESS_TEXT = (By.CSS_SELECTOR, "div.alert.alert-success")
