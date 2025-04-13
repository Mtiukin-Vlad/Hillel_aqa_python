# Завдання:
# Обрати від 3 до 5 різних домашніх завдань.
# Перетворити їх у функції (якщо ще не зроблено).
# Створити файл homeworks.py і додати до нього ці функції.
# Покрити функції не менш ніж 10 тестами загалом (у test_homeworks08.py).
# Імпорт та самі тести розміщуються в окремому файлі.

# Функції взято з домашнього завдання №7.

def total_area(black_sea_area: int, azov_sea_area: int) -> int:
    """Повертає сумарну площу Чорного та Азовського морів (у км²)."""
    return black_sea_area + azov_sea_area


def count_products(all_warehouse: int, first_and_second: int, second_and_third: int) -> tuple[int, int, int]:
    """Обчислює кількість товарів на кожному складі.
    Повертає кортеж: (перший склад, другий склад, третій склад).
    """
    first = all_warehouse - second_and_third
    second = first_and_second - first
    third = second_and_third - second
    return first, second, third


def laptop_cost(monthly_payment: int, months: int) -> int:
    """Обчислює загальну вартість комп’ютера за щомісячною оплатою."""
    return monthly_payment * months
