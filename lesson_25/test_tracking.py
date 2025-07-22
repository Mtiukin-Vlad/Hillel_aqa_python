import pytest
from tracking_page import TrackingPage

EXPECTED_STATUS = "Отримана"


def test_tracking_status(driver, ttn):
    """
    відкриваю сторінку трекінгу, вводжу номер накладної, отримую статус
    і перевіряю, що він відповідає очікуваному.
    """
    page = TrackingPage(driver)
    page.open()
    page.enter_tracking_number(ttn)
    actual_status = page.get_status()
    assert actual_status == EXPECTED_STATUS, (
        f"Очікував статус '{EXPECTED_STATUS}', але отримав '{actual_status}'. "
        f"Використаний номер: {ttn}"
    )
