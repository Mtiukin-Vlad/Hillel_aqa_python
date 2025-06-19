# client.py
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Course

# Створюю базу SQLite у файлі
engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)

# Створюю сесію для взаємодії з базою
Session = sessionmaker(bind=engine)
session = Session()

# Додаю курси
def create_courses():
    course_titles = ['Math', 'Physics', 'History', 'Art', 'Biology']
    for title in course_titles:
        session.add(Course(title=title))
    session.commit()

# Додаю студентів і випадково реєструю їх на курси
def create_students_and_enroll():
    courses = session.query(Course).all()
    for i in range(20):
        student = Student(name=f'Student_{i + 1}')
        student.courses = random.sample(courses, random.randint(1, 3))
        session.add(student)
    session.commit()

# Додаю нового студента до курсу
def add_student_to_course(student_name, course_title):
    course = session.query(Course).filter_by(title=course_title).first()
    if not course:
        print("Курс не знайдено")
        return
    student = Student(name=student_name)
    student.courses.append(course)
    session.add(student)
    session.commit()

# Показую студентів на курсі
def get_students_on_course(course_title):
    course = session.query(Course).filter_by(title=course_title).first()
    if course:
        for student in course.students:
            print(student)

# Оновлення імені студента
def update_student_name(student_id, new_name):
    student = session.get(Student, student_id)
    if student:
        student.name = new_name
        session.commit()

# Видалення студента
def delete_student(student_id):
    student = session.get(Student, student_id)
    if student:
        session.delete(student)
        session.commit()

if __name__ == '__main__':
    create_courses()
    create_students_and_enroll()
    add_student_to_course('Newbie', 'Math')
    print("Студенти на курсі Math:")
    get_students_on_course('Math')
    update_student_name(1, 'Updated_Student')
    delete_student(2)
