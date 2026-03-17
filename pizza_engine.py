"""
-----------------------------------------------------------------------
ASSIGNMENT 10A: THE RESILIENT PIZZA ENGINE
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global constant TOPPINGS defined as a Tuple in ALL_CAPS.
[ ] 3. Function 'make_pizza' defines 4 specific parameters.
[ ] 4. 'make_pizza' uses a DEFAULT value for is_delivery.
[ ] 5. main() displays the Global Pantry list to the user.
[ ] 6. main() calls the function using KEYWORD ARGUMENTS.
-----------------------------------------------------------------------
"""

# GLOBAL CONSTANTs 
TOPPINGS = ("Pepperoni", "Mushrooms", "Sausage", "Extra Cheese")


def make_pizza(customer, size, topping, is_delivery=False):

    print("PIZZA ORDER TICKET")
    print(f"Customer: {customer}")
    print(f"Size: {size}")
    print(f"Topping: {topping}")

    if is_delivery:
        print("Order Type: Delivery")
    else:
        print("Order Type: Pickup")


def main():
    """Handles user interaction and passes data to make_pizza."""

    customer_name = input("Customer name: ").title()
    size = input("Pizza size (Small, Medium, Large): ").title()

    # Show global toppings
    print(f"Available toppings: {TOPPINGS}")
    topping_choice = input("Choose a topping: ").title()

    # Delivery input with error safety
    delivery_input = input("Delivery? (yes/no): ").lower()

    try:
        if delivery_input == "yes":
            delivery = True
        elif delivery_input == "no":
            delivery = False
        else:
            raise ValueError
    except ValueError:
        print("Invalid input. Defaulting to pickup.")
        delivery = False

    # Function call using KEYWORD ARGUMENTS
    make_pizza(
        customer=customer_name,
        size=size,
        topping=topping_choice,
        is_delivery=delivery
    )


# Run the program
main()