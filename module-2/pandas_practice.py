import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "Diana"],
    "department": ["Engineering", "Marketing", "Engineering", "Sales"],
    "salary": [95000, 72000, 110000, 68000],
    "years": [5, 2, 8, 1],
}

df = pd.DataFrame(data)
print(df)

high_earners = df[df["salary"] > 80000]

engineerrs = df[df["department"] == "Engineering"]

senior_engineer = df[(df["department"] == "Engineering") & (df["salary"] >= 90000)]

# print(senior_engineer)

df_sorted = df.sort_values("salary", ascending=False)
# print(df_sorted)

df_sorted = df.sort_values(["department", "salary"], ascending=[False, False])
# print(df_sorted)

dept_avg = df.groupby("department")["salary"].mean()
print(dept_avg)