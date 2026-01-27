"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Ask user for Monthly Income (float).
[ ] 3. Ask user for 5 DIFFERENT expense amounts (float).
[ ] 4. Calculate Total Expenses and Remaining Balance.
[ ] 5. Calculate Percentage of Income Spent.
[ ] 6. Output formatted to 2 decimal places (:,.2f).
-----------------------------------------------------------------------
"""


# covert input 

income = float(input("How much do you make?  "))
car = float(input("Amount spent on your car?"))
events = float(input("Amount spent on events"))
snacks = float(input("Amount spent on snacks"))
books = float(input("Amount spent on books"))
subs = float(input("Amount spent on subscriptions"))



# Equations  

spent = snacks + car + events + books + subs
total_expence = income - snacks - car - events - books - subs
percent = spent/income

# Display

print(f"You earn {income: ,.2f}")
print(f"You spend {spent: ,.2f} a month.")
print(f"You have {total_expence: ,.2f} left")
print(f"You spent %{percent:.2f} of your income.")