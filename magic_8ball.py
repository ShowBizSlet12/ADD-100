"""
-----------------------------------------------------------------------
ASSIGNMENT 7B: THE MAGIC 8 BALL
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. RESPONSES is a tuple containing at least 8 string options.
[ ] 3. Program uses a 'while True' loop to keep the game running.
[ ] 4. random.choice() selects the answer from the tuple.
[ ] 5. Logic checks if "quit" is in the user input to break the loop.
-----------------------------------------------------------------------
Name: Calvin
-----------------------------------------------------------------------
"""

import random

RESPONSES = (
    "Yes, definitely.",
    "No way.",
    "Maybe someday.",
    "Ask again later.",
    "Outlook good.",
    "Very doubtful.",
    "Signs point to yes.",
    "I wouldn't count on it.",
    "You're cooked.",
    "Quit now",
    "It's over"
)

print("Welcome to the Digital 8 ball!")
print("Type your question… (type 'quit' to exit)\n")

while True:
    question = input("Your question: ")

    clean_question = question.strip().lower()

    # empty question check
    if clean_question == "":
        print("🎱 Ask a real question!\n")
        continue

    # Exit
    if "quit" in clean_question:
        print("The 8 Ball rests… Goodbye!")
        break

    answer = random.choice(RESPONSES)
    print("🎱:", answer, "\n")