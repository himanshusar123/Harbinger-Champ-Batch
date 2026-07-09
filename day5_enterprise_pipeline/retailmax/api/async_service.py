"""Asynchronous API Ingestion Demo.

Demonstrates Sprint 9 (Async / Concurrency vs Sequential fetching).
"""

import asyncio
from typing import Any

import httpx

from retailmax.utils.logger import get_logger

logger = get_logger(__name__)


async def fetch_mock_endpoint(
    client: httpx.AsyncClient, name: str, delay: float
) -> dict[str, Any]:
    """Simulates fetching from a specific microservice with a artificial delay.

    Args:
        client: The HTTPX AsyncClient.
        name: Name of the microservice (e.g. 'payroll', 'attendance').
        delay: Sleep delay in seconds to simulate network latency.

    Returns:
        A dictionary containing simulated API response data.
    """
    logger.info(f"[Async] Starting fetch for {name.capitalize()} API...")
    # Simulate non-blocking sleep (network wait)
    await asyncio.sleep(delay)
    logger.info(f"[Async] Completed fetch for {name.capitalize()} API")
    return {"service": name, "status": "online", "latency_ms": int(delay * 1000)}


async def fetch_all_auxiliary_data() -> list[dict[str, Any]]:
    """Fetches data from three distinct auxiliary services concurrently.

    Runs them concurrently using asyncio.gather to avoid sequential blocking.
    """
    logger.info("Initializing concurrent fetch of auxiliary APIs...")
    async with httpx.AsyncClient() as client:
        # Define tasks for concurrent execution
        # Fetching Weather API, Payroll API, and Attendance API concurrently
        task_weather = fetch_mock_endpoint(client, "weather", 0.5)
        task_payroll = fetch_mock_endpoint(client, "payroll", 0.8)
        task_attendance = fetch_mock_endpoint(client, "attendance", 0.4)

        # Execute all tasks concurrently (asyncio.gather)
        results: list[dict[str, Any]] = list(
            await asyncio.gather(task_weather, task_payroll, task_attendance)
        )

        logger.info("Successfully fetched all auxiliary API data concurrently!")
        return results
