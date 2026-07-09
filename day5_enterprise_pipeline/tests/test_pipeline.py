"""Unit Tests for RetailMax Enterprise Data Pipeline.

Demonstrates Sprint 6 (Unit Testing with Pytest).
"""

from retailmax.analytics.analyzer import calculate_bonus
from retailmax.employees.validation import validate_email, validate_salary


# Sprint 6 basic calculation function
def annual_salary(monthly: float) -> float:
    """Calculates annual salary from monthly base.

    Args:
        monthly: Monthly salary.

    Returns:
        Annual salary.
    """
    return monthly * 12


# Sprint 6 basic unit test
def test_salary_math() -> None:
    """Verifies basic monthly to annual salary multiplication."""
    assert annual_salary(50000.0) == 600000.0
    assert annual_salary(0.0) == 0.0


def test_calculate_bonus() -> None:
    """Verifies that bonuses are calculated correctly at the configured 10% rate."""
    assert calculate_bonus(100000.0) == 10000.0
    assert calculate_bonus(50000.0) == 5000.0


def test_validate_salary() -> None:
    """Verifies that the validation contract rejects negative and zero salaries."""
    assert validate_salary(1000.00) is True
    assert validate_salary(0.0) is False
    assert validate_salary(-5000.00) is False


def test_validate_email() -> None:
    """Verifies email validation rules."""
    assert validate_email("test@retailmax.com") is True
    assert validate_email("invalid-email") is False
    assert validate_email("john.doe@company.org") is True
