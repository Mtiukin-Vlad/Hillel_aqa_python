alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії"
# task 01 - Рішення
alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n'
'"That depends a good deal on where you want to get to," said the Cat.\n'
'"I don\'t much care where ——" said Alice.\n'
'"Then it doesn\'t matter which way you go," said the Cat.\n'
'"—— so long as I get somewhere," Alice added as an explanation.\n'
'"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'


# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті"
# task 02 - Рішення
alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don\'t much care where ——" said Alice.\n"Then it doesn\'t matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'


# task 03 == Виведіть змінну alice_in_wonderland на друк"
# task 03 - Рішення
print(alice_in_wonderland)



"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
# task 04 - Рішення
black_sea_area: int = 436402  
azov_sea_area: int = 37800

total_area: int = black_sea_area + azov_sea_area
print(f"Чорне та Азовське моря займають разом {total_area} км2") 


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
# task 05 - Рішення
all_warehouse = 375291
first_and_second_warehouse = 250449
second_and_third_warehouse = 222950

first_warehouse = all_warehouse - second_and_third_warehouse
second_warehouse = first_and_second_warehouse - first_warehouse
third_warehouse = second_and_third_warehouse - second_warehouse

print(f"Перший склад містить {first_warehouse} одиниці товарів\n"
      f"Другий склад містить {second_warehouse} одиниці товарів\n"
      f"Третій склад містить {third_warehouse} одиниці товарів")


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
# task 06 - Рішення
pay_per_month = 1179
months_for_credit = 18  # 1.5 года = 18 месяцев

laptop_cost = pay_per_month * months_for_credit
print(f"Повна вартість комп’ютера становить {laptop_cost} грн")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
# task 07 - Рішення
print(f"Остача від діленя чисел 8019 : 8 становить {8019 % 8}\n"
      f"Остача від діленя чисел 9907 : 9 становить {9907 % 9}\n"
      f"Остача від діленя чисел 2789 : 5 становить {2789 % 5}\n"
      f"Остача від діленя чисел 7248 : 6 становить {7248 % 6}\n"
      f"Остача від діленя чисел 7128 : 5 становить {7128 % 5}\n"
      f"Остача від діленя чисел 19224 : 9 становить {19224 % 9}\n")



# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
# task 08 - Рішення
print(f"{274 * 4} гривень знадобиться для купівлі 4 великих піц\n"
      f"{218 * 2} гривень знадобиться для купівлі 2 середніх піц\n"
      f"{35 * 4} гривень знадобиться для купівлі 4 пачок соку\n"
      f"{350 * 1} гривень знадобиться для купівлі 1 торта\n"
      f"{21 * 3} гривень знадобиться для купівлі 3 пляшок води")
      

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
# task 09 - Рішення
all_photos: int = 232
photos_on_list: int = 8
ihor_needs_lists: int = all_photos // photos_on_list
print(f"Для 232 фото карток, Ігорю знадобиться {ihor_needs_lists} сторінок у альбомі")


# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
# task 10 - Рішення
all_length: int = 1600  # відстань в км
oil_on_100km: int = 9  # кількість літрів на 100 км
bak: int = 48  # місткість баку в літрах

# 1) Скільки літрів бензину знадобиться для подорожі
need_for_trip: int = (all_length / 100) * oil_on_100km

# 2) Скільки разів потрібно заїхати на заправку
needed_refills: int = need_for_trip // bak  

print(f"Для подорожі знадобиться {need_for_trip} літрів бензину."
      f"Родині потрібно заїхати на заправку {needed_refills} рази.")