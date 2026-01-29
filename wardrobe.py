"""
    conditionals - if then statements
"""

# get a value
temp = int(input("Whate is the outside temperataure (F)?  "))

# is it cold 
# is it cold???
if temp <= 32:
    print("It is Freezing!!!")

    snow = input("Is it going to snow? (y/n)")
    if snow == "y" or "Y" or "yes" or "Yes":
        print("Wear boots and a parka.")
    else:
        print("Do not forget your coat!")
else:
    print("It is warm engugh for water") # not freezing 
    rain =input("is it going to rain? (y/N)")
    if rain == "y" or "Y":
        print ("4 dollar unbrella")
    else:
        print ("shoes are fine")



#elif 

age = int(input("how old are you?"))
