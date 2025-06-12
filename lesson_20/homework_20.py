import logging
from datetime import datetime

# Налаштовую логер: записую WARNING і ERROR у файл hb_test.log
logging.basicConfig(
    filename='hb_test.log',
    level=logging.WARNING,
    format='%(levelname)s:%(asctime)s:%(message)s',
    datefmt='%H:%M:%S',
    encoding='utf-8'  # Вказую кодування UTF-8
)

def read_log_file(filename, key):
    """Читаю лог-файл і вибираю рядки, де є потрібний ключ"""
    filtered_lines = []
    with open(filename, 'r') as file:
        for line in file:
            if key in line:
                filtered_lines.append(line.strip())
    return filtered_lines

def parse_timestamp(line):
    """Знаходжу в рядку час (Timestamp) і конвертую його у datetime"""
    pos = line.find("Timestamp ")
    if pos == -1:
        return None
    time_str = line[pos + 10:pos + 18]  # Витягаю час у форматі HH:MM:SS
    try:
        return datetime.strptime(time_str, "%H:%M:%S")
    except ValueError:
        return None

def analyze_heartbeat(lines):
    """Перевіряю різницю між сусідніми timestamp і логую попередження/помилки"""
    for i in range(len(lines) - 1):
        time_current = parse_timestamp(lines[i])
        time_next = parse_timestamp(lines[i + 1])
        if not time_current or not time_next:
            continue  # Якщо час не парситься — пропускаю

        diff = (time_current - time_next).total_seconds()

        # Логую WARNING, якщо інтервал 31 < heartbeat < 33 секунд
        if 31 < diff < 33:
            logging.warning(f'Затримка heartbeat {diff:.2f} секунд о {time_current.strftime("%H:%M:%S")}')
        # Логую ERROR, якщо інтервал >= 33 секунд
        elif diff >= 33:
            logging.error(f'ПОМИЛКА! Затримка heartbeat {diff:.2f} секунд о {time_current.strftime("%H:%M:%S")}')

def main():
    """Основна функція запуску: читаю лог, аналізую heartbeat"""
    key = "TSTFEED0300|7E3E|0400"
    filename = 'hblog.txt'

    print("Починаю аналіз логів...")
    lines = read_log_file(filename, key)
    analyze_heartbeat(lines)
    print("Аналіз завершено. Результати у файлі hb_test.log")

if __name__ == '__main__':
    main()
