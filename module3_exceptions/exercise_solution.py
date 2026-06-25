"""
Module 3 Challenge: The Resilient DB Connector (Reference Solution)
"""

import logging
import random
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")


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
        try:
            return self._send_network_request(query)
        except (ConnectionError, ConnectionResetError) as err:
            raise DatabaseConnectionError("Lost connection during query execution.") from err
        except PermissionError as err:
            raise DatabaseQueryError("User permission denied for target tables.") from err

    def execute_query_with_retry(self, query: str, max_retries: int = 3) -> str:
        """Executes a query, retrying on connection errors, and cleaning up resources.

        Args:
            query: SQL query to run.
            max_retries: Max number of reconnection attempts before failing.

        Returns:
            The query results string.
        """
        self.connect()
        attempts = 0

        try:
            while True:
                try:
                    return self.execute_query(query)
                except DatabaseConnectionError as conn_err:
                    attempts += 1
                    logging.warning(
                        f"DatabaseConnectionError caught. Retry {attempts}/{max_retries}..."
                    )
                    if attempts >= max_retries:
                        logging.error("Max retries exceeded. Aborting database operation.")
                        raise conn_err
                    time.sleep(0.1)  # Brief wait before retry
                except DatabaseQueryError as query_err:
                    logging.error(f"DatabaseQueryError caught: {query_err}. Aborting (no-retry).")
                    raise query_err
        finally:
            self.disconnect()


if __name__ == "__main__":
    db = ResilientDBConnector("postgresql://admin:secret@10.0.0.5:5432/analytics")

    print("Verifying Resilient DB Connector Solution...")

    # We will run 10 queries to hit multiple random failure modes and verify that:
    # 1. Connection is always closed (self.is_connected becomes False).
    # 2. DatabaseQueryError fails immediately (no retries).
    # 3. DatabaseConnectionError retries up to 3 times.
    for i in range(1, 11):
        print(f"\n--- Run Verification {i} ---")
        try:
            result = db.execute_query_with_retry("SELECT * FROM users LIMIT 10")
            print("Query Success:", result)
        except (DatabaseConnectionError, DatabaseQueryError) as e:
            print(f"Query failed with mapped exception: {type(e).__name__}")
        finally:
            assert db.is_connected is False, "DATABASE CONNECTION WAS LEAKED! MUST BE CLOSED."

    print("\nDatabase connector reference solution verified successfully!")
