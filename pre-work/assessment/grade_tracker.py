"""
Project: Student Grade Tracker
Pre-Work Section C — Python Fundamentals
Estimated time: 45-60 minutes

Objective: Build a data processing script that reads student grades from
a CSV, calculates averages, assigns letter grades, and writes a summary report.

Your job: implement all the functions marked with # TODO.
Do NOT modify the function signatures or the main() function.
"""

import csv


# ============================================================
# FUNCTION 1: Load data from CSV
# ============================================================

def load_students(filepath: str) -> list[dict]:
    """
    Read student data from a CSV file.

    Each row becomes a dictionary. The CSV has columns:
    student_name, math, science, english, history

    Some cells may be empty strings (missing grades) — that's expected.

    Args:
        filepath: Path to the CSV file.

    Returns:
        A list of dicts, one per student.
        Example: [{"student_name": "Alice", "math": "92", ...}, ...]

    Raises:
        FileNotFoundError: if the CSV file doesn't exist.
    """
    data = []
    # try opening the file and return message and empty list if file not found
    try:
        with open (filepath, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
            return data
    except FileNotFoundError:
        print(f"File not found @ '{filepath}'")
        return []



# ============================================================
# FUNCTION 2: Calculate average, handling missing values
# ============================================================

def calculate_average(grades: list) -> float | None:
    """
    Calculate the average of a list of grade values.

    Grade values may be strings (from the CSV), empty strings, or numbers.
    Ignore any value that can't be converted to a float.

    Args:
        grades: A list of values (e.g., ["92", "88", "", "79"]).

    Returns:
        The average as a float, rounded to 1 decimal place.
        Returns None if there are no valid grades.
    """
    cleaned_grades = []
    # Loop through the list
    for value in grades:
        if value != "":
            cleaned_grades.append(int(value))
    # return the average after empties have been removed 
    if cleaned_grades:
        return round(sum(cleaned_grades)/len(cleaned_grades), 2)
    else:
        return None
# print(calculate_average(['95', '86', '', '98']))
# print(calculate_average(['', '', '', '']))
        
# ============================================================
# FUNCTION 3: Assign letter grade
# ============================================================

def get_letter_grade(average: float | None) -> str:
    """
    Convert a numeric average to a letter grade.

    Scale:
        90+  → "A"
        80-89 → "B"
        70-79 → "C"
        60-69 → "D"
        < 60  → "F"
        None  → "N/A" (no grades available)

    Args:
        average: The numeric average, or None.

    Returns:
        The letter grade as a string.
    """
    if average == None:
        return "N/A"
    if average >= 90:
        return "A"
    elif average < 60:
        return "F"
    elif average < 70:
        return "D"
    elif average < 80:
        return "C"
    elif average < 90:
        return "B"


# ============================================================
# FUNCTION 4: Generate summary report
# ============================================================

def generate_report(students: list[dict]) -> dict:
    """
    Generate a class summary report.

    Args:
        students: The list of student dicts from load_students().

    Returns:
        A dict with these keys:
            "total_students":   int — how many students
            "class_average":    float — average of all valid averages
            "highest_average":  float — the best average
            "lowest_average":   float — the lowest average
            "grade_distribution": dict — {"A": 3, "B": 5, ...}
            "students":         list of dicts, each with:
                                    name, average, grade
    """
    total_students = len(students)
    class_average, highest_average, lowest_average = 0.0, 0.0, 100.0
    students_averages, class_averages = [], []
    grade_count  = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    #  Loop through the student list
    for student in students:
        # Make a new dict to put the averages in
        cleaned_student = {}
        # Calculate averages and letter grade
        cleaned_student["name"] = student["student_name"]
        cleaned_student["average"] = calculate_average([student["math"], student["science"], student["english"], student["history"]])
        cleaned_student["grade"] = get_letter_grade(cleaned_student["average"])
        
        # Iterate our letter grade counter
        grade_count[cleaned_student["grade"]] += 1
        
        # Add the new dict to our list of students
        students_averages.append(cleaned_student)
        
    # Loop through the new list of dicts to find the class average
    for student in students_averages:
        if student['average'] > highest_average:
            highest_average = student['average']
        elif student['average'] < lowest_average:
            lowest_average = student['average']
        
        # Add all the averages to a list
        class_averages.append(student['average'])
        
    # Calculate class average
    class_average = calculate_average(class_averages)
    
    return {
        "total_students": total_students,
        "class_average": class_average,
        "highest_average": highest_average,
        "lowest_average": lowest_average,
        "grade_distribution": grade_count,
        "students": students_averages
    }
    


# ============================================================
# FUNCTION 5: Write report to a file
# ============================================================

def write_report(report: dict, filepath: str) -> None:
    """
    Write the summary report to a text file.

    Format example:
        ===========================
        STUDENT GRADE REPORT
        ===========================
        Total students: 15
        Class average:  81.3
        Highest average: 95.0
        Lowest average:  55.0

        Grade Distribution:
          A: 5
          B: 4
          ...

        Individual Results:
          Alice Johnson    Avg: 91.5  Grade: A
          ...

    Args:
        report:   The dict returned by generate_report().
        filepath: Path to write the report file.
    """
    with open(filepath, "w") as file:
        
        file.write("==================================================\n")
        file.write("               STUDENT GRADE REPORT               \n")
        file.write("==================================================\n\n")
        
        # 1. Summary Statistics
        file.write("## CLASS SUMMARY STATISTICS\n")
        file.write("--------------------------------------------------\n")
        class_avg = report["class_average"]
        high_avg = report["highest_average"]
        low_avg = report["lowest_average"]
        
        file.write(f"Overall Class Average: {f'{class_avg:.2f}' if class_avg is not None else 'N/A'}\n")
        file.write(f"Highest Student Avg:   {f'{high_avg:.2f}' if high_avg is not None else 'N/A'}\n")
        file.write(f"Lowest Student Avg:    {f'{low_avg:.2f}' if low_avg is not None else 'N/A'}\n\n")
        
        # 2. Grade Distribution
        file.write("## GRADE DISTRIBUTION\n")
        file.write("--------------------------------------------------\n")
        dist = report["grade_distribution"]
        for grade in ["A", "B", "C", "D", "F", "N/A"]:
            file.write(f"{grade}: {dist.get(grade, 0)}\n")
        file.write("\n")
        
        # 3. Individual Results
        file.write("## INDIVIDUAL STUDENT RESULTS\n")
        file.write("--------------------------------------------------\n")
        file.write(f"{'Student Name':<20} | {'Average':<8} | {'Letter Grade':<12}\n")
        file.write("-" * 50 + "\n")
        
        for s in report["students"]:
            avg_str = f"{s['average']:.2f}" if s["average"] is not None else "N/A"
            file.write(f"{s['name']:<20} | {avg_str:<8} | {s['grade']:<12}\n")

# ============================================================
# MAIN — do not modify
# ============================================================

def main():
    print("Loading student data...")
    students = load_students("data/students.csv")
    print(f"Loaded {len(students)} students.")

    print("Generating report...")
    report = generate_report(students)

    print("\n--- Summary ---")
    print(f"Total students:   {report['total_students']}")
    print(f"Class average:    {report['class_average']}")
    print(f"Highest average:  {report['highest_average']}")
    print(f"Lowest average:   {report['lowest_average']}")

    print("\nGrade Distribution:")
    for grade, count in sorted(report["grade_distribution"].items()):
        print(f"  {grade}: {count}")

    print("\nTop 5 students:")
    sorted_students = sorted(
        [s for s in report["students"] if s["average"] is not None],
        key=lambda s: s["average"],
        reverse=True
    )
    for s in sorted_students[:5]:
        print(f"  {s['name']:<20} {s['average']:.1f}  ({s['grade']})")

    write_report(report, "grade_report.txt")
    print("\nReport written to grade_report.txt")


if __name__ == "__main__":
    main()