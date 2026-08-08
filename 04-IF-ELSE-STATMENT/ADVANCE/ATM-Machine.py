# Simple ATM machine using if-elif-else statements.

# Set the account PIN and initial balance.
correct_pin = 1234
balance = 10000

# Take the PIN from the user.
pin = int(input("Enter your PIN: "))

# Verify the PIN.
if pin == correct_pin:
    print("\n========== ATM MENU ==========")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    # Perform an action based on the selected option.
    if choice == 1:
        print(f"\nAvailable Balance: ₹{balance:.2f}")

    elif choice == 2:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid amount.")

        elif amount > balance:
            print("Insufficient balance.")

        else:
            balance -= amount
            print("Withdrawal successful.")
            print(f"Remaining Balance: ₹{balance:.2f}")

    elif choice == 3:
        amount = float(input("Enter deposit amount: "))

        if amount <= 0:
            print("Invalid amount.")

        else:
            balance += amount
            print("Deposit successful.")
            print(f"Updated Balance: ₹{balance:.2f}")

    elif choice == 4:
        print("Thank you for using our ATM.")

    else:
        print("Invalid choice.")

else:
    print("Incorrect PIN. Access denied.")
