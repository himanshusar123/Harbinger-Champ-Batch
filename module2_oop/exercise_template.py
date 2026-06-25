"""
Module 2 Challenge: JSON Ingestor (Template)

Your task:
1. Subclass the abstract `DataIngestor` class.
2. Implement the `JSONIngestor` to read a JSON file and parse its contents.
3. Expose the parsed records via a read-only property `records`.
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

    # TODO: Implement the records property (getter)
    # Hint: Use the @property decorator
    @property
    @abstractmethod
    def records(self) -> list[dict[str, Any]]:
        """Returns the parsed records."""
        pass

    # TODO: Implement the get_record_count method
    def get_record_count(self) -> int:
        """Returns the total number of records ingested."""
        # Replace this placeholder
        return 0


# TODO: Implement JSONIngestor concrete subclass
class JSONIngestor(DataIngestor):
    """Data Ingestor for JSON format files."""

    def __init__(self, filepath: str):
        # TODO: Call superclass __init__
        pass

    def parse(self) -> None:
        # TODO: Open self.filepath, load using json module, and save to self._records
        pass

    # TODO: Implement records property (getter)
    # Hint: Return self._records
    @property
    def records(self) -> list[dict[str, Any]]:
        return []


# =====================================================================
# Trainee Verification Area: Test Cases
# =====================================================================
if __name__ == "__main__":
    # Setup: Create a temporary json file for testing
    temp_json_path = "temp_test_data.json"
    dummy_data = [
        {"id": 101, "item": "Laptop", "price": 1200},
        {"id": 102, "item": "Keyboard", "price": 150},
        {"id": 103, "item": "Monitor", "price": 300},
    ]

    with open(temp_json_path, "w") as f:
        json.dump(dummy_data, f)

    print("Running OOP Ingestor tests...")

    try:
        ingestor = JSONIngestor(temp_json_path)
        ingestor.parse()

        # Check record count
        cnt = ingestor.get_record_count()
        print(f"Record Count: {cnt}")  # Expected: 3

        # Check records contents
        recs = ingestor.records
        print("First Record:", recs[0])  # Expected: {'id': 101, 'item': 'Laptop', ...}

        # Check read-only protection (should fail/warn depending on execution)
        try:
            ingestor.records = []
            print("WARNING: records property is not read-only!")
        except AttributeError:
            print("Success: records property is correctly read-only.")

    except Exception as e:
        print("Failed with exception:", e)

    finally:
        # Cleanup temporary file
        temp_file = Path(temp_json_path)
        if temp_file.exists():
            temp_file.unlink()
