"""Analytics and Report Generator.

Demonstrates Sprint 2 (Type Hints), Sprint 4 (Transform API Data),
and Sprint 11 (Mini Project Analytics & Reports).
"""

import os

import pandas as pd

from retailmax.config import BONUS_PERCENTAGE
from retailmax.utils.logger import get_logger

logger = get_logger(__name__)


def calculate_bonus(salary: float) -> float:
    """Calculates employee bonus based on salary.

    Demonstrates Sprint 2 Type Hints:
        - salary: float
        - return type: float

    Args:
        salary: The annual or monthly salary of the employee.

    Returns:
        The calculated bonus amount.
    """
    return salary * BONUS_PERCENTAGE


def generate_hr_report(df: pd.DataFrame) -> str:
    """Performs business aggregations and generates a structured HR report.

    Args:
        df: Validated employee Pandas DataFrame.

    Returns:
        A Markdown string of the generated report.
    """
    logger.info("Running pipeline analytics metrics...")

    # Calculate metrics
    total_headcount: int = len(df)
    average_annual_salary: float = float(df["annual_salary"].mean())
    max_annual_salary: float = float(df["annual_salary"].max())

    # Apply type-hinted bonus calculation
    df["bonus"] = df["annual_salary"].apply(calculate_bonus)
    total_bonus_payout: float = float(df["bonus"].sum())

    # Aggregation: Headcount and Avg Salary by City
    city_summary = (
        df.groupby("city")
        .agg(
            headcount=("employee_id", "count"),
            avg_salary=("annual_salary", "mean"),
        )
        .reset_index()
    )

    # Format the city summary table as Markdown
    city_table_rows = [
        "| City | Headcount | Average Salary ($) |",
        "| --- | --- | --- |",
    ]
    for _, row in city_summary.iterrows():
        city_table_rows.append(
            f"| {row['city']} | {row['headcount']} | {row['avg_salary']:,.2f} |"
        )
    city_table_markdown = "\n".join(city_table_rows)

    # Construct the final Markdown report
    report_md = f"""# RetailMax Enterprise HR Analytics Report

Generated from production REST API pipeline data.

## Summary Metrics
* **Total Headcount:** {total_headcount}
* **Average Annual Salary:** ${average_annual_salary:,.2f}
* **Maximum Annual Salary:** ${max_annual_salary:,.2f}
* **Total Est. Bonus Payout (10%):** ${total_bonus_payout:,.2f}

## Geographic Breakdown
{city_table_markdown}

## Employee Directory with Bonuses
"""
    # Append employee list
    report_md += "| ID | Name | Email | Annual Salary ($) | Bonus ($) |\n"
    report_md += "| --- | --- | --- | --- | --- |\n"
    for _, row in df.sort_values(by="annual_salary", ascending=False).iterrows():
        report_md += (
            f"| {row['employee_id']} | {row['name']} | {row['email']} | "
            f"{row['annual_salary']:,.2f} | {row['bonus']:,.2f} |\n"
        )

    # Write report to disk
    report_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "..", "hr_report.md"
    )
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report_md)

    logger.info(f"HR report generated successfully at {os.path.abspath(report_path)}")
    return report_md
