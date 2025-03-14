# task 01 == Виправте синтаксичні помилки
print("Hello", end = " ")
    print("world!")
# task 01 == відповідь
print("Hello", end = " ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
print(f"{hello} {world}!")
# task 02 == відповідь
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print()
# task 03 == відповідь
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = x
# task 04 == відповідь
apples = 2
banana = apples * 4
print(banana)

# task 05 == виправте назви змінних
1_storona = 1
?torona_2 = 2
сторона_3 = 3
$torona_4 = 4
# task 05 == відповідь
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = ? + ? + ? + ?
print()
# task 06 == відповідь
perimetery = storona_1 + storona_2 + storona_3 + storona_4
print(perimetery)


"""
 # Задачі 07 -10:
# Переведіть задачі з книги "Математика, 2 клас"
# на мову пітон і виведіть відповідь, так, щоб було
# зрозуміло дитині, що навчається в другому класі
"""

# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
# task 07 == відповідь
apples_tree = 4
pears_tree = apples_tree + 5
plums_tree = apples_tree - 2
all_trees = apples_tree + pears_tree + plums_tree
print(f"{all_trees} дерев посадили в саду")

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
# task 08 == відповідь

morning_temp = 5  # До обіду температура повітря була +5 градусів
afternoon_temp = morning_temp - 10  # Після обіду температура опустилася на 10 градусів
evening_temp = afternoon_temp + 4  # Надвечір потепліло на 4 градуси. Яка температура надвечір?
print(f"Температура надвечір: {evening_temp} градусів")



# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
# task 09 == відповідь

all_boys = 24
all_girls = all_boys // 2
boys_today = all_boys - 1
girls_today = all_girls - 2
today_children = boys_today + girls_today
print(f"До теотрального кружку сьогоднs прийшло {today_children} дитини")

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
# task 10 == відповідь

first_book_cost = 8
second_book_cost = first_book_cost + 2
third_book_cost = (first_book_cost + second_book_cost) / 2
all_books_price = first_book_cost + second_book_cost + third_book_cost
print(f"Вартість усіх трьох книг разом складае {today_children} гривень")