"""Logging utility for RetailMax Enterprise Data Pipeline.

Provides clean console output with levels. Fully type hinted.
"""

import logging
import sys

# Configure standard formatting
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)


def get_logger(name: str) -> logging.Logger:
    """Creates or returns a logger with the given name.

    Args:
        name: Name of the logger, typically __name__.

    Returns:
        An instance of logging.Logger.
    """
    return logging.getLogger(name)
