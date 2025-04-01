# task - Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

lst: list[str] = input("Введіть числа через пробіл: ").split()  # Отримую список чисел як рядки
sum_even: int = 0  # Зберігаю суму парних чисел

for num in lst:
    num_int: int = int(num.replace(',', ''))  # Видаляю кому і перетворюю на число
    if num_int % 2 == 0:  # Перевіряю, чи число парне
        sum_even += num_int  # Додаю до суми

print(sum_even)  # Виводжу суму парних чисел

