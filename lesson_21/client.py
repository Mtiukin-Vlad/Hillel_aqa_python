import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Course

class DBClient:
    def __init__(self, db_url="sqlite:///database.db"):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    # Створюю курси
    def create_courses(self):
        course_titles = ["Math", "Physics", "History", "Biology", "Art"]
        for title in course_titles:
            self.session.add(Course(title=title))
        self.session.commit()

    # Створюю студентів і записую їх на випадкові курси
    def create_students(self):
        courses = self.session.query(Course).all()
        for i in range(20):
            student = Student(name=f"Student_{i+1}")
            student.courses = random.sample(courses, random.randint(1, 3))
            self.session.add(student)
        self.session.commit()

    # Додаю нового студента на курс
    def add_student_to_course(self, student_name, course_title):
        course = self.session.query(Course).filter_by(title=course_title).first()
        if not course:
            print("Курс не знайдено")
            return
        student = Student(name=student_name)
        student.courses.append(course)
        self.session.add(student)
        self.session.commit()
        print(f"{student_name} додано до курсу {course_title}")

    # Показую студентів на конкретному курсі
    def show_students_on_course(self, course_title):
        course = self.session.query(Course).filter_by(title=course_title).first()
        if course:
            print(f"Студенти на курсі {course_title}:")
            for student in course.students:
                print(student)

    # Показую курси, на які записаний студент
    def show_courses_of_student(self, student_id):
        student = self.session.get(Student, student_id)
        if student:
            print(f"{student.name} записаний на курси:")
            for course in student.courses:
                print(course)

    # Оновлюю ім'я студента
    def update_student_name(self, student_id, new_name):
        student = self.session.get(Student, student_id)
        if student:
            student.name = new_name
            self.session.commit()
            print(f"Ім'я оновлено на {new_name}")

    # Видаляю студента
    def delete_student(self, student_id):
        student = self.session.get(Student, student_id)
        if student:
            self.session.delete(student)
            self.session.commit()
            print(f"Студент {student_id} видалений")

# Приклад використання
if __name__ == "__main__":
    db = DBClient()
    db.create_courses()
    db.create_students()
    db.add_student_to_course("Newbie", "Math")
    db.show_students_on_course("Math")
    db.show_courses_of_student(1)
    db.update_student_name(1, "Updated_Student")
    db.delete_student(2)
