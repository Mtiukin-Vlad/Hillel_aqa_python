import datetime

# Я відкриваю файл hblog.txt для зчитування всіх рядків
with open("hblog.txt", "r") as file:
    log_lines = file.readlines()

# Я створюю список для збереження лише тих рядків, які містять потрібний ключ
filtered_log = []
for line in log_lines:
    if "Key TSTFEED0300|7E3E|0400" in line:
        filtered_log.append(line)

# Я створюю список для збереження часу з кожного відфільтрованого рядка
timestamps = []
for line in filtered_log:
    # Я знаходжу позицію слова "Timestamp "
    idx = line.find("Timestamp ")
    if idx != -1:
        # Я виділяю час після слова "Timestamp "
        time_str = line[idx + len("Timestamp "): idx + len("Timestamp ") + 8]
        # Я перетворюю цей рядок у формат часу datetime
        time_obj = datetime.datetime.strptime(time_str, "%H:%M:%S")
        timestamps.append(time_obj)

# Я відкриваю файл hb_test.log для запису результатів перевірки
with open("hb_test.log", "w") as log_file:
    # Я проходжу по кожній парі сусідніх часових міток
    for i in range(len(timestamps) - 1):
        t1 = timestamps[i]
        t2 = timestamps[i + 1]
        # Я обчислюю різницю в секундах між сусідніми часовими мітками
        delta = (t1 - t2).total_seconds()
        if delta < 0:
            # Якщо перший час менший, я додаю 24 години (для переходу через північ)
            delta += 24 * 3600

        # Я визначаю рівень повідомлення для логів (WARNING чи ERROR)
        if 31 < delta < 33:
            log_file.write(f"WARNING at {filtered_log[i]}Heartbeat delta: {delta} seconds\n")
        elif delta >= 33:
            log_file.write(f"ERROR at {filtered_log[i]}Heartbeat delta: {delta} seconds\n")
        # Якщо різниця менше або дорівнює 31 секунді, я нічого не записую

# Я повідомляю, що аналіз завершено
print("Аналіз завершено. Результати записані у файл hb_test.log")
