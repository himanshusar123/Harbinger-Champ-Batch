import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# =====================================================================
# RetailMax HR Dashboard Mini-Project Solution (Sprint 9)
# =====================================================================

def load_data(file_path: str) -> pd.DataFrame:
    """
    Loads data from either a CSV file or SQLite database.
    If database, loads from the 'employees' table.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Source file not found at: {file_path}")
        
    _, ext = os.path.splitext(file_path.lower())
    
    if ext == ".csv":
        print(f"Loading data from CSV: {file_path}")
        return pd.read_csv(file_path)
    elif ext in [".db", ".sqlite", ".sqlite3"]:
        print(f"Loading data from SQLite DB: {file_path}")
        conn = sqlite3.connect(file_path)
        try:
            df = pd.read_sql_query("SELECT * FROM employees", conn)
        finally:
            conn.close()
        return df
    else:
        raise ValueError(f"Unsupported file extension: {ext}. Only CSV and SQLite databases (.db, .sqlite) are supported.")

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the dataset by:
    1. Removing records with null EmployeeID.
    2. Converting Salary to numeric, filling missing values with the median.
    3. Dropping duplicates on EmployeeID (keeping the first occurrence).
    """
    df_clean = df.copy()
    
    # 1. Clean missing EmployeeIDs
    initial_len = len(df_clean)
    df_clean = df_clean.dropna(subset=["EmployeeID"])
    # Cast EmployeeID to integer for clean representation
    df_clean["EmployeeID"] = df_clean["EmployeeID"].astype(int)
    dropped_ids = initial_len - len(df_clean)
    if dropped_ids > 0:
        print(f"-> Dropped {dropped_ids} records due to missing EmployeeID.")
        
    # 2. Clean Salary (Convert to numeric first, handle missing/invalid)
    df_clean["Salary"] = pd.to_numeric(df_clean["Salary"], errors="coerce")
    median_salary = df_clean["Salary"].median()
    null_salaries = df_clean["Salary"].isnull().sum()
    if null_salaries > 0:
        print(f"-> Filling {null_salaries} missing/invalid salaries with median: ${median_salary:,.2f}")
        df_clean["Salary"] = df_clean["Salary"].fillna(median_salary)
    df_clean["Salary"] = df_clean["Salary"].astype(float)

    # 3. Clean duplicates
    before_dup = len(df_clean)
    df_clean = df_clean.drop_duplicates(subset=["EmployeeID"], keep="first")
    dropped_dups = before_dup - len(df_clean)
    if dropped_dups > 0:
        print(f"-> Dropped {dropped_dups} duplicate records based on EmployeeID.")
        
    # Reset index for clean DataFrame structure
    df_clean = df_clean.reset_index(drop=True)
    return df_clean

def validate_data_contract(df: pd.DataFrame) -> bool:
    """
    Validates data against agreed quality rules:
    - No null EmployeeID
    - No negative Salary
    - No invalid Departments (Only HR, Engineering, Finance, Sales, Marketing are allowed)
    
    Returns:
        bool: True if data passes all contracts, False otherwise.
    """
    valid_departments = ["HR", "Engineering", "Finance", "Sales", "Marketing"]
    passed = True
    
    print("\n--- Data Contract Verification ---")
    
    # Rule 1: No missing IDs
    missing_ids = df["EmployeeID"].isnull().sum()
    if missing_ids > 0:
        print(f"[FAIL] Rule 1: Missing EmployeeID check failed. Found {missing_ids} record(s).")
        passed = False
    else:
        print("[PASS] Rule 1: No missing EmployeeIDs.")

    # Rule 2: No duplicate IDs
    duplicate_ids = df.duplicated(subset=["EmployeeID"]).sum()
    if duplicate_ids > 0:
        print(f"[FAIL] Rule 2: Duplicate EmployeeID check failed. Found {duplicate_ids} record(s).")
        passed = False
    else:
        print("[PASS] Rule 2: No duplicate EmployeeIDs.")

    # Rule 3: No negative salaries
    negative_salaries = (df["Salary"] < 0).sum()
    if negative_salaries > 0:
        print(f"[FAIL] Rule 3: Salary non-negativity check failed. Found {negative_salaries} record(s) with negative salaries.")
        print(df[df["Salary"] < 0][["EmployeeID", "Name", "Salary"]])
        passed = False
    else:
        print("[PASS] Rule 3: No negative salaries.")

    # Rule 4: Valid departments
    invalid_dept_mask = ~df["Department"].isin(valid_departments)
    invalid_dept_count = invalid_dept_mask.sum()
    if invalid_dept_count > 0:
        print(f"[FAIL] Rule 4: Department verification failed. Found {invalid_dept_count} record(s) with invalid departments.")
        print(df[invalid_dept_mask][["EmployeeID", "Name", "Department"]])
        passed = False
    else:
        print("[PASS] Rule 4: All departments are valid.")
        
    return passed

