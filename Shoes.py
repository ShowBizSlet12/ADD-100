"""
ASSIGNMENT 9B: SPRINT 2 - FUNCTIONAL STUBS
Project: Shoe Store Sales Tracker v1.0
Developer: Calvin
"""

# GLOBAL CONSTANTS
INVENTORY_FILE = "inventory.txt"
SALES_HISTORY_FILE = "sales_history.txt"


def get_salesperson():
    """Collects the sales associate's name."""
    # TODO: Ask user for sales team member name
    return "Alex Johnson"


def get_sale_details():
    """Collects the shoe brand, model, size, and price."""
    # TODO: Ask for brand, model, size
    # TODO: Load price from inventory file
    return {
        "brand": "Nike",
        "model": "Air Max",
        "size": 10,
        "price": 170.00
    }


def preview_sale(salesperson, sale_data):
    """Displays a preview of the sale before confirming."""
    # TODO: Print formatted preview
    # TODO: Ask user to confirm sale
    pass


def record_sale(salesperson, sale_data):
    """Saves the sale information to the sales history file."""
    # TODO: Append sale data to sales_history.txt
    # TODO: Store salesperson name with the sale
    pass


def print_receipt(salesperson, sale_data):
    """Prints a formatted receipt for the store record."""
    # TODO: Print formatted receipt output
    pass


def main():
    # 1. Identity Phase
    salesperson = get_salesperson()

    # 2. Data Collection Phase
    sale_info = get_sale_details()

    # 3. Preview Phase
    preview_sale(salesperson, sale_info)

    # 4. Record Sale Phase
    record_sale(salesperson, sale_info)

    # 5. Receipt Phase
    print_receipt(salesperson, sale_info)


main()