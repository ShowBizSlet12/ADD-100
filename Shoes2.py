"""
ASSIGNMENT 10B: SPRINT 3 - REFACTORING & DATA ACCOUNTABILITY
Project: Shoe Store Sales Tracker v3.0
Developer: Calvin
"""

# GLOBAL CONSTANTS (Store Rules)
INVENTORY_FILE = "inventory.txt"
SALES_HISTORY_FILE = "sales_history.txt"
DEFAULT_SIZE = 9
DEFAULT_PRICE = 100.00

# Example tuple structure for available brands
BRANDS = ("Nike", "Adidas", "Puma", "New Balance")


def get_salesperson():
    """Collect the sales associate's name."""
    name = input("Sales team member's name: ").title()
    return name


def get_sale_details(default_size=DEFAULT_SIZE):
    """
    Collects sale information from the user.
    Uses default shoe size if none is entered.
    """
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
    # I choose this return insted of the standard if else becouse it is shorter.
    # it works by if the user enters y it returns true if not it returns false. 
    return confirm.lower() == "y"


def record_sale(salesperson, sale_data):
    """Stores the sale in the sales history file."""
# The "with open" statement is used to safely open a file.
# It automatically closes the file after writing, which sould prevents errors.
# The "a" mode means append, so new sales are added instead of deleting previous data
# This is key so that i can store sales data form a while back to learn trends from. 
    with open(SALES_HISTORY_FILE, "a") as file:
        file.write(
            f"{salesperson},"
            f"{sale_data['brand']} {sale_data['model']},"
            f"{sale_data['size']},"
            f"{sale_data['price']}\n"
        )


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

    # 3. Preview Phase
    confirmed = preview_sale(
        salesperson=salesperson_name,
        sale_data=sale_info
    )

    if confirmed:
        # 4. Record Phase
        record_sale(
            salesperson=salesperson_name,
            sale_data=sale_info
        )

        # 5. Receipt Phase
        print_receipt(
            salesperson=salesperson_name,
            sale_data=sale_info
        )
    else:
        print("Sale cancelled.")


main()
