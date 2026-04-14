"""
-----------------------------------------------------------------------
ASSIGNMENT 14A: THE HERO BLUEPRINT
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Define a class named 'Hero'.
[ ] 3. Use __init__ to give the hero a name and a power.
[ ] 4. Add a method 'intro' that prints "I am [name] and I use [power]!".
[ ] 5. Instantiate two hero objects and call their 'intro' method.
-----------------------------------------------------------------------
"""

class Hero:
    def __init__(self, name, power, team, rating):
        self.name = name
        self.power = power
        self.team = team
        self.rating = rating

    def intro(self):
        print(f"I am {self.name}, I work with {self.team}, and I use {self.power}!")

    def show_rating(self):
        print(f"{self.name}'s hero rating is {self.rating}/10.")


# Creating hero objects (The Boys theme)
hero1 = Hero("Homelander", "laser eyes", "The Seven", 10)
hero2 = Hero("The Deep", "talking to fish", "The Seven", 4)
hero3 = Hero("Starlight", "light blasts", "The Seven", 7)
hero4 = Hero("Black Noir", "stealth combat", "The Seven", 9)
hero5 = Hero("Billy Butcher", "supe-destruction rage", "The Boys", 8)

# Calling methods
heroes = [hero1, hero2, hero3, hero4, hero5]

for hero in heroes:
    hero.intro()
    hero.show_rating()
    print("-----")