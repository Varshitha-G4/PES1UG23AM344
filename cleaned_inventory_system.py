# cleaned_inventory_system.py
"""
A simple inventory management system.

This module allows adding, removing, and tracking items in an inventory,
with functionality to save and load data from a JSON file.
"""

import json
import logging
from datetime import datetime
from typing import Dict, List, Optional

# Configure basic logging
logging.basicConfig(
    level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s'
)


# FIX E501: Broke the long function signature
def add_item(
    stock_data: Dict[str, int],
    item: str,
    qty: int,
    logs: Optional[List[str]] = None
) -> None:
    """
    Adds a specified quantity of an item to the stock.
    """
    if logs is None:
        logs = []

    if (not isinstance(item, str) or
            not isinstance(qty, int)):
        logging.warning(
            "Invalid type for item or quantity. "
            "Item must be str, qty must be int."
        )
        return

    if not item:
        logging.warning("Attempted to add an item with no name.")
        return

    stock_data[item] = stock_data.get(item, 0) + qty

    log_message = f"Added {qty} of {item}"
    logs.append(f"{datetime.now()}: {log_message}")
    logging.info(log_message)


def remove_item(
    stock_data: Dict[str, int], item: str, qty: int
) -> None:
    """
    Removes a specified quantity of an item from the stock.
    """
    try:
        if not isinstance(item, str) or not isinstance(qty, int):
            logging.warning("Invalid type for item or quantity.")
            return

        if item not in stock_data:
            logging.warning(
                f"Attempted to remove '{item}', which is not in stock."
            )
            return

        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
            logging.info(
                f"Removed '{item}' from stock as quantity reached zero."
            )
        else:
            logging.info(f"Removed {qty} of '{item}'.")

    except KeyError:
        logging.error(
            f"KeyError: Tried to remove '{item}' which does not exist."
        )
    except TypeError:
        logging.error("TypeError: Invalid types passed to remove_item.")


def get_qty(stock_data: Dict[str, int], item: str) -> int:
    """
    Gets the current quantity of a specific item.
    """
    return stock_data.get(item, 0)


def load_data(file: str = "inventory.json") -> Dict[str, int]:
    """
    Loads inventory data from a JSON file.
    """
    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
            logging.info(f"Stock data loaded from {file}")
            return data
    except FileNotFoundError:
        logging.warning(
            f"Inventory file {file} not found. "
            "Starting with empty inventory."
        )
        return {}
    except json.JSONDecodeError:
        logging.error(
            f"Could not decode JSON from {file}. "
            "Starting with empty inventory."
        )
        return {}


# FIX E501: Broke the long function signature
def save_data(
    stock_data: Dict[str, int], file: str = "inventory.json"
) -> None:
    """
    Saves the current inventory data to a JSON file.
    """
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, indent=4)
            logging.info(f"Stock data saved to {file}")
    except IOError as e:
        logging.error(f"Could not write to file {file}: {e}")


def print_data(stock_data: Dict[str, int]) -> None:
    """
    Prints a report of all items and their quantities.
    """
    print("\n--- Items Report ---")
    if not stock_data:
        print("Inventory is empty.")
    for item, quantity in stock_data.items():
        print(f"{item} -> {quantity}")
    print("----------------------\n")


def check_low_items(
    stock_data: Dict[str, int], threshold: int = 5
) -> List[str]:
    """
    Returns a list of items that are at or below the threshold.
    """
    result = []
    for item, quantity in stock_data.items():
        if quantity <= threshold:
            result.append(item)
    return result


def main():
    """
    Main function to run the inventory management simulation.
    """
    stock_data = load_data("inventory.json")
    master_log = []

    add_item(stock_data, "apple", 10, master_log)
    add_item(stock_data, "banana", 15, master_log)

    add_item(stock_data, "banana", 5, master_log)  # Was -2

    add_item(stock_data, 123, "ten", master_log)

    remove_item(stock_data, "apple", 3)

    remove_item(stock_data, "orange", 1)

    print(f"Apple stock: {get_qty(stock_data, 'apple')}")
    print(f"Orange stock: {get_qty(stock_data, 'orange')}")

    low_items = check_low_items(stock_data, 10)
    print(f"Low items (<=10): {low_items}")

    print_data(stock_data)
    save_data(stock_data, "inventory.json")

    logging.info("Main execution finished.")


if __name__ == "__main__":
    main()

# FIX W292: This is now the last line, and it is a blank line.