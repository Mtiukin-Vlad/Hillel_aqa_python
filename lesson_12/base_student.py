class Student:
    # Конструктор класу. Тут я ініціалізую атрибути студента.
    def __init__(self, first_name, last_name, age, average_grade):
        self.first_name = first_name  # Зберігаю ім'я студента.
        self.last_name = last_name  # Зберігаю прізвище студента.
        self.age = age  # Зберігаю вік студента.
        self.average_grade = average_grade  # Зберігаю середній бал студента.

    # Метод для оновлення середнього балу студента.
    def update_average_grade(self, new_grade):
        self.average_grade = new_grade  # Оновлюю середній бал на новий.

    # Метод для отримання рядкового представлення об'єкта студента.
    def __str__(self):
        return (f"Студент: {self.first_name} {self.last_name}, "
                f"вік: {self.age}, середній бал: {self.average_grade}")  # Повертаю строку з інформацією про студента.
