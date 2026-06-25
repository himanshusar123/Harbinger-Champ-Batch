# Day 1: Modern Python for Data & AI Engineers
## Theme: "Building Enterprise Grade Python Applications"
### Duration: 8 Hours | Workspace Setup & Trainer Guide

Welcome to the **Day 1 Training Package** for newly hired Data & AI Engineers. This training is designed to bypass passive slide-reading and jump straight into enterprise-grade coding practices through real-world business scenarios, active discussions, live pair-programming ("Code Together"), and self-guided coding challenges.

---

## 📅 Course Agenda (8-Hour Breakdown)

| Time | Module | Focus Areas | Key Deliverables |
| :--- | :--- | :--- | :--- |
| **09:00 - 11:00** | **Module 1: Professional Python & Functions** | Coding Standards (PEP 8), Type Hinting, Docstrings, Reusable Functions (`*args`, `**kwargs`). | Trainees refactor a legacy data-parsing script into clean, reusable utility functions. |
| **11:00 - 13:00** | **Module 2: OOP for Data/AI Pipelines** | Classes, Constructors, Inheritance, Polymorphism, Abstract classes, Interface design. | Trainees build a multi-format data ingestion pipeline (CSV, JSON) using clean class structures. |
| **13:00 - 14:00** | *Lunch Break* | *Networking and informal discussion* | - |
| **14:00 - 16:00** | **Module 3: Exception Handling & Logging** | Exception hierarchy, custom exceptions, safe resource management (`with`), enterprise logging. | Trainees build a resilient transaction processor that safely handles failures and logs errors. |
| **16:00 - 18:00** | **Module 4: API Work & Mini-App Project** | API communication (`requests`/`urllib`), JSON parsing, building a Mini Corporate Application. | Trainees build a **Corporate Portfolio Risk Monitor** integrating all concepts from the day. |

---

## 👩‍🏫 Trainer Strategy: The "How-To" Guide

As the trainer, you must **avoid presenting slides or lecturing on basic syntax**. Instead, use the following sequence for each 2-hour block:

1. **Problem First (15 mins)**:
   - Introduce the **Business Scenario**. Present a poorly written, fragile, or failing piece of legacy code.
   - Run the script and show where it breaks or fails to scale.
2. **Discussion (15 mins)**:
   - Prompt the group: *"What could go wrong here in production?"*, *"Why is this code expensive to maintain?"*
   - Let trainees suggest ideas. Lead them toward the module's target concepts (e.g., OOP, robust error handling).
3. **Code Together (30 mins)**:
   - Work with the trainees to refactor the legacy script live.
   - Walk through the conceptual reasoning behind each refactoring step.
4. **Assessment / MCQ (15 mins)**:
   - Present the 5 Multiple-Choice Questions included in each module README.
   - Have trainees vote or answer, then briefly clarify the logic.
5. **Challenge (35 mins)**:
   - Assign the Hands-on Challenge. Provide the path to the module's `exercise_template.py`.
   - Walk around and assist trainees.
6. **Reflection (10 mins)**:
   - Ask: *"What is the main takeaway from this challenge?"*
   - Review the reference solution (`exercise_solution.py`) and discuss trade-offs.

---

## 💻 Workspace & Development Environment Setup

Please guide the trainees to set up their local development environments as follows:

### 1. Requirements
Ensure Python 3.10+ is installed. Check the version using:
```bash
python --version
```

### 2. Workspace Layout
Instruct trainees to open this folder in their IDE (e.g., VS Code or Antigravity IDE):
```text
python_day1_training/
├── module1_professional_code/
├── module2_oop/
├── module3_exceptions/
└── module4_mini_app/
```

### 3. Dependencies
This course uses only the standard library and the `requests` library for Module 4. Ask trainees to install dependencies using:
```bash
pip install requests flake8 black
```

### 4. Style Checking
Encourage trainees to run code formatters and checkers on their solutions to verify PEP 8 compliance:
```bash
black --check module1_professional_code/exercise_solution.py
flake8 module1_professional_code/exercise_solution.py
```

Let's begin! Refer to the individual `README.md` files in each module folder to guide your teaching.
