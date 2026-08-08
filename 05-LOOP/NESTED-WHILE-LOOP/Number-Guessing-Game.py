# Create a number guessing game.

# Set the secret number.
secret_number = 9

# Keep asking the user to guess until the correct number is entered.
while True:
    guess = int(input("Enter a number: "))

    # Check whether the guessed number is correct.
    if guess == secret_number:
        print("\n==== You Won! ====\n")
        break

    else:
        print("\n==== Try Again! ====\n")
