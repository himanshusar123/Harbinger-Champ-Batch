"""
Main entry point for Corporate Portfolio Risk Monitor (Template).
"""

import logging
from models import BondAsset, StockAsset
from utils import APIClientError, get_market_price_safe


def run_portfolio_monitor():
    """Ingests corporate assets, fetches live prices, and generates a risk summary."""
    logging.info("Starting Corporate Portfolio Risk Monitor pipeline...")

    # Create dummy client portfolio assets
    portfolio = [
        StockAsset("A001", "AAPL", purchase_price=170.0, shares=100, volatility_index=0.15),
        StockAsset("A002", "MSFT", purchase_price=410.0, shares=50, volatility_index=0.12),
        StockAsset("A003", "TSLA", purchase_price=180.0, shares=200, volatility_index=0.35),
        BondAsset("B001", "US-T-BOND", purchase_price=1000.0, face_value=10000.0, yield_rate=0.045),
        BondAsset("B002", "CORP-BOND", purchase_price=950.0, face_value=5000.0, yield_rate=0.062),
    ]

    total_portfolio_risk = 0.0

    print("\n" + "=" * 80)
    print(f"{'Asset ID':<10} | {'Name':<12} | {'Asset Type':<10} | {'Price Source':<12} | {'Current Price':<13} | {'Risk Score':<10}")
    print("=" * 80)

    # TODO 1: Process each asset in the portfolio
    for asset in portfolio:
        current_price = asset.purchase_price
        price_source = "PURCHASE"

        # Determine asset type string
        asset_type = "Stock" if isinstance(asset, StockAsset) else "Bond"

        # TODO 2: Query API for StockAsset current price (Bonds do not need API lookup)
        # Wrap in a try-except block to catch APIClientError:
        # - If exception: log warning: logging.warning("...")
        #   and fallback to purchase_price (already set).
        # - If success: set current_price and price_source = "API"

        # TODO 3: Calculate risk score using asset.calculate_risk(current_price)
        risk_score = 0.0
        total_portfolio_risk += risk_score

        # TODO 4: Check if risk exceeds warning threshold (e.g., 5000.0)
        # If yes, log warning: logging.warning(f"HIGH RISK DETECTED: {asset.name}...")

        print(
            f"{asset.asset_id:<10} | {asset.name:<12} | {asset_type:<10} | {price_source:<12} | ${current_price:<12.2f} | {risk_score:<10.2f}"
        )

    print("=" * 80)
    print(f"Total Portfolio Risk Index: {total_portfolio_risk:.2f}")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    run_portfolio_monitor()
