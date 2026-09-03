"""
Exercise: School Enrollment System
Module 3 | Lesson 8 | ~35 min

Objective:
  Build a school database with both a one-to-many relationship
  (Department -> Teacher -> Course) and a many-to-many relationship
  (Course <-> Student), using SQLAlchemy's relationship() and an
  association table.
"""

from sqlalchemy import (
    create_engine, String, Integer, ForeignKey, Table, Column
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session
from typing import List

engine = create_engine("sqlite:///:memory:", echo=False)


class Base(DeclarativeBase):
    pass


# This table links students to courses (many-to-many).
# It has no extra columns — just two foreign keys, both part of the PK.

student_courses = Table(
    "student_courses",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("students.id"), primary_key=True),
    Column("course_id",  Integer, ForeignKey("courses.id"),  primary_key=True),
)


class Department(Base):
    """Represents a department in the school.
    
    A department can have multiple teachers. This is a one-to-many relationship
    where one department is associated with many teachers.
    
    Attributes:
        id: Primary key identifier for the department.
        name: Unique name of the department.
        teachers: List of Teacher objects belonging to this department.
    """
    __tablename__ = "departments"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    
    teachers: Mapped[List["Teacher"]] = relationship(back_populates="department")
    
    def __repr__(self) -> str:
        return f"Department(name='{self.name}')"


class Teacher(Base):
    """Represents a teacher in the school.
    
    A teacher belongs to a department and teaches multiple courses.
    This establishes a many-to-one relationship with Department and
    a one-to-many relationship with Course.
    
    Attributes:
        id: Primary key identifier for the teacher.
        name: Name of the teacher.
        department_id: Foreign key referencing the department.
        department: Department object this teacher belongs to.
        courses: List of Course objects taught by this teacher.
    """
    __tablename__ = "teachers"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    department_id: Mapped[int] = mapped_column(ForeignKey("departments.id"))
    
    department: Mapped["Department"] = relationship(back_populates="teachers")
    courses: Mapped[List["Course"]] = relationship(back_populates="teacher")
    
    def __repr__(self) -> str:
        return f"Teacher(name='{self.name}')"
    


class Course(Base):
    """Represents a course offered by the school.
    
    A course is taught by one teacher (many-to-one relationship) and
    can be enrolled in by multiple students (many-to-many relationship
    via the student_courses association table).
    
    Attributes:
        id: Primary key identifier for the course.
        title: Name/title of the course.
        teacher_id: Foreign key referencing the teacher teaching this course.
        teacher: Teacher object who teaches this course.
        students: List of Student objects enrolled in this course.
    """
    __tablename__ = "courses"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    teacher_id: Mapped[int] = mapped_column(ForeignKey("teachers.id"))
    
    teacher: Mapped["Teacher"] = relationship(back_populates="courses")
    students: Mapped[List["Student"]] = relationship(secondary=student_courses, back_populates="courses")
    
    def __repr__(self) -> str:
        return f"Course(title='{self.title}')"


class Student(Base):
    """Represents a student in the school enrollment system.
    
    A student can be enrolled in multiple courses through a many-to-many
    relationship via the student_courses association table.
    """
    __tablename__ = "students"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    
    courses: Mapped[List["Course"]] = relationship(secondary=student_courses, back_populates="students")
    
    def __repr__(self) -> str:
        return f"Student(name='{self.name}', email='{self.email}')"
    


# ── Test block ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        # ── Seed: 2+ departments, 4+ teachers, 5+ courses ────────────────────
        cs   = Department(name="Computer Science")
        math = Department(name="Mathematics")
        session.add_all([cs, math])
        session.flush()

        t1 = Teacher(name="Dr. Alice Park",   department_id=cs.id)
        t2 = Teacher(name="Prof. Bob Chen",   department_id=cs.id)
        t3 = Teacher(name="Dr. Carol White",  department_id=math.id)
        t4 = Teacher(name="Prof. Dan Rivera", department_id=math.id)
        session.add_all([t1, t2, t3, t4])
        session.flush()

        c1 = Course(title="Intro to Python", teacher_id=t1.id)
        c2 = Course(title="Data Structures",  teacher_id=t1.id)
        c3 = Course(title="Web Development",  teacher_id=t2.id)
        c4 = Course(title="Calculus I",       teacher_id=t3.id)
        c5 = Course(title="Linear Algebra",   teacher_id=t4.id)
        session.add_all([c1, c2, c3, c4, c5])
        session.flush()

        # ── Seed: 6+ students with various enrollments ───────────────────────
        s1 = Student(name="Zoe Adams",   email="zoe@school.edu")
        s2 = Student(name="Raj Patel",   email="raj@school.edu")
        s3 = Student(name="Nina Brown",  email="nina@school.edu")
        s4 = Student(name="Marco Diaz",  email="marco@school.edu")
        s5 = Student(name="Yuki Tanaka", email="yuki@school.edu")
        s6 = Student(name="Olu Okafor",  email="olu@school.edu")
        session.add_all([s1, s2, s3, s4, s5, s6])
        session.flush()

        s1.courses += [c1, c3, c5]
        s2.courses += [c2, c4, c5]
        s3.courses += [c1, c3, c4]
        s4.courses += [c2, c3]
        s5.courses += [c1, c4, c5]
        s6.courses += [c2, c3, c4]
        
        session.commit()

    # ── Demo 1: each department and its teachers ────────────────────────────
    print("=== Departments and Teachers ===")
    departments = session.query(Department).all()
    for department in departments:
        print(f"Department: {department.name}")
        for teacher in department.teachers:
            print(f"Teacher: {teacher.name}")
        print()

    # ── Demo 2: each teacher and the courses they teach ─────────────────────
    print("=== Teachers and Their Courses ===")
    teachers = session.query(Teacher).all()
    for teacher in teachers:
        print(teacher.name)
        for course in teacher.courses:
            print(course.title)
        print()

    # ── Demo 3: each course with its enrolled students ──────────────────────
    print("=== Courses and Enrolled Students ===")
    courses = session.query(Course).all()
    for course in courses:
        print(course.title)
        for student in course.students:
            print("-" + student.name)
        print()

    # ── Demo 4: each student and the courses they're enrolled in ────────────
    print("=== Students and Their Courses ===")
    students = session.query(Student).all()
    for student in students:
        print(student)
        for course in student.courses:
            print("-" + course.title)
        print()

    # ── Demo 5: any course with more than 3 students ────────────────────────
    print("=== Courses With More Than 3 Students ===")

    courses = session.query(Course).all()
    for course in courses:
        if len(course.students) > 3:
            print(course.title) 
    print()