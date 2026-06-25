# Module 4: Working with APIs & Mini Corporate Application
## Duration: 2 Hours (16:00 - 18:00)

---

## 💼 Business Scenario: "The Portfolio Risk Monitor"
Our wealth management division needs a tool that monitors the real-time values of corporate assets. They need to fetch current prices from a financial ticker API, clean the data, calculate risk exposures dynamically, and log warning signals when a customer's portfolio exposure exceeds risk limits.

The challenges are:
- Financial APIs are expensive, throttled, and occasionally return server errors (HTTP 500) or corrupt data.
- The system must support different asset types (e.g., Stocks vs. Bonds) which calculate risk exposure using distinct formulas.
- Output formatting must be professional, PEP 8 compliant, and log all events for security audit trails.

---

## 💬 Discussion Prompts
1. **HTTP Status Codes**: What do 200, 400, 401, 404, and 500 status codes mean? How should our Python app behave differently for each of them?
2. **Third-Party Libraries**: Python comes with a built-in `urllib` module, but the community uses `requests`. What are the benefits of using `requests` in enterprise software?
3. **Synthesis**: How do all the tools we learned today (Functions, OOP, Exception Handling, Logging, PEP 8) combine to form a production-ready application?

---

## 🤝 Code Together: API Communication in `code_together_api.py`
In this session, we will query a free placeholder REST API using the standard library `urllib` and third-party `requests` to fetch, validate, and parse JSON data.
Open [code_together_api.py](file:///C:/Users/Himanshu%20Sardana/.gemini/antigravity-ide/scratch/python_day1_training/module4_mini_app/code_together_api.py) to follow along.

---

## 📝 Multiple-Choice Questions (MCQs)

#### Q1. Which HTTP method is typically used to retrieve data from a REST API endpoint?
A) POST  
B) PUT  
C) GET  
D) DELETE  

#### Q2. When using the `requests` library, how do you convert an API JSON response directly into a Python dictionary or list?
A) `json.dumps(response.text)`  
B) `response.json()`  
C) `dict(response)`  
D) `response.parse_to_json()`  

#### Q3. What is the standard way to raise an exception for an unsuccessful HTTP response status (like 404 or 500) using the `requests` library?
A) `response.raise_for_status()`  
B) `raise response.error()`  
C) `response.assert_status(200)`  
D) The library raises exceptions automatically for all non-200 responses.  

#### Q4. What does a "500 Internal Server Error" response indicate to your client application?
A) The client provided invalid authentication credentials.  
B) The requested resource does not exist on the server.  
C) The server encountered an unexpected condition that prevented it from fulfilling the request.  
D) The client made too many requests in a short period of time.  

#### Q5. Why is it important to define a `timeout` argument in `requests.get('https://api.example.com', timeout=5.0)`?
A) It specifies how long the response data should be cached locally.  
B) It prevents the application from hanging indefinitely if the server is offline or unresponsive.  
C) It limits the time the user has to read the query response.  
D) It speeds up network transmission times.  

---

### MCQ Answers & Explanations
* **Q1: C** - GET retrieves representation data, POST creates resources, PUT updates resources, and DELETE removes them.
* **Q2: B** - The `.json()` helper method parses the JSON body of the response directly into Python objects.
* **Q3: A** - `response.raise_for_status()` will raise an `HTTPError` if the response code was a client (4xx) or server (5xx) error.
* **Q4: C** - 5xx errors represent server-side problems. 4xx errors represent client-side problems (e.g., 401 Unauthorized, 404 Not Found).
* **Q5: B** - Without a timeout, Python request calls can block indefinitely under certain network failures, consuming server threads and locking up the system.

---

## 🏆 Hands-On Mini-Project: "Corporate Portfolio Risk Monitor"
You will build a terminal-based corporate application that pulls real-time stock prices, processes investments, and checks if they exceed volatility thresholds.

### Project Requirements:
1. **Config & Standards**: Set up a custom logger, use standard docstrings, and write fully type-hinted code.
2. **Object Models (OOP)**:
   - Create an abstract base class `Asset`.
   - Implement `StockAsset` (calculates risk: `shares * price * volatility_index`).
   - Implement `BondAsset` (calculates risk: `face_value * yield_rate`).
3. **Flaky API Integration**:
   - Write a client that simulates calling a financial API.
   - Handle connection loss and bad payload structures using custom exception handlers.
4. **Main Pipeline**:
   - Ingest a list of assets, query their live prices, calculate their risk index, and print a formatted summary report.

The starter files are available in:
- [mini_app_template/models.py](file:///C:/Users/Himanshu%20Sardana/.gemini/antigravity-ide/scratch/python_day1_training/module4_mini_app/mini_app_template/models.py)
- [mini_app_template/utils.py](file:///C:/Users/Himanshu%20Sardana/.gemini/antigravity-ide/scratch/python_day1_training/module4_mini_app/mini_app_template/utils.py)
- [mini_app_template/main.py](file:///C:/Users/Himanshu%20Sardana/.gemini/antigravity-ide/scratch/python_day1_training/module4_mini_app/mini_app_template/main.py)

Review the reference solution at:
- [mini_app_solution/main.py](file:///C:/Users/Himanshu%20Sardana/.gemini/antigravity-ide/scratch/python_day1_training/module4_mini_app/mini_app_solution/main.py)
