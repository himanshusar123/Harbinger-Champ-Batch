# Day 4 Assessment: Data Analytics & Business Intelligence Quiz

Test your understanding of Pandas, DuckDB, Data Contracts, and Business Intelligence concepts covered in the Day 4 curriculum.

---

## 📝 Section 1: Multiple-Choice Questions (MCQs)

### Q1: What is the main structural difference between a Pandas Series and a Pandas DataFrame?
- A) A Series is 1D (representing a single column/row) with an index, whereas a DataFrame is 2D (representing a table with columns and rows) with both column and index labels.
- B) A Series can only hold numeric data, whereas a DataFrame can hold mixed types.
- C) A Series is mutable, whereas a DataFrame is immutable.
- D) A Series does not have an index.

<details>
<summary>💡 Click to reveal the answer & explanation</summary>

**Correct Answer: A**
**Explanation:** A Pandas Series is a 1-dimensional labeled array capable of holding any data type. A DataFrame is a 2-dimensional labeled data structure with columns of potentially different types, resembling an Excel sheet or SQL table. Both have indexes.
</details>

---

### Q2: If you run `df.shape` on a DataFrame with 1,000 rows and 7 columns, what is the output type and value?
- A) String: `"1000 rows, 7 columns"`
- B) List: `[1000, 7]`
- C) Tuple: `(1000, 7)`
- D) Integer: `7000`

<details>
<summary>💡 Click to reveal the answer & explanation</summary>

**Correct Answer: C**
**Explanation:** `df.shape` returns a tuple representing the dimensionality of the DataFrame. The format is `(rows, columns)`, so the output is the tuple `(1000, 7)`.
</details>

---

### Q3: When cleaning data, which Pandas function is best suited to replace all `NaN` (missing) values in a column with a specific default value, like the median or 0?
- A) `df.dropna()`
- B) `df.fillna()`
- C) `df.replace_nan()`
- D) `df.drop_duplicates()`

<details>
<summary>💡 Click to reveal the answer & explanation</summary>

**Correct Answer: B**
**Explanation:** `df.fillna()` is used to fill `NaN` (null) values with a specified value or method (like backfill/ffill). `dropna()` removes the rows containing nulls entirely.
</details>

---

### Q4: You want to filter a DataFrame `df` to get employees in "Engineering" who make more than $90,000. Which syntax is correct?
- A) `df[df["Department"] == "Engineering" and df["Salary"] > 90000]`
- B) `df[(df["Department"] == "Engineering") & (df["Salary"] > 90000)]`
- C) `df[(df["Department"] == "Engineering") | (df["Salary"] > 90000)]`
- D) `df.query("Department == 'Engineering' & Salary > 90000")` (Wait, both B and D are technically correct in Pandas. Choose the most common boolean indexing option)

<details>
<summary>💡 Click to reveal the answer & explanation</summary>

**Correct Answer: B** (or **D** if using the `.query()` method)
**Explanation:** For boolean indexing in Pandas, you must use bitwise operators like `&` (AND), `|` (OR), and `~` (NOT) instead of python keywords `and`/`or`. Additionally, each condition must be wrapped in parentheses due to operator precedence rules.
</details>

---

### Q5: How would you retrieve the top 5 highest-paid employees in a DataFrame `df`?
- A) `df.sort_values("Salary").head(5)`
- B) `df.sort_values("Salary", ascending=False).head(5)`
- C) `df.nlargest(5, "Salary")`
- D) Both B and C are correct.

<details>
<summary>💡 Click to reveal the answer & explanation</summary>

**Correct Answer: D**
**Explanation:** Sorting by `Salary` in descending order (`ascending=False`) and taking the first 5 records (`.head(5)`) produces the exact same result as using the dedicated, highly efficient `.nlargest(5, 'Salary')` method.
</details>

---

### Q6: What is a key advantage of using DuckDB over Pandas for certain analytical queries on local files?
- A) DuckDB can execute standard SQL queries directly on files (CSV, Parquet) and in-memory DataFrames without requiring a database server.
- B) DuckDB automatically builds web visualizations.
- C) DuckDB replaces the need for Matplotlib.
- D) DuckDB requires setting up a PostgreSQL cluster.

<details>
<summary>💡 Click to reveal the answer & explanation</summary>

**Correct Answer: A**
**Explanation:** DuckDB is an embedded, serverless SQL OLAP database engine. It allows running SQL queries directly on Parquet files, CSVs, or Pandas DataFrames in memory at extremely high speeds, making it great for SQL-fluent developers.
</details>

---

### Q7: What is the primary purpose of a "Data Contract" in data pipelines?
- A) To legally lock in client specifications.
- B) To enforce data format, schema boundaries, and quality rules on incoming data before it passes into downstream processing.
- C) To speed up Python loops.
- D) To create database backups automatically.

<details>
<summary>💡 Click to reveal the answer & explanation</summary>

**Correct Answer: B**
**Explanation:** A data contract defines the schema, types, and quality invariants (e.g., non-negative salary, unique IDs) that data must satisfy before entering a pipeline, preventing "Garbage In, Garbage Out" scenarios.
</details>

---

## 💻 Section 2: Code Comprehension & Debugging

### Case 1: The Broken Filter
A trainee writes the following code to find employees with a performance score of 5:
```python
top_performers = df[df["PerformanceScore"] = 5]
```
**Question:** Why does this code raise a `SyntaxError` or `ValueError`? How do you fix it?

<details>
<summary>💡 Click to reveal the answer & explanation</summary>

**Why it fails:** 
The assignment operator `=` is used instead of the comparison operator `==`. Pandas is attempting to assign the value `5` to the series instead of evaluating equality.

**Correct Code:**
```python
top_performers = df[df["PerformanceScore"] == 5]
```
</details>

---

### Case 2: The Silent Duplication
A trainee cleans duplicates using:
```python
df.drop_duplicates(subset=["EmployeeID"])
print(df.shape)  # Still shows the original count of rows!
```
**Question:** Why did the row count not decrease even though duplicates existed?

<details>
<summary>💡 Click to reveal the answer & explanation</summary>

**Why it fails:** 
By default, `drop_duplicates` returns a copy of the DataFrame with duplicates removed; it does **not** modify the original DataFrame in-place.

**How to fix:**
Either re-assign the result to the variable:
```python
df = df.drop_duplicates(subset=["EmployeeID"])
```
Or use the `inplace=True` parameter (though re-assignment is generally preferred in modern Pandas):
```python
df.drop_duplicates(subset=["EmployeeID"], inplace=True)
```
</details>

---

## 🏢 Section 3: Scenario-Based Design Challenges

### Scenario: High Salary Alert
The HR Director wants to set up an automated report that identifies if any employee in a newly imported CSV has a salary **exceeding $200,000**, OR has a salary **below $30,000**, and flag these records as "Out of Bounds" in a validation report.

**Task:** Write a simple Pandas snippet that takes a DataFrame `df`, filters for these records, and prints their names and salaries.

<details>
<summary>💡 Click to reveal the code solution</summary>

```python
# Identify records out of bounds
out_of_bounds = df[(df["Salary"] > 200000) | (df["Salary"] < 30000)]

if not out_of_bounds.empty:
    print(f"WARNING: Found {len(out_of_bounds)} record(s) out of bounds:")
    print(out_of_bounds[["Name", "Salary"]])
else:
    print("All employee salaries are within bounds ($30k - $200k).")
```
</details>
