# models.py
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

# Багатозначна звʼязка між студентами і курсами
student_course_table = Table(
    'student_course',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    # Вказую, що студент може бути записаний на декілька курсів
    courses = relationship('Course', secondary=student_course_table, back_populates='students')

    def __repr__(self):
        return f'Student(id={self.id}, name="{self.name}")'

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    title = Column(String)

    # Кожен курс може мати багато студентів
    students = relationship('Student', secondary=student_course_table, back_populates='courses')

    def __repr__(self):
        return f'Course(id={self.id}, title="{self.title}")'
