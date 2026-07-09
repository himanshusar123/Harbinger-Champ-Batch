"""Data Transformer module.

Demonstrates Sprint 4 (JSON -> DataFrame conversion & calculations)
and Sprint 2 (Type Hints).
"""

from typing import Any

import pandas as pd

from retailmax.utils.logger import get_logger

logger = get_logger(__name__)


def transform_raw_employees(raw_users: list[dict[str, Any]]) -> pd.DataFrame:
    """Transforms raw API user dictionary payload into a structured Pandas DataFrame.

    Also flattens nested address and company info, and simulates salary parameters
    for RetailMax operations.

    Args:
        raw_users: List of user records retrieved from the JSON API.

    Returns:
        A structured Pandas DataFrame ready for validation and analytics.
    """
    logger.info("Starting transformation of raw API payload to Pandas DataFrame")

    processed_records = []
    for user in raw_users:
        address = user.get("address", {})
        company = user.get("company", {})

        # Extracting and flattening nested fields
        record = {
            "employee_id": int(user["id"]),
            "name": str(user["name"]),
            "username": str(user["username"]),
            "email": str(user["email"]),
            "city": str(address.get("city", "Unknown")),
            "company_name": str(company.get("name", "Unknown")),
            # Simulating monthly salary based on employee ID (e.g., $40,000 to $50,000)
            "monthly_salary": float(1000 * int(user["id"]) + 40000),
        }
        processed_records.append(record)

    # Sprint 5: Injecting an invalid record (negative salary) to demonstrate validation
    invalid_record = {
        "employee_id": 999,
        "name": "Jane Doe (Invalid Test)",
        "username": "janedoe",
        "email": "janedoe@retailmax.com",
        "city": "Metropolis",
        "company_name": "RetailMax Corp",
        "monthly_salary": -5000.00,  # Negative salary representing corrupted API input
    }
    processed_records.append(invalid_record)

    # Creating DataFrame
    df = pd.DataFrame(processed_records)

    # Adding derived columns (Sprint 6/11 business logic)
    df["annual_salary"] = df["monthly_salary"] * 12

    logger.info(f"DataFrame transformation complete. Total rows: {len(df)}")
    return df
