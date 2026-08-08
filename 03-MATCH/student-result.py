result = input("Enter Result (P/F): ").upper()

match result:
    case "P":
        print("Congratulations! You Passed.")
    case "F":
        print("Better Luck Next Time.")
    case _:
        print("Invalid Input")
