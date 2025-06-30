from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_frame_verification():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://localhost:8000/dz.html")

    # Перехід у перший фрейм
    driver.switch_to.frame("frame1")
    input1 = driver.find_element(By.ID, "input1")
    input1.send_keys("Frame1_Secret")
    driver.find_element(By.TAG_NAME, "button").click()

    alert = Alert(driver)
    time.sleep(1)
    assert alert.text == "Верифікація пройшла успішно!"
    alert.accept()

    # Назад у головну сторінку
    driver.switch_to.default_content()

    # Перехід у другий фрейм
    driver.switch_to.frame("frame2")
    input2 = driver.find_element(By.ID, "input2")
    input2.send_keys("Frame2_Secret")
    driver.find_element(By.TAG_NAME, "button").click()

    alert = Alert(driver)
    time.sleep(1)
    assert alert.text == "Верифікація пройшла успішно!"
    alert.accept()

    driver.quit()
