# Create a PIN verification system with limited attempts.

# Set the correct PIN and maximum number of attempts.
pin = 1234
attempts = 3

# Allow the user to enter the PIN up to three times.
while attempts > 0:
    entered_pin = int(input("\nEnter your PIN: "))

    # Check whether the entered PIN is correct.
    if entered_pin == pin:
        print("\nLogin successful.\n")
        break

    # Reduce the remaining attempts after an incorrect PIN.
    attempts -= 1

    # Display the appropriate message based on remaining attempts.
    if attempts > 0:
        print(f"Incorrect PIN. Attempts remaining: {attempts}\n")
    else:
        print("Account locked.\n")
