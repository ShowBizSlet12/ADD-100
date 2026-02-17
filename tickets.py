"""
-----------------------------------------------------------------------
ASSIGNMENT 6A: TICKET SALES
-----------------------------------------------------------------------
[ ] 1. Create a list of 20 seats (numbered 1-20).
[ ] 2. Display the list of available seats.
[ ] 3. Ask user for a seat number (0 to quit).
[ ] 4. Remove the selected seat from the list.
[ ] 5. Handle invalid inputs (seat taken or doesn't exist).
[ ] 6. Repeat until user quits or seats are empty.
-----------------------------------------------------------------------
"""

# Create list of seats 1–20
seats = list(range(1, 21))

TICKET_PRICE = 15
total_sales = 0

# Repeat until user quits or seats are empty
while len(seats) > 0:

    # Display available seats
    print("Available Seats:", seats)

    try:
        # Ask for input
        choice = int(input("Select a seat number (0 to quit): "))

        # Quit option
        if choice == 0:
            print(f"Total sales today: ${total_sales}")

            break

        # Validate input
        if choice in seats:
            # Remove selected seat
            seats.remove(choice)
            total_sales += TICKET_PRICE
            print(f"Seat {choice} purchased for ${TICKET_PRICE}")
        else:
            print("Seat taken or invalid seat number.")

    except ValueError:
        print("Invalid input. Please enter a number.")

# If seats sell out
if len(seats) == 0:
    print("The show is full!")
    print(f"Total sales today: ${total_sales}")
