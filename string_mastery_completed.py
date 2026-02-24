"""
-----------------------------------------------------------------------
ASSIGNMENT 7A: STRING MASTERY LAB
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with your name.
[ ] 2. Task 1: String Basics (Length, Indexing, ASCII) completed.
[ ] 3. Task 2: The Cleanup Crew (Strip, Case, Replace) completed.
[ ] 4. Task 3: Validation (isdigit check) completed.
[ ] 5. Task 4: The Duck Loop (.join and direct iteration) completed.
-----------------------------------------------------------------------
Name: Calvin
-----------------------------------------------------------------------
"""

# --- TASK 1: TUNING THE GUITAR 🎸 ---
instrument = "Acoustic Guitar"

# Length
print("Length:", len(instrument))

# First and last letter
print("First letter:", instrument[0])
print("Last letter:", instrument[-1])

# ASCII lowest and highest
print("Lowest ASCII:", min(instrument))
print("Highest ASCII:", max(instrument))


# --- TASK 2: THE CLEANUP CREW 🧵 ---
messy_input = "   vOLUME_knob_11   "

cleaned = messy_input.strip()      
cleaned = cleaned.upper()          
cleaned = cleaned.replace("_", " ")  

print("Cleaned Input:", cleaned)


# --- TASK 3: THE VALIDATOR 🔍 ---
serial_number = "90210"

if serial_number.isdigit():
    print("Valid Serial")
else:
    print("Invalid Serial")


# --- TASK 4: THE DUCK BRIDGE 🦆🎵 ---
name_string = "DUCKY"
duck_letters = list(name_string)
count = 0

print("--- Singing the Duck Song! ---")

for char in name_string:
    current_name = " ".join(duck_letters)

    print("There was a teacher who had a duck and Ducky was his Name-o")
    print((f"({current_name}) ") * 3)
    print("and Ducky was his Name-o!")

    duck_letters[count] = "🦆"
    count += 1

# Finale
final_name = " ".join(duck_letters)
print((f"({final_name}) ") * 3)
print("and Ducky was his Name-o!")