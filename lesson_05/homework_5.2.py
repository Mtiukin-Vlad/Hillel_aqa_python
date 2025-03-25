# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

# Список даних про людей (ім'я, прізвище, вік, професія, місце розташування)
people_records: list[tuple[str, str, int, str, str]] = [
    ('John', 'Doe', 28, 'Engineer', 'New York'),
    ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
    ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
    ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
    ('Michael', 'Brown', 22, 'Student', 'Seattle'),
    ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
    ('David', 'Miller', 33, 'Software Developer', 'Austin'),
    ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
    ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
    ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
    ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
    ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
    ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
    ('Ava', 'White', 42, 'Journalist', 'San Diego'),
    ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

# 1 - Add your new record o the beginning of the given list - Рішення
my_new_record: tuple[str, str, str, str, str] = ('Vladyslav', 'Matiukhin', "25", "Qa", "Kishinay")
people_records.insert(0, my_new_record)  # Вставляю новий запис на першу позицію
print(people_records)

# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result - Рішення
people_records[1], people_records[5] = people_records[5], people_records[1]  # Міняю записи місцями
print(people_records)

# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result - Рішення
age_check: list[int] = [6, 10, 13]  # Індекси для перевірки

for age in age_check:
    if people_records[age][2] >= 30:  # Перевіряю вік (індекс 2 - це вік)
        print(people_records[age][2])  # Виводжу вік, якщо він >= 30
