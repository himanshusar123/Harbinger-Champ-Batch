"""Database Persistence Subpackage.

Handles SQLite connection and table operations.
"""

from retailmax.database.db import save_employees_to_db

__all__ = ["save_employees_to_db"]
