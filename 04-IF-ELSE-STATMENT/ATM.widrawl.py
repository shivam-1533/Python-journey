# Process a bank withdrawal and display the remaining balance.

# Set the initial account balance.
balance = 10000

# Take the withdrawal amount as input.
amount = float(input("Enter withdrawal amount: "))

# Validate the withdrawal amount and account balance.
if amount <= 0:
    print("Invalid amount.")

elif amount > balance:
    print("Insufficient balance.")

else:
    # Deduct the withdrawal amount from the account balance.
    balance -= amount

    # Display the transaction result and remaining balance.
    print("Withdrawal successful.")
    print(f"Remaining balance = ₹{balance:.2f}")
