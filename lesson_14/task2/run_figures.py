# lesson_10/run_figures.py

from task2 import Circle, Rectangle, Square

# Створюю список фігур, які хочу перевірити
figures = [
    Circle(5),        # Коло з радіусом 5
    Rectangle(3, 4),  # Прямокутник 3х4
    Square(6)         # Квадрат зі стороною 6
]

# У циклі виводжу площу і периметр кожної фігури
for figure in figures:
    print(f"Площа: {figure.get_area():.2f}, Периметр: {figure.get_perimeter():.2f}")