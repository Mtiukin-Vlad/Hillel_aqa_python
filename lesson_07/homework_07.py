# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= number:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > "25":
            # Enter the action to take if the result is greater than 25
            pass
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multi += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

# Рішення завданя №1
def multiplication_table(number: int) -> None:
    # Ініціалізація множника
    multiplier = 1

    # Умова циклу була неправильною (треба обмежувати результат, а не множник)
    while True:
        result = number * multiplier

        # Помилка: "25" було рядком, а потрібно число
        if result > 25:
            break  # При перевищенні 25 завершуємо цикл

        print(f"{number}x{multiplier}={result}")  # Зручніший формат виводу

        # Помилка: змінна `multi` не існує, треба збільшувати `multiplier`
        multiplier += 1

# Виклик функції
multiplication_table(3)

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
# Рішення завданя №2
def sum_of_two_numbers(a: int, b: int) -> int:
    # Приймаю два параметри a та b, обчислюємо їх суму
    return a + b

# Викликаю функцію з прикладом, де a = 5, b = 7
result = sum_of_two_numbers(5, 7)

# Виводжу результат на екран
print(result)  # Виведе: 12


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
# Рішення завданя №3
def average(numbers: list[float]) -> float: #Обчислює середнє арифметичне списку чисел.

# Виклик функції
example_numbers = [2, 4, 6]  # Простий список чисел
result = average(example_numbers)  # Обчислення середнього значення
print(result)  # Вивід результату

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
# Рішення завданя №4
def reverse_string(string: str) -> str:  # Перевертає рядок у зворотному порядку.

    result = ""  # Створюю порожній рядок для результату
    for i in string:  # Проходжу через кожен символ рядка
        result = i + result  # Додаю кожен символ на початок нового рядка
    return result  # Повертаю перевернутий рядок

# Виклик функції
reversed_string = reverse_string('hello world')  # Перевертаю рядок
print(reversed_string)  # Виводжу перевернутий рядок

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
# Рішення завданя №5
def longest_word(words: list) -> str:  # Повертає найдовше слово з списку слів.

    longest = ""  # Спочатку припускаємо, що найдовше слово порожнє
    for word in words:  # Перебираю всі слова в списку
        if len(word) > len(longest):  # Якщо поточне слово довше за поточне найдовше
            longest = word  # Оновлюю найдовше слово
    return longest

# Виклик функції
longest = longest_word(["apple", "banana", "kiwi", "strawberry"])
print(longest)  # Вивести найдовше слово

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
# Рішення завданя №6
def find_substring(str1: str, str2: str) -> int: # Повертає індекс першого входження другого рядка у перший рядок,
    return str1.find(str2)

# Приклад виклику функції
str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # Поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # Поверне -1

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
# Обравав задачі с дз №3

# task 7
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
def total_area(black_sea_area: int, azov_sea_area: int) -> None:
    # Повертає загальну площу Чорного та Азовського морів і виводить результат.
    print(f"Чорне та Азовське моря займають разом {black_sea_area + azov_sea_area} км2")

# Виклик функції для виведення результату
total_area(436402, 37800)

# task 8
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
def count_products(all_warehouse: int, first_and_second_warehouse: int,
                   second_and_third_warehouse: int) -> None:  # Повертає кількість товарів на кожному зі складів.

    # Вираховую кількість товарів на кожному складі
    first_warehouse = all_warehouse - second_and_third_warehouse  # Перший склад
    second_warehouse = first_and_second_warehouse - first_warehouse  # Другий склад
    third_warehouse = second_and_third_warehouse - second_warehouse  # Третій склад

    # Виводжу результати
    print(f"Перший склад містить {first_warehouse} одиниці товарів")
    print(f"Другий склад містить {second_warehouse} одиниці товарів")
    print(f"Третій склад містить {third_warehouse} одиниці товарів")

count_products(375291, 250449, 222950)

# task 9
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
def laptop_cost(pay_per_month: int,
                months_for_credit: int) -> None:  # Вираховує повну вартість ноутбука на основі щомісячних платежів та кількості місяців кредиту. ноутбуку

    # Вираховую повну вартість ноутбука
    total_cost = pay_per_month * months_for_credit

    # Виводжу результат
    print(f"Повна вартість комп’ютера становить {total_cost} грн")

# Виклик функціїз даними
laptop_cost(1179, 18)

# task 10
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
def needs_lists(all_photos: int, photos_on_list: int) -> None: # Вираховує скільки потрібно листів у альбомі під готові фото картки
    # Вираховую скільки потрібно листів у альбомі
    ihor_needs_lists: int = all_photos // photos_on_list

    # Виводжу результат
    print(f"Для {all_photos} фото карток, Ігорю знадобиться {ihor_needs_lists} сторінок у альбомі")

# Виклик функції з даними
needs_lists(232, 8)
