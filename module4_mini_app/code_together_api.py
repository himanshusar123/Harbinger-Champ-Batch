"""
Module 4: Working with APIs - Code Together
Theme: Fetching and parsing data from REST API endpoints safely.
"""

import json
import logging
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)


def fetch_todo_item(todo_id: int) -> dict | None:
    """Fetches a single Todo item from JSONPlaceholder REST API using urllib.

    Args:
        todo_id: The ID of the item to retrieve.

    Returns:
        A dictionary containing todo details, or None if fetch failed.
    """
    url = f"https://jsonplaceholder.typicode.com/todos/{todo_id}"
    req = Request(url, headers={"User-Agent": "Enterprise-Python-App/1.0"})

    try:
        logging.info(f"Sending GET request to: {url}")
        # Fetch URL with a 5-second timeout to prevent hanging
        with urlopen(req, timeout=5.0) as response:
            status_code = response.status
            logging.info(f"Response status: {status_code}")

            # Read and parse body
            raw_body = response.read().decode("utf-8")
            data = json.loads(raw_body)
            return data

    except HTTPError as e:
        # Handles server issues (e.g., 404, 500)
        logging.error(f"HTTP Error occurred: Code {e.code} - {e.reason}")
    except URLError as e:
        # Handles connection issues, dns resolution, network drops
        logging.error(f"Network Connection/URL Error: {e.reason}")
    except json.JSONDecodeError as e:
        # Handles corrupt or malformed payload
        logging.error(f"Failed to parse response body as JSON: {e}")
    except Exception as e:
        logging.error(f"Unexpected error occurred: {e}")

    return None


if __name__ == "__main__":
    print("--- 1. Fetching Valid Todo Item ---")
    todo = fetch_todo_item(1)
    if todo:
        print("Successfully parsed Todo item:")
        print(f"  Title:  {todo.get('title')}")
        print(f"  Status: {'Completed' if todo.get('completed') else 'Pending'}")
    else:
        print("Failed to fetch Todo.")

    print("\n--- 2. Fetching Invalid Todo Item (Triggering 404) ---")
    # There are only 200 items in JSONPlaceholder, so 999 will trigger a 404 Error
    todo_error = fetch_todo_item(999)
    if todo_error:
        print("Todo item found:", todo_error)
    else:
        print("Gracefully handled 404 response!")
