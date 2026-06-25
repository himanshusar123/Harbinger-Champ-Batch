"""
Main execution script for Corporate Portfolio Risk Monitor (Solution).
"""

import logging
from config import RISK_WARNING_THRESHOLD, setup_application_logging
from core_pipeline import (
    APIClientError,
    BondAsset,
    StockAsset,
    get_market_price_safe,
)


def run_portfolio_monitor() -> None:
    """Ingests client portfolio records, fetches live prices, and checks risk limits."""
    # Setup application logging
    setup_application_logging()
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

    print("\n" + "=" * 85)
    print(
        f"{'Asset ID':<10} | {'Name':<12} | {'Asset Type':<10} | {'Price Source':<12} | {'Current Price':<13} | {'Risk Score':<10}"
    )
    print("=" * 85)

    for asset in portfolio:
        current_price = asset.purchase_price
        price_source = "PURCHASE"
        asset_type = "Stock" if isinstance(asset, StockAsset) else "Bond"

        # Tickers are only looked up for Stock assets
        if isinstance(asset, StockAsset):
            try:
                current_price = get_market_price_safe(asset.name)
                price_source = "API"
            except APIClientError as err:
                logging.error(
                    f"Transient API Error on {asset.name}. Falling back to purchase price. Error: {err}"
                )
                # Keep purchase_price and flag it
                price_source = "FALLBACK"

        # Calculate risk using polymorphism
        risk_score = asset.calculate_risk(current_price)
        total_portfolio_risk += risk_score

        # Check if asset risk exceeds threshold
        if risk_score > RISK_WARNING_THRESHOLD:
            logging.warning(
                f"HIGH RISK ALERT: Asset '{asset.name}' ({asset.asset_id}) has risk score {risk_score:.2f} (Threshold: {RISK_WARNING_THRESHOLD})"
            )

        print(
            f"{asset.asset_id:<10} | {asset.name:<12} | {asset_type:<10} | {price_source:<12} | ${current_price:<12.2f} | {risk_score:<10.2f}"
        )

    print("=" * 85)
    print(f"Total Portfolio Risk Index: {total_portfolio_risk:.2f}")
    print("=" * 85 + "\n")

    logging.info("Corporate Portfolio Risk Monitor completed successfully.")


if __name__ == "__main__":
    run_portfolio_monitor()
