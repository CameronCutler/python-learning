import sqlite3

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

# Students table
cursor.execute("""
    CREATE TABLE students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
""")

# Courses table
cursor.execute("""
    CREATE TABLE courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        instructor TEXT NOT NULL,
        credits INTEGER NOT NULL
    )
""")

# Enrollments table — connects students to courses
cursor.execute("""
    CREATE TABLE enrollments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        course_id INTEGER NOT NULL,
        grade TEXT,
        FOREIGN KEY (student_id) REFERENCES students(id),
        FOREIGN KEY (course_id) REFERENCES courses(id)
    )
""")

print("Tables created!")


# Add students
students = [
    ("Alice Park", "alice@school.edu"),
    ("Bob Martinez", "bob@school.edu"),
    ("Carol Zhang", "carol@school.edu"),
    ("David Okafor", "david@school.edu"),  # Won't enroll in anything
]
cursor.executemany(
    "INSERT INTO students (name, email) VALUES (?, ?)", students
)

# Add courses
courses = [
    ("Intro to Python", "Dr. Smith", 3),
    ("Database Systems", "Dr. Johnson", 4),
    ("Web Development", "Dr. Lee", 3),
]
cursor.executemany(
    "INSERT INTO courses (title, instructor, credits) VALUES (?, ?, ?)", courses
)

# Add enrollments
enrollments = [
    (1, 1, "A"),     # Alice in Intro to Python, grade A
    (1, 2, "B+"),    # Alice in Database Systems, grade B+
    (2, 1, "B"),     # Bob in Intro to Python, grade B
    (2, 3, "A-"),    # Bob in Web Development, grade A-
    (3, 2, None),    # Carol in Database Systems, no grade yet
]
cursor.executemany(
    "INSERT INTO enrollments (student_id, course_id, grade) VALUES (?, ?, ?)",
    enrollments
)

connection.commit()
print("Data inserted!")

print("\n=== Student Enrollments (INNER JOIN) ===")
cursor.execute("""
    SELECT s.name, c.title, e.grade
    FROM enrollments AS e
    INNER JOIN students s ON e.student_id = s.id
    INNER JOIN courses c ON e.course_id = c.id
    ORDER BY s.name, c.title
""")

for row in cursor.fetchall():
    grade = row[2] if row[2] else "Not graded"
    print(f"  {row[0]} — {row[1]}: {grade}")
    

print("\n=== Students Not Enrolled in Any Course ===")
cursor.execute("""
    SELECT s.name, s.email
    FROM students s
    LEFT JOIN enrollments e ON s.id = e.student_id
    WHERE e.id IS NULL
""")

for row in cursor.fetchall():
    print(f"  {row[0]} ({row[1]})")
    

print("\n=== Students Per Course ===")
# cursor.execute("""
#     SELECT c.title, COUNT(e.student_id) AS student_count
#     FROM courses c
#     LEFT JOIN enrollments e ON c.id = e.course_id
#     GROUP BY c.id, c.title
#     ORDER BY student_count DESC
# """)
cursor.execute("""
    SELECT c.title, COUNT(e.student_id) AS student_count
    FROM courses c
    JOIN enrollments e ON c.id = e.course_id
    GROUP BY c.title
""")

for row in cursor.fetchall():
    print(f"  {row[0]}: {row[1]} student(s)")