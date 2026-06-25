"""
Module 1 Challenge: Enterprise Data Standardizer (Reference Solution)
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
    valid_styles = {"title", "upper", "lower"}
    if case_style not in valid_styles:
        raise ValueError(
            f"Invalid case_style: '{case_style}'. Must be one of {valid_styles}"
        )

    # Convert to set for faster lookup, handle None case
    exclude_set = set(exclude_keys) if exclude_keys else set()

    cleaned_list = []

    for record in records:
        cleaned_record = {}
        for key, value in record.items():
            if key in exclude_set:
                continue

            # Standardize missing/empty values
            if value is None or (isinstance(value, str) and value.strip() == ""):
                cleaned_record[key] = default_placeholder
            # Standardize string capitalization and whitespace
            elif isinstance(value, str):
                stripped = value.strip()
                if case_style == "title":
                    cleaned_record[key] = stripped.title()
                elif case_style == "upper":
                    cleaned_record[key] = stripped.upper()
                elif case_style == "lower":
                    cleaned_record[key] = stripped.lower()
            else:
                cleaned_record[key] = value

        cleaned_list.append(cleaned_record)

    return cleaned_list


if __name__ == "__main__":
    raw_data = [
        {"name": " alice smith ", "role": "developer", "city": "new york"},
        {"name": "BOB JONES", "role": "MANAGER", "city": ""},
        {"name": "charlie brown", "role": None, "city": "london"},
    ]

    print("Running reference solution verification tests...")

    # Test Case 1
    res1 = clean_records(raw_data)
    assert res1[0]["name"] == "Alice Smith"
    assert res1[1]["city"] == "N/A"
    assert res1[2]["role"] == "N/A"

    # Test Case 2
    res2 = clean_records(
        raw_data, case_style="upper", default_placeholder="MISSING"
    )
    assert res2[0]["name"] == "ALICE SMITH"
    assert res2[1]["city"] == "MISSING"

    # Test Case 3
    res3 = clean_records(raw_data, exclude_keys=["city"])
    assert "city" not in res3[0]
    assert len(res3[0]) == 2

    print("All reference solution checks passed successfully!")
