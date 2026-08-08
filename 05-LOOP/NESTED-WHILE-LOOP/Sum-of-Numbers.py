# Calculate the sum of numbers entered by the user.
# Enter -1 to stop the program.

# Initialize the total sum.
total = 0

# Keep accepting numbers until the user chooses to exit.
while True:
    num = int(input("\nTo exit, enter -1.\n\nEnter a number to add: "))

    # Stop the program when -1 is entered.
    if num == -1:
        print("\n<---------------------------------------->")
        print("\t<--- PROGRAM ENDED --->")
        print("<---------------------------------------->\n")
        break

    # Add the number to the total if it is non-negative.
    if num >= 0:
        total += num

        # Display the current sum.
        print("\n<------------- Result ------------->")
        print(f"\tResult is = {total}")
        print("<----------------------------------->\n")

    else:
        print("\nInvalid input. Please enter a non-negative number or -1 to exit.")
