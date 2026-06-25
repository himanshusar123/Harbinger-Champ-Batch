# Module 2: Object-Oriented Programming (OOP) for Data & AI
## Duration: 2 Hours (11:00 - 13:00)

---

## 💼 Business Scenario: "The Multi-Source Ingestion Pipeline"
Our platform ingests customer transactions and metadata from three sources:
1. Local CSV reports.
2. Real-time JSON files pushed to an S3 bucket.
3. Web REST APIs.

A developer wrote three distinct functions: `parse_csv()`, `parse_json()`, and `parse_api()`. Each function handles its own file opening, exception checking, and logs its own success metrics.

The problems are:
- **Redundancy**: Shared steps (like logging, timing, and counting processed records) are duplicated in all three functions.
- **Inflexibility**: If we add an XML source tomorrow, we must write a whole new set of helper functions, making it difficult to swap sources at runtime.

---

## 💬 Discussion Prompts
1. **When to use OOP**: Why does data ingestion fit the OOP paradigm so well? (Think: shared behavior but different implementations).
2. **Abstract Base Classes**: What is the purpose of an Abstract Class or Interface? Why is it useful to prevent developers from instantiating the base `DataIngestor` directly?
3. **Encapsulation**: Why do we use properties and private variables (e.g., `_records`) instead of directly modifying attributes of an object from outside the class?

---

## 🤝 Code Together: OOP Design in `code_together.py`
In this session, we will design an abstract base class `DataIngestor` and build a concrete subclass `CSVIngestor` to read customer CSV data.
Open [code_together.py](file:///C:/Users/Himanshu%20Sardana/.gemini/antigravity-ide/scratch/python_day1_training/module2_oop/code_together.py) to follow along.

---

## 📝 Multiple-Choice Questions (MCQs)

#### Q1. How do you define an abstract class in Python?
A) By writing `interface DataIngestor:`  
B) By inheriting from `abc.ABC` and using the `@abc.abstractmethod` decorator.  
C) By declaring all methods inside a class without any body (using `pass`).  
D) Python does not support abstract classes.  

#### Q2. What is the difference between a class attribute and an instance attribute?
A) Class attributes are defined using `self.`, while instance attributes are defined at the class level.  
B) Class attributes are shared across all instances of the class; instance attributes are unique to each object.  
C) Instance attributes can only be modified inside static methods.  
D) There is no difference; they are completely interchangeable.  

#### Q3. What is the purpose of the `@property` decorator in a Python class?
A) It marks a method as private so it cannot be called outside the class.  
B) It turns a method into a getter, allowing it to be accessed like an attribute without using parentheses `()`.  
C) It declares that a class is a database model.  
D) It speeds up variable lookups inside the method.  

#### Q4. Which special "dunder" (double underscore) method is used to customize the string representation of a class when printed with `print(object)`?
A) `__init__`  
B) `__repr__`  
C) `__str__`  
D) `__call__`  

#### Q5. Consider the following code. What does it output?
```python
class Animal:
    def speak(self):
        return "Generic Sound"

class Dog(Animal):
    def speak(self):
        return "Woof"

animals = [Animal(), Dog()]
for animal in animals:
    print(animal.speak(), end=" ")
```
A) `Generic Sound Generic Sound`  
B) `Woof Woof`  
C) `Generic Sound Woof`  
D) AttributeError: Dog has no attribute speak  

---

### MCQ Answers & Explanations
* **Q1: B** - Python uses the `abc` (Abstract Base Class) module. Concrete classes subclass the base class that inherits from `abc.ABC`.
* **Q2: B** - Class attributes are defined directly inside the class scope. Instance attributes are defined inside methods (usually `__init__`) using `self.attribute`.
* **Q3: B** - `@property` enables encapsulation by letting a method act as a read-only attribute, making it easy to add validation rules in the future without changing public APIs.
* **Q4: C** - `__str__` is called by `str(obj)` and `print(obj)`. `__repr__` is intended to be an unambiguous representation for debugging.
* **Q5: C** - This is a classic demonstration of Polymorphism. The loop calls `speak()`, which executes the overridden subclass method for the `Dog` instance.

---

## 🏆 Hands-On Challenge: "The JSON & CSV Extensible Pipeline"
Your task is to build a `JSONIngestor` subclass that extends the abstract `DataIngestor` class.

### Requirements:
1. Subclass `DataIngestor` in `exercise_template.py`.
2. Implement the `__init__(self, filepath)` constructor.
3. Implement the `parse(self)` abstract method:
   - Use the built-in `json` module to load data from `filepath`.
   - Store the parsed list of dicts in a private attribute `_records`.
4. Implement a getter property `records` that returns the loaded list of dictionaries.
5. In the parent `DataIngestor` class, implement a concrete helper method `get_record_count(self) -> int` that returns the number of ingested records.

Open [exercise_template.py](file:///C:/Users/Himanshu%20Sardana/.gemini/antigravity-ide/scratch/python_day1_training/module2_oop/exercise_template.py) to write your solution.
Check [exercise_solution.py](file:///C:/Users/Himanshu%20Sardana/.gemini/antigravity-ide/scratch/python_day1_training/module2_oop/exercise_solution.py) for reference.
