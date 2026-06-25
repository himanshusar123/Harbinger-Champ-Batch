# Module 3: Exception Handling & Resilient Operations
## Duration: 2 Hours (14:00 - 16:00)

---

## 💼 Business Scenario: "The Midnight Server Crash"
Our automated nightly database ingestion script runs at 02:00 AM. It fetches raw transactions, parses them, and saves them to our analytics database. Last night, the script crashed at 02:05 AM due to a brief, 5-second network hiccup.

Because the junior engineer wrote:
```python
# Bad example
try:
    data = fetch_db()
except:
    pass  # Silently ignored the connection error!
```

The script:
1. Did not raise an alarm, so the DevOps dashboard showed a "Green/Healthy" state.
2. Left the database connection pool open, leading to connection exhaustion.
3. Left file handles open on the local filesystem.
4. Led to silent data loss, which was only discovered by the billing team 12 hours later.

---

## 💬 Discussion Prompts
1. **Catching generic exceptions**: Why is `except:` or `except Exception:` dangerous? What hidden bugs (like `KeyboardInterrupt` or syntax issues) can it swallow?
2. **Try-Except-Else-Finally**: What are the specific use cases for `else` and `finally` blocks? (Hint: `else` runs only if no exception occurred; `finally` runs *always*).
3. **Structured Logging vs. Print**: In production, where do standard prints (`print("Error!")`) go? Why is a structured logging framework (with levels like DEBUG, INFO, WARNING, ERROR, CRITICAL) better?

---

## 🤝 Code Together: Resilient Code in `code_together.py`
In this session, we will write a batch processor using custom exceptions and Python's standard `logging` library.
Open [code_together.py](file:///C:/Users/Himanshu%20Sardana/.gemini/antigravity-ide/scratch/python_day1_training/module3_exceptions/code_together.py) to follow along.

---

## 📝 Multiple-Choice Questions (MCQs)

#### Q1. What happens if an exception is raised inside a `try` block, and there is a matching `except` block as well as a `finally` block?
A) The `finally` block is skipped.  
B) The `except` block runs, and then the `finally` block runs.  
C) Only the `finally` block runs.  
D) The program crashes immediately without running either block.  

#### Q2. What is the main difference between using `print()` and `logging.warning()` for reporting problems?
A) `print()` writes to a file, while `logging` only displays text on the screen.  
B) `logging` allows you to direct output to multiple destinations (console, files, cloud monitors) and filter messages by severity levels dynamically.  
C) `logging` pauses program execution until the user presses Enter.  
D) There is no difference; they are different names for the same action.  

#### Q3. How do you create a custom user-defined exception in Python?
A) By defining a function that raises `Exception`.  
B) By creating a new class that inherits from `Exception` (or one of its subclasses).  
C) By declaring a variable equal to `raise Exception`.  
D) Python does not allow custom exceptions; you must use built-in ones.  

#### Q4. What is the purpose of the `else` block in a `try-except` statement?
A) It executes if an exception is raised, acting as a secondary handler.  
B) It executes only if the code in the `try` block runs successfully *without* raising any exceptions.  
C) It serves as a default fallback if the `finally` block fails.  
D) It is syntactically invalid and causes a `SyntaxError`.  

#### Q5. What does the following code print?
```python
def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Zero"
    finally:
        return "Finally"

print(division(10, 0))
```
A) `Zero`  
B) `Finally`  
C) `Zero` and then `Finally`  
D) ZeroDivisionError  

---

### MCQ Answers & Explanations
* **Q1: B** - The `except` block catches and processes the exception, and the `finally` block is guaranteed to run afterward to clean up resources.
* **Q2: B** - Logging provides levels (DEBUG, INFO, WARNING, ERROR, CRITICAL) and configurable destinations, which is vital for production applications.
* **Q3: B** - Inheriting from `Exception` integrates your custom error into Python's native exception-handling framework.
* **Q4: B** - The `else` block is useful for code that should execute only if the `try` block succeeded, avoiding catching unintended exceptions from the handler itself.
* **Q5: B** - **Caution!** If a `finally` block contains a `return` statement, it will override any `return` statement executed in the `try` or `except` blocks.

---

## 🏆 Hands-On Challenge: "The Resilient DB Connector"
Your task is to implement a robust, retry-enabled database client class that handles connection drops gracefully.

### Requirements:
1. Define two custom exceptions:
   - `DatabaseConnectionError(Exception)`
   - `DatabaseQueryError(Exception)`
2. Complete the class `ResilientDBConnector` in `exercise_template.py`:
   - The method `execute_query(self, query: str)` calls the simulated method `_send_network_request()`.
   - `_send_network_request()` randomly raises `ConnectionResetError` or `PermissionError`.
   - In `execute_query()`, catch `ConnectionResetError` and raise `DatabaseConnectionError`. Catch `PermissionError` and raise `DatabaseQueryError`.
   - In `execute_query_with_retry(self, query: str, max_retries: int = 3)`:
     - Attempt to run `execute_query()`.
     - If a `DatabaseConnectionError` is caught, log a warning, wait briefly, and try again.
     - If it fails after `max_retries`, log a critical error and raise a final `DatabaseConnectionError`.
     - If a `DatabaseQueryError` occurs, do NOT retry (since it is a permissions issue that won't resolve with retries) - fail immediately.
     - Ensure the connection is marked closed inside a `finally` block.

Open [exercise_template.py](file:///C:/Users/Himanshu%20Sardana/.gemini/antigravity-ide/scratch/python_day1_training/module3_exceptions/exercise_template.py) to write your solution.
Check [exercise_solution.py](file:///C:/Users/Himanshu%20Sardana/.gemini/antigravity-ide/scratch/python_day1_training/module3_exceptions/exercise_solution.py) for reference.
