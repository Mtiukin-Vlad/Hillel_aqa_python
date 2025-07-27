from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import STATUS_TEXT_LABEL, INPUT_FALLBACK, STATUS_TEXT_LABEL

class TrackingPage:
    URL = "https://tracking.novaposhta.ua/#/uk"

    def __init__(self, driver, timeout: int = 15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        self.driver.get(self.URL)

    def _get_input(self):
        try:
            return self.wait.until(EC.presence_of_element_located(STATUS_TEXT_LABEL))
        except Exception:
            return self.wait.until(EC.presence_of_element_located(INPUT_FALLBACK))

    def enter_tracking_number(self, number: str):
        field = self._get_input()
        field.clear()
        field.send_keys(number)
        field.send_keys(Keys.ENTER)
        return self

    def get_status(self) -> str:
        el = self.wait.until(EC.visibility_of_element_located(STATUS_TEXT_LABEL))
        return el.text.strip()
