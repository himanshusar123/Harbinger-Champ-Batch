# Day 4: Data Analytics & Business Intelligence with Pandas

## Theme: "From Data Storage to Business Intelligence"
### Duration: 8 Hours | Workspace Setup & Trainer Guide

Welcome to **Day 4** of the RetailMax training program. Today, we shift focus from **software engineering & storage** (CSV, SQLite) to **data engineering, analytics, and business intelligence**. Participants will learn how to turn raw employee data into actionable insights for the executive board.

---

## 📅 Course Agenda (8-Hour Breakdown)

| Time | Module / Sprint | Focus Areas | Key Deliverables |
| :--- | :--- | :--- | :--- |
| **09:00 - 09:30** | **The CTO's Pitch & Intro to BI** | Moving from storage to insights; loops vs. Pandas vectorization; BI pipeline. | Introduction & Interactive Discussion. |
| **09:30 - 10:30** | **Sprint 1 & 2: Load & Explore** | Loading from CSV & SQLite (`pd.read_csv`, `pd.read_sql_query`); Exploring structure (`info`, `describe`). | Code-along: Database load & descriptive profiling. |
| **10:30 - 11:30** | **Sprint 3: Data Cleaning** | Dealing with duplicates (`drop_duplicates`) and missing values (`fillna`, `isnull`). | Code-along: Cleaning dirty data imports. |
| **11:30 - 12:30** | **Sprint 4 & 5: HR Analytics & Filtering** | Aggregate functions (`mean`, `max`, `min`, `groupby`); Boolean indexing filters. | Code-along: Answering HR Director's questions. |
| **12:30 - 13:00** | **Sprint 6: Sorting & Ranking** | Ordering by salary (`sort_values`, `nlargest`). | Code-along: Identifying top earners. |
| **13:00 - 14:00** | *Lunch Break* | *Networking and informal discussion* | - |
| **14:00 - 14:45** | **Sprint 7: Data Visualization** | Matplotlib chart generation (Bar, Pie, Histograms). | Code-along: Outputting chart PNGs. |
| **14:45 - 15:15** | **Sprint 8: Exporting Reports** | Generating output files (`to_csv`, `to_excel`). | Code-along: Generating XLSX reports. |
| **15:15 - 16:15** | **Special Topics: Tools & Contracts** | Comparing Pandas vs. Polars vs. DuckDB; Setting up Data Contracts. | Code-together: DuckDB SQL query, Pandas validation contract. |
| **16:15 - 17:30** | **Sprint 9: Mini-Project Challenge** | Build **RetailMax HR Dashboard v4.0** pipeline from template. | Hand-on Challenge: Complete `exercise_template.py`. |
| **17:30 - 18:00** | **Sprint 10: CEO Presentations & Reflection** | Presentations of business insights discovered. | Reflection and preview of Tomorrow (Pipelines & Airflow). |

---

## 👩‍🏫 Trainer Script & Storyline

### 9:00 AM — The CTO's Morning Briefing

> **Trainer Script:**
> *"Good morning Team! Congratulations on yesterday's work. We successfully migrated our HR database to SQLite, and the HR Director is absolutely thrilled with the clean storage.*
>
> *But today... things change. The CEO has just contacted us. RetailMax is expanding to 500 stores, which means we now have 15,000 employees.*
>
> *The CEO doesn't want to see 15,000 individual records. The CEO needs to make decisions: Where should we recruit? Which departments have the highest salary bills? Which locations need attention?*
>
> *Today, we are moving **from Data Storage to Business Intelligence**."*

#### Visual Board Drawing:
```text
  RetailMax
  (500 Stores)
      │
      ▼
  15,000 Employees
      │
      ▼
   CEO Needs Insights (KPIs, Charts, Trends) 
   NOT Raw Data Rows!
```

---

## 🧠 Core Concepts Explained

### 1. The BI Value Chain
Explain to trainees how data matures into decisions:
```text
  Raw Data (SQLite/CSV) ──► Information (KPIs/Stats) ──► Insights (Trends/Charts) ──► Business Decisions
```
* **Yesterday (Day 3):** We focused on storing and updating raw data.
* **Today (Day 4):** We extract information, visualize insights, and present recommendations to executives.

### 2. Why Pandas? Vectorization vs. Loops
Ask the trainees: *"How would we find all employees in the Finance department in vanilla Python?"*
They will likely suggest writing a loop with an `if` condition.

Explain the loop complexity:
```python
# The Old Way (Slow, verbose, CPU-intensive loops)
finance_employees = []
for row in employee_database:
    if row['Department'] == 'Finance':
        finance_employees.append(row)
```

Show them the Pandas way:
```python
# The Pandas Way (Vectorized, fast C-under-the-hood, single line)
df[df["Department"] == "Finance"]
```
Pandas utilizes **vectorized operations** to perform calculations across entire arrays instantly, bypassing slower Python loops.

---

## 🏃‍♂️ Sprints Breakdown

### Sprint 1: Loading Data
Participants learn to read data from different storage types:
* **CSV:** `pd.read_csv("employees.csv")`
* **SQLite:** `pd.read_sql_query("SELECT * FROM employees", sqlite3.connect("employees.db"))`

### Sprint 2: Explore Data
Before analyzing, we must inspect the dataset's shape, types, and summary statistics:
```python
df.head()      # Preview top 5 rows
df.tail()      # Preview bottom 5 rows
df.shape       # Check dimension tuple (rows, cols)
df.columns     # Get column name list
df.info()      # Check data types and non-null counts
df.describe()  # Output statistical descriptions (mean, min, max, std)
```

