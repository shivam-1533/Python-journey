choice = int(input("1.Balance\n2.Withdraw\n3.Deposit\n4.Exit\nEnter choice: "))

match choice:
    case 1:
        print("Balance = ₹10000")
    case 2:
        print("Withdraw Selected")
    case 3:
        print("Deposit Selected")
    case 4:
        print("Thank You")
    case _:
        print("Invalid Choice")
