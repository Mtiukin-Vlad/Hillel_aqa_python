from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TrackingPage:
    """описую сторінку трекінгу НП та всі дії, які мені потрібні в тестах."""

    URL = "https://tracking.novaposhta.ua/#/uk"

    # Локатори (я зібрав кілька варіантів, бо сайт динамічний і може міняти класи)
    _INPUT_MAIN = (By.CSS_SELECTOR, "input.tracking-input")  # основне поле (часто працює)
    _INPUT_FALLBACK = (By.CSS_SELECTOR, "input[type='text']")  # запасний варіант
    _STATUS_TEXT = (By.CSS_SELECTOR, ".header__status-text")  # текст поточного статусу

    def __init__(self, driver, timeout: int = 15):
        # зберігаю драйвер і таймаут очікувань
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        """відкриваю сторінку трекінгу."""
        self.driver.get(self.URL)

    def _get_input(self):
        """намагаюсь знайти поле вводу номеру ТТН: спочатку основний локатор, потім запасний."""
        try:
            return self.wait.until(EC.presence_of_element_located(self._INPUT_MAIN))
        except Exception:
            return self.wait.until(EC.presence_of_element_located(self._INPUT_FALLBACK))

    def enter_tracking_number(self, number: str):
        """
        ввожу номер накладної в поле і запускаю пошук (Enter).
        Повертаю себе, щоб можна було чейнити виклики.
        """
        field = self._get_input()
        field.clear()
        field.send_keys(number)
        field.send_keys(Keys.ENTER)
        return self

    def get_status(self) -> str:
        """
        чекаю появи блоку зі статусом і повертаю текст (обрізаю пробіли).
        Якщо статус не з’явиться вчасно — впаде виключення (і тест покаже причину).
        """
        el = self.wait.until(EC.visibility_of_element_located(self._STATUS_TEXT))
        return el.text.strip()
