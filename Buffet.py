"""
-----------------------------------------------------------------------
ASSIGNMENT: 3B - The Buffet Calculator
DATE: 1/29/26
FILE: buffet.py
-----------------------------------------------------------------------
REQUIREMENTS:
1. Ask user for their age (convert to int).
2. Use if/elif/else to determine price:
   - Under 1: FREE ($0.00)
   - 1 to 11: $1.00 per year of age (Example: 5 years = $5.00)
   - 12 to 64: $16.95 (Standard Adult)
   - 65 and older: $12.95 (Senior Discount)
3. Print the final price formatted as currency (e.g., $16.95).
-----------------------------------------------------------------------
"""

# asking age 

age = int(input("how old are you?"))

# how much will food cost 

if age < 1:
    print("Your food is 0.00")
elif age < 12:
    print(f"You will pay ${age}.00 our kids rate")
elif age < 65:
    print("Your price is $16.95 our standard rate.")
elif age < 109:
    print("Your price is $12.95 our sinor discount")
else:
    print("You are messing with me there is no way you are that age.")
