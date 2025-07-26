
EXPECTED_STATUS = "Отримана"


def test_tracking_status(tracking_page, ttn):
    tracking_page.open()
    tracking_page.enter_tracking_number(ttn)
    actual_status = tracking_page.get_status()
    assert actual_status == EXPECTED_STATUS, (
        f"Очікував статус '{EXPECTED_STATUS}', але отримав '{actual_status}'. "
        f"Використаний номер: {ttn}"
    )
