"""
-----------------------------------------------------------------------
ASSIGNMENT 5B: THE ATM
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. 'while' loop keeps the program running.
[ ] 3. I have handled ValueErrors (Type Safety).
[ ] 4. I have blocked Negative numbers and Overdrafts.
[ ] 5. I have pinned the 'balance' in the WATCH window and took a screenshot.
By Calvin 
Description: A simple ATM machine that allows users to check balance,
deposit money, withdraw money, and exit safely using a loop.
-----------------------------------------------------------------------
"""

# Starting balance
balance = 1000.00
running = True

print("Welcome to The Simple ATM!")

# Main Loop
while running:

    print("--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    try:
        choice = int(input("Select an option (1-4): "))

        #1 Check Balance
        if choice == 1:
            print(f"Your current balance is: ${balance:.2f}")

        #2 Deposit
        elif choice == 2:
            try:
                deposit = float(input("Enter deposit amount: $"))

                if deposit <= 0:
                    print("Deposit must be greater than $0.00")
                else:
                    balance += deposit
                    print(f"Deposited: ${deposit:.2f}")
                    print(f"New balance: ${balance:.2f}")

            except ValueError:
                print("Please enter a valid number.")

        #3 Withdraw
        elif choice == 3:
            try:
                withdraw = float(input("Enter withdrawal amount: $"))

                if withdraw <= 0:
                    print("Withdrawal must be greater than $0.00")
                elif withdraw > balance:
                    print("Insufficient funds. No overdrafts allowed.")
                else:
                    balance -= withdraw
                    print(f"Withdrawn: ${withdraw:.2f}")
                    print(f"New balance: ${balance:.2f}")

            except ValueError:
                print("Please enter a valid number.")

        #4 Exit
        elif choice == 4:
            running = False
            print("Thank you for using The Simple ATM!")

        # Invalid Menu Choice
        else:
            print("Invalid choice. Please select 1-4.")

    except ValueError:
        print("Please enter a number between 1 and 4.")
