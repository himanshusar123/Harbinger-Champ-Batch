# Hands-on Project: Corporate Portfolio Risk Monitor (Starter Template)

In this hands-on project, you will build a terminal-based tool that:
1. Ingests corporate assets (stocks and bonds) via an Object-Oriented pipeline.
2. Queries their live market values via a simulated API.
3. Computes their risk metrics based on specific asset class formulas.
4. Checks if the risk exceeds defined limits, raising alerts and logging metrics.

---

## Directory Structure

```text
mini_app_template/
│
├── README.md             # This instruction file
├── models.py              # OOP Asset definitions (TODOs inside)
├── utils.py              # Logging and Flaky API client (TODOs inside)
└── main.py               # Main execution logic and report printing (TODOs inside)
```

---

## Tasks to Complete

### Task 1: Complete `models.py`
- Implement abstract base class `Asset` and define properties: `asset_id`, `name`, `purchase_price`.
- Define an abstract method `calculate_risk(self, current_price: float) -> float`.
- Implement concrete class `StockAsset(Asset)`:
  - Add instance attributes: `shares`, `volatility_index`.
  - Implement `calculate_risk(self, current_price: float)`: `shares * current_price * volatility_index`.
- Implement concrete class `BondAsset(Asset)`:
  - Add instance attributes: `face_value`, `yield_rate`.
  - Implement `calculate_risk(self, current_price: float)`: `face_value * yield_rate` (bond values are relatively stable).

### Task 2: Complete `utils.py`
- Setup standard python logging to print messages with levels and timestamps.
- Implement error mapping in `fetch_current_market_price(symbol: str) -> float`:
  - Wrap network simulation calls.
  - Throw custom exception `APIClientError` on HTTP failures or network timeout errors.

### Task 3: Complete `main.py`
- Ingest a list of mixed `StockAsset` and `BondAsset` instances.
- Loop through the assets:
  - Query the live price using `fetch_current_market_price()` inside a try-except block.
  - If a transient API failure occurs, use the original `purchase_price` as a fallback, log a Warning, and proceed (defensive coding!).
  - Compute total risk value of the portfolio.
  - Output a neat, tabular report summarizing the calculations.
