"""
Module 2 Challenge: JSON Ingestor (Reference Solution)
"""

import json
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any


class DataIngestor(ABC):
    """Abstract Base Class for Data Ingestors."""

    def __init__(self, filepath: str):
        self.filepath = filepath
        self._records: list[dict[str, Any]] = []

    @abstractmethod
    def parse(self) -> None:
        """Parses the data from the source filepath."""
        pass

    @property
    @abstractmethod
    def records(self) -> list[dict[str, Any]]:
        """Returns the parsed records."""
        pass

    def get_record_count(self) -> int:
        """Returns the total number of records ingested."""
        return len(self._records)


class JSONIngestor(DataIngestor):
    """Data Ingestor for JSON format files."""

    def __init__(self, filepath: str):
        super().__init__(filepath)

    def parse(self) -> None:
        with open(self.filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            # Ensure loaded data is a list of dictionaries
            if isinstance(data, list):
                self._records = data
            elif isinstance(data, dict):
                self._records = [data]
            else:
                raise ValueError("JSON content must be an array or an object.")

    @property
    def records(self) -> list[dict[str, Any]]:
        return self._records


# =====================================================================
# Reference Solution Verification Area
# =====================================================================
if __name__ == "__main__":
    temp_json_path = "temp_solution_data.json"
    dummy_data = [
        {"id": 101, "item": "Laptop", "price": 1200},
        {"id": 102, "item": "Keyboard", "price": 150},
        {"id": 103, "item": "Monitor", "price": 300},
    ]

    with open(temp_json_path, "w") as f:
        json.dump(dummy_data, f)

    print("Verifying JSONIngestor Reference Solution...")

    try:
        ingestor = JSONIngestor(temp_json_path)
        ingestor.parse()

        # Assertions
        assert ingestor.get_record_count() == 3
        assert ingestor.records[0]["item"] == "Laptop"
        assert ingestor.records[2]["price"] == 300

        # Try mutating records
        try:
            ingestor.records = []
            raise AssertionError("records property was modified but should be read-only!")
        except AttributeError:
            pass  # Expected exception

        print("JSONIngestor reference solution verified successfully!")
    finally:
        temp_file = Path(temp_json_path)
        if temp_file.exists():
            temp_file.unlink()
