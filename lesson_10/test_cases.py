import os
import logging
from homework_10 import log_event

LOG_FILE = 'login_system.log'

class TestUserLogin:

    def test_success_log(self):
        log_event("Vlad", "success")
        with open(LOG_FILE, "r") as file:
            content = file.read()
        assert "Username: Vlad" in content
        assert "Status: success" in content
        assert "INFO" in content

    def test_expired_log(self):
        log_event("Vlad", "expired")
        with open(LOG_FILE, "r") as file:
            content = file.read()
        assert "Username: Vlad" in content
        assert "Status: expired" in content
        assert "WARNING" in content

    def test_empty_username_failed(self):
        log_event("", "failed")
        with open(LOG_FILE, "r") as file:
            content = file.read()
        assert "Username: " in content
        assert "Status: failed" in content
        assert "ERROR" in content
