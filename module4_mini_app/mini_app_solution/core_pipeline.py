"""
Core Models and Ingestion Pipelines for Corporate Portfolio Risk Monitor (Solution).
"""

import logging
import random
from abc import ABC, abstractmethod


# =====================================================================
# ✅ CUSTOM EXCEPTIONS
# =====================================================================
class PortfolioMonitorError(Exception):
    """Base exception for the portfolio monitoring application."""

    pass


class APIClientError(PortfolioMonitorError):
    """Raised when query connection or data formatting fails for the external financial API."""

    pass


# =====================================================================
# ✅ OBJECT MODELS
# =====================================================================
class Asset(ABC):
    """Abstract Base Class representing a corporate investment asset."""

    def __init__(self, asset_id: str, name: str, purchase_price: float):
        self.asset_id = asset_id
        self.name = name
        self.purchase_price = purchase_price

    @abstractmethod
    def calculate_risk(self, current_price: float) -> float:
        """Calculates and returns the risk score for this asset class."""
        pass


class StockAsset(Asset):
    """Represents a corporate equity/stock asset."""

    def __init__(
        self,
        asset_id: str,
        name: str,
        purchase_price: float,
        shares: int,
        volatility_index: float,
    ):
        super().__init__(asset_id, name, purchase_price)
        self.shares = shares
        self.volatility_index = volatility_index

    def calculate_risk(self, current_price: float) -> float:
        """Risk Formula: shares * current_price * volatility_index."""
        return round(self.shares * current_price * self.volatility_index, 2)


class BondAsset(Asset):
    """Represents a corporate debt/bond asset."""

    def __init__(
        self,
        asset_id: str,
        name: str,
        purchase_price: float,
        face_value: float,
        yield_rate: float,
    ):
        super().__init__(asset_id, name, purchase_price)
        self.face_value = face_value
        self.yield_rate = yield_rate

    def calculate_risk(self, current_price: float) -> float:
        """Risk Formula: face_value * yield_rate."""
        return round(self.face_value * self.yield_rate, 2)


# =====================================================================
# ✅ API CLIENT
# =====================================================================
def fetch_current_market_price(symbol: str) -> float:
    """Simulates querying a flaky external stock price REST API.

    DO NOT MODIFY.
    """
    tickers = {
        "AAPL": 175.50,
        "MSFT": 420.25,
        "GOOGL": 150.75,
        "AMZN": 180.00,
        "TSLA": 170.50,
    }

    if symbol not in tickers:
        raise ValueError(f"Unknown ticker symbol: {symbol}")

    # Simulate 30% failure rate
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
    try:
        return fetch_current_market_price(symbol)
    except (ConnectionError, ValueError) as err:
        logging.warning(
            f"Underlying connection failure querying ticker '{symbol}': {err}"
        )
        raise APIClientError(
            f"Failed to fetch market price for ticker: {symbol}"
        ) from err
