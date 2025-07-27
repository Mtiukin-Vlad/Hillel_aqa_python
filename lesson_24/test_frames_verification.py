import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

def test_frame_verification(selenium_driver_elements):
    # Відкриваю головну сторінку з фреймами
    selenium_driver_elements.get("http://localhost:8000/dz.html")

    # Перехід у перший фрейм
    selenium_driver_elements.switch_to.frame("frame1")
    selenium_driver_elements.find_element(By.ID, "input1").send_keys("Frame1_Secret")
    selenium_driver_elements.find_element(By.TAG_NAME, "button").click()

    time.sleep(1)  # Даємо час алерту з’явитись
    alert = Alert(selenium_driver_elements)
    assert alert.text == "Верифікація пройшла успішно!"
    alert.accept()

    # Назад у головну сторінку
    selenium_driver_elements.switch_to.default_content()

    # Перехід у другий фрейм
    selenium_driver_elements.switch_to.frame("frame2")
    selenium_driver_elements.find_element(By.ID, "input2").send_keys("Frame2_Secret")
    selenium_driver_elements.find_element(By.TAG_NAME, "button").click()

    time.sleep(1)
    alert = Alert(selenium_driver_elements)
    assert alert.text == "Верифікація пройшла успішно!"
    alert.accept()
