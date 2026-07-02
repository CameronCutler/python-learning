import csv

# Functions
def load_students(filepath):
    data = []
    try:
        with open (filepath, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
            # use conditional to set empty values to 0, then convert to int
                row["math"] = row["math"] or "0"
                row["math"] = int(row["math"])
                
                row["science"] = row["science"] or "0"
                row["science"] = int(row["science"])
                
                row["english"] = row["english"] or "0"
                row["english"] = int(row["english"])
                
                row["history"] = row["history"] or "0"
                row["history"] = int(row["history"])
                data.append(row)
            return data
    except FileNotFoundError:
        print(f"File not found @ '{filepath}'")
        return []


# def calculate_average(grades):
        
print(load_students("data/students.csv"))