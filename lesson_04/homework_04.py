adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
# task 01 - Рішення
new_adwentures_of_tom_sawer: str = adwentures_of_tom_sawer.replace("\n", " ")
print(new_adwentures_of_tom_sawer)

# task 02 ==
""" Замініть .... на пробіл
"""
# task 02 - Рішення
new1_adwentures_of_tom_sawer: str = new_adwentures_of_tom_sawer.replace("....", " ")
print(new1_adwentures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
# task 03 - Рішення
new2_adwentures_of_tom_sawer: str = ' '.join(new1_adwentures_of_tom_sawer.split())
print(new2_adwentures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
# task 04 - Рішення
new3_adwentures_of_tom_sawer: int = new2_adwentures_of_tom_sawer.lower().count('h')
print(f"Літера h зустричаеться у тексті {new3_adwentures_of_tom_sawer}разів")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
# task 05 - Рішення
new4_adwentures_of_tom_sawer: list[str] = new2_adwentures_of_tom_sawer.split()
count_title_words = 0

for word in new4_adwentures_of_tom_sawer:
    if word.istitle():
        count_title_words += 1

print(f"{count_title_words} разів у тексті зустрічаются слова з виликої літері")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
# task 06 - Рішення
first_tom: int = new2_adwentures_of_tom_sawer.find('Tom')  
second_tom: int = new2_adwentures_of_tom_sawer.find('Tom', first_tom + 1)

print(f"На {second_tom} позиціі зустричается слово Tom вдруге")

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
# task 07 - Рішення
adwentures_of_tom_sawer_sentences: list[str] = new2_adwentures_of_tom_sawer.split(". ")

print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
# task 08 - Рішення
adwentures_of_tom_sawer_sentences: tuple = new2_adwentures_of_tom_sawer.split(". ")
fourth_sentence: str = adwentures_of_tom_sawer_sentences[3].lower()
print(fourth_sentence)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
# task 09 - Рішення
adwentures_of_tom_sawer_sentences: tuple = new2_adwentures_of_tom_sawer.split(". ")
print(adwentures_of_tom_sawer_sentences)
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.startswith("By the time"):
        print(f"Рядок {sentence} починається з 'By the time'")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
# task 10 - Рішення
adwentures_of_tom_sawer_sentences: list[str] = new2_adwentures_of_tom_sawer.split(". ")
last_sentence: int = adwentures_of_tom_sawer_sentences[-1]
word_count: int = len(last_sentence.split())
print(f"Кількість слів в останньому реченні: {word_count}")