# RetailMax Enterprise Data Pipeline (v5.0)

Welcome to the **Day 5: Enterprise Software Engineering** workspace! Today we transition from writing quick, single-file scripts to building a robust, production-ready, and professional software package.

This codebase is structured exactly as an enterprise pipeline would be, showcasing type safety, automated validation, database persistence, asynchronous programming, unit testing, and tooling for code quality.

---

## 🎯 Learning Journey (Day 5 Sprints)

The code in this project demonstrates the following concepts from today's curriculum:

### 📁 Sprint 1: Project Structure
Instead of putting all code in a single file (like a Jupyter Notebook or a simple script), we separate concerns into distinct modules within the `retailmax/` package:
- `app.py`: The pipeline orchestrator.
- `retailmax/config.py`: Centralized configuration.
- `retailmax/api/`: Data ingestion from REST APIs (sync and async).
- `retailmax/employees/`: Data validation and DataFrame transformations.
- `retailmax/database/`: SQLite persistence layer.
- `retailmax/analytics/`: Business logic, aggregations, and report rendering.

### 🏷️ Sprint 2: Type Hints
You will find strict type hinting (`str`, `int`, `float`, `dict`, `list`, `pd.DataFrame`) across all function signatures, variables, and return types. This prevents runtime errors and enables full static verification via `mypy`.

### 🌐 Sprint 3: REST API Ingestion
`retailmax/api/service.py` uses Python's `requests` library to consume structured JSON data from a REST endpoint (`https://jsonplaceholder.typicode.com/users`), representing ingestion from a corporate HR system.

### 🔄 Sprint 4: JSON to DataFrame
`retailmax/employees/transformer.py` converts raw JSON structures into Pandas DataFrames, performing cleanup and calculating customized fields (such as simulating monthly and annual salaries, base payouts, and bonuses).

### 🛡️ Sprint 5: Data Validation (Data Contracts)
`retailmax/employees/validation.py` defines standard schemas and row-level checks to filter out invalid records (e.g. checking that email formats are valid, IDs are positive, and salaries are non-negative) before saving to the database.

### 🧪 Sprint 6: Unit Testing
`tests/test_pipeline.py` contains testing suites with `pytest`. It shows how to write clean, assertion-driven tests for computations, schema validation, and pipeline steps.

### 💎 Sprint 7: Code Quality Tooling
The project is configured for three critical static check tools (via `pyproject.toml`):
- **Black**: Automatic formatting.
- **Ruff**: Ultra-fast linting and import sorting.
- **Mypy**: Static type safety validator.

### 📦 Sprint 8: Packaging
By introducing `__init__.py` files, `retailmax/` is structured as a standard Python package. This enables cleaner imports:
```python
from retailmax.employees.validation import validate_employee_record
```

### ⚡ Sprint 9: Async
`retailmax/api/async_service.py` provides a demonstration using `asyncio` and `httpx` to concurrently fetch data from multiple endpoints (e.g. simulating Weather API, Payroll API, and Attendance API) without blocking execution.

### 🚀 Sprint 10: CI/CD
`tests/` and configuration files lay the foundation for automated CI pipelines (like GitHub Actions, GitLab CI, or Jenkins). On every git push, the environment runs:
1. `black --check .` (Formatting)
2. `ruff check .` (Linting)
3. `mypy .` (Types)
4. `pytest` (Tests)

---

## 🛠️ Getting Started

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the End-to-End Pipeline
```bash
python app.py
```

### 3. Run Unit Tests
```bash
pytest
```

### 4. Run Code Quality Checks
```bash
# Format the code
black .

# Lint code
ruff check .

# Static type check
mypy .
```
