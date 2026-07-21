import matplotlib.pyplot as plt
import pandas as pd

# departments = ["Engineering", "Sales", "Marketing", "Support"]
# headcount = [45, 30, 20, 15]

# plt.figure(figsize=(8, 5))
# plt.bar(departments, headcount, color="steelblue")
# plt.title("Employees by Department")
# plt.xlabel("Department")
# plt.ylabel("Headcount")
# # plt.tight_layout()        # Prevents labels from being cut off
# plt.savefig("headcount.png", dpi=150)  # Save to file
# plt.show()


# dates = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
# revenue = [12000, 15000, 13500, 18000, 22000, 19500]

# plt.figure(figsize=(8, 5))
# plt.plot(dates, revenue, marker="o", color="coral", linewidth=2)
# plt.title("Monthly Revenue")
# plt.xlabel("Month")
# plt.ylabel("Revenue ($)")
# plt.grid(True, alpha=0.3)   # Light gridlines for readability
# plt.tight_layout()
# plt.show()


# import numpy as np

# salaries = [45000, 52000, 58000, 62000, 65000, 68000, 70000, 72000,
#             75000, 78000, 82000, 88000, 95000, 110000, 150000]

# plt.figure(figsize=(8, 5))
# plt.hist(salaries, bins=8, color="seagreen", edgecolor="black")
# plt.title("Salary Distribution")
# plt.xlabel("Salary ($)")
# plt.ylabel("Number of Employees")
# plt.tight_layout()
# plt.show()


# fig, axes = plt.subplots(1, 3, figsize=(15, 5))  # 1 row, 3 columns

# # Chart 1
# axes[0].bar(departments, headcount, color="steelblue")
# axes[0].set_title("Headcount by Department")

# # Chart 2
# axes[1].plot(dates, revenue, marker="o", color="coral")
# axes[1].set_title("Monthly Revenue")

# # Chart 3
# axes[2].hist(salaries, bins=8, color="seagreen", edgecolor="black")
# axes[2].set_title("Salary Distribution")

# plt.tight_layout()
# plt.savefig("dashboard.png", dpi=150)
# plt.show()

# Guided Example
messy_data = {
    "name": ["Alice", "Bob", "Charlie", "  Diana  ", "Eve", "Bob", "Frank", None, "Grace", "Henry"],
    "department": ["Engineering", "marketing", "ENGINEERING", "Sales", "engineering",
                   "marketing", "Sales", None, "Engineering", "sales"],
    "salary": ["95000", "72000", "110000", "68000", "88000",
               "72000", "75000", "82000", "-5000", "78000"],
    "start_date": ["2020-03-15", "2022-01-10", "2018-07-22", "2024-06-01", "2021-11-30",
                   "2022-01-10", "2023-03-15", "2020-08-01", "not a date", "2023-09-15"],
    "email": ["alice@co.com", "bob@co.com", "charlie@co.com", "diana@co.com", "eve@co.com",
              "bob@co.com", "frank@co.com", "unknown@co.com", "grace@co.com", "henry@co.com"],
}


df = pd.DataFrame(messy_data)
print("=== Raw Data ===")
print(df)
print(f"\nShape: {df.shape}")
print(f"\nMissing values:\n{df.isnull().sum()}")

# Fix whitespace in names
df["name"] = df["name"].str.strip()

# Standardize department names
df["department"] = df["department"].str.title().str.strip()

# Convert salary to numeric
df["salary"] = pd.to_numeric(df["salary"], errors="coerce")

# Convert dates
df["start_date"] = pd.to_datetime(df["start_date"], errors="coerce")

# Remove duplicates
df = df.drop_duplicates(subset=["email"], keep="first")

# Handle missing values
df = df.dropna(subset="name")
# df = df.dropna(subset=["start_date"])

# Fix invalid values
df.loc[df["salary"] < 0, "salary"] = pd.NA

print(df)