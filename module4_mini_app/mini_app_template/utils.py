"""
Utility functions and exception handlers for Corporate Portfolio Risk Monitor (Template).
"""

import logging
import random
import sys

# TODO 1: Initialize logging configurations
# Standard format: '%(asctime)s [%(levelname)s] %(message)s'
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)


# TODO 2: Create a custom Exception class APIClientError
class APIClientError(Exception):
    """Raised when query connection or data formatting fails for the external financial API."""

    pass


def fetch_current_market_price(symbol: str) -> float:
    """Simulates querying a flaky external stock price REST API.

    DO NOT MODIFY THIS METHOD.
    """
    # Simulated ticker data
    tickers = {
        "AAPL": 175.50,
        "MSFT": 420.25,
        "GOOGL": 150.75,
        "AMZN": 180.00,
        "TSLA": 170.50,
    }

    if symbol not in tickers:
        raise ValueError(f"Unknown ticker symbol: {symbol}")

    # Simulate network noise (30% failure rate)
    rand = random.random()
    if rand < 0.20:
        raise ConnectionError("Network timeout connecting to api.marketdata.com.")
    elif rand < 0.30:
        raise ValueError("Corrupt empty JSON response received.")

    # Return base price with a tiny random variation
    variation = random.uniform(-2.0, 2.0)
    return round(tickers[symbol] + variation, 2)


def get_market_price_safe(symbol: str) -> float:
    """Gets market price, wrapping underlying network and value errors in a custom APIClientError.

    Args:
        symbol: Ticker symbol to query.

    Returns:
        The fetched current float price.
    """
    # TODO 3: Implement try-except mapping
    # - Call fetch_current_market_price(symbol)
    # - Catch ConnectionError or ValueError and raise APIClientError
    try:
        return fetch_current_market_price(symbol)
    except (ConnectionError, ValueError) as err:
        raise APIClientError(f"API Error fetching price for {symbol}: {err}") from err
