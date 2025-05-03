import os
import json
import logging

# Налаштування логера
logging.basicConfig(
    filename=r'json__ivanov.log',  # Вказую шлях до лог-файлу
    level=logging.INFO,  # Встановлюю рівень логування на INFO
    format='%(asctime)s - %(levelname)s - %(message)s',  # Формат логування
    encoding='utf-8'  # Вказую кодування для коректного збереження кирилиці
)

def validate_json_file(file_path):
    """Функція для перевірки валідності JSON файлу."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            json.load(file)  # Спробую завантажити JSON. Якщо не валідний, виникне помилка
        logging.info(f"Файл {file_path} успішно перевірений.")
    except json.JSONDecodeError as e:
        # Якщо виникає помилка при парсингу JSON, записую помилку в лог
        logging.error(f"Невалідний JSON файл: {file_path} - {str(e)}")
    except Exception as e:
        # Якщо сталася інша помилка при відкритті файлу, також записую в лог
        logging.error(f"Помилка при відкритті файлу {file_path}: {str(e)}")

def validate_json_in_directory(directory_path):
    """Функція для перевірки всіх файлів в зазначеній папці."""
    # Перевіряю, чи існує директорія
    if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
        logging.error(f"Директорія не знайдена або не є папкою: {directory_path}")
        return

    # Переглядаю всі файли в директорії
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path) and filename.endswith('.json'):  # Перевіряю лише .json файли
            validate_json_file(file_path)  # Перевіряю кожен файл на валідність


# Вказую шлях до папки з файлами
directory_path = r'C:\Users\Vlad\PycharmProjects\Python_hillel\Hillel_aqa_python\lesson_11\Task2'

# Запускаю перевірку файлів в зазначеній папці
validate_json_in_directory(directory_path)
