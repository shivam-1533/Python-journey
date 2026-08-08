# Simulate an ATM withdrawal system with PIN verification.

PIN = "1234"
balance = 10000
attempts = 3

# Verify the user's PIN.
while attempts > 0:
    entered_pin = input("Enter your 4-digit PIN: ")

    if entered_pin == PIN:
        print("\nLogin Successful!\n")
        break

    attempts -= 1
    print(f"Incorrect PIN! Attempts left: {attempts}")

if attempts == 0:
    print("Your account has been locked.")
    exit()

# Display the ATM menu.
while True:
    print("\n====== ATM MENU ======")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print(f"Your Balance: ₹{balance}")

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: ₹"))

        if amount <= 0:
            print("Invalid amount!")

        elif amount > balance:
            print("Insufficient balance!")

        else:
            balance -= amount
            print("Withdrawal Successful!")
            print(f"Remaining Balance: ₹{balance}")

    elif choice == "3":
        amount = float(input("Enter deposit amount: ₹"))

        if amount <= 0:
            print("Invalid amount!")

        else:
            balance += amount
            print("Deposit Successful!")
            print(f"Updated Balance: ₹{balance}")

    elif choice == "4":
        print("Thank you for using our ATM!")
        break

    else:
        print("Invalid choice! Please select 1-4.")
