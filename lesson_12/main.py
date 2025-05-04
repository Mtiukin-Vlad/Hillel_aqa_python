from base_student import Student

# Створення обʼєкта
student = Student("Владислав", "Матюхін", 25, 88.5)

# Вивід інформації
print(student)

# Оновлення середнього балу
student.update_average_grade(100.0)

# Повторний вивід
print("Після оновлення балу:")
print(student)