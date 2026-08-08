# Display a simple banking menu using the match-case statement.

choice = int(
    input(
        "1. Balance\n" "2. Withdraw\n" "3. Deposit\n" "4. Exit\n" "Enter your choice: "
    )
)

# Execute an action based on the user's choice.
match choice:
    case 1:
        print("Balance = ₹10,000")

    case 2:
        print("Withdraw Selected")

    case 3:
        print("Deposit Selected")

    case 4:
        print("Thank you!")

    case _:
        print("Invalid choice.")
