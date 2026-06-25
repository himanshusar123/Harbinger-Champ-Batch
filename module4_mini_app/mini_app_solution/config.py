"""
Configuration settings and logging setups for Corporate Portfolio Risk Monitor (Solution).
"""

import logging
import sys

# Volatility warning threshold
RISK_WARNING_THRESHOLD = 5000.0

# Logging Format config
LOG_FORMAT = "%(asctime)s [%(levelname)s] (%(filename)s:%(lineno)d) - %(message)s"


def setup_application_logging() -> None:
    """Configures application-wide logging formats and severity outputs."""
    logging.basicConfig(
        level=logging.INFO,
        format=LOG_FORMAT,
        handlers=[
            logging.StreamHandler(sys.stdout),
            # In a real app, we could also append to a local file
            logging.FileHandler("portfolio_monitor.log", mode="a", encoding="utf-8"),
        ],
    )
