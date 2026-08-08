balance = 10000
amount = float(input("Enter withdrawal amount: "))

if amount <= 0:
    print("Invalid Amount")
elif amount > balance:
    print("Insufficient Balance")
else:
    balance = balance - amount
    print("Withdrawal Successful")
    print("Remaining Balance =", balance)

