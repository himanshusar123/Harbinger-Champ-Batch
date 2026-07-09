"""Data Validation Contracts.

Demonstrates Sprint 5 (Data Validation / Data Contracts) and Sprint 2 (Type Hints).
"""

import re

import pandas as pd

from retailmax.config import MIN_VALID_SALARY
from retailmax.utils.logger import get_logger

logger = get_logger(__name__)

# Basic email regex pattern
EMAIL_REGEX = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")


def validate_salary(salary: float) -> bool:
    """Verifies that a salary is non-negative and valid.

    Args:
        salary: The monthly salary value.

    Returns:
        True if the salary is valid, False otherwise.
    """
    return salary > MIN_VALID_SALARY


def validate_email(email: str) -> bool:
    """Verifies that an email is in a valid format.

    Args:
        email: Email string.

    Returns:
        True if valid format, False otherwise.
    """
    return bool(EMAIL_REGEX.match(email))


def validate_employee_records(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Filters employee records, separating clean data from corrupted data.

    Demonstrates checking row-level contracts in an enterprise pipeline.

    Args:
        df: The raw processed DataFrame containing employee records.

    Returns:
        A tuple of (clean_df, invalid_df).
    """
    logger.info("Executing validation checks against data contracts...")

    valid_mask = df.apply(
        lambda row: validate_salary(float(row["monthly_salary"]))
        and validate_email(str(row["email"])),
        axis=1,
    )

    clean_df = df[valid_mask].copy()
    invalid_df = df[~valid_mask].copy()

    logger.info(
        f"Validation checks complete. Valid: {len(clean_df)} records, "
        f"Invalid/Corrupted: {len(invalid_df)} records."
    )

    if not invalid_df.empty:
        for _idx, row in invalid_df.iterrows():
            logger.warning(
                f"Discarded record: ID={row['employee_id']}, Name='{row['name']}', "
                f"Reason: Failed Salary/Email rules (Salary={row['monthly_salary']})"
            )

    return clean_df, invalid_df
