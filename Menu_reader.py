"""
-----------------------------------------------------------------------
ASSIGNMENT 12A: THE CONFIGURABLE MENU & AUDITOR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. PHASE 1: External menu_config.txt file created in workspace.
[ ] 3. Program reads and parses the .txt file into a Dictionary.
[ ] 4. PHASE 2: break the dictionary into individual variables.
[ ] 6. Print each category and its details
[ ] 7. try/except used to prevent crashes on FileNotFoundError.
-----------------------------------------------------------------------
"""
def read_menu():
    menus = {}

    try:
        with open("menu.txt", "r") as file:
            for line in file:
                parts = line.strip().split(";")

                if len(parts) != 2:
                    continue

                category = parts[0].strip().upper()
                items = parts[1].strip()

                menus[category] = items

        return menus

    except FileNotFoundError:
        print("ERROR: menu.txt file not found.")
        return {}


def split_into_variables(menu_items):
    food = menu_items.get("FOOD", "")
    drinks = menu_items.get("DRINKS", "")
    extras = menu_items.get("ETRAS", "") 

    return food, drinks, extras


def print_menu(food, drinks, extras):

    print("\n===== MENU =====\n")

    if food:
        print("FOOD")
        for item in food.split(","):
            print(" -", item.strip())

    if drinks:
        print("\nDRINKS")
        for item in drinks.split(","):
            print(" -", item.strip())

    if extras:
        print("\nEXTRAS")
        for item in extras.split(","):
            print(" -", item.strip())


def main():
    menu_items = read_menu()

    food, drinks, extras = split_into_variables(menu_items)

    print_menu(food, drinks, extras)


main()