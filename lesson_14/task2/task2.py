from abc import ABC, abstractmethod
import math

# Створюю абстрактний клас Figure
class Figure(ABC):
    @abstractmethod
    def get_area(self):
        pass  # Метод для обчислення площі

    @abstractmethod
    def get_perimeter(self):
        pass  # Метод для обчислення периметра

# Створюю клас Коло
class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius  # Зберігаю радіус приватно

    def get_area(self):
        return math.pi * self.__radius ** 2  # Обчислюю площу круга

    def get_perimeter(self):
        return 2 * math.pi * self.__radius  # Обчислюю периметр круга

# Створюю клас Прямокутник
class Rectangle(Figure):
    def __init__(self, width, height):
        self.__width = width  # Зберігаю ширину приватно
        self.__height = height  # Зберігаю висоту приватно

    def get_area(self):
        return self.__width * self.__height  # Площа прямокутника

    def get_perimeter(self):
        return 2 * (self.__width + self.__height)  # Периметр прямокутника

# Створюю клас Квадрат
class Square(Figure):
    def __init__(self, side):
        self.__side = side  # Зберігаю сторону приватно

    def get_area(self):
        return self.__side ** 2  # Площа квадрата

    def get_perimeter(self):
        return 4 * self.__side  # Периметр квадрата