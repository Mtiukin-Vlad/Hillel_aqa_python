# Отримую рядок від користувача
string = input("Введіть строку: ")

# Створюю множину унікальних символів у рядку
unique_chars = set(string)

# Перевіряю, чи кількість унікальних символів більше 10, і виводжу результат
print(len(unique_chars) > 10)