### Sprint 3: Data Cleaning
Explain the phrase **"Garbage In, Garbage Out"**. If the source data is dirty, the executive dashboard will lie.
* **Detecting Nulls:** `df.isnull().sum()`
* **Detecting Duplicates:** `df.duplicated().sum()`
* **Dropping Duplicates:** `df.drop_duplicates(subset=["EmployeeID"], keep="first")`
* **Filling Nulls:** `df["Salary"].fillna(median_salary)`

### Sprint 4: HR Analytics
Learn basic aggregations:
* Headcount: `len(df)`
* Salary stats: `df["Salary"].mean()`, `df["Salary"].max()`, `df["Salary"].min()`
* Department breakdown: `df.groupby("Department").size()`

### Sprint 5: Filtering
Retrieve sub-segments of data using boolean masking:
* `df[df["Department"] == "Finance"]`
* `df[df["Salary"] > 70000]`
* Composite filters: `df[(df["Salary"] > 70000) & (df["Department"] == "Finance")]`

### Sprint 6: Sorting
* Sort table: `df.sort_values(by="Salary", ascending=False)`
* Find top earners: `df.nlargest(10, "Salary")`

### Sprint 7: Visualization
The CEO wants charts, not text tables. Introduce `matplotlib.pyplot`:
* **Bar Chart:** Headcount by Department
* **Pie Chart:** Expense share by Department
* **Histogram:** Salary distribution

### Sprint 8: Export Report
* Write to CSV: `df.to_csv("report.csv", index=False)`
* Write to Excel: `df.to_excel("report.xlsx", index=False)`

---

## 🚀 Additional Professional Topics

### 1. Comparing Data Tools

Trainees will encounter other popular tools in the data engineering ecosystem. Use this comparison table:

| Tool | Best Use Case | Performance Characteristics |
| :--- | :--- | :--- |
| **Pandas** | General data analysis, medium datasets (< 2GB). | In-memory, single-threaded, easy-to-use API. |
| **Polars** | High-performance, large datasets (> 2GB). | In-memory, multi-threaded (Rust core), lazy evaluation support. |
| **DuckDB** | Running SQL queries directly on local files (CSV, Parquet, JSON) or DataFrames. | Serverless, vectorized query execution, highly optimized for analytical queries (OLAP). |

#### DuckDB Integration Example:
DuckDB can execute SQL queries directly on a Pandas DataFrame:
```python
import duckdb
# Query df directly as if it were a SQL table!
avg_salary_df = duckdb.query("""
    SELECT Department, AVG(Salary) as AvgSal 
    FROM df 
    GROUP BY Department
""").to_df()
```

### 2. Data Contracts
Before ingestion into the analytics pipeline, data must pass validation rules (contracts) to ensure quality.

**Contract Rules for RetailMax HR System:**
1. **EmployeeID:** Must be present (non-null) and unique (no duplicates).
2. **Salary:** Must be positive (greater than 0).
3. **Department:** Must belong to the list of approved corporate departments: `["HR", "Engineering", "Finance", "Sales", "Marketing"]`.

*Note for Trainees:* Enterprise tools like `Pandera` or `Great Expectations` are used for production data contracts, but simple assertions and boolean filters in Pandas work well for lightweight pipelines.

---

## 📝 Multiple-Choice Questions (MCQs) for Assessment

**1. Why are vectorized operations in Pandas preferred over standard Python loops for large datasets?**
- A) They use less disk storage.
- B) They execute operations in optimized C under the hood, running operations in parallel across arrays rather than element-by-element in Python.
- C) They automatically write data to a database.
- D) They do not support missing data.
- *Answer: B*

**2. Which command would you use to find the count of non-null values and data types of all columns in a DataFrame?**
- A) `df.describe()`
- B) `df.shape`
- C) `df.info()`
- D) `df.columns`
- *Answer: C*

**3. What does the `df.drop_duplicates(subset=["EmployeeID"], keep="first")` operation do?**
- A) It deletes the entire dataset except the first row.
- B) It deletes the EmployeeID column.
- C) It removes rows with duplicate EmployeeIDs, retaining only the first occurrence in the dataset.
- D) It throws an error if duplicates are found.
- *Answer: C*

**4. How does DuckDB query a Pandas DataFrame in a Python script?**
- A) DuckDB uploads the DataFrame to an external cloud database server.
- B) DuckDB converts the DataFrame into a CSV file, then runs SQL queries on the file.
- C) DuckDB queries the Pandas DataFrame in-memory using its serverless vectorized SQL engine directly.
- D) DuckDB requires you to install PostgreSQL first.
- *Answer: C*

**5. What is the main objective of a Data Contract in a data pipeline?**
- A) To encrypt files before sending them over the network.
- B) To enforce predefined schema and quality rules on raw incoming data before it is ingested by the analytics pipeline.
- C) To manage employee payroll contracts automatically.
- D) To speed up SQL queries.
- *Answer: B*

---

## 🏁 Summary of Deliverables for Day 4
By the end of the day, trainees will have written:
1. `generate_data.py` (Script to establish training data).
2. `code_together.py` (Complete code-along implementation of Sprints 1-8, DuckDB, and Data Contracts).
3. `final_hr_report.csv` & `final_hr_report.xlsx` (Exported corporate reports).
4. `headcount_by_dept.png`, `salary_expenses_by_dept.png`, `salary_distribution.png` (Visualization assets).
5. A fully operational pipeline in `exercise_solution.py`.
