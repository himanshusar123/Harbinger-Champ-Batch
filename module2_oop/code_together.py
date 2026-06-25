"""
Module 2: Object-Oriented Programming (OOP) - Code Together
Theme: Building a structured, extensible Data Ingestion Pipeline.
"""

import csv
from abc import ABC, abstractmethod
from io import StringIO
from typing import Any


# =====================================================================
# ✅ ABSTRACT BASE CLASS (The Interface / Contract)
# =====================================================================
class DataIngestor(ABC):
    """Abstract Base Class defining the contract for all Data Ingestors."""

    def __init__(self, source_name: str):
        self.source_name = source_name
        self._records: list[dict[str, Any]] = []  # Protected attribute

    @abstractmethod
    def parse(self) -> None:
        """Parses the data from the source. Must be implemented by subclasses."""
        pass

    # A concrete helper method inherited by all subclasses
    def show_summary(self) -> None:
        """Prints a standardized summary of the ingested dataset."""
        print(f"--- Ingestion Summary [{self.source_name}] ---")
        print(f"Total Records Ingested: {len(self._records)}")
        for idx, record in enumerate(self._records[:3], start=1):
            print(f"  Record {idx}: {record}")
        if len(self._records) > 3:
            print("  ...")
        print("-" * 40)

    # Property (Getter) to access encapsulated data safely
    @property
    def records(self) -> list[dict[str, Any]]:
        """Exposes the internal records list as a read-only property."""
        return self._records


# =====================================================================
# ✅ CONCRETE SUBCLASS (Implementing CSV Ingestion)
# =====================================================================
class CSVIngestor(DataIngestor):
    """Data Ingestor specifically designed to parse CSV content."""

    def __init__(self, source_name: str, csv_data: str):
        # Call the parent constructor
        super().__init__(source_name)
        self.csv_data = csv_data

    # Implement the abstract method
    def parse(self) -> None:
        # Simulate reading from a file using StringIO
        f = StringIO(self.csv_data.strip())
        reader = csv.DictReader(f)

        self._records = []
        for row in reader:
            # Strip whitespace from keys/values
            cleaned_row = {k.strip(): v.strip() for k, v in row.items()}
            self._records.append(cleaned_row)


# =====================================================================
# Execution Demo
# =====================================================================
if __name__ == "__main__":
    raw_csv = """name, role, department
    Alice, Engineer, Platform
    Bob, Architect, Cloud
    Charlie, Manager, Operations
    """

    print("Attempting to instantiate DataIngestor directly...")
    try:
        # This will fail because DataIngestor contains abstract methods
        ingestor = DataIngestor("Generic")
    except TypeError as e:
        print("Success: Direct instantiation prevented as expected!")
        print("Error message:", e)

    print("\nInstantiating and parsing using CSVIngestor...")
    csv_ingestor = CSVIngestor("CRM Exports", raw_csv)
    csv_ingestor.parse()

    # Call the inherited concrete method
    csv_ingestor.show_summary()

    # Access the read-only property
    print("Direct Property Access (First Record Name):")
    print(csv_ingestor.records[0]["name"])
