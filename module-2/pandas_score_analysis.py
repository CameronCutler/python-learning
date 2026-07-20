import pandas as pd

data = {
    "student": ["Alice", "Bob", "Charlie", "Diana", "Eve",
                 "Frank", "Grace", "Henry", "Iris", "Jack"],
    "course": ["Python", "Python", "SQL", "SQL", "Python",
               "SQL", "Python", "SQL", "Python", "SQL"],
    "score": [92, 78, 85, 91, 88, 72, 95, 68, 84, 90],
    "hours_studied": [20, 12, 18, 22, 15, 8, 25, 10, 16, 19],
    "passed": [True, True, True, True, True, False, True, False, True, True],
}

df = pd.DataFrame(data)

# How many students in each course
students_in_each_course = df.groupby("course").agg(headcount=("student", "count"))
print("1. How many students are in each course?")
print(students_in_each_course)


# What is the average score per course?
avg_score_per_course = df.groupby("course").agg(average=("score", "mean"))
print("2. What is the average score per course?")
print(avg_score_per_course)


# Who are the top 3 students by score?
df_sorted = df.sort_values("score", ascending=False)
print("3. Who are the top 3 students by score?")
print(df_sorted.head(3))


# What is the average hours studied for students who passed vs. didn’t pass?
passing_students = df.groupby("passed").agg(average_hours_studied=("hours_studied", "mean"))
print("4. What is the average hours studied for students who passed vs. didn’t pass?")
print(passing_students)


# Create a "grade" column: 90+ = “A”, 80-89 = “B”, 70-79 = “C”, below 70 = “F”
df_grades = df
df_grades["grade"] = "F"
df_grades.loc[df_grades["score"] >= 70, "grade"] = "C"
df_grades.loc[df_grades["score"] >= 80, "grade"] = "B"
df_grades.loc[df_grades["score"] >= 90, "grade"] = "A"
print("5. Create a 'grade' column and assing letter values")
print(df_grades)


# What’s the distribution of grades per course?
value_counts = df_grades.groupby("course")["grade"].value_counts()
print("6. What’s the distribution of grades per course?")
print(value_counts)