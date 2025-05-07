import xmltodict
import logging

# Налаштування логера з кодуванням
logging.basicConfig(
    filename='xml__search_log.log',  # Вказую шлях до лог-файлу
    level=logging.INFO,  # Встановлюю рівень логування на INFO
    format='%(asctime)s - %(levelname)s - %(message)s',  # Формат логування
    encoding='utf-8'  # Вказую кодування UTF-8
)

def search_group_by_number(file_path, group_number):
    """Функція для пошуку за номером групи та повернення значення timingExbytes/incoming."""
    try:
        with open(file_path, encoding='utf-8') as f:
            data = xmltodict.parse(f.read())  # Я зчитую та парсю XML у словник

        # Я отримую список груп
        groups = data['root']['group']
        if not isinstance(groups, list):  # Якщо лише одна група — обгортаю в список
            groups = [groups]

        # Я перебираю групи і шукаю номер
        for group in groups:
            if group['number'] == group_number:
                incoming = group.get('timingExbytes', {}).get('incoming')
                if incoming:
                    logging.info(f"Значення для group/number {group_number}: {incoming}")
                    return incoming

        logging.info(f"Група з номером {group_number} не знайдена.")
    except Exception as e:
        logging.error(f"Помилка при обробці XML файлу: {str(e)}")

# Вказую шлях до XML файлу
file_path = r'C:\Users\Vlad\PycharmProjects\Python_hillel\Hillel_aqa_python\lesson_11\Task3\groups.xml'

# Запускаю пошук по групі з номером
search_group_by_number(file_path, '1')  # Замість '1' вказати потрібний номер групи
