"""
Module 1: Professional Python & Functions - Code Together
Theme: Refactoring a fragile data parser into an enterprise-grade utility.
"""

import csv
from typing import Any

# =====================================================================
# ❌ LEGACY CODE (Procedural, fragile, no standards)
# =====================================================================
print("--- Running Legacy Code ---")

legacy_data = "name,age,email\nJohn Doe, 25, john@example.com\nJane Smith, 17, jane@example.com\n"
rows = [line.split(",") for line in legacy_data.strip().split("\n")]
res = []
for r in rows[1:]:
    n = r[0].strip().title()
    a = int(r[1].strip())
    e = r[2].strip().lower()
    if a >= 18:
        res.append({"name": n, "age": a, "email": e})
print(res)


# =====================================================================
# ✅ REFACTORED ENTERPRISE-GRADE CODE (Clean, PEP 8, Type-Hinted, Robust)
# =====================================================================
print("\n--- Running Refactored Code ---")


def parse_customer_registrations(
    raw_csv_data: str,
    min_age: int = 18,
    delimiter: str = ",",
) -> list[dict[str, Any]]:
    """Parses customer CSV data, filters underage customers, and standardizes formats.

    This function dynamically checks the CSV header to map fields, preventing
    errors due to changing column order, and handles empty records cleanly.

    Args:
        raw_csv_data: The raw CSV content as a single string.
        min_age: The minimum age cutoff (inclusive). Defaults to 18.
        delimiter: The character separating columns. Defaults to ','.

    Returns:
        A list of dictionaries representing valid registered customers.

    Raises:
        ValueError: If age data cannot be converted to integer.
    """
    cleaned_records: list[dict[str, Any]] = []

    # Using the standard csv.DictReader resolves column ordering issues automatically
    lines = raw_csv_data.strip().splitlines()
    reader = csv.DictReader(lines, delimiter=delimiter)

    for row in reader:
        # Prevent errors from empty rows
        if not any(row.values()):
            continue

        try:
            # Strip whitespace from keys and values dynamically
            clean_row = {key.strip(): val.strip() for key, val in row.items()}

            name = clean_row.get("name", "Unknown").title()
            email = clean_row.get("email", "").lower()
            age_str = clean_row.get("age", "0")
            age = int(age_str)

            # Check business rule
            if age >= min_age:
                cleaned_records.append(
                    {
                        "name": name,
                        "age": age,
                        "email": email,
                    }
                )
        except (ValueError, TypeError) as error:
            # Informative error logging instead of breaking the entire execution
            print(f"Warning: Skipping invalid record {row} due to error: {error}")

    return cleaned_records


# Test running the professional parser with shifted columns
shifted_column_data = "email,age,name\njohn@example.com, 25, John Doe\njane@example.com, 17, Jane Smith"
processed_data = parse_customer_registrations(shifted_column_data)
print(processed_data)
