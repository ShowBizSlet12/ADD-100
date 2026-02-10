"""
-------------------------------------------------------
ASSIGNMENT 5A: INPUT VALIDATION
Calvin Hamill
[ ] 1. Header Docstring included.
[ ] 2. All 4 inputs have 'while' loop validation.
[ ] 3. The Chaperone loop uses .upper() and correct Boolean logic.
[ ] 4. I have pinned a variable in the WATCH window and took a screenshot.
-------------------------------------------------------
"""


# First name 

first_name = input("Enter First Name: ")
while first_name == "":
    print("First name cannot be blank.")
    first_name = input("Enter First Name: ")

# Last name

last_name = input("Enter Last Name: ")
while last_name == "":
    print("Last name cannot be blank.")
    last_name = input("Enter Last Name: ")

#Chaperone 

chaperone = input("Will you chaperone? (Y/N): ").upper()
while chaperone != "Y" and chaperone != "N":
    print("Enter Y or N only.")
    chaperone = input("Will you chaperone? (Y/N): ").upper()

#Phone number 

phone = input("Enter Phone Number: ")
while phone == "":
    print("Phone number cannot be blank.")
    phone = input("Enter Phone Number: ")

# Ticket count 

tickets = 0
while True:
    try:
        tickets = int(input("How many tickets? "))
        if tickets > 0:
            break
        print("Ticket count must be greater than 0.")
    except ValueError:
        print("Please enter a valid NUMBER.")


# Confirmation
print("REGISTRATION COMPLETE")
print(f"Name: {first_name} {last_name}")
if chaperone == "Y":
    print("Chaperone: Yes")
else:
    print("Chaperone: No")
print(f"Phone: {phone}")
print(f"Tickets: {tickets}")