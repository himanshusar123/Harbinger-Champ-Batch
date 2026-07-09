"""SQLite persistence module.

Handles SQLite connection and table population.
"""

import sqlite3

import pandas as pd

from retailmax.config import DB_FILE
from retailmax.utils.logger import get_logger

logger = get_logger(__name__)


def init_database() -> None:
    """Initializes the SQLite schema if it doesn't already exist.

    Ensures the target database has the correct table structure.
    """
    logger.info(f"Initializing database schema in {DB_FILE}")
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            employee_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            city TEXT NOT NULL,
            company_name TEXT NOT NULL,
            monthly_salary REAL NOT NULL,
            annual_salary REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()
    logger.info("Database schema initialized successfully")


def save_employees_to_db(df: pd.DataFrame) -> None:
    """Saves the cleaned employee DataFrame to the SQLite database.

    Args:
        df: Cleaned and validated employee Pandas DataFrame.
    """
    init_database()

    logger.info(f"Writing {len(df)} employee records to SQLite...")
    conn = sqlite3.connect(DB_FILE)

    # Use pandas to_sql to easily write the DataFrame to SQLite
    df.to_sql("employees", conn, if_exists="replace", index=False)

    conn.commit()
    conn.close()
    logger.info("Database write complete")
