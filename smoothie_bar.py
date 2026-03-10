"""
-----------------------------------------------------------------------
ASSIGNMENT 9A: THE SMOOTHIE SPRINT
By, Calvin 
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global Constants BASES and FRUITS defined as Tuples.
[ ] 3. Professional function get_price(size) returns a float.
[ ] 4. Professional function blend(size, base, fruit, scoops) for output.
[ ] 5. main() function handles try/except for scoops (int).
[ ] 6. main() calls both functions correctly.
-----------------------------------------------------------------------
"""

# GLOBAL CONSTANTS 
BASES = ("Water", "Apple Juice", "Orange Juice", "Milk")
FRUITS = ("Strawberry", "Banana", "Mango", "Blueberry")


def get_price(size):
    """Return smoothie price based on size."""
    if size == "Small":
        return 3.00
    elif size == "Medium":
        return 4.00
    else:
        return 5.00


def blend(size, base, fruit, scoops):
    """Display the smoothie order."""
    print("--- Blending Smoothie ---")
    print(f"Size: {size}")
    print(f"Base: {base}")
    print(f"Fruit: {fruit}")
    print(f"Protein Scoops: {scoops}")


def main():
    print("Welcome to the Smoothie Bar")

    size = input("Size (Small/Medium/Large): ").title().strip()
    base = input(f"Choose a base({BASES}): ")
    fruit = input(f"Choose a fruit ({FRUITS}): ")
    try:
        scoops = int(input("How many protein scoops?: "))
    except ValueError:
        print("Invalid entry. Defaulting to 1 scoop.")
        scoops = 1

    price = get_price(size)

    blend(size, base, fruit, scoops)

    print(f"Total Cost: ${price:.2f}")


# Run the program
main()