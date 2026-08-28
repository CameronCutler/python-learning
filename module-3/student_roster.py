import sqlite3

connection = sqlite3.connect("school.db")

# A cursor is what you use to execute SQL commands
cursor = connection.cursor()

# Create students table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        grade INTEGER NOT NULL,
        gpa REAL
    )
""")
connection.commit()
print("Database created!")


# Functions
def add_student(name: str, grade: int, gpa: float) -> None:
    cursor.execute(
        """
        INSERT INTO students (name, grade, gpa)
        VALUES (?, ?, ?) 
        """,
        (name, grade, gpa)
    )
    connection.commit()
    
def get_all_students():
    cursor.execute("""SELECT * FROM students""")
    return cursor.fetchall()

def get_student_by_id(student_id: int):
    cursor.execute("""SELECT * FROM students WHERE id = ?""", (student_id))
    return cursor.fetchone()

def update_student_gpa(student_id: int, new_gpa: float):
    cursor.execute("""UPDATE students SET gpa = ? WHERE id = ?""", (new_gpa, student_id))
    connection.commit()
    
def delete_student(student_id: int):
    cursor.execute(
        """DELETE FROM students WHERE id = ?""",
        (student_id,)
    )
    connection.commit()

def print_all_students():
    students = get_all_students()
    for student in students:
        print(student)
    
    
# Main block
add_student("Cameron Cutler", 12, 3.8)
add_student("George Washington", 10, 4.0)
add_student("Abraham Lincoln", 9, 3.5)
add_student("John Adams", 11, 3.7)

print_all_students()

update_student_gpa(1, 4.0)
print("Student GPA updated!")

delete_student(4)
print("Student Deleted!")

print_all_students()

connection.close()