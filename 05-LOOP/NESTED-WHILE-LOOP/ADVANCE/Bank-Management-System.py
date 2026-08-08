# Create a basic bank management system using nested while loops.

print("======================================")
print("          BANK MANAGEMENT SYSTEM")
print("======================================")

account_pin = 4321
balance = 50000
transactions = 0

# Login system.
while True:
    pin = int(input("\nEnter your account PIN: "))

    if pin == account_pin:
        print("Login successful.")
        break

    else:
        print("Incorrect PIN.")

# Main banking system.
while True:
    print("\n======================================")
    print("              BANK MENU")
    print("======================================")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transfer Money")
    print("5. Change PIN")
    print("6. Account Details")
    print("7. Logout")
    print("======================================")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print(f"\nCurrent Balance: ₹{balance:.2f}")

    elif choice == 2:
        while True:
            amount = float(input("\nEnter deposit amount: ₹"))

            if amount <= 0:
                print("Invalid amount.")
                continue

            balance += amount
            transactions += 1

            print(f"₹{amount:.2f} deposited successfully.")
            print(f"New Balance: ₹{balance:.2f}")
            break

    elif choice == 3:
        while True:
            amount = float(input("\nEnter withdrawal amount: ₹"))

            if amount <= 0:
                print("Invalid amount.")
                continue

            if amount > balance:
                print("Insufficient balance.")
                continue

            balance -= amount
            transactions += 1

            print(f"₹{amount:.2f} withdrawn successfully.")
            print(f"Remaining Balance: ₹{balance:.2f}")
            break

    elif choice == 4:
        while True:
            account = input("\nEnter receiver account number: ")
            amount = float(input("Enter transfer amount: ₹"))

            if amount <= 0:
                print("Invalid amount.")
                continue

            if amount > balance:
                print("Insufficient balance.")
                continue

            balance -= amount
            transactions += 1

            print("\nTransfer successful.")
            print(f"Receiver Account: {account}")
            print(f"Transferred: ₹{amount:.2f}")
            print(f"Remaining Balance: ₹{balance:.2f}")
            break

    elif choice == 5:
        old_pin = int(input("\nEnter current PIN: "))

        if old_pin == account_pin:
            new_pin = int(input("Enter new four-digit PIN: "))

            if new_pin >= 1000 and new_pin <= 9999:
                account_pin = new_pin
                print("PIN changed successfully.")

            else:
                print("Invalid PIN format.")

        else:
            print("Incorrect current PIN.")

    elif choice == 6:
        print("\n========== ACCOUNT DETAILS ==========")
        print("Account Type : Savings Account")
        print("Status       : Active")
        print(f"Balance      : ₹{balance:.2f}")
        print(f"Transactions : {transactions}")
        print("=====================================")

    elif choice == 7:
        print("\nYou have been logged out.")
        print("Thank you for banking with us.")
        break

    else:
        print("Invalid choice.")
