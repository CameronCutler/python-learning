"""
pipeline.py — Module 2 Project Starter
Your job: implement each method in the DataPipeline class below.
The docstrings describe exactly what each method should do.
"""

import pandas as pd
import re
import os
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


class DataPipeline:
    """
    A data processing pipeline for employee survey data.

    Usage (once implemented):
        pipeline = DataPipeline("data/messy_employee_survey.csv")
        results = pipeline.run()
    """

    # Canonical spellings for normalization — use these dicts in your clean() method.
    DEPT_MAP = {
        "engineering": "Engineering",
        "eng":         "Engineering",
        "marketing":   "Marketing",
        "mktg":        "Marketing",
        "sales":       "Sales",
        "hr":          "HR",
        "human resources": "HR",
        "h.r.":        "HR",
        "finance":     "Finance",
        "fin":         "Finance",
    }

    LOC_MAP = {
        "new york":        "New York",
        "nyc":             "New York",
        "chicago":         "Chicago",
        "chi":             "Chicago",
        "austin":          "Austin",
        "austin, tx":      "Austin",
        "atx":             "Austin",
        "seattle":         "Seattle",
        "sea":             "Seattle",
        "remote":          "Remote",
        "work from home":  "Remote",
    }

    def __init__(self, filepath):
        """Load the CSV at `filepath` into self.df (a pandas DataFrame).
        Print how many rows and columns were loaded.

        Hint: use pd.read_csv()
        Wrap the load in try/except to catch FileNotFoundError.

        Args:
            filepath: path to the messy CSV file
        """
        try:
            self.df = pd.read_csv(filepath)
            rows, cols = self.df.shape
            print(f"Loaded {rows} rows and {cols} columns.")
        except FileNotFoundError:
            print(f"File not found: {filepath}")
            self.df = pd.DataFrame()

    def clean(self):
        """Clean the DataFrame stored in self.df and print a summary.

        Steps to implement (in order):
        1. Remove rows with duplicate employee_id (keep first occurrence).
           Hint: df.drop_duplicates(subset=["employee_id"], keep="first")

        2. Standardize 'name' — strip whitespace, title case.
           Hint: df["name"].str.strip().str.title()

        3. Normalize 'department' — map messy variants to canonical names.
           Hint: df["department"].str.strip().str.lower().map(self.DEPT_MAP)

        4. Normalize 'office_location' — same pattern as department.
           Hint: use self.LOC_MAP

        5. Convert 'salary' to float — strip "$" and "," first, set negatives to None.
           Hint: write a helper function and use df["salary"].apply(helper)
                 import re; re.sub(r"[$,]", "", str(val)) strips the symbols

        6. Convert 'years_experience' to numeric; set values > 50 to None (outliers).
           Hint: pd.to_numeric(..., errors="coerce")

        7. Convert 'satisfaction_score' to numeric; set values outside 1–10 to None.

        8. Parse 'survey_date' — multiple formats exist (MM/DD/YYYY, YYYY-MM-DD, DD-MM-YYYY).
           Hint: write a helper that tries pd.to_datetime(val, format=fmt) for each format.
                 Formats to try: "%m/%d/%Y", "%Y-%m-%d", "%d-%m-%Y"

        After all steps, reassign self.df = df and print a missing-values summary.

        Returns self so calls can be chained: pipeline.clean().analyze()
        """
        if self.df.empty:
            print("DataFrame is empty; nothing to clean.")
            return self

        df = self.df.copy()

        # 1) Remove duplicate employee IDs, keeping the first row.
        df = df.drop_duplicates(subset=["employee_id"], keep="first")

        # 2) Standardize names.
        df["name"] = df["name"].str.strip().str.title()

        # 3) Normalize department spellings.
        df["department"] = df["department"].str.strip().str.lower().map(self.DEPT_MAP)
        

        # 4) Normalize office location spellings.
        df["office_location"] = df["office_location"].str.strip().str.lower().map(self.LOC_MAP)
        

        # 5) Clean and convert salary.
        def parse_salary(val):
            if pd.isna(val):
                return None
            cleaned = re.sub(r"[$,]", "", str(val)).strip()
            try:
                salary = float(cleaned)
            except ValueError:
                return None
            if salary < 0:
                return None
            return salary

        df["salary"] = df["salary"].apply(parse_salary)

        # 6) Convert years_experience and remove outliers.
        df["years_experience"] = pd.to_numeric(df["years_experience"], errors="coerce")
        df.loc[df["years_experience"] > 50, "years_experience"] = None

        # 7) Convert satisfaction_score and enforce 1-10 bounds.
        df["satisfaction_score"] = pd.to_numeric(df["satisfaction_score"], errors="coerce")
        invalid_satisfaction = (df["satisfaction_score"] < 1) | (df["satisfaction_score"] > 10)
        df.loc[invalid_satisfaction, "satisfaction_score"] = None

        # 8) Parse survey_date with known format variants.
        def parse_date(val):
            if pd.isna(val):
                return pd.NaT
            for fmt in ("%m/%d/%Y", "%Y-%m-%d", "%d-%m-%Y"):
                try:
                    return pd.to_datetime(val, format=fmt)
                except (ValueError, TypeError):
                    continue
            return pd.NaT

        df["survey_date"] = df["survey_date"].apply(parse_date)

        self.df = df
        print("Missing values after cleaning:")
        print(self.df.isna().sum())
        return self

    def analyze(self):
        """Compute summary statistics from the cleaned self.df.

        Compute and print:
        1. Average salary by department
           Hint: df.groupby("department")["salary"].mean().round(0)

        2. Average satisfaction score by department

        3. Headcount by office location
           Hint: df["office_location"].value_counts()

        4. Pearson correlation between years_experience and salary
           Hint: drop rows where either is NaN, then Series.corr()

        5. One additional insight of your choice (e.g., satisfaction by location)

        Return a dict with all results so main.py can use them.
        Keys to use: "avg_salary_by_dept", "avg_satisfaction_by_dept",
                     "headcount_by_location", "experience_salary_correlation",
                     "avg_satisfaction_by_location"
        """
        # Working copy
        df = self.df.copy()
        
        # average salary by department
        average_salary_by_dept = df.groupby("department")["salary"].mean().round(0)
        
        # average satisfaction by department
        average_satisfaction_by_dept = df.groupby("department")["satisfaction_score"].mean().round(0)
        
        # Headcount
        headcount = df["office_location"].value_counts()
        
        # Pearson correlation between experience and salary
        valid_rows = df.dropna(subset=["years_experience", "salary"])
        experience_salary_correlation = valid_rows["years_experience"].corr(valid_rows["salary"])
        
        # Average satisfaction by location
        satisfaction_by_location = df.groupby("office_location")["satisfaction_score"].mean().round(0)
        
        return {
            "avg_salary_by_dept": average_salary_by_dept, 
            "avg_satisfaction_by_dept": average_satisfaction_by_dept,
            "headcount_by_location": headcount, 
            "experience_salary_correlation": experience_salary_correlation,
            "avg_satisfaction_by_location": satisfaction_by_location
        }

    def visualize(self, output_path="output/charts.png"):
        """Create and save visualizations to `output_path`.

        Required charts:
        - Bar chart: average salary by department
        - Histogram: satisfaction score distribution (bins 1–10)
        Bonus:
        - Horizontal bar: headcount by office location

        Use matplotlib with plt.subplots() for a multi-chart layout.
        Save with plt.savefig(output_path, dpi=120, bbox_inches="tight").
        Call plt.close() after saving.

        Hint: import matplotlib; matplotlib.use("Agg") at top of file
              prevents errors when no display is available.

        Args:
            output_path: where to save the PNG file
        """
        if self.df.empty:
            print("DataFrame is empty; no charts were created.")
            return

        try:
            output_dir = os.path.dirname(output_path)
            if output_dir:
                os.makedirs(output_dir, exist_ok=True)

            df = self.df.copy()
            avg_salary = df.groupby("department")["salary"].mean().dropna().sort_values()
            satisfaction = df["satisfaction_score"].dropna()
            headcount = df["office_location"].value_counts()

            fig, axes = plt.subplots(1, 3, figsize=(16, 5))

            avg_salary.plot(kind="bar", ax=axes[0], color="steelblue")
            axes[0].set_title("Average Salary by Department")
            axes[0].set_xlabel("Department")
            axes[0].set_ylabel("Salary")

            bins = [0.5 + i for i in range(0, 11)]
            axes[1].hist(satisfaction, bins=bins, color="seagreen", edgecolor="black")
            axes[1].set_title("Satisfaction Score Distribution")
            axes[1].set_xlabel("Score")
            axes[1].set_ylabel("Count")
            axes[1].set_xticks(range(1, 11))

            headcount.sort_values().plot(kind="barh", ax=axes[2], color="slategray")
            axes[2].set_title("Headcount by Office Location")
            axes[2].set_xlabel("Headcount")
            axes[2].set_ylabel("Office Location")

            plt.tight_layout()
            plt.savefig(output_path, dpi=120, bbox_inches="tight")
            plt.close(fig)
            print(f"Saved charts to: {output_path}")
        except Exception as exc:
            print(f"Could not create charts: {exc}")

    def export(self, output_path="output/clean_employees.csv"):
        """Save the cleaned self.df to a CSV at `output_path`.

        Create the output directory if it doesn't exist.
        Wrap in try/except.

        Hint: df.to_csv(output_path, index=False)

        Args:
            output_path: path for the exported CSV
        """
        if self.df.empty:
            print("DataFrame is empty; nothing to export.")
            return

        try:
            output_dir = os.path.dirname(output_path)
            if output_dir:
                os.makedirs(output_dir, exist_ok=True)
            self.df.to_csv(output_path, index=False)
            print(f"Exported cleaned data to: {output_path}")
        except Exception as exc:
            print(f"Could not export cleaned data: {exc}")

    def run(self):
        """Execute the full pipeline: clean → analyze → visualize → export.

        Build output paths using os.path.join(os.path.dirname(__file__), "output", ...).
        Return the results dict from analyze().
        """
        base_dir = os.path.dirname(__file__)
        output_dir = os.path.join(base_dir, "output")
        charts_path = os.path.join(output_dir, "charts.png")
        clean_csv_path = os.path.join(output_dir, "clean_employees.csv")

        self.clean()
        results = self.analyze()
        self.visualize(charts_path)
        self.export(clean_csv_path)
        return results