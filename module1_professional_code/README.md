# Module 1: Writing Professional Code & Reusable Functions
## Duration: 2 Hours (09:00 - 11:00)

---

## 💼 Business Scenario: "The Fragile CSV Loader"
Our system receives daily export logs of newly registered customer accounts from our legacy CRM. A junior engineer quickly wrote a script (`parse_data.py`) to parse these logs, filter out underage users, and format their names for our marketing database. 

However:
- The CRM export columns keep changing order.
- The script has no functions, no type hints, and hardcoded index lookups like `row[2]`.
- It breaks silently or crashes when a blank row is encountered.
- There are no coding standards (variable names like `x`, `temp`, and no documentation).

### Legacy Code (The Problem)
```python
import csv
data = "name,age,email\nJohn Doe, 25, john@example.com\nJane Smith, 17, jane@example.com\n"
rows = [line.split(",") for line in data.strip().split("\n")]
res = []
for r in rows[1:]:
    # Hardcoded index lookups - if order changes, this breaks!
    n = r[0].strip().title()
    a = int(r[1].strip())
    e = r[2].strip().lower()
    if a >= 18:
        res.append({"name": n, "age": a, "email": e})
print(res)
```

---

## 💬 Discussion Prompts
1. **Maintainability**: Why are hardcoded index lookups like `r[0]` highly dangerous in production pipelines?
2. **Type Safety**: How can type hinting and standard signatures help other engineers when they use your library code?
3. **PEP 8**: Why does consistent spacing and formatting (e.g., snake_case vs CamelCase) matter for a team of 50+ engineers?

---

## 🤝 Code Together: Refactoring `code_together.py`
In this session, we will run and refactor `code_together.py` from procedural, fragile code to a professional, PEP 8 compliant, type-hinted, and robust function.
Open [code_together.py](file:///C:/Users/Himanshu%20Sardana/.gemini/antigravity-ide/scratch/python_day1_training/module1_professional_code/code_together.py) to follow along.

---

## 📝 Multiple-Choice Questions (MCQs)

#### Q1. According to PEP 8, what is the recommended naming convention for variables and functions in Python?
A) camelCase  
B) PascalCase  
C) snake_case  
D) UPPERCASE  

#### Q2. Which of the following is the correct way to specify type hints for a function that takes a list of strings and returns a dictionary mapping strings to integers?
A) `def process(data: list) -> dict:`  
B) `def process(data: list[str]) -> dict[str, int]:`  
C) `def process(data: ListOfStrings) -> DictOfStrInt:`  
D) `def process(data: [str]) -> {str: int}:`  

#### Q3. What is the primary purpose of `*args` and `**kwargs` in a Python function definition?
A) To enforce static type checking.  
B) To allow the function to accept a variable number of positional and keyword arguments.  
C) To speed up function execution time.  
D) To make all parameters optional by defaulting them to `None`.  

#### Q4. What does a "docstring" do, and where should it be placed?
A) It comments out code; placed at the end of the file.  
B) It defines variable types; placed inside the function body using `#`.  
C) It documents the function's purpose, parameters, and return value; placed immediately after the function header using triple quotes `"""`.  
D) It configures linter rules; placed in a separate configuration file.  

#### Q5. What is the output of the following function call?
```python
def greet(name: str, *titles: str, prefix: str = "Hello") -> str:
    title_str = " ".join(titles)
    return f"{prefix} {title_str} {name}".strip()

print(greet("Smith", "Dr.", "Ph.D.", prefix="Welcome"))
```
A) `Welcome Dr. Ph.D. Smith`  
B) `Hello Dr. Ph.D. Smith`  
C) `Welcome Smith Dr. Ph.D.`  
D) SyntaxError: *args must come after keyword arguments  

---

### MCQ Answers & Explanations
* **Q1: C** - PEP 8 recommends using `snake_case` for functions and variables, `PascalCase` for classes, and `UPPER_CASE` for constants.
* **Q2: B** - Since Python 3.9, built-in types `list` and `dict` support generics directly (e.g., `list[str]` and `dict[str, int]`).
* **Q3: B** - `*args` collects positional arguments into a tuple, while `**kwargs` collects keyword arguments into a dict.
* **Q4: C** - Docstrings are placed immediately under the function definition and describe its behavior, inputs, and outputs.
* **Q5: A** - The arguments `"Dr."` and `"Ph.D."` are captured by `*titles`. `prefix` is explicitly set to `"Welcome"`. Output is `Welcome Dr. Ph.D. Smith`.

---

## 🏆 Hands-On Challenge: "Enterprise Data Standardizer"
Your task is to write a reusable utility function that cleans and standardizes messy dictionaries representing records from an API payload.

### Requirements:
1. Create a function `clean_records(records: list[dict], **kwargs) -> list[dict]`.
2. Clean all string fields:
   - Trim leading/trailing whitespace.
   - Adjust letter capitalization:
     - By default, capitalize strings using `.title()`.
     - Allow customization via keyword argument `case_style`: `"upper"`, `"lower"`, or `"title"`.
3. Handle missing values:
   - If a value is missing (`None` or empty string `""`), set it to a default placeholder value specified by `default_placeholder` (default is `"N/A"`).
4. Allow dynamic field dropping:
   - Trainees must support dropping specific keys by passing them as a list through `exclude_keys`.

Open [exercise_template.py](file:///C:/Users/Himanshu%20Sardana/.gemini/antigravity-ide/scratch/python_day1_training/module1_professional_code/exercise_template.py) to write your solution.
Check [exercise_solution.py](file:///C:/Users/Himanshu%20Sardana/.gemini/antigravity-ide/scratch/python_day1_training/module1_professional_code/exercise_solution.py) for the reference solution.
