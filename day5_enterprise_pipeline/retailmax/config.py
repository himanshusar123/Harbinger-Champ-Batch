"""Configuration settings for the RetailMax Enterprise Data Pipeline.

Demonstrates Sprint 2 (Type Hints) and Sprint 8 (Packaging / Config Separation).
"""

import os
from typing import Final

# API Configurations
USERS_API_URL: Final[str] = "https://jsonplaceholder.typicode.com/users"

# Database Configurations
DB_FILE: Final[str] = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "retailmax_hr.db"
)

# Business Logic Coefficients
BONUS_PERCENTAGE: Final[float] = 0.10
TAX_PERCENTAGE: Final[float] = 0.15
MIN_VALID_SALARY: Final[float] = 0.0
