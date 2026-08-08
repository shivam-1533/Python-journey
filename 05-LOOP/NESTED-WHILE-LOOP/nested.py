# Calculate the product of numbers entered by the user.
# Enter -1 to stop the program.

# Initialize the product.
total = 1

# Continuously take numbers until the user chooses to exit.
while True:
    num = int(input("\nTo exit, enter -1.\nEnter a number to multiply: "))

    # Stop the program when -1 or any negative number is entered.
    if num < 0:
        print("\n<---------------------------------------->")
        print("\t<--- PROGRAM ENDED --->")
        print("<---------------------------------------->\n")
        break

    # Multiply the entered number with the current result.
    total *= num

    # Display the current result.
    print("\n<------------- Result ------------->")
    print(f"\tResult is = {total}")
    print("<----------------------------------->\n")
