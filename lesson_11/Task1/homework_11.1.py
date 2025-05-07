import csv


#функція, яка приймає список файлів і об'єднує їх в один
def merge_csv_files(file_list, output_file='result_Matiukhin.csv'):
    # Створюю множину для унікальних рядків
    rows = set()

    # Відкриваю кожен файл і зчитую рядки
    for file in file_list:
        with open(file, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                rows.add(tuple(row))  # додаю кортеж, бо множина не підтримує списки

    # Я зберігаю результат у новий файл
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for row in sorted(rows):
            writer.writerow(row)


# Викликаю функцію, передаючи список файлів
merge_csv_files(['random.csv', 'random-michaels.csv'])
