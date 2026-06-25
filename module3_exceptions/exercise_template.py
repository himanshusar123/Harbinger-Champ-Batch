"""
Module 3 Challenge: The Resilient DB Connector (Template)

Your task:
1. Define custom exceptions DatabaseConnectionError and DatabaseQueryError.
2. Complete the methods inside ResilientDBConnector to support mapping exceptions and retrying flaky queries.
"""

import logging
import random
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")


# TODO 1: Implement custom exceptions
class DatabaseConnectionError(Exception):
    """Raised when connection to database is lost or cannot be established."""

    pass


class DatabaseQueryError(Exception):
    """Raised when query execution fails due to permissions or syntax."""

    pass


class ResilientDBConnector:
    """Simulates a database client that connects, executes queries, and disconnects."""

    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        self.is_connected = False

    def connect(self) -> None:
        """Connects to the database."""
        logging.info(f"Connecting to database: {self.connection_string}...")
        self.is_connected = True

    def disconnect(self) -> None:
        """Closes the connection to the database."""
        logging.info("Disconnecting from database...")
        self.is_connected = False

    def _send_network_request(self, query: str) -> str:
        """Simulates raw network layer behavior.

        DO NOT MODIFY THIS METHOD.
        """
        if not self.is_connected:
            raise ConnectionError("No active connection established.")

        # Simulate network noise
        rand = random.random()
        if rand < 0.4:
            raise ConnectionResetError("Remote host reset connection.")
        elif rand < 0.6:
            raise PermissionError("Access denied for user 'read_only_user'.")

        return f"Results for: {query}"

    def execute_query(self, query: str) -> str:
        """Executes a query and maps low-level errors to custom domain exceptions.

        Args:
            query: SQL query to run.

        Returns:
            The raw query output string.
        """
        # TODO 2:
        # Wrap self._send_network_request(query) in a try-except block.
        # - Catch ConnectionError and ConnectionResetError -> Raise DatabaseConnectionError
        # - Catch PermissionError -> Raise DatabaseQueryError
        return self._send_network_request(query)

    def execute_query_with_retry(self, query: str, max_retries: int = 3) -> str:
        """Executes a query, retrying on connection errors, and cleaning up resources.

        Args:
            query: SQL query to run.
            max_retries: Max number of reconnection attempts before failing.

        Returns:
            The query results string.
        """
        # Ensure connection is established before querying
        self.connect()

        attempts = 0
        # TODO 3: Implement the retry and resource management logic.
        # - Run a loop that tries to call self.execute_query(query).
        # - Catch DatabaseConnectionError:
        #     - Increment attempts.
        #     - Log a warning: logging.warning(f"Connection lost. Retry {attempts}/{max_retries}...")
        #     - If attempts >= max_retries, log error and re-raise.
        #     - Sleep for 0.1 seconds: time.sleep(0.1)
        # - Catch DatabaseQueryError:
        #     - Do NOT retry. Log error and re-raise immediately.
        # - Ensure self.disconnect() is ALWAYS called at the end of execution (use finally).

        # Replace this placeholder
        try:
            return self.execute_query(query)
        except Exception as e:
            logging.error(f"Failed to execute query: {e}")
            raise
        finally:
            self.disconnect()


# =====================================================================
# Trainee Verification Area: Test Cases
# =====================================================================
if __name__ == "__main__":
    db = ResilientDBConnector("postgresql://admin:secret@10.0.0.5:5432/analytics")

    print("Running Resilient DB Connector tests (runs multiple times to test random states)...")

    for i in range(1, 4):
        print(f"\n--- Run {i} ---")
        try:
            result = db.execute_query_with_retry("SELECT * FROM users LIMIT 10")
            print("Query Success:", result)
        except DatabaseConnectionError:
            print("Query failed with: DatabaseConnectionError (Expected after max retries)")
        except DatabaseQueryError:
            print("Query failed with: DatabaseQueryError (Expected immediately on permissions issue)")
        except Exception as e:
            print("UNEXPECTED ERROR:", type(e), e)
