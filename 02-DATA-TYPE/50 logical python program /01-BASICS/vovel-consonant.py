# Check whether an alphabet is a vowel or a consonant.

# Take a single alphabet as input from the user.
letter = input("Enter an alphabet: ").lower()

# Define the vowels.
vowels = "aeiou"

# Check whether the entered letter is a vowel or consonant.
if letter in vowels:
    print(f"{letter} is a vowel.")
else:
    print(f"{letter} is a consonant.")
