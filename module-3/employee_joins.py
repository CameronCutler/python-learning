import sqlite3

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

# Departments table
cursor.execute("""
    CREATE TABLE departments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        location TEXT NOT NULL
    )
""")

# Employees table
cursor.execute("""
    CREATE TABLE employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        role TEXT NOT NULL,
        salary INTEGER,
        department_id INTEGER NOT NULL,
        FOREIGN KEY (department_id) REFERENCES departments(id)
    )
""")

#  Projects Table
cursor.execute("""
    CREATE TABLE projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        employee_id INTEGER NOT NULL,
        FOREIGN KEY (employee_id) REFERENCES employees(id)
    )
""")
connection.commit()
print("Tables created successfully.")

# Insert departments
departments = [
    ("Engineering", "Seattle"),
    ("Human Resources", "Chicago"),
    ("Marketing", "Austin"),
]

for dept in departments:
    cursor.execute(
        """
        INSERT INTO departments (name, location)
        VALUES (?, ?)
        """,
        dept
    )

# Insert employees
employees = [
    ("Alice Johnson", "Software Engineer", 120000, 1),
    ("Ben Smith", "Data Analyst", 98000, 1),
    ("Cara Lee", "DevOps Engineer", 110000, 1),
    ("Darius Moore", "Recruiter", 82000, 2),
    ("Ella Davis", "HR Manager", 95000, 2),
    ("Frank Green", "Marketing Manager", 102000, 3),
    ("Grace Chen", "Graphic Designer", 87000, 3),
    ("Henry Patel", "Content Strategist", 89000, 3),
]

for employee in employees:
    cursor.execute(
        """
        INSERT INTO employees (name, role, salary, department_id)
        VALUES (?, ?, ?, ?)
        """,
        employee
    )

# Insert projects
projects = [
    ("Website Refresh", 6),   # Frank Green
    ("API Modernization", 1),  # Alice Johnson
    ("Hiring Campaign", 4),    # Darius Moore
    ("Brand Launch", 7),       # Grace Chen
]

for project in projects:
    cursor.execute(
        """
        INSERT INTO projects (title, employee_id)
        VALUES (?, ?)
        """,
        project
    )

connection.commit()
print("Sample data inserted successfully.")


# List all employees with department name
print("===== EMPLOYEES =====")
cursor.execute("""
    SELECT e.name, d.name
    FROM employees e
    JOIN departments d ON e.department_id = d.id
    ORDER BY e.name ASC
""")

for row in cursor.fetchall():
    print(f"  {row[0]} ({row[1]})")
print()
    

# List all departments, even those with no employees
cursor.execute("""
    SELECT d.name, COUNT(e.id) AS employee_count
    FROM departments d
    LEFT JOIN employees e ON d.id = e.department_id
    GROUP BY d.id, d.name
    ORDER BY d.name
""")
print("===== DEPARTMENTS =====")
for row in cursor.fetchall():
    print(f"  {row[0]} ({row[1]} employees)")
print()
    
    
# List all employees and the projects they lead, including employees who don't lead any project
cursor.execute("""
    SELECT e.name, p.title
    FROM employees e
    LEFT JOIN projects p ON p.employee_id = e.id
    ORDER BY e.name ASC
""")
print("===== Employees and Their Projects =====")

for row in cursor.fetchall():
    print(f"  {row[0]} - {row[1]} ")
print()


# Find employees who don't lead any project 
cursor.execute("""
    SELECT e.name, p.title
    FROM employees e
    LEFT JOIN projects p ON p.employee_id = e.id
    WHERE p.title IS NULL
    ORDER BY e.name ASC
""")
print("===== Employees Without a Project =====")
for row in cursor.fetchall():
    print(f"  {row[0]}")
print()

    
# List all projects with the project lead's name AND their department name 
cursor.execute("""
    SELECT
        p.title AS project_title,
        e.name AS project_lead,
        d.name AS department_name
    FROM projects p
    JOIN employees e ON p.employee_id = e.id
    JOIN departments d ON e.department_id = d.id
    ORDER BY p.title
""")
print("===== Projects in Progress =====")
for row in cursor.fetchall():
    print(f"{row[0]} | {row[1]} | {row[2]}")