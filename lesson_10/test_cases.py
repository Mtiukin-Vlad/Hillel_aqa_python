import os
import logging
from homework_10 import log_event

LOG_FILE = 'login_system.log'

class TestPositiveUserLogin:

    def test_success_log(self):
        log_event("Vlad", "success")
        with open(LOG_FILE, "r") as file:
            content = file.read()
        assert "Username: Vlad, Status: success" in content

    def test_success_log_full_name(self):
        log_event("Vlad Matiukhin", "success")
        with open(LOG_FILE, "r") as file:
            content = file.read()
        assert "Username: Vlad Matiukhin, Status: success" in content


class TestNegativeUserLogin:

    def test_expired_log(self):
        log_event("Vlad", "expired")
        with open(LOG_FILE, "r") as file:
            content = file.read()
        assert "Username: Vlad, Status: expired" in content

    def test_empty_username_failed(self):
        log_event("", "failed")
        with open(LOG_FILE, "r") as file:
            content = file.read()
        assert "Username: , Status: failed" in content
