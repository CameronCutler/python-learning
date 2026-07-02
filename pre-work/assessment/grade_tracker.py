import csv

# Functions
def load_students(filepath):
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
# print(load_students("data/students.csv"))


def calculate_average(grades):
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
        
def get_letter_grade(average):
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
print(get_letter_grade(None))