"""
Unit test verification file for Corporate Portfolio Risk Monitor (Solution).
"""

from core_pipeline import APIClientError, BondAsset, StockAsset, get_market_price_safe


def test_asset_risk_calculations():
    print("Testing asset risk calculation logic...")

    # Stock asset: shares=100, vol=0.15, price=200 -> Risk: 100 * 200 * 0.15 = 3000
    stock = StockAsset("A001", "AAPL", purchase_price=170.0, shares=100, volatility_index=0.15)
    assert stock.calculate_risk(200.0) == 3000.0, "Stock risk calculation failed!"

    # Bond asset: face_value=10000, yield=0.045 -> Risk: 10000 * 0.045 = 450
    bond = BondAsset("B001", "US-T-BOND", purchase_price=1000.0, face_value=10000.0, yield_rate=0.045)
    assert bond.calculate_risk(1010.0) == 450.0, "Bond risk calculation failed!"

    print("Asset risk tests passed!")


def test_api_client_error_mapping():
    print("Testing API client error handling...")

    # Test unknown ticker error mapping
    try:
        get_market_price_safe("INVALID_TICKER")
        raise AssertionError("get_market_price_safe did not raise APIClientError for unknown ticker!")
    except APIClientError:
        print("APIClientError correctly mapped for invalid ticker.")

    print("API mapping tests passed!")


if __name__ == "__main__":
    print("Running verification suite...")
    test_asset_risk_calculations()
    test_api_client_error_mapping()
    print("All unit tests run and verified successfully!")
