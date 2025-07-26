import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

def test_frame_verification(driver):
    # Відкриваю головну сторінку з фреймами
    driver.get("http://localhost:8000/dz.html")

    # Перехід у перший фрейм
    driver.switch_to.frame("frame1")
    driver.find_element(By.ID, "input1").send_keys("Frame1_Secret")
    driver.find_element(By.TAG_NAME, "button").click()

    time.sleep(1)  # Даємо час алерту з’явитись
    alert = Alert(driver)
    assert alert.text == "Верифікація пройшла успішно!"
    alert.accept()

    # Назад у головну сторінку
    driver.switch_to.default_content()

    # Перехід у другий фрейм
    driver.switch_to.frame("frame2")
    driver.find_element(By.ID, "input2").send_keys("Frame2_Secret")
    driver.find_element(By.TAG_NAME, "button").click()

    time.sleep(1)
    alert = Alert(driver)
    assert alert.text == "Верифікація пройшла успішно!"
    alert.accept()
