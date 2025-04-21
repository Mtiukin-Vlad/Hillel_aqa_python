"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import logging

def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.

    status: Статус події входу:

    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """
    log_message = f"Login event - Username: {username}, Status: {status}"

    # Створення та налаштування логера
    logging.basicConfig(
        filename='login_system.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        force=True
    )
    logger = logging.getLogger("log_event")

    # Логування події
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)


class TestPositiveUserLogin:

    # Я перевіряю, що подія з іменем "Vlad" і статусом "success" записується в лог
    def test_success_log(self):
        log_event("Vlad", "success")
        with open('login_system.log', "r") as file:
            content = file.read()
        assert "Username: Vlad, Status: success" in content

    # Я перевіряю, що повне ім’я користувача також правильно логірується
    def test_success_log2(self):
        log_event("Vlad Matiukhin", "success")
        with open('login_system.log', "r") as file:
            content = file.read()
        assert "Username: Vlad Matiukhin, Status: success" in content


class TestNegativeUserLogin:

    # Я перевіряю, що подія з іменем "Vlad" і статусом "expired" правильно записується
    def test_expired_log(self):
        log_event("Vlad", "expired")
        with open('login_system.log', "r") as file:
            content = file.read()
        assert "Username: Vlad, Status: expired" in content

    # Я перевіряю, що подія з порожнім ім’ям також записується у лог як "failed"
    def test_empty_log(self):
        log_event("", "failed")
        with open('login_system.log', "r") as file:
            content = file.read()
        assert "Username: , Status: failed" in content




