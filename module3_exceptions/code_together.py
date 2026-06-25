"""
Module 3: Exception Handling & Resilient Operations - Code Together
Theme: Building a robust transaction processor with custom logging.
"""

import logging
import sys

# Configure structured logging to standard output
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)


# =====================================================================
# ✅ CUSTOM EXCEPTIONS
# =====================================================================
class DataProcessingError(Exception):
    """Base exception class for data processing errors."""

    pass


class InvalidTransactionError(DataProcessingError):
    """Raised when a transaction payload fails validation checks."""

    pass


# =====================================================================
# ✅ TRANSACTION PROCESSOR
# =====================================================================
def process_transaction(transaction: dict[str, str | int]) -> None:
    """Processes a single financial transaction.

    Demonstrates try-except-else-finally structure.
    """
    logging.info(f"Starting transaction processing for: {transaction.get('id')}")

    try:
        # Validate critical fields
        if "amount" not in transaction or "id" not in transaction:
            raise InvalidTransactionError("Missing mandatory 'id' or 'amount' fields.")

        amount = transaction["amount"]
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise InvalidTransactionError(
                f"Invalid transaction amount: {amount}. Must be positive."
            )

        # Simulate writing transaction to a file safely using context manager
        filename = f"tx_{transaction['id']}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"TxID: {transaction['id']}\nAmount: {amount}\nStatus: APPROVED\n")

    except InvalidTransactionError as err:
        logging.error(f"Validation Failure: {err}")
        # Re-raise to let caller handle if necessary, or swallow and log
        raise

    except IOError as err:
        logging.error(f"Disk Write Failure: {err}")
        raise DataProcessingError("Failed to persist transaction to disk.") from err

    else:
        # Runs only if NO exception occurred in the try block
        logging.info("Transaction processed and saved successfully.")

    finally:
        # Always runs, perfect for resource cleanup
        logging.info("Completed processing attempt.")


# =====================================================================
# Execution Demo
# =====================================================================
if __name__ == "__main__":
    valid_tx = {"id": "tx101", "amount": 250.50}
    invalid_tx = {"id": "tx102", "amount": -10}

    print("--- 1. Processing Valid Transaction ---")
    try:
        process_transaction(valid_tx)
    except Exception as e:
        print(f"Caught top-level exception: {e}")

    # Remove the created file to clean up the workspace
    import os

    if os.path.exists("tx_tx101.txt"):
        os.remove("tx_tx101.txt")

    print("\n--- 2. Processing Invalid Transaction ---")
    try:
        process_transaction(invalid_tx)
    except InvalidTransactionError as e:
        print(f"Top-level handler caught validation error: {e}")
