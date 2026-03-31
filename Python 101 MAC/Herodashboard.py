"""
-----------------------------------------------------------------------
ASSIGNMENT 11A: THE OFFICE HERO DASHBOARD
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global constants OFFICE_NAME and TAX_RATE defined in ALL_CAPS.
[ ] 3. Function 'process_expenses' returns TWO values (float, string).
[ ] 4. main() function uses try/except for numeric price/qty inputs.
[ ] 5. main() calls function using KEYWORD ARGUMENTS.
[ ] 6. main() correctly unpacks and prints both return values.
-----------------------------------------------------------------------
"""

# GLOBAL CONSTANTS
OFFICE_NAME = "Calvin's Office Supply for Pros"
TAX_RATE = 0.07


def process_expenses(item_name, price, quantity):
    """
    Calculates total expense including tax and returns:
    (final_total, summary_string)
    """
    subtotal = price * quantity
    tax = subtotal * TAX_RATE
    final_total = subtotal + tax

    summary = f"{quantity} x {item_name} | Subtotal: ${subtotal:.2f} | Total w/ Tax: ${final_total:.2f}"

    return final_total, summary  # MULTIPLE RETURN


def main():
    print(f"Welcome to {OFFICE_NAME} Expense Dashboard\n")

    item_name = input("Enter item name: ")

    # PRICE INPUT
    try:
        price = float(input("Enter item price: "))
    except ValueError:
        print("Invalid price. Defaulting to $1.00")
        price = 1.00

    # QUANTITY INPUT
    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Invalid quantity. Defaulting to 1")
        quantity = 1

    # FUNCTION CALL (KEYWORD ARGUMENTS + UNPACKING)
    final_cost, summary_text = process_expenses(
        item_name=item_name,
        price=price,
        quantity=quantity
    )

    print("\n--- RECEIPT ---")
    print(summary_text)
    print(f"Final Cost: ${final_cost:.2f}")


# RUNNING PROGRAM
main()