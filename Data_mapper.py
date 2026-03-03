"""
-----------------------------------------------------------------------
ASSIGNMENT 8A: OPTION A - NATO TRANSLATOR
-----------------------------------------------------------------------
[] 1. Header Docstring included.
[] 2. NATO_ALPHABET constant is a dictionary (Full A-Z).
[] 3. Program takes a word and uppercases it.
[] 4. Program loops through letters and prints NATO words.
[] 5. A 'try/except' block handles punctuation or numbers.
-----------------------------------------------------------------------
Name: Calvin
-----------------------------------------------------------------------
"""

#dictinary prompt i added the extra stuff 
#Create a Python dictionary constant named NATO_ALPHABET that maps every uppercase letter A–Z to its correct NATO phonetic alphabet word.Only output the dictionary code

# create dictionary
NATO_ALPHABET = {
    "A": "Alpha",   "B": "Bravo",   "C": "Charlie",
    "D": "Delta",   "E": "Echo",    "F": "Foxtrot",
    "G": "Golf",    "H": "Hotel",   "I": "India",
    "J": "Juliett", "K": "Kilo",    "L": "Lima",
    "M": "Mike",    "N": "November","O": "Oscar",
    "P": "Papa",    "Q": "Quebec",  "R": "Romeo",
    "S": "Sierra",  "T": "Tango",   "U": "Uniform",
    "V": "Victor",  "W": "Whiskey", "X": "X-ray",
    "Y": "Yankee",  "Z": "Zulu", " ": " ", ",": ",", ".": "."
}

word = input("Enter word to spell: ").upper().strip()

print("NATO Translation:")

for letter in word:
    try:
        print(NATO_ALPHABET[letter])
    except KeyError:
        print(f"[Unsupported character: {letter}]")