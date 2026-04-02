"""
ASSIGNMENT 11B: SPRINT 4 - WRITING TO FILES
Project: Shoe Store Sales Tracker v4.0
Developer: Calvin
"""

import datetime

# GLOBAL CONSTANTS (Store Rules)
INVENTORY_FILE = "inventory.txt"
SALES_HISTORY_FILE = "sales_history.txt"
DEFAULT_SIZE = 9
DEFAULT_PRICE = 160.00

# Example tuple structure for available brands
BRANDS = ("Nike", "Adidas", "Puma", "New Balance","Brooks")


def get_salesperson():
    """Collect the sales associate's name."""
    name = input("Sales team member's name: ").title()
    return name


def get_sale_details(default_size=DEFAULT_SIZE):
    """Collects sale information from the user."""
    print(f"Available Brands: {BRANDS}")

    brand = input("Enter Shoe Brand: ")
    model = input("Enter Shoe Model: ")

    size_input = input(f"Enter Shoe Size (Default {default_size}): ")

    if size_input == "":
        size = default_size
    else:
        size = int(size_input)

    price_input = input("Enter Price: ")

    if price_input == "":
        price = DEFAULT_PRICE
    else:
        price = float(price_input)

    return {
        "brand": brand,
        "model": model,
        "size": size,
        "price": price
    }


def preview_sale(salesperson, sale_data):
    """Displays a preview of the sale before recording it."""
    print("\n-----------------------------------")
    print("SALE PREVIEW:")
    print(f"Sales team members name: {salesperson}")
    print(f"Shoe: {sale_data['brand']} {sale_data['model']}")
    print(f"Size: {sale_data['size']}")
    print(f"Price: ${sale_data['price']:.2f}")
    print("-----------------------------------")

    confirm = input("Confirm sale? (y/n): ")
    return confirm.lower() == "y"


def record_sale(salesperson, sale_data):
    """Stores the sale with timestamp in the sales history file."""

    # Generate timestamp
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(SALES_HISTORY_FILE, "a") as file:
        file.write(f"\n[{current_time}] SALE RECORD\n")
        file.write(f"Salesperson: {salesperson}\n")

        # Loop through dictionary (Sprint 4 requirement)
        for key, value in sale_data.items():
            file.write(f"{key.capitalize()}: {value}\n")

        file.write("-----------------------------\n")

    print("Sale successfully logged to system!")


def print_receipt(salesperson, sale_data):
    """Prints the receipt output."""

    print("\n====================================")
    print("        SHOE STORE SALES RECEIPT")
    print("====================================")
    print(f"Sales team members name: {salesperson.upper()}")
    print(f"BRAND: {sale_data['brand'].upper()}")
    print(f"MODEL: {sale_data['model'].upper()}")
    print(f"SIZE: {sale_data['size']}")
    print(f"PRICE: ${sale_data['price']:.2f}")
    print("------------------------------------")
    print("STATUS: SALE RECORDED")
    print("====================================")


def main():
    # 1. Identity Phase
    salesperson_name = get_salesperson()

    # 2. Data Collection Phase
    sale_info = get_sale_details()

    # 3. Preview Phase (KEYWORD ARGUMENTS)
    confirmed = preview_sale(
        salesperson=salesperson_name,
        sale_data=sale_info
    )

    if confirmed:
        # 4. Record Phase (KEYWORD ARGUMENTS)
        record_sale(
            salesperson=salesperson_name,
            sale_data=sale_info
        )

        # 5. Receipt Phase (KEYWORD ARGUMENTS)
        print_receipt(
            salesperson=salesperson_name,
            sale_data=sale_info
        )
    else:
        print("Sale cancelled.")


main()