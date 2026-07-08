import csv
import sqlite3
import random
import os
from datetime import datetime, timedelta

def generate_datasets():
    # Setup paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    clean_csv_path = os.path.join(base_dir, "employees.csv")
    dirty_csv_path = os.path.join(base_dir, "employees_dirty.csv")
    sqlite_db_path = os.path.join(base_dir, "employees.db")

    print("Generating clean dataset...")
    
    first_names = ["John", "Jane", "Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah", 
                   "Ian", "Julia", "Kevin", "Laura", "Michael", "Nina", "Oscar", "Penelope", "Quincy", "Rachel"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Rodriguez", "Wilson",
                  "Martinez", "Anderson", "Taylor", "Thomas", "Hernandez", "Moore", "Martin", "Jackson", "Thompson", "White"]
    
    departments = ["HR", "Engineering", "Finance", "Sales", "Marketing"]
    roles = {
        "HR": ["HR Associate", "HR Manager", "Recruiter", "HR Director"],
        "Engineering": ["Software Engineer", "Senior Developer", "QA Analyst", "Engineering Manager"],
        "Finance": ["Financial Analyst", "Accountant", "Finance Manager", "Finance Director"],
        "Sales": ["Sales Associate", "Sales Manager", "Account Executive", "Sales Director"],
        "Marketing": ["Marketing Analyst", "SEO Specialist", "Marketing Manager", "Marketing Director"]
    }

    # Generate 1000 clean records
    clean_employees = []
    start_date = datetime(2020, 1, 1)
    
    # Consistent seed for reproducibility
    random.seed(42)

    for emp_id in range(1001, 2001):
        dept = random.choice(departments)
        role = random.choice(roles[dept])
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        name = f"{first_name} {last_name}"
        salary = random.randint(45000, 125000)
        
        # Random date in last 5 years
        random_days = random.randint(0, 1800)
        join_date = (start_date + timedelta(days=random_days)).strftime("%Y-%m-%d")
        perf_score = random.randint(1, 5)
        
        clean_employees.append({
            "EmployeeID": emp_id,
            "Name": name,
            "Department": dept,
            "Role": role,
            "Salary": salary,
            "JoiningDate": join_date,
            "PerformanceScore": perf_score
        })

    # Write clean CSV
    with open(clean_csv_path, mode="w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=clean_employees[0].keys())
        writer.writeheader()
        writer.writerows(clean_employees)
    print(f"Created clean dataset at: {clean_csv_path}")

    # Write clean SQLite Database
    if os.path.exists(sqlite_db_path):
        os.remove(sqlite_db_path)
    conn = sqlite3.connect(sqlite_db_path)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE employees (
            EmployeeID INTEGER PRIMARY KEY,
            Name TEXT,
            Department TEXT,
            Role TEXT,
            Salary INTEGER,
            JoiningDate TEXT,
            PerformanceScore INTEGER
        )
    """)
    for emp in clean_employees:
        cursor.execute("""
            INSERT INTO employees (EmployeeID, Name, Department, Role, Salary, JoiningDate, PerformanceScore)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (emp["EmployeeID"], emp["Name"], emp["Department"], emp["Role"], emp["Salary"], emp["JoiningDate"], emp["PerformanceScore"]))
    conn.commit()
    conn.close()
    print(f"Created SQLite database at: {sqlite_db_path}")

    # Generate dirty dataset for Sprint 3 and Data Contracts validation
    print("Generating dirty dataset...")
    dirty_employees = []
    for emp in clean_employees[:100]:  # Use first 100 rows as starting point
        dirty_employees.append(emp.copy())

    # 1. Inject duplicate rows (same EmployeeID)
    for i in range(5):
        dup_row = dirty_employees[i].copy()
        dirty_employees.append(dup_row)

    # 2. Inject missing salaries
    for i in range(5, 10):
        dirty_employees[i]["Salary"] = ""

    # 3. Inject negative salaries
    for i in range(10, 15):
        dirty_employees[i]["Salary"] = -1 * abs(dirty_employees[i]["Salary"])

    # 4. Inject missing EmployeeID
    for i in range(15, 20):
        dirty_employees[i]["EmployeeID"] = ""

    # 5. Inject invalid department names (typos)
    typos = {20: "Financcce", 21: "Engg", 22: "HRRR", 23: "Sales&Marketing", 24: "Marketin"}
    for idx, bad_dept in typos.items():
        dirty_employees[idx]["Department"] = bad_dept

    # Write dirty CSV
    with open(dirty_csv_path, mode="w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=dirty_employees[0].keys())
        writer.writeheader()
        writer.writerows(dirty_employees)
    print(f"Created dirty dataset at: {dirty_csv_path}")

if __name__ == "__main__":
    generate_datasets()
