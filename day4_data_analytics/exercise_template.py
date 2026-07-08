import os
import pandas as pd
import matplotlib.pyplot as plt

# =====================================================================
# RetailMax HR Dashboard Mini-Project Template (Sprint 9)
# =====================================================================
# Target: Create a fully automated pipeline that:
# 1. Loads data (CSV or SQLite)
# 2. Validates data contracts (ID check, non-negative salary, valid depts)
# 3. Cleans dirty records (duplicates, missing salaries)
# 4. Computes executive KPIs
# 5. Generates business charts
# 6. Exports management reports
# =====================================================================

def load_data(file_path: str) -> pd.DataFrame:
    """
    Loads data from either a CSV file or SQLite database.
    If database, loads from the 'employees' table.
    """
    # TODO: Implement database loading and CSV loading
    # Hint: Use pd.read_csv() or sqlite3/pd.read_sql_query() based on file extension
    pass

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the dataset by:
    1. Removing duplicate rows based on EmployeeID (keeping the first occurrence).
    2. Filling missing Salaries with the median salary of the dataset.
    3. Ensuring appropriate data types (e.g. Salary as numeric, EmployeeID as integer/string).
    """
    # TODO: Remove duplicates, handle missing salaries, cast types
    pass

def validate_data_contract(df: pd.DataFrame) -> bool:
    """
    Validates data against agreed quality rules:
    - No null EmployeeID
    - No negative Salary
    - No invalid Departments (Only HR, Engineering, Finance, Sales, Marketing are allowed)
    
    Returns:
        bool: True if data passes all contracts, False otherwise.
    """
    # TODO: Implement contract validation checks
    # Print warnings for any violations found.
    pass

def generate_kpis(df: pd.DataFrame) -> dict:
    """
    Computes key performance indicators:
    - Total Headcount
    - Average Salary
    - Max Salary
    - Min Salary
    - Median Performance Score
    """
    # TODO: Compute KPIs using Pandas aggregation methods
    pass

def generate_charts(df: pd.DataFrame, output_dir: str) -> None:
    """
    Generates and saves visual charts:
    1. Bar chart: Headcount by Department
    2. Pie chart: Total salary expenses by Department
    3. Histogram: Distribution of employee salaries
    """
    # TODO: Create charts using matplotlib and save them as PNGs in output_dir
    pass

def export_report(df: pd.DataFrame, output_csv: str, output_excel: str) -> None:
    """
    Exports the final cleaned and sorted DataFrame to CSV and Excel.
    """
    # TODO: Write code to export files using df.to_csv() and df.to_excel()
    pass

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(base_dir, "employees_dirty.csv")  # Change to employees.csv or database to test clean flow
    
    print("=== STARTING HR PIPELINE ===")
    
    # 1. Load data
    print(f"Loading data from: {input_file}")
    # df = load_data(input_file)
    
    # 2. Clean data
    # df_cleaned = clean_data(df)
    
    # 3. Validate Data Contracts
    # contract_passed = validate_data_contract(df_cleaned)
    # print(f"Data Contract Passed: {contract_passed}")
    
    # 4. Generate KPIs
    # kpis = generate_kpis(df_cleaned)
    # print("\n--- Executive KPIs ---")
    # for k, v in kpis.items():
    #     print(f"{k}: {v}")
        
    # 5. Generate Charts
    # print(f"Generating charts in directory: {base_dir}")
    # generate_charts(df_cleaned, base_dir)
    
    # 6. Export Reports
    # out_csv = os.path.join(base_dir, "final_hr_report.csv")
    # out_xlsx = os.path.join(base_dir, "final_hr_report.xlsx")
    # export_report(df_cleaned, out_csv, out_xlsx)
    
    print("=== PIPELINE RUN COMPLETE ===")

if __name__ == "__main__":
    main()
