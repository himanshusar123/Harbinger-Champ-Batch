"""Main application entrypoint for the RetailMax Enterprise Data Pipeline.

Orchestrates the entire data pipeline flow:
    API Ingestion -> Transform -> Validate -> SQLite -> Analytics -> Report.

Contains annotations mapping back to the Sprints.
"""

import asyncio
import sys
from typing import Any

from retailmax.analytics.analyzer import generate_hr_report

# Sprint 8: Packaging - importing from modules inside our package
from retailmax.api.async_service import fetch_all_auxiliary_data
from retailmax.api.service import fetch_employees
from retailmax.database.db import save_employees_to_db
from retailmax.employees.transformer import transform_raw_employees
from retailmax.employees.validation import validate_employee_records
from retailmax.utils.logger import get_logger

logger = get_logger("app_orchestrator")


async def run_async_demographics_fetch() -> None:
    """Sprint 9: Async Demo.

    Fetches auxiliary data (weather, payroll status, attendance)
    concurrently without blocking the main thread execution.
    """
    logger.info("==========================================")
    logger.info("Sprint 9 Demo: Async Concurrency fetch")
    logger.info("==========================================")
    try:
        aux_data = await fetch_all_auxiliary_data()
        logger.info(f"Async data fetch results: {aux_data}")
    except Exception as e:
        logger.error(f"Async demo failed: {e}")
    logger.info("==========================================\n")


def run_pipeline() -> None:
    """Runs the synchronous ETL data pipeline end-to-end.

    Demonstrates Sprints 1, 2, 3, 4, 5, 8, and 11.
    """
    logger.info("=== Starting RetailMax Enterprise ETL Pipeline ===")

    # 1. Ingestion: Sprint 3 (REST API)
    try:
        raw_employees: list[dict[str, Any]] = fetch_employees()
    except Exception as e:
        logger.critical(f"Pipeline Ingestion Failed: {e}")
        sys.exit(1)

    # 2. Transformation: Sprint 4 (JSON -> DataFrame)
    df_raw = transform_raw_employees(raw_employees)

    # 3. Validation: Sprint 5 (Data Validation & Contracts)
    # Splits valid and invalid records to enforce clean corporate ingestion.
    clean_df, invalid_df = validate_employee_records(df_raw)

    # 4. Database Persistence: SQLite Storage
    # Save clean records to SQLite
    try:
        save_employees_to_db(clean_df)
    except Exception as e:
        logger.critical(f"Database Persistence Failed: {e}")
        sys.exit(1)

    # 5. Analytics & Report Generation: Sprint 11 (Mini Project)
    # Calculate bonuses using Sprint 2 (Type Hints) calculations,
    # generate a Markdown report, and print summary dashboard.
    report = generate_hr_report(clean_df)

    logger.info("=== Pipeline Run Finished Successfully! ===")
    logger.info("Generated Report Summary:")
    print(
        report[:400]
        + "\n... [Report truncated, view hr_report.md for full details] ...\n"
    )


if __name__ == "__main__":
    # First run the Async concurrent microservice fetch demo (Sprint 9)
    asyncio.run(run_async_demographics_fetch())

    # Then run the main ETL pipeline
    run_pipeline()
