"""
Models module for Corporate Portfolio Risk Monitor (Template).
"""

from abc import ABC, abstractmethod


class Asset(ABC):
    """Abstract Base Class representing an investment asset."""

    def __init__(self, asset_id: str, name: str, purchase_price: float):
        self.asset_id = asset_id
        self.name = name
        self.purchase_price = purchase_price

    # TODO 1: Implement abstract method calculate_risk
    @abstractmethod
    def calculate_risk(self, current_price: float) -> float:
        """Calculates and returns the risk score for this asset.

        Must be overridden by concrete asset subclasses.
        """
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
        # TODO 2: Call parent constructor and initialize shares/volatility_index
        super().__init__(asset_id, name, purchase_price)
        self.shares = shares
        self.volatility_index = volatility_index

    # TODO 3: Implement calculate_risk for stock assets
    # Risk Formula: shares * current_price * volatility_index
    def calculate_risk(self, current_price: float) -> float:
        return 0.0


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
        # TODO 4: Call parent constructor and initialize face_value/yield_rate
        super().__init__(asset_id, name, purchase_price)
        self.face_value = face_value
        self.yield_rate = yield_rate

    # TODO 5: Implement calculate_risk for bond assets
    # Risk Formula: face_value * yield_rate
    def calculate_risk(self, current_price: float) -> float:
        return 0.0
