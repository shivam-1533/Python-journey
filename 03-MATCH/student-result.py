# Display a message based on the student's result.

# Take the result as input and convert it to uppercase.
result = input("Enter result (P/F): ").upper()

# Display the appropriate message based on the result.
match result:
    case "P":
        print("Congratulations! You passed.")

    case "F":
        print("Better luck next time.")

    case _:
        print("Invalid input.")
