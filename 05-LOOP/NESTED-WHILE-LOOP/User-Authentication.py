# Create a password verification system.

# Set the correct password.
correct_password = "shivam1234"

# Keep asking for the password until it is correct.
while True:
    password = input("Enter your password (a-z + 0-9): ")

    # Check whether the entered password is correct.
    if password == correct_password:
        print("\n<------ Login Successful ------->\n")
        break

    else:
        print("\n<------ Try Again ------->\n")
