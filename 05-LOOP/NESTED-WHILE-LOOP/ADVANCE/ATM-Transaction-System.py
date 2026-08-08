# Create an ATM transaction system using nested while loops.

# Set the account details.
correct_pin = 1234
balance = 25000
attempts = 3

# Verify the user's PIN.
while attempts > 0:
    pin = int(input("\nEnter your PIN: "))

    if pin == correct_pin:
        print("\nLogin successful.")
        break

    attempts -= 1

    if attempts > 0:
        print(f"Incorrect PIN. Attempts remaining: {attempts}")
    else:
        print("Account locked.")
        break


# Open the ATM menu after successful login.
if attempts >= 0 and pin == correct_pin:
    while True:
        print("\n================================")
        print("          ATM MENU")
        print("================================")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Change PIN")
        print("5. Mini Statement")
        print("6. Exit")
        print("================================")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print(f"\nAvailable Balance: ₹{balance:.2f}")

        elif choice == 2:
            while True:
                amount = float(input("\nEnter withdrawal amount: "))

                if amount <= 0:
                    print("Invalid amount.")
                    continue

                if amount > balance:
                    print("Insufficient balance.")
                    continue

                if amount % 100 != 0:
                    print("Please enter an amount in multiples of ₹100.")
                    continue

                balance -= amount

                print("\nWithdrawal successful.")
                print(f"Withdrawn Amount: ₹{amount:.2f}")
                print(f"Remaining Balance: ₹{balance:.2f}")
                break

        elif choice == 3:
            while True:
                amount = float(input("\nEnter deposit amount: "))

                if amount <= 0:
                    print("Invalid amount.")
                    continue

                balance += amount

                print("\nDeposit successful.")
                print(f"Deposited Amount: ₹{amount:.2f}")
                print(f"Updated Balance: ₹{balance:.2f}")
                break

        elif choice == 4:
            old_pin = int(input("\nEnter current PIN: "))

            if old_pin == correct_pin:
                new_pin = int(input("Enter new PIN: "))

                if new_pin >= 1000 and new_pin <= 9999:
                    correct_pin = new_pin
                    print("PIN changed successfully.")
                else:
                    print("PIN must contain exactly 4 digits.")

            else:
                print("Incorrect current PIN.")

        elif choice == 5:
            print("\n========== MINI STATEMENT ==========")
            print("Account Type : Savings")
            print(f"Current Balance: ₹{balance:.2f}")
            print("Last Transaction: Available in account")
            print("====================================")

        elif choice == 6:
            print("\nThank you for using our ATM.")
            print("Please collect your card.")
            break

        else:
            print("Invalid choice. Please try again.")
