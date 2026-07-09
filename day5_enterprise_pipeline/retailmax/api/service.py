"""Synchronous REST API service.

Demonstrates Sprint 3 (REST API) and Sprint 2 (Type Hints).
"""

from typing import Any

import requests

from retailmax.config import USERS_API_URL
from retailmax.utils.logger import get_logger

logger = get_logger(__name__)


def fetch_employees() -> list[dict[str, Any]]:
    """Fetches employee data from the REST API.

    Returns:
        A list of dictionaries representing individual employees.

    Raises:
        requests.RequestException: If the HTTP request fails.
    """
    logger.info(f"Initiating GET request to {USERS_API_URL}")
    response = requests.get(USERS_API_URL, timeout=10)

    # Sprint 3: Print HTTP Status and Parse JSON
    logger.info(f"API Response Status Code: {response.status_code}")
    response.raise_for_status()

    employees: list[dict[str, Any]] = response.json()
    logger.info(f"Successfully retrieved {len(employees)} raw records from API")
    return employees
