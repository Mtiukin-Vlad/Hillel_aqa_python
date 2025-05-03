import os
import xml.etree.ElementTree as ET
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
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Шукаю всі елементи group і перевіряємо їх number
        for group in root.findall('group'):
            number = group.find('number').text
            if number == group_number:
                timing = group.find('timingExbytes/incoming')
                if timing is not None:
                    logging.info(f"Значення для group/number {group_number}: {timing.text}")
                    return timing.text
        logging.info(f"Група з номером {group_number} не знайдена.")
    except Exception as e:
        logging.error(f"Помилка при обробці XML файлу: {str(e)}")

# Вказую шлях до XML файлу
file_path = r'C:\Users\Vlad\PycharmProjects\Python_hillel\Hillel_aqa_python\lesson_11\Task3\groups.xml'

# Запускаємо пошук по групі з номером
search_group_by_number(file_path, '1')  # Замість '1' вказати потрібний номер групи
