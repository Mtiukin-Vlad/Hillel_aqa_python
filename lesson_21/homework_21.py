from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import random

# Створюю базовий клас для моделей
Base = declarative_base()

# Описую таблицю-зв'язок між студентами і курсами (багато-до-багатьох)
student_course_table = Table(
    'student_course', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

# Створюю модель студента
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    courses = relationship('Course', secondary=student_course_table, back_populates='students')

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}')>"

# Створюю модель курсу
class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    students = relationship('Student', secondary=student_course_table, back_populates='courses')

    def __repr__(self):
        return f"<Course(id={self.id}, name='{self.name}')>"

# Налаштовую SQLite базу даних
engine = create_engine('sqlite:///students.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Додаю стартові курси
def create_courses():
    courses = [Course(name=name) for name in ["Math", "Biology", "History", "Physics", "English"]]
    session.add_all(courses)
    session.commit()
    print("Курси створені")

# Додаю 20 випадкових студентів і призначаю їм випадкові курси
def create_students():
    courses = session.query(Course).all()
    for i in range(1, 21):
        student = Student(name=f"Student {i}")
        session.add(student)  # додаю до сесії перед додаванням курсів
        student.courses = random.sample(courses, k=random.randint(1, 3))
    session.commit()
    print("Студенти створені")

# Додаю нового студента та прикріплюю його до вибраних курсів
def add_student(name, course_ids):
    student = Student(name=name)
    session.add(student)
    for cid in course_ids:
        course = session.get(Course, cid)
        if course:
            student.courses.append(course)
    session.commit()
    print(f"Студента '{name}' додано")

# Виводжу список студентів, які зареєстровані на певний курс
def get_students_by_course(course_id):
    course = session.get(Course, course_id)
    if course:
        print(f"Студенти на курсі {course.name}:")
        for student in course.students:
            print(student.name)
    else:
        print("Курс не знайдено")

# Виводжу список курсів, на які зареєстрований студент
def get_courses_by_student(student_id):
    student = session.get(Student, student_id)
    if student:
        print(f"Курси для студента {student.name}:")
        for course in student.courses:
            print(course.name)
    else:
        print("Студента не знайдено")

# Оновлюю ім'я студента
def update_student_name(student_id, new_name):
    student = session.get(Student, student_id)
    if student:
        student.name = new_name
        session.commit()
        print(f"Ім'я оновлено на '{new_name}'")
    else:
        print("Студента не знайдено")

# Видаляю студента з бази даних
def delete_student(student_id):
    student = session.get(Student, student_id)
    if student:
        session.delete(student)
        session.commit()
        print(f"Студента '{student.name}' видалено")
    else:
        print("Студента не знайдено")

# Основний блок запуску
if __name__ == '__main__':
    # Виконується один раз при першому запуску
    if not session.query(Course).first():
        create_courses()
        create_students()

    # Демонстрація роботи
    add_student("Newbie", [1, 2])
    get_students_by_course(1)
    get_courses_by_student(21)
    update_student_name(21, "Updated Newbie")
    delete_student(21)
