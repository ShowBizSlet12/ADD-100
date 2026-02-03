"""
-----------------------------------------------------------------------
ASSIGNMENT: Boolean Logic
Calvin Hamill
Purpose: Practice using AND, OR, NOT, and ELIF statements.
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with your name.
[ ] 2. Ask user for two integers (num1 and num2).
[ ] 3. Perform 6 logical checks: 
Both > 0, 
Both > 100, 
Either Even, 
Either < 100, 
Not Equal, 
Not Zero.
[ ] 4. Use if/elif/else to categorize num1 (Positive/Negative/Zero).
[ ] 5. Code is clean and uses descriptive variable names.
[ ] 6. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""


# Asking for numbers 

num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter another number: "))


# 1. Testing if both numbers greater than 0 
if num1 > 0 and num2 > 0:
    print("Both numbers are greater than 0.")
else:
    print("Both numbers are NOT greater than 0.")


# 2. Testing if both numbers greater than 100 
if num1 > 100 and num2 > 100:
    print("Both numbers are greater than 100.")
else:
    print("Both numbers are NOT greater than 100.")


# 3. Testing if either number is even 
if num1 % 2 == 0 or num2 % 2 == 0:
    print("At least one number is even.")
else:
    print("Neither number is even.")


# 4. Testing if either number less than 100 
if num1 < 100 or num2 < 100:
    print("At least one number is less than 100.")
else:
    print("Neither number is less than 100.")


# 5. Seeing if numbers are not equal 
if not (num1 == num2):
    print("The numbers are not equal.")
else:
    print("The numbers are equal.")


# 6. Seeing if neither number is zero 
if not (num1 == 0 or num2 == 0):
    print("Neither number is zero.")
else:
    print("One or both numbers are zero.")


print("Categorizing the first number")


# ELIF BRANCHING TO CATEGORIZE NUM1
if num1 > 0:
    print("The first number is Positive.")
elif num1 < 0:
    print("The first number is Negative.")
else:
    print("The first number is Zero.")