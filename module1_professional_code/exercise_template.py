"""
Module 1 Challenge: Enterprise Data Standardizer (Template)

Your task:
Write a reusable function `clean_records` that accepts a list of customer data dictionaries,
standardizes string capitalization, handles missing values, and supports custom exclude criteria.
"""

from typing import Any


def clean_records(
    records: list[dict[str, Any]],
    case_style: str = "title",
    default_placeholder: str = "N/A",
    exclude_keys: list[str] | None = None,
) -> list[dict[str, Any]]:
    """Standardizes records by cleaning whitespace, adjusting string casing,

    handling missing values, and optionally dropping specified fields.

    Args:
        records: A list of dictionaries representing customer raw data.
        case_style: Casing for string fields. Must be one of 'title', 'upper', 'lower'.
        default_placeholder: Standard placeholder to replace empty string or None.
        exclude_keys: Optional list of keys to drop from all returned records.

    Returns:
        A list of cleaned and filtered dictionaries.
    """
    # Verify case_style parameter validity
    valid_styles = {"title", "upper", "lower"}
    if case_style not in valid_styles:
        raise ValueError(
            f"Invalid case_style: '{case_style}'. Must be one of {valid_styles}"
        )

    cleaned_list = []

    # TODO: Implement the cleaning logic:
    # 1. Loop through each record in records.
    # 2. Loop through key, value pairs in the record.
    # 3. If a key is in exclude_keys, skip adding it.
    # 4. If value is None or empty string (""), replace it with default_placeholder.
    # 5. If value is a string, strip leading/trailing whitespace, and apply the case_style:
    #    - 'title' -> value.title()
    #    - 'upper' -> value.upper()
    #    - 'lower' -> value.lower()
    # 6. Append the cleaned record dictionary to cleaned_list.

    return cleaned_list


# =====================================================================
# Trainee Verification Area: Test Cases
# =====================================================================
if __name__ == "__main__":
    raw_data = [
        {"name": " alice smith ", "role": "developer", "city": "new york"},
        {"name": "BOB JONES", "role": "MANAGER", "city": ""},
        {"name": "charlie brown", "role": None, "city": "london"},
    ]

    print("Running tests...")

    # Test Case 1: Standard title case
    print("\nTest Case 1 (Default settings):")
    try:
        res1 = clean_records(raw_data)
        print("Result:", res1)
        # Expected output:
        # [
        #   {'name': 'Alice Smith', 'role': 'Developer', 'city': 'New York'},
        #   {'name': 'Bob Jones', 'role': 'Manager', 'city': 'N/A'},
        #   {'name': 'Charlie Brown', 'role': 'N/A', 'city': 'London'}
        # ]
    except Exception as e:
        print("Failed with exception:", e)

    # Test Case 2: Upper case and custom placeholder
    print("\nTest Case 2 (Upper case & 'MISSING' placeholder):")
    try:
        res2 = clean_records(
            raw_data, case_style="upper", default_placeholder="MISSING"
        )
        print("Result:", res2)
        # Expected:
        # [
        #   {'name': 'ALICE SMITH', 'role': 'DEVELOPER', 'city': 'NEW YORK'},
        #   {'name': 'BOB JONES', 'role': 'MANAGER', 'city': 'MISSING'},
        #   {'name': 'CHARLIE BROWN', 'role': 'MISSING', 'city': 'LONDON'}
        # ]
    except Exception as e:
        print("Failed with exception:", e)

    # Test Case 3: Drop 'city' field
    print("\nTest Case 3 (Exclude 'city' key):")
    try:
        res3 = clean_records(raw_data, exclude_keys=["city"])
        print("Result:", res3)
        # Expected:
        # [
        #   {'name': 'Alice Smith', 'role': 'Developer'},
        #   {'name': 'Bob Jones', 'role': 'Manager'},
        #   {'name': 'Charlie Brown', 'role': 'N/A'}
        # ]
    except Exception as e:
        print("Failed with exception:", e)
