"""
-----------------------------------------------------------------------
ASSIGNMENT 6B: THE LOCKED CALENDAR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. MONTHS is defined as a constant tuple ().
[ ] 3. Program uses a for loop to display each month.
[ ] 4. 'try' and 'except' blocks catch a TypeError.
[ ] 5. Comments explain why the modification failed.
-----------------------------------------------------------------------
📚 ADD-100: Intro to Python
Author: Calvin
Description: Demonstrates data integrity using constants, tuples,
and error handling.
-----------------------------------------------------------------------
"""

# Constant 
MONTHS = (
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
)

# Display each month using a for loop
print("Calendar Months:")
for month in MONTHS:
    print(month)

print("Attempting illegal modification...")

try:
    # This line tries to change January to Smarch.
    MONTHS[0] = "Smarch"

except TypeError:
    # This runs instead of crashing the program.
    print("Error: You cannot change a system constant!")

# Program continues safely after handling the error
print("System running normally.")