def generate_kpis(df: pd.DataFrame) -> dict:
    """
    Computes key performance indicators:
    - Total Headcount
    - Average Salary
    - Max Salary
    - Min Salary
    - Average Performance Score
    """
    return {
        "Total Headcount": len(df),
        "Average Salary": f"${df['Salary'].mean():,.2f}",
        "Max Salary": f"${df['Salary'].max():,.2f}",
        "Min Salary": f"${df['Salary'].min():,.2f}",
        "Average Performance Score": round(df["PerformanceScore"].mean(), 2)
    }

def generate_charts(df: pd.DataFrame, output_dir: str) -> None:
    """
    Generates and saves visual charts:
    1. Bar chart: Headcount by Department
    2. Pie chart: Total salary expenses by Department
    3. Histogram: Distribution of employee salaries
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Bar Chart: Headcount by Department
    plt.figure(figsize=(8, 4))
    dept_headcount = df["Department"].value_counts()
    dept_headcount.plot(kind="bar", color="#4e73df", edgecolor="black")
    plt.title("Headcount by Department", fontsize=14, fontweight="bold")
    plt.xlabel("Department", fontsize=11)
    plt.ylabel("Number of Employees", fontsize=11)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    chart1_path = os.path.join(output_dir, "headcount_by_dept.png")
    plt.savefig(chart1_path)
    plt.close()
    print(f"Saved: {chart1_path}")

    # 2. Pie Chart: Total Salary Expenses by Department
    plt.figure(figsize=(6, 6))
    dept_salaries = df.groupby("Department")["Salary"].sum()
    dept_salaries.plot(kind="pie", autopct="%1.1f%%", startangle=140, 
                       colors=["#4e73df", "#1cc88a", "#36b9cc", "#f6c23e", "#e74a3b"])
    plt.title("Total Salary Expenses by Department", fontsize=14, fontweight="bold")
    plt.ylabel("")
    plt.tight_layout()
    chart2_path = os.path.join(output_dir, "salary_expenses_by_dept.png")
    plt.savefig(chart2_path)
    plt.close()
    print(f"Saved: {chart2_path}")

    # 3. Histogram: Distribution of Salaries
    plt.figure(figsize=(8, 4))
    plt.hist(df["Salary"], bins=15, color="#1cc88a", edgecolor="black", alpha=0.8)
    plt.title("Salary Distribution of Employees", fontsize=14, fontweight="bold")
    plt.xlabel("Salary ($)", fontsize=11)
    plt.ylabel("Frequency", fontsize=11)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    chart3_path = os.path.join(output_dir, "salary_distribution.png")
    plt.savefig(chart3_path)
    plt.close()
    print(f"Saved: {chart3_path}")

def export_report(df: pd.DataFrame, output_csv: str, output_excel: str) -> None:
    """
    Exports the final cleaned and sorted DataFrame to CSV and Excel.
    """
    # Sort by Salary descending for business reporting convenience
    df_sorted = df.sort_values(by="Salary", ascending=False)
    
    # Save CSV
    df_sorted.to_csv(output_csv, index=False)
    print(f"Exported clean report to CSV: {output_csv}")
    
    # Save Excel (requires openpyxl)
    df_sorted.to_excel(output_excel, index=False, sheet_name="HR Analytics Report")
    print(f"Exported clean report to Excel: {output_excel}")

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(base_dir, "employees_dirty.csv")
    
    # Make sure datasets exist
    if not os.path.exists(input_file):
        print("Data files not found. Running generator script first...")
        from generate_data import generate_datasets
        generate_datasets()
        
    print("=" * 60)
    print(" RUNNING MINI-PROJECT PIPELINE - RETAILMAX HR DASHBOARD ")
    print("=" * 60)
    
    # 1. Load data
    df_raw = load_data(input_file)
    print(f"Raw data loaded: {df_raw.shape[0]} rows, {df_raw.shape[1]} columns.")
    
    # 2. Clean data
    print("\nRunning cleaning module...")
    df_cleaned = clean_data(df_raw)
    print(f"Data cleaned. Working row count: {len(df_cleaned)}")
    
    # 3. Validate Data Contracts
    contract_passed = validate_data_contract(df_cleaned)
    print(f"\nFinal Cleaned Data Contract Passed? {contract_passed}")
    
    # 4. Generate KPIs
    kpis = generate_kpis(df_cleaned)
    print("\n--- Executive KPIs Summary ---")
    for k, v in kpis.items():
        print(f"  {k:<30}: {v}")
        
    # 5. Generate Charts
    print("\nGenerating charts and visualizations...")
    generate_charts(df_cleaned, base_dir)
    
    # 6. Export Reports
    print("\nExporting executive reports...")
    out_csv = os.path.join(base_dir, "final_hr_report.csv")
    out_xlsx = os.path.join(base_dir, "final_hr_report.xlsx")
    export_report(df_cleaned, out_csv, out_xlsx)
    
    print("\n" + "=" * 60)
    print(" HR DASHBOARD PIPELINE COMPLETED SUCCESSFULLY! ")
    print("=" * 60)

if __name__ == "__main__":
    main()
