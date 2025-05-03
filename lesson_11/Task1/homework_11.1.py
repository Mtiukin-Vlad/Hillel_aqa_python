import csv
import os

# Я задаю шлях до файлів (усі лежать у поточній папці lesson_11)
file1 = 'random.csv'
file2 = 'random-michaels.csv'

# Я створюю множину для унікальних рядків
rows = set()

# Я відкриваю кожен файл і зчитую рядки
for file in [file1, file2]:
    with open(file, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            rows.add(tuple(row))  # додаю кортеж, бо множина не підтримує списки

# Я зберігаю результат у новий файл
with open('result_Matiukhin.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for row in sorted(rows):
        writer.writerow(row)