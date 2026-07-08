import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import duckdb

def run_trainer_demo():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    clean_csv = os.path.join(base_dir, "employees.csv")
    dirty_csv = os.path.join(base_dir, "employees_dirty.csv")
    db_path = os.path.join(base_dir, "employees.db")

    # Double check files exist, if not generate them
    if not (os.path.exists(clean_csv) and os.path.exists(db_path)):
        print("Data files not found. Generating them first...")
        from generate_data import generate_datasets
        generate_datasets()

    print("=" * 60)
    print(" RETAILMAX HR ANALYTICS SYSTEM v4.0 - LIVE DEMO ")
    print("=" * 60)

    # -------------------------------------------------------------
    # SPRINT 1: Loading Data
    # -------------------------------------------------------------
    print("\n--- SPRINT 1: Loading Data ---")
    
    # Method A: Loading from CSV
    print("Loading data from CSV...")
    df_csv = pd.read_csv(clean_csv)
    print(f"Loaded {len(df_csv)} records from CSV.")
    
    # Method B: Loading from SQLite Database
    print("Loading data from SQLite Database...")
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM employees", conn)
    conn.close()
    print(f"Loaded {len(df)} records from SQLite database.")

    # -------------------------------------------------------------
    # SPRINT 2: Explore Data
    # -------------------------------------------------------------
    print("\n--- SPRINT 2: Explore Data ---")
    print("1. df.head(): First 3 records:")
    print(df.head(3))
    
    print("\n2. df.tail(): Last 3 records:")
    print(df.tail(3))
    
    print(f"\n3. df.shape: {df.shape} (Rows: {df.shape[0]}, Columns: {df.shape[1]})")
    print(f"4. df.columns: {list(df.columns)}")
    
    print("\n5. df.info():")
    df.info()
    
    print("\n6. df.describe() (Summary statistics for numerical columns):")
    print(df.describe())

    # -------------------------------------------------------------
    # SPRINT 3: Data Cleaning
    # -------------------------------------------------------------
    print("\n--- SPRINT 3: Data Cleaning ---")
    print("Loading dirty data for cleaning simulation...")
    df_dirty = pd.read_csv(dirty_csv)
    print(f"Dirty Data Shape: {df_dirty.shape}")
    
    # Identify issues
    print("\nDetecting missing salaries (df['Salary'].isnull().sum()):")
    print(df_dirty["Salary"].isnull().sum())
    
    print("\nDetecting duplicate EmployeeIDs (df_dirty.duplicated(subset=['EmployeeID']).sum()):")
    print(df_dirty.duplicated(subset=["EmployeeID"]).sum())
    
    # Perform cleanups
    print("\nCleaning data...")
    # Drop duplicates
    df_cleaned = df_dirty.drop_duplicates(subset=["EmployeeID"], keep="first").copy()
    # Handle missing salaries by filling them with the median salary
    median_sal = df_cleaned["Salary"].median()
    print(f"Filling missing salaries with median salary: {median_sal}")
    df_cleaned["Salary"] = df_cleaned["Salary"].fillna(median_sal)
    
    print(f"Cleaned Data Shape: {df_cleaned.shape}")

    # -------------------------------------------------------------
    # SPRINT 4: HR Analytics
    # -------------------------------------------------------------
    print("\n--- SPRINT 4: HR Analytics (Clean SQLite Data) ---")
    total_employees = len(df)
    avg_salary = df["Salary"].mean()
    max_salary = df["Salary"].max()
    min_salary = df["Salary"].min()
    dept_counts = df.groupby("Department").size()
    
    print(f"Total Employees: {total_employees}")
    print(f"Average Salary: ${avg_salary:.2f}")
    print(f"Highest Salary: ${max_salary:,}")
    print(f"Lowest Salary: ${min_salary:,}")
    print("\nEmployees per Department:")
    print(dept_counts)

    # -------------------------------------------------------------
    # SPRINT 5: Filtering
    # -------------------------------------------------------------
    print("\n--- SPRINT 5: Filtering ---")
    finance_employees = df[df["Department"] == "Finance"]
    print(f"Employees in Finance: {len(finance_employees)}")
    
    high_earners = df[df["Salary"] > 100000]
    print(f"Employees earning > $100,000: {len(high_earners)}")
    
    high_perf_finance = df[(df["Department"] == "Finance") & (df["PerformanceScore"] >= 4)]
    print(f"High-performing (Score >= 4) Finance employees: {len(high_perf_finance)}")

    # -------------------------------------------------------------
    # SPRINT 6: Sorting
    # -------------------------------------------------------------
    print("\n--- SPRINT 6: Sorting ---")
    print("Top 5 highest paid employees:")
    top_paid = df.sort_values(by="Salary", ascending=False).head(5)
    print(top_paid[["Name", "Department", "Salary"]])
    
    print("\nUsing df.nlargest(3, 'Salary'):")
    print(df.nlargest(3, "Salary")[["Name", "Department", "Salary"]])

    # -------------------------------------------------------------
    # SPRINT 7: Visualization
    # -------------------------------------------------------------
    print("\n--- SPRINT 7: Visualization ---")
    # A. Department counts bar chart
    plt.figure(figsize=(8, 4))
    df["Department"].value_counts().plot(kind="bar", color="skyblue", edgecolor="black")
    plt.title("Employee Count by Department")
    plt.xlabel("Department")
    plt.ylabel("Count")
    plt.tight_layout()
    chart1_path = os.path.join(base_dir, "department_counts.png")
    plt.savefig(chart1_path)
    plt.close()
    print(f"Saved Department Count Bar Chart to: {chart1_path}")

    # B. Salary distribution hist/pie chart
    plt.figure(figsize=(6, 6))
    df.groupby("Department")["Salary"].mean().plot(kind="pie", autopct="%1.1f%%", startangle=90, colors=["gold", "lightgreen", "lightcoral", "lightskyblue", "violet"])
    plt.title("Share of Average Salary by Department")
    plt.ylabel("")
    plt.tight_layout()
    chart2_path = os.path.join(base_dir, "salary_pie_chart.png")
    plt.savefig(chart2_path)
    plt.close()
    print(f"Saved Average Salary Pie Chart to: {chart2_path}")

    # -------------------------------------------------------------
    # SPRINT 8: Export Report
    # -------------------------------------------------------------
    print("\n--- SPRINT 8: Export Report ---")
    report_csv = os.path.join(base_dir, "report.csv")
    report_xlsx = os.path.join(base_dir, "report.xlsx")
    
    # Export clean data summary to CSV & Excel
    df.to_csv(report_csv, index=False)
    print(f"Exported CSV report to: {report_csv}")
    
    df.to_excel(report_xlsx, index=False)
    print(f"Exported Excel report to: {report_xlsx}")

    # -------------------------------------------------------------
    # ADDITIONAL TOPIC 1: Comparing Data Tools (Pandas vs. DuckDB)
    # -------------------------------------------------------------
    print("\n--- ADDITIONAL TOPIC 1: Comparing Data Tools ---")
    print("Business Query: Calculate Average Salary & Headcount per Department")
    
    # Pandas implementation
    pandas_result = df.groupby("Department")["Salary"].agg(
        AverageSalary="mean",
        Headcount="count"
    ).reset_index()
    print("\n[Pandas Result]")
    print(pandas_result)
    
    # DuckDB implementation (Running SQL directly on the local Pandas DataFrame!)
    duckdb_result = duckdb.query("""
        SELECT 
            Department, 
            AVG(Salary) AS AverageSalary, 
            COUNT(*) AS Headcount
        FROM df 
        GROUP BY Department
        ORDER BY Department
    """).to_df()
    print("\n[DuckDB Result]")
    print(duckdb_result)

    # -------------------------------------------------------------
    # ADDITIONAL TOPIC 2: Data Contracts
    # -------------------------------------------------------------
    print("\n--- ADDITIONAL TOPIC 2: Data Contracts ---")
    print("Validating 'employees_dirty.csv' against quality rules...")
    
    # 1. Load raw data (making sure EmployeeID is loaded as string or checked for nulls properly)
    df_raw = pd.read_csv(dirty_csv)
    
    valid_departments = ["HR", "Engineering", "Finance", "Sales", "Marketing"]
    violations = []
    
    # Rule 1: Missing Employee IDs
    missing_id_rows = df_raw[df_raw["EmployeeID"].isnull()]
    if len(missing_id_rows) > 0:
        violations.append(f"CRITICAL: Found {len(missing_id_rows)} record(s) with missing EmployeeID.")
        print(f"-> Missing ID violations (Indices): {list(missing_id_rows.index)}")
        
    # Rule 2: Duplicate Employee IDs
    # Exclude null IDs from duplicate check
    non_null_ids = df_raw[df_raw["EmployeeID"].notnull()]
    duplicate_ids = non_null_ids[non_null_ids.duplicated(subset=["EmployeeID"], keep=False)]
    if len(duplicate_ids) > 0:
        violations.append(f"WARNING: Found {len(duplicate_ids)} record(s) with duplicate EmployeeIDs.")
        print(f"-> Duplicate ID violations:\n{duplicate_ids[['EmployeeID', 'Name']]}")

    # Rule 3: Negative salaries
    # We cast to numeric first (empty strings become NaN)
    salaries_numeric = pd.to_numeric(df_raw["Salary"], errors="coerce")
    negative_salary_rows = df_raw[salaries_numeric < 0]
    if len(negative_salary_rows) > 0:
        violations.append(f"CRITICAL: Found {len(negative_salary_rows)} record(s) with negative salaries.")
        print(f"-> Negative salary violations:\n{negative_salary_rows[['EmployeeID', 'Name', 'Salary']]}")

    # Rule 4: Invalid departments
    invalid_dept_rows = df_raw[~df_raw["Department"].isin(valid_departments) & df_raw["Department"].notnull()]
    if len(invalid_dept_rows) > 0:
        violations.append(f"WARNING: Found {len(invalid_dept_rows)} record(s) with invalid departments.")
        print(f"-> Invalid department violations:\n{invalid_dept_rows[['EmployeeID', 'Name', 'Department']]}")

    print("\n=== Data Contract Summary ===")
    if violations:
        print(f"Data contract verification FAILED! Details:")
        for v in violations:
            print(f"- {v}")
    else:
        print("Data contract verification PASSED! Clean data.")
        
    print("=" * 60)

if __name__ == "__main__":
    run_trainer_demo()
