"""API Ingestion Subpackage.

Contains synchronous (requests) and asynchronous (httpx) API handlers.
"""

from retailmax.api.service import fetch_employees

__all__ = ["fetch_employees"]
